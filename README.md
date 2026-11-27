# OSDEPYM · Landings 2027 · dos caminos

Prototipo de presentación de **ecobe para OSDEPYM**, noviembre de 2026.
Las landings de los planes 1000, 2500 y 4000 reconstruidas sobre el concepto
de marca 2027, en dos caminos completos y navegables.

**No es un sitio oficial de OSDEPYM.** Todas las páginas llevan `noindex` y un
aviso visible arriba de todo.

## Qué hay

```
docs/                 el sitio publicado
  index.html          portada: Camino A o Camino B
  a/index.html        home del Camino A · Claridad
  a/plan-1000.html    · plan-2500.html · plan-4000.html
  b/index.html        home del Camino B · Recorrido
  b/plan-1000.html    · plan-2500.html · plan-4000.html
  assets/             Gotham, logos e imágenes
```

### Camino A · Claridad

Luminoso y editorial. La curva de marca ordena el encabezado y después se
retira. El comparador de los tres planes está en el centro de la página.
Movimiento medido —solo apariciones por scroll— y presupuesto que baja a
cero cuando empieza el formulario. **Es el camino recomendado para
producción.**

### Camino B · Recorrido

La curva deja de ser un adorno y pasa a ser el mecanismo: la página se abre
como una lente. Las cuatro dimensiones del bienestar se atraviesan en oscuro
y, al llegar a la decisión, todo invierte a claro y sin efectos. La frontera
es explícita: *«Hasta acá la promesa. Ahora, los números.»*

## De dónde sale cada cosa

Nada acá está inventado. Las tres fuentes:

1. **Export de WordPress de `landingpm.osdepym.com.ar`** (26/11/2026).
   De ahí salen las prestaciones, los textos de la app, Viví+ y —sobre
   todo— los identificadores de los formularios de Bitrix24.
2. **Documento Brand Life OSDEPYM** (septiembre 2026, 52 láminas) y su
   **Bajada a Conceptos** (octubre 2026). De ahí salen el propósito, el
   diferencial de las cuatro dimensiones, los mensajes clave, el tono y la
   gramática visual: la curva, el azul `#144580 → #242541`, la foto cálida.
3. **La sección DUAL aprobada** para las landings (noviembre 2026), con su
   texto legal congelado.

Donde una fuente no dice algo, acá no figura.

## Los formularios de Bitrix24

Son los **de producción**, uno por página, como en el sitio actual:

| Página | Formulario |
|---|---|
| Plan 1000 | `loader_24` |
| Plan 2500 | `loader_26` |
| Plan 4000 | `loader_28` |
| Home (provisorio) | `loader_26` |

Todos en el portal `b31865227`. **Lo que se envíe desde este prototipo entra
en Bitrix24 como un lead real.** La home usa provisoriamente el formulario
del 2500 porque en el export no existe uno general: conviene que Comercial
cree uno propio para no ensuciar la atribución.

El estilo del formulario se reescribe por CSS desde el contenedor padre, sin
tocar la funcionalidad. Lo que no se puede por código es agregar o renombrar
campos: eso se hace en el diseñador de Bitrix24.

## El comparador

El cuadro compara los tres planes según **el alcance publicado de cada uno**.
Para el Plan 1000 se toma la lista cerrada que enumera su propia página
actual. Los límites, los coseguros y las exclusiones se detallan en las
condiciones de afiliación, y así lo dice la nota al pie del cuadro.

## Cómo se construye

```
python construir.py
```

| Archivo | Qué hace |
|---|---|
| `contenido.py` | Todo el contenido y los datos. Lo único que se edita para cambiar textos. |
| `sistema.py` | Paleta, tipografía, la curva, los componentes compartidos. |
| `caminos.py` | Las plantillas de los dos caminos y la portada. |
| `construir.py` | Arma `docs/` y copia los assets. |

Hay además un chequeo que mide cada página con Chrome headless —desborde
horizontal, tipografía mínima, un solo `<h1>`, `alt` en las imágenes— a
1440 px y a 390 px. Las nueve pasan limpio.

## Pendiente

- **Las fotos.** Solo la home lleva fotografía. Las páginas de plan resuelven
  su cara izquierda con el número del plan sobre el azul de marca, que es una
  decisión de diseño defendible —el plan es un producto, no una persona—,
  pero si se prefieren fotos, se cambian en una línea de `contenido.py`.
- **La diferencia real entre el 2500 y el 4000.** Con el contenido actual son
  casi la misma página: cambian un titular y una prestación. Es una decisión
  de Comercial, no de diseño.
- **Un formulario propio para la home.**
