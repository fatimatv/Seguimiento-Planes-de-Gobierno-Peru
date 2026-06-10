# -*- coding: utf-8 -*-
"""Extracción de Dimensión Social - Roberto Sánchez (Task 13).

Cubre secciones 6.1 a 6.7: Salud, Educación, Violencia de Género,
Inclusión Social, Igualdad de Oportunidades, Juventud y Deporte.
"""
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
            "linea_fin": linea_fin,
        },
        "meta_cuantitativa": meta,
    }


nuevas = []

# =====================================================================
# 6.1 SALUD (líneas 285-295) — tema: salud
# =====================================================================
S61 = "Dimensión Social — 6.1 Salud"

nuevas.append(mk(
    "r-salud-001", "salud", "diagnostico", "ALTA",
    "Diagnóstico estructural: el sistema de salud peruano es fragmentado, segmentado, estratificado, desfinanciado, ineficiente, mercantilizado, corrupto y deshumanizado; la pandemia con más de 200,000 muertos develó la urgencia de su reforma.",
    "el sistema de salud actual es fragmentado, segmentado, estratificado, desfinanciado, ineficiente, dependiente, mercantilizado, corrupto y deshumanizado",
    f"{S61} — Situación Actual", 287, 287,
))

nuevas.append(mk(
    "r-salud-002", "salud", "diagnostico", "ALTA",
    "Diagnóstico de desigualdad: el gasto per cápita en salud refleja crisis sanitaria — SIS S/ 81, EsSalud S/ 1,300 y privado S/ 5,000, con muertes evitables sobre todo en el primer nivel de atención.",
    "La crisis sanitaria no solo se refleja en la desigualdad del gasto per cápita en salud del SIS (S/81), EsSalud (S/1300) y el privado (5000)",
    f"{S61} — Situación Actual", 287, 287,
    meta="Gasto per cápita: SIS S/ 81, EsSalud S/ 1,300, privado S/ 5,000",
))

nuevas.append(mk(
    "r-salud-003", "salud", "diagnostico", "ALTA",
    "Diagnóstico presupuestal: en 2022 el Perú destinó apenas 6.2% del PBI a salud, entre los más bajos de la región; presupuesto 2025 S/ 30,400 millones (12.1% del nacional) insuficiente para revertir desigualdades.",
    "En 2022, el país destinó apenas 6.2 % del Producto Bruto Interno (PBI) al sistema de salud, esa cifra lo sitúa entre los países con menor presupuesto asignado a la salud de la región",
    f"{S61} — Situación Actual", 287, 287,
    meta="Salud: 6.2% PBI; presupuesto 2025 S/ 30,400M",
))

nuevas.append(mk(
    "r-salud-004", "salud", "diagnostico", "ALTA",
    "Diagnóstico de infraestructura: en 2022, 7 de cada 10 peruanos que necesitaron atención médica no la obtuvieron; más del 70% de establecimientos tiene más de 30 años de antigüedad; 98% carece de infraestructura adecuada.",
    "en el 2022, 7 de cada 10 peruanos que necesitaron atención médica no la obtuvieron",
    f"{S61} — Situación Actual", 287, 287,
))

nuevas.append(mk(
    "r-salud-005", "salud", "diagnostico", "ALTA",
    "Diagnóstico de confianza ciudadana: solo 24% de peruanos se declara satisfecho con servicios médicos públicos; el sector Salud perdió S/ 1,751 millones por corrupción en 2022; >50 mil quejas SUSALUD en 9 meses de 2023.",
    "Hoy por hoy, solo 24% de peruanos se declara satisfecho con los servicios médicos públicos – una minoría – y apenas 30% confía en que recibirá el mejor tratamiento posible",
    f"{S61} — Situación Actual", 288, 288,
    meta="Satisfacción salud pública: 24%; corrupción 2022: S/ 1,751M",
))

nuevas.append(mk(
    "r-salud-006", "salud", "propuesta", "ALTA",
    "Salud pública universal con integración progresiva de subsistemas: las personas podrán tratarse en cualquier centro público, privado, policial o militar con costos estandarizados; integración en tres fases (0-18, 18-36, 36-60 meses).",
    "Salud pública universal para toda la población con acceso integrado a cualquiera de los centros de atención del Estado, de las Fuerzas Policiales y Militares, y del sector privado",
    f"{S61} — Medidas Propuestas", 292, 292,
))

nuevas.append(mk(
    "r-salud-007", "salud", "propuesta", "ALTA",
    "Priorizar el Nivel I de atención (atención primaria, preventiva, inmediata y cercana) para que las personas accedan sin grandes colas; descongestionar hospitales resolviendo más en la comunidad.",
    "La estrategia de salud priorizará el Nivel I de atención de salud, es decir. la atención primaria, preventiva, inmediata y cercana a la población",
    f"{S61} — Medidas Propuestas", 292, 292,
))

nuevas.append(mk(
    "r-salud-008", "salud", "propuesta", "ALTA",
    "Plan nacional de inversión hospitalaria: cada región contará con al menos un hospital moderno de alta resolución, equipado y con personal calificado; priorizar regiones con mayor brecha.",
    "Construiremos, modernizaremos e innovaremos la gestión de hospitales estratégicos en regiones priorizadas, a través de la elaboración de un plan nacional de inversión hospitalaria",
    f"{S61} — Medidas Propuestas", 292, 292,
))

nuevas.append(mk(
    "r-salud-009", "salud", "meta", "ALTA",
    "Meta financiera: lograr una inversión adicional en salud de S/ 180,000 millones para 2026-2031; incrementar el gasto en salud al 7% del PBI al finalizar el periodo; eliminar copagos y avanzar a gratuidad total.",
    "Se propone lograr una Inversión adicional en salud de S/ 180,000 millones para el periodo 2026-2031",
    f"{S61} — Medidas Propuestas", 292, 292,
    meta="Inversión salud: +S/ 180,000M (2026-2031); gasto 7% PBI; gratuidad total",
))

nuevas.append(mk(
    "r-salud-010", "salud", "meta", "ALTA",
    "Meta de prevención: 1,000 equipos territoriales de Salud en zonas con mayores riesgos sanitarios y vulnerables; 500 establecimientos de Salud Intercultural al 2031.",
    "Prevención y Promoción de la Salud (1000 equipos territoriales de Salud en zonas con mayores riesgos sanitarios y vulnerables)",
    f"{S61} — Medidas Propuestas", 292, 292,
    meta="1,000 equipos territoriales; 500 establecimientos Salud Intercultural",
))

nuevas.append(mk(
    "r-salud-011", "salud", "meta", "ALTA",
    "Meta de infraestructura: construir y/o remodelar 500 establecimientos de salud del primer nivel a nivel nacional, priorizando territorios con mayores brechas.",
    "Construir y/o remodelar quinientos (500) establecimientos de salud del primer nivel de atención a nivel nacional",
    f"{S61} — Medidas Propuestas", 293, 293,
    meta="500 establecimientos del primer nivel",
))

