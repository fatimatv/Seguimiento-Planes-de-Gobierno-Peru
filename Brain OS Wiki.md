# Brain OS — Manual de arquitectura para un sistema personal de conocimiento operativo con IA

## Guía completa para construir un ecosistema donde Claude (u otro modelo) funcione como colaborador operativo

**Versión:** 1.2 genérica — 2026
**Propósito:** Este documento es el punto de partida para que cualquier persona construya su propio sistema de inteligencia operativa personal. Es un manual maestro que describe arquitectura, identidad del asistente, memoria, herramientas y flujos de trabajo. Puede entregarse directamente a Claude (vía `claude.md`, sistema RAG o contexto inicial) para que entienda el sistema.

**Sobre el nombre:** El documento usa "Brain OS" como nombre genérico del sistema. En la práctica cada persona le pone un nombre propio — por ejemplo `[TuInicial]-Brain`, `SegundoCerebro`, `OS-Personal`, etc. Reemplazá "Brain OS" por el nombre que prefieras al implementarlo.

**Cambios en esta versión:**
- Correo del asistente redefinido como canal de ingesta pasiva (no de envío).
- Slack redefinido como bitácora de acciones por tipo, no comunicación conversacional.
- Vector DB (Pinecone) adelantado a Fase 1 para corpus de referencia.
- Nueva sección: mantenimiento del sistema y rutinas periódicas por capa.
- Actualización de stack de herramientas y flujos consecuentes.

---

# PARTE 1 — PERFIL DEL USUARIO Y CÓMO TRABAJA

## 1.1 ¿Para quién es este manual?

Este manual sirve a cualquier persona que cumpla al menos tres de estas características:

- **Trabaja por proyectos o clientes múltiples** en paralelo (consultores, freelancers, abogados independientes, directores de proyectos, académicos con múltiples líneas de investigación, creadores de contenido con varios formatos).
- **Genera y recibe documentación viva**: transcripciones, propuestas, actas, correos, contratos que se actualizan constantemente.
- **Acumula conocimiento de referencia** que necesita accesible pero no cambia mucho (papers, frameworks, regulación, bibliografía, materiales de curso).
- **Opera desde múltiples dispositivos** y necesita continuidad entre computadora, teléfono y trabajo delegado.
- **Prefiere outputs sobre conversaciones**: no quiere texto para copiar, quiere archivos listos, correos redactados, informes generados.

Si tu trabajo se puede describir como "manejo volumen alto de información sobre proyectos específicos y produzco entregables", este manual es para vos.

## 1.2 Principios operativos que asume el sistema

Brain OS está diseñado bajo cinco principios. Si no coincidís con alguno, ajustá el sistema antes de implementarlo:

1. **Trabajo estructurado por proyectos con ciclo de vida definido.** Cada proyecto tiene propuesta → contrato → ejecución → entregables → facturación → cierre. Algo parecido aplica aunque no factures (proyectos académicos, personales, etc.).
2. **Información viva separada de información estática.** Lo que cambia (conversaciones, estados) vive en bitácoras cronológicas. Lo que no cambia (contratos firmados, papers de referencia) vive en carpetas de insumos o biblioteca.
3. **Claude escribe, vos revisás.** El asistente mantiene el vault. Vos rara vez editás archivos directamente.
4. **Outcomes sobre chat.** El sistema produce archivos listos, no respuestas para copiar.
5. **Memoria persistente.** El sistema recuerda correcciones, preferencias, decisiones. No tenés que repetir nada.

## 1.3 Estilo de comunicación recomendado para interactuar con el sistema

- Directo y sin relleno.
- Listas cuando hay múltiples items; prosa cuando es análisis.
- Un idioma principal (español o inglés) para documentación; técnica en inglés si conviene.
- Contexto antes de recomendaciones.
- No repetir información que ya está en el vault.

---

# PARTE 2 — ARQUITECTURA DEL SISTEMA

## 2.1 Filosofía base (modelo compilador de Andrej Karpathy)

El sistema sigue el modelo compilador descrito por Karpathy para bases de conocimiento con LLMs:

```
raw/ (fuentes brutas)
  → Compiler (LLM procesa y estructura)
    → wiki/ (conocimiento compilado, navegable)
      → runtime (Claude consulta y actúa)
        → outputs/ (archivos listos, no respuestas de chat)
```

**Principio central:** Claude escribe y mantiene la base de conocimiento. El usuario rara vez toca los archivos directamente. El sistema mejora solo con cada sesión de trabajo.

**Principio operativo clave:** El compiler no es un script que ejecutes ni una pieza que toques manualmente. Compilar significa simplemente decirle a Claude "procesá esto". Claude es el compilador — lee lo que hay en `raw/`, lo destila, y actualiza la wiki.

## 2.2 Las cuatro capas funcionales

### Capa A — Ingesta bruta (`raw/`)

Todo lo que entra al sistema sin procesar vive temporalmente en `raw/`. Hay **cuatro mecanismos de ingesta** según la fuente:

#### Mecanismo 1 — Arrastre manual a carpeta (lo más simple)

El usuario crea subcarpetas dentro de `raw/` por proyecto y copia archivos físicos ahí: PDFs recibidos, contratos, transcripciones locales, documentos de Word. Eso es todo de su parte.

El proceso de compilación se dispara cuando el usuario le dice a Claude (vía Cowork o chat): "procesá los archivos nuevos en `raw/[Cliente]/`". Claude los lee, extrae lo importante, y actualiza `log.md` y `overview.md` del proyecto. El archivo original queda en `raw/` como respaldo, y el conocimiento destilado queda en la wiki.

```
Usuario copia →  raw/Acme-Corp/contrato-servicios.pdf
                 raw/Acme-Corp/transcripcion-reunion-10abr.txt

Claude procesa → actualiza 02-Proyectos/Acme-Corp/log.md
                 actualiza 02-Proyectos/Acme-Corp/overview.md
                 mueve procesados a raw/Acme-Corp/procesados/
```

#### Mecanismo 2 — Conectores MCP jalan la info directamente

Para Gmail y Google Drive no se copia nada. Claude, con los conectores activos, va directamente a buscar la información en el momento que se le pide. Cuando el usuario dice "revisá el correo de Acme Corp y actualizá el log", Claude:

1. Busca en Gmail los correos con etiqueta del cliente (o del dominio).
2. Los lee en ese momento.
3. Escribe las entradas relevantes en `log.md`.

No hay archivos intermedios. La información viaja directo de Gmail al vault. Esto es lo que automatiza el skill `onboard-project` — ejecuta exactamente este flujo para un cliente completo.

#### Mecanismo 3 — Obsidian Web Clipper (para la biblioteca)

Para artículos, papers y referencias de internet, se usa la extensión Obsidian Web Clipper en Chrome. Cuando el usuario encuentra algo que quiere guardar, presiona el botón y el artículo va directamente a `raw/biblioteca/` como archivo Markdown, con texto limpio y sin ads.

Después el skill `library-compiler` lo procesa: crea un artículo de wiki temático, lo conecta con proyectos relevantes, y lo agrega al índice de la biblioteca. Si el corpus de biblioteca ya supera la ventana de contexto de Claude, el skill lo ingesta directamente a Pinecone en lugar de a Obsidian.

#### Mecanismo 4 — Correo del asistente como canal de ingesta pasiva *(nuevo en v1.2)*

Este es el mecanismo más automatizado y menos obvio del sistema. El asistente tiene una dirección de correo propia (`asistente@[tu-dominio].com`). Esta cuenta **no envía correos** — solo recibe. Su propósito es actuar como bandeja de ingesta pasiva de cosas que llegan solas:

- **Transcripciones de reuniones:** Cuando el usuario crea un evento en Google Meet, agrega la cuenta del asistente como participante. Al terminar la reunión, la transcripción automática llega al correo del asistente. El usuario puede entonces decirle a Claude: "revisá la transcripción que acaba de llegar, procesala al log del proyecto y archivá el original".
- **Confirmaciones automáticas de servicios:** Correos de confirmación de herramientas, plataformas, o servicios que Claude debe registrar.
- **Documentos enviados por terceros:** Cuando un colega o cliente envía algo específicamente para que Claude lo procese.

