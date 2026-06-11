# -*- coding: utf-8 -*-
"""Extracción de declaraciones del Debate 2 (equipos técnicos).

Seis bloques temáticos, cada uno con voceros de Fuerza Popular (FP) y
Juntos por el Perú (JxP). Cada declaración se atribuye al candidato
(keiko o roberto) y registra el vocero específico que la pronunció.

Voceros por bloque:
- Reforma del Estado: Sinesio López (JxP) / Vladimiro Huaroc (FP)
- Juventud y Deporte: Ernesto Zunini Yerrén (JxP) / Rosángela Barbarán (FP)
- Agricultura y ambiente: César Guarniz Vigo (JxP) / Marco Vineli Ruiz (FP)
- Infraestructura: Gustavo Guerra García (JxP) / Carlos Neuhaus (FP)
- Economía y empleo: Pedro Francke (JxP) / Luis Carranza (FP)
- Salud: Hernando Ceballos (JxP) / José Recoba (FP)
"""
import json
from pathlib import Path

ARCHIVO_FUENTE = "02-Debates/raw/Debate 2.txt"
DEBATE_ID = "debate-2"


def mk(id_, candidato, tema, tipo, texto, cita, contexto, linea_ini, linea_fin, vocero, timestamp=None):
    return {
        "id": id_,
        "debate_id": DEBATE_ID,
        "candidato": candidato,
        "vocero": vocero,
        "tema": tema,
        "tipo": tipo,
        "texto": texto,
        "cita_textual": cita,
        "contexto": contexto,
        "fuente": {
            "archivo": ARCHIVO_FUENTE,
            "linea_inicio": linea_ini,
            "linea_fin": linea_fin,
        },
        "timestamp": timestamp,
    }


nuevas = []

# =====================================================================
# BLOQUE 1: REFORMA DEL ESTADO (L117-682)
# JxP: Sinesio López Jiménez | FP: Vladimiro Huaroc Portocarrero
# =====================================================================
CTX_B1 = "Bloque 1 — Reforma del Estado"
LOPEZ = "Sinesio López Jiménez"
HUAROC = "Vladimiro Huaroc Portocarrero"

nuevas.append(mk(
    "debate-2-r-001", "roberto", "constitucion", "diagnostico",
    "Desde 2016 el Perú vive un régimen parlamentarista de facto, no presidencialista; hemos tenido 8 presidentes en 10 años (6 elegidos por el Parlamento y 2 por el pueblo).",
    "desde 2016 para acá vivimos un régimen parlamentarista y no un régimen presidencialista",
    CTX_B1, 162, 172, vocero=LOPEZ, timestamp="28:21",
))
nuevas.append(mk(
    "debate-2-r-002", "roberto", "constitucion", "ataque",
    "El Congreso ha concentrado todos los poderes del Estado (ejecutivo, legislativo, fiscalía) y los organismos de control son sus apéndices; ya no es un régimen autoritario sino una dictadura parlamentaria.",
    "el Congreso ha concentrado todos los poderes del Estado",
    CTX_B1, 173, 184, vocero=LOPEZ, timestamp="29:03",
))
nuevas.append(mk(
    "debate-2-r-003", "roberto", "economia", "diagnostico",
    "El Estado tiene muchas funciones y pocas capacidades porque tiene pocos recursos: presión tributaria de 14% vs. media latinoamericana de 22%.",
    "La presión tributaria es 14% y no digamos la media latinoamericana es básicamente eh 22",
    CTX_B1, 209, 212, vocero=LOPEZ, timestamp="30:45",
))
nuevas.append(mk(
    "debate-2-k-001", "keiko", "economia", "diagnostico",
    "Caracteriza el caos como ineficiencia del Estado: trámite eterno, obra paralizada, inversión que se detiene, oportunidad perdida y estado que no coordina.",
    "el caos es un trámite eterno, es una obra paralizada, una inversión que se detiene",
    CTX_B1, 255, 259, vocero=HUAROC, timestamp="32:43",
))
nuevas.append(mk(
    "debate-2-k-002", "keiko", "constitucion", "propuesta",
    "Reforma moderna del Estado no para crear más oficinas ni burocracia, sino para que el Estado funcione y resuelva problemas concretos; convertir la Presidencia en un Centro de Gobierno estratégico.",
    "convertir a la presidencia de la República en un verdadero centro de gobierno estratégico",
    CTX_B1, 284, 287, vocero=HUAROC, timestamp="34:04",
))
nuevas.append(mk(
    "debate-2-r-004", "roberto", "corrupcion", "diagnostico",
    "Lo más preocupante no es la corrupción sino la impunidad: el 50% de parlamentarios han sido acusados de algún delito, y han dictado leyes pro-crimen que en lugar de combatir la corrupción la refuerzan.",
    "El 50% de los parlamentarios han sido acusados de algún tipo de delito",
    CTX_B1, 358, 364, vocero=LOPEZ, timestamp="37:00",
))
nuevas.append(mk(
    "debate-2-r-005", "roberto", "constitucion", "propuesta",
    "Los organismos autónomos (JNJ, TC, Defensoría del Pueblo) deben ser autónomos y no apéndices del poder parlamentario; sin esto no es posible combatir la corrupción.",
    "aquellos organismos autónomos que tienen la función de de controlar el Estado, de controlar la corrupción, debieran ser autónomos y no apéndice del poder parlamentario",
    CTX_B1, 410, 420, vocero=LOPEZ, timestamp="39:14",
))
nuevas.append(mk(
    "debate-2-k-003", "keiko", "constitucion", "propuesta",
    "Centro de gestión estratégica dentro del Ejecutivo que articule las instituciones públicas en todos los niveles; repensar la descentralización.",
    "necesitamos absolutamente un centro de gestión estratégica dentro del ejecutivo, que pueda articular las instituciones públicas a todos los niveles",
    CTX_B1, 387, 404, vocero=HUAROC, timestamp="38:25",
))
nuevas.append(mk(
    "debate-2-k-004", "keiko", "constitucion", "propuesta",
    "Digitalización de la función pública en los tres niveles: ministerios, regiones y municipios interconectados como propuesta central de la modernización del Estado.",
    "Fuerza Popular en su programa de gobierno ha presentado la modernización del Estado y uno de los ejes fundamentales es la digitalización de la función pública a sus tres niveles",
    CTX_B1, 466, 475, vocero=HUAROC, timestamp="41:58",
))
nuevas.append(mk(
    "debate-2-r-006", "roberto", "constitucion", "diagnostico",
    "El Estado está desigualmente distribuido en el territorio: concentrado en la costa, débil o inexistente en sierra y selva; no genera un 'nosotros' en la población.",
    "El estado está desigualmente distribuido en el territorio. Si uno mira el mapa del estado, tenemos estado fundamentalmente en la costa",
    CTX_B1, 442, 449, vocero=LOPEZ, timestamp="40:51",
))
nuevas.append(mk(
    "debate-2-r-007", "roberto", "constitucion", "diagnostico",
    "El Estado debiera producir bienes públicos de calidad para todos (educación, salud, seguridad y justicia iguales para todos) y eso no se da.",
    "todos debiéramos tener posibilidad de de gozar de la educación pública de calidad, la salud pública de calidad, de seguridad, de justicia, igual para todos",
    CTX_B1, 457, 461, vocero=LOPEZ, timestamp="41:38",
))
nuevas.append(mk(
    "debate-2-r-008", "roberto", "constitucion", "diagnostico",
    "Evaluamos al Estado por procedimientos legales y no por resultados; en 10 años hemos tenido 8 presidentes y gabinetes que duran apenas meses sin tiempo para producir resultados.",
    "generalmente la evaluación que se hace del Estado se hace por procedimientos legales y no por resultados",
    CTX_B1, 526, 540, vocero=LOPEZ, timestamp="44:15",
))

