# -*- coding: utf-8 -*-
"""Construye comparaciones plan_vs_plan en comparaciones.json.

Para cada tema común a ambos candidatos, se contrastan propuestas-ancla
por dimensión (diagnóstico, propuesta principal, meta, enfoque). Los temas
exclusivos de un candidato se registran como SOLO_A (Keiko) o SOLO_B (Roberto).
"""
import json
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

VAULT = Path(__file__).resolve().parent.parent.parent
RUTA = VAULT / "00-Sistema" / "datos" / "comparaciones.json"


def mk(id_, tema, dimension, pk, pr, relacion, analisis):
    return {
        "id": id_,
        "tema": tema,
        "dimension": dimension,
        "propuesta_keiko": pk,
        "propuesta_roberto": pr,
        "relacion": relacion,
        "analisis": analisis,
    }


# Numeración secuencial por tema
nuevas = []

# =====================================================================
# SEGURIDAD CIUDADANA
# =====================================================================
nuevas.append(mk(
    "cmp-pp-seguridad-001", "seguridad", "diagnostico",
    "k-seguridad-001", "r-seguridad-002", "COINCIDE",
    "Ambos diagnostican la inseguridad como problema crítico nacional. Keiko enfatiza victimización (27.1% urbana) y debilidad estatal; Roberto añade un pacto de impunidad entre criminalidad y política mafiosa fujimorista. Coinciden en la gravedad y la responsabilidad estatal, divergen en el reparto de culpas."
))
nuevas.append(mk(
    "cmp-pp-seguridad-002", "seguridad", "propuesta_principal",
    "k-seguridad-016", "r-seguridad-009", "DIVERGE",
    "Keiko ancla la solución en tecnología y comando (C5i, videovigilancia, plataformas en tiempo real). Roberto ancla en pacto político y comando unificado contra el crimen organizado con énfasis en la inteligencia y la articulación PNP-Fiscalía. Mismo objetivo, enfoques institucionales distintos."
))
nuevas.append(mk(
    "cmp-pp-seguridad-003", "seguridad", "meta",
    None, "r-seguridad-013", "SOLO_B",
    "Roberto fija meta cuantitativa clara (incremento de 20,000 efectivos PNP en 3 años y ratio 1 policía/220 habitantes según ONU). Keiko detalla múltiples medidas pero no compromete una meta numérica equivalente de pie de fuerza policial."
))
nuevas.append(mk(
    "cmp-pp-seguridad-004", "seguridad", "enfoque_institucional",
    "k-seguridad-017", "r-seguridad-006", "DIVERGE",
    "Keiko propone delegación de facultades legislativas por 60 días para acelerar medidas de emergencia. Roberto propone derogar leyes pro-crimen (31751, 31990, 32108 etc.) atribuidas al Congreso fujimorista. Ambos buscan reforma normativa pero por vías incompatibles."
))

# =====================================================================
# CORRUPCIÓN
# =====================================================================
nuevas.append(mk(
    "cmp-pp-corrupcion-001", "corrupcion", "diagnostico",
    "k-corrupcion-001", "r-corrupcion-001", "COINCIDE",
    "Ambos diagnostican la corrupción como mal estructural con costos masivos (Roberto cita S/ 24,268 millones perdidos en 2023, 'Segundo gran mal'). Convergen en que penetra todos los niveles del Estado, pero Roberto la liga al Congreso actual y Keiko la describe en términos más generales."
))
nuevas.append(mk(
    "cmp-pp-corrupcion-002", "corrupcion", "propuesta_principal",
    "k-corrupcion-005", "r-corrupcion-009", "DIVERGE",
    "Keiko prioriza fortalecer la Procuraduría General y blindarla; Roberto crea un Sistema Nacional de Integridad y Transparencia (SNIT) según recomendación OCDE. Ambos refuerzan institucionalidad pero con arquitecturas distintas."
))
nuevas.append(mk(
    "cmp-pp-corrupcion-003", "corrupcion", "enfoque_institucional",
    "k-corrupcion-006", "r-corrupcion-004", "DIVERGE",
    "Keiko refuerza Contraloría con OCI autónomos. Roberto deroga leyes pro-corrupción (31751, 32104, 31990, 32108, 32054) atribuidas al fujimorismo. Hay convergencia en fortalecer el control pero choque normativo sobre qué leyes son útiles o nocivas."
))

