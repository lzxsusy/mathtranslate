#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""compile_section.py — 只编译某一节（临时目录，不污染主工程 aux）

用法：python compile_section.py 5 [--keep]

做法：在 %TEMP%/sy0245_sNN/ 生成 solo.tex：
    \\documentclass[11pt,a4paper]{article}
    \\input{<工程>/源码/preamble.tex}
    \\begin{document}
    \\input{<工程>/源码/sections/sNN-*.tex}
    \\end{document}
用 xelatex 编译两遍，抽取 `! ` 开头的错误与最终的 Overfull/Undefined 摘要。
"""
import re
import shutil
import subprocess
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SECT = ROOT / "源码" / "sections"
XELATEX = r"C:/Users/admin/AppData/Local/Programs/MiKTeX/miktex/bin/x64/xelatex.exe"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    nn = int(sys.argv[1])
    keep = "--keep" in sys.argv
    hits = sorted(SECT.glob(f"s{nn:02d}-*.tex"))
    if not hits:
        print(f"找不到 源码/sections/s{nn:02d}-*.tex")
        return 2
    f = hits[0]
    tmp = Path(tempfile.mkdtemp(prefix=f"sy0245_s{nn:02d}_"))
    solo = tmp / "solo.tex"
    solo.write_text(
        "\\documentclass[11pt,a4paper]{article}\n"
        f"\\input{{{ (ROOT / '源码' / 'preamble.tex').as_posix() }}}\n"
        "\\begin{document}\n"
        f"\\input{{{ f.as_posix() }}}\n"
        "\\end{document}\n",
        encoding="utf-8",
    )
    print(f"编译 {f.name} 于 {tmp}")
    ok = True
    for i in (1, 2):
        p = subprocess.run([XELATEX, "-interaction=nonstopmode", "-halt-on-error",
                            "-output-directory", str(tmp), str(solo)],
                           capture_output=True, text=True, errors="replace")
        log = (tmp / "solo.log")
        if p.returncode != 0:
            text = log.read_text(encoding="utf-8", errors="replace") if log.exists() else p.stdout
            errs = [ln for ln in text.splitlines() if ln.startswith("!")]
            ctx = []
            lines = text.splitlines()
            for k, ln in enumerate(lines):
                if ln.startswith("!"):
                    ctx.extend(lines[k:k + 6])
            print(f"--- 第 {i} 遍失败 (exit {p.returncode}) ---")
            print("\n".join(errs[:20]) if errs else "(日志里没有 '!' 行，看下方片段)")
            print("\n".join(ctx[:40]))
            ok = False
            break
    if ok:
        log = (tmp / "solo.log").read_text(encoding="utf-8", errors="replace")
        warns = [ln for ln in log.splitlines()
                 if re.search(r"(Overfull|Underfull|Undefined control|Missing character)", ln)]
        pages = re.search(r"Output written on .*?\((\d+) page", log)
        print(f"OK：0 error，{pages.group(1) if pages else '?'} 页，警告 {len(warns)} 条")
        for w in warns[:10]:
            print("   ", w.strip()[:120])
    if not keep:
        shutil.rmtree(tmp, ignore_errors=True)
    else:
        print(f"保留目录：{tmp}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
