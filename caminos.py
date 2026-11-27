# -*- coding: utf-8 -*-
"""Los dos caminos de entrega, más la portada que los presenta.

CAMINO A · Claridad
    Luminoso y editorial. El comparador de planes en el centro de la página.
    La curva de marca ordena el hero y después se retira. Movimiento medido
    (solo reveals) y presupuesto que baja a cero al llegar al formulario.

CAMINO B · Recorrido
    La curva deja de ser un adorno y pasa a ser el mecanismo: la página se
    abre como una lente. Las cuatro dimensiones del bienestar se atraviesan
    en oscuro y, al llegar a la decisión, TODO invierte a claro y sin
    efectos. Es la regla E02 del catálogo de Panni —inversión de tema por
    sección— con un argumento de marca propio: la promesa puede ser un
    recorrido; la decisión se toma con la luz prendida.

Los dos usan el mismo sistema, el mismo contenido y los mismos formularios.
"""

import contenido as C
import sistema as S

# ===========================================================  CAMINO A  ===

CSS_A = """
.sec{padding:clamp(54px,7vw,94px) 0}
.sec--crema{background:var(--crema)}
.sec--azulp{background:var(--azulp)}
.sec--linea{border-top:1px solid var(--linea)}
.sec__head{display:flex;flex-direction:column;gap:15px;
  margin-bottom:clamp(26px,3.4vw,42px);max-width:64ch}
.g4{display:grid;gap:14px;grid-template-columns:repeat(4,1fr)}
.g3{display:grid;gap:14px;grid-template-columns:repeat(3,1fr)}
.g5{display:grid;gap:14px;grid-template-columns:repeat(5,1fr)}
.g2{display:grid;gap:clamp(30px,4.4vw,60px);
  grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);align-items:start}
.oferta{display:flex;flex-direction:column;gap:3px;background:var(--amar);
  color:var(--navy);font-weight:700;font-size:15px;padding:13px 20px;
  border-radius:14px;align-self:flex-start;line-height:1.32;max-width:36ch}
.oferta small{font-weight:500;font-size:12.5px;opacity:.74}
.hero__cta{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.comp-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
.comp{min-width:540px}
.planes-links{display:grid;gap:12px;grid-template-columns:repeat(3,1fr);
  margin-top:26px}
.planes-links a{display:flex;flex-direction:column;gap:6px;padding:20px 22px;
  border:1px solid var(--linea);border-radius:12px;background:#fff;
  text-decoration:none;transition:border-color .18s,transform .18s}
.planes-links a:hover{border-color:var(--azul);transform:translateY(-2px)}
.planes-links b{font-size:17px;color:var(--navy)}
.planes-links span{font-size:14px;color:var(--suave);font-weight:300}
.planes-links em{font-style:normal;font-size:12px;font-weight:700;
  letter-spacing:.07em;text-transform:uppercase;color:var(--azul);
  display:inline-flex;align-items:center;gap:6px;margin-top:4px}
.planes-links em .ic{width:16px;height:16px}
.dual-sec .g4{margin-top:4px}
.dual-sec .dual{margin-top:18px}
.dual-sec .cierre{margin-top:18px;font-size:17px;font-weight:500;
  color:var(--azul)}
.legalito{font-size:12.5px;line-height:1.5;color:var(--suave);font-weight:300;
  margin-top:16px;max-width:94ch}
.vivi__txt p{margin-bottom:18px}
.form-sec{background:linear-gradient(180deg,var(--azulp) 0%,#fff 100%)}
@media (max-width:1000px){
  .g4,.g5{grid-template-columns:repeat(2,1fr)}
  .g2{grid-template-columns:1fr}
  .planes-links{grid-template-columns:1fr}
}
@media (max-width:620px){
  .g3,.g4,.g5{grid-template-columns:1fr}
}
"""


def _hero_panel_home():
    return """<p class="eyebrow sobre-oscuro">Planes OSDEPYM</p>
<h1 class="t-xl">%(h1)s</h1>
<p class="lead sobre-oscuro">%(lead)s</p>
<div class="hero__cta">
  <a class="btn btn-p" href="#comparador">Comparar los planes</a>
  <a class="btn btn-o" href="tel:%(telc)s">%(ic)s %(tel)s</a>
</div>""" % {"h1": C.MENSAJE_1, "lead": C.PROPOSITO,
             "telc": C.MARCA["telefono_crudo"], "tel": C.MARCA["telefono"],
             "ic": S.ico("tel")}


