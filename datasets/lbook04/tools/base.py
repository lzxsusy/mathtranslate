# -*- coding: utf-8 -*-
"""lbook04 资料卡公共辅助：书目、源路径、card() 构造函数。"""

BOOK = "Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004"
SRC = "08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/"


OFFSET = {1: 8, 2: 8, 3: 7, 4: 6, 5: 5, 6: 5, 7: 4, 8: 3, 9: 3, 10: 3, 11: 2, 12: 2}


def src(ch, sec, pages, anchor, section=None):
    """ch=章号；pages 用印刷页码；pdf_pages 按 work/PAGE_MAP.md 的偏移推出。"""
    return {
        "book": BOOK,
        "section": section or sec,
        "pages": pages,
        "pdf_pages": [p + OFFSET[ch] for p in pages],
        "anchor": SRC + anchor,
    }


def card(cid, track, title, aliases, summary, question, text, notation, keys, formulas,
         pitfalls, ann, related, sources, theorems=None):
    return {
        "id": "lbook04/concept/" + cid,
        "type": "concept",
        "track": track,
        "title": title,
        "aliases": aliases,
        "summary": summary,
        "question": question,
        "definition": {"text": text, "notation": notation},
        "key_points": keys,
        "formulas": formulas,
        "theorems": theorems or [],
        "pitfalls": pitfalls,
        "annotations": ann,
        "related": ["lbook04/concept/" + r for r in related],
        "sources": sources,
        "rights": "rewritten",
        "status": "reviewed",
        "verification": {"status": "source-only", "checked_on": "2026-11-23", "checks": []},
    }