# =====================================================================
# ECONOMÍA
# =====================================================================
nuevas.append(mk(
    "cmp-pp-economia-001", "economia", "diagnostico",
    "k-economia-001", "r-economia-001", "DIVERGE",
    "Keiko diagnostica desaceleración, baja inversión y necesidad de retomar la senda de crecimiento. Roberto enmarca cuatro grandes males (desigualdad, corrupción, criminalidad, abuso de poder) con la desigualdad como primer mal estructural. Mismo país, marcos analíticos distintos."
))
nuevas.append(mk(
    "cmp-pp-economia-002", "economia", "propuesta_principal",
    "k-economia-002", "r-economia-010", "COINCIDE",
    "Ambos defienden economía de mercado abierta y autonomía del BCR. Keiko propone shock desregulatorio; Roberto declara expresamente respeto a TLCs y al rol del BCRP. Convergencia explícita en estabilidad macroeconómica."
))
nuevas.append(mk(
    "cmp-pp-economia-003", "economia", "meta",
    "k-economia-003", "r-economia-012", "COINCIDE",
    "Ambos fijan crecimiento del 6% del PBI como meta. Keiko habla de duplicar tasa actual; Roberto exige crecimiento real sostenido del 6%. Coinciden en la cifra; divergen en cómo conseguirla (Keiko inversión privada y desregulación, Roberto industrialización con inversión pública)."
))
nuevas.append(mk(
    "cmp-pp-economia-004", "economia", "enfoque_institucional",
    "k-economia-007", "r-economia-008", "CONTRADICE",
    "Keiko defiende exoneraciones tributarias sectoriales como herramienta para inversión. Roberto diagnostica que las exoneraciones (1,000+ proyectos de FP) drenaron presión tributaria del 17.5% (2022) al 14.6% (2025) y propone revertirlas con reforma tributaria solidaria. Posiciones opuestas."
))

# =====================================================================
# EDUCACIÓN
# =====================================================================
nuevas.append(mk(
    "cmp-pp-educacion-001", "educacion", "diagnostico",
    "k-educacion-001", "r-educacion-002", "COINCIDE",
    "Ambos diagnostican fracaso del sistema en comprensión lectora y matemática. Roberto cita cifras UMC 2024 (30% logro en 4°, 18% en 6° matemática); Keiko enfoca brechas de infraestructura. Coinciden en la crisis pero la cuantifican diferente."
))
nuevas.append(mk(
    "cmp-pp-educacion-002", "educacion", "propuesta_principal",
    "k-educacion-005", "r-educacion-018", "DIVERGE",
    "Keiko apuesta por construcción/repotenciación de colegios (5,000 según debate) con servicios básicos. Roberto apuesta por red de institutos tecnológicos y CETPRO de excelencia descentralizados. Ambos buscan calidad pero priorizan distintos eslabones del sistema."
))
nuevas.append(mk(
    "cmp-pp-educacion-003", "educacion", "meta",
    "k-educacion-007", "r-educacion-014", "DIVERGE",
    "Keiko: duplicar Beca 18 y entregar 5 millones de kits escolares. Roberto: mejorar infraestructura urbana 55% y rural 40% en 5 años; deserción rural ≤5%. Metas en distintas dimensiones del sistema, ambas verificables."
))
nuevas.append(mk(
    "cmp-pp-educacion-004", "educacion", "enfoque_institucional",
    "k-educacion-010", "r-educacion-020", "DIVERGE",
    "Keiko defiende SUNEDU y la reforma universitaria sin alterar el modelo curricular nacional. Roberto plantea descentralizar la política curricular con un Marco Curricular Nacional y diversificación regional gestionada autónomamente por pueblos originarios. Enfoques estructurales distintos."
))

