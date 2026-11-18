#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_index.py —— 扫描 cards/ 生成 index.jsonl。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "cards"


def main():
    rows = []
    for p in sorted(CARDS.glob("**/*.json")):
        c = json.loads(p.read_text(encoding="utf-8"))
        rows.append({
            "id": c["id"],
            "type": c["type"],
            "track": c["track"],
            "title": c["title"],
            "summary": c["summary"],
            "question": c["question"],
            "pages": [s["pages"] for s in c.get("sources", [])],
            "related": c.get("related", []),
            "path": str(p.relative_to(ROOT)).replace("\\", "/"),
            "status": c.get("status", "draft"),
        })
    rows.sort(key=lambda r: (r["type"], r["track"], r["id"]))
    out = ROOT / "index.jsonl"
    with out.open("w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"index.jsonl：{len(rows)} 条")


if __name__ == "__main__":
    main()
