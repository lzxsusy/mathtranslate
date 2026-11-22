#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rough completeness checker for translated chunks.
Flags lines that look like untranslated English prose and structural issues.
Not a substitute for reading; used as a smoke test.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
CH = ROOT / "源码" / "chunks"
CJK = re.compile(r"[\u4e00-\u9fff]")
WORD = re.compile(r"[A-Za-z][A-Za-z'\-]{1,}")

def strip_math(s: str) -> str:
    s = re.sub(r"\$[^$]*\$", "", s)
    s = re.sub(r"\\\[.*?\\\]", "", s, flags=re.S)
    s = re.sub(r"\\\([^)]*\\\)", "", s)
    return s

def strip_cmds(s: str) -> str:
    # remove command names but keep their brace content (which may be prose)
    s = re.sub(r"\\[A-Za-z@]+\*?", "", s)
    s = re.sub(r"[{}$&_^~]", " ", s)
    return s

def check(path: pathlib.Path):
    text = path.read_text(encoding="utf-8")
    problems = []
    # structural
    nb, ne = text.count("\\begin{"), text.count("\\end{")
    if nb != ne:
        problems.append(f"begin/end mismatch: {nb} vs {ne}")
    if text.count("{") != text.count("}"):
        problems.append(f"brace mismatch: {text.count('{')} vs {text.count('}')}")
    # sections with no Chinese
    for m in re.finditer(r"\\(?:sub)*section\{([^{}]*)\}", text):
        title = m.group(1)
        if not CJK.search(title):
            problems.append(f"section title not Chinese: {title[:60]}")
    # english prose lines
    for i, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("%"):
            continue
        s = strip_cmds(strip_math(line))
        words = WORD.findall(s)
        if len(words) >= 8 and not CJK.search(line):
            problems.append(f"L{i}: possible untranslated prose ({len(words)} words): {line.strip()[:90]}")
    nzy = len(re.findall(r"\\zy\{", text))
    nyz = len(re.findall(r"\\begin\{yizhu\}", text))
    return problems, nzy, nyz

def main():
    total_bad = 0
    for path in sorted(CH.glob("ch*.tex")):
        problems, nzy, nyz = check(path)
        status = "OK" if not problems else f"{len(problems)} flag(s)"
        print(f"{path.name}: {status}  (zy={nzy}, yizhu={nyz})")
        for p in problems[:12]:
            print("   -", p)
        if len(problems) > 12:
            print(f"   ... {len(problems)-12} more")
        total_bad += len(problems)
    print(f"\nTOTAL flags: {total_bad}")
    return 1 if total_bad else 0

if __name__ == "__main__":
    sys.exit(main())
