# -*- coding: utf-8 -*-
"""Sistema de diseño de las landings 2027 de OSDEPYM.

Paleta y gestos tomados del Documento Brand Life (septiembre 2026) y de su
Bajada a Conceptos (octubre 2026). Los valores de azul salen de medir las
propias láminas, no de estimarlos:

    panel de concepto   #144580 arriba  →  #242541 abajo
    azul de titulares   #084E87
    verde de chapas     #1F5C38

El gesto de marca es LA CURVA: en las láminas el panel azul corta la foto
con un arco convexo, que es el mismo arco del isotipo. Acá se implementa
como media elipse en el borde del panel (`border-radius` con dos radios),
no como imagen, para que acompañe cualquier alto.

Los dos caminos comparten TODO esto. Lo que cambia entre A y B es la capa
de arriba: color de fondo, orden de las secciones y presupuesto de motion.
"""

import os

import contenido as C

# ------------------------------------------------------------------ paleta

PAL = {
    "azul":    "#0E4C86",   # institucional, el de los titulares de lámina
    "azulcl":  "#1D6FB8",   # acento claro
    "navy":    "#242541",   # fondo profundo del panel de concepto
    "navy2":   "#1A1B31",   # más profundo todavía, para el camino B
    "verde":   "#1F5C38",
    "verdecl": "#2E7D4F",
    "amar":    "#F2C300",
    "tinta":   "#1C1F28",
    "suave":   "#5B6070",
    "suave2":  "#8A8F9E",
    "linea":   "#DDE1E8",
    "lineao":  "#2E3350",   # línea sobre oscuro
    "crema":   "#F6F4EE",
    "azulp":   "#EDF3F9",
    "verdep":  "#EDF4EF",
    "blanco":  "#FFFFFF",
}

# ------------------------------------------------------------------ iconos
# Mismo trazo y misma caja 24 para todos: es lo que los hace un sistema.

_IC = {
    "peso":     "M12 3v18M8 7h6a2.6 2.6 0 0 1 0 5.2h-4a2.6 2.6 0 0 0 0 5.2h6",
    "sello":    "M12 3l2.1 1.6 2.6-.3 1 2.4 2.4 1-.3 2.6L21.3 13l-1.6 2.1.3 2.6-2.4 1-1 2.4-2.6-.3L12 22.4 9.9 20.8l-2.6.3-1-2.4-2.4-1 .3-2.6L2.7 13l1.6-2.1-.3-2.6 2.4-1 1-2.4 2.6.3zM9.4 12.4l1.9 1.9 3.5-3.6",
    "persona":  "M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM4.5 20.5a7.5 7.5 0 0 1 15 0",
    "corazon":  "M12 20.2C7.2 17.6 4 14.3 4 10.6A4.1 4.1 0 0 1 12 8.9a4.1 4.1 0 0 1 8 1.7c0 3.7-3.2 7-8 9.6z",
    "cama":     "M3 17v-6a2 2 0 0 1 2-2h10a4 4 0 0 1 4 4v4M3 13h18M3 17v3M21 17v3M7 9V7",
    "escudo":   "M12 3l7 2.7v5.1c0 4.2-2.8 7.6-7 9-4.2-1.4-7-4.8-7-9V5.7z",
    "factura":  "M5 3h14v18l-3-2-2 2-2-2-2 2-3-2zM9 8h6M9 12h6",
    "check":    "M4.5 12.5l5 5 10-11",
    "tel":      "M6.5 3.5h3l1.5 4-2 1.5a12 12 0 0 0 6 6l1.5-2 4 1.5v3a2 2 0 0 1-2.2 2A17.5 17.5 0 0 1 4.5 5.7a2 2 0 0 1 2-2.2z",
    "credencial": "M3 6h18v12H3zM3 10h18M6.5 14h4",
    "cartilla": "M4 4h11l5 5v11H4zM15 4v5h5M8 13h8M8 16.5h5",
    "medico":   "M12 4a4 4 0 0 1 4 4v1a4 4 0 0 1-8 0V8a4 4 0 0 1 4-4zM5 20.5c0-3.3 3.1-5.5 7-5.5s7 2.2 7 5.5",
    "doc":      "M5 3h9l5 5v13H5zM14 3v5h5M8.5 13h7M8.5 16.5h4",
    "campana":  "M12 3a5.5 5.5 0 0 1 5.5 5.5c0 4 1.5 5.5 1.5 5.5H5s1.5-1.5 1.5-5.5A5.5 5.5 0 0 1 12 3zM10 17.5a2 2 0 0 0 4 0",
    "flecha":   "M5 12h13M13 6.5l5.5 5.5L13 17.5",
    "lupa":     "M11 4a7 7 0 1 1 0 14 7 7 0 0 1 0-14zM16.2 16.2L21 21",
    # Rubros de Vivi mas OSDEPYM: mismo trazo, misma caja 24.
    "carrito":   "M3 4h2.2l2.3 10.4h9.6L19 7.4H6.1M9.5 19a1.2 1.2 0 1 0 0-2.4 1.2 1.2 0 0 0 0 2.4zM16.5 19a1.2 1.2 0 1 0 0-2.4 1.2 1.2 0 0 0 0 2.4z",
    "remera":    "M9 3.5L5 5.5l1.4 4L8 9v11.5h8V9l1.6.5L19 5.5l-4-2a3 3 0 0 1-6 0z",
    "pesa":      "M4 9v6M7 7v10M17 7v10M20 9v6M7 12h10",
    "flor":      "M12 9.4a2.6 2.6 0 1 0 0 5.2 2.6 2.6 0 0 0 0-5.2zM12 9.4C12 6.4 10.4 4 8.4 4S5.5 6.1 6.8 8.3M12 14.6c0 3 1.6 5.4 3.6 5.4s2.9-2.1 1.6-4.3M9.4 10.7C6.8 9.2 4 9.4 3 11.2s.5 3.7 3 3.4M14.6 13.3c2.6 1.5 5.4 1.3 6.4-.5s-.5-3.7-3-3.4",
    "llave":     "M14.5 3a6.5 6.5 0 0 1 2.6 12.4L15 17.5l-2 2-2.5-.5-.5 2.5-3-3 7.1-7.1A6.5 6.5 0 0 1 14.5 3zM16.6 7.4h.01",
    "auto":      "M4.5 16.5v2.5h2.6v-2.5M16.9 16.5V19h2.6v-2.5M3.5 16.5h17v-4l-1.7-4.3a2 2 0 0 0-1.9-1.2H7.1a2 2 0 0 0-1.9 1.2L3.5 12.5zM3.5 12.5h17M7 14.4h.01M17 14.4h.01",
    "cine":      "M3 7.5h18v13H3zM3 7.5l3.5-4M9.5 7.5L13 3.5M16 7.5L19.5 3.5M10 11.5l5 2.5-5 2.5z",
    "valija":    "M4.5 8h15v12h-15zM9 8V5.5A1.5 1.5 0 0 1 10.5 4h3A1.5 1.5 0 0 1 15 5.5V8M9.5 12v4M14.5 12v4",
    "birrete":   "M12 4l9 4.2-9 4.2-9-4.2zM6.5 10.5v5c0 1.4 2.5 2.6 5.5 2.6s5.5-1.2 5.5-2.6v-5M21 8.2v5",
}

