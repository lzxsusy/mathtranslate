#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble survey-v1 drafts into the final encyclopedia page.

Reads s1..s5, extracts sections / card tables / source tables / mermaid /
pitfalls, normalizes relative links to the final page position
(datasets/encyclopedia/pages/geometric-langlands.md), and writes
work/survey-v1/merged.md for review.  No draft file is modified.
"""
import hashlib
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAGES = HERE.parent.parent            # datasets/encyclopedia/pages
ROOT = PAGES.parents[2]               # repo root

DRAFTS = [
    "s1-intro-spectral.md",
    "s2-statement.md",
    "s3-hecke-spectral-action.md",
    "s4-proof-map.md",
    "s5-proof-details-status.md",
]

AUX_PREFIXES = ("本节资料卡", "出处对照", "思维导图", "易错点与待核",
                "交稿前自检", "本节要回答")

# work dirs inside datasets/ ; top-level dirs at repo root
DATASET_WORKS = ("benzvi_glc", "glc", "glc1", "raskin_glc", "sy0246",
                 "leanstmt", "encyclopedia")


def heading(line):
    m = re.match(r"^(#{2,4})\s+(.*)$", line)
    return (len(m.group(1)), m.group(2).strip()) if m else (0, "")


def link_targets(text):
    for m in re.finditer(r"\]\((?:<([^>]+)>|([^)\s]+))\)", text):
        yield m.group(0), (m.group(1) or m.group(2))


def fix_target(tgt):
    """Rewrite a repo link so it resolves from datasets/encyclopedia/pages/."""
    if tgt.startswith(("#", "http://", "https://", "mailto:")):
        return tgt
    core = tgt
    frag = ""
    if "#" in core:
        core, frag = core.split("#", 1)
        frag = "#" + frag
    segs = [s for s in core.split("/") if s not in ("", ".")]
    # drop all leading '..'
    while segs and segs[0] == "..":
        segs.pop(0)
    if not segs:
        return tgt
    head = segs[0]
    if head == "08_source_code":
        new = "/".join(["..", "..", ".."] + segs)
    elif head in DATASET_WORKS:
        new = "/".join(["..", ".."] + segs)
    elif head == "datasets":
        new = "/".join(["..", ".."] + segs[1:])
    elif head == "entries":
        new = "/".join([".."] + segs)
    else:
        new = "/".join(["..", ".."] + segs)
    return new + frag


def fix_links(text):
    def repl(m):
        whole, tgt = m.group(0), (m.group(1) or m.group(2))
        new = fix_target(tgt)
        if new == tgt:
            return whole
        if m.group(1) is not None:
            return "](<%s>)" % new if (" " in new or "（" in new) else "](%s)" % new
        return "](%s)" % new
    return re.sub(r"\]\((?:<([^>]+)>|([^)\s]+))\)", repl, text)


def parse_draft(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    units = []          # dicts: kind, level, title, lines
    cur = {"kind": "preamble", "level": 0, "title": "", "lines": []}
    units.append(cur)
    for ln in lines:
        lvl, title = heading(ln)
        if lvl:
            if title.startswith("本节要回答") or title.startswith("交稿前自检"):
                cur = {"kind": "drop", "level": lvl, "title": title, "lines": []}
            elif title.startswith("本节资料卡"):
                cur = {"kind": "cards", "level": lvl, "title": title, "lines": []}
            elif title.startswith("出处对照"):
                cur = {"kind": "sources", "level": lvl, "title": title, "lines": []}
            elif title.startswith("思维导图"):
                cur = {"kind": "mermaid", "level": lvl, "title": title, "lines": []}
            elif title.startswith("易错点与待核"):
                cur = {"kind": "pitfalls", "level": lvl, "title": title, "lines": []}
            elif title.startswith("附录 A"):
                cur = {"kind": "chrono", "level": lvl, "title": title, "lines": []}
            elif title.startswith("§"):
                cur = {"kind": "section", "level": lvl, "title": title, "lines": []}
            elif title.startswith("本节思路图"):
                cur = {"kind": "mermaid", "level": lvl, "title": title, "lines": []}
            else:
                cur = {"kind": "sub", "level": lvl, "title": title, "lines": []}
            units.append(cur)
        else:
            cur["lines"].append(ln)
    return units


def section_no(title_or_ctx):
    m = re.search(r"§\s*(\d)", title_or_ctx)
    if m:
        return int(m.group(1))
    m = re.match(r"^(\d)(?:\.\d)?\s", title_or_ctx)
    if m:
        return int(m.group(1))
    return None


def parse_table(block_lines):
    rows = []
    for ln in block_lines:
        s = ln.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if not cells:
            continue
        if all(re.fullmatch(r":?-{2,}:?", c.replace(" ", "")) for c in cells if c):
            continue
        if cells[0] in ("概念", "简称", "卡 id", "记号"):
            continue
        rows.append(cells)
    return rows


def main():
    all_cards = {}       # id -> dict(title, path, pages, sections=set)
    order = []           # card ids in first-appearance order
    sources = {}         # short -> (file_cell, page_basis)
    pitfalls = {}        # section no -> [错误用法 bullet]
    todo = {}            # section no -> [待核事项]
    err = pitfalls       # alias
    mermaids = {}        # section no -> code block text
    bodies = {}          # section no -> list of markdown lines (already normalized)
    chrono = []

    for fname in DRAFTS:
        units = parse_draft(HERE / fname)
        cur_sec = None
        for u in units:
            if u["kind"] in ("section", "sub"):
                n = section_no(u["title"])
                if n is not None:
                    cur_sec = n
            if u["kind"] in ("section", "sub"):
                if cur_sec is None:
                    continue
                out = bodies.setdefault(cur_sec, [])
                title = u["title"]
                if u["kind"] == "section":
                    # '## §3 为什么成立' -> '## 3 为什么成立'
                    t = re.sub(r"^§\s*(\d)\s*", r"\1 ", title)
                    out.append("## " + t.strip())
                else:
                    if u["level"] == 2:
                        out.append("### " + title)
                    else:
                        out.append("#" * u["level"] + " " + title)
                out.extend(u["lines"])
            elif u["kind"] == "cards":
                for cells in parse_table(u["lines"]):
                    if len(cells) < 3:
                        continue
                    title = cells[0].strip("*")
                    cid = cells[1].strip("` ")
                    path = cells[2]
                    m = re.search(r"\]\((?:<([^>]+)>|([^)\s]+))\)", path)
                    lpath = (m.group(1) or m.group(2)) if m else path.strip("` ")
                    page = cells[3] if len(cells) > 3 else ""
                    sec = section_no(u["title"]) or cur_sec
                    d = all_cards.setdefault(cid, {"title": title, "path": lpath,
                                                   "pages": page, "sections": set()})
                    if sec is not None:
                        d["sections"].add(sec)
                    if not d["pages"] and page:
                        d["pages"] = page
                    if cid not in order:
                        order.append(cid)
            elif u["kind"] == "sources":
                for cells in parse_table(u["lines"]):
                    if len(cells) < 3:
                        continue
                    short = cells[0].strip("*` ")
                    short = re.sub(r"\s*(（.*|\(.*|§.*|p\..*)$", "", short).strip()
                    f = cells[1]
                    basis = cells[2]
                    has_link = "](" in f
                    old = sources.get(short)
                    if old is None or (has_link and "](" not in old[0]):
                        sources[short] = (f, basis)
            elif u["kind"] == "mermaid":
                block = "\n".join(u["lines"]).strip()
                m = re.search(r"```mermaid.*?```", block, re.S)
                if m:
                    mermaids[cur_sec] = m.group(0)
            elif u["kind"] == "pitfalls":
                sec = section_no(u["title"]) or cur_sec
                mode = "err"
                for ln in u["lines"]:
                    s = ln.strip()
                    if not s or s.startswith("#") or s.startswith("> "):
                        continue
                    if "待核" in s and len(s) < 30:
                        mode = "todo"
                        continue
                    if s.startswith("- "):
                        text = s[2:].strip()
                        head = text[:14]
                        if "待核" in head:
                            mode_t = "todo"
                            text = re.sub(r"^\*\*待核\*\*\s*[：:]?\s*", "", text)
                        elif text.startswith("**易错**"):
                            mode_t = "err"
                            text = text[6:].lstrip("：: ").strip()
                        else:
                            mode_t = mode
                        (err if mode_t == "err" else todo).setdefault(sec, []).append(text)
                    else:
                        m = re.match(r"^\d+\.\s+(.*)$", s)
                        if m:
                            (err if mode == "err" else todo).setdefault(sec, []).append(m.group(1))
            elif u["kind"] == "chrono":
                chrono = [l for l in u["lines"]]

    # s4 was written without a '## §5' wrapper: give it one
    if 5 in bodies and not any(l.strip().startswith("## 5 ") for l in bodies[5]):
        bodies[5] = ["## 5 证明地图：五篇论文与 Scholze 路线", ""] + bodies[5]

    # normalise every body block
    for sec, lines in bodies.items():
        bodies[sec] = fix_links("\n".join(lines)).splitlines()

    # cards index: fill missing meta from cards.tsv and compute hashes
    tsv = {}
    for ln in (HERE / "cards.tsv").read_text(encoding="utf-8").splitlines()[1:]:
        c = ln.split("\t")
        if len(c) >= 5:
            tsv[c[0]] = {"work": c[1], "track": c[2], "title": c[3],
                         "pages": c[4], "path": c[5] if len(c) > 5 else ""}
    compiled = []
    for cid in order:
        d = all_cards[cid]
        meta = tsv.get(cid, {})
        if not d["title"] and meta:
            d["title"] = meta["title"]
        if not d["title"]:
            d["title"] = cid
        fp = None
        p = d["path"]
        if p:
            cand = (PAGES / p).resolve()
            if cand.exists():
                fp = cand
        if fp:
            h = hashlib.sha256(fp.read_bytes()).hexdigest()[:16]
            compiled.append((cid, h))

    # ---------------- assemble ----------------
    L = []
    L += ["---",
          "id: page/geometric-langlands",
          "title: 几何 Langlands 对应是什么：从谱定理到五部曲",
          "aliases:",
          "  - 几何 Langlands 纲领",
          "  - 几何 Langlands 对应",
          "  - geometric Langlands correspondence",
          "  - 几何朗兰兹纲领",
          "kind: topic",
          "status: draft",
          "version: 1.0",
          "reviewed_by: []",
          "reviewed_on: 2026-11-27",
          "related:",
          "  - page/kapustin-witten",
          "  - page/langlands-program",
          "entries:",
          "  - geometry/geometric-langlands",
          "  - geometry/bun-n",
          "  - geometry/local-system",
          "  - geometry/hecke-eigensheaf",
          "  - geometry/hecke-correspondence",
          "  - geometry/perverse-sheaf",
          "  - geometry/verdier-duality",
          "  - geometry/geometric-satake",
          "  - geometry/geometric-class-field-theory",
          "  - geometry/picard-variety",
          "  - geometry/abel-jacobi",
          "  - geometry/affine-grassmannian",
          "  - algebra/langlands-correspondence",
          "  - algebra/hecke-operator",
          "parents:",
          "  - page/langlands-program",
          "order: 20",
          "note: 底本 D. Ben-Zvi, What is the Geometric Langlands Correspondence about?（arXiv:2605.23167v1，2026）；证明主线 P. Scholze, Séminaire Bourbaki n°1252（2026）中译；技术细节陈麟 2023 讲义中译与 Laumon 2002 Bourbaki 906 中译。概念旁的 card 宏指向资料卡，〔…〕标记指向仓库内文献页，映射见 §0.6。",
          "compiled_from:",
          ]
    for cid, h in compiled:
        L += ["  - id: %s" % cid, "    hash: %s" % h]
    L += ["---", "",
          "# 几何 Langlands 对应是什么：从谱定理到五部曲", "",
          "> 本页是新版综述（v1.0，2026-11-27）。底本 Ben-Zvi 2026 负责叙事骨架，Scholze 2026 Bourbaki 1252 中译负责证明主线，陈麟 2023 讲义中译补技术细节，Laumon 2002 与 GLC I–V 作历史层。读法：概念旁的 card 宏打开资料卡；段末的〔…〕是出处，§0.6 给出简称到仓库文件的映射。旧页（以 Laumon 2002 为底本）已归档为 [v0.3](work/geometric-langlands-v0.3-2026-11-27.md)。", ""]

    # section bodies, in numeric order; insert global source table after 0.5
    for sec in sorted(bodies):
        blk = bodies[sec]
        if sec == 0:
            # insert 0.6 before §1 heading
            L.extend(blk)
            L += ["", "### 0.6 引用与页码约定", "",
                  "本页所有〔…〕标记按下列简称书写；点文件名可回到仓库内文献本身。页码约定已按各自 PDF 的页码基准核对过。", "",
                  "| 简称 | 仓库文件 | 页码基准 |", "| --- | --- | --- |"]
            for short, (f, basis) in sources.items():
                L.append("| %s | %s | %s |" % (short, fix_links(f), basis))
            L.append("")
        else:
            L.extend(blk)
            if sec in mermaids:
                L += ["", "### 本节思路图", "", mermaids[sec], ""]
            if pitfalls.get(sec):
                L += ["", "### 易错点", ""]
                for b in pitfalls[sec]:
                    L.append("- " + fix_links(b))
                L.append("")

    TITLES = {0: "0 导读", 1: "1 这是什么类型的命题：谱定理 → Fourier → 非阿贝尔对偶",
              2: "2 它在说什么：两个模空间与主定理",
              3: "3 为什么成立：Hecke、因子化与谱作用",
              4: "4 怎么变具体：Abel 化与 Hitchin",
              5: "5 证明地图：五篇论文与 Scholze 路线",
              6: "6 证明细节：Whittaker、Eisenstein、Kac–Moody、尖点",
              7: "7 现状、开放问题与形式化"}
    for i, ln in enumerate(L):
        m = re.match(r"^## (\d) .*$", ln)
        if m and int(m.group(1)) in TITLES:
            L[i] = "## " + TITLES[int(m.group(1))]

    # appendix A chronology
    L += ["## 附录 A 年表 1978–2026", ""]
    L.extend([fix_links(x) for x in chrono if x.strip()])
    L.append("")

    # appendix B card index
    L += ["## 附录 B 资料卡总索引", "",
          "按节列出本页引用的全部资料卡。卡 id 可在 `datasets/<work>/cards/` 下按路径打开；「节」指首次出现处。", "",
          "| 卡 id | 概念 | 卡文件 | 节 | 底本页 |", "| --- | --- | --- | --- | --- |"]
    for cid in order:
        d = all_cards[cid]
        secs = "/".join("§%d" % s for s in sorted(d["sections"])) or "—"
        m = re.search(r"\]\((?:<([^>]+)>|([^)\s]+))\)", d["path"])
        lpath = (m.group(1) or m.group(2)) if m else d["path"]
        L.append("| `%s` | %s | [%s](%s) | %s | %s |" % (
            cid, d["title"], lpath.split("/")[-1], fix_target(lpath), secs,
            d["pages"] or "—"))
    L.append("")

    # appendix C master map
    L += ["## 附录 C 证明思维导图", "",
          "全页总图：上半是「为什么可能」，下半是五篇论文的证明链与两条收口。分节小图见各节末尾。", "",
          "```mermaid", "flowchart TD",
          '  S0["§0–1 代数谱定理 / Fourier<br/>范畴化的调和分析"] --> S1["§3 几何 Satake<br/>Sph_G ≃ Rep(Ĝ)"]',
          '  S1 --> S2["§3 谱作用<br/>QCoh(Loc_Ĝ) ↷ D(Bun_G)"]',
          '  S2 --> I["I · 造 Langlands 函子 L_G<br/>D(Bun_G) → IndCoh_Nilp(Loc_Ĝ)"]',
          '  KM["II · Kac–Moody + opers<br/>临界水平局部化 ⇒ 尖点层"] --> I',
          '  I --> III["III · Eisenstein 归纳<br/>化到 Levi 与尖点"]',
          '  III --> IV["IV · ambidexterity<br/>左/右伴随差扭同构"]',
          '  IV --> V["V · 重数一<br/>A_Ĝ 自对偶 ⇒ 局部系统"]',
          '  V --> TH["char 0 主定理<br/>D(Bun_G) ≃ IndCoh_Nilp(Loc_Ĝ)"]',
          '  CP["char p（独立 2025a）<br/>Witt 提升 + LocSys′"] --> TH',
          '  TH --> FQ["Frobenius 的迹<br/>⇒ F_q 上函数同构（Thm 1.7）"]',
          '  S2 -.-> BE["§7 Beilinson 投影子<br/>投影到幂零支撑"]',
          '  BE -.-> I', "```", ""]

    text = "\n".join(L)
    text = text.replace("Ǵ", "Ĝ")
    text = text.replace("`08_source_code/SY02-35_几何Langlands猜想I_函子的构造/成品/SY02-35_几何Langlands猜想I_函子的构造_v1.0.pdf`",
                        "[GLC I 中译](../../../08_source_code/SY02-35_几何Langlands猜想I_函子的构造/成品/SY02-35_几何Langlands猜想I_函子的构造_v1.0.pdf)")
    # blank line before every H2 except at file start / after a blank line
    lines = text.split("\n")
    fixed = []
    for i, ln in enumerate(lines):
        if ln.startswith("## ") and fixed and fixed[-1].strip() != "":
            fixed.append("")
        fixed.append(ln)
    text = "\n".join(fixed)
    out = HERE / "merged.md"
    out.write_text(text + "\n", encoding="utf-8")
    q = ["# 起草期待核事项（统稿后交给核对者）", "",
         "由 survey-v1 各稿的「易错点与待核」拆出，仅供核对流程使用，不进主页面。", ""]
    for sec in sorted(todo):
        for t in todo[sec]:
            q.append("- 〔§%d〕%s" % (sec, t))
    (HERE / "open-questions.md").write_text("\n".join(q) + "\n", encoding="utf-8")
    print("wrote", out)
    print("cards:", len(order), "sources:", list(sources), "sections:",
          sorted(bodies), "pitfalls:", {k: len(v) for k, v in pitfalls.items()},
          "mermaid:", sorted(k for k in mermaids if k is not None))
    sizes = {s: len("".join(bodies[s])) for s in bodies}
    print("body chars:", sizes, "total:", sum(sizes.values()))


if __name__ == "__main__":
    main()
