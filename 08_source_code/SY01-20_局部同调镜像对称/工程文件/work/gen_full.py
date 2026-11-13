# -*- coding: utf-8 -*-
"""生成 work/check/full_auto.tex：只 input 实际存在的 chunk，缺块时打印警告。"""
import io
import os

ROOT = r"<本地路径>"
chunks = os.path.join(ROOT, "src", "chunks")
out = [r"\input{../../src/preamble.tex}", r"\begin{document}"]
out.append(r"\input{../../src/front/s00-front.tex}")
out.append(r"\input{../../src/front/s01-guide.tex}")
missing = []
for i in range(15):
    name = "ch%02d" % i
    if os.path.isfile(os.path.join(chunks, name + ".tex")):
        out.append(r"\input{../../src/chunks/%s.tex}" % name)
    else:
        missing.append(name)
for b in ("terms", "pagemap", "notes-index", "errata"):
    out.append(r"\input{../../src/back/%s.tex}" % b)
out.append(r"\bibliographystyle{alphaurl}")
out.append(r"\bibliography{../../src/refs}")
out.append(r"\end{document}")
io.open(os.path.join(ROOT, "work", "check", "full_auto.tex"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("missing:", missing)
