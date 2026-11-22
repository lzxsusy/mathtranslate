# -*- coding: utf-8 -*-
r"""把 arXiv 源 main.tex 里的非法字节定位并给出可读的 UTF-8 工作副本。

原文是老式 TeX 源，混入了 latin-1 的重音字节（如 \'e 直接写成 0xE9），
UTF-8 解码会在这些位置失败。做法：逐行尝试 utf-8；失败的行按 latin-1 解，
并打印行号与前后文，便于人工确认没有把数学符号改坏。
用法： python clean_source.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "work", "原文", "arxiv", "main.tex")
OUT = os.path.join(ROOT, "work", "原文", "main.tex")

raw = open(SRC, "rb").read()
lines = raw.split(b"\n")
out = []
bad = []
for i, b in enumerate(lines, 1):
    try:
        out.append(b.decode("utf-8"))
    except UnicodeDecodeError:
        bad.append(i)
        out.append(b.decode("latin-1"))
open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
print("lines", len(lines), "latin-1 fallback lines:", len(bad))
print(bad[:40])
for i in bad[:20]:
    print(i, repr(lines[i - 1][:120]))