**Flujo tipo para transcripciones de Meet:**

```
1. Usuario crea evento en Google Meet
2. Agrega asistente@[dominio].com como participante
3. Reunión ocurre — transcripción se genera automáticamente
4. Transcripción llega al correo del asistente
5. Usuario dice a Claude: "procesá la transcripción de la reunión de hoy"
6. Claude lee el correo, extrae la transcripción
7. Destila al log.md del proyecto correspondiente
8. Actualiza overview.md si hay cambios de estado
9. Archiva el correo original
10. Reporta en Slack: "Transcripción Meet [fecha] procesada. Proyecto: [X]. Acuerdos registrados: [N]."
```

**Regla de oro del correo del asistente:** Solo recibe, nunca envía. Todo envío de correo a terceros requiere aprobación explícita del usuario.

#### Cuadro resumen — por dónde entra cada cosa

| Fuente | Cómo entra | Quién compila |
|--------|------------|---------------|
| PDF/docs recibidos | Usuario los copia a `raw/[proyecto]/` | Claude cuando se le indica |
| Correos Gmail (usuario) | MCP los jala directo | Claude automático o a pedido |
| Drive del cliente | MCP los jala directo | Claude automático o a pedido |
| Transcripciones locales | Usuario las copia a `raw/[proyecto]/` | Claude cuando se le indica |
| Artículos web | Web Clipper → `raw/biblioteca/` | Skill `library-compiler` |
| Transcripciones Meet | Auto → correo asistente → MCP | Skill `meet-processor` a pedido |
| Docs de referencia (PDFs, libros) | Usuario los copia a `raw/biblioteca/` o `raw/vector-inbox/` | Skill `vector-ingest` → Pinecone |
| Sesiones de trabajo | Hooks automáticos (Fase 2) | Flush diario automático |

**Regla de oro de la ingesta:** Para empezar, todo lo físico (PDFs, docs) va arrastrado a `raw/[proyecto]/`. Todo lo que está en Gmail y Drive, Claude lo jala con MCP cuando se le pide procesar un proyecto. El compiler no se toca manualmente — es decirle a Claude "procesá esto".

### Capa B — Compilador (LLM procesa `raw/` → wiki o vector DB)

Skills que transforman información bruta en conocimiento estructurado:

- **Skill: `onboard-project`** — Lee Gmail + Drive de un cliente, crea `overview.md` y `log.md`, clasifica documentos entre estáticos (contratos, propuestas firmadas) y dinámicos (conversaciones, avances).
- **Skill: `raw-processor`** — Procesa archivos físicos depositados en `raw/[proyecto]/`, clasifica entre estáticos y dinámicos, destila al log y mueve el original a `raw/[proyecto]/procesados/`.
- **Skill: `meet-processor`** — Lee el correo del asistente, detecta transcripciones nuevas de Google Meet, identifica el proyecto, destila al log y archiva.
- **Skill: `vector-ingest`** — Toma documentos de `raw/vector-inbox/` (PDFs, libros, transcripciones históricas, entregables finales), los fragmenta y los ingesta a Pinecone con metadatos de proyecto/tipo/fecha.
- **Skill: `daily-flush`** — Toma logs de sesiones del día, extrae decisiones y lecciones, actualiza la wiki. Se ejecuta automáticamente.
- **Skill: `library-compiler`** — Procesa artículos capturados con Web Clipper, crea artículos de wiki temáticos, conecta papers con proyectos activos. Deriva a `vector-ingest` si el documento es largo o de solo referencia.

### Capa C — Vault (Obsidian + GitHub + Pinecone)

El almacenamiento estructurado tiene ahora **dos repositorios complementarios**:

**Obsidian (para lo que cambia y tiene estructura):** Todo en Markdown. Todo versionado.

```
Brain-OS/ (vault raíz)
├── 00-Sistema/
│   ├── claude.md              ← cerebro dentro del cerebro
│   ├── index.md               ← mapa de navegación del vault
│   ├── projects.base          ← dashboard de estado de todos los proyectos
│   ├── memory.md              ← preferencias y correcciones aprendidas
│   ├── skills/                ← archivos .skill de Cowork
│   └── prompts-maestros/      ← prompts reutilizables por flujo
│
├── 01-Biblioteca/
│   ├── frameworks/            ← frameworks, metodologías de referencia
│   ├── papers/                ← investigaciones, estudios referenciados (resúmenes)
│   ├── regulacion/            ← marco regulatorio relevante al dominio
│   ├── cursos/                ← materiales de referencia para enseñanza
│   └── index-tematico.md      ← mapa de toda la biblioteca
│
├── 02-Proyectos/
│   ├── Acme-Corp/             ← ejemplo: cliente corporativo
│   ├── Beta-Industries/       ← ejemplo: cliente industrial
│   ├── Gamma-Municipal/       ← ejemplo: cliente público
│   └── [Cliente]/             ← ver estructura detallada en sección 2.3
│
├── 03-Daily-logs/
│   ├── 2026-04-12.md          ← log auto-generado por hooks de Claude Code
│   └── ...
│
├── 04-Inbox-Claude/
│   └── sin-proyecto/          ← items que Claude recibe sin proyecto asignado
│
└── raw/                       ← Capa A — zona de ingesta bruta
    ├── Acme-Corp/
    │   ├── procesados/        ← archivos ya destilados al vault
    │   └── [archivos nuevos sin procesar]
    ├── Beta-Industries/
    ├── biblioteca/            ← destino del Web Clipper
    │   └── procesados/
    ├── vector-inbox/          ← PDFs y documentos que van directo a Pinecone
    │   └── procesados/
    └── [otros-proyectos]/
```

**Pinecone (para lo que no cambia y solo se consulta):**

La regla de separación es clara:
- **Obsidian:** todo lo que tiene ciclo de vida activo, necesita edición o navegación estructural (proyectos, notas de reuniones, borradores, daily logs).
- **Pinecone:** todo lo que es corpus de referencia, ya está "terminado", y solo se necesita recuperar por búsqueda semántica.

Qué va a Pinecone desde el primer día:
- Papers y regulación (PDFs completos)
- Libros y capítulos de referencia
- Transcripciones históricas del podcast y escritos publicados
- Entregables finales aprobados (propuestas, informes, análisis)
- Materiales de curso completos

Metadatos obligatorios en cada vector:
```json
{
  "tipo": "paper | regulacion | libro | transcripcion | entregable | curso",
  "proyecto": "[cliente o 'biblioteca']",
  "fecha": "YYYY-MM-DD",
  "titulo": "[nombre del documento]",
  "fuente": "[URL o ruta en raw/procesados/]"
}
```

### Capa D — Runtime (Query + Acción)

Donde el usuario interactúa con el sistema:
- **Claude Cowork** — para tareas que producen archivos, trabajo por proyecto, scheduled tasks.
- **Claude.ai + MCP** — para consultas diarias, acceso a Gmail/Drive/Calendar.
- **Claude Code** — para automatización avanzada, hooks, flush automático (Fase 2).
- **Dispatch (móvil)** — para delegar tareas desde el teléfono mientras Cowork tiene acceso al vault local.

Cuando Claude responde a una consulta que involucra conocimiento de referencia, puede combinar Obsidian (para estado actual del proyecto) y Pinecone (para contexto de biblioteca) en la misma respuesta.

## 2.3 Estructura interna de cada proyecto

Cada carpeta de cliente/proyecto sigue esta anatomía:

```
02-Proyectos/[Cliente]/
├── overview.md          ← perfil del cliente, alcance, contactos clave, estado actual
├── log.md               ← bitácora cronológica: reuniones, decisiones, acuerdos
├── insumos/             ← lo que el cliente entregó (briefs, contratos recibidos, specs)
├── entregables/         ← lo que el usuario produce y entrega (propuestas, informes)
├── financiero/          ← control de facturas, pagos, hitos económicos
└── outputs-ai/          ← drafts y análisis generados por Claude (con estado)
```

