#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""check_sections.py — SY02-46 分节自检（译手交付闸门 + 主控总检）

用法：
    python check_sections.py 5      # 检查 s05
    python check_sections.py all    # 检查全部已有 sNN-*.tex

检查项：
  1. 文件存在，且首个非注释命令是 \\section{
  2. 禁用命令：\\ref \\eqref \\label \\cite \\pageref \\autoref \\nocite \\bibliography
  3. 环境 begin/end 配对；花括号平衡；$ 与 $$ 奇偶；\\[ \\] 配对
  4. 页锚 \\srcpage{N}：落在该节印刷页范围内、单调不减、且覆盖范围内每一页
  5. 编号条目：类型序列与 sections.json 的 seq 完全一致（数量+类型+先后）
  6. 条目编号未被手写（第 0 节的 (0.n) 例外，写在可选参数里是原文体例）
"""
import json
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]          # 工程根
SECT = ROOT / "源码" / "sections"
WORK = ROOT / "工程文件" / "work"
SECTIONS_JSON = WORK / "sections.json"

ENV_OF = {
    "Theorem": "theorem",
    "Definition": "definition",
    "Lemma": "lemma",
    "Proposition": "proposition",
    "Corollary": "corollary",
    "Remark": "remark",
    "DefinitionZ": "definitionZ",
    "LemmaZ": "lemmaZ",
}
ENVS = set(ENV_OF.values())

FORBIDDEN = [r"\\ref\b", r"\\eqref\b", r"\\label\b", r"\\cite\b",
             r"\\pageref\b", r"\\autoref\b", r"\\nocite\b", r"\\bibliography\b"]

COMMENT = re.compile(r"(?<!\\)%.*$")


def strip_comments(text: str) -> str:
    return "\n".join(COMMENT.sub("", ln) for ln in text.splitlines())


def find_file(nn: int):
    hits = sorted(SECT.glob(f"s{nn:02d}-*.tex"))
    return hits[0] if hits else None


def load_sections():
    return {s["sec"]: s for s in json.loads(SECTIONS_JSON.read_text(encoding="utf-8"))}


def check_one(nn: int, meta, verbose=True) -> list:
    errs = []
    f = find_file(nn)
    if f is None:
        return [f"s{nn:02d}: 找不到文件 源码/sections/s{nn:02d}-*.tex"]
    raw = f.read_text(encoding="utf-8")
    txt = strip_comments(raw)

    # 1. section 命令
    if not re.search(r"\\section\*?\{", txt):
        errs.append("缺少 \\section{...}")
    else:
        head = txt[: txt.find("\\section")]
        if len(head.strip()) > 0:
            errs.append(f"\\section 之前有多余内容：{head.strip()[:60]!r}")

    # 2. 禁用命令
    for pat in FORBIDDEN:
        for m in re.finditer(pat, txt):
            ln = txt[: m.start()].count("\n") + 1
            errs.append(f"第 {ln} 行出现禁用命令 {m.group(0)}")

    # 3. 环境配对
    stack = []
    for m in re.finditer(r"\\(begin|end)\{([^}]*)\}", txt):
        kind, name = m.group(1), m.group(2).strip()
        ln = txt[: m.start()].count("\n") + 1
        if kind == "begin":
            stack.append((name, ln))
        else:
            if not stack:
                errs.append(f"第 {ln} 行多余 \\end{{{name}}}")
            elif stack[-1][0] != name:
                errs.append(f"第 {ln} 行 \\end{{{name}}} 与第 {stack[-1][1]} 行 "
                            f"\\begin{{{stack[-1][0]}}} 不配对")
                stack.pop()
            else:
                stack.pop()
    for name, ln in stack:
        errs.append(f"第 {ln} 行 \\begin{{{name}}} 未闭合")

    # 花括号平衡（去掉 \{ \} 与 \$）
    t2 = re.sub(r"\\[{}]", "", txt)
    if t2.count("{") != t2.count("}"):
        errs.append(f"花括号不平衡：{{ {t2.count('{')} 个，}} {t2.count('}')} 个")
    # 数学模式
    t3 = re.sub(r"\\\$", "", t2)
    if t3.count("$") % 2 != 0:
        errs.append(f"$ 个数为奇数（{t3.count('$')}），数学模式未闭合")
    if len(re.findall(r"\\\[", t3)) != len(re.findall(r"\\\]", t3)):
        errs.append("\\[ 与 \\] 数量不等")

    # 4. 页锚
    pages_meta = meta.get("pages") or []
    if pages_meta:
        start, end = pages_meta[0], pages_meta[-1]
        anchors = [int(x) for x in re.findall(r"\\srcpage\{(\d+)\}", txt)]
        if not anchors:
            errs.append(f"没有任何 \\srcpage（应为 {start}–{end}）")
        else:
            if anchors[0] != start:
                errs.append(f"首个页锚是 {anchors[0]}，该节起始页应为 {start}")
            for a, b in zip(anchors, anchors[1:]):
                if b < a:
                    errs.append(f"页锚逆序：{a} 之后出现 {b}")
            out = [a for a in anchors if a < start or a > end]
            if out:
                errs.append(f"页锚越界（该节 {start}–{end}）：{sorted(set(out))}")
            missing = [p for p in range(start, end + 1) if p not in anchors]
            if missing:
                errs.append(f"缺少页锚：{missing}")

    # 5. 条目类型序列
    got = [(m.group(1), txt[: m.start()].count("\n") + 1)
           for m in re.finditer(r"\\begin\{(" + "|".join(sorted(ENVS)) + r")\}", txt)]
    want = [(ENV_OF[t], num) for t, num in meta.get("seq", [])]
    got_types = [g[0] for g in got]
    want_types = [w[0] for w in want]
    if got_types != want_types:
        i = 0
        while i < min(len(got_types), len(want_types)) and got_types[i] == want_types[i]:
            i += 1
        g = f"{got_types[i]}(第{got[i][1]}行)" if i < len(got_types) else "（无）"
        w = f"{want_types[i]}({want[i][1]})" if i < len(want_types) else "（无）"
        errs.append(f"条目序列不符：第 {i+1} 个应为 {w}，实际 {g}；"
                    f"共 {len(got_types)} 条，应为 {len(want_types)} 条")

    # 6. 手写编号（第 0 节的 (0.n) 例外）
    for m in re.finditer(r"\\begin\{(?:" + "|".join(sorted(ENVS)) + r")\}\[([^\]]*)\]", txt):
        note = m.group(1).strip()
        if re.match(r"\(\s*0\.\d+\s*\)", note):
            continue
        if re.match(r"\s*\d+\.\d+", note):
            ln = txt[: m.start()].count("\n") + 1
            errs.append(f"第 {ln} 行条目可选参数里手写了编号：{note!r}")

    if verbose:
        n_seg = len(re.findall(r"\\srcpage\{", txt))
        n_par = len([p for p in re.split(r"\n\s*\n", txt) if p.strip()])
        n_yz = len(re.findall(r"\\yizhu\{", txt))
        status = "OK " if not errs else "FAIL"
        print(f"[{status}] {f.name}  页锚 {n_seg}  条目 {len(got_types)}/{len(want_types)}  "
              f"译注 {n_yz}  字符 {len(raw)}")
        for e in errs:
            print(f"      - {e}")
    return errs


def main():
    if not SECTIONS_JSON.exists():
        print(f"缺少 {SECTIONS_JSON}")
        return 2
    metas = load_sections()
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    arg = sys.argv[1].strip().lower()
    todo = []
    if arg == "all":
        todo = [n for n in sorted(metas) if find_file(n)]
        if not todo:
            print("还没有任何 sections/*.tex")
            return 1
    else:
        try:
            todo = [int(arg)]
        except ValueError:
            print("参数应为节次整数或 all")
            return 2
    bad = 0
    for nn in todo:
        if nn not in metas:
            print(f"s{nn:02d}: sections.json 里没有这一节")
            bad += 1
            continue
        if check_one(nn, metas[nn]):
            bad += 1
    print()
    if bad:
        print(f"== {bad} 节未通过 ==")
        return 1
    print(f"== 全部 {len(todo)} 节 OK ==")
    return 0


if __name__ == "__main__":
    sys.exit(main())
