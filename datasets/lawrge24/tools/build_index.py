#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""cards/{concepts,derivations}/*.json -> index.jsonl"""
import glob
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ORDER = {"O": 0, "A": 1, "B": 2, "C": 3, "D": 4, "E": 5}


def main():
    rows = []
    for kind in ("concepts", "derivations"):
        for p in glob.glob(os.path.join(ROOT, "cards", kind, "*.json")):
            with io.open(p, encoding="utf-8") as f:
                c = json.load(f)
            rows.append({
                "id": c["id"],
                "type": c["type"],
                "track": c["track"],
                "title": c["title"],
                "summary": c["summary"],
                "path": os.path.relpath(p, ROOT).replace(os.sep, "/"),
            })
    rows.sort(key=lambda r: (ORDER.get(r["track"], 9), r["type"], r["id"]))
    out = os.path.join(ROOT, "index.jsonl")
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("index.jsonl: %d cards" % len(rows))


if __name__ == "__main__":
    main()
