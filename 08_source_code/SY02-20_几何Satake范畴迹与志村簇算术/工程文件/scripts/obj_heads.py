# -*- coding: utf-8 -*-
r"""列出每个定理类编号对象的首句，供写 01-结果清单.md 时核对。

用法：python obj_heads.py > ../work/对象首句.txt
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PROJ = os.path.dirname(ROOT)
CHUNKS = os.path.join(PROJ, "源码", "chunks")

NAME = ["thm", "theorem", "prop", "proposition", "lem", "lemma", "sublem", "sublemma",
        "lem-def", "cor", "corollary", "conj", "conjecture", "example", "ex", "exs",
        "remark", "rmk", "dfn", "definition", "construction", "notation", "convention",
        "hypothesis"]
text = ""
for p in sorted(glob.glob(os.path.join(CHUNKS, "ch*.tex"))):
    text += open(p, encoding="utf-8").read() + "\n"

pat = re.compile(r"\\begin\{(%s)\}" % "|".join(NAME))
idx = list(pat.finditer(text))
for i, m in enumerate(idx):
    end = idx[i + 1].start() if i + 1 < len(idx) else len(text)
    body = text[m.end():end]
    lab = re.search(r"\\label\{([^}]*)\}", body)
    body = re.sub(r"\\label\{[^}]*\}", "", body)
    body = re.sub(r"\$[^$]*\$", "〔式子〕", body)
    body = re.sub(r"\\[A-Za-z]+\*?(\[[^\]]*\])?", "", body)
    body = re.sub(r"[{}]", "", body)
    body = re.sub(r"\s+", " ", body).strip()
    print("%-6s %-22s %s" % (m.group(1), lab.group(1) if lab else "-", body[:110]))
