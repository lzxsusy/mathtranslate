from PIL import Image
import os
out = r"<HOME>\Downloads\GL_work\figures"
for name in ["fig1", "fig2", "fig3"]:
    p = os.path.join(out, name + ".png")
    im = Image.open(p).convert("RGB")
    w, h = im.size
    s = 1400 / max(w, h)
    if s < 1:
        im = im.resize((int(w*s), int(h*s)), Image.LANCZOS)
    q = os.path.join(out, name + ".jpg")
    im.save(q, "JPEG", quality=90)
    print(q, im.size, os.path.getsize(q)//1024, "KB")
