# -*- coding: utf-8 -*-
"""Extracción de declaraciones del Debate 1 (cara-a-cara).

Estructura del debate:
- Apertura
- Bloque 1: ¿Por qué debería ser elegido presidente?
- Bloque 2: Seguridad ciudadana
- Bloque 3: Fortalecimiento del Estado Democrático y DDHH
- Bloque 4: Educación y Salud
- Bloque 5: Economía, Empleo y Reducción de la Pobreza
- Carta Blanca (palabras finales)

Convención de ID: debate-1-[k|r]-NNN, NNN secuencial por candidato.
"""
import json
from pathlib import Path

ARCHIVO_FUENTE = "02-Debates/raw/Debate 1.txt"
DEBATE_ID = "debate-1"


def mk(id_, candidato, tema, tipo, texto, cita, contexto, linea_ini, linea_fin, vocero=None, timestamp=None):
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
# APERTURA (líneas 1-50)
# =====================================================================
CTX_APERTURA = "Apertura — palabras iniciales"

nuevas.append(mk(
    "debate-1-r-001", "roberto", "pensiones", "diagnostico",
    "Cifras de pobreza, desnutrición infantil y violencia sexual contra niñas como diagnóstico de apertura.",
    "9 millones de peruanos vivan con pobreza extrema y exclusión, 1 millón de niños con desnutrición y anemia",
    CTX_APERTURA, 11, 14,
))
nuevas.append(mk(
    "debate-1-r-002", "roberto", "constitucion", "ataque",
    "Caracteriza al Congreso liderado por Keiko Fujimori como 'dictadura congresal' a la que hay que poner fin.",
    "Hay que acabar con la dictadura congresal que dirige Keiko Fujimori",
    CTX_APERTURA, 18, 20,
))
nuevas.append(mk(
    "debate-1-k-001", "keiko", "economia", "principio",
    "Visión-país: el Perú es un país emprendedor con bases económicas sólidas y solo necesita ordenarse.",
    "Somos el país más emprendedor del mundo. Tenemos las tierras más ricas y variadas, unas bases económicas sólidas",
    CTX_APERTURA, 35, 38,
))
nuevas.append(mk(
    "debate-1-k-002", "keiko", "seguridad", "compromiso",
    "Compromiso a 5 años: dejar un país con más empleo y más seguridad si la eligen.",
    "Si los peruanos nos dan una oportunidad, en 5 años dejaremos un país con más empleo y con más seguridad",
    CTX_APERTURA, 45, 47,
))

# =====================================================================
# BLOQUE 1: ¿POR QUÉ DEBERÍA SER ELEGIDO PRESIDENTE? (líneas 51-148)
# =====================================================================
CTX_B1 = "Bloque 1 — ¿Por qué debería ser elegido presidente?"

nuevas.append(mk(
    "debate-1-k-003", "keiko", "seguridad", "diagnostico",
    "Diagnóstico del país: extorsiones, alza del precio del pan, bodegas que no abren por miedo, dificultad para conseguir cita médica y falta de agua.",
    "Extorsiones, aumenta el precio del pan. El dinero cada vez alcanza menos. Hay más rejas en los barrios. Las bodegas no abren por miedo. Conseguir un turno médico es casi imposible",
    CTX_B1, 73, 78,
))
nuevas.append(mk(
    "debate-1-k-004", "keiko", "economia", "principio",
    "Dicotomía estratégica: orden vs caos como las dos opciones del país, asociando el caos a la fórmula Castillo-Sánchez-Santauro.",
    "Orden o caos. Estas son las dos opciones que tiene hoy nuestro país. Orden pollo más barato. Balones de gas a precio accesible",
    CTX_B1, 85, 88,
))
nuevas.append(mk(
    "debate-1-r-003", "roberto", "educacion", "principio",
    "Biografía como argumento: hijo de la educación pública y orgulloso egresado de la UNMSM como base de identificación con el pueblo peruano.",
    "Soy hijo de la educación pública. Estudié mi primaria en el 21009 y la secundaria en el Andrés de los Reyes",
    CTX_B1, 106, 109,
))
nuevas.append(mk(
    "debate-1-r-004", "roberto", "justicia", "ataque",
    "Imputa al fujimorismo (Fuerza Popular) el secuestro de la democracia y la corrosión del sistema de justicia durante más de 10 años.",
    "salvar nuestra democracia de las garras de quienes han secuestrado hace más de 10 años, subvertido el sistema de justicia, han corroído el país y ellos son Fuerza Popular",
    CTX_B1, 131, 137,
))

# =====================================================================
# BLOQUE 2: SEGURIDAD CIUDADANA (líneas 202-604)
# =====================================================================
CTX_B2 = "Bloque 2 — Seguridad ciudadana"

# Datos de contexto (no propuesta, no cita de candidato)
# (intencionalmente saltamos los datos del moderador)

