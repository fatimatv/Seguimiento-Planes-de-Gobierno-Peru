# -*- coding: utf-8 -*-
"""Extracción de Dimensión Económica - Roberto Sánchez (Task 11).

Cubre secciones 4.1 a 4.7 del plan: Economía, Industrialización, Minería,
Empleo, Emprendimiento, Mercados Populares y CTI.
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
# 4.1 ECONOMÍA (líneas 170-180) — tema: economia
# Continúa desde r-economia-003
# =====================================================================
S41 = "Dimensión Económica — 4.1 Economía"

nuevas.append(mk(
    "r-economia-004", "economia", "diagnostico", "ALTA",
    "Diagnóstico fiscal: en 2024 el Perú incumplió por segundo año las reglas fiscales — déficit 3.5% del PBI (tope 2.8%) y gasto público creció 6.2% (tope 4.7%) — atribuido a captura del Congreso por bancada fujimorista.",
    "En 2024, el Perú volvió a incumplir por segundo año consecutivo las reglas fiscales que establecen límites al déficit y al crecimiento del gasto público. El déficit fiscal llegó a 3,5 % del PBI, por encima del tope permitido de 2,8 %",
    f"{S41} — Situación Actual", 172, 172,
))

nuevas.append(mk(
    "r-economia-005", "economia", "diagnostico", "MEDIA",
    "Diagnóstico de disparidades regionales: pobreza monetaria nacional 25.7%, con regiones andinas hasta 41% (Cajamarca, Loreto, Puno, Pasco) y pobreza rural casi dobla la urbana.",
    "En 2025, por ejemplo, la pobreza monetaria a nivel nacional alcanzó 25,7% de la población (INEI) pero con enormes variaciones entre departamentos: regiones andinas como Cajamarca (41% de pobreza), Loreto (40.1%), Puno (37.5%) o Pasco (36.4%)",
    f"{S41} — Situación Actual", 172, 172,
))

nuevas.append(mk(
    "r-economia-006", "economia", "diagnostico", "ALTA",
    "Diagnóstico de concentración primario-exportadora: minería, agricultura y energía representan ~85% de las exportaciones; el país ocupa el puesto 105 de 130 en el Índice de Complejidad Económica.",
    "Minería, agricultura y energía representan cerca del 85% de las exportaciones totales del país, reflejando una canasta poco diversificada y de baja complejidad (Perú ocupa el puesto 105 de 130 economías en el Índice de Complejidad Económica)",
    f"{S41} — Situación Actual", 172, 172,
))

nuevas.append(mk(
    "r-economia-007", "economia", "diagnostico", "MEDIA",
    "Diagnóstico financiero: crédito privado solo 42% del PIB (vs 76% promedio OCDE); oligopolio de 4 bancos maneja el 80% de intermediación financiera; concentración en pagos con tarjeta.",
    "el crédito privado representa solo el 42% del PIB, muy por debajo del promedio de la OCDE (76%)",
    f"{S41} — Situación Actual", 174, 174,
))

nuevas.append(mk(
    "r-economia-008", "economia", "diagnostico", "ALTA",
    "Diagnóstico tributario: la presión tributaria cayó de 17.5% (2022) a 14.6% (2025); Fuerza Popular ha promovido 1,000+ proyectos de ley de exoneraciones tributarias por S/ 27,000M anuales.",
    "En 2022, gracias a una reforma tributaria parcial propuesta por nuestro compañero Pedro Francke en el año 2021, la presión tributaria llegó en setiembre del año 2022 17.5% del PBI, el mayor nivel en décadas. Pero hoy, tras años de exoneraciones tributarias impulsadas por un Congreso capturado",
    f"{S41} — Situación Actual", 174, 174,
))

nuevas.append(mk(
    "r-economia-009", "economia", "diagnostico", "MEDIA",
    "Diagnóstico evasión tributaria: el 34% del IGV y el 50% del Impuesto a la Renta no se pagan, mayormente por grandes empresas, no por personas comunes.",
    "Además, el 34 % del IGV y el 50 % del Impuesto a la Renta no se pagan, y no son las personas comunes quienes evaden, sino principalmente las grandes empresas",
    f"{S41} — Situación Actual", 174, 174,
))

nuevas.append(mk(
    "r-economia-010", "economia", "principio", "ALTA",
    "Principio: ser un Estado de economía de mercado abierta, respetuoso de los Tratados de Libre Comercio (TLCs), con normas amigables a la inversión interna y externa cuyos contratos estén protegidos por el Estado de derecho.",
    "Ser Estado de economía de mercado abierta, respetuosos de los Tratados Internacionales de Libre Comercio – TLCs, con normas amigables a la inversión interna y externa, cuyos contratos estén protegidos por el Estado de derecho",
    f"{S41} — Medidas Propuestas", 178, 178,
))

nuevas.append(mk(
    "r-economia-011", "economia", "propuesta", "ALTA",
    "Preservar la autonomía y capacidad técnica del Banco Central de Reserva del Perú (BCRP) garantizando su mandato constitucional y su rol de complemento a la estabilidad fiscal.",
    "Preservar la autonomía y capacidad técnica del Banco Central de Reserva del Perú (BCRP), garantizando su mandato constitucional",
    f"{S41} — Medidas Propuestas", 178, 178,
))

nuevas.append(mk(
    "r-economia-012", "economia", "meta", "ALTA",
    "Meta macroeconómica: garantizar un crecimiento real del PBI sostenido de 6% para generar las condiciones de mayores ingresos, mejor empleo y crecimiento de largo plazo.",
    "Garantizar un crecimiento importante y sostenido del real del PBI de 6%",
    f"{S41} — Medidas Propuestas", 178, 178,
    meta="Crecimiento real del PBI de 6% sostenido",
))

nuevas.append(mk(
    "r-economia-013", "economia", "propuesta", "MEDIA",
    "Fortalecer el Consejo Fiscal preservando su autonomía y capacidad técnica, dotándolo de opinión vinculante sobre el uso de recursos públicos.",
    "Fortalecimiento del Consejo Fiscal, preservando su autonomía y capacidad técnica, además de brindarle más facultades para contribuir con la estabilidad macroeconómica",
    f"{S41} — Medidas Propuestas", 178, 178,
))

nuevas.append(mk(
    "r-economia-014", "economia", "propuesta", "MEDIA",
    "Consolidar una senda de reducción del déficit fiscal priorizando el incremento de la recaudación y la eficiencia del gasto, sin afectar programas sociales esenciales.",
    "Consolidar una senda de reducción del déficit fiscal, priorizando el incremento de la recaudación y la eficiencia del gasto, sin afectar programas sociales esenciales",
    f"{S41} — Medidas Propuestas", 178, 178,
))

nuevas.append(mk(
    "r-economia-015", "economia", "propuesta", "MEDIA",
    "Optimizar la calidad del gasto público mediante evaluaciones de desempeño y presupuestos por resultados con un enfoque ágil y menos burocrático.",
    "Optimizar la calidad del gasto público, mediante evaluaciones de desempeño y presupuestos por resultados, con un enfoque ágil y menos burocrático",
    f"{S41} — Medidas Propuestas", 178, 178,
))

nuevas.append(mk(
    "r-economia-016", "economia", "propuesta", "MEDIA",
    "Establecer un marco claro y transparente para las asociaciones público-privadas (APPs), priorizando proyectos de alto impacto económico y social, con el gobierno como promotor del desarrollo y no principal actor.",
    "Establecer un marco claro y transparente para las asociaciones público-privada, priorizando proyectos de alto impacto económico y social",
    f"{S41} — Medidas Propuestas", 180, 180,
))

nuevas.append(mk(
    "r-economia-017", "economia", "propuesta", "MEDIA",
    "Autorizar y fomentar el ingreso de nuevos competidores en el mercado financiero, eliminar procedimientos innecesarios e impulsar la interoperabilidad con fintechs y start-ups.",
    "Autorizar y fomentar el ingreso de nuevos competidores en el mercado financiero nacional, con miras a brindar mejores servicios financieros, mejores condiciones de préstamos y un trato adecuado a los ciudadanos",
    f"{S41} — Medidas Propuestas", 180, 180,
))

nuevas.append(mk(
    "r-economia-018", "economia", "propuesta", "MEDIA",
    "Implementar un mecanismo de fast-track para proyectos priorizados de canon en el marco de Planes de Desarrollo Territorial y Cierre de Brechas, con ventanilla única intersectorial y plazos máximos obligatorios.",
    "Se implementará un mecanismo de “fast track” para proyectos priorizados en el marco de Planes de Desarrollo Territorial y Cierre de Brechas, que reduzca plazos y simplifique trámites",
    f"{S41} — Medidas Propuestas", 180, 180,
))

nuevas.append(mk(
    "r-economia-019", "economia", "propuesta", "MEDIA",
    "Implementar una estrategia de diplomacia económica activa que articule MINCETUR, Cancillería, MEF y PromPerú para defender el acceso de productos peruanos a mercados internacionales en un contexto de proteccionismo creciente.",
    "Implementar una estrategia de diplomacia económica activa que articule al MINCETUR, la Cancillería, el MEF y PromPerú para defender el acceso de los productos peruanos a los mercados internacionales",
    f"{S41} — Medidas Propuestas", 180, 180,
))

nuevas.append(mk(
    "r-economia-020", "economia", "propuesta", "MEDIA",
    "Institucionalizar mesas sectoriales permanentes de diálogo y concertación con gremios profesionales, empresariales y laborales en sectores estratégicos (minería, agroexportación, turismo, manufactura, construcción).",
    "Institucionalizar mesas sectoriales permanentes de diálogo y concertación con gremios profesionales, empresariales y laborales en sectores estratégicos",
    f"{S41} — Medidas Propuestas", 180, 180,
))

# =====================================================================
# 4.2 INDUSTRIALIZACIÓN (líneas 180-184) — tema: industria
# =====================================================================
S42 = "Dimensión Económica — 4.2 Industrialización"

nuevas.append(mk(
    "r-industria-001", "industria", "diagnostico", "ALTA",
    "Diagnóstico estructural: el modelo primario-exportador peruano ha generado dependencia, informalidad y bajo valor agregado, dejándonos vulnerables a precios internacionales.",
    "El modelo primario-exportador ha generado dependencia, informalidad y bajo valor agregado",
    f"{S42} — Situación Actual", 180, 180,
))

nuevas.append(mk(
    "r-industria-002", "industria", "diagnostico", "MEDIA",
    "Diagnóstico de fragmentación industrial: pequeños industriales en zonas altoandinas y amazónicas carecen de infraestructura y tecnología para desarrollar un sistema industrial propio.",
    "Uno de los problemas críticos es la falta de infraestructura adecuada que permita a pequeños industriales, especialmente en zonas altoandinas y amazónicas de acceder a tecnologías adaptas para desarrollar un propio sistema industrial",
    f"{S42} — Situación Actual", 180, 180,
))

nuevas.append(mk(
    "r-industria-003", "industria", "propuesta", "ALTA",
    "Propuesta ancla 'Made in Perú': ejecutar un shock de medidas para impulsar la industrialización, transformar materias primas en productos de mayor valor agregado y crear Ferias Industriales Internacionales por cada región.",
    "Potenciaremos la producción Made In Perú: Ejecutaremos un shock de medidas para impulsar la industrialización, el aprovechamiento de materias primas hacia actividades de mayor valor agregado y promoción de la transformación productiva",
    f"{S42} — Medidas Propuestas", 182, 182,
))

nuevas.append(mk(
    "r-industria-004", "industria", "propuesta", "ALTA",
    "Garantizar la seguridad energética sin privatizar PETROPERU; fortalecerlo y reformarlo con una nueva Ley de Desarrollo Corporativo bajo meritocracia y enfoque de integración vertical.",
    "Garantizaremos la seguridad energética del país, no privatizaremos PETROPERU y lo fortaleceremos y reformaremos con una nueva Ley de Desarrollo Corporativo para asegurar la estabilidad de su dirección",
    f"{S42} — Medidas Propuestas", 182, 182,
))

nuevas.append(mk(
    "r-industria-005", "industria", "propuesta", "MEDIA",
    "Potenciar la descentralización productiva impulsando Parques Industriales Regionales en terrenos del Estado, interconectados y cerca de fuentes de materia prima.",
    "A nivel territorial potenciaremos la descentralización productiva impulsando y masificando los Parques Industriales Regionales en terrenos del Estado",
    f"{S42} — Medidas Propuestas", 182, 182,
))

nuevas.append(mk(
    "r-industria-006", "industria", "meta", "ALTA",
    "Meta financiera: implementar el programa 'Financiamiento Popular' con S/ 15,000 millones de garantía pública para dinamizar pequeñas y medianas empresas, cooperativas, agronegocios familiares y transporte urbano.",
    "implementaremos un programa denominado “Financiamiento Popular”, con una garantía pública de S/ 15,000 millones, articulado con el sistema financiero, destinado a dinamizar a las pequeñas y medianas empresas",
    f"{S42} — Medidas Propuestas", 182, 182,
    meta="Garantía pública S/ 15,000 millones (Financiamiento Popular)",
))

nuevas.append(mk(
    "r-industria-007", "industria", "meta", "ALTA",
    "Meta: al menos un millón de agricultores familiares, comuneros y pequeños agricultores accederán a crédito barato y asistencia técnica para fines productivos.",
    "Al menos un millón de agricultores familiares, comuneros y pequeña agricultura accederán a crédito barato y asistencia técnica para fines productivos",
    f"{S42} — Medidas Propuestas", 182, 182,
    meta="≥1 millón agricultores familiares con crédito barato y asistencia técnica",
))

nuevas.append(mk(
    "r-industria-008", "industria", "propuesta", "ALTA",
    "Desarrollar e implementar un Sistema Industrial descentralizado y sostenible para industrializar todos los principales recursos naturales (agrícolas, marítimos, tierras raras, minerales estratégicos) y generar productos con alto valor agregado in situ.",
    "Desarrollar e implementar el Sistema Industrial totalmente descentralizado y sostenible, que beneficie a toda la población y a la Nación, transformando el sistema extractor actual para generar productos con alto valor agregado in situ",
    f"{S42} — Medidas Propuestas", 182, 182,
))

nuevas.append(mk(
    "r-industria-009", "industria", "propuesta", "MEDIA",
    "Crear el Sistema 'Producto Peruano, Moderno, Tecnológico e Innovador' para definir familias de productos con alto valor agregado destinados a los mercados e industrias más avanzadas del mundo.",
    "Crear el \"Sistema Producto Peruano, Moderno, Tecnológico e Innovador\" para definir familias de productos con alto valor agregado",
    f"{S42} — Medidas Propuestas", 184, 184,
))

nuevas.append(mk(
    "r-industria-010", "industria", "propuesta", "MEDIA",
    "Construir parques industriales interconectados en todas las regiones del Perú, cerca de las fuentes de materia prima, con suministro integral de servicios básicos y logísticos (agua, energía, gas, internet, carreteras, ferrocarril, aeropuertos).",
    "Construir e implementar parques industriales interconectados en todas las regiones del Perú, cerca de las fuentes de materia prima, con suministro integral de servicios básicos y Logísticos",
    f"{S42} — Medidas Propuestas", 184, 184,
))

nuevas.append(mk(
    "r-industria-011", "industria", "propuesta", "MEDIA",
    "Crear un Mapa Nacional de Recursos Naturales que identifique todos los recursos por región y defina los potenciales productos con alto valor agregado que se pueden producir con cada materia prima.",
    "Crear un Mapa Nacional de Recursos Naturales que identifique todos los recursos por región y defina los potenciales productos con alto valor que se pueden producir con cada materia prima",
    f"{S42} — Medidas Propuestas", 184, 184,
))

nuevas.append(mk(
    "r-industria-012", "industria", "propuesta", "MEDIA",
    "Crear programas de cooperación Industria–Universidad–Gobierno para acelerar la industrialización, integrando investigación, desarrollo de productos y publicaciones.",
    "Crear programas de cooperación Industria – Universidad - Gobierno para acelerar la industrialización, integrando investigación, desarrollo de productos y publicaciones",
    f"{S42} — Medidas Propuestas", 184, 184,
))

# =====================================================================
# 4.3 MINERÍA (líneas 184-198) — tema: mineria
# =====================================================================
S43 = "Dimensión Económica — 4.3 Minería"

nuevas.append(mk(
    "r-mineria-001", "mineria", "diagnostico", "ALTA",
    "Diagnóstico cuantitativo: la minería representa 9% del PBI nacional, 66%+ de exportaciones (US$ 62,848M en 2025) y 280,674 empleos formales; pero la recaudación es solo 13.9% del PBI minero, menos del 15% del valor exportado.",
    "La minería representa el 9.0% del PBI Nacional (PBI Minero Metálico), el 66%+ de las exportaciones totales del Perú, 280,674 empleos directos formales (Dic 2025). Las exportaciones mineras del 2025 fueron de US$ 62,848 M",
    f"{S43} — Situación Actual", 184, 184,
    meta="Minería: 9% PBI, 66%+ exportaciones, US$ 62,848M (2025)",
))

nuevas.append(mk(
    "r-mineria-002", "mineria", "diagnostico", "ALTA",
    "Diagnóstico de paralización: 21 proyectos mineros por US$ 18,000 millones están paralizados y existen 197 conflictos sociales activos, reflejo de injusticias en la distribución de los beneficios.",
    "Actualmente, 21 proyectos por US$ 18,000 millones están paralizados y hay 197 conflictos sociales activos que dificultan implementar el plan de inversión minera",
    f"{S43} — Situación Actual", 184, 184,
    meta="21 proyectos US$ 18,000M paralizados; 197 conflictos sociales activos",
))

nuevas.append(mk(
    "r-mineria-003", "mineria", "diagnostico", "ALTA",
    "Diagnóstico de venta a precio bajo: el país exporta hierro al 62% de pureza a US$ 16/tonelada y cobre al 100% a US$ 13,000/tonelada, sin control sobre minerales y tierras raras esenciales para alta tecnología.",
    "Estamos vendiendo minerales a precio de regalo, con altos costos ambientales, sociales y económicos. Hierro con 62% de pureza a 16 dólares la tonelada, y cobre al 100% de pureza a 13,000 dólares la tonelada",
    f"{S43} — Situación Actual", 184, 184,
))

nuevas.append(mk(
    "r-mineria-004", "mineria", "diagnostico", "MEDIA",
    "Diagnóstico industrial: Perú es uno de los mayores productores de cobre, pero no figura en el ranking de productores de cobre refinado; la mayoría exporta concentrados y el refinado se hace en el extranjero.",
    "Aunque el Perú es uno de los mayores productores de cobre del mundo, no figuramos en el ranking de países productores de cobre refinado. La gran mayoría de las empresas mineras (como Antamina o Las Bambas) exportan concentrados de cobre y no cátodos",
    f"{S43} — Situación Actual", 186, 186,
))

nuevas.append(mk(
    "r-mineria-005", "mineria", "diagnostico", "ALTA",
    "Diagnóstico de minería ilegal: entre informalidad e ilegalidad se mueven ~S/ 12,000 millones anuales y el Estado deja de recaudar ~S/ 7,800 millones.",
    "Entre la informalidad y la ilegalidad se mueven cerca de 12,000 mil millones de soles anuales y el Estado deja de recaudar aproximadamente 7,800 millones",
    f"{S43} — Situación Actual", 186, 186,
    meta="Minería ilegal: S/ 12,000M anuales; S/ 7,800M no recaudados",
))

nuevas.append(mk(
    "r-mineria-006", "mineria", "diagnostico", "ALTA",
    "Diagnóstico de la formalización fallida: solo 2.4% de los 84,000 inscritos originalmente logró culminar el proceso de formalización en 14 años; tras transferencia al MINEM en 2024 solo se formalizaron 20 mineros.",
    "De los 84 mil inscritos originalmente solo el 2.4% logró, en 14 años, culminar el proceso de formalización. Esta grave situación se ha profundizado desde que el año 2024 se transfirieron las competencias",
    f"{S43} — Situación Actual", 197, 197,
    meta="Formalización minera: 2.4% de 84,000 inscritos en 14 años",
))

nuevas.append(mk(
    "r-mineria-007", "mineria", "propuesta", "ALTA",
    "Soberanía sobre los recursos naturales: convertir al Estado en promotor de la industrialización minera para ampliar la cadena de valor, con transformación y transferencia tecnológica dentro del Perú y generación de empleos dignos.",
    "Garantizaremos la soberanía sobre los recursos naturales de la minería metálica y no metálica, convirtiendo al Estado peruano en promotor de la industrialización como eje del desarrollo de los próximos años",
    f"{S43} — Medidas Propuestas", 195, 195,
))

nuevas.append(mk(
    "r-mineria-008", "mineria", "propuesta", "ALTA",
    "Salto a la metalurgia avanzada: refinerías y metalurgia de nueva generación para el procesamiento del cobre, zinc, hierro y litio.",
    "Perfilar el gran salto a la metalurgia avanzada (refinación y aleaciones): Refinerías y metalurgia de nueva generación para el procesamiento del cobre, zinc, hierro, litio",
    f"{S43} — Medidas Propuestas", 195, 195,
))

nuevas.append(mk(
    "r-mineria-009", "mineria", "propuesta", "MEDIA",
    "Priorizar futuros otorgamientos de concesiones a empresas que acepten condiciones de transferencia tecnológica y compensación industrial.",
    "Priorizaremos los futuros otorgamientos de concesiones a las empresas que acepten condiciones de transferencia tecnológica y compensación industrial",
    f"{S43} — Medidas Propuestas", 195, 195,
))

nuevas.append(mk(
    "r-mineria-010", "mineria", "propuesta", "MEDIA",
    "Poner en operatividad la ventanilla única digital minera para uniformizar, transparentar y simplificar los trámites administrativos a lo largo de todo el ciclo de un proyecto minero.",
    "Poner en operatividad la ventanilla única digital minera para uniformizar, transparentar y simplificar los trámites administrativos a lo largo de todo el ciclo de un proyecto minero",
    f"{S43} — Medidas Propuestas", 195, 195,
))

nuevas.append(mk(
    "r-mineria-011", "mineria", "propuesta", "ALTA",
    "Aprobar la Política Nacional para el fomento, promoción y formalización permanente de la Pequeña Minería y Minería Artesanal, diferenciando con claridad la minería en proceso de formalización de la minería ilegal.",
    "Aprobar la Política Nacional para el fomento, promoción y formalización permanente de la Pequeña Minería y Minería Artesanal, diferenciando con claridad la minería en proceso de formalización de la minería ilegal",
    f"{S43} — Medidas Propuestas", 195, 195,
))

nuevas.append(mk(
    "r-mineria-012", "mineria", "propuesta", "MEDIA",
    "Aprobar la Ley de fomento y promoción de la pequeña minería y minería artesanal con seguridad jurídica, asistencia técnica descentralizada, trazabilidad, líneas de financiamiento y fondo de remediación ambiental basado en aportes mineros.",
    "Aprobar la Ley de fomento y promoción de la pequeña minería y minería artesanal. que contemple normas como seguridad jurídica de operaciones",
    f"{S43} — Medidas Propuestas", 195, 195,
))

nuevas.append(mk(
    "r-mineria-013", "mineria", "propuesta", "ALTA",
    "Moratoria de concesiones aluviales en la Amazonía y revisión de concesiones otorgadas que se superponen a cuerpos de agua, para mantener libre de minería esa región.",
    "Para nuestra Amazonía, que debe estar libre de minería en especial la aluvial (en cualquiera de sus formas, sea ilegal, informal y legal), se plantea la moratoria de concesiones y revisar las concesiones otorgadas que se superponen a cuerpos de agua",
    f"{S43} — Medidas Propuestas", 197, 197,
))

nuevas.append(mk(
    "r-mineria-014", "mineria", "propuesta", "MEDIA",
    "Implementar el censo minero y el plan de Formalización Minera en concordancia con los Gobiernos Regionales para efectivizar el procedimiento iniciado en 2012 que ha fracasado.",
    "Implementaremos el censo minero. Nuestro compromiso con los pequeños mineros y artesanales en su proceso de formalización",
    f"{S43} — Medidas Propuestas", 197, 197,
))

nuevas.append(mk(
    "r-mineria-015", "mineria", "propuesta", "MEDIA",
    "Regular, controlar y formalizar todos los eslabones de la cadena de producción y comercialización del oro mediante un sistema de trazabilidad.",
    "Se regulará, controlará y formalizará a todos los eslabones de la cadena de producción y comercialización del oro. A través de la implementación de un sistema de control, de trazabilidad",
    f"{S43} — Medidas Propuestas", 197, 197,
))

nuevas.append(mk(
    "r-mineria-016", "mineria", "propuesta", "ALTA",
    "Impulso a Zonas Económicas Especiales (ZEE) cerca de los puertos de Ilo, Matarani y Chancay para favorecer industrias de transformación de minerales.",
    "Impulso a zonas económicas especiales (ZEE) cerca de los puertos de Ilo, Matarani y Chancay para favorecer industrias de transformación de minerales",
    f"{S43} — Medidas Propuestas", 197, 197,
))

nuevas.append(mk(
    "r-mineria-017", "mineria", "propuesta", "ALTA",
    "Constituir un Fondo Soberano con ingresos de la extracción de recursos minerales para financiar salud, educación, pensiones y la regeneración de áreas degradadas.",
    "Constituir un Fondo Soberano con ingresos de la extracción de recursos minerales para financiar salud, educación, pensiones y la regeneración de las áreas degradadas",
    f"{S43} — Medidas Propuestas", 197, 197,
))

nuevas.append(mk(
    "r-mineria-018", "mineria", "100dias", "100DIAS",
    "Compromiso de 100 días: en el primer año se instalará el Consejo Nacional de Transformación Productiva — con sectores ministeriales, GORE, academia y sector privado — que elaborará el Plan Nacional de Transformación Productiva 2026-2031.",
    "El primer año se instalará el Consejo Nacional de Transformación Productiva, con los sectores ministeriales, los Gobiernos Regionales, la academia y el sector privado, el cual elaborará el Plan Nacional de Transformación Productiva 2026-2031",
    f"{S43} — Medidas Propuestas", 197, 197,
))

nuevas.append(mk(
    "r-mineria-019", "mineria", "propuesta", "MEDIA",
    "Garantizar el cierre efectivo de minas para que las áreas intervenidas retornen a su estado previo, con responsabilidad de las empresas mineras y sanción a los titulares que no cumplan.",
    "Garantizar el efectivo cierre de minas a fin de que las áreas intervenidas por los proyectos mineros retornen a su estado previo al desarrollo de la actividad",
    f"{S43} — Medidas Propuestas", 197, 197,
))

nuevas.append(mk(
    "r-mineria-020", "mineria", "propuesta", "MEDIA",
    "Régimen tributario simplificado para PPM/PMA con retención única y definitiva del 5% en la planta de beneficio que cancele Impuesto a la Renta e IGV, y elevar límites operativos a 800 UIT en ventas.",
    "También un régimen simplificado con costos menores de formalización, incluyendo la retención única y definitiva del 5% en la planta de beneficio, pago que cancela automáticamente el Impuesto a la Renta e IGV",
    f"{S43} — Medidas Propuestas", 195, 195,
    meta="Régimen PPM/PMA: retención 5%; límite 800 UIT ventas, 400 UIT activos",
))

# =====================================================================
# 4.4 EMPLEO (líneas 199-205) — tema: trabajo
# =====================================================================
S44 = "Dimensión Económica — 4.4 Empleo"

nuevas.append(mk(
    "r-trabajo-001", "trabajo", "diagnostico", "ALTA",
    "Diagnóstico de crecimiento y poder adquisitivo: desde 2014 el PBI no supera 4% anual (salvo 2021); la remuneración mínima no cubre ni el componente alimentario de la canasta básica familiar.",
    "Desde el 2014 el PBI no supera el 4% de crecimiento anual (a excepción del 2021). La productividad ha seguido la misma tendencia. No se ha podido recuperar el poder de compra de los ingresos laborales prepandemia",
    f"{S44} — Situación Actual", 199, 199,
))

nuevas.append(mk(
    "r-trabajo-002", "trabajo", "diagnostico", "ALTA",
    "Diagnóstico de precarización: la situación es especialmente grave para las mujeres; solo 1 de cada 3 trabajadores formales del sector privado son mujeres; tasa de subempleo y desempleo por encima del nivel pre-pandemia.",
    "La situación es especialmente grave para las mujeres, considerando que solo 1 de cada 3 trabajadores formales del sector privado son mujeres",
    f"{S44} — Situación Actual", 199, 199,
))

nuevas.append(mk(
    "r-trabajo-003", "trabajo", "diagnostico", "MEDIA",
    "Diagnóstico estructural: solo 50% de la PEA ocupada tiene empleo asalariado (formal o informal); en países desarrollados es 90%.",
    "Sólo 50% de la PEA ocupada tiene un empleo asalariado (formal o informal), mientras que la otra mitad se desempeña como autónomos (la gran mayoría en condiciones precarias). En los países desarrollados, en promedio, 90% del empleo es asalariado",
    f"{S44} — Situación Actual", 199, 199,
))

nuevas.append(mk(
    "r-trabajo-004", "trabajo", "diagnostico", "MEDIA",
    "Diagnóstico de uso desnaturalizado de la contratación temporal: 2 de cada 3 trabajadores formales privados tienen contrato temporal pese a realizar labores permanentes, impidiendo sindicalización y negociación colectiva.",
    "Dos de cada 3 trabajadores formales privados tienen un contrato temporal, a pesar de que la mayoría de ellos realiza labores permanentes, lo cual imposibilita en la práctica el ejercicio de la sindicalización",
    f"{S44} — Situación Actual", 199, 199,
))

nuevas.append(mk(
    "r-trabajo-005", "trabajo", "diagnostico", "MEDIA",
    "Diagnóstico previsional: solo 1 de cada 3 trabajadores está afiliado a algún sistema previsional; EsSalud sufre recortes de aporte (agroexportadores) y la libre disposición de CTS desnaturalizó su rol como protección contra el desempleo.",
    "Solo 1 de cada 3 trabajadores está afiliado a algún sistema previsional y no todos cotizan de manera regular",
    f"{S44} — Situación Actual", 199, 199,
))

nuevas.append(mk(
    "r-trabajo-006", "trabajo", "meta", "ALTA",
    "Meta de inversión pública: acelerar la inversión pública en infraestructura productiva para una tasa de crecimiento de al menos 6% anual, mejorar productividad y ampliar el crecimiento potencial.",
    "Aplicaremos una política que acelere la inversión pública en infraestructura productiva para contribuir a reactivar la economía a una tasa de crecimiento de al menos 6% anual",
    f"{S44} — Medidas Propuestas", 201, 201,
    meta="≥6% crecimiento PBI anual",
))

nuevas.append(mk(
    "r-trabajo-007", "trabajo", "propuesta", "ALTA",
    "Fomentar la sindicalización y negociación colectiva a nivel supraempresarial para que los trabajadores conviertan los incrementos de productividad en mayores remuneraciones y mejores condiciones.",
    "Fomentaremos la sindicalización y negociación colectiva (sobre todo a nivel supraempresarial), para que los trabajadores logren convertir los incrementos de su productividad en mayores remuneraciones",
    f"{S44} — Medidas Propuestas", 201, 201,
))

nuevas.append(mk(
    "r-trabajo-008", "trabajo", "meta", "ALTA",
    "Meta salarial: aumentar progresivamente la Remuneración Mínima Vital a S/ 1,500 (canasta básica familiar equivale a S/ 1,848), haciendo vinculante el mecanismo técnico del Consejo Nacional de Trabajo.",
    "Dado que la canasta básica familiar equivale a S/ 1848, aumentaremos la remuneración mínima vital progresivamente a S/ 1500",
    f"{S44} — Medidas Propuestas", 203, 203,
    meta="RMV progresiva a S/ 1,500 (canasta básica S/ 1,848)",
))

nuevas.append(mk(
    "r-trabajo-009", "trabajo", "meta", "ALTA",
    "Meta de empleo: generar 1 millón de nuevos empleos formales con derechos laborales plenos mediante la reactivación económica y el fomento de la inversión privada.",
    "A través de la reactivación económica y el fomento de la inversión privada generaremos 1 millón de nuevos empleos formales, con derechos laborales plenos",
    f"{S44} — Medidas Propuestas", 203, 203,
    meta="1 millón empleos formales nuevos",
))

nuevas.append(mk(
    "r-trabajo-010", "trabajo", "meta", "ALTA",
    "Meta: duplicar el presupuesto del programa Trabaja Perú (Llamkasun) del MTPE para generar 400 mil empleos temporales para los más vulnerables (sobre todo mujeres), a nivel urbano y rural.",
    "Duplicaremos el presupuesto del programa Trabaja Perú (Llamkasun) del MTPE para generar 400 mil empleos temporales para los más vulnerables (sobre todo mujeres)",
    f"{S44} — Medidas Propuestas", 203, 203,
    meta="400 mil empleos temporales; duplicar Trabaja Perú",
))

nuevas.append(mk(
    "r-trabajo-011", "trabajo", "propuesta", "MEDIA",
    "Aplicar un subsidio temporal escalonado a los aportes a la seguridad social en salud y pensiones para incentivar la contratación formal y estable en MYPEs, sobre todo de jóvenes y mujeres.",
    "Aplicaremos un subsidio temporal escalonado a los aportes a la seguridad social en salud y pensiones, para incentivar la contratación formal y estable en MYPEs",
    f"{S44} — Medidas Propuestas", 203, 203,
))

nuevas.append(mk(
    "r-trabajo-012", "trabajo", "propuesta", "ALTA",
    "Nueva ley agraria que equipare derechos laborales y de seguridad social de trabajadores agrarios con el régimen general, fomente negociación colectiva supraempresarial y reduzca beneficios tributarios a agroexportación.",
    "Propondremos una nueva ley agraria que equipare derechos laborales y de seguridad social de los trabajadores agrarios con los del régimen general",
    f"{S44} — Medidas Propuestas", 203, 203,
))

nuevas.append(mk(
    "r-trabajo-013", "trabajo", "propuesta", "MEDIA",
    "Aprobar una nueva Política Nacional de Empleo promotora del empleo de calidad mediante políticas activas (incentivo a demanda y oferta) y pasivas (protección de contingencias vejez, desempleo y salud).",
    "Aprobaremos una nueva Política Nacional de Empleo que sea promotora del empleo de calidad",
    f"{S44} — Medidas Propuestas", 203, 203,
))

nuevas.append(mk(
    "r-trabajo-014", "trabajo", "propuesta", "MEDIA",
    "Constituir la Comisión Intersectorial e Intergubernamental del Autoempleo para proponer políticas de desarrollo, acceso a derechos y formalización del autoempleo productivo.",
    "Constituiremos la Comisión Intersectorial e Intergubernamental del Autoempleo, con la finalidad de proponer políticas para el desarrollo, acceso a derechos y formalización del autoempleo productivo",
    f"{S44} — Medidas Propuestas", 203, 203,
))

nuevas.append(mk(
    "r-trabajo-015", "trabajo", "propuesta", "ALTA",
    "Reforma laboral integral que promueva el empleo formal, estable, productivo y con mayores ingresos; así como la sindicalización y negociación colectiva.",
    "Propondremos una reforma laboral integral que promueva el empleo formal, estable, productivo y con mayores ingresos",
    f"{S44} — Medidas Propuestas", 203, 203,
))

nuevas.append(mk(
    "r-trabajo-016", "trabajo", "propuesta", "MEDIA",
    "Reestructurar EsSalud con dirección más transparente y democrática; nivelar a 9% la tasa de aporte en todos los sectores y uniformizar la base contributiva.",
    "Reestructuraremos EsSalud para una gestión más eficiente, lo cual requiere una dirección más transparente y democrática (que la presidencia ejecutiva rote entre los sectores que integran el Consejo Directivo), nivelar a 9% la tasa de aporte en todos los sectores",
    f"{S44} — Medidas Propuestas", 203, 203,
    meta="EsSalud: tasa aporte 9% uniforme",
))

nuevas.append(mk(
    "r-trabajo-017", "trabajo", "propuesta", "ALTA",
    "Implementar un seguro de desempleo para proteger a los trabajadores frente a la pérdida de empleo.",
    "Implementaremos un seguro de desempleo",
    f"{S44} — Medidas Propuestas", 203, 203,
))

nuevas.append(mk(
    "r-trabajo-018", "trabajo", "propuesta", "MEDIA",
    "Crear el Consejo Nacional del Empleo Público para discutir políticas del servicio civil entre trabajadores y empleadores; incluir la fiscalización del cumplimiento laboral en el Estado entre las competencias de SUNAFIL.",
    "crearemos el Consejo Nacional del Empleo Público, donde se discutan las principales políticas del servicio civil entre representantes de los trabajadores y los empleadores",
    f"{S44} — Medidas Propuestas", 205, 205,
))

# =====================================================================
# 4.5 EMPRENDIMIENTO (líneas 205-209) — tema: mype
# =====================================================================
S45 = "Dimensión Económica — 4.5 Emprendimiento"

nuevas.append(mk(
    "r-mype-001", "mype", "diagnostico", "ALTA",
    "Diagnóstico estructural: más del 99% de las empresas peruanas son micro, pequeñas o medianas y generan ~48% del empleo, pero solo aportan 16% del PBI; cerca del 86% opera en la informalidad.",
    "Más del 99% de las empresas son micro, pequeñas o medianas y generan alrededor del 48 % del empleo, pero solo aportan cerca del 16 % del PBI, con una productividad ínfima frente a las grandes firmas. Al mismo tiempo, la gran mayoría de estas unidades opera en la informalidad: alrededor del 86%",
    f"{S45} — Situación Actual", 205, 205,
))

nuevas.append(mk(
    "r-mype-002", "mype", "diagnostico", "ALTA",
    "Diagnóstico de productividad: la microempresa peruana es en promedio 50 veces menos productiva que la gran empresa, dado que la mayoría son negocios de autoempleo en sectores de bajo valor agregado.",
    "La microempresa peruana es, en promedio, 50 veces menos productiva que la gran empresa. Esto se debe a que la mayoría son negocios de \"autoempleo\" en sectores de bajo valor agregado",
    f"{S45} — Situación Actual", 205, 205,
))

nuevas.append(mk(
    "r-mype-003", "mype", "diagnostico", "MEDIA",
    "Diagnóstico de pequeña agricultura: productores envejecidos, más de la mitad solo con primaria, capacitación 6.6%, asistencia técnica 3.8% y 93% fuera de cualquier organización económica.",
    "En la pequeña agricultura, la ENA 2022 muestra productores envejecidos, con bajo nivel educativo (más de la mitad solo primaria), muy baja cobertura de capacitación (≈6,6 %) y asistencia técnica (≈3,8 %)",
    f"{S45} — Situación Actual", 205, 205,
))

nuevas.append(mk(
    "r-mype-004", "mype", "diagnostico", "MEDIA",
    "Diagnóstico de financiamiento: alrededor del 90.9% de productores agrícolas no busca crédito; solo un tercio tiene título y proporción menor inscrita en registros públicos limitando el uso como garantía.",
    "alrededor del 90,9 % de productores no busca crédito y solo una fracción de quienes lo solicitan lo obtiene; aunque el 76 % se considera propietario de al menos una parcela, solo cerca de un tercio tendría título",
    f"{S45} — Situación Actual", 205, 205,
))

nuevas.append(mk(
    "r-mype-005", "mype", "diagnostico", "MEDIA",
    "Diagnóstico tributario: coexisten cuatro regímenes (NRUS, RER, RMT y régimen general) más regímenes laborales especiales, induciendo a las empresas a dividirse o mantenerse pequeñas para no perder beneficios.",
    "Existen cuatro regímenes tributarios (NRUS, RER, RMT y régimen general) y varios regímenes laborales especiales (Mype, agrario, entre otros), cada uno con sus propias reglas, libros y costos",
    f"{S45} — Situación Actual", 207, 207,
))

nuevas.append(mk(
    "r-mype-006", "mype", "meta", "ALTA",
    "Meta de formalidad: reducir la informalidad de 70.7% a 55% (trayectoria -1.5 a -4 puntos anuales); al menos 60 mil micro y pequeñas empresas integradas a la nueva formalidad mediante un programa de nueva formalidad productiva.",
    "Programa de nueva formalidad productiva que simplifique las condiciones de funcionamiento legal para formales e informales y permita la formalización masiva de las actividades económica. Ello permitirá reducir la informalidad cuando menos del 70.7% al 55%",
    f"{S45} — Medidas Propuestas", 207, 207,
    meta="Informalidad 70.7%→55%; 60 mil micro/pequeñas empresas formalizadas",
))

nuevas.append(mk(
    "r-mype-007", "mype", "propuesta", "MEDIA",
    "Programa especial de fortalecimiento de la micro, pequeña y mediana empresa formal e informal, con línea especial de crédito gestionada por el Banco de la Nación y COFIDE.",
    "Programa especial de fortalecimiento de la micro, pequeña y mediana empresa, formal e informal, para incrementar la productividad, el valor, agregado, la escala y la calidad de sus productos",
    f"{S45} — Medidas Propuestas", 207, 207,
))

nuevas.append(mk(
    "r-mype-008", "mype", "propuesta", "MEDIA",
    "Programa especial de fortalecimiento de las capacidades productivas y formas empresariales de las comunidades originarias, cooperativas y otras formas asociativas.",
    "Programa especial de fortalecimiento de las capacidades productivas y formas empresariales de las comunidades originarias, cooperativas y otras formas asociativas",
    f"{S45} — Medidas Propuestas", 207, 207,
))

nuevas.append(mk(
    "r-mype-009", "mype", "propuesta", "MEDIA",
    "Impulsar el uso masivo de la Billetera Digital MIPYME entre comerciantes y pequeños negocios informales, para superar la barrera del historial crediticio tradicional.",
    "Impulsaremos el uso masivo de la Billetera Digital MIPYME entre comerciantes y pequeños negocios informales, el cual representaría una oportunidad única para superar la barrera del historial crediticio tradicional",
    f"{S45} — Medidas Propuestas", 207, 207,
))

nuevas.append(mk(
    "r-mype-010", "mype", "propuesta", "ALTA",
    "Régimen tributario único MIPYME: articular NRUS, RER y RMT en un solo régimen escalonado con una sola declaración y un solo pago mensual (modelo 'impuesto único sobre ventas + contribuciones sociales').",
    "Articular NRUS, RER y RMT en un solo régimen escalonado para MIPYME, con una sola declaración y un solo pago mensual (modelo “impuesto único sobre ventas + contribuciones sociales”)",
    f"{S45} — Medidas Propuestas", 207, 207,
))

nuevas.append(mk(
    "r-mype-011", "mype", "propuesta", "MEDIA",
    "Shock desregulatorio y Burocracia Cero: reforma regulatoria para eliminar duplicidad de funciones entre niveles de gobierno y simplificar drásticamente registro, licenciamiento y permisos.",
    "Shock Desregulatorio y Burocracia Cero: Lideraremos una reforma regulatoria para eliminar la duplicidad de funciones entre niveles de gobierno y simplificar drásticamente los procedimientos de registro, licenciamiento y permisos",
    f"{S45} — Medidas Propuestas", 209, 209,
))

nuevas.append(mk(
    "r-mype-012", "mype", "propuesta", "MEDIA",
    "Fortalecer la asociatividad empresarial mediante asociaciones, cooperativas, consorcios y redes empresariales con asistencia legal, técnica e incentivos económicos.",
    "Fortaleceremos la asociatividad empresarial, promoviendo asociaciones, cooperativas, consorcio y redes empresariales con asistencia legal, técnica e Incentivos económicos",
    f"{S45} — Medidas Propuestas", 209, 209,
))

nuevas.append(mk(
    "r-mype-013", "mype", "propuesta", "MEDIA",
    "Programa Nacional de Cadenas Productivas articulado por sectores estratégicos, integrando MIPYME con compras públicas y proyectos de inversión pública y privada.",
    "“Programa Nacional de Cadenas Productivas”, articulado por sectores estratégicos, integrando a las MIPYME articulándolos con compras públicas y proyectos de inversión pública y privada",
    f"{S45} — Medidas Propuestas", 209, 209,
))

nuevas.append(mk(
    "r-mype-014", "mype", "meta", "ALTA",
    "Empoderamiento económico de mujeres rurales: aumentar a S/ 40 millones anuales la Estrategia de Emprendimiento de la Mujer Rural; garantizar copropiedad efectiva (50% títulos a mujeres) y paridad en juntas de agua y consejos agrarios.",
    "Empoderamiento Económico de Mujeres Rurales. Aumentaremos los fondos a S/ 40 millones anuales para la Estrategia de Emprendimiento de la Mujer Rural e indígena, con acceso preferencial a créditos",
    f"{S45} — Medidas Propuestas", 209, 209,
    meta="S/ 40 millones anuales mujer rural; 50% copropiedad de títulos",
))

nuevas.append(mk(
    "r-mype-015", "mype", "propuesta", "MEDIA",
    "Red de laboratorios MIPYME en CTDE, universidades y CITES para prototipado, diseño de productos, adopción de comercio electrónico y herramientas de gestión digital con énfasis en jóvenes y mujeres.",
    "Red de laboratorios (en CTDE, universidades, CITES) donde MIPYME acceden a servicios de prototipado, diseño de productos, adopción de comercio electrónico, herramientas de gestión digital y modelos de negocio innovadores",
    f"{S45} — Medidas Propuestas", 209, 209,
))

nuevas.append(mk(
    "r-mype-016", "mype", "propuesta", "MEDIA",
    "Implementar una ventanilla única digital interoperable que articule SUNAT, SUNARP, municipalidades, MTPE, EsSalud, ONP/AFP y REINFO para facilitar todo el ciclo de vida de la empresa.",
    "Implementar una ventanilla única digital e interoperable: Articular SUNAT, SUNARP, municipalidades, MTPE, EsSalud, ONP/AFP, REINFO para facilitar todo el ciclo de vida de la empresa",
    f"{S45} — Medidas Propuestas", 209, 209,
))

nuevas.append(mk(
    "r-mype-017", "mype", "propuesta", "BAJA",
    "Promover el emprendimiento juvenil con capital semilla, capacitación y acompañamiento técnico.",
    "Promoveremos el emprendimiento juvenil con capital semilla, capacitación y acompañamiento técnico",
    f"{S45} — Medidas Propuestas", 209, 209,
))

# =====================================================================
# 4.6 MERCADOS POPULARES Y CONSUMIDOR (líneas 211-215) — tema: economia (protección al consumidor)
# =====================================================================
S46 = "Dimensión Económica — 4.6 Mercados Populares y Protección al Consumidor"

nuevas.append(mk(
    "r-economia-021", "economia", "diagnostico", "MEDIA",
    "Diagnóstico de abuso de mercado: prácticas comerciales que corrompen el libre mercado (precios monopólicos, ofertas engañosas, créditos exorbitantes) en sistema financiero, aerolíneas, transporte y cadenas comerciales.",
    "se han expandido prácticas comerciales que corrompen la idea de un libre mercado que marche en armonía con los derechos de los consumidores. Precios monopólicos, condiciones exorbitantes en créditos, ofertas engañosas",
    f"{S46} — Situación Actual", 213, 213,
))

nuevas.append(mk(
    "r-economia-022", "economia", "diagnostico", "MEDIA",
    "Diagnóstico de tasas crediticias: las tasas promedio para microempresa superan el 55% anual en determinados segmentos del sistema financiero, atrapando a miles de pequeños productores en esquemas profundamente desiguales.",
    "Según información publicada por la SBS en 2026, las tasas promedio para microempresa superan el 55 % anual en determinados segmentos del sistema financiero",
    f"{S46} — Situación Actual", 213, 213,
    meta="Tasas microempresa >55% anual (SBS 2026)",
))

nuevas.append(mk(
    "r-economia-023", "economia", "propuesta", "MEDIA",
    "Plan de fortalecimiento de mercados de abasto, ferias barriales y comercio ambulante organizado con acceso a crédito, legalización ordenada de espacios públicos, infraestructura adecuada y apoyo para formalización.",
    "Se creará un plan de fortalecimiento de mercados de abasto, ferias barriales y comercio ambulante organizado, con acceso a crédito, legalización ordenada de espacios públicos, infraestructura adecuada",
    f"{S46} — Medidas Propuestas", 215, 215,
))

nuevas.append(mk(
    "r-economia-024", "economia", "propuesta", "ALTA",
    "Fortalecer INDECOPI como entidad de control firme de prácticas abusivas de mercado, con capacidad para fiscalizar supermercados, farmacias y empresas de servicios básicos.",
    "Se fortalecerá INDECOPI como entidad de control firme de las prácticas abusivas de mercado, con capacidad para fiscalizar supermercados, farmacias y empresas de servicios básicos",
    f"{S46} — Medidas Propuestas", 215, 215,
))

nuevas.append(mk(
    "r-economia-025", "economia", "propuesta", "ALTA",
    "Crear el Observatorio Nacional de Precios Justos para transparentar información, detectar prácticas concertadas y alertar márgenes abusivos en mercados altamente concentrados.",
    "Se creará el Observatorio Nacional de Precios Justos para transparentar información, detectar prácticas concertadas, alertar márgenes abusivos y fortalecer mecanismos de defensa económica",
    f"{S46} — Medidas Propuestas", 215, 215,
))

nuevas.append(mk(
    "r-economia-026", "economia", "propuesta", "MEDIA",
    "Regular el sistema de tarjetas de crédito para el control de intereses abusivos y cláusulas que sumergen a las familias en deudas interminables.",
    "Regular el sistema de tarjetas de crédito para el control de intereses abusivos y cláusulas que sumen a las familias en deudas interminables",
    f"{S46} — Medidas Propuestas", 215, 215,
))

# =====================================================================
# 4.7 CIENCIA, TECNOLOGÍA E INNOVACIÓN (líneas 215-221) — tema: cti
# =====================================================================
S47 = "Dimensión Económica — 4.7 Ciencia, Tecnología e Innovación"

nuevas.append(mk(
    "r-cti-001", "cti", "diagnostico", "ALTA",
    "Diagnóstico de I+D: el Perú destina apenas 0.16% del PBI a investigación y desarrollo, una de las cifras más bajas de América Latina; han proliferado los incentivos para el mercadeo académico y la titulocracia.",
    "El Perú destina apenas entre 0.16% del PBI a investigación y desarrollo, una de las cifras más bajas de América Latina, muy lejos de países que transforman su economía con ciencia y tecnología",
    f"{S47} — Situación Actual", 217, 217,
    meta="I+D 0.16% del PBI",
))

nuevas.append(mk(
    "r-cti-002", "cti", "diagnostico", "MEDIA",
    "Diagnóstico institucional: CONCYTEC y el Sistema Nacional de Ciencia, Tecnología e Innovación necesitan dejar de funcionar únicamente como espacios de administración de fondos dispersos y producción académica desconectada de prioridades nacionales.",
    "CONCYTEC y el Sistema Nacional de Ciencia, Tecnología e Innovación",
    f"{S47} — Situación Actual", 217, 217,
))

nuevas.append(mk(
    "r-cti-003", "cti", "propuesta", "ALTA",
    "Crear el Ministerio de Ciencia y Tecnología orientado a las metas del plan de transformación productiva, vinculado a institutos técnicos regionales, ZEE en Ilo/Matarani/Chancay, fondo de innovación y alianzas universidad-empresa.",
    "Crear el Ministerio de Ciencia y Tecnología para el Fomento de la innovación tecnológica, directamente orientado a las metas al plan de transformación nacional",
    f"{S47} — Medidas Propuestas", 221, 221,
))

nuevas.append(mk(
    "r-cti-004", "cti", "propuesta", "MEDIA",
    "Shock de inversiones en tecnología para un gobierno digital y moderno para todos, liderado por el Ministerio de Ciencia y Tecnología.",
    "Shock de inversiones en tecnología para un gobierno digital y moderno para todos, liderada por el Ministerio de Ciencia y Tecnología",
    f"{S47} — Medidas Propuestas", 221, 221,
))

nuevas.append(mk(
    "r-cti-005", "cti", "propuesta", "MEDIA",
    "Los CITEs actuarán como laboratorios de punta para que las MIPYME adopten estándares internacionales de calidad; se cofinanciarán misiones tecnológicas y pasantías en el exterior para empresas con alto potencial exportador.",
    "Los Centros de Innovación Productiva y Transferencia Tecnológica (CITEs) actuarán como laboratorios de punta para que las Mipymes adopten estándares internacionales de calidad",
    f"{S47} — Medidas Propuestas", 221, 221,
))

nuevas.append(mk(
    "r-cti-006", "cti", "propuesta", "MEDIA",
    "Fortalecer INACAL para que los productos peruanos cumplan normas técnicas internacionales; una certificación de calidad puede incrementar el valor agregado del producto hasta en 66%.",
    "Fortalecer INACAL para que los productos peruanos cumplan normas técnicas internacionales, facilitando su inserción en cadenas globales de valor. Una certificación de calidad puede incrementar el valor agregado del producto hasta en un 66%",
    f"{S47} — Medidas Propuestas", 221, 221,
    meta="Certificación de calidad: +66% valor agregado del producto",
))

nuevas.append(mk(
    "r-cti-007", "cti", "propuesta", "MEDIA",
    "Culminar el Parque Industrial de Ancón (1,300 hectáreas) como plataforma para manufactura avanzada y agroexportación de valor agregado.",
    "Culminar el Parque Industrial de Ancón (1,300 hectáreas): plataforma para manufactura avanzada y agroexportación de valor agregado",
    f"{S47} — Medidas Propuestas", 221, 221,
    meta="Parque Industrial Ancón: 1,300 hectáreas",
))

nuevas.append(mk(
    "r-cti-008", "cti", "propuesta", "MEDIA",
    "Posicionar el Puerto de Chancay como nodo regional y hub para industrialización, no solo punto de extracción.",
    "Puerto de Chancay como nodo regional: no solo punto de extracción, sino hub para industrialización",
    f"{S47} — Medidas Propuestas", 221, 221,
))

nuevas.append(mk(
    "r-cti-009", "cti", "propuesta", "MEDIA",
    "Atraer inversiones en tecnología para las regiones exigiendo 100% trabajo local a cambio de beneficios tributarios.",
    "Atraeremos inversiones en tecnología para nuestras regiones exigiendo 100% trabajo local a cambio de beneficios tributarios",
    f"{S47} — Medidas Propuestas", 221, 221,
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
