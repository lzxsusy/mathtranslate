# -*- coding: utf-8 -*-
r"""把编号（来自条款索引合并.tsv）与对象首句拼在一起，供写结果清单。"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WORK = os.path.join(ROOT, "work")

idx = [l.rstrip("\n").split("\t") for l in open(os.path.join(WORK, "条款索引合并.tsv"),
                                                encoding="utf-8") if l.strip()]
idx = [r for r in idx if r[1] != "公式"]
heads = [l.rstrip("\n") for l in open(os.path.join(WORK, "对象首句.txt"),
                                      encoding="utf-8") if l.strip()]
assert len(idx) == len(heads), (len(idx), len(heads))
for r, h in zip(idx, heads):
    parts = h.split(None, 3)
    print("%s\t%s\t%s\t%s" % (r[0], r[1], parts[1] if len(parts) > 1 else "-",
                              parts[3] if len(parts) > 3 else ""))
