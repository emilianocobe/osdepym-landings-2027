# -*- coding: utf-8 -*-
"""Construye el sitio de presentación.

    python construir.py

Salida en docs/ (lo que publica GitHub Pages):

    index.html          portada: Camino A o Camino B
    a/index.html        home del camino A
    a/plan-1000.html    · plan-2500.html · plan-4000.html
    b/index.html        home del camino B
    b/plan-1000.html    · plan-2500.html · plan-4000.html
    assets/             fuentes, logos e imágenes

Todo estático: se publica tal cual en GitHub Pages.
"""

import os
import shutil
import io

import caminos as K

HERE = os.path.dirname(os.path.abspath(__file__))
# La salida se llama docs/ porque es la carpeta que GitHub Pages
# sabe publicar directamente desde la rama principal.
SITIO = os.path.join(HERE, "docs")
ASSETS = os.path.join(HERE, "assets")

# Las paginas de plan no llevan foto: su cara izquierda es grafica.
FOTOS = ("home.jpg",)


def escribir(rel, html):
    destino = os.path.join(SITIO, rel)
    carpeta = os.path.dirname(destino)
    if carpeta and not os.path.isdir(carpeta):
        os.makedirs(carpeta)
    io.open(destino, "w", encoding="utf-8").write(html)
    return destino, len(html.encode("utf-8"))


def marcadores():
    """Si todavía no bajamos una foto, deja un marcador para poder medir la
    página igual. Nunca se publica una página con un marcador sin avisar."""
    from PIL import Image, ImageDraw
    faltan = []
    carpeta = os.path.join(ASSETS, "img")
    if not os.path.isdir(carpeta):
        os.makedirs(carpeta)
    for f in FOTOS:
        p = os.path.join(carpeta, f)
        if os.path.exists(p):
            continue
        faltan.append(f)
        im = Image.new("RGB", (1600, 1100), (36, 37, 65))
        d = ImageDraw.Draw(im)
        for i in range(0, 1100, 44):
            d.line([(0, i), (1600, i)], fill=(46, 51, 80), width=1)
        d.text((60, 60), "FALTA LA FOTO\n%s" % f, fill=(174, 184, 204))
        im.save(p, quality=88)
    return faltan


def copiar_assets():
    destino = os.path.join(SITIO, "assets")
    if os.path.isdir(destino):
        shutil.rmtree(destino)
    shutil.copytree(ASSETS, destino)


def main():
    faltan = marcadores()
    copiar_assets()
    # .nojekyll: sin esto GitHub ignora cualquier archivo que empiece con _
    io.open(os.path.join(SITIO, ".nojekyll"), "w", encoding="utf-8").write("")

    paginas = [("index.html", K.portada("assets/"))]
    paginas.append(("a/index.html", K.home_a("../assets/")))
    paginas.append(("b/index.html", K.home_b("../assets/")))
    for clave in ("1000", "2500", "4000"):
        paginas.append(("a/plan-%s.html" % clave, K.plan_a(clave, "../assets/")))
        paginas.append(("b/plan-%s.html" % clave, K.plan_b(clave, "../assets/")))

    total = 0
    for rel, html in paginas:
        _, n = escribir(rel, html)
        total += n
        print("  %-22s %6.1f KB" % (rel, n / 1024.0))
    print("\n%d páginas · %.1f KB de HTML" % (len(paginas), total / 1024.0))
    if faltan:
        print("\nOJO, faltan fotos (van marcadores): %s" % ", ".join(faltan))
    print("Sitio en: %s" % SITIO)


if __name__ == "__main__":
    main()
