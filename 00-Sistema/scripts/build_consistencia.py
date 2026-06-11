# -*- coding: utf-8 -*-
"""Construye agregaciones consistencia_por_candidato.

Para cada (candidato, tema) calcula:
  n_propuestas_plan, n_declaraciones_debate, consistentes, amplia_debate,
  vaguea, contradice_debate, omite, nuevo_debate, indice_consistencia.

indice_consistencia = (consistentes + amplia_debate) /
                       (consistentes + amplia_debate + vaguea + contradice_debate)
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

VAULT = Path(__file__).resolve().parent.parent.parent
RUTA_C = VAULT / "00-Sistema" / "datos" / "comparaciones.json"
RUTA_P = VAULT / "00-Sistema" / "datos" / "propuestas.json"
RUTA_D = VAULT / "00-Sistema" / "datos" / "declaraciones.json"


def main():
    cmp_data = json.loads(RUTA_C.read_text(encoding="utf-8"))
    prop_data = json.loads(RUTA_P.read_text(encoding="utf-8"))
    decl_data = json.loads(RUTA_D.read_text(encoding="utf-8"))

    # Conteos plan y debate por (cand, tema)
    n_plan = defaultdict(int)
    for p in prop_data["propuestas"]:
        n_plan[(p["candidato"], p["tema"])] += 1

    n_decl = defaultdict(int)
    for d in decl_data["declaraciones"]:
        n_decl[(d["candidato"], d["tema"])] += 1

    # Lookup: propuesta_id → tema, declaracion_id → tema
    prop_tema = {p["id"]: p["tema"] for p in prop_data["propuestas"]}
    decl_tema = {d["id"]: d["tema"] for d in decl_data["declaraciones"]}

    # Conteos de relaciones por (cand, tema)
    counts = defaultdict(lambda: defaultdict(int))
    REL_MAP = {
        "CONSISTENTE": "consistentes",
        "AMPLIA_DEBATE": "amplia_debate",
        "VAGUEA": "vaguea",
        "CONTRADICE_DEBATE": "contradice_debate",
        "OMITE": "omite",
        "NUEVO_DEBATE": "nuevo_debate",
    }
    for c in cmp_data["plan_vs_debate"]:
        cand = c["candidato"]
        # Determinar tema: si hay propuesta, usar su tema; si solo declaración, usar el de la declaración
        tema = None
        if c.get("propuesta_id"):
            tema = prop_tema.get(c["propuesta_id"])
        elif c.get("declaracion_id"):
            tema = decl_tema.get(c["declaracion_id"])
        if tema is None:
            continue
        counts[(cand, tema)][REL_MAP[c["relacion"]]] += 1

    # Construir agg
    agg = []
    # Universo: todas las combinaciones (cand, tema) que tienen plan o debate o comparación
    universo = set()
    for k in n_plan.keys():
        universo.add(k)
    for k in n_decl.keys():
        universo.add(k)
    for k in counts.keys():
        universo.add(k)

    for cand, tema in sorted(universo):
        c = counts.get((cand, tema), {})
        cons = c.get("consistentes", 0)
        amp = c.get("amplia_debate", 0)
        vag = c.get("vaguea", 0)
        con = c.get("contradice_debate", 0)
        om = c.get("omite", 0)
        new = c.get("nuevo_debate", 0)
        denom = cons + amp + vag + con
        ic = round((cons + amp) / denom, 4) if denom > 0 else None
        agg.append({
            "candidato": cand,
            "tema": tema,
            "n_propuestas_plan": n_plan.get((cand, tema), 0),
            "n_declaraciones_debate": n_decl.get((cand, tema), 0),
            "consistentes": cons,
            "amplia_debate": amp,
            "vaguea": vag,
            "contradice_debate": con,
            "omite": om,
            "nuevo_debate": new,
            "indice_consistencia": ic,
            "notas": None,
        })

    cmp_data["consistencia_por_candidato"] = agg
    RUTA_C.write_text(json.dumps(cmp_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Agregaciones generadas: {len(agg)}")
    print("OK escrito.")


if __name__ == "__main__":
    main()