def _seccion_dimensiones():
    return """<section class="sec sec--crema" id="dimensiones">
  <div class="wrap">
    <div class="sec__head">
      <p class="eyebrow">Más que cobertura médica</p>
      <h2 class="t-lg">Una mirada completa del bienestar</h2>
      <p class="lead">%(dif)s</p>
    </div>
    <div class="trazo rv" aria-hidden="true"><i></i></div>
    <div class="g4">%(dims)s</div>
  </div>
</section>""" % {"dif": C.DIFERENCIAL, "dims": S.dimensiones()}


def _seccion_app():
    a = C.APP
    return """<section class="sec">
  <div class="wrap">
    <div class="sec__head">
      <p class="eyebrow">App OSDEPYM</p>
      <h2 class="t-lg">%(tit)s</h2>
      <p class="lead">%(baj)s</p>
    </div>
    <div class="g5">%(items)s</div>
  </div>
</section>""" % {"tit": a["titulo"], "baj": a["bajada"],
                 "items": "".join(S.bloque_app())}


def _seccion_vivi():
    """Nueve rubros con icono y texto. Reducirlo a fichas sueltas le hacia
    perder la jerarquia que tiene como diferencial de la dimension social."""
    v = C.VIVI
    return """<section class="sec sec--crema">
  <div class="wrap">
    <div class="sec__head">
      <p class="eyebrow">Dimensión social</p>
      <h2 class="t-lg">%(tit)s</h2>
      <p class="lead">%(baj)s</p>
    </div>
    <div class="vivi">%(rub)s</div>
  </div>
</section>""" % {"tit": v["titulo"], "baj": v["bajada"], "rub": S.bloque_vivi()}


def _seccion_incluye(p):
    """Reemplaza al comparador dentro de las landings: una landing muestra lo
    que ese plan SI tiene. La comparacion queda en las homes."""
    return """<section class="sec sec--linea" id="incluye">
  <div class="wrap fija">
    <div class="fija__col">
      <div class="sec__head">
        <p class="eyebrow">En detalle</p>
        <h2 class="t-md">Todo lo que incluye el %(nombre)s</h2>
        <p class="lead">Sin letra chica. Lo que ves acá es lo que está
          comprendido en el plan.</p>
      </div>
      <a class="btn btn-p" href="#formulario">Quiero asesorarme</a>
    </div>
    <div>
      %(lista)s
      <p class="legalito">Los límites, los coseguros y las exclusiones de cada
        prestación se detallan en las condiciones de afiliación.</p>
    </div>
  </div>
</section>""" % {"nombre": p["nombre"], "lista": S.incluye(p["clave"])}


def _seccion_dual(oscuro=False):
    d = C.DUAL
    return """<section class="sec dual-sec sec--linea%(osc)s" id="dual">
  <div class="wrap">
    <div class="sec__head">
      <p class="eyebrow">%(eye)s</p>
      <h2 class="t-lg">%(tit)s</h2>
      <p class="lead">%(baj)s</p>
    </div>
    <div class="g4">%(cards)s</div>
    <div class="dual"><p>%(callout)s</p></div>
    <p class="cierre"><b>%(cta)s</b></p>
    <p class="legalito">%(legal)s</p>
  </div>
</section>""" % {"osc": " osc" if oscuro else "", "eye": d["eyebrow"],
                 "tit": d["titulo"], "baj": d["bajada"],
                 "cards": S.bloque_dual_cards(), "callout": d["callout"],
                 "cta": d["cta"], "legal": d["legal"]}


