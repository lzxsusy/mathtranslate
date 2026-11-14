# -*- coding: utf-8 -*-
"""Static QC for generated LaTeX section files (v2).

Usage: python qc.py [file ...]
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def strip_comments(s):
    out = []
    for line in s.splitlines(True):
        m = re.search(r"(?<!\\)%", line)
        out.append(line if m is None else line[: m.start()] + "\n")
    return "".join(out)


def strip_math(body):
    body = re.sub(r"\\\[.*?\\\]", " ", body, flags=re.S)
    body = re.sub(r"\$\$.*?\$\$", " ", body, flags=re.S)
    body = re.sub(r"(?<!\\)\$.*?(?<!\\)\$", " ", body, flags=re.S)
    body = re.sub(r"\\begin\{(equation|align|gather|multline|eqnarray)\*?\}.*?"
                  r"\\end\{\1\*?\}", " ", body, flags=re.S)
    return body


def check(path):
    src = open(path, encoding="utf-8").read()
    body = strip_comments(src)
    issues = []

    envs = re.findall(r"\\(begin|end)\{([^}]+)\}", body)
    stack = []
    for kind, name in envs:
        if kind == "begin":
            stack.append(name)
        else:
            if not stack:
                issues.append("unexpected end{%s}" % name)
            elif stack[-1] != name:
                issues.append("mismatch: begin{%s} vs end{%s}" % (stack[-1], name))
                stack.pop()
            else:
                stack.pop()
    if stack:
        issues.append("unclosed env: " + ", ".join(stack))

    depth = 0
    for ch in body:
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                issues.append("negative brace depth")
                depth = 0
    if depth:
        issues.append("brace depth ends at %d" % depth)

    dollars = len(re.findall(r"(?<!\\)\$", body))
    if dollars % 2:
        issues.append("odd number of $ (%d)" % dollars)

    opens = len(re.findall(r"(?<!\\)\\\[", body))
    closes = len(re.findall(r"(?<!\\)\\\]", body))
    if opens != closes:
        issues.append("display math [ %d vs ] %d" % (opens, closes))

    lefts = len(re.findall(r"\\left[^a-zA-Z]", body)) + len(re.findall(r"\\left$", body, re.M))
    rights = len(re.findall(r"\\right[^a-zA-Z]", body)) + len(re.findall(r"\\right$", body, re.M))
    if lefts != rights:
        issues.append("left %d vs right %d" % (lefts, rights))

    tags = re.findall(r"\\tag\{([^}]*)\}", body)
    eqs = len(re.findall(r"\\begin\{equation\}", body)) + len(
        re.findall(r"\\begin\{align\}", body)
    )
    pages = [int(x) for x in re.findall(r"%\s*=====\s*原文\s*p\.(\d+)", src)]
    figs = re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", body)
    missing = [f for f in figs if not os.path.exists(os.path.join(ROOT, f))]
    ocr = [t for t in ["¢", "£", "\ufffd", "IR2", "VJ", "8µ", "rnatrix"] if t in body]

    prose = strip_math(body)
    cjk = len(re.findall(r"[\u4e00-\u9fff]", prose))
    latin_words = len(re.findall(r"[A-Za-z]{3,}", prose))
    english = []
    for line in prose.splitlines():
        if re.search(r"\\[a-zA-Z]+", line):
            continue
        words = re.findall(r"[A-Za-z][A-Za-z'\-]{2,}", line)
        if len(words) > 14:
            english.append(line.strip()[:70])

    stats = dict(chars=len(src), cjk=cjk, latin=latin_words, equations=eqs,
                 tags=len(tags), figures=len(figs), pages=pages)
    return issues, missing, ocr, english, stats


def main():
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, "sections", "*.tex")))
    bad = 0
    for f in files:
        issues, missing, ocr, english, st = check(f)
        name = os.path.basename(f)
        ratio = st["cjk"] / max(1, st["cjk"] + st["latin"])
        print("\n== %s: %d chars, CJK %d (%.0f%%), %d eqs, %d tags, %d figs" % (
            name, st["chars"], st["cjk"], ratio * 100, st["equations"], st["tags"], st["figures"]))
        if st["pages"]:
            print("   pages: %d -> %d (%d)" % (st["pages"][0], st["pages"][-1], len(st["pages"])))
        for i in issues:
            print("   ISSUE:", i)
        for m in missing:
            print("   MISSING FIG:", m)
        if ocr:
            print("   OCR LEAK:", ocr)
        if english:
            print("   ENGLISH LINES: %d e.g. %s" % (len(english), english[:2]))
        if ratio < 0.35:
            print("   LOW CHINESE RATIO")
        if issues or missing:
            bad += 1
    print("\nchecked %d files, %d with hard issues" % (len(files), bad))


if __name__ == "__main__":
    main()
