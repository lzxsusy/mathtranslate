# -*- coding: utf-8 -*-
"""Assemble the delivery folder on the Desktop."""
import os, shutil, sys

PROJ = r"<本地路径>"
REVIEW = r"<本地路径>"
FINAL = r"<本地路径>"
ORIG = r"<本地路径>"
OUT = r"<本地路径>"

SRC_EXCLUDE = {"build", "review", ".git"}
SRC_EXCLUDE_FILES = {"build_split_check.log", "main.bbl", "main.aux", "main.log", "main.pdf"}

if os.path.isdir(OUT):
    print("delivery folder exists, removing:", OUT)
    shutil.rmtree(OUT)
os.makedirs(OUT)

# 1. PDF
shutil.copy2(os.path.join(PROJ, "build", "main.pdf"),
             os.path.join(OUT, "Dirichlet膜与镜像对称（校订版）.pdf"))

# 2. report
shutil.copy2(os.path.join(FINAL, "校订报告.md"), os.path.join(OUT, "校订报告.md"))

# 3. source tree
src = os.path.join(OUT, "源码")
os.makedirs(src)
for name in sorted(os.listdir(PROJ)):
    if name in SRC_EXCLUDE or name in SRC_EXCLUDE_FILES:
        continue
    p = os.path.join(PROJ, name)
    dst = os.path.join(src, name)
    if os.path.isdir(p):
        shutil.copytree(p, dst)
    else:
        shutil.copy2(p, dst)

# 4. original pdf
os.makedirs(os.path.join(OUT, "原文"))
shutil.copy2(ORIG, os.path.join(OUT, "原文", "Dirichlet Branes and Mirror Symmetry (Clay, 2008).pdf"))

# 5. review records
rec = os.path.join(OUT, "校对记录")
os.makedirs(rec)
for name in ["GUIDE.md", "term_audit.md", "verify_landed.md", "integrity_audit.md", "bib_orig.txt",
             "_summary.json", "_chunks.txt"]:
    p = os.path.join(REVIEW, name)
    if os.path.exists(p):
        shutil.copy2(p, os.path.join(rec, "校对标准与方法.md" if name == "GUIDE.md" else name))
for name in sorted(os.listdir(REVIEW)):
    if name.startswith("log_") and name.endswith(".md"):
        shutil.copy2(os.path.join(REVIEW, name), os.path.join(rec, name))

# 6. sizes
def dsize(path):
    total = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            total += os.path.getsize(os.path.join(root, f))
    return total

print("PDF      : %.1f MB" % (os.path.getsize(os.path.join(OUT, "Dirichlet膜与镜像对称（校订版）.pdf")) / 1e6))
for name in ["源码", "原文", "校对记录"]:
    print("%-9s: %.1f MB" % (name, dsize(os.path.join(OUT, name)) / 1e6))
print("total    : %.1f MB" % (dsize(OUT) / 1e6))
print("files    :", sum(len(f) for _, _, f in os.walk(OUT)))
