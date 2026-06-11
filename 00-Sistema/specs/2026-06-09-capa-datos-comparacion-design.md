# Capa de datos unificada para comparación de planes y debates

**Estado:** Diseño aprobado — pendiente de plan de implementación
**Fecha:** 2026-06-09
**Autora del proyecto:** Fátima (abogada, usuaria del vault)
**Repo destino:** GitHub público + despliegue Vercel

---

## 1. Problema y objetivo

El vault "Brain Político Perú" tiene la arquitectura, la ontología y los datos fuente listos (2 planes de gobierno + 2 transcripciones de debates), pero **las carpetas de salida están vacías**: `02-Debates/procesados/` no tiene declaraciones estructuradas y `03-Comparaciones/` no tiene los reportes comparativos. El dashboard HTML existe pero opera sobre datos hardcoded de ejemplo, no sobre los planes reales.

**Objetivo:** producir todo el análisis comparativo — propuestas de cada plan, declaraciones de cada debate, relaciones entre ellas, y especialmente la **consistencia del discurso de campaña** (planes escritos vs. lo declarado en debates) — desplegado como sitio público en Vercel respaldado por un repositorio GitHub.

## 2. Principio arquitectónico: una sola fuente de verdad

Los JSON en `00-Sistema/datos/` son la única fuente de verdad. Todo lo demás (los `.md` de reportes y el dashboard HTML) son **vistas** generadas determinísticamente desde esos JSON. Corregir un error en un JSON re-renderiza todo coherente.

```
FUENTES (read-only) ──► CAPA DE DATOS (JSON) ──► VISTAS (.md + HTML)
  planes .md                propuestas.json         03-Comparaciones/
  debates .txt              declaraciones.json      02-Debates/procesados/
                            comparaciones.json      dashboard (index.html)
```

## 3. Esquema de datos

### 3.1 `00-Sistema/datos/propuestas.json`

```jsonc
{
  "candidatos": {
    "keiko":   { "nombre": "Keiko Fujimori", "partido": "Fuerza Popular", "color": "#C0392B" },
    "roberto": { "nombre": "Roberto Sánchez Palomino", "partido": "Juntos por el Perú", "color": "#2471A3" }
  },
  "temas": [
    { "id": "seguridad", "nombre": "Seguridad Ciudadana", "icono": "🔒" }
    // 29 temas según CLAUDE.md §4
  ],
  "propuestas": [
    {
      "id": "k-seguridad-001",
      "candidato": "keiko",
      "tema": "seguridad",
      "tipo": "propuesta",           // propuesta | meta | diagnóstico | principio | 100dias
      "relevancia": "ALTA",          // ALTA | MEDIA | BAJA | 100DIAS
      "texto": "Resumen analítico de la propuesta (1-3 oraciones).",
      "cita_textual": "Cita verbatim del plan.",
      "fuente": {
        "archivo": "01-Planes-de-Gobierno/Keiko-Fujimori/Plan-de-Gobierno-Keiko.md",
        "seccion": "Eje 1 — Orden, §2.3",
        "linea_inicio": 1245,
        "linea_fin": 1252
      },
      "meta_cuantitativa": "Reducir homicidios en 20% al 2031"   // null si no aplica
    }
  ]
}
```

Convención de IDs: `[k|r]-[tema_id]-[NNN]` donde NNN es secuencial dentro del tema.

### 3.2 `00-Sistema/datos/declaraciones.json`