nuevas.append(mk(
    "r-salud-012", "salud", "meta", "ALTA",
    "Implementar 700 clínicas especializadas entre policlínicos urbanos y clínicas rurales; modelo de 'Hospital Modular' para regiones con brechas críticas (Sierra y Selva).",
    "Implementaremos 700 clínicas especializadas entre policlínicos urbanos y clínicas rurales en todo el país",
    f"{S61} — Medidas Propuestas", 293, 293,
    meta="700 clínicas especializadas",
))

nuevas.append(mk(
    "r-salud-013", "salud", "meta", "ALTA",
    "Contratar 5,000 equipos de salud familiar y comunitaria para que cada uno atienda a 3,000 personas como médicos de familia en vecindarios y comunidades.",
    "Contrataremos 5,000 equipos de salud familiar y comunitaria para que cada uno atienda a 3,000 personas como médicos de familia",
    f"{S61} — Medidas Propuestas", 293, 293,
    meta="5,000 equipos de salud familiar (3,000 personas c/u)",
))

nuevas.append(mk(
    "r-salud-014", "salud", "propuesta", "MEDIA",
    "Reorientar el sistema hacia la atención preventiva con aumento sustancial de inversión en programas de vacunación, control de epidemias y nutrición.",
    "Reorientaremos el sistema hacia la atención preventiva. Aumentaremos sustancialmente la inversión en programas de vacunación",
    f"{S61} — Medidas Propuestas", 293, 293,
))

nuevas.append(mk(
    "r-salud-015", "salud", "propuesta", "ALTA",
    "Salud mental como pilar estructural: fortalecer Centros de Salud Mental Comunitarios, equipos móviles en colegios, psicólogos en todas las instituciones educativas y centros de salud, cobertura obligatoria en todos los seguros.",
    "Haremos de la salud mental un pilar estructural fortaleciendo los Centros de Salud Mental Comunitarios, desplegando equipos móviles que intervengan en colegios",
    f"{S61} — Medidas Propuestas", 293, 293,
))

nuevas.append(mk(
    "r-salud-016", "salud", "propuesta", "MEDIA",
    "Fortalecer los servicios de salud sexual y reproductiva con atención diferenciada para adolescentes, jóvenes, mujeres y personas LGBTIQ+, respetando la autonomía y la diversidad cultural.",
    "Fortaleceremos los servicios de salud sexual y reproductiva, con atención diferenciada para adolescentes, jóvenes, mujeres y personas LGBTIQ+",
    f"{S61} — Medidas Propuestas", 293, 293,
))

nuevas.append(mk(
    "r-salud-017", "salud", "propuesta", "MEDIA",
    "Aplicar enfoque meritocrático y ético en la gestión: seleccionar directivos por concurso público, eliminar influencia política en nombramientos, código de conducta obligatorio para todos los niveles.",
    "Aplicar un enfoque meritocrático y ético en la gestión del sistema de salud. Seleccionar a los directivos por concurso público y eliminar la influencia política en los nombramientos",
    f"{S61} — Medidas Propuestas", 293, 293,
))

nuevas.append(mk(
    "r-salud-018", "salud", "propuesta", "ALTA",
    "Digitalizar la atención con un sistema nacional de Historial Clínico Electrónico (HCE) interoperable que registre de forma segura, continua y confidencial la información médica de cada paciente.",
    "Digitalizar la atención a través de un sistema nacional de historial clínico electrónico. Diseñar e implementar una plataforma interoperable de historial clínico electrónico",
    f"{S61} — Medidas Propuestas", 293, 293,
))

nuevas.append(mk(
    "r-salud-019", "salud", "propuesta", "ALTA",
    "Reflotamiento del sistema de laboratorios y producción pública de medicamentos, insumos y dispositivos tecnológicos sanitarios; creación del Instituto de Medicina Tradicional para investigación de plantas medicinales.",
    "Reflotamiento del sistema de laboratorios y producción pública de medicamentos, insumos y dispositivos tecnológicos sanitarios",
    f"{S61} — Medidas Propuestas", 295, 295,
))

nuevas.append(mk(
    "r-salud-020", "salud", "propuesta", "ALTA",
    "Política nacional de medicamentos basada en Red Nacional de Farmacias y Boticas Populares que ofrezcan genéricos de calidad a precios accesibles, con topes razonables a las ganancias.",
    "Desarrollaremos una política nacional de medicamentos basada en una red Nacional de Farmacias y Boticas Populares que ofrezcan genéricos de calidad a precios accesibles",
    f"{S61} — Medidas Propuestas", 295, 295,
))

nuevas.append(mk(
    "r-salud-021", "salud", "propuesta", "ALTA",
    "Banco nacional de medicamentos y compras integradas: centralizar adquisición al por mayor a través de sistema único de compra para aprovechar economías de escala, reducir precios y asegurar abastecimiento continuo.",
    "Banco nacional de medicamentos y compras integradas. Centralizar la adquisición al por mayor de medicamentos básicos a través de un sistema único de compra",
    f"{S61} — Medidas Propuestas", 295, 295,
))

# =====================================================================
# 6.2 EDUCACIÓN (líneas 295-306) — tema: educacion
# =====================================================================
S62 = "Dimensión Social — 6.2 Educación"

nuevas.append(mk(
    "r-educacion-001", "educacion", "diagnostico", "ALTA",
    "Diagnóstico estructural: la educación pública ha perdido calidad, ha deteriorado su identificación con la cultura peruana y aporta muy poco en la producción tecnológica. Requiere ser relanzada como aliado de la transformación nacional.",
    "La educación pública ha perdido calidad, ha deteriorado su identificación con la cultura peruana, y aporta muy poco en la producción tecnológica",
    f"{S62} — Situación Actual", 297, 297,
))

nuevas.append(mk(
    "r-educacion-002", "educacion", "diagnostico", "ALTA",
    "Diagnóstico de aprendizajes: según UMC-MINEDU 2024 solo 3 de cada 10 estudiantes de 4to grado alcanzan lo esperado en lectura y matemática; en 6to grado solo 26% alcanza nivel satisfactorio en lectura y 18% en matemática.",
    "Según la Evaluación Muestral 2024 (UMC – MINEDU), solo 3 de cada 10 estudiantes de 4° alcanzan lo esperado, tanto en lectura como en matemática",
    f"{S62} — Situación Actual", 298, 298,
    meta="4° grado: 30% logra; 6° lectura 26%; 6° matemática 18%",
))

