# -*- coding: utf-8 -*-
"""提取标题层级（按字号），生成 headings.txt。"""
import io, sys
import pymupdf

PDF = r"<本地路径>).pdf"
ROOT = r"<本地路径>"
doc = pymupdf.open(PDF)
out = io.StringIO()

for i, page in enumerate(doc):
    rows = []
    for b in page.get_text("dict")["blocks"]:
        if b.get("type") != 0:
            continue
        for ln in b["lines"]:
            spans = [s for s in ln["spans"] if s["text"].strip()]
            if not spans:
                continue
            mx = max(s["size"] for s in spans)
            if mx >= 13.0:
                txt = "".join(s["text"] for s in spans).strip()
                bold = any("Bold" in s["font"] or "BX" in s["font"] or "CMBX" in s["font"] for s in spans)
                rows.append((round(mx, 1), bold, txt))
    if rows:
        out.write("---- page %d ----\n" % (i + 1))
        for r in rows:
            out.write("%6.1f %s  %s\n" % (r[0], "B" if r[1] else " ", r[2]))

# 同时导出每页首行（用于判断页首是否续句）
out.write("\n\n===== PAGE FIRST/LAST LINES =====\n")
for i, page in enumerate(doc):
    lines = [l.strip() for l in page.get_text("text").splitlines() if l.strip()]
    if not lines:
        continue
    out.write("p%03d FIRST: %s\n" % (i + 1, lines[0][:110]))
    out.write("p%03d LAST : %s\n" % (i + 1, lines[-1][:110]))

open(ROOT + r"\probe\headings.txt", "w", encoding="utf-8").write(out.getvalue())
print("ok")
