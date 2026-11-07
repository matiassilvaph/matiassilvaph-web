from PIL import Image, ImageOps
import json
A="/mnt/user-data/attachments/0c9f43ce-5c7b-5878-9acb-2e5c3e3d85c8/"
P={"gaviota-cartel":"8ecc9ddc","arcos-santuario":"82d5046b","ventana-blanca":"74a2adf2","candado":"6bc6993e",
 "calle-blanca":"33fba413","farol":"da909a61","azulejo":"dec56ee7","escalera-forte":"d04d6829",
 "gaviota-cupula":"712c89b9","ciervo":"6731d02b","ascensor-noche":"75885602","playa-gris":"77aa5b5c",
 "portico-big-wave":"af4e2ec1","praia-norte-arriba":"564a0b15","arcoiris-forte":"09972647","tablas-forte":"37eedb4b",
 "matias-orilla":"839ccf83"}
meta=json.load(open("meta.json"))
for s,f in P.items():
    im=ImageOps.exif_transpose(Image.open(A+f+"-image.jpg")).convert("RGB")
    full=im.copy(); full.thumbnail((1440,1440)); th=im.copy(); th.thumbnail((760,760))
    for d in ("site/img/","/home/claude/matiassilvaph-web/img/"):
        full.save(d+s+".jpg",quality=82,optimize=True,progressive=True); th.save(d+s+"-s.jpg",quality=76,optimize=True,progressive=True)
    meta[s]=list(full.size); print(s,full.size)
json.dump(meta,open("meta.json","w"))