Y en paralelo, su zona de ingesta:
```
raw/[Cliente]/
├── procesados/          ← lo que ya fue compilado al vault
└── [archivos pendientes de procesar]
```

### Anatomía de `overview.md`

```yaml
---
cliente: [Nombre del cliente]
entidad-legal: [Razón social si aplica]
estado: activo | pausado | cerrado
inicio: YYYY-MM-DD
contacto-principal: [Nombre y correo]
tags: [consultoría, estrategia, etc.]
---

## Perfil
[Quién es el cliente, su industria, tamaño]

## Alcance del proyecto
[Qué se acordó hacer]

## Contactos clave
| Nombre | Rol | Correo |
|--------|-----|--------|

## Estado actual
[Párrafo de estado al momento de la última actualización]

## Hitos y fechas críticas
- [ ] Fecha: entregable
```

### Anatomía de `log.md`

```markdown
## 2026-04-12 — Reunión de kickoff
**Presentes:** [Usuario], [contacto del cliente]
**Acuerdos:** [lista]
**Pendientes:** [lista]
**Próxima acción:** [qué hace el usuario]

## 2026-03-28 — Envío de propuesta v2
**Entregable:** nombre-archivo.pdf
**Estado:** pendiente de feedback
**Notas:** [contexto relevante]
```

### Estado de `outputs-ai/`

Cada archivo en `outputs-ai/` debe tener en su frontmatter:
```yaml
estado: borrador | enviado | aprobado | archivado
fecha: YYYY-MM-DD
tipo: correo | propuesta | informe | análisis | draft
```

---

# PARTE 3 — IDENTIDAD DE CLAUDE EN ESTE SISTEMA

## 3.1 Qué es Claude en este ecosistema

Claude no es un chatbot en este sistema. Es un **colaborador con infraestructura propia** — tiene acceso a cuentas, carpetas y herramientas como un empleado digital. La configuración recomendada incluye:

- **Correo propio:** `asistente@[dominio-del-usuario].com` — **solo recibe**, nunca envía por iniciativa propia. Es un canal de ingesta pasiva para transcripciones de Meet, documentos enviados por terceros, y confirmaciones automáticas.
- **Google Drive de trabajo:** Shared drives del usuario a los que Claude tiene acceso MCP. El usuario tiene además sus propios drives de respaldo personales que Claude no toca.
- **Slack por canales de acción:** Canal separado por tipo de acción para log de trabajo (ver sección 3.4).
- **Carpeta local asignada:** `/Brain-OS/` en la computadora del usuario — Cowork opera aquí.
- **GitHub conectado:** acceso al repositorio del vault para ver versiones y cambios.
- **Obsidian conectado:** lee y escribe en el vault vía CLI habilitado.
- **Pinecone:** Claude consulta y ingesta via API para corpus de referencia.

**Separación de drives:** El usuario mantiene drives de respaldo personal propios. Claude opera sobre los shared drives de trabajo. Esta separación es intencional — los drives personales del usuario son su territorio, no del sistema.

## 3.2 Reglas de identidad de Claude en este sistema

1. **Claude escribe el vault, el usuario lo revisa.** El usuario no edita archivos directamente salvo casos puntuales.
2. **Claude entrega archivos, no respuestas de chat.** Cuando produce algo, lo guarda en la carpeta correcta con nombre descriptivo y fecha.
3. **Claude pregunta antes de borrar, sobreescribir o renombrar.** Muestra qué cambiará y espera confirmación.
4. **Claude aprende de cada corrección.** Si el usuario modifica un output, Claude detecta qué cambió y actualiza `memory.md` con esa preferencia.
5. **Claude mantiene el índice actualizado.** Cada vez que crea o mueve un archivo, actualiza `index.md`.
6. **Claude usa estado en cada output.** Ningún archivo de `outputs-ai/` existe sin un campo `estado:` en el frontmatter.
7. **Claude mueve los archivos de `raw/` a `raw/[proyecto]/procesados/` después de destilarlos.** No duplica ni deja rastros ambiguos.
8. **Claude reporta en Slack al terminar cualquier tarea de procesamiento.** El canal recibe la notificación correspondiente según el tipo de acción (ver sección 3.4).

## 3.3 El archivo `claude.md` — cerebro dentro del cerebro

Este archivo vive en `00-Sistema/claude.md` y es lo primero que Claude lee al iniciar cualquier sesión. Contiene:

```markdown
# Claude en Brain OS — Instrucciones maestras

## Quién soy en este sistema
Soy el colaborador digital del usuario. Tengo acceso completo
al vault Brain OS, a las cuentas conectadas, y opero con autonomía delegada.

## Proyectos activos (actualizado: YYYY-MM-DD)
- [Cliente A]: [fase] — [pendiente clave] — contacto: [nombre]
- [Cliente B]: [fase] — [pendiente clave]
- [Proyecto interno]: [fase] — [próxima fecha]

## Cómo trabajo con el usuario
- Entrego archivos, no texto de chat
- Pregunto antes de borrar o sobreescribir
- Uso [idioma principal] en toda documentación de proyecto
- Prefiero síntesis ejecutiva + detalle bajo demanda
- Nunca repito información que ya está en el vault
- Al terminar cualquier tarea de procesamiento, reporto en el canal Slack correcto

## Mis herramientas disponibles
- Gmail MCP (cuenta del usuario): leer correos por etiqueta de proyecto
- Gmail MCP (asistente): leer correo pasivo — transcripciones Meet, docs recibidos
- Google Drive MCP (shared drives de trabajo): acceso a carpetas de clientes
- Google Calendar MCP: leer agenda, crear eventos con aprobación
- Obsidian CLI: leer y escribir markdown en el vault
- GitHub: ver historial de cambios del vault
- Pinecone: ingestar y consultar corpus de referencia
- Slack (por canal): reportar acciones completadas

## Drives y acceso
- Shared drives de trabajo: accedo vía MCP para proyectos
- Drives personales del usuario: no accedo salvo instrucción explícita

## Qué va a Obsidian vs Pinecone
- Obsidian: todo lo que tiene ciclo de vida activo (proyectos, logs, borradores, daily logs)
- Pinecone: corpus de referencia (papers, regulación, libros, transcripciones históricas, entregables finales)

## Cómo ingesta información al sistema
- Archivos físicos (PDFs, docs): usuario los deposita en `raw/[proyecto]/`, yo proceso cuando se me indica
- Correos del usuario: jalo vía MCP cuando se me indica
- Drive: jalo vía MCP cuando se me indica
- Artículos web: llegan por Web Clipper a `raw/biblioteca/`
- Transcripciones Meet: llegan a correo del asistente, proceso con skill `meet-processor`
- Corpus de referencia: usuario deposita en `raw/vector-inbox/`, yo ingesto a Pinecone con skill `vector-ingest`

Mi trabajo al procesar `raw/`:
1. Leer cada archivo nuevo
2. Clasificar: activo (destilar a log/vault) vs referencia (ingestar a Pinecone)
3. Actualizar `overview.md` si hay cambios de estado
4. Mover originales a `raw/[proyecto]/procesados/`
5. Reportar en Slack y en chat qué procesé y qué pendientes detecté

## Convenciones de nombres de archivo
- Proyectos: kebab-case, ej: propuesta-estrategia-v2.md
- Logs: YYYY-MM-DD-descripcion.md
- Entregables: cliente-tipo-descripcion-vN.extension

## Estado de aprendizaje
[Claude actualiza esta sección con preferencias aprendidas del usuario]
- [Ejemplo: El usuario prefiere resúmenes ejecutivos de máximo 3 párrafos]
- [Ejemplo: En correos formales, siempre incluir línea de siguiente paso]
```

## 3.4 Slack como bitácora de acciones *(nuevo en v1.2)*

Slack en Brain OS no es para conversación. Es el **log de trabajo de Claude** — un registro estructurado de qué hizo, qué movió y qué cambió. El usuario lo consulta como bitácora, no como chat.

