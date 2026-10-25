import json, html
meta = json.load(open("/home/claude/web/meta.json"))

CH = [
 ("mar", "I", "El mar",
  "Praia do Norte es la playa de las olas más grandes del mundo. El cañón submarino de Nazaré concentra la energía del Atlántico frente al Forte, y en invierno el mar se vuelve espectáculo.",
  [
   ("forte-bruma","Día grande en Praia do Norte","Forte de São Miguel Arcanjo","La bruma de las olas cubre el acantilado. La gente sobre el Forte da la escala de lo que está pasando abajo."),
   ("ola-spray","El viento contra la ola","Praia do Norte","El viento de tierra levanta la cresta y la deja suspendida. Es el viento que esperan los surfistas."),
   ("praia-do-norte","Praia do Norte desde el acantilado","Praia do Norte","Las personas sobre la arena son puntos. Ellas dan la medida de la playa."),
   ("acantilado-olas","Mirar desde arriba","Praia do Norte","Dos personas caminan hacia el borde mientras el mar golpea la roca. Vista en picado desde el sendero."),
   ("acantilado-pueblo","El acantilado y la bahía","Sítio da Nazaré","La roca nítida en primer plano y el pueblo suave al fondo separan los planos y dan profundidad."),
   ("westfalia","Westfalia frente al mar","Costa de Nazaré","La cultura del surf y las furgonetas, en rojo contra el azul del Atlántico."),
  ]),
 ("pueblo", "II", "El pueblo",
  "Entre la playa y el Sítio vive un pueblo de pescadores con calles que bajan al mar, barcos pintados a mano y muros donde los gatos miran pasar a la gente.",
  [
   ("calle-mar","La calle termina en el mar","Praia da Nazaré","Las fachadas forman un corredor y la luz entra por el fondo, donde está el mar."),
   ("pino-sitio","El pueblo entre ramas","Vista hacia el Sítio","Las ramas del pino enmarcan los techos, el acantilado y el Forte. El tronco a la derecha da profundidad."),
   ("farol","Al faro","Nazaré","El cartel nítido y la calle desenfocada cuentan hacia dónde va todo el mundo."),
   ("barcos","Barcos de la playa","Praia da Nazaré","Las embarcaciones tradicionales de pesca descansan sobre la arena, pintadas con los colores de siempre."),
   ("avenida-ascensor","La avenida y el ascensor","Praia da Nazaré","El ascensor une la playa con el Sítio, en lo alto del acantilado."),
   ("tuktuk","Tuk-tuk en el acantilado","Nazaré","Tres momentos en el mismo cuadro: un hombre al teléfono, el tuk-tuk y dos personas que siguen camino."),
   ("arco","Bajo el arco","Nazaré","Un encuadre dentro del encuadre. Los carteles de tránsito suman algo de humor."),
   ("mural","Dos generaciones","Nazaré","Mural sobre una medianera: la mujer nazarena tradicional y una joven, unidas por una trenza."),
   ("santuario","Santuario de Nossa Senhora da Nazaré","Sítio da Nazaré","Las torres del santuario contra un cielo limpio de invierno."),
   ("casa-amarilla","La casa amarilla","Nazaré","Palomas en el techo y una gaviota en vuelo sobre la fachada."),
   ("amapola","Amapola en la calçada","Nazaré","Una flor que creció en la junta de la vereda de piedra portuguesa."),
   ("noria","Feria con tormenta","Nazaré","La noria iluminada por un claro de sol, con el cielo cargado detrás."),
  ]),
 ("luz", "III", "La luz",
  "Nazaré mira al oeste. Cada tarde el sol baja sobre el Atlántico y el pueblo entero se acerca a los miradores para verlo.",
  [
   ("familia","Bajada al atardecer","Nazaré","Contraluz y sombras largas. La familia camina hacia el mar al final del día."),
   ("dorado","Última luz sobre la playa","Vista desde el Sítio","La luz rasante pinta el pasto y los techos. La pareja arriba a la izquierda mira lo mismo que nosotros."),
   ("maiores-ondas","Maiores Ondas do Mundo","Acceso al Forte","El portal de entrada a Praia do Norte, con el sol justo encima."),
   ("contraluz","Contraluz en la avenida","Praia da Nazaré","El sol detrás de las nubes y la vereda brillando hacia el mar."),
   ("forte-dorado","El Forte en silueta","Forte de São Miguel Arcanjo","El faro rojo y el reflejo del sol sobre el agua equilibran el cuadro."),
   ("farol-mirador","Farol en el mirador","Miradouro do Suberco, Sítio","El cielo encendido después de la puesta. El farol y las personas son el sujeto."),
   ("ciervo","El ciervo","Camino al Forte","La escultura del ciervo surfista, iluminada por un claro entre las nubes."),
   ("noche","Nazaré de noche","Vista desde el Sítio","La curva de la playa y las luces de la avenida, en la hora azul."),
  ]),
]
CATS = [
 ("gato-siames","El siamés del patio","Nazaré","Mira a cámara. Las plantas adelante y el otro gato a la izquierda dan capas."),
 ("gato-muro","Guardián del muro","Nazaré","La diagonal del muro, la pared cálida y el cielo frío."),
 ("gato-salto","El salto","Nazaré","El instante justo en que deja la maceta rumbo a la ventana."),
]

