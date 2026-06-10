# -*- coding: utf-8 -*-
"""Extracción de Dimensión Institucional - Roberto Sánchez (Task 10)."""
import json
from pathlib import Path

ARCHIVO_FUENTE = "01-Planes-de-Gobierno/Roberto-Sanchez/Plan-de-Gobierno-Roberto_Sanchez.md"

def mk(id_, tema, tipo, relevancia, texto, cita, seccion, linea_ini, linea_fin, meta=None):
    return {
        "id": id_,
        "candidato": "roberto",
        "tema": tema,
        "tipo": tipo,
        "relevancia": relevancia,
        "texto": texto,
        "cita_textual": cita,
        "fuente": {
            "archivo": ARCHIVO_FUENTE,
            "seccion": seccion,
            "linea_inicio": linea_ini,
            "linea_fin": linea_fin
        },
        "meta_cuantitativa": meta
    }

nuevas = []

# =====================================================================
# 3.1 REFORMA CONSTITUCIONAL DE CONSENSO (líneas 108-116) — tema: constitucion
# Continúa desde r-constitucion-002
# =====================================================================

# r-constitucion-003: Diagnóstico vicio de origen Const. 1993
nuevas.append(mk(
    "r-constitucion-003", "constitucion", "diagnostico", "ALTA",
    "Diagnóstico del vicio de origen de la Constitución de 1993: nació del autogolpe de 1992 y carece de consenso nacional; se plantea reemplazarla por una Constitución construida participativamente.",
    "La Constitución de 1993 cargó desde el inicio con un vicio de origen: nació del autogolpe de 1992 y se aprobó en un referéndum estrecho y cuestionado, sin el consenso de la nación",
    "Dimensión Institucional — 3.1 Reforma Constitucional — Situación Actual",
    110, 110
))

# r-constitucion-004: Propuesta ancla — Reforma Constitucional de Consenso
nuevas.append(mk(
    "r-constitucion-004", "constitucion", "propuesta", "ALTA",
    "Propuesta ancla: liderar un proceso democrático y participativo de cambio constitucional, ya sea por reforma integral del art. 206 o asamblea constituyente, para dotar al país de una Constitución de consenso.",
    "Liderar un proceso democrático y participativo de cambio constitucional que, a través del diálogo nacional y de la consulta a la ciudadanía, defina la vía —la reforma integral por el cauce del artículo 206 o la convocatoria a una asamblea constituyente— para dotar al país de una Constitución de consenso",
    "Dimensión Institucional — 3.1 Reforma Constitucional — Medidas Propuestas",
    114, 114
))

# r-constitucion-005: Devolver al Estado rol planificador estratégico
nuevas.append(mk(
    "r-constitucion-005", "constitucion", "propuesta", "ALTA",
    "Reforma del régimen económico constitucional para devolver al Estado un papel activo como planificador estratégico del desarrollo y garante de la soberanía sobre los recursos naturales y servicios universales.",
    "Devolver al Estado un papel activo como planificador estratégico del desarrollo, garante de la soberanía sobre los recursos naturales y de los servicios universales, revisando el régimen económico de la Constitución",
    "Dimensión Institucional — 3.1 Reforma Constitucional — Medidas Propuestas",
    114, 114
))

# r-constitucion-006: Restablecer equilibrio de poderes / vacancia
nuevas.append(mk(
    "r-constitucion-006", "constitucion", "propuesta", "MEDIA",
    "Restablecer el equilibrio entre poderes del Estado precisando en la Constitución las causales de vacancia presidencial y delimitando con claridad la figura de incapacidad moral permanente.",
    "Restablecer el equilibrio y la independencia entre los poderes del Estado, precisando en la Constitución las causales de la vacancia presidencial y delimitando con claridad la figura de la",
    "Dimensión Institucional — 3.1 Reforma Constitucional — Medidas Propuestas",
    114, 114
))

# r-constitucion-007: Reforma selección magistrados TC
nuevas.append(mk(
    "r-constitucion-007", "constitucion", "propuesta", "MEDIA",
    "Reformar la selección y nombramiento de los magistrados del Tribunal Constitucional para asegurar independencia y mérito mediante concurso público, mayoría calificada y participación plural.",
    "Reformar la selección y el nombramiento de los magistrados del Tribunal Constitucional para asegurar su independencia y su mérito, con concurso público, mayoría calificada y participación plural",
    "Dimensión Institucional — 3.1 Reforma Constitucional — Medidas Propuestas",
    116, 116
))

# r-constitucion-008: Reconocer derechos colectivos pueblos originarios
nuevas.append(mk(
    "r-constitucion-008", "constitucion", "propuesta", "MEDIA",
    "Reconocer en la Constitución los derechos colectivos de los pueblos originarios y comunidades campesinas, andinas, amazónicas y afroperuanas, incluida la consulta previa.",
    "Reconocer en la Constitución los derechos colectivos de los pueblos originarios y de las comunidades campesinas, andinas, amazónicas y afroperuanas, incluida la consulta previa",
    "Dimensión Institucional — 3.1 Reforma Constitucional — Medidas Propuestas",
    114, 114
))

# r-constitucion-009: Elevar acceso a salud a derecho fundamental
nuevas.append(mk(
    "r-constitucion-009", "constitucion", "propuesta", "MEDIA",
    "Elevar a derecho fundamental exigible ante la justicia el acceso universal a una salud pública de calidad en todo el territorio con financiamiento garantizado.",
    "Elevar a derecho fundamental, exigible ante la justicia, el acceso universal a una salud pública de calidad en todo el territorio, con un sistema integrado, financiamiento garantizado",
    "Dimensión Institucional — 3.1 Reforma Constitucional — Medidas Propuestas",
    114, 114
))

# r-constitucion-010: 6% PBI en educación
nuevas.append(mk(
    "r-constitucion-010", "constitucion", "meta", "MEDIA",
    "Meta: hacer cumplir efectivamente el mandato del artículo 16 de invertir cada año no menos del 6% del PBI en educación pública.",
    "haciendo cumplir de manera efectiva el mandato del artículo 16 de invertir cada año no menos del 6 % del PBI en educación",
    "Dimensión Institucional — 3.1 Reforma Constitucional — Medidas Propuestas",
    114, 114,
    meta="No menos del 6% del PBI anual en educación (art. 16)"
))

