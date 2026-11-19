# -*- coding: utf-8 -*-
"""从 cards/ 生成 index.jsonl（一行一卡，按 id 排序）。"""
from __future__ import annotations

import glob
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main() -> int:
    rows = []
    for p in sorted(glob.glob(os.path.join(ROOT, "cards", "**", "*.json"), recursive=True)):
        card = json.load(io.open(p, encoding="utf-8"))
        rows.append({
            "id": card["id"],
            "title": card["title"],
            "track": card["track"],
            "scope": card["scope"],
            "section": card["source"]["section"],
            "pages": card["source"]["pages"],
            "lean_name": card["lean"]["name"],
            "lean_file": card["lean"]["file"],
            "verification": card["verification"]["status"],
            "sorry_count": card["verification"]["sorry_count"],
            "mathlib_rev": card["verification"]["mathlib_rev"],
        })
    rows.sort(key=lambda r: r["id"])
    out = os.path.join(ROOT, "index.jsonl")
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    cert = sum(1 for r in rows if r["verification"] == "certified")
    print(f"wrote {out} rows={len(rows)} certified={cert} gap={len(rows) - cert}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
