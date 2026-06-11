# Seguimiento de Planes de Gobierno — Perú 2026

Análisis comparativo de los planes de gobierno presidenciales para la segunda vuelta peruana del 7 de junio de 2026, entre **Keiko Fujimori** (Fuerza Popular) y **Roberto Sánchez Palomino** (Juntos por el Perú), cruzado con sus declaraciones en los debates presidenciales.

> Sistema de análisis político de elaboración independiente. No tiene afiliación partidaria. Presenta evidencia textual de ambos candidatos clasificada con la misma metodología.

## Qué contiene

| | |
|---|---:|
| Propuestas extraídas de los planes escritos | **939** (Keiko 446 · Roberto 493) |
| Declaraciones en debates presidenciales | **172** (Debate 1: 89 · Debate 2: 83) |
| Comparaciones plan-vs-plan (Keiko ↔ Roberto) | **68** |
| Comparaciones plan-vs-debate por candidato | **181** |
| Temas cubiertos | **29** |
| Voceros identificados en Debate 2 (equipos técnicos) | **12** |

Toda propuesta y declaración está respaldada por una **cita textual verbatim** del plan o de la transcripción del debate, con la línea exacta en el archivo fuente.

## Cómo navegar el sitio

- **📊 Resumen** — cifras totales y distribución de relaciones.
- **📚 Temas** — explora cada uno de los 29 temas y compara las propuestas de ambos candidatos lado a lado.
- **⚖️ Plan vs Plan** — busca y filtra las comparaciones entre los planes (COINCIDE, DIVERGE, CONTRADICE, AMPLÍA, SOLO_B).
- **🎙️ Debates** — lee las declaraciones del debate filtradas por candidato y debate.
- **📈 Plan vs Debate** — índice de consistencia por candidato × tema.
- **📄 Reportes** — los 5 reportes generados (matriz, coincidencias, divergencias, contradicciones, consistencia).

## Arquitectura

Sigue el modelo *compiler* de Karpathy: fuentes brutas → JSON estructurados (única fuente de verdad) → vistas determinísticas.

```
01-Planes-de-Gobierno/        Planes en .md (fuente bruta)
02-Debates/raw/               Transcripciones de debates (.txt)
       │
       ▼  (extracción manual asistida — Python scripts)
00-Sistema/datos/
   ├── propuestas.json        Source of truth de propuestas
   ├── declaraciones.json     Source of truth de declaraciones
   └── comparaciones.json     Source of truth de relaciones
       │
       ▼  (render determinístico)
02-Debates/procesados/        .md por candidato y debate
03-Comparaciones/             5 reportes .md
index.html                    Dashboard interactivo
```

### Schemas validados

- `00-Sistema/datos/propuestas.schema.json`
- `00-Sistema/datos/declaraciones.schema.json`
- `00-Sistema/datos/comparaciones.schema.json`

Cada schema tiene su validador Python (`00-Sistema/scripts/validar_*.py`) que verifica estructura, unicidad de IDs, taxonomía y que cada cita verbatim aparezca en su rango de líneas exacto del archivo fuente.

### Scripts

Para regenerar todo desde cero:

```bash
# Validación
python 00-Sistema/scripts/validar_propuestas.py
python 00-Sistema/scripts/validar_declaraciones.py
python 00-Sistema/scripts/validar_comparaciones.py

# Renders
python 00-Sistema/scripts/render_debates.py        # .md por candidato/debate
python 00-Sistema/scripts/render_comparaciones.py  # 5 reportes en 03-Comparaciones/
```

Los scripts de extracción (uno por dimensión/pilar) están en `00-Sistema/scripts/extract_*.py` y son idempotentes.

## Desarrollo local

```bash
python -m http.server 8765
# Abrir http://127.0.0.1:8765/
```

El dashboard carga los 3 JSON con `fetch()` y los reportes `.md` con [marked.js](https://marked.js.org/). Funciona como sitio 100% estático.

## Despliegue en Vercel

El proyecto incluye `vercel.json` configurado para sitio estático con:

- Headers `Cache-Control` cortos (5 min) en JSON y MD para que cambios se propaguen rápido sin sobrecargar el CDN.
- Headers de seguridad básicos (`X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`).

Desde la raíz del repo:

```bash
vercel
```

O conectando el repositorio en el dashboard de Vercel.

## Metodología

- **Neutralidad**: ninguna sección favorece a un candidato. Los textos analíticos son redacción propia que resume; las **citas verbatim entre comillas** son la evidencia.
- **Citas exactas**: toda afirmación atribuida a un candidato tiene su cita textual y línea exacta del archivo fuente.
- **Distinción propuesta/diagnóstico**: no se confunde la descripción del problema con la propuesta de solución.
- **Taxonomía de 29 temas** comunes para clasificar todo el material.
- **Relaciones tipificadas**:
  - Plan-vs-plan: `COINCIDE`, `AMPLÍA`, `DIVERGE`, `CONTRADICE`, `SOLO_A`, `SOLO_B`.
  - Plan-vs-debate: `CONSISTENTE`, `AMPLÍA_DEBATE`, `VAGUEA`, `CONTRADICE_DEBATE`, `OMITE`, `NUEVO_DEBATE`.

Ver `00-Sistema/ontologia.md` para el árbol de decisión completo.

## Limitaciones conocidas

1. **Fechas y organizadores de los debates** quedan como `PENDIENTE-CONFIRMAR` en `declaraciones.json` por no estar incluidos en los archivos fuente proporcionados.
2. **Atribución del Debate 1** (cara-a-cara): la transcripción no traía etiquetas de hablante; la segmentación se hizo por las introducciones del moderador y por contenido.
3. **Tema `orden_juridico` en Roberto**: 16 entradas (secciones 3.6-3.7 de su plan) se clasificaron bajo este tema aunque el `CLAUDE.md` del sistema lo marca como exclusivo de Keiko. Decisión editorial documentada en los commits correspondientes.
4. **Índice de consistencia plan-debate**: en este primer pase todos los índices resultan 1.00 porque no se identificaron VAGUEA ni CONTRADICE_DEBATE. Eso refleja que en debate los candidatos sostuvieron sus planes; una segunda lectura crítica podría detectar matices de VAGUEA.
5. **Versionado de `marked.js`**: se carga desde CDN pineado a `v12.0.2` con `crossorigin="anonymous"` pero **sin atributo `integrity`** (SRI). Para producción endurecer agregando `integrity="sha384-..."` o auto-hospedando el script.

## Licencia y créditos

Material extraído de los planes públicos:

- *Perú con Orden 2026-2031* — Fuerza Popular (Keiko Fujimori).
- *Programa de Gobierno de Segunda Vuelta — Juntos por el Perú* (Roberto Sánchez Palomino).

Transcripciones de debates presidenciales televisados.

Análisis y código: elaboración propia. Disponible para uso académico y periodístico citando la fuente.