ALL=[]
def fig(slug,t,place,note,chap,cls=""):
    i=len(ALL); ALL.append(dict(s=slug,t=t,p=place,n=note,c=chap))
    w,h=meta[slug]
    return (f'<figure class="ph {cls}" data-i="{i}"><button class="open" aria-label="Ampliar: {html.escape(t)}">'
            f'<img src="img/{slug}-s.jpg" width="{w}" height="{h}" decoding="async" alt="{html.escape(t)}. {html.escape(place)}, Nazaré, Portugal. Fotografía de Matías Silva."></button>'
            f'<figcaption><span class="t">{html.escape(t)}</span><span class="p">{html.escape(place)}</span></figcaption></figure>')

chap_html=""
for key,num,title,intro,photos in CH:
    figs="".join(fig(s,t,p,n,title) for s,t,p,n in photos)
    extra=""
    if key=="pueblo":
        cats="".join(fig(s,t,p,n,"El pueblo · Serie gatos","cat") for s,t,p,n in CATS)
        extra=f'''<div class="series"><div class="series-head"><p class="eyebrow">Serie</p><h3>Los gatos del pueblo</h3><p>Viven en los patios y sobre los muros. Nadie los apura.</p></div><div class="cats">{cats}</div></div>'''
    chap_html+=f'''
<section id="{key}" class="chapter wrap" aria-labelledby="h-{key}">
  <header class="ch-head">
    <span class="num">{num}</span>
    <div><h2 id="h-{key}">{title}</h2><p>{intro}</p></div>
    <span class="count">{len(photos)+(3 if key=="pueblo" else 0)} fotografías</span>
  </header>
  <div class="grid">{figs}</div>{extra}
</section>'''

covers=[("mar","forte-bruma","El mar","Olas, acantilado y el Forte"),("pueblo","barcos","El pueblo","Calles, barcos y gatos"),("luz","dorado","La luz","Atardeceres y la hora azul")]
cover_html="".join(f'<a class="cover" href="#{k}"><img src="img/{s}-s.jpg" alt="" width="{meta[s][0]}" height="{meta[s][1]}"><span class="cn">{n}</span><span class="cd">{d}</span></a>' for k,s,n,d in covers)

