# -*- coding: utf-8 -*-
"""从 txt/04 抽指定页中含关键词的完整句子，供逐字引用。"""
import os, re, sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "txt", "04")

def sent_of(page, keyword):
    path = os.path.join(BASE, "p%03d.txt" % page)
    try:
        raw = open(path, encoding="utf-8").read()
    except OSError:
        return "<no page>"
    flat = re.sub(r"\s+", " ", raw)
    # 按句号切，保留引号内内容
    sents = re.split(r"(?<=[.!?])\s+", flat)
    out = []
    for s in sents:
        if keyword.lower() in s.lower():
            out.append(s.strip())
        if len(out) >= 2:
            break
    return "\n    ".join(out) if out else "<none>"

QUERIES = [
    (29, "integral"), (29, "period"), (30, "commut"), (30, "constant"),
    (33, "coisotropic"), (33, "exists"), (34, "fixed point"),
    (36, "discrete series"), (38, "blow"), (40, "highest weight"),
    (41, "unitary"), (43, "extension"), (47, "moment map"),
    (48, "invariant"), (53, "fixed point"), (56, "complementary"),
    (57, "reducible"), (61, "lowest weight"), (66, "Chern-Simons"),
    (68, "twisted"), (69, "level"),
]
for page, kw in QUERIES:
    print("p%03d [%s]" % (page, kw))
    print("    " + sent_of(page, kw))
