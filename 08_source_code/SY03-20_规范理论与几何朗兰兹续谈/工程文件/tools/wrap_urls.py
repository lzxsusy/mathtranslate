# -*- coding: utf-8 -*-
r"""把四个 part 文件里 \transnote{...} 中的裸 URL 包成 \url{...}，避免脚注里长 URL 撑破行（overfull）。

* 只处理 http/https 裸链接；已包在 \url{...} 里的不动。
* 只在 \transnote 参数内部动手（用花括号配对定位），注释行跳过。
* 幂等：重复运行不会重复包装。
Run:  python 工程文件/tools/wrap_urls.py [--check]
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(ROOT, "源码")
PARTS = ["part1_zh.tex", "part2_zh.tex", "part3_zh.tex", "part4_zh.tex"]

TRANSNOTE = re.compile(r"\\transnote\s*\{")
URL = re.compile(r"https?://[A-Za-z0-9\-._~:/?#\[\]@!$&'()*+,;=%]+")
# URL 末尾常跟着中文标点或西文标点，剥掉
TAIL = re.compile(r"[.,;:!?'\)\]]+$")


def find_close(text, open_pos):
    depth = 0
    i = open_pos
    while i < len(text):
        ch = text[i]
        if ch == "\\":
            i += 2
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def strip_comment_map(text):
    """返回每行是否处于注释中的布尔数组（行内 % 之前算正文）。"""
    out = []
    for line in text.split("\n"):
        in_comment = False
        i = 0
        cut = None
        while i < len(line):
            if line[i] == "\\":
                i += 2
                continue
            if line[i] == "%":
                cut = i
                break
            i += 1
        out.append(cut if cut is not None else -1)
    return out


def wrap_body(body):
    """在正文片段里包装 URL；返回 (新片段, 包装个数)。"""
    changed = 0

    def repl(m):
        nonlocal changed
        raw = m.group(0)
        m2 = TAIL.search(raw)
        tail = ""
        if m2:
            tail = m2.group(0)
            raw = raw[: -len(tail)]
        changed += 1
        return "\\url{%s}%s" % (raw, tail)

    new = URL.sub(repl, body)
    return new, changed


def process(path):
    raw = open(path, encoding="utf-8").read()
    comment_cut = strip_comment_map(raw)
    pos = 0
    pieces = []
    total = 0
    for m in TRANSNOTE.finditer(raw):
        open_pos = m.end() - 1
        close_pos = find_close(raw, open_pos)
        if close_pos < 0:
            continue
        body = raw[open_pos + 1 : close_pos]
        new_body, n = wrap_body(body)
        if n:
            pieces.append((open_pos + 1, close_pos, new_body))
            total += n
    if not pieces:
        return 0
    out = []
    last = 0
    for a, b, nb in pieces:
        out.append(raw[last:a])
        out.append(nb)
        last = b
    out.append(raw[last:])
    new = "".join(out)
    open(path, "w", encoding="utf-8", newline="\n").write(new)
    return total


def main():
    check = "--check" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    files = [f for f in PARTS if (not only or f in only or f.replace(".tex", "") in only)]
    grand = 0
    for fn in files:
        p = os.path.join(SRC, fn)
        if check:
            raw = open(p, encoding="utf-8").read()
            n = 0
            for m in TRANSNOTE.finditer(raw):
                body = raw[m.end() - 1: find_close(raw, m.end() - 1)]
                n += len(URL.findall(body))
            print("%s: 裸 URL %d 处" % (fn, n))
            grand += n
        else:
            n = process(p)
            print("%s: 包装 %d 处" % (fn, n))
            grand += n
    if check:
        print("合计待包装 %d 处" % grand)
    return 0


if __name__ == "__main__":
    sys.exit(main())
