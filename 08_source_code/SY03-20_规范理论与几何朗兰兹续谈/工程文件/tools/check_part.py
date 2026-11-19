# -*- coding: utf-8 -*-
"""Lightweight structural check for one part file (run before handing back).

Usage: python check_part.py 源码/part1_zh.tex
Checks: UTF-8 decodable; brace balance; unescaped %; $ balance; begin/end environment
matching; count of \\transnote; suspicious patterns.
"""
import re
import sys
import os

def main(path):
    raw = open(path, "rb").read()
    problems = []
    if raw.startswith(b"\xef\xbb\xbf"):
        problems.append("文件带 UTF-8 BOM")
    if b"\r\n" in raw:
        problems.append("含 CRLF 行尾（应为 LF）")
    try:
        txt = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        print("FATAL: 不是合法 UTF-8: %s" % exc)
        return 1

    # strip comments line-wise (a % not escaped by backslash)
    lines = txt.split("\n")
    stripped = []
    for no, line in enumerate(lines, 1):
        out = []
        i = 0
        while i < len(line):
            ch = line[i]
            if ch == "\\" and i + 1 < len(line):
                out.append(line[i : i + 2])
                i += 2
                continue
            if ch == "%":
                problems.append("第 %d 行有未转义 %%（注释或误写）: %s" % (no, line.strip()[:60]))
                break
            out.append(ch)
            i += 1
        stripped.append("".join(out))
    body = "\n".join(stripped)

    # remove \verb and verbatim if any
    body_nv = re.sub(r"\\verb\*?\|[^|]*\||\\verb\*?\{(?:[^{}]|\{[^{}]*\})*\}", "", body)

    depth = 0
    i = 0
    while i < len(body_nv):
        ch = body_nv[i]
        if ch == "\\" and i + 1 < len(body_nv):
            i += 2
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                problems.append("花括号提前闭合（位置字符 %d）" % i)
                depth = 0
        i += 1
    if depth != 0:
        problems.append("花括号不平衡，剩余深度 %d" % depth)

    # $ balance ignoring \$
    dollar = len(re.findall(r"(?<!\\)\$", body_nv))
    if dollar % 2:
        problems.append("$ 个数为奇数（%d）" % dollar)

    # environments
    stack = []
    for m in re.finditer(r"\\(begin|end)\{([A-Za-z*]+)\}", body_nv):
        kind, name = m.group(1), m.group(2)
        if kind == "begin":
            stack.append(name)
        else:
            if not stack:
                problems.append("多余的 \\end{%s}" % name)
            elif stack[-1] != name:
                problems.append("环境不匹配：期望 \\end{%s}，实际 \\end{%s}" % (stack[-1], name))
                stack.pop()
            else:
                stack.pop()
    for name in stack:
        problems.append("未闭合环境 \\begin{%s}" % name)

    notes = len(re.findall(r"\\transnote\{", body_nv))
    print("file: %s" % path)
    print("transnote 条数: %d" % notes)
    print("环境/花括号/$ 检查完成")
    if problems:
        print("发现 %d 个问题：" % len(problems))
        for p in problems:
            print("  - " + p)
        return 1
    print("OK")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
