# -*- coding: utf-8 -*-
"""Extracción de Dimensión Infraestructura y Servicios Básicos - Roberto (Task 12).

Cubre secciones 5.1 a 5.8: Transporte, Telecomunicaciones, Energía,
Agricultura, Turismo, Pesca, Vivienda y Agua/Saneamiento.

Nota de tema: Telecomunicaciones (5.2) se asigna a 'transporte' para
mantener consistencia con la sub-sección equivalente de Keiko (Pilar 2 §2.6
'Transportes y Comunicaciones').
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
# 5.1 TRANSPORTE (líneas 225-241) — tema: transporte
# =====================================================================
S51 = "Dimensión Infraestructura — 5.1 Transporte"

nuevas.append(mk(
    "r-transporte-001", "transporte", "diagnostico", "ALTA",
    "Diagnóstico de costo logístico: el costo de distribución de transporte equivale al 26% del PBI, atribuido a la mala calidad de carreteras subnacionales (departamentales y vecinales).",
    "El costo logístico de la distribución de transporte equivale al 26% del PBI. Los mayores costos se deben a la mala calidad de las carreteras subnacionales",
    f"{S51} — Situación Actual", 227, 227,
    meta="Costo logístico = 26% del PBI",
))

nuevas.append(mk(
    "r-transporte-002", "transporte", "diagnostico", "MEDIA",
    "Diagnóstico de caminos rurales: el MTC registra 120,000 km pero la red real supera 180,000 km; más del 80% están en mal estado con déficit de mantenimiento significativo.",
    "El MTC, al cierre de 2024, tiene registrados 120 000 km de caminos rurales que atienden a la población en sus traslados a centros urbanos provinciales; sin embargo, se estima que la red real supera los 180,000 km",
    f"{S51} — Situación Actual", 227, 227,
))

nuevas.append(mk(
    "r-transporte-003", "transporte", "diagnostico", "ALTA",
    "Diagnóstico de seguridad vial: en 2023 se produjeron 87,083 accidentes con 58,000 heridos y 3,316 fallecidos; tasa de mortalidad 12.7 por 100 mil habitantes, superior al resto de la región.",
    "El Observatorio Nacional de Seguridad Vial reportó que en 2023 se produjeron 87,083 accidentes de tránsito, resultando en 58,000 heridos y 3,316 fallecidos",
    f"{S51} — Situación Actual", 227, 227,
    meta="87,083 accidentes; 3,316 fallecidos (2023); 12.7 muertes/100k hab",
))

nuevas.append(mk(
    "r-transporte-004", "transporte", "diagnostico", "MEDIA",
    "Diagnóstico estructural: el Perú es uno de los pocos países que no subsidia el transporte urbano; solo en Lima existen más de 2 millones de personas de bajos recursos sin acceso a transporte masivo.",
    "Sólo en Lima existen más de 2 millones de personas de bajos recursos que no tienen acceso al transporte masivo. El Perú es uno de los pocos países que no subsidia el transporte urbano",
    f"{S51} — Situación Actual", 229, 229,
))

nuevas.append(mk(
    "r-transporte-005", "transporte", "propuesta", "ALTA",
    "Puesta en funcionamiento de la Línea 2 del Metro de Lima e inicio de ejecución de la Línea 3, articulada a los trenes de cercanía norte y sur.",
    "Puesta en funcionamiento de la Línea 2. • Iniciar ejecución de la Línea 3 articulada a los trenes de cercanía norte y sur",
    f"{S51} — Medidas Propuestas", 231, 231,
))

nuevas.append(mk(
    "r-transporte-006", "transporte", "propuesta", "ALTA",
    "Crear y mejorar ferrocarriles estratégicos en tres fases: Fase 1 incluye ferrocarril costero (Lima-Ica, Lima-Barranca) y túnel transandino con modernización del Ferrocarril Central.",
    "Se realizará la creación y mejoramiento de ferrocarriles estratégicos en tres fases de inversión",
    f"{S51} — Medidas Propuestas", 231, 231,
))

nuevas.append(mk(
    "r-transporte-007", "transporte", "propuesta", "MEDIA",
    "Fase 2 ferroviaria: Huancavelica-Ayacucho; modernización Cusco-Puno-Arequipa; rehabilitación Cusco-Quillabamba vía APP. Fase 3: Cajamarca-Bayóvar y Apurímac-Ica.",
    "Realización de los estudios básicos, diseño conceptual, expediente técnico y ejecución del 25% del ferrocarril Huancavelica-Ayacucho. ▪ Modernización del Ferrocarril Cusco-Puno-Arequipa",
    f"{S51} — Medidas Propuestas", 236, 236,
))

nuevas.append(mk(
    "r-transporte-008", "transporte", "propuesta", "MEDIA",
    "Adecuar la reglamentación del transporte acuático a la realidad de los ríos de la Selva; navegabilidad de Amazonas, Ucayali, Huallaga, Marañón, Napo, Putumayo y Urubamba; nuevos puertos de Sinchicuy (Loreto) y Pucallpa.",
    "Realizar los estudios de preinversión, estudios técnicos y ejecución de las acciones de navegabilidad de los principales ríos de la Amazonía (Amazonas, Ucayali, Huallaga, Marañón, Napo, Putumayo y Urubamba)",
    f"{S51} — Medidas Propuestas", 237, 237,
))

nuevas.append(mk(
    "r-transporte-009", "transporte", "propuesta", "MEDIA",
    "Trasladar la sede central de ENAPU a la Selva como Administrador Portuario de la Selva, para conducir inversiones en embarcaderos de carga y pasajeros.",
    "La sede central de la empresa ENAPU se trasladará a la Selva y será el Administrador Portuario de la Selva. ENAPU conducirá las inversiones en Embarcaderos",
    f"{S51} — Medidas Propuestas", 237, 237,
))

nuevas.append(mk(
    "r-transporte-010", "transporte", "propuesta", "MEDIA",
    "Financiar el 50% de inversiones faltantes para pavimentar la Red Vial Departamental siempre que los GORE mejoren las carreteras con contratos por niveles de servicio.",
    "Financiaremos el 50% de las inversiones faltantes para pavimentar la Red Vial Departamental, siempre que los GORES mejoren las carreteras con contratos por niveles de servicio",
    f"{S51} — Medidas Propuestas", 239, 239,
    meta="50% cofinanciamiento Red Vial Departamental",
))

nuevas.append(mk(
    "r-transporte-011", "transporte", "meta", "ALTA",
    "Meta de caminos rurales: pavimentar con solución básica y conservar 8,000 km de caminos rurales prioritarios; rehabilitar y conservar en afirmado 20,000 km adicionales con contratos por niveles de servicio.",
    "Pavimentaremos con solución básica (pavimento no definitivo) y conservaremos 8,000 km de caminos rurales prioritarios mediante contratos por niveles de servicio. • Rehabilitaremos y conservaremos en afirmado 20 000 km",
    f"{S51} — Medidas Propuestas", 239, 239,
    meta="8,000 km caminos pavimentados + 20,000 km afirmado",
))

nuevas.append(mk(
    "r-transporte-012", "transporte", "meta", "ALTA",
    "Recuperar transitabilidad y mantener (mantenimiento rutinario) 60,000 km de vías rurales mediante microempresas de campesinos organizadas por las comunidades, con contratos por niveles de servicio de 5 años.",
    "Recuperaremos la transitabilidad y mantendremos (con mantenimiento rutinario) 60,000 km de vías rurales mediante microempresas de campesinos organizadas por las comunidades",
    f"{S51} — Medidas Propuestas", 239, 239,
    meta="60,000 km vías rurales mantenidas por microempresas campesinas",
))

nuevas.append(mk(
    "r-transporte-013", "transporte", "propuesta", "MEDIA",
    "Plan de Chatarreo para camiones de más de 20 años como incentivo a la renovación vehicular, e implementación de truck centers cerca de zonas portuarias.",
    "Implementación del Plan de Chatarreo para camiones de más de 20 años como incentivo a la renovación vehicular",
    f"{S51} — Medidas Propuestas", 239, 239,
))

nuevas.append(mk(
    "r-transporte-014", "transporte", "meta", "ALTA",
    "Meta de transporte limpio: incorporar 10,000 buses eléctricos en cinco años (5,000 para Lima y 5,000 para las ocho ciudades más grandes) mediante política de subsidios.",
    "Implementaremos una política de subsidios para incorporar 10,000 buses eléctricos en cinco años (5,000 para Lima y 5,000 para las ocho ciudades más grandes)",
    f"{S51} — Medidas Propuestas", 239, 239,
    meta="10,000 buses eléctricos en 5 años",
))

nuevas.append(mk(
    "r-transporte-015", "transporte", "meta", "ALTA",
    "Chatarrear (compra o bono) 10,000 camiones de más de 20 años y 15,000 buses de más de 15 años a nivel nacional.",
    "Chatarrearemos (a través de compra o bono) 10,000 camiones de más de 20 años y 15.000 buses de más de 15 años a nivel nacional",
    f"{S51} — Medidas Propuestas", 239, 239,
    meta="Chatarreo: 10,000 camiones + 15,000 buses",
))

nuevas.append(mk(
    "r-transporte-016", "transporte", "meta", "ALTA",
    "Subsidio progresivo al transporte urbano: 50% de descuento en la segunda conexión y viaje gratis en la tercera si el recorrido no excede 90 minutos. Subsidios crecientes: S/ 800M (2027) a S/ 3,000M (2030).",
    "Aplicaremos un subsidio progresivo: 50 % de descuento en la segunda conexión y viaje gratis en la tercera, siempre que el recorrido no exceda 90 minutos",
    f"{S51} — Medidas Propuestas", 239, 239,
    meta="Subsidio transporte: S/ 800M (2027) → S/ 3,000M (2030)",
))

nuevas.append(mk(
    "r-transporte-017", "transporte", "meta", "ALTA",
    "Implementar 500 km de carriles exclusivos o preferentes para transporte público al 2030, priorizando la justicia espacial (el transporte público moviliza al 70% de usuarios de viajes motorizados).",
    "Implementaremos 500 km de carriles exclusivos o preferentes para transporte público al 2030",
    f"{S51} — Medidas Propuestas", 239, 239,
    meta="500 km carriles exclusivos transporte público al 2030",
))

nuevas.append(mk(
    "r-transporte-018", "transporte", "propuesta", "MEDIA",
    "Cofinanciamiento 75% en inversión en ciclovías a gobiernos provinciales que implementen ciclovías según planes maestros (PMUS).",
    "Se brindará un cofinanciamiento de 75% en la inversión en ciclovías a los gobiernos provinciales que implementen las ciclovías según sus planes maestros",
    f"{S51} — Medidas Propuestas", 239, 239,
))

nuevas.append(mk(
    "r-transporte-019", "transporte", "propuesta", "MEDIA",
    "Crear Autoridades de Transporte en todas las provincias con suficiente autonomía administrativa y capacidad de fiscalización.",
    "Se promoverán la creación de Autoridades de Transporte en todas las provincias con un Modelo con suficiente autonomía administrativa y capacidad de fiscalización",
    f"{S51} — Medidas Propuestas", 241, 241,
))

nuevas.append(mk(
    "r-transporte-020", "transporte", "propuesta", "BAJA",
    "Optimizar el esquema de subsidios aéreos amazónicos para ampliar frecuencias y capacidad; implementar Servicio de Información de Vuelo (AFIS) en aeródromos estratégicos (Puerto Esperanza, Rodríguez de Mendoza, etc.).",
    "Optimizar el diseño del esquema de subsidios aéreos para ampliar frecuencias, capacidad de flota y número de asientos en las rutas aéreas amazónicas",
    f"{S51} — Medidas Propuestas", 241, 241,
))

# =====================================================================
# 5.2 TELECOMUNICACIONES (líneas 241-249) — tema: transporte
# (consistente con Keiko §2.6 'Transportes y Comunicaciones')
# =====================================================================
S52 = "Dimensión Infraestructura — 5.2 Telecomunicaciones"

nuevas.append(mk(
    "r-transporte-021", "transporte", "principio", "ALTA",
    "Principio rector: las telecomunicaciones y el acceso a internet constituyen un servicio público esencial e infraestructura crítica; el Estado asumirá un rol rector, regulador y operador con cobertura universal y soberanía digital.",
    "Las telecomunicaciones y el acceso a internet constituyen un servicio público esencial e infraestructura crítica, vinculados a la soberanía digital, la seguridad nacional",
    f"{S52} — Situación Actual", 243, 243,
))

nuevas.append(mk(
    "r-transporte-022", "transporte", "meta", "ALTA",
    "Meta de conectividad: incrementar de 58.4% a 85% el número de hogares peruanos con internet; elevar hogares rurales con internet hasta 80%.",
    "incrementaremos de 58.4% a 85% el número de hogares peruanos a través de proyectos formulados por PRONATEL o por proyectos combinados de vías rurales e internet. Elevaremos el porcentaje de hogares rurales con internet hasta un 80%",
    f"{S52} — Medidas Propuestas", 247, 247,
    meta="Hogares con internet 58.4%→85%; rurales 61%→80%",
))

nuevas.append(mk(
    "r-transporte-023", "transporte", "propuesta", "MEDIA",
    "Asegurar provisión de energía e internet en todos los colegios para asegurar la transformación digital de la educación pública peruana en todo el país.",
    "Aseguraremos, provisión de energía e internet en todos los colegios para asegurar la transformación digital de la educación pública peruana",
    f"{S52} — Medidas Propuestas", 247, 247,
))

nuevas.append(mk(
    "r-transporte-024", "transporte", "propuesta", "MEDIA",
    "Plan Nacional de Cableado Subterráneo, eliminando progresivamente el cableado aéreo desordenado y coordinando con gobiernos regionales y locales para ordenamiento urbano.",
    "Implementaremos un Plan Nacional de Cableado Subterráneo, eliminando progresivamente el cableado aéreo desordenado",
    f"{S52} — Medidas Propuestas", 247, 247,
))

nuevas.append(mk(
    "r-transporte-025", "transporte", "propuesta", "ALTA",
    "Declarar las telecomunicaciones como infraestructura crítica del Estado, sujeta a control público, supervisión permanente y criterios de seguridad nacional y soberanía digital.",
    "Declararemos las telecomunicaciones como infraestructura crítica del Estado, sujeta a control público, supervisión permanente y criterios de seguridad nacional y soberanía digital",
    f"{S52} — Medidas Propuestas", 247, 247,
))

nuevas.append(mk(
    "r-transporte-026", "transporte", "propuesta", "MEDIA",
    "Disponer que áreas estratégicas de operación y control de redes (incluidos NOCs) se desarrollen obligatoriamente en territorio nacional por razones de soberanía tecnológica.",
    "Dispondremos que las áreas estratégicas de operación y control de redes, incluidos los Centros de Operaciones de Red (NOC), se desarrollen obligatoriamente en territorio nacional",
    f"{S52} — Medidas Propuestas", 247, 247,
))

nuevas.append(mk(
    "r-transporte-027", "transporte", "propuesta", "MEDIA",
    "Fortalecer OSIPTEL con autonomía técnica, recursos suficientes y capacidades efectivas de fiscalización, estableciendo sanciones reales y proporcionales por incumplimientos de calidad del servicio.",
    "Fortalecer a OSIPTEL con autonomía técnica, recursos suficientes y capacidades efectivas de fiscalización, estableciendo sanciones reales y proporcionales por incumplimientos",
    f"{S52} — Medidas Propuestas", 247, 247,
))

nuevas.append(mk(
    "r-transporte-028", "transporte", "propuesta", "MEDIA",
    "Reactivar y fortalecer el INICTEL como eje de investigación, capacitación y desarrollo tecnológico nacional en telecomunicaciones, redes, fibra óptica, datos y ciberseguridad.",
    "Reactivaremos y fortaleceremos el INICTEL como eje de investigación, capacitación y desarrollo tecnológico nacional en telecomunicaciones",
    f"{S52} — Medidas Propuestas", 247, 247,
))

nuevas.append(mk(
    "r-transporte-029", "transporte", "propuesta", "ALTA",
    "Implementar un Plan Nacional de Despliegue 5G con enfoque soberano, priorizando cobertura territorial, uso social del espectro y preparación estratégica para tecnologías futuras como 6G.",
    "Implementaremos un Plan Nacional de Despliegue 5G con enfoque soberano, priorizando la cobertura territorial, el uso social del espectro y la preparación estratégica para tecnologías futuras como 6G",
    f"{S52} — Medidas Propuestas", 247, 247,
))

nuevas.append(mk(
    "r-transporte-030", "transporte", "propuesta", "MEDIA",
    "Plan Nacional de Ciberseguridad en Telecomunicaciones, garantizando protección de datos personales y defensa de las redes frente a ciberataques.",
    "Implementaremos un Plan Nacional de Ciberseguridad en Telecomunicaciones, garantizando la protección de datos personales, la defensa de las redes frente a ciberataques",
    f"{S52} — Medidas Propuestas", 249, 249,
))

# =====================================================================
# 5.3 ENERGÍA (líneas 249-256) — tema: energia
# =====================================================================
S53 = "Dimensión Infraestructura — 5.3 Energía"

nuevas.append(mk(
    "r-energia-001", "energia", "diagnostico", "ALTA",
    "Diagnóstico de PETROPERU: el país consume más de 300 mil barriles diarios de combustibles; capacidad de refinación 125,800 bpd. PETROPERU pasó de abastecer 95% del mercado (años 80) a solo 20% hoy, producto de privatizaciones.",
    "El país consume más de 300 mil barriles diarios de combustibles, mientras que la capacidad instalada de Refinación de Petroperú es de 125,800 bpd",
    f"{S53} — Situación Actual", 249, 249,
    meta="Consumo 300k bpd; refinación PETROPERU 125,800 bpd; cuota mercado 20%",
))

nuevas.append(mk(
    "r-energia-002", "energia", "diagnostico", "ALTA",
    "Diagnóstico del gas: existe un solo gasoducto (Camisea-Pisco-Lima); el resto del país se abastece con GNL en camiones cisterna a precios al menos el doble que en Lima, fortaleciendo el centralismo.",
    "Si en el Perú no queremos seguir teniendo injustas diferencias en el precio del gas en las diferentes ciudades del país, entonces se debería terminar de construir el Gasoducto del Sur",
    f"{S53} — Situación Actual", 249, 249,
))

nuevas.append(mk(
    "r-energia-003", "energia", "diagnostico", "MEDIA",
    "Diagnóstico de consumo doméstico de gas: el consumo doméstico representa menos del 5% del consumo total del gas de Camisea; más del 80% de conexiones residenciales se concentra en Lima y Callao.",
    "Más del 80% de conexiones residenciales se concentra en Lima y Callao. El consumo doméstico representa menos del 5% del consumo total del gas de Camisea",
    f"{S53} — Situación Actual", 251, 251,
))

nuevas.append(mk(
    "r-energia-004", "energia", "diagnostico", "MEDIA",
    "Diagnóstico de cobertura: el Perú ha cubierto el 94% de hogares con electricidad, pero persisten brechas rurales del 16.7%, afectando principalmente a la Amazonía y zonas altoandinas; cobertura de gas doméstico solo 17% (2025).",
    "el Perú ha logrado avances importantes en electrificación cubriendo el 94% de los hogares, aún persisten brechas significativas",
    f"{S53} — Situación Actual", 251, 251,
    meta="Electrificación 94%; brecha rural 16.7%; gas doméstico 17%",
))

nuevas.append(mk(
    "r-energia-005", "energia", "meta", "ALTA",
    "Meta de PETROPERU: recuperar progresivamente su participación comercial en segmentos estratégicos hasta recuperar entre 40% y 45% del mercado nacional de combustibles, bajo criterios de gobierno corporativo eficiente.",
    "Recuperar progresivamente su participación comercial en segmentos estratégicos como diésel, gasolinas y abastecimiento regional, hasta recuperar entre 40% y 45% del mercado nacional de combustibles",
    f"{S53} — Medidas Propuestas", 251, 251,
    meta="PETROPERU: 40-45% del mercado nacional de combustibles",
))

nuevas.append(mk(
    "r-energia-006", "energia", "propuesta", "ALTA",
    "Recuperar el control para definir los destinos de consumo del gas: asegurar abastecimiento del mercado nacional, masificación del consumo y transformación industrial del gas con la planta petroquímica del Sur.",
    "Recuperar el control para definir los destinos de consumo del gas para asegurar el abastecimiento del mercado nacional, la masificación del consumo",
    f"{S53} — Medidas Propuestas", 251, 251,
))

nuevas.append(mk(
    "r-energia-007", "energia", "propuesta", "ALTA",
    "Renegociación estratégica de los contratos de Camisea para garantizar seguridad energética, reposición de reservas con compromisos de exploración, masificación nacional e industrialización.",
    "Renegociación estratégica de los contratos de Camisea. El objetivo general es garantizar la seguridad energética, la reposición de reservas con compromisos de exploración",
    f"{S53} — Medidas Propuestas", 253, 253,
))

nuevas.append(mk(
    "r-energia-008", "energia", "propuesta", "ALTA",
    "Nueva Política Nacional de Exploración Gasífera con un Plan agresivo 2026-2035 priorizando las Cuencas Madre de Dios, Ucayali, Noroeste y Offshore.",
    "Nueva Política Nacional de Exploración Gasífera. La exploración privada ha sido insuficiente durante los últimos 30 años",
    f"{S53} — Medidas Propuestas", 253, 253,
))

nuevas.append(mk(
    "r-energia-009", "energia", "propuesta", "ALTA",
    "Impulso al proyecto SITGAS (Sistema Integrado de Transporte de Gas Zona Sur) como principal obra energética de integración territorial y desarrollo industrial del sur peruano.",
    "Impulso a la ejecución del proyecto SITGAS como proyecto estratégico. El SITGAS debe convertirse en la principal obra energética de integración territorial",
    f"{S53} — Medidas Propuestas", 253, 253,
))

nuevas.append(mk(
    "r-energia-010", "energia", "propuesta", "ALTA",
    "Promover el establecimiento de un polo petroquímico en el sur ligado a SITGAS, dando prioridad a la producción de urea y fertilizantes para abastecer el mercado interno.",
    "Promover el establecimiento de un polo petroquímico en el sur. Esta propuesta está íntimamente ligada al desarrollo del proyecto SITGAS",
    f"{S53} — Medidas Propuestas", 253, 253,
))

nuevas.append(mk(
    "r-energia-011", "energia", "propuesta", "ALTA",
    "Acelerar la masificación residencial del gas natural como política social universal (similar a electrificación nacional), financiada con FISE, canon gasífero y subsidios focalizados; tarifas diferenciadas para hogares pobres.",
    "Acelerar la masificación residencial del gas natural. La masificación debe convertirse en política social universal, similar a la electrificación nacional",
    f"{S53} — Medidas Propuestas", 253, 253,
))

nuevas.append(mk(
    "r-energia-012", "energia", "propuesta", "MEDIA",
    "Reforma del mercado eléctrico: revisar el esquema tarifario eléctrico vinculando las tarifas al costo real del gas regulado, dado que las generadoras compran gas barato del Lote 88.",
    "Reforma del mercado eléctrico y uso del gas barato. Las generadoras eléctricas compran gas barato del lote 88, sin embargo, las tarifas de electricidad no lo reflejan",
    f"{S53} — Medidas Propuestas", 253, 253,
))

nuevas.append(mk(
    "r-energia-013", "energia", "propuesta", "ALTA",
    "Recuperar el proyecto del Gasoducto del Sur Peruano desde Camisea hasta Ilo-Mollendo, pasando por Cusco y Arequipa; MINEM y PROINVERSIÓN elaborarán nuevas bases para concurso internacional.",
    "Recuperar el proyecto del Gasoducto del Sur peruano desde Camisea hasta Ilo-Mollendo, pasando por Cusco y Arequipa",
    f"{S53} — Medidas Propuestas", 253, 253,
))

nuevas.append(mk(
    "r-energia-014", "energia", "meta", "ALTA",
    "Incrementar el presupuesto del MINEM para electrificación rural de S/ 489 millones (2025) a un promedio anual de S/ 1,100 millones (2026-2030); más de 100 proyectos adicionales por año.",
    "Incrementaremos el presupuesto del Ministerio de Energía y Minas para electrificación rural, de S/ 489 millones en el año 2025 a un promedio anual de S/ 1100 millones entre los años 2026 y 2030",
    f"{S53} — Medidas Propuestas", 255, 255,
    meta="Electrificación rural: S/ 489M → S/ 1,100M anuales",
))

nuevas.append(mk(
    "r-energia-015", "energia", "propuesta", "MEDIA",
    "Programa Nacional de Energía Rural y Amazónica priorizando soluciones descentralizadas (solar, eólica, microhidro, biomasa) con participación comunitaria.",
    "Implementar un Programa Nacional de Energía Rural y Amazónica, priorizando soluciones descentralizadas (solar, eólica, microhidro, biomasa)",
    f"{S53} — Medidas Propuestas", 255, 255,
))

nuevas.append(mk(
    "r-energia-016", "energia", "propuesta", "MEDIA",
    "Impulsar la transición energética aumentando progresivamente la participación de energías renovables no convencionales; desarrollar la industria del hidrógeno verde y expandir solar y eólica.",
    "Impulsar la transición energética, que debe ser definida como: Una Guía y no una Regla de acuerdo a nuestras características",
    f"{S53} — Medidas Propuestas", 255, 255,
))

nuevas.append(mk(
    "r-energia-017", "energia", "propuesta", "MEDIA",
    "Programa de expansión de energía hidráulica y diversificación renovable (solar, viento, hidrógeno verde, olas del mar); actualmente hidroelectricidad cubre ~50% del sistema.",
    "Programa de expansión de la energía hidráulica y diversificación de energías renovables (solar, de viento, hidrógeno verde, y de las olas del mar)",
    f"{S53} — Medidas Propuestas", 255, 255,
))

nuevas.append(mk(
    "r-energia-018", "energia", "propuesta", "BAJA",
    "Fortalecer el programa BONOGAS para ampliar el acceso de gas doméstico a las familias, principalmente en regiones.",
    "Fortalecer el programa BONOGAS para ampliar el acceso de gas doméstico de las familias, principalmente en regiones",
    f"{S53} — Medidas Propuestas", 255, 255,
))

# =====================================================================
# 5.4 AGRICULTURA (líneas 257-268) — tema: agricultura
# =====================================================================
S54 = "Dimensión Infraestructura — 5.4 Agricultura"

nuevas.append(mk(
    "r-agricultura-001", "agricultura", "diagnostico", "ALTA",
    "Diagnóstico estructural: el sector agrario peruano sufre una profunda injusticia social y territorial; la única política sostenida ha favorecido a la gran agroexportación con tierra y agua barata, regímenes tributarios y laborales de privilegio.",
    "Actualmente, el sector agrario peruano se caracteriza por una profunda injusticia social y territorial",
    f"{S54} — Situación Actual", 257, 257,
))

nuevas.append(mk(
    "r-agricultura-002", "agricultura", "diagnostico", "ALTA",
    "Diagnóstico de concentración: el modelo agroexportador concentra la riqueza en menos del 5% de productores (con S/ 20,000M en exoneraciones a 10 años); más de 2 millones de Unidades Productivas familiares producen el 60% de la alimentación de las ciudades.",
    "Mientras el modelo agroexportador concentra la riqueza en menos del 5% de productores (con S/ 20,000 millones en exoneraciones para los próximo 10 años)",
    f"{S54} — Situación Actual", 257, 257,
))

nuevas.append(mk(
    "r-agricultura-003", "agricultura", "diagnostico", "ALTA",
    "Diagnóstico de anemia y desnutrición: a inicios de 2026 la anemia afecta a más del 43% de los niños menores de tres años; alta prevalencia en Puno (53.1%) y Loreto.",
    "A inicios de 2026, la anemia afecta a más del 43 % de los niños menores de tres años (de 6 a 35 meses), con alta prevalencia en regiones como Puno (53.1 %) y Loreto",
    f"{S54} — Situación Actual", 259, 259,
    meta="Anemia infantil: 43% (Puno 53.1%)",
))

nuevas.append(mk(
    "r-agricultura-004", "agricultura", "diagnostico", "ALTA",
    "Diagnóstico de dependencia alimentaria: aceites 58%, cereales 43%, trigo 87%, maíz amarillo duro 60%, azúcar 34%, leche 13%; el país hasta importa papas congeladas.",
    "La dependencia alimentaria se ha incrementado en aceites (58%) y cereales (43%), trigo 87%, el 60% de maíz amarillo duro, el 34% de azúcar y el 13% de leche",
    f"{S54} — Situación Actual", 259, 259,
))

nuevas.append(mk(
    "r-agricultura-005", "agricultura", "meta", "ALTA",
    "Meta de soberanía alimentaria: que la canasta de consumo de las familias se abastezca en más del 90% con la producción agropecuaria nacional en todas las regiones.",
    "Nuestra meta es que la canasta de consumo de las familias se abastezca en más del 90% con la producción agropecuaria nacional en todas las regiones",
    f"{S54} — Situación Actual", 259, 259,
    meta=">90% canasta familiar de producción nacional",
))

nuevas.append(mk(
    "r-agricultura-006", "agricultura", "meta", "ALTA",
    "Transformar el MIDAGRI: en cinco años duplicaremos el presupuesto de la función agraria a S/ 14,000 millones; reestructurar 200 Agencias Agrarias Territoriales con 100% cobertura de extensión tecnológica.",
    "En cinco años duplicaremos el presupuesto de toda la función agraria (MIDAGRI, gobiernos regionales y locales) a S/ 14,000 millones, reestructurando 200 Agencias Agrarias Territoriales",
    f"{S54} — Medidas Propuestas", 263, 263,
    meta="Función agraria: S/ 14,000M (duplicar); 200 Agencias Agrarias",
))

nuevas.append(mk(
    "r-agricultura-007", "agricultura", "propuesta", "ALTA",
    "Eliminar la concentración de derechos de uso de agua y promover justa redistribución; prioridad para consumo humano y pequeña agricultura para garantizar seguridad alimentaria.",
    "Eliminaremos la concentración de los derechos del uso de agua y promoveremos la justa redistribución de los derechos del agua. Nuestra prioridad será el consumo humano y la pequeña agricultura",
    f"{S54} — Medidas Propuestas", 263, 263,
))

nuevas.append(mk(
    "r-agricultura-008", "agricultura", "propuesta", "MEDIA",
    "Instalar Consejos de Recursos Hídricos de Cuenca (CRHC) para fortalecer la gobernanza multiactor con participación de todos los niveles de gobierno y sociedad civil.",
    "Instalar Consejos de Recursos Hídricos de Cuenca (CRHC): Fortalecer la gobernanza multiactor con participación de todos los niveles de gobierno y sociedad civil",
    f"{S54} — Medidas Propuestas", 263, 263,
))

nuevas.append(mk(
    "r-agricultura-009", "agricultura", "propuesta", "ALTA",
    "Impulsar un Nuevo Banco Agrario reestructurando Agrobanco; AgroPatria garantizará crédito barato y asistencia técnica especializada para al menos 1 millón de agricultores familiares, comuneros y pequeña agricultura.",
    "Impulsaremos el Nuevo Banco Agrario, para ello reestructuraremos Agrobanco dotándolo de todas las funciones y capacidades de un banco moderno",
    f"{S54} — Medidas Propuestas", 263, 263,
))

nuevas.append(mk(
    "r-agricultura-010", "agricultura", "propuesta", "MEDIA",
    "Programa especial de fortalecimiento de la agricultura familiar con incentivos tributarios, compensaciones y línea de crédito especial en Agrobanco.",
    "Programa especial de fortalecimiento de la agricultura familiar, con incentivos tributarios y compensaciones. Creación de una línea de crédito especial en Agrobanco para la agricultura familiar",
    f"{S54} — Medidas Propuestas", 265, 265,
))

nuevas.append(mk(
    "r-agricultura-011", "agricultura", "propuesta", "MEDIA",
    "Programa especial de recuperación de agricultura milenaria basada en andenería, lagunas altoandinas, amunas; cultivos y crianzas ancestrales (cereales y tubérculos andinos, llamas, alpacas, vicuñas, huanaco).",
    "Programa especial de recuperación de la agricultura milenaria basada en el manejo de andenería, lagunas altoandinas, amunas, orientado a la recuperación de cultivos y crianzas ancestrales",
    f"{S54} — Medidas Propuestas", 265, 265,
))

nuevas.append(mk(
    "r-agricultura-012", "agricultura", "meta", "ALTA",
    "Meta hídrica: incrementar 300,000 ha de riego tecnificado para agricultura familiar; implementar riego tecnificado en 100,000 ha adicionales; recuperar al menos 120,000 ha con tecnologías ancestrales; masificar 20 megaproyectos hídricos.",
    "Incrementaremos en 300,000 ha el riego tecnificado para agricultura familiar, e implementaremos riego tecnificado en 100,000 ha adicionales, recuperaremos al menos 120,000 ha. revalorando tecnologías y sistemas ancestrales",
    f"{S54} — Medidas Propuestas", 265, 265,
    meta="Riego tecnificado: +300k ha familiar + 100k ha adicionales + 120k ha ancestrales; 20 megaproyectos hídricos",
))

nuevas.append(mk(
    "r-agricultura-013", "agricultura", "meta", "MEDIA",
    "Presupuesto de gestión hídrica subirá a S/ 400 millones anuales para masificar proyectos de siembra y cosecha de agua, microrrepresas y gestión de recursos naturales.",
    "El presupuesto de gestión hídrica subirá a S/ 400 millones anuales",
    f"{S54} — Medidas Propuestas", 265, 265,
    meta="Gestión hídrica: S/ 400M anuales",
))

nuevas.append(mk(
    "r-agricultura-014", "agricultura", "propuesta", "ALTA",
    "Programa especial de fomento a la elaboración de conservas de anchoveta destinadas a la alimentación popular para reducir desnutrición y anemia en zonas de pobreza.",
    "Programa especial de fomento a la elaboración de conservas de anchoveta destinadas a la alimentación popular, para reducir la desnutrición y la anemia",
    f"{S54} — Medidas Propuestas", 265, 265,
))

nuevas.append(mk(
    "r-agricultura-015", "agricultura", "propuesta", "ALTA",
    "Apoyo decidido al cambio de matriz productiva: agroecología, protección y promoción de mega-biodiversidad y calidad de semillas; conservación in situ de ecosistemas y agrobiodiversidad con bancos de germoplasma en el INIA.",
    "Apoyo decidido al cambio de matriz productiva, promoviendo la agroecología, la protección y promoción de nuestra mega-biodiversidad y la calidad de semillas",
    f"{S54} — Medidas Propuestas", 265, 265,
))

nuevas.append(mk(
    "r-agricultura-016", "agricultura", "meta", "ALTA",
    "Asociatividad democrática: fortalecer 2,000 organizaciones gremiales con democracia transparente y paridad de género (50% mujeres en dirigencias); Programa 'Ayni Productivo'.",
    "Asociatividad Democrática y Gobernanza Comunitaria. Fomentaremos la asociatividad fortaleciendo 2,000 organizaciones gremiales con democracia transparente y paridad de género (50% mujeres en dirigencias)",
    f"{S54} — Medidas Propuestas", 265, 265,
    meta="2,000 organizaciones gremiales fortalecidas; 50% mujeres en dirigencias",
))

nuevas.append(mk(
    "r-agricultura-017", "agricultura", "propuesta", "ALTA",
    "Soberanía alimentaria con compras públicas: promulgar Ley de Soberanía Alimentaria que obligue al Estado a comprar 40% de alimentos para Wasi Mikuna, hospitales y cárceles directamente de agricultura campesino-comunera y familiar.",
    "implementaremos un programa de compras públicas de alimentos de la agricultura familiar y comunera promulgando la Ley de Soberanía Alimentaria que obligue al Estado a comprar el 40% de alimentos",
    f"{S54} — Medidas Propuestas", 267, 267,
    meta="40% compras públicas alimentos de agricultura familiar/comunera",
))

nuevas.append(mk(
    "r-agricultura-018", "agricultura", "meta", "ALTA",
    "Diversificación productiva rural: industrialización con 500 Centros de Acopio y Transformación Modular (público-comunitarios) y Biofábricas Industriales de fertilizantes orgánicos; sello 'Saludable Peruana' (CS-P).",
    "Diversificación productiva rural: Impulsaremos la industrialización y transformación de la producción agropecuaria para darle mayor valor agregado y conquistar nuevos y mejores mercados con 500 Centros de Acopio y Transformación Modular",
    f"{S54} — Medidas Propuestas", 267, 267,
    meta="500 Centros de Acopio y Transformación Modular",
))

nuevas.append(mk(
    "r-agricultura-019", "agricultura", "propuesta", "ALTA",
    "Protección integral de la tierra y los territorios: titulación de comunidades campesinas y nativas; reconocimiento constitucional de Rondas Campesinas y Guardias Indígenas como defensoras del territorio.",
    "Protección Integral de la Tierra y los Territorios. Titulación de las comunidades campesinas y nativas y reconocimiento de pueblos indígenas originarios. Reconocimiento constitucional de Rondas Campesinas",
    f"{S54} — Medidas Propuestas", 267, 267,
))

nuevas.append(mk(
    "r-agricultura-020", "agricultura", "propuesta", "MEDIA",
    "Modernizar la sanidad agraria garantizando inocuidad, trazabilidad y certificaciones para el acceso a mercados nacionales e internacionales.",
    "Modernizar la sanidad agraria",
    f"{S54} — Medidas Propuestas", 267, 267,
))

# =====================================================================
# 5.5 TURISMO (líneas 269-271) — tema: turismo
# =====================================================================
S55 = "Dimensión Infraestructura — 5.5 Turismo"

nuevas.append(mk(
    "r-turismo-001", "turismo", "diagnostico", "MEDIA",
    "Diagnóstico de aporte: el turismo representa el 4% del PBI nacional y 8% de la PEA; población laboral directa e indirecta de ~3 millones; tercer generador de divisas.",
    "Representa el 4% del PBI nacional y el 8% de la PEA. Además, es una actividad intensiva en empleo que cuenta con una población laboral directa e indirecta de alrededor de 3 millones de personas",
    f"{S55} — Situación Actual", 269, 269,
    meta="Turismo: 4% PBI; 8% PEA; ~3M empleos",
))

nuevas.append(mk(
    "r-turismo-002", "turismo", "diagnostico", "MEDIA",
    "Diagnóstico de captación: el Perú solo capta el 0.3% de los 1,500 millones de turistas que viajan por el mundo cada año; la pandemia provocó una caída de 73%, la más alta de Sudamérica.",
    "Solo captamos el 0.3% de los mil quinientos millones de turistas que viajan por el mundo cada año",
    f"{S55} — Situación Actual", 269, 269,
))

nuevas.append(mk(
    "r-turismo-003", "turismo", "diagnostico", "MEDIA",
    "Diagnóstico de concentración: el potencial turístico está concentrado en 90% entre Lima y Cusco, con infraestructura deficiente en regiones de alto atractivo (Apurímac, Ayacucho, Puno, Amazonas, Loreto).",
    "el potencial turístico del Perú es enorme en atractivos naturales y arqueológicos en todas las regiones del Perú; sin embargo, se halla concentrado en un 90% entre Lima y Cusco",
    f"{S55} — Situación Actual", 269, 269,
))

nuevas.append(mk(
    "r-turismo-004", "turismo", "diagnostico", "MEDIA",
    "Diagnóstico de las ANP: las Áreas Naturales Protegidas generan más de USD 2,885 millones anuales y sostienen el 80% del turismo receptivo, pero solo reciben USD 39 millones para su gestión.",
    "Las Áreas Naturales Protegidas (ANP) generan más de USD 2,885 millones anuales y sostienen el 80% del turismo receptivo, pero solo reciben USD 39 millones para su gestión",
    f"{S55} — Situación Actual", 269, 269,
    meta="ANP: USD 2,885M ingresos; USD 39M presupuesto",
))

nuevas.append(mk(
    "r-turismo-005", "turismo", "propuesta", "ALTA",
    "Reordenar la gobernanza turística regional ajustando competencias del sector ambiental, SERNANP, Ministerio de Cultura y MINCETUR, reforzando el rol de los GORE en planeación e inversión turística.",
    "Reordenar la gobernanza turística en las regiones reajustando y coordinando las competencias del sector ambiental, el SERNANP, Ministerio de Cultura y el MINCETUR",
    f"{S55} — Medidas Propuestas", 269, 269,
))

nuevas.append(mk(
    "r-turismo-006", "turismo", "meta", "ALTA",
    "Incrementar el presupuesto de gestión de ANP a USD 150 millones anuales y desarrollar infraestructura turística sostenible en corredores ecoturísticos.",
    "Desarrollar infraestructura turística sostenible en ANP y corredores ecoturísticos creando condiciones habilitantes para atraer la inversión privada hacia el turismo sostenible. Incrementar el presupuesto de gestión de ANP a USD 150 millones anuales",
    f"{S55} — Medidas Propuestas", 269, 269,
    meta="Presupuesto ANP: USD 150M anuales",
))

nuevas.append(mk(
    "r-turismo-007", "turismo", "propuesta", "MEDIA",
    "Mediante ley destinar al menos el 30% del boleto turístico para constituir un fondo de restauración y mantenimiento de sitios arqueológicos y áreas destinadas al turismo.",
    "Mediante ley se destinará al menos el 30% del boleto turístico para constituir un fondo de restauración y mantenimiento de los sitios arqueológicos",
    f"{S55} — Medidas Propuestas", 269, 269,
    meta="30% boleto turístico → fondo de restauración",
))

nuevas.append(mk(
    "r-turismo-008", "turismo", "propuesta", "MEDIA",
    "Creación del Fondo Nacional de Museos, Bibliotecas y Patrimonio financiado mediante turismo cultural, obras por impuestos y cooperación internacional.",
    "Creación del Fondo Nacional de Museos, Bibliotecas y Patrimonio financiado mediante turismo cultural, obras por impuestos y cooperación internacional",
    f"{S55} — Medidas Propuestas", 269, 269,
))

nuevas.append(mk(
    "r-turismo-009", "turismo", "meta", "ALTA",
    "Meta de empleo turístico: incrementar en 300 mil trabajadores el sector y multiplicar los negocios turísticos y productivos vinculados en al menos 20% durante el periodo de gobierno.",
    "En el periodo de gobierno se espera incrementar en 300 mil trabajadores en este sector, y multiplicar los negocios turísticos y productivos vinculados en al menos un 20%",
    f"{S55} — Medidas Propuestas", 269, 269,
    meta="+300 mil trabajadores turismo; +20% negocios turísticos",
))

nuevas.append(mk(
    "r-turismo-010", "turismo", "propuesta", "MEDIA",
    "Proyectos integrales de turismo regional: Corredor del Colca (Arequipa), turismo de playa Tumbes-Piura, ecoturismo Loreto-Ucayali y Madre de Dios-Puno, Eje Moche (La Libertad-Lambayeque), Amazonas-San Martín; US$ 100M por eje.",
    "Se implementarán proyectos integrales de Turismo en Arequipa (Corredor del Colca), Tumbes-Piura (turismo de playa), Loreto-Ucayali (turismo de observación y ecoturismo en la Amazonía)",
    f"{S55} — Medidas Propuestas", 271, 271,
))

nuevas.append(mk(
    "r-turismo-011", "turismo", "propuesta", "MEDIA",
    "Reestructurar PromPerú con política acorde al PENTUR; mejorar el uso del impuesto extraordinario de US$ 15 en pasajes aéreos para orientarlo a promoción turística.",
    "Se reestructurará Promperú para el mejor cumplimiento de sus objetivos, a través de una política acorde con el PENTUR",
    f"{S55} — Medidas Propuestas", 271, 271,
))

# =====================================================================
# 5.6 PESCA (líneas 271-273) — tema: pesca
# =====================================================================
S56 = "Dimensión Infraestructura — 5.6 Pesca"

nuevas.append(mk(
    "r-pesca-001", "pesca", "diagnostico", "ALTA",
    "Diagnóstico de la pesca: aporta al PBI a través de extracción y acuicultura; genera al menos 300 mil empleos. Soporte de seguridad y soberanía alimentaria del país.",
    "genera al menos 300 mil puestos de trabajo, incluida las redes de comercialización de pescado y mariscos como de productos pesqueros",
    f"{S56} — Situación Actual", 271, 271,
    meta="Pesca: 300 mil empleos",
))

nuevas.append(mk(
    "r-pesca-002", "pesca", "diagnostico", "ALTA",
    "Diagnóstico de concentración: cinco empresas controlan el 80% de la anchoveta; exportan US$ 2,100 millones anuales en harina de pescado pero pagan al Estado menos del 1.5% del valor extraído.",
    "Cinco empresas controlan el 80% de la anchoveta. Exportan US$ 2,100 millones anuales en harina de pescado, pero pagan al Estado menos del 1.5% del valor extraído",
    f"{S56} — Situación Actual", 271, 271,
    meta="5 empresas controlan 80% anchoveta; pago Estado <1.5%",
))

nuevas.append(mk(
    "r-pesca-003", "pesca", "propuesta", "MEDIA",
    "Derogar el DS 024-2016-PRODUCE y normas complementarias para reformar el marco regulatorio pesquero.",
    "Derogar el DS 024-2016-PRODUCE y normas complementarias",
    f"{S56} — Medidas Propuestas", 273, 273,
))

nuevas.append(mk(
    "r-pesca-004", "pesca", "propuesta", "MEDIA",
    "Actualización tecnológica de balanzas en plantas de harina de pescado, con calibración y envío encriptado y autónomo de información a PRODUCE.",
    "Realizar una actualización tecnológica / operativa de las balanzas en las plantas de harina de pescado, su calibración y envío encriptada y autónoma de la información a PRODUCE",
    f"{S56} — Medidas Propuestas", 273, 273,
))

nuevas.append(mk(
    "r-pesca-005", "pesca", "propuesta", "MEDIA",
    "Aplicación de la Ley 31749 (reclasificación de flota artesanal, transparencia y participación); monitoreo satelital para la protección de recursos dentro de las 3 millas marinas.",
    "Aplicación de la ley 31749 en los aspectos normados de reclasificación de la flota artesanal, transparencia, reportes sobre la situación de los recursos",
    f"{S56} — Medidas Propuestas", 273, 273,
))

nuevas.append(mk(
    "r-pesca-006", "pesca", "propuesta", "ALTA",
    "Reimpulso al consumo humano de anchoveta eliminando distorsiones que la destinan a harina de pescado; innovación productiva y refuerzo de control.",
    "Reimpulso al consumo de anchoveta, eliminando las distorsiones actuales que la destinan a la harina de pescado",
    f"{S56} — Medidas Propuestas", 273, 273,
))

nuevas.append(mk(
    "r-pesca-007", "pesca", "propuesta", "MEDIA",
    "Fortalecer técnica y operacionalmente la pequeña acuicultura altoandina y amazónica reorientando los programas de innovación existentes.",
    "Fortalecer técnica y operacionalmente la pequeña acuicultura altoandina y amazónica",
    f"{S56} — Medidas Propuestas", 273, 273,
))

nuevas.append(mk(
    "r-pesca-008", "pesca", "propuesta", "ALTA",
    "Conformar una superintendencia de fiscalización pesquera para combatir construcción ilegal de lanchas y procedimientos laxos de formalización que han ampliado la flota legalizada por encima de la real.",
    "Conformación de una superintendencia de fiscalización pesquera",
    f"{S56} — Medidas Propuestas", 273, 273,
))

nuevas.append(mk(
    "r-pesca-009", "pesca", "propuesta", "MEDIA",
    "Asegurar la independencia técnica de IMARPE adecuándola a la Ley Orgánica del Poder Ejecutivo como institución técnica especializada.",
    "Asegurar independencia técnica de IMARPE. Adecuación a la ley orgánica del poder ejecutivo, como institución técnica especializada",
    f"{S56} — Medidas Propuestas", 273, 273,
))

nuevas.append(mk(
    "r-pesca-010", "pesca", "propuesta", "MEDIA",
    "Incremento de los derechos de pesca correspondientes a la anchoveta y otras especies capturadas por la flota industrial.",
    "Incremento de los derechos de pesca correspondientes a la anchoveta y otras especies capturadas por la flota industrial",
    f"{S56} — Medidas Propuestas", 273, 273,
))

# =====================================================================
# 5.7 VIVIENDA (líneas 273-277) — tema: vivienda
# =====================================================================
S57 = "Dimensión Infraestructura — 5.7 Vivienda"

nuevas.append(mk(
    "r-vivienda-001", "vivienda", "diagnostico", "ALTA",
    "Diagnóstico urbano: en las últimas dos décadas, el 93% del crecimiento urbano en el Perú ha sido informal; solo el 15% de los municipios cuenta con un Plan de Desarrollo Urbano (PDU).",
    "En las últimas dos décadas, el 93% del crecimiento urbano en el Perú ha sido informal. Solo el 15% de los municipios cuenta con un Plan de Desarrollo Urbano (PDU)",
    f"{S57} — Situación Actual", 273, 273,
    meta="93% crecimiento urbano informal; 15% municipios con PDU",
))

nuevas.append(mk(
    "r-vivienda-002", "vivienda", "diagnostico", "ALTA",
    "Diagnóstico de déficit habitacional: el déficit asciende a 1.86 millones de viviendas; se construyen 76,000 formales/año pero el déficit crece en 142,000 unidades anuales; 80% de viviendas informales no cumple condiciones mínimas.",
    "El déficit habitacional en el Perú asciende a 1.86 millones de viviendas. Cada año se construyen unas 76,000 viviendas formales, pero el déficit crece en 142,000 unidades anuales",
    f"{S57} — Situación Actual", 273, 273,
    meta="Déficit habitacional: 1.86M viviendas; crece +142k/año",
))

nuevas.append(mk(
    "r-vivienda-003", "vivienda", "diagnostico", "MEDIA",
    "Diagnóstico de informalidad predial: la informalidad predial urbana bordea el 45.8%; casi la mitad de familias no tiene título de propiedad, lo que les impide acceder a crédito y servicios formales.",
    "La informalidad predial urbana en el Perú bordea el 45.8%. Esto significa que casi la mitad de las familias no tiene título de propiedad",
    f"{S57} — Situación Actual", 275, 275,
    meta="Informalidad predial urbana: 45.8%",
))

nuevas.append(mk(
    "r-vivienda-004", "vivienda", "propuesta", "ALTA",
    "Titulación masiva de viviendas reduciendo papeleo, costos y formalidades innecesarias para superar la informalidad predial.",
    "Titulación masiva de viviendas, reduciendo el papeleo, los costos y formalidades innecesarias",
    f"{S57} — Medidas Propuestas", 275, 275,
))

nuevas.append(mk(
    "r-vivienda-005", "vivienda", "meta", "ALTA",
    "Programa Nacional de Vivienda Rural WASI UKHU: invertir S/ 2,500 millones en 50 mil viviendas nuevas y 100 mil mejoradas, articuladas a titulación, materiales locales, energía limpia, agua y saneamiento.",
    "Creación del Programa Nacional de Vivienda Rural WASI UKHU (hogar digno), que habilitará viviendas de bajo costo, adecuadas al estilo de la arquitectura y condiciones climáticas",
    f"{S57} — Medidas Propuestas", 275, 275,
    meta="WASI UKHU: S/ 2,500M; 50k viviendas nuevas + 100k mejoradas",
))

nuevas.append(mk(
    "r-vivienda-006", "vivienda", "propuesta", "MEDIA",
    "Diagnóstico masivo del riesgo estructural en barrios populares y centros poblados; bonos de reforzamiento estructural y ampliación segura con asistencia técnica obligatoria.",
    "Se realizará un diagnóstico masivo del riesgo estructural en barrios populares y centros poblados, para identificar viviendas vulnerables frente a sismos y otros peligros",
    f"{S57} — Medidas Propuestas", 275, 275,
))

nuevas.append(mk(
    "r-vivienda-007", "vivienda", "propuesta", "ALTA",
    "Reorganizar el Fondo MIVIVIENDA y TECHO PROPIO para cortar la intermediación costosa con grandes bancos y constructoras; dirigir recursos directamente a familias vía Bancas de Desarrollo y ampliar acceso a pequeñas/medianas constructoras.",
    "Reorganizaremos el Fondo MIVIVIENDA y TECHO PROPIO para cortar la intermediación costosa con grandes bancos y constructoras",
    f"{S57} — Medidas Propuestas", 275, 275,
))

nuevas.append(mk(
    "r-vivienda-008", "vivienda", "propuesta", "MEDIA",
    "Plan Nacional de Reubicación de poblaciones en riesgos sísmicos y de inundaciones no mitigables, con financiamiento flexible para compra, construcción o mejora de viviendas en zonas seguras.",
    "Plan Nacional de Reubicación de poblaciones en riesgos, que relocalice a las poblaciones que están en zonas de riesgos sísmico y de inundaciones no mitigables",
    f"{S57} — Medidas Propuestas", 275, 275,
))

nuevas.append(mk(
    "r-vivienda-009", "vivienda", "propuesta", "MEDIA",
    "Mejorar el confort térmico y dar vivienda rural digna en zonas de friaje extremo y heladas mediante el mecanismo de Obras por Impuestos.",
    "Mejorar el confort térmico y dar una vivienda rural digna en las zonas de friaje extremo y heladas mediante el mecanismo de Obras por Impuestos",
    f"{S57} — Medidas Propuestas", 277, 277,
))

nuevas.append(mk(
    "r-vivienda-010", "vivienda", "propuesta", "MEDIA",
    "Usar recursos del canon y sobrecanon para financiar bonos familiares habitacionales, priorizando zonas con alta demanda y baja oferta.",
    "Usar recursos del canon y sobrecanon para financiar bonos familiares habitacionales, priorizando zonas con alta demanda y baja oferta",
    f"{S57} — Medidas Propuestas", 277, 277,
))

nuevas.append(mk(
    "r-vivienda-011", "vivienda", "propuesta", "MEDIA",
    "Plan Nacional de Veredas y Accesibilidad que asegure veredas seguras, inclusivas y accesibles para niñas, niños, personas adultas mayores y personas con discapacidad.",
    "Desarrollar un Plan Nacional de Veredas y Accesibilidad, que asegure veredas seguras, inclusivas y accesibles para niñas, niños, personas adultas mayores y personas con discapacidad",
    f"{S57} — Medidas Propuestas", 275, 275,
))

nuevas.append(mk(
    "r-vivienda-012", "vivienda", "propuesta", "MEDIA",
    "Programa Nacional de Parques y Zonas Recreativas garantizando parques, áreas verdes y espacios recreativos en cada barrio urbano y rural; prioridad a barrios populares, asentamientos humanos y comunidades rurales.",
    "Implementar un Programa Nacional de Parques y Zonas Recreativas, garantizando que cada barrio urbano y rural cuente con parques, áreas verdes y espacios recreativos",
    f"{S57} — Medidas Propuestas", 275, 275,
))

# =====================================================================
# 5.8 AGUA Y SANEAMIENTO (líneas 277-282) — tema: agua
# =====================================================================
S58 = "Dimensión Infraestructura — 5.8 Agua y Saneamiento"

nuevas.append(mk(
    "r-agua-001", "agua", "diagnostico", "ALTA",
    "Diagnóstico de calidad del agua: según INEI (2024) solo el 40.4% de hogares accedió a agua con nivel adecuado de cloro (≥0.5 mg/L); un preocupante 39.9% accedió a agua sin cloro alguno.",
    "Según el INEI (2024), solo el 40,4 % de los hogares accedió a agua con el nivel adecuado de cloro (≥ 0,5 mg/L), mientras que un preocupante 39.9 % accedió a agua sin cloro alguno",
    f"{S58} — Situación Actual", 277, 277,
    meta="40.4% agua con cloro adecuado; 39.9% sin cloro (INEI 2024)",
))

nuevas.append(mk(
    "r-agua-002", "agua", "diagnostico", "ALTA",
    "Diagnóstico de continuidad: entre oct-2023 y sep-2024, solo el 59.5% contó con agua las 24 horas; el resto accedió por tramos parciales del día.",
    "Entre octubre 2023 y setiembre 2024, solo el 59,5 % contó con agua las 24 horas, mientras el resto accedió por tramos",
    f"{S58} — Situación Actual", 279, 279,
    meta="Continuidad 24h agua: 59.5%",
))

nuevas.append(mk(
    "r-agua-003", "agua", "diagnostico", "ALTA",
    "Diagnóstico de brecha de financiamiento: SUNASS (2025) estima en S/ 95,789 millones la brecha de financiamiento para lograr acceso universal al agua para el año 2030.",
    "De acuerdo con cálculos de SUNASS (2025), la brecha de financiamiento para lograr acceso universal para el año 2030, se estima en S/ 95,789 millones",
    f"{S58} — Situación Actual", 279, 279,
    meta="Brecha agua para acceso universal: S/ 95,789M",
))

nuevas.append(mk(
    "r-agua-004", "agua", "diagnostico", "MEDIA",
    "Diagnóstico climático: el cambio climático agrava la escasez y estrés hídrico; el 50% de la cobertura de glaciares ha desaparecido en los últimos 30 años; 46% del territorio nacional es muy vulnerable a desastres naturales asociados a El Niño.",
    "El 50% de la cobertura de glaciares en el Perú han desaparecido en los últimos 30 años",
    f"{S58} — Situación Actual", 279, 279,
    meta="Glaciares: -50% en 30 años; 46% territorio vulnerable a El Niño",
))

nuevas.append(mk(
    "r-agua-005", "agua", "propuesta", "ALTA",
    "Crear el Programa nacional 'El Agua es un derecho' para asegurar la calidad del agua, que sea barata y en lo posible administrada con participación directa de las comunidades de usuarios.",
    "Se creará, El Programa nacional “El Agua es un derecho”, con el fin de asegurar la calidad del agua, que sea barata y en lo posible administrada con participación directa de las comunidades de usuarios",
    f"{S58} — Medidas Propuestas", 279, 279,
))

nuevas.append(mk(
    "r-agua-006", "agua", "propuesta", "ALTA",
    "Apuntalar el programa de agua y saneamiento para todos bajo control público y comunitario, poniendo fin a la privatización de los servicios.",
    "Se apuntalará el programa de agua y saneamiento para todos bajo control público y comunitario, poniendo fin a la privatización de los servicios",
    f"{S58} — Medidas Propuestas", 279, 279,
))

nuevas.append(mk(
    "r-agua-007", "agua", "meta", "ALTA",
    "Acelerar el proyecto 'Obras de Cabecera' a cargo de Proinversión que añadirá 5 metros cúbicos de agua por segundo en Lima Metropolitana evitando el riesgo de desabastecimiento.",
    "Se acelerará la implementación del proyecto “Obras de Cabecera” a cargo de Proinversión que debe añadir 5 metros cúbicos de agua por segunda en Lima Metropolitana",
    f"{S58} — Medidas Propuestas", 279, 279,
    meta="Obras de Cabecera: +5 m³/s para Lima Metropolitana",
))

nuevas.append(mk(
    "r-agua-008", "agua", "propuesta", "MEDIA",
    "Impulsar asociaciones público-privadas para construcción, operación y mantenimiento de infraestructuras hídricas incluyendo recuperación de fuentes de agua y reducción del riesgo de desastres.",
    "Impulsar asociaciones público-privadas para la construcción, operación y mantenimiento de las infraestructuras hídricas que incluyen la recuperación de fuentes de agua",
    f"{S58} — Medidas Propuestas", 279, 279,
))

nuevas.append(mk(
    "r-agua-009", "agua", "propuesta", "MEDIA",
    "Modernizar las tecnologías en el uso del agua: redes de distribución, plantas de potabilización, sistemas de cloración, reducción de pérdidas y contaminación, facturación.",
    "Modernizar las tecnologías en el uso del agua: redes de distribución, plantas de potabilización, sistemas de cloración, reducción de pérdidas y contaminación",
    f"{S58} — Medidas Propuestas", 279, 279,
))

nuevas.append(mk(
    "r-agua-010", "agua", "propuesta", "MEDIA",
    "EPS cumplirán metas obligatorias de continuidad y calidad con incentivos por desempeño y sanciones por incumplimiento; laboratorios móviles y monitoreo comunitario para control del cloro y la calidad del agua.",
    "Las EPS cumplirán metas obligatorias de continuidad y calidad, con incentivos por desempeño y",
    f"{S58} — Medidas Propuestas", 279, 279,
))

nuevas.append(mk(
    "r-agua-011", "agua", "propuesta", "ALTA",
    "Sistemas de agua y saneamiento adaptados al contexto rural y amazónico: bombeo solar, captación de lluvia, baños ecológicos y pequeñas plantas compactas; fortalecimiento de la gestión comunitaria (JASS 2.0).",
    "Se impulsarán sistemas de agua y saneamiento adaptados al contexto rural y amazónico, como bombeo solar, captación de lluvia, baños ecológicos y pequeñas plantas compactas",
    f"{S58} — Medidas Propuestas", 281, 281,
))

nuevas.append(mk(
    "r-agua-012", "agua", "propuesta", "MEDIA",
    "Regulación estricta de camiones cisterna y puntos de abastecimiento con topes tarifarios para evitar abusos; tarifa social con subsidios cruzados transparentes para proteger a hogares vulnerables.",
    "Se implementará una regulación estricta de los camiones cisterna y puntos de abastecimiento, estableciendo topes tarifarios para evitar abusos",
    f"{S58} — Medidas Propuestas", 281, 281,
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
