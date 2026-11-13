# -*- coding: utf-8 -*-
import pymupdf, os, sys
ROOT = r"<本地路径>"
PDF = os.path.join(ROOT, "src.pdf")
doc = pymupdf.open(PDF)
out = []
for i in range(0, 20):
    p = doc[i]
    out.append("=" * 20 + f" PDF page {i+1}  size={p.rect.width:.0f}x{p.rect.height:.0f} imgs={len(p.get_images())} draw={len(p.get_drawings())}" + "=" * 20)
    out.append(p.get_text())
open(os.path.join(ROOT, "work", "probe", "front.txt"), "w", encoding="utf-8").write("\n".join(out))
print("pages", len(doc))
for i in range(0, 20):
    t = doc[i].get_text().strip().replace("\n", " | ")
    print(f"--- p{i+1}: {t[:300]}")
