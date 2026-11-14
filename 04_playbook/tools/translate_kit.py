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
  python translate_kit.py prep     <pdf> <workdir> [--pages-per-chunk 6] [--offset 0]
  python translate_kit.py budget   <workdir> [--chapter-budget 60000]
  python translate_kit.py contract <project_root> --chunk ch01     # 生成译前契约卡
  python translate_kit.py contract <project_root> --check          # 校验契约已填已审
  python translate_kit.py gate     <project_root> [--legacy]
  python translate_kit.py check    <project_root> [--out check_report.md]

v1.1 新增（见 08_资源受限路线_v1.md）：
  contract —— 把「读完这块要传达什么」逼成 10–15 行可审的接口，开工前冻结；
  gate     —— 除通读/疑点/术语外，新增 definitions.tsv、疑点归因列、契约已审；
  check    —— 新增定理环境数偏差（路线偏离）、\routenote 页码、译注密度。

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


def _chunks_dir(root: str) -> str:
    """译文所在目录：兼容 源码/chunks（新流程）、源码/sections、以及 77 部已交付工程的其他排布。

    顺序：源码/chunks → 源码/sections → chunks → sections → 源码 下第一个含 .tex 的子目录
          → 源码 本身（部分工程把 .tex 平铺在 源码/ 下）。
    """
    for rel in (("源码", "chunks"), ("源码", "sections"), ("chunks",), ("sections",)):
        p = os.path.join(root, *rel)
        if os.path.isdir(p):
            return p
    src = os.path.join(root, "源码")
    if os.path.isdir(src):
        for d in sorted(os.listdir(src)):
            p = os.path.join(src, d)
            if os.path.isdir(p) and any(f.endswith(".tex") for f in os.listdir(p)):
                return p
        if any(f.endswith(".tex") for f in os.listdir(src)):
            return src
    return ""


NOTE_CMDS = ("zhnote", "transnote", "tutornote")


def _iter_notes(t: str):
    """遍历译文里的译注，产出 (起始偏移, 注文)。

    支持命令形式 \\zhnote{…} / \\transnote{…} / \\tutornote{…}（花括号配对计数，允许嵌套）
    与环境形式 \\begin{yizhu}[类别] … \\end{yizhu}。
    """
    for cmd in NOTE_CMDS:
        for m in re.finditer(r"\\" + cmd + r"\s*\{", t):
            i = m.end()
            depth, j = 1, i
            while j < len(t) and depth > 0:
                c = t[j]
                if c == "\\":
                    j += 2
                    continue
                if c == "{":
                    depth += 1
                elif c == "}":
                    depth -= 1
                j += 1
            if depth == 0:
                yield m.start(), t[i:j - 1]
    for m in re.finditer(r"\\begin\{yizhu\}(?:\[[^\]]*\])?(.*?)\\end\{yizhu\}", t, re.S):
        yield m.start(), m.group(1)


