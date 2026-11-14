# -*- coding: utf-8 -*-
"""Coverage / consistency audit for the translated book.

Usage: python audit.py
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLANK = {40, 64, 80, 106, 128, 144, 162, 208, 246, 284, 292}


def build_order():
    order = ["intro"]
    for n in range(1, 20):
        if n == 9:
            order.append("lec09")
            continue
        parts = sorted(glob.glob(os.path.join(ROOT, "sections", "lec%02d_p*.tex" % n)))
        order += ["lec%02d_p%d" % (n, k) for k in range(1, len(parts) + 1)]
    order += ["exo_p1", "sol_p1", "sol_p2", "glossary"]
    return order


def main():
    order = build_order()
    files = {os.path.basename(f)[:-4]: f
             for f in glob.glob(os.path.join(ROOT, "sections", "*.tex"))}
    print("section files present:", len(files))
    missing_files = [n for n in order if n not in files]
    if missing_files:
        print("MISSING FILES:", missing_files)

    covered = {}
    total_eq = total_fig = total_notes = 0
    problems = []
    defines = {}
    for name in order:
        if name not in files:
            continue
        src = open(files[name], encoding="utf-8").read()
        pages = [int(x) for x in re.findall(r"%\s*=====\s*原文\s*p\.(\d+)", src)]
        for p in pages:
            covered.setdefault(p, []).append(name)
        total_eq += len(re.findall(r"\\tag\{", src))
        figs = re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", src)
        total_fig += len(figs)
        for f in figs:
            if not os.path.exists(os.path.join(ROOT, f)):
                problems.append("%s: missing figure %s" % (name, f))
        total_notes += len(re.findall(r"%\s*\[Tutor Note:", src))
        for m in re.findall(r"\\newcommand\{\\([A-Za-z@]+)\}", src):
            defines.setdefault(m, []).append(name)
        if re.search(r"\\(documentclass|usepackage|begin\{document\}|end\{document\})", src):
            problems.append("%s: contains preamble/document commands" % name)
        if re.search(r"\\section\{", src) and name not in ["lec%02d_p1" % n for n in range(1, 20)] + ["lec09"]:
            problems.append("%s: unexpected section" % name)

    expected = [p for p in range(3, 307) if p not in BLANK]
    uncovered = [p for p in expected if p not in covered]
    dup = {p: v for p, v in covered.items() if len(v) > 1}
    print("pages expected %d, covered %d, uncovered %d" % (
        len(expected), len(set(covered) & set(expected)), len(uncovered)))
    if uncovered:
        rs = []
        s = prev = uncovered[0]
        for p in uncovered[1:]:
            if p == prev + 1:
                prev = p
            else:
                rs.append((s, prev))
                s = prev = p
        rs.append((s, prev))
        print("UNCOVERED:", ", ".join(("%d" % a) if a == b else ("%d-%d" % (a, b)) for a, b in rs))
    if dup:
        print("DUPLICATE coverage:", {k: v for k, v in list(dup.items())[:10]})
        problems.append("%d pages covered twice" % len(dup))
    print("equations tagged: %d, figures: %d, tutor notes: %d" % (
        total_eq, total_fig, total_notes))
    for k, v in defines.items():
        if len(v) > 1:
            problems.append("newcommand \\%s redefined in %s" % (k, v))
    print("problems:", len(problems))
    for p in problems[:40]:
        print("  -", p)
    return 1 if (uncovered or missing_files or problems) else 0


if __name__ == "__main__":
    sys.exit(main())
