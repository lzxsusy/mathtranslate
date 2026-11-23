#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""第二代资料卡抽取器：把 08_source_code 里两种新格式灌进 KB。

来源
----
1. `资料卡/cards/**/*.json`        —— 新格式单卡（SY02-25 / SY02-26 …）
2. `资料卡/03-论证链.md`            —— 论证链（问题/起点/步骤带 warrant/收口/反事实）
3. `资料卡/0X-*.md` 五件套          —— 00-速览 / 01-结果清单 / 02-论证地图 / 04-术语文献勘误

输出
----
`kb/cards5/<work>.jsonl`，一卡一行，字段对齐 kb/schema/card.schema.json。
不覆盖 `kb/cards/`（那是 ingest.py 从 datasets JSON 卡抽的），两边由 build_kb.py 合并。

用法
----
    python kb/ingest_gen2.py            # 全量
    python kb/ingest_gen2.py --stats    # 只报数
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SRC = REPO / "08_source_code"
OUT = Path(__file__).resolve().parent / "cards5"

PDF_OFFSET_HINT = "PDF 页 = 原书页 + {n}"  # 每部书不同，写进 caveat 只在已知时

# ---------------------------------------------------------------- 通用工具

def norm_dash(s: str) -> str:
    return s.replace("\u2013", "-").replace("\u2014", "-").replace("\u2212", "-")


def clean_tex(s: str) -> str:
    """把常见 LaTeX 包裹降成可读文本，但保留 $...$ 里的公式原样。"""
    s = s.replace("\\\\", "\\")
    s = re.sub(r"\\on\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\b([A-Za-z]+)", r"\1", s)          # \bZ → Z（黑体宏当普通字母）
    s = re.sub(r"\\(?:mathrm|operatorname|text|mathcal|mathbb|mathfrak|mathbf)\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\m?[Oo]m?\b", "O", s)               # \mO → O
    return s.strip()


def pages_in(text: str) -> list[int]:
    """抽 ASCII 页码：p.47 / pp.47-49 / (p. 47)。上限 30 个，保持出现顺序。"""
    out: list[int] = []
    for m in re.finditer(r"\bpp?\.\s*(\d{1,4})(?:\s*[-–]\s*(\d{1,4}))?", text):
        a = int(m.group(1))
        b = int(m.group(2)) if m.group(2) else None
        for v in ([a] if b is None else list(range(a, min(b, a + 20) + 1))):
            if v not in out:
                out.append(v)
        if len(out) >= 30:
            break
    return out[:30]


def work_id(dirname: str) -> str:
    m = re.match(r"^(SY\d{2}-\d{2})", dirname)
    if m:
        return m.group(1)
    # 兜底：取反斜杠前的一段
    return dirname.split("_")[0] or "UNKNOWN"


def slug(s: str, fallback: str = "x") -> str:
    s = norm_dash(clean_tex(s))
    s = re.sub(r"[^\w\u4e00-\u9fff]+", "-", s, flags=re.UNICODE).strip("-")
    return (s[:40] or fallback).lower()


def card(**kw) -> dict:
    base = {
        "id": None, "work": None, "kind": "note", "level": "L1",
        "title": "", "aliases": [], "summary": "", "pages": [],
        "prereqs": [], "links": [], "sources": [], "evidence_quote": "",
        "status": "draft", "review": {}, "terms": [], "symbols": [],
        "caveat": "", "updated": "", "origin": "gen2",
    }
    base.update(kw)
    return base


# ---------------------------------------------------------------- 1. gen2 JSON 单卡

KIND_MAP = {
    "concept": "concept", "definition": "concept", "term": "term",
    "statement": "theorem", "theorem": "theorem", "proposition": "theorem",
    "lemma": "theorem", "corollary": "theorem", "claim": "theorem",
    "derivation": "chain", "proof": "proof", "example": "example",
    "exercise": "example", "errata": "errata", "alignment": "alignment",
    "note": "note", "work": "work", "question": "note",
}