# =====================================================================
# 3.2 SEGURIDAD CIUDADANA (líneas 116-127) — tema: seguridad
# Continúa desde r-seguridad-001
# =====================================================================

# r-seguridad-002: Diagnóstico pacto criminal-político
nuevas.append(mk(
    "r-seguridad-002", "seguridad", "diagnostico", "ALTA",
    "Diagnóstico del pacto de protección e impunidad entre la criminalidad y un sector de la clase política mafiosa que ha permitido al crimen organizado apoderarse del sistema de justicia.",
    "La criminalidad en nuestro país tiene un pacto de protección e impunidad con un sector importante de la clase política mafiosa liderada por la bancada fujimorista y sus aliados",
    "Dimensión Institucional — 3.2 Seguridad Ciudadana — Situación Actual",
    118, 118
))

# r-seguridad-003: Datos cuantitativos pérdidas por corrupción / homicidios
nuevas.append(mk(
    "r-seguridad-003", "seguridad", "diagnostico", "MEDIA",
    "Diagnóstico cuantitativo: pérdidas económicas por corrupción de 24,268 millones de soles en 2023 (~6,500 millones USD) y disparo paralelo de asesinatos y violencia organizada.",
    "Las pérdidas económicas por corrupción alcanzaron en el año 2023 unos 24,268 millones de soles (aprox. 6,500 millones de dólares), mientras que los asesinatos y la violencia organizada se dispararon en paralelo",
    "Dimensión Institucional — 3.2 Seguridad Ciudadana — Situación Actual",
    118, 118,
    meta="Pérdidas por corrupción 2023: S/ 24,268 millones (~USD 6,500 M)"
))

# r-seguridad-004: Datos extorsión 2026
nuevas.append(mk(
    "r-seguridad-004", "seguridad", "diagnostico", "MEDIA",
    "Diagnóstico de crisis de extorsión: 5,609 casos de extorsión y 936 homicidios vinculados a sicariato/extorsión entre enero y mayo de 2026; 21% de peruanos ha sufrido extorsión.",
    "Entre enero y mayo de 2026 se registraron 5,609 casos de extorsión y 936 casos de homicidios vinculados al sicariato y extorsión. Además, El 21% de los peruanos ha sufrido extorsión",
    "Dimensión Institucional — 3.2 Seguridad Ciudadana — Situación Actual",
    118, 118,
    meta="Ene-May 2026: 5,609 extorsiones, 936 homicidios sicariato; 21% víctimas de extorsión"
))

# r-seguridad-005: Pacto Nacional por la Justicia
nuevas.append(mk(
    "r-seguridad-005", "seguridad", "propuesta", "ALTA",
    "Propuesta ancla: convocar a un Pacto Nacional por la Justicia contra la captura criminal del Estado.",
    "Convocatoria a un Pacto Nacional por la Justicia, contra la captura criminal del Estado",
    "Dimensión Institucional — 3.2 Seguridad Ciudadana — Medidas Propuestas",
    122, 122
))

# r-seguridad-006: Derogar leyes pro-crimen
nuevas.append(mk(
    "r-seguridad-006", "seguridad", "propuesta", "ALTA",
    "Derogar las normas pro-crimen (Leyes 31751, 31990, 32108, 32107, 32182, 32181, 32326) y conformar una comisión de revisión normativa para facilitar la lucha contra el crimen organizado.",
    "Derogar las normas pro-crimen, leyes N° 31751, 31990, 32108, 32107, 32182, 32181, 32326 y formación de una comisión de revisión normativa que facilite la Lucha contra el Crimen Organizado",
    "Dimensión Institucional — 3.2 Seguridad Ciudadana — Medidas Propuestas",
    122, 122
))

# r-seguridad-007: Reforma estructural PNP
nuevas.append(mk(
    "r-seguridad-007", "seguridad", "propuesta", "ALTA",
    "Reforma estructural de la Policía Nacional para recuperar el rol del policía de calle, crear una unidad de élite con inteligencia y poder de fuego para combatir el crimen organizado, y especializar el control migratorio y penitenciario.",
    "Reformar estructuralmente la Policía, la cual tenga como objetivo recuperar el rol del policía de calle o proximidad; el rol de efectivo de investigación, creando una de élite, con inteligencia y poder de fuego para combatir a las organizaciones criminales",
    "Dimensión Institucional — 3.2 Seguridad Ciudadana — Medidas Propuestas",
    122, 122
))

# r-seguridad-008: Control fronterizo a FFAA
nuevas.append(mk(
    "r-seguridad-008", "seguridad", "propuesta", "MEDIA",
    "Transferir el control fronterizo y de activos críticos nacionales a las Fuerzas Armadas para liberar y elevar el número de policías en las calles.",
    "Dar el control fronterizo y de todos los activos críticos nacionales a las Fuerzas Armadas, lo que permitirá elevar el número de policías en las calles",
    "Dimensión Institucional — 3.2 Seguridad Ciudadana — Medidas Propuestas",
    122, 122
))

# r-seguridad-009: Comando unificado contra crimen organizado
nuevas.append(mk(
    "r-seguridad-009", "seguridad", "propuesta", "MEDIA",
    "Crear el comando unificado contra el crimen organizado con comisión especial de inteligencia, unificación estratégica bajo un solo mando y el Sistema Nacional Integrado de Información Criminal.",
    "Crear el comando unificado contra el crimen organizado, con una comisión especial de inteligencia y seguimiento de la criminalidad. Unificación estratégica de las instituciones en el campo de la inteligencia bajo un solo mando, creación del Sistema Nacional Integrado de Información Criminal",
    "Dimensión Institucional — 3.2 Seguridad Ciudadana — Medidas Propuestas",
    122, 122
))

