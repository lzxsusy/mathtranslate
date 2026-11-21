#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""GMN1 合稿 QA：编译 + 编号对账 + 段落体量体检。

用法（在工程根或任意目录）：
    python 工程文件/qa.py

做四件事：
1) 在 源码/ 里跑 xelatex 三遍；
2) 统计 main.log 的 error / overfull / undefined；
3) 把译文 PDF 与原文 PDF 的「编号公式」集合逐节对账，报缺失与多余；
4) 输出每节页数、总页数，供与原文 66 页对照。
"""
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)
SRC = os.path.join(PROJ, "源码")
ORIG = os.path.join(
    PROJ, "..", "..", "00_原文", "GMN1_0807.4723", "0807.4723v3.pdf"
)
ORIG = os.path.normpath(ORIG)
XELATEX = r"C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe"


def build():
    for i in range(3):
        p = subprocess.run(
            [XELATEX, "-interaction=nonstopmode", "main.tex"],
            cwd=SRC,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    log = os.path.join(SRC, "main.log")
    txt = open(log, encoding="utf-8", errors="replace").read()
    errors = [l for l in txt.splitlines() if l.startswith("!")]
    over = re.findall(r"Overfull \\hbox \(([\d.]+)pt too wide\)", txt)
    over_big = [float(x) for x in over if float(x) > 3]
    undef = len(re.findall(r"Reference `[^']+' on page", txt))
    cite = len(re.findall(r"Citation `[^']+' on page", txt))
    pages = re.search(r"Output written on main\.pdf \((\d+) pages", txt)
    return {
        "errors": errors,
        "overfull_total": len(over),
        "overfull_gt3": over_big,
        "undefined_ref": undef,
        "undefined_cite": cite,
        "pages": int(pages.group(1)) if pages else None,
    }


def eqnums(pdf_path):
    """返回 {'2': [18, 19, ...], 'A': [...]} 形式的编号集合。

    只认「位于行末的公式编号」，避免把正文里引用的式 (2.18) 也算进来。
    """
    import fitz

    doc = fitz.open(pdf_path)
    got = defaultdict(set)
    pat = re.compile(r"^\(\s*(\d+|[A-E])\s*\.\s*(\d+)\s*\)$")
    for page in doc:
        lines = defaultdict(list)
        for word in page.get_text("words"):
            key = round(word[1] / 3.0)
            lines[key].append(word)
        for key, ws in lines.items():
            ws.sort(key=lambda w: w[0])
            txt = ws[-1][4]
            m = pat.match(txt)
            if m:
                got[m.group(1)].add(int(m.group(2)))
    return {k: sorted(v) for k, v in got.items()}


def compare():
    ours = eqnums(os.path.join(SRC, "main.pdf"))
    theirs = eqnums(ORIG) if os.path.exists(ORIG) else {}
    report = []
    for sec in sorted(set(ours) | set(theirs), key=lambda s: (len(s), s)):
        o = set(ours.get(sec, []))
        t = set(theirs.get(sec, []))
        missing = sorted(t - o)
        extra = sorted(o - t)
        report.append((sec, len(t), len(o), missing, extra))
    return report


def main():
    b = build()
    print("=" * 60)
    print("编译：%d 页" % (b["pages"] or -1))
    print("error：%d 处" % len(b["errors"]))
    for e in b["errors"][:10]:
        print("   ", e)
    print("overfull 总数 %d，其中 >3pt：%d 处 %s"
          % (b["overfull_total"], len(b["overfull_gt3"]), b["overfull_gt3"][:10]))
    print("undefined ref：%d，undefined cite：%d"
          % (b["undefined_ref"], b["undefined_cite"]))
    print("=" * 60)
    print("编号对账（节号：原文数 / 译文数 → 缺 / 多）")
    for sec, nt, no, miss, extra in compare():
        flag = ""
        if miss or extra:
            flag = "  <<<"
        print("  %-2s %3d / %3d  缺%s 多%s%s"
              % (sec, nt, no, miss[:12], extra[:12], flag))
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
