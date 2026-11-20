#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply review/*.json issue lists onto chapters/*.tex.

Each issue carries: line (in units/uXX.tex), quote, new, type, confidence.
Mapping: units/uXX.tex line 1 is the '% UNIT' header, line 2 == manifest start.
Usage:  python apply_review.py            # apply all, write report
        python apply_review.py --dry      # report only
"""
import json, os, sys, glob, collections

BASE = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE)
DRY = "--dry" in sys.argv

manifest = {m["unit"]: m for m in json.load(open("units/manifest.json", encoding="utf-8"))}

try:
    MANUAL_SKIP = {(x["unit"], x["quote"]) for x in json.load(open("manual_skip.json", encoding="utf-8"))}
except FileNotFoundError:
    MANUAL_SKIP = set()

cache = {}

def load(path):
    if path not in cache:
        with open(path, encoding="utf-8") as f:
            cache[path] = f.read().split("\n")
    return cache[path]

def save(path):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(cache[path]))

applied, unmatched, skipped = [], [], []
filtered = []
seen = set()

for jf in sorted(glob.glob("review/u*.json")):
    try:
        data = json.load(open(jf, encoding="utf-8"))
    except Exception as e:
        skipped.append((jf, "json-error", str(e)))
        continue
    unit = data.get("unit") or os.path.basename(jf)[:-5]
    m = manifest.get(unit)
    if not m:
        skipped.append((unit, "no-manifest", ""))
        continue
    path = m["file"]
    lines = load(path)
    start, end = m["start"], m["end"]
    for iss in data.get("issues", []):
        q = iss.get("quote", "")
        new = iss.get("new", "")
        typ = iss.get("type", "?")
        conf = iss.get("confidence", "?")
        # filters:
        #  - low confidence: not applied, kept in review_filtered.json
        #  - quotes containing 单值化: handled by global_fix.py uniformly (avoids 单值变换/单值性变换 split)
        if conf == "low":
            filtered.append({"unit": unit, "reason": "low-confidence", **iss})
            continue
        if "单值化" in q:
            filtered.append({"unit": unit, "reason": "global-fix-handles", **iss})
            continue
        if (unit, q) in MANUAL_SKIP:
            filtered.append({"unit": unit, "reason": "manual-skip", **iss})
            continue
        if not q or q not in "\n".join(lines[start - 1:end]) and q not in "\n".join(lines):
            unmatched.append((unit, iss.get("line"), typ, q[:60]))
            continue
        if q == new:
            skipped.append((unit, "quote==new", q[:40]))
            continue
        key = (path, q, new)
        if key in seen:
            skipped.append((unit, "dup", q[:40]))
            continue
        # candidate window first, then whole file
        cand = list(range(start - 1, end))
        idx = next((i for i in cand if q in lines[i]), None)
        if idx is None:
            idx = next((i for i, s in enumerate(lines) if q in lines[i]), None)
        if idx is None:
            unmatched.append((unit, iss.get("line"), typ, q[:60]))
            continue
        if not DRY:
            lines[idx] = lines[idx].replace(q, new, 1)
        seen.add(key)
        applied.append({"unit": unit, "file": path, "line": idx + 1, "type": typ,
                        "conf": conf, "quote": q, "new": new,
                        "problem": iss.get("problem", ""), "page": iss.get("page")})

if not DRY:
    for p in {a["file"] for a in applied}:
        save(p)

cnt = collections.Counter(a["type"] for a in applied)
conf = collections.Counter(a["conf"] for a in applied)
print(f"applied={len(applied)} unmatched={len(unmatched)} skipped={len(skipped)} filtered={len(filtered)}")
print("types:", dict(cnt))
print("conf:", dict(conf))
if unmatched:
    print("\n-- unmatched (first 40) --")
    for u in unmatched[:40]:
        print(u)
json.dump(applied, open("review_applied.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(filtered, open("review_filtered.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(unmatched, open("review_unmatched.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
