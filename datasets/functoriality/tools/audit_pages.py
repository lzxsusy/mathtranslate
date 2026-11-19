#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_pages.py —— 资料卡页码锚点核对。

每张卡的 sources[].section 形如 "§3.4"，pages 为 [起, 止]；本文件内置
「节号 → 原文印刷页区间」映射（由 arXiv:2210.11159v1 逐页抽文定位所得，
见 workflow/PRODUCTION.md），检查：
  1. pages 落在该节的页区间内；
  2. anchor 里的「原书 p.N」数字落在 pages 区间内；
  3. pages 区间不超过 3 页（一张卡不应跨太多页）。

用法：python tools/audit_pages.py cards
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGEMAP = {
    "1": (1, 3),
    "1.1": (2, 3),
    "1.2": (4, 4),
    "1.3": (4, 4),
    "2": (4, 18),
    "2.1": (5, 9),
    "2.2": (9, 11),
    "2.3": (12, 15),
    "2.4": (16, 18),
    "3": (19, 38),
    "3.1": (19, 19),
    "3.2": (20, 20),
    "3.3": (21, 21),
    "3.4": (22, 24),
    "3.5": (25, 28),
    "3.6": (29, 31),
    "3.7": (32, 32),
    "3.8": (33, 33),
    "3.9": (34, 35),
    "3.10": (36, 36),
    "3.11": (37, 39),
    "4": (39, 52),
    "4.1": (42, 44),
    "4.2": (45, 46),
    "4.3": (47, 48),
    "4.4": (49, 50),
    "4.5": (51, 52),
    "5": (53, 68),
    "5.1": (53, 54),
    "5.2": (55, 55),
    "5.3": (56, 56),
    "5.4": (57, 57),
    "5.5": (58, 58),
    "5.6": (59, 59),
    "5.7": (59, 68)
}
SEC_RE = re.compile(r"§(\d+(?:\.\d+)?)")
PAGE_RE = re.compile(r"p\.(\d+)")


def main():
    base = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "cards")
    issues = []
    n = 0
    for p in sorted(base.glob("**/*.json")):
        c = json.loads(p.read_text(encoding="utf-8"))
        n += 1
        for s in c.get("sources", []):
            sec = s.get("section", "")
            pages = s.get("pages") or [0, 0]
            anchor = s.get("anchor", "")
            m = SEC_RE.search(sec) or SEC_RE.search(anchor)
            if not m:
                issues.append("%s: 无法解析节号 %r" % (c["id"], sec))
                continue
            key = m.group(1)
            if key not in PAGEMAP:
                issues.append("%s: 节号 %s 不在映射表" % (c["id"], key))
                continue
            lo, hi = PAGEMAP[key]
            if not (lo <= pages[0] <= pages[1] <= hi):
                issues.append("%s: p.%d-%d 超出 §%s 的 p.%d-%d" % (c["id"], pages[0], pages[1], key, lo, hi))
            if pages[1] - pages[0] > 3:
                issues.append("%s: 跨页过多 p.%d-%d" % (c["id"], pages[0], pages[1]))
            for num in PAGE_RE.findall(anchor):
                if not (pages[0] <= int(num) <= pages[1]):
                    issues.append("%s: anchor %s 与 pages %d-%d 不符" % (c["id"], anchor, pages[0], pages[1]))
    print("核对 %d 张卡" % n)
    if issues:
        for i in issues:
            print("ERROR", i)
        print("共 %d 处问题" % len(issues))
        return 1
    print("OK 页码锚点全部通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