# Keiko exposición inicial
nuevas.append(mk(
    "debate-1-k-005", "keiko", "seguridad", "diagnostico",
    "Diagnóstico del 'mundo al revés': militares y policías perseguidos, vecinos enrejados, delincuentes libres; te matan por un celular y hay granadas en los colegios.",
    "Los militares y policías son perseguidos, los vecinos viven enrejados y los delincuentes libres",
    CTX_B2, 229, 232,
))
nuevas.append(mk(
    "debate-1-k-006", "keiko", "seguridad", "propuesta",
    "Plan de pacificación nacional desde el primer día con policías y militares 24/7 en los buses de las áreas metropolitanas.",
    "Implementaremos el plan de pacificación nacional. Hoy los transportistas y los pasajeros sufren una doble extorsión",
    CTX_B2, 237, 245,
))
nuevas.append(mk(
    "debate-1-k-007", "keiko", "seguridad", "propuesta",
    "Trabajo con entidades financieras y plataformas de pago para identificar, rastrear y bloquear el dinero de las extorsiones.",
    "Trabajaremos con las entidades financieras y las plataformas de pago para identificar, rastrear, bloquear el dinero de las extorsiones",
    CTX_B2, 247, 250,
))
nuevas.append(mk(
    "debate-1-k-008", "keiko", "seguridad", "propuesta",
    "Expulsión inmediata de migrantes ilegales que cometan delitos y rastrillajes en zonas peligrosas.",
    "Expulsaremos inmediatamente a todos los migrantes ilegales que cometan delitos. Activaremos los rastrillajes en las zonas peligrosas",
    CTX_B2, 251, 254,
))
nuevas.append(mk(
    "debate-1-k-009", "keiko", "seguridad", "propuesta",
    "Fuerzas armadas asumirán el control de las fronteras; ejemplo de la frontera con Ecuador con solo dos patrullas.",
    "Las fuerzas armadas asumirán el control de nuestras fronteras. Hoy, por ejemplo, en la frontera con Ecuador solo hay dos patrullas",
    CTX_B2, 259, 261,
))
nuevas.append(mk(
    "debate-1-k-010", "keiko", "justicia", "cifra",
    "Cifra de impunidad: de cada 10,000 denuncias solo cinco llegan a sentencia; en unidades de flagrancia el 91% llega a sentencia.",
    "Hoy de cada 10,000 denuncias solo cinco llegan a ser sentencia. En las unidades de flagrancia el 91% llegó a ser sentencia",
    CTX_B2, 268, 272,
))
nuevas.append(mk(
    "debate-1-k-011", "keiko", "justicia", "propuesta",
    "Unidades de flagrancia como piedra angular del sistema de justicia renovado, con casos de extorsión sentenciados en 4 días vs >1000 días en justicia ordinaria.",
    "las unidades de flagrancia se convertirán en una piedra angular de un sistema de justicia renovado",
    CTX_B2, 277, 280,
))
nuevas.append(mk(
    "debate-1-k-012", "keiko", "seguridad", "propuesta",
    "Reforzar el sistema de inteligencia: la inteligencia derrotó al terrorismo y se volverá a usar contra la criminalidad.",
    "reforzaremos el sistema de inteligencia. La inteligencia derrotó al terrorismo y ahora la volveremos a usar para derrotar la criminalidad",
    CTX_B2, 280, 284,
))

# Roberto exposición inicial seguridad
nuevas.append(mk(
    "debate-1-r-005", "roberto", "seguridad", "cifra",
    "Siete peruanos mueren cada día por criminalidad; más de 100 choferes transportistas asesinados.",
    "siete peruanos mueren cada día producto de la criminalidad. Más de 100 chóeres transportistas han sido asesinados",
    CTX_B2, 295, 298,
))
nuevas.append(mk(
    "debate-1-r-006", "roberto", "seguridad", "ataque",
    "Imputa al Congreso (fujimorismo) la creación de 'leyes pro-crímenes' para limpiarse de juicios y sentencias, profundizando la inseguridad. Llama a Keiko 'la señora del caos con K'.",
    "una fuerza parlamentaria del Congreso para limpiarse de sus fechorías, juicios y sentencias ha subvertido el sistema de justicia y ha creado las leyes procrímenes",
    CTX_B2, 303, 310,
))
nuevas.append(mk(
    "debate-1-r-007", "roberto", "seguridad", "propuesta",
    "Limpiar la PNP de malos elementos, profesionalizar con inteligencia, crear policía de investigaciones y pagar deuda social del 2% e incrementar sueldos.",
    "Hay que limpiar nuestra policía nacional de los malos elementos, recuperarlos profesionalizándolos, poniendo inteligencia para el servicio",
    CTX_B2, 313, 321,
))
nuevas.append(mk(
    "debate-1-r-008", "roberto", "corrupcion", "propuesta",
    "Reto público a Keiko: ¿está dispuesta a derogar las 'leyes pro-crímenes'? Necesidad de recuperar el sistema de justicia con consecuencia y acción.",
    "¿está dispuesta la señora Fujimori a derogar las leyes procrímenes? ¿Qué le dice al Perú? Necesitamos recuperar de verdad el sistema de justicia",
    CTX_B2, 330, 335,
))
nuevas.append(mk(
    "debate-1-r-009", "roberto", "corrupcion", "propuesta",
    "'Muerte civil' para funcionarios corruptos como sanción ejemplar contra la corrupción.",
    "lucha contra la corrupción venga, por ejemplo, con muerte civil para los funcionarios corruptos. muerte civil",
    CTX_B2, 336, 340,
))
nuevas.append(mk(
    "debate-1-r-010", "roberto", "seguridad", "propuesta",
    "Convocatoria a fuerzas patrióticas: ronderos, sociedad civil y comunidades campesinas como aliados en la lucha por la seguridad como política de Estado.",
    "convocamos a las fuerzas patrióticas, a los ronderos, a la sociedad civil, comunidades campesinas, porque la seguridad ciudadana, la lucha para defender la vida es una política de estado",
    CTX_B2, 352, 358,
))

