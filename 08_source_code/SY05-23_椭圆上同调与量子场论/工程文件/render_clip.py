import pymupdf, sys
# usage: render_clip.py page x0 y0 x1 y1 dpi out
p = int(sys.argv[1]); x0, y0, x1, y1 = map(float, sys.argv[2:6])
dpi = int(float(sys.argv[6])); out = sys.argv[7]
doc = pymupdf.open(r"<本地路径>")
page = doc[p - 1]
r = page.rect
clip = pymupdf.Rect(r.x0 + x0 * r.width, r.y0 + y0 * r.height,
                    r.x0 + x1 * r.width, r.y0 + y1 * r.height)
pix = page.get_pixmap(clip=clip, dpi=dpi)
pix.save(out)
print("saved", out, pix.width, "x", pix.height)