def cmd_check(args):
    root = args.root
    chunks_dir = _chunks_dir(root)
    if not chunks_dir:
        print(f"找不到译文目录（试过 源码/chunks、源码/sections、chunks、sections）: {root}")
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
    # 已交付工程实际用的命令是 \transnote{…}（436 条）/ \tutornote{…}（17 条）/ \begin{yizhu} 环境；
    # 新工程统一 \zhnote{…}。三种都要认，否则老工程一跑 check 全是"漏检"。
    missing = 0
    n_notes = 0
    for name, t in texts.items():
        for start, block in _iter_notes(t):
            n_notes += 1
            if not any(k in block for k in ("[来源：", "[译者按", "\\cite{", "[依据：")):
                missing += 1
                line = t[:start].count("\n") + 1
                problems.append(
                    f"[译注无来源] {name}:{line} —— 必须带 [来源：…]、[译者按（无外部依据）…] 或 \\cite{{…}}")
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
    # 7) 路线偏离：定理/定义环境数与原文比对（北大案例里"整块跑偏"的机器版红旗）
    work = _workdir(root)
    orig_n = 0
    pages_dir = os.path.join(work, "pages")
    if os.path.isdir(pages_dir):
        env_head = re.compile(
            r"(?m)^\s*(Theorem|Lemma|Proposition|Corollary|Definition|Example|Remark|Claim|Fact|Notation)\b")
        for f in sorted(os.listdir(pages_dir)):
            if f.endswith(".txt"):
                orig_n += len(env_head.findall(open(os.path.join(pages_dir, f), encoding="utf-8",
                                                    errors="replace").read()))
    tex_n = len(re.findall(
        r"\\begin\{(theorem|lemma|proposition|corollary|definition|example|remark|claim|fact|notation)\}",
        joined, re.I))
    line = f"环境数: 原文 {orig_n} 个定理/定义类标记，译文 {tex_n} 个"
    if orig_n >= 5:
        ratio = tex_n / orig_n
        if ratio < 0.6:
            problems.append(f"[路线偏离] {line}（比值 {ratio:.2f}）——漏译或把定理降级成正文？")
        elif ratio > 1.6:
            problems.append(f"[路线偏离] {line}（比值 {ratio:.2f}）——多出原文没有的定理级结构，检查是否跑偏")

    # 8) \routenote 必须带页码（路线注的作用就是可回查）
    rn = re.compile(r"\\routenote\{((?:[^{}]|\{[^{}]*\})*)\}", re.S)
    rn_bad = 0
    for name, t in texts.items():
        for m in rn.finditer(t):
            if not re.search(r"(p\.\s*\d+|第\s*\d+\s*页|p\.\s*\d+\s*[–-]\s*\d+)", m.group(1)):
                rn_bad += 1
                ln = t[:m.start()].count("\n") + 1
                problems.append(f"[路线注] {name}:{ln} 缺页码——路线注必须能回查原文")

    # 9) 译注密度（他们剪掉一半节点；我们的译注也不该淹了正文）
    hints = []
    cjk = len(CJK.findall(joined))
    if cjk > 2000:
        density = n_notes / (cjk / 1000.0)
        hints.append(f"译注密度 {density:.1f} 条/千字（>3 提示：读者成本高，只注「真会卡住」处）"
                     if density > 3 else f"译注密度 {density:.1f} 条/千字（正常）")

    print(f"检查文件: {len(files)} 个 chunk，{len(joined):,} 字符")
    print(line)
    for h in hints:
        print("  [提示] " + h)
    print(f"路线注: {len(rn.findall(joined))} 条，缺页码 {rn_bad} 条")
    print(f"译注: {n_notes} 条，其中缺来源标记 {missing} 条")
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
            fh.write(f"- chunks: {len(files)}\n- 译注: {n_notes}（缺来源 {missing}）\n")
            fh.write(f"- 问题: {len(problems)}\n\n")
            for p in problems:
                fh.write(f"- {p}\n")
        print(f"报告已写: {args.out}")
    return 1 if problems else 0


CONTRACT_BLOCKED = "⟨待填"
CONTRACT_STATUS = ("未填", "已填", "已审")


def _workdir(root: str) -> str:
    for rel in (os.path.join("工程文件", "work"), "work"):
        p = os.path.join(root, rel)
        if os.path.isdir(p):
            return p
    return os.path.join(root, "工程文件", "work")


def _chunks(work: str) -> list:
    p = os.path.join(work, "chunks.json")
    if not os.path.exists(p):
        return []
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return []


def _chunk_original(work: str, chunk: dict) -> str:
    """取本块原文：优先 pages/pNNN.txt 拼接，退回 fulltext.txt 的相对位置。"""
    out = []
    for n in range(chunk["from"], chunk["to"] + 1):
        p = os.path.join(work, "pages", f"p{n:03d}.txt")
        if os.path.exists(p):
            out.append(open(p, encoding="utf-8", errors="replace").read())
    return "\n".join(out)


def _glossary_hits(work: str, text: str) -> list:
    gl = os.path.join(work, "glossary.tsv")
    if not os.path.exists(gl) or not text:
        return []
    hits, low = [], text.lower()
    for ln in open(gl, encoding="utf-8", errors="replace"):
        r = ln.rstrip("\n").split("\t")
        if len(r) < 2 or not r[0].strip() or r[0].startswith("#"):
            continue
        if r[0].strip().lower() in low:
            hits.append(f"{r[0].strip()} = {r[1].strip()}")
    return hits