# =====================================================================
# BLOQUE 2: JUVENTUD Y DEPORTE (L683-1361)
# JxP: Ernesto Zunini Yerrén | FP: Rosángela Barbarán
# =====================================================================
CTX_B2 = "Bloque 2 — Juventud y Deporte"
ZUNINI = "Ernesto Alonso Zunini Yerrén"
BARBARAN = "Rosángela Andrea Barbarán Reyes"

nuevas.append(mk(
    "debate-2-k-005", "keiko", "juventud", "diagnostico",
    "Los jóvenes representan el 30% del país y son la población más golpeada; más de 1 millón de ninis y miles abandonan estudios por no poder pagar.",
    "Representamos el 30% del país y somos la población más golpeada",
    CTX_B2, 701, 713, vocero=BARBARAN, timestamp="52:34",
))
nuevas.append(mk(
    "debate-2-k-006", "keiko", "juventud", "propuesta",
    "Modernización total de la educación técnica para mejorar infraestructura, tecnología y adaptar la malla curricular a las regiones y a la demanda laboral; ampliar becas.",
    "proponemos la modernización total de la educación técnica para mejorar la infraestructura, tecnología, adaptar la malla curricular",
    CTX_B2, 721, 726, vocero=BARBARAN, timestamp="53:29",
))
nuevas.append(mk(
    "debate-2-k-007", "keiko", "juventud", "propuesta",
    "Repotenciar Jóvenes Productivos con nuevas capacitaciones y alianzas con empresas; capital semilla y impuesto cero los tres primeros años para emprendedores jóvenes.",
    "repotenciaremos el programa Jóvenes Productivos, ampliando nuevas capacitaciones",
    CTX_B2, 728, 736, vocero=BARBARAN, timestamp="53:45",
))
nuevas.append(mk(
    "debate-2-k-008", "keiko", "deporte", "propuesta",
    "El IPD pasará a manos de la PCM para invertir en deporte en todos sus niveles (recreativo, escolar y profesional) y alejar a los jóvenes de la delincuencia y las drogas.",
    "el IPD pasará a manos de la PCM. Desde ahí vamos a invertir en el deporte en todos sus niveles",
    CTX_B2, 739, 746, vocero=BARBARAN, timestamp="54:13",
))
nuevas.append(mk(
    "debate-2-r-009", "roberto", "juventud", "diagnostico",
    "El modelo fujimorista mantiene a más de 1.6 millones de jóvenes sin oportunidades para estudiar o trabajar.",
    "se mantiene a más de 1,6 millones de nuestros jóvenes sin oportunidades para estudiar o trabajar",
    CTX_B2, 777, 783, vocero=ZUNINI, timestamp="55:48",
))
nuevas.append(mk(
    "debate-2-r-010", "roberto", "juventud", "propuesta",
    "Programa Mi Primera Chamba: 100,000 jóvenes recibirán S/ 6,150 en una cuenta del Banco de la Nación para capacitación, capital semilla o subvención de 6 meses de salario en su primer empleo formal.",
    "Para ellos va el programa Mi primera Champa. 100,000 jóvenes recibirán 6,150 soles en una cuenta individual del Banco de la Nación",
    CTX_B2, 790, 801, vocero=ZUNINI, timestamp="56:22",
))
nuevas.append(mk(
    "debate-2-r-011", "roberto", "educacion", "propuesta",
    "Reconocer la educación superior y la formación permanente como derecho constitucional; el examen de admisión no será excusa para excluir a los que menos tienen.",
    "vamos a reconocer la educación superior y la formación permanente como un derecho constitucional",
    CTX_B2, 808, 815, vocero=ZUNINI, timestamp="56:59",
))
nuevas.append(mk(
    "debate-2-r-012", "roberto", "educacion", "compromiso",
    "Ampliar las becas del Estado a 30,000, enfocadas en jóvenes en pobreza de zonas urbanomarginales, comunidades originarias, campesinas, zonas rurales y afrodescendientes.",
    "ampliaremos las becas del Estado a 30,000",
    CTX_B2, 816, 823, vocero=ZUNINI, timestamp="57:14",
))
nuevas.append(mk(
    "debate-2-r-013", "roberto", "deporte", "compromiso",
    "Lima 2027 será el evento más importante y mejor organizado de la historia del país, sostenido por Casa Futuro: polideportivos con bibliotecas y centros de recursos tecnológicos.",
    "Lima 202 será por Juntos por el Perú el evento más importante y mejor organizado de la historia de nuestro país",
    CTX_B2, 833, 855, vocero=ZUNINI, timestamp="57:46",
))
nuevas.append(mk(
    "debate-2-r-014", "roberto", "salud", "propuesta",
    "Un psicólogo por escuela (iniciativa parlamentaria de Roberto Sánchez); apostar por la salud psicológica de la juventud con asistencia en Casa Futuro.",
    "nuestro presidente Roberto Sánchez ha apostado desde el parlamento para facilitar la disposición de un psicólogo por escuela",
    CTX_B2, 1007, 1019, vocero=ZUNINI, timestamp="63:52",
))
nuevas.append(mk(
    "debate-2-k-009", "keiko", "juventud", "propuesta",
    "Centros de Oportunidades y Orientación Local (COL) en todas las regiones: cursos, talleres, orientación vocacional, becas, bolsas de trabajo y atención psicológica 24/7.",
    "vamos a crear los centros y oportunidades y orientación local en todas las regiones del país, los cool",
    CTX_B2, 962, 970, vocero=BARBARAN, timestamp="62:09",
))
nuevas.append(mk(
    "debate-2-k-010", "keiko", "juventud", "compromiso",
    "Fuerza Popular impulsó normas para que las prácticas pre-profesionales y profesionales sean experiencia laboral y que el voluntariado pueda contar como créditos académicos.",
    "se han impulsado las principales normas para los jóvenes. que las prácticas preprofesionales y profesionales sean consideradas experiencia laboral",
    CTX_B2, 1086, 1093, vocero=BARBARAN, timestamp="66:38",
))
nuevas.append(mk(
    "debate-2-k-011", "keiko", "deporte", "propuesta",
    "Incluir al deporte en la Ley de Obras por Impuestos para que las regiones obtengan inversión en infraestructura deportiva competitiva y promover el desarrollo del talento nacional.",
    "actualmente tenemos la ley de obras por impuestos y esto no incluye a los deportes, privando a que las regiones puedan obtener inversión",
    CTX_B2, 1220, 1227, vocero=BARBARAN, timestamp="71:27",
))
nuevas.append(mk(
    "debate-2-r-015", "roberto", "juventud", "propuesta",
    "Programa Ayni de voluntariado juvenil: 45,000 jóvenes podrán participar en mantenimiento de caminos vecinales y mejoras de barrios que abonará a su experiencia laboral.",
    "le propondemos el programa Aini para que cuanto 45,000 jóvenes puedan participar en acciones menores de mantenimiento de caminos decenales",
    CTX_B2, 1106, 1113, vocero=ZUNINI, timestamp="67:23",
))