ICONOS_APP = ["credencial", "cartilla", "medico", "doc", "campana"]


def ico(n, clase="ic"):
    return ('<svg class="%s" viewBox="0 0 24 24" fill="none" '
            'stroke="currentColor" stroke-width="1.7" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true"><path d="%s"/></svg>'
            % (clase, _IC[n]))


# ------------------------------------------------------------- CSS base
# Hereda la lección de la landing del QR: declarar todo explícitamente.
# Acá el sitio es propio, así que no hay tema hostil, pero la disciplina
# de no depender de la herencia se mantiene.

BASE = """
@font-face{font-family:'Gotham';src:url('%(ruta)sfuentes/Gotham-Light.woff2') format('woff2');font-weight:300;font-display:swap}
@font-face{font-family:'Gotham';src:url('%(ruta)sfuentes/Gotham-Book.woff2') format('woff2');font-weight:400;font-display:swap}
@font-face{font-family:'Gotham';src:url('%(ruta)sfuentes/Gotham-Medium.woff2') format('woff2');font-weight:500;font-display:swap}
@font-face{font-family:'Gotham';src:url('%(ruta)sfuentes/Gotham-Bold.woff2') format('woff2');font-weight:700;font-display:swap}

:root{
  --azul:%(azul)s; --azulcl:%(azulcl)s; --navy:%(navy)s; --navy2:%(navy2)s;
  --verde:%(verde)s; --verdecl:%(verdecl)s; --amar:%(amar)s;
  --tinta:%(tinta)s; --suave:%(suave)s; --suave2:%(suave2)s;
  --linea:%(linea)s; --lineao:%(lineao)s; --crema:%(crema)s;
  --azulp:%(azulp)s; --verdep:%(verdep)s;
  --ff:'Gotham',system-ui,-apple-system,'Segoe UI',sans-serif;
  --ancho:1180px; --gut:24px;
  --dur:.5s; --ease:cubic-bezier(.2,.7,.3,1);
}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%%}
body{margin:0;font-family:var(--ff);font-weight:400;color:var(--tinta);
  background:#fff;line-height:1.5;-webkit-font-smoothing:antialiased;
  font-feature-settings:"kern" 1,"liga" 1;overflow-x:hidden}
img,svg{max-width:100%%}
h1,h2,h3,h4{font-family:var(--ff);margin:0;letter-spacing:-.018em;
  line-height:1.08;font-weight:700;text-wrap:balance}
p{margin:0}
ul{margin:0;padding:0;list-style:none}
a{color:inherit}
.ic{width:24px;height:24px;flex:none}

/* ---- contenedor ---- */
.wrap{max-width:var(--ancho);margin:0 auto;padding:0 var(--gut);width:100%%}
section{position:relative}

/* ---- filete tricolor: la firma del pie del manual ---- */
.filete{display:flex;height:4px;width:96px;overflow:hidden;border-radius:2px}
.filete i{flex:1}
.filete i:nth-child(1){background:var(--azul)}
.filete i:nth-child(2){background:var(--verde)}
.filete i:nth-child(3){background:var(--amar)}

/* ---- eyebrow ---- */
.eyebrow{display:inline-flex;align-items:center;gap:9px;font-size:12px;
  font-weight:700;letter-spacing:.12em;text-transform:uppercase;
  color:var(--azul);margin:0}
.eyebrow::before{content:"";width:26px;height:3px;border-radius:2px;
  background:var(--amar);flex:none}
.eyebrow.sobre-oscuro{color:#BFD4EA}

/* ---- titulos ---- */
.t-xl{font-size:clamp(34px,5.2vw,60px)}
.t-lg{font-size:clamp(28px,3.6vw,42px)}
.t-md{font-size:clamp(22px,2.4vw,28px)}
.lead{font-size:clamp(17px,1.5vw,20px);line-height:1.52;font-weight:300;
  color:var(--suave);max-width:62ch}
.lead.sobre-oscuro{color:#C7D2E3}

/* ---- botones ---- */
.btn{display:inline-flex;align-items:center;gap:10px;font-family:var(--ff);
  font-size:14px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;
  line-height:1;padding:17px 30px;border-radius:9px;text-decoration:none;
  border:2px solid transparent;cursor:pointer;transition:background .18s,
  color .18s,border-color .18s}
.btn .ic{width:18px;height:18px}
.btn-p{background:var(--amar);color:var(--navy);border-color:var(--amar)}
.btn-p:hover,.btn-p:focus-visible{background:#FFD426;border-color:#FFD426}
.btn-s{background:transparent;color:var(--azul);border-color:var(--linea)}
.btn-s:hover,.btn-s:focus-visible{border-color:var(--azul);background:var(--azulp)}
.btn-o{background:transparent;color:#fff;border-color:rgba(255,255,255,.4)}
.btn-o:hover,.btn-o:focus-visible{border-color:#fff;background:rgba(255,255,255,.1)}
:focus-visible{outline:3px solid var(--amar);outline-offset:3px}

/* ---- LA CURVA: media elipse en el borde del panel ---- */
.lente{position:relative;display:flex;align-items:stretch;overflow:hidden;
  min-height:clamp(430px,56vw,640px);background:var(--navy)}
/* La foto ocupa una columna del 62%% y el panel entra desde el 38%%: la union
   de las dos cubre todo el ancho, asi que no puede quedar un hueco blanco, y
   la figura cae en la parte que el panel no alcanza. Si la foto fuera a
   sangre, la protagonista quedaria justo detras del azul. */
.lente__fondo{position:absolute;inset:0 auto 0 0;width:62%%;z-index:0;
  background:var(--navy)}
.lente__fondo img{width:100%%;height:100%%;object-fit:cover;display:block}
/* Cuando la pagina es de producto y no de persona, la cara es grafica. En
   verde de marca, para no apilar dos azules contra el panel. */
.lente__fondo--verde{background:
  radial-gradient(122%% 94%% at 24%% 14%%,#2E7D4F 0%%,#1F5C38 46%%,#10301D 100%%)}
.lente__num{position:absolute;inset:0;width:46%%;display:flex;
  flex-direction:column;align-items:center;justify-content:center;gap:12px;
  color:#fff;padding:40px 20px;text-align:center}
.lente__num i{font-style:normal;font-size:12px;font-weight:700;
  letter-spacing:.22em;text-transform:uppercase;color:#BFD9C8}
.lente__num span{font-size:clamp(78px,11vw,158px);font-weight:700;
  line-height:.88;letter-spacing:-.045em}
.lente__num .filete{margin-top:6px}
.lente__panel{position:relative;z-index:2;margin-left:auto;width:62%%;
  background:linear-gradient(140deg,#144580 0%%,#163F72 48%%,var(--navy) 100%%);
  color:#fff;display:flex;flex-direction:column;justify-content:center;
  gap:22px;padding:clamp(34px,4.4vw,64px) clamp(26px,4vw,64px);
  border-top-left-radius:34%% 50%%;border-bottom-left-radius:34%% 50%%;
  padding-left:clamp(56px,9vw,140px)}
.lente__panel > *{position:relative;z-index:1}

/* ---- franja de datos ---- */
/* Verde, no navy: separa del azul del encabezado en vez de apilar tonos. */
.datos{background:var(--verde);color:#fff}
.datos ul{display:grid;grid-template-columns:repeat(4,1fr);gap:2px;
  background:rgba(255,255,255,.16)}
.datos li{background:var(--verde);padding:26px 22px}
.datos b{display:block;font-size:19px;font-weight:700;margin-bottom:5px}
.datos span{font-size:14px;line-height:1.4;color:#C6DCCE;font-weight:300}

/* ---- tarjetas ---- */
.cards{display:grid;gap:14px}
.card{border:1px solid var(--linea);border-radius:12px;padding:24px 22px;
  background:#fff}
.card .ic{color:var(--azul);margin-bottom:12px}
.card h3{font-size:16px;margin-bottom:8px;color:var(--navy);line-height:1.3}
.card p{font-size:15px;line-height:1.45;color:var(--suave);font-weight:300}

/* ---- dimensiones ---- */
.dim{border-radius:14px;overflow:hidden;border:1px solid var(--linea);
  display:flex;flex-direction:column;background:#fff}
.dim__top{background:var(--verde);color:#fff;padding:20px 22px 18px;
  display:flex;align-items:center;gap:12px}
.dim__top .ic{color:var(--amar)}
.dim__top b{font-size:12px;font-weight:700;letter-spacing:.11em;
  text-transform:uppercase;display:block}
.dim__top span{font-size:17px;font-weight:700;display:block;margin-top:2px}
.dim__body{padding:20px 22px 22px;flex:1}
.dim__body p{font-size:15px;line-height:1.45;color:var(--suave);
  font-weight:300;margin-bottom:14px}
.dim__body li{font-size:15px;line-height:1.4;display:flex;gap:9px;
  align-items:flex-start;padding:6px 0;color:var(--tinta)}
.dim__body li .ic{width:17px;height:17px;color:var(--verdecl);margin-top:3px}
.dim__body li.pronto{color:var(--suave2)}
.dim__body li.pronto .ic{color:var(--suave2)}
.dim__body em{font-style:normal;font-size:11px;font-weight:700;
  letter-spacing:.08em;text-transform:uppercase;color:var(--suave2);
  border:1px solid var(--linea);border-radius:10px;padding:2px 7px;
  margin-left:6px;white-space:nowrap}

/* ---- comparador ---- */
.comp{width:100%%;border-collapse:collapse;font-size:15px}
.comp caption{text-align:left;font-size:13px;color:var(--suave);
  font-weight:300;padding-bottom:14px;line-height:1.45}
.comp th,.comp td{padding:13px 14px;border-bottom:1px solid var(--linea);
  text-align:left;vertical-align:top;position:relative}
.comp thead th{font-size:12px;font-weight:700;letter-spacing:.09em;
  text-transform:uppercase;color:var(--suave);border-bottom:2px solid var(--navy);
  white-space:nowrap}
.comp thead th.p{color:var(--navy);font-size:15px;letter-spacing:.02em;
  text-transform:none}
.comp tbody th{font-weight:400;color:var(--tinta);width:38%%}
.comp td{text-align:center;width:20.6%%;color:var(--suave);font-weight:300;
  font-size:13.5px;line-height:1.35}
.comp td .ic{width:20px;height:20px;color:var(--verdecl)}
.comp td.no{color:var(--suave2)}
.comp td.no span{display:inline-block;width:14px;height:2px;border-radius:1px;
  background:var(--linea)}
.comp col.destacado{background:var(--azulp)}
.comp tfoot td{border-bottom:none;padding-top:18px}
.comp-hint{display:none;font-size:12.5px;color:var(--suave2);
  font-weight:300;margin-top:10px}

/* ---- lo que incluye cada plan (reemplaza al comparador en las landings) ---- */
.incluye{display:grid;grid-template-columns:repeat(2,1fr);gap:0 clamp(24px,3vw,44px)}
.incluye li{display:flex;gap:11px;align-items:flex-start;padding:11px 0;
  border-bottom:1px solid var(--linea);font-size:15.5px;line-height:1.4}
.incluye li .ic{width:19px;height:19px;color:var(--verdecl);margin-top:2px}
.incluye em{font-style:normal;display:block;font-size:13px;color:var(--suave);
  font-weight:300;margin-top:3px}

/* ---- Vivi mas: tarjetas con icono, no fichas sueltas ---- */
.vivi{display:grid;gap:14px;grid-template-columns:repeat(3,1fr)}
.vivi article{border:1px solid var(--linea);border-radius:12px;
  padding:22px 20px;background:#fff}
.vivi .ic{color:var(--verde);margin-bottom:11px}
.vivi h3{font-size:16px;margin-bottom:7px;color:var(--verde);line-height:1.3}
.vivi p{font-size:14.5px;line-height:1.45;color:var(--suave);font-weight:300}

/* ---- formulario de Bitrix ---- */
.form{background:#fff;border:1px solid var(--linea);border-radius:14px;
  padding:clamp(22px,3vw,34px);box-shadow:0 18px 48px -28px rgba(20,40,80,.4)}
.form h3{font-size:20px;color:var(--navy);margin-bottom:8px}
.form > p{font-size:15px;color:var(--suave);font-weight:300;line-height:1.45;
  margin-bottom:20px}
.form__caja{min-height:260px}
.form__ph{display:flex;align-items:center;gap:10px;color:var(--suave2);
  font-size:14px;padding:30px 0}
.form__ph i{width:16px;height:16px;border:2px solid var(--linea);
  border-top-color:var(--azul);border-radius:50%%;
  animation:gira .8s linear infinite;flex:none}
@keyframes gira{to{transform:rotate(360deg)}}
.form .b24-form-btn:not(.b24-form-btn-border){background:var(--amar)!important;
  border-color:var(--amar)!important;color:var(--navy)!important;
  font-weight:700!important;font-family:var(--ff)!important;
  text-transform:uppercase!important;letter-spacing:.05em!important;
  border-radius:9px!important}
.form .b24-form-btn:not(.b24-form-btn-border):hover{background:#FFD426!important;
  border-color:#FFD426!important}
.form .b24-form-border-bottom{border-bottom-color:var(--azul)!important}
.form .b24-form-wrapper{font-family:var(--ff)!important}
.form .b24-form-header{display:none!important}
.form__nota{font-size:12px;color:var(--suave2);font-weight:300;
  line-height:1.45;margin-top:14px}

/* ---- DUAL ---- */
.dual{background:var(--crema);border-left:5px solid var(--amar);
  padding:20px 24px;border-radius:0 10px 10px 0}
.dual p{font-size:16px;line-height:1.45;color:#223428}
.dual b{font-weight:700;color:var(--navy)}

/* ---- rubros ---- */
.rubros{display:flex;flex-wrap:wrap;gap:8px}
.rubros li{font-size:13px;font-weight:500;padding:8px 15px;border-radius:16px;
  background:var(--verdep);color:var(--verde);
  box-shadow:inset 0 0 0 1px #CFE2D6}

/* ---- cabecera ---- */
.head{position:sticky;top:0;z-index:40;background:rgba(255,255,255,.92);
  backdrop-filter:saturate(1.6) blur(10px);border-bottom:1px solid var(--linea)}
.head__in{display:flex;align-items:center;justify-content:space-between;
  gap:18px;height:68px}
.head__logo img{height:30px;width:auto;display:block}
.head nav{display:flex;align-items:center;gap:26px}
.head nav a{font-size:14px;font-weight:500;color:var(--tinta);
  text-decoration:none}
.head nav a:hover{color:var(--azul)}
.head nav a.act{color:var(--verde);font-weight:700;
  box-shadow:inset 0 -2px 0 var(--verde)}
.head .btn{padding:12px 20px;font-size:12.5px}

/* ---- pie ---- */
.pie{background:var(--navy);color:#fff;padding:52px 0 34px;margin-top:0}
.pie__top{display:flex;flex-wrap:wrap;gap:28px;justify-content:space-between;
  align-items:flex-start;padding-bottom:28px;border-bottom:1px solid var(--lineao)}
.pie__logo img{height:38px;width:auto;display:block;margin-bottom:12px}
.pie__logo p{font-size:13px;color:#AEB8CC;font-weight:300;max-width:34ch;
  line-height:1.5}
.pie__tel{display:inline-flex;align-items:center;gap:10px;font-size:19px;
  font-weight:700;color:#fff;text-decoration:none;background:rgba(255,255,255,.08);
  border:1px solid var(--lineao);border-radius:28px;padding:12px 22px}
.pie__legal{font-size:12px;line-height:1.6;color:#8E97AC;font-weight:300;
  padding-top:22px;max-width:92ch}
.pie__legal b{color:#C7D2E3;font-weight:500}

/* ---- aviso de prototipo ---- */
.proto{background:var(--amar);color:var(--navy);font-size:12.5px;
  font-weight:500;text-align:center;padding:9px 16px;line-height:1.4}
.proto b{font-weight:700}
.proto a{color:var(--navy)}

/* ====== EFECTOS ======
   Seleccion del catalogo de efectos no convencionales. Cada uno entra con
   un argumento de marca; los que no lo tienen quedaron afuera. El
   presupuesto decrece hacia el formulario: en la zona de decision no se
   mueve nada. Todos se apagan con prefers-reduced-motion.             */

/* E107 · Contadores verificables.
   La prueba se cuenta, no se adjetiva. Solo cifras reales. */
.cuenta{display:inline-block;min-width:1.7ch;text-align:right}

/* E31 · Trazo por scroll.
   "Una mirada completa" se dibuja: la linea une las cuatro dimensiones. */
.trazo{position:relative;height:2px;background:rgba(0,0,0,.08);
  margin:0 0 clamp(22px,2.6vw,34px);overflow:hidden;border-radius:2px}
.trazo i{display:block;height:100%%;width:0;background:var(--verde);
  transition:width 1.15s var(--ease)}
.trazo.visible i{width:100%%}
.trazoV{position:absolute;left:0;top:0;bottom:0;width:2px;
  background:var(--lineao);border-radius:2px;overflow:hidden}
.trazoV i{display:block;width:100%%;height:0;background:var(--amar)}

/* E85 · Columna fija desfasada.
   El titulo se queda mientras la lista pasa: contrapunto editorial. */
.fija{display:grid;gap:clamp(24px,3.6vw,56px);
  grid-template-columns:minmax(0,300px) minmax(0,1fr);align-items:start}
.fija__col{position:sticky;top:96px}

/* E16 · Marquesina de datos.
   La cobertura es larga: se nombra entera. Lo mismo esta en el DOM como
   lista, asi que la marquesina no es la unica via al dato. */
.marq{overflow:hidden;background:var(--navy);padding:15px 0;
  border-top:1px solid var(--lineao);border-bottom:1px solid var(--lineao)}
.marq__in{display:flex;width:max-content;animation:marq 56s linear infinite}
.marq span{font-size:12.5px;font-weight:700;letter-spacing:.09em;
  text-transform:uppercase;color:#AEB8CC;padding:0 20px;white-space:nowrap;
  display:inline-flex;align-items:center;gap:20px}
.marq span::after{content:"";width:5px;height:5px;border-radius:50%%;
  background:var(--amar);flex:none}
@keyframes marq{to{transform:translateX(-50%%)}}

/* E33 + E87 · Barra fija de accion en telefono.
   Se retira al llegar al formulario: ahi la accion ya esta a la vista. */
.ctafija{position:fixed;left:0;right:0;bottom:0;z-index:50;display:none;
  padding:10px 16px calc(10px + env(safe-area-inset-bottom));
  background:rgba(255,255,255,.96);border-top:1px solid var(--linea);
  transform:translateY(115%%);transition:transform .26s var(--ease)}
.ctafija .btn{width:100%%;justify-content:center}
.ctafija.on{transform:none}
@media (max-width:860px){.ctafija{display:block}}

/* E92 · Borde que se dibuja (tambien en foco, no solo al pasar el mouse) */
.card,.dim,.vivi article,.planes-links a{position:relative}
.card::after,.vivi article::after{content:"";position:absolute;inset:-1px;
  border-radius:inherit;border:2px solid var(--verde);opacity:0;
  transition:opacity .2s;pointer-events:none}
.card:hover::after,.vivi article:hover::after,
.card:focus-within::after,.vivi article:focus-within::after{opacity:1}

/* E02 · Inversion de tema por seccion.
   Marca la frontera entre dos clases de contenido. */
.osc{background:var(--navy2);color:#fff}
.osc h2,.osc h3{color:#fff}
.osc .lead{color:#C7D2E3}
.osc .card{background:rgba(255,255,255,.04);border-color:var(--lineao)}
.osc .card h3{color:#fff}
.osc .card p{color:#AEB8CC}
.osc .card .ic{color:var(--amar)}
.osc .dim{background:rgba(255,255,255,.04);border-color:var(--lineao)}
.osc .dim__body p{color:#AEB8CC}
.osc .dim__body li{color:#E6EBF3}
.osc .incluye li{border-bottom-color:var(--lineao);color:#E6EBF3}
.osc .incluye em{color:#9FB4CE}
.osc .vivi article{background:rgba(255,255,255,.04);border-color:var(--lineao)}
.osc .vivi h3{color:#fff}
.osc .vivi p{color:#AEB8CC}
.osc .vivi .ic{color:var(--amar)}
.osc .planes-links a{background:rgba(255,255,255,.04);border-color:var(--lineao)}
.osc .planes-links a:hover{border-color:var(--amar)}
.osc .planes-links b{color:#fff}
.osc .planes-links span{color:#AEB8CC}
.osc .planes-links em{color:var(--amar)}
.osc .legalito{color:#8E97AC}
.osc .trazo{background:rgba(255,255,255,.12)}
.osc .trazo i{background:var(--amar)}
.osc .dual{background:rgba(255,255,255,.05);border-left-color:var(--amar)}
.osc .dual p{color:#E6EBF3}
.osc .dual b{color:#fff}
.dual-sec.osc .cierre{color:var(--amar)}   /* le gana a .dual-sec .cierre */
.osc .eyebrow{color:#BFD4EA}

/* La cita del proposito: un respiro entre dos grillas */
.cita{background:var(--verde);color:#fff;
  padding:clamp(50px,6.4vw,86px) 0}
.cita p{font-size:clamp(23px,3.1vw,38px);line-height:1.22;font-weight:700;
  letter-spacing:-.016em;max-width:21ch;text-wrap:balance}
.cita .filete{margin-bottom:22px}
.cita small{display:block;margin-top:18px;font-size:12px;font-weight:700;
  letter-spacing:.14em;text-transform:uppercase;color:#C6DCCE}

/* ---- reveals (E23 del catálogo: nunca oculta sin JS) ---- */
.rv{opacity:0;transform:translateY(14px);transition:opacity var(--dur) var(--ease),
  transform var(--dur) var(--ease)}
html:not(.js) .rv{opacity:1;transform:none}
.rv.visible{opacity:1;transform:none}

/* ---- movimiento reducido: total, como manda la regla 7 ---- */
@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{animation:none!important;transition:none!important;
    scroll-behavior:auto!important}
  .rv{opacity:1!important;transform:none!important}
}

/* ---- responsive ---- */
@media (max-width:1000px){
  .datos ul{grid-template-columns:repeat(2,1fr)}
  .vivi{grid-template-columns:repeat(2,1fr)}
  .comp{font-size:14px}
  .comp th,.comp td{padding:11px 9px}
  .comp tbody th{width:34%%}
}
@media (max-width:860px){
  .fija{grid-template-columns:1fr}
  .fija__col{position:static}
  .lente{flex-direction:column;min-height:0}
  .lente__fondo{position:relative;inset:auto;width:100%%;
    height:clamp(240px,46vw,350px)}
  .lente__num{width:100%%}
  .lente__panel{width:100%%;margin-left:0;margin-top:-11%%;
    padding-left:clamp(26px,6vw,44px);padding-top:clamp(56px,13vw,86px);
    border-radius:50%% 50%% 0 0 / 11%% 11%% 0 0}
  .head nav{display:none}
  .incluye{grid-template-columns:1fr}
}
@media (max-width:620px){
  :root{--gut:20px}
  .vivi{grid-template-columns:1fr}
  .comp-hint{display:block}
  .comp thead th.p{font-size:13px}
  .comp td{font-size:12.5px;padding:10px 5px}
  .comp tbody th{font-size:13px;width:40%%}
  .pie__top{flex-direction:column}
}
"""


