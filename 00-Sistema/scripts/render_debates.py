# -*- coding: utf-8 -*-
"""Renderiza los .md por candidato/debate desde declaraciones.json.

Genera:
    02-Debates/procesados/debate-1/keiko.md
    02-Debates/procesados/debate-1/roberto.md
    02-Debates/procesados/debate-2/keiko.md
    02-Debates/procesados/debate-2/roberto.md
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
DATOS = VAULT / "00-Sistema" / "datos" / "declaraciones.json"
PROP = VAULT / "00-Sistema" / "datos" / "propuestas.json"
PROCESADOS = VAULT / "02-Debates" / "procesados"


NOMBRE_CANDIDATO = {"keiko": "Keiko Fujimori", "roberto": "Roberto Sánchez"}


def render(debate, candidato_id, declaraciones, tema_label):
    nombre = NOMBRE_CANDIDATO[candidato_id]
    sub = [d for d in declaraciones if d["debate_id"] == debate["id"] and d["candidato"] == candidato_id]
    if not sub:
        return f"# {nombre} — {debate['id']}\n\n(Sin declaraciones registradas.)\n"

    lines = []
    lines.append(f"# {nombre} — {debate['id']}")
    lines.append("")
    lines.append(f"**Fuente:** `{debate['archivo_fuente']}`")
    lines.append(f"**Formato:** {debate['formato']}")
    lines.append(f"**Fecha:** {debate['fecha']}")
    lines.append(f"**Organizador:** {debate['organizador']}")
    lines.append(f"**Declaraciones:** {len(sub)}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Agrupar por contexto (bloque)
    por_ctx = defaultdict(list)
    for d in sub:
        ctx = d.get("contexto") or "(Sin contexto)"
        por_ctx[ctx].append(d)

    # Preservar orden por linea_inicio del primer elemento
    ctx_order = sorted(por_ctx.keys(), key=lambda c: min(x["fuente"]["linea_inicio"] for x in por_ctx[c]))

    for ctx in ctx_order:
        lines.append(f"## {ctx}")
        lines.append("")
        items = sorted(por_ctx[ctx], key=lambda x: x["fuente"]["linea_inicio"])
        for d in items:
            tema_nombre = tema_label.get(d["tema"], d["tema"])
            cabeza = f"### `{d['id']}` — {tema_nombre} ({d['tipo']})"
            lines.append(cabeza)
            lines.append("")
            if d.get("vocero"):
                lines.append(f"**Vocero:** {d['vocero']}")
            if d.get("timestamp"):
                lines.append(f"**Timestamp:** `[{d['timestamp']}]`")
            f = d["fuente"]
            lines.append(f"**Líneas:** {f['archivo']}:L{f['linea_inicio']}-{f['linea_fin']}")
            lines.append("")
            lines.append(f"**Texto:** {d['texto']}")
            lines.append("")
            lines.append(f"> {d['cita_textual']}")
            lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main():
    data = json.loads(DATOS.read_text(encoding="utf-8"))
    propuestas_data = json.loads(PROP.read_text(encoding="utf-8"))
    tema_label = {t["id"]: t["nombre"] for t in propuestas_data["temas"]}

    PROCESADOS.mkdir(parents=True, exist_ok=True)

    for debate in data["debates"]:
        debate_dir = PROCESADOS / debate["id"]
        debate_dir.mkdir(parents=True, exist_ok=True)
        for cand_id in ("keiko", "roberto"):
            content = render(debate, cand_id, data["declaraciones"], tema_label)
            path = debate_dir / f"{cand_id}.md"
            path.write_text(content, encoding="utf-8")
            print(f"Escrito: {path.relative_to(VAULT)}")

    print("OK.")


if __name__ == "__main__":
    main()
