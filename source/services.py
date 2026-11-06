import sys, os, html
sys.path.insert(0, "/home/claude/web")
import blog  # reutiliza page(), CSS y textos comunes

SITE = blog.SITE
MAIL = "matiassilva.ph@gmail.com"
AREA = ["San Miguel", "Bella Vista", "Muñiz", "José C. Paz", "Hurlingham", "Pilar"]

CSS = """
.svc-head{padding-block:40px 28px;border-bottom:1px solid var(--line);margin-bottom:36px;max-width:820px}
.svc-head h1{font-family:var(--display);font-weight:400;font-size:clamp(2.4rem,6vw,4.4rem);line-height:1;margin:0 0 16px;text-wrap:balance}
.svc-head p{margin:0;color:var(--muted);max-width:62ch;font-size:1.05rem}
.launch{display:inline-flex;gap:10px;align-items:center;margin-top:20px;font:12px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--accent);border:1px solid var(--accent);padding:8px 12px}
.svcs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}
.svc{border:1px solid var(--line);background:var(--surface);padding:28px;display:flex;flex-direction:column;gap:14px}
.svc h2{font-family:var(--display);font-weight:400;font-size:1.8rem;line-height:1.1;margin:0}
.svc .price{font:400 2.2rem/1 var(--display);color:var(--fg)}
.svc .price small{display:block;font:12px var(--mono);color:var(--muted);letter-spacing:.06em;margin-top:6px}
.svc ul{margin:0;padding-left:18px;color:#c9c5be}
.svc li{margin-bottom:6px}
.svc .note{font-size:.9rem;color:var(--muted);margin:0}
.svc.soon{opacity:.75}
.steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px;margin-top:8px}
.step{border-top:1px solid var(--line);padding-top:14px}
.step .n{font:italic 2.2rem/1 var(--display);color:var(--accent)}
.step h3{font:500 1rem var(--body);margin:8px 0 4px}
.step p{margin:0;color:var(--muted);font-size:.92rem}
.block{padding-block:56px 0}
.block > h2{font-family:var(--display);font-weight:400;font-size:clamp(1.8rem,3.4vw,2.4rem);margin:0 0 20px}
.contact-box{border:1px solid var(--accent);padding:28px;display:flex;flex-direction:column;gap:10px;max-width:640px}
.contact-box .mail{font:400 1.6rem var(--display);user-select:all;overflow-wrap:anywhere}
.contact-box p{margin:0;color:var(--muted)}
.contact-box a{color:var(--accent)}
@media (max-width:860px){.svcs{grid-template-columns:1fr}.steps{grid-template-columns:1fr 1fr}}
@media (max-width:480px){.steps{grid-template-columns:1fr}}
"""

