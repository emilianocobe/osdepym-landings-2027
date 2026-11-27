# -*- coding: utf-8 -*-
"""Recorta las fotos de Envato para los dos caminos.

    python _importar_fotos.py <carpeta con los originales>

REGLA DE ENCUADRE, que es de donde salieron las cabezas cortadas:

  `object-fit: cover` recorta por el lado que sobra. Si la imagen es mas
  ANGOSTA que el contenedor, recorta ARRIBA y ABAJO — y lo primero que se
  pierde es la cabeza. Si es mas ANCHA, recorta a los costados y el alto
  entra entero.

  Camino A: el contenedor de la foto llega como maximo a 1,40 de relacion
  (62%% del ancho por el alto del encabezado). Los recortes salen a ~1,46,
  siempre por encima, asi que el alto SIEMPRE entra entero y la cabeza no
  se puede cortar. La figura va en la mitad izquierda, donde el panel no
  llega, y `object-position` ancla a la izquierda.

  Camino B: la apertura ocupa la pantalla, asi que la relacion del
  contenedor varia demasiado (de 0,5 en telefono a 1,9 en escritorio) y no
  hay un solo lado que sobre siempre. Ahi los recortes van a 1,50 con la
  cabeza bien adentro y `object-position: 78%% 22%%`, que mantiene la cara
  tanto cuando recorta a lo alto como cuando recorta a lo ancho.

Las fracciones de abajo salieron de medir cada original sobre una grilla,
no de estimarlas.
"""
import os
import sys

from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
DESTINO = os.path.join(AQUI, "assets", "img")

# origen -> (recorte A, salida A, recorte B, salida B)
# El recorte es (izquierda, arriba, derecha, abajo) en fracciones.
TRABAJOS = {
    "home.jpg": ((0.10, 0.00, 0.90, 0.82), "home.jpg",
                 (0.10, 0.00, 0.68, 0.58), "home-b.jpg"),
    "n1000.jpg": ((0.30, 0.00, 1.00, 0.72), "plan-1000.jpg",
                  (0.22, 0.00, 0.80, 0.58), "plan-1000-b.jpg"),
    "p2500.jpg": ((0.14, 0.00, 0.94, 0.82), "plan-2500.jpg",
                  (0.14, 0.00, 0.72, 0.58), "plan-2500-b.jpg"),
    "n4000.jpg": ((0.14, 0.10, 0.94, 0.92), "plan-4000.jpg",
                  (0.12, 0.06, 0.70, 0.64), "plan-4000-b.jpg"),
}


def recortar(im, r):
    w, h = im.size
    return im.crop((int(w * r[0]), int(h * r[1]), int(w * r[2]), int(h * r[3])))


def main(origen):
    for src, (ra, da, rb, db) in TRABAJOS.items():
        ruta = os.path.join(origen, src)
        if not os.path.exists(ruta):
            print("falta %s" % ruta)
            continue
        base = Image.open(ruta).convert("RGB")
        for r, dst, lado in ((ra, da, "A"), (rb, db, "B")):
            im = recortar(base, r)
            im.thumbnail((2200, 2200), Image.LANCZOS)
            im.save(os.path.join(DESTINO, dst), quality=84, optimize=True,
                    progressive=True)
            print("%-18s %-11s relacion %.2f" % (dst, im.size, im.size[0] / float(im.size[1])))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