nuevas.append(mk(
    "r-educacion-003", "educacion", "diagnostico", "ALTA",
    "Diagnóstico de inversión: el Perú invierte menos del 4% del PBI en educación; inversión por estudiante S/ 6,600 primaria, S/ 5,015 secundaria, mientras COAR S/ 24,300.",
    "El Perú invierte menos del 4% del PBI en educación, siendo en su mayor parte gasto corriente",
    f"{S62} — Situación Actual", 300, 300,
    meta="Educación <4% PBI; primaria S/6,600/estudiante; COAR S/24,300",
))

nuevas.append(mk(
    "r-educacion-004", "educacion", "diagnostico", "MEDIA",
    "Diagnóstico de docentes e infraestructura: solo 3 de cada 10 docentes accede a capacitación pertinente cada año; 47% de locales escolares presenta deficiencias graves; 1 de cada 4 no cuenta con agua potable (Censo 2023).",
    "Solo 3 de cada 10 docentes acceden a capacitación pertinente cada año. El 47% de locales escolares presenta deficiencias graves de infraestructura",
    f"{S62} — Situación Actual", 298, 298,
    meta="47% locales con deficiencias; 25% sin agua potable",
))

nuevas.append(mk(
    "r-educacion-005", "educacion", "diagnostico", "MEDIA",
    "Diagnóstico de educación superior: solo 3 de 98 universidades licenciadas figuran en el top 1000 de rankings internacionales; en educación tecnológica solo 140 de 1,131 institutos lograron licenciarse (12%).",
    "solo 3 de 98 universidades licenciadas figuran en el top 1000 de rankings internacionales como QS o THE",
    f"{S62} — Situación Actual", 298, 298,
))

nuevas.append(mk(
    "r-educacion-006", "educacion", "propuesta", "ALTA",
    "Potenciar la educación tecnológica para que ningún egresado de secundaria se quede sin aprender un oficio; fortalecer institutos de innovación tecnológica y potenciar institutos técnicos de las FFAA en cada región.",
    "Potenciación de la educación tecnológica para que ningún egresado de secundaria se quede sin aprender un oficio",
    f"{S62} — Medidas Propuestas", 302, 302,
))

nuevas.append(mk(
    "r-educacion-007", "educacion", "propuesta", "ALTA",
    "Establecer estándares nacionales para condiciones mínimas de educabilidad en todo el territorio: acceso a agua, luz, conectividad, alimentación escolar, espacios seguros y apoyo emocional.",
    "Establecer estándares nacionales para condiciones mínimas de educabilidad en todo el territorio nacional: acceso a agua, luz, conectividad, alimentación escolar",
    f"{S62} — Medidas Propuestas", 302, 302,
))

nuevas.append(mk(
    "r-educacion-008", "educacion", "propuesta", "ALTA",
    "Consolidar la reforma universitaria garantizando la calidad, autonomía y fiscalización efectiva de la SUNEDU, promoviendo la movilidad académica entre regiones.",
    "Consolidar la reforma universitaria garantizando la calidad, autonomía y fiscalización efectiva de la SUNEDU",
    f"{S62} — Medidas Propuestas", 302, 302,
))

nuevas.append(mk(
    "r-educacion-009", "educacion", "100dias", "100DIAS",
    "Compromiso de primer año: implementar un sistema de supervisión que abarque todos los componentes del sistema educativo (estudiantes, docentes, currículos, recursos, infraestructura).",
    "En el primer año de gobierno, se implementará un sistema de supervisión que abarque todos los componentes del sistema",
    f"{S62} — Medidas Propuestas", 302, 302,
))

nuevas.append(mk(
    "r-educacion-010", "educacion", "meta", "ALTA",
    "Meta de deserción: disminuir la deserción escolar en áreas rurales y marginales al 5% en cinco años.",
    "Disminuir la deserción escolar en áreas rurales y marginales al 5% en cinco años",
    f"{S62} — Medidas Propuestas", 302, 302,
    meta="Deserción escolar rural/marginal: ≤5% en 5 años",
))

nuevas.append(mk(
    "r-educacion-011", "educacion", "propuesta", "ALTA",
    "Plan quinquenal focalizado en 4° de primaria y 2° de secundaria para lectura, matemática y habilidades socioemocionales, con refuerzo escolar, tutorías entre pares y evaluación formativa alineada a ENLA.",
    "Implementar un plan quinquenal focalizado en 4.º de primaria y 2.º de secundaria para lectura, matemática y habilidades socioemocionales",
    f"{S62} — Medidas Propuestas", 302, 302,
))

nuevas.append(mk(
    "r-educacion-012", "educacion", "propuesta", "MEDIA",
    "Fortalecer la formación docente inicial con estándares de calidad, prácticas en aula desde los primeros ciclos y articulación entre institutos pedagógicos y universidades.",
    "Fortalecer la formación docente inicial con estándares de calidad, prácticas en aula desde los primeros ciclos",
    f"{S62} — Medidas Propuestas", 304, 304,
))

nuevas.append(mk(
    "r-educacion-013", "educacion", "propuesta", "MEDIA",
    "Implementar un plan de residencias docentes en contextos rurales; programas de capacitación continua para el 100% de docentes de áreas rurales y marginales.",
    "Implementar un plan de residencias docentes en los contextos rurales",
    f"{S62} — Medidas Propuestas", 304, 304,
))

nuevas.append(mk(
    "r-educacion-014", "educacion", "meta", "MEDIA",
    "Meta de infraestructura: mejorar la infraestructura educativa en áreas urbanas en 55% y en áreas rurales en 40% en cinco años.",
    "Mejorar la infraestructura educativa en áreas urbanas en un 55% en cinco años y un 40% en áreas rurales",
    f"{S62} — Medidas Propuestas", 304, 304,
    meta="Infraestructura: +55% urbana, +40% rural en 5 años",
))

nuevas.append(mk(
    "r-educacion-015", "educacion", "propuesta", "MEDIA",
    "Ajustar la Carrera Pública Magisterial para ofrecer mejores condiciones a docentes y directores en zonas rurales, EIB y amazónicas: bonificaciones permanentes, vivienda docente, puntaje adicional en concursos.",
    "Ajustar la Carrera Pública Magisterial para ofrecer mejores condiciones a docentes y directores en zonas rurales, EIB y amazónicas",
    f"{S62} — Medidas Propuestas", 304, 304,
))

nuevas.append(mk(
    "r-educacion-016", "educacion", "propuesta", "ALTA",
    "Ampliación del Programa Beca 18 y creación del Programa de Becas para investigaciones tecnológicas, Maestría y Doctorado a cargo de las universidades públicas conforme a prioridades de desarrollo nacional.",
    "Ampliación del Programa Beca 18 y creación del Programa de Becas para investigaciones tecnológicas, de Maestría y Doctorado",
    f"{S62} — Medidas Propuestas", 304, 304,
))