T = {
 "es": dict(
  url="/servicios/", title="Servicios de fotografía en San Miguel · Matías Silva",
  desc="Retrato profesional para asesores inmobiliarios, equipos y eventos en San Miguel, Bella Vista y zona norte del conurbano. Fotografía por sesión, con agenda limitada.",
  eyebrow="Servicios", h1="Fotografía por sesión en San Miguel",
  intro="Trabajo por sesión, no por cantidad de fotos. Cada encuentro incluye la dirección, la edición y una entrega cuidada. Tomo pocas sesiones por mes para dedicarle a cada una el tiempo que necesita.",
  launch="Valores de lanzamiento · Noviembre 2026",
  svcs=[
   ("Retrato profesional para asesores", "$140.000", "por sesión",
    ["1,5 horas en locación: oficina, propiedad o exterior", "2 cambios de ropa", "Dirección de pose y expresión", "10 fotografías editadas", "Entrega en 5 días hábiles"],
    "Pensado para perfiles en portales, redes y tarjetas profesionales.", False),
   ("Equipo inmobiliario", "$380.000", "hasta 5 personas",
    ["Media mañana en la oficina o en locación", "Retratos individuales de cada asesor", "Foto de equipo", "Estilo de edición unificado para toda la inmobiliaria"],
    "Para que todo el equipo tenga una imagen coherente.", False),
   ("Eventos seleccionados", "$220.000", "hasta 3 horas",
    ["Cobertura documental, sin interrumpir", "Edición de la selección final", "Entrega en 10 días hábiles"],
    "Presentaciones, lanzamientos y encuentros. Tomo pocos eventos y elijo los que encajan con mi trabajo.", False),
   ("Fotografía de propiedades", "A consulta", "próximamente",
    ["Interiores y exteriores", "Luz natural", "Fotos listas para portales"],
    "Disponible en los próximos meses.", True),
  ],
  how="Cómo trabajo", steps=[("Consulta","Me escribís con la idea y la fecha."),("Charla breve","Definimos lugar, ropa y estilo."),("Sesión","Sin apuro y con dirección en todo momento."),("Entrega","Galería online con las fotos editadas.")],
  faq_h="Preguntas frecuentes",
  faq=[
   ("¿En qué zonas trabajás?", "En San Miguel, Bella Vista, Muñiz, José C. Paz, Hurlingham y Pilar. Para otras zonas de Buenos Aires, consultame."),
   ("¿Por qué cobrás por sesión y no por foto?", "Porque lo que se paga es el trabajo completo: la preparación, la dirección durante la sesión y la edición. Entrego las mejores fotos, no la mayor cantidad."),
   ("¿Qué ropa conviene llevar a un retrato profesional?", "Colores lisos y neutros, sin estampados chicos ni logos. Conviene llevar una opción formal y otra más relajada. Lo hablamos antes de la sesión."),
   ("¿Cuánto tarda la entrega?", "Cinco días hábiles para retratos y diez para eventos."),
   ("¿Por qué dicen valores de lanzamiento?", "Porque son los valores de los primeros trabajos en San Miguel. Se actualizan periódicamente."),
  ],
  contact_h="Consultas", contact_p="Escribime con el tipo de sesión, la fecha que tenés en mente y la zona.", ig="O por mensaje directo en Instagram:",
  areaname="San Miguel, Buenos Aires"),
 "en": dict(
  url="/en/servicios/", title="Photography services in San Miguel, Buenos Aires · Matías Silva",
  desc="Professional portraits for real estate agents, teams and events in San Miguel, Bella Vista and Buenos Aires' northern suburbs. Priced per session, limited availability.",
  eyebrow="Services", h1="Photography by session in San Miguel, Buenos Aires",
  intro="I work by session, not by number of photos. Every shoot includes direction, editing and a careful delivery. I take only a few sessions a month so each one gets the time it needs.",
  launch="Launch rates · November 2026",
  svcs=[
   ("Professional portraits for real estate agents", "ARS 140,000", "per session",
    ["1.5 hours on location: office, property or outdoors", "2 outfit changes", "Posing and expression direction", "10 edited photographs", "Delivered within 5 business days"],
    "For listing portals, social media and business cards.", False),
   ("Real estate team", "ARS 380,000", "up to 5 people",
    ["Half a morning at the office or on location", "Individual portraits of each agent", "Team photo", "One consistent editing style for the whole agency"],
    "So the whole team has a consistent image.", False),
   ("Selected events", "ARS 220,000", "up to 3 hours",
    ["Documentary coverage, without interrupting", "Editing of the final selection", "Delivered within 10 business days"],
    "Launches, presentations and gatherings. I take few events and choose the ones that fit my work.", False),
   ("Property photography", "On request", "coming soon",
    ["Interiors and exteriors", "Natural light", "Photos ready for listing portals"],
    "Available in the coming months.", True),
  ],
  how="How I work", steps=[("Enquiry","Write to me with the idea and the date."),("Short call","We decide location, clothing and style."),("Session","Unhurried, with direction throughout."),("Delivery","An online gallery with the edited photos.")],
  faq_h="Frequently asked questions",
  faq=[
   ("Which areas do you cover?", "San Miguel, Bella Vista, Muñiz, José C. Paz, Hurlingham and Pilar. For other parts of Buenos Aires, get in touch."),
   ("Why do you charge per session and not per photo?", "Because what you pay for is the whole job: preparation, direction during the session and editing. I deliver the best photos, not the most."),
   ("What should I wear for a professional portrait?", "Plain, neutral colours, no small prints or logos. Bring one formal option and one more relaxed. We talk it through before the session."),
   ("How long does delivery take?", "Five business days for portraits and ten for events."),
   ("Why launch rates?", "They are the rates for my first jobs in San Miguel. They are reviewed periodically."),
  ],
  contact_h="Enquiries", contact_p="Write to me with the type of session, the date you have in mind and the area.", ig="Or send a direct message on Instagram:",
  areaname="San Miguel, Buenos Aires"),
 "pt": dict(
  url="/pt/servicios/", title="Serviços de fotografia em San Miguel, Buenos Aires · Matías Silva",
  desc="Retrato profissional para consultores imobiliários, equipas e eventos em San Miguel, Bella Vista e na zona norte da Grande Buenos Aires. Preço por sessão, agenda limitada.",
  eyebrow="Serviços", h1="Fotografia por sessão em San Miguel, Buenos Aires",
  intro="Trabalho por sessão, não por número de fotografias. Cada sessão inclui a direção, a edição e uma entrega cuidada. Aceito poucas sessões por mês para dedicar a cada uma o tempo de que precisa.",
  launch="Preços de lançamento · Novembro 2026",
  svcs=[
   ("Retrato profissional para consultores imobiliários", "ARS 140.000", "por sessão",
    ["1,5 horas no local: escritório, imóvel ou exterior", "2 mudas de roupa", "Direção de pose e expressão", "10 fotografias editadas", "Entrega em 5 dias úteis"],
    "Pensado para perfis em portais, redes sociais e cartões profissionais.", False),
   ("Equipa imobiliária", "ARS 380.000", "até 5 pessoas",
    ["Meia manhã no escritório ou no local", "Retratos individuais de cada consultor", "Fotografia de equipa", "Estilo de edição único para toda a imobiliária"],
    "Para que toda a equipa tenha uma imagem coerente.", False),
   ("Eventos selecionados", "ARS 220.000", "até 3 horas",
    ["Cobertura documental, sem interromper", "Edição da seleção final", "Entrega em 10 dias úteis"],
    "Apresentações, lançamentos e encontros. Aceito poucos eventos e escolho os que se ajustam ao meu trabalho.", False),
   ("Fotografia de imóveis", "Sob consulta", "brevemente",
    ["Interiores e exteriores", "Luz natural", "Fotografias prontas para portais"],
    "Disponível nos próximos meses.", True),
  ],
  how="Como trabalho", steps=[("Contacto","Escreve-me com a ideia e a data."),("Conversa breve","Definimos local, roupa e estilo."),("Sessão","Sem pressa e com direção a todo o momento."),("Entrega","Galeria online com as fotografias editadas.")],
  faq_h="Perguntas frequentes",
  faq=[
   ("Em que zonas trabalhas?", "Em San Miguel, Bella Vista, Muñiz, José C. Paz, Hurlingham e Pilar. Para outras zonas de Buenos Aires, contacta-me."),
   ("Porque cobras por sessão e não por fotografia?", "Porque o que se paga é o trabalho completo: a preparação, a direção durante a sessão e a edição. Entrego as melhores fotografias, não a maior quantidade."),
   ("Que roupa convém levar para um retrato profissional?", "Cores lisas e neutras, sem padrões pequenos nem logótipos. Convém levar uma opção formal e outra mais descontraída. Falamos sobre isso antes da sessão."),
   ("Quanto tempo demora a entrega?", "Cinco dias úteis para retratos e dez para eventos."),
   ("Porquê preços de lançamento?", "Porque são os preços dos primeiros trabalhos em San Miguel. São atualizados periodicamente."),
  ],
  contact_h="Contactos", contact_p="Escreve-me com o tipo de sessão, a data que tens em mente e a zona.", ig="Ou por mensagem direta no Instagram:",
  areaname="San Miguel, Buenos Aires"),
}

