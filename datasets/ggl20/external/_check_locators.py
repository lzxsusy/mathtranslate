# -*- coding: utf-8 -*-
"""自检：locator / anchor 的页码与式号是否真存在（verify_pages 不查这些）。"""
import json, glob, os, re, sys

here = os.path.dirname(os.path.abspath(__file__))
pkg = os.path.dirname(here)
root = os.path.dirname(os.path.dirname(pkg))
cards = sorted(glob.glob(os.path.join(pkg, "cards", "concepts", "*.json")) +
               glob.glob(os.path.join(pkg, "cards", "derivations", "*.json")))
pages = {}
for i in range(1, 23):
    with open(os.path.join(root, "txt", "20", "p%03d.txt" % i), encoding="utf-8") as f:
        pages[i] = f.read()

bad = 0
seen = 0
for c in cards:
    d = json.load(open(c, encoding="utf-8"))
    locs = []
    for s in d.get("steps", []):
        locs.append(("step %s" % s.get("no"), s.get("locator", "")))
    for i, s in enumerate(d.get("sources", [])):
        locs.append(("source %d" % i, s.get("anchor", "")))
    for tag, loc in locs:
        seen += 1
        m = re.search(r"\bp\.(\d+)", loc)
        if not m:
            print("NO PAGE", os.path.basename(c), tag, loc); bad += 1; continue
        n = int(m.group(1))
        if not (1 <= n <= 22):
            print("PAGE RANGE", os.path.basename(c), tag, loc); bad += 1; continue
        for eq in re.findall(r"eq \((\d+)\)", loc):
            if ("(%s)" % eq) not in pages[n]:
                print("EQ MISSING", os.path.basename(c), tag, loc); bad += 1
print("locators checked:", seen, "problems:", bad)
sys.exit(1 if bad else 0)
