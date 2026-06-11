# Sub-proyecto 1 — Extracción de propuestas a `propuestas.json`

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Construir `00-Sistema/datos/propuestas.json` con todas las propuestas, metas, diagnósticos, principios y compromisos de 100 días extraídos de los dos planes de gobierno, con citas textuales, fuente exacta (archivo + rango de líneas) y clasificación por tema/tipo/relevancia.

**Architecture:** JSON como source of truth. Schema formal (`propuestas.schema.json`) + script validador Python (`validar_propuestas.py`) que verifica estructura, unicidad de IDs, formato de IDs, conformidad de temas con la taxonomía, y existencia del rango de líneas en el archivo fuente. Extracción incremental por sección (pilar/dimensión); commit después de cada sección.

**Tech Stack:** Python 3 (stdlib only — `json`, `re`, `sys`, `pathlib`), git, archivos `.md` de los planes ya cargados.

**Spec de referencia:** `00-Sistema/specs/2026-06-09-capa-datos-comparacion-design.md`

**Working directory:** `C:\Users\Iriarte 06\Downloads\Seguimiento Planes de Gobierno Perú` (referida como `<vault>` en este plan)

---

## Fase 1 — Infraestructura

### Task 1: Inicializar git y estructura de carpetas

**Files:**
- Create: `<vault>/.gitignore`
- Create: `<vault>/00-Sistema/datos/.gitkeep`

- [ ] **Step 1: Inicializar repositorio git en el vault**

Run:
```bash
cd "/c/Users/Iriarte 06/Downloads/Seguimiento Planes de Gobierno Perú"
git init -b main
```

Expected: `Initialized empty Git repository in .../Seguimiento Planes de Gobierno Perú/.git/`

- [ ] **Step 2: Crear `.gitignore`**

Crear archivo `<vault>/.gitignore` con el siguiente contenido exacto:

```
# OS
.DS_Store
Thumbs.db
desktop.ini

# Editores
.vscode/
.idea/
*.swp
*~

# Python (para el validador)
__pycache__/
*.pyc
.venv/

# Node (futuro: marked.js si lo bajamos local)
node_modules/

# Build / despliegue (futuro)
.vercel/
```

- [ ] **Step 3: Crear directorios para datos y scripts**

Run:
```bash
mkdir -p "00-Sistema/datos" "00-Sistema/scripts"
touch "00-Sistema/datos/.gitkeep" "00-Sistema/scripts/.gitkeep"
```

- [ ] **Step 4: Primer commit**

```bash
git add .gitignore "00-Sistema/datos/.gitkeep" "00-Sistema/scripts/.gitkeep"
git commit -m "chore: inicializar git y crear estructura de capa de datos"
```

Expected: commit creado con 3 archivos.

---

### Task 2: Definir el JSON Schema de `propuestas.json`

**Files:**
- Create: `<vault>/00-Sistema/datos/propuestas.schema.json`

- [ ] **Step 1: Escribir el schema completo**

