# -*- coding: utf-8 -*-
"""Contenido de las landings 2027 de OSDEPYM.

TODO lo que hay acá sale de una de estas tres fuentes, y nada se inventa:

  (1) El export de WordPress del 26/11/2026 (landingpm.osdepym.com.ar).
      Las prestaciones, los textos de la app, Viví+ y los id de formulario
      de Bitrix24 son los que están hoy publicados.
  (2) El Documento Brand Life OSDEPYM (septiembre 2026, 52 láminas) y su
      Bajada a Conceptos (octubre 2026). De ahí salen el propósito, el
      diferencial de las cuatro dimensiones, los mensajes clave, el tono
      y los titulares de campaña ya aprobados.
  (3) La sección DUAL aprobada para las landings (noviembre 2026).

Cuando una fuente no dice algo, acá no figura. Es la regla que viene de la
landing del QR: no prometer disponibilidad que OSDEPYM no controla.
"""

# --------------------------------------------------------------- la marca

MARCA = {
    "nombre": "OSDEPYM",
    "firma": "Te estamos cuidando",
    "telefono": "0800-288-8432",
    "telefono_crudo": "08002888432",
    "razon": "Obra Social de Empresarios, Profesionales y Monotributistas",
    "domicilio": "Reconquista 458, 2º piso · Ciudad de Buenos Aires",
    "tel_admin": "(011) 5288-5600",
    "rnos": "4-0170-4",
    "rnemp": "614869",
    "sss": "Superintendencia de Servicios de Salud · 0800-222-72583 · www.sssalud.gob.ar",
    "trayectoria": "Más de 55 años",
}

# Lámina 9. Es la frase que ordena todo el sitio.
PROPOSITO = ("OSDEPYM genera las condiciones para que las personas vivan, "
             "trabajen y se desarrollen plenamente.")

# Lámina 37, mensaje clave 1. Se usa como H1 de la home: es la bajada
# literal del territorio de accesibilidad y ya está aprobada.
MENSAJE_1 = "Una buena cobertura en salud no es un privilegio de pocos."

# Lámina 17.
DIFERENCIAL = ("OSDEPYM incorpora dimensiones económicas, profesionales, "
               "emocionales y sociales porque entiende que la salud va "
               "más allá de lo físico.")

# --------------------------------------------- las cuatro dimensiones (l.18)
# El orden es el de la lámina. "Cobertura de accidentes personales" figuraba
# como próximamente: ya salió, es DUAL, así que se nombra como disponible.

DIMENSIONES = [
    {
        "clave": "economica",
        "titulo": "Económica",
        "bajada": "Que la salud entre en el presupuesto, sin letra chica.",
        "icono": "peso",
        "items": [
            ("Precio accesible", True),
            ("Cobertura de accidentes personales (DUAL)", True),
        ],
    },
    {
        "clave": "profesional",
        "titulo": "Profesional",
        "bajada": "Que tu trabajo también tenga quien lo acompañe.",
        "icono": "sello",
        "items": [
            ("Escuela de Emprendedores", True),
        ],
    },
    {
        "clave": "social",
        "titulo": "Social",
        "bajada": "Que la cobertura se note fuera del consultorio.",
        "icono": "persona",
        "items": [
            ("Escuela de Emprendedores", True),
            ("Viví más OSDEPYM", True),
        ],
    },
    {
        "clave": "emocional",
        "titulo": "Emocional",
        "bajada": "Que lo que te importa esté contemplado.",
        "icono": "corazon",
        "items": [
            ("Centro para la mujer", True),
            ("Cobertura de mascotas", False),
        ],
    },
]

# ------------------------------------------------------------- los planes
# Los id de Bitrix24 son los del export: cada página tiene el suyo y es así
# como Comercial atribuye la fuente. Son variables de página, no del sistema.

# ---------------------------------------------- formularios de Bitrix24
# Tabla que pasó Comercial el 27/11/2026. Hay UN formulario por landing y
# por fuente de tráfico: esa numeración ES la atribución. El `ref` lleva
# número Y hash: sin el hash el script carga pero no se engancha.

