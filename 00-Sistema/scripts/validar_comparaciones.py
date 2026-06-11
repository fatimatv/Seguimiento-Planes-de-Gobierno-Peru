#!/usr/bin/env python3
"""Validador de 00-Sistema/datos/comparaciones.json.

Verifica:
  1. Conformidad estructural.
  2. Unicidad de IDs.
  3. Que cada referencia a propuesta_keiko/propuesta_roberto exista en
     propuestas.json con el candidato correcto.
  4. Que cada referencia a declaracion_id exista en declaraciones.json.
  5. Que cada tema referenciado exista en la taxonomía (propuestas.json).
  6. Coherencia: si relacion es SOLO_A entonces propuesta_roberto es null
     y propuesta_keiko no es null; SOLO_B al revés.
  7. Para plan_vs_debate: NUEVO_DEBATE requiere propuesta_id null y
     declaracion_id no null; OMITE requiere propuesta_id no null y
     declaracion_id null.
  8. Coherencia de la agregación consistencia_por_candidato: indice =
     (consistentes + amplia_debate) / (consistentes + amplia_debate +
     vaguea + contradice_debate) cuando el denominador > 0.

Uso: python 00-Sistema/scripts/validar_comparaciones.py
Exit code: 0 OK, 1 falla.
"""
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

VAULT = Path(__file__).resolve().parent.parent.parent
DATOS = VAULT / "00-Sistema" / "datos" / "comparaciones.json"
PROP = VAULT / "00-Sistema" / "datos" / "propuestas.json"
DECL = VAULT / "00-Sistema" / "datos" / "declaraciones.json"

ID_PP = re.compile(r"^cmp-pp-[a-z_]+-[0-9]{3}$")
ID_PD = re.compile(r"^cmp-pd-[kr]-[0-9]{3}$")
DIMENSIONES = {"diagnostico", "propuesta_principal", "meta", "enfoque_institucional", "principio"}
REL_PP = {"COINCIDE", "AMPLIA", "DIVERGE", "CONTRADICE", "SOLO_A", "SOLO_B"}
REL_PD = {"CONSISTENTE", "AMPLIA_DEBATE", "VAGUEA", "CONTRADICE_DEBATE", "OMITE", "NUEVO_DEBATE"}