def _seccion_comparador(destacado=None, con_links=True):
    links = ""
    if con_links:
        ls = []
        for p in C.PLANES:
            ls.append('<a href="plan-%s.html"><b>%s</b><span>%s</span>'
                      '<em>Ver el plan %s</em></a>'
                      % (p["clave"], p["nombre"], p["para"], S.ico("flecha")))
        links = '<div class="planes-links">%s</div>' % "".join(ls)
    return """<section class="sec sec--linea">
  <div class="wrap">
    <div class="sec__head">
      <p class="eyebrow">Lo que pagás y lo que recibís</p>
      <h2 class="t-lg">Los tres planes, uno al lado del otro</h2>
      <p class="lead">Sin letra chica y sin costos ocultos. Si algo no está
        incluido, acá también lo vas a ver.</p>
    </div>
    <div class="comp-wrap">%(tabla)s</div>
    <p class="comp-hint">Deslizá el cuadro para ver los tres planes.</p>
    %(links)s
  </div>
</section>""" % {"tabla": S.comparador(destacado), "links": links}


def _seccion_form(plan, titulo=None):
    return """<section class="sec form-sec">
  <div class="wrap g2">
    <div>
      <div class="sec__head">
        <p class="eyebrow">Hablemos</p>
        <h2 class="t-lg">Un asesor te explica, sin vueltas</h2>
        <p class="lead">Dejanos tus datos y te contactamos. Te contamos qué
          cubre cada plan, cuánto sale y qué pasa si cambia tu situación.
          Hablás con personas, no con un robot.</p>
      </div>
      <a class="btn btn-s" href="tel:%(telc)s">%(ic)s %(tel)s</a>
    </div>
    %(form)s
  </div>
</section>""" % {"telc": C.MARCA["telefono_crudo"], "tel": C.MARCA["telefono"],
                 "ic": S.ico("tel"), "form": S.formulario(plan, titulo)}


def home_a(ruta="../assets/"):
    cuerpo = """%(proto)s
%(head)s
<main>
  %(hero)s
  %(datos)s
  %(dims)s
  %(cita)s
  %(comp)s
  %(dual)s
  %(app)s
  %(form)s
</main>
%(pie)s
%(ctafija)s""" % {
        "proto": S.aviso_proto(),
        "head": S.cabecera(ruta, "index.html"),
        "hero": S.lente("home.jpg", "Una joven espera en la vereda de su barrio",
                        "56% center", _hero_panel_home(), ruta),
        "datos": S.franja_datos(),
        "dims": _seccion_dimensiones(),
        "cita": S.cita(),
        "comp": _seccion_comparador(),
        "dual": _seccion_dual(oscuro=True),
        "app": _seccion_app(),
        "form": _seccion_form(None, "Quiero que me asesoren"),
        "pie": S.pie(ruta),
        "ctafija": S.cta_fija(),
    }
    return S.documento(
        "OSDEPYM · Planes 1000, 2500 y 4000",
        "Una buena cobertura en salud no es un privilegio de pocos. "
        "Compará los planes OSDEPYM 1000, 2500 y 4000.",
        CSS_A, cuerpo, ruta)


def _hero_panel_plan(p):
    oferta = ""
    if p["oferta"]:
        oferta = ('<p class="oferta">%s <small>%s</small></p>'
                  % (p["oferta"], p["oferta_cond"]))
    return """<p class="eyebrow sobre-oscuro">%(nombre)s · %(para)s</p>
<h1 class="t-xl">%(tit)s</h1>
<p class="lead sobre-oscuro">%(baj)s</p>
%(oferta)s
<div class="hero__cta">
  <a class="btn btn-p" href="#formulario">Quiero asesorarme</a>
  <a class="btn btn-o" href="#incluye">Ver todo lo que incluye</a>
</div>""" % {"nombre": p["nombre"], "para": p["para"], "tit": p["titular"],
             "baj": p["bajada"], "oferta": oferta}


