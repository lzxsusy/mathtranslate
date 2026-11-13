# -*- coding: utf-8 -*-
r"""页覆盖检查：每个块的 % [原文 p.N] 标记是否覆盖了分配的印刷页段。
用法：python tools/check_pages.py
"""
import sys, io, os, glob, re
sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"<本地路径>"
CH = os.path.join(ROOT, "src", "chunks")

RANGES = {
    "c01": (1, 8), "ch02": (9, 19), "ch03": (20, 32), "ch04": (33, 41), "ch05": (42, 58),
    "ch06a": (59, 70), "ch06b": (71, 83), "ch07": (84, 99), "ch08": (100, 106),
    "ch09": (107, 121), "appA": (122, 131), "appB": (132, 141), "appC": (142, 149),
    "appD": (150, 154),
}

for base, (lo, hi) in RANGES.items():
    files = sorted(glob.glob(os.path.join(CH, f"{base}-*.tex")))
    pages = []
    for f in files:
        for ln in io.open(f, encoding="utf-8", errors="replace"):
            m = re.search(r"%\s*\[原文 p\.(\d+)\]", ln)
            if m:
                pages.append(int(m.group(1)))
    have = set(pages)
    miss = [p for p in range(lo, hi + 1) if p not in have]
    extra = sorted(p for p in have if p < lo or p > hi)
    status = "OK" if not miss and not extra else "CHECK"
    print(f"{base:6s} pp.{lo:3d}-{hi:3d} files={len(files):2d} pages={len(have):3d} "
          f"missing={miss if miss else '-'} out_of_range={extra if extra else '-'}  [{status}]")
