#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""编译整本书：生成 main.tex -> xelatex 两遍 -> 报告页数与错误。

用法（工作区根目录）：
  python qsg/tools/build.py
"""
import os
import re
import subprocess
import sys
from pathlib import Path

QSG = Path(__file__).resolve().parent.parent
WS = QSG.parent
TEXBIN = WS / ".texlive" / "2026" / "bin" / "windows"
XELATEX = TEXBIN / "xelatex.exe"


def run(cmd, cwd, logfile, env):
    with open(logfile, "wb") as fh:
        p = subprocess.run(cmd, cwd=str(cwd), stdout=fh, stderr=subprocess.STDOUT,
                           env=env, timeout=1200)
    return p.returncode


def strip_comments(text):
    out = []
    for line in text.splitlines():
        i, cut = 0, len(line)
        while i < len(line):
            if line[i] == "\\":
                i += 2
                continue
            if line[i] == "%":
                cut = i
                break
            i += 1
        out.append(line[:cut])
    return "\n".join(out)


def check_envs():
    """编译前检查每个片段的 LaTeX 环境是否闭合（防止读到写了一半的文件）。"""
    import re
    bad = []
    for f in sorted((QSG / "tex").glob("*.tex")):
        s = strip_comments(f.read_text(encoding="utf-8"))
        stack = []
        for m in re.finditer(r"\\(begin|end)\{([^}]+)\}", s):
            if m.group(1) == "begin":
                stack.append(m.group(2))
            elif stack and stack[-1] == m.group(2):
                stack.pop()
            else:
                stack.append("MISMATCH:" + m.group(2))
        if stack:
            bad.append((f.name, stack[-4:]))
    return bad


def main():
    if not XELATEX.exists():
        sys.exit(f"找不到 xelatex: {XELATEX}")
    broken = check_envs()
    if broken:
        print("!! 以下片段环境未闭合（可能仍在写入）：")
        for name, st in broken:
            print(f"   {name}: {st}")
        sys.exit(2)
    env = dict(os.environ)
    env["PATH"] = str(TEXBIN) + os.pathsep + env.get("PATH", "")

    subprocess.run([sys.executable, str(QSG / "tools" / "make_main.py")],
                   cwd=str(QSG), check=True)

    build = QSG / "build"
    build.mkdir(exist_ok=True)
    for name in ("main.aux", "main.toc", "main.out", "main.lof", "main.lot"):
        p = QSG / name
        if p.exists():
            p.unlink()
    for i in (1, 2):
        rc = run([str(XELATEX), "-interaction=nonstopmode", "main.tex"],
                 QSG, build / f"pass{i}.log", env)
        print(f"pass{i}: exit {rc}")

    log = (QSG / "main.log").read_text(encoding="utf-8", errors="replace")
    errs = [ln for ln in log.splitlines() if ln.startswith("!")]
    if errs:
        print("---- ERROR ----")
        for ln in errs[:20]:
            print(ln)
        # 定位上下文
        for m in re.finditer(r"^!.*$", log, re.M):
            ctx = log[max(0, m.start() - 200):m.start()]
            print("...上下文:", ctx.splitlines()[-3:])
            break
        sys.exit(1)

    pdf = QSG / "main.pdf"
    if not pdf.exists():
        sys.exit("没有生成 main.pdf")
    pages = 0
    m = re.search(r"Output written on .*?\((\d+) pages?", log)
    if m:
        pages = int(m.group(1))
    print(f"BUILD OK: {pdf}  {pages} pages  {pdf.stat().st_size/1024/1024:.2f} MiB")


if __name__ == "__main__":
    main()
