# -*- coding: utf-8 -*-
r"""粗查漏译：按小节比较「正文段落」的条数（块计数，不是行计数）。

把整份源文件按空行切块：块首若是 \begin/\end/\label/\section/\subsection/\[/$$ 等
命令，就不算正文段；否则算一个正文段（原文与译文都遵守「一段一块」的写法）。
比较时按小节键（"2.1" 这种）配对。
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PROJ = os.path.dirname(ROOT)
ORIG = os.path.join(ROOT, "work", "原文", "main.tex")
CHUNKS = os.path.join(PROJ, "源码", "chunks")

NO_PROSE = ("\\begin", "\\end", "\\label", "\\item", "\\section", "\\subsection",
            "\\bibitem", "\\[", "$$", "\\index", "\\hspace", "\\vspace",
            "\\newpage", "\\clearpage", "\\par", "\\medskip", "\\bigskip",
            "\\smallskip", "%", "\\documentclass", "\\input", "\\title",
            "\\author", "\\date", "\\maketitle", "\\tableofcontents")


def blocks(text):
    buf = []
    for raw in text.split("\n"):
        if raw.strip():
            buf.append(raw)
        elif buf:
            yield buf
            buf = []
    if buf:
        yield buf


def prose_blocks(text):
    """产出 (行号, 块文本) 的正文段。"""
    out = []
    for blk in blocks(text):
        first = blk[0].strip()
        if first.startswith("%"):
            continue
        if any(first.startswith(p) for p in NO_PROSE):
            continue
        out.append("\n".join(blk))
    return out


def locate(text):
    """产出 (块文本, 小节键)，块按出现次序。"""
    sec = sub = 0
    cur = "0"
    out = []
    pos = 0
    for blk in blocks(text):
        first = blk[0].strip()
        for line in blk:
            if re.search(r"\\section(?!\*)\s*\{", line):
                sec += 1
                sub = 0
                cur = "%d" % sec
            elif re.search(r"\\subsection(?!\*)\s*\{", line):
                sub += 1
                cur = "%d.%d" % (sec, sub)
        if first.startswith("%"):
            continue
        if any(first.startswith(p) for p in NO_PROSE):
            continue
        out.append((cur, "\n".join(blk)))
    return out


def main():
    otext = open(ORIG, encoding="utf-8").read().split(r"\begin{thebibliography}")[0]
    files = sorted(glob.glob(os.path.join(CHUNKS, "ch*.tex")))
    mtext = ""
    for f in files:
        mtext += open(f, encoding="utf-8").read().split(r"\begin{thebibliography}")[0] + "\n\n"

    po = locate(otext)
    pm = locate(mtext)
    oo, mo = [], []
    for k, _ in po:
        if k not in oo:
            oo.append(k)
    for k, _ in pm:
        if k not in mo:
            mo.append(k)
    o = {k: sum(1 for kk, _ in po if kk == k) for k in oo}
    m = {k: sum(1 for kk, _ in pm if kk == k) for k in mo}

    print("原文小节 %d 个，译文小节 %d 个；原文正文段 %d，译文正文段 %d"
          % (len(oo), len(mo), len(po), len(pm)))
    bad = 0
    for k in oo:
        a, b = o.get(k, 0), m.get(k)
        if b is None:
            print("%-6s orig %3d | mine  （缺）   <-- 译文无此小节" % (k, a))
            bad += 1
        elif a != b:
            print("%-6s orig %3d | mine %3d   <-- 差 %+d" % (k, a, b, b - a))
            bad += 1
        else:
            print("%-6s orig %3d | mine %3d" % (k, a, b))
    for k in mo:
        if k not in o:
            print("%-6s orig  （无） | mine %3d   <-- 译文多出" % (k, m[k]))
            bad += 1
    print("段落数不一致的小节数：", bad)


if __name__ == "__main__":
    main()
