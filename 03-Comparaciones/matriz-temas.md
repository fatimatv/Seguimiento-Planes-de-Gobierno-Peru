# Matriz Comparativa por Tema

> Tabla maestra con todos los temas, número de propuestas por candidato en el plan, número de declaraciones en debates, y las relaciones plan-vs-plan detectadas.

**Generado:** 2026-06-10  
**Fuente:** `00-Sistema/datos/propuestas.json`, `00-Sistema/datos/declaraciones.json`, `00-Sistema/datos/comparaciones.json`  
**Generador:** `00-Sistema/scripts/render_comparaciones.py`

---

| Tema | Icono | Plan Keiko | Plan Roberto | Debate Keiko | Debate Roberto | Relaciones plan-vs-plan |
|---|---|---:|---:|---:|---:|---|
| Seguridad Ciudadana | 🔒 | 38 | 15 | 13 | 6 | COINCIDE (diagnostico), DIVERGE (propuesta_principal), SOLO_B (meta), DIVERGE (enfoque_institucional) |
| Anticorrupción | 🛡️ | 16 | 9 | 0 | 3 | COINCIDE (diagnostico), DIVERGE (propuesta_principal), DIVERGE (enfoque_institucional) |
| Economía / Macroeconomía | 💰 | 19 | 26 | 8 | 8 | DIVERGE (diagnostico), COINCIDE (propuesta_principal), COINCIDE (meta), CONTRADICE (enfoque_institucional) |
| Trabajo y Empleo | 💼 | 0 | 18 | 1 | 2 | SOLO_B (propuesta_principal) |
| MYPE y Emprendimiento | 🏪 | 22 | 17 | 3 | 2 | COINCIDE (diagnostico), DIVERGE (propuesta_principal) |
| Minería | ⛏️ | 16 | 20 | 0 | 0 | COINCIDE (diagnostico), DIVERGE (propuesta_principal), CONTRADICE (enfoque_institucional), SOLO_B (meta) |
| Agricultura | 🌾 | 35 | 20 | 5 | 5 | DIVERGE (diagnostico), DIVERGE (propuesta_principal), DIVERGE (meta), CONTRADICE (enfoque_institucional) |
| Pesca | 🐟 | 18 | 10 | 0 | 0 | DIVERGE (diagnostico), CONTRADICE (propuesta_principal) |
| Energía | ⚡ | 20 | 18 | 1 | 3 | COINCIDE (diagnostico), CONTRADICE (propuesta_principal), COINCIDE (propuesta_principal), AMPLIA (meta) |
| Transporte e Infraestructura | 🚧 | 24 | 30 | 7 | 8 | COINCIDE (diagnostico), DIVERGE (propuesta_principal), DIVERGE (enfoque_institucional) |
| Turismo | 🏞️ | 19 | 11 | 1 | 0 | DIVERGE (propuesta_principal) |
| Industria | 🏭 | 17 | 12 | 0 | 3 | DIVERGE (propuesta_principal), CONTRADICE (propuesta_principal) |
| Ambiente / Desarrollo Sostenible | 🌳 | 19 | 31 | 2 | 2 | COINCIDE (diagnostico), CONTRADICE (propuesta_principal), CONTRADICE (enfoque_institucional), SOLO_B (meta) |
| Educación | 📚 | 23 | 21 | 6 | 7 | COINCIDE (diagnostico), DIVERGE (propuesta_principal), DIVERGE (meta), DIVERGE (enfoque_institucional) |
| Salud | 🏥 | 25 | 21 | 9 | 12 | COINCIDE (diagnostico), DIVERGE (propuesta_principal), DIVERGE (meta), DIVERGE (enfoque_institucional) |
| Vivienda | 🏠 | 18 | 12 | 1 | 0 | COINCIDE (diagnostico), DIVERGE (propuesta_principal) |
| Agua y Saneamiento | 💧 | 18 | 12 | 4 | 2 | COINCIDE (diagnostico), CONTRADICE (propuesta_principal) |
| Pensiones / Programas Sociales | 👵 | 25 | 12 | 3 | 2 | COINCIDE (diagnostico), COINCIDE (propuesta_principal), DIVERGE (meta) |
| Deporte | ⚽ | 15 | 12 | 2 | 2 | DIVERGE (propuesta_principal) |
| Sistema de Justicia | ⚖️ | 9 | 13 | 2 | 4 | DIVERGE (diagnostico), DIVERGE (propuesta_principal), CONTRADICE (enfoque_institucional) |
| Orden Jurídico / Seguridad Jurídica | 📜 | 11 | 16 | 0 | 0 | DIVERGE (propuesta_principal) |
| Relaciones Exteriores | 🌎 | 0 | 40 | 0 | 2 | SOLO_B (propuesta_principal) |
| Reforma Constitucional / Institucional | 🏛️ | 0 | 16 | 8 | 14 | SOLO_B (propuesta_principal) |
| Pueblos Indígenas y DDHH | 🪶 | 0 | 4 | 0 | 1 | SOLO_B (propuesta_principal) |
| Género e Inclusión | 🤝 | 0 | 17 | 0 | 0 | SOLO_B (propuesta_principal), SOLO_B (propuesta_principal) |
| Ciencia, Tecnología e Innovación | 🔬 | 0 | 9 | 0 | 0 | SOLO_B (propuesta_principal) |
| Juventud | 🧑‍🎓 | 19 | 15 | 5 | 3 | DIVERGE (propuesta_principal), DIVERGE (meta) |
| Cultura | 🎭 | 0 | 21 | 0 | 0 | SOLO_B (propuesta_principal) |
| Peruanos en el Extranjero | ✈️ | 20 | 15 | 0 | 0 | COINCIDE (propuesta_principal) |

---

## Leyenda de relaciones

- **COINCIDE**: ambos proponen lo mismo o soluciones equivalentes.
- **AMPLÍA**: un candidato va más lejos que el otro en la misma dirección.
- **DIVERGE**: mismo objetivo, soluciones distintas no necesariamente incompatibles.
- **CONTRADICE**: posiciones mutuamente excluyentes.
- **SOLO_A / SOLO_B**: el tema solo aparece en el plan de uno (B = Roberto).
