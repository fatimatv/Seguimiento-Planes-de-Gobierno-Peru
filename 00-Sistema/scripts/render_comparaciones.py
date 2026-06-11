# -*- coding: utf-8 -*-
"""Renderiza los 5 reportes .md a partir de propuestas.json, declaraciones.json
y comparaciones.json.

Outputs en 03-Comparaciones/:
  - matriz-temas.md
  - coincidencias.md
  - divergencias.md
  - contradicciones.md
  - consistencia-discurso.md
"""
import json
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

VAULT = Path(__file__).resolve().parent.parent.parent
DATOS = VAULT / "00-Sistema" / "datos"
OUT = VAULT / "03-Comparaciones"
OUT.mkdir(parents=True, exist_ok=True)

prop_data = json.loads((DATOS / "propuestas.json").read_text(encoding="utf-8"))
decl_data = json.loads((DATOS / "declaraciones.json").read_text(encoding="utf-8"))
cmp_data = json.loads((DATOS / "comparaciones.json").read_text(encoding="utf-8"))

TEMA_INFO = {t["id"]: t for t in prop_data["temas"]}
PROP_BY_ID = {p["id"]: p for p in prop_data["propuestas"]}
DECL_BY_ID = {d["id"]: d for d in decl_data["declaraciones"]}

NOMBRE = {"keiko": "Keiko Fujimori", "roberto": "Roberto Sánchez Palomino"}
COLOR = {"keiko": "rojo", "roberto": "azul"}

HOY = "2026-06-10"


def header(titulo: str, descripcion: str) -> str:
    return (
        f"# {titulo}\n\n"
        f"> {descripcion}\n\n"
        f"**Generado:** {HOY}  \n"
        f"**Fuente:** `00-Sistema/datos/propuestas.json`, "
        f"`00-Sistema/datos/declaraciones.json`, "
        f"`00-Sistema/datos/comparaciones.json`  \n"
        f"**Generador:** `00-Sistema/scripts/render_comparaciones.py`\n\n"
        f"---\n\n"
    )


def cita_propuesta(prop_id: str) -> str:
    if prop_id is None:
        return "(no aplica)"
    p = PROP_BY_ID.get(prop_id)
    if not p:
        return f"`{prop_id}` (no encontrada)"
    return f"**[{prop_id}]** {p['texto']}"


def cita_declaracion(decl_id: str) -> str:
    if decl_id is None:
        return "(no aplica)"
    d = DECL_BY_ID.get(decl_id)
    if not d:
        return f"`{decl_id}` (no encontrada)"
    extra = ""
    if d.get("vocero"):
        extra += f" — *Vocero: {d['vocero']}*"
    if d.get("timestamp"):
        extra += f" — `[{d['timestamp']}]`"
    return f"**[{decl_id}]** {d['texto']}{extra}\n\n  > {d['cita_textual']}"


# =====================================================================
# 1. matriz-temas.md
# =====================================================================
def render_matriz_temas():
    out = [header(
        "Matriz Comparativa por Tema",
        "Tabla maestra con todos los temas, número de propuestas por candidato "
        "en el plan, número de declaraciones en debates, y las relaciones "
        "plan-vs-plan detectadas."
    )]

    pp_by_tema = defaultdict(list)
    for c in cmp_data["plan_vs_plan"]:
        pp_by_tema[c["tema"]].append(c)

    out.append("| Tema | Icono | Plan Keiko | Plan Roberto | Debate Keiko | Debate Roberto | Relaciones plan-vs-plan |\n")
    out.append("|---|---|---:|---:|---:|---:|---|\n")

    n_plan = defaultdict(lambda: defaultdict(int))
    for p in prop_data["propuestas"]:
        n_plan[p["tema"]][p["candidato"]] += 1
    n_decl = defaultdict(lambda: defaultdict(int))
    for d in decl_data["declaraciones"]:
        n_decl[d["tema"]][d["candidato"]] += 1

    for tema in prop_data["temas"]:
        tid = tema["id"]
        rels = pp_by_tema.get(tid, [])
        rels_str = ", ".join(f"{r['relacion']} ({r['dimension']})" for r in rels) if rels else "—"
        out.append(
            f"| {tema['nombre']} | {tema.get('icono','')} | "
            f"{n_plan[tid]['keiko']} | {n_plan[tid]['roberto']} | "
            f"{n_decl[tid]['keiko']} | {n_decl[tid]['roberto']} | "
            f"{rels_str} |\n"
        )

    out.append("\n---\n\n")
    out.append("## Leyenda de relaciones\n\n")
    out.append("- **COINCIDE**: ambos proponen lo mismo o soluciones equivalentes.\n")
    out.append("- **AMPLÍA**: un candidato va más lejos que el otro en la misma dirección.\n")
    out.append("- **DIVERGE**: mismo objetivo, soluciones distintas no necesariamente incompatibles.\n")
    out.append("- **CONTRADICE**: posiciones mutuamente excluyentes.\n")
    out.append("- **SOLO_A / SOLO_B**: el tema solo aparece en el plan de uno (B = Roberto).\n")

    (OUT / "matriz-temas.md").write_text("".join(out), encoding="utf-8")
    print("Escrito: 03-Comparaciones/matriz-temas.md")