nuevas.append(mk(
    "r-educacion-017", "educacion", "propuesta", "MEDIA",
    "Rediseñar y escalar la EBA hacia un sistema de educación para personas jóvenes y adultas con horarios flexibles, modelos semipresenciales y virtuales, rutas cortas certificables y campaña nacional de reenganche educativo.",
    "Rediseñar y escalar la EBA hacia un sistema de educación de educación para las personas jóvenes y adultas para convertirla en la principal puerta de acceso y/o retorno educativo",
    f"{S62} — Medidas Propuestas", 304, 304,
))

nuevas.append(mk(
    "r-educacion-018", "educacion", "propuesta", "ALTA",
    "Red de institutos tecnológicos y CETPRO públicos de excelencia especializados por cadenas productivas con énfasis en Amazonía y regiones rurales (bioeconomía, agroindustria, turismo sostenible, servicios digitales).",
    "Desarrollar una red de institutos tecnológicos y CETPRO públicos de excelencia, especializados por cadenas productivas y con énfasis en Amazonía y regiones rurales",
    f"{S62} — Medidas Propuestas", 304, 304,
))

nuevas.append(mk(
    "r-educacion-019", "educacion", "propuesta", "MEDIA",
    "Institucionalizar modelos de formación dual y prácticas pre-profesionales obligatorias en empresas y organizaciones locales, con incentivos tributarios a empresas que ofrezcan cupos.",
    "Institucionalizar modelos de formación dual y prácticas pre-profesionales obligatorias en empresas y organizaciones locales",
    f"{S62} — Medidas Propuestas", 304, 304,
))

nuevas.append(mk(
    "r-educacion-020", "educacion", "propuesta", "ALTA",
    "Política curricular descentralizada: Marco Curricular Nacional (MCN) con diversificación que responda a cada región y localidad; los pueblos y naciones indígenas gestionarán autónomamente su proceso de diversificación.",
    "La política curricular del sistema consistirá en un Marco Curricular Nacional (MCN) y una política descentralizada de diversificación del MCN que responda a cada región y localidad",
    f"{S62} — Medidas Propuestas", 306, 306,
))

nuevas.append(mk(
    "r-educacion-021", "educacion", "propuesta", "ALTA",
    "Sistema educativo nacional se regirá por un enfoque general intercultural, con enfoque intercultural bilingüe (EIB) para pueblos y naciones indígenas; enfoque de género en todos los niveles y modalidades.",
    "El sistema educativo nacional se regirá por un enfoque general intercultural, para todos y un enfoque intercultural bilingüe para los pueblos y naciones indígenas",
    f"{S62} — Medidas Propuestas", 306, 306,
))

# =====================================================================
# 6.3 VIOLENCIA DE GÉNERO (líneas 306-310) — tema: genero
# =====================================================================
S63 = "Dimensión Social — 6.3 Violencia de Género"

nuevas.append(mk(
    "r-genero-001", "genero", "diagnostico", "ALTA",
    "Diagnóstico cuantitativo: en 2024 se reportaron 71,717 casos de violencia psicológica, 63,692 física y 32,388 sexual atendidos por los CEM; 170 feminicidios incluyendo 10 niñas y adolescentes.",
    "tan sólo en el 2024 se reportaron 71,717 casos de violencia psicológica, 63,692 casos de violencia física y 32,388 casos de violencia sexual atendidos por los Centros de Emergencia Mujer",
    f"{S63} — Situación Actual", 306, 306,
    meta="2024: 71,717 violencia psicológica + 63,692 física + 32,388 sexual; 170 feminicidios",
))

nuevas.append(mk(
    "r-genero-002", "genero", "diagnostico", "ALTA",
    "Diagnóstico de desapariciones: en 2023 se registraron 10,817 mujeres desaparecidas; solo poco más de la mitad fueron ubicadas; 5,184 son niñas y mujeres; mayor incidencia en Lima (3,561), Cusco (681) y Junín (646).",
    "en el año 2023 se registraron 10,817 casos, de las cuáles apenas poco más de la mitad fueron ubicadas",
    f"{S63} — Situación Actual", 306, 306,
    meta="2023: 10,817 mujeres desaparecidas; 5,184 niñas/mujeres",
))

nuevas.append(mk(
    "r-genero-003", "genero", "diagnostico", "ALTA",
    "Diagnóstico de explotación sexual: el Ministerio Público registró 29,400 casos entre 2018-2023, la mayoría víctimas menores; problemática expandida más allá de La Pampa y La Rinconada hacia Lima, Arequipa, La Libertad, Piura y Tumbes.",
    "el Ministerio Público y la Fiscalía de la Nación registró 29,400 casos entre 2018 y 2023, la mayoría de ellas víctimas menores de edad",
    f"{S63} — Situación Actual", 306, 306,
))

nuevas.append(mk(
    "r-genero-004", "genero", "propuesta", "MEDIA",
    "Mejorar políticas regionales y locales vía acompañamiento y capacitación del MIMP; asignación presupuestal a Instancias de Concertación contra la Violencia para que sean espacios de acción, no de conversación.",
    "Mejoraremos las políticas, planes e intervenciones de las autoridades regionales y locales vía acompañamiento y capacitación del Ministerio de la Mujer y Población Vulnerables",
    f"{S63} — Medidas Propuestas", 308, 308,
))

nuevas.append(mk(
    "r-genero-005", "genero", "propuesta", "ALTA",
    "Atención rápida y oportuna en casos de desaparición, feminicidio, violencia contra mujeres y población vulnerable; tipificar como delito la omisión de acciones inmediatas de policías ante denuncias.",
    "Atención rápida y oportuna en casos de desaparición, de feminicidio, violencia contra las mujeres y población vulnerable como niñeces con discapacidad. Tipificar como delito la omisión de acciones inmediatas de policías ante denuncias",
    f"{S63} — Medidas Propuestas", 308, 308,
))

nuevas.append(mk(
    "r-genero-006", "genero", "propuesta", "ALTA",
    "Educación Sexual Integral pertinente en cada nivel del sistema educativo para garantizar entornos libres de violencia, en un marco de respeto, valorando el consentimiento y la autonomía corporal.",
    "Educación Sexual Integral pertinente en cada uno de los niveles del sistema educativo, para garantizar que infancias y adolescencias crezcan en entornos escolares y hogares libres de violencia",
    f"{S63} — Medidas Propuestas", 308, 308,
))

nuevas.append(mk(
    "r-genero-007", "genero", "propuesta", "ALTA",
    "Declarar en emergencia la seguridad de las mujeres trans, especialmente de aquellas que ejercen el trabajo sexual, frente al incremento de crímenes de odio y violencia estructural.",
    "Declararemos en emergencia la seguridad de las mujeres trans, especialmente de aquellas que ejercen el trabajo sexual",
    f"{S63} — Medidas Propuestas", 308, 308,
))