# =====================================================================
# SALUD
# =====================================================================
nuevas.append(mk(
    "cmp-pp-salud-001", "salud", "diagnostico",
    "k-salud-001", "r-salud-001", "COINCIDE",
    "Ambos diagnostican un sistema de salud colapsado, fragmentado y con largas esperas; Roberto añade que es estratificado, mercantilizado y deshumanizado, y cita 200,000 muertes COVID como prueba. Convergencia en gravedad."
))
nuevas.append(mk(
    "cmp-pp-salud-002", "salud", "propuesta_principal",
    "k-salud-005", "r-salud-006", "DIVERGE",
    "Keiko ancla en telemedicina y fortalecimiento del fondo de enfermedades de alto costo. Roberto ancla en salud pública universal con integración progresiva de subsistemas (público, privado, policial, militar) en tres fases. Mismo objetivo (acceso), arquitecturas distintas."
))
nuevas.append(mk(
    "cmp-pp-salud-003", "salud", "meta",
    "k-salud-006", "r-salud-009", "DIVERGE",
    "Keiko fija meta de cobertura SIS al 100% y construir 5,000 colegios (relacionado a anemia/nutrición escolar). Roberto compromete +S/ 180,000M de inversión adicional 2026-2031, escalar gasto al 7% PBI y gratuidad total eliminando copagos. Metas en planos distintos (cobertura vs financiamiento)."
))
nuevas.append(mk(
    "cmp-pp-salud-004", "salud", "enfoque_institucional",
    "k-salud-008", "r-salud-020", "DIVERGE",
    "Keiko propone gestión por resultados y APP en hospitales. Roberto crea red nacional de farmacias y boticas populares con genéricos y banco nacional de medicamentos con compras integradas centralizadas. Mismo objetivo (acceso a medicamentos), enfoques institucionales casi opuestos."
))

# =====================================================================
# AGRICULTURA
# =====================================================================
nuevas.append(mk(
    "cmp-pp-agricultura-001", "agricultura", "diagnostico",
    "k-agricultura-001", "r-agricultura-001", "DIVERGE",
    "Keiko diagnostica falta de tecnología, brechas de riego y abandono institucional. Roberto diagnostica injusticia estructural (modelo agroexportador con privilegios vs agricultura familiar abandonada). Mismo sector, marcos distintos: Keiko 'productivista', Roberto 'redistributivo'."
))
nuevas.append(mk(
    "cmp-pp-agricultura-002", "agricultura", "propuesta_principal",
    "k-agricultura-002", "r-agricultura-006", "DIVERGE",
    "Keiko relanza el agro con riego tecnificado, semillas mejoradas y crédito vía Agrobanco. Roberto duplica presupuesto MIDAGRI a S/ 14,000M en 5 años y reestructura 200 Agencias Agrarias Territoriales con cobertura del 100% en extensión. Ambos refuerzan el agro; magnitudes y prioridades diferentes."
))
nuevas.append(mk(
    "cmp-pp-agricultura-003", "agricultura", "meta",
    "k-agricultura-005", "r-agricultura-017", "DIVERGE",
    "Keiko: 5 megaproyectos de irrigación y +1 millón de ha bajo riego. Roberto: compras públicas de alimentos al 40% directamente de agricultura familiar y campesina, beneficiando 1M familias agricultoras y 3M urbanas. Metas en distintas dimensiones (oferta hídrica vs demanda institucional)."
))
nuevas.append(mk(
    "cmp-pp-agricultura-004", "agricultura", "enfoque_institucional",
    "k-agricultura-007", "r-agricultura-007", "CONTRADICE",
    "Keiko propone fortalecer derechos sobre el agua para la agroexportación y promover propiedad y mercados. Roberto elimina la concentración de derechos de agua y los redistribuye priorizando consumo humano y pequeña agricultura. Posiciones incompatibles sobre quién tiene derecho prioritario al agua."
))

