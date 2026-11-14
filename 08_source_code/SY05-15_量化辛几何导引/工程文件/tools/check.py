#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""静态检查：覆盖页、LaTeX 结构、图片、编号、批注、要点等。

用法（工作区根目录）：
  python qsg/tools/check.py ch05
  python qsg/tools/check.py all
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

QSG = Path(__file__).resolve().parent.parent
TEX = QSG / "tex"
RANGES = json.loads((QSG / "tools" / "ranges.json").read_text(encoding="utf-8"))

FORBIDDEN = [r"\usepackage", r"\documentclass", r"\begin{document}", r"\newcommand",
             r"\renewcommand", r"\tableofcontents", r"\bibliography{"]
UNICODE_MATH = set("×÷−≥≤→←↔⊗⊕≅≃≈∞√∑∏∫∂∇αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΦΨΩ")


def strip_comments(text: str) -> str:
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


def lint(path: Path, tagbag):
    raw = path.read_text(encoding="utf-8")
    body = strip_comments(raw)
    probs = []

    # braces
    depth = 0
    for ch in body:
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                probs.append("花括号多余 '}'")
                depth = 0
    if depth:
        probs.append(f"花括号未闭合（{depth}）")

    # environments
    stack = []
    for m in re.finditer(r"\\(begin|end)\{([^}]+)\}", body):
        kind, env = m.group(1), m.group(2)
        ln = body[:m.start()].count("\n") + 1
        if kind == "begin":
            stack.append((env, ln))
        else:
            if not stack or stack[-1][0] != env:
                probs.append(f"L{ln}: \\end{{{env}}} 不匹配")
                if stack:
                    stack.pop()
            else:
                stack.pop()
    for env, ln in stack:
        probs.append(f"L{ln}: \\begin{{{env}}} 未闭合")

    # $ parity
    dollars = len(re.findall(r"(?<!\\)\$", body))
    if dollars % 2:
        probs.append("$ 数量为奇数（数学模式未闭合）")
    if len(re.findall(r"\\left", body)) != len(re.findall(r"\\right", body)):
        probs.append("\\left/\\right 不配对")

    for f in FORBIDDEN:
        if f in body:
            probs.append(f"出现禁止命令 {f}")

    bad = [c for c in body if c in UNICODE_MATH]
    if bad:
        probs.append(f"Unicode 数学字符 {Counter(bad).most_common(5)}")

    if re.search(r"\\mathbb\s*\{\s*1\s*\}", body):
        probs.append("使用 \\mathbb{1}，请改为 \\mathbf{1}")

    for pat in ("TODO", "待补", "???", "XXX"):
        if pat in body:
            probs.append(f"残留占位符 {pat}")

    figs = re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", body)
    missing = [f for f in figs if not (QSG / f).exists()]
    if missing:
        probs.append(f"图片文件缺失 {missing}")

    tags = re.findall(r"\\tag\*?\{([^}]+)\}", body)
    for t in tags:
        tagbag[t].append(path.name)

    # suspicious untranslated long ASCII lines (allow pure LaTeX/math/reference lines)
    eng = []
    for i, line in enumerate(body.splitlines(), 1):
        s = line.strip()
        if not s or "\\" in s or s.startswith("$"):
            continue
        if len(re.findall(r"\b[A-Za-z]{3,}\b", s)) >= 8 and not any(
                "\u4e00" <= ch <= "\u9fff" for ch in s):
            eng.append(f"L{i}")
    if eng:
        probs.append(f"疑似未译英文行 {eng[:6]}（共 {len(eng)}）")

    return raw, probs, len(figs), len(tags)


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else "all"
    keys = [k for k in RANGES if k not in ("front", "bib", "index", "missing_appendix")]
    if arg != "all":
        keys = [k for k in keys if k == arg] or [k for k in keys if k.startswith(arg)]
        if not keys:
            sys.exit(f"未知前缀: {arg}")

    all_bad = False
    for key in keys:
        info = RANGES[key]
        lo, hi = info["pdf"]
        prefix = info.get("prefix", key)
        files = sorted(TEX.glob(f"{prefix}-*.tex"))
        print(f"\n=== {key}  PDF p{lo}-p{hi}  文件 {len(files)} 个 ===")
        if not files:
            print("  [缺少全部文件]")
            all_bad = True
            continue

        covered = set()
        notes = takes = secs = figs = 0
        tagbag = defaultdict(list)
        for f in files:
            raw, probs, nfig, ntag = lint(f, tagbag)
            body = strip_comments(raw)
            for m in re.finditer(r"%\s*>>>\s*p(\d+)", raw):
                covered.add(int(m.group(1)))
            notes += len(re.findall(r"%\s*\[Tutor Note", raw))
            takes += len(re.findall(r"\\begin\{keytakeaways\}", body))
            secs += len(re.findall(r"\\section\{", body))
            figs += nfig
            if probs:
                all_bad = True
                print(f"  [!] {f.name}")
                for p in probs:
                    print(f"      - {p}")

        expected = set(range(lo, hi + 1))
        missing = sorted(expected - covered)
        extra = sorted(p for p in covered if p < lo or p > hi)
        if missing:
            all_bad = True
            print(f"  [缺页] {missing}")
        if extra:
            print(f"  [越界页标记] {extra}")
        print(f"  覆盖 {len(covered & expected)}/{hi - lo + 1} 页 | "
              f"节 {secs} | 要点 {takes} | 批注 {notes} | 图 {figs} | 公式编号 {sum(len(v) for v in tagbag.values())}")
        if takes < secs:
            print(f"  [提示] 有 {secs - takes} 个 \\section 缺 keytakeaways")
        dup = {t: v for t, v in tagbag.items() if len(v) > 1}
        if dup:
            print(f"  [重复 tag] {dup}")

    print("\n==== 结论 ====")
    print("有问题的项：", "见上" if all_bad else "无")
    return 1 if all_bad else 0


if __name__ == "__main__":
    sys.exit(main())