### Estructura de canales por tipo de acción

| Canal | Qué reporta Claude ahí |
|-------|------------------------|
| `#brain-archivos` | Cada vez que crea, mueve, renombra o archiva un documento |
| `#brain-procesados` | Cuando termina de procesar `raw/` (proyecto o biblioteca) |
| `#brain-transcripciones` | Cuando procesa una transcripción de Meet o llamada |
| `#brain-alertas` | Pendientes detectados, conflictos, cosas que requieren atención del usuario |
| `#brain-daily` | Brief del día (mañana) y flush de cierre (tarde) |

### Formato estándar de notificación

```
[ACCIÓN] [Proyecto/Área] — [descripción breve]
Archivos: [lista si aplica]
Pendientes detectados: [si los hay]
```

Ejemplo real:
```
[PROCESADO] Acme-Corp — Transcripción Meet 14-abr procesada
Archivos: log.md actualizado (3 entradas), overview.md estado actualizado
Pendientes detectados: Envío de propuesta v3 acordado para 18-abr
```

**Lo que Claude nunca hace en Slack:** iniciar conversación, preguntar algo que puede resolver leyendo el vault, enviar el mismo reporte a múltiples canales, mandar notificaciones de acciones menores (autocorrecciones, reformateos internos).

---

# PARTE 4 — SISTEMA RAG Y MEMORIA LONG-TERM

## 4.1 Arquitectura de memoria — dos capas según tipo de documento

El sistema usa **dos mecanismos de recuperación** dependiendo de qué tipo de información necesitás:

### Índices de texto en Obsidian (para lo que cambia)

Claude navega por índices de texto plano que él mismo mantiene. Funciona bien para todo el trabajo activo — proyectos, logs, notas, borradores.

```
00-Sistema/index.md                ← mapa completo del vault (Claude lo mantiene)
01-Biblioteca/index-tematico.md    ← índice de toda la biblioteca por tema
02-Proyectos/[cliente]/overview.md ← punto de entrada por proyecto
03-Daily-logs/index-logs.md        ← índice de logs por fecha y tema
```

Cuando Claude recibe una consulta sobre un proyecto, lee primero `index.md`, identifica qué secciones son relevantes, y va directo a los archivos correspondientes.

### Pinecone (para el corpus de referencia) *(adelantado a Fase 1 en v1.2)*

Pinecone entra desde el día uno para todo el corpus de referencia — no porque el vault de proyectos lo necesite ahora, sino porque los documentos de biblioteca lo superan rápidamente.

**Regla de asignación (no negociable):**
- ¿El documento cambia, necesita edición, o tiene ciclo de vida activo? → **Obsidian**
- ¿El documento ya está terminado y solo lo vas a consultar semánticamente? → **Pinecone**

**Qué va a Pinecone desde el Día 1:**
- Papers de investigación (PDFs completos)
- Regulación, marcos legales
- Libros y capítulos de referencia
- Transcripciones históricas del podcast
- Escritos y artículos publicados (archivo completo)
- Entregables finales aprobados (propuestas, informes, análisis entregados)
- Materiales de curso completos (versiones finales)

**Por qué Pinecone y no LanceDB:** Pinecone cloud es accesible desde cualquier dispositivo, incluyendo Dispatch desde el móvil. LanceDB local estaría atado a una máquina. Si el sistema necesita funcionar de forma distribuida, Pinecone es la elección correcta desde el inicio.

## 4.2 Memoria de corto plazo — Daily logs

Inspirado en el sistema de hooks de Claude Code:

Cada sesión de trabajo genera un log en `03-Daily-logs/YYYY-MM-DD.md`:

```markdown
# Log 2026-04-12

## Sesión 1 — 09:30-10:15
**Proyecto:** Acme Corp
**Tarea:** Revisión de gaps en propuesta v2
**Decisiones:** Se prioriza [decisión] antes que [otra opción]
**Pendientes:** Enviar análisis comparativo antes del viernes
**Aprendizajes:** El cliente tiene resistencia interna en [área] — considerar en propuesta

## Sesión 2 — 14:00-15:30
**Proyecto:** Beta Industries
**Tarea:** Agenda de reunión estratégica
**Decisiones:** Estructura acordada: [formato del encuentro]
**Pendientes:** Invitaciones individuales a [stakeholders]
```

## 4.3 Memoria de largo plazo — Daily flush

Una vez al día (automático en Fase 2, manual en Fase 1), Claude toma los daily logs y los "promueve" a la wiki:

- Extrae decisiones importantes → actualiza `overview.md` del proyecto correspondiente.
- Extrae lecciones aprendidas → agrega a sección de aprendizajes en `00-Sistema/memory.md`.
- Identifica conexiones entre proyectos → crea o actualiza backlinks en Obsidian.
- Detecta items sin proyecto asignado → los mueve a `04-Inbox-Claude/`.

## 4.4 El loop compuesto (self-improving)

```
Sesión de trabajo
  → daily log capturado
    → flush diario
      → wiki crece y se refina
        → índices mejoran
          → próxima consulta es más rápida y precisa
            → Claude aprende preferencias del usuario
              → outputs mejoran solos
                → el usuario da menos instrucciones por sesión
```

---

# PARTE 5 — HERRAMIENTAS Y CONECTORES

## 5.1 Stack completo del sistema

| Herramienta | Rol | Capa | Fase |
|-------------|-----|------|------|
| Obsidian | IDE del vault, visualización | C | 1 |
| GitHub (privado) | Version control, backup gratuito | C | 1 |
| Plugin Git (Obsidian) | Auto-sync cada 1 min | C | 1 |
| Obsidian Web Clipper | Captura de artículos web a `raw/biblioteca/` | A | 1 |
| Claude.ai + MCP | Chat diario, consultas, connectors | D | 1 |
| Gmail MCP (cuenta usuario) | Lectura de correos por proyecto | A, D | 1 |
| Gmail MCP (cuenta asistente) | Ingesta pasiva: Meet, docs recibidos | A | 1 |
| Drive MCP (shared drives trabajo) | Acceso a docs de clientes | A, D | 1 |
| Calendar MCP | Agenda, eventos, scheduling | D | 1 |
| Pinecone | Vector search para corpus de referencia | C | 1 |
| Claude Cowork | Agente local, archivos, skills | D | 1-2 |
| Dispatch (móvil) | Tareas remotas vía Cowork | D | 2 |
| Claude Code | Hooks, automatización, flush | B | 2 |
| Slack (por canal) | Bitácora de acciones de Claude | D | 1 |
| Obsidian CLI | Cowork opera el vault | C | 2 |

## 5.2 Configuración de acceso de Claude

### Gmail — dos cuentas con propósitos distintos

**Cuenta del usuario:** Claude la conecta vía MCP para leer correos de proyectos. Permisos: read-only al inicio.

**Cuenta del asistente (`asistente@[dominio].com`):** Canal de ingesta pasiva. Claude la monitorea para procesar lo que llega. Nunca envía. Permisos: read + archive (para mover procesados a archivo).

### Google Drive — shared drives vs drives personales

Claude accede a los **shared drives de trabajo** del usuario vía MCP. Los drives personales del usuario son territorio propio — Claude no los toca salvo instrucción explícita. Esta separación es por diseño: mantiene una frontera clara entre el sistema operativo de trabajo y la vida personal del usuario.

Estructura recomendada:
- `[Nombre]-Work-Drive/` (shared con Claude, para proyectos activos)
- `[Nombre]-Personal-Drive/` (solo del usuario, respaldos personales)

### Slack — canales de bitácora

Crear en el workspace los cinco canales listados en sección 3.4 (`#brain-archivos`, `#brain-procesados`, `#brain-transcripciones`, `#brain-alertas`, `#brain-daily`). Claude conecta vía Slack MCP en Cowork.

### Pinecone

