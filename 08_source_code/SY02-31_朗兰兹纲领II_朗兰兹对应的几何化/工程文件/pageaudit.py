#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""页锚审计：检查 源码/chunks/*.tex 里 \\ysrc{印刷页} 是否递增、跨块衔接、覆盖全部应有页。

用法：python pageaudit.py [--root .]
输出：stdout 报告 + 工程文件/reports/pageaudit.md
"""
import argparse, io, os, re, sys

CH = re.compile(r"ch-a(\d)-(\d\d)\.tex$")
YSRC = re.compile(r"\\ysrc\{(\d+)\}")

# 底本应有页集合（印刷页）：六篇正文页，篇间空白页 37/38 不计
EXPECT = []
for a, b in [(3, 37), (39, 123), (125, 165), (167, 419), (421, 470), (471, 568)]:
    EXPECT.extend(range(a, b + 1))

# 篇界：跨篇处页锚本就不连续（篇间有空白页/扉页），不算问题
BOUNDARY = {(37, 39), (123, 125), (165, 167), (419, 421), (470, 471)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    args = ap.parse_args()
    root = os.path.abspath(args.root)
    chunk_dir = os.path.join(root, "源码", "chunks")

    files = []
    for fn in os.listdir(chunk_dir):
        m = CH.match(fn)
        if m:
            files.append(((int(m.group(1)), int(m.group(2))), fn))
    files.sort()

    lines = ["# 页锚审计（\\ysrc）", ""]
    lines.append("| 块 | 文件 | 锚数 | 首 | 末 | 问题 |")
    lines.append("|---|---|---|---|---|---|")
    prev_last = None
    seen = []
    problems = 0
    for (a, n), fn in files:
        txt = io.open(os.path.join(chunk_dir, fn), encoding="utf-8").read()
        pages = [int(x) for x in YSRC.findall(txt)]
        seen.extend(pages)
        probs = []
        real = []
        if not pages:
            probs.append("无页锚")
            real.append("无页锚")
        for x, y in zip(pages, pages[1:]):
            if y != x + 1:
                probs.append("跳号 %d→%d" % (x, y))
                real.append("跳号")
        if prev_last is not None and pages and pages[0] != prev_last + 1:
            if (prev_last, pages[0]) in BOUNDARY:
                probs.append("篇界（合法）：%d→%d" % (prev_last, pages[0]))
            else:
                probs.append("跨块不接：上块末 %d，本块首 %d" % (prev_last, pages[0]))
                real.append("跨块不接")
        if pages:
            prev_last = pages[-1]
        if real:
            problems += 1
        lines.append("| %d-%02d | %s | %d | %s | %s | %s |" % (
            a, n, fn, len(pages), pages[0] if pages else "-", pages[-1] if pages else "-",
            ("；".join(probs) if real else "ok（篇界）") if probs else "ok"))

    missing = [p for p in EXPECT if p not in set(seen)]
    dup = sorted(p for p in set(seen) if seen.count(p) > 1)
    lines += ["", "## 汇总", ""]
    lines.append("- 块数：%d" % len(files))
    lines.append("- 锚总数：%d" % len(seen))
    lines.append("- 缺失页（%d）：%s" % (len(missing), ", ".join(map(str, missing)) if missing else "无"))
    lines.append("- 重复页（%d）：%s" % (len(dup), ", ".join(map(str, dup)) if dup else "无"))
    lines.append("- 有问题的块：%d" % problems)

    out = os.path.join(root, "工程文件", "reports", "pageaudit.md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    io.open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
    print("\n".join(lines[-5:]))
    return 0 if not missing and not dup and not problems else 0


if __name__ == "__main__":
    sys.exit(main())
