# -*- coding: utf-8 -*-
"""扫 bold 小标题 与 编号定理（多段编号）。"""
import re, io
import pymupdf

PDF = r"<本地路径>).pdf"
ROOT = r"<本地路径>"
doc = pymupdf.open(PDF)
out = io.StringIO()

# --- 粗体小标题（CMBX12 且字号 12） ---
out.write("===== BOLD SPANS (size 10.5-13, CMBX) =====\n")
for i, page in enumerate(doc):
    for b in page.get_text("dict")["blocks"]:
        if b.get("type") != 0:
            continue
        for ln in b["lines"]:
            for s in ln["spans"]:
                if "CMBX" in s["font"] and s["text"].strip():
                    out.write("p%03d [%.1f] %s\n" % (i + 1, s["size"], s["text"].strip()[:90]))

# --- 编号定义/定理 ---
out.write("\n===== NUMBERED ITEMS =====\n")
pat = re.compile(r"\b(Definition|Proposition|Theorem|Lemma|Corollary|Example|Remark|Note|Exercise|Claim|Conjecture|Scholium)\s+(\d+(?:\.\d+){0,3})")
cnt = {}
for i, page in enumerate(doc):
    t = page.get_text("text").replace("\n", " ")
    for m in pat.finditer(t):
        key = m.group(1)
        cnt[key] = cnt.get(key, 0) + 1
        out.write("p%03d  %s\n" % (i + 1, m.group(0)))
out.write("\nCOUNTS: %r\n" % cnt)

# --- 花括号/方括号/公式标记线索：统计 $ 类字符 ---
open(ROOT + r"\probe\bold_and_items.txt", "w", encoding="utf-8").write(out.getvalue())
print(out.getvalue()[:4000])