# =====================================================================
# BLOQUE 3: AGRICULTURA Y AMBIENTE (L1362-1986)
# JxP: César Guarniz Vigo | FP: Marco Vineli Ruiz
# =====================================================================
CTX_B3 = "Bloque 3 — Agricultura y medio ambiente"
GUARNIZ = "César Milton Guarniz Vigo"
VINELI = "Marco Antonio Vineli Ruiz"

nuevas.append(mk(
    "debate-2-r-016", "roberto", "agricultura", "diagnostico",
    "Dos caras de la moneda en el agro: agroexportador con beneficios tributarios (Ley Climper aprobada por Fuerza Popular) y agricultura familiar abandonada sin créditos y con precios bajos.",
    "Tenemos dos caras de la moneda. De un lado, el sector agroexportador que tiene todas las políticas públicas de su lado",
    CTX_B3, 1383, 1396, vocero=GUARNIZ, timestamp="79:12",
))
nuevas.append(mk(
    "debate-2-r-017", "roberto", "agua", "propuesta",
    "Soberanía hídrica con un Programa Nacional / Fondo Nacional del Agua trabajando con las organizaciones de usuarios de agua y núcleos ejecutores.",
    "vamos a plantear agua, soberanía hídrica, seguridad hídrica. Para eso el tema de una construcción de un programa nacional de un fondo nacional",
    CTX_B3, 1401, 1410, vocero=GUARNIZ, timestamp="80:00",
))
nuevas.append(mk(
    "debate-2-r-018", "roberto", "agricultura", "compromiso",
    "Construir un Banco de Desarrollo Agropecuario con cobertura de impacto a 1 millón de productores agrarios en los primeros 100 días de gobierno.",
    "un banco de desarrollo agropecuario con una cobertura importante de impacto a 1 millón de productores agrarios en los primeros 100 días de gobierno",
    CTX_B3, 1419, 1427, vocero=GUARNIZ, timestamp="80:42",
))
nuevas.append(mk(
    "debate-2-r-019", "roberto", "industria", "propuesta",
    "Industrializar insumos: planta de urea y fosfatos de Bayóvar; centros de acopio y de transformación para los pequeños productores.",
    "Hay que ver la planta de uia y los fosfatos de Bobar",
    CTX_B3, 1437, 1441, vocero=GUARNIZ, timestamp="81:23",
))
nuevas.append(mk(
    "debate-2-r-020", "roberto", "ambiente", "propuesta",
    "Derogar la Ley Antiforestal aprobada por el fujimorismo; promover una agricultura al poder que deshierbe a la clase política tradicional.",
    "planteamos en medio ambiente derogar la ley antiforestal que ha sido aprobada por el fujimorismo",
    CTX_B3, 1446, 1452, vocero=GUARNIZ, timestamp="81:45",
))
nuevas.append(mk(
    "debate-2-k-012", "keiko", "agricultura", "diagnostico",
    "Saluda a los más de 2.2 millones de agricultores; reconoce que no tienen acceso al agua, al crédito, a asistencia técnica ni a maquinaria y tecnología.",
    "saludo a los más de 2.2 millones de agricultores del Perú que todos los días madrugan a trabajar la tierra",
    CTX_B3, 1460, 1470, vocero=VINELI, timestamp="82:13",
))
nuevas.append(mk(
    "debate-2-k-013", "keiko", "agricultura", "propuesta",
    "Reactivar PRONAMACHCS para construir pequeños reservorios, zanjas de infiltración y reforestación en cuencas altas, a través de núcleos ejecutores como en la década de los 90.",
    "En agricultura lo primero que vamos a hacer es reactivar el PRAMamach",
    CTX_B3, 1477, 1487, vocero=VINELI, timestamp="83:00",
))
nuevas.append(mk(
    "debate-2-k-014", "keiko", "agua", "propuesta",
    "Maquinaria pesada a las 127 juntas de usuarios de agua para limpiar canales, cauces de ríos y caminos, y aumentar rentabilidad y productividad.",
    "queremos invitar a las 127 juntas de usuarios de agua del Perú",
    CTX_B3, 1488, 1497, vocero=VINELI, timestamp="83:30",
))
nuevas.append(mk(
    "debate-2-k-015", "keiko", "agricultura", "propuesta",
    "Programa nacional de asistencia técnica para la pequeña agricultura: combatir el Fusarium en banano, la roya en café y dar acceso a mercados para papa y arroz.",
    "vamos a implementar un programa de asistencia técnica nacional para la pequeña agricultura",
    CTX_B3, 1498, 1512, vocero=VINELI, timestamp="83:54",
))
nuevas.append(mk(
    "debate-2-k-016", "keiko", "agua", "propuesta",
    "Destrabar y construir la represa de Chonta (Cajamarca), la irrigación del río Chicha, segunda etapa de Cachi (Ayacucho) y Majes-Siguas 2 (Arequipa).",
    "vamos a destrabar y construir la represa de Chonta que está abandonada en Cajamarca",
    CTX_B3, 1548, 1559, vocero=VINELI, timestamp="85:57",
))
nuevas.append(mk(
    "debate-2-r-021", "roberto", "agua", "propuesta",
    "Programa nacional de presas altoandinas: trabajar con comunidades campesinas, 127 juntas de usuarios, 2,500 comisiones y 10,000 comités de riego a nivel nacional.",
    "Nosotros planteamos un programa nacional de presas altoandinas. Si no hay agua, no hay vida",
    CTX_B3, 1565, 1574, vocero=GUARNIZ, timestamp="86:29",
))
nuevas.append(mk(
    "debate-2-r-022", "roberto", "agricultura", "cifra",
    "Brecha de infraestructura de riego: más de S/ 14,000 millones (~US$ 3,800 millones) necesarios para cerrar la brecha en organizaciones de usuarios de agua a nivel nacional.",
    "no se cierra la brecha de infraestructura de riego que son más de 14,000 millones de soles",
    CTX_B3, 1591, 1598, vocero=GUARNIZ, timestamp="87:33",
))
nuevas.append(mk(
    "debate-2-k-017", "keiko", "agricultura", "propuesta",
    "Mecanización: entregar 5,000 tractores a las comunidades a nivel nacional y armar un equipo de alto rendimiento para ejecutar inversiones en agricultura.",
    "vamos a entregar 5000 tractores a las comunidades a nivel nacional",
    CTX_B3, 1773, 1784, vocero=VINELI, timestamp="100:13",
))
nuevas.append(mk(
    "debate-2-k-018", "keiko", "ambiente", "propuesta",
    "Combatir la minería ilegal en Amazonía usando tecnología — imágenes satelitales, drones y combate directo a la tala ilegal.",
    "vamos a proteger nuestra Amazonía. Soy de Madre de Dios, Puerto Malonado de la selva del Perú, a través de la tecnología, usando imágenes satelitales, drones",
    CTX_B3, 1739, 1745, vocero=VINELI, timestamp="92:57",
))
nuevas.append(mk(
    "debate-2-r-023", "roberto", "ambiente", "ataque",
    "Suena bonito decir 'vamos a proteger la Amazonía', pero son ellos (Fuerza Popular) quienes han aprobado la Ley Antiforestal; Juntos por el Perú la derogará.",
    "Qué bonito, qué bonito suena decir, \"Vamos a proteger nuestra Amazonía.\" Sin embargo, son ellos los que han aprobado la ley antiforestal",
    CTX_B3, 1746, 1753, vocero=GUARNIZ, timestamp="93:15",
))

