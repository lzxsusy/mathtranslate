#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查每张卡的 sources 页码是否等于 anchor 所覆盖的印刷页；只报不一致。"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "SY07-03" / "chunks"


def resolve_src():
    """底本源码不入仓；用 --src 指向 chunks/ 目录即可复核。"""
    global SRC
    if "--src" in sys.argv:
        SRC = Path(sys.argv[sys.argv.index("--src") + 1]).resolve()
    if not (SRC / "ch05a.tex").exists():
        print(
            f"未找到底本源码：{SRC}\n"
            "该目录不在数据集内（版权原因）。本地复核时用：\n"
            "  python tools/audit_pages.py --src /path/to/SY07-03/chunks"
        )
        return False
    return True


def page_map(fn):
    marks = []
    for i, line in enumerate((SRC / fn).read_text(encoding="utf-8").splitlines(), 1):
        m = re.search(r"\[原文 p\.(\d+)\]", line)
        if m:
            marks.append((i, int(m.group(1))))
    return marks


def page_at(marks, line):
    cur = None
    for i, p in marks:
        if i <= line:
            cur = p
        else:
            break
    return cur


def main():
    if not resolve_src():
        return 2
    maps = {"ch05a.tex": page_map("ch05a.tex"), "ch05b.tex": page_map("ch05b.tex")}
    bad = 0
    for p in sorted(ROOT.glob("cards/*/*.json")):
        c = json.loads(p.read_text(encoding="utf-8"))
        for s in c.get("sources", []):
            m = re.match(r"(ch05[ab]\.tex):(\d+)-(\d+)$", s.get("anchor", ""))
            if not m:
                print(f"[ANCHOR] {c['id']}: {s.get('anchor')}")
                bad += 1
                continue
            fn, a, b = m.group(1), int(m.group(2)), int(m.group(3))
            actual = [page_at(maps[fn], a), page_at(maps[fn], b)]
            if actual != s.get("pages"):
                print(f"[PAGE] {c['id']}: {s['anchor']} actual={actual} decl={s.get('pages')}")
                bad += 1
    print(f"checked; issues={bad}")


if __name__ == "__main__":
    main()