for lang in ("es", "en", "pt"):
    t = T[lang]
    cards = ""
    for name, price, unit, items, note, soon in t["svcs"]:
        lis = "".join(f"<li>{html.escape(i)}</li>" for i in items)
        cards += f'<article class="svc{" soon" if soon else ""}"><h2>{name}</h2><div class="price">{price}<small>{unit}</small></div><ul>{lis}</ul><p class="note">{note}</p></article>'
    steps = "".join(f'<div class="step"><span class="n">{i+1}</span><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(t["steps"]))
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    content = f"""<div class="wrap">
  <header class="svc-head"><p class="eyebrow">{t['eyebrow']}</p><h1>{t['h1']}</h1><p>{t['intro']}</p><span class="launch">{t['launch']}</span></header>
  <div class="svcs">{cards}</div>
  <section class="block"><h2>{t['how']}</h2><div class="steps">{steps}</div></section>
  <section class="block faq"><h2>{t['faq_h']}</h2>{faq}</section>
  <section class="block"><h2>{t['contact_h']}</h2>
    <div class="contact-box"><p>{t['contact_p']}</p><span class="mail">{MAIL}</span>
    <p>{t['ig']} <a href="https://www.instagram.com/matiassilva.ph/" target="_blank" rel="noopener">@matiassilva.ph</a></p></div>
  </section>
</div>"""
    offers = [{"@type": "Offer", "name": n, "priceCurrency": "ARS", "price": p.replace("ARS ", "").replace("$", "").replace(".", "").replace(",", "")} for n, p, *_ in t["svcs"] if any(c.isdigit() for c in p)]
    ld = {"@context": "https://schema.org", "@type": "ProfessionalService", "name": "Matías Silva Fotografía",
          "url": SITE + t["url"], "email": MAIL, "image": SITE + "/img/familia.jpg",
          "address": {"@type": "PostalAddress", "addressLocality": "San Miguel", "addressRegion": "Buenos Aires", "addressCountry": "AR"},
          "areaServed": [{"@type": "Place", "name": a + ", Buenos Aires"} for a in AREA],
          "founder": {"@type": "Person", "name": "Matías Silva"},
          "hasOfferCatalog": {"@type": "OfferCatalog", "name": t["eyebrow"], "itemListElement": offers}}
    pg = blog.page(lang, t["title"], t["desc"], t["url"], "/servicios/", "/en/servicios/", ld, content, alt_pt="/pt/servicios/")
    pg = pg.replace("<title>", '<meta name="robots" content="noindex">\n<title>', 1).replace("</style>", CSS + "</style>", 1)
    path = "/home/claude/web/site" + t["url"] + "index.html"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(pg)
print("servicios ok")
