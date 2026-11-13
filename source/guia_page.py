import sys, os, shutil
sys.path.insert(0, "/home/claude/web")
import blog
SITE = blog.SITE
CSS = """
.g-wrap{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:48px;align-items:start;padding-block:40px}
.g-cover img{width:100%;max-width:420px;box-shadow:0 20px 60px rgba(0,0,0,.5);display:block}
.g-text h1{font-family:var(--display);font-weight:400;font-size:clamp(2.4rem,6vw,4rem);line-height:1;margin:8px 0 16px}
.g-text .lead{font-size:1.1rem;color:var(--fg);max-width:52ch}
.g-text ul{color:#c9c5be;padding-left:20px;margin:18px 0 26px}
.g-text li{margin-bottom:6px}
.g-form{border:1px solid var(--accent);background:var(--surface);padding:24px;display:flex;flex-direction:column;gap:12px;max-width:460px}
.g-form label{font:12px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.g-form input[type=text],.g-form input[type=email]{width:100%;background:#0b0f12;border:1px solid var(--line);color:var(--fg);font:1rem var(--body);padding:12px;margin-top:6px;box-sizing:border-box}
.g-form .chk{display:flex;gap:10px;align-items:flex-start;font:.88rem var(--body);text-transform:none;letter-spacing:0;color:var(--muted)}
.g-form button{background:var(--accent);color:#0b0f12;border:0;font:500 1rem var(--body);padding:14px;cursor:pointer}
.g-form .hp{display:none}
.g-note{font-size:.85rem;color:var(--muted);margin-top:10px;max-width:460px}
.g-ok{max-width:640px;padding-block:60px}
.g-ok h1{font-family:var(--display);font-weight:400;font-size:clamp(2.2rem,5vw,3.4rem);margin:0 0 16px}
@media (max-width:820px){.g-wrap{grid-template-columns:1fr}.g-cover img{max-width:300px}}
"""