def _contract_template(chunk: dict, orig: str, hits: list, chunk_id: str) -> str:
    ids = chunk_id
    head = orig.strip().splitlines()[:3]
    head_txt = " / ".join(x.strip() for x in head if x.strip())[:160]
    hit_lines = "\n".join(f"  - {h}  ⟨核对是否本块首次出现⟩" for h in hits[:12]) or \
        "  - ⟨本块无已知术语命中；若出现新概念在此登记，并同步 definitions.tsv⟩"
    return f"""# 译前契约 {ids}（p{chunk['from']:03d}–p{chunk['to']:03d}）

> 用途：开工**之前**把这一块的接口定死，只审这张卡，不审全文。
> 规则：不允许「见原文」；带 `{CONTRACT_BLOCKED}` 的字段 gate 不认；`状态: 已审` 才准动笔。
> 依据：11_资源受限路线_v1.md §2（冻结接口 + 审阅前移的零预算版）。

- 块范围: p{chunk['from']:03d}–p{chunk['to']:03d}（约 {chunk.get('tokens', 0):,} tok）
- 原文开头: {head_txt}
- 一句话主题: {CONTRACT_BLOCKED}：这一块要读者带走什么（≤40 字）⟩
- 本块断言清单（可独立检查的结论，一条一行）:
  - {CONTRACT_BLOCKED}⟩
- 关键定义（本块首次出现的概念；必须同步进 work/definitions.tsv）:
{hit_lines}
- 记号约定（易混、易漏，尤其是原文默认省略的）:
  - {CONTRACT_BLOCKED}⟩
- 前提与依赖（上一块给了什么、本块必须接受的假设）:
  - {CONTRACT_BLOCKED}⟩
- 公式与图清单（编号 → 处理方式：重排/照抄/裁图）:
  - {CONTRACT_BLOCKED}⟩
- 明确不做的（本块不展开、不引入的概念——防路线漂移）:
  - {CONTRACT_BLOCKED}⟩
- 下游接口（下一块需要本块产出什么）:
  - {CONTRACT_BLOCKED}⟩
- 状态: 未填
- 审阅: ⟨审阅人 日期；`已审` 前必须签字⟩
"""


def _contract_check(path: str) -> list:
    """返回契约未通过的条目。"""
    txt = open(path, encoding="utf-8", errors="replace").read()
    fails = []
    if CONTRACT_BLOCKED in txt:
        n = txt.count(CONTRACT_BLOCKED)
        fails.append(f"还有 {n} 处未填（{CONTRACT_BLOCKED}）")
    # 「状态」在说明行里也会出现���取最后一次（真正的字段在文末）
    st = re.findall(r"状态\s*[:：]\s*([^\s`]+)", txt)
    if not st:
        fails.append("缺 `状态:` 行")
    elif st[-1] not in CONTRACT_STATUS:
        fails.append(f"状态 `{st[-1]}` 不是 {'/'.join(CONTRACT_STATUS)}")
    elif st[-1] != "已审":
        fails.append(f"状态是「{st[-1]}」——契约未审，不准开工")
    rev = re.findall(r"审阅\s*[:：]\s*(.+)", txt)
    if not rev or len(rev[-1].strip()) < 3 or "⟨" in rev[-1] or CONTRACT_BLOCKED in rev[-1]:
        fails.append("审阅签字为空")
    if "本块断言清单" not in txt:
        fails.append("缺「本块断言清单」")
    return fails


def cmd_contract(args):
    root = args.root
    work = _workdir(root)
    plan = _chunks(work)
    cdir = os.path.join(work, "contracts")

    if args.check:
        if not os.path.isdir(cdir):
            print(f"缺目录 {cdir} —— 先跑 contract（不带 --check）生成契约卡")
            return 1
        ids = [c["id"] for c in plan] or [f[:-3] for f in sorted(os.listdir(cdir)) if f.endswith(".md")]
        bad = 0
        print(f"契约校验: {len(ids)} 块")
        for cid in ids:
            p = os.path.join(cdir, f"{cid}.md")
            if not os.path.exists(p):
                print(f"  ✗ {cid}: 缺契约卡")
                bad += 1
                continue
            fs = _contract_check(p)
            if fs:
                bad += 1
                print(f"  ✗ {cid}: " + "；".join(fs))
            else:
                print(f"  ✓ {cid}")
        print("  ✓ 全部契约已填已审" if not bad else f"  未通过 {bad} 块")
        return 1 if bad else 0

    if not plan:
        print(f"缺 {os.path.join(work, 'chunks.json')}，先跑 prep")
        return 2
    os.makedirs(cdir, exist_ok=True)
    todo = [c for c in plan if not args.chunk or c["id"] == args.chunk]
    if args.chunk and not todo:
        print(f"没有块 {args.chunk}；可选: {', '.join(c['id'] for c in plan)}")
        return 2
    print(f"生成译前契约: {len(todo)} 个 → {cdir}")
    for c in todo:
        p = os.path.join(cdir, f"{c['id']}.md")
        if os.path.exists(p) and not args.force:
            print(f"  - {c['id']} 已存在（--force 覆盖）")
            continue
        orig = _chunk_original(work, c)
        hits = _glossary_hits(work, orig)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(_contract_template(c, orig, hits, c["id"]))
        print(f"  + {c['id']}  p{c['from']:03d}-p{c['to']:03d}  术语命中 {len(hits)}")
    print("下一步：把它填完 → 找人审一行 → 改 `状态: 已审` → 再开工。")
    return 0


