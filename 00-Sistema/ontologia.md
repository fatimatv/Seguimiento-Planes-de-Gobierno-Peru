# Ontología del Análisis Político — Brain Político Perú

> Definición de entidades, relaciones y tipologías para el sistema de comparación de planes de gobierno.

---

## ENTIDADES (Nodos)

### 1. CANDIDATO
Representa a cada candidato presidencial con su identidad política.

```yaml
CANDIDATO:
  id: keiko | roberto
  nombre: "Nombre completo"
  partido: "Nombre del partido"
  coalición: ["partidos aliados"]
  lema: "Lema del plan de gobierno"
  ejes: ["Eje 1", "Eje 2"]
  color: "#HEX"
  visión_país: "Texto de visión al 2031"
```

**Instancias:**
- `keiko` → Keiko Fujimori, Fuerza Popular, "Perú con Orden"
- `roberto` → Roberto Sánchez Palomino, Juntos por el Perú, "Economía Popular y Progreso"

---

### 2. TEMA
Área temática de política pública. Permite agrupar propuestas y declaraciones por ámbito.

```yaml
TEMA:
  id: "string-minúsculas"
  nombre: "Nombre completo"
  icono: "🔒"
  dimensiones_keiko: ["Eje al que pertenece en el plan Keiko"]
  dimensiones_roberto: ["Dimensión en el plan Roberto"]
```

Ver taxonomía completa en `CLAUDE.md` sección 4.

---

### 3. PROPUESTA
Una propuesta concreta de un candidato en un tema, extraída de su plan de gobierno.

```yaml
PROPUESTA:
  id: "[candidato_inicial]-[tema_id]-[n]"   # ej: k-seg-001
  candidato: keiko | roberto
  tema: [ID de TEMA]
  texto: "Descripción de la propuesta"
  tipo: propuesta | meta | diagnóstico | principio | 100dias
  meta_cuantitativa: "Reducir X en Y% al año Z"    # si aplica
  fuente: "Plan de Gobierno, Eje X, p. Y"
  fecha_fuente: "2026"
```

**Tipos de PROPUESTA:**
- `propuesta` → Acción concreta que el candidato se compromete a realizar.
- `meta` → Objetivo medible a alcanzar (con porcentaje, plazo, cifra).
- `diagnóstico` → Descripción del problema, no de la solución.
- `principio` → Valor o enfoque filosófico que guía las decisiones.
- `100dias` → Acción comprometida en los primeros 100 días de gobierno.

---

### 4. DECLARACIÓN_DEBATE
Una declaración específica de un candidato en un debate presidencial.

```yaml
DECLARACIÓN_DEBATE:
  id: "[debate_id]-[candidato]-[n]"
  candidato: keiko | roberto
  tema: [ID de TEMA]
  texto: "Cita textual de la declaración"
  contexto: "Pregunta o tema que motivó la declaración"
  tipo: propuesta | diagnóstico | ataque | defensa | cifra | compromiso | evasión
  debate_id: "debate-YYYY-MM-DD-[organizador]"
  timestamp: "HH:MM"     # si está disponible
```

**Tipos de DECLARACIÓN_DEBATE:**
- `propuesta` → Anuncia qué hará.
- `diagnóstico` → Describe el problema.
- `ataque` → Critica la posición del adversario.
- `defensa` → Responde a críticas.
- `cifra` → Presenta un dato estadístico.
- `compromiso` → Promesa directa con fórmula "yo me comprometo / voy a / haré".
- `evasión` → Evita responder la pregunta directamente.

---

### 5. IMPLEMENTACIÓN *(Etapa 2)*
Registro del estado de cumplimiento de una propuesta durante el gobierno.

```yaml
IMPLEMENTACIÓN:
  id: "impl-[propuesta_id]-[fecha]"
  candidato_en_gobierno: keiko | roberto
  propuesta_id: [ID de PROPUESTA o DECLARACIÓN_DEBATE]
  estado: CUMPLIDA | PARCIAL | INCUMPLIDA | PENDIENTE | BLOQUEADA
  evidencia: "Cita de norma, noticia o informe oficial"
  norma: "D.S. N° XXX-2026 / Ley N° XXXXX"    # si aplica
  fecha_evidencia: "YYYY-MM-DD"
  notas: "Análisis del cumplimiento"
  última_actualización: "YYYY-MM-DD"
```

**Estados de IMPLEMENTACIÓN:**
- `CUMPLIDA` → Medida implementada conforme a lo prometido.
- `PARCIAL` → Implementación incompleta, postergada o modificada sustancialmente.
- `INCUMPLIDA` → No implementada habiendo condiciones para hacerlo; plazo vencido.
- `PENDIENTE` → Dentro del plazo comprometido, aún en curso.
- `BLOQUEADA` → No implementada por factores externos (Congreso, crisis, pandemia, etc.).

