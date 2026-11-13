# -*- coding: utf-8 -*-
"""fix_quotes.py — 把源码里的 ASCII 直双引号 " 成对换成中文引号 “ ”。

用法：python fix_quotes.py [--dry-run]
规则：按文件顺序扫描非注释文本，遇到未转义的 " 交替替换为 “ / ”。
      只统计"成对"的情况；某文件出现奇数个则报告并保持原样（避免破坏）。
      不改注释行（% 之后）里的内容，除非注释里的引号也成对——注释也一并处理，便于阅读。
"""
import glob, os, sys

ROOT = r"<本地路径>"
DRY = "--dry-run" in sys.argv


def convert(s):
    out = []
    n = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s):
            out.append(s[i:i + 2])
            i += 2
            continue
        if c == '"':
            out.append("“" if n % 2 == 0 else "”")
            n += 1
        else:
            out.append(c)
        i += 1
    return "".join(out), n


bad = []
changed = []
for f in sorted(glob.glob(os.path.join(ROOT, "src", "*.tex"))):
    if os.path.basename(f) == "preamble.tex":
        continue
    s = open(f, encoding="utf-8").read()
    t, n = convert(s)
    if n == 0:
        continue
    if n % 2:
        bad.append((os.path.basename(f), n))
        continue
    if t != s:
        changed.append((os.path.basename(f), n))
        if not DRY:
            open(f, "w", encoding="utf-8", newline="\n").write(t)

print("替换：", changed)
if bad:
    print("!! 引号数为奇数的文件（未改，需人工看）：", bad)
