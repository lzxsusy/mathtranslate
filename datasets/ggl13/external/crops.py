import pymupdf, os
pdf = r"C:\Users\admin\Downloads\ggl_文献库\pdf\13_IX_1108.3103.pdf"
out = r"C:\Users\admin\Downloads\ggl_文献库\out\13_ggl13\external"
doc = pymupdf.open(pdf)
jobs = [(4, "muli", "p004_muliplier"), (13, "connnection", "p013_connnection"),
        (15, "Bogomoly", "p015_bogomoly"), (17, "large than", "p017_large_than")]
for pno, needle, name in jobs:
    page = doc[pno - 1]
    rects = page.search_for(needle)
    if not rects:
        print("MISS", pno, needle)
        continue
    r = rects[0]
    clip = pymupdf.Rect(max(0, r.x0 - 220), max(0, r.y0 - 22), min(page.rect.x1, r.x1 + 220), min(page.rect.y1, r.y1 + 22))
    pix = page.get_pixmap(clip=clip, dpi=300)
    pix.save(os.path.join(out, name + ".png"))
    print("OK", name, pix.width, pix.height)