def css_base(ruta="assets/"):
    d = dict(PAL)
    d["ruta"] = ruta
    return BASE % d


# ------------------------------------------------------------- componentes

def cabecera(ruta="assets/", inicio="index.html", activo=""):
    """Los tres planes SIEMPRE a mano: son las paginas que se usan."""
    nav = []
    for clave in ("1000", "2500", "4000"):
        cls = ' class="act" aria-current="page"' if clave == activo else ""
        nav.append('<a href="plan-%s.html"%s>Plan %s</a>' % (clave, cls, clave))
    nav.append('<a href="#dual">DUAL</a>')
    return """<header class="head">
  <div class="wrap head__in">
    <a class="head__logo" href="%(inicio)s" aria-label="OSDEPYM, inicio">
      <img src="%(ruta)sosdepym-color.png" alt="OSDEPYM" width="158" height="38">
    </a>
    <nav aria-label="Secciones">%(nav)s</nav>
    <a class="btn btn-p" href="#formulario">Quiero asesorarme</a>
  </div>
</header>""" % {"ruta": ruta, "inicio": inicio, "nav": "".join(nav)}


def pie(ruta="assets/", legal_extra=""):
    m = C.MARCA
    return """<footer class="pie">
  <div class="wrap">
    <div class="pie__top">
      <div class="pie__logo">
        <img src="%(ruta)sosdepym-blanco.png" alt="OSDEPYM · Te estamos cuidando"
             width="210" height="56">
        <p>%(razon)s</p>
      </div>
      <div>
        <a class="pie__tel" href="tel:%(telcrudo)s">%(ic)s %(tel)s</a>
      </div>
    </div>
    <p class="pie__legal">
      <b>%(razon)s</b> · %(domicilio)s · %(teladmin)s.<br>
      %(extra)s
      %(sss)s · R.N.O.S. %(rnos)s / R.N.E.M.P. %(rnemp)s
    </p>
  </div>
</footer>""" % {"ruta": ruta, "razon": m["razon"], "telcrudo": m["telefono_crudo"],
                "tel": m["telefono"], "ic": ico("tel"), "domicilio": m["domicilio"],
                "teladmin": m["tel_admin"], "sss": m["sss"], "rnos": m["rnos"],
                "rnemp": m["rnemp"], "extra": legal_extra}


