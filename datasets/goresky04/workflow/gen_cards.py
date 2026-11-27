#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_cards.py —— 生成 goresky04 资料卡 JSON（单一事实源，避免手写转义）。

上游：06_Goresky_Langlands_Conjectures_for_Physicists.pdf（20 页，dvips）
页数范围：印本页 1–20，PDF 页 = 印本页。
生成后跑 tools/lint_cards.py、tools/build_index.py、tools/render_md.py。
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PKG = "goresky04"


def card(kind, slug, **kw):
    c = {
        "id": f"{PKG}/{'concept' if kind == 'concepts' else 'deriv'}/{slug}",
        "type": "concept" if kind == "concepts" else "derivation",
        "rights": "rewritten",
        "status": "dev",
    }
    c.update(kw)
    return c


def src(pages, anchor, section, text="A"):
    return {"text": text, "section": section, "pages": pages, "anchor": anchor}


def write_cards(cards, only=None):
    n = 0
    for rel, c in sorted(cards.items()):
        if only and rel.split("/", 1)[1] not in only:
            continue
        path = ROOT / "cards" / (rel + ".json")
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(c, f, ensure_ascii=False, indent=2)
            f.write("\n")
        n += 1
    return n


CARDS = {}