# Diálogo seguridad: pregunta ciudadana extorsión
CTX_B2_PREG = "Bloque 2 — Pregunta ciudadana sobre extorsión"
nuevas.append(mk(
    "debate-1-k-013", "keiko", "seguridad", "propuesta",
    "Compromiso de 100 días: pedir facultades, implementar comisarías, comprar patrulleros; uso del sistema de flagrancia para condenas rápidas.",
    "Pensamos pedir además facultades para los 100 primeros días de gobierno, implementar las comisarías, comprar patrulleros",
    CTX_B2_PREG, 418, 422,
))
nuevas.append(mk(
    "debate-1-k-014", "keiko", "constitucion", "defensa",
    "Defensa contra acusación de Roberto: 'Caos se escribe con C, con la C de Castillo'; Fuerza Popular solo tiene 20 de 130 congresistas.",
    "quiero decirle que Caos se escribe con C, con la C de Castillo. Y ustedes ya gobernaron. Fuerza Popular solo tiene 20 congresistas de 130",
    CTX_B2_PREG, 423, 427,
))
nuevas.append(mk(
    "debate-1-r-011", "roberto", "seguridad", "propuesta",
    "Reformar la ley para que las FFAA puedan, excepcionalmente, apoyar a la PNP en territorios coptados por la criminalidad y la extorsión.",
    "es importante hacer algunas reformas a la ley para que las fuerzas armadas excepcionalmente puedan venir en auxilio, en apoyo de la Policía Nacional",
    CTX_B2_PREG, 434, 442,
))
nuevas.append(mk(
    "debate-1-k-015", "keiko", "seguridad", "ataque",
    "Ataque a Roberto: en sus filas tiene a Antauro Humala, 'asesino de policías', y en el último mitin de primera vuelta dijo que la lucha contra el crimen estará en sus manos.",
    "tiene usted en sus filas Antaurumala, asesino de policías. Usted el 8 de abril en el último miting de primera vuelta dijo lo siguiente",
    CTX_B2_PREG, 458, 466,
))
nuevas.append(mk(
    "debate-1-r-012", "roberto", "justicia", "ataque",
    "Imputa a Keiko el archivamiento de la investigación de los más de 50 asesinatos durante las protestas de 2022-2023 con Dina Boluarte.",
    "más de 50 asesinatos, señora Keiko, que usted ha blindado, que no le ha importado la vida de más de 50 compatriotas con su socia Dina Boluarte",
    CTX_B2_PREG, 469, 473,
))
nuevas.append(mk(
    "debate-1-k-016", "keiko", "seguridad", "defensa",
    "Defensa: Fuerza Popular promovió la Ley 32062 que protege a ciudadanos en legítima defensa y la Ley 32291 que defiende el uso de fuerza por la policía.",
    "La primera que fue promovida por nosotros, que protege a los ciudadanos en caso de legítima defensa frente a los delincuentes, la 3206",
    CTX_B2_PREG, 492, 503,
))

# Cierres seguridad
CTX_B2_CIERRE = "Bloque 2 — Cierre seguridad"
nuevas.append(mk(
    "debate-1-k-017", "keiko", "seguridad", "propuesta",
    "Modelo histórico: derrota al terrorismo combinando FFAA, PNP, rondas campesinas, comités de autodefensa y población organizada; aplicarlo a la criminalidad.",
    "Para poder combatir el terrorismo se fortaleció las fuerzas armadas, la policía nacional, se trabajó con las rondas campesinas, los comités autodefensa",
    CTX_B2_CIERRE, 566, 570,
))
nuevas.append(mk(
    "debate-1-k-018", "keiko", "seguridad", "ataque",
    "A Sánchez lo acompaña 'un asesino de policías'; ella estará acompañada por Marco Miyashiro y el general Astudillo, 'héroes nacionales'.",
    "Me acompañan además a mí dos héroes nacionales, Marco Millashiro y el general Astudillo. En cambio, al señor Sánchez lo acompaña un asesino de policías",
    CTX_B2_CIERRE, 573, 578,
))

# =====================================================================
# BLOQUE 3: ESTADO DEMOCRÁTICO Y DDHH (líneas 657-1033)
# =====================================================================
CTX_B3 = "Bloque 3 — Fortalecimiento del Estado Democrático y DDHH"