STATUS_MAP = {
    "已核": "checked", "已复核": "verified", "verified": "verified",
    "checked": "checked", "reviewed": "checked", "published": "verified",
    "draft": "draft", "草稿": "draft", "gap": "draft", "待核": "draft",
    "disputed": "disputed",
}


def from_gen2_json(path: Path, work: str) -> list[dict]:
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []
    if not isinstance(d, dict) or not d.get("id"):
        return []
    cid = str(d["id"])
    kind = KIND_MAP.get(str(d.get("type") or "").lower(), "note")
    status = STATUS_MAP.get(str(d.get("status") or "").lower(), "draft")
    pages = [int(p) for p in (d.get("pages") or []) if isinstance(p, (int, float))][:30]
    pdf_pages = [int(p) for p in (d.get("pdf_pages") or []) if isinstance(p, (int, float))][:30]

    # 正文：优先 summary，再拼 definition / proof / steps 的正文
    parts = [d.get("summary") or ""]
    for key in ("statement", "definition", "proof", "sketch", "argument"):
        v = d.get(key)
        if isinstance(v, dict):
            v = v.get("text") or v.get("statement") or ""
        if isinstance(v, str) and v.strip():
            parts.append(v.strip())
    if d.get("question"):
        parts.append("问题：" + str(d["question"]))
    summary = "\n\n".join(clean_tex(p) for p in parts if p).strip()

    steps = d.get("steps") or d.get("derivation") or []
    if isinstance(steps, list):
        lines = []
        for s in steps:
            if isinstance(s, dict):
                t = s.get("claim") or s.get("text") or s.get("title") or ""
                loc = s.get("locator") or s.get("warrant") or ""
                lines.append(f"- {clean_tex(str(t))}" + (f"（{loc}）" if loc else ""))
            elif isinstance(s, str):
                lines.append("- " + clean_tex(s))
        if lines:
            summary = (summary + "\n\n" + "\n".join(lines)).strip()
            if not pages:
                pages = pages_in("\n".join(lines))

    aliases = [str(a) for a in (d.get("aliases") or [])][:12]
    srcs = []
    for s in (d.get("sources") or [])[:6]:
        if isinstance(s, dict):
            srcs.append({"grade": str(s.get("grade") or "C").upper()[:1],
                         "ref": str(s.get("ref") or s.get("label") or s.get("url") or "")[:200]})
        elif isinstance(s, str):
            srcs.append({"grade": "C", "ref": s[:200]})

    caveat = ""
    if pdf_pages:
        caveat = f"原书页 pages={pages or '未标'}；对应 PDF 页 {pdf_pages[0]}–{pdf_pages[-1]}。"
    if not pages:
        caveat = (caveat + " 卡内未标页码，引用前请回原文核对。").strip()

    return [card(
        id=cid, work=work, kind=kind,
        level=str(d.get("level") or ("L4" if kind == "chain" else "L2")),
        title=clean_tex(str(d.get("title") or cid)), aliases=aliases,
        summary=summary, pages=pages,
        prereqs=[str(x) for x in (d.get("prereqs") or [])][:20],
        sources=srcs, evidence_quote=str(d.get("evidence_quote") or "")[:200],
        status=status,
        review={"drafter": "gen2", "reviewer": "", "blindtest": "pending",
                "rounds": 2 if status == "verified" else (1 if status == "checked" else 0)},
        terms=[str(t) for t in (d.get("terms") or [])][:20],
        caveat=caveat, updated=str(d.get("updated") or ""),
        origin=f"gen2:{path.relative_to(SRC).as_posix()}",
    )]


# ---------------------------------------------------------------- 2. 论证链 md

CHAIN_HEAD = re.compile(r"^###\s*链\s*([0-9]+)\s*[：:]\s*(.+?)\s*$", re.M)
FIELD = re.compile(r"^-\s*(问题|起点|步骤|收口|反事实)\s*[：:]\s*(.*)$", re.M)