# =====================================================================
# BLOQUE 4: INFRAESTRUCTURA (L1987-2599)
# JxP: Gustavo Guerra García | FP: Carlos Neuhaus
# =====================================================================
CTX_B4 = "Bloque 4 — Infraestructura"
GUERRA = "Gustavo Guerra García Picasso"
NEUHAUS = "Carlos Alberto Neuhaus Tudela"

nuevas.append(mk(
    "debate-2-k-019", "keiko", "transporte", "cifra",
    "Según la Contraloría existen 2,241 obras públicas inconclusas valorizadas en aproximadamente S/ 73,000 millones; hospitales, carreteras y sistemas de agua abandonados.",
    "Según la Contraloría, existen 2,241 obras públicas inconclusas valorizadas aproximadamente en 73,000 millones de soles",
    CTX_B4, 2014, 2017, vocero=NEUHAUS, timestamp="104:17",
))
nuevas.append(mk(
    "debate-2-k-020", "keiko", "transporte", "propuesta",
    "Hacer carreteras, puertos, aeropuertos y corredores logísticos modernos que integren regiones y reduzcan costos para conectar al Perú productivo y generar crecimiento.",
    "Haremos carreteras, puertos, aeropuertos, corredores logísticos modernos que integren regiones",
    CTX_B4, 2056, 2068, vocero=NEUHAUS, timestamp="106:02",
))
nuevas.append(mk(
    "debate-2-r-024", "roberto", "transporte", "cifra",
    "En 2021 la inversión pública creció 20% (récord) con la tasa de ejecución más alta desde Invierte.pe (2017); inversión privada creció 37%.",
    "Nosotros en el año 2021 hicimos crecer la inversión pública en 20%, batimos récord de inversión pública",
    CTX_B4, 2084, 2089, vocero=GUERRA, timestamp="107:07",
))
nuevas.append(mk(
    "debate-2-r-025", "roberto", "transporte", "propuesta",
    "Prioridad: conexiones que unen Chancay y Callao con Pucallpa en el marco del proyecto bioceánico que articulará Brasil con China; modernizar ferrocarril del sur a Corío.",
    "nuestra prioridad van a ser las conexiones que van a unir los puertos de Chancay y el Callao con la ciudad de Pocalpa en el marco del gran proyecto bioceánico",
    CTX_B4, 2097, 2117, vocero=GUERRA, timestamp="107:39",
))
nuevas.append(mk(
    "debate-2-r-026", "roberto", "energia", "propuesta",
    "Recuperar el ducto Camisea–Cuzco; no necesitamos el Gasoducto del Sur sino una red de gasoductos para igualar precios; relanzar la obra que ya estaba 35% construida.",
    "tenemos que recuperar el ducto de camisea al Cuzco. No necesitamos el gasoducto del sur porque no podemos seguir teniendo a la gente que está en la zona de producción",
    CTX_B4, 2119, 2131, vocero=GUERRA, timestamp="108:20",
))
nuevas.append(mk(
    "debate-2-r-027", "roberto", "transporte", "compromiso",
    "Programa ambicioso para 180,000 km de caminos rurales: pavimentación económica de 8,000 km, 12,000 mejorados afirmados, 30,000 km bajo costo de tranistabilidad con microempresas campesinas.",
    "Vamos a proponer un ambicioso programa de pavimentación económica de 8,000 km de caminos rurales, 12,000 mejorados",
    CTX_B4, 2141, 2150, vocero=GUERRA, timestamp="109:08",
))
nuevas.append(mk(
    "debate-2-r-028", "roberto", "transporte", "diagnostico",
    "El caos del transporte urbano responde a los decretos legislativos de los 90s de Fujimori; las personas que ganan menos de S/ 1,000 gastan el 50% de sus ingresos en transporte urbano.",
    "En el Perú el caos del transporte urbano responde a los decretos legislativos dados en los 90s en el gobierno de Fujimori",
    CTX_B4, 2152, 2168, vocero=GUERRA, timestamp="109:33",
))
nuevas.append(mk(
    "debate-2-k-021", "keiko", "transporte", "propuesta",
    "Reactivar obras paralizadas judicializadas cortando contratos y convocando nuevas licitaciones transparentes usando tecnología para evitar el factor humano que mete la mano.",
    "lo que tiene uno que hacer es cortar, aplicar los contratos y convocar una nueva licitación",
    CTX_B4, 2281, 2288, vocero=NEUHAUS, timestamp="114:28",
))
nuevas.append(mk(
    "debate-2-r-029", "roberto", "transporte", "diagnostico",
    "Causas tradicionales de obras paralizadas: controversias judiciales, fallas en expedientes, abandono por contratistas; pero crece la falta de financiamiento por inestabilidad política e interferencia del Congreso.",
    "Las causas principales tradicionales eran controversias de carácter judicial, fallas en los expedientes técnicos",
    CTX_B4, 2295, 2317, vocero=GUERRA, timestamp="115:01",
))
nuevas.append(mk(
    "debate-2-r-030", "roberto", "transporte", "propuesta",
    "Priorizar la Línea 3 del Metro de Lima articulada con trenes de cercanía norte (a Barranca) y sur (a Ica) como primer paso del tren costero mayor.",
    "Nosotros queremos priorizar la línea tres. Los trenes se acercarían norte y sur a Barranca y a Ica",
    CTX_B4, 2372, 2384, vocero=GUERRA, timestamp="117:39",
))
nuevas.append(mk(
    "debate-2-r-031", "roberto", "transporte", "propuesta",
    "Política de subsidios al transporte urbano siguiendo prácticas internacionales para abaratarlo; en Lima 2 millones de personas no tienen transporte público y deben iniciar viajes en taxis y mototaxis.",
    "Nosotros vamos a ir por una importante política de subsidios siguiendo las prácticas internacionales de todos los países del mundo para valentar el transporte urbano",
    CTX_B4, 2420, 2429, vocero=GUERRA, timestamp="119:21",
))
nuevas.append(mk(
    "debate-2-k-022", "keiko", "transporte", "propuesta",
    "Transporte eléctrico: vehículos eléctricos como en Santiago de Chile; desincentivar el transporte individual; subsidiar para que paguen menos impuestos y puedan dar servicios.",
    "acá es también es importante los vehículos eléctricos. Ya hay países que todas las transportes",
    CTX_B4, 2431, 2442, vocero=NEUHAUS, timestamp="119:38",
))
nuevas.append(mk(
    "debate-2-r-032", "roberto", "energia", "propuesta",
    "Aumentar de S/ 2.4 millones a S/ 11 millones los programas de electrificación rural anuales e impedir que el gobierno use S/ 240 millones del programa para privatizar Petroperú.",
    "vamos a impedir que el gobierno de la dictadura parlamentaria de Keiko utilice 240 millones del programa de electrificación rural para la privatización de Petroperú",
    CTX_B4, 2469, 2476, vocero=GUERRA, timestamp="120:59",
))