def plan_a(clave, ruta="../assets/"):
    p = C.PLAN_POR_CLAVE[clave]
    cards = "".join(
        '<article class="card rv">%s<h3>%s</h3><p>%s</p></article>'
        % (S.ico(k), t, d) for k, (t, d) in
        zip(("check", "cartilla", "medico", "lupa"), p["destacados"]))
    vivi = _seccion_vivi() if clave in ("2500", "4000") else ""
    cuerpo = """%(proto)s
%(head)s
<main>
  %(hero)s
  <section class="sec">
    <div class="wrap">
      <div class="sec__head">
        <p class="eyebrow">Qué incluye</p>
        <h2 class="t-lg">Lo que el %(nombre)s te da</h2>
      </div>
      <div class="trazo rv" aria-hidden="true"><i></i></div>
      <div class="g4">%(cards)s</div>
    </div>
  </section>
  %(datos)s
  %(comp)s
  %(app)s
  %(vivi)s
  %(dual)s
  %(form)s
</main>
%(pie)s
%(ctafija)s""" % {
        "proto": S.aviso_proto(),
        "head": S.cabecera(ruta, "index.html", activo=clave),
        "hero": S.lente(p["foto"], p["alt"], p.get("foco", ""),
                        _hero_panel_plan(p), ruta, p.get("numero")),
        "nombre": p["nombre"], "cards": cards,
        "datos": S.franja_datos(),
        "comp": _seccion_incluye(p),
        "app": _seccion_app(),
        "vivi": vivi,
        "dual": _seccion_dual(oscuro=True),
        "form": _seccion_form(clave),
        "pie": S.pie(ruta),
        "ctafija": S.cta_fija(),
    }
    return S.documento(
        "OSDEPYM · %s" % p["nombre"],
        "%s %s" % (p["titular"], p["bajada"]),
        CSS_A, cuerpo, ruta)


# ===========================================================  CAMINO B  ===
# El recorrido. Oscuro hasta la decisión; de ahí en adelante, claro y quieto.

CSS_B = CSS_A + """
/* ---- apertura: la lente ocupa la pantalla y se abre al entrar ---- */
.apertura{position:relative;min-height:100vh;min-height:100dvh;display:grid;
  place-items:center;overflow:hidden;background:var(--navy2);isolation:isolate}
.apertura__foto{position:absolute;inset:0;z-index:0}
.apertura__foto img{width:100%;height:100%;object-fit:cover;
  object-position:center 32%;filter:saturate(.72) contrast(1.06)}
.apertura__velo{position:absolute;inset:0;z-index:1;background:
  linear-gradient(100deg,rgba(13,39,70,.96) 0%,rgba(26,27,49,.74) 44%,
  rgba(26,27,49,.30) 100%)}
/* el arco: una media elipse gigante que "abre" la vista */
/* El arco no debe taparle la cara a la protagonista: se corre a la izquierda */
.apertura__arco{position:absolute;z-index:2;top:-14%;bottom:-14%;left:-68%;
  width:112%;border-radius:0 50% 50% 0 / 0 50% 50% 0;
  background:linear-gradient(120deg,#144580 0%,#163F72 52%,var(--navy2) 100%);
  transform:translateX(-14%) scaleX(.94);transform-origin:left center;
  transition:transform 1.5s var(--ease)}
html.abierto .apertura__arco{transform:translateX(0) scaleX(1)}
.apertura__in{position:relative;z-index:3;display:flex;flex-direction:column;
  gap:24px;padding:clamp(80px,12vh,140px) 0 clamp(60px,9vh,100px);
  max-width:min(760px,100%)}
.apertura h1{font-size:clamp(38px,6.6vw,78px);color:#fff}
.apertura .lead{font-size:clamp(17px,1.7vw,21px);color:#CBD7E8;max-width:52ch}
.apertura__scroll{display:inline-flex;align-items:center;gap:10px;
  font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
  color:#9FB4CE;text-decoration:none}
.apertura__scroll i{width:1px;height:34px;background:linear-gradient(180deg,
  #9FB4CE,transparent);display:block}

/* ---- el recorrido: cuatro dimensiones apiladas (E29, CSS puro) ---- */
.ruta{padding:clamp(54px,7vw,94px) 0}
.ruta__head{max-width:62ch;display:flex;flex-direction:column;gap:15px;
  margin-bottom:clamp(30px,4vw,54px)}
.pasos{display:flex;flex-direction:column;gap:18px}
.paso{position:sticky;top:90px;border:1px solid var(--lineao);border-radius:16px;
  background:#1F2039;padding:clamp(26px,3.4vw,42px);display:grid;
  grid-template-columns:auto minmax(0,1fr);gap:clamp(20px,3vw,40px);
  align-items:start;box-shadow:0 -14px 40px -24px rgba(0,0,0,.9)}
.paso__n{font-size:13px;font-weight:700;letter-spacing:.14em;color:var(--amar);
  border:1px solid var(--lineao);border-radius:10px;padding:8px 12px;
  white-space:nowrap}
.paso h3{font-size:clamp(23px,2.7vw,34px);margin-bottom:12px}
.paso p{font-size:16px;line-height:1.5;color:#AEB8CC;font-weight:300;
  margin-bottom:16px;max-width:52ch}
.paso li{font-size:15.5px;display:flex;gap:10px;align-items:flex-start;
  padding:6px 0;color:#E6EBF3}
.paso li .ic{width:18px;height:18px;color:var(--verdecl);margin-top:3px}
.paso li.pronto{color:#8E97AC}
.paso li.pronto .ic{color:#8E97AC}
.paso em{font-style:normal;font-size:11px;font-weight:700;letter-spacing:.08em;
  text-transform:uppercase;color:#8E97AC;border:1px solid var(--lineao);
  border-radius:10px;padding:2px 7px;margin-left:6px;white-space:nowrap}

/* ---- la frontera: acá termina el relato y empieza la decisión ---- */
.frontera{background:var(--navy2);padding:0}
.frontera__in{background:#fff;border-radius:34px 34px 0 0;
  padding:clamp(44px,6vw,80px) 0 0;text-align:center}
.frontera__in .filete{margin:0 auto 20px}
.frontera__in h2{font-size:clamp(26px,3.4vw,40px);color:var(--navy);
  max-width:20ch;margin:0 auto 14px}
.frontera__in p{font-size:17px;color:var(--suave);font-weight:300;
  max-width:54ch;margin:0 auto}
/* de acá en adelante no hay más efectos: es contrato, no sugerencia */
.decision .rv{opacity:1;transform:none}

/* Verde, no azul: el panel y el velo ya son azules. */
.apertura__foto--num{background:radial-gradient(122% 92% at 24% 14%,
  #2E7D4F 0%,#1F5C38 46%,#10301D 100%)}
.apertura__cta{display:flex;flex-wrap:wrap;align-items:center;gap:20px}
.apertura__num{position:absolute;z-index:2;right:clamp(24px,6vw,86px);
  top:50%;transform:translateY(-50%);display:flex;flex-direction:column;
  align-items:flex-end;gap:8px;color:#fff;text-align:right}
.apertura__num i{font-style:normal;font-size:12px;font-weight:700;
  letter-spacing:.22em;text-transform:uppercase;color:#BFD9C8}
.apertura__num span{font-size:clamp(68px,9.5vw,146px);font-weight:700;
  line-height:.86;letter-spacing:-.045em;opacity:.94}
@media (max-width:980px){.apertura__num{display:none}}
@media (max-width:860px){
  .paso{grid-template-columns:1fr;gap:16px;position:static}
  .apertura__arco{left:-86%;width:150%}
}
"""