nuevas.append(mk(
    "r-genero-008", "genero", "principio", "ALTA",
    "Garantizar la igualdad ante la ley para todas y todos, en especial el derecho a la identidad, salud, educación y trabajo para la diversidad.",
    "Garantizaremos la igualdad ante la ley para todas y todos, en especial garantizar el derecho a la identidad, salud, educación y trabajo para la diversidad",
    f"{S63} — Medidas Propuestas", 308, 308,
))

nuevas.append(mk(
    "r-genero-009", "genero", "propuesta", "ALTA",
    "Asegurar acceso real, oportuno y seguro al aborto terapéutico cuando sea necesario para salvar la vida de la gestante o evitar un daño grave y permanente a su salud, con consentimiento informado.",
    "el Estado debe asegurar un acceso real, oportuno y seguro al aborto terapéutico cuando sea necesario para salvar la vida de la gestante",
    f"{S63} — Medidas Propuestas", 308, 308,
))

nuevas.append(mk(
    "r-genero-010", "genero", "propuesta", "ALTA",
    "Despenalizar la interrupción del embarazo en casos de violencia sexual y/o riesgo para la vida o salud de la madre, para que ninguna víctima sea obligada a continuar un embarazo forzado.",
    "proponemos despenalizar la interrupción del embarazo en casos de violencia sexual y/o riesgo para la vida o la salud de la madre",
    f"{S63} — Medidas Propuestas", 308, 308,
))

nuevas.append(mk(
    "r-genero-011", "genero", "propuesta", "MEDIA",
    "Actualización y fortalecimiento de la política de aborto terapéutico para garantizar el cumplimiento de estándares internacionales de DDHH e implementación efectiva de la Guía Técnica en todo el país.",
    "Actualización y fortalecimiento de la política de aborto terapéutico que garantice el cumplimiento de los estándares internacionales de derechos humanos",
    f"{S63} — Medidas Propuestas", 308, 308,
))

# =====================================================================
# 6.4 INCLUSIÓN SOCIAL (líneas 310-313) — tema: pensiones (programas sociales)
# =====================================================================
S64 = "Dimensión Social — 6.4 Inclusión Social"

nuevas.append(mk(
    "r-pensiones-001", "pensiones", "diagnostico", "ALTA",
    "Diagnóstico de pobreza: en 2024 el 27.6% de peruanos (9.39 millones) vive en pobreza monetaria y 5.5% en pobreza extrema; 31.8% en vulnerabilidad monetaria; >60% son pobres o están en riesgo de serlo.",
    "En 2024, el 27,6 % de los peruanos —unos 9,39 millones de personas— vive en pobreza monetaria, y el 5,5 % en pobreza extrema",
    f"{S64} — Situación Actual", 310, 310,
    meta="Pobreza 2024: 27.6% (9.39M); extrema 5.5%; vulnerable 31.8%",
))

nuevas.append(mk(
    "r-pensiones-002", "pensiones", "diagnostico", "ALTA",
    "Diagnóstico de urbanización de la pobreza: en 2021 el 68.7% de pobres vivía en ciudades, Lima concentra 24% de la pobreza total; el Programa Juntos sigue diseñado para entorno rural.",
    "Aunque históricamente se concentraba en las zonas rurales, hoy se ha urbanizado: en 2021, el 68,7 % de las personas pobres vivían en ciudades, y Lima por sí sola concentra el 24 %",
    f"{S64} — Situación Actual", 310, 310,
))

nuevas.append(mk(
    "r-pensiones-003", "pensiones", "diagnostico", "MEDIA",
    "Diagnóstico de inversión social: en 2022 el gasto en protección social no contributiva fue inferior al 0.8% del PIB, muy lejos del estándar 1.5-2.5%; gasto per cápita US$ 646/año vs promedio regional US$ 1,175.",
    "En 2022, el gasto en protección social no contributiva fue inferior al 0,8 % del PIB, por debajo del promedio de América del Sur",
    f"{S64} — Situación Actual", 310, 310,
    meta="Gasto protección social 0.8% PIB (estándar 1.5-2.5%); US$ 646 vs US$ 1,175 regional",
))

nuevas.append(mk(
    "r-pensiones-004", "pensiones", "propuesta", "ALTA",
    "Rediseñar el Ministerio de Inclusión Social hacia un Ministerio de Bienestar y Desarrollo Nacional.",
    "Rediseñar el Ministerio de Inclusión Social hacia un Ministerio de Bienestar y Desarrollo Nacional",
    f"{S64} — Medidas Propuestas", 312, 312,
))

nuevas.append(mk(
    "r-pensiones-005", "pensiones", "propuesta", "ALTA",
    "Transformar los programas sociales focalizados en un sistema de protección social articulado que acompañe a las familias en sus transiciones fuera de la pobreza y garantice ciudadanía social sin clientelismo.",
    "Transformar los programas sociales focalizados en un sistema de protección social articulado, que acompañe a las familias en sus transiciones fuera de la pobreza",
    f"{S64} — Medidas Propuestas", 312, 312,
))

nuevas.append(mk(
    "r-pensiones-006", "pensiones", "propuesta", "ALTA",
    "Rediseñar el Programa Juntos para adaptarlo a la nueva geografía urbana de la pobreza; duplicar la cobertura y el monto del programa Juntos.",
    "Rediseñar el Programa Juntos para adaptarlo a la nueva geografía de la pobreza, considerando que en 2021 el 68,7 % de las personas pobres vivían en zonas urbanas",
    f"{S64} — Medidas Propuestas", 312, 312,
    meta="Programa Juntos: duplicar cobertura y monto",
))

nuevas.append(mk(
    "r-pensiones-007", "pensiones", "meta", "ALTA",
    "Paquete integrado de protección social para primera infancia: incrementar cobertura para gestantes y niños menores de 5 años de 31.6% a 70%.",
    "Implementar un paquete integrado de protección social para la primera infancia, beneficiando a hogares con gestantes y niños menores de 5 años que hoy representan un 31,6 % de cobertura en incentivos y que deben llegar al 70 %",
    f"{S64} — Medidas Propuestas", 312, 312,
    meta="Cobertura primera infancia: 31.6%→70%",
))

nuevas.append(mk(
    "r-pensiones-008", "pensiones", "meta", "ALTA",
    "Programa nacional de alimentación escolar que garantice al menos una comida diaria en el 100% de las escuelas públicas de inicial, primaria y secundaria, con compras directas a agricultores locales.",
    "Crear un programa nacional de alimentación escolar que garantice al menos una comida diaria en el 100 % de las escuelas públicas",
    f"{S64} — Medidas Propuestas", 312, 312,
    meta="100% escuelas públicas con alimentación escolar diaria",
))

