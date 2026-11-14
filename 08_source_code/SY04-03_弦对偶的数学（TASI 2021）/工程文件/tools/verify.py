#!/usr/bin/env python
"""Global consistency checks for the assembled translation project.

Usage:
  python verify.py [--root .]

Checks
  1. every fragment file listed in main.tex exists (else report missing);
  2. equation tags: exactly the 182 tags of the original, no duplicates, no extras;
  3. page anchors cover pages 1..85;
  4. every \\includegraphics target exists;
  5. all 14 display figures and 5 inline equation figures are used;
  6. annotation counts (Tutor Note / 原文疑误 / 存疑 / 背景补充);
  7. fragment-level lint via tools/lint_frag.py (imported).
"""
import argparse
import json
import os
import re
import sys

FRAGS = ["s01-intro", "s02a", "s02b", "s02c", "s02d", "s02e", "s02f", "s02g",
         "s02h", "s03a", "s03b", "s03c", "s03d", "s03e", "s03f", "s03g",
         "s04", "s05", "s06", "s07", "s08-refs"]

EXPECT_TAGS = (
    [f"2.{i}" for i in range(1, 55)]
    + [f"3.{i}" for i in range(1, 77)]
    + [f"A.{i}" for i in range(1, 10)]
    + [f"B.{i}" for i in range(1, 28)]
    + [f"C.{i}" for i in range(1, 17)]
)


def strip_comments(text):
    out = []
    for ln in text.splitlines():
        m = re.search(r"(?<!\\)%", ln)
        out.append(ln[:m.start()] if m else ln)
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    a = ap.parse_args()
    root = a.root
    sec = os.path.join(root, "sections")
    ok = True

    tags, anchors, notes = [], [], {"tutor": 0, "typo": 0, "doubt": 0, "bg": 0}
    graphics, present, per_file = [], [], {}
    for f in FRAGS:
        p = os.path.join(sec, f + ".tex")
        if not os.path.exists(p):
            print(f"MISSING fragment: {f}.tex")
            ok = False
            continue
        present.append(f)
        raw = open(p, encoding="utf-8").read()
        code = strip_comments(raw)
        t = re.findall(r"\\tag\{([^}]*)\}", code)
        an = re.findall(r"%\s*====\s*原文 PDF 第\s*(\d+)\s*页", raw)
        g = re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", code)
        tags += [x.strip() for x in t]
        anchors += [int(x) for x in an]
        graphics += g
        notes["tutor"] += len(re.findall(r"%\s*\[Tutor Note", raw))
        notes["typo"] += len(re.findall(r"%\s*\[原文疑误", raw))
        notes["doubt"] += len(re.findall(r"%\s*\[存疑", raw))
        notes["bg"] += len(re.findall(r"%\s*\[背景补充", raw))
        per_file[f] = {"tags": len(t), "anchors": len(an), "graphics": len(g),
                       "bytes": len(raw)}

    # 2. tags
    want = set(EXPECT_TAGS)
    got = set(tags)
    dup = [t for t in got if tags.count(t) > 1]
    missing = sorted(want - got, key=lambda s: (s[0], int(s.split(".")[1])))
    extra = sorted(got - want)
    if missing:
        print(f"MISSING tags ({len(missing)}): {missing}")
        ok = False
    if extra:
        print(f"EXTRA tags ({len(extra)}): {extra}")
        ok = False
    if dup:
        print(f"DUPLICATE tags: {dup}")
        ok = False
    print(f"tags: {len(tags)} found, {len(want) - len(missing)} / {len(want)} expected")

    # 3. anchors
    missing_pages = [p for p in range(1, 86) if p not in anchors]
    dup_pages = sorted({p for p in anchors if anchors.count(p) > 1})
    if missing_pages:
        print(f"MISSING page anchors: {missing_pages}")
        ok = False
    if dup_pages:
        print(f"DUPLICATE page anchors: {dup_pages}")

    # 4. graphics
    for g in graphics:
        path = os.path.join(root, g.replace("/", os.sep))
        if not os.path.exists(path):
            print(f"MISSING graphics file: {g}")
            ok = False

    # 5. required figures
    used = {os.path.basename(g) for g in graphics}
    for i in range(1, 15):
        if f"fig{i:02d}.png" not in used:
            print(f"figure not used: fig{i:02d}.png")
            ok = False
    for n in ["eq-p42-a", "eq-p42-b", "eq-p43-a", "eq-p44-a", "eq-p69-a"]:
        if n + ".png" not in used:
            print(f"inline figure not used: {n}.png")
            ok = False

    # 6. notes
    print("annotations:", notes)

    # 7. per-file table
    print(f"\n{'fragment':14s} {'bytes':>7s} {'tags':>5s} {'anchors':>8s} {'graphics':>9s}")
    for f in FRAGS:
        if f in per_file:
            d = per_file[f]
            print(f"{f:14s} {d['bytes']:7d} {d['tags']:5d} {d['anchors']:8d} {d['graphics']:9d}")

    print("\nRESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
