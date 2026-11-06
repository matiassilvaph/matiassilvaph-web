# Artículos del blog. Cada artículo tiene versión en español y en inglés.
# body: HTML del cuerpo. Las imágenes usan rutas absolutas del sitio (/img/...).

POSTS = [
{
 "slug": "triangulo-de-exposicion",
 "date": "2026-10-28",
 "image": "dorado",
 "es": {
  "title": "Triángulo de exposición: apertura, velocidad e ISO explicados simple",
  "desc": "Qué son la apertura, la velocidad de obturación y el ISO, cómo se compensan entre sí y en qué orden decidirlos. Sirve para cualquier cámara.",
  "cat": "Fundamentos",
  "body": """
<p class="lead">Una foto es luz que llega al sensor. Para controlar cuánta luz entra, cualquier cámara tiene tres ajustes: la <strong>apertura</strong>, la <strong>velocidad de obturación</strong> y el <strong>ISO</strong>. Juntos forman lo que se llama el triángulo de exposición.</p>
<p>Los tres hacen lo mismo, dar más o menos luz, pero cada uno tiene un efecto secundario distinto sobre la imagen. Entender ese efecto es lo que separa una foto correcta de una foto pensada.</p>

<h2>1. La apertura: cuánta luz entra y qué queda nítido</h2>
<p>La apertura es el tamaño del agujero del diafragma, dentro del lente. Se expresa con la letra <strong>f</strong> y un número: f/2.8, f/5.6, f/11.</p>
<ul>
<li><strong>Número bajo (f/1.8, f/2.8)</strong>: diafragma muy abierto. Entra mucha luz y el fondo sale desenfocado.</li>
<li><strong>Número alto (f/11, f/16)</strong>: diafragma cerrado. Entra poca luz y casi todo queda nítido, de adelante hacia atrás.</li>
</ul>
<p>Que un número más chico signifique más luz confunde a todo el mundo al principio. Pensalo como una fracción: f/2 es un agujero más grande que f/16.</p>
<p><strong>Efecto secundario: la profundidad de campo.</strong> Es la franja de la imagen que se ve nítida. Una apertura abierta la achica, y eso separa al sujeto del fondo. Una apertura cerrada la agranda, y eso sirve para paisajes y calles donde querés todo definido.</p>

<h2>2. La velocidad de obturación: cuánto tiempo entra la luz</h2>
<p>Es el tiempo que el obturador queda abierto. Se mide en segundos o fracciones: 1/1000, 1/125, 1/30, 2".</p>
<ul>
<li><strong>Velocidad alta (1/1000 o más)</strong>: congela el movimiento. Una ola rompiendo, un surfista, un pájaro en vuelo.</li>
<li><strong>Velocidad baja (1/30 o menos)</strong>: lo que se mueve sale barrido. Sirve para el agua sedosa o las luces de los autos de noche, pero con trípode.</li>
</ul>
<p><strong>Efecto secundario: el movimiento.</strong> Tanto el del sujeto como el tuyo. Con la cámara en la mano, una referencia práctica es no bajar de 1 dividido la distancia focal: con un lente de 50 mm, no menos de 1/50. Si la cámara o el lente tienen estabilizador, se puede bajar algo más, pero el estabilizador no frena a un sujeto que se mueve.</p>

<figure class="fig"><img src="/img/ola-spray.jpg" alt="Ola rompiendo con el spray levantado por el viento en Praia do Norte, Nazaré." loading="lazy" width="1440" height="960"><figcaption>Para congelar el agua y el spray hace falta una velocidad alta. Praia do Norte, Nazaré.</figcaption></figure>

<h2>3. El ISO: cuánto se amplifica la señal</h2>
<p>El ISO indica cuánto se amplifica la luz que capta el sensor. ISO 100 es la sensibilidad base de muchas cámaras; ISO 3200 la amplifica 32 veces.</p>
<ul>
<li><strong>ISO bajo (100–400)</strong>: imagen limpia. Para días de sol o con trípode.</li>
<li><strong>ISO alto (1600 o más)</strong>: permite sacar con poca luz, a costa de grano.</li>
</ul>
<p><strong>Efecto secundario: el ruido.</strong> A más ISO, más grano y menos detalle en las sombras. Cuánto ISO tolera cada cámara depende del sensor: las de cuadro completo suelen aguantar más que las de sensor chico o los celulares. La regla general es usar el ISO más bajo que la situación permita.</p>

<h2>Cómo se compensan: los pasos</h2>
<p>Cada uno de los tres ajustes se mueve en <strong>pasos</strong>. Un paso duplica o reduce a la mitad la luz.</p>
<div class="table-wrap"><table>
<thead><tr><th>Ajuste</th><th>Valores en pasos completos (de más luz a menos luz)</th></tr></thead>
<tbody>
<tr><td>Apertura</td><td>f/1.4 · f/2 · f/2.8 · f/4 · f/5.6 · f/8 · f/11 · f/16</td></tr>
<tr><td>Velocidad</td><td>1/30 · 1/60 · 1/125 · 1/250 · 1/500 · 1/1000 · 1/2000</td></tr>
<tr><td>ISO</td><td>3200 · 1600 · 800 · 400 · 200 · 100</td></tr>
</tbody></table></div>
<p>La clave es que se pueden intercambiar. Si cerrás la apertura un paso, perdés la mitad de la luz, y la recuperás alargando la velocidad un paso o subiendo el ISO un paso. Estas tres combinaciones dan <strong>la misma exposición</strong>:</p>
<div class="table-wrap"><table>
<thead><tr><th>Apertura</th><th>Velocidad</th><th>ISO</th><th>Qué cambia en la foto</th></tr></thead>
<tbody>
<tr><td>f/8</td><td>1/250</td><td>100</td><td>Punto de partida</td></tr>
<tr><td>f/5.6</td><td>1/500</td><td>100</td><td>Fondo más desenfocado, movimiento más congelado</td></tr>
<tr><td>f/11</td><td>1/250</td><td>200</td><td>Más profundidad de campo, algo más de ruido</td></tr>
</tbody></table></div>
<p>La luz que llega es la misma. Lo que cambia es el aspecto de la imagen. Ahí está la decisión del fotógrafo.</p>

<h2>En qué orden decidir</h2>
<ol>
<li><strong>Preguntate qué querés mostrar.</strong> Si importa el fondo (desenfocado o nítido), la prioridad es la apertura. Si importa el movimiento (congelado o barrido), la prioridad es la velocidad.</li>
<li><strong>Fijá ese ajuste</strong> y elegí el otro para que la exposición cierre.</li>
<li><strong>Usá el ISO como último recurso</strong>: lo más bajo posible, y subilo solo cuando la apertura y la velocidad ya no te dan margen.</li>
</ol>

<h2>Puntos de partida para situaciones comunes</h2>
<div class="table-wrap"><table>
<thead><tr><th>Situación</th><th>Prioridad</th><th>Ajustes orientativos</th></tr></thead>
<tbody>
<tr><td>Retrato en la calle</td><td>Desenfocar el fondo</td><td>f/2.8–f/4 · 1/250 o más · ISO automático</td></tr>
<tr><td>Paisaje o calle de día</td><td>Todo nítido</td><td>f/8–f/11 · la velocidad que dé · ISO 100</td></tr>
<tr><td>Olas, surf o deporte</td><td>Congelar</td><td>1/1000–1/2000 · apertura abierta · ISO el necesario</td></tr>
<tr><td>Atardecer</td><td>No quemar el cielo</td><td>f/8 · ISO 100 · medir sobre el cielo</td></tr>
<tr><td>Ciudad de noche</td><td>Luces y detalle</td><td>Trípode · f/8 · ISO 100 · varios segundos</td></tr>
</tbody></table></div>
<p>Son puntos de partida, no reglas. Cada escena tiene su luz, y el histograma de la cámara te dice si te acercaste.</p>

<h2>Una referencia sin fotómetro: la regla del sol 16</h2>
<p>En un día de sol pleno, con la apertura en f/16, la velocidad correcta es aproximadamente 1 dividido el ISO. Con ISO 100, 1/100 (o 1/125, el valor más cercano). Sirve para entender la lógica de los pasos y para comprobar si la cámara está midiendo bien.</p>

<h2>Ejercicio para practicar</h2>
<p>Elegí una escena con un sujeto cerca y un fondo lejos: una planta, una persona, un poste. Sacá la misma foto tres veces, en el modo de prioridad de apertura, a <strong>f/4</strong>, <strong>f/8</strong> y <strong>f/16</strong>. Después compará cuánto se desenfoca el fondo y mirá qué velocidad eligió la cámara en cada caso. En diez minutos vas a entender el triángulo mejor que leyendo cualquier manual.</p>
<p class="next">Siguiente lectura: <a href="/blog/modos-de-la-camara/">Modos de la cámara: cuándo usar A, S, M y P</a>.</p>
"""
 },
 "en": {
  "title": "The exposure triangle: aperture, shutter speed and ISO explained simply",
  "desc": "What aperture, shutter speed and ISO are, how they trade off against each other and in what order to set them. Works with any camera.",
  "cat": "Fundamentals",
  "body": """
<p class="lead">A photograph is light reaching a sensor. To control how much light gets in, every camera has three settings: <strong>aperture</strong>, <strong>shutter speed</strong> and <strong>ISO</strong>. Together they form what is called the exposure triangle.</p>
<p>All three do the same thing, add or remove light, but each one has a different side effect on the image. Understanding that side effect is what separates a correct photo from a considered one.</p>

<h2>1. Aperture: how much light gets in and what stays sharp</h2>
<p>Aperture is the size of the opening in the lens diaphragm. It is written with the letter <strong>f</strong> and a number: f/2.8, f/5.6, f/11.</p>
<ul>
<li><strong>Low number (f/1.8, f/2.8)</strong>: wide open. A lot of light gets in and the background goes soft.</li>
<li><strong>High number (f/11, f/16)</strong>: closed down. Little light gets in and almost everything is sharp, front to back.</li>
</ul>
<p>A smaller number meaning more light confuses everyone at first. Think of it as a fraction: f/2 is a bigger opening than f/16.</p>
<p><strong>Side effect: depth of field.</strong> This is the band of the image that looks sharp. A wide aperture makes it shallow, which separates the subject from the background. A narrow aperture makes it deep, which suits landscapes and streets where you want everything defined.</p>

<h2>2. Shutter speed: how long the light comes in</h2>
<p>This is the time the shutter stays open, measured in seconds or fractions: 1/1000, 1/125, 1/30, 2".</p>
<ul>
<li><strong>Fast (1/1000 or faster)</strong>: freezes motion. A breaking wave, a surfer, a bird in flight.</li>
<li><strong>Slow (1/30 or slower)</strong>: anything that moves turns into a blur. Good for silky water or car light trails at night, but on a tripod.</li>
</ul>
<p><strong>Side effect: motion.</strong> Both the subject's and yours. Handheld, a practical guide is not to go slower than 1 over the focal length: with a 50 mm lens, no slower than 1/50. Stabilization in the camera or lens lets you go a bit slower, but it does not stop a moving subject.</p>

<figure class="fig"><img src="/img/ola-spray.jpg" alt="A wave breaking with spray lifted by the wind at Praia do Norte, Nazaré." loading="lazy" width="1440" height="960"><figcaption>Freezing the water and spray takes a fast shutter speed. Praia do Norte, Nazaré.</figcaption></figure>

<h2>3. ISO: how much the signal is amplified</h2>
<p>ISO tells you how much the light captured by the sensor is amplified. ISO 100 is the base sensitivity of many cameras; ISO 3200 amplifies it 32 times.</p>
<ul>
<li><strong>Low ISO (100–400)</strong>: clean image. For sunny days or a tripod.</li>
<li><strong>High ISO (1600 and up)</strong>: lets you shoot in low light, at the cost of grain.</li>
</ul>
<p><strong>Side effect: noise.</strong> The higher the ISO, the more grain and the less detail in the shadows. How much ISO a camera can handle depends on its sensor: full-frame cameras usually cope better than small-sensor cameras or phones. The general rule is to use the lowest ISO the situation allows.</p>

<h2>How they trade off: stops</h2>
<p>Each of the three settings moves in <strong>stops</strong>. One stop doubles or halves the light.</p>
<div class="table-wrap"><table>
<thead><tr><th>Setting</th><th>Full-stop values (from more light to less light)</th></tr></thead>
<tbody>
<tr><td>Aperture</td><td>f/1.4 · f/2 · f/2.8 · f/4 · f/5.6 · f/8 · f/11 · f/16</td></tr>
<tr><td>Shutter</td><td>1/30 · 1/60 · 1/125 · 1/250 · 1/500 · 1/1000 · 1/2000</td></tr>
<tr><td>ISO</td><td>3200 · 1600 · 800 · 400 · 200 · 100</td></tr>
</tbody></table></div>
<p>The key is that they are interchangeable. Close the aperture one stop and you lose half the light; you get it back by slowing the shutter one stop or raising the ISO one stop. These three combinations give <strong>the same exposure</strong>:</p>
<div class="table-wrap"><table>
<thead><tr><th>Aperture</th><th>Shutter</th><th>ISO</th><th>What changes in the photo</th></tr></thead>
<tbody>
<tr><td>f/8</td><td>1/250</td><td>100</td><td>Starting point</td></tr>
<tr><td>f/5.6</td><td>1/500</td><td>100</td><td>Softer background, motion more frozen</td></tr>
<tr><td>f/11</td><td>1/250</td><td>200</td><td>More depth of field, slightly more noise</td></tr>
</tbody></table></div>
<p>The amount of light is the same. What changes is how the image looks. That is the photographer's decision.</p>

<h2>In what order to decide</h2>
<ol>
<li><strong>Ask yourself what you want to show.</strong> If the background matters (soft or sharp), aperture comes first. If motion matters (frozen or blurred), shutter speed comes first.</li>
<li><strong>Set that one</strong> and choose the other so the exposure works.</li>
<li><strong>Use ISO as the last resort</strong>: as low as possible, raised only when aperture and shutter leave you no room.</li>
</ol>

<h2>Starting points for common situations</h2>
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>Priority</th><th>Suggested settings</th></tr></thead>
<tbody>
<tr><td>Street portrait</td><td>Soft background</td><td>f/2.8–f/4 · 1/250 or faster · auto ISO</td></tr>
<tr><td>Landscape or street by day</td><td>Everything sharp</td><td>f/8–f/11 · whatever shutter results · ISO 100</td></tr>
<tr><td>Waves, surf or sport</td><td>Freeze</td><td>1/1000–1/2000 · wide aperture · ISO as needed</td></tr>
<tr><td>Sunset</td><td>Keep the sky from blowing out</td><td>f/8 · ISO 100 · meter on the sky</td></tr>
<tr><td>City at night</td><td>Lights and detail</td><td>Tripod · f/8 · ISO 100 · several seconds</td></tr>
</tbody></table></div>
<p>These are starting points, not rules. Every scene has its own light, and the camera's histogram tells you whether you got close.</p>

<h2>A reference without a light meter: the sunny 16 rule</h2>
<p>On a bright sunny day, at f/16, the correct shutter speed is roughly 1 over the ISO. At ISO 100, 1/100 (or 1/125, the nearest value). It is a good way to understand how stops work and to check whether your camera is metering correctly.</p>

<h2>Practice exercise</h2>
<p>Pick a scene with a nearby subject and a distant background: a plant, a person, a post. Take the same photo three times in aperture priority mode, at <strong>f/4</strong>, <strong>f/8</strong> and <strong>f/16</strong>. Then compare how soft the background gets and look at which shutter speed the camera chose each time. In ten minutes you will understand the triangle better than from any manual.</p>
<p class="next">Read next: <a href="/en/blog/modos-de-la-camara/">Camera modes: when to use A, S, M and P</a>.</p>
"""
 },
},
{
 "slug": "modos-de-la-camara",
 "date": "2026-10-28",
 "image": "forte-bruma",
 "es": {
  "title": "Modos de la cámara: cuándo usar A, S, M y P (Av y Tv en Canon)",
  "desc": "Qué hace cada modo de disparo, cómo se llama en Sony, Canon, Nikon y Fujifilm, y cuál conviene en cada situación para dejar el automático.",
  "cat": "Fundamentos",
  "body": """
<p class="lead">El dial de modos es lo primero que asusta de una cámara nueva. En realidad dice algo simple: <strong>quién decide cada ajuste</strong>, vos o la cámara.</p>
<p>Este artículo parte del <a href="/blog/triangulo-de-exposicion/">triángulo de exposición</a>. Si todavía no está claro qué hacen la apertura, la velocidad y el ISO, conviene leerlo primero.</p>

<h2>Cómo se llama cada modo según la marca</h2>
<div class="table-wrap"><table>
<thead><tr><th>Modo</th><th>Sony</th><th>Nikon</th><th>Canon</th><th>Fujifilm</th></tr></thead>
<tbody>
<tr><td>Prioridad de apertura</td><td>A</td><td>A</td><td>Av</td><td>A en el dial de velocidad</td></tr>
<tr><td>Prioridad de velocidad</td><td>S</td><td>S</td><td>Tv</td><td>A en el anillo de apertura</td></tr>
<tr><td>Manual</td><td>M</td><td>M</td><td>M</td><td>Los dos ajustes en valores fijos</td></tr>
<tr><td>Programa</td><td>P</td><td>P</td><td>P</td><td>Los dos en A</td></tr>
</tbody></table></div>
<p>En muchas Fujifilm no hay dial de modos: se elige con el dial de velocidad y el anillo de apertura. Poner uno en <strong>A</strong> significa que la cámara calcula ese valor. En los celulares, el modo "Pro" o "Manual" da acceso a la velocidad y al ISO; la apertura suele ser fija.</p>

<h2>Automático: por qué conviene dejarlo</h2>
<p>En automático la cámara elige todo, y casi siempre logra una foto bien expuesta. El problema es que no sabe qué querés mostrar: no sabe si el fondo tiene que desenfocarse o si la ola tiene que quedar congelada. Elige un promedio seguro. Además, en muchas cámaras el automático bloquea el formato RAW y otros ajustes.</p>

<h2>P · Programa</h2>
<p>La cámara elige la apertura y la velocidad, pero vos controlás el ISO, la compensación de exposición y el resto. En la mayoría de las cámaras, girando una rueda cambiás la combinación sin cambiar la exposición.</p>
<p><strong>Cuándo usarlo:</strong> para fotos rápidas donde lo único que importa es no perder el momento. Es un buen paso intermedio, pero conviene no quedarse ahí.</p>

<h2>A / Av · Prioridad de apertura</h2>
<p>Vos elegís la apertura y la cámara calcula la velocidad. Es el modo que más usan los fotógrafos, porque la apertura define el aspecto de la imagen: cuánto se desenfoca el fondo.</p>
<p><strong>Cuándo usarlo:</strong> retratos, calle, paisaje, viaje. Casi todo lo que no se mueve rápido.</p>
<p><strong>Lo que hay que vigilar:</strong> la velocidad que elige la cámara. Si con poca luz baja de 1/60, la foto puede salir movida. La solución es abrir el diafragma o subir el ISO, o configurar el ISO automático con una velocidad mínima, una opción que tienen muchas cámaras.</p>

<h2>S / Tv · Prioridad de velocidad</h2>
<p>Vos elegís la velocidad y la cámara calcula la apertura. Sirve cuando el movimiento es lo principal.</p>
<p><strong>Cuándo usarlo:</strong> surf, olas, deporte, animales, autos. También para lo contrario: velocidades lentas para barrer el agua o las luces.</p>
<p><strong>Lo que hay que vigilar:</strong> si pedís una velocidad muy alta con poca luz, la cámara abre el diafragma al máximo y, si no alcanza, la foto sale oscura. Ahí entra el ISO.</p>

<figure class="fig"><img src="/img/forte-bruma.jpg" alt="Olas grandes rompiendo frente al Forte de São Miguel Arcanjo en Nazaré, con la bruma cubriendo el acantilado." loading="lazy" width="1440" height="960"><figcaption>En un día de olas, la prioridad es la velocidad. Forte de São Miguel Arcanjo, Nazaré.</figcaption></figure>

<h2>M · Manual</h2>
<p>Vos elegís la apertura y la velocidad. La cámara te muestra un indicador de exposición, una escala de −3 a +3, que te dice si la foto va a salir clara u oscura.</p>
<p><strong>Cuándo usarlo:</strong> cuando la luz no cambia y querés resultados idénticos en toda la serie. Fotografía nocturna con trípode, estudio, flash, panorámicas, o escenas donde el fotómetro se engaña.</p>
<p><strong>Un truco útil: manual con ISO automático.</strong> Fijás la apertura y la velocidad, que son las que definen la imagen, y dejás que el ISO se ajuste solo a la luz. Para surf funciona muy bien: 1/2000 fijo para congelar, la apertura que quieras, y el ISO acompaña cuando pasa una nube.</p>

<h2>La compensación de exposición</h2>
<p>En los modos P, A y S la cámara decide la exposición midiendo la luz, y a veces se equivoca. El botón o la rueda marcados con <strong>+/−</strong> le dicen "más clara" o "más oscura".</p>
<ul>
<li><strong>Escenas muy claras</strong> (playa, espuma, nieve): la cámara las oscurece porque cree que hay demasiada luz. Corregí con <strong>+0,7 o +1</strong>.</li>
<li><strong>Escenas oscuras o atardeceres</strong>: la cámara intenta aclararlas y quema el cielo. Corregí con <strong>−0,7 o −1</strong>.</li>
</ul>
<p>Después de usarla, volvé a 0. Olvidarla en −1 es uno de los errores más comunes: todas las fotos siguientes salen oscuras.</p>

<h2>Por dónde empezar</h2>
<ol>
<li><strong>Primeras semanas: A / Av.</strong> Aprendés a decidir la profundidad de campo y a mirar qué velocidad elige la cámara.</li>
<li><strong>Cuando fotografíes movimiento: S / Tv.</strong></li>
<li><strong>Cuando ya entiendas los pasos: M</strong>, primero con ISO automático y después con todo fijo.</li>
</ol>

<h2>Ejercicio para practicar</h2>
<p>Buscá algo que se mueva de forma constante: una fuente de agua, autos pasando, gente caminando. En modo S / Tv, sacá la misma escena a <strong>1/1000</strong>, <strong>1/125</strong> y <strong>1/15</strong>. Mirá cómo cambia el movimiento y qué apertura e ISO eligió la cámara en cada caso. Después repetí en M, ajustando vos todo.</p>
<p class="next">Lectura anterior: <a href="/blog/triangulo-de-exposicion/">Triángulo de exposición: apertura, velocidad e ISO</a>. Siguiente: <a href="/blog/como-leer-el-histograma/">Cómo leer el histograma</a>.</p>
"""
 },
 "en": {
  "title": "Camera modes: when to use A, S, M and P (Av and Tv on Canon)",
  "desc": "What each shooting mode does, what it is called on Sony, Canon, Nikon and Fujifilm, and which one to use in each situation to get off auto.",
  "cat": "Fundamentals",
  "body": """
<p class="lead">The mode dial is the first thing that intimidates people about a new camera. It actually says something simple: <strong>who decides each setting</strong>, you or the camera.</p>
<p>This article builds on the <a href="/en/blog/triangulo-de-exposicion/">exposure triangle</a>. If it is not yet clear what aperture, shutter speed and ISO do, read that first.</p>

<h2>What each mode is called by brand</h2>
<div class="table-wrap"><table>
<thead><tr><th>Mode</th><th>Sony</th><th>Nikon</th><th>Canon</th><th>Fujifilm</th></tr></thead>
<tbody>
<tr><td>Aperture priority</td><td>A</td><td>A</td><td>Av</td><td>A on the shutter dial</td></tr>
<tr><td>Shutter priority</td><td>S</td><td>S</td><td>Tv</td><td>A on the aperture ring</td></tr>
<tr><td>Manual</td><td>M</td><td>M</td><td>M</td><td>Both set to fixed values</td></tr>
<tr><td>Program</td><td>P</td><td>P</td><td>P</td><td>Both on A</td></tr>
</tbody></table></div>
<p>Many Fujifilm cameras have no mode dial: you choose with the shutter speed dial and the aperture ring. Setting either one to <strong>A</strong> means the camera works out that value. On phones, "Pro" or "Manual" mode gives you shutter speed and ISO; the aperture is usually fixed.</p>

<h2>Auto: why it is worth leaving</h2>
<p>In auto the camera picks everything, and it almost always gets a well-exposed photo. The problem is that it does not know what you want to show: whether the background should go soft or the wave should be frozen. It picks a safe average. On many cameras, auto also locks out RAW and other settings.</p>

<h2>P · Program</h2>
<p>The camera picks aperture and shutter speed, but you control ISO, exposure compensation and everything else. On most cameras, turning a dial shifts the combination without changing the exposure.</p>
<p><strong>When to use it:</strong> quick shots where the only thing that matters is not missing the moment. It is a good intermediate step, but do not stay there.</p>

<h2>A / Av · Aperture priority</h2>
<p>You choose the aperture and the camera works out the shutter speed. It is the mode photographers use most, because aperture defines the look of the image: how soft the background gets.</p>
<p><strong>When to use it:</strong> portraits, street, landscape, travel. Almost anything that is not moving fast.</p>
<p><strong>What to watch:</strong> the shutter speed the camera picks. If it drops below 1/60 in low light, the photo may come out blurred. Open the aperture or raise the ISO, or set auto ISO with a minimum shutter speed, an option many cameras offer.</p>

<h2>S / Tv · Shutter priority</h2>
<p>You choose the shutter speed and the camera works out the aperture. Use it when motion is the main thing.</p>
<p><strong>When to use it:</strong> surf, waves, sport, animals, cars. Also for the opposite: slow speeds to blur water or lights.</p>
<p><strong>What to watch:</strong> if you ask for a very fast speed in low light, the camera opens the aperture all the way and, if that is not enough, the photo comes out dark. That is where ISO comes in.</p>

<figure class="fig"><img src="/img/forte-bruma.jpg" alt="Big waves breaking in front of the Forte de São Miguel Arcanjo in Nazaré, with spray covering the cliff." loading="lazy" width="1440" height="960"><figcaption>On a big wave day, shutter speed comes first. Forte de São Miguel Arcanjo, Nazaré.</figcaption></figure>

<h2>M · Manual</h2>
<p>You choose both aperture and shutter speed. The camera shows an exposure indicator, a scale from −3 to +3, that tells you whether the photo will come out bright or dark.</p>
<p><strong>When to use it:</strong> when the light is not changing and you want identical results across a series. Night photography on a tripod, studio, flash, panoramas, or scenes that fool the meter.</p>
<p><strong>A useful trick: manual with auto ISO.</strong> You fix aperture and shutter speed, the two that define the image, and let ISO follow the light. It works very well for surf: 1/2000 fixed to freeze the action, whatever aperture you want, and ISO adjusts when a cloud passes.</p>

<h2>Exposure compensation</h2>
<p>In P, A and S the camera decides the exposure by metering the light, and sometimes it gets it wrong. The button or dial marked <strong>+/−</strong> tells it "brighter" or "darker".</p>
<ul>
<li><strong>Very bright scenes</strong> (beach, white water, snow): the camera darkens them because it thinks there is too much light. Correct with <strong>+0.7 or +1</strong>.</li>
<li><strong>Dark scenes or sunsets</strong>: the camera tries to brighten them and blows out the sky. Correct with <strong>−0.7 or −1</strong>.</li>
</ul>
<p>Set it back to 0 afterwards. Leaving it at −1 is one of the most common mistakes: every photo after that comes out dark.</p>

<h2>Where to start</h2>
<ol>
<li><strong>First few weeks: A / Av.</strong> You learn to decide depth of field and to watch which shutter speed the camera picks.</li>
<li><strong>When you shoot motion: S / Tv.</strong></li>
<li><strong>Once you understand stops: M</strong>, first with auto ISO, then with everything fixed.</li>
</ol>

<h2>Practice exercise</h2>
<p>Find something that moves steadily: a fountain, passing cars, people walking. In S / Tv, shoot the same scene at <strong>1/1000</strong>, <strong>1/125</strong> and <strong>1/15</strong>. See how the motion changes and which aperture and ISO the camera chose each time. Then repeat in M, setting everything yourself.</p>
<p class="next">Previous: <a href="/en/blog/triangulo-de-exposicion/">The exposure triangle: aperture, shutter speed and ISO</a>. Next: <a href="/en/blog/como-leer-el-histograma/">How to read a histogram</a>.</p>
"""
 },
},
{
 "slug": "como-leer-el-histograma",
 "date": "2026-11-03",
 "image": "forte-dorado",
 "es": {
  "title": "Cómo leer el histograma: la herramienta para no quemar ni empastar una foto",
  "desc": "Qué muestra el histograma de la cámara, cómo detectar luces quemadas y sombras empastadas, y cuándo una montaña pegada a un borde está bien. Sirve para cualquier cámara.",
  "cat": "Fundamentos",
  "body": """
<p class="lead">La pantalla de la cámara engaña. Con sol se ve oscura, de noche se ve brillante, y una foto que parece bien en la mano puede estar quemada en la computadora. El histograma no depende de la pantalla ni de la luz que haya alrededor: es la forma más confiable de saber si la exposición está bien.</p>
<p>Este artículo sigue a <a href="/blog/triangulo-de-exposicion/">Triángulo de exposición</a> y <a href="/blog/modos-de-la-camara/">Modos de la cámara</a>. Con el histograma sabés si los ajustes que elegiste funcionaron.</p>

<h2>Qué muestra</h2>
<p>El histograma es un gráfico de cuántos píxeles de la foto hay en cada nivel de brillo.</p>
<ul>
<li><strong>Eje horizontal</strong>: el brillo. A la izquierda, el negro puro. A la derecha, el blanco puro. En el medio, los tonos intermedios.</li>
<li><strong>Altura</strong>: cuántos píxeles tienen ese brillo. Una montaña alta en un punto significa que gran parte de la foto tiene ese tono.</li>
</ul>
<p>No muestra <em>dónde</em> está cada tono en la imagen, solo cuánto hay de cada uno. Un cielo claro y una pared blanca suman en el mismo lugar del gráfico.</p>

<div class="table-wrap"><table>
<thead><tr><th>Zona del gráfico</th><th>Qué representa</th><th>Ejemplos</th></tr></thead>
<tbody>
<tr><td>Borde izquierdo</td><td>Negros</td><td>Siluetas, noche, sombras profundas</td></tr>
<tr><td>Izquierda</td><td>Sombras</td><td>Árboles a contraluz, interiores</td></tr>
<tr><td>Centro</td><td>Medios tonos</td><td>Piel, pasto, cielo azul, asfalto</td></tr>
<tr><td>Derecha</td><td>Luces</td><td>Nubes, arena con sol</td></tr>
<tr><td>Borde derecho</td><td>Blancos</td><td>Espuma de las olas, el sol, la nieve</td></tr>
</tbody></table></div>

<h2>Los dos problemas que detecta</h2>
<p><strong>1. Luces quemadas.</strong> Si la montaña choca contra el borde derecho y se corta, una parte de la foto quedó en blanco puro, sin información. Es lo que pasa con un cielo de atardecer que sale blanco, o con la espuma de una ola sin textura. En edición no se recupera: no hay datos para recuperar.</p>
<p><strong>2. Sombras empastadas.</strong> Si la montaña choca contra el borde izquierdo, una parte quedó en negro puro. Se recupera un poco más que las luces, sobre todo en RAW, pero al aclararla aparece ruido.</p>
<p>Muchas cámaras tienen además una <strong>alerta de luces altas</strong>: al ver la foto, las zonas quemadas parpadean. Se activa en el menú de reproducción, con nombres como "Alerta de altas luces", "Destellos" o "Resaltar zonas quemadas", según la marca.</p>

<figure class="fig"><img src="/img/familia.jpg" alt="Familia caminando hacia el mar al atardecer en contraluz, en una calle de Nazaré." loading="lazy" width="1440" height="961"><figcaption>En un contraluz, la montaña se reparte hacia los dos bordes: sombras oscuras y el cielo cerca del blanco. Lo importante es que el sol sea lo único que toque el borde derecho. Nazaré.</figcaption></figure>

<h2>No existe un histograma correcto</h2>
<p>El error más común es pensar que la montaña tiene que estar centrada. No es así: el histograma correcto depende de la escena.</p>
<ul>
<li><strong>Escena clara</strong> (playa con sol, nieve, una pared blanca): la montaña va a la derecha, y está bien.</li>
<li><strong>Escena oscura</strong> (la ciudad de noche, un interior con poca luz): la montaña va a la izquierda, y está bien.</li>
<li><strong>Escena con mucho contraste</strong> (un contraluz al atardecer): la montaña se reparte hacia los dos bordes. Ahí hay que decidir qué se sacrifica.</li>
</ul>
<p>La pregunta no es "¿está centrada?", sino <strong>"¿se cortó algo importante?"</strong>. Si lo único que toca el borde derecho es el sol, no importa. Si es la cara de una persona o la cresta de la ola, hay que corregir.</p>

<h2>Cómo corregir</h2>
<div class="table-wrap"><table>
<thead><tr><th>Lo que ves</th><th>En A/Av, S/Tv o P</th><th>En manual</th></tr></thead>
<tbody>
<tr><td>Montaña cortada a la derecha</td><td>Compensación de exposición en −0,7 o −1</td><td>Velocidad más alta o diafragma más cerrado</td></tr>
<tr><td>Montaña cortada a la izquierda (y la sombra importa)</td><td>Compensación en +0,7 o +1</td><td>Velocidad más baja, diafragma más abierto o más ISO</td></tr>
<tr><td>Cortada en los dos lados</td><td colspan="2">La escena tiene más contraste del que el sensor registra. Elegí qué proteger (casi siempre las luces) o hacé varias fotos con distinta exposición para combinarlas.</td></tr>
</tbody></table></div>

<h2>Histograma RGB</h2>
<p>Muchas cámaras ofrecen dos versiones: <strong>luminosidad</strong> (un solo gráfico) y <strong>RGB</strong> (uno por cada color: rojo, verde y azul). Conviene usar el RGB: en un atardecer, el canal rojo se quema antes que el resto, y en el gráfico de luminosidad no se ve. El resultado es un naranja plano, sin degradé.</p>

<h2>Un detalle si sacás en RAW</h2>
<p>El histograma de la cámara se calcula sobre la vista previa en JPEG, no sobre el archivo RAW. El RAW suele guardar un poco más de información en las luces de lo que muestra el gráfico. Por eso, si el histograma toca apenas el borde derecho, muchas veces se recupera en edición. Sirve como margen, no como excusa: lo seguro es no cortar.</p>

<h2>Dónde verlo</h2>
<ul>
<li><strong>Al revisar la foto</strong>: en casi todas las cámaras, presionando el botón de información (INFO o DISP) varias veces en reproducción.</li>
<li><strong>Antes de disparar</strong>: las cámaras sin espejo y muchas réflex en visión directa lo muestran en vivo, en la pantalla o en el visor electrónico. Es la forma más rápida de trabajar.</li>
<li><strong>En el celular</strong>: las apps de cámara con modo profesional o manual suelen mostrarlo; la cámara nativa del iPhone y de muchos Android, no.</li>
</ul>

<h2>Ejercicio para practicar</h2>
<p>Buscá una escena con cielo y sombra a la vez: una calle a la tarde, un árbol contra el cielo. Sacá la misma foto con la compensación de exposición en <strong>−1</strong>, <strong>0</strong> y <strong>+1</strong>. Mirá cómo se corre la montaña en cada caso y en cuál de las tres el cielo deja de tocar el borde derecho. Después compará las tres en la computadora.</p>
<p class="next">Lectura anterior: <a href="/blog/modos-de-la-camara/">Modos de la cámara: cuándo usar A, S, M y P</a>.</p>
"""
 },
 "en": {
  "title": "How to read a histogram: the tool that keeps you from blowing out or crushing a photo",
  "desc": "What the camera histogram shows, how to spot blown highlights and crushed shadows, and when a peak against one edge is fine. Works with any camera.",
  "cat": "Fundamentals",
  "body": """
<p class="lead">The camera screen lies. In sunlight it looks dark, at night it looks bright, and a photo that looks fine in your hand can turn out blown on the computer. The histogram does not depend on the screen or the light around you: it is the most reliable way to know whether the exposure is right.</p>
<p>This article follows <a href="/en/blog/triangulo-de-exposicion/">The exposure triangle</a> and <a href="/en/blog/modos-de-la-camara/">Camera modes</a>. The histogram tells you whether the settings you chose worked.</p>

<h2>What it shows</h2>
<p>A histogram is a graph of how many pixels in the photo sit at each brightness level.</p>
<ul>
<li><strong>Horizontal axis</strong>: brightness. Pure black on the left, pure white on the right, midtones in between.</li>
<li><strong>Height</strong>: how many pixels have that brightness. A tall peak at one point means a large part of the photo has that tone.</li>
</ul>
<p>It does not show <em>where</em> each tone is in the image, only how much of each there is. A bright sky and a white wall add up in the same place on the graph.</p>

<div class="table-wrap"><table>
<thead><tr><th>Area of the graph</th><th>What it represents</th><th>Examples</th></tr></thead>
<tbody>
<tr><td>Left edge</td><td>Blacks</td><td>Silhouettes, night, deep shadow</td></tr>
<tr><td>Left</td><td>Shadows</td><td>Backlit trees, interiors</td></tr>
<tr><td>Centre</td><td>Midtones</td><td>Skin, grass, blue sky, asphalt</td></tr>
<tr><td>Right</td><td>Highlights</td><td>Clouds, sunlit sand</td></tr>
<tr><td>Right edge</td><td>Whites</td><td>White water, the sun, snow</td></tr>
</tbody></table></div>

<h2>The two problems it reveals</h2>
<p><strong>1. Blown highlights.</strong> If the graph runs into the right edge and gets cut off, part of the photo is pure white with no information. That is what happens when a sunset sky turns white, or the foam on a wave has no texture. It cannot be recovered in editing: there is no data to recover.</p>
<p><strong>2. Crushed shadows.</strong> If the graph runs into the left edge, part of the photo is pure black. Shadows recover a little better than highlights, especially in RAW, but brightening them brings out noise.</p>
<p>Many cameras also have a <strong>highlight warning</strong>: when you review the photo, blown areas blink. It is switched on in the playback menu, under names like "Highlight alert", "Blinkies" or "Highlight warning", depending on the brand.</p>

<figure class="fig"><img src="/img/familia.jpg" alt="A backlit family walking toward the sea at sunset on a street in Nazaré." loading="lazy" width="1440" height="961"><figcaption>In a backlit scene, the graph spreads toward both edges: dark shadows and a sky near white. What matters is that the sun is the only thing touching the right edge. Nazaré.</figcaption></figure>

<h2>There is no correct histogram</h2>
<p>The most common mistake is thinking the graph should sit in the middle. It should not: the right histogram depends on the scene.</p>
<ul>
<li><strong>Bright scene</strong> (sunny beach, snow, a white wall): the graph sits to the right, and that is fine.</li>
<li><strong>Dark scene</strong> (a city at night, a dim interior): the graph sits to the left, and that is fine.</li>
<li><strong>High-contrast scene</strong> (a sunset backlight): the graph spreads toward both edges. You have to decide what to give up.</li>
</ul>
<p>The question is not "is it centred?" but <strong>"did something important get cut off?"</strong> If the only thing touching the right edge is the sun, it does not matter. If it is someone's face or the crest of the wave, correct it.</p>

<h2>How to correct it</h2>
<div class="table-wrap"><table>
<thead><tr><th>What you see</th><th>In A/Av, S/Tv or P</th><th>In manual</th></tr></thead>
<tbody>
<tr><td>Graph cut off on the right</td><td>Exposure compensation at −0.7 or −1</td><td>Faster shutter or smaller aperture</td></tr>
<tr><td>Graph cut off on the left (and the shadow matters)</td><td>Compensation at +0.7 or +1</td><td>Slower shutter, wider aperture or higher ISO</td></tr>
<tr><td>Cut off on both sides</td><td colspan="2">The scene has more contrast than the sensor can record. Choose what to protect (usually the highlights) or take several exposures to blend later.</td></tr>
</tbody></table></div>

<h2>RGB histogram</h2>
<p>Many cameras offer two versions: <strong>luminance</strong> (a single graph) and <strong>RGB</strong> (one per colour channel: red, green and blue). Use RGB: at sunset the red channel blows out before the others, and the luminance graph does not show it. The result is a flat orange with no gradation.</p>

<h2>A note if you shoot RAW</h2>
<p>The camera histogram is calculated from the JPEG preview, not from the RAW file. The RAW usually holds a little more highlight information than the graph shows. So if the histogram just touches the right edge, it can often be recovered in editing. Treat it as a margin, not an excuse: the safe option is not to clip.</p>

<h2>Where to see it</h2>
<ul>
<li><strong>When reviewing a photo</strong>: on almost every camera, press the information button (INFO or DISP) a few times in playback.</li>
<li><strong>Before you shoot</strong>: mirrorless cameras and many DSLRs in live view show it live, on the screen or in the electronic viewfinder. It is the fastest way to work.</li>
<li><strong>On a phone</strong>: camera apps with a pro or manual mode usually show it; the built-in camera on iPhone and many Android phones does not.</li>
</ul>

<h2>Practice exercise</h2>
<p>Find a scene with both sky and shade: a street in the afternoon, a tree against the sky. Take the same photo with exposure compensation at <strong>−1</strong>, <strong>0</strong> and <strong>+1</strong>. Watch how the graph shifts each time and in which of the three the sky stops touching the right edge. Then compare all three on the computer.</p>
<p class="next">Previous: <a href="/en/blog/modos-de-la-camara/">Camera modes: when to use A, S, M and P</a>.</p>
"""
 },
},
{
 "slug": "temporada-de-olas-en-nazare",
 "date": "2026-11-06",
 "image": "praia-do-norte",
 "es": {
  "title": "Temporada de olas grandes en Nazaré 2026/27: cuándo ir, dónde pararse y cómo saber si va a haber olas",
  "desc": "Guía práctica de la temporada de olas gigantes en Praia do Norte: meses, Nazaré Big Wave Challenge 2026/27, cómo leer el pronóstico, dónde ver las olas y cómo fotografiarlas.",
  "cat": "Nazaré",
  "body": """
<p class="lead">De noviembre a febrero, Praia do Norte puede recibir las olas más grandes que se surfean en el mundo. No hay fecha fija: aparecen cuando una tormenta del Atlántico Norte manda el mar de fondo justo hacia Nazaré. Esta guía resume cuándo ir, cómo saber si va a haber olas y dónde pararse para verlas y fotografiarlas.</p>

<h2>Por qué en Nazaré</h2>
<p>Frente a Praia do Norte nace el <strong>Cañón de Nazaré</strong>, una grieta submarina de unos 230 kilómetros de largo que llega a cerca de 5.000 metros de profundidad. El cañón lleva la energía del mar de fondo casi intacta hasta muy cerca de la costa, y ahí la ola crece de golpe. Por eso, con la misma tormenta, en Nazaré rompen olas mucho más grandes que en el resto de la costa portuguesa.</p>

<h2>Cuándo es la temporada</h2>
<div class="table-wrap"><table>
<thead><tr><th>Meses</th><th>Qué esperar</th></tr></thead>
<tbody>
<tr><td>Noviembre a febrero</td><td>La mayor probabilidad de olas gigantes. Es cuando se concentran las tormentas del Atlántico Norte.</td></tr>
<tr><td>Octubre y marzo</td><td>Puede haber días grandes, pero son menos frecuentes.</td></tr>
<tr><td>Abril a septiembre</td><td>Mar mayormente tranquilo. Buena época para la playa, la luz y las calles.</td></tr>
</tbody></table></div>
<p>Aunque vayas en plena temporada, no hay olas gigantes todos los días. Entre un swell y otro pueden pasar semanas de mar normal. Si el viaje es solo por las olas, conviene tener flexibilidad de unos días y decidir con el pronóstico.</p>

<h2>La competencia: Nazaré Big Wave Challenge 2026/27</h2>
<p>La World Surf League organiza cada invierno el <strong>Nazaré Big Wave Challenge</strong>. Para la temporada 2026/27, el período de espera va del <strong>1 de noviembre de 2026 al 31 de marzo de 2027</strong>. La competencia se hace en un solo día, cuando llega un swell de al menos 25 pies (unos 7,6 metros) y el viento, la marea y la seguridad lo permiten.</p>
<ul>
<li><strong>Alerta amarilla</strong>: se emite hasta 72 horas antes y avisa que el evento podría activarse.</li>
<li><strong>Alerta verde</strong>: confirma que la competencia se hace en las 24 horas siguientes, si las condiciones se mantienen.</li>
</ul>
<p>Compiten nueve equipos invitados de surf remolcado: seis masculinos y tres femeninos. El día de la competencia el Forte se llena desde muy temprano.</p>

<h2>El récord</h2>
<p>El récord Guinness de la ola más grande surfeada lo tiene el alemán <strong>Sebastian Steudtner</strong>: <strong>26,21 metros</strong>, el 29 de octubre de 2020, en Praia do Norte. En 2024 surfeó en el mismo lugar una ola medida en 28,57 metros, que según la información disponible todavía no fue homologada como récord.</p>

<h2>Cómo saber si va a haber olas</h2>
<p>Las olas grandes se ven venir con varios días de anticipación en cualquier pronóstico de surf. Estos son los datos que importan:</p>
<div class="table-wrap"><table>
<thead><tr><th>Dato</th><th>Lo que buscás</th><th>Por qué</th></tr></thead>
<tbody>
<tr><td>Período</td><td>13 segundos o más</td><td>Cuanto más largo el período, más energía trae el mar de fondo y más crece en el cañón.</td></tr>
<tr><td>Dirección del swell</td><td>Oeste o noroeste</td><td>Es la dirección que entra de lleno por el cañón hacia Praia do Norte.</td></tr>
<tr><td>Viento</td><td>Suave, del este o sudeste</td><td>Viento de tierra: ordena la ola y levanta el spray de la cresta.</td></tr>
<tr><td>Marea</td><td>Media, subiendo</td><td>Suele dar las series más fuertes.</td></tr>
</tbody></table></div>
<p>La altura sola engaña. Un pronóstico de 5 metros con 18 segundos de período en Nazaré es mucho más que uno de 6 metros con 10 segundos. Si el período es corto y el viento sopla del oeste, el mar va a estar grande pero desordenado.</p>

<figure class="fig"><img src="/img/acantilado-olas.jpg" alt="Dos personas caminan hacia el borde del acantilado mientras el mar golpea la roca en Praia do Norte, Nazaré." loading="lazy" width="1440" height="960"><figcaption>Desde el sendero que baja a Praia do Norte se ve la fuerza del mar contra la roca. Nazaré.</figcaption></figure>

<h2>Dónde pararse</h2>
<div class="table-wrap"><table>
<thead><tr><th>Lugar</th><th>Para qué sirve</th><th>A tener en cuenta</th></tr></thead>
<tbody>
<tr><td>Explanada del Forte de São Miguel Arcanjo</td><td>Ver romper la ola de frente, con el faro en primer plano. Es el lugar clásico.</td><td>En días grandes se llena. Llegá a primera hora.</td></tr>
<tr><td>Acantilado y sendero hacia Praia do Norte</td><td>Ver la ola de costado y la escala de la gente contra el mar.</td><td>Mantenete lejos del borde y de las zonas cerradas.</td></tr>
<tr><td>Arena de Praia do Norte</td><td>Textura del agua y del spray, a nivel del mar.</td><td>Quedate muy lejos de la orilla. En días grandes el agua sube sin aviso.</td></tr>
<tr><td>Sítio y Miradouro do Suberco</td><td>Vista general del pueblo, la playa y el Forte.</td><td>Desde ahí no se ve bien la ola, pero sirve para ubicarse y para el atardecer.</td></tr>
</tbody></table></div>

<h2>Cómo organizarse ese día</h2>
<ul>
<li><strong>Llegá temprano.</strong> Estacionar cerca del Forte es casi imposible en días grandes. Muchos dejan el auto en el pueblo, suben al Sítio en el ascensor y caminan desde ahí.</li>
<li><strong>Abrigo y protección para la lluvia.</strong> Se pasan horas parado al viento y el spray llega lejos.</li>
<li><strong>Paciencia.</strong> Las series grandes vienen cada tanto. Entre una y otra pueden pasar varios minutos.</li>
<li><strong>Seguí los avisos locales.</strong> La policía marítima cierra zonas cuando el mar está peligroso. Respetarlas no es opcional.</li>
</ul>

<figure class="fig"><img src="/img/maiores-ondas.jpg" alt="Portón de entrada al Forte de São Miguel Arcanjo con la inscripción Maiores Ondas do Mundo y el sol encima." loading="lazy" width="1440" height="960"><figcaption>La entrada al Forte, el punto de observación más conocido. Nazaré.</figcaption></figure>

<h2>Para fotografiarlas</h2>
<ul>
<li><strong>Lente</strong>: para los surfistas hace falta un teleobjetivo largo, entre 400 y 600 mm, porque muchas olas rompen lejos. Para la escala del lugar alcanza con un zoom estándar.</li>
<li><strong>Velocidad</strong>: 1/2000 o más para congelar la ola y el spray. Lo más práctico es el modo manual con ISO automático, como se explica en <a href="/blog/modos-de-la-camara/">Modos de la cámara</a>.</li>
<li><strong>Exposición</strong>: la espuma engaña al fotómetro. Mirá el <a href="/blog/como-leer-el-histograma/">histograma</a> para no quemar la cresta.</li>
<li><strong>Equipo</strong>: llevá un paño para el frente del lente. La sal del spray se pega y arruina la nitidez sin que lo notes en la pantalla.</li>
</ul>
<p>Más allá de la ola, el día de mar grande tiene otras fotos: la gente en el Forte, las motos de agua, la bruma sobre el pueblo. Muchas veces son las que mejor cuentan lo que se vive ahí.</p>
<p class="next">Para ver fotos de Nazaré y la guía para fotografiarla, visitá la <a href="/">página principal</a>.</p>
"""
 },
 "en": {
  "title": "Nazaré big wave season 2026/27: when to go, where to stand and how to tell if the waves are coming",
  "desc": "A practical guide to the giant wave season at Praia do Norte: months, the 2026/27 Nazaré Big Wave Challenge, how to read the forecast, where to watch and how to photograph the waves.",
  "cat": "Nazaré",
  "body": """
<p class="lead">From November to February, Praia do Norte can get the biggest waves ever surfed. There is no fixed date: they show up when a North Atlantic storm sends its swell straight at Nazaré. This guide covers when to go, how to tell whether the waves are coming and where to stand to watch and photograph them.</p>

<h2>Why Nazaré</h2>
<p>Off Praia do Norte lies the <strong>Nazaré Canyon</strong>, an underwater gorge about 230 kilometres long that reaches depths of around 5,000 metres. The canyon carries the swell's energy almost intact to very close to the shore, where the wave suddenly grows. That is why, with the same storm, Nazaré gets much bigger waves than the rest of the Portuguese coast.</p>

<h2>When the season is</h2>
<div class="table-wrap"><table>
<thead><tr><th>Months</th><th>What to expect</th></tr></thead>
<tbody>
<tr><td>November to February</td><td>The best chance of giant waves. This is when North Atlantic storms are most frequent.</td></tr>
<tr><td>October and March</td><td>Big days are possible, but less frequent.</td></tr>
<tr><td>April to September</td><td>Mostly calm sea. A good time for the beach, the light and the streets.</td></tr>
</tbody></table></div>
<p>Even in peak season there are not giant waves every day. Weeks of ordinary sea can pass between swells. If the trip is only about the waves, keep a few days of flexibility and decide with the forecast.</p>

<h2>The contest: Nazaré Big Wave Challenge 2026/27</h2>
<p>Every winter the World Surf League runs the <strong>Nazaré Big Wave Challenge</strong>. For the 2026/27 season the waiting period runs from <strong>1 November 2026 to 31 March 2027</strong>. The contest takes place on a single day, when a swell of at least 25 feet (about 7.6 metres) arrives and wind, tide and safety allow it.</p>
<ul>
<li><strong>Yellow alert</strong>: issued up to 72 hours ahead, it signals that the event may be activated.</li>
<li><strong>Green alert</strong>: confirms the contest will run within the next 24 hours, as long as conditions hold.</li>
</ul>
<p>Nine invited tow-surfing teams compete: six men's and three women's. On contest day the Forte fills up from very early.</p>

<h2>The record</h2>
<p>The Guinness record for the largest wave surfed belongs to Germany's <strong>Sebastian Steudtner</strong>: <strong>26.21 metres</strong>, on 29 October 2020, at Praia do Norte. In 2024 he rode a wave measured at 28.57 metres at the same spot, which, according to available information, has not yet been ratified as a record.</p>

<h2>How to tell whether the waves are coming</h2>
<p>Big waves show up several days ahead in any surf forecast. These are the numbers that matter:</p>
<div class="table-wrap"><table>
<thead><tr><th>Data</th><th>What you want</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Period</td><td>13 seconds or more</td><td>The longer the period, the more energy the swell carries and the more it grows in the canyon.</td></tr>
<tr><td>Swell direction</td><td>West or northwest</td><td>It is the direction that runs straight up the canyon to Praia do Norte.</td></tr>
<tr><td>Wind</td><td>Light, from the east or southeast</td><td>Offshore wind: it cleans up the wave and lifts the spray off the crest.</td></tr>
<tr><td>Tide</td><td>Mid, rising</td><td>It often brings the strongest sets.</td></tr>
</tbody></table></div>
<p>Height alone is misleading. A 5-metre forecast with an 18-second period in Nazaré is far more than 6 metres at 10 seconds. If the period is short and the wind blows from the west, the sea will be big but messy.</p>

<figure class="fig"><img src="/img/acantilado-olas.jpg" alt="Two people walk toward the cliff edge as the sea hits the rock at Praia do Norte, Nazaré." loading="lazy" width="1440" height="960"><figcaption>From the trail down to Praia do Norte you can see the force of the sea against the rock. Nazaré.</figcaption></figure>

<h2>Where to stand</h2>
<div class="table-wrap"><table>
<thead><tr><th>Spot</th><th>What it is good for</th><th>Keep in mind</th></tr></thead>
<tbody>
<tr><td>Forte de São Miguel Arcanjo esplanade</td><td>Watching the wave break head-on, with the lighthouse in the foreground. The classic spot.</td><td>It gets packed on big days. Arrive first thing.</td></tr>
<tr><td>Cliff and trail toward Praia do Norte</td><td>A side view of the wave and the scale of people against the sea.</td><td>Stay away from the edge and from closed areas.</td></tr>
<tr><td>Praia do Norte sand</td><td>Texture of the water and spray, at sea level.</td><td>Stay well back from the shoreline. On big days the water surges without warning.</td></tr>
<tr><td>Sítio and Miradouro do Suberco</td><td>An overview of the town, the beach and the Forte.</td><td>You cannot see the wave well from there, but it is good for getting your bearings and for sunset.</td></tr>
</tbody></table></div>

<h2>Planning the day</h2>
<ul>
<li><strong>Arrive early.</strong> Parking near the Forte is almost impossible on big days. Many people leave the car in town, take the funicular up to the Sítio and walk from there.</li>
<li><strong>Warm clothes and rain gear.</strong> You will stand for hours in the wind, and the spray carries far.</li>
<li><strong>Patience.</strong> Big sets come now and then. Several minutes can pass between them.</li>
<li><strong>Follow local warnings.</strong> The maritime police close areas when the sea is dangerous. Respecting them is not optional.</li>
</ul>

<figure class="fig"><img src="/img/maiores-ondas.jpg" alt="Entrance gate to the Forte de São Miguel Arcanjo with the inscription Maiores Ondas do Mundo and the sun above." loading="lazy" width="1440" height="960"><figcaption>The entrance to the Forte, the best-known viewpoint. Nazaré.</figcaption></figure>

<h2>Photographing them</h2>
<ul>
<li><strong>Lens</strong>: for the surfers you need a long telephoto, between 400 and 600 mm, because many waves break far out. For the scale of the place a standard zoom is enough.</li>
<li><strong>Shutter speed</strong>: 1/2000 or faster to freeze the wave and the spray. The most practical setup is manual mode with auto ISO, as explained in <a href="/en/blog/modos-de-la-camara/">Camera modes</a>.</li>
<li><strong>Exposure</strong>: white water fools the light meter. Check the <a href="/en/blog/como-leer-el-histograma/">histogram</a> so you do not blow out the crest.</li>
<li><strong>Gear</strong>: bring a cloth for the front element. Salt from the spray sticks to it and ruins sharpness without showing on the screen.</li>
</ul>
<p>Beyond the wave, a big-sea day has other photographs: the crowd at the Forte, the jet skis, the mist over the town. Often they tell the story of the day best.</p>
<p class="next">To see photographs of Nazaré and the guide to photographing it, visit the <a href="/en/">home page</a>.</p>
"""
 },
},
]
