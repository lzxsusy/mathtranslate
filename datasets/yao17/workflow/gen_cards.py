#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_cards.py —— 把各 track 模块里的字典写成 cards/{concepts,derivations}/*.json。

用法：python workflow/gen_cards.py            # 全量写盘
      python workflow/gen_cards.py --only A   # 只写 track A 的卡
"""
from __future__ import annotations

import argparse
import importlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KIND = {"concept": "concepts", "derivation": "derivations"}
MODULES = ["cards_o", "cards_a", "cards_b", "cards_c", "cards_d", "cards_deriv"]

CASES: list[dict] = []


def mk(**kw) -> dict:
    CASES.append(kw)
    return kw


def dump(data: list[dict]) -> int:
    n = 0
    for c in data:
        d = ROOT / "cards" / KIND[c["type"]]
        d.mkdir(parents=True, exist_ok=True)
        slug = c["id"].rsplit("/", 1)[-1]
        p = d / f"{slug}.json"
        p.write_text(json.dumps(c, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        n += 1
    return n


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=None, help="只写某个 track")
    args = ap.parse_args()
    for name in MODULES:
        try:
            mod = importlib.import_module(name)
        except ModuleNotFoundError:
            continue
        if hasattr(mod, "add"):
            mod.add(mk)
    data = [c for c in CASES if args.only is None or c["track"] == args.only]
    print(f"wrote {dump(data)} cards")


if __name__ == "__main__":
    main()