# r-seguridad-010: META — 20 mil efectivos / 1 por 220 habitantes
nuevas.append(mk(
    "r-seguridad-010", "seguridad", "meta", "ALTA",
    "Meta cuantitativa: incrementar en 20 mil los efectivos policiales en los primeros tres años, alcanzando un ratio de un efectivo de seguridad por cada 220 habitantes, según lo sugiere Naciones Unidas.",
    "Incrementar en 20 mil los efectivos para la seguridad dentro de los primeros tres años, reasignando al personal policial hacia los distritos más poblados, con la meta concreta de alcanzar un efectivo de seguridad por cada 220 habitantes",
    "Dimensión Institucional — 3.2 Seguridad Ciudadana — Medidas Propuestas",
    123, 123,
    meta="+20,000 efectivos PNP en 3 años; ratio 1 policía/220 habitantes"
))

# r-seguridad-011: Polígrafo obligatorio PNP
nuevas.append(mk(
    "r-seguridad-011", "seguridad", "propuesta", "BAJA",
    "Hacer obligatoria la prueba de polígrafo para procesos de admisión de la Policía Nacional así como para la asignación de cargos.",
    "Hacer obligatorio la prueba de polígrafo para procesos de admisión de la PNP, así como para asignación de cargos",
    "Dimensión Institucional — 3.2 Seguridad Ciudadana — Medidas Propuestas",
    123, 123
))

# r-seguridad-012: Bono Anticrimen
nuevas.append(mk(
    "r-seguridad-012", "seguridad", "propuesta", "BAJA",
    "Implementar el Bono Anticrimen para investigadores criminales y aumentar el pago de Plan Celador a 20 soles por hora.",
    "Implementar el Bono Anticrimen para investigadores criminales y aumentando el pago de Plan Celador (compra de día franco) a 20 soles por hora",
    "Dimensión Institucional — 3.2 Seguridad Ciudadana — Medidas Propuestas",
    123, 123,
    meta="Plan Celador: S/ 20/hora"
))

# r-seguridad-013: Mejorar percepción de seguridad 15 puntos
nuevas.append(mk(
    "r-seguridad-013", "seguridad", "meta", "MEDIA",
    "Meta: mejorar en 15 puntos porcentuales el Índice de percepción de seguridad vecinal.",
    "Mejorar en 15 puntos porcentuales el Índice de la percepción de seguridad vecinal",
    "Dimensión Institucional — 3.2 Seguridad Ciudadana — Medidas Propuestas",
    125, 125,
    meta="+15 puntos porcentuales en Índice de percepción de seguridad vecinal"
))

# r-seguridad-014: Construcción 5 mega-cárceles
nuevas.append(mk(
    "r-seguridad-014", "seguridad", "meta", "MEDIA",
    "Meta: construir cinco nuevas mega-cárceles con los mayores estándares de seguridad para descongestionar el sistema penitenciario.",
    "Construcción de cinco nuevas mega-cárceles con los mayores estándares de seguridad para descongestionar el sistema penitenciario",
    "Dimensión Institucional — 3.2 Seguridad Ciudadana — Medidas Propuestas",
    127, 127,
    meta="5 nuevas mega-cárceles"
))

# r-seguridad-015: Inhabilitación funcionarios sentenciados por corrupción
nuevas.append(mk(
    "r-seguridad-015", "seguridad", "propuesta", "MEDIA",
    "Aprobar ley que establezca la inhabilitación para trabajar en el Estado de los funcionarios públicos con sentencia condenatoria por corrupción.",
    "Aprobar una ley que establezca que los funcionarios públicos con sentencia condenatoria por corrupción sean inhabilitados para trabajar el Estado",
    "Dimensión Institucional — 3.2 Seguridad Ciudadana — Medidas Propuestas",
    125, 125
))

# =====================================================================
# 3.3 JUSTICIA Y DERECHOS HUMANOS (líneas 127-135) — tema: justicia
# Tema nuevo en Roberto: empieza en 001
# =====================================================================

# r-justicia-001: Compromiso DDHH y memoria
nuevas.append(mk(
    "r-justicia-001", "justicia", "principio", "ALTA",
    "Compromiso programático con la defensa de los derechos humanos, la búsqueda de personas desaparecidas, el cumplimiento de sentencias y reparaciones, y la reconciliación como política pública: la justicia y la memoria como cimiento de la República.",
    "asumimos un compromiso firme con la defensa de los derechos humanos, la búsqueda humanitaria de las personas desaparecidas, el cumplimiento de las sentencias que hacen justicia y devuelven la verdad a las víctimas, el pago efectivo de las reparaciones y asumimos el rol de reconciliación como política pública",
    "Dimensión Institucional — 3.3 Justicia y Derechos Humanos — Presentación",
    127, 127
))

# r-justicia-002: Diagnóstico debilitamiento Sist. Interamericano
nuevas.append(mk(
    "r-justicia-002", "justicia", "diagnostico", "ALTA",
    "Diagnóstico del debilitamiento del estándar peruano frente al Sistema Interamericano por las recientes leyes de amnistía y prescripción de crímenes de lesa humanidad (Leyes 32419 y 32107).",
    "En los últimos años ese estándar se ha debilitado con normas que se apartan del Estado de derecho —como las recientes leyes de amnistía y de prescripción de crímenes de lesa humanidad (Leyes 32419 y 32107)",
    "Dimensión Institucional — 3.3 Justicia y Derechos Humanos — Situación Actual",
    129, 129
))

# r-justicia-003: Diagnóstico víctimas conflicto armado interno
nuevas.append(mk(
    "r-justicia-003", "justicia", "diagnostico", "MEDIA",
    "Diagnóstico de la deuda con víctimas del conflicto armado interno (1980-2000): de 70,000 víctimas, el RENADE contabiliza 22,551 personas desaparecidas, la mayoría aún sin localizar.",
    "Subsiste la deuda con las víctimas del conflicto armado interno: de las cerca de 70 000 víctimas que dejó entre 1980 y 2000, el RENADE contabiliza 22 551 personas desaparecidas, la mayoría aún sin localizar",
    "Dimensión Institucional — 3.3 Justicia y Derechos Humanos — Situación Actual",
    131, 131,
    meta="70,000 víctimas conflicto 1980-2000; 22,551 desaparecidas en RENADE"
))

