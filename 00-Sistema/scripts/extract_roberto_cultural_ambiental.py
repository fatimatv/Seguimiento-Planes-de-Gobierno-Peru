# -*- coding: utf-8 -*-
"""Extracción de Dimensión Cultural-Ambiental - Roberto Sánchez (Task 14).

Cubre secciones 7.1 (Protección de Ecosistemas y Derecho a un Ambiente Sano)
y 7.2 (Cultura), incluyendo elementos transversales de Pueblos Indígenas.
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
# 7.1 AMBIENTE (líneas 335-345) — tema: ambiente (algunos a indigenas/energia)
# =====================================================================
S71 = "Dimensión Cultural-Ambiental — 7.1 Protección de Ecosistemas"

nuevas.append(mk(
    "r-ambiente-001", "ambiente", "diagnostico", "ALTA",
    "Diagnóstico estructural: el Perú es uno de los países más biodiversos del planeta pero enfrenta presiones sin precedentes por cambio climático, deforestación y degradación; el modelo extractivista ha expandido fronteras extractivas en territorios frágiles.",
    "El Perú es uno de los países más biodiversos del planeta, con ecosistemas únicos que proveen servicios ecosistémicos esenciales para la vida y la economía. Sin embargo, enfrenta presiones sin precedentes",
    f"{S71} — Situación Actual", 335, 335,
))

nuevas.append(mk(
    "r-ambiente-002", "ambiente", "diagnostico", "ALTA",
    "Diagnóstico climático cuantitativo: entre 2003-2022 más de 12 millones de personas fueron afectadas por desastres naturales con pérdidas >US$ 6,000 millones; deforestación de 150,000 hectáreas anuales en la Amazonía.",
    "Entre 2003 y 2022, más de 12 millones de personas se vieron afectadas por desastres naturales provocados principalmente por eventos climáticos extremos, con pérdidas superiores a US$6,000 millones",
    f"{S71} — Situación Actual", 335, 335,
    meta="12M afectados por desastres 2003-2022; pérdidas >US$6,000M; deforestación 150,000 ha/año",
))

nuevas.append(mk(
    "r-ambiente-003", "ambiente", "diagnostico", "ALTA",
    "Diagnóstico de NDC: solo el 40% de las medidas NDC se han cumplido al 2023; cambios recientes a la Ley Forestal y de Fauna Silvestre han debilitado la gobernanza para gestión sostenible del patrimonio forestal.",
    "Solo el 40% de las medidas NDC se han cumplido al 2023, y cambios recientes a la Ley Forestal y de Fauna Silvestre han debilitado la gobernanza",
    f"{S71} — Situación Actual", 335, 335,
    meta="NDC cumplidas: 40% al 2023",
))

nuevas.append(mk(
    "r-ambiente-004", "ambiente", "diagnostico", "MEDIA",
    "Diagnóstico de degradación: más de 19 millones de hectáreas presentan algún nivel de degradación; pérdida de cobertura vegetal, deterioro de suelos y alteración de ciclos hidrológicos afectan disponibilidad de agua y biodiversidad.",
    "Se estima que más de 19 millones de hectáreas presentan algún nivel de degradación, producto de la pérdida de cobertura vegetal",
    f"{S71} — Situación Actual", 335, 335,
    meta="19M hectáreas con algún nivel de degradación",
))

nuevas.append(mk(
    "r-ambiente-005", "ambiente", "diagnostico", "MEDIA",
    "Diagnóstico energético: solo el 8.2% de la generación eléctrica proviene de renovables no convencionales; dependencia de combustibles fósiles genera emisiones y vulnerabilidad económica; economía circular incipiente.",
    "El Perú cuenta con abundantes recursos energéticos renovables, pero solo el 8.2% de la generación eléctrica proviene de renovables no convencionales",
    f"{S71} — Situación Actual", 337, 337,
    meta="Renovables no convencionales: 8.2% generación eléctrica",
))

nuevas.append(mk(
    "r-ambiente-006", "ambiente", "propuesta", "ALTA",
    "Reconocer constitucionalmente a la naturaleza (a los ríos, cuencas, etc.) como sujetos de derecho; defender el agua como derecho humano y bien común, priorizando su uso para la vida sobre el lucro privado.",
    "Reconoceremos constitucionalmente a la naturaleza (a los ríos, cuencas, etc.) como sujetos de derecho",
    f"{S71} — Medidas Propuestas", 337, 337,
))

nuevas.append(mk(
    "r-ambiente-007", "ambiente", "propuesta", "ALTA",
    "Cuidar la Amazonía como bien común estratégico para toda la humanidad; prohibición de la actividad minera metálica en la Amazonía baja que degrada los ecosistemas y la biodiversidad.",
    "Cuidaremos la Amazonía como un bien común estratégico para toda la humanidad. Prohibición de la actividad minera metálica en la Amazonía baja",
    f"{S71} — Medidas Propuestas", 337, 337,
))

nuevas.append(mk(
    "r-ambiente-008", "ambiente", "propuesta", "MEDIA",
    "Integrar las acciones de residuos sólidos con enfoque de Economía Circular y la Ley Integral de Residuos Sólidos para transitar de botaderos ilegales hacia establecimientos regulados.",
    "En relación al problema de los residuos sólidos, en Juntos por el Perú consideramos que se deben integrar las acciones consistentes con el enfoque de la Economía Circular",
    f"{S71} — Medidas Propuestas", 337, 337,
))

nuevas.append(mk(
    "r-ambiente-009", "ambiente", "propuesta", "MEDIA",
    "Fomentar y fortalecer la educación ambiental desde el MINAM; programas de voluntariado ambiental para la recuperación de espacios urbanos y rurales, con énfasis en ecosistemas frágiles.",
    "consideramos que se debe fomentar y fortalecer la educación ambiental, desde el propio MINAM",
    f"{S71} — Medidas Propuestas", 337, 337,
))

nuevas.append(mk(
    "r-ambiente-010", "ambiente", "propuesta", "ALTA",
    "Implementación efectiva del Sistema Nacional de Ordenamiento Territorial dotándolo de presupuesto para articular las políticas sectoriales de ocupación del territorio y aprovechamiento de recursos naturales.",
    "Ordenamiento territorial para fomentar territorios productivos, competitivos y sostenibles. Implementación efectiva del Sistema Nacional de Ordenamiento Territorial dotándolo de presupuesto",
    f"{S71} — Medidas Propuestas", 337, 337,
))

nuevas.append(mk(
    "r-ambiente-011", "ambiente", "propuesta", "MEDIA",
    "Creación de un Fondo Nacional de Ordenamiento Territorial con presupuesto mixto (cooperación y canon) para financiar proyectos estratégicos.",
    "Creación de un Fondo Nacional de Ordenamiento Territorial con presupuesto mixto (cooperación y canon) para financiar proyectos estratégicos",
    f"{S71} — Medidas Propuestas", 337, 337,
))

nuevas.append(mk(
    "r-ambiente-012", "ambiente", "propuesta", "MEDIA",
    "Fortalecimiento de la Infraestructura de Datos Espaciales del Perú (IDEP) que asegure la interoperabilidad de la información para la toma de decisiones y construir el Sistema de Información de Ordenamiento Territorial.",
    "Fortalecimiento de la Infraestructura de Datos Espaciales del Perú (IDEP) que asegure la interoperabilidad de la información",
    f"{S71} — Medidas Propuestas", 339, 339,
))

nuevas.append(mk(
    "r-ambiente-013", "ambiente", "propuesta", "ALTA",
    "Terminar la derogatoria de la llamada Ley Antiforestal; luchar contra la deforestación y el acaparamiento de tierras estableciendo una moratoria a los monocultivos industriales en la Amazonía.",
    "Terminar la derogatoria de la llamada Ley Antiforestal. Luchar contra la deforestación y el acaparamiento de tierras, estableciendo una moratoria a los monocultivos industriales en la Amazonía",
    f"{S71} — Medidas Propuestas", 341, 341,
))

nuevas.append(mk(
    "r-ambiente-014", "ambiente", "propuesta", "ALTA",
    "Implementar estrategias territoriales integrales para detener y revertir la deforestación, articulando ordenamiento territorial, gestión sostenible de bosques, gobernanza local y seguridad jurídica sobre la tierra.",
    "Implementar estrategias territoriales integrales para detener y revertir la deforestación",
    f"{S71} — Medidas Propuestas", 341, 341,
))

nuevas.append(mk(
    "r-ambiente-015", "ambiente", "propuesta", "MEDIA",
    "Recuperar ecosistemas degradados en cabeceras de cuenca y zonas de recarga hídrica, priorizando intervenciones de restauración para fortalecer la regulación hídrica y reducir vulnerabilidad frente a sequías e inundaciones.",
    "Recuperar ecosistemas degradados en cabeceras de cuenca y zonas de recarga hídrica",
    f"{S71} — Medidas Propuestas", 341, 341,
))

nuevas.append(mk(
    "r-ambiente-016", "ambiente", "propuesta", "MEDIA",
    "Programa nacional de manejo forestal comunitario: equipar a comunidades para control y vigilancia de bosques; compensar económicamente por reducir deforestación; promover asociatividad y diversificación de productos del bosque.",
    "Programa nacional de manejo forestal comunitario, consistente en: equipar a las comunidades para que realicen un control y vigilancia de los bosques",
    f"{S71} — Medidas Propuestas", 341, 341,
))

nuevas.append(mk(
    "r-ambiente-017", "ambiente", "propuesta", "MEDIA",
    "Pagos justos por servicios ecosistémicos a las comunidades y población que cuida los bosques y el ambiente, identificando previamente las áreas de impacto en procesos de certificación.",
    "Pagos justos por servicios ecosistémicos a las comunidades y a la población que cuida los bosques y el ambiente",
    f"{S71} — Medidas Propuestas", 341, 341,
))

nuevas.append(mk(
    "r-ambiente-018", "ambiente", "propuesta", "ALTA",
    "Reconocer a los Gobiernos Territoriales Autónomos de la Amazonía; ratificar el Acuerdo de Escazú e implementar un Sistema Nacional de Protección a Defensores Ambientales con mecanismos de alerta temprana.",
    "Reconocer a los Gobiernos Territoriales Autónomos de la Amazonía quienes se organizan en la defensa del agua y el bosque. Ratificar el Acuerdo de Escazú",
    f"{S71} — Medidas Propuestas", 341, 341,
))

nuevas.append(mk(
    "r-ambiente-019", "ambiente", "meta", "ALTA",
    "Implementar de forma inmediata un Plan Nacional de Restauración y Remediación Ambiental con participación ciudadana, financiado por impuesto a utilidades extraordinarias del sector extractivo; restaurar 500,000 hectáreas de ecosistemas degradados priorizando cabeceras de cuenca.",
    "Implementar de forma inmediata un Plan Nacional de Restauración y Remediación Ambiental con participación ciudadana, financiado por un impuesto a las utilidades extraordinarias del sector extractivo",
    f"{S71} — Medidas Propuestas", 343, 343,
    meta="500,000 ha de ecosistemas restaurados",
))

nuevas.append(mk(
    "r-ambiente-020", "ambiente", "meta", "ALTA",
    "Implementar tratamiento de aguas residuales en todas las ciudades de más de 50,000 habitantes, articulado con acciones del sector vivienda para mitigar impactos ambientales de la construcción de PTAR.",
    "Implementar tratamiento de aguas residuales en todas las ciudades de más de 50,000 habitantes",
    f"{S71} — Medidas Propuestas", 343, 343,
    meta="Tratamiento de aguas residuales en ciudades >50k habitantes",
))

nuevas.append(mk(
    "r-ambiente-021", "ambiente", "propuesta", "MEDIA",
    "Construcción de Plantas Regionales y Municipales de compostaje para gestión de residuos orgánicos orientada a la obtención de abonos orgánicos para la agroecología.",
    "Impulsaremos la construcción de Plantas Regionales y Municipales de compostaje para la gestión de residuos orgánicos",
    f"{S71} — Medidas Propuestas", 343, 343,
))

nuevas.append(mk(
    "r-ambiente-022", "ambiente", "propuesta", "MEDIA",
    "Implementar un sistema nacional de monitoreo de la calidad del aire con datos en tiempo real; reducir quema de residuos y fuentes urbanas de contaminación atmosférica.",
    "Implementar un sistema nacional de monitoreo de la calidad del aire con datos en tiempo real",
    f"{S71} — Medidas Propuestas", 343, 343,
))

nuevas.append(mk(
    "r-ambiente-023", "ambiente", "propuesta", "ALTA",
    "Fortalecer el sistema de gestión, supervisión y sanción ambiental (ANA, OEFA, SENACE y OSINERGMIN) garantizando autonomía y presupuesto; reforzar SENACE para garantizar instrumentos adecuados de gestión ambiental.",
    "Fortaleceremos el sistema de gestión, supervisión y sanción ambiental (ANA, OEFA, SENACE y OSINERMIN), garantizando autonomía y presupuesto",
    f"{S71} — Medidas Propuestas", 343, 343,
))

nuevas.append(mk(
    "r-ambiente-024", "ambiente", "principio", "ALTA",
    "Principio de Transición Energética Justa y Popular: promover soberanía sobre riqueza natural estratégica (gas, electromovilidad, cobre y otros minerales para la transición) y garantizar acceso universal a energías limpias y asequibles.",
    "Impulsar una Transición Energética Justa y Popular, que promueva la soberanía sobre nuestra riqueza natural estratégica",
    f"{S71} — Medidas Propuestas", 343, 343,
))

nuevas.append(mk(
    "r-ambiente-025", "ambiente", "propuesta", "MEDIA",
    "Reducir progresivamente la dependencia de combustibles fósiles en la matriz energética nacional, incrementando la participación de fuentes más limpias consistente con las NDC y la seguridad energética.",
    "Reducir progresivamente la dependencia de combustibles fósiles en la matriz energética nacional",
    f"{S71} — Medidas Propuestas", 343, 343,
))

nuevas.append(mk(
    "r-ambiente-026", "ambiente", "propuesta", "MEDIA",
    "Implementar el Plan Nacional de Energía Limpia y Eficiencia Energética con metas sectoriales vinculantes; impulsar alianzas público-privadas para hidrógeno verde, almacenamiento y geotermia.",
    "Implementar el Plan Nacional de Energía Limpia y Eficiencia Energética con metas sectoriales vinculantes",
    f"{S71} — Medidas Propuestas", 345, 345,
))

nuevas.append(mk(
    "r-ambiente-027", "ambiente", "propuesta", "MEDIA",
    "Lanzar el Programa Perú Circular para promover reciclaje, reutilización y reparación; cada sector tendrá su propio plan de economía circular según particularidades sectoriales.",
    "Lanzar el Programa Perú Circular para promover reciclaje, reutilización y reparación",
    f"{S71} — Medidas Propuestas", 345, 345,
))

nuevas.append(mk(
    "r-ambiente-028", "ambiente", "propuesta", "ALTA",
    "Crear un Fondo Nacional de Resiliencia Climática para financiar infraestructura natural y restauración de cuencas hidrográficas; Sistema Nacional de Prevención y Respuesta a Eventos Climáticos Extremos con monitoreo satelital y centros regionales.",
    "Crear un Fondo Nacional de Resiliencia Climática para financiar infraestructura natural y restauración de cuencas hidrográficas",
    f"{S71} — Medidas Propuestas", 345, 345,
))

nuevas.append(mk(
    "r-ambiente-029", "ambiente", "propuesta", "MEDIA",
    "Implementar las acciones pendientes de la Ley Marco de Cambio Climático, incluyendo los Fondos de Garantía aún no implementados; integrar la gestión del riesgo climático en la planificación del desarrollo.",
    "La Ley de Cambio Climático no ha concluido su implementación y las acciones pendientes serán prioridad de Juntos por el Perú",
    f"{S71} — Medidas Propuestas", 345, 345,
))

nuevas.append(mk(
    "r-ambiente-030", "ambiente", "propuesta", "MEDIA",
    "Implementar un Programa Nacional de Bionegocios Sostenibles con financiamiento y asistencia técnica; certificar y promover productos basados en la biodiversidad.",
    "Implementar un Programa Nacional de Bionegocios Sostenibles con financiamiento y asistencia técnica",
    f"{S71} — Medidas Propuestas", 345, 345,
))

nuevas.append(mk(
    "r-ambiente-031", "ambiente", "propuesta", "ALTA",
    "Crear un Consejo Nacional de Transición Socioecológica con enfoque de justicia social y ambiental que articule gobierno central, GORE y organizaciones sociales, con presupuesto autónomo y capacidad regulatoria bajo rectoría del MINAM.",
    "Crear un Consejo Nacional de Transición Socioecológica con enfoque de justicia social y ambiental",
    f"{S71} — Medidas Propuestas", 345, 345,
))

# =====================================================================
# 7.2 CULTURA (líneas 345-353) — tema: cultura (algunos a indigenas)
# =====================================================================
S72 = "Dimensión Cultural-Ambiental — 7.2 Cultura"

nuevas.append(mk(
    "r-cultura-001", "cultura", "principio", "ALTA",
    "Principio identitario: el Perú es una de las grandes cunas civilizatorias del mundo, con 55 pueblos indígenas y 48 lenguas originarias reconocidas oficialmente; pionero de la educación intercultural bilingüe.",
    "Somos un país creador de comunidades, festividades y artes; innovador en el campo de industrias culturales; con 55 pueblos indígenas y 48 lenguas originarias reconocidas oficialmente",
    f"{S72} — Situación Actual", 345, 345,
))

nuevas.append(mk(
    "r-indigenas-001", "indigenas", "diagnostico", "ALTA",
    "Diagnóstico étnico: según el Censo INEI 2017, aproximadamente el 23% de la población peruana pertenece a pueblos originarios — 20.1% quechuas, 2.8% aimaras y 0.7% amazónicos.",
    "Según el censo del INEI de 2017, aproximadamente el 23 % de la población peruana pertenece a pueblos originarios: 20.1 % quechuas, 2.8 % aimaras y 0.7 % amazónicos",
    f"{S72} — Situación Actual", 345, 345,
    meta="23% población pertenece a pueblos originarios (Censo 2017)",
))

nuevas.append(mk(
    "r-indigenas-002", "indigenas", "diagnostico", "ALTA",
    "Diagnóstico estructural: a partir de la colonización española se perpetúa una jerarquía social basada en el desprecio a culturas originarias, generando distribución desigual del poder económico, político y simbólico, traducida en racismo y exclusión política.",
    "a partir del proceso de colonización española y el inicio de la república, se sigue perpetuando la desigualdad en perjuicio de los pueblos indígenas, originarios y afroperuanos",
    f"{S72} — Situación Actual", 345, 345,
))

nuevas.append(mk(
    "r-cultura-002", "cultura", "diagnostico", "ALTA",
    "Diagnóstico de patrimonio arqueológico: más del 98% de los Monumentos Arqueológicos Prehispánicos declarados Patrimonio Cultural de la Nación no cuenta con proyectos de inversión pública, aumentando vulnerabilidad ante invasiones y actividades ilícitas.",
    "más del 98 % de los Monumentos Arqueológicos Prehispánicos declarados Patrimonio Cultural de la Nación no cuenta con proyectos de inversión pública",
    f"{S72} — Situación Actual", 347, 347,
    meta="98% Monumentos Arqueológicos sin proyectos de inversión",
))

nuevas.append(mk(
    "r-cultura-003", "cultura", "diagnostico", "MEDIA",
    "Diagnóstico de acceso cultural: la lectura de libros en adultos alfabetos casi duplica en estratos altos frente a ámbitos rurales; menor entre hablantes de lenguas indígenas y personas con discapacidad (ENL 2022 / INEI).",
    "La Encuesta Nacional de Lectura 2022 muestra que la lectura de libros en adultos alfabetos casi duplica en estratos altos frente a ámbitos rurales",
    f"{S72} — Situación Actual", 347, 347,
))

nuevas.append(mk(
    "r-cultura-004", "cultura", "diagnostico", "MEDIA",
    "Diagnóstico de infraestructura cultural: la infraestructura cultural básica está fuertemente concentrada; solo una parte de los gobiernos locales cuenta con bibliotecas públicas municipales; los museos del MINCUL se ubican sobre todo en Lima.",
    "La infraestructura cultural básica está fuertemente concentrada. Solo una parte de los gobiernos locales cuenta con bibliotecas públicas municipales",
    f"{S72} — Situación Actual", 347, 347,
))

nuevas.append(mk(
    "r-cultura-005", "cultura", "propuesta", "ALTA",
    "Plan y Campaña permanente de lucha contra el racismo y la discriminación que fomente el valor de la ciudadanía intercultural; Voluntariado Joven y Observatorio nacional para monitorear avances.",
    "Promoveremos un Plan y Campaña permanente de lucha contra el racismo y la discriminación, que fomente el valor de la ciudadanía intercultural",
    f"{S72} — Medidas Propuestas", 351, 351,
))

nuevas.append(mk(
    "r-cultura-006", "cultura", "propuesta", "MEDIA",
    "Programa nacional de capacitación a servidores públicos en no discriminación y derechos humanos; impulsar debate constitucional sobre derechos de la Madre Tierra y derechos colectivos en el horizonte del Buen Vivir.",
    "Implementación del Programa nacional de capacitación a servidores públicos en no discriminación y derechos humanos",
    f"{S72} — Medidas Propuestas", 351, 351,
))

nuevas.append(mk(
    "r-cultura-007", "cultura", "propuesta", "ALTA",
    "Crear el Ministerio de Las Culturas que releve el valor de la diversidad cultural y priorice las competencias respecto de pueblos indígenas originarios — como titulación de territorios y georreferenciación de comunidades nativas y campesinas.",
    "Crearemos el Ministerio de Las Culturas que releve el valor de nuestra diversidad cultural y que priorizará las competencias respecto de los pueblos indígenas originarios",
    f"{S72} — Medidas Propuestas", 351, 351,
))

nuevas.append(mk(
    "r-cultura-008", "cultura", "propuesta", "ALTA",
    "Implementar la pertinencia intercultural y lingüística (información en lenguas, programación representativa) y accesibilidad universal (discapacidad) en la oferta cultural priorizada por territorio.",
    "Implementaremos la pertinencia intercultural y lingüística (información y mediación cultural en lenguas, programación representativa) y accesibilidad universal",
    f"{S72} — Medidas Propuestas", 351, 351,
))

nuevas.append(mk(
    "r-cultura-009", "cultura", "propuesta", "MEDIA",
    "Lanzamiento de la Escuela Nacional de Ciudadanía articulada a los espacios de participación vecinal en los gobiernos locales.",
    "Lanzamiento de la Escuela Nacional de Ciudadanía articulada a los espacios de participación vecinal en los gobiernos locales",
    f"{S72} — Medidas Propuestas", 351, 351,
))

nuevas.append(mk(
    "r-cultura-010", "cultura", "propuesta", "ALTA",
    "Programa de recuperación y fortalecimiento de prácticas productivas y culturales de las comunidades originarias; afirmación de la vida en comunidad y cultura pública basada en respeto a la interculturalidad.",
    "Programa de recuperación y fortalecimientos de las prácticas productivas y culturales de las comunidades originarias",
    f"{S72} — Medidas Propuestas", 351, 351,
))

nuevas.append(mk(
    "r-cultura-011", "cultura", "propuesta", "MEDIA",
    "Acceso territorial a oferta cultural y deportiva: ampliar red de espacios culturales con programación regular, horarios extendidos y servicios accesibles, con énfasis en distritos rurales y periferias urbanas.",
    "Acceso territorial a oferta cultural y deportiva: Incrementar el acceso y ampliar una red de espacios culturales, artísticos y deportivos con programación regular",
    f"{S72} — Medidas Propuestas", 351, 351,
))

nuevas.append(mk(
    "r-cultura-012", "cultura", "propuesta", "MEDIA",
    "Promover el trabajo de organizaciones culturales comunitarias en todo el Perú convirtiendo Puntos de Cultura en un programa nacional.",
    "Promoveremos el trabajo de las organizaciones culturales comunitarias en todo el Perú convirtiendo Puntos de Cultura en un programa nacional",
    f"{S72} — Medidas Propuestas", 351, 351,
))

nuevas.append(mk(
    "r-cultura-013", "cultura", "propuesta", "MEDIA",
    "Fomentar la economía creativa y el encadenamiento productivo de industrias culturales con líneas concursables vía ProInnóvate/PRODUCE, laboratorios creativos regionales y marcas como Ruraq Maki.",
    "Fomentaremos la economía creativa y el encadenamiento productivo de industrias culturales: líneas concursables con ProInnóvate/Produce",
    f"{S72} — Medidas Propuestas", 351, 351,
))

nuevas.append(mk(
    "r-cultura-014", "cultura", "propuesta", "MEDIA",
    "Modificar la ley de cine con criterios democráticos y descentralistas; cuota de pantalla para el cine nacional con proporcionalidad de la diversidad regional.",
    "Modificaremos la ley de cine con criterios democráticos y descentralistas. Plantearemos una cuota de pantalla para el cine nacional con proporcionalidad de la diversidad regional",
    f"{S72} — Medidas Propuestas", 353, 353,
))

nuevas.append(mk(
    "r-cultura-015", "cultura", "propuesta", "MEDIA",
    "Crear las Olimpíadas Culturales del Perú, torneo anual para la valoración, cultivo, profesionalización y expansión de manifestaciones artísticas y culturales.",
    "Creación de las Olimpíadas Culturales del Perú, torneo anual para la valoración, cultivo, profesionalización y expansión de nuestras manifestaciones artísticas",
    f"{S72} — Medidas Propuestas", 353, 353,
))

nuevas.append(mk(
    "r-cultura-016", "cultura", "propuesta", "MEDIA",
    "Plan de fortalecimiento y democratización de los medios de comunicación públicos como estrategia transversal de reconstrucción democrática, con programación diferenciada vinculada a instituciones culturales y académicas.",
    "Crearemos el Plan de fortalecimiento y democratización de los medios de comunicación públicos para posicionarlos como una estrategia transversal de reconstrucción democrática",
    f"{S72} — Medidas Propuestas", 353, 353,
))

nuevas.append(mk(
    "r-cultura-017", "cultura", "propuesta", "MEDIA",
    "Impulsar la industria editorial con prioridad en las regiones; modificación de la Ley del Libro para la exoneración permanente del impuesto a la producción y venta de libros.",
    "Impulsaremos la industria editorial con prioridad en las regiones. Modificación de la Ley del Libro para la exoneración permanente del impuesto",
    f"{S72} — Medidas Propuestas", 353, 353,
))

nuevas.append(mk(
    "r-cultura-018", "cultura", "propuesta", "MEDIA",
    "Priorizar la lectura como política de ciudadanía: mediadores, bibliotecas itinerantes y digitales, enfoque rural y en lenguas originarias, alianzas con municipios y escuelas; metas por territorio y población prioritaria.",
    "Priorizaremos la lectura como política de ciudadanía: mediadores, bibliotecas itinerantes y digitales, enfoque rural y lenguas originarias",
    f"{S72} — Medidas Propuestas", 353, 353,
))

nuevas.append(mk(
    "r-cultura-019", "cultura", "propuesta", "MEDIA",
    "Recuperar bibliotecas municipales con estándares básicos (colección, conectividad, mediación lectora, accesibilidad) articuladas a Perú Lee y escuelas.",
    "Recuperaremos e impulsaremos bibliotecas municipales con estándares básicos (colección, conectividad, mediación lectora, accesibilidad) y programación",
    f"{S72} — Medidas Propuestas", 353, 353,
))

nuevas.append(mk(
    "r-cultura-020", "cultura", "propuesta", "BAJA",
    "Crear la Cinemateca y Fonoteca Nacional del Perú; fortalecer el Archivo General de la Nación priorizando la construcción de su nueva sede.",
    "Crearemos la Cinemateca y Fonoteca Nacional del Perú",
    f"{S72} — Medidas Propuestas", 353, 353,
))

nuevas.append(mk(
    "r-indigenas-003", "indigenas", "propuesta", "ALTA",
    "Promover la existencia de escaños reservados para asegurar la representación de pueblos originarios en el Congreso de la República y otros espacios de elección popular.",
    "Promoveremos la existencia de escaños reservados para asegurar la representación de pueblos originarios en el Congreso de la República",
    f"{S72} — Medidas Propuestas", 353, 353,
))

nuevas.append(mk(
    "r-indigenas-004", "indigenas", "propuesta", "ALTA",
    "Garantizar la participación de pueblos indígenas originarios en la dirección y gestión estatal, a través de cuotas y otros mecanismos.",
    "Garantizar la participación de pueblos indígenas originarios en la dirección y gestión estatal, a través de cuotas y otros mecanismos",
    f"{S72} — Medidas Propuestas", 353, 353,
))

nuevas.append(mk(
    "r-cultura-021", "cultura", "propuesta", "MEDIA",
    "Impulsar una Ley General de la Cocina Peruana entendiéndola como manifestación y eje articulador de la identidad cultural y social como nación, y como motor de dinamización de la economía nacional y local en vinculación con la actividad turística.",
    "Impulsar una Ley General de la Cocina Peruana, entendiéndola como manifestación y eje articulador de nuestra identidad cultural",
    f"{S72} — Medidas Propuestas", 353, 353,
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