# =====================================================================
# MINERÍA
# =====================================================================
nuevas.append(mk(
    "cmp-pp-mineria-001", "mineria", "diagnostico",
    "k-mineria-001", "r-mineria-001", "COINCIDE",
    "Ambos reconocen el peso de la minería en la economía (Roberto: 9% PBI, 66% exportaciones). Roberto añade que la recaudación es menor al 15% del valor exportado y critica el modelo extractivo puro. Keiko enfatiza minería responsable. Diagnósticos compatibles, énfasis distintos."
))
nuevas.append(mk(
    "cmp-pp-mineria-002", "mineria", "propuesta_principal",
    "k-mineria-002", "r-mineria-007", "DIVERGE",
    "Keiko destraba proyectos paralizados con ventanilla única y reglas claras. Roberto declara soberanía sobre recursos y convierte al Estado en promotor de la industrialización minera con transferencia tecnológica. Ambos quieren más minería pero en modelos casi opuestos."
))
nuevas.append(mk(
    "cmp-pp-mineria-003", "mineria", "enfoque_institucional",
    "k-mineria-006", "r-mineria-013", "CONTRADICE",
    "Keiko impulsa formalización con ventanilla única y promueve concesiones para destrabar inversión. Roberto declara moratoria de concesiones aluviales en Amazonía y prohíbe minería en cuerpos de agua. Posiciones opuestas sobre fronteras de extracción."
))
nuevas.append(mk(
    "cmp-pp-mineria-004", "mineria", "meta",
    None, "r-mineria-017", "SOLO_B",
    "Roberto constituye un Fondo Soberano con ingresos mineros para financiar salud, educación, pensiones y regeneración ambiental. Keiko no plantea un fondo soberano equivalente."
))

# =====================================================================
# ENERGÍA
# =====================================================================
nuevas.append(mk(
    "cmp-pp-energia-001", "energia", "diagnostico",
    "k-energia-001", "r-energia-001", "COINCIDE",
    "Ambos diagnostican debilidad estructural en abastecimiento y precios. Roberto detalla el deterioro de PETROPERU (de 95% del mercado en los 80 a 20% hoy). Diagnósticos compatibles aunque Roberto liga la causa a privatizaciones."
))
nuevas.append(mk(
    "cmp-pp-energia-002", "energia", "propuesta_principal",
    "k-energia-002", "r-energia-005", "CONTRADICE",
    "Keiko privatiza/reestructura PETROPERU y abre el mercado de hidrocarburos. Roberto reflota y reestructura PETROPERU para recuperar 40-45% del mercado nacional bajo gobierno corporativo. Posiciones opuestas sobre el rol del Estado en hidrocarburos."
))
nuevas.append(mk(
    "cmp-pp-energia-003", "energia", "propuesta_principal",
    "k-energia-006", "r-energia-013", "COINCIDE",
    "Ambos comprometen recuperar el Gasoducto del Sur peruano. Keiko lo plantea como prioridad de infraestructura energética. Roberto detalla la ruta Camisea-Ilo-Mollendo. Convergencia explícita en el proyecto."
))
nuevas.append(mk(
    "cmp-pp-energia-004", "energia", "meta",
    "k-energia-007", "r-energia-014", "AMPLIA",
    "Keiko compromete masificación del gas con apoyo del FISE. Roberto detalla incremento del presupuesto de electrificación rural de S/ 489M a S/ 1,100M anuales (2026-2030) con +100 proyectos por año. Roberto va más lejos en magnitud y especificidad presupuestal."
))

# =====================================================================
# TRABAJO/EMPLEO (Roberto único cubre 'trabajo'; Keiko cubre mype/economia)
# =====================================================================
nuevas.append(mk(
    "cmp-pp-trabajo-001", "trabajo", "propuesta_principal",
    None, "r-trabajo-009", "SOLO_B",
    "Roberto compromete 1 millón de empleos formales nuevos con derechos plenos vía reactivación e inversión privada. Keiko aborda empleo a través de propuestas en MYPE y economía, sin meta numérica equivalente bajo tema 'trabajo'."
))

# =====================================================================
# MYPE
# =====================================================================
nuevas.append(mk(
    "cmp-pp-mype-001", "mype", "diagnostico",
    "k-mype-001", "r-mype-001", "COINCIDE",
    "Ambos reconocen que las MIPYME son el motor de la economía con alta informalidad. Roberto cifra: 99% de empresas son MIPYME, generan 48% del empleo pero solo 16% PBI, 86% informalidad. Coincidencia en el diagnóstico estructural."
))
nuevas.append(mk(
    "cmp-pp-mype-002", "mype", "propuesta_principal",
    "k-mype-005", "r-mype-006", "DIVERGE",
    "Keiko: tributación cero los 3 primeros años y licencia cero con una sola declaración (régimen pro-mercado). Roberto: programa de nueva formalidad productiva con meta de bajar informalidad de 70.7% a 55% y régimen tributario único MIPYME escalonado. Mismo objetivo (formalización), arquitecturas distintas."
))

