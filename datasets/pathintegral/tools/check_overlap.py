#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_overlap.py —— 扫描卡片散文中与底本连续相同的汉字串。

用法：
    python tools/check_overlap.py --src /path/to/SY07-03/chunks
    python tools/check_overlap.py --src ... --top 30 --threshold 20

只统计汉字（CJK 统一表意文字）；公式、标点、空白不参与匹配。
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CJK = re.compile(r"[\u4e00-\u9fff]")

def han(s):
    return "".join(CJK.findall(s or ""))

class SAM:
    def __init__(self):
        self.next = [{}]
        self.link = [-1]
        self.length = [0]
        self.last = 0
    def extend(self, ch):
        cur = len(self.next)
        self.next.append({}); self.length.append(self.length[self.last] + 1); self.link.append(0)
        p = self.last
        while p != -1 and ch not in self.next[p]:
            self.next[p][ch] = cur
            p = self.link[p]
        if p == -1:
            self.link[cur] = 0
        else:
            q = self.next[p][ch]
            if self.length[p] + 1 == self.length[q]:
                self.link[cur] = q
            else:
                clone = len(self.next)
                self.next.append(dict(self.next[q])); self.length.append(self.length[p] + 1); self.link.append(self.link[q])
                while p != -1 and self.next[p].get(ch) == q:
                    self.next[p][ch] = clone
                    p = self.link[p]
                self.link[q] = self.link[cur] = clone
        self.last = cur
    def longest(self, s):
        v = 0; l = 0; best = 0
        for ch in s:
            while v and ch not in self.next[v]:
                v = self.link[v]; l = self.length[v]
            if ch in self.next[v]:
                v = self.next[v][ch]; l += 1
                best = max(best, l)
            else:
                v = 0; l = 0
        return best

def iter_strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for k, v in o.items():
            if k in ("id", "type", "track", "rights", "status", "aliases"):
                continue
            yield from iter_strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from iter_strings(v)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--threshold", type=int, default=20)
    ap.add_argument("--top", type=int, default=25)
    a = ap.parse_args()
    src = Path(a.src)
    if not (src / "ch02a.tex").exists():
        print(f"找不到底本：{src}"); return 2
    book = "".join(han(p.read_text(encoding="utf-8")) for p in sorted(src.glob("ch02*.tex")))
    sam = SAM()
    for ch in book:
        sam.extend(ch)
    rows = []
    for p in sorted((ROOT / "cards").glob("*/*.json")):
        c = json.loads(p.read_text(encoding="utf-8"))
        best = 0; where = ""
        for s in iter_strings(c):
            n = sam.longest(han(s))
            if n > best:
                best = n; where = s[:60].replace("\n", " ")
        if best:
            rows.append((best, c["id"], where))
    rows.sort(reverse=True)
    bad = [r for r in rows if r[0] >= a.threshold]
    for n, cid, where in rows[:a.top]:
        flag = "BAD" if n >= a.threshold else "ok "
        print(f"{flag} {n:3d}  {cid}  {where}")
    print(f"\ncards={len(rows)}  >= {a.threshold}: {len(bad)}")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
