import pymupdf, sys
sys.stdout.reconfigure(encoding="utf-8")
doc = pymupdf.open(r"<本地路径>")
for kw in sys.argv[1:]:
    hits = []
    for i, p in enumerate(doc):
        t = " ".join(p.get_text().split())
        if kw in t:
            hits.append(i + 1)
    print(kw, "->", hits)
