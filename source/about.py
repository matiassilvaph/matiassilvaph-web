import sys, os, html
sys.path.insert(0, "/home/claude/web")
import blog

SITE = blog.SITE
MAIL = "matiassilva.ph@gmail.com"
IG = "https://www.instagram.com/matiassilva.ph/"
VN = "https://www.instagram.com/vivanazare/"

CSS = """
.ab-head{padding-block:40px 28px;border-bottom:1px solid var(--line);margin-bottom:36px;max-width:860px}
.ab-head h1{font-family:var(--display);font-weight:400;font-size:clamp(2.6rem,7vw,5rem);line-height:.95;margin:0 0 16px}
.ab-head .lead{font-family:var(--display);font-size:clamp(1.3rem,2.6vw,1.7rem);line-height:1.35;margin:0;color:var(--fg);max-width:40ch}
.ab-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:40px;align-items:start}
.ab-grid figure{margin:0;position:sticky;top:90px}
.ab-grid figure img{width:100%;aspect-ratio:3/4;object-fit:cover}
.ab-grid figcaption{font:12px/1.7 var(--mono);color:var(--muted);padding-top:8px}
.ab-text h2{font-family:var(--display);font-weight:400;font-size:clamp(1.6rem,3vw,2.1rem);margin:1.6em 0 .5em}
.ab-text h2:first-child{margin-top:0}
.ab-text p{margin:0 0 1.05em;max-width:66ch}
.ab-text a{color:var(--accent)}
.facts2{display:grid;grid-template-columns:max-content 1fr;gap:10px 24px;margin:0 0 8px;padding:20px;border:1px solid var(--line);background:var(--surface);max-width:66ch}
.facts2 dt{font:12px var(--mono);text-transform:uppercase;letter-spacing:.08em;color:var(--muted);padding-top:3px}
.facts2 dd{margin:0}
.ab-text .faq details{max-width:66ch}
@media (max-width:820px){.ab-grid{grid-template-columns:1fr}.ab-grid figure{position:static;max-width:360px}.facts2{grid-template-columns:1fr;gap:2px}.facts2 dd{margin-bottom:10px}}
"""