def from_chain_md(path: Path, work: str) -> list[dict]:
    text = path.read_text(encoding="utf-8", errors="replace")
    heads = list(CHAIN_HEAD.finditer(text))
    out = []
    for i, h in enumerate(heads):
        start = h.end()
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        body = text[start:end].strip()
        fields = {}
        cur = None
        buf: list[str] = []
        for line in body.splitlines():
            m = re.match(r"^-\s*(问题|起点|步骤|收口|反事实)\s*[：:]\s*(.*)$", line)
            if m:
                if cur:
                    fields[cur] = "\n".join(buf).strip()
                cur, buf = m.group(1), [m.group(2)]
            elif cur:
                buf.append(line)
        if cur:
            fields[cur] = "\n".join(buf).strip()

        num, title = h.group(1), clean_tex(h.group(2))
        summary_bits = []
        for k in ("问题", "起点", "收口", "反事实"):
            if fields.get(k):
                summary_bits.append(f"{k}：{clean_tex(fields[k])}")
        if fields.get("步骤"):
            summary_bits.append("步骤：\n" + clean_tex(fields["步骤"]))
        summary = "\n\n".join(summary_bits).strip()
        pages = pages_in(body)
        prereqs = sorted(set(re.findall(rf"{re.escape(work)}\.(?:concept|stmt|statement)\.[\w.\-]+", body)))[:30]
        out.append(card(
            id=f"{work}.chain.na{num}", work=work, kind="chain", level="L4",
            title=f"论证链 {num}：{title}", aliases=[title],
            summary=summary, pages=pages, prereqs=prereqs,
            status="checked" if pages else "draft",
            review={"drafter": "gen2", "reviewer": "", "blindtest": "pending",
                    "rounds": 1 if pages else 0},
            caveat="论证链由读手撰写并 Lead 合并；页码来自链内标注，引用前回原文核对。",
            origin=f"gen2:{path.relative_to(SRC).as_posix()}",
        ))
    return out


# ---------------------------------------------------------------- 3. 五件套 md

def _bullets(body: str) -> list[str]:
    out, buf = [], []
    for line in body.splitlines():
        if re.match(r"^[-*]\s+", line):
            if buf:
                out.append(" ".join(buf))
            buf = [re.sub(r"^[-*]\s+", "", line)]
        elif buf and line.strip():
            buf.append(line.strip())
        elif not line.strip() and buf:
            out.append(" ".join(buf))
            buf = []
    if buf:
        out.append(" ".join(buf))
    return [b.strip() for b in out if len(b.strip()) > 12]


def from_results_md(path: Path, work: str) -> list[dict]:
    """01-结果清单：按 ## 小节切，每条 bullet 一张 theorem 卡（结果簇）。"""
    text = path.read_text(encoding="utf-8", errors="replace")
    out = []
    sections = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.M))
    for i, s in enumerate(sections):
        start = s.end()
        end = sections[i + 1].start() if i + 1 < len(sections) else len(text)
        sec_title = clean_tex(s.group(1))
        for j, b in enumerate(_bullets(text[start:end])):
            bt = clean_tex(b)
            lead = re.match(r"\*\*(.+?)\*\*\s*[：:]\s*(.*)$", bt)
            if lead:
                title, summary = clean_tex(lead.group(1)), clean_tex(lead.group(2))
            else:
                title = re.split(r"[。；;]", bt)[0][:48]
                summary = bt
            nums = re.findall(r"\d+\.\d+(?:\.\d+)?", b)
            out.append(card(
                id=f"{work}.theorem.{slug(sec_title)}.{j + 1}", work=work,
                kind="theorem", level="L2", title=title,
                aliases=nums[:6], summary=f"[{sec_title}] {summary}",
                pages=pages_in(b),
                status="draft",
                caveat="结果簇条目，编号对象明细见 03-条款索引；未标页码者需回原文定位。",
                origin=f"gen2:{path.relative_to(SRC).as_posix()}",
            ))
    return out