# Roberto exposición inicial
nuevas.append(mk(
    "debate-1-r-013", "roberto", "constitucion", "diagnostico",
    "El régimen semipresidencialista ha sido subvertido de facto con medidas antidemocráticas como quitarle el derecho al referéndum al pueblo peruano.",
    "El régimen político de nuestro país semipresidencialista ha sido subvertido y modificado de facto",
    CTX_B3, 665, 672,
))
nuevas.append(mk(
    "debate-1-r-014", "roberto", "constitucion", "propuesta",
    "Recuperar el derecho al referéndum y convocar a fuerzas patrióticas para restablecer el equilibrio y separación de poderes.",
    "el pueblo necesita recuperar el derecho al referéndum y nosotros estamos invocando a todas las fuerzas patrióticas democráticas para recuperar ese derecho",
    CTX_B3, 696, 704,
))
nuevas.append(mk(
    "debate-1-r-015", "roberto", "constitucion", "propuesta",
    "Estado descentralizado e intercultural: descentralizar recursos presupuestales hasta centros poblados menores; afirmar el rostro andino-amazónico de la nación.",
    "vamos a también a descentralizar recursos presupuestales, por ejemplo, a los centros poblados menores",
    CTX_B3, 710, 717,
))
nuevas.append(mk(
    "debate-1-r-016", "roberto", "exterior", "propuesta",
    "Fortalecer institucionalidad interamericana, Acuerdo de Escazú, Acuerdo Chapultepec y presencia en el Sistema Interamericano de DDHH.",
    "fortalecer la institucionalidad interamericana, el acuerdo de Escasú, el acuerdo Chapultepec",
    CTX_B3, 724, 730,
))

# Keiko exposición inicial
nuevas.append(mk(
    "debate-1-k-019", "keiko", "agua", "diagnostico",
    "Diagnóstico: 45% de las familias no tienen títulos de propiedad ni agua potable; colegios, postas médicas y hospitales colapsados.",
    "45% de las familias no tienen títulos de propiedad ni agua potable",
    CTX_B3, 747, 751,
))
nuevas.append(mk(
    "debate-1-k-020", "keiko", "agua", "propuesta",
    "Plan de agua: finalizar esquemas de agua y ramal sur de Lima; plantas desalinizadoras en costa; reservorios y cochas en sierra; pozos y sistemas potabilizadores en Amazonía.",
    "nos ocuparemos de los servicios básicos, el agua. En Lima finalizaremos los esquemas de agua, la construcción del ramal sur",
    CTX_B3, 753, 760,
))
nuevas.append(mk(
    "debate-1-k-021", "keiko", "vivienda", "compromiso",
    "Meta: entregar 1 millón de títulos de propiedad en los próximos 5 años a través de Cofopri potenciado.",
    "Potenciaremos Cofopri. Cada hogar tiene que tener su título de propiedad y aspiramos que en los próximos 5 años entregaremos 1 millón de títulos",
    CTX_B3, 762, 765,
))
nuevas.append(mk(
    "debate-1-k-022", "keiko", "transporte", "propuesta",
    "Programa Nacional de Interconexión Vial: cuando hay pistas y carreteras los agricultores sacan productos, los niños van a la escuela y el turismo crece.",
    "lanzaremos el programa nacional de interconexión vial. Nuestras carreteras están destruidas, los puentes no se construyen",
    CTX_B3, 775, 780,
))
nuevas.append(mk(
    "debate-1-k-023", "keiko", "ambiente", "propuesta",
    "Obras de prevención ante el Fenómeno del Niño: limpieza de ríos, compra de maquinaria pesada, sistemas de regulación hídrica y reforestación.",
    "Para las inundaciones, trabajaremos en la limpieza de los ríos y la compra de maquinarias pesadas. Implementaremos sistemas de regulación hídrica",
    CTX_B3, 789, 793,
))

# Pregunta ciudadana discriminación
CTX_B3_PREG = "Bloque 3 — Pregunta ciudadana sobre discriminación, racismo y homofobia"
nuevas.append(mk(
    "debate-1-r-017", "roberto", "indigenas", "principio",
    "Lucha contra la discriminación como política de Estado; reconocer la diversidad y la interculturalidad; el Perú es un pueblo de todas las sangres.",
    "la lucha contra la discriminación tiene que ser una política de estado porque es una condición mínima de un estado con cohesión",
    CTX_B3_PREG, 833, 845,
))
nuevas.append(mk(
    "debate-1-k-024", "keiko", "educacion", "propuesta",
    "Prevenir discriminación mejorando la currícula escolar; combatir la ausencia del Estado en poblaciones alejadas, especialmente en la Amazonía.",
    "esto se tiene que prevenir primero a través de la educación. Eh, la currícula escolar tiene que ser mejorada",
    CTX_B3_PREG, 860, 864,
))
nuevas.append(mk(
    "debate-1-r-018", "roberto", "justicia", "ataque",
    "Imputa impunidad por los 56 asesinados en el sur en las protestas; el Congreso ha secundado esa impunidad bajo el liderazgo de Keiko.",
    "como hoy 56 asesinados en el sur, ¿de qué ¿De qué igualdad? ¿De qué cero discriminación se está hablando?",
    CTX_B3_PREG, 884, 893,
))
nuevas.append(mk(
    "debate-1-k-025", "keiko", "transporte", "compromiso",
    "Compromisos viales: Panamericana 4 vías de Trujillo a Tumbes y de Ica a Tacna; Carretera Libertadores asfaltada; cuatro carreteras de penetración hacia el centro.",
    "de Trujillo hacia Tumbes y de Ica hacia Tacna tengamos la Panamericana de cuatro vías. La carretera Libertadores tiene que ser asfaltada",
    CTX_B3_PREG, 904, 914,
))
nuevas.append(mk(
    "debate-1-r-019", "roberto", "exterior", "compromiso",
    "Firme compromiso con el Sistema Interamericano de DDHH y el Pacto de San José de Costa Rica; en Juntos por el Perú no se corre frente a los DDHH.",
    "El Perú necesita un firme compromiso ante el sistema interamericano de derechos humanos. En Juntos por el Perú no nos corremos de derechos humanos",
    CTX_B3_PREG, 924, 932,
))