nuevas.append(mk(
    "r-pensiones-009", "pensiones", "meta", "ALTA",
    "Incrementar a 700 soles bimensuales el monto de las pensiones no contributivas (Pensión 65) para todas y todos.",
    "Incrementar a 700 soles bimensuales el monto de las pensiones no contributivas (Pensión 65) para todas y todos",
    f"{S64} — Medidas Propuestas", 312, 312,
    meta="Pensión 65: S/ 700 bimensuales",
))

nuevas.append(mk(
    "r-pensiones-010", "pensiones", "propuesta", "MEDIA",
    "Implementar un modelo de ventanilla única de servicios sociales en gobiernos locales priorizando zonas con mayor pobreza extrema.",
    "Implementar un modelo de ventanilla única de servicios sociales en gobiernos locales, priorizando zonas con mayor pobreza extrema",
    f"{S64} — Medidas Propuestas", 312, 312,
))

nuevas.append(mk(
    "r-pensiones-011", "pensiones", "meta", "MEDIA",
    "Construir un registro social inclusivo, adaptativo y digital con inteligencia artificial para alcanzar una clasificación socioeconómica actualizada del 70% de la población pobre.",
    "Construir un registro social inclusivo, adaptativo y digital, con inteligencia artificial, para alcanzar una clasificación socioeconómica actualizada del 70 % de la población pobre",
    f"{S64} — Medidas Propuestas", 312, 312,
    meta="Registro social digital: 70% población pobre clasificada",
))

nuevas.append(mk(
    "r-pensiones-012", "pensiones", "meta", "ALTA",
    "Desarrollar estrategias territoriales de cierre de brechas sociales para que el 90% de hogares cuente con agua, saneamiento, electricidad e internet antes de 2031.",
    "Desarrollar estrategias territoriales de cierre de brechas sociales que permitan que el 90 % de hogares cuente con agua, saneamiento, electricidad e internet antes de 2031",
    f"{S64} — Medidas Propuestas", 312, 312,
    meta="90% hogares con servicios básicos al 2031",
))

# =====================================================================
# 6.5 IGUALDAD DE OPORTUNIDADES (líneas 314-316) — tema: genero
# =====================================================================
S65 = "Dimensión Social — 6.5 Igualdad de Oportunidades"

nuevas.append(mk(
    "r-genero-012", "genero", "diagnostico", "ALTA",
    "Diagnóstico de cuidado: en el 82% de los hogares peruanos la principal responsable del trabajo doméstico y de cuidado no remunerado es una mujer; afecta su trayectoria laboral, educativa y participación política.",
    "En el 82% de los hogares peruanos, la principal responsable del trabajo doméstico y de cuidado no remunerado es una mujer",
    f"{S65} — Situación Actual", 314, 314,
    meta="82% hogares: cuidado no remunerado a cargo de mujeres",
))

nuevas.append(mk(
    "r-genero-013", "genero", "diagnostico", "MEDIA",
    "Diagnóstico de uso del tiempo: en días laborables las mujeres dedican 5 horas 7 minutos al trabajo no remunerado doméstico y de cuidados, más del doble que los hombres (ENUT 2024).",
    "La Encuesta Nacional de Uso del Tiempo 2024 muestra que, en días laborables, las mujeres dedican en promedio 5 horas y 7 minutos al trabajo no remunerado",
    f"{S65} — Situación Actual", 314, 314,
    meta="Mujeres: 5h 7min/día trabajo no remunerado (ENUT 2024)",
))

nuevas.append(mk(
    "r-genero-014", "genero", "propuesta", "MEDIA",
    "Asignar un bono único de 800 soles a madres que den a luz en el SIS y carezcan de licencia de maternidad remunerada.",
    "Asignación de un bono único de 800 soles a las madres que den a luz en el SIS y carezcan de licencia de maternidad remunerada",
    f"{S65} — Medidas Propuestas", 314, 314,
    meta="Bono S/ 800 madres SIS sin licencia maternidad",
))

nuevas.append(mk(
    "r-genero-015", "genero", "propuesta", "ALTA",
    "Crear e implementar un Sistema Nacional de Cuidados con enfoque de género e intercultural que reduzca la sobrecarga de cuidados sobre las mujeres y garantice atención de calidad a niñas y niños, personas mayores, con discapacidad y en dependencia.",
    "Crear e implementar un Sistema Nacional de Cuidados con enfoque de género e intercultural que reduzca la sobrecarga de cuidados sobre las mujeres",
    f"{S65} — Medidas Propuestas", 316, 316,
))

nuevas.append(mk(
    "r-genero-016", "genero", "propuesta", "MEDIA",
    "Inversión en infraestructura y servicios de cuidado comunitario: retorno de Wawawasi en hogares de madres usuarias con acompañamiento estatal; cobertura de Educuna y Cunamás con derechos laborales y salario mínimo.",
    "Inversión en infraestructura y servicios de cuidado comunitario en zonas urbanas y rurales. Retorno de Wawawasi en hogares de madres usuarias",
    f"{S65} — Medidas Propuestas", 316, 316,
))

nuevas.append(mk(
    "r-genero-017", "genero", "propuesta", "MEDIA",
    "Incremento progresivo de licencias de paternidad para lograr licencias parentales equitativas y servicios de cuidado infantil en centros laborales.",
    "Incremento progresivo de licencias de paternidad para lograr licencias parentales equitativas y servicios de cuidado infantil en centros laborales",
    f"{S65} — Medidas Propuestas", 316, 316,
))

# =====================================================================
# 6.6 JUVENTUD (líneas 316-322) — tema: juventud
# =====================================================================
S66 = "Dimensión Social — 6.6 Juventud"

nuevas.append(mk(
    "r-juventud-001", "juventud", "diagnostico", "ALTA",
    "Diagnóstico estructural: la juventud peruana en 2026 se caracteriza por incertidumbre crítica marcada por la precariedad laboral y la falta de proyectos de vida concretos; el 82% de jóvenes trabaja en condiciones de informalidad.",
    "El 82% de los jóvenes trabaja en condiciones de informalidad, lo que limita su acceso a estabilidad económica, protección social y oportunidades de desarrollo",
    f"{S66} — Situación Actual", 318, 318,
    meta="Informalidad juvenil: 82%",
))

nuevas.append(mk(
    "r-juventud-002", "juventud", "diagnostico", "MEDIA",
    "Diagnóstico de brecha digital: persiste una profunda brecha digital que mantiene aisladas a comunidades rurales y amazónicas, restringiendo su acceso a educación, información y oportunidades económicas.",
    "Persiste una profunda brecha digital que mantiene aisladas a comunidades rurales y amazónicas",
    f"{S66} — Situación Actual", 318, 318,
))

