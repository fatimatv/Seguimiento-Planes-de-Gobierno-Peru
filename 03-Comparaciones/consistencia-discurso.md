# Consistencia del Discurso de Campaña

> Análisis de la consistencia entre lo que cada candidato escribió en su plan de gobierno y lo que declaró en los debates presidenciales. Incluye el índice de consistencia por (candidato × tema) y un detalle de las propuestas omitidas y los nuevos compromisos asumidos en debate.

**Generado:** 2026-06-10  
**Fuente:** `00-Sistema/datos/propuestas.json`, `00-Sistema/datos/declaraciones.json`, `00-Sistema/datos/comparaciones.json`  
**Generador:** `00-Sistema/scripts/render_comparaciones.py`

---

**Fórmula del índice de consistencia:**  
$$I_c = \frac{\text{CONSISTENTE} + \text{AMPLÍA\_DEBATE}}{\text{CONSISTENTE} + \text{AMPLÍA\_DEBATE} + \text{VAGUEA} + \text{CONTRADICE\_DEBATE}}$$

Rango 0–1. **No** penaliza OMITE ni NUEVO_DEBATE en el denominador (son comportamientos distintos: silencio o expansión, no contradicción).

## Resumen por candidato y tema

| Candidato | Tema | n_plan | n_debate | Consist. | Amplía | Vaguea | Contradice | Omite | Nuevo | Índice |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Keiko Fujimori | Agricultura | 35 | 5 | 3 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| Keiko Fujimori | Agua y Saneamiento | 18 | 4 | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| Keiko Fujimori | Ambiente / Desarrollo Sostenible | 19 | 2 | 2 | 0 | 0 | 0 | 1 | 0 | 1.00 |
| Keiko Fujimori | Reforma Constitucional / Institucional | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 5 | — |
| Keiko Fujimori | Anticorrupción | 16 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | — |
| Keiko Fujimori | Deporte | 15 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| Keiko Fujimori | Economía / Macroeconomía | 19 | 8 | 5 | 5 | 0 | 0 | 0 | 1 | 1.00 |
| Keiko Fujimori | Educación | 23 | 6 | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| Keiko Fujimori | Energía | 20 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1.00 |
| Keiko Fujimori | Industria | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Keiko Fujimori | Sistema de Justicia | 9 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 1.00 |
| Keiko Fujimori | Juventud | 19 | 5 | 4 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| Keiko Fujimori | Minería | 16 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | — |
| Keiko Fujimori | MYPE y Emprendimiento | 22 | 3 | 2 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| Keiko Fujimori | Orden Jurídico / Seguridad Jurídica | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Keiko Fujimori | Pensiones / Programas Sociales | 25 | 3 | 2 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| Keiko Fujimori | Peruanos en el Extranjero | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Keiko Fujimori | Pesca | 18 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | — |
| Keiko Fujimori | Salud | 25 | 9 | 4 | 5 | 0 | 0 | 0 | 0 | 1.00 |
| Keiko Fujimori | Seguridad Ciudadana | 38 | 13 | 8 | 3 | 0 | 0 | 0 | 2 | 1.00 |
| Keiko Fujimori | Trabajo y Empleo | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | — |
| Keiko Fujimori | Transporte e Infraestructura | 24 | 7 | 2 | 5 | 0 | 0 | 0 | 0 | 1.00 |
| Keiko Fujimori | Turismo | 19 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| Keiko Fujimori | Vivienda | 18 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | Agricultura | 20 | 5 | 3 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | Agua y Saneamiento | 12 | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | Ambiente / Desarrollo Sostenible | 31 | 2 | 2 | 0 | 0 | 0 | 1 | 0 | 1.00 |
| Roberto Sánchez Palomino | Reforma Constitucional / Institucional | 16 | 14 | 10 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | Anticorrupción | 9 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | Ciencia, Tecnología e Innovación | 9 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | — |
| Roberto Sánchez Palomino | Cultura | 21 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1.00 |
| Roberto Sánchez Palomino | Deporte | 12 | 2 | 0 | 1 | 0 | 0 | 0 | 1 | 1.00 |
| Roberto Sánchez Palomino | Economía / Macroeconomía | 26 | 8 | 7 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | Educación | 21 | 7 | 3 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | Energía | 18 | 3 | 1 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | Relaciones Exteriores | 40 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | Género e Inclusión | 17 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | — |
| Roberto Sánchez Palomino | Pueblos Indígenas y DDHH | 4 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | — |
| Roberto Sánchez Palomino | Industria | 12 | 3 | 4 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | Sistema de Justicia | 13 | 4 | 4 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | Juventud | 15 | 3 | 2 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | Minería | 20 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | MYPE y Emprendimiento | 17 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Roberto Sánchez Palomino | Orden Jurídico / Seguridad Jurídica | 16 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | Pensiones / Programas Sociales | 12 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | Peruanos en el Extranjero | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Roberto Sánchez Palomino | Pesca | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Roberto Sánchez Palomino | Salud | 21 | 12 | 7 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | Seguridad Ciudadana | 15 | 6 | 6 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | Trabajo y Empleo | 18 | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | Transporte e Infraestructura | 30 | 8 | 2 | 4 | 0 | 0 | 0 | 0 | 1.00 |
| Roberto Sánchez Palomino | Turismo | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Roberto Sánchez Palomino | Vivienda | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |

---

## Propuestas del plan no mencionadas en debate (OMITE)

### Keiko Fujimori

- **[k-corrupcion-005]** Sistema único de declaraciones juradas de bienes, rentas e intereses administrado por la Contraloría, interoperable con SUNAT y UIF.  
  *Fortalecer la Procuraduría General es propuesta ALTA del plan de Keiko pero no fue mencionada en ningún debate.*

- **[k-mineria-002]** La minería ilegal representa hasta el 90% de las operaciones en Madre de Dios, generando mafias, deforestación y violencia (caso Pataz 2024 con 13 muertos).  
  *Destrabar proyectos mineros con ventanilla única es propuesta clave del plan pero ausente en debates.*

- **[k-pesca-003]** Más del 70% de los trabajadores pesqueros operan de manera informal, sin seguros ni protección laboral; estudios reportan trabajo forzoso e infantil en la cadena pesquera.  
  *Fortalecer industria de harina de pescado y exportación pesquera no fue desarrollada en debates.*

- **[k-ambiente-005]** Crear plantas de tratamiento y valorización energética de residuos sólidos urbanos mediante APP, priorizando ciudades con más de 200,000 habitantes.  
  *El respaldo a la flexibilización forestal del plan no fue defendido explícitamente en debate.*

### Roberto Sánchez Palomino

- **[r-ambiente-019]** Implementar de forma inmediata un Plan Nacional de Restauración y Remediación Ambiental con participación ciudadana, financiado por impuesto a utilidades extraordinarias del sector extractivo; restaurar 500,000 hectáreas de ecosistemas degradados priorizando cabeceras de cuenca.  
  *Plan Nacional de Restauración Ambiental con 500,000 ha es propuesta ALTA del plan pero no fue mencionada en debates.*

- **[r-indigenas-003]** Promover la existencia de escaños reservados para asegurar la representación de pueblos originarios en el Congreso de la República y otros espacios de elección popular.  
  *Escaños reservados para pueblos originarios en el Congreso no fueron mencionados en debates.*

- **[r-genero-010]** Despenalizar la interrupción del embarazo en casos de violencia sexual y/o riesgo para la vida o salud de la madre, para que ninguna víctima sea obligada a continuar un embarazo forzado.  
  *Despenalización del aborto en casos de violencia sexual y riesgo de la madre, propuesta sensible, no fue mencionada en debates.*

- **[r-cultura-007]** Crear el Ministerio de Las Culturas que releve el valor de la diversidad cultural y priorice las competencias respecto de pueblos indígenas originarios — como titulación de territorios y georreferenciación de comunidades nativas y campesinas.  
  *Creación del Ministerio de Las Culturas no fue mencionada en debates.*

- **[r-cti-003]** Crear el Ministerio de Ciencia y Tecnología orientado a las metas del plan de transformación productiva, vinculado a institutos técnicos regionales, ZEE en Ilo/Matarani/Chancay, fondo de innovación y alianzas universidad-empresa.  
  *Creación del Ministerio de Ciencia y Tecnología no fue mencionada en debates.*

---

## Compromisos asumidos en debate sin contraparte en el plan (NUEVO_DEBATE)

### Keiko Fujimori

- **[debate-1-k-014]** Defensa contra acusación de Roberto: 'Caos se escribe con C, con la C de Castillo'; Fuerza Popular solo tiene 20 de 130 congresistas.

  > quiero decirle que Caos se escribe con C, con la C de Castillo. Y ustedes ya gobernaron. Fuerza Popular solo tiene 20 congresistas de 130

  *Defensa contextual ('Caos se escribe con C de Castillo') es una intervención debatística sin contraparte en el plan.*

