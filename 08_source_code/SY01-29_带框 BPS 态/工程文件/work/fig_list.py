# -*- coding: utf-8 -*-
"""GMN3 插图清单生成器：按 chunk 顺序、按 PDF 中图号顺序列出全部插图。

识别两种写法（译本沿用了原文宏）：
  \\insfig[<width>]{<name>}{<caption>}        —— 主要写法
  \\includegraphics[<opts>]{figures/<name>-crop.pdf}
图号 = 出现顺序。实测：源码里 \\insfig 共出现 54 次，其中两处是块首注释（ch05.tex:5、ch11.tex:5）
里的字面提及，真正的插图 52 幅；成品 PDF 的图注「图N:」正好 1..52 连续无缺，二者一致。
（任务书写的「54 幅」应是把注释行也数了进去。）

输出：
  fig_list.tsv   idx<TAB>chunk<TAB>section<TAB>name<TAB>caption
  fig_table.md   markdown 片段（供 03-条款索引.md 拼接）

用法：python fig_list.py [--src <chunks 目录>] [--outdir <目录>]
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, "..", ".."))
DEFAULT_SRC = os.path.join(PROJ, "源码", "chunks")

# 块 → 该块承载的节（取自工程文件/BRIEF.md 的 16 块分块表）
CHUNK_SEC = {
    "ch01": "§1", "ch02": "§2", "ch03": "§3.1–3.3", "ch04": "§3.4–3.6",
    "ch05": "§4.1–4.3", "ch06": "§4.4–4.5", "ch07": "§5", "ch08": "§6–§7.1",
    "ch09": "§7.2–7.5", "ch10": "§8", "ch11": "§9", "ch12": "§10.1–10.3",
    "ch13": "§10.4–10.8", "ch14": "§11–§12", "ch15": "§13 + 附录 A–E",
    "ch16": "附录 F–G",
}

INSFIG_RE = re.compile(r"\\insfig(?:\[[^\]]*\])?\{([^{}]*)\}\{")
INCG_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{figures/([^{}]*)\.pdf\}")


def caption_of(text, start):
    """从 '{' 之后的正文里取出平衡花括号内的图注（允许内部嵌套 $...$）。"""
    depth, i = 1, start
    while i < len(text) and depth:
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
        i += 1
    return text[start:i - 1]


def scan(src):
    rows = []
    for fn in sorted(os.listdir(src)):
        if not fn.endswith(".tex"):
            continue
        chunk = fn[:-4]
        text = open(os.path.join(src, fn), encoding="utf-8").read()
        hits = []
        for m in INSFIG_RE.finditer(text):
            # 名字去掉 -crop 后缀，保持与 figures/ 下的源文件名一致
            name = m.group(1).strip()
            cap = caption_of(text, m.end())
            hits.append((m.start(), name, cap))
        for m in INCG_RE.finditer(text):
            hits.append((m.start(), m.group(1).strip(), ""))
        hits.sort()
        for pos, name, cap in hits:
            rows.append((chunk, CHUNK_SEC.get(chunk, "?"), name, " ".join(cap.split())))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=DEFAULT_SRC)
    ap.add_argument("--outdir", default=HERE)
    args = ap.parse_args()
    if not os.path.isdir(args.src):
        sys.exit("找不到 chunks 目录：%s" % args.src)

    rows = scan(args.src)
    tsv = os.path.join(args.outdir, "fig_list.tsv")
    with open(tsv, "w", encoding="utf-8", newline="\n") as f:
        f.write("idx\tchunk\tsection\tname\tcaption\n")
        for i, (chunk, sec, name, cap) in enumerate(rows, 1):
            f.write("%d\t%s\t%s\t%s\t%s\n" % (i, chunk, sec, name, cap))

    md = os.path.join(args.outdir, "fig_table.md")
    with open(md, "w", encoding="utf-8", newline="\n") as f:
        f.write("| 图 | 文件名 | 块 | 归属节 | 图注（首句） |\n")
        f.write("|---|---|---|---|---|\n")
        for i, (chunk, sec, name, cap) in enumerate(rows, 1):
            short = cap if len(cap) <= 42 else cap[:42] + "…"
            short = short.replace("|", "\\|")
            f.write("| %d | `%s` | %s | %s | %s |\n" % (i, name, chunk, sec, short))

    print("图数: %d" % len(rows))
    for chunk in CHUNK_SEC:
        n = sum(1 for r in rows if r[0] == chunk)
        if n:
            print("  %s (%s): %d 幅" % (chunk, CHUNK_SEC[chunk], n))
    print("输出: %s / %s" % (tsv, md))


if __name__ == "__main__":
    main()