- Crear cuenta en pinecone.io (plan Starter es suficiente para empezar).
- Crear un índice: nombre `brain-os`, dimensiones según el modelo de embedding a usar (1536 para text-embedding-3-small de OpenAI, o 768 para otros).
- Guardar API key en variables de entorno del sistema (nunca en el vault).
- Claude ingesta via el skill `vector-ingest` usando la API de Pinecone.

### GitHub
- **Repositorio:** `github.com/[usuario]/brain-os` (privado).
- **Sync:** Automático vía plugin Git de Obsidian (cada 1 minuto).
- **Acceso Claude Code:** Configurar en Fase 2 para hooks de sesión.

### Obsidian CLI
- **Activación:** Settings → General → Advanced → Command Line Interface: ON.
- **Propósito:** Claude Code y Cowork pueden leer/escribir el vault programáticamente.

### Obsidian Web Clipper
- **Instalación:** Extensión de Chrome oficial de Obsidian.
- **Configuración:**
  - Default vault: Brain OS.
  - Default folder: `raw/biblioteca/`.
  - Template: artículo con texto limpio, autor, fuente, fecha de captura.
- **Uso:** Botón de extensión en cualquier página web → se guarda como Markdown en el vault.
- **Regla:** El usuario solo captura. Claude procesa vía skill `library-compiler` cuando se le indica.

---

# PARTE 6 — SKILLS Y FLUJOS DE TRABAJO

## 6.1 Skills prioritarios (crear en este orden)

### Skill 1: `onboard-project`
**Trigger:** "Onboardá el proyecto [Cliente]"
**Flujo:**
1. Lee Gmail con etiqueta del cliente (últimos 90 días).
2. Lee carpeta del cliente en Drive.
3. Crea estructura en `02-Proyectos/[Cliente]/` (y `raw/[Cliente]/`).
4. Genera `overview.md` con perfil, alcance, contactos.
5. Genera `log.md` con cronología de conversaciones.
6. Clasifica documentos: estáticos → `insumos/`, dinámicos → `log.md`.
7. Actualiza `00-Sistema/projects.base`.
8. Reporta en `#brain-procesados`: "Proyecto [Cliente] onbordeado. [N] documentos procesados. Pendientes: [lista]".

### Skill 2: `raw-processor`
**Trigger:** "Procesá lo nuevo en `raw/[proyecto]/`"
**Flujo:**
1. Lista archivos en `raw/[proyecto]/` que no estén en `raw/[proyecto]/procesados/`.
2. Por cada archivo:
   - Determina tipo (contrato, transcripción, propuesta, doc misceláneo).
   - Clasifica: estático → mover a `02-Proyectos/[proyecto]/insumos/` o `entregables/`.
   - Dinámico → destilar al `log.md` y agregar entrada con fecha.
3. Mueve originales a `raw/[proyecto]/procesados/`.
4. Actualiza `overview.md` si hubo cambios de estado.
5. Reporta en `#brain-procesados` y en chat: "[N] archivos procesados. [lista de cambios]".

### Skill 3: `meet-processor` *(nuevo en v1.2)*
**Trigger:** "Procesá la transcripción de la reunión de hoy" o automático al detectar correo nuevo en cuenta del asistente.
**Flujo:**
1. Lee correos nuevos en la cuenta del asistente.
2. Filtra los que son transcripciones de Google Meet.
3. Por cada transcripción:
   - Identifica el proyecto correspondiente (por título del evento o participantes).
   - Si no puede identificarlo, pregunta al usuario antes de continuar.
   - Destila la transcripción: acuerdos, decisiones, pendientes, próximas acciones.
   - Crea entrada en `log.md` del proyecto con fecha y tipo "reunión".
   - Actualiza `overview.md` si hay cambios de estado.
   - Archiva el correo original en la bandeja del asistente.
4. Reporta en `#brain-transcripciones`: "Transcripción [evento] procesada. Proyecto: [X]. [N] acuerdos registrados."

### Skill 4: `vector-ingest` *(nuevo en v1.2)*
**Trigger:** "Ingestá los documentos nuevos en `raw/vector-inbox/`" o como parte de `library-compiler` para docs largos.
**Flujo:**
1. Lista archivos en `raw/vector-inbox/` no procesados.
2. Por cada archivo:
   - Extrae metadatos: tipo, proyecto, fecha, título.
   - Fragmenta el documento en chunks con overlap.
   - Genera embeddings.
   - Ingesta a Pinecone con los metadatos obligatorios.
3. Mueve original a `raw/vector-inbox/procesados/`.
4. Agrega entrada en `01-Biblioteca/index-tematico.md` (título + metadatos, sin contenido completo).
5. Reporta en `#brain-archivos`: "[N] documentos ingestados a Pinecone. Tipos: [lista]."

### Skill 5: `estado-proyecto`
**Trigger:** "¿Cuál es el estado de [Cliente]?"
**Flujo:**
1. Lee `02-Proyectos/[Cliente]/overview.md`.
2. Lee últimas 5 entradas de `02-Proyectos/[Cliente]/log.md`.
3. Consulta Gmail por correos sin respuesta de ese cliente (últimos 7 días).
4. Genera resumen ejecutivo: estado actual, pendientes del usuario, pendientes del cliente, próximas fechas críticas.
5. Guarda en `outputs-ai/estado-[cliente]-[fecha].md` con `estado: borrador`.

### Skill 6: `daily-brief`
**Trigger:** Automático a las 7:30 AM (scheduled task).
**Flujo:**
1. Lee `00-Sistema/projects.base` — proyectos activos.
2. Lee Calendar del día.
3. Revisa Gmail — correos sin leer prioritarios.
4. Revisa correo del asistente — transcripciones pendientes de procesar.
5. Genera brief: reuniones del día, pendientes críticos, correos que necesitan respuesta, transcripciones pendientes.
6. Guarda en `03-Daily-logs/brief-[fecha].md`.
7. Reporta en `#brain-daily`.

### Skill 7: `draft-comunicacion`
**Trigger:** "Redactá [tipo] para [Cliente] sobre [tema]"
**Flujo:**
1. Lee `overview.md` del cliente para contexto y tono.
2. Lee entradas recientes del `log.md` para contexto específico.
3. Si el tema requiere contexto de biblioteca, consulta Pinecone con los metadatos del proyecto.
4. Redacta el documento (correo, propuesta, acta, informe).
5. Guarda en `02-Proyectos/[Cliente]/outputs-ai/` con `estado: borrador`.
6. Muestra el borrador y espera aprobación antes de enviar.

### Skill 8: `library-compiler`
**Trigger:** "Procesá los artículos nuevos en `raw/biblioteca/`"
**Flujo:**
1. Lista archivos en `raw/biblioteca/` no procesados.
2. Por cada artículo:
   - Determina si es corto (artículo, nota) o largo (paper, capítulo, doc extenso).
   - Corto: extrae temas, autores, conceptos clave. Crea artículo temático en `01-Biblioteca/[categoría]/`. Conecta con proyectos activos.
   - Largo: deriva a `vector-ingest` para ingestión a Pinecone. Crea solo entrada de índice en Obsidian.
3. Actualiza `01-Biblioteca/index-tematico.md`.
4. Mueve originales a `raw/biblioteca/procesados/`.
5. Reporta en `#brain-procesados`: "[N] artículos procesados. [N] ingestados a Pinecone. Conexiones nuevas: [lista]".

### Skill 9: `flush-diario`
**Trigger:** Al final de cada jornada (manual Fase 1, automático Fase 2).
**Flujo:**
1. Lee todos los daily logs del día.
2. Por cada proyecto mencionado: actualiza `log.md` con entradas nuevas.
3. Extrae decisiones importantes → actualiza `overview.md` relevantes.
4. Extrae lecciones → agrega a `memory.md`.
5. Actualiza `index.md` con archivos nuevos o modificados.
6. Reporta en `#brain-daily`: "Flush completado. [N] proyectos actualizados. [N] lecciones registradas."

