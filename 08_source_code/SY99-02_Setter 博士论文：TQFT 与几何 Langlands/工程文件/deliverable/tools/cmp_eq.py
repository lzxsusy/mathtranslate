import sys, io, os, re
sys.stdout.reconfigure(encoding="utf-8")
import pymupdf

ROOT = r"<本地路径>"
ORIG = r"<本地路径>"

tag = sys.argv[1]
# 原文页
opage = None
for ln in io.open(os.path.join(ROOT, "tags.txt"), encoding="utf-8"):
    if ln.startswith("#"):
        continue
    parts = ln.split("\t")
    if parts[0] == tag:
        opage = int(parts[1])
print("tag", tag, "original PDF page", opage)

# 译本页
tdoc = pymupdf.open(os.path.join(ROOT, "src", "main.pdf"))
tpage = None
for i, p in enumerate(tdoc):
    if f"({tag})" in p.get_text():
        tpage = i + 1
        break
print("translated page:", tpage, "/", len(tdoc))

if opage:
    od = pymupdf.open(ORIG)
    od[opage - 1].get_pixmap(dpi=140).save(os.path.join(ROOT, "build", f"cmp_orig_{tag.replace('.','_')}.png"))
if tpage:
    tdoc[tpage - 1].get_pixmap(dpi=110).save(os.path.join(ROOT, "build", f"cmp_tr_{tag.replace('.','_')}.png"))
print("saved:", os.path.join(ROOT, "build", f"cmp_orig_{tag.replace('.','_')}.png"),
      os.path.join(ROOT, "build", f"cmp_tr_{tag.replace('.','_')}.png"))
