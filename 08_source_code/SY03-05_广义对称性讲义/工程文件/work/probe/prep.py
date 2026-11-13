# -*- coding: utf-8 -*-
"""Material prep for 2307.07547v2: pages, split text, tags, refs detection."""
import sys, re, io, os, json
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz
from collections import defaultdict

ROOT = r"<本地路径>"
PDF = os.path.join(ROOT, "2307.07547v2.pdf")
WORK = os.path.join(ROOT, "work")
for d in ("pages", "split", "figures", "src", "tmp"):
    os.makedirs(os.path.join(WORK, d), exist_ok=True)

doc = fitz.open(PDF)
N = len(doc)
print("pages", N, "size", doc[0].rect)

# ---------- 1. render pages ----------
for i, p in enumerate(doc):
    out = os.path.join(WORK, "pages", f"p{i+1:03d}.png")
    if not os.path.exists(out):
        p.get_pixmap(dpi=200).save(out)
print("rendered")

# ---------- 2. split text ----------
for i, p in enumerate(doc):
    txt = f"% PDF p.{i+1} (printed {i+1}) sections: []\n" + p.get_text()
    with io.open(os.path.join(WORK, "split", f"p{i+1:03d}.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(txt)
with io.open(os.path.join(WORK, "full.txt"), "w", encoding="utf-8", newline="\n") as fh:
    for i, p in enumerate(doc):
        fh.write(f"\n\n===== PDF p.{i+1} =====\n")
        fh.write(p.get_text())
print("split done")

# ---------- 3. equation tags (span algorithm) ----------
tagpat = re.compile(r"^\(\s*(\d+\.\d+)\s*\)$")
tags = []
for i, p in enumerate(doc):
    W = p.rect.width
    d = p.get_text("dict")
    cand = []
    for b in d["blocks"]:
        for l in b.get("lines", []):
            txt = "".join(s["text"] for s in l["spans"]).strip()
            x1 = max((s["bbox"][2] for s in l["spans"]), default=0)
            m = tagpat.match(txt)
            if m and x1 > W * 0.78:
                cand.append((m.group(1), round(x1, 1)))
    seen = []
    for tg, x in cand:
        if not seen or seen[-1][0] != tg:
            seen.append((tg, x))
    for tg, x in seen:
        tags.append((tg, i + 1))
print("tags found:", len(tags))

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

bypage = defaultdict(list)
for tg, pg in tags:
    bypage[pg].append(tg)
lines = [f"p{pg:03d}: " + ", ".join(v) for pg, v in sorted(bypage.items())]
with io.open(os.path.join(WORK, "tags_bypage.txt"), "w", encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(lines) + "\n")
print("done")