# r-justicia-004: Diagnóstico hacinamiento penitenciario
nuevas.append(mk(
    "r-justicia-004", "justicia", "diagnostico", "MEDIA",
    "Diagnóstico de crisis penitenciaria estructural: sobrepoblación cercana al 147% que el Tribunal Constitucional ordenó resolver, uso inadecuado de prisión preventiva y deficiencias de infraestructura.",
    "El sistema penitenciario atraviesa una crisis estructural: una sobrepoblación cercana al 147 % que el propio Tribunal Constitucional ordenó resolver, el uso inadecuado de la prisión preventiva",
    "Dimensión Institucional — 3.3 Justicia y Derechos Humanos — Situación Actual",
    131, 131,
    meta="Sobrepoblación penitenciaria ~147%"
))

# r-justicia-005: Cumplimiento Corte IDH
nuevas.append(mk(
    "r-justicia-005", "justicia", "propuesta", "ALTA",
    "Garantizar el cumplimiento de las decisiones de la Corte IDH, adecuando la institucionalidad y marco jurídico nacional al Sistema Interamericano y reafirmando la permanencia del Perú en él.",
    "Garantizar el cumplimiento de las decisiones de la Corte IDH, adecuando la institucionalidad y el marco jurídico nacional a las exigencias del Sistema Interamericano y reafirmando la permanencia del Perú en él",
    "Dimensión Institucional — 3.3 Justicia y Derechos Humanos — Medidas Propuestas",
    133, 133
))

# r-justicia-006: Derogar leyes de amnistía e impunidad
nuevas.append(mk(
    "r-justicia-006", "justicia", "propuesta", "ALTA",
    "Impulsar ante el Congreso la derogación de las leyes de impunidad y amnistía para violadores de derechos humanos y corruptos, en particular las Leyes 32107 y 32419.",
    "Impulsar ante el Congreso la derogación de las leyes de impunidad y amnistía para violadores de derechos humanos y corruptos, en particular las Leyes 32107 y 32419",
    "Dimensión Institucional — 3.3 Justicia y Derechos Humanos — Medidas Propuestas",
    133, 133
))

# r-justicia-007: Comisión de la Verdad sobre protestas 2022-2023
nuevas.append(mk(
    "r-justicia-007", "justicia", "propuesta", "ALTA",
    "Crear mediante decreto una Comisión de la Verdad sobre las graves violaciones cometidas en las protestas de 2022 y 2023 para esclarecer los hechos, promover la sanción de responsables y dignificar a las víctimas.",
    "Crear, mediante decreto, una Comisión de la Verdad sobre las graves violaciones cometidas en las protestas de 2022 y 2023, que esclarezca los hechos y promueva, ante el Ministerio Público y el Poder Judicial, la sanción de los responsables",
    "Dimensión Institucional — 3.3 Justicia y Derechos Humanos — Medidas Propuestas",
    133, 133
))

# r-justicia-008: Derogar DL 1589 (criminalización protesta)
nuevas.append(mk(
    "r-justicia-008", "justicia", "propuesta", "MEDIA",
    "Derogar el Decreto Legislativo 1589 (diciembre 2023) que criminalizó la protesta social agravando los delitos de entorpecimiento del transporte (art. 283 CP) y disturbios (art. 315 CP).",
    "Impulsar la derogación del Decreto Legislativo 1589 (diciembre de 2023), que criminalizó la protesta social al agravar los delitos de entorpecimiento del transporte (art. 283 CP) y disturbios (art. 315 CP)",
    "Dimensión Institucional — 3.3 Justicia y Derechos Humanos — Medidas Propuestas",
    133, 133
))

# r-justicia-009: Fortalecer Dirección Búsqueda Desaparecidos
nuevas.append(mk(
    "r-justicia-009", "justicia", "propuesta", "MEDIA",
    "Fortalecer la Dirección General de Búsqueda de Personas Desaparecidas (Ley 30470) con más profesionales, presupuesto sostenido y capacidad forense para investigar casos y entregar los restos a las familias.",
    "Fortalecer, desde el Ejecutivo, la Dirección General de Búsqueda de Personas Desaparecidas (Ley 30470) con más profesionales, presupuesto sostenido y capacidad forense",
    "Dimensión Institucional — 3.3 Justicia y Derechos Humanos — Medidas Propuestas",
    135, 135
))

# r-justicia-010: Plan Integral de Reparaciones
nuevas.append(mk(
    "r-justicia-010", "justicia", "propuesta", "MEDIA",
    "Priorizar las reparaciones a víctimas y familias en el marco del Plan Integral de Reparaciones (Ley 28592) con cobertura integral de salud y pensiones por discapacidad, viudez y orfandad.",
    "Priorizar las reparaciones a las víctimas y sus familias en el marco del Plan Integral de Reparaciones (Ley 28592) —cobertura integral de salud y pensiones por discapacidad, viudez y orfandad—, ejecutadas en el plazo más inmediato",
    "Dimensión Institucional — 3.3 Justicia y Derechos Humanos — Medidas Propuestas",
    135, 135
))

# r-justicia-011: Justicia de paz - ampliación
nuevas.append(mk(
    "r-justicia-011", "justicia", "meta", "MEDIA",
    "Meta: ampliar la justicia de paz con 500 juzgados de paz letrados y 1000 juzgados de paz no letrados adicionales para cubrir todos los distritos del país.",
    "Impulsar, junto con el Poder Judicial, la ampliación de la justicia de paz —500 juzgados de paz letrados y 1000 juzgados de paz no letrados adicionales— para cubrir todos los distritos del país",
    "Dimensión Institucional — 3.3 Justicia y Derechos Humanos — Medidas Propuestas",
    135, 135,
    meta="+500 juzgados paz letrados; +1000 juzgados paz no letrados"
))