# =====================================================================
# BLOQUE 5: ECONOMÍA Y EMPLEO (L2600-3072)
# JxP: Pedro Francke | FP: Luis Carranza
# =====================================================================
CTX_B5 = "Bloque 5 — Economía y generación de empleo"
FRANCKE = "Pedro Andrés Francke Ballvé"
CARRANZA = "Luis Julián Martín Carranza Ugarte"

nuevas.append(mk(
    "debate-2-r-033", "roberto", "economia", "principio",
    "El Perú tiene las condiciones para un crecimiento del 6%: excelentes precios de metales, gran riqueza y una fuerza emprendedora y trabajadora del pueblo.",
    "tiene las condiciones para que nuestro crecimiento económico sea de 6%. Tenemos excelentes precios los metales",
    CTX_B5, 2619, 2624, vocero=FRANCKE, timestamp="127:33",
))
nuevas.append(mk(
    "debate-2-r-034", "roberto", "seguridad", "compromiso",
    "Derogar las ocho leyes pro-crimen votadas por la bancada fujimorista que extorsionan a pequeñas comerciantes, transportistas y obreros de construcción.",
    "vamos a derogar las ocho leyes procrimen que votó la bancada fungimorista",
    CTX_B5, 2638, 2643, vocero=FRANCKE, timestamp="128:24",
))
nuevas.append(mk(
    "debate-2-r-035", "roberto", "mype", "propuesta",
    "Sistema de financiamiento de S/ 15,000 millones de crédito barato a favor de pequeños empresarios sacándoles de encima regulaciones absurdas y funcionarios corruptos que cobran coimas.",
    "puede haber un sistema de financiamiento de 15,000 millones de soles de crédito barato a favor de los pequeños empresarios",
    CTX_B5, 2650, 2664, vocero=FRANCKE, timestamp="128:52",
))
nuevas.append(mk(
    "debate-2-r-036", "roberto", "economia", "defensa",
    "Respetar autonomía del BCR, pidiéndole a Julio Velarde que siga en su puesto; respetar metas de déficit fiscal y contratos. No habrá estatizaciones.",
    "respetando la autonomía del Banco Central y pidiéndole a Julio Belarde que siga en su puesto",
    CTX_B5, 2665, 2683, vocero=FRANCKE, timestamp="129:23",
))
nuevas.append(mk(
    "debate-2-r-037", "roberto", "energia", "propuesta",
    "Reactivar el fondo de estabilización de combustibles; en el pasado redujo el precio de la gasolina en S/ 5 por galón.",
    "Anteriormente nuestro perio enfrentaba eso con el fondo de estabilización",
    CTX_B5, 2687, 2693, vocero=FRANCKE, timestamp="130:14",
))
nuevas.append(mk(
    "debate-2-k-023", "keiko", "pensiones", "cifra",
    "En 2021 la pobreza estuvo en 25.9%; en 2022 hubo 644,000 nuevos peruanos en pobreza; en 2025 la pobreza está en 25.7%, sin avances pre-pandemia.",
    "En 2021 la pobreza estuvo en 25.9%",
    CTX_B5, 2706, 2715, vocero=CARRANZA, timestamp="131:05",
))
nuevas.append(mk(
    "debate-2-k-024", "keiko", "economia", "principio",
    "Tres pilares del plan: orden económico (autonomía del BCR, equilibrio fiscal), capitalismo popular (inversión privada y MIPYMES) y orden social (salud, educación, pensión mínima universal con Pensión 65).",
    "El plan ahora es para levantar a nuestro Perú y tiene tres pilares: orden económico, capitalismo popular y orden social",
    CTX_B5, 2723, 2752, vocero=CARRANZA, timestamp="132:01",
))
nuevas.append(mk(
    "debate-2-k-025", "keiko", "mype", "propuesta",
    "Apoyar a MYPEs con créditos garantizados por banco de desarrollo (no subsidiados) y desarrollar la infraestructura sacando los grandes proyectos atorados.",
    "apoyar a nuestras pequeñas y medianas empresas. dándoles créditos con garantías de nuestro banco de desarrollo",
    CTX_B5, 2735, 2746, vocero=CARRANZA, timestamp="132:38",
))
nuevas.append(mk(
    "debate-2-k-026", "keiko", "mype", "propuesta",
    "La informalidad estructural se resuelve con dos medidas: inversión privada que cree empleo y eficiencia del Estado que reduzca trámites; costo cero e incentivos tributarios para formalización.",
    "El tema de la informalidad es un tema estructural en Perú y se puede resolver con dos medidas. Primero, inversión privada que cree empleo",
    CTX_B5, 2800, 2811, vocero=CARRANZA, timestamp="135:00",
))
nuevas.append(mk(
    "debate-2-r-038", "roberto", "industria", "propuesta",
    "Incentivar y promover la inversión privada en industria, agroindustria y agricultura con gran transformación tecnológica que genere empleos masivamente.",
    "incentivar y promover la inversión privada en la industria, en la agroindustria, en la agricultura. y con una gran transformación tecnológica",
    CTX_B5, 2821, 2828, vocero=FRANCKE, timestamp="135:43",
))
nuevas.append(mk(
    "debate-2-r-039", "roberto", "trabajo", "cifra",
    "En los 6 meses de gestión de Pedro Francke como ministro se crearon 300,000 empleos según el Banco Central de Reserva.",
    "En los 6 meses que estuvo en la gestión el Ministerio de Economía y Finanzas creamos 300,000 empleos",
    CTX_B5, 2843, 2846, vocero=FRANCKE, timestamp="136:32",
))
nuevas.append(mk(
    "debate-2-k-027", "keiko", "trabajo", "ataque",
    "En 2022 la inversión privada en Perú no creció nada y se perdieron 393,000 puestos de empleo; en 2023 hubo recesión sin crisis externa severa.",
    "en el año 2022 la inversión privada en el Perú no creció nada y perdimos ese año 2022 perdimos 393,000 puestos de empleo",
    CTX_B5, 2853, 2858, vocero=CARRANZA, timestamp="136:51",
))
nuevas.append(mk(
    "debate-2-r-040", "roberto", "educacion", "ataque",
    "El Congreso aumentó S/ 1,500 millones su presupuesto y no le pueden dar S/ 120 millones a estudiantes para becas; ahora prometen duplicar las becas.",
    "El presupuesto aprobado por el señor Rospigliosi, presidente del Congreso, aumenta 1,500 millones de soles su presupuesto en estos 5 años",
    CTX_B5, 2939, 2949, vocero=FRANCKE, timestamp="140:01",
))
nuevas.append(mk(
    "debate-2-k-028", "keiko", "economia", "compromiso",
    "Regla fiscal debe cambiar para controlar el crecimiento del gasto corriente, apostar por inversión pública y regresar al déficit del 1%; meta de crecimiento 67% al 2028.",
    "La regla fiscal tiene que controlar el crecimiento, el gasto corriente, apostar por la inversión pública y regresar al déficit de 1%",
    CTX_B5, 3007, 3014, vocero=CARRANZA, timestamp="142:49",
))
nuevas.append(mk(
    "debate-2-r-041", "roberto", "agricultura", "ataque",
    "Fuerza Popular regaló S/ 20,000 millones al sector agroexportador que no lo necesitaba porque son los que financian su campaña.",
    "Fuerza Popular le regaló 20,000 millones de soles al sector agroexportador",
    CTX_B5, 3040, 3046, vocero=FRANCKE, timestamp="143:58",
))

