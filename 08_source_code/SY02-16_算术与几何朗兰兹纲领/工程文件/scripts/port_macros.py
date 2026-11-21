# -*- coding: utf-8 -*-
"""从原文 preamble 抽取宏定义，生成 源码/preamble_macros.tex。

原文用 \\nc{...}{...}（\\nc = \\newcommand），这里统一改成 \\newcommand，
并跳过 \\on（改用 \\operatorname 简写）、\\nc 本身、\\quash、\\xw、\\xinwen。
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "work", "原文", "ICM-arXiv.tex")
OUT = os.path.join(os.path.dirname(ROOT), "源码", "preamble_macros.tex")

SKIP = {"on", "nc", "quash", "xw", "xinwen", "textcyr"}

PAT = re.compile(r"^\s*(?:\\newcommand\{\\([A-Za-z@]+)\}|\\nc\{\\([A-Za-z@]+)\})\s*(\[[^\]]*\])?\s*\{(.*)\}\s*$")


def main() -> None:
    with open(SRC, encoding="utf-8", errors="replace") as fh:
        lines = fh.read().splitlines()
    out = ["% 由 工程文件/scripts/port_macros.py 从原文 preamble 自动移植，勿手改。"]
    seen = set()
    count = 0
    for line in lines[48:470]:
        line = re.split(r"(?<!\\)%", line)[0]
        m = PAT.match(line)
        if not m:
            continue
        name = m.group(1) or m.group(2)
        if name in SKIP or name in seen:
            continue
        body = m.group(4)
        # 去掉源码里 \\ 转义（read 工具视角下的双写），实际文件是单写
        seen.add(name)
        narg = m.group(3) or ""
        out.append("\\newcommand{\\%s}%s{%s}" % (name, narg, body))
        count += 1
    out.append("\\newcommand{\\on}{\\operatorname}")
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    print("macros:", count, "->", OUT)


if __name__ == "__main__":
    main()