# r-justicia-012: Comisión de Reforma integral de Justicia
nuevas.append(mk(
    "r-justicia-012", "justicia", "propuesta", "ALTA",
    "Instalar una Comisión de Reforma Integral de la Justicia integrada por magistrados, estudiosos y representantes ciudadanos para rediseñar el sistema, considerar la elección de jueces, proteger la independencia judicial e introducir jurados en procedimientos penales.",
    "Se instalará una Comisión de Reforma integral de la Justicia, integrada por magistrados, estudiosos y representantes de la ciudadanía, con el fin de rediseñar el sistema de acceso a la justicia, considerar la elección de los jueces, proteger la independencia del poder judicial",
    "Dimensión Institucional — 3.3 Justicia y Derechos Humanos — Medidas Propuestas",
    135, 135
))

# r-justicia-013: Reducir hacinamiento penitenciario
nuevas.append(mk(
    "r-justicia-013", "justicia", "propuesta", "MEDIA",
    "Reducir sustancialmente el hacinamiento penitenciario en cumplimiento del mandato del Tribunal Constitucional, con inversión en infraestructura, racionalización de la prisión preventiva y reformas en beneficios penitenciarios.",
    "Reducir sustancialmente el hacinamiento penitenciario, en cumplimiento del mandato del Tribunal Constitucional, con inversión en infraestructura, racionalización de la prisión preventiva y reformas en beneficios penitenciarios",
    "Dimensión Institucional — 3.3 Justicia y Derechos Humanos — Medidas Propuestas",
    135, 135
))

# =====================================================================
# 3.4 REORGANIZACIÓN DEL SISTEMA ANTICORRUPCIÓN (líneas 135-143) — tema: corrupcion
# Continúa desde r-corrupcion-001
# =====================================================================

# r-corrupcion-002: Diagnóstico copamiento e impunidad
nuevas.append(mk(
    "r-corrupcion-002", "corrupcion", "diagnostico", "ALTA",
    "Diagnóstico del copamiento del Estado por la corrupción: los corruptos han logrado copar todas las entidades estatales y la impunidad multiplica el mal uso de recursos públicos.",
    "La corrupción nos ha ganado momentáneamente la batalla. Los corruptos han logrado copar todas las entidades del Estado y, aunque vemos sus actos en tiempo real, hay total",
    "Dimensión Institucional — 3.4 Sistema Anticorrupción — Situación Actual",
    137, 138
))

# r-corrupcion-003: Diagnóstico Contraloría y OCI inoperativos
nuevas.append(mk(
    "r-corrupcion-003", "corrupcion", "diagnostico", "MEDIA",
    "Diagnóstico de inoperancia del sistema anticorrupción: la Contraloría, los OCI, la Secretaría de Integridad Pública y el sistema de justicia están pintados; el Congreso decide qué y a quién se investiga.",
    "La Contraloría General de la República, los órganos de control institucional, la Secretaría de Integridad Pública y el sistema de justicia, están pintados",
    "Dimensión Institucional — 3.4 Sistema Anticorrupción — Situación Actual",
    139, 139
))

# r-corrupcion-004: Diagnóstico OCDE - sistema desarticulado
nuevas.append(mk(
    "r-corrupcion-004", "corrupcion", "diagnostico", "BAJA",
    "Diagnóstico OCDE/CEPLAN: pese al Plan Nacional de Integridad y Lucha contra la Corrupción, el sistema funciona desarticulado entre Ejecutivo, Congreso, Poder Judicial, Contraloría y gobiernos subnacionales.",
    "La OCDE (2025) y CEPLAN señalan que, pese a la existencia del Plan Nacional de Integridad y Lucha contra la Corrupción (PNILC), el sistema anticorrupción funciona de manera desarticulada entre Ejecutivo, Congreso, Poder Judicial, Contraloría y gobiernos subnacionales",
    "Dimensión Institucional — 3.4 Sistema Anticorrupción — Situación Actual",
    139, 139
))

# r-corrupcion-005: Derogar leyes pro corrupción
nuevas.append(mk(
    "r-corrupcion-005", "corrupcion", "propuesta", "ALTA",
    "Derogar leyes pro corrupción: Leyes 31751 y 32104 (reducen plazos de prescripción), Ley 31990 (debilita colaboración eficaz), Ley 32108 (redefine organización criminal) y Ley 32054 (exime a partidos de responsabilidad legal).",
    "Derogar las leyes pro corrupción que han favorecido su avance: Leyes N° 31751 y N° 32104, que modifican el Código Penal y el Nuevo Código Procesal Penal para reducir los plazos de prescripción de delitos; Ley N° 31990, que debilita el sistema de colaboración eficaz",
    "Dimensión Institucional — 3.4 Sistema Anticorrupción — Medidas Propuestas",
    141, 141
))

# r-corrupcion-006: Verificación obligatoria de integridad
nuevas.append(mk(
    "r-corrupcion-006", "corrupcion", "propuesta", "MEDIA",
    "Establecer verificación obligatoria de integridad previa a la designación y de manera periódica de todo alto funcionario, incluyendo al Ministerio Público y al Poder Judicial, siguiendo un criterio de riesgos.",
    "Establecer verificación obligatoria de integridad previamente a la designación y de manera periódica de todo alto funcionario, incluyendo al Ministerio Público y al Poder Judicial, siguiendo un criterio de riesgos",
    "Dimensión Institucional — 3.4 Sistema Anticorrupción — Medidas Propuestas",
    141, 141
))

# r-corrupcion-007: Cambiar elección TC y JNJ - quitar poder al Congreso
nuevas.append(mk(
    "r-corrupcion-007", "corrupcion", "propuesta", "ALTA",
    "Contrarrestar el copamiento de entidades públicas cambiando las reglas de elección de los miembros del Tribunal Constitucional y la Junta Nacional de Justicia, quitando poder al Congreso en estas decisiones.",
    "Contrarrestar el copamiento de las entidades públicas para romper el círculo de la impunidad. Cambiar las reglas de elección de los miembros del Tribunal Constitucional y la Junta Nacional de Justicia, quitando poder al Congreso en estas decisiones",
    "Dimensión Institucional — 3.4 Sistema Anticorrupción — Medidas Propuestas",
    141, 141
))

