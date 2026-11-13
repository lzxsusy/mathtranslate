# -*- coding: utf-8 -*-
"""重建被环境边界切割的 4 个 chunk: ch10, ch11, ch13, ch14"""
import io
import os

ROOT = r"<本地路径>"
SRC = r"<本地路径>"

chunks = [
    ("ch10", 3291, 3657, "6a 导出 dg-范畴 / 6b 等变 dg-范畴（前）"),
    ("ch11", 3658, 4215, "6b 等变 dg-范畴（含 dfn:GEquivQCohdg 起）"),
    ("ch13", 4656, 5023, "附录 A Eilenberg-Zilber 收缩（前）"),
    ("ch14", 5024, 5545, "附录 A Eilenberg-Zilber 收缩（后，含 align* 起）"),
]

src = io.open(SRC, encoding="utf-8").read().split("\n")
base = os.path.join(ROOT, "src", "chunks", "_src")
for name, a, b, title in chunks:
    lines = ["%% ===== %s : 原文 main.tex 第 %d--%d 行（%s）=====" % (name, a, b, title),
             "%% 本文件是原文 LaTeX 源码的逐行分片，仅供翻译时对照；最终译文写到 src/chunks/%s.tex。" % name]
    for ln in range(a, b + 1):
        if ln % 20 == 0:
            lines.append("%% ---- 原文行 %d ----" % ln)
        lines.append(src[ln - 1])
    io.open(os.path.join(base, name + "_src.tex"), "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
    print(name, a, b, len("\n".join(src[a-1:b])))