- **[debate-1-k-015]** Ataque a Roberto: en sus filas tiene a Antauro Humala, 'asesino de policías', y en el último mitin de primera vuelta dijo que la lucha contra el crimen estará en sus manos.

  > tiene usted en sus filas Antaurumala, asesino de policías. Usted el 8 de abril en el último miting de primera vuelta dijo lo siguiente

  *El ataque puntual a Antauro Humala es retórica de debate, no figura en el plan.*

- **[debate-1-k-018]** A Sánchez lo acompaña 'un asesino de policías'; ella estará acompañada por Marco Miyashiro y el general Astudillo, 'héroes nacionales'.

  > Me acompañan además a mí dos héroes nacionales, Marco Millashiro y el general Astudillo. En cambio, al señor Sánchez lo acompaña un asesino de policías

  *Mención a sus acompañantes (Miyashiro, Astudillo) y descalificación a Antauro son retórica de debate.*

- **[debate-1-k-026]** Convocatoria a inscribir personeros en Fuerza Popular y en el otro grupo político; los observadores internacionales serán claves para fortalecer la democracia.

  > hacemos esta convocatoria para que todos los ciudadanos se inscriban como personeros, no solamente en Fuerza Popular, también en el otro grupo político

  *Convocatoria a personeros y observadores internacionales para defender el voto no está en el plan.*

- **[debate-1-k-043]** Equipo económico con Carranza (exministro de Economía), Neuhaus (infraestructura) y Rafael Belaunde (minería); meta: pasar del 3% al 6% de crecimiento al fin del mandato.

  > Con ellos nosotros vamos a nuevamente impulsar las cifras de crecimiento que hoy están en cerca de 3% y los dejaremos al culminar nuestro mandato en cifras del 6%

  *Mención del equipo económico (Carranza, Neuhaus, Belaunde) y cifra 3%→6% son retórica del debate, sin equivalente en el plan.*

- **[debate-1-k-046]** Reconoce errores cometidos, dice haber aprendido y levantarse con más fuerza; pide ser presidenta para ejecutar las obras necesarias.

  > Sé que a lo largo de mi vida política he cometido errores, de ellos aprendí, pero me levanté además con mucha más fuerza

  *Reconocimiento de errores y pedido del voto en cierre — emoción de campaña sin contraparte programática en el plan.*

- **[debate-1-k-047]** Aspira a gobernar 'con fuerza y con amor', dejar a los jóvenes un Perú en paz y con progreso, en un mensaje de reconciliación tras 30 años recorriendo el país.

  > aspiro a gobernar con fuerza y con amor. Le pido al Señor que bendiga cada uno de sus hogares

  *Aspiración a gobernar 'con fuerza y con amor' es lenguaje de cierre, no programa.*

- **[debate-2-k-027]** En 2022 la inversión privada en Perú no creció nada y se perdieron 393,000 puestos de empleo; en 2023 hubo recesión sin crisis externa severa. — *Vocero: Luis Julián Martín Carranza Ugarte* — `[136:51]`

  > en el año 2022 la inversión privada en el Perú no creció nada y perdimos ese año 2022 perdimos 393,000 puestos de empleo

  *Ataque puntual con cifras 2022 y 2023 es contraargumento de debate sin contraparte en plan.*

- **[debate-2-k-034]** Esta elección no es de derechas ni de izquierdas: es saber si seguimos con el caos o ponemos orden; invitación a poner orden con la fuerza de la salud. — *Vocero: José Francisco Recoba Martínez* — `[164:54]`

  > Esta elección no es de derechas ni de izquierdas. Esta elección es para saber si vamos a continuar con el caos

  *Reflexión 'no es derechas ni izquierdas, es orden vs caos' es cierre retórico, no programa.*

### Roberto Sánchez Palomino

- **[debate-2-r-013]** Lima 2027 será el evento más importante y mejor organizado de la historia del país, sostenido por Casa Futuro: polideportivos con bibliotecas y centros de recursos tecnológicos. — *Vocero: Ernesto Alonso Zunini Yerrén* — `[57:46]`

  > Lima 202 será por Juntos por el Perú el evento más importante y mejor organizado de la historia de nuestro país

  *Lima 2027 como evento más importante del país y Casa Futuro no figuran como propuesta-ancla en el plan.*