FUENTES = {
    "mads": "Meta Ads",
    "gads": "Google Ads",
    "pmax": "Performance Max",
    "tads": "TikTok Ads",
    "org":  "Orgánico",
}

# fuente, plan -> (ref, utm, página de gracias)
FORMULARIOS = {
    ("mads", "1000"): ("4/55cljc",  "utm_source=meta&utm_medium=paid-media&utm_campaign=plan-1000", "mads-gracias-plan-1000"),
    ("mads", "2500"): ("6/wekght",  "utm_source=meta&utm_medium=paid-media&utm_campaign=plan-2500", "mads-gracias-plan-2500"),
    ("mads", "4000"): ("8/8zgk4b",  "utm_source=meta&utm_medium=paid-media&utm_campaign=plan-4000", "mads-gracias-plan-4000"),
    ("gads", "1000"): ("10/ve5ihq", "utm_source=google&utm_medium=sem&utm_campaign=plan-1000", "gads-gracias-plan-1000"),
    ("gads", "2500"): ("12/eixy47", "utm_source=google&utm_medium=sem&utm_campaign=plan-2500", "gads-gracias-plan-2500"),
    ("gads", "4000"): ("14/v6mg73", "utm_source=google&utm_medium=sem&utm_campaign=plan-4000", "gads-gracias-plan-4000"),
    ("pmax", "1000"): ("18/79rncn", "utm_source=google&utm_medium=pmax&utm_campaign=plan-1000", "pmax-gracias-plan-1000"),
    ("pmax", "2500"): ("20/6yni0m", "utm_source=google&utm_medium=pmax&utm_campaign=plan-2500", "pmax-gracias-plan-2500"),
    ("pmax", "4000"): ("22/z52phr", "utm_source=google&utm_medium=pmax&utm_campaign=plan-4000", "pmax-gracias-plan-4000"),
    ("org",  "1000"): ("24/prqjij", "utm_source=org&utm_medium=org&utm_campaign=plan-1000", "org-gracias-plan-1000"),
    ("org",  "2500"): ("26/jf3a3u", "utm_source=org&utm_medium=org&utm_campaign=plan-2500", "org-gracias-plan-2500"),
    ("org",  "4000"): ("28/o14tpu", "utm_source=org&utm_medium=org&utm_campaign=plan-4000", "org-gracias-plan-4000"),
    ("tads", "1000"): ("46/biuoyu", "utm_source=tiktok&utm_medium=paid-media&utm_campaign=plan-1000", "tads-gracias-plan-1000"),
    ("tads", "2500"): ("48/brtl0e", "utm_source=tiktok&utm_medium=paid-media&utm_campaign=plan-2500", "tads-gracias-plan-2500"),
    ("tads", "4000"): ("50/ma2ygt", "utm_source=tiktok&utm_medium=paid-media&utm_campaign=plan-4000", "tads-gracias-plan-4000"),
}

# Dos sueltos, con solo e-mail y teléfono:
#   email remarketing  52/f4e7re   ·  QR de vía pública  106/5c34mv

# Con qué fuente se arma el prototipo. Cambiando esta línea salen las
# landings de cualquier otra fuente, con su formulario y su atribución.
FUENTE = "org"


def ref_form(plan, fuente=None):
    return FORMULARIOS[(fuente or FUENTE, plan)][0]


PORTAL_BITRIX = "b31865227"

