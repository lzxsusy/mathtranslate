# -*- coding: utf-8 -*-
"""生成 GMN2 资料卡所需的机械索引：式号->译本页、图清单、节页表。"""
import re, io, glob, os, collections

ROOT = r"C:\Users\admin\Desktop\GMN系列\01_翻译\GMN2_0907.3987"
SRC = ROOT + r"\源码"
WORK = ROOT + r"\工程文件\work"

aux = io.open(SRC + r"\main.aux", encoding="utf-8", errors="replace").read()
labels = re.findall(r"\\newlabel\{([^}]*)\}\{\{([^}]*)\}\{([^}]*)\}", aux)

def key(num):
    m = re.match(r"([A-E]|\d+)\.(\d+)([a-z]?)$", num)
    if not m:
        return (999, 0, 0, num)
    sec = m.group(1)
    s = 100 if sec in "ABCDE" else int(sec)
    return (s, int(m.group(2)), ord(m.group(3) or "a"), num)

eqs = [(num, int(pg), lab) for lab, num, pg in labels if lab.startswith("eq:")]
eqs.sort(key=lambda t: key(t[0]))
with io.open(WORK + r"\eq_index.tsv", "w", encoding="utf-8") as f:
    for num, pg, lab in eqs:
        f.write("%s\t%d\t%s\n" % (num, pg, lab))
print("eq_index.tsv:", len(eqs))

# fmt -> number->page dict
with io.open(WORK + r"\eq_page.tsv", "w", encoding="utf-8") as f:
    for num, pg, lab in eqs:
        f.write("%s\t%d\n" % (num, pg))

# labels of interest
kw = ["pois", "bracket", "cross", "darboux", "jump", "omnipop", "ks", "wkb",
      "sympl", "flat", "spec", "def", "curve", "hitchin", "sf", "rh", "S-",
      "transform", "flip", "pop", "juggle", "quant", "sign", "turning", "asym"]
print("=== labels by keyword ===")
for num, pg, lab in eqs:
    if any(k.lower() in lab.lower() for k in kw):
        print("%s\t%d\t%s" % (num, pg, lab))
