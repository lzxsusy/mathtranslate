#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按关键词在逐页文本里挑候选原句，供资料卡 sources[].quote 使用。"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "src")

KEYS = sys.argv[1:]


def sentences(text):
    t = re.sub(r"\s+", " ", text)
    t = t.replace("´e", "é").replace("`e", "è").replace("ˆe", "ê")
    return re.split(r"(?<=[.!?])\s+(?=[A-ZÉÀÔÇÎÂÊÛÜ␣])", t)


def main():
    pages = {}
    for f in sorted(os.listdir(SRC)):
        if re.fullmatch(r"p\d{3}\.txt", f):
            pages[int(f[1:4])] = open(os.path.join(SRC, f), encoding="utf-8").read()
    for kw in KEYS:
        print("### " + kw)
        n = 0
        for p, txt in sorted(pages.items()):
            for s in sentences(txt):
                if kw.lower() in s.lower():
                    s = s.strip()
                    if 40 <= len(s) <= 220:
                        print("p%d\t%s" % (p, s))
                        n += 1
                        if n >= 3:
                            break
            if n >= 3:
                break
        if n == 0:
            print("p?\t(未找到)")


main()