# r-corrupcion-008: Protección a denunciantes
nuevas.append(mk(
    "r-corrupcion-008", "corrupcion", "propuesta", "MEDIA",
    "Fortalecer la protección a denunciantes con mecanismos anti-represalias: confidencialidad, canales seguros, medidas cautelares, asesoría legal, protección laboral, reubicación y sanciones a represalias.",
    "Fortalecer protección a denunciantes con mecanismos anti-represalias (confidencialidad, canales seguros, medidas cautelares, asesoría legal, protección laboral, reubicación cuando corresponda y sanciones a represalias)",
    "Dimensión Institucional — 3.4 Sistema Anticorrupción — Medidas Propuestas",
    143, 143
))

# r-corrupcion-009: Sistema Nacional de Integridad y Transparencia (SNIT)
nuevas.append(mk(
    "r-corrupcion-009", "corrupcion", "propuesta", "MEDIA",
    "Crear el Sistema Nacional de Integridad y Transparencia (SNIT) que integre políticas de integridad, transparencia, acceso a la información y protección de datos según propuesta OCDE.",
    "Crear el Sistema Nacional de Integridad y Transparencia (SNIT), que integre las políticas de integridad, transparencia, acceso a la información y protección de datos (propuesta de la OCDE)",
    "Dimensión Institucional — 3.4 Sistema Anticorrupción — Medidas Propuestas",
    143, 143
))

# =====================================================================
# 3.5 DEMOCRACIA SOCIAL DE LOS PUEBLOS (líneas 143-151) — tema: constitucion
# =====================================================================

# r-constitucion-011: Principio democracia popular participativa
nuevas.append(mk(
    "r-constitucion-011", "constitucion", "principio", "ALTA",
    "Principio: la nueva democracia debe ser radicalmente distinta —popular, inclusiva y participativa— construida desde abajo, desde las comunidades, trabajadores y sectores históricamente excluidos.",
    "la nueva democracia debe ser radicalmente distinta: popular, inclusiva y participativa, construida desde abajo, desde las comunidades, los trabajadores y los sectores históricamente excluidos",
    "Dimensión Institucional — 3.5 Democracia Social de los Pueblos — Situación Actual",
    145, 145
))

# r-constitucion-012: Recuperar equilibrio de poderes / anular incapacidad moral
nuevas.append(mk(
    "r-constitucion-012", "constitucion", "propuesta", "ALTA",
    "Recuperar el equilibrio de poderes restituyendo facultades al Ejecutivo para que el Senado no sea el epicentro del poder sin control y anular la figura de incapacidad moral permanente como causal de vacancia.",
    "Recuperar el equilibrio de poderes, restituyendo facultades al Ejecutivo para que el Senado no sea el epicentro del poder sin control. Anular la figura de la incapacidad moral permanente como causal de vacancia",
    "Dimensión Institucional — 3.5 Democracia Social de los Pueblos — Medidas Propuestas",
    149, 149
))

# r-constitucion-013: Reforma Ley Organizaciones Políticas
nuevas.append(mk(
    "r-constitucion-013", "constitucion", "propuesta", "MEDIA",
    "Reformar la Ley de Organizaciones Políticas (Ley 28094) en sus requisitos de constitución e inscripción para prohibir el comercio de nombres y registros, prohibir el transfuguismo y elevar el número mínimo de integrantes de grupos parlamentarios.",
    "una reforma de la Ley de Organizaciones Políticas (Ley 28094) en sus requisitos de constitución e inscripción (artículos 4 al 10), que prohíba el comercio de nombres y registros y el transfuguismo",
    "Dimensión Institucional — 3.5 Democracia Social de los Pueblos — Medidas Propuestas",
    149, 149
))

# r-constitucion-014: Reforma Ley 26300 y derogar Ley 31399
nuevas.append(mk(
    "r-constitucion-014", "constitucion", "propuesta", "MEDIA",
    "Modificar la Ley de los Derechos de Participación y Control Ciudadanos (Ley 26300) para reducir barreras y derogar la Ley 31399 que condiciona a aprobación del Congreso la convocatoria a referéndum para reforma constitucional.",
    "Promover la modificación de la Ley de los Derechos de Participación y Control Ciudadanos (Ley 26300) para reducir las barreras formales y facilitar el acceso de la población a los mecanismos de participación y control, e impulsar la derogación de la Ley 31399",
    "Dimensión Institucional — 3.5 Democracia Social de los Pueblos — Medidas Propuestas",
    149, 149
))

# r-constitucion-015: Paridad sustantiva 45% mujeres en cargos directivos
nuevas.append(mk(
    "r-constitucion-015", "constitucion", "meta", "MEDIA",
    "Meta: garantizar que al menos el 45% de los cargos directivos de la administración pública nacional sean ocupados por mujeres mediante concursos meritocráticos, en coordinación con SERVIR y MIMP.",
    "garantizar que al menos el 45 % de los cargos directivos de la administración pública nacional sean ocupados por mujeres mediante concursos meritocráticos",
    "Dimensión Institucional — 3.5 Democracia Social de los Pueblos — Medidas Propuestas",
    149, 149,
    meta="≥45% de cargos directivos en administración pública nacional ocupados por mujeres"
))

# r-constitucion-016: Renovación parcial escalonada bicameral
nuevas.append(mk(
    "r-constitucion-016", "constitucion", "propuesta", "MEDIA",
    "Promover dentro del diseño bicameral (Ley 31988) la reforma constitucional que establezca la renovación parcial y escalonada de la representación parlamentaria, empezando por el Senado.",
    "Promover, dentro del nuevo diseño bicameral (Ley 31988), la reforma constitucional que establezca la renovación parcial y escalonada de la representación parlamentaria —empezando por el Senado",
    "Dimensión Institucional — 3.5 Democracia Social de los Pueblos — Medidas Propuestas",
    151, 151
))

# =====================================================================
# 3.6 REFORMA DEL PODER EJECUTIVO (líneas 151-159) — tema: orden_juridico (administrativo)
# Tema nuevo en Roberto: empieza en 001
# =====================================================================

