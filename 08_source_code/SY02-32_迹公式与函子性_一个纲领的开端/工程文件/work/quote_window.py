#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用法：python quote_window.py 13:BunG 43:adélisation ...
输出：页码 + 关键词周围（前 60 后 60 字符）的逐字窗口，用于卡片 quote。"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "src")


def load(p):
    fp = os.path.join(SRC, "p%03d.txt" % p)
    t = open(fp, encoding="utf-8").read()
    t = re.sub(r"\s+", " ", t)
    return t


for arg in sys.argv[1:]:
    p, kw = arg.split(":", 1)
    p = int(p)
    t = load(p)
    idx = t.lower().find(kw.lower())
    if idx < 0:
        print("### p%d %s -> (未找到)" % (p, kw))
        continue
    a = max(0, idx - 65)
    b = min(len(t), idx + len(kw) + 65)
    print("### p%d %s" % (p, kw))
    print(t[a:b].strip())
