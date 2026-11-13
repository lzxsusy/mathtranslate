# -*- coding: utf-8 -*-
import io

# 1) main.tex：在 notes-index 后插入 errata；顺带补注释
p = r"<本地路径>"
s = io.open(p, encoding="utf-8").read()
if "errata.tex" not in s:
    s = s.replace(r"\input{back/notes-index.tex}",
                  "\\input{back/notes-index.tex}\n\\input{back/errata.tex}")
    s = s.replace("%      back/notes-index.tex 附录 D 译注索引",
                  "%      back/notes-index.tex 附录 D 译注索引\n%      back/errata.tex     附录 E 原文勘误与存疑")
    io.open(p, "w", encoding="utf-8").write(s)
    print("main.tex patched")

# 2) pagemap.tex：加 label
p = r"<本地路径>"
s = io.open(p, encoding="utf-8").read()
if "label{sec:pagemap}" not in s:
    s = s.replace(r"\section{", "\\label{sec:pagemap}\n\\section{", 1)
    io.open(p, "w", encoding="utf-8").write(s)
    print("pagemap patched")

# 3) gen_full.py：errata 加入
p = r"<本地路径>"
s = io.open(p, encoding="utf-8").read()
if "errata" not in s:
    s = s.replace('("terms", "pagemap", "notes-index")',
                  '("terms", "pagemap", "notes-index", "errata")')
    io.open(p, "w", encoding="utf-8").write(s)
    print("gen_full patched")