def main() -> int:
    if not DATOS.exists():
        print(f"[X] No existe {DATOS}")
        return 1

    propuestas_data = json.loads(PROP.read_text(encoding="utf-8"))
    declaraciones_data = json.loads(DECL.read_text(encoding="utf-8"))

    tema_ids = {t["id"] for t in propuestas_data["temas"]}
    propuestas_by_id = {p["id"]: p for p in propuestas_data["propuestas"]}
    decl_by_id = {d["id"]: d for d in declaraciones_data["declaraciones"]}

    data = json.loads(DATOS.read_text(encoding="utf-8"))
    errores: list[str] = []

    # plan_vs_plan
    pp_ids: set[str] = set()
    for i, c in enumerate(data.get("plan_vs_plan", [])):
        if not ID_PP.match(c["id"]):
            errores.append(f"plan_vs_plan #{i}: ID invalido {c['id']!r}")
        if c["id"] in pp_ids:
            errores.append(f"plan_vs_plan: ID duplicado {c['id']!r}")
        pp_ids.add(c["id"])

        if c["tema"] not in tema_ids:
            errores.append(f"{c['id']}: tema {c['tema']!r} no esta en taxonomia")
        if c["dimension"] not in DIMENSIONES:
            errores.append(f"{c['id']}: dimension invalida {c['dimension']!r}")
        if c["relacion"] not in REL_PP:
            errores.append(f"{c['id']}: relacion invalida {c['relacion']!r}")

        pk = c.get("propuesta_keiko")
        pr = c.get("propuesta_roberto")
        if pk is not None:
            if pk not in propuestas_by_id:
                errores.append(f"{c['id']}: propuesta_keiko {pk!r} no existe")
            elif propuestas_by_id[pk]["candidato"] != "keiko":
                errores.append(f"{c['id']}: propuesta_keiko {pk!r} no es de keiko")
        if pr is not None:
            if pr not in propuestas_by_id:
                errores.append(f"{c['id']}: propuesta_roberto {pr!r} no existe")
            elif propuestas_by_id[pr]["candidato"] != "roberto":
                errores.append(f"{c['id']}: propuesta_roberto {pr!r} no es de roberto")

        # Coherencia SOLO_A / SOLO_B
        if c["relacion"] == "SOLO_A":
            if pk is None or pr is not None:
                errores.append(f"{c['id']}: SOLO_A requiere propuesta_keiko no-null y propuesta_roberto null")
        if c["relacion"] == "SOLO_B":
            if pr is None or pk is not None:
                errores.append(f"{c['id']}: SOLO_B requiere propuesta_roberto no-null y propuesta_keiko null")
        if c["relacion"] in {"COINCIDE", "AMPLIA", "DIVERGE", "CONTRADICE"}:
            if pk is None or pr is None:
                errores.append(f"{c['id']}: {c['relacion']} requiere ambas propuestas no-null")

    # plan_vs_debate
    pd_ids: set[str] = set()
    for i, c in enumerate(data.get("plan_vs_debate", [])):
        if not ID_PD.match(c["id"]):
            errores.append(f"plan_vs_debate #{i}: ID invalido {c['id']!r}")
        if c["id"] in pd_ids:
            errores.append(f"plan_vs_debate: ID duplicado {c['id']!r}")
        pd_ids.add(c["id"])

        if c["relacion"] not in REL_PD:
            errores.append(f"{c['id']}: relacion invalida {c['relacion']!r}")

        prop_id = c.get("propuesta_id")
        decl_id = c.get("declaracion_id")
        if prop_id is not None:
            if prop_id not in propuestas_by_id:
                errores.append(f"{c['id']}: propuesta_id {prop_id!r} no existe")
            elif propuestas_by_id[prop_id]["candidato"] != c["candidato"]:
                errores.append(f"{c['id']}: propuesta_id no coincide con candidato {c['candidato']!r}")
        if decl_id is not None:
            if decl_id not in decl_by_id:
                errores.append(f"{c['id']}: declaracion_id {decl_id!r} no existe")
            elif decl_by_id[decl_id]["candidato"] != c["candidato"]:
                errores.append(f"{c['id']}: declaracion_id no coincide con candidato {c['candidato']!r}")

        if c["relacion"] == "OMITE":
            if prop_id is None or decl_id is not None:
                errores.append(f"{c['id']}: OMITE requiere propuesta_id no-null y declaracion_id null")
        elif c["relacion"] == "NUEVO_DEBATE":
            if prop_id is not None or decl_id is None:
                errores.append(f"{c['id']}: NUEVO_DEBATE requiere propuesta_id null y declaracion_id no-null")
        else:
            # CONSISTENTE / AMPLIA_DEBATE / VAGUEA / CONTRADICE_DEBATE
            if prop_id is None or decl_id is None:
                errores.append(f"{c['id']}: {c['relacion']} requiere ambos IDs no-null")

    # consistencia_por_candidato
    for i, a in enumerate(data.get("consistencia_por_candidato", [])):
        if a["tema"] not in tema_ids:
            errores.append(f"consistencia #{i}: tema {a['tema']!r} no esta en taxonomia")
        denom = a["consistentes"] + a["amplia_debate"] + a["vaguea"] + a["contradice_debate"]
        if denom > 0:
            ic = (a["consistentes"] + a["amplia_debate"]) / denom
            ic_decl = a.get("indice_consistencia")
            if ic_decl is None:
                errores.append(f"consistencia {a['candidato']}/{a['tema']}: falta indice_consistencia")
            elif abs(ic - ic_decl) > 1e-6:
                errores.append(f"consistencia {a['candidato']}/{a['tema']}: indice {ic_decl} no coincide con calculado {ic:.4f}")

    if errores:
        for e in errores:
            print("[X]", e)
        print(f"\n{len(errores)} error(es).")
        return 1

    n_pp = len(data.get("plan_vs_plan", []))
    n_pd = len(data.get("plan_vs_debate", []))
    n_ag = len(data.get("consistencia_por_candidato", []))
    print(f"[OK] Validacion OK - plan_vs_plan: {n_pp}, plan_vs_debate: {n_pd}, consistencia: {n_ag}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