# =====================================================================
# BLOQUE 6: SALUD (L3153-3567)
# JxP: Hernando Ceballos | FP: José Recoba
# =====================================================================
CTX_B6 = "Bloque 6 — Salud"
CEBALLOS = "Hernando Ceballos Flores"
RECOBA = "José Francisco Recoba Martínez"

nuevas.append(mk(
    "debate-2-k-029", "keiko", "salud", "diagnostico",
    "Uno de cada dos niños menores de 3 años tienen anemia; cuatro de cada 10 peruanos no tienen vacunas; nueve de cada 10 establecimientos de salud están en condiciones de abandono.",
    "Uno de cada dos niños de nuestro país, menores de 3 años, tienen anemia. Cuatro de cada 10 peruanos no tienen vacunas",
    CTX_B6, 3181, 3194, vocero=RECOBA, timestamp="151:13",
))
nuevas.append(mk(
    "debate-2-k-030", "keiko", "salud", "diagnostico",
    "10 ministros de salud (nueve de esta gestión) en 5 años y 12 presidentes de salud; centros de salud atienden pocas horas y los diagnósticos de cáncer demoran 3-12 meses sin tratamientos.",
    "10 ministros de salud, nueve de esta gestión en 5 años y 12 presidentes de salud han determinado que hoy día estemos colapsando",
    CTX_B6, 3201, 3216, vocero=RECOBA, timestamp="151:57",
))
nuevas.append(mk(
    "debate-2-r-042", "roberto", "salud", "principio",
    "La salud no es vista como un derecho en el país; nosotros sí decimos que el Estado debe garantizarla independientemente de las posibilidades económicas, gratuita y de calidad.",
    "el Estado debe garantizar la salud porque la salud es un derecho fundamental",
    CTX_B6, 3252, 3258, vocero=CEBALLOS, timestamp="154:05",
))
nuevas.append(mk(
    "debate-2-r-043", "roberto", "salud", "diagnostico",
    "250,000 ciudadanos fallecidos en la pandemia no fallecieron por el virus sino por la miseria de un sistema excluyente; el gasto en salud está cerca de la mitad de lo que recomienda la OMS (3.3%).",
    "luego de tener 250,000 ciudadanos fallecidos por la pandemia, que no fallecieron por el virus, sino fallecieron por la miseria de un sistema excluyente",
    CTX_B6, 3259, 3289, vocero=CEBALLOS, timestamp="154:24",
))
nuevas.append(mk(
    "debate-2-r-044", "roberto", "salud", "ataque",
    "Fuerza Popular ha controlado el Congreso desde 2016; vacaron al presidente Castillo a un año y 3 meses; hegemonía en el Congreso después de la vacancia.",
    "después de que vacaron al presidente Pedro Castillo? una cúpula donde tiene la hegemonía Fuerza Popular",
    CTX_B6, 3277, 3284, vocero=CEBALLOS, timestamp="155:11",
))
nuevas.append(mk(
    "debate-2-k-031", "keiko", "salud", "propuesta",
    "Mapear casa por casa, niño por niño, madre gestante con control prenatal para tener trazabilidad sobre anemia y desnutrición que ha aumentado dos puntos porcentuales.",
    "Nosotros vamos a estar mapeando casa por casa, niño por niño, madre gestante con control prenatal",
    CTX_B6, 3396, 3406, vocero=RECOBA, timestamp="160:02",
))
nuevas.append(mk(
    "debate-2-r-045", "roberto", "salud", "propuesta",
    "Financiar la salud no regalando exoneraciones tributarias a agroexportadoras; fortalecer sistema nacional de salud, atención primaria, nombramiento de trabajadores, política de medicamentos e historia clínica electrónica.",
    "no le vamos a regalar exoneraciones tributarias a las grandes empresas agroexportadoras",
    CTX_B6, 3409, 3425, vocero=CEBALLOS, timestamp="160:31",
))
nuevas.append(mk(
    "debate-2-k-032", "keiko", "salud", "diagnostico",
    "El 97% de los establecimientos de salud está deteriorado en condiciones deplorables; en Piura los 7 hospitales están al 100% en malas condiciones.",
    "El 97% de los establecimientos de salud de nuestro país está deteriorado en condiciones realmente deplorables",
    CTX_B6, 3436, 3446, vocero=RECOBA, timestamp="161:33",
))
nuevas.append(mk(
    "debate-2-k-033", "keiko", "salud", "propuesta",
    "Implementar red de telemedicina que llegue a regiones donde no hay quien atender; brigadas de salud que lleguen a casas de personas más necesitadas, empezando por las regiones del sur.",
    "tenemos que implementar una red de telemedicina que ya existe, pero lo vamos a fortalecer",
    CTX_B6, 3447, 3462, vocero=RECOBA, timestamp="161:58",
))
nuevas.append(mk(
    "debate-2-r-046", "roberto", "economia", "propuesta",
    "Financiar la atención dejando de regalarle plata a Petroperú: S/ 30,000 millones en 5 años podrán liberarse para lo que han abandonado.",
    "Es fácil dejando de regalarle plata a Petroperú. Ustedes le han dado 30,000 millones de soles en 5 años",
    CTX_B6, 3469, 3478, vocero=CEBALLOS, timestamp="162:46",
))
nuevas.append(mk(
    "debate-2-r-047", "roberto", "salud", "compromiso",
    "Pasar a tener más de 1,000 establecimientos de salud mental y repotenciar el primer nivel con conjunto de especialistas para no saturar los hospitales.",
    "hay que pasar a tener más de 1000 establecimientos de salud, de salud mental",
    CTX_B6, 3501, 3508, vocero=CEBALLOS, timestamp="163:57",
))
nuevas.append(mk(
    "debate-2-r-048", "roberto", "justicia", "ataque",
    "Fuerza Popular puso orden 'asesinando a 70 peruanos' que protestaban reclamando su derecho al voto; exoneró a Dina Boluarte; no interpeló al ministro Vásquez por sueros fisiológicos.",
    "Seguramente van a poner orden, como pusieron orden asesinando a 70 peruanos porque protestaban reclamando el derecho a su voto",
    CTX_B6, 3533, 3547, vocero=CEBALLOS, timestamp="165:12",
))
nuevas.append(mk(
    "debate-2-r-049", "roberto", "constitucion", "principio",
    "Construir un país diferente, lejos de las mafias, lejos de la corrupción, buscando transparencia y más equidad; no se trata solo de Keiko Fujimori y Roberto Sánchez.",
    "podemos construir un país diferente, lejos de las mafias, donde está Fuerza Popular, lejos de la corrupción",
    CTX_B6, 3556, 3567, vocero=CEBALLOS, timestamp="166:14",
))
nuevas.append(mk(
    "debate-2-k-034", "keiko", "constitucion", "compromiso",
    "Esta elección no es de derechas ni de izquierdas: es saber si seguimos con el caos o ponemos orden; invitación a poner orden con la fuerza de la salud.",
    "Esta elección no es de derechas ni de izquierdas. Esta elección es para saber si vamos a continuar con el caos",
    CTX_B6, 3526, 3532, vocero=RECOBA, timestamp="164:54",
))

# =====================================================================
# Volcar al JSON y guardar
# =====================================================================
ruta = Path("00-Sistema/datos/declaraciones.json")
d = json.loads(ruta.read_text(encoding="utf-8"))
print(f"Antes: {len(d['declaraciones'])} declaraciones")
print(f"Nuevas a agregar: {len(nuevas)}")

ids_existentes = {p["id"] for p in d["declaraciones"]}
duplicados = [n["id"] for n in nuevas if n["id"] in ids_existentes]
if duplicados:
    print(f"ERROR: IDs duplicados: {duplicados}")
    raise SystemExit(1)

ids_nuevos = [n["id"] for n in nuevas]
if len(ids_nuevos) != len(set(ids_nuevos)):
    print("ERROR: IDs duplicados dentro de nuevas")
    raise SystemExit(1)

d["declaraciones"].extend(nuevas)
ruta.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Despues: {len(d['declaraciones'])} declaraciones")
print("OK escrito.")
