#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""GMN3 编号公式精确计数（排除注释行、处理 align 各行与 \\notag/\\nonumber）。

用法：python eqcount2.py
输出：每块式数 + 合计，并与 PDF 行末编号实测值对照。
"""
import io
import os
import re

TEX = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "..", "..", "00_原文", "GMN3_1006.0146", "1006.0146v2_src", "Lamination-Paper.tex"))

CHUNKS = [
    ("ch01", 360, 560), ("ch02", 561, 1028), ("ch03", 1029, 1506), ("ch04", 1507, 2020),
    ("ch05", 2021, 2606), ("ch06", 2607, 3114), ("ch07", 3115, 3694), ("ch08", 3695, 4378),
    ("ch09", 4379, 4685), ("ch10", 4686, 5050), ("ch11", 5051, 5359), ("ch12", 5360, 5654),
    ("ch13", 5655, 5863), ("ch14", 5864, 6289), ("ch15", 6290, 6895), ("ch16", 6896, 7129),
]


def strip_comment(line):
    """去掉行内未转义的 % 之后的内容。"""
    out, i = [], 0
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


def count_region(lines):
    """lines: 已去注释的文本行列表。返回编号公式数。"""
    n = 0
    i = 0
    while i < len(lines):
        s = lines[i]
        if re.search(r"\\begin\{equation\}", s):
            # 单行环境：equation 里出现 notag/nonumber 则无编号
            body = s
            j = i
            while not re.search(r"\\end\{equation\}", body) and j + 1 < len(lines):
                j += 1
                body += " " + lines[j]
            if not re.search(r"\\(notag|nonumber)\b", body):
                n += 1
            i = j + 1
            continue
        m = re.search(r"\\begin\{(align|gather|eqnarray)\}", s)
        if m:
            env = m.group(1)
            body = s
            j = i
            while not re.search(r"\\end\{" + env + r"\}", body) and j + 1 < len(lines):
                j += 1
                body += "\n" + lines[j]
            inner = re.sub(r"^.*?\\begin\{" + env + r"\}", "", body, count=1, flags=re.S)
            inner = re.sub(r"\\end\{" + env + r"\}.*$", "", inner, flags=re.S)
            # 按行尾 \\ 切行
            rows = re.split(r"\\\\", inner)
            for row in rows:
                if row.strip() and not re.search(r"\\(notag|nonumber)\b", row) \
                   and not re.match(r"^\s*$", row):
                    n += 1
            i = j + 1
            continue
        i += 1
    return n


def main():
    raw = io.open(TEX, encoding="utf-8", errors="replace").read().split("\n")
    clean = [strip_comment(l) for l in raw]
    total = 0
    rows = []
    for name, a, b in CHUNKS:
        c = count_region(clean[a - 1:b])
        total += c
        rows.append((name, a, b, c))
    for name, a, b, c in rows:
        print("%s  %4d-%4d  式 %2d" % (name, a, b, c))
    print("合计 %d" % total)


if __name__ == "__main__":
    main()