T = {
 "es": dict(
  url="/sobre/",
  title="Matías Silva · Fotógrafo argentino de San Miguel y Nazaré",
  desc="Matías Silva es un fotógrafo argentino de San Miguel, Buenos Aires, que fotografía Nazaré, Portugal: las olas grandes de Praia do Norte, el pueblo y la luz del Atlántico.",
  eyebrow="Sobre mí", h1="Matías Silva",
  lead="Fotógrafo argentino. Vivo en San Miguel, Buenos Aires, y fotografío Nazaré, Portugal.",
  alt="Matías Silva asomado a una ventana en un muro de piedra del Forte de São Miguel Arcanjo, Nazaré.", cap="Forte de São Miguel Arcanjo, Nazaré.",
  sections=[
   ("Nazaré", [
     "Imaginé Nazaré durante años antes de conocerla. La seguía desde 2014 y llegué por primera vez en 2022.",
     "Después viví tres años en Portugal. Una parte de ese tiempo la pasé instalado en Nazaré y el resto viajaba hasta allá cada vez que podía, para conocer sus olas, su cultura y su gente. De ahí sale la forma en que la fotografío.",
     "Creé <a href=\"" + VN + "\" rel=\"noopener\">Viva Nazaré</a>, un proyecto dedicado a la gente, la cultura y las olas gigantes del pueblo. Soy cofundador de Nazaré Inside, que publica reportes sobre las olas y la vida local.",
   ]),
   ("Qué fotografío", [
     "El mar y las olas grandes, el surf, la calle, la naturaleza y la arquitectura: edificios, techos, lo que queda en pie entre lo que se mueve. Prefiero una edición sobria, más oscura y fría, y publico mis fotos sin marca de agua.",
     "Trabajo con una Sony A7 III y un 50 mm f/1.8. Me preparo para volver a Nazaré en el invierno de 2027 y fotografiar la temporada de olas grandes desde el Forte.",
   ]),
   ("Qué escribo", [
     "En el <a href=\"/blog/\">blog</a> explico fotografía de forma simple, con conceptos que sirven para cualquier cámara, y guías para fotografiar Nazaré. Todo el sitio está en español, inglés y portugués.",
   ]),
  ],
  facts_h="En resumen",
  facts=[("Nombre","Matías Silva"),("Base","San Miguel, Buenos Aires, Argentina"),("Fotografía","Nazaré (Portugal), mar y olas grandes, calle, naturaleza"),
         ("Proyectos","Viva Nazaré · cofundador de Nazaré Inside"),("Instagram","<a href=\"" + IG + "\" rel=\"noopener\">@matiassilva.ph</a>"),("Contacto",MAIL)],
  faq_h="Preguntas frecuentes",
  faq=[
   ("¿Quién es Matías Silva?","Matías Silva es un fotógrafo argentino de San Miguel, Buenos Aires. Fotografía Nazaré, Portugal, donde pasó parte de los tres años que vivió en ese país, y escribe un blog de fotografía en español, inglés y portugués."),
   ("¿Dónde vive Matías Silva?","En San Miguel, en el noroeste del Gran Buenos Aires, Argentina."),
   ("¿Qué relación tiene con Nazaré?","Vivió tres años en Portugal, parte de ellos en Nazaré. Creó Viva Nazaré, un proyecto sobre la gente, la cultura y las olas del pueblo, y es cofundador de Nazaré Inside."),
   ("¿Qué fotografía?","Mar y olas grandes, surf, fotografía de calle, naturaleza y arquitectura."),
   ("¿Cómo contactarlo?","Por correo a " + MAIL + " o por mensaje directo en Instagram, @matiassilva.ph."),
  ],
  job="Fotógrafo"),
 "en": dict(
  url="/en/sobre/",
  title="Matías Silva · Argentine photographer from San Miguel and Nazaré",
  desc="Matías Silva is an Argentine photographer from San Miguel, Buenos Aires, who photographs Nazaré, Portugal: the big waves of Praia do Norte, the town and the Atlantic light.",
  eyebrow="About", h1="Matías Silva",
  lead="Argentine photographer. I live in San Miguel, Buenos Aires, and I photograph Nazaré, Portugal.",
  alt="Matías Silva at a window in a stone wall of the Forte de São Miguel Arcanjo, Nazaré.", cap="Forte de São Miguel Arcanjo, Nazaré.",
  sections=[
   ("Nazaré", [
     "I imagined Nazaré for years before I knew it. I had followed it since 2014 and first got there in 2022.",
     "Then I lived in Portugal for three years. Part of that time I was based in Nazaré, and the rest I travelled there whenever I could, to get to know its waves, its culture and its people. That is where the way I photograph it comes from.",
     "I created <a href=\"" + VN + "\" rel=\"noopener\">Viva Nazaré</a>, a project dedicated to the people, the culture and the giant waves of the town. I am a co-founder of Nazaré Inside, which publishes reports on the waves and local life.",
   ]),
   ("What I photograph", [
     "The sea and big waves, surfing, the street, nature and architecture: buildings, rooftops, what stays standing among what moves. I prefer a restrained edit, darker and cooler, and I publish my photographs without a watermark.",
     "I work with a Sony A7 III and a 50 mm f/1.8. I am preparing to return to Nazaré in the winter of 2027 to photograph the big wave season from the Forte.",
   ]),
   ("What I write", [
     "On the <a href=\"/en/blog/\">blog</a> I explain photography simply, with concepts that work with any camera, and guides to photographing Nazaré. The whole site is in Spanish, English and Portuguese.",
   ]),
  ],
  facts_h="At a glance",
  facts=[("Name","Matías Silva"),("Based in","San Miguel, Buenos Aires, Argentina"),("Photographs","Nazaré (Portugal), the sea and big waves, street, nature"),
         ("Projects","Viva Nazaré · co-founder of Nazaré Inside"),("Instagram","<a href=\"" + IG + "\" rel=\"noopener\">@matiassilva.ph</a>"),("Contact",MAIL)],
  faq_h="Frequently asked questions",
  faq=[
   ("Who is Matías Silva?","Matías Silva is an Argentine photographer from San Miguel, Buenos Aires. He photographs Nazaré, Portugal, where he spent part of the three years he lived in that country, and writes a photography blog in Spanish, English and Portuguese."),
   ("Where does Matías Silva live?","In San Miguel, in the north-west of Greater Buenos Aires, Argentina."),
   ("What is his connection to Nazaré?","He lived in Portugal for three years, part of them in Nazaré. He created Viva Nazaré, a project about the town's people, culture and waves, and is a co-founder of Nazaré Inside."),
   ("What does he photograph?","The sea and big waves, surfing, street photography, nature and architecture."),
   ("How can I contact him?","By email at " + MAIL + " or by direct message on Instagram, @matiassilva.ph."),
  ],
  job="Photographer"),
 "pt": dict(
  url="/pt/sobre/",
  title="Matías Silva · Fotógrafo argentino de San Miguel e da Nazaré",
  desc="Matías Silva é um fotógrafo argentino de San Miguel, Buenos Aires, que fotografa a Nazaré: as ondas grandes da Praia do Norte, a vila e a luz do Atlântico.",
  eyebrow="Sobre mim", h1="Matías Silva",
  lead="Fotógrafo argentino. Vivo em San Miguel, Buenos Aires, e fotografo a Nazaré.",
  alt="Matías Silva numa janela de um muro de pedra do Forte de São Miguel Arcanjo, Nazaré.", cap="Forte de São Miguel Arcanjo, Nazaré.",
  sections=[
   ("Nazaré", [
     "Imaginei a Nazaré durante anos antes de a conhecer. Acompanhava-a desde 2014 e cheguei lá pela primeira vez em 2022.",
     "Depois vivi três anos em Portugal. Parte desse tempo morei na Nazaré e, no resto, ia lá sempre que podia, para conhecer as suas ondas, a sua cultura e a sua gente. É daí que vem a forma como a fotografo.",
     "Criei o <a href=\"" + VN + "\" rel=\"noopener\">Viva Nazaré</a>, um projeto dedicado às pessoas, à cultura e às ondas gigantes da vila. Sou cofundador do Nazaré Inside, que publica relatos sobre as ondas e a vida local.",
   ]),
   ("O que fotografo", [
     "O mar e as ondas grandes, o surf, a rua, a natureza e a arquitetura: edifícios, telhados, o que fica de pé no meio do que se move. Prefiro uma edição sóbria, mais escura e fria, e publico as minhas fotografias sem marca de água.",
     "Trabalho com uma Sony A7 III e uma 50 mm f/1.8. Estou a preparar-me para voltar à Nazaré no inverno de 2027 e fotografar a época das ondas grandes a partir do Forte.",
   ]),
   ("O que escrevo", [
     "No <a href=\"/pt/blog/\">blog</a> explico fotografia de forma simples, com conceitos que servem para qualquer câmara, e guias para fotografar a Nazaré. Todo o site está em espanhol, inglês e português.",
   ]),
  ],
  facts_h="Em resumo",
  facts=[("Nome","Matías Silva"),("Base","San Miguel, Buenos Aires, Argentina"),("Fotografia","Nazaré (Portugal), mar e ondas grandes, rua, natureza"),
         ("Projetos","Viva Nazaré · cofundador do Nazaré Inside"),("Instagram","<a href=\"" + IG + "\" rel=\"noopener\">@matiassilva.ph</a>"),("Contacto",MAIL)],
  faq_h="Perguntas frequentes",
  faq=[
   ("Quem é Matías Silva?","Matías Silva é um fotógrafo argentino de San Miguel, Buenos Aires. Fotografa a Nazaré, onde passou parte dos três anos em que viveu em Portugal, e escreve um blog de fotografia em espanhol, inglês e português."),
   ("Onde vive Matías Silva?","Em San Miguel, no noroeste da Grande Buenos Aires, Argentina."),
   ("Qual é a ligação dele à Nazaré?","Viveu três anos em Portugal, parte deles na Nazaré. Criou o Viva Nazaré, um projeto sobre as pessoas, a cultura e as ondas da vila, e é cofundador do Nazaré Inside."),
   ("O que fotografa?","O mar e as ondas grandes, o surf, a fotografia de rua, a natureza e a arquitetura."),
   ("Como o contactar?","Por e-mail para " + MAIL + " ou por mensagem direta no Instagram, @matiassilva.ph."),
  ],
  job="Fotógrafo"),
}

