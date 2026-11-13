import pymupdf, sys, io
sys.stdout.reconfigure(encoding="utf-8")
doc = pymupdf.open(r"<本地路径>")
print("pages:", doc.page_count)
for i, p in enumerate(doc):
    t = " ".join(p.get_text().split())
    print(f"p{i+1:02d} | {t[:90]}")
