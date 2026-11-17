#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_pages.py —— 核对卡片的 anchor 与本地页文本是否一致（底本源码不入仓）。

数据集的 sources 用「印刷页」：`B p.38`、`B p.46 eq (4.11)`。本脚本在**本机**用
解经工程 `source/text/pNNN.txt`（印刷页 N ↔ p(N+1).txt）逐条核对：
  1) anchor 的页号落在 sources.pages 区间内；
  2) 对应 pNNN.txt 文件存在且非空；
  3) anchor 带 `eq (x.y)` 时，该页文本里必须有这个式号。

用法：
    python tools/audit_pages.py --src "C:/Users/admin/Desktop/witten-exegesis/papers/WIT-0604151-EMDGL/source/text"
不带 --src 时只做内部一致性检查（1 和 pages 合法性）。
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ANCHOR_RE = re.compile(r"^(?P<t>[ABCD]) p\.(?P<p>\d+)(?:\s*[–-]\s*(?P<q>\d+))?(?:\s+eq\s+\(?(?P<eq>[\w.\-]+)\)?)?$")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="", help="解经工程的 source/text 目录（本机复核用）")
    ap.add_argument("--only", default="B", help="只核对哪个底本（默认 B，A/C/D 页文本不在本机）")
    args = ap.parse_args()
    src = Path(args.src) if args.src else None

    issues = 0
    checked = 0
    for p in sorted(ROOT.glob("cards/*/*.json")):
        c = json.loads(p.read_text(encoding="utf-8"))
        for s in c.get("sources", []):
            a = s.get("anchor", "")
            m = ANCHOR_RE.match(a)
            if not m:
                print(f"[FORMAT] {c['id']}: anchor={a!r}")
                issues += 1
                continue
            if m.group("t") != args.only:
                continue
            page = int(m.group("p"))
            pages = s.get("pages") or []
            if not (len(pages) == 2 and pages[0] <= page <= pages[1]):
                print(f"[RANGE] {c['id']}: anchor p.{page} 不在 pages={pages}")
                issues += 1
            if src is None:
                continue
            f = src / f"p{page + 1:03d}.txt"
            if not f.exists() or f.stat().st_size < 20:
                print(f"[FILE] {c['id']}: 缺 {f.name}")
                issues += 1
                continue
            checked += 1
            eq = m.group("eq")
            if eq:
                q = int(m.group("q") or page)
                pat = re.compile(r"\(\s*" + re.escape(eq) + r"\s*\)")
                hit = False
                for pg in range(page, q + 1):
                    fp = src / f"p{pg + 1:03d}.txt"
                    if fp.exists() and pat.search(fp.read_text(encoding="utf-8", errors="replace")):
                        hit = True
                        break
                if not hit:
                    print(f"[EQ] {c['id']}: p.{page}–{q} 里找不到式号 ({eq})")
                    issues += 1
    print(f"checked={checked} issues={issues}")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
