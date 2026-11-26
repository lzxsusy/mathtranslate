#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Compact single-card dump for lead review: python show_card.py <id-or-slug> [...]"""
import json
import sys
import glob
import os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))


def find(arg):
    hits = [p for p in glob.glob(os.path.join(REPO, "datasets", "glc", "cards",
                                              "**", "*.json"), recursive=True)
            if os.path.basename(p)[:-5] == arg or arg in p.replace("\\", "/")]
    return hits


def dump(path, full=False):
    c = json.load(open(path, encoding="utf-8"))
    print("=" * 78)
    print("%s  |  %s  |  track=%s  status=%s  type=%s"
          % (c["id"], c["title"], c.get("track"), c.get("status"), c.get("type")))
    print("aliases:", c.get("aliases"))
    print("\n[summary] %s" % c["summary"])
    print("\n[question] %s" % c["question"])
    print("\n[definition.text] %s" % c["definition"]["text"])
    print("\n[definition.notation] %s" % c["definition"]["notation"])
    for i, k in enumerate(c["key_points"]):
        print("\n[key_points %d] %s" % (i, k))
    for i, f in enumerate(c["formulas"]):
        print("\n[formulas %d] %s" % (i, f))
    for i, t in enumerate(c["theorems"]):
        print("\n[theorems %d] name=%s" % (i, t.get("name")))
        print("  statement: %s" % t.get("statement"))
        pr = t.get("proof", {})
        print("  proof.status=%s steps=%s gap_note=%s"
              % (pr.get("status"), pr.get("steps"), pr.get("gap_note")))
        print("  source: %s" % t.get("source"))
    for i, p in enumerate(c.get("pitfalls", [])):
        print("\n[pitfalls %d] %s" % (i, p))
    print("\n[related] %s" % c.get("related"))
    for i, s in enumerate(c["sources"]):
        print("\n[sources %d] book=%s\n  section=%s\n  pages=%s pdf_pages=%s\n  anchor=%s"
              % (i, s["book"], s["section"], s["pages"], s["pdf_pages"], s["anchor"]))
    print("\n[rights] %s" % c.get("rights"))
    v = c.get("verification", {})
    print("[verification] status=%s checked_on=%s checks=%s"
          % (v.get("status"), v.get("checked_on"), v.get("checks")))
    if full:
        print("\n[json]\n" + json.dumps(c, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    for a in sys.argv[1:]:
        hits = find(a)
        if not hits:
            print("NOT FOUND:", a)
            continue
        for h in hits:
            dump(h, full=False)