### Skill 10: `update-claude-md`
**Trigger:** "Actualizá tu contexto basándote en lo que trabajamos hoy"
**Flujo:**
1. Lee conversación reciente y daily logs del día.
2. Identifica: proyectos con cambios de estado, preferencias nuevas del usuario, convenciones aprendidas.
3. Actualiza `00-Sistema/claude.md` sección "Proyectos activos" y "Estado de aprendizaje".
4. Muestra qué cambió antes de guardar.

## 6.2 Flujo de trabajo diario típico

```
07:30  → Skill daily-brief corre automáticamente
         Claude genera brief del día en logs/
         Reporta en #brain-daily

08:00  → Usuario abre Dispatch o Cowork
         Lee el brief
         Asigna tareas: "trabajá en esto primero"

Durante el día:
  → Usuario deposita archivos físicos en raw/[proyecto]/
  → Usuario hace consultas: "estado de [Cliente]"
  → Usuario captura artículos con Web Clipper
  → Reuniones de Meet → transcripción llega a correo asistente
  → Cowork responde con archivos, no chat
  → Claude reporta en canal Slack correcto al terminar cada tarea
  → Usuario aprueba o corrige outputs
  → Correcciones van a memory.md automáticamente

17:00  → Skill raw-processor corre sobre proyectos con ingresos nuevos
         Archivos físicos se destilan al vault
  → Skill meet-processor corre si hay transcripciones pendientes
         Reporta en #brain-transcripciones

18:00  → Skill flush-diario corre
         Daily logs se promueven a wiki
         Proyectos actualizados
         Claude.md actualizado con estado del día
         Reporta en #brain-daily

18:15  → Skill update-claude-md
         "Mañana sigo desde aquí"
```

---

# PARTE 7 — MANTENIMIENTO DEL SISTEMA *(nuevo en v1.2)*

Un sistema que solo crece y nunca se limpia se vuelve ruido. Esta parte describe **qué hace el usuario manualmente**, qué **rutinas periódicas corre Claude**, y cómo mantener las tres capas del sistema en orden.

## 7.1 Las tres capas y su lógica de mantenimiento

El sistema tiene tres capas con lógicas de mantenimiento distintas:

| Capa | Contenido | Deterioro típico | Responsable del mantenimiento |
|------|-----------|-----------------|-------------------------------|
| **Identidad** (`00-Sistema/`) | claude.md, memory.md, skills | Se queda desactualizado con el tiempo | Claude actualiza, usuario revisa mensualmente |
| **Trabajo activo** (`02-Proyectos/`) | overviews, logs, entregables | Proyectos cerrados no archivados, logs sin flush | Claude diario + usuario semanal |
| **Memoria long-term** (Pinecone + Biblioteca) | corpus de referencia, índices | Documentos ingestados sin metadatos, índice desconectado | Rutina mensual Claude + usuario trimestral |

## 7.2 Qué hace el usuario manualmente (y cuándo)

Estas son las acciones que el sistema no puede hacer por sí solo y que son responsabilidad del usuario:

### Acciones diarias (< 5 minutos)
- **Depositar archivos físicos en `raw/`:** PDFs recibidos, docs descargados, transcripciones locales.
- **Capturar artículos con Web Clipper** cuando los lee.
- **Verificar el brief de las 7:30** y confirmar prioridades del día.
- **Aprobar o rechazar drafts** en `outputs-ai/` antes de enviar.

### Acciones semanales (< 30 minutos)
- **Revisar `04-Inbox-Claude/`:** items que llegaron sin proyecto asignado. Decidir a qué proyecto van o si se descartan.
- **Revisar `#brain-alertas` en Slack:** pendientes que Claude detectó pero requieren decisión del usuario.
- **Confirmar estado de proyectos:** abrir `projects.base` y verificar que los estados reflejen la realidad. Corregir lo que esté mal.
- **Archivar proyectos cerrados:** cuando un proyecto termina, decirle a Claude "cerrá el proyecto [X]" para que mueva la carpeta a un archivo histórico.

### Acciones mensuales (< 1 hora)
- **Revisar `memory.md`:** leer las preferencias que Claude aprendió. Corregir las que estén mal, eliminar las obsoletas.
- **Revisar `claude.md`:** verificar que las instrucciones maestras sigan siendo precisas. Actualizar secciones que se quedaron viejas.
- **Revisar `raw/vector-inbox/`:** confirmar que no haya documentos importantes que se olvidaron de ingestar.
- **Auditar Pinecone:** revisar el índice en Obsidian (`01-Biblioteca/index-tematico.md`) y confirmar que los metadatos estén bien.

### Acciones trimestrales (< 2 horas)
- **Revisión de skills:** correr cada skill manualmente y verificar que el flujo siga siendo correcto. Actualizar los que se quedaron obsoletos.
- **Limpieza de `raw/procesados/`:** mover los archivos procesados hace más de 3 meses a un archivo histórico en Drive personal.
- **Revisión de `01-Biblioteca/`:** identificar artículos de Obsidian que deberían moverse a Pinecone porque son más útiles por búsqueda semántica que por navegación.

## 7.3 Rutinas periódicas que corre Claude

Estas son rutinas que Claude ejecuta de forma programada o cuando se le indica. En Fase 1 son manuales; en Fase 2 pueden automatizarse con Cowork scheduled tasks.

### Rutina diaria — `daily-maintenance`
**Cuándo:** Automático al final de cada jornada (parte del `flush-diario`).
**Qué hace:**
- Verifica que todos los archivos en `raw/[proyecto]/` tengan su carpeta `procesados/`.
- Detecta archivos en `raw/` que llevan más de 3 días sin procesar → alerta en `#brain-alertas`.
- Verifica que todos los outputs-ai del día tengan campo `estado:` en frontmatter.
- Actualiza `index.md` con cambios del día.

### Rutina semanal — `vault-lint`
**Cuándo:** Viernes al cierre (manual Fase 1, automático Fase 2).
**Qué hace:**
1. Escanea todos los `overview.md` de proyectos activos — detecta los que no se actualizaron en más de 7 días.
2. Verifica que todos los proyectos activos en `projects.base` tengan carpeta correspondiente en `02-Proyectos/`.
3. Detecta archivos huérfanos (sin backlinks, sin proyecto asignado).
4. Verifica consistencia de nombres de archivo (kebab-case, sin espacios, sin caracteres especiales).
5. Reporta en `#brain-alertas`: "Vault lint [fecha]. [N] issues encontrados: [lista]."

### Rutina mensual — `memory-review`
**Cuándo:** Primer lunes del mes (manual).
**Qué hace:**
1. Lee `memory.md` completo.
2. Identifica preferencias contradictorias o desactualizadas.
3. Propone una versión limpia al usuario para aprobación.
4. Actualiza `claude.md` sección "Estado de aprendizaje" con las preferencias consolidadas.
5. Reporta cambios propuestos antes de guardar.

### Rutina mensual — `pinecone-audit`
**Cuándo:** Primer lunes del mes (junto con `memory-review`).
**Qué hace:**
1. Lee `01-Biblioteca/index-tematico.md`.
2. Verifica que todos los documentos listados como "en Pinecone" tengan sus metadatos completos.
3. Detecta documentos en `raw/vector-inbox/procesados/` que no aparecen en el índice.
4. Propone lista de documentos que deberían ingestarse pero no están.
5. Reporta en `#brain-alertas`.

## 7.4 Señales de que el sistema necesita atención

Si ves alguna de estas señales, el sistema está acumulando deuda técnica:

- `raw/[proyecto]/` con archivos que llevan más de una semana sin procesar.
- `04-Inbox-Claude/` con más de 10 items sin asignar.
- `#brain-alertas` con más de 5 mensajes no atendidos.
- Proyectos en `projects.base` con estado que no refleja la realidad.
- Claude respondiendo "no tengo información sobre eso" en proyectos activos (señal de que el log está desactualizado).
- Archivos en `outputs-ai/` con `estado: borrador` de hace más de dos semanas.

**Regla general:** Si tardás más de 30 segundos en encontrar algo que debería estar en el vault, el índice está atrasado. Le decís a Claude `vault-lint` y en 5 minutos tenés el diagnóstico.

---

