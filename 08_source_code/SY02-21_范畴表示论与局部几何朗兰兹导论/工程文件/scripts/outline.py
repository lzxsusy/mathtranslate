# -*- coding: utf-8 -*-
"""生成原文结构大纲：节/小节/小节内编号环境（定理、例、注）的首句。
输出 work/outline.txt，供通读与结果清单使用。
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "work", "原文", "samplez.tex")
OUT = os.path.join(ROOT, "work", "outline.txt")

ENVS = ("theo", "theo*", "lem", "lemma", "cor", "pro", "conj", "proofw",
        "defn", "re", "remark", "example", "ex")

def clean(s):
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = re.sub(r"\\cite\{[^}]*\}", "[cit]", s)
    s = re.sub(r"\$[^$]*\$", "M", s)
    s = s.replace("\n", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()

def main():
    lines = open(SRC, encoding="utf-8", errors="replace").read().splitlines()
    out = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        m = re.match(r"\s*\\\\?(?:sub)*section", line)
        if re.match(r"\s*\\(section|subsection|subsubsection)\b", line):
            kind = re.match(r"\s*\\(section|subsection|subsubsection)\b", line).group(1)
            title = re.search(r"\\(?:section|subsection|subsubsection)\*?\{((?:[^{}]|\{[^{}]*\})*)\}",
                              line + (lines[i + 1] if i + 1 < n else ""))
            t = title.group(1) if title else ""
            if t.strip() or kind != "subsubsection":
                out.append("%-14s L%-5d %s %s" % (kind, i + 1, "=" * 3, clean(t)))
            i += 1
            continue
        m = re.match(r"\s*\\begin\{(" + "|".join(re.escape(e) for e in ENVS) + r")\}", line)
        if m:
            env = m.group(1)
            # 收集环境开头 600 字符
            buf = [line]
            j = i
            while j < n and ("\\end{%s}" % env) not in lines[j] and j - i < 8:
                j += 1
                if j < n:
                    buf.append(lines[j])
            body = clean(" ".join(buf))
            body = re.sub(r"^\\begin\{[^}]*\}", "", body)
            body = body.replace("\\end{%s}" % env, "")
            out.append("  [%s] L%-5d %s" % (env, i + 1, body[:150]))
            i += 1
            continue
        i += 1
    open(OUT, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("lines:", len(out), "->", OUT)

if __name__ == "__main__":
    main()