# =====================================================================
# INDUSTRIA
# =====================================================================
nuevas.append(mk(
    "cmp-pp-industria-001", "industria", "propuesta_principal",
    "k-industria-001", "r-industria-003", "DIVERGE",
    "Keiko impulsa la industria 4.0 con incentivos a la digitalización y exportación. Roberto lanza 'Made in Perú' con shock de industrialización y ferias internacionales por región. Ambos buscan industrialización; Keiko orientada al mercado externo, Roberto al desarrollo nacional descentralizado."
))
nuevas.append(mk(
    "cmp-pp-industria-002", "industria", "propuesta_principal",
    "k-industria-006", "r-industria-004", "CONTRADICE",
    "Keiko promueve la privatización o reestructuración de PETROPERU. Roberto rechaza privatizar PETROPERU y propone reformarlo con nueva Ley de Desarrollo Corporativo y enfoque de integración vertical. Posiciones incompatibles."
))

# =====================================================================
# TRANSPORTE
# =====================================================================
nuevas.append(mk(
    "cmp-pp-transporte-001", "transporte", "diagnostico",
    "k-transporte-001", "r-transporte-001", "COINCIDE",
    "Ambos diagnostican infraestructura vial deficiente y altos costos logísticos. Roberto cuantifica: costo logístico = 26% del PBI; 80% de caminos vecinales en mal estado. Coincidencia con cuantificación distinta."
))
nuevas.append(mk(
    "cmp-pp-transporte-002", "transporte", "propuesta_principal",
    "k-transporte-002", "r-transporte-005", "DIVERGE",
    "Keiko destraba megaproyectos paralizados (Carretera Central, Aeropuerto Chinchero, Líneas Metro 3-6). Roberto prioriza Línea 2 + Línea 3 articulada con trenes de cercanía norte-sur y red ferroviaria en tres fases. Ambos priorizan transporte masivo con criterios distintos."
))
nuevas.append(mk(
    "cmp-pp-transporte-003", "transporte", "enfoque_institucional",
    "k-transporte-005", "r-transporte-016", "DIVERGE",
    "Keiko opera con APP y modelos privados como motor. Roberto subsidiará el transporte urbano con S/ 800M-3,000M (2027-2030) bajo prácticas internacionales, dado que 2 millones de limeños no tienen transporte masivo. Subsidio explícito vs mercado APP."
))

# =====================================================================
# VIVIENDA / AGUA
# =====================================================================
nuevas.append(mk(
    "cmp-pp-vivienda-001", "vivienda", "diagnostico",
    "k-vivienda-001", "r-vivienda-001", "COINCIDE",
    "Ambos identifican alto déficit habitacional y crecimiento urbano informal. Roberto cuantifica: 93% del crecimiento urbano informal en 2 décadas, 15% de municipios con PDU. Coincidencia con cuantificación de Roberto más detallada."
))
nuevas.append(mk(
    "cmp-pp-vivienda-002", "vivienda", "propuesta_principal",
    "k-vivienda-005", "r-vivienda-005", "DIVERGE",
    "Keiko: 1 millón de títulos de propiedad en 5 años vía Cofopri. Roberto: Programa WASI UKHU con S/ 2,500M para 50k viviendas nuevas + 100k mejoradas con energía limpia y materiales locales. Ambos atienden el déficit; Keiko vía formalización, Roberto vía construcción rural directa."
))
nuevas.append(mk(
    "cmp-pp-agua-001", "agua", "diagnostico",
    "k-agua-001", "r-agua-001", "COINCIDE",
    "Ambos diagnostican brechas críticas en acceso y calidad del agua. Roberto cifra: 40.4% de hogares con cloro adecuado vs 39.9% sin cloro alguno. Convergencia con cuantificación distinta."
))
nuevas.append(mk(
    "cmp-pp-agua-002", "agua", "propuesta_principal",
    "k-agua-007", "r-agua-006", "CONTRADICE",
    "Keiko promueve APP en saneamiento y rol creciente del sector privado. Roberto explícitamente pone fin a la privatización del agua y apuntala control público y comunitario. Posiciones opuestas sobre el modelo de gestión."
))