def aviso_proto():
    return ('<div class="proto"><b>Prototipo de presentación</b> · '
            'ecobe para OSDEPYM · noviembre 2026. No es un sitio oficial. '
            'Los formularios son los de producción: lo que se envíe entra en '
            'Bitrix24 como un lead real.</div>')


_MEDIDAS = {}


def _suj(foto):
    """La franja de la figura y el tamano real del archivo, para que el
    chequeo pueda calcular el encuadre sin depender de que la imagen haya
    terminado de cargar."""
    a, b = C.SUJETO.get(foto, (0.0, 1.0))
    if foto not in _MEDIDAS:
        try:
            from PIL import Image
            ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "assets", "img", foto)
            with Image.open(ruta) as im:
                _MEDIDAS[foto] = im.size
        except Exception:
            _MEDIDAS[foto] = (0, 0)
    w, h = _MEDIDAS[foto]
    return "%s,%s,%d,%d" % (a, b, w, h)


def lente(foto, alt, foco, contenido_panel, ruta="assets/", numero=None):
    """El gesto de marca: cara izquierda (foto o numero) y panel con el arco."""
    if foto:
        izq = ('<div class="lente__fondo"><img src="%simg/%s" alt="%s" '
               'style="object-position:%s" data-sujeto="%s" width="1800" '
               'height="1200" fetchpriority="high"></div>'
               % (ruta, foto, alt, foco, _suj(foto)))
    else:
        izq = ('<div class="lente__fondo lente__fondo--verde">'
               '<div class="lente__num"><i>Plan OSDEPYM</i><span>%s</span>'
               '<div class="filete" aria-hidden="true"><i></i><i></i><i></i>'
               '</div></div></div>' % numero)
    return """<div class="lente">
  %(izq)s
  <div class="lente__panel">%(panel)s</div>
</div>""" % {"izq": izq, "panel": contenido_panel}


