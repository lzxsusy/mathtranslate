# -*- coding: utf-8 -*-
r"""生成原文结构图：节/小节/定理类对象清单（含首句摘要）与计数。

用法： python outline.py
输出： 工程文件/work/原文/outline.txt
      屏幕打印 节-小节-定理类对象 计数
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "work", "原文", "main.tex")
OUT = os.path.join(ROOT, "work", "原文", "outline.txt")

THM = ("thm|prop|lem|sublem|lem-def|cor|theorem|proposition|lemma|sublemma|conjecture|"
       "corollary|example|remark|hypothesis|definition|question|ex|exs|notation|"
       "construction|caution|convention|rmk|dfn")

text = open(SRC, encoding="utf-8").read()
lines = text.split("\n")

recs = []
thmcount = {}
eqcount = 0
for i, line in enumerate(lines, 1):
    m = re.match(r"\s*\\(section|subsection)\*?\{(.*)", line)
    if m:
        recs.append((i, m.group(1), m.group(2)[:110]))
    m = re.match(r"\s*\\begin\{(%s)\}" % THM, line)
    if m:
        kind = m.group(1)
        thmcount[kind] = thmcount.get(kind, 0) + 1
        # 收集该环境首 200 字
        body = []
        j = i
        while j < min(i + 8, len(lines)):
            body.append(lines[j - 1])
            if "\\end{%s}" % kind in lines[j - 1]:
                break
            j += 1
        head = " ".join(body)
        head = re.sub(r"\s+", " ", head)[:170]
        recs.append((i, kind, head))
    if re.search(r"\\begin\{(equation|align|multline|gather)\}", line):
        eqcount += 1
    if "\\begin{thebibliography}" in line:
        recs.append((i, "BIB", ""))

with open(OUT, "w", encoding="utf-8") as fh:
    for i, k, h in recs:
        fh.write("%5d  %-12s %s\n" % (i, k, h))

print("定理类对象：", sum(thmcount.values()), thmcount)
print("编号公式（\\begin 计数）：", eqcount)
print("thebibliography 起始行：", [i for i, k, _ in recs if k == "BIB"])
print("写出", OUT)
