#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""translate_kit.py — 数译流程提效工具 v1（配合 06_流程提效_v1.md）

设计目标：在不破坏「先通读、后落笔」纪律的前提下，把每部译注工程
的计费 token 压下来。手段只有三个：
  1) prep   —— 把 PDF 一次性拆成文本页 + 全文单文件 + 分章计划（省掉逐页 read 的轮次）；
  2) budget —— 在建会话之前算清楚每章要吃掉多少输入 token，超预算就重新切块；
  3) check  —— 把纪律里能机器判的部分（黑名单、译注来源、悬空引用、中文标点、TODO）
               全部脚本化，别让模型用眼睛逐条核对。

用法：
  python translate_kit.py prep   <pdf> <workdir> [--pages-per-chunk 6] [--offset 0]
  python translate_kit.py budget <workdir> [--chapter-budget 60000]
  python translate_kit.py check  <project_root> [--out check_report.md]

目录约定（与 playbook_agent.md 一致）：
  <workdir>/pages/pNNN.txt      逐页文本，带 ===== BOOK PAGE n (PDF m) ===== 标记
  <workdir>/fulltext.txt        全文单文件（通读只读这一个文件，1 次 read）
  <workdir>/pages.json          每页字符数 / token 估计
  <workdir>/chunks.json         分章计划（页范围 + token 估计）
