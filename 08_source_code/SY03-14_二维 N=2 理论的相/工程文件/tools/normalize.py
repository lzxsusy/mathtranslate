#!/usr/bin/env python
"""Book-wide typographic unification (run once, after all review passes).

Rules (decided by Lead, faithful to the original typesetting):
  * \\mathbb{CP} -> \\mathbf{CP}   (Witten prints CP in bold upright)
  * \\mathbb{P}  -> \\mathbf{CP}   (all occurrences denote CP^{n-1}, CP^5, ...)
  * \\mathbb{WCP} -> \\mathbf{WCP}
Comments are also normalised (harmless, keeps source coherent).

Usage: python tools/normalize.py [--check]
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECT = os.path.join(ROOT, "sections")

RULES = [
    (r"\\mathbb\{CP\}", r"\\mathbf{CP}"),
    (r"\\mathbb\{WCP\}", r"\\mathbf{WCP}"),
    (r"\\mathbb\{P\}", r"\\mathbf{CP}"),
]


def main():
    check = "--check" in sys.argv
    changes = {}
    for path in sorted(glob.glob(os.path.join(SECT, "*.tex"))):
        raw = open(path, encoding="utf-8").read()
        new = raw
        n = 0
        for pat, rep in RULES:
            new, k = re.subn(pat, rep, new)
            n += k
        if n:
            changes[os.path.basename(path)] = n
            if not check:
                open(path, "w", encoding="utf-8", newline="\n").write(new)
    print(("would change: " if check else "normalised: ") +
          (", ".join(f"{k}({v})" for k, v in changes.items()) if changes else "none"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