nuevas.append(mk(
    "r-juventud-003", "juventud", "meta", "ALTA",
    "Crear el Programa de voluntariado juvenil del sector público (AYNI): tareas menores de cuidado ambiental, mantenimiento del ornato, educación cívica; 45 mil jóvenes en todas las regiones el primer año.",
    "Creación del Programa de voluntariado juvenil del sector público (AYNI), de tiempo parcial, para que los jóvenes puedan realizar tareas menores de cuidado ambiental",
    f"{S66} — Medidas Propuestas", 320, 320,
    meta="AYNI: 45,000 jóvenes en regiones (primer año)",
))

nuevas.append(mk(
    "r-juventud-004", "juventud", "meta", "ALTA",
    "Programa 'Mi Primera Chamba': bono de 6,150 soles a cada joven egresado de secundaria para iniciar estudios/capacitación, emprendimiento o subsidio de hasta 6 meses mientras encuentra empleo.",
    "Programa especial de apoyo a los jóvenes “Mi Primera Chamba”, que asignará un bono de 6,150 soles a cada joven egresado de secundaria",
    f"{S66} — Medidas Propuestas", 320, 320,
    meta="Mi Primera Chamba: bono S/ 6,150 por egresado de secundaria",
))

nuevas.append(mk(
    "r-juventud-005", "juventud", "propuesta", "MEDIA",
    "Subsidio temporal de hasta 22% al costo de la formalidad para incentivar contratación formal de jóvenes en MYPEs; exención de Impuesto a la Renta por 24 meses para nuevos contratos a menores de 25 años.",
    "Establecer subsidio temporal de hasta 22% al costo de la formalidad para incentivar la contratación formal y estable de jóvenes en MYPEs",
    f"{S66} — Medidas Propuestas", 322, 322,
    meta="Subsidio 22% formalidad; exención IR 24 meses contratos <25 años",
))

nuevas.append(mk(
    "r-juventud-006", "juventud", "meta", "ALTA",
    "Fortalecer Jóvenes Productivos con formaciones técnicas en logística portuaria y energías renovables para alcanzar tasa de inserción laboral del 85% en sectores estratégicos.",
    "Instaurar y fortalecer el programa Jóvenes Productivos con formaciones técnicas especializadas en logística portuaria y energías renovables para alcanzar una tasa de inserción laboral del 85%",
    f"{S66} — Medidas Propuestas", 322, 322,
    meta="Tasa inserción laboral: 85% en sectores estratégicos",
))

nuevas.append(mk(
    "r-juventud-007", "juventud", "meta", "ALTA",
    "Fondo capital semilla Juventud Innovadora para apoyar 50,000 negocios tecnológicos regionales en sostenibilidad ambiental y productividad agrícola, con fondos a fondo perdido del Banco de la Nación.",
    "Activar el fondo capital semilla Juventud Innovadora para apoyar 50,000 negocios tecnológicos regionales",
    f"{S66} — Medidas Propuestas", 322, 322,
    meta="50,000 negocios tecnológicos juveniles regionales",
))

nuevas.append(mk(
    "r-juventud-008", "juventud", "meta", "ALTA",
    "Construir una red nacional de 700 clínicas de control emocional con horarios extendidos y centros de salud mental comunitaria modernizados con teleconsulta asistida por IA.",
    "Construir una red nacional de 700 clínicas de control emocional con horarios extendidos",
    f"{S66} — Medidas Propuestas", 322, 322,
    meta="700 clínicas de control emocional juvenil",
))

nuevas.append(mk(
    "r-juventud-009", "juventud", "propuesta", "ALTA",
    "Servicio Civil de Salud Mental: presencia obligatoria de un psicólogo especializado por cada 300 alumnos en todas las instituciones educativas públicas de secundaria a nivel nacional.",
    "Instituir el Servicio Civil de Salud Mental para garantizar la presencia obligatoria de un psicólogo especializado por cada 300 alumnos",
    f"{S66} — Medidas Propuestas", 322, 322,
    meta="1 psicólogo/300 alumnos en secundaria pública",
))

nuevas.append(mk(
    "r-juventud-010", "juventud", "meta", "ALTA",
    "Desarrollar 50 Parques de Innovación, Deporte y Cultura equipados con laboratorios de robótica y estudios de grabación en distritos de alta peligrosidad como alternativa al reclutamiento por economías ilegales.",
    "Desarrollar 50 Parques de Innovación, Deporte y Cultura equipados con laboratorios de robótica y estudios de grabación en distritos de alta peligrosidad",
    f"{S66} — Medidas Propuestas", 322, 322,
    meta="50 Parques de Innovación, Deporte y Cultura",
))

nuevas.append(mk(
    "r-juventud-011", "juventud", "meta", "ALTA",
    "Asegurar la entrega de 10,000 becas adicionales por año a través de PRONABEC priorizando carreras de ingeniería y ciencias aplicadas, con descentralización para jóvenes de comunidades campesinas y nativas.",
    "Asegurar la entrega de 10.000 becas adicionales por año a través de PRONABEC, dando prioridad a las carreras de ingeniería y ciencias aplicadas",
    f"{S66} — Medidas Propuestas", 322, 322,
    meta="+10,000 becas PRONABEC anuales",
))

nuevas.append(mk(
    "r-juventud-012", "juventud", "meta", "ALTA",
    "Proyecto nacional Integratel para extender la Red Dorsal de Fibra Óptica a todo el territorio nacional y proveer acceso gratuito a internet de banda ancha en el 85% de hogares rurales.",
    "Ejecutar el proyecto nacional Integratel para extender la Red Dorsal de Fibra Óptica a todo el territorio nacional y proveer acceso gratuito a internet de banda ancha en el 85% de los hogares rurales",
    f"{S66} — Medidas Propuestas", 322, 322,
    meta="Integratel: internet gratuito en 85% hogares rurales",
))

nuevas.append(mk(
    "r-juventud-013", "juventud", "meta", "MEDIA",
    "Crear 25 sedes digitales de universidades públicas en provincias remotas y modernizar 80 institutos tecnológicos con infraestructura avanzada en inteligencia artificial, robótica y programación.",
    "Crear 25 sedes digitales de universidades públicas en provincias remotas y modernizar 80 institutos tecnológicos",
    f"{S66} — Medidas Propuestas", 322, 322,
    meta="25 sedes digitales universidades + 80 institutos modernizados",
))

nuevas.append(mk(
    "r-juventud-014", "juventud", "meta", "ALTA",
    "Garantizar servicios de salud amigables en el 100% de centros de primer nivel con entrega gratuita de anticonceptivos de larga duración para reducir el embarazo adolescente al 7%.",
    "Garantizar servicios de salud amigables en el 100 por ciento de centros de primer nivel con entrega gratuita de métodos anticonceptivos de larga duración para reducir el embarazo adolescente al 7 por ciento",
    f"{S66} — Medidas Propuestas", 322, 322,
    meta="Embarazo adolescente: ≤7%",
))

