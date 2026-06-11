# -*- coding: utf-8 -*-
"""Construye comparaciones plan_vs_debate.

Para cada declaración del debate se identifica si el candidato refuerza
una propuesta de su plan (CONSISTENTE), la amplía (AMPLIA_DEBATE), la
vaguea (VAGUEA), la contradice (CONTRADICE_DEBATE) o introduce algo
nuevo no contemplado en el plan (NUEVO_DEBATE).

También se incluye un conjunto curado de OMITE — propuestas-ancla del
plan que el candidato no mencionó en debates.

Numeración:
- cmp-pd-k-NNN para declaraciones de Keiko + OMITE de Keiko
- cmp-pd-r-NNN para declaraciones de Roberto + OMITE de Roberto
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


# Cada entrada:
# (declaracion_id_o_None, propuesta_id_o_None, relacion, analisis)
# Si relacion es OMITE: declaracion_id=None, propuesta_id=ID
# Si relacion es NUEVO_DEBATE: declaracion_id=ID, propuesta_id=None
# Resto: ambos no-null
MAPPINGS_KEIKO = [
    # --- DEBATE 1 — Keiko ---
    ("debate-1-k-001", "k-economia-001", "CONSISTENTE", "La visión país emprendedor del debate refuerza la propuesta-ancla del plan de Keiko sobre el potencial productivo nacional."),
    ("debate-1-k-002", "k-seguridad-005", "CONSISTENTE", "El compromiso de empleo y seguridad a 5 años repite el eje central del plan 'Perú con Orden'."),
    ("debate-1-k-003", "k-seguridad-001", "CONSISTENTE", "El diagnóstico de extorsiones, inseguridad y servicios deficientes coincide con el diagnóstico de seguridad del plan."),
    ("debate-1-k-004", "k-economia-001", "AMPLIA_DEBATE", "El binomio orden/caos personaliza y populariza el diagnóstico económico del plan, dándole carga retórica."),
    ("debate-1-k-005", "k-seguridad-001", "CONSISTENTE", "La narrativa de 'mundo al revés' refuerza el diagnóstico de inseguridad del plan."),
    ("debate-1-k-006", "k-seguridad-017", "AMPLIA_DEBATE", "El Plan de Pacificación Nacional con presencia policial-militar en buses metropolitanos especifica el Plan de Emergencia de 60 días del plan."),
    ("debate-1-k-007", "k-seguridad-019", "CONSISTENTE", "El rastreo financiero de extorsiones repite la estrategia de inteligencia financiera del plan."),
    ("debate-1-k-008", "k-seguridad-020", "CONSISTENTE", "Expulsión de migrantes ilegales que delinquen coincide con propuestas migratorias del plan."),
    ("debate-1-k-009", "k-seguridad-022", "CONSISTENTE", "Control fronterizo a cargo de FFAA es una propuesta explícita del plan."),
    ("debate-1-k-010", "k-justicia-002", "CONSISTENTE", "La cifra '5 de 10,000 denuncias' refuerza el diagnóstico de impunidad del plan."),
    ("debate-1-k-011", "k-justicia-003", "CONSISTENTE", "Las unidades de flagrancia como piedra angular son propuesta-ancla del plan."),
    ("debate-1-k-012", "k-seguridad-024", "CONSISTENTE", "Reforzar inteligencia contra la criminalidad replica el componente de inteligencia operativa del plan."),
    ("debate-1-k-013", "k-seguridad-017", "AMPLIA_DEBATE", "El detalle de implementación de comisarías y compra de patrulleros en 100 días concreta el Plan de Emergencia del plan."),
    ("debate-1-k-014", None, "NUEVO_DEBATE", "Defensa contextual ('Caos se escribe con C de Castillo') es una intervención debatística sin contraparte en el plan."),
    ("debate-1-k-015", None, "NUEVO_DEBATE", "El ataque puntual a Antauro Humala es retórica de debate, no figura en el plan."),
    ("debate-1-k-016", "k-seguridad-026", "AMPLIA_DEBATE", "La referencia a leyes específicas (32062, 32291) detalla y respalda la postura del plan sobre uso de fuerza."),
    ("debate-1-k-017", "k-seguridad-005", "CONSISTENTE", "El modelo histórico anti-terrorismo (FFAA, PNP, rondas) replica el modelo de prevención temprana del plan."),
    ("debate-1-k-018", None, "NUEVO_DEBATE", "Mención a sus acompañantes (Miyashiro, Astudillo) y descalificación a Antauro son retórica de debate."),
    ("debate-1-k-019", "k-agua-001", "CONSISTENTE", "La cifra '45% sin agua ni títulos' refuerza el diagnóstico de servicios básicos del plan."),
    ("debate-1-k-020", "k-agua-006", "CONSISTENTE", "Esquemas de agua, ramal sur, desalinizadoras, reservorios y pozos son propuestas explícitas del plan."),
    ("debate-1-k-021", "k-vivienda-007", "AMPLIA_DEBATE", "El compromiso de 1 millón de títulos en 5 años especifica el programa de Cofopri del plan."),
    ("debate-1-k-022", "k-transporte-002", "CONSISTENTE", "El Programa Nacional de Interconexión Vial replica el plan de carreteras y trochas del plan."),
    ("debate-1-k-023", "k-ambiente-008", "CONSISTENTE", "Limpieza de ríos y maquinaria pesada coincide con las medidas anti-FEN del plan."),
    ("debate-1-k-024", "k-educacion-005", "CONSISTENTE", "Mejorar currícula y combatir ausencia del Estado en Amazonía coincide con el enfoque del plan."),
    ("debate-1-k-025", "k-transporte-005", "AMPLIA_DEBATE", "La especificación de carreteras concretas (Panamericana 4 vías, Libertadores, penetración) detalla el plan vial."),
    ("debate-1-k-026", None, "NUEVO_DEBATE", "Convocatoria a personeros y observadores internacionales para defender el voto no está en el plan."),
    ("debate-1-k-027", "k-salud-002", "CONSISTENTE", "Las cifras del vía crucis oncológico refuerzan el diagnóstico de salud del plan."),
    ("debate-1-k-028", "k-salud-002", "CONSISTENTE", "La cifra de 46% anemia infantil refuerza el diagnóstico nutricional del plan."),
    ("debate-1-k-029", "k-salud-005", "CONSISTENTE", "Telemedicina y fondo de enfermedades de alto costo son propuestas-ancla del plan."),
    ("debate-1-k-030", "k-salud-008", "AMPLIA_DEBATE", "Plan gratuito en los primeros 1,000 días especifica el enfoque de primera infancia del plan."),
    ("debate-1-k-031", "k-educacion-006", "AMPLIA_DEBATE", "El compromiso específico de 5,000 colegios da magnitud al plan general de infraestructura educativa."),
    ("debate-1-k-032", "k-educacion-009", "AMPLIA_DEBATE", "Los 5 millones de kits escolares concretan la propuesta de apoyo escolar del plan vinculado a MYPE."),
    ("debate-1-k-033", "k-pensiones-008", "CONSISTENTE", "Recuperar Pronaa con compras directas a productores coincide con el modelo de programas sociales del plan."),
    ("debate-1-k-034", "k-educacion-013", "CONSISTENTE", "Saldar deuda social y defender al gremio docente coincide con la propuesta magisterial del plan."),
    ("debate-1-k-035", "k-educacion-015", "CONSISTENTE", "Duplicar becas técnicas concuerda con la propuesta de Beca 18 del plan."),
    ("debate-1-k-036", "k-educacion-015", "AMPLIA_DEBATE", "Cifra concreta '20,000 becas adicionales' especifica el compromiso del plan."),
    ("debate-1-k-037", "k-pensiones-011", "AMPLIA_DEBATE", "El bono de S/ 500 mensuales a mamitas detalla la propuesta de reconocimiento del plan social."),
    ("debate-1-k-038", "k-economia-008", "CONSISTENTE", "'La pobreza se reduce con empleo' replica la tesis central de empleo del plan."),
    ("debate-1-k-039", "k-economia-009", "CONSISTENTE", "Los cuatro pilares (seguridad jurídica, eliminar trabas, Promype, destrabar grandes proyectos) coinciden con el plan económico."),
    ("debate-1-k-040", "k-transporte-002", "AMPLIA_DEBATE", "La lista específica de obras paralizadas (Carretera Central, Chinchero, líneas Metro, etc.) detalla el plan de infraestructura."),
    ("debate-1-k-041", "k-energia-007", "CONSISTENTE", "Reactivar el fondo de estabilización de combustibles está en el plan energético."),
    ("debate-1-k-042", "k-mype-005", "AMPLIA_DEBATE", "Tributación cero por 3 años + licencia cero con sola declaración jurada especifica el régimen MYPE del plan."),
    ("debate-1-k-043", None, "NUEVO_DEBATE", "Mención del equipo económico (Carranza, Neuhaus, Belaunde) y cifra 3%→6% son retórica del debate, sin equivalente en el plan."),
    ("debate-1-k-044", "k-agricultura-002", "CONSISTENTE", "Foncodes y Pronamachs para reservorios y canales coincide con el plan agrario."),
    ("debate-1-k-045", "k-turismo-001", "AMPLIA_DEBATE", "La meta de 5 millones de turistas especifica numéricamente la propuesta turística del plan."),
    ("debate-1-k-046", None, "NUEVO_DEBATE", "Reconocimiento de errores y pedido del voto en cierre — emoción de campaña sin contraparte programática en el plan."),
    ("debate-1-k-047", None, "NUEVO_DEBATE", "Aspiración a gobernar 'con fuerza y con amor' es lenguaje de cierre, no programa."),

    # --- DEBATE 2 — Keiko ---
    ("debate-2-k-001", "k-economia-001", "CONSISTENTE", "El caos como ineficiencia replica el diagnóstico macro del plan."),
    ("debate-2-k-002", "k-economia-014", "AMPLIA_DEBATE", "Convertir la Presidencia en Centro de Gobierno estratégico amplía la propuesta de reforma del Ejecutivo."),
    ("debate-2-k-003", "k-economia-014", "CONSISTENTE", "Centro de gestión estratégica articulando instituciones replica la propuesta de modernización del Estado del plan."),
    ("debate-2-k-004", "k-economia-014", "AMPLIA_DEBATE", "Digitalización en los tres niveles especifica la propuesta de modernización del plan."),
    ("debate-2-k-005", "k-juventud-001", "CONSISTENTE", "Diagnóstico de jóvenes como 30% de la población más golpeada coincide con el plan."),
    ("debate-2-k-006", "k-juventud-002", "CONSISTENTE", "Modernización de educación técnica replica propuesta del plan de Keiko sobre juventud."),
    ("debate-2-k-007", "k-juventud-003", "CONSISTENTE", "Repotenciar Jóvenes Productivos con alianzas empresariales está en el plan."),
    ("debate-2-k-008", "k-deporte-002", "AMPLIA_DEBATE", "Que IPD pase a la PCM como propuesta institucional especifica el plan deportivo."),
    ("debate-2-k-009", "k-juventud-001", "AMPLIA_DEBATE", "Centros de Oportunidad y Orientación Local (COL) son una concreción operativa del plan."),
    ("debate-2-k-010", "k-juventud-006", "CONSISTENTE", "Prácticas como experiencia laboral y voluntariado como créditos están en el plan."),
    ("debate-2-k-011", "k-deporte-005", "AMPLIA_DEBATE", "Incluir el deporte en la Ley de Obras por Impuestos es un detalle no explícito en el plan pero compatible."),
    ("debate-2-k-012", "k-agricultura-002", "CONSISTENTE", "Saludo a 2.2 millones de agricultores reproduce el diagnóstico agrario del plan."),
    ("debate-2-k-013", "k-agricultura-003", "CONSISTENTE", "Reactivar PRONAMACHCS para reservorios y zanjas es propuesta directa del plan."),
    ("debate-2-k-014", "k-agua-002", "AMPLIA_DEBATE", "Maquinaria pesada a 127 juntas de usuarios de agua especifica la propuesta hídrica."),
    ("debate-2-k-015", "k-agricultura-004", "AMPLIA_DEBATE", "Asistencia técnica con foco en banano, café, papa y arroz detalla el plan agrario."),
    ("debate-2-k-016", "k-agua-005", "AMPLIA_DEBATE", "Lista específica de represas (Chonta, Cachi, Majes-Siguas 2) concreta el plan hídrico."),
    ("debate-2-k-017", "k-agricultura-006", "AMPLIA_DEBATE", "Entrega de 5,000 tractores especifica numéricamente el plan de mecanización agraria."),
    ("debate-2-k-018", "k-ambiente-006", "CONSISTENTE", "Combatir minería ilegal con tecnología satelital y drones es propuesta-ancla del plan."),
    ("debate-2-k-019", "k-transporte-001", "AMPLIA_DEBATE", "Cifra '2,241 obras paralizadas, S/ 73,000M' cuantifica el diagnóstico del plan."),
    ("debate-2-k-020", "k-transporte-002", "CONSISTENTE", "Carreteras, puertos, aeropuertos y corredores logísticos coinciden con el plan vial."),
    ("debate-2-k-021", "k-transporte-007", "AMPLIA_DEBATE", "Reactivar obras paralizadas judicializadas mediante corte de contratos detalla cómo se ejecutará el plan."),
    ("debate-2-k-022", "k-transporte-008", "AMPLIA_DEBATE", "Vehículos eléctricos subsidiados como meta es propuesta concordante y más específica que el plan."),
    ("debate-2-k-023", "k-pensiones-001", "CONSISTENTE", "Cifras de pobreza coinciden con el diagnóstico social del plan."),
    ("debate-2-k-024", "k-economia-001", "AMPLIA_DEBATE", "Tres pilares (orden económico, capitalismo popular, orden social) son una formalización del plan."),
    ("debate-2-k-025", "k-mype-005", "CONSISTENTE", "Créditos garantizados por banco de desarrollo es propuesta del plan MYPE."),
    ("debate-2-k-026", "k-mype-005", "CONSISTENTE", "Inversión privada + eficiencia del Estado para reducir trámites coincide con el plan MYPE."),
    ("debate-2-k-027", None, "NUEVO_DEBATE", "Ataque puntual con cifras 2022 y 2023 es contraargumento de debate sin contraparte en plan."),
    ("debate-2-k-028", "k-economia-009", "AMPLIA_DEBATE", "Regla fiscal para regresar al déficit 1% y crecimiento 67% al 2028 detalla el plan macro."),
    ("debate-2-k-029", "k-salud-002", "AMPLIA_DEBATE", "Cifras detalladas (1 de 2 niños con anemia, 4 de 10 sin vacunas, 9 de 10 establecimientos abandonados) refuerzan el diagnóstico."),
    ("debate-2-k-030", "k-salud-002", "AMPLIA_DEBATE", "Estadística de 10 ministros y 12 presidentes de salud especifica la crisis de gestión."),
    ("debate-2-k-031", "k-salud-008", "AMPLIA_DEBATE", "Mapeo casa por casa de niños y gestantes detalla el plan de primera infancia."),
    ("debate-2-k-032", "k-salud-002", "AMPLIA_DEBATE", "Cifra '97% establecimientos deteriorados' y 'Piura 7 hospitales malas condiciones' cuantifica el diagnóstico."),
    ("debate-2-k-033", "k-salud-005", "CONSISTENTE", "Red de telemedicina y brigadas de salud son propuestas-ancla del plan."),
    ("debate-2-k-034", None, "NUEVO_DEBATE", "Reflexión 'no es derechas ni izquierdas, es orden vs caos' es cierre retórico, no programa."),

    # --- OMITE — Keiko (propuestas ALTA importantes no mencionadas en debate) ---
    (None, "k-corrupcion-005", "OMITE", "Fortalecer la Procuraduría General es propuesta ALTA del plan de Keiko pero no fue mencionada en ningún debate."),
    (None, "k-mineria-002", "OMITE", "Destrabar proyectos mineros con ventanilla única es propuesta clave del plan pero ausente en debates."),
    (None, "k-pesca-003", "OMITE", "Fortalecer industria de harina de pescado y exportación pesquera no fue desarrollada en debates."),
    (None, "k-ambiente-005", "OMITE", "El respaldo a la flexibilización forestal del plan no fue defendido explícitamente en debate."),
]

MAPPINGS_ROBERTO = [
    # --- DEBATE 1 — Roberto ---
    ("debate-1-r-001", "r-economia-002", "CONSISTENTE", "Diagnóstico de pobreza, desnutrición y violencia sexual a niñas refuerza el 'primer gran mal' (desigualdad) del plan."),
    ("debate-1-r-002", "r-constitucion-001", "CONSISTENTE", "Imputación de dictadura congresal a Keiko coincide con el 'cuarto gran mal' (abuso de poder) del plan."),
    ("debate-1-r-003", "r-educacion-001", "CONSISTENTE", "Biografía como hijo de educación pública refuerza el principio educativo del plan."),
    ("debate-1-r-004", "r-justicia-002", "CONSISTENTE", "Acusación al fujimorismo por secuestrar la democracia coincide con el diagnóstico de DDHH del plan."),
    ("debate-1-r-005", "r-seguridad-001", "CONSISTENTE", "Cifras de criminalidad y transportistas asesinados refuerzan el diagnóstico de inseguridad del plan."),
    ("debate-1-r-006", "r-seguridad-006", "CONSISTENTE", "Imputación al Congreso por 'leyes pro-crimen' coincide con la propuesta de derogación del plan."),
    ("debate-1-r-007", "r-seguridad-007", "CONSISTENTE", "Limpiar PNP, profesionalizar e inteligencia coinciden con la reforma estructural del plan."),
    ("debate-1-r-008", "r-seguridad-006", "AMPLIA_DEBATE", "El reto público a Keiko sobre derogación de leyes procrimen amplifica retóricamente la propuesta."),
    ("debate-1-r-009", "r-corrupcion-006", "AMPLIA_DEBATE", "Muerte civil para funcionarios corruptos es endurecimiento del enfoque anticorrupción del plan."),
    ("debate-1-r-010", "r-seguridad-011", "CONSISTENTE", "Convocatoria a fuerzas patrióticas (ronderos, comunidades campesinas) es propuesta-ancla del plan."),
    ("debate-1-r-011", "r-seguridad-008", "CONSISTENTE", "Reforma para que FFAA puedan apoyar excepcionalmente a PNP coincide con la propuesta del plan."),
    ("debate-1-r-012", "r-justicia-007", "AMPLIA_DEBATE", "Imputación específica de 50+ asesinatos detalla la propuesta de Comisión de la Verdad del plan."),
    ("debate-1-r-013", "r-constitucion-003", "CONSISTENTE", "Régimen semipresidencialista subvertido refuerza el diagnóstico constitucional del plan."),
    ("debate-1-r-014", "r-constitucion-005", "CONSISTENTE", "Recuperar el referéndum y fuerzas patrióticas para reforma constitucional es propuesta-ancla."),
    ("debate-1-r-015", "r-orden_juridico-011", "CONSISTENTE", "Descentralización a centros poblados menores coincide con el plan de descentralización."),
    ("debate-1-r-016", "r-exterior-031", "CONSISTENTE", "Acuerdo de Escazú y fortalecimiento del SIDH son propuestas-ancla del plan exterior."),
    ("debate-1-r-017", "r-cultura-005", "CONSISTENTE", "Lucha contra la discriminación como política de Estado es propuesta del plan cultural."),
    ("debate-1-r-018", "r-justicia-007", "AMPLIA_DEBATE", "Cifra '56 asesinados en el sur' especifica la propuesta de Comisión de la Verdad del plan."),
    ("debate-1-r-019", "r-exterior-036", "CONSISTENTE", "Compromiso con el SIDH y Pacto de San José replica el plan exterior."),
    ("debate-1-r-020", "r-constitucion-005", "AMPLIA_DEBATE", "Convocatoria al consenso nacional para estado democrático refuerza la propuesta constitucional."),
    ("debate-1-r-021", "r-educacion-005", "CONSISTENTE", "Cifras '3 de 10 ingresan a universidad, 400k egresan sin acceso' refuerzan el diagnóstico educativo."),
    ("debate-1-r-022", "r-constitucion-013", "AMPLIA_DEBATE", "Convertir el ingreso universitario en derecho universal estratificado especifica la propuesta constitucional sobre educación."),
    ("debate-1-r-023", "r-educacion-015", "CONSISTENTE", "Piso de 1 UIT para maestros y homologación docente coincide con la Carrera Pública Magisterial del plan."),
    ("debate-1-r-024", "r-salud-012", "AMPLIA_DEBATE", "500 policlínicos y brigadas de salud detallan la propuesta de atención primaria del plan."),
    ("debate-1-r-025", "r-salud-015", "CONSISTENTE", "Duplicar Centros de Salud Mental Comunitaria es propuesta-ancla del plan."),
    ("debate-1-r-026", "r-salud-009", "CONSISTENTE", "Inversión 6% PBI en educación y escalar a 9% en salud coincide con las metas presupuestales del plan."),
    ("debate-1-r-027", "r-economia-009", "CONSISTENTE", "Cifras de evasión 9% PBI y presión tributaria 14% refuerzan el diagnóstico del plan."),
    ("debate-1-r-028", "r-economia-008", "CONSISTENTE", "Reforma tributaria solidaria para financiar lo social es propuesta del plan."),
    ("debate-1-r-029", "r-salud-006", "CONSISTENTE", "DNI para intercambio prestacional entre sistemas de salud coincide con la integración del plan."),
    ("debate-1-r-030", "r-deporte-009", "AMPLIA_DEBATE", "Aprovechar la ley de apuestas deportivas para salud mental especifica el financiamiento del plan."),
    ("debate-1-r-031", "r-salud-016", "AMPLIA_DEBATE", "Rehabilitación de víctimas de violencia sexual amplía el componente de salud sexual del plan."),
    ("debate-1-r-032", "r-justicia-007", "CONSISTENTE", "Crítica a esterilizaciones masivas refuerza el plan de Verdad y Justicia."),
    ("debate-1-r-033", "r-trabajo-008", "CONSISTENTE", "Canasta básica S/ 1,814 vs RMV S/ 1,130 con incremento de S/ 15 refuerza la meta de RMV S/ 1,500 del plan."),
    ("debate-1-r-034", "r-industria-006", "CONSISTENTE", "Fondo S/ 15,000M de garantía pública es propuesta-ancla del plan industrial (Financiamiento Popular)."),
    ("debate-1-r-035", "r-pensiones-006", "CONSISTENTE", "Reforzar Juntos y al menos 1M de familias con pensión coincide con el plan de pensiones."),
    ("debate-1-r-036", "r-economia-011", "CONSISTENTE", "Defensa de autonomía del BCRP y Julio Velarde repite el plan económico."),
    ("debate-1-r-037", "r-industria-003", "CONSISTENTE", "Industrializar y tecnificar el país es el corazón del plan económico de Roberto."),
    ("debate-1-r-038", "r-economia-021", "AMPLIA_DEBATE", "'Neoliberalismo salvaje' con monopolios y oligopolios amplía la crítica al modelo del plan."),
    ("debate-1-r-039", "r-agricultura-001", "AMPLIA_DEBATE", "Segunda Reforma Agraria con 2M de predios abandonados especifica el diagnóstico agrario del plan."),
    ("debate-1-r-040", "r-mineria-016", "AMPLIA_DEBATE", "Megapuerto de Chancay, tren bioceánico y carreteras especifican propuestas-ancla del plan."),
    ("debate-1-r-041", "r-constitucion-001", "CONSISTENTE", "Cerrarle filas al fujimorismo en 2011, 2016, 2021 refuerza el 'cuarto gran mal' del plan."),
    ("debate-1-r-042", "r-constitucion-006", "AMPLIA_DEBATE", "Necesidad de gran consenso nacional articula el plan de unidad política."),

    # --- DEBATE 2 — Roberto ---
    ("debate-2-r-001", "r-constitucion-004", "CONSISTENTE", "Régimen parlamentarista de facto desde 2016 refuerza el diagnóstico constitucional del plan."),
    ("debate-2-r-002", "r-constitucion-004", "CONSISTENTE", "Congreso concentrando todos los poderes coincide con diagnóstico de dictadura parlamentaria del plan."),
    ("debate-2-r-003", "r-economia-007", "CONSISTENTE", "Presión tributaria 14% vs 22% LATAM coincide con el diagnóstico tributario del plan."),
    ("debate-2-r-004", "r-corrupcion-002", "AMPLIA_DEBATE", "Cifra 50% parlamentarios acusados detalla el diagnóstico del copamiento del Estado."),
    ("debate-2-r-005", "r-constitucion-014", "CONSISTENTE", "Autonomía de JNJ, TC y Defensoría es propuesta-ancla del plan constitucional."),
    ("debate-2-r-006", "r-orden_juridico-008", "CONSISTENTE", "Distribución desigual del Estado refuerza el diagnóstico de descentralización del plan."),
    ("debate-2-r-007", "r-constitucion-013", "CONSISTENTE", "Bienes públicos de calidad para todos (educación, salud, seguridad, justicia) coincide con propuesta de derechos constitucionales."),
    ("debate-2-r-008", "r-orden_juridico-002", "CONSISTENTE", "Evaluación por resultados y crítica a 8 presidentes en 10 años replica el plan."),
    ("debate-2-r-009", "r-juventud-001", "AMPLIA_DEBATE", "Cifra 1.6M de jóvenes sin oportunidades detalla el diagnóstico juvenil."),
    ("debate-2-r-010", "r-juventud-004", "CONSISTENTE", "Mi Primera Chamba con bono S/ 6,150 es propuesta-ancla del plan juvenil."),
    ("debate-2-r-011", "r-constitucion-013", "CONSISTENTE", "Reconocer educación superior como derecho constitucional replica propuesta del plan."),
    ("debate-2-r-012", "r-educacion-016", "AMPLIA_DEBATE", "Ampliar becas del Estado a 30,000 con foco en zonas rurales detalla la propuesta de Beca 18 del plan."),
    ("debate-2-r-013", None, "NUEVO_DEBATE", "Lima 2027 como evento más importante del país y Casa Futuro no figuran como propuesta-ancla en el plan."),
    ("debate-2-r-014", "r-salud-015", "CONSISTENTE", "Un psicólogo por escuela como iniciativa parlamentaria de Roberto refuerza el plan de salud mental."),
    ("debate-2-r-015", "r-juventud-003", "CONSISTENTE", "Programa AYNI de voluntariado juvenil es propuesta-ancla del plan."),
    ("debate-2-r-016", "r-agricultura-002", "CONSISTENTE", "Dos caras (agroexportador con privilegios vs familiar abandonada) repite el diagnóstico del plan."),
    ("debate-2-r-017", "r-agua-005", "CONSISTENTE", "Soberanía y seguridad hídrica con Programa/Fondo Nacional de Agua coincide con el plan."),
    ("debate-2-r-018", "r-agricultura-009", "CONSISTENTE", "Banco de Desarrollo Agropecuario con 1M productores en 100 días replica el Nuevo Banco Agrario/AgroPatria del plan."),
    ("debate-2-r-019", "r-industria-008", "AMPLIA_DEBATE", "Planta de urea y fosfatos de Bayóvar como industrialización especifica el Sistema Industrial del plan."),
    ("debate-2-r-020", "r-ambiente-013", "CONSISTENTE", "Derogar Ley Antiforestal es propuesta-ancla del plan ambiental."),
    ("debate-2-r-021", "r-agua-007", "AMPLIA_DEBATE", "Programa nacional de presas altoandinas y trabajo con 127 juntas + 2,500 comisiones + 10,000 comités detalla el plan hídrico."),
    ("debate-2-r-022", "r-agricultura-012", "AMPLIA_DEBATE", "Brecha de infraestructura de riego de S/ 14,000M concreta el plan agrario."),
    ("debate-2-r-023", "r-ambiente-013", "CONSISTENTE", "Crítica a FP por aprobar Ley Antiforestal refuerza la propuesta de derogarla."),
    ("debate-2-r-024", "r-economia-001", "AMPLIA_DEBATE", "Cifra 20% crecimiento inversión pública en 2021 sostiene el plan económico."),
    ("debate-2-r-025", "r-transporte-006", "CONSISTENTE", "Bioceánico Chancay-Pucallpa-Brasil-China replica la propuesta-ancla del plan."),
    ("debate-2-r-026", "r-energia-009", "AMPLIA_DEBATE", "Ducto Camisea-Cuzco como alternativa al Gasoducto del Sur diverge en detalle del plan (que mantiene SITGAS) sin contradecirlo, especificando una etapa adicional."),
    ("debate-2-r-027", "r-transporte-011", "AMPLIA_DEBATE", "Pavimentación 8,000 km + 12,000 km mejorados + 30,000 km bajo costo detalla la propuesta vial rural del plan."),
    ("debate-2-r-028", "r-transporte-001", "AMPLIA_DEBATE", "Diagnóstico de caos del transporte urbano por decretos de los 90s amplía el diagnóstico del plan."),
    ("debate-2-r-029", "r-transporte-002", "AMPLIA_DEBATE", "Inestabilidad política magnificando obras paralizadas amplía el diagnóstico de gestión."),
    ("debate-2-r-030", "r-transporte-005", "AMPLIA_DEBATE", "Priorizar Línea 3 + cercanías norte-sur a Barranca e Ica especifica el plan ferroviario."),
    ("debate-2-r-031", "r-transporte-016", "CONSISTENTE", "Subsidios al transporte urbano son propuesta-ancla del plan."),
    ("debate-2-r-032", "r-energia-014", "AMPLIA_DEBATE", "Pasar de S/ 2.4M a S/ 11M anuales en electrificación rural detalla el plan energético."),
    ("debate-2-r-033", "r-economia-012", "CONSISTENTE", "Meta de crecimiento 6% PBI replica el plan económico."),
    ("debate-2-r-034", "r-seguridad-006", "CONSISTENTE", "Derogar las 8 leyes pro-crimen es propuesta-ancla del plan."),
    ("debate-2-r-035", "r-industria-006", "CONSISTENTE", "Financiamiento Popular S/ 15,000M para MYPEs es propuesta-ancla del plan."),
    ("debate-2-r-036", "r-economia-011", "CONSISTENTE", "Autonomía del BCR y Julio Velarde + metas de déficit fiscal replican el plan macro."),
    ("debate-2-r-037", "r-energia-007", "CONSISTENTE", "Reactivar fondo de estabilización de combustibles coincide con el plan energético."),
    ("debate-2-r-038", "r-industria-003", "CONSISTENTE", "Incentivar inversión privada en industria, agroindustria y agricultura replica el plan industrial."),
    ("debate-2-r-039", "r-trabajo-009", "AMPLIA_DEBATE", "Cifra 300,000 empleos en 6 meses como ministro Francke sostiene el compromiso de 1M empleos del plan."),
    ("debate-2-r-040", "r-educacion-016", "AMPLIA_DEBATE", "Ataque sobre el Congreso negando S/ 120M para becas refuerza el plan de Beca 18."),
    ("debate-2-r-041", "r-agricultura-002", "CONSISTENTE", "S/ 20,000M de exoneración a agroexportadores que financian campaña FP coincide con el diagnóstico del plan agrario."),
    ("debate-2-r-042", "r-salud-006", "CONSISTENTE", "Salud como derecho fundamental garantizado por el Estado es propuesta-ancla."),
    ("debate-2-r-043", "r-salud-003", "CONSISTENTE", "250,000 muertes COVID por sistema excluyente refuerza el diagnóstico de salud del plan."),
    ("debate-2-r-044", "r-justicia-002", "CONSISTENTE", "Crítica al fujimorismo por hegemonía en el Congreso coincide con el diagnóstico institucional."),
    ("debate-2-r-045", "r-salud-019", "AMPLIA_DEBATE", "Financiar salud sin exoneraciones tributarias detalla la financiación del plan de salud universal."),
    ("debate-2-r-046", "r-energia-005", "AMPLIA_DEBATE", "S/ 30,000M a Petroperú vs prioridad salud invierte la jerarquía de gasto. Sostiene el plan de salud reorientando recursos."),
    ("debate-2-r-047", "r-salud-015", "CONSISTENTE", "1,000+ establecimientos de salud mental coincide con la propuesta del plan."),
    ("debate-2-r-048", "r-justicia-007", "CONSISTENTE", "Crítica por 70 muertes y exoneración a Boluarte refuerza la propuesta de Comisión de la Verdad."),
    ("debate-2-r-049", "r-constitucion-005", "CONSISTENTE", "Construir país lejos de mafias y corrupción refuerza el espíritu del plan constitucional."),

    # --- OMITE — Roberto (propuestas ALTA importantes no mencionadas en debate) ---
    (None, "r-ambiente-019", "OMITE", "Plan Nacional de Restauración Ambiental con 500,000 ha es propuesta ALTA del plan pero no fue mencionada en debates."),
    (None, "r-indigenas-003", "OMITE", "Escaños reservados para pueblos originarios en el Congreso no fueron mencionados en debates."),
    (None, "r-genero-010", "OMITE", "Despenalización del aborto en casos de violencia sexual y riesgo de la madre, propuesta sensible, no fue mencionada en debates."),
    (None, "r-cultura-007", "OMITE", "Creación del Ministerio de Las Culturas no fue mencionada en debates."),
    (None, "r-cti-003", "OMITE", "Creación del Ministerio de Ciencia y Tecnología no fue mencionada en debates."),
]


def main():
    d = json.loads(RUTA.read_text(encoding="utf-8"))
    print(f"Antes plan_vs_debate: {len(d['plan_vs_debate'])}")

    nuevas = []
    # Keiko: numeración secuencial
    for i, (decl_id, prop_id, rel, analisis) in enumerate(MAPPINGS_KEIKO, start=1):
        nuevas.append({
            "id": f"cmp-pd-k-{i:03d}",
            "candidato": "keiko",
            "propuesta_id": prop_id,
            "declaracion_id": decl_id,
            "relacion": rel,
            "analisis": analisis,
        })
    # Roberto
    for i, (decl_id, prop_id, rel, analisis) in enumerate(MAPPINGS_ROBERTO, start=1):
        nuevas.append({
            "id": f"cmp-pd-r-{i:03d}",
            "candidato": "roberto",
            "propuesta_id": prop_id,
            "declaracion_id": decl_id,
            "relacion": rel,
            "analisis": analisis,
        })

    print(f"Nuevas a agregar: {len(nuevas)}")
    d["plan_vs_debate"].extend(nuevas)
    RUTA.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Despues plan_vs_debate: {len(d['plan_vs_debate'])}")
    print("OK escrito.")


if __name__ == "__main__":
    main()
