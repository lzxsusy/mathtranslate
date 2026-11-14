# -*- coding: utf-8 -*-
"""Compare equation numbers present in OCR text with \\tag{...} in translations.

Usage: python compare_eq.py [lecture]
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE_OF = {}


def load_pages():
    for n in range(1, 20):
        files = glob.glob(os.path.join(ROOT, "sections", f"lec{n:02d}_p*.tex"))
        files = sorted(files, key=lambda f: int(re.search(r"_p(\d+)", f).group(1)))
        if n == 9:
            files = [os.path.join(ROOT, "sections", "lec09.tex")]
        pages = []
        for f in files:
            src = open(f, encoding="utf-8").read()
            pages.append((f, [int(x) for x in re.findall(r"%\s*=====\s*原文\s*p\.(\d+)", src)]))
        PAGE_OF[n] = pages


def main():
    load_pages()
    target = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for n in range(1, 20):
        if target and n != target:
            continue
        if n not in PAGE_OF:
            continue
        pages = []
        for f, ps in PAGE_OF[n]:
            pages += ps
        if not pages:
            continue
        lo, hi = min(pages), max(pages)
        orig = set()
        for p in range(lo, hi + 1):
            txt = open(os.path.join(ROOT, "text", f"p{p:03d}.txt"), encoding="utf-8").read()
            for m in re.finditer(r"\((\d+)\s*\.\s*(\d+)\)", txt):
                a, b = int(m.group(1)), int(m.group(2))
                if a == n:
                    orig.add((a, b))
        tags = set()
        for f, _ in PAGE_OF[n]:
            src = open(f, encoding="utf-8").read()
            for m in re.finditer(r"\\tag\{(\d+)\s*\.\s*(\d+)\}", src):
                tags.add((int(m.group(1)), int(m.group(2))))
        missing = sorted(orig - tags)
        extra = sorted(tags - orig)
        print(f"L{n:02d}: OCR numbers {len(orig)}, tags {len(tags)}; "
              f"missing {missing[:12]}{'...' if len(missing) > 12 else ''}; "
              f"extra {extra[:8]}{'...' if len(extra) > 8 else ''}")


if __name__ == "__main__":
    main()