def from_map_md(path: Path, work: str) -> list[dict]:
    """02-论证地图：## D<n> 段 → chain 卡；「作者未说透」段 → note 卡。"""
    text = path.read_text(encoding="utf-8", errors="replace")
    heads = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.M))
    out = []
    for i, h in enumerate(heads):
        start = h.end()
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        title = clean_tex(h.group(1))
        body = text[start:end].strip()
        if not body:
            continue
        if "未说透" in title or "译者按" in title:
            out.append(card(
                id=f"{work}.note.weishuotou", work=work, kind="note", level="L2",
                title=f"{title}", summary=clean_tex(body)[:4000],
                status="checked", origin=f"gen2:{path.relative_to(SRC).as_posix()}",
                caveat="译者按，属作者未明说处的补注；属解释性内容，非原文。",
            ))
            continue
        m = re.match(r"^(D\d+)", title)
        key = m.group(1) if m else slug(title)
        out.append(card(
            id=f"{work}.chain.{key.lower()}", work=work, kind="chain", level="L4",
            title=title, summary=clean_tex(body)[:6000], pages=pages_in(body),
            prereqs=sorted(set(re.findall(r"§[\d.]+", body)))[:20],
            status="checked", origin=f"gen2:{path.relative_to(SRC).as_posix()}",
            caveat="论证地图（全书主链）；小节号来自 § 引用，页码需回原文定位。",
        ))
    return out


def from_terms_md(path: Path, work: str) -> list[dict]:
    """04-术语文献勘误：三列表格 → term 卡；勘误小节 → errata 卡。"""
    text = path.read_text(encoding="utf-8", errors="replace")
    out = []
    section = ""
    rows: list[list[str]] = []
    for line in text.splitlines() + [""]:
        h = re.match(r"^#{2,3}\s+(.+?)\s*$", line)
        if h:
            if rows:
                out.extend(_term_rows(rows, section, work, path))
                rows = []
            section = clean_tex(h.group(1))
            continue
        if line.strip().startswith("|") and not re.match(r"^\|[\s:|-]+\|$", line.strip()):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and cells[0] not in ("英文", "术语", "原文"):
                rows.append(cells)
    if rows:
        out.extend(_term_rows(rows, section, work, path))

    # 勘误：形如 "1. **§x.y**：…" 的条目
    for sec in re.finditer(r"^#{2,3}\s*(勘误|已知问题|原文缺陷).*?$", text, re.M):
        start = sec.end()
        nxt = re.search(r"^#{2,3}\s", text[start:], re.M)
        body = text[start:start + (nxt.start() if nxt else len(text))]
        for j, item in enumerate(re.findall(r"^\s*\d+\.\s+(.+?)(?=^\s*\d+\.\s|\Z)", body, re.M | re.S)):
            t = clean_tex(item).strip()
            if len(t) < 10:
                continue
            out.append(card(
                id=f"{work}.errata.{j + 1}", work=work, kind="errata", level="L2",
                title=t.split("：")[0][:60], summary=t[:2000], pages=pages_in(t),
                status="checked", origin=f"gen2:{path.relative_to(SRC).as_posix()}",
                caveat="原文缺陷/勘误条目；引用前回原书页确认。",
            ))
    return out


