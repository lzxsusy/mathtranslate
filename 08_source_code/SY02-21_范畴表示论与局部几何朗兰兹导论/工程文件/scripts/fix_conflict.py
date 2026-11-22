# -*- coding: utf-8 -*-
r"""把 preamble_macros.tex 里与 LaTeX 已有命令冲突的 \newcommand 改成 \renewcommand。

做法：先由 port_macros2.py 生成干净文件，再对「LaTeX 内核已有定义」的短名
改用 \renewcommand。名单含：文本重音命令、字体切换命令、希腊/数学惯用命令。
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.abspath(os.path.join(HERE, "..", "..", "源码", "preamble_macros.tex"))

CONFLICT = [
    # 文本重音
    "a", "b", "c", "d", "i", "j", "k", "l", "o", "r", "t", "u", "v", "H",
    # 字体切换（旧式）
    "sl", "sp", "sc", "it", "bf", "rm", "tt", "sf", "em",
    # 数学/排版惯用
    "AA", "aa", "AE", "ae", "OE", "oe", "O", "o", "L", "l", "SS", "ss",
    "dag", "ddag", "P", "S", "Im", "Re", "div", "sslash", "th", "S",
]

s = open(P, encoding="utf-8").read()
for n in CONFLICT:
    s = s.replace("\\newcommand{\\%s}" % n, "\\renewcommand{\\%s}" % n)
open(P, "w", encoding="utf-8").write(s)
print("renewcommand count:", len(re.findall(r"\\renewcommand", s)))
