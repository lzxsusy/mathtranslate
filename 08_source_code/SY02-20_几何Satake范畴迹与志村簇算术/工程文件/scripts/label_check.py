# -*- coding: utf-8 -*-
r"""对账：原文 \label 集合 vs 译文 \label 集合；并打印译文分节结构。

正文与文献分开：原文取 \begin{thebibliography} 之前的部分，译文取 chunks/*.tex 中
thebibliography 之前的部分（ch25 只含文献）。
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                       # 工程文件
PROJ = os.path.dirname(ROOT)
SRC = os.path.join(ROOT, "work", "原文", "main.tex")
CH = os.path.join(PROJ, "源码", "chunks")

otext = open(SRC, encoding="utf-8").read()
otext = otext.split(r"\begin{thebibliography}")[0]
olabels = re.findall(r"\\label\{([^}]*)\}", otext)

mtext = ""
for f in sorted(os.listdir(CH)):
    if f.endswith(".tex"):
        piece = open(os.path.join(CH, f), encoding="utf-8").read()
        piece = piece.split(r"\begin{thebibliography}")[0]
        mtext += piece + "\n"
mlabels = re.findall(r"\\label\{([^}]*)\}", mtext)

o, m = set(olabels), set(mlabels)
print("原文 label:", len(o), " 译文 label:", len(m))
print("missing:", sorted(o - m))
print("extra  :", sorted(m - o))
dups = [x for x in m if mlabels.count(x) > 1]
print("重复  :", sorted(set(dups)))

print("\n译文分节：")
for line in mtext.split("\n"):
    if line.startswith("\\section{") or line.startswith("\\subsection{"):
        print("  " + line[:80])
