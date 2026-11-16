#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_index.py —— 扫描 cards/ 生成 index.jsonl（路径积分资料卡）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "cards"
TRACK_NAMES = {"A": "基础与时间切片", "B": "高斯路径积分与谐振子", "C": "渐近方法与半经典", "D": "格林函数与 WKB", "E": "微扰与代数结构", "O": "总览"}
ORDER = {"O": 0, "A": 1, "B": 2, "C": 3, "D": 4, "E": 5}


def main():
    rows = []
    for kind in ("concepts", "examples"):
        for p in sorted((CARDS / kind).glob("*.json")):
            c = json.loads(p.read_text(encoding="utf-8"))
            pages = []
            for s in c.get("sources", []):
                pages.extend(s.get("pages", []))
            rows.append({
                "id": c["id"], "type": c["type"], "title": c["title"],
                "track": c["track"], "track_name": TRACK_NAMES.get(c["track"], ""),
                "summary": c["summary"], "question": c.get("question", ""),
                "concept_refs": c.get("concept_refs", []), "related": c.get("related", []),
                "pages": [min(pages), max(pages)] if pages else [],
                "path": f"cards/{kind}/{p.name}",
            })
    rows.sort(key=lambda r: (ORDER.get(r["track"], 9), r["type"], r["id"]))
    out = ROOT / "index.jsonl"
    with out.open("w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"wrote {out} ({len(rows)} cards)")


if __name__ == "__main__":
    main()