# =====================================================================
# 2. coincidencias.md
# =====================================================================
def render_coincidencias():
    out = [header(
        "Coincidencias entre los Planes",
        "Áreas en las que Keiko Fujimori y Roberto Sánchez Palomino convergen, "
        "ya sea en el diagnóstico del problema o en la dirección de la solución."
    )]

    coincidencias = [c for c in cmp_data["plan_vs_plan"] if c["relacion"] in ("COINCIDE", "AMPLIA")]
    coincidencias.sort(key=lambda c: (c["tema"], c["dimension"]))

    if not coincidencias:
        out.append("_No se detectaron coincidencias significativas._\n")
    else:
        out.append(f"**{len(coincidencias)} coincidencias detectadas** en {len(set(c['tema'] for c in coincidencias))} temas.\n\n")

        by_tema = defaultdict(list)
        for c in coincidencias:
            by_tema[c["tema"]].append(c)

        for tema_id in sorted(by_tema):
            tema = TEMA_INFO[tema_id]
            out.append(f"## {tema.get('icono','')} {tema['nombre']}\n\n")
            for c in by_tema[tema_id]:
                out.append(f"### {c['dimension'].replace('_',' ').title()} — `{c['relacion']}`\n\n")
                out.append(f"- **Keiko:** {cita_propuesta(c['propuesta_keiko'])}\n")
                out.append(f"- **Roberto:** {cita_propuesta(c['propuesta_roberto'])}\n\n")
                out.append(f"**Análisis:** {c['analisis']}\n\n")
            out.append("---\n\n")

    (OUT / "coincidencias.md").write_text("".join(out), encoding="utf-8")
    print("Escrito: 03-Comparaciones/coincidencias.md")


# =====================================================================
# 3. divergencias.md
# =====================================================================
def render_divergencias():
    out = [header(
        "Divergencias entre los Planes",
        "Áreas en las que Keiko Fujimori y Roberto Sánchez Palomino comparten "
        "el objetivo o el problema pero proponen soluciones distintas (sin "
        "ser mutuamente excluyentes)."
    )]

    divergencias = [c for c in cmp_data["plan_vs_plan"] if c["relacion"] == "DIVERGE"]
    divergencias.sort(key=lambda c: (c["tema"], c["dimension"]))

    out.append(f"**{len(divergencias)} divergencias detectadas** en {len(set(c['tema'] for c in divergencias))} temas.\n\n")

    by_tema = defaultdict(list)
    for c in divergencias:
        by_tema[c["tema"]].append(c)

    for tema_id in sorted(by_tema):
        tema = TEMA_INFO[tema_id]
        out.append(f"## {tema.get('icono','')} {tema['nombre']}\n\n")
        for c in by_tema[tema_id]:
            out.append(f"### {c['dimension'].replace('_',' ').title()}\n\n")
            out.append(f"- **Keiko:** {cita_propuesta(c['propuesta_keiko'])}\n")
            out.append(f"- **Roberto:** {cita_propuesta(c['propuesta_roberto'])}\n\n")
            out.append(f"**Análisis:** {c['analisis']}\n\n")
        out.append("---\n\n")

    (OUT / "divergencias.md").write_text("".join(out), encoding="utf-8")
    print("Escrito: 03-Comparaciones/divergencias.md")


# =====================================================================
# 4. contradicciones.md
# =====================================================================
def render_contradicciones():
    out = [header(
        "Contradicciones detectadas",
        "Contradicciones plan-vs-plan (posiciones mutuamente excluyentes entre "
        "Keiko y Roberto) y contradicciones plan-vs-debate por candidato "
        "(cuando un candidato dijo en debate algo incompatible con su plan)."
    )]

    # Plan vs Plan
    contradicciones_pp = [c for c in cmp_data["plan_vs_plan"] if c["relacion"] == "CONTRADICE"]
    contradicciones_pp.sort(key=lambda c: c["tema"])

    out.append("## A) Contradicciones plan-vs-plan (Keiko ↔ Roberto)\n\n")
    if not contradicciones_pp:
        out.append("_No se detectaron contradicciones directas entre los planes._\n\n")
    else:
        out.append(f"**{len(contradicciones_pp)} contradicciones estructurales** entre los dos planes.\n\n")
        for c in contradicciones_pp:
            tema = TEMA_INFO[c["tema"]]
            out.append(f"### {tema.get('icono','')} {tema['nombre']} — {c['dimension'].replace('_',' ').title()}\n\n")
            out.append(f"- **Keiko:** {cita_propuesta(c['propuesta_keiko'])}\n")
            out.append(f"- **Roberto:** {cita_propuesta(c['propuesta_roberto'])}\n\n")
            out.append(f"**Análisis:** {c['analisis']}\n\n")
            out.append("---\n\n")

    # Plan vs Debate por candidato
    out.append("## B) Contradicciones plan-vs-debate por candidato\n\n")
    contradicciones_pd = [c for c in cmp_data["plan_vs_debate"] if c["relacion"] == "CONTRADICE_DEBATE"]

    if not contradicciones_pd:
        out.append(
            "_No se detectaron contradicciones directas entre los planes escritos y "
            "lo declarado en debates. Ambos candidatos sostuvieron en debate sus "
            "propuestas centrales del plan; vale revisión humana adicional para "
            "identificar matices de VAGUEA o contradicción sutil._\n\n"
        )
    else:
        for cand in ("keiko", "roberto"):
            subs = [c for c in contradicciones_pd if c["candidato"] == cand]
            if not subs:
                continue
            out.append(f"### {NOMBRE[cand]}\n\n")
            for c in subs:
                out.append(f"- **Plan:** {cita_propuesta(c['propuesta_id'])}\n")
                out.append(f"- **Debate:** {cita_declaracion(c['declaracion_id'])}\n")
                out.append(f"- **Análisis:** {c['analisis']}\n\n")

    (OUT / "contradicciones.md").write_text("".join(out), encoding="utf-8")
    print("Escrito: 03-Comparaciones/contradicciones.md")


