import pymupdf, sys
sys.stdout.reconfigure(encoding="utf-8")
# usage: find_bbox.py page "text" [out.png dpi pad_pt]
page_no = int(sys.argv[1]); needle = sys.argv[2]
doc = pymupdf.open(r"<本地路径>")
page = doc[page_no - 1]
r = page.rect
rects = page.search_for(needle)
print("page size", r.width, r.height, "hits", len(rects))
for b in rects:
    print("bbox", [round(v, 1) for v in (b.x0, b.y0, b.x1, b.y1)],
          "frac", [round((b.x0-r.x0)/r.width, 3), round((b.y0-r.y0)/r.height, 3),
                   round((b.x1-r.x0)/r.width, 3), round((b.y1-r.y0)/r.height, 3)])
if len(sys.argv) > 3 and rects:
    out = sys.argv[3]; dpi = int(float(sys.argv[4])) if len(sys.argv) > 4 else 300
    pad = float(sys.argv[5]) if len(sys.argv) > 5 else 18
    b = rects[0]
    clip = pymupdf.Rect(0, max(b.y0 - pad, 0), r.width, min(b.y1 + pad, r.height))
    page.get_pixmap(clip=clip, dpi=dpi).save(out)
    print("saved", out)