# PARTE 8 — CONFIGURACIÓN TÉCNICA PASO A PASO

## 8.1 Fase 1 — Lo que se monta el primer día

### Paso 1: Crear repositorio GitHub
1. Ir a github.com → New repository.
2. Nombre: `brain-os` (o el nombre que elegiste para tu sistema).
3. Visibilidad: **Private**.
4. Sin README (se creará desde Obsidian).
5. Copiar URL del repositorio.

### Paso 2: Clonar con GitHub Desktop
1. Descargar GitHub Desktop si no está instalado.
2. File → Clone repository → elegir `brain-os`.
3. Destino: `/Users/[usuario]/Brain-OS/`.

### Paso 3: Abrir como vault en Obsidian
1. Abrir Obsidian → Open folder as vault.
2. Seleccionar `/Users/[usuario]/Brain-OS/`.
3. Confirmar.

### Paso 4: Crear estructura de carpetas
En Obsidian, crear estas carpetas exactamente con estos nombres:
```
00-Sistema
01-Biblioteca
01-Biblioteca/frameworks
01-Biblioteca/papers
01-Biblioteca/regulacion
01-Biblioteca/cursos
02-Proyectos
03-Daily-logs
04-Inbox-Claude
raw
raw/biblioteca
raw/biblioteca/procesados
raw/vector-inbox
raw/vector-inbox/procesados
```

### Paso 5: Crear archivos base
En `00-Sistema/`, crear:
- `claude.md` — copiar template de Sección 3.3 y personalizar.
- `index.md` — empezar vacío, Claude lo populará.
- `projects.base` — empezar con tabla básica de proyectos activos.
- `memory.md` — empezar vacío.

### Paso 6: Instalar plugin Git en Obsidian
1. Settings → Community plugins → Turn on.
2. Browse → buscar "Git" → Install → Enable.
3. Settings del plugin:
   - Auto commit and sync after stopping file edits: **ON**.
   - Interval: **1** (minuto).
   - Pull on startup: **ON**.

### Paso 7: Configurar connectors en Claude.ai
1. Abrir claude.ai → Settings → Connectors.
2. Conectar: Gmail (cuenta personal), Google Drive (shared drives de trabajo), Google Calendar.
3. Permisos recomendados para empezar:
   - Gmail: read-only (sin envío automático).
   - Drive: read-only.
   - Calendar: read + create con aprobación.

### Paso 8: Crear cuenta del asistente y conectarla
1. En Google Workspace (o Gmail gratuito): crear `asistente@[tu-dominio].com`.
2. En Claude.ai / Cowork: conectar esta segunda cuenta Gmail con permisos read + archive.
3. Esta cuenta no necesita Drive ni Calendar — solo Gmail.

### Paso 9: Configurar Pinecone
1. Crear cuenta en pinecone.io.
2. Crear índice: nombre `brain-os`, región según tu ubicación, dimensiones 1536 (para embeddings de OpenAI).
3. Guardar API key en un gestor de contraseñas y en variables de entorno del sistema operativo.
4. **Nunca** guardar la API key dentro del vault.

### Paso 10: Configurar Slack
1. Crear workspace (o usar el existente).
2. Crear los 5 canales: `#brain-archivos`, `#brain-procesados`, `#brain-transcripciones`, `#brain-alertas`, `#brain-daily`.
3. Conectar Slack MCP en Cowork.

### Paso 11: Instalar Obsidian Web Clipper
1. Ir al Chrome Web Store y buscar "Obsidian Web Clipper".
2. Instalar extensión oficial.
3. Configurar:
   - Default vault: Brain OS.
   - Default folder: `raw/biblioteca/`.
4. Pin a la barra de extensiones para acceso rápido.

### Paso 12: Crear primer proyecto
1. En `02-Proyectos/`, crear carpeta del primer cliente/proyecto.
2. Dentro, crear las 4 subcarpetas: `insumos`, `entregables`, `financiero`, `outputs-ai`.
3. Crear `overview.md` con template de Sección 2.3.
4. Crear `log.md` vacío.
5. En `raw/`, crear carpeta `[Cliente]/procesados/`.
6. Repetir para los 2-3 proyectos más activos del momento.

### Paso 13: Primer commit
1. Abrir GitHub Desktop.
2. Ver los archivos creados.
3. Summary: "Initial vault structure".
4. Commit to main → Push origin.

**✓ Fase 1 completa.** El vault está vivo, versionado, Pinecone conectado desde el inicio, y Claude puede empezar a trabajar con los cuatro mecanismos de ingesta activos.

## 8.2 Fase 2 — Semanas 2-4

- Crear skills en Cowork (empezar con `estado-proyecto`, `draft-comunicacion`, `raw-processor`, `meet-processor`).
- Crear skill `vector-ingest` y procesar los primeros documentos de referencia.
- Configurar `daily-brief` como scheduled task en Cowork a las 7:30 AM.
- Configurar `flush-diario` como scheduled task a las 18:00.
- Habilitar Obsidian CLI (Settings → General → Advanced → CLI).
- Crear skill `vault-lint` y correrlo manualmente la primera vez para detectar inconsistencias iniciales.

## 8.3 Fase 3 — Mes 2 en adelante

- Instalar Claude Code.
- Configurar hooks de sesión (session-start, pre-compact, session-end).
- Implementar flush automático al final de cada jornada.
- Crear skill `library-compiler` completo con derivación automática a `vector-ingest`.
- Implementar rutinas mensuales `memory-review` y `pinecone-audit` como scheduled tasks.
- Evaluar si se justifica una interfaz de consulta semántica directa a Pinecone vía Dispatch.

---

# PARTE 9 — INSTRUCCIONES PARA CLAUDE AL RECIBIR ESTE DOCUMENTO

*Esta sección es directamente para Claude — debe leerla al recibir el documento como contexto inicial. Cuando implementés tu sistema, personalizá esta sección con la identidad y prioridades concretas del usuario.*

## Quién es el usuario y qué necesita

El usuario que implementa este sistema maneja volumen alto de información sobre proyectos y clientes. Cuando recibís este documento como contexto:

1. Ya estamos en modo operativo — no expliques qué es Obsidian o por qué usamos GitHub.
2. Conocés la arquitectura del sistema, las herramientas y los flujos.
3. Tu trabajo es producir outputs, no conversación.

## Cómo responder al usuario

- Si te pide el estado de un proyecto: dá un resumen ejecutivo de 3-5 líneas + lista de pendientes + próxima acción recomendada.
- Si te pide redactar algo: redactalo y guardalo en la carpeta correcta con el estado correcto en el frontmatter.
- Si algo no está claro: hacé UNA pregunta específica, no una lista de aclaraciones.
- Si necesitás información que debería estar en el vault pero no está: decilo directamente y sugerí cómo obtenerla (¿está en Gmail? ¿en Drive? ¿la copia a `raw/`?).
- Al terminar cualquier tarea de procesamiento: reportá en el canal Slack correcto.

## Cómo ingresa información al sistema

Cuatro mecanismos, ningún otro:
1. **Archivos físicos** — El usuario los pone en `raw/[proyecto]/` o `raw/vector-inbox/`. Vos los procesás cuando te lo pide.
2. **Gmail y Drive** — Vos los jalás vía MCP cuando te lo pide.
3. **Artículos web** — El usuario los captura con Web Clipper a `raw/biblioteca/`. Vos los procesás cuando te lo pide.
4. **Correo del asistente** — Transcripciones de Meet y docs pasivos llegan solos. Vos los procesás con `meet-processor` cuando se te indica.

No inventes un quinto mecanismo. No pidas que "pegue el contenido" — si es un archivo físico, el usuario lo copia a `raw/` y vos lo leés desde ahí.

## Reglas de memoria y almacenamiento

- **¿El documento tiene ciclo de vida activo?** → Obsidian.
- **¿Es corpus de referencia terminado?** → Pinecone (vía `vector-ingest`).
- Nunca dupliques: si algo va a Pinecone, en Obsidian va solo la entrada de índice (título + metadatos).