def _term_rows(rows: list[list[str]], section: str, work: str, path: Path) -> list[dict]:
    out = []
    for r in rows:
        en, zh = r[0], r[1]
        basis = r[2] if len(r) > 2 else ""
        if not en or not zh or len(en) > 80 or len(zh) > 80:
            continue
        grade = "C"
        if basis:
            g = basis.strip()[:1].upper()
            if g in ("A", "B", "I"):
                grade = "A" if g == "A" else "B"
        out.append(card(
            id=f"{work}.term.{slug(zh)}", work=work, kind="term", level="L0",
            title=zh, aliases=[en], summary=f"{en} → {zh}" + (f"（依据 {basis}）" if basis else ""),
            sources=[{"grade": grade, "ref": basis[:160]}] if basis else [],
            status="checked" if grade == "A" else "draft",
            review={"drafter": "gen2", "reviewer": "", "blindtest": "pending",
                    "rounds": 1 if grade == "A" else 0},
            origin=f"gen2:{path.relative_to(SRC).as_posix()}",
            caveat=f"术语条目（{section}）；译名已冻结则勿改，改用需三同步。",
        ))
    return out


def from_overview_md(path: Path, work: str) -> list[dict]:
    text = path.read_text(encoding="utf-8", errors="replace")
    title = ""
    m = re.search(r"^#\s+(.+?)$", text, re.M)
    if m:
        title = clean_tex(m.group(1))
    body = re.sub(r"^#\s+.+?$", "", text, count=1, flags=re.M).strip()
    return [card(
        id=f"{work}.work", work=work, kind="work", level="L0",
        title=title or work, summary=clean_tex(body)[:6000],
        status="checked", origin=f"gen2:{path.relative_to(SRC).as_posix()}",
        caveat="作品速览（本工程自述），非原文内容。",
    )]


# ---------------------------------------------------------------- 驱动

def run(stats_only: bool = False) -> None:
    if not SRC.is_dir():
        sys.exit(f"找不到 {SRC}")
    per_work: dict[str, list[dict]] = {}
    kinds: dict[str, int] = {}
    dirs = sorted([d for d in SRC.iterdir() if d.is_dir()])
    for d in dirs:
        carddir = d / "资料卡"
        if not carddir.is_dir():
            continue
        work = work_id(d.name)
        cards: list[dict] = []

        # 1) gen2 JSON 单卡
        for f in sorted(carddir.glob("cards/**/*.json")):
            cards.extend(from_gen2_json(f, work))
        # 2) 论证链 md（两种命名）
        for f in sorted(carddir.glob("*论证链*.md")):
            cards.extend(from_chain_md(f, work))
        # 3) 五件套
        for f in sorted(carddir.glob("*.md")):
            name = f.name
            try:
                if name.startswith("00-"):
                    cards.extend(from_overview_md(f, work))
                elif name.startswith("01-") and "结果" in name:
                    cards.extend(from_results_md(f, work))
                elif name.startswith("02-") and "论证" in name:
                    cards.extend(from_map_md(f, work))
                elif name.startswith("04-"):
                    cards.extend(from_terms_md(f, work))
                # 03-条款索引 不进卡（编号索引，价值在明细而非检索）
            except Exception as e:  # noqa: BLE001
                print(f"  ! {name}: {e}", file=sys.stderr)
        if not cards:
            continue
        # 去重（同 id 保第一条）
        seen, uniq = set(), []
        for c in cards:
            if c["id"] in seen:
                continue
            seen.add(c["id"])
            uniq.append(c)
        per_work[work] = uniq
        for c in uniq:
            kinds[c["kind"]] = kinds.get(c["kind"], 0) + 1

    total = sum(len(v) for v in per_work.values())
    print(f"作品 {len(per_work)} 部 / 卡片 {total} 张")
    for k, v in sorted(kinds.items(), key=lambda x: -x[1]):
        print(f"  {k:10s} {v}")
    if stats_only:
        return
    OUT.mkdir(parents=True, exist_ok=True)
    for f in OUT.glob("*.jsonl"):
        f.unlink()
    for work, cards in per_work.items():
        p = OUT / f"{work}.jsonl"
        with p.open("w", encoding="utf-8") as fh:
            for c in cards:
                fh.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(f"已写入 {OUT}（{len(per_work)} 个文件）")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--stats", action="store_true")
    a = ap.parse_args()
    run(stats_only=a.stats)