def franja_datos():
    """E107: la unica cifra real se cuenta sola; el resto es texto."""
    li = []
    for d in C.PRUEBAS:
        if "n" in d:
            tit = ('%s<span class="cuenta" data-a="%d">%d</span>%s'
                   % (d["pre"], d["n"], d["n"], d["post"]))
        else:
            tit = d["txt"]
        li.append('<li><b>%s</b><span>%s</span></li>' % (tit, d["sub"]))
    return ('<section class="datos" aria-label="OSDEPYM en datos">'
            '<div class="wrap"><ul>%s</ul></div></section>' % "".join(li))


def cita():
    """Un respiro entre dos grillas: el proposito, en grande, sobre verde."""
    return """<section class="cita">
  <div class="wrap">
    <div class="filete" aria-hidden="true"><i></i><i></i><i></i></div>
    <p>%s</p>
    <small>Propósito de marca · OSDEPYM</small>
  </div>
</section>""" % C.PROPOSITO


def marquesina():
    """E16: la cobertura es larga, se nombra entera. El mismo dato esta en
    la lista del DOM, asi que la marquesina no es la unica via."""
    items = [f[0] for f in C.COMPARADOR]
    tira = "".join("<span>%s</span>" % i for i in items)
    return ('<div class="marq" aria-hidden="true"><div class="marq__in">'
            '%s%s</div></div>' % (tira, tira))