PLANES = [
    {
        "clave": "1000",
        "nombre": "Plan 1000",
        "para": "Monotributistas",
        "titular": "Lo esencial, bien cubierto.",
        "bajada": ("Si sos monotributista y buscás una cobertura médica "
                   "esencial, el Plan 1000 es para vos: servicios médicos "
                   "esenciales con copagos accesibles."),
        "oferta": None,
        "foto": "plan-1000.jpg",
        "foto_b": "plan-1000-b.jpg",
        "foco": "0% 50%",
        "numero": "1000",
        "alt": "Un almacenero revisando la mercadería en su mostrador",
        "destacados": [
            ("Atención primaria",
             "Consultas médicas generales para tu salud cotidiana."),
            ("Urgencias y emergencias",
             "Asistencia las 24 horas, los 365 días del año."),
            ("Centros médicos propios en AMBA",
             "Atención en nuestras instalaciones."),
            ("Cobertura nacional",
             "Red básica de prestadores en todo el país."),
        ],
    },
    {
        "clave": "2500",
        "nombre": "Plan 2500",
        "para": "Quien busca relación precio-calidad",
        "titular": "La cobertura que te acompaña.",
        "bajada": ("Pensado para darte la tranquilidad de una cobertura "
                   "médica sólida, con coseguros accesibles y una red "
                   "nacional de prestadores."),
        "oferta": "30% de descuento durante los primeros 6 meses",
        "oferta_cond": "Para personas de hasta 50 años.",
        "foto": "plan-2500.jpg",
        "foto_b": "plan-2500-b.jpg",
        "foco": "0% 50%",
        "numero": "2500",
        "alt": "Una familia caminando por un parque",
        "destacados": [
            ("Amplia red de prestadores",
             "Acceso a una extensa red de profesionales y centros médicos."),
            ("Centros médicos propios en AMBA",
             "Atención rápida en nuestras instalaciones."),
            ("Cobertura nacional",
             "Estés donde estés, te acompañamos."),
            ("Coseguros diferenciales",
             "Coseguros diferenciados para mayor tranquilidad."),
        ],
    },
    {
        "clave": "4000",
        "nombre": "Plan 4000",
        "para": "Quien quiere la cobertura completa",
        "titular": "La cobertura completa.",
        "bajada": ("Una cobertura integral que combina tecnología, "
                   "comodidad y beneficios adicionales que te cuidan en "
                   "cada aspecto de tu vida."),
        "oferta": "30% de descuento durante los primeros 6 meses",
        "oferta_cond": "Para personas de hasta 50 años.",
        "foto": "plan-4000.jpg",
        "foto_b": "plan-4000-b.jpg",
        "foco": "0% 50%",
        "numero": "4000",
        "alt": "Una peluquera con las tijeras en la mano, en su salón",
        "destacados": [
            ("Amplia red de prestadores",
             "Acceso a una extensa red de profesionales y centros médicos."),
            ("Centros médicos propios en AMBA",
             "Atención rápida en nuestras instalaciones."),
            ("Consultas médicas online",
             "Resolvé tus dudas desde la app con el Dr. OSDEPYM."),
            ("Cobertura nacional",
             "Estés donde estés, te acompañamos."),
        ],
    },
]

PLAN_POR_CLAVE = {p["clave"]: p for p in PLANES}

# ---------------------------------------------------------- el comparador
# Estados: "si" · "no" · texto libre. El "no" del 1000 es lo que surge de su
# propia página, que enumera cuatro prestaciones y cierra la lista.

COMPARADOR = [
    ("Atención primaria y consultas",            "si",  "si", "si"),
    ("Urgencias y emergencias, 24 h",            "si",  "si", "si"),
    ("Centros médicos propios en AMBA",          "si",  "si", "si"),
    ("Cobertura nacional",                 "Red básica", "Red nacional", "Red nacional"),
    ("Amplia red de prestadores",                "no",  "si", "si"),
    ("Internaciones programadas y de urgencia",  "no",  "si", "si"),
    ("Estudios de baja, mediana y alta complejidad", "no", "si", "si"),
    ("Odontología básica y especializada",       "no",  "si", "si"),
    ("Ortodoncia y prótesis",      "no", "Aranceles preferenciales", "Aranceles preferenciales"),
    ("Óptica",                     "no", "100% en armazones y cristales estándar, menores de 15", "100% en armazones y cristales estándar, menores de 15"),
    ("Medicamentos en farmacias",  "no", "50% de descuento", "50% de descuento"),
    ("Salud mental",                             "no",  "si", "si"),
    ("Programas preventivos",                    "no",  "si", "si"),
    ("Coseguros diferenciales",                  "no",  "si", "no"),
    ("Consultas médicas online con Dr. OSDEPYM", "no",  "no", "si"),
    ("Viví más OSDEPYM",                         "no",  "si", "si"),
    ("App OSDEPYM",                              "si",  "si", "si"),
    ("DUAL · accidentes personales",             "si",  "si", "si"),
]