"""
import argparse
import json
import os
import re
import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

CJK = re.compile(r"[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]")


def est_tokens(text: str) -> int:
    """粗估 token：中文按 1.6 字/token，其余按 3.6 字符/token。只用于预算，不用于计费。"""
    cjk = len(CJK.findall(text))
    other = max(0, len(text) - cjk)
    return int(cjk / 1.6 + other / 3.6) + 1


def cmd_prep(args):
    import pymupdf  # noqa: F401  (runtime 自带 pymupdf)

    pdf, work = args.pdf, args.workdir
    os.makedirs(os.path.join(work, "pages"), exist_ok=True)
    doc = pymupdf.open(pdf)
    offset = args.offset
    pages = []
    full = []
    for i in range(doc.page_count):
        book = i + 1 - offset
        text = doc[i].get_text("text")
        text = text.replace("\r\n", "\n").strip()
        marker = f"===== BOOK PAGE {book} (PDF {i + 1}) ====="
        body = f"{marker}\n{text}\n"
        p = os.path.join(work, "pages", f"p{book:03d}.txt")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(body)
        pages.append({"book": book, "pdf": i + 1, "chars": len(text), "tokens": est_tokens(text)})
        full.append(body)

    with open(os.path.join(work, "pages.json"), "w", encoding="utf-8") as fh:
        json.dump({"pdf": pdf, "offset": offset, "pages": pages}, fh, ensure_ascii=False, indent=1)

    fulltext = "\n".join(full)
    with open(os.path.join(work, "fulltext.txt"), "w", encoding="utf-8") as fh:
        fh.write(fulltext)

    # 分章计划：按页分组（默认 6 页/块），--chunks 可手写覆盖
    if args.chunks:
        ranges = []
        for part in args.chunks.split(","):
            a, b = part.split("-")
            ranges.append((int(a), int(b)))
    else:
        step = max(1, args.pages_per_chunk)
        ranges = [(s, min(s + step - 1, len(pages))) for s in range(1, len(pages) + 1, step)]

    plan = []
    for idx, (a, b) in enumerate(ranges, 1):
        chunk = [p for p in pages if a <= p["book"] <= b]
        txt = "\n".join(full[p["pdf"] - 1] for p in chunk)
        plan.append({"id": f"ch{idx:02d}", "from": a, "to": b,
                     "chars": sum(p["chars"] for p in chunk),
                     "tokens": est_tokens(txt)})
    with open(os.path.join(work, "chunks.json"), "w", encoding="utf-8") as fh:
        json.dump(plan, fh, ensure_ascii=False, indent=1)

    total_tokens = sum(p["tokens"] for p in pages)
    print(f"PDF: {pdf}")
    print(f"页数: {len(pages)}  全书 token 估计: {total_tokens:,}")
    print(f"全文单文件: {os.path.join(work, 'fulltext.txt')}  ({len(fulltext):,} 字符)")
    print(f"分块: {len(plan)} 块")
    for c in plan:
        print(f"  {c['id']}  p{c['from']:03d}-p{c['to']:03d}  {c['chars']:6,} 字符  ~{c['tokens']:6,} tok")
    print("下一页：把 fulltext.txt 一次读完做通读（不要逐页 read）；通读笔记与疑点清单落 work/。")
    return 0


def cmd_budget(args):
    work = args.workdir
    cp = os.path.join(work, "chunks.json")
    if not os.path.exists(cp):
        print(f"缺 {cp}，先跑 prep")
        return 2
    plan = json.load(open(cp, encoding="utf-8"))
    notes = os.path.join(work, "通读笔记.md")
    glossary = os.path.join(work, "glossary.tsv")
    notes_tok = est_tokens(open(notes, encoding="utf-8").read()) if os.path.exists(notes) else 0
    gl_tok = est_tokens(open(glossary, encoding="utf-8").read()) if os.path.exists(glossary) else 0
    FIXED = 1200  # 纪律摘要 + 任务书 + 衔接卡 + 余量
    print(f"固定前缀: 纪律摘要+任务书≈{FIXED} + 通读笔记 {notes_tok} + 术语表 {gl_tok} = {FIXED + notes_tok + gl_tok:,} tok")
    over = []
    total = 0
    for c in plan:
        need = FIXED + notes_tok + gl_tok + c["tokens"] + 800
        total += need
        flag = "  <== 超预算" if need > args.chapter_budget else ""
        print(f"  {c['id']}  p{c['from']:03d}-p{c['to']:03d}  约 {need:6,} tok{flag}")
        if need > args.chapter_budget:
            over.append(c["id"])
    print(f"全部章节输入合计约 {total:,} tok（这是所有章节会话输入之和，不是单次）")
    if over:
        print(f"超预算块: {', '.join(over)} —— 请缩小分块或先压缩通读笔记/术语表，不要靠'到聊天里再压'。")
        return 1
    return 0


def _strip_math(tex: str) -> str:
    tex = re.sub(r"\$[^$]*\$", " ", tex, flags=re.S)
    tex = re.sub(r"\\\[.*?\\\]", " ", tex, flags=re.S)
    tex = re.sub(r"\\begin\{(equation|align|eqnarray|gather|multline)\*?\}.*?\\end\{\1\*?\}", " ", tex, flags=re.S)
    tex = re.sub(r"%.*", " ", tex)
    return tex


def cmd_check(args):
    root = args.root
    chunks_dir = os.path.join(root, "源码", "chunks")
    if not os.path.isdir(chunks_dir):
        chunks_dir = os.path.join(root, "chunks")
    if not os.path.isdir(chunks_dir):
        print(f"找不到 chunks 目录: {root}\\源码\\chunks")
        return 2
    glossary = args.glossary or os.path.join(root, "工程文件", "work", "glossary.tsv")
    files = [os.path.join(chunks_dir, f) for f in sorted(os.listdir(chunks_dir)) if f.endswith(".tex")]
    texts = {os.path.basename(f): open(f, encoding="utf-8", errors="replace").read() for f in files}
    joined = "\n".join(texts.values())

    problems = []

    # 1) 来源黑名单
    blacklist = ["知乎", "百度百科", "CSDN", "简书", "博客园"]
    for name, t in texts.items():
        for kw in blacklist:
            for m in re.finditer(kw, t):
                line = t[:m.start()].count("\n") + 1
                problems.append(f"[黑名单] {name}:{line} 出现「{kw}」——纪律 §2.5.9：不得进入任何工作文件")

    # 2) 译注来源标记
    zhnote = re.compile(r"\\zhnote\{(.*?)\n?\}", re.S)
    missing = 0
    for name, t in texts.items():
        for m in zhnote.finditer(t):
            block = m.group(1)
            if "[来源：" not in block and "[译者按" not in block:
                missing += 1
                line = t[:m.start()].count("\n") + 1
                problems.append(f"[译注无来源] {name}:{line} —— 必须带 [来源：…] 或 [译者按（无外部依据）…]")
    # 3) 悬空引用
    labels = set(re.findall(r"\\label\{([^}]+)\}", joined))
    refs = set(re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", joined))
    for r in sorted(refs - labels):
        problems.append(f"[悬空引用] \\ref{{{r}}} 没有对应 \\label")

    # 4) 中文里的半角标点
    for name, t in texts.items():
        bare = _strip_math(t)
        for m in re.finditer(r"[\u4e00-\u9fff][,;:!?][\u4e00-\u9fff]", bare):
            line = bare[:m.start()].count("\n") + 1
            problems.append(f"[标点] {name}:{line} 中文之间用了半角标点")
            if sum(1 for p in problems if p.startswith("[标点]")) >= 20:
                break

    # 5) 残留 TODO / 待补
    for name, t in texts.items():
        for m in re.finditer(r"(TODO|FIXME|待补|待核|XXX|\?\?\?)", t):
            line = t[:m.start()].count("\n") + 1
            problems.append(f"[残留] {name}:{line} 「{m.group(0)}」")
            if sum(1 for p in problems if p.startswith("[残留]")) >= 20:
                break

    # 6) 术语表覆盖率（只提示，不判错）
    uncovered = []
    if os.path.exists(glossary):
        rows = [ln.strip().split("\t") for ln in open(glossary, encoding="utf-8") if ln.strip()]
        rows = [r for r in rows if len(r) >= 2 and not r[0].startswith("#")]
        for r in rows:
            en, zh = r[0], r[1]
            if en and en.lower() not in joined.lower() and zh and zh not in joined:
                uncovered.append(f"{en} → {zh}")
    print(f"检查文件: {len(files)} 个 chunk，{len(joined):,} 字符")
    print(f"译注: {len(zhnote.findall(joined))} 条，其中缺来源标记 {missing} 条")
    print(f"术语表条目: {len(rows) if os.path.exists(glossary) else '（缺 glossary.tsv）'}"
          + (f"，未在译文中出现的: {len(uncovered)}" if uncovered else ""))
    if problems:
        print(f"\n发现 {len(problems)} 条问题:")
        for p in problems[:80]:
            print("  " + p)
        if len(problems) > 80:
            print(f"  … 另有 {len(problems) - 80} 条")
    else:
        print("\n全部通过：黑名单 0、译注来源 0 缺失、引用闭合、无残留标记。")
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write("# 静态检查报告\n\n")
            fh.write(f"- chunks: {len(files)}\n- 译注: {len(zhnote.findall(joined))}（缺来源 {missing}）\n")
            fh.write(f"- 问题: {len(problems)}\n\n")
            for p in problems:
                fh.write(f"- {p}\n")
        print(f"报告已写: {args.out}")
    return 1 if problems else 0


def cmd_gate(args):
    """G0 开译闸门：通读笔记 + 疑点清单（未解=0）+ 术语表，且通读早于任何 chunk。"""
    root = args.root
    work = os.path.join(root, "工程文件", "work")
    notes = os.path.join(work, "通读笔记.md")
    doubts = os.path.join(work, "疑点清单.tsv")
    gl = os.path.join(work, "glossary.tsv")
    fails, warns = [], []

    if not os.path.exists(notes):
        fails.append("缺 工程文件/work/通读笔记.md")
    else:
        txt = open(notes, encoding="utf-8", errors="replace").read()
        if len(txt.strip()) < 300:
            fails.append(f"通读笔记太短（{len(txt.strip())} 字符），四节内容不齐")
        for key in ("主旨", "论证", "体裁", "阅读顺序"):
            if key not in txt:
                warns.append(f"通读笔记里没看到「{key}」小标题")

    unresolved = 0
    if not os.path.exists(doubts):
        fails.append("缺 工程文件/work/疑点清单.tsv")
    else:
        rows = [ln.rstrip("\n").split("\t") for ln in open(doubts, encoding="utf-8") if ln.strip()]
        body = [r for r in rows if not r[0].startswith("#")]
        unresolved = sum(1 for r in body if r and r[-1].strip() == "未解")
        if unresolved:
            fails.append(f"疑点清单还有 {unresolved} 条「未解」——纪律 §1.0：未解=0 才准开译")

    if not os.path.exists(gl):
        fails.append("缺 工程文件/work/glossary.tsv（术语表）")
    else:
        body = [ln for ln in open(gl, encoding="utf-8") if ln.strip() and not ln.startswith("#")]
        if len(body) < 3:
            fails.append(f"术语表只有 {len(body)} 行，定义/定理名/核心概念必须已入表")

    chunks_dir = os.path.join(root, "源码", "chunks")
    if os.path.isdir(chunks_dir):
        tex = [os.path.join(chunks_dir, f) for f in os.listdir(chunks_dir) if f.endswith(".tex")]
        if tex and os.path.exists(notes):
            first = min(os.path.getmtime(p) for p in tex)
            if os.path.getmtime(notes) > first:
                fails.append("通读笔记的修改时间晚于最早的 chunks/*.tex——纪律 §1.0.4：必须先通读后落笔")

    print(f"G0 闸门: {root}")
    for w in warns:
        print("  [提醒] " + w)
    if fails:
        print(f"  未通过（{len(fails)} 项）:")
        for f in fails:
            print("   ✗ " + f)
        return 1
    print("  ✓ 通过：通读笔记齐、疑点未解=0、术语表就绪、通读早于落笔")
    return 0


def main():
    ap = argparse.ArgumentParser(description="数译流程提效工具")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("prep", help="PDF → 逐页文本 + 全文 + 分块计划")
    p1.add_argument("pdf")
    p1.add_argument("workdir")
    p1.add_argument("--pages-per-chunk", type=int, default=6)
    p1.add_argument("--offset", type=int, default=0, help="原书页 = PDF 页 - offset")
    p1.add_argument("--chunks", default="", help="手写分块，如 1-8,9-16,17-24")
    p1.set_defaults(func=cmd_prep)

    p2 = sub.add_parser("budget", help="按分块计划估算每章输入 token")
    p2.add_argument("workdir")
    p2.add_argument("--chapter-budget", type=int, default=60000)
    p2.set_defaults(func=cmd_budget)

    p3 = sub.add_parser("check", help="静态检查：黑名单/译注来源/引用/标点/残留")
    p3.add_argument("root")
    p3.add_argument("--glossary", default="")
    p3.add_argument("--out", default="")
    p3.set_defaults(func=cmd_check)

    p4 = sub.add_parser("gate", help="G0 开译闸门：通读笔记/疑点未解/术语表/先后顺序")
    p4.add_argument("root")
    p4.set_defaults(func=cmd_gate)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