# r-orden_juridico-001: Diagnóstico deterioro Ejecutivo
nuevas.append(mk(
    "r-orden_juridico-001", "orden_juridico", "diagnostico", "ALTA",
    "Diagnóstico del deterioro extremo del Poder Ejecutivo: ha perdido legitimidad, capacidad de toma de decisiones y se ha alejado de la gente; opera con capacidades insuficientes para priorizar, coordinar y asegurar ejecución estratégica.",
    "Actualmente el Poder Ejecutivo del país se ha deteriorado en extremo. Ha perdido legitimidad, capacidad de toma de decisiones y se ha alejado de la gente",
    "Dimensión Institucional — 3.6 Reforma del Poder Ejecutivo — Situación Actual",
    151, 151
))

# r-orden_juridico-002: Muerte cruzada
nuevas.append(mk(
    "r-orden_juridico-002", "orden_juridico", "propuesta", "MEDIA",
    "Aprobar la muerte cruzada si se presenta una crisis insalvable, para que sea la voluntad popular la que defina el rumbo del país.",
    "Aprobar la muerte cruzada si se presenta una crisis insalvable para que sea la voluntad popular la que defina el rumbo del país",
    "Dimensión Institucional — 3.6 Reforma del Poder Ejecutivo — Medidas Propuestas",
    151, 151
))

# r-orden_juridico-003: Acuerdo de Escazú y Convenio 169
nuevas.append(mk(
    "r-orden_juridico-003", "orden_juridico", "propuesta", "ALTA",
    "Garantizar la protección de las comunidades indígenas de la Amazonía y el Ande con respeto irrestricto al Convenio 169 de la OIT y firmar el Acuerdo de Escazú.",
    "Garantizar la protección de las comunidades indígenas de la Amazonía y el Ande, con respeto irrestricto al Convenio 169 de la OIT y firmar el Acuerdo de Escazú",
    "Dimensión Institucional — 3.6 Reforma del Poder Ejecutivo — Medidas Propuestas",
    153, 153
))

# r-orden_juridico-004: Simplificación DECIDIR
nuevas.append(mk(
    "r-orden_juridico-004", "orden_juridico", "propuesta", "MEDIA",
    "Implementar la estrategia de simplificación del proceso de decisiones públicas (DECIDIR) elaborada por un grupo especial de trabajo de la Presidencia, eliminando instancias innecesarias, reprocesos y bloqueos en los sistemas administrativos.",
    "Implementación de una estrategia de simplificación del proceso de decisiones públicas (DECIDIR) elaborada por un grupo especial de trabajo de la Presidencia, eliminando instancias innecesarias, reprocesos, bloqueos",
    "Dimensión Institucional — 3.6 Reforma del Poder Ejecutivo — Medidas Propuestas",
    153, 153
))

# r-orden_juridico-005: Modificar Ley Orgánica Contraloría
nuevas.append(mk(
    "r-orden_juridico-005", "orden_juridico", "propuesta", "MEDIA",
    "Modificar la Ley Orgánica de la Contraloría (27785) para aumentar el foco de control en finanzas y eliminar la injerencia de contralores en tareas de dirección, planeación y control técnico propias de cada sector.",
    "Se modificará la Ley Orgánica de Contraloría (27785), para aumentar el foco de control en el manejo de las finanzas y los recursos públicos y eliminar la injerencia de los contralores en las tareas de dirección, planeación y control",
    "Dimensión Institucional — 3.6 Reforma del Poder Ejecutivo — Medidas Propuestas",
    153, 153
))

# r-orden_juridico-006: Creación Ministerio de Ciencia y Tecnología
nuevas.append(mk(
    "r-orden_juridico-006", "orden_juridico", "propuesta", "MEDIA",
    "Crear el Ministerio de Ciencia y Tecnología orientado al fomento de la investigación científica y la innovación tecnológica articuladas al Plan de Transformación Productiva Nacional, con un fondo financiado por el 5% del canon minero.",
    "Creación del Ministerio de Ciencia y Tecnología. El objetivo de este Ministerio será el Fomento de la investigación científica y de la innovación tecnológica",
    "Dimensión Institucional — 3.6 Reforma del Poder Ejecutivo — Medidas Propuestas",
    153, 153,
    meta="Fondo de innovación tecnológica financiado con 5% del canon minero"
))

# r-orden_juridico-007: Autonomía Bomberos Voluntarios
nuevas.append(mk(
    "r-orden_juridico-007", "orden_juridico", "propuesta", "BAJA",
    "Brindar autonomía al Cuerpo General de Bomberos Voluntarios del Perú para que no dependan del MININTER, financiando su presupuesto con un impuesto a la electricidad y un 4% a pólizas de seguros contra incendios.",
    "Se le brindará autonomía al Cuerpo General de Bomberos Voluntarios del Perú, para que no dependan del MININTER",
    "Dimensión Institucional — 3.6 Reforma del Poder Ejecutivo — Medidas Propuestas",
    159, 159,
    meta="Financiamiento: impuesto a electricidad (excepto <120 KWh) + 4% a pólizas de seguros contra incendios"
))

# =====================================================================
# 3.7 DESCENTRALIZACIÓN (líneas 159-164) — tema: orden_juridico
# =====================================================================

# r-orden_juridico-008: Diagnóstico descentralización paralizada
nuevas.append(mk(
    "r-orden_juridico-008", "orden_juridico", "diagnostico", "ALTA",
    "Diagnóstico: desde 2007 la descentralización ha sido abandonada por el Gobierno Nacional; el Consejo Nacional de Descentralización fue anulado por DS 007-2007-PCM inconstitucionalmente, generando gobiernos regionales débiles y desarrollo territorial desigual.",
    "Desde el año 2007, en que se aprobó la Ley Orgánica del Poder Ejecutivo (LOPE), ley 29158, la descentralización ha sido abandonada por el Gobierno Nacional. El Consejo Nacional de Descentralización (CND) fue anulado",
    "Dimensión Institucional — 3.7 Descentralización — Situación Actual",
    159, 159
))

