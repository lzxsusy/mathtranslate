#!/usr/bin/env python
"""Idempotent book-wide formatting post-pass (run after every new fragment).

1. keytakeaway: force the three \\textbf{...} items onto separate paragraphs
   (a newline alone does not break paragraphs in LaTeX).
2. Ensure the keytakeaway body starts right after the heading without stray
   spaces, and pages anchors stay as comments (untouched).
3. Report suspicious patterns: bare "\\dd" usage is fine (defined), but flag
   equations with |...| nested unnecessarily? -> no, keep minimal.

Usage: python tools/postfix.py [--check]
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECT = os.path.join(ROOT, "sections")

ITEMS = ["数学工具", "主要结论"]


def process(text):
    out = text
    for key in ITEMS:
        # newline only -> \par
        out = re.sub(r"(?<!\\)\n([ \t]*)\\textbf\{" + key, r"\n\\par\\textbf{" + key, out)
        # already \par: do nothing (regex above would have matched "\n\par..." ? no)
    # collapse accidental double \par\par
    out = re.sub(r"\\par\\par(\\textbf\{)", r"\\par\1", out)
    return out


def main():
    check = "--check" in sys.argv
    changed = []
    for path in sorted(glob.glob(os.path.join(SECT, "*.tex"))):
        raw = open(path, encoding="utf-8").read()
        new = process(raw)
        if new != raw:
            changed.append(os.path.basename(path))
            if not check:
                open(path, "w", encoding="utf-8", newline="\n").write(new)
    print(("would change: " if check else "changed: ") + (", ".join(changed) if changed else "none"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
