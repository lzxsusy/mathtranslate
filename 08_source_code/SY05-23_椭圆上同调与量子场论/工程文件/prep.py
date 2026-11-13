# -*- coding: utf-8 -*-
"""prep.py — 为 SY05-23（Berwick-Evans 综述）备料
输出：底本 PDF 副本、200dpi 页图、逐页文字层、full.txt、equation inventory、probe.md
用法： python prep.py
"""
import os, re, shutil, hashlib
import pymupdf

SRC = r"<本地路径>"
PROJ = r"<本地路径>"
ENG = os.path.join(PROJ, "工程文件")
PAGES = os.path.join(ENG, "pages")
SPLIT = os.path.join(ENG, "split")
for d in (PAGES, SPLIT):
    os.makedirs(d, exist_ok=True)

doc = pymupdf.open(SRC)
n = doc.page_count
out = []
out.append("pages=%d" % n)
out.append("md5=%s" % hashlib.md5(open(SRC, "rb").read()).hexdigest())
out.append("size=%d" % os.path.getsize(SRC))
out.append("metadata=%r" % (doc.metadata,))
out.append("toc=%r" % (doc.get_toc(),))

full = []
eqs = []
for i in range(n):
    page = doc[i]
    pix = page.get_pixmap(dpi=200)
    pix.save(os.path.join(PAGES, "p%02d.png" % (i + 1)))
    txt = page.get_text()
    with open(os.path.join(SPLIT, "p%02d.txt" % (i + 1)), "w", encoding="utf-8", newline="\n") as f:
        f.write(txt)
    full.append("\n\n<<<<< PAGE %d >>>>>\n" % (i + 1))
    full.append(txt)
    for ln in txt.splitlines():
        s = ln.strip()
        m = re.fullmatch(r"\((\d+\.\d+|\d+)\)", s)
        if m:
            eqs.append((i + 1, m.group(1)))
with open(os.path.join(ENG, "full.txt"), "w", encoding="utf-8", newline="\n") as f:
    f.write("".join(full))

with open(os.path.join(ENG, "eqs_raw.txt"), "w", encoding="utf-8", newline="\n") as f:
    for pg, tag in eqs:
        f.write("p%d\t(%s)\n" % (pg, tag))

# 每页首行/末行概览，便于分块
out.append("\n--- page first/last lines ---")
for i in range(n):
    t = doc[i].get_text().splitlines()
    t = [x.strip() for x in t if x.strip()]
    out.append("p%02d | %s ... %s" % (i + 1, (t[0][:70] if t else ""), (t[-1][:70] if t else "")))

out.append("\n--- equations found: %d ---" % len(eqs))
out.append(", ".join("(%s)@p%d" % (tag, pg) for pg, tag in eqs))

with open(os.path.join(ENG, "probe_raw.txt"), "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(out))

# 底本副本
shutil.copyfile(SRC, os.path.join(ENG, "底本_arXiv-2408.07693.pdf"))
print("ok pages=%d eqs=%d" % (n, len(eqs)))
