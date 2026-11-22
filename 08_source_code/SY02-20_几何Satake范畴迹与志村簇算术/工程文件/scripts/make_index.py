# -*- coding: utf-8 -*-
r"""生成条款索引数据：编号、类别（定理类/公式）、页、label 键。

类别由 label 前面最近的 \begin{环境} 判断；页码取自 main.aux。
用法：python make_index.py > ../work/条款索引数据.tsv
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PROJ = os.path.dirname(ROOT)
AUX = os.path.join(PROJ, "源码", "main.aux")
CHUNKS = os.path.join(PROJ, "源码", "chunks")

NAME = {
    "thm": "定理", "theorem": "定理",
    "prop": "命题", "proposition": "命题",
    "lem": "引理", "lemma": "引理", "sublem": "子引理", "sublemma": "子引理",
    "lem-def": "引理-定义",
    "cor": "推论", "corollary": "推论",
    "conj": "猜想", "conjecture": "猜想",
    "example": "例", "ex": "例", "exs": "例",
    "remark": "注", "rmk": "注",
    "dfn": "定义", "definition": "定义",
    "construction": "构造", "notation": "记号", "convention": "约定",
    "hypothesis": "假设",
}
EQ = ("equation", "align", "gather", "multline", "eqnarray")

# 页码表
aux = open(AUX, encoding="utf-8", errors="replace").read()
page_of = {}
for m in re.finditer(r"\\newlabel\{([^}]*)\}\{\{([^}]*)\}\{([^}]*)\}", aux):
    key, num, page = m.group(1), m.group(2), m.group(3)
    if page.isdigit():
        page_of[key] = (num, int(page))

rows = []
for f in sorted(glob.glob(os.path.join(CHUNKS, "ch*.tex"))):
    text = open(f, encoding="utf-8").read()
    stack = []
    i = 0
    while i < len(text):
        b = re.compile(r"\\begin\{([A-Za-z\-]+)\}").search(text, i)
        e = re.compile(r"\\end\{([A-Za-z\-]+)\}").search(text, i)
        l = re.compile(r"\\label\{([^}]*)\}").search(text, i)
        nxt = min([m.start() for m in (b, e, l) if m] or [len(text)])
        if nxt == len(text):
            break
        if b and b.start() == nxt:
            stack.append(b.group(1))
            i = b.end()
            continue
        if e and e.start() == nxt:
            if stack:
                stack.pop()
            i = e.end()
            continue
        key = l.group(1)
        env = None
        for cand in reversed(stack):
            if cand in EQ or cand in NAME:
                env = cand
                break
        if env in EQ:
            kind = "公式"
        elif env in NAME:
            kind = NAME[env]
        else:
            kind = "?"
        if key in page_of:
            num, page = page_of[key]
            rows.append((page, num, kind, key))
        i = l.end()

rows.sort(key=lambda r: (r[0], r[1], r[3]))
for page, num, kind, key in rows:
    print("%s\t%s\t%d\t%s" % (num, kind, page, key))
