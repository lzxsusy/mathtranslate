# -*- coding: utf-8 -*-
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
p = r"<本地路径>"
t = open(p, encoding="utf-8").read()
if "% [原文 p.13]" in t:
    print("already has p.13"); sys.exit()
# 在 lemma* 1.4.7 之后的 \begin{proof} 前插入 p.13 标记
i = t.find("\\begin{lemma*}{1.4.7}")
j = t.find("\\begin{proof}", i)
assert i > 0 and j > i, (i, j)
t = t[:j] + "% [原文 p.13]\n" + t[j:]
open(p, "w", encoding="utf-8", newline="\n").write(t)
print("inserted p.13 marker at", j)
