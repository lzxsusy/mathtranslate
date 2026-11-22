# -*- coding: utf-8 -*-
"""解压 arXiv e-print（gzip 单文件或 tar.gz）。系统 bash 无 gzip，故用 Python。"""
import gzip
import io
import os
import tarfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                     # 工程文件
SRC = os.path.join(ROOT, "work", "原文", "src.gz")
OUT = os.path.join(ROOT, "work", "原文")

raw = gzip.open(SRC, "rb").read()
print("raw bytes", len(raw), "head", raw[:8])
if raw[257:262] == b"ustar":
    tf = tarfile.open(fileobj=io.BytesIO(raw))
    tf.extractall(OUT)
    for m in tf.getmembers():
        print(" ", m.name, m.size)
else:
    p = os.path.join(OUT, "main.tex")
    with open(p, "wb") as fh:
        fh.write(raw)
    print("wrote", p, os.path.getsize(p))
