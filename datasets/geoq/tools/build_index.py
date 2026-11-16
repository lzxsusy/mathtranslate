#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_index.py —— 扫描 cards/ 生成 index.jsonl（供检索与静态站使用）。

用法：python tools/build_index.py
输出：index.jsonl（每行一张卡），字段按固定顺序。
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "cards"
TRACK_NAMES = {"A": "辛几何底座", "B": "半经典量子化", "C": "海森堡表示", "D": "量子化机器", "O": "总览"}


def main():
    rows = []
    for kind in ("concepts", "examples"):
        for p in sorted((CARDS / kind).glob("*.json")):
            c = json.loads(p.read_text(encoding="utf-8"))
            pages = []
            for s in c.get("sources", []):
                pages.extend(s.get("pages", []))
            rows.append({
                "id": c["id"],
                "type": c["type"],
                "title": c["title"],
                "track": c["track"],
                "track_name": TRACK_NAMES.get(c["track"], ""),
                "summary": c["summary"],
                "question": c.get("question", ""),
                "concept_refs": c.get("concept_refs", []),
                "related": c.get("related", []),
                "pages": [min(pages), max(pages)] if pages else [],
                "path": f"cards/{kind}/{p.name}",
            })
    rows.sort(key=lambda r: ({"O": 0, "A": 1, "B": 2, "C": 3, "D": 4}.get(r["track"], 9), r["type"], r["id"]))
    out = ROOT / "index.jsonl"
    with out.open("w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"wrote {out} ({len(rows)} cards)")


if __name__ == "__main__":
    main()