# =====================================================================
# PENSIONES / PROGRAMAS SOCIALES
# =====================================================================
nuevas.append(mk(
    "cmp-pp-pensiones-001", "pensiones", "diagnostico",
    "k-pensiones-001", "r-pensiones-001", "COINCIDE",
    "Ambos diagnostican pobreza creciente y desigualdad estructural. Roberto cifra: 27.6% pobreza monetaria, 5.5% extrema; Lima concentra 24% de la pobreza nacional. Convergencia con datos."
))
nuevas.append(mk(
    "cmp-pp-pensiones-002", "pensiones", "propuesta_principal",
    "k-pensiones-005", "r-pensiones-005", "COINCIDE",
    "Ambos prometen reordenar y fortalecer programas sociales. Roberto transforma programas focalizados en sistema articulado sin clientelismo. Keiko repotencia Foncodes, Juntos y Pensión 65. Convergencia en intención de fortalecer la red de protección."
))
nuevas.append(mk(
    "cmp-pp-pensiones-003", "pensiones", "meta",
    "k-pensiones-006", "r-pensiones-009", "DIVERGE",
    "Keiko: aumento de Pensión 65 y bono a mamitas de comedores (S/ 500 mensuales). Roberto: Pensión 65 a S/ 700 bimensuales para todos; duplicar cobertura y monto del Programa Juntos. Misma dirección redistributiva, magnitudes distintas."
))

# =====================================================================
# JUSTICIA
# =====================================================================
nuevas.append(mk(
    "cmp-pp-justicia-001", "justicia", "diagnostico",
    "k-justicia-001", "r-justicia-001", "DIVERGE",
    "Keiko diagnostica lentitud del sistema y baja efectividad de sentencias. Roberto enfatiza debilitamiento del estándar Corte IDH y leyes de amnistía 32419/32107 atribuidas al fujimorismo. Diagnósticos en planos distintos."
))
nuevas.append(mk(
    "cmp-pp-justicia-002", "justicia", "propuesta_principal",
    "k-justicia-003", "r-justicia-012", "DIVERGE",
    "Keiko: unidades de flagrancia como piedra angular de un sistema renovado. Roberto: Comisión de Reforma Integral de la Justicia con magistrados, estudiosos y ciudadanía para rediseñar acceso a la justicia y considerar elección de jueces. Ambos reforman pero con alcances muy distintos."
))
nuevas.append(mk(
    "cmp-pp-justicia-003", "justicia", "enfoque_institucional",
    "k-justicia-006", "r-justicia-004", "CONTRADICE",
    "Keiko ha respaldado normas que reducen la influencia de organismos internacionales en decisiones nacionales. Roberto reafirma permanencia del Perú en el SIDH y cumplimiento estricto de decisiones de la Corte IDH. Posiciones incompatibles sobre soberanía vs. SIDH."
))

# =====================================================================
# JUVENTUD
# =====================================================================
nuevas.append(mk(
    "cmp-pp-juventud-001", "juventud", "propuesta_principal",
    "k-juventud-001", "r-juventud-004", "DIVERGE",
    "Keiko: Centros de Oportunidad y Orientación Local (COL) en todas las regiones con cursos y atención psicológica 24/7. Roberto: Mi Primera Chamba con bono S/ 6,150 por egresado de secundaria para estudios, emprendimiento o subsidio salarial. Mismo objetivo, instrumentos distintos."
))
nuevas.append(mk(
    "cmp-pp-juventud-002", "juventud", "meta",
    "k-juventud-004", "r-juventud-011", "DIVERGE",
    "Keiko: programa Jóvenes Productivos repotenciado con alianzas empresariales. Roberto: +10,000 becas PRONABEC anuales priorizando ingenierías y ciencias aplicadas, descentralizadas a comunidades campesinas y nativas amazónicas. Metas en distintos eslabones."
))