# r-orden_juridico-009: Diagnóstico descentralización fiscal incompleta
nuevas.append(mk(
    "r-orden_juridico-009", "orden_juridico", "diagnostico", "MEDIA",
    "Diagnóstico: paradoja de la descentralización; se transfirieron funciones y responsabilidades pero no se consolidó una verdadera descentralización fiscal ni institucionalidad territorial capaz de articular planificación, inversión y control ciudadano.",
    "se transfirieron funciones y responsabilidades a gobiernos regionales y locales, pero no se consolidó una verdadera descentralización fiscal, ni una institucionalidad territorial capaz de articular planificación, inversión, abastecimiento, control ciudadano e innovación productiva",
    "Dimensión Institucional — 3.7 Descentralización — Situación Actual",
    159, 159
))

# r-orden_juridico-010: Datos presupuesto subnacional 36.24%
nuevas.append(mk(
    "r-orden_juridico-010", "orden_juridico", "diagnostico", "BAJA",
    "Diagnóstico cuantitativo: los gobiernos descentralizados solo manejan al año 2026 el 36.24% del total del presupuesto público; el Gobierno Nacional administra la mayor parte.",
    "Los Gobiernos descentralizados, solo manejan, al año 2026, el 36.24% del total del presupuesto público",
    "Dimensión Institucional — 3.7 Descentralización — Situación Actual",
    161, 161,
    meta="Gobiernos subnacionales manejan 36.24% del presupuesto público (2026)"
))

# r-orden_juridico-011: Restablecer CND
nuevas.append(mk(
    "r-orden_juridico-011", "orden_juridico", "propuesta", "ALTA",
    "Restablecer las funciones del Consejo Nacional de Descentralización (CND) creado por el art. 23.1 de la Ley 27783 (Ley de Bases de la Descentralización), derogando el DS 007-2007-PCM para reasumir la función de promoción del proceso de descentralización.",
    "Restablecer las funciones del Consejo Nacional de Descentralización (CND), creado por el artículo 23.1 de la ley 27783 (Ley De Bases de la Descentralización), derogando el D.S 007-2007-PCM",
    "Dimensión Institucional — 3.7 Descentralización — Medidas Propuestas",
    161, 161
))

# r-orden_juridico-012: FONCOMUN y FONCOR / proporción fija IGV
nuevas.append(mk(
    "r-orden_juridico-012", "orden_juridico", "propuesta", "MEDIA",
    "Fortalecer el FONCOMUN y el FONCOR mediante transferencias automáticas vinculadas a una proporción fija del IGV, garantizando financiamiento estable para gobiernos locales y regionales.",
    "Fortalecer el FONCOMUN y el FONCOR mediante transferencias automáticas vinculadas a una proporción fija del IGV, garantizando financiamiento estable para gobiernos locales y regionales",
    "Dimensión Institucional — 3.7 Descentralización — Medidas Propuestas",
    163, 163,
    meta="FONCOMUN y FONCOR: proporción fija del IGV"
))

# r-orden_juridico-013: Fondo de estabilización del canon
nuevas.append(mk(
    "r-orden_juridico-013", "orden_juridico", "propuesta", "MEDIA",
    "Crear un fondo de estabilización del canon y regalías que permita ahorrar en ciclos de bonanza y sostener la inversión pública cuando caen los precios internacionales, mejorando la redistribución.",
    "Crear un fondo de estabilización del canon y regalías, que permita ahorrar en ciclos de bonanza y sostener la inversión pública cuando caen los precios internacionales",
    "Dimensión Institucional — 3.7 Descentralización — Medidas Propuestas",
    163, 163
))

# r-orden_juridico-014: Ministerio de Planificación y Desarrollo Territorial
nuevas.append(mk(
    "r-orden_juridico-014", "orden_juridico", "propuesta", "MEDIA",
    "Articular la planificación, programación multianual, inversión pública y abastecimiento en un nuevo Ministerio de Planificación y Desarrollo Territorial.",
    "Articular planificación, programación multianual, inversión pública y abastecimiento en un nuevo Ministerio de Planificación y Desarrollo Territorial",
    "Dimensión Institucional — 3.7 Descentralización — Medidas Propuestas",
    163, 163
))

# r-orden_juridico-015: Carrera pública meritocrática descentralizada
nuevas.append(mk(
    "r-orden_juridico-015", "orden_juridico", "propuesta", "BAJA",
    "Fortalecimiento de capacidades en los tres niveles de gobierno y establecimiento de la carrera pública meritocrática que otorgue estabilidad a servidores y permita desarrollo profesional no dependiente de la capital.",
    "Fortalecimiento de capacidades en los tres niveles de gobierno y establecimiento de la carrera pública meritocrática que otorgue estabilidad a las y los servidores",
    "Dimensión Institucional — 3.7 Descentralización — Medidas Propuestas",
    163, 163
))

# r-orden_juridico-016: Cerrar brechas digitales rurales
nuevas.append(mk(
    "r-orden_juridico-016", "orden_juridico", "propuesta", "BAJA",
    "Cerrar las brechas digitales rurales mediante conectividad, alfabetización digital y plataformas de servicios públicos para descentralizar la presencia del Estado.",
    "Cerrar brechas digitales rurales mediante conectividad, alfabetización digital y plataformas de servicios públicos",
    "Dimensión Institucional — 3.7 Descentralización — Medidas Propuestas",
    164, 164
))

# =====================================================================
# Volcar al JSON y guardar
# =====================================================================
ruta = Path("00-Sistema/datos/propuestas.json")
d = json.loads(ruta.read_text(encoding="utf-8"))
print(f"Antes: {len(d['propuestas'])} propuestas")
print(f"Nuevas a agregar: {len(nuevas)}")

# IDs únicos check
ids_existentes = {p["id"] for p in d["propuestas"]}
duplicados = [n["id"] for n in nuevas if n["id"] in ids_existentes]
if duplicados:
    print(f"ERROR: IDs duplicados: {duplicados}")
    raise SystemExit(1)

ids_nuevos = [n["id"] for n in nuevas]
if len(ids_nuevos) != len(set(ids_nuevos)):
    print("ERROR: IDs duplicados dentro de nuevas")
    raise SystemExit(1)

d["propuestas"].extend(nuevas)
ruta.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Despues: {len(d['propuestas'])} propuestas")
print("OK escrito.")