## Lo que nunca hagas

- Repetir información que ya está en este documento o en el vault.
- Preguntar cosas que podés resolver leyendo `overview.md` del proyecto relevante.
- Generar texto de chat cuando corresponde un archivo.
- Empezar respuestas con "¡Claro!" o "Por supuesto" — ir directo al grano.
- Dejar archivos huérfanos en `raw/` sin mover a `procesados/` cuando terminás.
- Enviar correos por la cuenta del asistente sin aprobación explícita del usuario.
- Acceder a los drives personales del usuario sin instrucción explícita.
- Reportar en múltiples canales de Slack la misma acción.

## Personalización por usuario

Esta sección debe completarse por cada usuario que implementa el sistema:

```markdown
## Quién soy (completar por el usuario)
Nombre: [Nombre del usuario]
Idioma principal de trabajo: [español / inglés / otro]
Zona horaria: [UTC-X]
Dominio principal de trabajo: [consultoría / academia / derecho / etc.]

## Proyectos activos al día de hoy
1. [Cliente/proyecto más urgente] — [fase] — [próxima fecha]
2. [Cliente/proyecto] — [estado]
3. [Cliente/proyecto] — [estado]

## Preferencias específicas conocidas
- [Ejemplo: siempre incluir call-to-action en correos]
- [Ejemplo: reportes en formato ejecutivo de máximo 1 página]

## Contexto que no está en el vault pero debés saber
- [Sensibilidades específicas de ciertos clientes]
- [Relaciones entre proyectos que afectan decisiones]
```

---

# APÉNDICE A — Glosario del sistema

| Término | Significado en Brain OS |
|---------|------------------------|
| vault | El repositorio Obsidian en `/Brain-OS/` (o el nombre que le haya puesto el usuario) |
| raw | Información sin procesar en la Capa A |
| wiki | Información compilada y estructurada por Claude en Obsidian |
| compilar | Que Claude lea `raw/` y destile al vault. No es un script; es una instrucción. |
| flush | Proceso de promover daily logs a la wiki |
| onboarding | Proceso de incorporar un proyecto nuevo al sistema |
| skill | Workflow reusable en Cowork — como un SOP automatizado |
| output | Archivo listo en la carpeta correcta (no texto de chat) |
| estado | Campo YAML obligatorio en todos los outputs de Claude |
| backlink | Enlace entre notas en Obsidian que conecta conocimiento |
| `index.md` | Mapa de navegación del vault, mantenido por Claude |
| `claude.md` | Instrucciones maestras de Claude para este vault |
| `memory.md` | Preferencias y aprendizajes acumulados del usuario |
| `projects.base` | Dashboard de estado de todos los proyectos activos |
| Web Clipper | Extensión de Chrome que guarda artículos limpios en `raw/biblioteca/` |
| procesados | Subcarpeta dentro de `raw/[X]/` donde van los archivos ya destilados |
| correo del asistente | Canal de ingesta pasiva — solo recibe, nunca envía por iniciativa propia |
| vector-inbox | Carpeta `raw/vector-inbox/` para docs que van directo a Pinecone |
| Pinecone | Base de datos vectorial cloud para corpus de referencia |
| shared drives | Drives de trabajo compartidos con Claude (separados de drives personales) |
| bitácora Slack | Los canales `#brain-*` donde Claude reporta sus acciones |

---

# APÉNDICE B — Templates listos para copiar

## Template: `overview.md`

```yaml
---
cliente: [Nombre]
entidad-legal: [Razón social]
estado: activo
inicio: YYYY-MM-DD
contacto-principal: [Nombre] — [correo]
tags: [consultoría, estrategia]
---

## Perfil
[Quién es el cliente, industria, contexto]

## Alcance del proyecto
[Qué se acordó hacer, en qué fases]

## Contactos clave
| Nombre | Rol | Correo | Notas |
|--------|-----|--------|-------|
| | | | |

## Estado actual
[Actualizado: YYYY-MM-DD]
[Párrafo de estado]

## Hitos y fechas críticas
- [ ] YYYY-MM-DD: [entregable]

## Notas importantes
[Contexto sensible que Claude debe considerar]
```

## Template: `log.md`

```markdown
# Log de proyecto — [Cliente]

## YYYY-MM-DD — [Tipo de interacción]
**Tipo:** reunión | correo | llamada | entregable | procesamiento-raw | transcripción-meet
**Presentes:** [si aplica]
**Resumen:** [1-2 oraciones]
**Acuerdos:**
-
**Pendientes del usuario:**
-
**Pendientes del cliente:**
-
**Próxima acción:** [qué pasa next y cuándo]
**Fuente:** [reunión directa | correo de X | archivo `raw/[Cliente]/Y.pdf` | transcripción Meet YYYY-MM-DD]
```

## Template: `claude.md` inicial

```markdown
# Claude en Brain OS — Instrucciones maestras
Versión: [fecha]

## Mi identidad en este sistema
Soy el colaborador digital del usuario.
Opero con autonomía delegada dentro del vault Brain OS.

## Proyectos activos
[Claude actualiza esta sección con flush-diario]

## Mis herramientas
- Gmail MCP (usuario): correo por proyecto
- Gmail MCP (asistente): ingesta pasiva — Meet, docs recibidos
- Google Drive MCP (shared drives de trabajo): docs de clientes
- Calendar MCP: agenda
- Obsidian CLI: leer/escribir vault
- GitHub: historial del vault
- Pinecone: corpus de referencia
- Slack (canales por tipo): bitácora de acciones

## Separación de drives
- Shared drives de trabajo: accedo para proyectos
- Drives personales del usuario: no accedo salvo instrucción explícita

## Cómo ingresa información al sistema
- `raw/[proyecto]/` — el usuario deposita archivos físicos aquí
- `raw/vector-inbox/` — documentos de referencia que van a Pinecone
- Gmail/Drive — yo jalo vía MCP a pedido
- `raw/biblioteca/` — destino del Web Clipper
- Correo del asistente — transcripciones Meet y docs pasivos

Siempre muevo archivos de `raw/` a `raw/[X]/procesados/` después de destilarlos.
Siempre reporto en el canal Slack correcto al terminar una tarea de procesamiento.

## Convenciones
- Archivos: kebab-case con fecha cuando corresponde
- Estado obligatorio en todo output
- [Idioma principal] para proyectos, inglés para tech si es más claro
- Resúmenes ejecutivos: máximo 3 párrafos

## Preferencias aprendidas del usuario
[Claude agrega aquí automáticamente con cada corrección]
```

## Template: `projects.base` inicial

```yaml
---
type: base
---

filters:
  - folder: "02-Proyectos"

views:
  - type: table
    name: "Proyectos activos"
    filters:
      - property: estado
        operator: equals
        value: activo
    columns:
      - cliente
      - fase
      - contacto-principal
      - próxima-fecha
```

## Template: `memory.md` inicial

```markdown
# Memoria del sistema — preferencias y aprendizajes

## Preferencias de formato
- [Claude completa automáticamente]

## Preferencias de tono y estilo
- [Claude completa automáticamente]

## Lecciones aprendidas por proyecto
### [Cliente A]
- [decisiones y contexto importante]

### [Cliente B]
- [decisiones y contexto importante]

## Reglas que el usuario ha corregido
- [Cada vez que el usuario ajusta un output de Claude, se registra aquí la regla extraída]
```

## Template: notificación Slack estándar

```
[TIPO] [Proyecto/Área] — [descripción breve]
Archivos: [lista si aplica]
Pendientes detectados: [lista | ninguno]
```

Tipos válidos: `[PROCESADO]` `[TRANSCRIPCIÓN]` `[ARCHIVADO]` `[ALERTA]` `[BRIEF]` `[FLUSH]` `[VAULT-LINT]`

---

*Manual genérico de arquitectura — 2026*
*Versión 1.2 agnóstica*
*Personalizá todos los placeholders `[entre-corchetes]` antes de implementarlo*
*Próxima revisión sugerida: cuando el vault supere 200 archivos o al completar Fase 2*
