import sys, io, os, re
sys.stdout.reconfigure(encoding="utf-8")
import pymupdf

ROOT = r"<本地路径>"
pdf = os.path.join(ROOT, "src", "main.pdf")
d = pymupdf.open(pdf)
print("translated pages:", len(d))

# 1) 译本目录页文本（frontmatter 中 "目录" 起始页）
toc_pages = []
started = False
for i, p in enumerate(d):
    t = p.get_text()
    if "目录" in t and not started:
        started = True
    if started:
        toc_pages.append(t)
        if len(toc_pages) >= 5:
            break
toc_txt = "\n".join(toc_pages)

# 提取形如 3.2 / 6.4.3.4 / B.2.1 / A.1 的编号
tr_nums = re.findall(r"(?m)^\s*([A-D]\.\d(?:\.\d)*|\d+\.\d+(?:\.\d+)*)\s", toc_txt)
tr_nums = [n for n in tr_nums if not n.startswith("第")]
# 去重保序
seen = set(); tr = []
for n in tr_nums:
    if n not in seen:
        seen.add(n); tr.append(n)

# 2) 原文目录编号（logs/toc.txt）
orig_txt = io.open(os.path.join(ROOT, "logs", "toc.txt"), encoding="utf-16").read()
onums = re.findall(r"(?m)^([A-D]\.\d(?:\.\d)*|\d+\.\d+(?:\.\d+)*)\s*$", orig_txt)
seen = set(); og = []
for n in onums:
    if n not in seen:
        seen.add(n); og.append(n)

print("orig sections:", len(og), "translated sections:", len(tr))
missing = [n for n in og if n not in set(tr)]
extra = [n for n in tr if n not in set(og)]
print("MISSING in translation TOC:", missing)
print("EXTRA in translation TOC:", extra)

# 3) 原文 tag 是否都在 PDF 文本中
full = "\n".join(p.get_text() for p in d)
tags = [l.split("\t")[0] for l in io.open(os.path.join(ROOT, "tags.txt"), encoding="utf-8") if l.strip() and not l.startswith("#")]
miss_tag = [t for t in tags if f"({t})" not in full]
print("tags missing in PDF text:", miss_tag)
