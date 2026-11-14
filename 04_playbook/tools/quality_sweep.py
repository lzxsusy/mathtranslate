#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""译注与文本质量巡检（quality_sweep）

用途：对 08_source_code 下所有已交付工程做一遍"机器能判"的质量审计，输出一张 TSV。
它不判断数学对错，只量化四件可数的事：

  1. 译注条数与译注密度（每千汉字）——密度过高=替读者思考，过低=可能漏注；
  2. 译注**来源标记覆盖率**——纪律 §2.5 要求每条解释性译注带 [来源：…]/[译者按]/\\cite；
     已交付的 91 部里多数是 v2.0 之前译的，这项会很低：那是**历史欠账，不是脚本 bug**；
  3. 黑名单来源命中（§2.5.9）；
  4. 悬空 \\ref（编译会变成 ??）。

为什么不做"定理环境数对账"：那需要原文 pages/*.txt，已交付工程大多没有 work 目录。
新工程请用 `translate_kit.py check <工程>`，那里的对账是带原文的。

用法：
  python quality_sweep.py [--root <数译仓库>] [--out <tsv>]
"""
import argparse
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def load_kit():
    p = os.path.join(HERE, "translate_kit.py")
    spec = importlib.util.spec_from_file_location("translate_kit", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def read_tex_dir(d):
    """返回 {文件名: 文本}（只收 .tex）。"""
    out = {}
    if not d or not os.path.isdir(d):
        return out
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".tex"):
            continue
        with open(os.path.join(d, fn), encoding="utf-8", errors="replace") as f:
            out[fn] = f.read()
    return out


def cjk_count(s):
    return len(re.findall(r"[\u4e00-\u9fff]", s))


def audit_project(kit, root):
    chunks_dir = kit._chunks_dir(root)
    texts = read_tex_dir(chunks_dir)
    if not texts:
        return None
    joined = "\n".join(texts.values())
    cjk = cjk_count(joined)

    notes = 0
    missing = 0
    for name, t in texts.items():
        for _start, block in kit._iter_notes(t):
            notes += 1
            if not any(k in block for k in ("[来源：", "[译者按", "\\cite{", "[依据：")):
                missing += 1

    black = 0
    for kw in ("知乎", "百度百科", "CSDN", "简书", "博客园"):
        black += joined.count(kw)

    labels = set(re.findall(r"\\label\{([^}]+)\}", joined))
    refs = set(re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", joined))
    dangling = len(refs - labels)

    routenotes = joined.count("\\routenote")
    no_page = 0
    for m in re.finditer(r"\\routenote\{", joined):
        i = m.end()
        depth, j = 1, i
        while j < len(joined) and depth > 0:
            if joined[j] == "\\":
                j += 2
                continue
            depth += 1 if joined[j] == "{" else (-1 if joined[j] == "}" else 0)
            j += 1
        body = joined[i:j - 1]
        if not re.search(r"p\.\s*\d+|第\s*\d+\s*页|pp?\.\s*\d+", body):
            no_page += 1

    return dict(
        chunks=len(texts),
        cjk=cjk,
        notes=notes,
        missing=missing,
        density=(notes * 1000.0 / cjk) if cjk else 0.0,
        black=black,
        dangling=dangling,
        routenotes=routenotes,
        routenotes_no_page=no_page,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.abspath(os.path.join(HERE, "..", "..")),
                    help="数译仓库根目录（含 08_source_code）")
    ap.add_argument("--out", default=None, help="输出 TSV 路径")
    args = ap.parse_args()

    kit = load_kit()
    src = os.path.join(args.root, "08_source_code")
    if not os.path.isdir(src):
        sys.exit(f"找不到 {src}")

    rows = []
    for name in sorted(os.listdir(src)):
        p = os.path.join(src, name)
        if not os.path.isdir(p) or name.startswith((".", "_")):
            continue
        r = audit_project(kit, p)
        if r is None:
            rows.append((name, None))
            continue
        rows.append((name, r))

    out = args.out or os.path.join(args.root, "03_translations_meta", "译注审计_2026-11-14.tsv")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write("工程\t块数\t汉字数\t译注数\t缺来源\t来源覆盖率%\t密度(条/千字)\t黑名单\t悬空ref\t路线注\t路线注缺页码\n")
        for name, r in rows:
            if r is None:
                f.write(f"{name}\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n")
                continue
            cov = (100.0 * (r["notes"] - r["missing"]) / r["notes"]) if r["notes"] else None
            f.write("\t".join([
                name, str(r["chunks"]), str(r["cjk"]), str(r["notes"]), str(r["missing"]),
                (f"{cov:.1f}" if cov is not None else "-"), f"{r['density']:.2f}", str(r["black"]),
                str(r["dangling"]), str(r["routenotes"]), str(r["routenotes_no_page"]),
            ]) + "\n")

    ok = [r for _, r in rows if r]
    tot_notes = sum(r["notes"] for r in ok)
    tot_missing = sum(r["missing"] for r in ok)
    tot_cjk = sum(r["cjk"] for r in ok)
    print(f"巡检工程：{len(rows)}（有源码 {len(ok)}）")
    print(f"汉字：{tot_cjk:,}｜译注：{tot_notes:,}｜缺来源：{tot_missing:,} "
          f"（覆盖率 {100.0 * (tot_notes - tot_missing) / tot_notes:.1f}%）" if tot_notes else "")
    print(f"黑名单命中：{sum(r['black'] for r in ok)}｜悬空 ref：{sum(r['dangling'] for r in ok)}"
          f"｜路线注：{sum(r['routenotes'] for r in ok)}（缺页码 {sum(r['routenotes_no_page'] for r in ok)}）")
    print(f"明细：{out}")


if __name__ == "__main__":
    main()
