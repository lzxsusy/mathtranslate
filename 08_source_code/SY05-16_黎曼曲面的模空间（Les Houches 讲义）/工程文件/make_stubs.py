# -*- coding: utf-8 -*-
"""make_stubs.py — 生成空的块文件，保证 main.tex 可编译（Lead 做冒烟用）"""
import os
ROOT = r"<本地路径>"
STUBS = ["sec1.tex", "sec21.tex", "sec22.tex", "sec23a.tex", "sec23b.tex",
         "sec31.tex", "sec32.tex", "sec33.tex", "sec4.tex", "refs.tex"]
for f in STUBS:
    p = os.path.join(ROOT, "src", f)
    if not os.path.exists(p):
        open(p, "w", encoding="utf-8", newline="\n").write("%% STUB " + f + "\n")
        print("stub", f)