def cmd_gate(args):
    """G0 开译闸门：通读笔记 + 疑点清单（未解=0）+ 术语表 + definitions + 契约，且都早于落笔。"""
    root = args.root
    work = _workdir(root)
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
        body = [r for r in rows if r and not r[0].startswith("#")]
        if not body:
            fails.append("疑点清单是空的——通读没留下疑点，通常说明没真读")
        else:
            header = body[0]
            ci = next((i for i, h in enumerate(header) if h.strip() in ("状态", "status")), len(header) - 1)
            unresolved = sum(1 for r in body[1:] if len(r) > ci and r[ci].strip() == "未解")
            if unresolved:
                fails.append(f"疑点清单还有 {unresolved} 条「未解」——纪律 §1.0：未解=0 才准开译")
            for col in ("归因", "下一步"):
                if col not in " ".join(header):
                    msg = f"疑点清单缺「{col}」列——卡住时先归因（数学缺口/工程/协调）再动手"
                    (warns if args.legacy else fails).append(msg)

    if not os.path.exists(gl):
        fails.append("缺 工程文件/work/glossary.tsv（术语表）")
    else:
        body = [ln for ln in open(gl, encoding="utf-8") if ln.strip() and not ln.startswith("#")]
        if len(body) < 3:
            fails.append(f"术语表只有 {len(body)} 行，定义/定理名/核心概念必须已入表")

    # definitions.tsv：定义先行（北大经验里最贵的一条，我们零成本版就是这个文件）
    defs = os.path.join(work, "definitions.tsv")
    if not os.path.exists(defs):
        (warns if args.legacy else fails).append(
            "缺 工程文件/work/definitions.tsv——定义先行：没登记定义就等于没定接口")
    else:
        drows = [ln.rstrip("\n").split("\t") for ln in open(defs, encoding="utf-8") if ln.strip()]
        dbody = [r for r in drows if r and not r[0].startswith("#")]
        if len(dbody) < 6:
            (warns if args.legacy else fails).append(
                f"definitions.tsv 只有 {max(0, len(dbody) - 1)} 条定义（至少 5 条：定义/定理名/核心概念）")
        else:
            hi = dbody[0]
            si = next((i for i, h in enumerate(hi) if "来源" in h), None)
            if si is not None:
                filled = sum(1 for r in dbody[1:] if len(r) > si and r[si].strip())
                rate = filled / max(1, len(dbody) - 1)
                if rate < 0.6:
                    warns.append(f"definitions.tsv 来源列填充率 {rate:.0%}（<60%）——定义没出处就没法复核")

    # 译前契约：开工前把接口冻结（每块一张，已审才动笔）
    plan = _chunks(work)
    cdir = os.path.join(work, "contracts")
    if plan:
        if not os.path.isdir(cdir):
            (warns if args.legacy else fails).append(
                "缺 工程文件/work/contracts/——先跑 kit contract 生成每块的译前契约")
        else:
            ready, missing, bad = 0, [], []
            for c in plan:
                p = os.path.join(cdir, f"{c['id']}.md")
                if not os.path.exists(p):
                    missing.append(c["id"])
                    continue
                fs = _contract_check(p)
                if fs:
                    bad.append(f"{c['id']}（{fs[0]}）")
                else:
                    ready += 1
            if bad:
                (warns if args.legacy else fails).append(
                    f"{len(bad)} 块契约未填/未审: " + "；".join(bad[:4]) + ("…" if len(bad) > 4 else ""))
            if ready == 0:
                (warns if args.legacy else fails).append(
                    "没有任何一块契约通过——`已审` 是开工资格，不是形式")
            elif missing:
                warns.append(f"{len(missing)} 块还没有契约卡（{', '.join(missing[:6])}…），开那块之前必须补")

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
    print("  ✓ 通过：通读笔记齐、疑点未解=0、术语与定义已登记、契约已审、通读早于落笔")
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

    p4 = sub.add_parser("gate", help="G0 开译闸门：通读/疑点未解/术语与定义/契约/先后顺序")
    p4.add_argument("root")
    p4.add_argument("--legacy", action="store_true", help="旧工程回填：缺 definitions/契约 只提醒不拦")
    p4.set_defaults(func=cmd_gate)

    p5 = sub.add_parser("contract", help="译前契约卡：生成（默认）或校验（--check）")
    p5.add_argument("root")
    p5.add_argument("--chunk", default="", help="只生成某一块，如 ch01")
    p5.add_argument("--check", action="store_true", help="校验所有契约是否已填已审")
    p5.add_argument("--force", action="store_true", help="覆盖已存在的契约卡")
    p5.set_defaults(func=cmd_contract)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
