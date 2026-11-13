# -*- coding: utf-8 -*-
"""Material prep: render pages, split text, extract equation tags, figures."""
import sys, re, io, os, json
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz

SRC = r"<本地路径>).pdf"
ROOT = r"<本地路径>"
WORK = os.path.join(ROOT, "work")
for d in ("pages", "split", "figures", "src", "tmp"):
    os.makedirs(os.path.join(WORK, d), exist_ok=True)

doc = fitz.open(SRC)
N = len(doc)
print("pages", N, "size", doc[0].rect)

# ---------- 1. render pages ----------
for i, p in enumerate(doc):
    out = os.path.join(WORK, "pages", f"p{i+1:03d}.png")
    if not os.path.exists(out):
        pix = p.get_pixmap(dpi=200)
        pix.save(out)
print("rendered")

# ---------- 2. split text ----------
for i, p in enumerate(doc):
    t = p.get_text()
    lines = t.splitlines()
    head = []
    # section-ish first lines
    body = "\n".join(lines)
    txt = f"% PDF p.{i+1} (printed {i+1}) sections: []\n" + body
    with io.open(os.path.join(WORK, "split", f"p{i+1:03d}.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(txt)
with io.open(os.path.join(WORK, "full.txt"), "w", encoding="utf-8", newline="\n") as fh:
    for i, p in enumerate(doc):
        fh.write(f"\n\n===== PDF p.{i+1} =====\n")
        fh.write(p.get_text())
print("split done")

# ---------- 3. equation tags ----------
tagpat = re.compile(r"^\(\s*(\d+\.\d+)\s*\)$")
tags = []          # (tag, page)
uncertain = []
for i, p in enumerate(doc):
    W = p.rect.width
    cand = []
    d = p.get_text("dict")
    for b in d["blocks"]:
        for l in b.get("lines", []):
            # reconstruct line text
            for s in l["spans"]:
                st = s["text"].strip()
                m = tagpat.match(st)
                if m and s["bbox"][2] > W * 0.78:
                    cand.append((m.group(1), round(s["bbox"][2], 1)))
    # dedupe identical tag on same page (shadow artifacts)
    seen = []
    for tg, x in cand:
        if not seen or seen[-1][0] != tg:
            seen.append((tg, x))
    for tg, x in seen:
        tags.append((tg, i + 1))
print("tags found:", len(tags))

# check monotone sequence within each section group (tag major = section number)
from collections import defaultdict
bysect = defaultdict(list)
for tg, pg in tags:
    a, b = tg.split(".")
    bysect[a].append((int(b), pg))
report = []
for a, lst in sorted(bysect.items(), key=lambda kv: int(kv[0])):
    nums = [b for b, _ in lst]
    dups = [x for x in set(nums) if nums.count(x) > 1]
    missing = sorted(set(range(1, max(nums) + 1)) - set(nums)) if nums else []
    report.append(f"section {a}: n={len(nums)} max={max(nums) if nums else 0} dups={dups} missing={missing}")
    print(report[-1])

with io.open(os.path.join(WORK, "tags.txt"), "w", encoding="utf-8", newline="\n") as fh:
    for tg, pg in tags:
        fh.write(f"{tg}\tp{pg}\n")
with io.open(os.path.join(WORK, "tags_report.md"), "w", encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(report) + "\n")

# ---------- 4. per-page tag index ----------
bypage = defaultdict(list)
for tg, pg in tags:
    bypage[pg].append(tg)
lines = [f"p{pg:03d}: " + ", ".join(v) for pg, v in sorted(bypage.items())]
with io.open(os.path.join(WORK, "tags_bypage.txt"), "w", encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(lines) + "\n")
print("done")
