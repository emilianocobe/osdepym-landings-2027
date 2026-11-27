# -*- coding: utf-8 -*-
"""Chequeo de las 9 paginas del sitio (correr despues de construir.py): desborde horizontal, tipografia
minima, un solo H1 y alt en las imagenes. Mide con Chrome headless.

La sonda corre SINCRONA al final del body: los scripts de Bitrix no
resuelven en file://, asi que esperar a `load` deja la pagina colgada.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SITIO = os.path.join(HERE, "docs")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

JS = r"""
(function(){
  var d = document.documentElement, out = {doc:d.scrollWidth, vw:window.innerWidth,
    alto:d.scrollHeight, fuera:[], chicas:[]};
  // Un elemento que se sale pero vive dentro de un contenedor que recorta
  // (overflow hidden/auto/clip) NO desborda el documento: no cuenta.
  function recortado(el){
    for (var a = el.parentElement; a && a !== document.body; a = a.parentElement){
      var o = getComputedStyle(a);
      if (/hidden|auto|scroll|clip/.test(o.overflowX + o.overflow)) return true;
    }
    return false;
  }
  var todos = document.querySelectorAll('body *');
  for (var i=0;i<todos.length;i++){
    var el = todos[i], b = el.getBoundingClientRect();
    if (el.id === 'SONDA') continue;
    if (b.width > 0 && (b.right > window.innerWidth + 1.5 || b.left < -1.5)
        && !recortado(el)){
      if (out.fuera.length < 6)
        out.fuera.push(((el.className||el.tagName)+'').slice(0,30).trim() +
          ' [' + b.left.toFixed(0) + '..' + b.right.toFixed(0) + ']');
    }
    if (el.children.length === 0 && (el.textContent||'').trim()){
      var f = parseFloat(getComputedStyle(el).fontSize);
      if (f < 11 && out.chicas.length < 5)
        out.chicas.push(((el.className||el.tagName)+'').slice(0,24).trim()+' '+f+'px');
    }
  }
  /* ---- que el diseno no le tape la cara a la figura ----
     Se calcula el encuadre real (object-fit: cover) y despues el borde
     curvo del panel o del arco a la altura de la figura, resolviendo la
     elipse del border-radius. Es medicion, no inspeccion visual. */
  function borde(el, lado, y){
    var q = el.getBoundingClientRect(), cs = getComputedStyle(el);
    var rad = (lado === 'left' ? cs.borderTopLeftRadius : cs.borderTopRightRadius);
    var pr = rad.split(' '), rx = pr[0], ry = pr[1] || pr[0];
    var RX = rx.indexOf('%') >= 0 ? parseFloat(rx)/100*q.width : parseFloat(rx);
    var RY = ry.indexOf('%') >= 0 ? parseFloat(ry)/100*q.height : parseFloat(ry);
    if (!(RY > 0)) return lado === 'left' ? q.left : q.right;
    var dy = Math.abs(y - (q.top + q.height/2));
    var k = Math.min(1, dy / RY);
    var mete = RX * (1 - Math.sqrt(1 - k*k));
    return lado === 'left' ? q.left + mete : q.right - mete;
  }
  out.tapadas = [];
  [].forEach.call(document.querySelectorAll('img[data-sujeto]'), function(img){
    var d = img.getAttribute('data-sujeto').split(',');
    var a = parseFloat(d[0]), b = parseFloat(d[1]);
    var nw = parseFloat(d[2]), nh = parseFloat(d[3]);
    var r = img.getBoundingClientRect();
    if (!(nw > 0 && r.width > 0)) return;
    var esc = Math.max(r.width/nw, r.height/nh);
    var rw = nw*esc;
    var op = getComputedStyle(img).objectPosition.split(' ')[0];
    var px = op.indexOf('%') >= 0 ? parseFloat(op)/100 : 0.5;
    var offX = (r.width - rw) * px;
    var x0 = r.left + offX + a*rw, x1 = r.left + offX + b*rw;
    var ancho = x1 - x0;
    /* Si la imagen es mas angosta que su caja, el cover recorta ARRIBA y
       ABAJO: ahi es donde se pierden las cabezas. En el camino A nunca
       debe pasar, porque los recortes se hicieron para que no pase. */
    if (img.closest('.lente') || img.closest('.apertura')) {
      var perdido = (nh*esc - r.height) / (nh*esc);
      if (perdido > (img.closest('.lente') ? 0.02 : 0.08))
        out.tapadas.push(img.getAttribute('src').split('/').pop() +
          ': el encuadre recorta ' + Math.round(perdido*100) +
          '% del alto (riesgo de cortar la cabeza)');
    }
    var panel = document.querySelector('.lente__panel');
    var arco = document.querySelector('.apertura__arco');
    var tapa = 0, quien = '';
    var alturas = [r.top + r.height*0.30, r.top + r.height*0.5,
                   r.top + r.height*0.70];
    // En telefono el panel se apila DEBAJO de la foto: ahi lo que puede
    // tapar es el borde curvo de arriba, no el costado. Se mide distinto.
    if (panel && img.closest('.lente') &&
        panel.getBoundingClientRect().top > r.top + r.height*0.6) {
      var sup = panel.getBoundingClientRect().top;
      var cubre = Math.max(0, r.bottom - sup);
      if (cubre / r.height > 0.25)
        out.tapadas.push(img.getAttribute('src').split('/').pop() +
          ': el panel apilado tapa ' + Math.round(cubre/r.height*100) +
          '% del alto de la foto');
      return;
    }
    if (panel && img.closest('.lente')) {
      var e = Math.min.apply(null, alturas.map(function(y){
        return borde(panel, 'left', y); }));
      tapa = Math.max(0, x1 - e); quien = 'el panel';
    } else if (arco) {
      var e2 = Math.max.apply(null, alturas.map(function(y){
        return borde(arco, 'right', y); }));
      tapa = Math.max(0, e2 - x0); quien = 'el arco';
    }
    if (ancho > 0 && tapa / ancho > 0.18)
      out.tapadas.push(img.getAttribute('src').split('/').pop() + ': ' + quien +
        ' tapa ' + Math.round(tapa/ancho*100) + '% de la figura');
  });

  out.h1 = document.querySelectorAll('h1').length;
  out.sinalt = 0;
  var im = document.querySelectorAll('img');
  for (var j=0;j<im.length;j++) if (!im[j].getAttribute('alt')) out.sinalt++;
  return out;
})()
"""


def medir(ruta, W, H):
    cuerpo = open(ruta, encoding="utf-8").read()
    sonda = ('<pre id="SONDA" style="position:absolute;left:-9999px;'
             'width:100px;white-space:pre-wrap"></pre><script>'
             'document.getElementById("SONDA").textContent='
             'JSON.stringify(%s);</script>' % JS.strip())
    tmp = ruta.replace(".html", "__sonda.html")
    open(tmp, "w", encoding="utf-8").write(cuerpo.replace("</body>", sonda + "</body>"))
    r = subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
         "--allow-file-access-from-files", "--virtual-time-budget=6000",
         "--window-size=%d,%d" % (W, H), "--dump-dom",
         "file:///" + tmp.replace("\\", "/")],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    os.remove(tmp)
    i = r.stdout.find('id="SONDA"')
    if i < 0:
        return None
    j = r.stdout.find(">", i) + 1
    k = r.stdout.find("</pre>", j)
    c = r.stdout[j:k]
    for a, b in (("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"')):
        c = c.replace(a, b)
    try:
        return json.loads(c)
    except Exception:
        return None


PAGINAS = ["index.html", "a/index.html", "a/plan-1000.html", "a/plan-2500.html",
           "a/plan-4000.html", "b/index.html", "b/plan-1000.html",
           "b/plan-2500.html", "b/plan-4000.html"]


def main():
    fallas = 0
    for rel in PAGINAS:
        ruta = os.path.join(SITIO, rel.replace("/", os.sep))
        for et, (W, H) in (("1440", (1440, 900)), ("390", (390, 844))):
            m = medir(ruta, W, H)
            if m is None:
                print("%-20s %-5s  no pude medir" % (rel, et))
                fallas += 1
                continue
            pro = []
            if m["doc"] > m["vw"] + 1:
                pro.append("DESBORDE %d > %d" % (m["doc"], m["vw"]))
            if m["fuera"]:
                pro.append("FUERA: " + " | ".join(m["fuera"][:3]))
            if m["chicas"]:
                pro.append("TIPO<11px: " + " | ".join(m["chicas"][:3]))
            if m["h1"] != 1:
                pro.append("H1 = %d" % m["h1"])
            if m["sinalt"]:
                pro.append("%d img sin alt" % m["sinalt"])
            for t in m.get("tapadas", []):
                pro.append("FIGURA TAPADA " + t)
            fallas += len(pro)
            print("%-20s %-5s  %s" % (rel, et, "OK" if not pro else "; ".join(pro)))
    print("\n%s" % ("Todo limpio." if not fallas else "%d problema(s)." % fallas))
    sys.exit(1 if fallas else 0)


if __name__ == "__main__":
    main()
