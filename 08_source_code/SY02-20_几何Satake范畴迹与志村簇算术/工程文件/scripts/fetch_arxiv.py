# -*- coding: utf-8 -*-
r"""从 arXiv 取 e-print 源并解压到 工程文件/work/原文/arxiv/。

系统 bash 没有 gzip/unzip，这里全用 Python：
  - e-print 是 gzip（单文件 tex）或 tar.gz（多文件）
  - 先按 gzip 解，失败再按 tarfile 解
用法： python fetch_arxiv.py 1810.07375
"""
import gzip
import io
import os
import sys
import tarfile
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                    # 工程文件
OUT = os.path.join(ROOT, "work", "原文", "arxiv")
RAW = os.path.join(ROOT, "work", "原文", "eprint.bin")


def main() -> int:
    aid = sys.argv[1] if len(sys.argv) > 1 else "1810.07375"
    os.makedirs(OUT, exist_ok=True)
    url = "https://arxiv.org/e-print/" + aid
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research translation)"})
    data = urllib.request.urlopen(req, timeout=120).read()
    with open(RAW, "wb") as fh:
        fh.write(data)
    print("downloaded", len(data), "bytes")

    # 1) 试 gzip 单文件
    try:
        text = gzip.decompress(data)
        if text.lstrip()[:5] == b"\\docu" or b"\\documentclass" in text[:4000]:
            with open(os.path.join(OUT, "main.tex"), "wb") as fh:
                fh.write(text)
            print("gzip -> main.tex", len(text), "bytes")
            return 0
    except OSError:
        pass

    # 2) 试 tar
    try:
        tf = tarfile.open(fileobj=io.BytesIO(data))
        tf.extractall(OUT)
        names = tf.getnames()
        print("tar ->", len(names), "files")
        for n in names:
            print("   ", n)
        return 0
    except tarfile.TarError as exc:
        print("tar failed:", exc)
    b = gzip.decompress(data)
    with open(os.path.join(OUT, "main.tex"), "wb") as fh:
        fh.write(b)
    print("fallback raw gzip -> main.tex", len(b))
    return 0


if __name__ == "__main__":
    sys.exit(main())