T={
 "es":dict(url="/guia/",form="guia",pdf="/descargas/Empezar-a-fotografiar_Matias-Silva.pdf",rec="/recursos/",rec_l="Recursos",crumb="Guía gratuita",
  name="Nombre",mail="Correo electrónico",chk="Quiero recibir novedades: artículos nuevos, el curso y el libro. Sin spam, y te podés dar de baja cuando quieras.",btn="Descargar la guía gratis",
  alt="Tapa de la guía Empezar a fotografiar, con Matías Silva y su cámara Sony",eyebrow="Guía gratuita · PDF",h1="Empezar a fotografiar",
  lead="Lo esencial para dejar el modo automático y empezar a decidir tus fotos. Sirve para cualquier cámara, también para el celular.",
  items=["La luz y la exposición, explicadas simple","Modos de la cámara, histograma y enfoque","Composición y cómo leer la luz","Cómo configurar tu cámara el primer día","Un plan de práctica de cuatro semanas"],
  note="Dejá tu nombre y tu correo, y la descarga se abre al instante. Tus datos solo los uso para enviarte novedades de este sitio.",
  title="Guía gratuita: Empezar a fotografiar · Matías Silva",desc="Guía gratuita en PDF para dejar el modo automático: exposición, modos, histograma, enfoque, composición y un plan de práctica de cuatro semanas.",
  ok_e="Listo",ok_h="Gracias. Tu guía está acá.",ok_b="Descargar el PDF",blog="/blog/",
  ok_p='Mientras tanto, en el <a href="{blog}" style="color:var(--accent)">blog</a> hay artículos completos sobre cada tema, y en Instagram comparto fotos y proceso: <a href="https://www.instagram.com/matiassilva.ph/" style="color:var(--accent)">@matiassilva.ph</a>.',ok_t="Gracias · Guía Empezar a fotografiar",hp="No completar"),
 "en":dict(url="/en/guia/",form="guia-en",pdf="/descargas/Start-taking-photographs_Matias-Silva.pdf",rec="/en/recursos/",rec_l="Resources",crumb="Free guide",
  name="Name",mail="Email",chk="I would like to receive updates: new articles, the course and the book. No spam, and you can unsubscribe at any time.",btn="Download the free guide",
  alt="Cover of the guide Start taking photographs, with Matías Silva and his Sony camera",eyebrow="Free guide · PDF",h1="Start taking photographs",
  lead="The essentials to leave auto mode and start making your own decisions. It works with any camera, including your phone.",
  items=["Light and exposure, explained simply","Camera modes, histogram and focus","Composition and reading the light","Setting up your camera on day one","A four-week practice plan"],
  note="Leave your name and email and the download opens straight away. I only use your details to send you updates from this site.",
  title="Free guide: Start taking photographs · Matías Silva",desc="Free PDF guide to leave auto mode: exposure, camera modes, histogram, focus, composition and a four-week practice plan.",
  ok_e="Done",ok_h="Thank you. Here is your guide.",ok_b="Download the PDF",blog="/en/blog/",
  ok_p='Meanwhile, the <a href="{blog}" style="color:var(--accent)">blog</a> has full articles on every topic, and on Instagram I share photographs and process: <a href="https://www.instagram.com/matiassilva.ph/" style="color:var(--accent)">@matiassilva.ph</a>.',ok_t="Thank you · Start taking photographs",hp="Leave empty"),
 "pt":dict(url="/pt/guia/",form="guia-pt",pdf="/descargas/Comecar-a-fotografar_Matias-Silva.pdf",rec="/pt/recursos/",rec_l="Recursos",crumb="Guia gratuito",
  name="Nome",mail="E-mail",chk="Quero receber novidades: artigos novos, o curso e o livro. Sem spam, e podes cancelar quando quiseres.",btn="Descarregar o guia gratuito",
  alt="Capa do guia Começar a fotografar, com Matías Silva e a sua câmara Sony",eyebrow="Guia gratuito · PDF",h1="Começar a fotografar",
  lead="O essencial para deixar o modo automático e começar a decidir as tuas fotografias. Serve para qualquer câmara, também para o telemóvel.",
  items=["A luz e a exposição, explicadas de forma simples","Modos da câmara, histograma e focagem","Composição e como ler a luz","Configurar a câmara no primeiro dia","Um plano de prática de quatro semanas"],
  note="Deixa o teu nome e o teu e-mail e a transferência abre de imediato. Só uso os teus dados para te enviar novidades deste site.",
  title="Guia gratuito: Começar a fotografar · Matías Silva",desc="Guia gratuito em PDF para deixar o modo automático: exposição, modos, histograma, focagem, composição e um plano de prática de quatro semanas.",
  ok_e="Pronto",ok_h="Obrigado. Aqui está o teu guia.",ok_b="Descarregar o PDF",blog="/pt/blog/",
  ok_p='Entretanto, no <a href="{blog}" style="color:var(--accent)">blog</a> há artigos completos sobre cada tema, e no Instagram partilho fotografias e processo: <a href="https://www.instagram.com/matiassilva.ph/" style="color:var(--accent)">@matiassilva.ph</a>.',ok_t="Obrigado · Começar a fotografar",hp="Não preencher"),
}
TAPAS={"es":"guia-tapa","en":"guia-tapa-en","pt":"guia-tapa-pt"}
for lang,t in T.items():
    items="".join(f"<li>{x}</li>" for x in t["items"])
    form=f"""<form class="g-form" name="{t['form']}" method="POST" action="{t['url']}gracias/" data-netlify="true" netlify-honeypot="empresa">
  <input type="hidden" name="form-name" value="{t['form']}">
  <p class="hp"><label>{t['hp']}: <input name="empresa"></label></p>
  <label>{t['name']}<input type="text" name="nombre" required autocomplete="given-name"></label>
  <label>{t['mail']}<input type="email" name="email" required autocomplete="email"></label>
  <label class="chk"><input type="checkbox" name="novedades" value="si"> {t['chk']}</label>
  <button type="submit">{t['btn']}</button>
</form>"""
    script=f"""<script>
document.querySelector('form[name="{t['form']}"]').addEventListener('submit',function(e){{
  e.preventDefault();var f=this,b=f.querySelector('button');b.disabled=true;
  var go=function(){{location.href='{t['url']}gracias/';}};
  fetch('/',{{method:'POST',headers:{{'Content-Type':'application/x-www-form-urlencoded'}},body:new URLSearchParams(new FormData(f)).toString()}}).then(go,go);
  setTimeout(go,4000);
}});
</script>"""
    content=f"""<div class="wrap"><p class="crumbs" style="margin-top:24px"><a href="{t['rec']}">{t['rec_l']}</a> / {t['crumb']}</p><div class="g-wrap" style="padding-top:12px">
  <div class="g-cover"><img src="/img/{TAPAS[lang]}.jpg" alt="{t['alt']}" width="900" height="1272"></div>
  <div class="g-text"><p class="eyebrow">{t['eyebrow']}</p><h1>{t['h1']}</h1><p class="lead">{t['lead']}</p><ul>{items}</ul>{form}<p class="g-note">{t['note']}</p></div>
</div></div>"""+script
    ld={"@context":"https://schema.org","@type":"CreativeWork","name":t["h1"],"inLanguage":("pt-PT" if lang=="pt" else lang),"isAccessibleForFree":True,
        "author":{"@type":"Person","@id":SITE+"/#matias-silva","name":"Matías Silva"},"url":SITE+t["url"],"image":SITE+f"/img/{TAPAS[lang]}.jpg"}
    pg=blog.page(lang,t["title"],t["desc"],t["url"],"/guia/","/en/guia/",ld,content,"familia",alt_pt="/pt/guia/").replace("</style>",CSS+"</style>",1)
    d="/home/claude/web/site"+t["url"]; os.makedirs(d+"gracias",exist_ok=True)
    open(d+"index.html","w").write(pg)
    ok=f"""<div class="wrap"><div class="g-ok"><p class="eyebrow">{t['ok_e']}</p><h1>{t['ok_h']}</h1>
  <p><a class="btn" href="{t['pdf']}" target="_blank" rel="noopener">{t['ok_b']}</a></p>
  <p style="color:var(--muted);margin-top:24px">{t['ok_p'].format(blog=t['blog'])}</p></div></div>"""
    pg2=blog.page(lang,t["ok_t"],t["ok_t"],t["url"]+"gracias/",t["url"]+"gracias/",t["url"]+"gracias/",{},ok)
    pg2=pg2.replace("<title>",'<meta name="robots" content="noindex">\n<title>',1).replace("</style>",CSS+"</style>",1)
    open(d+"gracias/index.html","w").write(pg2)
print("guia ok x3")
