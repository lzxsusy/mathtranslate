#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数译知识库 · 摄入器（P1）

把仓库里三种并存的资料卡格式，统一成 kb/cards/<work>.jsonl（一卡一行）。

  python kb/ingest.py all           # 全量重跑（先清空 kb/cards）
  python kb/ingest.py frontmatter   # 08_source_code/*/资料卡/*.md（YAML frontmatter 单卡）
  python kb/ingest.py json          # datasets/**/cards/**/*.json（结构化 JSON 卡）
  python kb/ingest.py works         # 08_source_code/*/资料卡（五件套）→ 书级条目，一律 draft

设计要点
- 卡片 id 一律加 work 前缀，避免跨书撞名（MS-05 → SY01-26.MS-05）。
- 没有页码的卡也可以进 jsonl，但会被 build_kb.py 判为不可索引（保持“可检索=可回溯”）。
- 五件套是叙述体报告，不切段，只建 work 级条目（kind=work, status=draft），默认检索不返回。
"""
import json
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
KB = REPO / "kb"
CARDS_DIR = KB / "cards"

GRADE_RE = re.compile(r"^\s*([ABC])\s*级\s*[：:]\s*(.*)$", re.S)


def work_of(name: str) -> str:
    """"SY01-26_镜像对称与代数几何（Cox–Katz）" → "SY01-26"；"ggl20" → "ggl20" """
    m = re.match(r"^([A-Za-z]{2,6}\d{2}(?:-\d{2})?)", name)
    return m.group(1) if m else name


def parse_sources(raw):
    out = []
    for s in raw or []:
        if isinstance(s, dict):
            out.append({"grade": s.get("grade"), "text": str(s.get("text", "")).strip()})
            continue
        t = str(s).strip()
        m = GRADE_RE.match(t)
        if m:
            out.append({"grade": m.group(1), "text": m.group(2).strip()})
        else:
            out.append({"grade": None, "text": t})
    return [s for s in out if s["text"]]


def norm_status(st: str, review: dict) -> str:
    st = (st or "").strip().lower()
    if st in ("verified", "checked", "disputed", "draft"):
        return st
    bt = (review or {}).get("blindtest", "")
    if (review or {}).get("reviewer") and str(bt).lower() not in ("pending", "", "none"):
        return "checked"
    return "draft"


def norm_review(review: dict) -> dict:
    review = review or {}
    rounds = 0
    for k in ("drafter", "reviewer", "blindtest"):
        v = review.get(k)
        if v and str(v).lower() not in ("pending", "none", ""):
            rounds += 1
    return {
        "drafter": review.get("drafter"),
        "reviewer": review.get("reviewer"),
        "blindtest": review.get("blindtest"),
        "rounds": int(review.get("rounds", rounds) or rounds),
    }


def read_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return None, text
    parts = text.split("\n---", 2)
    if len(parts) < 2:
        return None, text
    head = parts[0].lstrip("-").strip()
    body = parts[1].split("\n", 1)[1] if "\n" in parts[1] else ""
    body = (body + (parts[2] if len(parts) > 2 else "")).strip()
    try:
        meta = yaml.safe_load(head) or {}
    except Exception as exc:  # noqa: BLE001
        print(f"  ! frontmatter 解析失败 {path.name}: {exc}")
        meta = {}
    return (meta if isinstance(meta, dict) else {}), body


def adapt_frontmatter():
    rows = []
    for card_dir in sorted(REPO.glob("08_source_code/*/资料卡")):
        work = work_of(card_dir.parent.name)
        for md in sorted(card_dir.glob("*.md")):
            meta, body = read_frontmatter(md)
            if not meta or not meta.get("id"):
                continue
            raw_id = str(meta["id"]).strip()
            cid = raw_id if raw_id.startswith(work + ".") else f"{work}.{raw_id}"
            prereqs = [str(p) if str(p).startswith(work + ".") else f"{work}.{p}"
                       for p in (meta.get("prereqs") or [])]
            terms = []
            for g in (meta.get("glossary_refs") or []):
                g = str(g)
                if "/" in g:
                    en, zh = [x.strip() for x in g.split("/", 1)]
                    terms.append({"en": en, "zh": zh})
                else:
                    terms.append({"zh": g})
            review = norm_review(meta.get("review") or {})
            rows.append({
                "id": cid,
                "work": work,
                "kind": (meta.get("kind") or "concept"),
                "level": meta.get("layer") or meta.get("level"),
                "title": meta.get("zh") or meta.get("title") or raw_id,
                "title_en": meta.get("en"),
                "aliases": [str(a) for a in (meta.get("aliases") or [])],
                "summary": body,
                # 页码：frontmatter 里没有独立 pages 字段时，从 sources 文本里抽 “p.206” 之类
                "pages": extract_pages(meta),
                "prereqs": prereqs,
                "links": [],
                "sources": parse_sources(meta.get("sources")),
                "status": norm_status(meta.get("status"), review),
                "review": review,
                "terms": terms,
                "symbols": [str(s) for s in (meta.get("symbols_refs") or [])],
                "updated": str(meta.get("updated") or ""),
                "origin": str(md.relative_to(REPO)).replace("\\", "/"),
            })
    return rows


PAGE_RE = re.compile(r"p\.?\s*(\d{1,3})(?:\s*[–\-~]\s*(\d{1,3}))?")


def extract_pages(meta: dict):
    pages = set()
    for s in (meta.get("sources") or []):
        for m in PAGE_RE.finditer(str(s)):
            a = int(m.group(1))
            b = int(m.group(2)) if m.group(2) else a
            for p in range(a, min(b, a + 40) + 1):
                pages.add(p)
    return sorted(pages)


KIND_MAP = {
    "correction": "errata",
    "derivation": "chain",
    "statement": "theorem",
    "remark": "note",
    "definition": "concept",
    "theorem": "theorem",
    "proof": "proof",
    "example": "example",
    "concept": "concept",
    "work": "work",
    "note": "note",
    "errata": "errata",
    "chain": "chain",
}

VERIF_VERIFIED = {"external-confirmed", "certified"}
VERIF_CHECKED = {"source-verified", "source-only"}

NUM_PAGE_RE = re.compile(r"(?:p\.|pp\.|page\s*)(\d{1,3})")


def _walk_pages(node, out, depth=0):
    """递归扫任意 JSON 结构里的页码线索（p.47 / pages:[13,20]）。"""
    if depth > 6:
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k in ("pages", "page") and isinstance(v, list):
                for x in v:
                    if str(x).isdigit() and 0 < int(x) < 1000:
                        out.add(int(x))
            elif k in ("pages", "page") and isinstance(v, (int, str)) and str(v).isdigit():
                p = int(v)
                if 0 < p < 1000:
                    out.add(p)
            else:
                _walk_pages(v, out, depth + 1)
    elif isinstance(node, list):
        for v in node:
            _walk_pages(v, out, depth + 1)
    elif isinstance(node, str):
        for m in NUM_PAGE_RE.finditer(node):
            p = int(m.group(1))
            if 0 < p < 1000:
                out.add(p)


def map_status_json(d: dict):
    st = str(d.get("status") or "").strip().lower()
    v = d.get("verification") or {}
    vs = str((v or {}).get("status") or "").strip().lower()
    if vs in VERIF_VERIFIED or (st == "published" and vs):
        return "verified", 2
    if vs in VERIF_CHECKED or st in ("reviewed", "published"):
        return "checked", 1
    return "draft", 0


def flat_text(v):
    """把任意字段值压成干净文本，避免出现 {'text': ...} 这类 repr 噪声。"""
    if v is None:
        return ""
    if isinstance(v, str):
        return v
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, dict):
        for k in ("text", "zh", "en", "summary", "statement", "content", "value"):
            if k in v and isinstance(v[k], str):
                return v[k]
        return " ".join(flat_text(x) for x in v.values())
    if isinstance(v, list):
        return "\n".join(flat_text(x) for x in v if x is not None)
    return str(v)


def norm_dashes(s: str) -> str:
    return (s or "").replace("\u2013", "-").replace("\u2014", "-").replace("\u2010", "-").replace("\u2212", "-")


def adapt_json():
    rows = []
    for f in sorted(REPO.glob("datasets/*/cards/**/*.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8", errors="replace"))
        except Exception:  # noqa: BLE001
            continue
        if not isinstance(d, dict) or not d.get("id"):
            continue
        work = d["id"].split("/")[0] if "/" in str(d["id"]) else f.relative_to(REPO / "datasets").parts[0]
        cid = re.sub(r"[/\\]", ".", str(d["id"]))
        status, rounds = map_status_json(d)
        pg = set()
        _walk_pages(d, pg)
        pages = sorted(pg)[:20]
        caveat = None
        if not pages:
            caveat = "无页码线索：只能作为“哪本书讲过这个话题”的指针，不能作为结论引用。"
        elif not (isinstance(d.get("sources"), list) and d.get("sources")) and not isinstance(d.get("source"), dict):
            caveat = "页码由卡内文本启发式抽取，引用前请回源核对。"
        ver = d.get("verification") or {}
        body = "\n".join(flat_text(d.get(k)) for k in (
            "summary", "question", "definition", "goal", "setup", "result", "why", "note",
        ) if d.get(k))
        rows.append({
            "id": cid,
            "work": work,
            "kind": KIND_MAP.get(str(d.get("type") or ""), "concept"),
            "level": d.get("level") or d.get("layer"),
            "title": norm_dashes(d.get("title") or cid),
            "title_en": d.get("title_en"),
            "aliases": [norm_dashes(str(a)) for a in (d.get("aliases") or [])],
            "summary": norm_dashes(body)[:6000],
            "pages": pages,
            "prereqs": [re.sub(r"[/\\]", ".", str(p)) for p in (d.get("prereqs") or [])],
            "links": [],
            "sources": parse_sources(d.get("sources")),
            "status": status,
            "review": {
                "rounds": rounds,
                "last_verified_at": str(ver.get("checked_on") or ""),
                "blindtest": str(ver.get("status") or ""),
            },
            "terms": d.get("terms") or [],
            "symbols": [str(s) for s in (d.get("symbols") or [])],
            "caveat": caveat,
            "updated": str(d.get("updated") or ver.get("checked_on") or ""),
            "origin": str(f.relative_to(REPO)).replace("\\", "/"),
        })
    return rows


def adapt_works():
    rows = []
    for card_dir in sorted(REPO.glob("08_source_code/*/资料卡")):
        name = card_dir.parent.name
        work = work_of(name)
        files = sorted(p.name for p in card_dir.glob("*.md"))
        if not files:
            continue
        quick = card_dir / "00-速览.md"
        summary = ""
        if quick.exists():
            summary = quick.read_text(encoding="utf-8", errors="replace").strip()[:1200]
        is_five = any(f.startswith(("00-", "01-", "02-")) for f in files)
        rows.append({
            "id": f"{work}.work",
            "work": work,
            "kind": "work",
            "level": None,
            "title": re.sub(r"^[A-Za-z0-9\-]+_", "", name),
            "title_en": None,
            "aliases": [name],
            "summary": summary or f"{len(files)} 个资料卡文件：{', '.join(files[:8])}",
            "pages": [],
            "prereqs": [],
            "links": [],
            "sources": [],
            "status": "draft",
            "review": {"rounds": 0},
            "terms": [],
            "symbols": [],
            "updated": "",
            "origin": str(card_dir.relative_to(REPO)).replace("\\", "/"),
            "caveat": ("书级条目：本作品资料卡为叙述体报告（五件套），尚未拆成逐条声明，"
                       "检索命中只说明“本书可能讲过”，不构成结论。") if is_five else None,
        })
    return rows


def dump(rows, tag):
    by_work = {}
    for r in rows:
        by_work.setdefault(r["work"], []).append(r)
    CARDS_DIR.mkdir(parents=True, exist_ok=True)
    for work, items in by_work.items():
        p = CARDS_DIR / f"{work}.jsonl"
        with p.open("w", encoding="utf-8") as fh:
            for it in items:
                fh.write(json.dumps(it, ensure_ascii=False) + "\n")
    print(f"[{tag}] {len(rows)} 张卡 → {len(by_work)} 个 work 文件，目录 {CARDS_DIR}")
    from collections import Counter
    print("      status:", dict(Counter(r["status"] for r in rows)))
    print("      kind:  ", dict(Counter(r["kind"] for r in rows)))
    idx = [r for r in rows if r.get("pages")]
    print(f"      带页码（可索引）: {len(idx)}")


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode in ("all", "clear"):
        for p in CARDS_DIR.glob("*.jsonl"):
            p.unlink()
    if mode in ("all", "frontmatter"):
        dump(adapt_frontmatter(), "frontmatter")
    if mode in ("all", "json"):
        dump(adapt_json(), "json")
    if mode in ("all", "works"):
        dump(adapt_works(), "works")


if __name__ == "__main__":
    main()
