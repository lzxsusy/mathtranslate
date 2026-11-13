# -*- coding: utf-8 -*-
"""中文标点/病灶词 lint + 自动修复 ASCII 引号与半角标点（仅当两侧是汉字时）。"""
import io
import os
import re

ROOT = r"<本地路径>"
SRC = os.path.join(ROOT, "src", "chunks")

CJK = r"\u4e00-\u9fff"
forbidden = ["被…所", "进行…的", "对于…而言"]


def fix(text):
    n = {}
    n["quote"] = text.count('"')
    text = re.sub(r'"([^"\n]*)"', lambda m: "\u300c" + m.group(1) + "\u300d", text)
    for half, full in [(r",", "\uff0c"), (r";", "\uff1b"), (r":", "\uff1a"), (r"\?", "\uff1f"), (r"!", "\uff01")]:
        pat = "(?<=[%s])%s(?=[%s\\s])" % (CJK, half, CJK)
        text, k = re.subn(pat, full, text)
        n[half] = k
    return text, n


total = {}
for i in range(15):
    name = "ch%02d" % i
    path = os.path.join(SRC, name + ".tex")
    if not os.path.isfile(path):
        continue
    text = io.open(path, encoding="utf-8").read()
    new, n = fix(text)
    if new != text:
        io.open(path, "w", encoding="utf-8").write(new)
    bad = [w for w in forbidden if w in new]
    total[name] = (n, bad)
    print(name, n, bad)
