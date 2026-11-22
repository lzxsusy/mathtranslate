# -*- coding: utf-8 -*-
r"""给条款索引补原文页（PDF 页序）。

- 定理类：在原文 PDF 里搜印刷头，如 "Example 2.1.1."。
- 编号公式：在相邻两个定理类对象的页之间搜 "(2.1.1)"，取该窗口内首次出现。
  （窗口很窄，故不会误取到远处的交叉引用。）

用法：python orig_pages.py > ../work/原文页.tsv
"""
import os
import re
import warnings

warnings.filterwarnings("ignore")
import pymupdf  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WORK = os.path.join(ROOT, "work")
PDF = os.path.join(WORK, "pdf", "src.pdf")
ORIG = os.path.join(WORK, "原文", "main.tex")

ENV2EN = {
    "thm": "Theorem", "theorem": "Theorem",
    "prop": "Proposition", "proposition": "Proposition",
    "lem": "Lemma", "lemma": "Lemma", "sublem": "Lemma", "sublemma": "Lemma",
    "lem-def": "Lemma", "cor": "Corollary", "corollary": "Corollary",
    "conj": "Conjecture", "conjecture": "Conjecture",
    "example": "Example", "ex": "Example", "exs": "Example",
    "remark": "Remark", "rmk": "Remark", "dfn": "Definition",
    "definition": "Definition", "construction": "Construction",
    "notation": "Notation", "convention": "Convention",
    "hypothesis": "Hypothesis",
}
THM_ENVS = "|".join(sorted(ENV2EN, key=len, reverse=True))

doc = pymupdf.open(PDF)
pages = [re.sub(r"\s+", " ", doc[i].get_text()) for i in range(len(doc))]

text = open(ORIG, encoding="utf-8").read()
out = []
i = 0
while True:
    j = text.find("\\quash{", i)
    if j < 0:
        out.append(text[i:])
        break
    out.append(text[i:j])
    k = j + 7
    depth = 1
    while k < len(text) and depth:
        if text[k] == "{":
            depth += 1
        elif text[k] == "}":
            depth -= 1
        k += 1
    i = k
text = "".join(out)

objs = []
sec = sub = sss = eqs = 0
for raw in text.split("\n"):
    line = "" if raw.lstrip().startswith("%") else re.sub(r"(?<!\\)%.*", "", raw)
    if re.search(r"\\section\s*\{", line):
        sec += 1
        sub = sss = eqs = 0
    if re.search(r"\\subsection\s*\{", line):
        sub += 1
        sss = eqs = 0
    for m in re.finditer(r"\\begin\{(%s)\}" % THM_ENVS, line):
        sss += 1
        objs.append(["%d.%d.%d" % (sec, sub, sss), "thm", ENV2EN[m.group(1)], None])
    for m in re.finditer(r"\\begin\{(equation|align|gather|multline|eqnarray)\}(?!\*)", line):
        eqs += 1
        objs.append(["%d.%d.%d" % (sec, sub, eqs), "eq", None, None])

# 定理类：按印刷头定位
for idx, o in enumerate(objs):
    if o[1] != "thm":
        continue
    pat = re.compile(re.escape(o[2]) + r"\s*" + re.escape(o[0]) + r"\.")
    for p, ptxt in enumerate(pages, 1):
        if pat.search(ptxt):
            o[3] = p
            break

# 公式：在相邻定理类对象的页之间找
thm_idx = [i for i, o in enumerate(objs) if o[1] == "thm" and o[3]]
for idx, o in enumerate(objs):
    if o[1] != "eq":
        continue
    lo = 1
    hi = len(pages)
    for i in thm_idx:
        if i < idx and objs[i][3]:
            lo = objs[i][3]
    for i in thm_idx:
        if i > idx and objs[i][3]:
            hi = objs[i][3]
            break
    pat = re.compile(re.escape("(" + o[0] + ")"))
    for p in range(lo, hi + 1):
        if pat.search(pages[p - 1]):
            o[3] = p
            break

for o in objs:
    print("%s\t%s\t%s" % (o[0], o[1], o[3] if o[3] else "-"))