LANG_TAG = {"es": "es", "en": "en", "pt": "pt-PT"}

for lang, t in T.items():
    secs = "".join(f"<h2>{h}</h2>" + "".join(f"<p>{p}</p>" for p in ps) for h, ps in t["sections"])
    facts = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in t["facts"])
    faq = "".join(f"<details><summary>{q}</summary><p>{html.escape(a)}</p></details>" for q, a in t["faq"])
    content = f"""<div class="wrap">
  <header class="ab-head"><p class="eyebrow">{t['eyebrow']}</p><h1>{t['h1']}</h1><p class="lead">{t['lead']}</p></header>
  <div class="ab-grid">
    <figure><img src="/img/matias-forte.jpg" width="960" height="1276" alt="{html.escape(t['alt'])}"><figcaption>{t['cap']}</figcaption></figure>
    <div class="ab-text">
      {secs}
      <h2>{t['facts_h']}</h2>
      <dl class="facts2">{facts}</dl>
      <section class="faq"><h2>{t['faq_h']}</h2>{faq}</section>
    </div>
  </div>
</div>"""
    person = {"@type": "Person", "@id": SITE + "/#matias-silva", "name": "Matías Silva", "alternateName": "matiassilva.ph",
              "jobTitle": t["job"], "nationality": {"@type": "Country", "name": "Argentina"},
              "homeLocation": {"@type": "Place", "name": "San Miguel, Buenos Aires, Argentina"},
              "url": SITE + "/", "email": "mailto:" + MAIL, "image": [SITE + "/img/matias.jpg", SITE + "/img/matias-forte.jpg"],
              "sameAs": [IG, VN],
              "knowsAbout": ["Nazaré", "Praia do Norte", "Big wave photography", "Surf photography", "Street photography", "Photography education"],
              "affiliation": [{"@type": "Organization", "name": "Viva Nazaré", "url": VN}, {"@type": "Organization", "name": "Nazaré Inside"}]}
    ld = [{"@type": "ProfilePage", "url": SITE + t["url"], "inLanguage": LANG_TAG[lang],
           "name": t["title"], "description": t["desc"], "mainEntity": person},
          {"@type": "FAQPage", "inLanguage": LANG_TAG[lang],
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}]
    pg = blog.page(lang, t["title"], t["desc"], t["url"], "/sobre/", "/en/sobre/", {"@context": "https://schema.org", "@graph": ld}, content, "familia", alt_pt="/pt/sobre/")
    pg = pg.replace("</style>", CSS + "</style>", 1)
    path = "/home/claude/web/site" + t["url"] + "index.html"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(pg)
print("sobre ok")