```jsonc
{
  "debates": [
    {
      "id": "debate-1",
      "fecha": "PENDIENTE-CONFIRMAR",
      "organizador": "PENDIENTE-CONFIRMAR",
      "formato": "cara-a-cara",
      "archivo_fuente": "02-Debates/raw/Debate 1.txt"
    },
    {
      "id": "debate-2",
      "fecha": "PENDIENTE-CONFIRMAR",
      "organizador": "PENDIENTE-CONFIRMAR",
      "formato": "equipos-tecnicos",
      "archivo_fuente": "02-Debates/raw/Debate 2.txt",
      "bloques": ["reforma-estado", "juventud-deporte", "agricultura-ambiente",
                  "infraestructura", "economia-empleo", "salud"]
    }
  ],
  "declaraciones": [
    {
      "id": "debate-1-keiko-001",
      "debate_id": "debate-1",
      "candidato": "keiko",                   // siempre keiko o roberto, también en equipos técnicos
      "vocero": null,                         // p.ej. "Luis Carranza" cuando habla equipo técnico
      "tema": "seguridad",
      "tipo": "compromiso",                   // propuesta | diagnóstico | ataque | defensa | cifra | compromiso | evasión
      "texto": "Resumen analítico (1-2 oraciones).",
      "cita_textual": "Cita verbatim del debate.",
      "contexto": "Pregunta del moderador o tema del bloque.",
      "fuente": { "archivo": "02-Debates/raw/Debate 1.txt", "linea_inicio": 234, "linea_fin": 248 },
      "timestamp": null                       // "[21:35]" para Debate 2, null para Debate 1
    }
  ]
}
```

**Justificación de `vocero`:** En el Debate 2 hablan voceros del equipo técnico en nombre del candidato. La declaración se atribuye al candidato (porque la posición es del partido y del candidato), pero registramos al vocero específico como atributo informativo.

### 3.3 `00-Sistema/datos/comparaciones.json`

```jsonc
{
  "plan_vs_plan": [
    {
      "id": "cmp-pp-seguridad-001",
      "tema": "seguridad",
      "dimension": "propuesta_principal",     // diagnostico | propuesta_principal | meta | enfoque_institucional
      "propuesta_keiko": "k-seguridad-001",   // ID de propuestas.json o null si SOLO_B
      "propuesta_roberto": "r-seguridad-007", // null si SOLO_A
      "relacion": "DIVERGE",                  // COINCIDE | AMPLÍA | DIVERGE | CONTRADICE | SOLO_A | SOLO_B
      "analisis": "2-3 oraciones explicando el contraste."
    }
  ],
  "plan_vs_debate": [
    {
      "id": "cmp-pd-keiko-001",
      "candidato": "keiko",
      "propuesta_id": "k-seguridad-001",       // null si NUEVO_DEBATE
      "declaracion_id": "debate-1-keiko-014",  // null si OMITE
      "relacion": "CONSISTENTE",               // CONSISTENTE | AMPLÍA_DEBATE | VAGUEA | CONTRADICE_DEBATE | OMITE | NUEVO_DEBATE
      "analisis": "Texto del análisis."
    }
  ],
  "consistencia_por_candidato": [
    {
      "candidato": "keiko",
      "tema": "seguridad",
      "n_propuestas_plan": 12,
      "n_declaraciones_debate": 7,
      "consistentes": 5,
      "amplia_debate": 1,
      "vaguea": 0,
      "contradice_debate": 1,
      "omite": 5,
      "nuevo_debate": 2,
      "indice_consistencia": 0.83,
      "notas": "Texto cualitativo opcional."
    }
  ]
}
```

**Fórmula del índice de consistencia:** `(consistentes + amplia_debate) / (consistentes + amplia_debate + vaguea + contradice_debate)`. Rango 0–1. No penaliza `omite` ni `nuevo_debate` en el denominador (son comportamientos distintos: silencio o expansión, no contradicción del discurso escrito).

## 4. Sub-proyectos

El trabajo se descompone en 4 sub-proyectos secuenciales. Cada uno tiene su propio plan de implementación y un checkpoint de revisión por parte de la usuaria al finalizar antes de pasar al siguiente.