SPOTS=[
 ("forte-dorado","Forte de São Miguel Arcanjo","El punto clásico para ver las olas grandes. El faro está sobre el acantilado que separa Praia do Norte del pueblo; desde la explanada se ve romper la ola de frente.","Olas grandes · teleobjetivo largo"),
 ("ola-spray","Praia do Norte, desde la arena","Para la textura del agua y el spray. Bajá por el sendero y quedate lejos de la orilla: en días grandes el mar sube sin aviso.","Detalle de olas · velocidad alta"),
 ("dorado","Sítio y Miradouro do Suberco","El mirador sobre el pueblo. Es el lugar para el atardecer y para la hora azul, cuando se encienden las luces de la avenida.","Atardecer y noche · trípode"),
 ("barcos","Praia da Nazaré y el pueblo","La playa de los barcos tradicionales y las calles que bajan al mar. Buena para fotografía de calle por la mañana y al final de la tarde.","Calle y cultura · lente fija"),
]
spot_html="".join(f'<article class="spot"><img src="img/{s}-s.jpg" alt="{html.escape(n)}" width="{meta[s][0]}" height="{meta[s][1]}"><div><h3>{n}</h3><p>{d}</p><span class="tag">{tg}</span></div></article>' for s,n,d,tg in SPOTS)

FAQ=[
 ("¿Cuándo hay olas grandes en Nazaré?","La temporada va de octubre a marzo. Noviembre, diciembre, enero y febrero son los meses con más probabilidad de olas gigantes. De mayo a agosto el mar suele estar tranquilo."),
 ("¿Por qué las olas de Nazaré son tan grandes?","Frente a Praia do Norte hay un cañón submarino que concentra la energía del oleaje del Atlántico Norte. Cuando llega una tormenta grande, la ola crece al entrar al cañón."),
 ("¿Dónde conviene pararse para fotografiar las olas?","En la explanada del Forte de São Miguel Arcanjo, sobre el acantilado. En días grandes hay mucha gente y es difícil estacionar, así que conviene llegar temprano."),
 ("¿Qué lente hace falta?","Para los surfistas, un teleobjetivo largo, entre 400 y 600 mm, porque muchas olas rompen lejos. Para el paisaje y la escala del lugar alcanza con un zoom estándar."),
 ("¿Cómo saber si va a haber olas grandes?","Hay que mirar el pronóstico de oleaje: período de 13 segundos o más, mar de fondo del oeste o noroeste y viento suave del este o sudeste. La marea media subiendo suele dar las series más fuertes."),
]
faq_html="".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ)

ld=[
 {"@context":"https://schema.org","@type":"Person","name":"Matías Silva","jobTitle":"Fotógrafo","email":"mailto:matiassilva.ph@gmail.com","homeLocation":{"@type":"Place","name":"San Miguel, Buenos Aires, Argentina"},
  "sameAs":["https://www.instagram.com/matiassilva.ph/","https://www.instagram.com/vivanazare/"],
  "knowsAbout":["Fotografía de Nazaré","Praia do Norte","Fotografía de olas grandes","Fotografía de calle"]},
 {"@context":"https://schema.org","@type":"ImageGallery","name":"Nazaré — Fotografía de Matías Silva","about":{"@type":"Place","name":"Nazaré, Portugal"},
  "author":{"@type":"Person","name":"Matías Silva"},
  "image":[{"@type":"ImageObject","contentUrl":f"https://matiassilvaph.netlify.app/img/{a['s']}.jpg","name":a["t"],"description":a["n"],"contentLocation":{"@type":"Place","name":a["p"]+", Nazaré, Portugal"},"creator":{"@type":"Person","name":"Matías Silva"},"creditText":"Matías Silva","copyrightNotice":"© 2026 Matías Silva","copyrightHolder":{"@type":"Person","name":"Matías Silva"}} for a in ALL]},
 {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]},
]

page=open("/home/claude/web/template.html").read()
page=(page.replace("{{CHAPTERS}}",chap_html).replace("{{COVERS}}",cover_html).replace("{{SPOTS}}",spot_html)
      .replace("{{FAQ}}",faq_html).replace("{{LD}}",json.dumps(ld,ensure_ascii=False))
      .replace("{{DATA}}",json.dumps(ALL,ensure_ascii=False)).replace("{{N}}",str(len(ALL)))
      .replace("{{HW}}",str(meta["familia"][0])).replace("{{HH}}",str(meta["familia"][1])))
open("/home/claude/web/site/index.html","w").write(page)
print(len(ALL),"fotos")