COMPARADOR_NOTA = ("Cuadro comparativo según el alcance publicado de cada plan. "
                   "Los límites, los coseguros y las exclusiones se detallan en "
                   "las condiciones de afiliación.")

# ------------------------------------------------- dónde está la figura
# Franja horizontal que ocupa la persona en cada foto, en fracciones del
# ancho de la imagen ya recortada. No es decorativo: el chequeo lo usa
# para verificar que ni el panel ni el arco le tapen la cara.
SUJETO = {
    "home.jpg":        (0.40, 0.56),
    "plan-1000.jpg":   (0.36, 0.60),
    "plan-2500.jpg":   (0.15, 0.58),
    "plan-4000.jpg":   (0.31, 0.57),
    "home-b.jpg":      (0.60, 0.79),
    "plan-1000-b.jpg": (0.60, 0.79),
    "plan-2500-b.jpg": (0.60, 0.70),
    "plan-4000-b.jpg": (0.60, 0.78),
}


# ------------------------------------------------------------------- la app

APP = {
    "titulo": "Tu cobertura, en el teléfono",
    "bajada": ("Gestioná tu cobertura y accedé a tus beneficios de forma "
               "rápida y segura desde la app."),
    "items": [
        ("Credencial digital", "Olvidate de las tarjetas físicas."),
        ("Cartilla online", "Buscá y elegí prestadores con facilidad."),
        ("Dr. OSDEPYM", "Consultas médicas rápidas y seguras."),
        ("Autorizaciones y facturación", "Gestionalas y descargá tus facturas en un clic."),
        ("Noticias y novedades", "Todo lo relacionado con tu plan de salud."),
    ],
}

# -------------------------------------------------------------- Viví más

VIVI = {
    "titulo": "Viví más OSDEPYM",
    "bajada": ("Con los planes 2500 y 4000 accedés no solo a una cobertura "
               "médica completa, sino también a una amplia gama de descuentos "
               "y promociones exclusivas en múltiples rubros."),
    # Los nueve rubros con sus textos del sitio actual. El icono es del
    # mismo sistema de trazo que el resto: caja 24, grosor 1,7.
    "rubros": [
        ("carrito", "Compras y gastronomía",
         "Ahorrá en tus compras diarias y disfrutá de promociones en tus "
         "restaurantes preferidos."),
        ("remera", "Indumentaria",
         "Descuentos en moda, ropa y accesorios de tus marcas favoritas."),
        ("pesa", "Gimnasios y deportes",
         "Precios especiales en gimnasios, centros deportivos y actividades "
         "fitness."),
        ("flor", "Belleza y salud",
         "Beneficios exclusivos en tratamientos de belleza, peluquerías y "
         "centros de estética."),
        ("llave", "Servicios",
         "Promociones en distintos servicios del hogar y personales."),
        ("auto", "Motos y autos",
         "Descuentos en mantenimiento, accesorios y seguros para tu vehículo."),
        ("cine", "Cines",
         "Entradas a precios promocionales en salas seleccionadas."),
        ("valija", "Turismo",
         "Precios especiales en hoteles, agencias y paquetes turísticos."),
        ("birrete", "Educación y cursos",
         "Beneficios en instituciones educativas y plataformas de formación "
         "para seguir desarrollando nuevas habilidades."),
    ],
}

# ----------------------------------------------------------------- DUAL
# Texto congelado en la V3 de las piezas de Comercial y en la sección
# aprobada para las landings. No se improvisa sobre esto.

