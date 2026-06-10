#!/usr/bin/env python3
"""
Validador de 00-Sistema/datos/propuestas.json.

Verifica:
  1. Conformidad estructural básica con el schema (sin librerías externas).
  2. Unicidad de IDs.
  3. Formato de IDs según convención [kr]-[tema_id]-NNN.
  4. Que cada `tema` referenciado por una propuesta exista en la lista de temas.
  5. Que linea_inicio <= linea_fin.
  6. Que el rango de líneas exista en el archivo fuente y la cita_textual aparezca
     (al menos un fragmento de 25 chars de la cita) entre esas líneas.

Uso:
    python 00-Sistema/scripts/validar_propuestas.py
Exit code:
    0  → OK
    1  → falla la validación (imprime detalle de errores)
"""
import json
import re
import sys
from pathlib import Path

# Asegurar UTF-8 en stdout/stderr para que los emojis funcionen en Windows cp1252
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

VAULT = Path(__file__).resolve().parent.parent.parent
DATOS = VAULT / "00-Sistema" / "datos" / "propuestas.json"

ID_PATTERN = re.compile(r"^[kr]-[a-z_]+-[0-9]{3}$")
TIPOS = {"propuesta", "meta", "diagnostico", "principio", "100dias"}
RELEVANCIAS = {"ALTA", "MEDIA", "BAJA", "100DIAS"}
CANDIDATOS = {"keiko", "roberto"}
REQ_PROPUESTA = {"id", "candidato", "tema", "tipo", "relevancia", "texto", "cita_textual", "fuente"}
REQ_FUENTE = {"archivo", "linea_inicio", "linea_fin"}


def load_lines(rel_path: str) -> list[str]:
    p = VAULT / rel_path
    if not p.exists():
        return []
    return p.read_text(encoding="utf-8").splitlines()


def normalizar(texto: str) -> str:
    """Colapsa espacios y normaliza para búsqueda flexible."""
    return re.sub(r"\s+", " ", texto).strip().lower()


def main() -> int:
    if not DATOS.exists():
        print(f"❌ No existe {DATOS}")
        return 1

    data = json.loads(DATOS.read_text(encoding="utf-8"))
    errores: list[str] = []

    # Top-level
    for k in ("candidatos", "temas", "propuestas"):
        if k not in data:
            errores.append(f"Falta clave de nivel raíz: {k}")

    if errores:
        for e in errores:
            print("❌", e)
        return 1

    # Candidatos
    for c in CANDIDATOS:
        if c not in data["candidatos"]:
            errores.append(f"Falta candidato: {c}")

    # Temas
    tema_ids = {t["id"] for t in data["temas"]}

    # Propuestas
    vistos: set[str] = set()
    cache_archivos: dict[str, list[str]] = {}
    for i, p in enumerate(data["propuestas"]):
        falta = REQ_PROPUESTA - set(p.keys())
        if falta:
            errores.append(f"Propuesta #{i}: faltan campos {falta}")
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
        if p["relevancia"] not in RELEVANCIAS:
            errores.append(f"{p['id']}: relevancia inválida {p['relevancia']!r}")
        if p["tema"] not in tema_ids:
            errores.append(f"{p['id']}: tema {p['tema']!r} no está en la taxonomía")

        # Consistencia ID ↔ candidato/tema
        prefijo = p["id"][0]
        if prefijo == "k" and p["candidato"] != "keiko":
            errores.append(f"{p['id']}: prefijo 'k' pero candidato es {p['candidato']!r}")
        if prefijo == "r" and p["candidato"] != "roberto":
            errores.append(f"{p['id']}: prefijo 'r' pero candidato es {p['candidato']!r}")
        partes = p["id"].split("-")
        if len(partes) >= 3 and partes[1] != p["tema"]:
            errores.append(f"{p['id']}: tema en ID ({partes[1]}) ≠ tema declarado ({p['tema']})")

        # Fuente
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

        # Verificación de cita textual: al menos 25 chars contiguos de la cita
        # deben aparecer en el rango [linea_inicio, linea_fin].
        rango = "\n".join(lineas[li - 1: lf])
        rango_norm = normalizar(rango)
        cita_norm = normalizar(p["cita_textual"])
        if len(cita_norm) >= 25:
            fragmento = cita_norm[:50] if len(cita_norm) >= 50 else cita_norm
            # Busca cualquier subcadena de 25 chars de la cita en el rango
            encontrado = any(
                fragmento[j:j + 25] in rango_norm
                for j in range(0, max(1, len(fragmento) - 24))
            )
            if not encontrado:
                errores.append(
                    f"{p['id']}: cita_textual no aparece en {archivo}:L{li}-{lf}"
                )

    if errores:
        for e in errores:
            print("❌", e)
        print(f"\n{len(errores)} error(es).")
        return 1

    n_props = len(data["propuestas"])
    n_k = sum(1 for p in data["propuestas"] if p["candidato"] == "keiko")
    n_r = sum(1 for p in data["propuestas"] if p["candidato"] == "roberto")
    print(f"✅ Validación OK — {n_props} propuestas (Keiko: {n_k}, Roberto: {n_r})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
