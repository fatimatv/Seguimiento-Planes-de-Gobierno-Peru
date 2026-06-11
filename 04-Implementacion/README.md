# Etapa 2 — Seguimiento de Implementación

> **Estado:** En espera. Se activa el **28 de julio de 2026** con la toma de mando del gobierno electo en la segunda vuelta del 7 de junio.

Esta carpeta está reservada para registrar el cumplimiento real de los compromisos electorales una vez iniciada la gestión. Hasta entonces queda vacía (excepto este README) y el panel `🔭 Etapa 2` del dashboard muestra todas las propuestas como `PENDIENTE` o `SIN DATO`.

## Cuándo retomar este trabajo

Apenas salga el primer decreto, ley, informe oficial o noticia verificada que **cumpla, modifique, bloquee o incumpla** una de las propuestas registradas en `00-Sistema/datos/propuestas.json`.

Plazos naturales en los que conviene actualizar:

| Fecha | Hito | Acción esperada |
|---|---|---|
| 28 jul 2026 | Inauguración | Confirmar candidato ganador, marcar las propuestas del perdedor como N/A |
| 5 nov 2026 | 100 días | Revisar todos los compromisos con `tipo: 100dias` y registrar estado |
| 28 jul 2027 | 1.er año | Revisión anual completa de propuestas-ancla |
| 28 jul 2028 | Mitad de período | Evaluación intermedia |
| 28 jul 2031 | Fin de mandato | Balance final |

## Diseño del pipeline (a construir cuando se necesite)

Cuando llegue el momento se construirá:

### 1. Ficha por implementación

Una carpeta por candidato-en-gobierno (`keiko/` o `roberto/`) y dentro un archivo Markdown por propuesta registrada:

```
04-Implementacion/
└── roberto/
    ├── r-ambiente-013.md     # Derogar la Ley Antiforestal
    ├── r-seguridad-006.md    # Derogar leyes pro-crimen
    └── r-trabajo-008.md      # RMV a S/ 1,500
```

Cada `.md` tendrá frontmatter YAML y cuerpo libre en markdown:

```markdown
---
propuesta_id: r-ambiente-013
estado: CUMPLIDA          # PENDIENTE | CUMPLIDA | PARCIAL | INCUMPLIDA | BLOQUEADA
fecha_evidencia: 2026-09-12
norma: "Decreto Supremo N° 045-2026-MINAM"
url: "https://elperuano.pe/..."
ultima_actualizacion: 2026-09-15
---

## Evidencia

> "Artículo 1°.- Deróguese la Ley N° 31973..."
> — Decreto Supremo N° 045-2026-MINAM

## Análisis

El DS publicado el 12 set 2026 deroga formalmente la "Ley Antiforestal"
en los términos comprometidos por el candidato durante la campaña.
La derogación incluye el restablecimiento del régimen previo de zonificación
forestal por OSINFOR.
```

### 2. Script builder

`00-Sistema/scripts/build_implementaciones.py`:

- Escanea `04-Implementacion/{keiko,roberto}/*.md`
- Parsea frontmatter (yaml) + cuerpo (markdown)
- Valida que `propuesta_id` exista en `propuestas.json`
- Genera `00-Sistema/datos/implementaciones.json` siguiendo el schema de la ontología

### 3. Schema + validador

`00-Sistema/datos/implementaciones.schema.json` y `00-Sistema/scripts/validar_implementaciones.py` — siguiendo el patrón de los 3 JSON existentes.

### 4. Dashboard

Actualizar `index.html` panel `🔭 Etapa 2`:

- Agregar `fetch('00-Sistema/datos/implementaciones.json')` al pipeline de carga.
- En `renderE2_100d()` y `renderE2_meta()`, para cada propuesta cruzar con la implementación:
  - Reemplazar badge `PENDIENTE`/`SIN DATO` por el real (`CUMPLIDA`, `PARCIAL`, etc.).
  - Mostrar la norma y la fecha en la columna **Evidencia**.
  - Click en la fila expande el análisis del .md renderizado con marked.js.

### 5. Flujo de trabajo de la usuaria

Una vez construido, cargar una evidencia toma 4 pasos:

```bash
# 1. Crear/editar la ficha
notepad "04-Implementacion/roberto/r-ambiente-013.md"

# 2. Regenerar el JSON
python 00-Sistema/scripts/build_implementaciones.py

# 3. Validar
python 00-Sistema/scripts/validar_implementaciones.py

# 4. Commit y push (Vercel redespliega solo)
git add 04-Implementacion/ 00-Sistema/datos/implementaciones.json
git commit -m "evidencia: r-ambiente-013 CUMPLIDA con DS 045-2026-MINAM"
git push
```

## Cómo retomar este trabajo

Cuando llegue el momento, decirle a Claude:

> "Arma el pipeline de evidencias de Etapa 2 según el plan en `04-Implementacion/README.md` y carga la primera ficha para la propuesta `<id>` con estado `<estado>` y evidencia `<norma o cita>`."

Claude tendrá todo el contexto necesario en este README para construirlo en una sola sesión.

## Fuentes oficiales esperadas

Para sustentar evidencias, las fuentes confiables son:

- **El Peruano** — decretos supremos, leyes, normas (https://elperuano.pe)
- **Congreso de la República** — leyes aprobadas (https://www.congreso.gob.pe)
- **MEF** — Marco Macroeconómico Multianual, Presupuesto
- **Contraloría General de la República** — informes de control
- **INEI** — estadísticas oficiales (pobreza, empleo, anemia, etc.)
- **Prensa verificada** — El Comercio, La República, Gestión, Semana Económica
- **Think tanks** — IEP, CIES, Grade, Proética