DUAL = {
    "eyebrow": "Nuevo",
    "titulo": "DUAL: una cobertura adicional por accidentes",
    "bajada": ("OSDEPYM incorporó a sus planes 1000, 2500 y 4000 una "
               "cobertura adicional de accidentes personales, destinada a "
               "monotributistas y profesionales independientes. Si trabajás "
               "por tu cuenta, tu respaldo también cuenta."),
    "tarjetas": [
        ("cama", "Beneficio por internación",
         "En caso de accidente, un beneficio económico de $100.000 por cada "
         "día de internación. Hasta 60 días, sin carencia ni deducibles."),
        ("peso", "Incapacidad total o parcial permanente",
         "Una indemnización económica, según las condiciones previstas."),
        ("escudo", "Fallecimiento por accidente",
         "Una indemnización económica ante el fallecimiento por un accidente."),
        ("factura", "Gastos de sepelio", "Reintegro con tope."),
    ],
    "callout": ("Contempla accidentes vinculados a la actividad laboral "
                "independiente, incluyendo tareas como repartos en moto o "
                "bicicleta."),
    "cta": "Consultá por los Planes 1000, 2500 y 4000 DUAL",
    "legal": ("Plan DUAL disponible en los planes OSDEPYM 1000, 2500 y 4000. "
              "El beneficio está disponible exclusivamente para nuevas "
              "afiliaciones a los planes indicados. Las prestaciones por "
              "accidentes personales son otorgadas por la compañía "
              "aseguradora y están sujetas a los términos, condiciones, "
              "límites y exclusiones de la póliza correspondiente."),
}

# ------------------------------------------------------- pruebas de la marca
# Lámina 38: proof points del mensaje "una marca humana". Todos verificables.

PRUEBAS = [
    {"n": 55, "pre": "Más de ", "post": " años",
     "sub": "acompañando a trabajadores independientes"},
    {"txt": "Centros médicos propios",
     "sub": "en AMBA, con atención en instalaciones propias"},
    {"txt": "Marca federal",
     "sub": "presente en distintos lugares y realidades del país"},
    {"txt": "Hablás con personas",
     "sub": "sucursales físicas y profesionales expertos"},
]

# --------------------------------------------------------------- audiencias
# Láminas 13 a 15. No se muestran como tal en el sitio: ordenan el copy y
# definen qué miedo hay que desarmar en cada sección.

AUDIENCIAS = [
    ("Los nativos", "Menos mal que al menos tengo esto",
     "Temen los gastos elevados u ocultos y los copagos."),
    ("Los caídos", "Podría ser peor",
     "Temen una cartilla limitada y una empresa sin prestigio."),
    ("Buscadores de eficiencia", "Soy una guerrera",
     "Comparan todo. Quieren maximizar el valor de cada peso."),
]

# -------------------------------------------------------------- los caminos

CAMINOS = {
    "a": {
        "letra": "A",
        "nombre": "Claridad",
        "titular": "Lo que pagás y lo que recibís, a la vista.",
        "bajada": ("El camino que lleva el concepto 2027 al terreno donde la "
                   "marca es más fuerte: decirlo claro. Luminoso, editorial, "
                   "con la comparación de planes en el centro de la página y "
                   "el precio sin letra chica. Movimiento medido, que baja a "
                   "cero cuando empieza el formulario."),
        "para": ("Para convertir. Es el camino que recomendamos para producción."),
    },
    "b": {
        "letra": "B",
        "nombre": "Recorrido",
        "titular": "La mirada completa, como un recorrido.",
        "bajada": ("El camino audaz. La curva de la marca deja de ser un "
                   "adorno y pasa a ser el mecanismo: la página se abre como "
                   "una lente. Las cuatro dimensiones del bienestar se "
                   "atraviesan en oscuro, y al llegar a la decisión todo "
                   "invierte a claro, sin efectos."),
        "para": ("Para presentar. Muestra hasta dónde puede estirarse la "
                 "identidad sin romperla."),
    },
}