### Sub-proyecto 1 — Extracción de propuestas
- **Input:** los 2 planes `.md`
- **Output:** `00-Sistema/datos/propuestas.json`
- **Trabajo:** recorrer cada plan, identificar propuestas/metas/diagnósticos/principios/100días, asignar tema único (el dominante según la taxonomía; si una propuesta toca varios, se elige el principal y los demás se mencionan en el campo `texto`), capturar cita textual + rango de líneas, asignar relevancia.
- **Verificación:** muestreo aleatorio de 10 propuestas por candidato; usuaria revisa que cita y fuente sean exactas.

### Sub-proyecto 2 — Procesamiento de debates
- **Input:** `Debate 1.txt`, `Debate 2.txt`
- **Output:** `00-Sistema/datos/declaraciones.json` + los `.md` por candidato/debate en `02-Debates/procesados/debate-{1,2}/{keiko,roberto}.md`
- **Trabajo:** identificar hablantes (en Debate 1 por contenido/turno; en Debate 2 con vocero del equipo técnico), clasificar por tema y tipo, generar reportes navegables por candidato.
- **Riesgo:** Debate 1 no trae etiquetas de hablante; hay que inferir por contexto. Usuaria revisa atribución antes de procesar Debate 2.

### Sub-proyecto 3 — Análisis comparativo
- **Input:** `propuestas.json` + `declaraciones.json`
- **Output:** `00-Sistema/datos/comparaciones.json`
- **Trabajo:**
  1. Para cada par (propuesta Keiko, propuesta Roberto) en el mismo tema, aplicar el árbol de decisión de la ontología (§MATRIZ DE ANÁLISIS RÁPIDO) y clasificar la relación.
  2. Para cada propuesta de plan, buscar declaración(es) del mismo candidato en debates en el mismo tema; clasificar relación.
  3. Agregar por candidato × tema: contar tipos de relación, calcular índice de consistencia.
- **Verificación:** usuaria revisa las contradicciones detectadas (`CONTRADICE` plan-vs-plan y `CONTRADICE_DEBATE`) antes de pasar a render.

### Sub-proyecto 4 — Render + dashboard + despliegue
- **Input:** los 3 JSON
- **Outputs:**
  - `03-Comparaciones/matriz-temas.md` (tabla maestra 29 temas)
  - `03-Comparaciones/coincidencias.md`
  - `03-Comparaciones/divergencias.md`
  - `03-Comparaciones/contradicciones.md` (plan-vs-plan + plan-vs-debate por candidato)
  - `03-Comparaciones/consistencia-discurso.md` (índices + análisis por tema y candidato)
  - `index.html` (renombrado desde `dashboard-comparacion.html`, ahora cargando JSON con `fetch()` + nueva pestaña "Reportes" con render de `.md` vía marked.js)
  - `vercel.json`, `README.md`, `.gitignore`
- **Verificación:** abrir el sitio desplegado en Vercel, revisar todos los temas con datos, ningún placeholder visible, los 5 reportes renderizan correctamente en la pestaña Reportes.

## 5. Despliegue

### 5.1 Estructura del repo

```
Seguimiento-Planes-de-Gobierno-Peru/
├── index.html                         ← renombrado desde dashboard-comparacion.html
├── vercel.json
├── README.md
├── .gitignore
├── 00-Sistema/
│   ├── CLAUDE.md
│   ├── ontologia.md
│   ├── specs/
│   │   └── 2026-06-09-capa-datos-comparacion-design.md
│   └── datos/
│       ├── propuestas.json
│       ├── declaraciones.json
│       └── comparaciones.json
├── 01-Planes-de-Gobierno/{Keiko-Fujimori,Roberto-Sanchez}/Plan-…md
├── 02-Debates/
│   ├── raw/Debate {1,2}.txt
│   └── procesados/debate-{1,2}/{keiko,roberto}.md
├── 03-Comparaciones/{matriz-temas,coincidencias,divergencias,contradicciones,consistencia-discurso}.md
├── 04-Implementacion/                 ← vacío hasta Etapa 2 (julio 2026)
├── Plan-de-Gobierno-Keiko.pdf         ← sube al repo
├── Plan-de-Gobierno-Roberto Sánchez.pdf
└── Brain OS Wiki.md
```