def _pasos_b():
    out = []
    for i, d in enumerate(C.DIMENSIONES, 1):
        items = []
        for txt, hay in d["items"]:
            cls = "" if hay else ' class="pronto"'
            tag = "" if hay else ' <em>Próximamente</em>'
            items.append('<li%s>%s<span>%s%s</span></li>'
                         % (cls, S.ico("check"), txt, tag))
        out.append("""<article class="paso" style="top:calc(90px + %(i)dpx)">
  <span class="paso__n">0%(n)d / 04</span>
  <div>
    <h3>Dimensión %(tit)s</h3>
    <p>%(baj)s</p>
    <ul>%(items)s</ul>
  </div>
</article>""" % {"i": (i - 1) * 16, "n": i, "tit": d["titulo"].lower(),
                 "baj": d["bajada"], "items": "".join(items)})
    return "".join(out)


def _planes_b():
    """En el camino B hacian falta: no habia como llegar a las landings."""
    ls = []
    for p in C.PLANES:
        ls.append('<a href="plan-%s.html"><b>%s</b><span>%s</span>'
                  '<em>Ver el plan %s</em></a>'
                  % (p["clave"], p["nombre"], p["para"], S.ico("flecha")))
    return """<section class="sec osc" id="planes">
  <div class="wrap">
    <div class="sec__head">
      <p class="eyebrow sobre-oscuro">Las tres puertas de entrada</p>
      <h2 class="t-lg">Elegí tu plan</h2>
    </div>
    <div class="planes-links">%s</div>
  </div>
</section>""" % "".join(ls)


