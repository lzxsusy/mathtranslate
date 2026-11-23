#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""核查 \\srcpage 页码锚点是否齐全。

用法（在 源码/ 下）：
    python ../工程文件/tools/check_pagemarks.py _check_c --start 39 --end 44
    python ../工程文件/tools/check_pagemarks.py main

读 <jobname>.pagemarks（preamble 里 \\srcpage 逐条写入），报：
  - 缺哪些页
  - 重复
  - 顺序是否单调（乱序通常是排版把锚点位置放错了）
"""
import argparse
import sys
from pathlib import Path


def read_marks(path: Path):
    if not path.exists():
        sys.exit(f"[error] 找不到 {path}（先编译一次）")
    out = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        s = line.strip()
        if not s:
            continue
        try:
            out.append(int(s))
        except ValueError:
            out.append(s)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("job", help="jobname，如 _check_c / main")
    ap.add_argument("--start", type=int, default=None)
    ap.add_argument("--end", type=int, default=None)
    ap.add_argument("--dir", default=".", help="pagemarks 所在目录（默认 源码/）")
    ap.add_argument("--pdf", action="store_true", help="同时核查 PDF 里这些 p.N 是否真的印出来了")
    a = ap.parse_args()

    path = Path(a.dir) / f"{a.job}.pagemarks"
    marks = read_marks(path)
    print(f"[info] {path}：共 {len(marks)} 个锚点")

    if not marks:
        sys.exit("[error] 一个锚点都没写出来——\\srcpage 没被调用？")

    # 重复
    seen, dup = set(), []
    for m in marks:
        if m in seen:
            dup.append(m)
        seen.add(m)
    if dup:
        print(f"[warn] 重复锚点：{sorted(set(dup))}")

    # 单调
    nums = [m for m in marks if isinstance(m, int)]
    bad = [(nums[i - 1], nums[i]) for i in range(1, len(nums)) if nums[i] < nums[i - 1]]
    if bad:
        print(f"[warn] 顺序倒退 {len(bad)} 处：{bad[:8]}")

    rc = 0
    # 视觉核查：页码条是否真印进 PDF
    if a.pdf:
        pdf = Path(a.dir) / f"{a.job}.pdf"
        if not pdf.exists():
            print(f"[FAIL] 找不到 {pdf}，无法核查视觉页码条")
            rc = 1
        else:
            try:
                import pymupdf  # noqa: F401
                import re
                doc = pymupdf.open(str(pdf))
                text = "\n".join(p.get_text() for p in doc)
                printed = {int(m) for m in re.findall(r"p\.(\d+)", text)}
                lost = [n for n in nums if n not in printed]
                if lost:
                    print(f"[FAIL] 有 {len(lost)} 个锚点没印出来（多半夹在行中间，挪到段首）：{lost}")
                    rc = 1
                else:
                    print(f"[ok] {len(nums)} 个锚点全部在 PDF 中可见")
            except ImportError:
                print("[warn] 没有 pymupdf，跳过视觉核查")

    # 完整性
    if a.start is not None and a.end is not None:
        want = set(range(a.start, a.end + 1))
        got = set(nums)
        missing = sorted(want - got)
        extra = sorted(got - want)
        if missing:
            print(f"[FAIL] 缺页 {len(missing)}：{missing}")
            rc = 1
        if extra:
            print(f"[warn] 超出范围：{extra}")
        if not missing and not extra:
            print(f"[ok] p.{a.start}–p.{a.end} 锚点齐全")
    return rc


if __name__ == "__main__":
    sys.exit(main())
