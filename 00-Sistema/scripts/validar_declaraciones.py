#!/usr/bin/env python3
"""
Validador de 00-Sistema/datos/declaraciones.json.

Verifica:
  1. Conformidad estructural básica.
  2. Unicidad de IDs de declaraciones y de debates.
  3. Formato de IDs según convención debate-N-[kr]-NNN.
  4. Que cada debate_id referenciado exista en la lista de debates.
  5. Que cada `tema` referenciado por una declaración exista en la
     taxonomía definida en propuestas.json (única fuente de verdad de temas).
  6. Que linea_inicio <= linea_fin.
  7. Que el rango de líneas exista en el archivo fuente y la cita_textual
     (al menos un fragmento de 20 chars de la cita) aparezca entre esas líneas.

Uso:
    python 00-Sistema/scripts/validar_declaraciones.py
Exit code:
    0  → OK
    1  → falla la validación
"""
import json
import re
import sys
from pathlib import Path

# Forzar UTF-8 en stdout para emojis en consola Windows
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

VAULT = Path(__file__).resolve().parent.parent.parent
DATOS = VAULT / "00-Sistema" / "datos" / "declaraciones.json"
PROPUESTAS = VAULT / "00-Sistema" / "datos" / "propuestas.json"

ID_PATTERN = re.compile(r"^debate-[0-9]+-[kr]-[0-9]{3}$")
DEBATE_ID_PATTERN = re.compile(r"^debate-[0-9]+$")
TIPOS = {"propuesta", "diagnostico", "ataque", "defensa", "cifra", "compromiso", "evasion", "principio"}
CANDIDATOS = {"keiko", "roberto"}
REQ_DECL = {"id", "debate_id", "candidato", "tema", "tipo", "texto", "cita_textual", "fuente"}
REQ_FUENTE = {"archivo", "linea_inicio", "linea_fin"}
REQ_DEBATE = {"id", "fecha", "organizador", "formato", "archivo_fuente"}


def load_lines(rel_path: str) -> list[str]:
    p = VAULT / rel_path
    if not p.exists():
        return []
    return p.read_text(encoding="utf-8").splitlines()


def normalizar(texto: str) -> str:
    return re.sub(r"\s+", " ", texto).strip().lower()


def main() -> int:
    if not DATOS.exists():
        print(f"[X] No existe {DATOS}")
        return 1
    if not PROPUESTAS.exists():
        print(f"[X] No existe {PROPUESTAS} (taxonomía de temas)")
        return 1

    propuestas_data = json.loads(PROPUESTAS.read_text(encoding="utf-8"))
    tema_ids = {t["id"] for t in propuestas_data["temas"]}

    data = json.loads(DATOS.read_text(encoding="utf-8"))
    errores: list[str] = []

    for k in ("debates", "declaraciones"):
        if k not in data:
            errores.append(f"Falta clave de nivel raíz: {k}")
    if errores:
        for e in errores:
            print("[X]", e)
        return 1

    # Debates
    debates_ids: set[str] = set()
    for i, d in enumerate(data["debates"]):
        falta = REQ_DEBATE - set(d.keys())
        if falta:
            errores.append(f"Debate #{i}: faltan campos {falta}")
            continue
        if not DEBATE_ID_PATTERN.match(d["id"]):
            errores.append(f"Debate id inválido: {d['id']!r}")
        if d["id"] in debates_ids:
            errores.append(f"Debate id duplicado: {d['id']!r}")
        debates_ids.add(d["id"])
        if d["formato"] not in {"cara-a-cara", "equipos-tecnicos"}:
            errores.append(f"{d['id']}: formato inválido {d['formato']!r}")

    # Declaraciones
    vistos: set[str] = set()
    cache_archivos: dict[str, list[str]] = {}
    for i, p in enumerate(data["declaraciones"]):
        falta = REQ_DECL - set(p.keys())
        if falta:
            errores.append(f"Declaración #{i}: faltan campos {falta}")
            continue

        if not ID_PATTERN.match(p["id"]):
            errores.append(f"ID inválido: {p['id']!r}")
        if p["id"] in vistos:
            errores.append(f"ID duplicado: {p['id']!r}")
        vistos.add(p["id"])

        if p["candidato"] not in CANDIDATOS:
            errores.append(f"{p['id']}: candidato inválido {p['candidato']!r}")
        if p["tipo"] not in TIPOS:
            errores.append(f"{p['id']}: tipo inválido {p['tipo']!r}")
        if p["tema"] not in tema_ids:
            errores.append(f"{p['id']}: tema {p['tema']!r} no está en la taxonomía")
        if p["debate_id"] not in debates_ids:
            errores.append(f"{p['id']}: debate_id {p['debate_id']!r} no existe en debates[]")

        # Consistencia ID ↔ debate / candidato
        partes = p["id"].split("-")
        if len(partes) >= 4:
            debate_num = partes[1]
            prefijo = partes[2]
            if f"debate-{debate_num}" != p["debate_id"]:
                errores.append(f"{p['id']}: debate en ID ≠ debate_id ({p['debate_id']})")
            if prefijo == "k" and p["candidato"] != "keiko":
                errores.append(f"{p['id']}: prefijo 'k' pero candidato es {p['candidato']!r}")
            if prefijo == "r" and p["candidato"] != "roberto":
                errores.append(f"{p['id']}: prefijo 'r' pero candidato es {p['candidato']!r}")

        f = p.get("fuente", {})
        falta_f = REQ_FUENTE - set(f.keys())
        if falta_f:
            errores.append(f"{p['id']}: faltan campos en fuente {falta_f}")
            continue
        li, lf = f["linea_inicio"], f["linea_fin"]
        if li > lf:
            errores.append(f"{p['id']}: linea_inicio ({li}) > linea_fin ({lf})")

        archivo = f["archivo"]
        if archivo not in cache_archivos:
            cache_archivos[archivo] = load_lines(archivo)
        lineas = cache_archivos[archivo]
        if not lineas:
            errores.append(f"{p['id']}: no se pudo leer fuente {archivo!r}")
            continue
        if lf > len(lineas):
            errores.append(f"{p['id']}: linea_fin ({lf}) excede líneas del archivo ({len(lineas)})")
            continue

        # Verificación de cita_textual: al menos 20 chars consecutivos
        # (los debates tienen citas más cortas que los planes)
        rango = "\n".join(lineas[li - 1: lf])
        rango_norm = normalizar(rango)
        cita_norm = normalizar(p["cita_textual"])
        if len(cita_norm) >= 20:
            fragmento = cita_norm[:60] if len(cita_norm) >= 60 else cita_norm
            encontrado = any(
                fragmento[j:j + 20] in rango_norm
                for j in range(0, max(1, len(fragmento) - 19))
            )
            if not encontrado:
                errores.append(
                    f"{p['id']}: cita_textual no aparece en {archivo}:L{li}-{lf}"
                )

    if errores:
        for e in errores:
            print("[X]", e)
        print(f"\n{len(errores)} error(es).")
        return 1

    n_decl = len(data["declaraciones"])
    n_k = sum(1 for p in data["declaraciones"] if p["candidato"] == "keiko")
    n_r = sum(1 for p in data["declaraciones"] if p["candidato"] == "roberto")
    print(f"[OK] Validacion OK - {n_decl} declaraciones (Keiko: {n_k}, Roberto: {n_r}) en {len(data['debates'])} debate(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
