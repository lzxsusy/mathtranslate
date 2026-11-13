# -*- coding: utf-8 -*-
"""Extract section/subsection outline + figure caption locations."""
import sys, re, io
sys.stdout.reconfigure(encoding='utf-8')

ROOT = r"<本地路径>"
doc_txt = io.open(ROOT + r"\work\full.txt", encoding="utf-8").read()

# split by page markers
pages = re.split(r"===== PDF p\.(\d+) =====", doc_txt)
# pages[0] is preamble empty; then (num, text) pairs
out = []
for k in range(1, len(pages), 2):
    no = int(pages[k]); txt = pages[k+1]
    lines = [l.rstrip() for l in txt.splitlines()]
    # find candidate headings: line matching pure number or dotted number, next nonempty line title
    for idx, l in enumerate(lines):
        s = l.strip()
        if re.fullmatch(r"\d+(\.\d+)*", s):
            # next nonempty line
            j = idx+1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines):
                title = lines[j].strip()
                if 0 < len(title) < 80:
                    out.append((no, s, title))
for no, num, title in out:
    depth = num.count(".") + 1
    ind = "  " * (depth-1)
    print(f"p{no:02d}  {ind}{num}  {title}")
