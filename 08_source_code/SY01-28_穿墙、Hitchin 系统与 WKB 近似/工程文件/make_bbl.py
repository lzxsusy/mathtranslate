# -*- coding: utf-8 -*-
"""把 wkb-paper.bbl 机械转换成 refs_bbl.tex（去掉 bbl 包装，\\N -> \\CN）。"""
import io, os, re

src = r"C:\Users\admin\Desktop\GMN系列\00_原文\GMN2_0907.3987\0907.3987v2_src\wkb-paper.bbl"
dst = r"C:\Users\admin\Desktop\GMN系列\01_翻译\GMN2_0907.3987\源码\refs_bbl.tex"

with io.open(src, encoding="utf-8") as f:
    txt = f.read()

txt = txt.replace("\\providecommand{\\href}[2]{#2}\\begingroup\\raggedright", "", 1)
txt = txt.rstrip()
if txt.endswith("\\endgroup"):
    txt = txt[: -len("\\endgroup")].rstrip()

txt = re.sub(r"\\N(?![a-zA-Z])", r"\\CN", txt)

header = "% 由 0907.3987v2 的 wkb-paper.bbl 机械转换（去掉 bbl 包装，反斜杠N -> 反斜杠CN）\n"
with io.open(dst, "w", encoding="utf-8", newline="\n") as f:
    f.write(header + txt + "\n")

print("written", dst, len(txt.splitlines()), "lines")
print("bibitems", txt.count("\\bibitem"))