def cta_fija(texto="Quiero asesorarme"):
    return ('<div class="ctafija"><a class="btn btn-p" href="#formulario">'
            '%s</a></div>' % texto)


def dimensiones():
    out = []
    for d in C.DIMENSIONES:
        items = []
        for txt, hay in d["items"]:
            cls = "" if hay else ' class="pronto"'
            tag = "" if hay else ' <em>Próximamente</em>'
            items.append('<li%s>%s<span>%s%s</span></li>'
                         % (cls, ico("check"), txt, tag))
        out.append("""<article class="dim rv">
  <div class="dim__top">%(ic)s<div><b>Dimensión</b><span>%(tit)s</span></div></div>
  <div class="dim__body"><p>%(baj)s</p><ul>%(items)s</ul></div>
</article>""" % {"ic": ico(d["icono"]), "tit": d["titulo"],
                 "baj": d["bajada"], "items": "".join(items)})
    return "".join(out)


def _celda(v):
    if v == "si":
        return '<td>%s<span class="vh"> Incluido</span></td>' % ico("check")
    if v == "no":
        return '<td class="no"><span></span><span class="vh">No incluido</span></td>'
    return '<td>%s</td>' % v


def comparador(destacado=None):
    cols = []
    for p in C.PLANES:
        cls = ' class="destacado"' if p["clave"] == destacado else ""
        cols.append("<col%s>" % cls)
    filas = []
    for fila in C.COMPARADOR:
        filas.append("<tr><th scope=\"row\">%s</th>%s</tr>"
                     % (fila[0], "".join(_celda(v) for v in fila[1:])))
    th = "".join('<th class="p" scope="col">%s</th>' % p["nombre"] for p in C.PLANES)
    return """<table class="comp" id="comparador">
  <caption>%(nota)s</caption>
  <colgroup><col>%(cols)s</colgroup>
  <thead><tr><th scope="col">Prestación</th>%(th)s</tr></thead>
  <tbody>%(filas)s</tbody>
</table>""" % {"nota": C.COMPARADOR_NOTA, "cols": "".join(cols),
               "th": th, "filas": "".join(filas)}