Crear `00-Sistema/datos/propuestas.schema.json` con el contenido:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Propuestas — Brain Político Perú",
  "type": "object",
  "required": ["candidatos", "temas", "propuestas"],
  "additionalProperties": false,
  "properties": {
    "candidatos": {
      "type": "object",
      "required": ["keiko", "roberto"],
      "additionalProperties": false,
      "properties": {
        "keiko": { "$ref": "#/$defs/candidato" },
        "roberto": { "$ref": "#/$defs/candidato" }
      }
    },
    "temas": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "nombre"],
        "additionalProperties": false,
        "properties": {
          "id": { "type": "string", "pattern": "^[a-z_]+$" },
          "nombre": { "type": "string" },
          "icono": { "type": "string" }
        }
      }
    },
    "propuestas": {
      "type": "array",
      "items": { "$ref": "#/$defs/propuesta" }
    }
  },
  "$defs": {
    "candidato": {
      "type": "object",
      "required": ["nombre", "partido", "color"],
      "properties": {
        "nombre": { "type": "string" },
        "partido": { "type": "string" },
        "color": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$" }
      }
    },
    "propuesta": {
      "type": "object",
      "required": ["id", "candidato", "tema", "tipo", "relevancia", "texto", "cita_textual", "fuente"],
      "additionalProperties": false,
      "properties": {
        "id": { "type": "string", "pattern": "^[kr]-[a-z_]+-[0-9]{3}$" },
        "candidato": { "enum": ["keiko", "roberto"] },
        "tema": { "type": "string" },
        "tipo": { "enum": ["propuesta", "meta", "diagnostico", "principio", "100dias"] },
        "relevancia": { "enum": ["ALTA", "MEDIA", "BAJA", "100DIAS"] },
        "texto": { "type": "string", "minLength": 10 },
        "cita_textual": { "type": "string", "minLength": 5 },
        "fuente": {
          "type": "object",
          "required": ["archivo", "linea_inicio", "linea_fin"],
          "properties": {
            "archivo": { "type": "string" },
            "seccion": { "type": "string" },
            "linea_inicio": { "type": "integer", "minimum": 1 },
            "linea_fin": { "type": "integer", "minimum": 1 }
          }
        },
        "meta_cuantitativa": { "type": ["string", "null"] }
      }
    }
  }
}
```

Notas de diseño del schema:
- El ID sigue el patrón `[kr]-[tema_id]-NNN` (regex `^[kr]-[a-z_]+-[0-9]{3}$`).
- `tipo` y `relevancia` están restringidos por `enum` para detectar typos.
- Los tema IDs en propuestas no se validan contra la lista de `temas` en el schema (el JSON Schema no lo permite cómodamente); eso lo hace el validador en Task 3.
- `additionalProperties: false` en `propuesta` para no aceptar campos extra silenciosos.

- [ ] **Step 2: Commit del schema**

```bash
git add "00-Sistema/datos/propuestas.schema.json"
git commit -m "feat: definir JSON Schema para propuestas.json"
```

---

### Task 3: Escribir el script validador

**Files:**
- Create: `<vault>/00-Sistema/scripts/validar_propuestas.py`

- [ ] **Step 1: Escribir el validador**

Crear `00-Sistema/scripts/validar_propuestas.py`:

```python
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
```

- [ ] **Step 2: Verificar que Python 3 esté disponible**

Run:
```bash
python --version
```

Expected: `Python 3.x.y` (x >= 8). Si no está disponible, probar `python3 --version` o `py --version` (Windows).

- [ ] **Step 3: Commit del validador**

```bash
git add "00-Sistema/scripts/validar_propuestas.py"
git commit -m "feat: script validador de propuestas.json"
```

---

### Task 4: Crear `propuestas.json` inicial con candidatos y temas, validar

**Files:**
- Create: `<vault>/00-Sistema/datos/propuestas.json`

- [ ] **Step 1: Crear `propuestas.json` con candidatos y los 29 temas**

Crear `00-Sistema/datos/propuestas.json` con el siguiente contenido exacto (los IDs y nombres coinciden con la taxonomía de `00-Sistema/CLAUDE.md` §4):

```json
{
  "candidatos": {
    "keiko": {
      "nombre": "Keiko Fujimori",
      "partido": "Fuerza Popular",
      "color": "#C0392B"
    },
    "roberto": {
      "nombre": "Roberto Sánchez Palomino",
      "partido": "Juntos por el Perú",
      "color": "#2471A3"
    }
  },
  "temas": [
    { "id": "seguridad", "nombre": "Seguridad Ciudadana", "icono": "🔒" },
    { "id": "corrupcion", "nombre": "Anticorrupción", "icono": "🛡️" },
    { "id": "economia", "nombre": "Economía / Macroeconomía", "icono": "💰" },
    { "id": "trabajo", "nombre": "Trabajo y Empleo", "icono": "💼" },
    { "id": "mype", "nombre": "MYPE y Emprendimiento", "icono": "🏪" },
    { "id": "mineria", "nombre": "Minería", "icono": "⛏️" },
    { "id": "agricultura", "nombre": "Agricultura", "icono": "🌾" },
    { "id": "pesca", "nombre": "Pesca", "icono": "🐟" },
    { "id": "energia", "nombre": "Energía", "icono": "⚡" },
    { "id": "transporte", "nombre": "Transporte e Infraestructura", "icono": "🚧" },
    { "id": "turismo", "nombre": "Turismo", "icono": "🏞️" },
    { "id": "industria", "nombre": "Industria", "icono": "🏭" },
    { "id": "ambiente", "nombre": "Ambiente / Desarrollo Sostenible", "icono": "🌳" },
    { "id": "educacion", "nombre": "Educación", "icono": "📚" },
    { "id": "salud", "nombre": "Salud", "icono": "🏥" },
    { "id": "vivienda", "nombre": "Vivienda", "icono": "🏠" },
    { "id": "agua", "nombre": "Agua y Saneamiento", "icono": "💧" },
    { "id": "pensiones", "nombre": "Pensiones / Programas Sociales", "icono": "👵" },
    { "id": "deporte", "nombre": "Deporte", "icono": "⚽" },
    { "id": "justicia", "nombre": "Sistema de Justicia", "icono": "⚖️" },
    { "id": "orden_juridico", "nombre": "Orden Jurídico / Seguridad Jurídica", "icono": "📜" },
    { "id": "exterior", "nombre": "Relaciones Exteriores", "icono": "🌎" },
    { "id": "constitucion", "nombre": "Reforma Constitucional / Institucional", "icono": "🏛️" },
    { "id": "indigenas", "nombre": "Pueblos Indígenas y DDHH", "icono": "🪶" },
    { "id": "genero", "nombre": "Género e Inclusión", "icono": "🤝" },
    { "id": "cti", "nombre": "Ciencia, Tecnología e Innovación", "icono": "🔬" },
    { "id": "juventud", "nombre": "Juventud", "icono": "🧑‍🎓" },
    { "id": "cultura", "nombre": "Cultura", "icono": "🎭" },
    { "id": "peruanos_exterior", "nombre": "Peruanos en el Extranjero", "icono": "✈️" }
  ],
  "propuestas": []
}
```

- [ ] **Step 2: Correr el validador**

Run:
```bash
python "00-Sistema/scripts/validar_propuestas.py"
```

Expected: `✅ Validación OK — 0 propuestas (Keiko: 0, Roberto: 0)`

- [ ] **Step 3: Commit**

```bash
git add "00-Sistema/datos/propuestas.json"
git commit -m "feat: inicializar propuestas.json con candidatos y taxonomía de 29 temas"
```

---

## Fase 2 — Extracción Keiko Fujimori

> **Criterios de extracción comunes a las Tasks 5-8** (no repetir mentalmente cada vez — están aquí):
>
> **¿Qué cuenta como una entrada en `propuestas`?** Toda afirmación que se pueda categorizar como uno de estos cinco tipos:
>
> - **`propuesta`** → Acción concreta que el candidato se compromete a realizar. Verbos: "implementaremos", "crearemos", "fortaleceremos", "lanzaremos", etc.
> - **`meta`** → Objetivo medible con cifra, porcentaje o plazo. Ej: "reducir homicidios en 20% al 2031".
> - **`diagnostico`** → Descripción de un problema (no una solución). Solo extraer diagnósticos **destacados** del plan (no cada frase de contexto). Heurística: si el diagnóstico aparece como bullet o en sección "Diagnóstico" → extraer; si es prosa de contexto → ignorar.
> - **`principio`** → Valor o enfoque filosófico que guía las decisiones del candidato. Ej: "creemos en la economía social de mercado". Suelen estar en Ideario/Visión.
> - **`100dias`** → Acción explícitamente listada en una sección de "Primeros 100 días" o "100 días".
>
> **Asignación de relevancia:**
> - **`ALTA`** → Propuesta-ancla mencionada en visión, presentación o mensaje del candidato.
> - **`MEDIA`** → Propuesta en sección específica, con meta cuantitativa, plazo claro o impacto sectorial mayor.
> - **`BAJA`** → Detalle sin meta ni plazo.
> - **`100DIAS`** → Solo si `tipo: 100dias`.
>
> **Asignación de tema:** Un tema único por propuesta (el dominante). Si toca varios, elegir el principal y mencionar los demás en el campo `texto` ("también impacta agua y ambiente"). Lista de IDs disponibles en `propuestas.json` → `temas`.
>
> **Convención de ID:** `k-<tema_id>-<NNN>` donde NNN es el siguiente número disponible para Keiko en ese tema, empezando en `001`.
>
> **Cita textual:** copiar verbatim del plan, sin reformatear. Si la propuesta abarca varias líneas, copiar el fragmento más representativo (1-3 oraciones, no más de 500 caracteres). El validador verifica que al menos 25 chars consecutivos de `cita_textual` aparezcan en el rango `[linea_inicio, linea_fin]`.
>
> **Campo `texto`:** redacción analítica propia de 1-3 oraciones que resume la propuesta. NO es la cita.
>
> **`fuente.seccion`:** identificador legible humano de la sección, p.ej. "Pilar 1 — Orden, §1.1 Orden Ciudadano".
>
> **Volumen esperado por candidato:** ~150-300 propuestas en total (Keiko). Si una sección produce <5 entradas, probablemente se está perdiendo información — releer la sección.

---

### Task 5: Extraer propuestas del Pilar 1 — ORDEN (Keiko)

**Files:**
- Read: `01-Planes-de-Gobierno/Keiko-Fujimori/Plan-de-Gobierno-Keiko.md` (líneas correspondientes al Pilar 1)
- Modify: `00-Sistema/datos/propuestas.json`

Pilar 1 cubre 4 subsecciones (según el índice del plan, líneas 47-53 del archivo):
- 1.1 Orden Ciudadano → tema `seguridad`
- 1.2 Lucha contra la Corrupción → tema `corrupcion`
- 1.3 Orden Económico → tema `economia`
- 1.4 Orden Jurídico → temas `orden_juridico` y/o `justicia`

- [ ] **Step 1: Localizar el rango de líneas del Pilar 1**

Run:
```bash
grep -n "^# PILAR ESTRATÉGICO" "01-Planes-de-Gobierno/Keiko-Fujimori/Plan-de-Gobierno-Keiko.md"
```

Esperado: 3 líneas (Pilar 1, Pilar 2, Pilar 3). Anotar la línea de inicio del Pilar 1 y la línea de inicio del Pilar 2 (esa es el fin del Pilar 1).

- [ ] **Step 2: Leer las 4 subsecciones del Pilar 1**

Leer las líneas del Pilar 1 sección por sección (1.1, 1.2, 1.3, 1.4). Identificar para cada una:
- El bloque "Diagnóstico" (extraer 1-3 diagnósticos destacados como `tipo: diagnostico`)
- El bloque "Nuestras propuestas" (extraer cada propuesta concreta como `tipo: propuesta`)
- Bloque "Primeros 100 días" si existe (como `tipo: 100dias`, `relevancia: 100DIAS`)
- Bloque "Principales metas e indicadores" si existe (cada meta cuantitativa como `tipo: meta`)

- [ ] **Step 3: Anexar las propuestas al array `propuestas` del JSON**

Editar `00-Sistema/datos/propuestas.json`. Anexar cada propuesta nueva al final del array `propuestas`. Ejemplo de entrada bien formada:

```json
{
  "id": "k-seguridad-001",
  "candidato": "keiko",
  "tema": "seguridad",
  "tipo": "propuesta",
  "relevancia": "ALTA",
  "texto": "Despliegue masivo de Policía Nacional con equipamiento renovado y centro de comando integrado C5i para combatir la criminalidad organizada.",
  "cita_textual": "Fortaleceremos la Policía Nacional con la adquisición de patrulleros, motorizadas y la implementación del Centro de Comando, Control, Comunicaciones, Computación e Inteligencia (C5i)",
  "fuente": {
    "archivo": "01-Planes-de-Gobierno/Keiko-Fujimori/Plan-de-Gobierno-Keiko.md",
    "seccion": "Pilar 1 — Orden, §1.1 Orden Ciudadano, Nuestras propuestas",
    "linea_inicio": 145,
    "linea_fin": 152
  },
  "meta_cuantitativa": null
}
```

> ⚠️ Importante: las líneas `linea_inicio`/`linea_fin` deben corresponder **exactamente** al rango donde aparece `cita_textual` en el archivo fuente. El validador lo comprueba.

- [ ] **Step 4: Validar**

```bash
python "00-Sistema/scripts/validar_propuestas.py"
```

Esperado: `✅ Validación OK — N propuestas (Keiko: N, Roberto: 0)` donde N >= 20 aprox.

Si falla: leer el output y corregir. Errores típicos:
- `cita_textual no aparece en archivo:Llinea_inicio-linea_fin` → el rango de líneas no contiene la cita. Ajustar líneas o la cita.
- `ID duplicado` → numeración incorrecta. Re-numerar.
- `tema no está en la taxonomía` → tema mal escrito. Usar el ID exacto.

- [ ] **Step 5: Sample check manual (2 entradas aleatorias)**

Elegir 2 propuestas extraídas al azar. Para cada una:
1. Abrir el archivo fuente en las líneas indicadas.
2. Verificar que `cita_textual` está ahí verbatim.
3. Verificar que la clasificación `tipo`/`relevancia`/`tema` tiene sentido.

- [ ] **Step 6: Commit**

```bash
git add "00-Sistema/datos/propuestas.json"
git commit -m "feat(keiko): extraer propuestas Pilar 1 — Orden"
```

---

### Task 6: Extraer propuestas del Pilar 2 — ECONÓMICO (Keiko)

**Files:**
- Read: `01-Planes-de-Gobierno/Keiko-Fujimori/Plan-de-Gobierno-Keiko.md` (Pilar 2)
- Modify: `00-Sistema/datos/propuestas.json`

Pilar 2 cubre 9 subsecciones:
- 2.1 Emprendedores (MYPE) → tema `mype`
- 2.2 Minería → tema `mineria`
- 2.3 Energía e Hidrocarburos → tema `energia`
- 2.4 Agricultura → tema `agricultura`
- 2.5 Pesca y Acuicultura → tema `pesca`
- 2.6 Transportes y Comunicaciones → tema `transporte`
- 2.7 Turismo → tema `turismo`
- 2.8 Industria y Comercio Exterior → tema `industria`
- 2.9 Desarrollo Sostenible o Ambiente → tema `ambiente`

- [ ] **Step 1: Localizar el rango del Pilar 2**

Run:
```bash
grep -n "^# PILAR ESTRATÉGICO" "01-Planes-de-Gobierno/Keiko-Fujimori/Plan-de-Gobierno-Keiko.md"
```

Anotar línea de inicio del Pilar 2 y línea de inicio del Pilar 3 (= fin del Pilar 2).

- [ ] **Step 2: Para cada subsección 2.1–2.9, extraer propuestas**

Aplicar los mismos criterios que en Task 5. Para cada subsección, anexar al array `propuestas`. Continuar la numeración del candidato Keiko dentro de cada tema desde 001.

Si una subsección tiene una **meta-ancla** (p.ej. "100% acceso eléctrico", "duplicar exportaciones turísticas"), marcarla `relevancia: ALTA`.

- [ ] **Step 3: Validar**

```bash
python "00-Sistema/scripts/validar_propuestas.py"
```

Esperado: `✅ Validación OK` con N que incluye Pilar 1 + Pilar 2.

- [ ] **Step 4: Sample check manual (3 entradas aleatorias de Pilar 2)**

Repetir el proceso de verificación de citas y clasificación.

- [ ] **Step 5: Commit**

```bash
git add "00-Sistema/datos/propuestas.json"
git commit -m "feat(keiko): extraer propuestas Pilar 2 — Económico"
```

---

### Task 7: Extraer propuestas del Pilar 3 — SOCIAL (Keiko)

**Files:**
- Read: `01-Planes-de-Gobierno/Keiko-Fujimori/Plan-de-Gobierno-Keiko.md` (Pilar 3)
- Modify: `00-Sistema/datos/propuestas.json`

Pilar 3 cubre las subsecciones 3.1–3.10 (revisar el índice en líneas 75-89 del archivo). Mapeo tema esperado:
- 3.1 Niños, Adolescentes y Jóvenes → tema `juventud`
- 3.2 Educación → tema `educacion`
- 3.3 Salud → tema `salud`
- 3.4 Trabajo (si existe) → tema `trabajo`
- 3.5 Vivienda → tema `vivienda`
- 3.6 Agua y Saneamiento → tema `agua`
- 3.7 Pensiones → tema `pensiones`
- 3.8 Programas Sociales → tema `pensiones` (compartido) o un sub-conjunto en `pensiones`
- 3.9 Deporte → tema `deporte`
- 3.10 Peruanos en el Extranjero → tema `peruanos_exterior`

> ⚠️ Verificar índice real porque el plan tiene 3.5 y 3.6 listados pero 3.1-3.4 podrían estar en otras líneas no mostradas en el índice resumido.

- [ ] **Step 1: Validar índice real del Pilar 3**

Run:
```bash
grep -n "^## 3\." "01-Planes-de-Gobierno/Keiko-Fujimori/Plan-de-Gobierno-Keiko.md"
```

- [ ] **Step 2: Extraer propuestas de cada subsección del Pilar 3**

Aplicar mismos criterios. Cada subsección tiene su propio bloque de Diagnóstico + Propuestas + 100 días + Metas.

- [ ] **Step 3: Validar**

```bash
python "00-Sistema/scripts/validar_propuestas.py"
```

- [ ] **Step 4: Sample check manual (3 entradas)**

- [ ] **Step 5: Commit**

```bash
git add "00-Sistema/datos/propuestas.json"
git commit -m "feat(keiko): extraer propuestas Pilar 3 — Social"
```

---

### Task 8: Extraer principios e Ideario (Keiko) + visión 2031

**Files:**
- Read: `01-Planes-de-Gobierno/Keiko-Fujimori/Plan-de-Gobierno-Keiko.md` (Mensaje, Ideario, Visión)
- Modify: `00-Sistema/datos/propuestas.json`

Capturar los principios filosóficos del candidato y la visión país. Estos NO son acciones concretas, pero son la base ideológica que da sentido a las propuestas.

- [ ] **Step 1: Localizar las secciones**

Run:
```bash
grep -n -E "^#+ (MENSAJE|IDEARIO|VISIÓN)" "01-Planes-de-Gobierno/Keiko-Fujimori/Plan-de-Gobierno-Keiko.md"
```

- [ ] **Step 2: Extraer principios**

Para cada principio destacado en Mensaje/Ideario/Visión:

```json
{
  "id": "k-economia-XXX",     // o el tema más relacionado con el principio
  "candidato": "keiko",
  "tema": "economia",          // tema dominante
  "tipo": "principio",
  "relevancia": "ALTA",
  "texto": "Resumen analítico del principio.",
  "cita_textual": "Cita verbatim.",
  "fuente": {
    "archivo": "01-Planes-de-Gobierno/Keiko-Fujimori/Plan-de-Gobierno-Keiko.md",
    "seccion": "Ideario de Fuerza Popular",
    "linea_inicio": 101,
    "linea_fin": 110
  },
  "meta_cuantitativa": null
}
```

Esperado: ~5-15 principios extraídos.

- [ ] **Step 3: Validar y sample check (1-2 entradas)**

```bash
python "00-Sistema/scripts/validar_propuestas.py"
```

- [ ] **Step 4: Commit**

```bash
git add "00-Sistema/datos/propuestas.json"
git commit -m "feat(keiko): extraer principios e ideario"
```

---

## Fase 3 — Extracción Roberto Sánchez Palomino

> Mismos criterios que Fase 2 (ver bloque al inicio de Fase 2). Prefijo de ID = `r-`. Roberto tiene 6 dimensiones (no 3 pilares).
>
> **Particularidad de Roberto:** El plan se llama "Programa de Gobierno de Segunda Vuelta" y abre con un **Contexto Internacional + Diagnóstico** ("cuatro grandes males"). Esos diagnósticos son **muy citados** en el debate y son anclas del discurso — extraerlos como `tipo: diagnostico`, `relevancia: ALTA`.

---

### Task 9: Extraer Diagnóstico ("cuatro grandes males") + Contexto Internacional (Roberto)

**Files:**
- Read: `01-Planes-de-Gobierno/Roberto-Sanchez/Plan-de-Gobierno-Roberto_Sanchez.md` (Contexto + Diagnóstico)
- Modify: `00-Sistema/datos/propuestas.json`

Según el índice (líneas 64-104):
- §1 Contexto Internacional (línea 64)
- §2 Diagnóstico de la Situación Actual del País (línea 76)

- [ ] **Step 1: Localizar y leer las secciones**

Run:
```bash
grep -n "^# " "01-Planes-de-Gobierno/Roberto-Sanchez/Plan-de-Gobierno-Roberto_Sanchez.md"
```

- [ ] **Step 2: Extraer los "cuatro grandes males" como diagnósticos ALTA**

Para cada mal identificado, una entrada `tipo: diagnostico`, `relevancia: ALTA`. El tema dependerá del contenido del mal (p.ej. desigualdad → `economia`, violencia → `seguridad`, etc.).

- [ ] **Step 3: Extraer principios del Contexto Internacional**

Si hay principios geopolíticos (p.ej. "soberanía", "no alineamiento"), capturar como `tipo: principio`, tema `exterior`.

- [ ] **Step 4: Validar y commit**

```bash
python "00-Sistema/scripts/validar_propuestas.py"
git add "00-Sistema/datos/propuestas.json"
git commit -m "feat(roberto): extraer Diagnóstico (4 grandes males) y Contexto Internacional"
```

---

### Task 10: Extraer Dimensión Institucional (Roberto)

**Files:**
- Read: `01-Planes-de-Gobierno/Roberto-Sanchez/Plan-de-Gobierno-Roberto_Sanchez.md` (Dimensión Institucional)
- Modify: `00-Sistema/datos/propuestas.json`

Cubre temas: `constitucion`, `corrupcion`, `justicia`, `seguridad`, `orden_juridico`.

- [ ] **Step 1: Localizar rango de la Dimensión Institucional**

Inicio en línea 104 según el índice. Fin: inicio de la Dimensión Económica (línea 166 aprox).

- [ ] **Step 2: Extraer propuestas, metas, principios, 100 días**

Aplicar criterios.

- [ ] **Step 3: Validar, sample check, commit**

```bash
python "00-Sistema/scripts/validar_propuestas.py"
git add "00-Sistema/datos/propuestas.json"
git commit -m "feat(roberto): extraer propuestas Dimensión Institucional"
```

---

### Task 11: Extraer Dimensión Económica (Roberto)

**Files:**
- Read: `01-Planes-de-Gobierno/Roberto-Sanchez/Plan-de-Gobierno-Roberto_Sanchez.md` (Dimensión Económica)
- Modify: `00-Sistema/datos/propuestas.json`

Cubre temas: `economia`, `trabajo`, `mype`, `mineria`, `agricultura`, `pesca`, `industria`.

- [ ] **Step 1: Localizar rango** (inicio ~línea 166, fin ~línea 223)
- [ ] **Step 2: Extraer**
- [ ] **Step 3: Validar, sample check, commit**

```bash
python "00-Sistema/scripts/validar_propuestas.py"
git add "00-Sistema/datos/propuestas.json"
git commit -m "feat(roberto): extraer propuestas Dimensión Económica"
```

---

### Task 12: Extraer Dimensión Infraestructura y Servicios Básicos (Roberto)

**Files:**
- Read: `01-Planes-de-Gobierno/Roberto-Sanchez/Plan-de-Gobierno-Roberto_Sanchez.md` (Dimensión Infraestructura)
- Modify: `00-Sistema/datos/propuestas.json`

Cubre temas: `transporte`, `energia`, `agua`, `vivienda`.

- [ ] **Step 1: Localizar rango** (inicio ~línea 223, fin ~línea 283)
- [ ] **Step 2: Extraer**
- [ ] **Step 3: Validar, sample check, commit**

```bash
python "00-Sistema/scripts/validar_propuestas.py"
git add "00-Sistema/datos/propuestas.json"
git commit -m "feat(roberto): extraer propuestas Dimensión Infraestructura"
```

---

### Task 13: Extraer Dimensión Social (Roberto)

**Files:**
- Read: `01-Planes-de-Gobierno/Roberto-Sanchez/Plan-de-Gobierno-Roberto_Sanchez.md` (Dimensión Social)
- Modify: `00-Sistema/datos/propuestas.json`

Cubre temas: `educacion`, `salud`, `pensiones`, `genero`, `juventud`, `indigenas`, `deporte`.

- [ ] **Step 1: Localizar rango** (inicio ~línea 283, fin ~línea 331)
- [ ] **Step 2: Extraer**
- [ ] **Step 3: Validar, sample check, commit**

```bash
python "00-Sistema/scripts/validar_propuestas.py"
git add "00-Sistema/datos/propuestas.json"
git commit -m "feat(roberto): extraer propuestas Dimensión Social"
```

---

### Task 14: Extraer Dimensión Cultural-Ambiental (Roberto)

**Files:**
- Read: `01-Planes-de-Gobierno/Roberto-Sanchez/Plan-de-Gobierno-Roberto_Sanchez.md` (Dimensión Cultural-Ambiental)
- Modify: `00-Sistema/datos/propuestas.json`

Cubre temas: `cultura`, `ambiente`, `cti`, `indigenas`, `turismo`.

- [ ] **Step 1: Localizar rango** (inicio ~línea 331, fin ~línea 355)
- [ ] **Step 2: Extraer**
- [ ] **Step 3: Validar, sample check, commit**

```bash
python "00-Sistema/scripts/validar_propuestas.py"
git add "00-Sistema/datos/propuestas.json"
git commit -m "feat(roberto): extraer propuestas Dimensión Cultural-Ambiental"
```

---

### Task 15: Extraer Dimensión Internacional + Notas finales (Roberto)

**Files:**
- Read: `01-Planes-de-Gobierno/Roberto-Sanchez/Plan-de-Gobierno-Roberto_Sanchez.md` (Dimensión Internacional + Notas)
- Modify: `00-Sistema/datos/propuestas.json`

Cubre temas: `exterior`, `peruanos_exterior` si aplica.

- [ ] **Step 1: Localizar rango** (inicio ~línea 355, fin del archivo)
- [ ] **Step 2: Extraer**
- [ ] **Step 3: Validar, sample check, commit**

```bash
python "00-Sistema/scripts/validar_propuestas.py"
git add "00-Sistema/datos/propuestas.json"
git commit -m "feat(roberto): extraer propuestas Dimensión Internacional"
```

---

## Fase 4 — Verificación final

### Task 16: Sample check ampliado (10 propuestas aleatorias)

**Files:**
- Read: `00-Sistema/datos/propuestas.json`

- [ ] **Step 1: Generar 10 IDs aleatorios**

Run:
```bash
python -c "import json, random; d=json.load(open('00-Sistema/datos/propuestas.json',encoding='utf-8')); random.seed(42); sample=random.sample(d['propuestas'], min(10,len(d['propuestas']))); [print(p['id'], '-', p['fuente']['archivo'], 'L'+str(p['fuente']['linea_inicio'])+'-'+str(p['fuente']['linea_fin'])) for p in sample]"
```

Expected: lista de 10 IDs con su archivo y rango de líneas.

- [ ] **Step 2: Para cada uno, abrir el archivo en el rango y verificar manualmente**

Para cada ID:
1. Abrir el archivo fuente en el editor entre `linea_inicio` y `linea_fin`.
2. Verificar que `cita_textual` está ahí (palabra por palabra o casi).
3. Verificar que `tipo` y `tema` son correctos.
4. Anotar errores.

- [ ] **Step 3: Si hay errores, corregir y re-validar**

Hacer ediciones puntuales en `propuestas.json`. Luego:
```bash
python "00-Sistema/scripts/validar_propuestas.py"
```

- [ ] **Step 4: Imprimir resumen final**

Run:
```bash
python -c "
import json
d = json.load(open('00-Sistema/datos/propuestas.json', encoding='utf-8'))
props = d['propuestas']
print(f'Total propuestas: {len(props)}')
for c in ('keiko', 'roberto'):
    sub = [p for p in props if p['candidato'] == c]
    print(f'  {c}: {len(sub)} (ALTA: {sum(1 for p in sub if p[\"relevancia\"]==\"ALTA\")}, MEDIA: {sum(1 for p in sub if p[\"relevancia\"]==\"MEDIA\")}, BAJA: {sum(1 for p in sub if p[\"relevancia\"]==\"BAJA\")}, 100DIAS: {sum(1 for p in sub if p[\"relevancia\"]==\"100DIAS\")})')
    print('    por tipo:', {t: sum(1 for p in sub if p['tipo']==t) for t in ('propuesta','meta','diagnostico','principio','100dias')})
    temas_cubiertos = sorted({p['tema'] for p in sub})
    print(f'    temas cubiertos ({len(temas_cubiertos)}): {temas_cubiertos}')
"
```

Esperado: resumen con conteos por candidato, por relevancia, por tipo, y temas cubiertos. **Bandera roja:** un candidato con <30 propuestas totales o <8 temas cubiertos — revisar qué falta.

- [ ] **Step 5: Commit final del sub-proyecto**

```bash
git add "00-Sistema/datos/propuestas.json"
git commit -m "chore: verificación final sub-proyecto 1 — extracción completa de propuestas" --allow-empty
```

---

## Cierre del sub-proyecto 1

Al completar Task 16, este sub-proyecto está terminado. El archivo `00-Sistema/datos/propuestas.json` queda como source-of-truth de las propuestas de ambos candidatos, listo para que el Sub-proyecto 2 (procesamiento de debates) lo lea y para que el Sub-proyecto 3 (análisis comparativo) lo cruce con `declaraciones.json`.

**Checkpoint para la usuaria:** revisar el resumen final del Task 16 y la salida del sample check antes de iniciar el Sub-proyecto 2.
