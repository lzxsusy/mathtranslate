#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""GMN3 合稿 QA：编译 + 编号对账 + 页数体检。

用法（在工程根或任意目录）：
    python 工程文件/qa.py

做四件事：
1) 在 源码/ 里跑 xelatex 三遍；
2) 统计 main.log 的 error / overfull / undefined / 重复 label；
3) 把译文 PDF 与原文 PDF 的「编号公式」集合逐节对账，报缺失与多余
   （分块阶段 main.tex 只 input 已译块，其余节会整节报「缺」，属预期；
     合稿后应全节为 0 缺 0 多）；
4) 输出总页数，供与原文 124 页（印刷 123 页）对照。
"""
import os
import re
import subprocess
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)
SRC = os.path.join(PROJ, "源码")
ORIG = os.path.normpath(os.path.join(
    PROJ, "..", "..", "00_原文", "GMN3_1006.0146", "1006.0146v2.pdf"
))
XELATEX = r"C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe"


def build():
    for _ in range(3):
        subprocess.run(
            [XELATEX, "-interaction=nonstopmode", "main.tex"],
            cwd=SRC, capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
    log = os.path.join(SRC, "main.log")
    txt = open(log, encoding="utf-8", errors="replace").read()
    errors = [l for l in txt.splitlines() if l.startswith("!")]
    over = re.findall(r"Overfull \\hbox \(([\d.]+)pt too wide\)", txt)
    over_big = sorted({float(x) for x in over if float(x) > 3}, reverse=True)
    undef = len(re.findall(r"Reference `[^']+' on page", txt))
    cite = len(re.findall(r"Citation `[^']+' on page", txt))
    dup = re.findall(r"LaTeX Warning: Label `([^']+)' multiply defined", txt)
    pages = re.search(r"Output written on main\.pdf \((\d+) pages", txt)
    return {
        "errors": errors,
        "overfull_total": len(over),
        "overfull_gt3": over_big,
        "undefined_ref": undef,
        "undefined_cite": cite,
        "dup_labels": sorted(set(dup)),
        "pages": int(pages.group(1)) if pages else None,
    }


def eqnums(pdf_path):
    """返回 {'1': [1, 2, ...], 'A': [...]} 形式的编号集合（只认行末编号）。"""
    import fitz

    doc = fitz.open(pdf_path)
    got = defaultdict(set)
    pat = re.compile(r"^\(\s*(\d+|[A-G])\s*\.\s*(\d+)\s*\)$")
    for page in doc:
        lines = defaultdict(list)
        for word in page.get_text("words"):
            key = round(word[1] / 3.0)
            lines[key].append(word)
        for ws in lines.values():
            ws.sort(key=lambda w: w[0])
            m = pat.match(ws[-1][4])
            if m:
                got[m.group(1)].add(int(m.group(2)))
    return {k: sorted(v) for k, v in got.items()}


def compare():
    ours = eqnums(os.path.join(SRC, "main.pdf"))
    theirs = eqnums(ORIG) if os.path.exists(ORIG) else {}
    report = []
    for sec in sorted(set(ours) | set(theirs), key=lambda s: (len(s), s)):
        o, t = set(ours.get(sec, [])), set(theirs.get(sec, []))
        report.append((sec, len(t), len(o), sorted(t - o), sorted(o - t)))
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
    print("undefined ref：%d，undefined cite：%d" % (b["undefined_ref"], b["undefined_cite"]))
    print("重复 label：%d 个 %s" % (len(b["dup_labels"]), b["dup_labels"][:10]))
    print("=" * 60)
    print("编号对账（节号：原文数 / 译文数 → 缺 / 多）")
    for sec, nt, no, miss, extra in compare():
        flag = "  <<<" if (miss or extra) else ""
        print("  %-2s %3d / %3d  缺%s 多%s%s"
              % (sec, nt, no, miss[:12], extra[:12], flag))
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
