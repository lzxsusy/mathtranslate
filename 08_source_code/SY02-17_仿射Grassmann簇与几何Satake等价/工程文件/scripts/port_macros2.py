# -*- coding: utf-8 -*-
r"""通用版宏移植：从原文 .tex 的导言区抽取宏定义，生成 源码/preamble_macros.tex。

用法： python port_macros2.py <原文.tex> <起始行> <结束行> [跳过名1,名2,...]

支持 \newcommand{\x}[n]{{...}}、\nc{\x}{...}、\def\x{...}、
\DeclareMathOperator{\x}{...}、\newtheorem 以外的简单定义。
行内 `%` 注释先剔除（带转义的 \% 不算）。
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(ROOT), "源码", "preamble_macros.tex")

SKIP_DEFAULT = {"on", "nc", "quash", "xw", "xinwen", "textcyr", "proof", "qedsymbol"}

NC = re.compile(r"^\s*\\(?:newcommand|renewcommand)\s*\{\s*\\([A-Za-z@]+)\s*\}(\[[^\]]*\])?\s*\{(.*)\}\s*$")
NC2 = re.compile(r"^\s*\\nc\s*\{\s*\\([A-Za-z@]+)\s*\}(\[[^\]]*\])?\s*\{(.*)\}\s*$")
DEF = re.compile(r"^\s*\\def\s*\\([A-Za-z@]+)\s*\{(.*)\}\s*$")
DMO = re.compile(r"^\s*\\DeclareMathOperator\*?\s*\{\s*\\([A-Za-z@]+)\s*\}\s*\{(.*)\}\s*$")


def strip_comment(line: str) -> str:
    out = []
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == "\\" and i + 1 < len(line):
            out.append(line[i:i + 2])
            i += 2
            continue
        if ch == "%":
            break
        out.append(ch)
        i += 1
    return "".join(out)


def main() -> None:
    if len(sys.argv) >= 3 and sys.argv[1].isdigit():
        src = os.path.join(ROOT, "work", "原文", "main.tex")
        a, b = int(sys.argv[1]), int(sys.argv[2])
        rest = sys.argv[3:]
    else:
        src, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
        rest = sys.argv[4:]

    skip = set(SKIP_DEFAULT)
    if rest:
        skip |= {t.strip() for t in rest[0].split(",") if t.strip()}
    with open(src, encoding="utf-8", errors="replace") as fh:
        lines = fh.read().splitlines()

    out = ["% 由 工程文件/scripts/port_macros2.py 从原文导言区自动移植，勿手改。"]
    seen = set()
    n = 0
    for line in lines[a - 1:b]:
        line = strip_comment(line)
        m = NC.match(line) or NC2.match(line)
        if m:
            name, opt, body = m.group(1), m.group(2) or "", m.group(3)
            if name in skip or name in seen:
                continue
            seen.add(name)
            out.append("\\newcommand{\\%s}%s{%s}" % (name, opt, body))
            n += 1
            continue
        m = DMO.match(line)
        if m:
            name, body = m.group(1), m.group(2)
            if name in skip or name in seen:
                continue
            seen.add(name)
            out.append("\\DeclareMathOperator{\\%s}{%s}" % (name, body))
            n += 1
            continue
        m = DEF.match(line)
        if m:
            name, body = m.group(1), m.group(2)
            if name in skip or name in seen:
                continue
            seen.add(name)
            out.append("\\newcommand{\\%s}{%s}" % (name, body))
            n += 1
    out.append("\\newcommand{\\on}{\\operatorname}")
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    print("macros:", n, "->", OUT)


if __name__ == "__main__":
    main()