---

## RELACIONES (Aristas)

### Entre PROPUESTAS de diferentes candidatos

| Tipo | Código | Descripción |
|------|--------|-------------|
| Acuerdo total | `COINCIDE` | Ambos proponen lo mismo o soluciones equivalentes al mismo problema. |
| Acuerdo con extensión | `AMPLÍA` | Un candidato va más lejos que el otro en la misma dirección; la propuesta mayor contiene a la menor. |
| Enfoques distintos | `DIVERGE` | Mismo objetivo o problema, soluciones diferentes (no necesariamente incompatibles). |
| Posiciones opuestas | `CONTRADICE` | Una propuesta hace imposible o contradice directamente a la otra. |
| Exclusiva de un candidato | `SOLO_A` / `SOLO_B` | El tema solo aparece en el plan de un candidato. |

---

### Entre PROPUESTA (plan) y DECLARACIÓN_DEBATE (del mismo candidato)

| Tipo | Código | Descripción |
|------|--------|-------------|
| Refuerzo | `CONSISTENTE` | El candidato repite o refuerza su propuesta escrita. |
| Extensión | `AMPLÍA_DEBATE` | En el debate, el candidato detalla o profundiza lo escrito en el plan. |
| Debilitamiento | `VAGUEA` | En el debate, el candidato se expresa de manera más vaga o menos comprometida. |
| Contradicción | `CONTRADICE_DEBATE` | La declaración en debate es directamente incompatible con la propuesta del plan. |
| Ausencia | `OMITE` | El candidato no mencionó en debates una propuesta clave de su plan. |
| Nuevo | `NUEVO_DEBATE` | El candidato prometió algo en el debate que no está en su plan escrito. |

---

### Entre PROPUESTA y su IMPLEMENTACIÓN *(Etapa 2)*

| Tipo | Código | Descripción |
|------|--------|-------------|
| Cumplimiento total | `CUMPLIDA` | La implementación refleja fielmente la propuesta. |
| Cumplimiento parcial | `PARCIAL` | Implementación incompleta o modificada. |
| Incumplimiento | `INCUMPLIDA` | No se implementó sin justificación estructural. |
| En curso | `PENDIENTE` | Dentro del plazo, en proceso de implementación. |
| Impedimento externo | `BLOQUEADA` | Factores externos impidieron la implementación. |

---

## GRAFO DE CONOCIMIENTO

El grafo del sistema tiene la siguiente topología:

```
CANDIDATO ──[propone_sobre]──► TEMA
    │                           │
    │                      [agrupa]
    │                           │
    └──[enuncia]──► PROPUESTA ◄─┘
                       │
               [COINCIDE / DIVERGE /
                CONTRADICE / AMPLÍA]
                       │
                   PROPUESTA (otro candidato)
                       │
               [CONSISTENTE / VAGUEA /
                CONTRADICE_DEBATE]
                       │
            DECLARACIÓN_DEBATE
                       │
               [CUMPLIDA / PARCIAL /
                INCUMPLIDA / BLOQUEADA]
                       │
               IMPLEMENTACIÓN (Etapa 2)
```

---

## MATRIZ DE ANÁLISIS RÁPIDO

Para cada par de propuestas (una por candidato en el mismo tema), aplicar este árbol de decisión:

```
¿Abordan el mismo problema específico?
├── NO → SOLO_A o SOLO_B (si el otro no tiene propuesta en ese sub-tema)
└── SÍ → ¿La dirección de la solución es compatible?
    ├── NO → CONTRADICE
    └── SÍ → ¿El alcance es similar?
        ├── SÍ → COINCIDE
        └── NO → ¿Uno va más lejos que el otro?
            ├── SÍ → AMPLÍA
            └── NO → DIVERGE (enfoques distintos, misma dirección general)
```

---

## PESOS DE RELEVANCIA

Para priorizar el análisis, las propuestas y comparaciones tienen pesos de relevancia:

| Nivel | Criterio | Ejemplos |
|-------|----------|---------|
| **ALTA** | Propuesta-ancla del plan, mencionada en presentación o visión | C5i, shock desregulatorio, FEPC, RMV |
| **MEDIA** | Propuesta en sección específica, con meta cuantitativa | reducir homicidios 20%, 6% presupuesto educación |
| **BAJA** | Propuesta de detalle, sin meta o plazo explícito | ventanilla única, parques industriales |
| **100 DÍAS** | Compromiso explícito en los primeros 100 días | DU patrulleros, retomar obras paralizadas |

---

*Ontología v1.0 — Brain Político Perú — Junio 2026*