# =====================================================================
# 5. consistencia-discurso.md
# =====================================================================
def render_consistencia():
    out = [header(
        "Consistencia del Discurso de Campaña",
        "Análisis de la consistencia entre lo que cada candidato escribió en su "
        "plan de gobierno y lo que declaró en los debates presidenciales. "
        "Incluye el índice de consistencia por (candidato × tema) y un detalle "
        "de las propuestas omitidas y los nuevos compromisos asumidos en debate."
    )]

    out.append(
        "**Fórmula del índice de consistencia:**  \n"
        "$$I_c = \\frac{\\text{CONSISTENTE} + \\text{AMPLÍA\\_DEBATE}}"
        "{\\text{CONSISTENTE} + \\text{AMPLÍA\\_DEBATE} + \\text{VAGUEA} + \\text{CONTRADICE\\_DEBATE}}$$\n\n"
        "Rango 0–1. **No** penaliza OMITE ni NUEVO_DEBATE en el denominador "
        "(son comportamientos distintos: silencio o expansión, no contradicción).\n\n"
    )

    agg = cmp_data["consistencia_por_candidato"]

    # Tabla resumen
    out.append("## Resumen por candidato y tema\n\n")
    out.append("| Candidato | Tema | n_plan | n_debate | Consist. | Amplía | Vaguea | Contradice | Omite | Nuevo | Índice |\n")
    out.append("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n")
    for a in sorted(agg, key=lambda x: (x["candidato"], x["tema"])):
        ic = f"{a['indice_consistencia']:.2f}" if a["indice_consistencia"] is not None else "—"
        tema = TEMA_INFO.get(a["tema"], {"nombre": a["tema"]})["nombre"]
        out.append(
            f"| {NOMBRE[a['candidato']]} | {tema} | {a['n_propuestas_plan']} | "
            f"{a['n_declaraciones_debate']} | {a['consistentes']} | {a['amplia_debate']} | "
            f"{a['vaguea']} | {a['contradice_debate']} | {a['omite']} | {a['nuevo_debate']} | "
            f"{ic} |\n"
        )

    # Propuestas OMITE
    out.append("\n---\n\n## Propuestas del plan no mencionadas en debate (OMITE)\n\n")
    omites = [c for c in cmp_data["plan_vs_debate"] if c["relacion"] == "OMITE"]
    if not omites:
        out.append("_No se identificaron omisiones relevantes en esta primera vuelta de análisis._\n\n")
    else:
        for cand in ("keiko", "roberto"):
            sub = [c for c in omites if c["candidato"] == cand]
            if not sub:
                continue
            out.append(f"### {NOMBRE[cand]}\n\n")
            for c in sub:
                out.append(f"- {cita_propuesta(c['propuesta_id'])}  \n")
                out.append(f"  *{c['analisis']}*\n\n")

    # Compromisos NUEVO_DEBATE
    out.append("---\n\n## Compromisos asumidos en debate sin contraparte en el plan (NUEVO_DEBATE)\n\n")
    nuevos = [c for c in cmp_data["plan_vs_debate"] if c["relacion"] == "NUEVO_DEBATE"]
    if not nuevos:
        out.append("_No se identificaron compromisos nuevos en esta primera vuelta._\n\n")
    else:
        for cand in ("keiko", "roberto"):
            sub = [c for c in nuevos if c["candidato"] == cand]
            if not sub:
                continue
            out.append(f"### {NOMBRE[cand]}\n\n")
            for c in sub:
                out.append(f"- {cita_declaracion(c['declaracion_id'])}\n\n")
                out.append(f"  *{c['analisis']}*\n\n")

    (OUT / "consistencia-discurso.md").write_text("".join(out), encoding="utf-8")
    print("Escrito: 03-Comparaciones/consistencia-discurso.md")


if __name__ == "__main__":
    render_matriz_temas()
    render_coincidencias()
    render_divergencias()
    render_contradicciones()
    render_consistencia()
    print("OK.")
