# -*- coding: utf-8 -*-
"""检查已写 chunk 的结构问题（译注数、引号、环境配平、页码标记、可疑字符）。"""
import io
import os
import re

ROOT = r"<本地路径>"
SRC = os.path.join(ROOT, "src", "chunks")

env_re = re.compile(r"\\(begin|end)\{([^}]*)\}")

rows = []
for i in range(15):
    name = "ch%02d" % i
    path = os.path.join(SRC, name + ".tex")
    if not os.path.isfile(path):
        rows.append((name, "MISSING", 0, 0, 0, 0, 0, 0, ""))
        continue
    text = io.open(path, encoding="utf-8").read()
    lines = text.splitlines()
    stack = []
    bad = []
    for ln, line in enumerate(lines, 1):
        code = re.sub(r"(?<!\\)%.*", "", line)
        for m in env_re.finditer(code):
            kind, env = m.group(1), m.group(2)
            if kind == "begin":
                stack.append((env, ln))
            else:
                found = False
                for j in range(len(stack) - 1, -1, -1):
                    if stack[j][0] == env:
                        if j != len(stack) - 1:
                            bad.append("mismatch %s at %d" % (env, ln))
                        del stack[j:]
                        found = True
                        break
                if not found:
                    bad.append("stray \\end{%s} at %d" % (env, ln))
    unclosed = ["%s@%d" % (e, l) for e, l in stack if e not in ("document",)]
    q = text.count('"')
    pcount = len(re.findall(r"% \[原文 p\.(\d+)\]", text))
    yz = len(re.findall(r"<本地路径>", text))
    cb = len(re.findall(r"<本地路径>", text))
    kt = len(re.findall(r"<本地路径>", text))
    texcmd = len(re.findall(r"\\[a-zA-Z]+", text))
    rows.append((name, os.path.getsize(path), yz, cb, kt, q, pcount, len(text), ";".join(bad + unclosed)))

for r in rows:
    print("\t".join(str(x) for x in r))
