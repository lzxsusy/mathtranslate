import re, sys, json
import pymupdf

pdf = r"C:\Users\admin\Downloads\ggl_文献库\pdf\13_IX_1108.3103.pdf"
doc = pymupdf.open(pdf)
pats = [r"Bogomol", r"Lagrange mul", r"conn+ection", r"large than", r"0705", r"Khovanov", r"muliplier"]
out = []
out.append("pages=%d" % doc.page_count)
for i, page in enumerate(doc):
    t = page.get_text("text")
    flat = re.sub(r"\s+", " ", t)
    for p in pats:
        for m in re.finditer(p, flat, re.I):
            a = max(0, m.start() - 90)
            b = min(len(flat), m.end() + 90)
            out.append("p%03d [%s] ...%s..." % (i + 1, p, flat[a:b]))
open(r"C:\Users\admin\Downloads\ggl_文献库\out\13_ggl13\external\probe.txt", "w", encoding="utf-8").write("\n".join(out))
