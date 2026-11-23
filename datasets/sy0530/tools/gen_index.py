# -*- coding: utf-8 -*-
"""从 cards/ 生成 index.jsonl 与 verification.jsonl（照 datasets/sy0117 的格式）。"""
import json, os, io, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

cards = []
for p in sorted(glob.glob(os.path.join(ROOT, "cards", "concepts", "*.json"))) + \
         sorted(glob.glob(os.path.join(ROOT, "cards", "work", "*.json"))):
    with io.open(p, encoding="utf-8") as f:
        cards.append(json.load(f))

with io.open(os.path.join(ROOT, "index.jsonl"), "w", encoding="utf-8", newline="\n") as f:
    for c in cards:
        s = c.get("sources") or [{}]
        f.write(json.dumps({
            "id": c["id"],
            "type": c.get("type"),
            "track": c.get("track"),
            "title": c.get("title"),
            "summary": c.get("summary"),
            "section": s[0].get("section"),
            "anchor": s[0].get("anchor"),
        }, ensure_ascii=False) + "\n")

with io.open(os.path.join(ROOT, "verification.jsonl"), "w", encoding="utf-8", newline="\n") as f:
    for c in cards:
        v = c.get("verification", {})
        f.write(json.dumps({
            "id": c["id"],
            "status": v.get("status"),
            "checked_on": v.get("checked_on"),
            "checks": v.get("checks", []),
        }, ensure_ascii=False) + "\n")

print("index", len(cards), "rows")