nuevas.append(mk(
    "r-juventud-015", "juventud", "propuesta", "ALTA",
    "Aplicar con carácter obligatorio el currículo de Educación Sexual Integral (ESI) desde perspectiva científica en nivel secundario; testeos masivos de ITS en centros de educación superior.",
    "Aplicar con carácter obligatorio el currículo de Educación Sexual Integral (ESI) desde una perspectiva científica en el nivel secundario",
    f"{S66} — Medidas Propuestas", 322, 322,
))

# =====================================================================
# 6.7 DEPORTE (líneas 322-329) — tema: deporte
# =====================================================================
S67 = "Dimensión Social — 6.7 Deporte"

nuevas.append(mk(
    "r-deporte-001", "deporte", "diagnostico", "ALTA",
    "Diagnóstico estructural: la realidad del deporte en 2026 evidencia profundas desigualdades y limitaciones institucionales; la ausencia de política nacional articulada, deterioro de infraestructura y centralismo en alto rendimiento generan un ecosistema excluyente.",
    "La realidad del deporte en el Perú al 2026 evidencia profundas desigualdades estructurales y limitaciones institucionales que afectan su desarrollo sostenible",
    f"{S67} — Situación Actual", 324, 324,
))

nuevas.append(mk(
    "r-deporte-002", "deporte", "diagnostico", "MEDIA",
    "Diagnóstico de sedentarismo: más del 60% de la población no alcanza los niveles mínimos recomendados de actividad física, afectando productividad económica, sostenibilidad del sistema de salud y calidad de vida.",
    "más del 60% de la población no alcanza los niveles mínimos recomendados de actividad física",
    f"{S67} — Situación Actual", 326, 326,
    meta="Sedentarismo: >60% no alcanza actividad física mínima",
))

nuevas.append(mk(
    "r-deporte-003", "deporte", "propuesta", "MEDIA",
    "Recuperación y activación de canchas y espacios públicos con iluminación, mantenimiento, señalización y uso programado (ligas barriales, recreación, talleres artísticos), reduciendo 'infraestructura vacía'.",
    "Recuperación y activación de los/as canchas y espacios públicos con iluminación, mantenimiento, señalización y uso programado",
    f"{S67} — Medidas Propuestas", 328, 328,
))

nuevas.append(mk(
    "r-deporte-004", "deporte", "propuesta", "MEDIA",
    "Escuelas deportivas de base y ligas barriales con horarios protegidos, entrenadores comunitarios certificados, prioridad en adolescencia y juventudes; articulación con seguridad ciudadana para entornos seguros.",
    "Escuelas deportivas de base y ligas barriales con horarios protegidos, entrenadores comunitarios certificados",
    f"{S67} — Medidas Propuestas", 328, 328,
))

nuevas.append(mk(
    "r-deporte-005", "deporte", "propuesta", "MEDIA",
    "Fortalecer educación física y deporte escolar con enfoque de hábitos y convivencia: competencias locales, rutas de talento, articulación MINEDU-IPD-municipios para uso compartido de espacios.",
    "Fortalecer educación física y deporte escolar con enfoque de hábitos (regularidad) y convivencia",
    f"{S67} — Medidas Propuestas", 328, 328,
))

nuevas.append(mk(
    "r-deporte-006", "deporte", "propuesta", "ALTA",
    "Crear el Sistema Nacional del Deporte, la Recreación y el Ocio Productivo articulando Estado, sector privado y comunidades.",
    "Crear el Sistema Nacional del Deporte, la Recreación y el Ocio Productivo, articulando Estado, sector privado y comunidades",
    f"{S67} — Medidas Propuestas", 328, 328,
))

nuevas.append(mk(
    "r-deporte-007", "deporte", "propuesta", "MEDIA",
    "Implementar el Programa 'Perú se Mueve' con acceso universal a actividades deportivas gratuitas en barrios y comunidades.",
    "Implementar el Programa Perú se Mueve, con acceso universal a actividades deportivas gratuitas en barrios y comunidades",
    f"{S67} — Medidas Propuestas", 328, 328,
))

nuevas.append(mk(
    "r-deporte-008", "deporte", "propuesta", "ALTA",
    "Lanzar el Programa Nacional de Infraestructura Deportiva 'Perú en Movimiento' para construcción, recuperación y mantenimiento de espacios deportivos.",
    "Lanzar el Programa Nacional de Infraestructura Deportiva “Perú en Movimiento”, para construcción, recuperación y mantenimiento de espacios deportivos",
    f"{S67} — Medidas Propuestas", 328, 328,
))

nuevas.append(mk(
    "r-deporte-009", "deporte", "propuesta", "MEDIA",
    "Crear el Fondo Nacional del Deporte y aprobar la Ley de Mecenazgo Deportivo para incrementar la inversión pública y privada.",
    "Crear el Fondo Nacional del Deporte y aprobar la Ley de Mecenazgo Deportivo para incrementar la inversión pública y privada",
    f"{S67} — Medidas Propuestas", 328, 328,
))

nuevas.append(mk(
    "r-deporte-010", "deporte", "propuesta", "MEDIA",
    "Instituir la Academia Nacional de Entrenadores para profesionalizar el sistema deportivo.",
    "Instituir la Academia Nacional de Entrenadores para profesionalizar el sistema deportivo",
    f"{S67} — Medidas Propuestas", 329, 329,
))

nuevas.append(mk(
    "r-deporte-011", "deporte", "propuesta", "ALTA",
    "Implementar el Programa Deporte Escolar Obligatorio garantizando educación física de calidad; crear el Plan Nacional de Alto Rendimiento Deportivo con centros descentralizados y detección temprana de talentos.",
    "Implementar el Programa Deporte Escolar Obligatorio, garantizando educación física de calidad",
    f"{S67} — Medidas Propuestas", 329, 329,
))

nuevas.append(mk(
    "r-deporte-012", "deporte", "propuesta", "MEDIA",
    "Implementar el Programa Deporte Inclusivo Perú garantizando acceso a poblaciones vulnerables; campañas nacionales de cultura física para reducir el sedentarismo.",
    "Implementar el Programa Deporte Inclusivo Perú, garantizando acceso a poblaciones vulnerables",
    f"{S67} — Medidas Propuestas", 329, 329,
))

# =====================================================================
# Volcar al JSON y guardar
# =====================================================================
ruta = Path("00-Sistema/datos/propuestas.json")
d = json.loads(ruta.read_text(encoding="utf-8"))
print(f"Antes: {len(d['propuestas'])} propuestas")
print(f"Nuevas a agregar: {len(nuevas)}")

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