CTA_HOME_B = """<a class="btn btn-p" href="#planes">Ver los tres planes</a>
        <a class="apertura__scroll" href="#recorrido">Empezá el recorrido
          <i aria-hidden="true"></i></a>"""

CTA_PLAN_B = """<a class="btn btn-p" href="#formulario">Quiero asesorarme</a>
        <a class="apertura__scroll" href="#incluye">Ver todo lo que incluye
          <i aria-hidden="true"></i></a>"""


def _apertura_b(foto, alt, h1, lead, ruta, numero=None, eyebrow=None,
                cta=None):
    if foto:
        fondo = ('<div class="apertura__foto"><img src="%simg/%s" alt="%s" '
                 'width="1800" height="1200" fetchpriority="high"></div>'
                 % (ruta, foto, alt))
    else:
        fondo = '<div class="apertura__foto apertura__foto--num"></div>'
    # El numero del plan tiene que estar: es lo que dice de que pagina se
    # trata antes de leer una sola linea.
    num = ""
    if numero:
        num = ('<div class="apertura__num" aria-hidden="true">'
               '<i>Plan OSDEPYM</i><span>%s</span></div>' % numero)
    vol = ('<p class="eyebrow sobre-oscuro">%s</p>' % eyebrow) if eyebrow else (
        '<div class="filete" aria-hidden="true"><i></i><i></i><i></i></div>')
    return """<section class="apertura">
  %(fondo)s
  <div class="apertura__velo" aria-hidden="true"></div>
  <div class="apertura__arco" aria-hidden="true"></div>
  %(num)s
  <div class="wrap">
    <div class="apertura__in">
      %(vol)s
      <h1>%(h1)s</h1>
      <p class="lead">%(lead)s</p>
      <div class="apertura__cta">%(cta)s</div>
    </div>
  </div>
</section>""" % {"fondo": fondo, "h1": h1, "lead": lead, "num": num,
                 "vol": vol, "cta": cta or CTA_HOME_B}


JS_B = """
requestAnimationFrame(function(){
  requestAnimationFrame(function(){
    document.documentElement.classList.add('abierto');
  });
});
"""


def home_b(ruta="../assets/"):
    cuerpo = """%(proto)s
%(head)s
<main>
  %(apertura)s
  %(marq)s
  %(planes)s
  %(datos)s
  <section class="osc ruta" id="recorrido">
    <div class="wrap">
      <div class="ruta__head">
        <p class="eyebrow sobre-oscuro">El diferencial</p>
        <h2 class="t-lg">Una mirada completa del bienestar</h2>
        <p class="lead">%(dif)s</p>
      </div>
      <div class="pasos">
        <div class="trazoV" aria-hidden="true"><i></i></div>
        %(pasos)s
      </div>
    </div>
  </section>
  <section class="frontera">
    <div class="frontera__in">
      <div class="wrap">
        <div class="filete" aria-hidden="true"><i></i><i></i><i></i></div>
        <h2>Hasta acá la promesa. Ahora, los números.</h2>
        <p>De acá en adelante no hay efectos: solo lo que pagás y lo que
          recibís, en claro.</p>
      </div>
    </div>
  </section>
  <div class="decision">
    %(comp)s
    %(dual)s
    %(form)s
  </div>
</main>
%(pie)s
%(ctafija)s""" % {
        "proto": S.aviso_proto(),
        "head": S.cabecera(ruta, "index.html"),
        "apertura": _apertura_b("home.jpg", "Una joven espera en la vereda de su barrio",
                                C.MENSAJE_1, C.PROPOSITO, ruta),
        "planes": _planes_b(), "marq": S.marquesina(),
        "dif": C.DIFERENCIAL, "pasos": _pasos_b(),
        "comp": _seccion_comparador(),
        "datos": S.franja_datos(),
        "dual": _seccion_dual(),
        "form": _seccion_form(None, "Quiero que me asesoren"),
        "pie": S.pie(ruta),
        "ctafija": S.cta_fija(),
    }
    doc = S.documento(
        "OSDEPYM · El recorrido · Planes 1000, 2500 y 4000",
        "Una mirada completa del bienestar. Compará los planes OSDEPYM.",
        CSS_B, cuerpo, ruta)
    return doc.replace("</body>", "<script>%s</script>\n</body>" % JS_B)