# =====================================================================
# PESCA
# =====================================================================
nuevas.append(mk(
    "cmp-pp-pesca-001", "pesca", "diagnostico",
    "k-pesca-001", "r-pesca-002", "DIVERGE",
    "Keiko diagnostica baja productividad y necesidad de modernización. Roberto cifra la concentración (5 empresas controlan 80% de la anchoveta; exportan US$ 2,100M pero pagan al Estado <1.5% del valor) como problema central. Diagnósticos compatibles, énfasis distintos."
))
nuevas.append(mk(
    "cmp-pp-pesca-002", "pesca", "propuesta_principal",
    "k-pesca-003", "r-pesca-006", "CONTRADICE",
    "Keiko fortalece industria de harina de pescado y exportación. Roberto reorienta la anchoveta del uso industrial (harina) al consumo humano popular para combatir anemia y desnutrición. Posiciones casi opuestas sobre el destino del recurso."
))

# =====================================================================
# TURISMO
# =====================================================================
nuevas.append(mk(
    "cmp-pp-turismo-001", "turismo", "propuesta_principal",
    "k-turismo-001", "r-turismo-005", "DIVERGE",
    "Keiko relanza PromPerú y atrae 5 millones de turistas. Roberto reordena la gobernanza turística regional articulando SERNANP, Cultura y MINCETUR con énfasis en gobiernos regionales. Ambos buscan crecimiento del turismo; Keiko desde la promoción, Roberto desde la institucionalidad descentralizada."
))

# =====================================================================
# AMBIENTE
# =====================================================================
nuevas.append(mk(
    "cmp-pp-ambiente-001", "ambiente", "diagnostico",
    "k-ambiente-001", "r-ambiente-002", "COINCIDE",
    "Ambos reconocen vulnerabilidad climática severa y deforestación. Roberto cifra: 12 millones de afectados por desastres 2003-2022 con pérdidas US$6,000M+ y deforestación de 150,000 ha anuales. Coincidencia en gravedad y datos."
))
nuevas.append(mk(
    "cmp-pp-ambiente-002", "ambiente", "propuesta_principal",
    "k-ambiente-005", "r-ambiente-013", "CONTRADICE",
    "Keiko respalda flexibilización forestal para producción agroindustrial (afín a la Ley Forestal vigente). Roberto deroga la 'Ley Antiforestal' y establece moratoria a monocultivos industriales en la Amazonía. Posiciones opuestas sobre uso del bosque amazónico."
))
nuevas.append(mk(
    "cmp-pp-ambiente-003", "ambiente", "enfoque_institucional",
    "k-ambiente-007", "r-ambiente-006", "CONTRADICE",
    "Keiko mantiene el modelo de naturaleza como recurso productivo. Roberto reconoce constitucionalmente a la naturaleza (ríos, cuencas) como sujetos de derecho. Posiciones filosóficamente opuestas."
))
nuevas.append(mk(
    "cmp-pp-ambiente-004", "ambiente", "meta",
    None, "r-ambiente-019", "SOLO_B",
    "Roberto: Plan Nacional de Restauración Ambiental con meta de 500,000 ha restauradas, financiado por impuesto a utilidades extraordinarias del sector extractivo. Keiko no fija meta comparable de restauración."
))

# =====================================================================
# ORDEN JURÍDICO (Roberto cubre con 3.6-3.7 reasignados; Keiko con 1.4)
# =====================================================================
nuevas.append(mk(
    "cmp-pp-orden_juridico-001", "orden_juridico", "propuesta_principal",
    "k-orden_juridico-001", "r-orden_juridico-011", "DIVERGE",
    "Keiko: predictibilidad jurídica para la inversión, con mecanismos de seguridad para contratos. Roberto: restablecer el CND derogando el DS 007-2007-PCM para retomar la descentralización planificada. Ambos buscan orden institucional pero en planos distintos (seguridad jurídica vs descentralización)."
))

