# -*- coding: utf-8 -*-
"""Extracción de Dimensión Internacional - Roberto Sánchez (Task 15).

Cubre secciones 8.1 (Defensa Nacional), 8.2 (Relaciones Exteriores)
y 8.3 (Peruanos en el Exterior).

Nota de tema: 8.1 Defensa Nacional se asigna a 'exterior' por estar
enmarcada en la Dimensión Internacional como parte de la política
soberana del Estado peruano frente al exterior.
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
# 8.1 DEFENSA NACIONAL (líneas 359-365) — tema: exterior
# (continúa desde r-exterior-005)
# =====================================================================
S81 = "Dimensión Internacional — 8.1 Defensa Nacional"

nuevas.append(mk(
    "r-exterior-006", "exterior", "principio", "ALTA",
    "Principio de soberanía: el problema central de los Estados es el respeto a la soberanía reconocido en la Carta de la ONU; corresponde al gobierno y a las FFAA tomar seriamente este principio y vigilar su cumplimiento.",
    "el problema central de los Estados y los pueblos del mundo, tal como lo revelan las guerras y conflictos que actualmente ocurren, es el respeto a la soberanía de los Estados, principio reconocido en la Carta de Naciones Unidas",
    f"{S81} — Situación Actual", 359, 359,
))

nuevas.append(mk(
    "r-exterior-007", "exterior", "diagnostico", "MEDIA",
    "Diagnóstico territorial: la selva peruana ocupa el 60.3% del territorio nacional pero tiene una densidad poblacional del 9.4%; se requiere nueva proyección de FFAA hacia la selva para asegurar defensa y crear polos de desarrollo.",
    "la cual, ocupa el 60.3 % del territorio nacional, pero tiene una densidad poblacional del 9.4 %",
    f"{S81} — Situación Actual", 359, 359,
    meta="Selva: 60.3% territorio, 9.4% densidad poblacional",
))

nuevas.append(mk(
    "r-exterior-008", "exterior", "diagnostico", "MEDIA",
    "Diagnóstico de ciberdefensa: las capacidades de ciberdefensa han mejorado en el sector defensa pero aún son muy limitadas; el ciberespacio constituye dimensión de gran relevancia para el devenir nacional.",
    "el Ciberespacio constituye una dimensión de gran relevancia para el devenir nacional",
    f"{S81} — Situación Actual", 359, 359,
))

nuevas.append(mk(
    "r-exterior-009", "exterior", "propuesta", "ALTA",
    "Desclasificar, transparentar y poner a disposición de autoridades judiciales toda la información relevante respecto de los sucesos de violencia del Estado ocurridos entre 1980/2000 y 2022-2025.",
    "Desclasificar, transparentar y poner a disposición de autoridades judiciales, toda la información relevante, respecto de los sucesos de violencia del Estado ocurridos entre 1980/2000 y 2022-2025",
    f"{S81} — Medidas Propuestas", 361, 361,
))

nuevas.append(mk(
    "r-exterior-010", "exterior", "propuesta", "ALTA",
    "Crear unidad especializada e independiente para casos de uso ilegítimo de la fuerza en FFAA, articulada con fiscalías y órganos disciplinarios, con peritos y capacidades de investigación financiera.",
    "Crear una unidad especializada e independiente para casos de uso ilegítimo de la fuerza en FF.AA., articulada con fiscalías y órganos disciplinarios",
    f"{S81} — Medidas Propuestas", 361, 361,
))

nuevas.append(mk(
    "r-exterior-011", "exterior", "propuesta", "ALTA",
    "Imprescriptibilidad de los delitos de lesa humanidad, control difuso y no aplicabilidad de amnistías contra violaciones a los DDHH.",
    "Imprescriptibilidad de los delitos de lesa humanidad, control difuso y no aplicabilidad de amnistías contra violaciones a los DDHH",
    f"{S81} — Medidas Propuestas", 361, 361,
))

nuevas.append(mk(
    "r-exterior-012", "exterior", "meta", "MEDIA",
    "Implementar el Programa Presupuestal ESCUDO III, incrementándolo al doble de la cantidad existente.",
    "Implementar el Programa Presupuestal ESCUDO III, incrementándolo al doble de la cantidad existente",
    f"{S81} — Medidas Propuestas", 361, 361,
    meta="Programa ESCUDO III: duplicar presupuesto",
))

nuevas.append(mk(
    "r-exterior-013", "exterior", "propuesta", "ALTA",
    "Sistema único y obligatorio de registro de todas las operaciones de FFAA en apoyo al orden interno, con datos de uso de la fuerza, identidad de mandos y registro audiovisual; alertas automáticas ante muertos o heridos graves.",
    "Crear un sistema único y obligatorio de registro de todas las operaciones de FF.AA. en apoyo al orden interno",
    f"{S81} — Medidas Propuestas", 361, 361,
))

nuevas.append(mk(
    "r-exterior-014", "exterior", "propuesta", "MEDIA",
    "Aprobar protocolo único para empleo de FFAA en apoyo a la PNP alineado a estándares internacionales, con registro obligatorio de todo incidente con uso de la fuerza y apertura automática de investigaciones.",
    "Aprobar un protocolo único para empleo de FF.AA. en apoyo a la PNP, alineado a estándares internacionales",
    f"{S81} — Medidas Propuestas", 361, 361,
))

nuevas.append(mk(
    "r-exterior-015", "exterior", "propuesta", "MEDIA",
    "Política de asentamiento regulado en zonas de frontera para poblaciones jóvenes y establecimiento de zonas especiales de industrialización; ocupación sostenible de la Amazonía en armonía con comunidades nativas.",
    "Política de asentamiento regulado en zonas de frontera, en especial para poblaciones jóvenes, así como para el establecimiento de zonas especiales de industrialización",
    f"{S81} — Medidas Propuestas", 361, 361,
))

nuevas.append(mk(
    "r-exterior-016", "exterior", "propuesta", "MEDIA",
    "Participación de las FFAA en tareas de desarrollo en zonas empobrecidas: habilitación de vías, sistemas de comunicaciones, rehabilitación de zonas afectadas y gestión del riesgo de desastres con INDECI, CENEPRED, SENAMHI e IMARPE.",
    "Participación de las Fuerzas Armadas en las tareas de desarrollo en las zonas empobrecidas del país, habilitación de vías, sistema de comunicaciones",
    f"{S81} — Medidas Propuestas", 361, 361,
))

nuevas.append(mk(
    "r-exterior-017", "exterior", "propuesta", "ALTA",
    "Redefinir el rol de las FFAA ante amenazas a defensa y seguridad nacionales, priorizando el control efectivo sobre fronteras y territorio, y la protección de la Amazonía peruana y sus recursos naturales.",
    "Redefinir el rol de las FFAA ante las amenazas a la defensa y seguridad nacionales, priorizando el control efectivo sobre las fronteras y el territorio",
    f"{S81} — Medidas Propuestas", 363, 363,
))

nuevas.append(mk(
    "r-exterior-018", "exterior", "propuesta", "MEDIA",
    "Crear o fortalecer una academia conjunta de defensa que integre doctrina, entrenamiento y certificación en operaciones conjuntas, ciberdefensa, protección de infraestructuras críticas y derechos humanos.",
    "Crear o fortalecer una academia conjunta de defensa que integre doctrina, entrenamiento y certificación en operaciones conjuntas",
    f"{S81} — Medidas Propuestas", 363, 363,
))

nuevas.append(mk(
    "r-exterior-019", "exterior", "propuesta", "MEDIA",
    "Desarrollar una red integrada de vigilancia y control de espacios marítimos, aéreos y fronterizos combinando radares, sensores, satélites y patrullas, con cooperación con países vecinos.",
    "Desarrollar una red integrada de vigilancia y control de espacios marítimos, aéreos y fronterizos",
    f"{S81} — Medidas Propuestas", 363, 363,
))

nuevas.append(mk(
    "r-exterior-020", "exterior", "propuesta", "ALTA",
    "Conformar un solo Servicio Nacional de Inteligencia al que se adscriben las ramas de cada FFAA, con alto profesionalismo y sólidos valores éticos y democráticos.",
    "La conformación de un solo Servicio Nacional de Inteligencia, al que se adscriben las ramas de cada FFAA",
    f"{S81} — Medidas Propuestas", 363, 363,
))

nuevas.append(mk(
    "r-exterior-021", "exterior", "propuesta", "MEDIA",
    "Repotenciar el Comando Operacional de Ciberdefensa con personal especializado, capacidades de detección y respuesta, equipamiento y marcos de cooperación internacional.",
    "Repotenciar el Comando Operacional de Ciberdefensa, en coordinación con la autoridad nacional competente",
    f"{S81} — Medidas Propuestas", 363, 363,
))

nuevas.append(mk(
    "r-exterior-022", "exterior", "propuesta", "MEDIA",
    "Establecimiento progresivo del Servicio Civil obligatorio (no acuartelado) en etapa formativa: atención de desastres, formación cívica, primeros auxilios, como incentivo para carrera pública y educación superior.",
    "Establecimiento progresivo del Servicio Civil obligatorio (no acuartelado) en etapa formativa",
    f"{S81} — Medidas Propuestas", 363, 363,
))

nuevas.append(mk(
    "r-exterior-023", "exterior", "propuesta", "MEDIA",
    "Modernización de la capacidad disuasiva de las tres armas a partir de una adecuada relación costo-beneficio; mejorar condiciones de la Estación Científica Machupicchu y capacidades del BAP CARRASCO.",
    "Modernización de la capacidad disuasiva de las tres armas, a partir de una adecuada relación costo beneficio",
    f"{S81} — Medidas Propuestas", 363, 363,
))

nuevas.append(mk(
    "r-exterior-024", "exterior", "propuesta", "ALTA",
    "Ante el inminente Fenómeno del Niño 2026 de alta intensidad, formar comando de acción en alianza pública, privada y militar en el marco del SINAGERD para la alerta, prevención, respuesta y rehabilitación.",
    "Ante la inminencia del Fenómeno del Niño 2026 de alta intensidad, el gobierno formará un comando de acción en alianza pública, privada y militar",
    f"{S81} — Medidas Propuestas", 363, 363,
))

nuevas.append(mk(
    "r-exterior-025", "exterior", "propuesta", "MEDIA",
    "Vincular las compras militares con la producción local alimentaria e industrial; fortalecer SIMA y SEMAN.",
    "Vincular las compras militares con la producción local alimentaria e industrial",
    f"{S81} — Medidas Propuestas", 365, 365,
))

nuevas.append(mk(
    "r-exterior-026", "exterior", "propuesta", "MEDIA",
    "Implementar plan de sensibilización del sector defensa en I+D con resultados tangibles al cuarto año; fortalecer la Industria Militar con convenios de transferencia tecnológica.",
    "implementar un plan de sensibilización y culturización del sector defensa en Investigación y Desarrollo con resultados tangibles y medibles al cuarto año de mandato",
    f"{S81} — Medidas Propuestas", 365, 365,
))

# =====================================================================
# 8.2 RELACIONES EXTERIORES (líneas 365-373) — tema: exterior
# =====================================================================
S82 = "Dimensión Internacional — 8.2 Relaciones Exteriores"

nuevas.append(mk(
    "r-exterior-027", "exterior", "diagnostico", "ALTA",
    "Diagnóstico de deterioro institucional: la democracia peruana ha atravesado un profundo deterioro institucional; la capacidad de la política exterior peruana para defender democracia y DDHH se ha visto debilitada en foros internacionales.",
    "En los últimos años, la democracia en el Perú ha atravesado un proceso de profundo deterioro institucional. En consecuencia, la capacidad de la política exterior peruana para defender la democracia",
    f"{S82} — Situación Actual", 365, 365,
))

nuevas.append(mk(
    "r-exterior-028", "exterior", "diagnostico", "MEDIA",
    "Diagnóstico de pérdida de liderazgo regional: el Perú ha visto reducida su presencia y liderazgo en América Latina; la persistente inestabilidad política y cuestionamientos en DDHH han debilitado los vínculos vecinales.",
    "El Perú ha visto reducida su presencia y liderazgo en América Latina. La persistente inestabilidad política, junto con los cuestionamientos en materia de democracia y derechos humanos",
    f"{S82} — Situación Actual", 365, 365,
))

nuevas.append(mk(
    "r-exterior-029", "exterior", "principio", "ALTA",
    "Principio rector: la política exterior del Perú será nacional, autónoma, humanista, democrática, social, descentralizada, medioambiental, normativa, institucional y pro paz.",
    "La política exterior del Perú será nacional, autónoma, humanista, democrática, social, descentralizada, medioambiental, normativa, institucional y pro paz",
    f"{S82} — Medidas Propuestas", 367, 367,
))

nuevas.append(mk(
    "r-exterior-030", "exterior", "propuesta", "ALTA",
    "Mantener relaciones de amistad y cooperación con todos los países, especialmente latinoamericanos, EE.UU., China, Europa, Corea, Japón e India por su importancia para la inserción internacional del Perú.",
    "Se mantendrán relaciones de amistad y cooperación con todos los países, especialmente con los países latinoamericanos, los Estados Unidos, China, Europa, Corea, Japón y la India",
    f"{S82} — Medidas Propuestas", 367, 367,
))

nuevas.append(mk(
    "r-exterior-031", "exterior", "principio", "ALTA",
    "La política exterior promoverá crecimiento económico inclusivo, desarrollo social, sostenibilidad ambiental, protección y promoción de DDHH, y una gobernanza multilateral basada en el Derecho Internacional y la Carta de la ONU.",
    "La política exterior promoverá el crecimiento económico inclusivo, el desarrollo social, la sostenibilidad ambiental, la protección y promoción de los derechos humanos",
    f"{S82} — Medidas Propuestas", 367, 367,
))

nuevas.append(mk(
    "r-exterior-032", "exterior", "100dias", "100DIAS",
    "Compromiso de 100 días: enviar al Congreso dentro de los primeros 30 días de gobierno el proyecto de Ley de Derechos de los peruanos y peruanas en el Exterior que los proteja sin discriminación.",
    "Será también una diplomacia para las clases medias y los sectores populares del país a través de la diplomacia social y el enfoque descentralizado de gestión. Protegerá activamente a los peruanos",
    f"{S82} — Medidas Propuestas", 367, 367,
))

nuevas.append(mk(
    "r-exterior-033", "exterior", "propuesta", "ALTA",
    "Reactivar los Gabinetes Binacionales y mecanismos de cooperación bilateral existentes; promover la Política Nacional para el Desarrollo e Integración Fronterizos con inversión y presencia estatal.",
    "Reactivar los Gabinetes Binacionales y mecanismos de cooperación bilateral existentes, y promover nuevos espacios de desarrollo conjunto",
    f"{S82} — Medidas Propuestas", 371, 371,
))

nuevas.append(mk(
    "r-exterior-034", "exterior", "propuesta", "ALTA",
    "Defender la soberanía y promover la integración regional: relanzar UNASUR, fortalecer la CELAC como bloque autónomo y promover programa estratégico de cooperación Sur-Sur con integración del Perú a los BRICS+.",
    "Defender la soberanía y promover la integración regional: relanzar UNASUR, fortalecer la CELAC como bloque autónomo",
    f"{S82} — Medidas Propuestas", 373, 373,
))

nuevas.append(mk(
    "r-exterior-035", "exterior", "propuesta", "ALTA",
    "Enfrentar la ofensiva neo-monroísta: promover una posición hemisférica común contra la injerencia externa, el despliegue militar en el Caribe y el rechazo a la instalación de bases militares extranjeras en la región.",
    "Enfrentar la ofensiva neo-monroísta: promover una posición hemisférica común contra la injerencia externa, el despliegue militar en el Caribe",
    f"{S82} — Medidas Propuestas", 373, 373,
))

nuevas.append(mk(
    "r-exterior-036", "exterior", "propuesta", "ALTA",
    "Impedir la salida de la Corte Interamericana de Derechos Humanos y restaurar el compromiso del Perú con el Sistema Interamericano de Derechos Humanos.",
    "Impedir la salida de la Corte Interamericana de Derechos Humanos y restaurar el compromiso del Perú con el Sistema Interamericano de Derechos Humanos",
    f"{S82} — Medidas Propuestas", 373, 373,
))

nuevas.append(mk(
    "r-exterior-037", "exterior", "propuesta", "MEDIA",
    "Utilizar el foro APEC, la Alianza del Pacífico y el CPTPP como herramientas para la integración económica en el Asia-Pacífico; mayor presencia en BRICS, G77 y UNCTAD.",
    "Utilizar el foro APEC, la Alianza Pacífico y el CPTPP como herramientas para nuestra integración económica en el Asia-Pacífico",
    f"{S82} — Medidas Propuestas", 371, 371,
))

nuevas.append(mk(
    "r-exterior-038", "exterior", "propuesta", "MEDIA",
    "Apuntalar el proceso de adhesión a la OCDE con el firme compromiso del Perú con la democracia, el Estado de derecho, los DDHH, la equidad de género y el medio ambiente.",
    "Apuntalar el proceso de adhesión a la OCDE con el firme compromiso del Perú con la democracia, el Estado de derecho, los derechos humanos",
    f"{S82} — Medidas Propuestas", 373, 373,
))

nuevas.append(mk(
    "r-exterior-039", "exterior", "propuesta", "MEDIA",
    "Desarrollar diplomacias específicas: diplomacia científica para cooperación e investigación; diplomacia universitaria con becas y movilidad; diplomacia ambiental de liderazgo en cambio climático con énfasis en la Amazonía.",
    "Promover una diplomacia científica que facilite la cooperación y la participación en foros internacionales",
    f"{S82} — Medidas Propuestas", 373, 373,
))

nuevas.append(mk(
    "r-exterior-040", "exterior", "propuesta", "MEDIA",
    "Política migratoria con enfoque de derechos: promover procesos de regularización, certificación laboral, acceso a educación y flexibilización normativa para garantizar integración, reduciendo la xenofobia y la explotación.",
    "Política migratoria con enfoque de derechos: promover procesos de regularización, certificación laboral, acceso a educación",
    f"{S82} — Medidas Propuestas", 373, 373,
))

# =====================================================================
# 8.3 PERUANOS EN EL EXTERIOR (líneas 373-377) — tema: peruanos_exterior
# =====================================================================
S83 = "Dimensión Internacional — 8.3 Peruanos en el Exterior"

nuevas.append(mk(
    "r-peruanos_exterior-001", "peruanos_exterior", "diagnostico", "ALTA",
    "Diagnóstico cuantitativo: según INEI 2024 los peruanos en el exterior son 3.5 millones (10.3% de la población); concentrados en EE.UU., España, Argentina, Chile e Italia; remesas >US$ 5,000 millones en 2025 (1.7% del PBI).",
    "Según el INEI al año 2024, los peruanos en el exterior son 3.5 millones, representando el 10.3% de la población. La migración se concentra en EE.UU, España, Argentina, Chile e Italia",
    f"{S83} — Situación Actual", 375, 375,
    meta="3.5M peruanos exterior (10.3% población); remesas >US$5B (1.7% PBI)",
))

nuevas.append(mk(
    "r-peruanos_exterior-002", "peruanos_exterior", "diagnostico", "MEDIA",
    "Diagnóstico institucional: los registros consulares son fragmentarios y voluntarios, lo que impide conocer la magnitud real de la diáspora peruana, su distribución y necesidades específicas.",
    "Los registros actuales de los consulados son fragmentarios y voluntarios, lo que impide conocer la magnitud real de la diáspora peruana",
    f"{S83} — Situación Actual", 375, 375,
))

nuevas.append(mk(
    "r-peruanos_exterior-003", "peruanos_exterior", "propuesta", "ALTA",
    "Crear una Clínica de Desarrollo Territorial para Peruanos en el Exterior: espacio permanente de articulación entre el Estado peruano y la comunidad migrante.",
    "se propone la creación de una Clínica de Desarrollo Territorial para Peruanos en el Exterior, un espacio permanente de articulación entre el Estado peruano y la comunidad migrante",
    f"{S83} — Medidas Propuestas", 375, 375,
))

nuevas.append(mk(
    "r-peruanos_exterior-004", "peruanos_exterior", "propuesta", "MEDIA",
    "Implementar un correo institucional para peruanos en el exterior vinculado al programa de la Clínica de Desarrollo Territorial.",
    "se propone la implementación de un correo institucional para peruanos en el exterior, vinculado al programa de la Clínica de Desarrollo Territorial",
    f"{S83} — Medidas Propuestas", 375, 375,
))

nuevas.append(mk(
    "r-peruanos_exterior-005", "peruanos_exterior", "propuesta", "ALTA",
    "Crear un Registro Territorial de Peruanos en el Exterior que incluya tanto personas individuales como organizaciones sociales, productivas y culturales formadas por peruanos en cada país.",
    "la creación de un Registro Territorial de Peruanos en el Exterior, que permita conocer y visibilizar la diversidad de actores que conforman la comunidad peruana",
    f"{S83} — Medidas Propuestas", 375, 375,
))

nuevas.append(mk(
    "r-peruanos_exterior-006", "peruanos_exterior", "propuesta", "ALTA",
    "Implementar el Censo de Peruanos en el Exterior (CIPEX) como instrumento oficial de registro, diagnóstico y acompañamiento integral coordinado por MRE y gestionado por Cancillerías, Embajadas y Consulados.",
    "Se propone la implementación de un Censo de Peruanos en el Exterior (CIPEX) como un instrumento oficial de registro",
    f"{S83} — Medidas Propuestas", 375, 375,
))

nuevas.append(mk(
    "r-peruanos_exterior-007", "peruanos_exterior", "propuesta", "MEDIA",
    "Crear un Instituto de Peruanos en el Exterior y una Plataforma Digital Integrada de Cultura, Educación y Emprendimiento Peruano articulada con MRE, Cultura, Educación y Producción.",
    "se propone la creación de un Instituto e Peruanos en el Exterior y una Plataforma Digital Integrada de Cultura, Educación y Emprendimiento Peruano en el Exterior",
    f"{S83} — Medidas Propuestas", 377, 377,
))

nuevas.append(mk(
    "r-peruanos_exterior-008", "peruanos_exterior", "propuesta", "MEDIA",
    "Crear un Programa de Financiamiento y Formación para Emprendimientos Culturales e Identitarios con fondos públicos gestionados desde el MRE en articulación con Cultura, Educación y los consulados.",
    "se propone la creación de un Programa de Financiamiento y Formación para Emprendimientos Culturales e Identitarios",
    f"{S83} — Medidas Propuestas", 369, 369,
))

nuevas.append(mk(
    "r-peruanos_exterior-009", "peruanos_exterior", "propuesta", "MEDIA",
    "Línea permanente de Talleres de Apoyo Subjetivo y Comunitario para fortalecer la salud emocional, identidad cultural y conciencia colectiva de los peruanos en el exterior.",
    "Se propone crear una línea permanente de Talleres de Apoyo Subjetivo y Comunitario, orientada a fortalecer la salud emocional",
    f"{S83} — Medidas Propuestas", 377, 377,
))

nuevas.append(mk(
    "r-peruanos_exterior-010", "peruanos_exterior", "propuesta", "ALTA",
    "Apoyo y acompañamiento en casos de detención, deportación y conflictos legales; agilización de trámites como poderes y recuperación, en especial para compatriotas indocumentados.",
    "Apoyo y acompañamiento en casos de detención, deportación y conflictos legales y agilización de trámites como poderes",
    f"{S83} — Medidas Propuestas", 377, 377,
))

nuevas.append(mk(
    "r-peruanos_exterior-011", "peruanos_exterior", "propuesta", "ALTA",
    "Promover un sistema público a través del Banco de la Nación para la recepción de remesas; facilitación de canales de bajo costo para envío de remesas y canalización de capitales de inversión.",
    "Promover un sistema público, a través del Banco de la Nación para la recepción de remesas",
    f"{S83} — Medidas Propuestas", 377, 377,
))

nuevas.append(mk(
    "r-peruanos_exterior-012", "peruanos_exterior", "propuesta", "MEDIA",
    "Modificar la 'Ley de Retorno' para extender sus beneficios no solo a peruanos exitosos sino también a quienes tienen dificultades económicas y requieren reinsertarse en la vida laboral.",
    "Modificar la “Ley de Retorno” que extienda sus beneficios no sólo a los peruanos exitosos sino también a los que tienen dificultades económicas",
    f"{S83} — Medidas Propuestas", 377, 377,
))

nuevas.append(mk(
    "r-peruanos_exterior-013", "peruanos_exterior", "propuesta", "MEDIA",
    "Mejora sustancial en el acceso a servicios consulares, trámites, distancias y costos; mejora del sistema consular digital para ejercicio pleno de derechos ciudadanos.",
    "Mejora sustancial en el acceso a los servicios consulares, trámites, distancias y costos, mejora del sistema consular digital",
    f"{S83} — Medidas Propuestas", 377, 377,
))

nuevas.append(mk(
    "r-peruanos_exterior-014", "peruanos_exterior", "propuesta", "ALTA",
    "Apoyo del gobierno nacional para condiciones laborales no precarias en el exterior: amparo contra discriminación y xenofobia, protección contra trata de personas, acceso a salud y seguridad social, asistencia legal especializada.",
    "Apoyo del gobierno nacional para que puedan desempeñarse en condiciones laborales no precarias en el exterior, en cuanto se refiere al amparo con la discriminación y xenofobia",
    f"{S83} — Medidas Propuestas", 377, 377,
))

nuevas.append(mk(
    "r-peruanos_exterior-015", "peruanos_exterior", "propuesta", "MEDIA",
    "Crear un programa financiero integral articulado entre el Banco de la Nación del Perú, la Cancillería y los Consulados para fortalecer el acompañamiento a los peruanos en el exterior.",
    "uno de los ejes fundamentales para fortalecer el acompañamiento a las y los peruanos en el exterior es la creación de un programa financiero integral",
    f"{S83} — Medidas Propuestas", 377, 377,
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