### 5.2 Carga de datos en el dashboard

Como Vercel sirve los archivos como sitio estático, se usa `fetch()`:

```js
const [propuestas, declaraciones, comparaciones] = await Promise.all([
  fetch('00-Sistema/datos/propuestas.json').then(r => r.json()),
  fetch('00-Sistema/datos/declaraciones.json').then(r => r.json()),
  fetch('00-Sistema/datos/comparaciones.json').then(r => r.json())
]);
```

### 5.3 Pestaña "Reportes" en el dashboard

Se añade una pestaña que muestra los 5 reportes de `03-Comparaciones/` renderizados en cliente. Se usa `marked.js` (~15KB minificado) cargado desde CDN. Esto cumple el requisito de que el sitio sea autocontenido sin necesidad de visitar GitHub.

### 5.4 `vercel.json`

```json
{
  "cleanUrls": true,
  "headers": [
    { "source": "/00-Sistema/datos/(.*).json",
      "headers": [{ "key": "Cache-Control", "value": "public, max-age=300" }] }
  ]
}
```

### 5.5 `README.md`

Descripción pública del proyecto, neutralidad explícita, cómo está organizado, cómo correr/desplegar, créditos y licencia.

## 6. Reglas del sistema heredadas (no negociables)

Estas reglas vienen del `CLAUDE.md` del vault y aplican a todo el trabajo:

1. **Neutralidad:** ningún output favorece a un candidato.
2. **Citas exactas:** toda afirmación se respalda con cita verbatim y referencia al archivo fuente con rango de líneas.
3. **Distinción propuesta/diagnóstico:** no confundir descripción del problema con propuesta de solución.
4. **Precisión terminológica:** usar siempre IDs de tema de la taxonomía; distinguir plan escrito vs. declaración en debate.
5. **Incertidumbre explícita:** "información insuficiente" antes que inferir.
6. **Leer solo `.md` para los planes** (PDFs son respaldo, no fuente de análisis).
7. **Todo en español.**

## 7. Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Volumen de propuestas (~200-400 por candidato): error o inconsistencia al extraer | Procesar tema por tema; checkpoint de muestreo aleatorio antes de continuar al siguiente sub-proyecto |
| Atribución de hablante en Debate 1 (sin etiquetas) | Procesar Debate 1 completo, usuaria revisa `keiko.md` resultante, ajustes antes de Debate 2 |
| Clasificación de relación (COINCIDE vs DIVERGE) es subjetiva | Aplicar el árbol de decisión de `ontologia.md` mecánicamente; documentar el razonamiento en el campo `analisis` |
| Cambios en propuestas implicarían regenerar todo el render | Diseño de single-source-of-truth lo hace barato (regenerar `.md` desde JSON es determinístico) |
| Datos faltantes en debates (fecha, organizador) | Usar placeholders explícitos `"PENDIENTE-CONFIRMAR"` que la usuaria llena luego, no inventar |

## 8. Lo que NO está en este spec (fuera de alcance)

- **Etapa 2** (seguimiento de implementación de gobierno): se activa cuando el ganador asume el 28-jul-2026. Está fuera de este trabajo.
- **Otros candidatos**: el sistema soporta solo Keiko y Roberto por ahora. Añadir otros candidatos requeriría un spec aparte.
- **Análisis automático de sentimiento o IA generativa para clasificación masiva**: las clasificaciones se hacen razonadamente con citas, no por algoritmo opaco.
- **Sitio multi-idioma**: solo español.
- **Edición colaborativa en el sitio desplegado**: el sitio es solo lectura; los cambios se hacen vía repo.

## 9. Próximo paso

Tras aprobación de este spec, se invoca `superpowers:writing-plans` para producir el plan de implementación del **Sub-proyecto 1 — Extracción de propuestas**. Los planes de los sub-proyectos 2, 3 y 4 se escriben uno a uno conforme se completa el anterior.
