#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""译幅覆盖率审计：按页比较「中文字符数 / 英文原文字数」，找疑似漏译或过度增补的页。

做法：以 \\ysrc{印刷页} 为界把 chunk 切成页段，数页段里的汉字数；
英文单词数取自底本逐页文本（lp2_work/pages/pNNN.txt，PDF 页 = 印刷页 + 13）。
经验比值：数学文本约 1.2–2.6 个汉字/英文词；低于 0.9 疑漏译，高于 3.2 疑大段增补。

用法：python coverage.py [--pages DIR]
输出：工程文件/reports/coverage.md
"""
import argparse, io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = re.compile(r"ch-a(\d)-(\d\d)\.tex$")
YSRC = re.compile(r"\\ysrc\{(\d+)\}")
HAN = re.compile(r"[\u4e00-\u9fff]")
LATIN = re.compile(r"[A-Za-z][A-Za-z']+")

LOW, HIGH = 0.9, 3.2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", default=os.path.join(os.path.expanduser("~"), "Downloads", "lp2_work", "pages"))
    args = ap.parse_args()

    chunk_dir = os.path.join(ROOT, "源码", "chunks")
    files = sorted(fn for fn in os.listdir(chunk_dir) if CH.match(fn))
    rows = []
    for fn in files:
        txt = io.open(os.path.join(chunk_dir, fn), encoding="utf-8").read()
        marks = [(m.start(), int(m.group(1))) for m in YSRC.finditer(txt)]
        for i, (pos, page) in enumerate(marks):
            end = marks[i + 1][0] if i + 1 < len(marks) else len(txt)
            seg = txt[pos:end]
            zh = len(HAN.findall(seg))
            src = os.path.join(args.pages, "p%03d.txt" % (page + 13))
            en = 0
            if os.path.exists(src):
                en = len(LATIN.findall(io.open(src, encoding="utf-8", errors="ignore").read()))
            ratio = (zh / en) if en else 0.0
            rows.append((fn, page, zh, en, ratio))

    bad = [r for r in rows if r[4] and (r[4] < LOW or r[4] > HIGH)]
    lines = ["# 译幅覆盖率审计", ""]
    lines.append("比值 = 该页译文汉字数 / 该页英文原文字数；经验区间 %.1f–%.1f。" % (LOW, HIGH))
    lines.append("")
    lines.append("| 文件 | 页 | 汉字 | 英文词 | 比值 | 判读 |")
    lines.append("|---|---|---|---|---|---|")
    for fn, page, zh, en, ratio in rows:
        if not en:
            flag = "无原文页"
        elif ratio < LOW:
            flag = "疑漏译"
        elif ratio > HIGH:
            flag = "疑增补"
        else:
            flag = "ok"
        if flag != "ok":
            lines.append("| %s | %d | %d | %d | %.2f | %s |" % (fn, page, zh, en, ratio, flag))
    lines += ["", "## 汇总", ""]
    lines.append("- 页段数：%d" % len(rows))
    lines.append("- 异常页段：%d（漏译 %d，增补 %d，缺原文 %d）" % (
        len(bad), sum(1 for r in bad if r[4] < LOW), sum(1 for r in bad if r[4] > HIGH),
        sum(1 for r in rows if not r[3])))
    vals = sorted(r[4] for r in rows if r[4])
    if vals:
        lines.append("- 比值中位数：%.2f；分位 10%%/90%%：%.2f/%.2f" % (
            vals[len(vals) // 2], vals[int(len(vals) * 0.1)], vals[int(len(vals) * 0.9)]))

    out = os.path.join(ROOT, "工程文件", "reports", "coverage.md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    io.open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
    print("pages=%d anomalies=%d -> %s" % (len(rows), len(bad), out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
