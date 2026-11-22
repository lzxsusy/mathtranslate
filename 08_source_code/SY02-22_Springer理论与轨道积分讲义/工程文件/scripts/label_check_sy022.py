# -*- coding: utf-8 -*-
r"""SY02-22 编号对账：原文 \label 集合 vs 译文 \label 集合。"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                       # 工程文件
PROJ = os.path.dirname(ROOT)
SRC = os.path.join(ROOT, "work", "src", "ZhiweiYunPCMI.tex")
CH = os.path.join(PROJ, "源码", "chunks")

text = open(SRC, encoding="utf-8").read()
# 只取正文（\begin{document} ... \begin{bibdiv}）
i0 = text.find("\\begin{document}")
i1 = text.find("\\begin{bibdiv}")
otext = text[i0:i1]
olabels = re.findall(r"\\label\{([^}]*)\}", otext)

mtext = ""
for f in sorted(os.listdir(CH)):
    if f.endswith(".tex"):
        mtext += open(os.path.join(CH, f), encoding="utf-8").read() + "\n"
mlabels = re.findall(r"\\label\{([^}]*)\}", mtext)

o, m = set(olabels), set(mlabels)
print("原文 label 数:", len(o), "  译文 label 数:", len(m), "  (原文出现次数 %d, 译文 %d)"
      % (len(olabels), len(mlabels)))
print("missing (原文有、译文无):", sorted(o - m))
print("extra   (译文有、原文无):", sorted(m - o))
dups = sorted({x for x in m if mlabels.count(x) > 1})
print("译文重复 label:", dups)

# 引用 key 对账
ocite = set(re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]*)\}", otext))
mcite = set(re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]*)\}", mtext))
exp_oc = set()
for c in ocite:
    for k in c.split(","):
        exp_oc.add(k.strip())
exp_mc = set()
for c in mcite:
    for k in c.split(","):
        exp_mc.add(k.strip())
print("\n原文 cite key 数:", len(exp_oc), " 译文 cite key 数:", len(exp_mc))
print("cite missing:", sorted(exp_oc - exp_mc))
print("cite extra  :", sorted(exp_mc - exp_oc))

# bibitem keys
bib = open(os.path.join(CH, "ch18.tex"), encoding="utf-8").read()
bk = set(re.findall(r"\\bibitem\{([^}]*)\}", bib))
print("\nbibitem 数:", len(bk))
print("cite 无对应 bibitem:", sorted(exp_mc - bk))
print("bibitem 未被引用:", sorted(bk - exp_mc))
