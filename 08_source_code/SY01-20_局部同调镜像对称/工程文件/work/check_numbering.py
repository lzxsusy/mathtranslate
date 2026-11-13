# -*- coding: utf-8 -*-
"""对比原 PDF 与译本的定理类编号序列（兼容「号 名」「名 号」两种排法）。"""
import io
import re

import pymupdf

ORIG = r"<本地路径>"
TRANS = r"<本地路径>"

EN_NAMES = "Theorem|Definition|Lemma|Proposition|Corollary|Question|Remark|Example|Notation|Conjecture|Convention|Exercise|Claim|Setup"
ZH_NAMES = "定理|定义|引理|命题|推论|问题|注记|注|例|记号|猜想|约定|练习|断言"
NUM = r"((?:\d+|[A])\.\d+)"

orig_text = io.open(ORIG, encoding="utf-8").read()
pdf = pymupdf.open(TRANS)
trans_text = "\n".join(p.get_text() for p in pdf)


def seq(text, names, lang):
    if lang == "en":
        pats = [re.compile(NUM + r"\s*\.?\s*(" + names + ")")]
    else:
        pats = [re.compile("(" + names + r")\s*" + NUM)]
    out = []
    for p in pats:
        for m in p.finditer(text):
            if lang == "en":
                out.append((m.group(1), m.group(2)))
            else:
                out.append((m.group(2), m.group(1)))
    return out


a = seq(orig_text, EN_NAMES, "en")
b = seq(trans_text, ZH_NAMES, "zh")
print("orig statements:", len(a))
print("trans statements:", len(b))
an = [x[0] for x in a]
bn = [x[0] for x in b]
print("only orig:", [x for x in an if x not in bn])
print("only trans:", [x for x in bn if x not in an])
