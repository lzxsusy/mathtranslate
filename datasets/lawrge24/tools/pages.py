#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""读取原文分页文本：page N 的正文在 '===== PDF PAGE N+1 =====' 之前。"""
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
DATASET = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(DATASET))
SRC = os.path.join(REPO, "08_source_code", "SY02-15_相对朗兰兹对偶",
                   "工程文件", "work", "原文")

MARK = re.compile(r"^===== PDF PAGE (\d+) =====\s*$", re.M)


def load_pages(n):
    """返回 {pageno: text}，覆盖 chNN.txt 的全部页。"""
    path = os.path.join(SRC, "ch%02d.txt" % n)
    with io.open(path, encoding="utf-8") as f:
        raw = f.read()
    marks = list(MARK.finditer(raw))
    pages = {}
    start = 0
    prev = None
    for m in marks:
        end = m.start()
        p = int(m.group(1)) - 1
        pages[p] = raw[start:end]
        start = m.end()
        prev = p
    if prev is not None:
        pages[prev + 1] = raw[start:]
    return pages


def norm(s):
    return re.sub(r"\s+", " ", s).strip()