def bloque_app():
    a = C.APP
    items = []
    for i, (t, d) in enumerate(a["items"]):
        items.append('<article class="card rv">%s<h3>%s</h3><p>%s</p></article>'
                     % (ico(ICONOS_APP[i]), t, d))
    return items


def bloque_vivi():
    return "".join(
        '<article class="rv">%s<h3>%s</h3><p>%s</p></article>' % (ico(k), t, d)
        for k, t, d in C.VIVI["rubros"])


def incluye(clave):
    """Lo que ese plan incluye, derivado del mismo cuadro comparativo.

    En las landings reemplaza al comparador: una landing no tiene por que
    mostrarle al visitante todo lo que su plan NO tiene."""
    col = {"1000": 1, "2500": 2, "4000": 3}[clave]
    items = []
    for fila in C.COMPARADOR:
        v = fila[col]
        if v == "no":
            continue
        extra = "" if v == "si" else "<em>%s</em>" % v
        items.append("<li>%s<span>%s%s</span></li>" % (ico("check"), fila[0], extra))
    return '<ul class="incluye">%s</ul>' % "".join(items)


def bloque_dual_cards():
    out = []
    for k, t, d in C.DUAL["tarjetas"]:
        out.append('<article class="card rv">%s<h3>%s</h3><p>%s</p></article>'
                   % (ico(k), t, d))
    return "".join(out)


