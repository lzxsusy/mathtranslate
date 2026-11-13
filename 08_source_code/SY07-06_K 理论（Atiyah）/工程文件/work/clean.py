# -*- coding: utf-8 -*-
"""清洗：去 BOM / CRLF / U+3000；并打印每个 chunk 状态"""
import os, glob, sys, re
sys.stdout.reconfigure(encoding='utf-8')
CH = r"<本地路径>"
for p in sorted(glob.glob(os.path.join(CH, "*.tex"))):
    b = open(p, "rb").read()
    orig = len(b)
    if b.startswith(b"\xef\xbb\xbf"):
        b = b[3:]
    t = b.decode("utf-8")
    t = t.replace("\r\n", "\n").replace("\r", "\n")
    if "\u3000" in t:
        t = t.replace("\u3000", "  ")
    if t.encode("utf-8") != b:
        open(p, "w", encoding="utf-8", newline="\n").write(t)
        print("cleaned", os.path.basename(p), orig, "->", len(t.encode()))
