# -*- coding: utf-8 -*-
"""生成分块预期清单：块 -> PDF 页段 -> 该范围内 OCR 到的陈述编号/公式编号（参考值）"""
import pymupdf, re, sys, collections, os, json
sys.stdout.reconfigure(encoding='utf-8')
SRC = r"<本地路径>"
ROOT = r"<本地路径>"

CHUNKS = [
    ("ch01a", 10, 17), ("ch01b", 18, 27), ("ch01c", 28, 37),
    ("ch02a", 38, 47), ("ch02b", 48, 57), ("ch02c", 58, 67),
    ("ch02d", 68, 77), ("ch02e", 78, 90),
    ("ch03a", 92, 101), ("ch03b", 102, 111), ("ch03c", 112, 118),
    ("appA", 120, 129),
    ("appB1", 130, 141), ("appB2", 142, 153), ("appB3", 154, 163), ("appB4", 164, 171),
    ("appC1", 172, 183), ("appC2", 184, 193), ("appC3", 194, 199),
    ("kaisetsu", 200, 211),
]

doc = pymupdf.open(SRC)
statre = re.compile(r'(定義|定理|命題|補題|系|例|注意|問題|仮定|記号|公式)\s*([0-9A-C])\s*[.．]\s*(\d+)(?:\s*[.．]\s*(\d+))?')
tagre = re.compile(r'[（(]\s*([0-9A-C])\s*[.．]\s*(\d{1,2})\s*(?:[.．]\s*(\d{1,2}))?\s*[）)]\s*$')

pages = {}
for i in range(doc.page_count):
    pages[i + 1] = doc[i].get_text("text")

out = []
for name, a, b in CHUNKS:
    st, tg, sec = [], [], []
    for p in range(a, b + 1):
        for line in pages[p].split("\n"):
            s = line.strip()
            for m in statre.finditer(s):
                num = f"{m.group(2)}.{m.group(3)}" + (f".{m.group(4)}" if m.group(4) else "")
                st.append((num, p, m.group(1)))
            m = tagre.search(s)
            if m:
                tg.append(f"{m.group(1)}.{m.group(2)}" + (f".{m.group(3)}" if m.group(3) else "") + f"@p{p}")
            if re.search(r'^\d+(\.\d+)*\s+\S', s) and len(s) < 40:
                sec.append((s, p))
    uniq = []
    seen = set()
    for num, p, k in st:
        if (num, k) not in seen:
            seen.add((num, k))
            uniq.append(f"{k}{num}(p{p})")
    out.append({"chunk": name, "pdf": [a, b], "book": [a - 9, b - 9],
                "statements": uniq, "tags": sorted(set(tg)),
                "headings": sec[:6]})

with open(os.path.join(ROOT, "work", "expect.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

lines = ["# 分块预期清单（OCR 统计，**参考值，非真值**）", "",
         "公式/陈述编号一律以原书页图为准；本表只用来提醒「这段里大概有哪些编号」。", ""]
for o in out:
    lines.append(f"## {o['chunk']}  PDF {o['pdf'][0]}–{o['pdf'][1]} = 原书 p.{o['book'][0]}–p.{o['book'][1]}")
    lines.append("")
    lines.append("- 陈述（OCR）：" + ("、".join(o["statements"]) if o["statements"] else "无"))
    lines.append("- 公式编号（OCR，漏检严重）：" + ("、".join(o["tags"]) if o["tags"] else "无"))
    lines.append("")
with open(os.path.join(ROOT, "work", "expect.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
for o in out:
    print(o["chunk"], o["pdf"], "sts=", len(o["statements"]), "tags=", len(o["tags"]))
