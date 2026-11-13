# -*- coding: utf-8 -*-
"""Sanitize split/*.txt and full.txt: strip control chars from the PDF text layer."""
import glob, os, re

ROOT = r"<本地路径>"
BAD = re.compile(r"[\x00-\x08\x0b-\x1f]")

for f in sorted(glob.glob(os.path.join(ROOT, "split", "*.txt"))):
    t = open(f, encoding="utf-8").read()
    # keep first line header, sanitize body
    line1, _, body = t.partition("\n")
    body = BAD.sub("", body)
    open(f, "w", encoding="utf-8", newline="\n").write(line1 + "\n" + body)

f = os.path.join(ROOT, "full.txt")
t = open(f, encoding="utf-8").read()
open(f, "w", encoding="utf-8", newline="\n").write(BAD.sub("", t))
print("sanitized")