# =====================================================================
# DEPORTE
# =====================================================================
nuevas.append(mk(
    "cmp-pp-deporte-001", "deporte", "propuesta_principal",
    "k-deporte-001", "r-deporte-006", "DIVERGE",
    "Keiko: el IPD pasa a la PCM para invertir en deporte recreativo, escolar y profesional, alejando jóvenes de la delincuencia. Roberto: Sistema Nacional del Deporte, la Recreación y el Ocio Productivo articulando Estado, sector privado y comunidades. Mismo objetivo, arquitecturas distintas."
))

# =====================================================================
# PERUANOS EN EL EXTERIOR
# =====================================================================
nuevas.append(mk(
    "cmp-pp-peruanos_exterior-001", "peruanos_exterior", "propuesta_principal",
    "k-peruanos_exterior-001", "r-peruanos_exterior-003", "COINCIDE",
    "Ambos comprometen mejor atención consular y vínculo con la diáspora. Roberto crea Clínica de Desarrollo Territorial y Registro Territorial; Keiko fortalece servicios consulares y derechos políticos. Convergencia en intención."
))

# =====================================================================
# TEMAS SOLO_B (Roberto exclusivo)
# =====================================================================
nuevas.append(mk(
    "cmp-pp-constitucion-001", "constitucion", "propuesta_principal",
    None, "r-constitucion-005", "SOLO_B",
    "Roberto propone una nueva Constitución de consenso vía art. 206 o asamblea constituyente como propuesta-ancla. Keiko no plantea reforma constitucional sustantiva (defiende la Constitución de 1993 y la reforma reciente del Congreso)."
))
nuevas.append(mk(
    "cmp-pp-cti-001", "cti", "propuesta_principal",
    None, "r-cti-003", "SOLO_B",
    "Roberto crea el Ministerio de Ciencia y Tecnología vinculado a institutos técnicos regionales, ZEE de Ilo/Matarani/Chancay y reforma CONCYTEC. Keiko no propone una arquitectura institucional equivalente para CTI."
))
nuevas.append(mk(
    "cmp-pp-cultura-001", "cultura", "propuesta_principal",
    None, "r-cultura-007", "SOLO_B",
    "Roberto crea el Ministerio de Las Culturas que prioriza derechos de pueblos originarios (titulación, georreferenciación). Keiko no plantea un rediseño institucional comparable."
))
nuevas.append(mk(
    "cmp-pp-exterior-001", "exterior", "propuesta_principal",
    None, "r-exterior-029", "SOLO_B",
    "Roberto diseña una política exterior 'nacional, autónoma, humanista, democrática, descentralizada, medioambiental, normativa, institucional y pro paz'. Keiko no detalla un marco doctrinal equivalente para política exterior."
))
nuevas.append(mk(
    "cmp-pp-genero-001", "genero", "propuesta_principal",
    None, "r-genero-015", "SOLO_B",
    "Roberto crea un Sistema Nacional de Cuidados con enfoque de género e intercultural. Keiko no propone un sistema equivalente; aborda género desde MIMP/CEM pero sin Sistema Nacional."
))
nuevas.append(mk(
    "cmp-pp-genero-002", "genero", "propuesta_principal",
    None, "r-genero-010", "SOLO_B",
    "Roberto despenaliza la interrupción del embarazo en casos de violencia sexual y riesgo para la madre. Keiko no respalda esta despenalización. SOLO_B en sentido propositivo (Keiko adopta postura contraria fuera de su plan formal)."
))
nuevas.append(mk(
    "cmp-pp-indigenas-001", "indigenas", "propuesta_principal",
    None, "r-indigenas-003", "SOLO_B",
    "Roberto propone escaños reservados para pueblos originarios en el Congreso y cuotas en la dirección/gestión estatal. Keiko no propone escaños reservados ni mecanismos equivalentes."
))


def main():
    d = json.loads(RUTA.read_text(encoding="utf-8"))
    print(f"Antes plan_vs_plan: {len(d['plan_vs_plan'])}")
    print(f"Nuevas a agregar: {len(nuevas)}")
    d["plan_vs_plan"].extend(nuevas)
    RUTA.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Despues plan_vs_plan: {len(d['plan_vs_plan'])}")
    print("OK escrito.")


if __name__ == "__main__":
    main()