def formulario(plan, titulo=None, bajada=None, ident="formulario"):
    """El formulario real de Bitrix24.

    Va DOS VECES por landing, el mismo: una apenas pasa el encabezado y
    otra antes del pie, para que nadie tenga que volver a buscarlo. El
    `ref` lleva numero y hash; el numero solo no engancha el formulario."""
    p = C.PLAN_POR_CLAVE[plan] if plan else None
    t = titulo or ("Consultá por el %s" % p["nombre"] if p else "Dejanos tus datos")
    b = bajada or ("Dejanos tus datos y un asesor te contacta. "
                   "Sin compromiso y sin costo.")
    ref = C.ref_form(plan) if plan else C.ref_form("2500")
    num = ref.split("/")[0]
    src = ("https://cdn.bitrix24.es/%s/crm/form/loader_%s.js"
           % (C.PORTAL_BITRIX, num))
    return """<div class="form" id="%(ident)s">
  <h3>%(t)s</h3>
  <p>%(b)s</p>
  <div class="form__caja" data-form>
    <div class="form__ph" aria-live="polite"><i aria-hidden="true"></i>
      <span>Cargando el formulario…</span></div>
    <script data-b24-form="inline/%(ref)s" data-skip-moving="true">
      (function(w,d,u){var s=d.createElement('script');s.async=true;
      s.src=u+'?'+(Date.now()/180000|0);var h=d.getElementsByTagName('script')[0];
      h.parentNode.insertBefore(s,h);})(window,document,'%(src)s');
    </script>
  </div>
  <p class="form__nota">Al enviar aceptás que OSDEPYM te contacte.
     Tus datos se tratan según la Ley 25.326 de Protección de Datos Personales.</p>
</div>""" % {"t": t, "b": b, "ref": ref, "src": src, "ident": ident}


# ------------------------------------------------------------------- JS
# Presupuesto: lo mínimo. Reveals por IntersectionObserver y el placeholder
# del formulario, que se retira cuando Bitrix inyecta su markup.

JS = """
document.documentElement.classList.add('js');
(function(){
  var RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!RM && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){
        if (e.isIntersecting){ e.target.classList.add('visible'); io.unobserve(e.target); }
      });
    }, {rootMargin:'0px 0px -8% 0px', threshold:.08});
    document.querySelectorAll('.rv').forEach(function(el){ io.observe(el); });
  } else {
    document.querySelectorAll('.rv').forEach(function(el){ el.classList.add('visible'); });
  }
    /* E107 · contadores. Con movimiento reducido queda la cifra final. */
  document.querySelectorAll('.cuenta').forEach(function(el){
    var fin = parseInt(el.getAttribute('data-a'), 10);
    if (isNaN(fin) || RM) return;
    var corrio = false;
    var obs = new IntersectionObserver(function(es){
      es.forEach(function(e){
        if (!e.isIntersecting || corrio) return;
        corrio = true; obs.disconnect();
        var t0 = performance.now(), dur = 950;
        (function paso(t){
          var k = Math.min(1, (t - t0) / dur);
          el.textContent = Math.round(fin * (1 - Math.pow(1 - k, 3)));
          if (k < 1) requestAnimationFrame(paso); else el.textContent = fin;
        })(t0);
      });
    }, {threshold:.6});
    obs.observe(el);
  });

  /* E31 · el trazo vertical del recorrido se dibuja con el scroll */
  var trazos = [].slice.call(document.querySelectorAll('.trazoV'));
  if (trazos.length && !RM) {
    var pend = false;
    var pintar = function(){
      pend = false;
      trazos.forEach(function(t){
        var c = t.parentElement.getBoundingClientRect();
        var k = (window.innerHeight * .6 - c.top) / c.height;
        t.firstElementChild.style.height =
          Math.max(0, Math.min(1, k)) * 100 + '%';
      });
    };
    addEventListener('scroll', function(){
      if (!pend) { pend = true; requestAnimationFrame(pintar); }
    }, {passive:true});
    pintar();
  }

  /* E33 + E87 · la barra de accion aparece pasado el encabezado y se
     retira cuando el formulario ya esta a la vista */
  var barra = document.querySelector('.ctafija');
  if (barra) {
    var forms = document.querySelectorAll('.form');
    var vistos = 0, verForm = false;
    if (forms.length && 'IntersectionObserver' in window) {
      var io2 = new IntersectionObserver(function(es){
        es.forEach(function(e){ vistos += e.isIntersecting ? 1 : -1; });
        verForm = vistos > 0; mover();
      }, {threshold:0});
      forms.forEach(function(f){ io2.observe(f); });
    }
    var mover = function(){
      barra.classList.toggle('on', window.scrollY > 460 && !verForm);
    };
    addEventListener('scroll', mover, {passive:true});
    mover();
  }

  document.querySelectorAll('[data-form]').forEach(function(caja){
    var ph = caja.querySelector('.form__ph');
    if (!ph) return;
    var t0 = Date.now();
    var iv = setInterval(function(){
      if (caja.querySelector('.b24-form, .b24-form-wrapper, form, iframe')) {
        ph.remove(); clearInterval(iv);
      } else if (Date.now() - t0 > 12000) {
        ph.innerHTML = '<span>No pudimos cargar el formulario. ' +
          'Escribinos o llamanos al 0800-288-8432.</span>';
        clearInterval(iv);
      }
    }, 300);
  });
})();
"""

VH = ".vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}"


def documento(titulo, descripcion, css_extra, cuerpo, ruta="assets/", clase=""):
    return """<!doctype html>
<html lang="es"%(clase)s>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>%(titulo)s</title>
<meta name="description" content="%(desc)s">
<meta name="theme-color" content="%(navy)s">
<link rel="preload" as="font" type="font/woff2" crossorigin
      href="%(ruta)sfuentes/Gotham-Bold.woff2">
<link rel="preload" as="font" type="font/woff2" crossorigin
      href="%(ruta)sfuentes/Gotham-Book.woff2">
<style>%(base)s
%(vh)s
%(extra)s</style>
</head>
<body>
%(cuerpo)s
<script>%(js)s</script>
</body>
</html>""" % {"titulo": titulo, "desc": descripcion, "navy": PAL["navy"],
              "ruta": ruta, "base": css_base(ruta), "vh": VH,
              "extra": css_extra, "cuerpo": cuerpo, "js": JS,
              "clase": (' class="%s"' % clase) if clase else ""}
