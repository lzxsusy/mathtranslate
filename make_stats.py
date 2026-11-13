# -*- coding: utf-8 -*-
r"""生成 README 里的统计块（单一事实源，避免手写数字漂移）。

用法：python make_stats.py            # 只打印
      python make_stats.py --write    # 写回 README.md 的 <!-- STATS:BEGIN/END --> 之间
"""
import argparse
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
REPO = os.path.dirname(os.path.abspath(__file__))
BEGIN = "<!-- STATS:BEGIN -->"
END = "<!-- STATS:END -->"


def mb(n):
    return "%.1f MB" % (n / 1048576.0)


def count_tree(path):
    n = b = 0
    for dp, dn, fn in os.walk(path):
        if ".git" in dp.split(os.sep):
            continue
        for f in fn:
            fp = os.path.join(dp, f)
            try:
                b += os.path.getsize(fp)
            except OSError:
                continue
            n += 1
    return n, b


def main():
    write = "--write" in sys.argv
    d08 = os.path.join(REPO, "08_source_code")
    d03 = os.path.join(REPO, "03_translations_meta")
    projs = [d for d in os.listdir(d08) if os.path.isdir(os.path.join(d08, d))] if os.path.isdir(d08) else []
    tex = img = 0
    with_src = 0
    for d in projs:
        p = os.path.join(d08, d)
        t = 0
        for dp, dn, fn in os.walk(p):
            for f in fn:
                lf = f.lower()
                if lf.endswith(".tex"):
                    tex += 1
                    t += 1
                elif lf.endswith((".png", ".jpg", ".jpeg", ".pdf")) and "figures" in dp.lower():
                    img += 1
        if t:
            with_src += 1

    # 成品 PDF
    pdfs = []
    for dp, dn, fn in os.walk(d03):
        for f in fn:
            if f.lower().endswith(".pdf"):
                pdfs.append(os.path.join(dp, f))
    pdf_bytes = sum(os.path.getsize(p) for p in pdfs)

    # 语料
    zp = os.path.join(REPO, "01_corpus_zh", "zh_paragraphs.jsonl")
    paras = uniq = with_math = near = zhsum = 0
    if os.path.isfile(zp):
        seen = set()
        for line in io.open(zp, encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            paras += 1
            t = d.get("text", "")
            if "$" in t or "\\begin{" in t:
                with_math += 1
            if d.get("near_dup_of"):
                near += 1
            zhsum += int(d.get("zh_chars") or 0)
            h = d.get("para_id")
            if h not in seen:
                seen.add(h)
                uniq += 1
    tb = os.path.join(REPO, "01_corpus_zh", "termbase.jsonl")
    terms = sum(1 for _ in io.open(tb, encoding="utf-8")) if os.path.isfile(tb) else 0

    # 轨迹
    tj = os.path.join(REPO, "02_trajectories", "traj_selected.jsonl")
    traj = sum(1 for _ in io.open(tj, encoding="utf-8")) if os.path.isfile(tj) else 0

    # 会话分片
    sdir = os.path.join(REPO, "06_sessions_raw")
    shards = [f for f in os.listdir(sdir)] if os.path.isdir(sdir) else []
    sbytes = sum(os.path.getsize(os.path.join(sdir, f)) for f in shards
                 if os.path.isfile(os.path.join(sdir, f)))

    nfiles, nbytes = count_tree(REPO)

    lines = [
        BEGIN,
        "",
        "| 指标 | 数值 |",
        "|---|---|",
        "| 译注工程 | **%d** 部（其中 **%d** 部带完整 LaTeX 源码） |" % (len(projs), with_src),
        "| 仓库文件 | %d 个 / **%s** |" % (nfiles, mb(nbytes)),
        "| LaTeX 源文件 / 插图 | %d 个 `.tex` / %d 张图 |" % (tex, img),
        "| 成品 PDF（预印本类） | %d 部 / **%s** |" % (len(pdfs), mb(pdf_bytes)),
        "| 中文段落语料 | **%d** 段（唯一 %d），其中 **%d** 段含公式（%.0f%%）；汉字 %s 字 |"
        % (paras, uniq, with_math, 100.0 * with_math / max(1, paras), format(zhsum, ",")),
        "| 近重复标注 | %d 段（保留，标 `near_dup_of`） |" % near,
        "| 术语基 | %d 条 |" % terms,
        "| 精选轨迹 | %d 条 |" % traj,
        "| 原始会话分片 | %d 片 / **%s** |" % (len([f for f in shards if ".part" in f]), mb(sbytes)),
        "",
        END,
    ]
    block = "\n".join(lines)
    print(block)
    if write:
        p = os.path.join(REPO, "README.md")
        s = io.open(p, encoding="utf-8").read()
        s2 = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda m: block, s, flags=re.S)
        io.open(p, "w", encoding="utf-8", newline="\n").write(s2)
        print("\n[written to README.md]")


if __name__ == "__main__":
    main()