# Cierres bloque 3
CTX_B3_CIERRE = "Bloque 3 — Cierre Estado y DDHH"
nuevas.append(mk(
    "debate-1-r-020", "roberto", "constitucion", "principio",
    "El Perú necesita un Estado democrático, descentralizado y cercano a la gente, con políticas de Estado que hagan de la salud y la vivienda derechos fundamentales.",
    "convocamos a todas las fuerzas a ese consenso para tener un estado democrático, descentralizado, amigo, con políticas de estado donde la salud, la vivienda sean derechos fundamentales",
    CTX_B3_CIERRE, 994, 1002,
))
nuevas.append(mk(
    "debate-1-k-026", "keiko", "constitucion", "compromiso",
    "Convocatoria a inscribir personeros en Fuerza Popular y en el otro grupo político; los observadores internacionales serán claves para fortalecer la democracia.",
    "hacemos esta convocatoria para que todos los ciudadanos se inscriban como personeros, no solamente en Fuerza Popular, también en el otro grupo político",
    CTX_B3_CIERRE, 1018, 1024,
))

# =====================================================================
# BLOQUE 4: EDUCACIÓN Y SALUD (líneas 1034-1430)
# =====================================================================
CTX_B4 = "Bloque 4 — Educación y Salud"

# Keiko salud
nuevas.append(mk(
    "debate-1-k-027", "keiko", "salud", "cifra",
    "Vía crucis del paciente oncológico: 45 días para primera cita con especialista, 75 días para tomografía o biopsia, 37 días para resultados y casi 6 meses para iniciar tratamiento.",
    "45 días para una primera cita con un especialista. 75 días para una primera tomografía o biopsia. 37 días para tener los resultados",
    CTX_B4, 1058, 1063,
))
nuevas.append(mk(
    "debate-1-k-028", "keiko", "salud", "cifra",
    "46% de niños sufren anemia, perdiendo para siempre parte de su capacidad para aprender.",
    "46% de nuestros niños sufren de anemia, perdiendo para siempre parte de su capacidad para aprender",
    CTX_B4, 1063, 1066,
))
nuevas.append(mk(
    "debate-1-k-029", "keiko", "salud", "propuesta",
    "Implementar telemedicina en todo el país y fortalecer el fondo para enfermedades de alto costo con cobertura a tratamientos de cáncer.",
    "Vamos a implementar telemedicina en todo el país, no más tiempos de espera",
    CTX_B4, 1068, 1077,
))
nuevas.append(mk(
    "debate-1-k-030", "keiko", "salud", "propuesta",
    "Plan gratuito para los primeros 1,000 días para proteger a la primera infancia, a la madre y combatir la anemia.",
    "Crearemos el plan gratuito en los primeros 1000 días. para proteger a la primera infancia, a la madre y así combatir la anemia",
    CTX_B4, 1078, 1081,
))
nuevas.append(mk(
    "debate-1-k-031", "keiko", "educacion", "compromiso",
    "Meta: construir y repotenciar 5,000 colegios con todos los servicios básicos y acceso a internet; siete de cada 10 colegios no tienen los tres servicios básicos.",
    "Construiremos y repotenciaremos 5000 colegios con todos los servicios básicos y acceso a internet",
    CTX_B4, 1085, 1087,
))
nuevas.append(mk(
    "debate-1-k-032", "keiko", "educacion", "compromiso",
    "Entregar 5 millones de kits escolares con mochilas, útiles, buzos y calzados hechos por las MYPE peruanas.",
    "Entregaremos 5 millones de kits escolares con mochilas, útiles, buzos, calzados hechos por nuestras MIPES",
    CTX_B4, 1088, 1093,
))
nuevas.append(mk(
    "debate-1-k-033", "keiko", "pensiones", "propuesta",
    "Recuperar el Pronaa para garantizar alimentación escolar de calidad con compras directas a productores locales.",
    "Recuperaremos el prona para garantizar alimentación escolar de calidad con compras directas a los productores locales",
    CTX_B4, 1094, 1098,
))
nuevas.append(mk(
    "debate-1-k-034", "keiko", "educacion", "compromiso",
    "Cumplir con la ley aprobada para saldar la deuda social a los maestros; defender al gremio, incluida la Derrama.",
    "vamos a cumplir con la ley aprobada para saldar la deuda social. A su vez, vamos a defender a su gremio, incluida a la derrama",
    CTX_B4, 1101, 1106,
))
nuevas.append(mk(
    "debate-1-k-035", "keiko", "educacion", "compromiso",
    "Duplicar y ampliar las becas para estudios técnicos requeridos por el mercado.",
    "Para nuestros jóvenes duplicaremos becapliaremos las becas a estudios técnicos requeridos por el mercado",
    CTX_B4, 1107, 1109,
))

