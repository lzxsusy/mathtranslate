#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""编号陈述审计：译文里 \\begin{thm|prop|lem|...}{编号} 的类型分布 vs 底本抽出的 statements.tsv。

statements.tsv 不入仓（由底本自动抽取的中间产物），默认从 ../lp2_work/statements.tsv 读；
可用 --statements 指定路径，缺失时只做译文自检。

用法：python audit_num.py [--statements PATH]
输出：工程文件/reports/numaudit.md
"""
import argparse, io, os, re, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = re.compile(r"ch-a(\d)-(\d\d)\.tex$")
BEGIN = re.compile(r"\\begin\{(thm|prop|lem|cor|conj|defn|rem|exam|ques|claim|notn|hyp|fact|prob)\}\{([^}]*)\}")
TYPE_ZH = {"thm": "Theorem", "prop": "Proposition", "lem": "Lemma", "cor": "Corollary",
           "conj": "Conjecture", "defn": "Definition", "rem": "Remark", "exam": "Example",
           "ques": "Question", "claim": "Claim", "notn": "Notation", "hyp": "Hypothesis",
           "fact": "Fact", "prob": "Problem"}


def load_expected(path):
    if not path or not os.path.exists(path):
        return None
    cnt = Counter()
    for i, line in enumerate(io.open(path, encoding="utf-8")):
        if i == 0:
            continue
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 2:
            continue
        cnt[parts[1].strip()] += 1
    return cnt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--statements", default=os.path.join(os.path.expanduser("~"), "Downloads", "lp2_work", "statements.tsv"))
    args = ap.parse_args()

    chunk_dir = os.path.join(ROOT, "源码", "chunks")
    files = sorted(fn for fn in os.listdir(chunk_dir) if CH.match(fn))
    got = Counter()
    per = []
    for fn in files:
        txt = io.open(os.path.join(chunk_dir, fn), encoding="utf-8").read()
        items = BEGIN.findall(txt)
        for k, _ in items:
            got[TYPE_ZH[k]] += 1
        per.append((fn, len(items)))
    exp = load_expected(args.statements)

    lines = ["# 编号陈述审计", ""]
    lines.append("| 块 | 编号陈述数 |")
    lines.append("|---|---|")
    for fn, n in per:
        lines.append("| %s | %d |" % (fn, n))
    lines += ["", "## 类型分布", "", "| 类型 | 译文 | 底本 | 差 |", "|---|---|---|---|"]
    keys = sorted(set(got) | set(exp or {}), key=lambda k: -(got.get(k, 0)))
    for k in keys:
        g = got.get(k, 0)
        e = (exp or {}).get(k, 0)
        lines.append("| %s | %d | %d | %+d |" % (k, g, e, g - e))
    lines += ["", "## 汇总", ""]
    lines.append("- 译文编号陈述合计：%d" % sum(got.values()))
    if exp:
        lines.append("- 底本编号陈述合计：%d" % sum(exp.values()))
        lines.append("- 检出率：%.1f%%（译文/底本；差额主要来自尚未落盘的块）" % (100.0 * sum(got.values()) / max(1, sum(exp.values()))))
    else:
        lines.append("- 底本 statements.tsv 不可用，仅统计译文")

    out = os.path.join(ROOT, "工程文件", "reports", "numaudit.md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    io.open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
    print("blocks=%d stmt=%d -> %s" % (len(files), sum(got.values()), out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
