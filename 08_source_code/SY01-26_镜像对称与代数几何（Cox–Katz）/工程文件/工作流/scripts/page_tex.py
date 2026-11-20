#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Print the translated text that belongs to one PDF page (\\SourcePage{N} block).

usage: python page_tex.py 121
"""
import glob, os, re, sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
page = int(sys.argv[1])
toks = []
for f in sorted(glob.glob("chapters/*.tex")):
    lines = open(f, encoding="utf-8").read().split("\n")
    cur = None
    for i, line in enumerate(lines, 1):
        for m in re.finditer(r"\\SourcePage\{(\d+)\}", line):
            cur = int(m.group(1))
        if cur == page:
            toks.append((f, i, line))
out = [f"# PDF page {page} (printed p{page - 23})"]
for f, i, line in toks:
    out.append(f"[{os.path.basename(f)}:{i}] {line}")
print("\n".join(out))