# Roberto educación y salud
nuevas.append(mk(
    "debate-1-r-021", "roberto", "educacion", "cifra",
    "De cada 10 jóvenes que debieran ingresar a la universidad solo tres lo logran; 400,000 jóvenes egresan de secundaria sin acceso al derecho.",
    "De cada 10 jóvenes en el Perú que debieran ingresar a la universidad, solamente tres lo logran. 400,000 jóvenes egresan de la secundaria",
    CTX_B4, 1132, 1136,
))
nuevas.append(mk(
    "debate-1-r-022", "roberto", "educacion", "principio",
    "Convertir el derecho al ingreso a la universidad en un derecho libre y universal de manera estratificada.",
    "logrando y convirtiendo al derecho al ingreso a la universidad como un derecho libre universal",
    CTX_B4, 1149, 1153,
))
nuevas.append(mk(
    "debate-1-r-023", "roberto", "educacion", "propuesta",
    "Reconocer la deuda social de los maestros; piso mínimo de una UIT para maestros y homologación docente para maestros de educación superior.",
    "Tenemos que reconocer su deuda social que hasta ahora no se le paga. No puede ver un maestro que no gane mínimo una OIT en su piso de escala",
    CTX_B4, 1156, 1162,
))
nuevas.append(mk(
    "debate-1-r-024", "roberto", "salud", "compromiso",
    "Garantizar atención gratuita en primer nivel; construir 500 policlínicos para acceso; brigadas de salud al campo; un psicólogo por colegio.",
    "garantizar la atención gratuita en el primer nivel de atención. 500 policlínicos de Podemos hacer",
    CTX_B4, 1176, 1183,
))
nuevas.append(mk(
    "debate-1-r-025", "roberto", "salud", "compromiso",
    "Duplicar los Centros de Salud Mental Comunitarios y priorizar la salud mental como política de Estado.",
    "Debemos duplicar los centros de salud mental comunitarios. Yo soy psicólogo",
    CTX_B4, 1184, 1188,
))
nuevas.append(mk(
    "debate-1-r-026", "roberto", "salud", "compromiso",
    "Salud y educación como derechos fundamentales: inversión mínima 6% del PIB en educación; pasar de 6% al 9% en salud durante el periodo de gobierno.",
    "La educación no debe tener menos del 6% del PIB como aportación a la inversión. y en salud debemos ir escalados del 6 al 9 en nuestro periodo de gobierno",
    CTX_B4, 1193, 1198,
))

# Pregunta ciudadana SUNEDU + diálogo
CTX_B4_PREG = "Bloque 4 — Pregunta ciudadana sobre universidades públicas y SUNEDU"
nuevas.append(mk(
    "debate-1-r-027", "roberto", "economia", "cifra",
    "Cifras tributarias: evasión de impuestos del 9% del PIB (>S/ 90,000 millones anuales); presión tributaria peruana del 14% vs 22% en Latam.",
    "9% del PIB. Es increíble. Más de 90,000 millones de soles por año en evasión y elusión",
    CTX_B4_PREG, 1239, 1245,
))
nuevas.append(mk(
    "debate-1-r-028", "roberto", "economia", "propuesta",
    "Reforma tributaria profunda con visión solidaria para financiar programas sociales, salud y educación.",
    "necesitamos una profunda reforma tributaria con visión solidaria. Allí hay una oportunidad de cambio y lo vamos a hacer",
    CTX_B4_PREG, 1246, 1251,
))
nuevas.append(mk(
    "debate-1-k-036", "keiko", "educacion", "compromiso",
    "20,000 becas adicionales a jóvenes a través del programa Beca 18, financiadas reordenando gastos como los de Petroperú.",
    "más de 20,000 becas a los jóvenes a través del programa Beca1",
    CTX_B4_PREG, 1255, 1263,
))
nuevas.append(mk(
    "debate-1-r-029", "roberto", "salud", "propuesta",
    "Basta el DNI para el intercambio prestacional en los tres sistemas de salud.",
    "en salud debe de bastar el DNI para el intercambio prestacional en los tres sistemas de salud",
    CTX_B4_PREG, 1281, 1284,
))
nuevas.append(mk(
    "debate-1-r-030", "roberto", "deporte", "propuesta",
    "Aprovechar la ley que grava con impuestos las apuestas deportivas a distancia: más de S/ 100 millones para priorizar salud mental.",
    "Con la ley que ahora graba con impuestos a las apuestas deportivas, se tiene más de 100 millones de soles para poder priorizar la atención en salud mental",
    CTX_B4_PREG, 1411, 1415,
))
nuevas.append(mk(
    "debate-1-r-031", "roberto", "salud", "compromiso",
    "Rehabilitación integral de niños y niñas víctimas de violencia sexual como política de Estado y deuda social.",
    "La violencia sexual a niños, niñas, debe de ser asumido como una política de estado para rehabilitar integralmente",
    CTX_B4_PREG, 1417, 1421,
))
nuevas.append(mk(
    "debate-1-r-032", "roberto", "salud", "ataque",
    "Cierra recordando que el Perú no debe volver a las esterilizaciones masivas, 'vergonzoso legado del gobierno de Fujimori'.",
    "Nunca más un gobierno debe de caminar por las esterilizaciones masivas, que es un triste vergonzoso legado del gobierno de Fujimori",
    CTX_B4_PREG, 1422, 1426,
))
nuevas.append(mk(
    "debate-1-k-037", "keiko", "pensiones", "compromiso",
    "Bono de reconocimiento de S/ 500 mensuales a las mamitas de los clubes de madre, comedores populares y ollas comunes; recuperar el Pronaa para desayunos y almuerzos escolares de calidad.",
    "A ustedes les vamos a dar un bono de reconocimiento, 500 soles mensuales",
    CTX_B4_PREG, 1395, 1400,
))

