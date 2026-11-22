import sys, fitz
pdf = sys.argv[1]
pages = sys.argv[2]
out = sys.argv[3] if len(sys.argv) > 3 else "."
doc = fitz.open(pdf)
sel = []
for part in pages.split(","):
    if "-" in part:
        a, b = part.split("-")
        sel += list(range(int(a), int(b) + 1))
    else:
        sel.append(int(part))
for p in sel:
    pg = doc[p - 1]
    pix = pg.get_pixmap(dpi=140)
    fn = f"{out}/p{p:03d}.png"
    pix.save(fn)
    print(fn, pix.width, pix.height)