def plan_b(clave, ruta="../assets/"):
    p = C.PLAN_POR_CLAVE[clave]
    oferta = ""
    if p["oferta"]:
        oferta = ('<p class="oferta">%s <small>%s</small></p>'
                  % (p["oferta"], p["oferta_cond"]))
    cards = "".join(
        '<article class="card rv">%s<h3>%s</h3><p>%s</p></article>'
        % (S.ico(k), t, d) for k, (t, d) in
        zip(("check", "cartilla", "medico", "lupa"), p["destacados"]))
    vivi = _seccion_vivi() if clave in ("2500", "4000") else ""
    cuerpo = """%(proto)s
%(head)s
<main>
  %(apertura)s
  %(marq)s
  <section class="osc ruta" id="recorrido">
    <div class="wrap">
      <div class="ruta__head">
        <p class="eyebrow sobre-oscuro">Qué incluye</p>
        <h2 class="t-lg">Lo que el %(nombre)s te da</h2>
        %(oferta)s
      </div>
      <div class="g4">%(cards)s</div>
    </div>
  </section>
  <section class="frontera">
    <div class="frontera__in">
      <div class="wrap">
        <div class="filete" aria-hidden="true"><i></i><i></i><i></i></div>
        <h2>Hasta acá la promesa. Ahora, los números.</h2>
        <p>Dónde está parado el %(nombre)s frente a los otros dos, sin
          maquillaje.</p>
      </div>
    </div>
  </section>
  <div class="decision">
    %(comp)s
    %(datos)s
    %(app)s
    %(vivi)s
    %(dual)s
    %(form)s
  </div>
</main>
%(pie)s
%(ctafija)s""" % {
        "proto": S.aviso_proto(),
        "head": S.cabecera(ruta, "index.html", activo=clave),
        "apertura": _apertura_b(
            p["foto"], p["alt"], p["titular"], p["bajada"], ruta,
            p.get("numero"), "%s · %s" % (p["nombre"], p["para"]),
            CTA_PLAN_B),
        "nombre": p["nombre"], "oferta": oferta, "cards": cards,
        "marq": S.marquesina(),
        "comp": _seccion_incluye(p),
        "datos": S.franja_datos(),
        "app": _seccion_app(),
        "vivi": vivi,
        "dual": _seccion_dual(),
        "form": _seccion_form(clave),
        "pie": S.pie(ruta),
        "ctafija": S.cta_fija(),
    }
    doc = S.documento(
        "OSDEPYM · %s · El recorrido" % p["nombre"],
        "%s %s" % (p["titular"], p["bajada"]),
        CSS_B, cuerpo, ruta)
    return doc.replace("</body>", "<script>%s</script>\n</body>" % JS_B)


# ===========================================================  PORTADA  ===