# =====================================================================
# BLOQUE 5: ECONOMÍA, EMPLEO Y POBREZA (líneas 1435-1820)
# =====================================================================
CTX_B5 = "Bloque 5 — Economía, empleo y reducción de la pobreza"

# Roberto
nuevas.append(mk(
    "debate-1-r-033", "roberto", "trabajo", "cifra",
    "Canasta básica familiar debiera ser S/ 1,814 pero la RMV está en S/ 1,130; injusticia que se mitigará subiendo S/ 15 la RMV.",
    "La canasta básica familiar por el precio de los combustibles, la inflación debiera estar hoy día, por lo menos para mitigar en 1814 soles. ¿Y cuánto está la remuneración mínima vital? 1130",
    CTX_B5, 1461, 1466,
))
nuevas.append(mk(
    "debate-1-r-034", "roberto", "mype", "compromiso",
    "Fondo de S/ 15,000 millones para crédito barato con garantías y asistencia técnica para emprendedores, especialmente para la mujer emprendedora y microempresarios.",
    "vamos a formar un fondo de 15,000 millones de soles para crédito accesible de verdad, crédito barato con garantías",
    CTX_B5, 1475, 1481,
))
nuevas.append(mk(
    "debate-1-r-035", "roberto", "pensiones", "compromiso",
    "Reforzar Programa Juntos también para ciudades; en el primer año al menos 1 millón de familias con pensión contra la pobreza priorizando a la mujer cabeza de hogar.",
    "En el primer año, no menos de 1 millón de familias van a ser reconocidas con una pensión para luchar contra la pobreza",
    CTX_B5, 1494, 1502,
))
nuevas.append(mk(
    "debate-1-r-036", "roberto", "economia", "defensa",
    "Defensa contra el 'relato del miedo': no son comunistas, no expropiarán ahorros, respetarán autonomía del BCR y mantendrán a Julio Velarde.",
    "Nosotros no somos ni comunistas. Nosotros creemos en el trabajo, en el derecho a crecer, a tener riqueza",
    CTX_B5, 1505, 1518,
))
nuevas.append(mk(
    "debate-1-r-037", "roberto", "industria", "propuesta",
    "Industrializar y tecnificar el país para generar valor agregado; integrar pequeña agricultura y clusters como Gamarra a cadenas de valor.",
    "Si no industrializamos el país, seguiremos vendiendo piedras. Qué gran minería que vende piedras",
    CTX_B5, 1523, 1530,
))

# Keiko
nuevas.append(mk(
    "debate-1-k-038", "keiko", "economia", "principio",
    "La pobreza no se reduce con discursos, se reduce con empleo; cuando hubo estabilidad, inversión y empleo, millones salieron de la pobreza.",
    "La pobreza no se reduce con discursos, se reduce con empleo. El Perú ya lo demostró",
    CTX_B5, 1538, 1542,
))
nuevas.append(mk(
    "debate-1-k-039", "keiko", "economia", "propuesta",
    "Cuatro pilares: seguridad jurídica con autonomía del BCR; eliminar trabas reformando SUNAT y SUNAFIL; reactivar Promype; destrabar grandes proyectos.",
    "Para volver a crecer necesitamos un estado que haga cuatro cosas fundamentales. Primero, dar seguridad jurídica",
    CTX_B5, 1549, 1558,
))
nuevas.append(mk(
    "debate-1-k-040", "keiko", "transporte", "compromiso",
    "Destrabar grandes proyectos paralizados: Carretera Central, Aeropuerto Chinchero, represas, líneas de Metro 3-6, Tren Lima-Barranca, Gasoducto Surandino, Majes 2.",
    "destrabaremos los grandes proyectos paralizados. Carretera central, Aeropuerto Chinchero, las represas de Pocho y Chavimoc 3, líneas de metros 3, 4, 5 y 6",
    CTX_B5, 1565, 1573,
))
nuevas.append(mk(
    "debate-1-k-041", "keiko", "energia", "propuesta",
    "Reactivar el fondo de estabilización de combustibles para garantizar un precio estable.",
    "reactivaremos el fondo de estabilización, garantizando un precio estable",
    CTX_B5, 1581, 1583,
))

