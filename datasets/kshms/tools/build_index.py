#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""build_index.py —— 重建 index.jsonl（轻量索引：id / type / track / kind / kind_no / title / summary / path）。"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    rows = []
    for dirpath, _, names in os.walk(os.path.join(ROOT, "cards")):
        for nm in sorted(names):
            if not nm.endswith(".json"):
                continue
            full = os.path.join(dirpath, nm)
            card = json.load(open(full, encoding="utf-8"))
            rows.append({
                "id": card["id"],
                "type": card.get("type", ""),
                "track": card.get("track", ""),
                "kind": card.get("kind", ""),
                "kind_no": card.get("kind_no", 0),
                "title": card.get("title", ""),
                "summary": card.get("summary", ""),
                "path": os.path.relpath(full, ROOT).replace("\\", "/"),
            })
    order = {"concept": 0, "remark": 1, "correction": 2}
    rows.sort(key=lambda r: (order.get(r["type"], 9), r["track"], r["kind_no"]))
    out = os.path.join(ROOT, "index.jsonl")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"index.jsonl: {len(rows)} 条")


if __name__ == "__main__":
    main()
