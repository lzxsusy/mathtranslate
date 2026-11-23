#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""从 .aux 提取「原文页 → 译本页」对照表。

\srcpage / \srcpageinl 每处都写了 \label{srcpage:N}，编译两遍后 aux 里记录它落在译本第几页。

用法（在 源码/ 下）：
    python ../工程文件/tools/page_map.py main
    python ../工程文件/tools/page_map.py _check_c --tsv ..\\工程文件\\work\\pagemap_c.tsv
输出：按原文页排序的对照表；检查是否缺页、是否单调。
"""
import argparse
import re
import sys
from pathlib import Path

RE = re.compile(r"\\newlabel\{srcpage:(\d+)\}\{\{[^{}]*\}\{(\d+)\}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("job")
    ap.add_argument("--dir", default=".")
    ap.add_argument("--tsv", default=None, help="写出 TSV（原文页\\t译本页）")
    ap.add_argument("--start", type=int, default=None)
    ap.add_argument("--end", type=int, default=None)
    a = ap.parse_args()

    aux = Path(a.dir) / f"{a.job}.aux"
    if not aux.exists():
        sys.exit(f"[error] 找不到 {aux}（先编译两遍：第一遍写 label，第二遍才定页）")
    txt = aux.read_text(encoding="utf-8", errors="replace")
    pairs = sorted({(int(n), int(p)) for n, p in RE.findall(txt)})
    if not pairs:
        sys.exit("[error] aux 里没有 srcpage 标签——\\srcpage 没被调用？")

    print(f"[info] {len(pairs)} 个原文页锚点")
    m = dict(pairs)
    pages = [p for _, p in pairs]
    nonmono = [(pairs[i - 1], pairs[i]) for i in range(1, len(pairs)) if pairs[i][1] < pairs[i - 1][1]]
    if nonmono:
        print(f"[warn] 译本页出现倒退 {len(nonmono)} 处（正文顺序与原文不一致？）：{nonmono[:5]}")

    if a.start is not None and a.end is not None:
        missing = [n for n in range(a.start, a.end + 1) if n not in m]
        if missing:
            print(f"[FAIL] 缺原文页 {len(missing)}：{missing}")
        else:
            print(f"[ok] 原文 p.{a.start}–p.{a.end} 全部有对照")

    span = f"{pairs[0][0]}–{pairs[-1][0]}" if pairs else ""
    print(f"[info] 原文页 {span} → 译本页 {min(pages)}–{max(pages)}")
    if a.tsv:
        out = Path(a.tsv)
        out.write_text("原文页\t译本页\n" + "".join(f"{n}\t{p}\n" for n, p in pairs), encoding="utf-8")
        print(f"[ok] 写入 {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