CSS_P = """
body{background:var(--navy2);color:#fff}
.port{min-height:100vh;min-height:100dvh;display:flex;flex-direction:column}
.port__top{padding:clamp(34px,5vw,58px) 0 0}
.port__logo img{height:40px;width:auto;display:block}
.port__in{flex:1;display:flex;flex-direction:column;justify-content:center;
  padding:clamp(34px,5vw,64px) 0}
.port__head{max-width:70ch;display:flex;flex-direction:column;gap:18px;
  margin-bottom:clamp(34px,4.6vw,56px)}
.port__head h1{font-size:clamp(32px,4.6vw,54px);color:#fff}
.port__head p{font-size:clamp(16px,1.5vw,19px);line-height:1.55;color:#C7D2E3;
  font-weight:300;max-width:68ch}
.caminos{display:grid;gap:18px;grid-template-columns:repeat(2,1fr)}
.cam{display:flex;flex-direction:column;gap:16px;padding:clamp(26px,3.2vw,40px);
  border:1px solid var(--lineao);border-radius:18px;
  background:linear-gradient(160deg,rgba(20,69,128,.42),rgba(31,32,57,.42));
  text-decoration:none;color:#fff;transition:border-color .2s,transform .2s,
  background .2s}
.cam:hover,.cam:focus-visible{border-color:var(--amar);transform:translateY(-3px);
  background:linear-gradient(160deg,rgba(20,69,128,.62),rgba(31,32,57,.52))}
.cam__let{font-size:13px;font-weight:700;letter-spacing:.16em;
  text-transform:uppercase;color:var(--amar)}
.cam h2{font-size:clamp(24px,2.8vw,34px)}
.cam h2 span{display:block;font-size:.62em;color:#9FB4CE;font-weight:500;
  letter-spacing:0;margin-top:6px}
.cam p{font-size:15.5px;line-height:1.5;color:#C7D2E3;font-weight:300}
.cam .para{font-size:13.5px;color:#9FB4CE;border-top:1px solid var(--lineao);
  padding-top:14px}
.cam .ver{display:inline-flex;align-items:center;gap:9px;font-size:13px;
  font-weight:700;letter-spacing:.07em;text-transform:uppercase;
  color:var(--amar);margin-top:auto}
.cam .ver .ic{width:17px;height:17px}
.port__pie{border-top:1px solid var(--lineao);padding:22px 0 30px;
  font-size:12.5px;color:#8E97AC;font-weight:300;line-height:1.6}
.port__pie b{color:#C7D2E3;font-weight:500}
.fuentes{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
.fuentes li{font-size:11.5px;font-weight:500;padding:6px 13px;border-radius:14px;
  background:rgba(255,255,255,.05);color:#AEB8CC;
  box-shadow:inset 0 0 0 1px var(--lineao)}
@media (max-width:820px){.caminos{grid-template-columns:1fr}}
"""


def portada(ruta="assets/"):
    cams = []
    for clave in ("a", "b"):
        c = C.CAMINOS[clave]
        cams.append("""<a class="cam" href="%(clave)s/index.html">
  <span class="cam__let">Camino %(letra)s</span>
  <h2>%(nombre)s<span>%(tit)s</span></h2>
  <p>%(baj)s</p>
  <p class="para">%(para)s</p>
  <span class="ver">Ver el camino %(letra)s %(ic)s</span>
</a>""" % {"clave": clave, "letra": c["letra"], "nombre": c["nombre"],
           "tit": c["titular"], "baj": c["bajada"], "para": c["para"],
           "ic": S.ico("flecha")})
    fuentes = ["Documento Brand Life · septiembre 2026",
               "Bajada a Conceptos · octubre 2026",
               "Export de landingpm.osdepym.com.ar · 26/11/2026",
               "Sección DUAL aprobada · noviembre 2026",
               "Formularios de Bitrix24 en producción"]
    cuerpo = """<div class="port">
  <div class="wrap port__top">
    <div class="port__logo">
      <img src="%(ruta)sosdepym-blanco.png" alt="OSDEPYM · Te estamos cuidando"
           width="220" height="59">
    </div>
  </div>
  <div class="wrap port__in">
    <div class="port__head">
      <div class="filete" aria-hidden="true"><i></i><i></i><i></i></div>
      <h1>Landings 2027. Dos caminos.</h1>
      <p>Las landings de los planes 1000, 2500 y 4000 reconstruidas sobre el
         concepto de marca 2027. Mismo contenido, mismos formularios de
         Bitrix24, mismas prestaciones: lo que cambia es cómo se cuenta.
         Los dos caminos están completos y son navegables.</p>
    </div>
    <div class="caminos">%(cams)s</div>
  </div>
  <div class="wrap port__pie">
    <p><b>Prototipo de presentación · ecobe para OSDEPYM · noviembre 2026.</b>
       No es un sitio oficial. Los formularios son los de producción: lo que se
       envíe entra en Bitrix24 como un lead real.</p>
    <ul class="fuentes">%(fuentes)s</ul>
  </div>
</div>""" % {"ruta": ruta, "cams": "".join(cams),
             "fuentes": "".join("<li>%s</li>" % f for f in fuentes)}
    return S.documento(
        "OSDEPYM · Landings 2027 · Dos caminos",
        "Camino A y Camino B para las landings de los planes OSDEPYM, "
        "sobre el concepto de marca 2027.",
        CSS_P, cuerpo, ruta)
