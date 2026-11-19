#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_index.py —— 扫描 cards/ 生成 index.jsonl（gtgl15 资料卡）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "cards"
TRACK_NAMES = {
    "A": "Hitchin 几何与谱曲线",
    "B": "对偶环面与 T-对偶",
    "C": "膜、线算符与本征膜",
    "D": "'t Hooft 算符与赫克修正",
    "E": "行列式线丛与本征值",
    "O": "总览",
}
ORDER = {"O": 0, "A": 1, "B": 2, "C": 3, "D": 4, "E": 5}


def main():
    rows = []
    for kind in ("concepts", "derivations"):
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
                "related": c.get("related", []),
                "pages": [min(pages), max(pages)] if pages else [],
                "n_steps": len(c.get("steps", [])),
                "status": c.get("status", "draft"),
                "path": f"cards/{kind}/{p.name}",
            })
    rows.sort(key=lambda r: (ORDER.get(r["track"], 9), r["type"], r["id"]))
    out = ROOT / "index.jsonl"
    with out.open("w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    n_c = sum(1 for r in rows if r["type"] == "concept")
    n_d = len(rows) - n_c
    print(f"wrote {out} ({len(rows)} cards: concept={n_c} derivation={n_d})")


if __name__ == "__main__":
    main()
