# -*- coding: utf-8 -*-
import io
import os
import re

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = os.path.join(root, "work", "原文", "main.tex")
out = os.path.join(os.path.dirname(root), "源码", "chunks", "ch08.tex")
s = io.open(src, encoding="utf-8", errors="replace").read()
keys_src = [m.group(1) for m in re.finditer(r"\\bib\{([^}]*)\}\{([a-zA-Z]+)\}\{", s)]
keys_out = re.findall(r"\\bibitem\{([^}]*)\}", io.open(out, encoding="utf-8").read())
print("src", len(keys_src), "out", len(keys_out))
print("missing:", [k for k in keys_src if k not in keys_out])
print("extra:", [k for k in keys_out if k not in keys_src])