# Pregunta ciudadana MYPE + diálogo
CTX_B5_PREG = "Bloque 5 — Pregunta ciudadana sobre formalización MYPE"
nuevas.append(mk(
    "debate-1-k-042", "keiko", "mype", "compromiso",
    "Para la pequeña empresa: tributación cero los tres primeros años, licencia cero con una sola declaración jurada y créditos blandos garantizados por el Estado.",
    "para ellos decimos tributación cero, los tres primeros años, licencia cero, con una sola declaración jurada podrás abrir tu negocio",
    CTX_B5_PREG, 1625, 1632,
))
nuevas.append(mk(
    "debate-1-r-038", "roberto", "economia", "ataque",
    "Imputa al modelo el ser el 'más salvaje neoliberalismo de América Latina', con monopolios y oligopolios; no es economía social de mercado.",
    "Aquí hay un régimen en los medicamentos oligopolios. monopolios, no hay economía social de mercado, es un régimen el más salvaje, neoliberalismo de América Latina",
    CTX_B5_PREG, 1654, 1660,
))
nuevas.append(mk(
    "debate-1-r-039", "roberto", "agricultura", "compromiso",
    "Segunda Reforma Agraria para tecnificar a la pequeña agricultura; 2 millones de predios agrícolas abandonados.",
    "una segunda reforma agraria para tecnificar precisamente la pequeña agricultura. 2,000ones de predios agrícolas abandonados",
    CTX_B5_PREG, 1691, 1695,
))
nuevas.append(mk(
    "debate-1-k-043", "keiko", "economia", "compromiso",
    "Equipo económico con Carranza (exministro de Economía), Neuhaus (infraestructura) y Rafael Belaunde (minería); meta: pasar del 3% al 6% de crecimiento al fin del mandato.",
    "Con ellos nosotros vamos a nuevamente impulsar las cifras de crecimiento que hoy están en cerca de 3% y los dejaremos al culminar nuestro mandato en cifras del 6%",
    CTX_B5_PREG, 1712, 1716,
))
nuevas.append(mk(
    "debate-1-r-040", "roberto", "transporte", "compromiso",
    "Promover inversión: megapuerto de Chancay, tren bioceánico y carreteras para circular la Carretera Central como infraestructura para generar empleo.",
    "Nosotros promoveremos inversión, megapuerto de Chancay, el tren bioceánico, carreteras para circular la carretera central",
    CTX_B5_PREG, 1738, 1741,
))
nuevas.append(mk(
    "debate-1-k-044", "keiko", "agricultura", "compromiso",
    "Apoyo al pequeño agricultor: Foncodes y Pronamachs para reservorios y canales; semillas mejoradas, riego tecnificado y tractores; Pronaa repotenciado para comprar sobreproducción.",
    "volverán los programas de Foncodes Pronamach para la construcción de reservorios, canales de irrigación",
    CTX_B5, 1804, 1815,
))
nuevas.append(mk(
    "debate-1-k-045", "keiko", "turismo", "compromiso",
    "Meta: que el Perú vuelva a tener 5 millones de turistas; impulsar el turismo nacional y promover el presupuesto de PromPerú.",
    "Nuestra meta es que el Perú vuelva a tener 5 millones de turistas",
    CTX_B5_PREG, 1762, 1767,
))

# =====================================================================
# CARTA BLANCA / CIERRE (líneas 1832-1929)
# =====================================================================
CTX_CIERRE = "Carta Blanca — palabras finales"

nuevas.append(mk(
    "debate-1-r-041", "roberto", "constitucion", "ataque",
    "En 2011, 2016 y 2021 el Perú le cerró filas al fujimorismo y a su legado de horror; convocatoria a fuerzas patrióticas para recuperar el orden de verdad.",
    "El 2011, el 2016, el 2021, el Perú le cerró filas al fujimorismo y su legado de horror, como lo hará este 7 de junio",
    CTX_CIERRE, 1851, 1857,
))
nuevas.append(mk(
    "debate-1-r-042", "roberto", "constitucion", "principio",
    "Llamado a un gran consenso nacional: ninguna fuerza obtuvo mayoría en primera vuelta y el mensaje del pueblo es capacidad de hacer consensos.",
    "Nosotros creemos en la necesidad de un gran consenso nacional. En la primera vuelta, ninguna fuerza política ha obtenido a la mayoría",
    CTX_CIERRE, 1864, 1872,
))
nuevas.append(mk(
    "debate-1-k-046", "keiko", "constitucion", "compromiso",
    "Reconoce errores cometidos, dice haber aprendido y levantarse con más fuerza; pide ser presidenta para ejecutar las obras necesarias.",
    "Sé que a lo largo de mi vida política he cometido errores, de ellos aprendí, pero me levanté además con mucha más fuerza",
    CTX_CIERRE, 1900, 1916,
))
nuevas.append(mk(
    "debate-1-k-047", "keiko", "constitucion", "principio",
    "Aspira a gobernar 'con fuerza y con amor', dejar a los jóvenes un Perú en paz y con progreso, en un mensaje de reconciliación tras 30 años recorriendo el país.",
    "aspiro a gobernar con fuerza y con amor. Le pido al Señor que bendiga cada uno de sus hogares",
    CTX_CIERRE, 1924, 1929,
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
