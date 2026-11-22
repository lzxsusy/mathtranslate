# -*- coding: utf-8 -*-
"""编号对账：从原 PDF 文本层按阅读顺序抽出所有编号对象（定理类 + 公式），
与译文编译出的 PDF 抽出的同类序列做 diff。

用法：
  python numbering.py orig           -> 工程文件/work/numbering_orig.txt
  python numbering.py mine <pdf>     -> 工程文件/work/numbering_mine.txt
  python numbering.py diff           -> 逐项比对，打印首个分歧位置
"""
import os
import re
import sys

import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(ROOT, "work")

ENV = (
    "Theorem|Proposition|Lemma|Corollary|Conjecture|Definition|Remark|Example|"
    "Construction|Hypothesis|Question|Notation|Convention|Exercise|Sublemma|Caution"
)
EN2ZH = {
    "Theorem": "定理", "Proposition": "命题", "Lemma": "引理", "Corollary": "推论",
    "Conjecture": "猜想", "Definition": "定义", "Remark": "注", "Example": "例",
    "Construction": "构造", "Hypothesis": "假设", "Question": "问题",
    "Notation": "记号", "Convention": "约定", "Exercise": "练习",
    "Sublemma": "子引理", "Caution": "注意",
}
ZH2EN = {v: k for k, v in EN2ZH.items()}

PAT_THM = re.compile(r"\b(" + ENV + r")\s+(\d+\.\d+\.\d+)")
PAT_EQ = re.compile(r"^\s*\((\d+\.\d+)\)\s*$")


def scan(pdf_path, zh=False):
    doc = pymupdf.open(pdf_path)
    out = []
    for pno, page in enumerate(doc, start=1):
        lines = page.get_text().splitlines()
        for line in lines:
            if zh:
                m = re.search(r"(" + "|".join(ZH2EN) + r")\s+(\d+\.\d+\.\d+)", line)
                if m:
                    out.append((pno, m.group(1), m.group(2)))
                    continue
            else:
                m = PAT_THM.search(line)
                if m:
                    out.append((pno, m.group(1), m.group(2)))
                    continue
            m = PAT_EQ.search(line)
            if m:
                out.append((pno, "EQ", m.group(1)))
    return out


def write(seq, path):
    with open(path, "w", encoding="utf-8") as fh:
        for pno, kind, num in seq:
            fh.write("%d\t%s\t%s\n" % (pno, kind, num))
    print("wrote", path, len(seq), "items")


def load(path):
    seq = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            pno, kind, num = line.rstrip("\n").split("\t")
            seq.append((int(pno), kind, num))
    return seq


def main():
    mode = sys.argv[1]
    if mode == "orig":
        write(scan(os.path.join(WORK, "pdf", "src.pdf")), os.path.join(WORK, "numbering_orig.txt"))
    elif mode == "mine":
        write(scan(sys.argv[2], zh=True), os.path.join(WORK, "numbering_mine.txt"))
    elif mode == "diff":
        a = load(os.path.join(WORK, "numbering_orig.txt"))
        b = load(os.path.join(WORK, "numbering_mine.txt"))
        print("orig %d items, mine %d items" % (len(a), len(b)))
        bad = 0
        for i, (x, y) in enumerate(zip(a, b)):
            if x[1:] != y[1:]:
                print("MISMATCH #%d: orig p%d %s %s | mine p%d %s %s" % (i, x[0], x[1], x[2], y[0], y[1], y[2]))
                bad += 1
                if bad >= 12:
                    print("... stop after 12 mismatches")
                    break
        if len(a) != len(b):
            print("tail orig:", a[min(len(a), len(b)):][:8])
            print("tail mine:", b[min(len(a), len(b)):][:8])
        if bad == 0 and len(a) == len(b):
            print("OK: numbering identical")


if __name__ == "__main__":
    main()
