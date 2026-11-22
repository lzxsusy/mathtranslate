# -*- coding: utf-8 -*-
"""解压 arXiv e-print（1602.01451）到 工程文件/work/原文/。
系统无 gzip/tar，全部用 Python 模块。
输入：work/eprint/yun.eprint（curl 下载的 gzip）
输出：work/原文/<源文件>
"""
import gzip
import io
import os
import sys
import tarfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                     # 工程文件
EP = os.path.join(ROOT, "work", "eprint", "yun.eprint")
OUT = os.path.join(ROOT, "work", "原文")
SRC = os.path.join(ROOT, "work", "src")


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    with open(EP, "rb") as fh:
        raw = fh.read()
    data = gzip.decompress(raw)
    print("decompressed bytes:", len(data), "magic:", data[:8])
    try:
        tf = tarfile.open(fileobj=io.BytesIO(data))
        names = tf.getnames()
        os.makedirs(SRC, exist_ok=True)
        count = 0
        for m in tf.getmembers():
            if not m.isfile():
                continue
            base = os.path.basename(m.name)
            if not base:
                continue
            with open(os.path.join(SRC, base), "wb") as out:
                out.write(tf.extractfile(m).read())
            count += 1
        print("tar members:", len(names), "files extracted to work/src:", count)
        for n in sorted(os.listdir(SRC)):
            print("  ", n, os.path.getsize(os.path.join(SRC, n)))
    except tarfile.TarError:
        # 单文件（.tex）
        dst = os.path.join(OUT, "main.tex")
        with open(dst, "wb") as out:
            out.write(data)
        print("single file written:", dst, len(data))


if __name__ == "__main__":
    sys.exit(main())
