"""生成 verification.jsonl：每张卡一条 source-only 记录。

用法（仓库根目录）：
    python datasets/lawrge24/tools/make_verification.py
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CARDS = ROOT / "cards"
OUT = ROOT / "verification.jsonl"


def card_files():
    for kind in ("concepts", "derivations"):
        yield from sorted((CARDS / kind).glob("*.json"))


def main() -> None:
    rows = []
    for path in card_files():
        card = json.loads(path.read_text(encoding="utf-8"))
        sources = card.get("sources") or []
        entries = []
        for src in sources:
            section = (src.get("section") or "").strip()
            anchor = (src.get("anchor") or "").strip()
            entries.append(f"{section} {anchor}".strip())
        entry = "；".join(dict.fromkeys(entries)) or "全文"
        rows.append(
            {
                "id": card["id"],
                "status": "source-only",
                "note": "逐节对齐 LAWRGE 2024 原文并经 lint 校验引文；未做 nLab / Stacks / 原始论文的外部核验。",
                "checks": [
                    {
                        "source": "LAWRGE 2024 NOTES",
                        "entry": entry,
                        "last_revised": "2024-12-03",
                        "asserts": "本卡的陈述与引文对齐该节；尚未找到逐字对应的外部核验页。",
                        "verdict": "source-only",
                    }
                ],
            }
        )
    with OUT.open("w", encoding="utf-8", newline="\n") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"verification.jsonl: {len(rows)} cards")


if __name__ == "__main__":
    main()
