#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数译知识库 · 查询器（P1）

  python kb/q.py search "Hecke 特征层" [--kind concept] [--work SY02-14] [--level L2]
                                     [--status verified] [--limit 8] [--include-draft] [--json]
  python kb/q.py card SY01-26.MS-05            # 单卡全文
  python kb/q.py brief --work SY02-08          # 阅读前置包（该作品已入库的卡 + 跨书同术语卡）
  python kb/q.py brief --query "顶点代数 代数曲线"   # 未入库新书的阅读前置包
  python kb/q.py gaps --min-works 3            # 多书提及却没有“术语卡/概念卡”的缺口
  python kb/q.py stats
  python kb/q.py verify SY01-26.MS-05          # 回源：页码 / 来源 / 证据引文

设计原则
- 只给线索不给结论：每条结果必带 status、pages、sources、caveat。
- 默认不返回 draft；显式 --include-draft 才返回，且会打上“未复核”标记。
- 可信度加权排序：verified 1.00 / checked 0.85 / disputed 0.70 / draft 0.55。
"""
import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "kb" / "shuyi.db"

TRUST = {"verified": 1.00, "checked": 0.85, "disputed": 0.70, "draft": 0.55}
TRUST_LABEL = {
    "verified": "已核（≥2 轮）",
    "checked": "已核（引文可核）",
    "disputed": "有争议",
    "draft": "未复核",
}
CJK = re.compile(r"[\u4e00-\u9fff]")


def con():
    if not DB.exists():
        sys.exit("kb/shuyi.db 不存在，先跑 python kb/build_kb.py")
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c


def jload(s, default):
    try:
        return json.loads(s) if s else default
    except json.JSONDecodeError:
        return default


def fts_query(q: str) -> str:
    """把用户输入变成 FTS5 查询串：按空白切词，整体加引号，词间 AND。"""
    q = (q or "").replace("\u2013", "-").replace("\u2014", "-").replace("\u2010", "-").replace("\u2212", "-")
    toks = [t for t in re.split(r"\s+", q.strip()) if t]
    if not toks:
        return '""'
    return " AND ".join('"' + t.replace('"', '""') + '"' for t in toks)


def search(args):
    c = con()
    q = fts_query(args.query)
    table = "fts_tri" if CJK.search(args.query) else "fts_uni"
    sql = f"""SELECT c.*, bm25({table}) AS score
              FROM {table} JOIN cards c ON c.id = {table}.id
              WHERE {table} MATCH ?"""
    params = [q]
    rows = []
    for r in c.execute(sql + " ORDER BY score LIMIT 300", params):
        rows.append(dict(r))
    if not rows:  # 换分词器再试一次
        other = "fts_uni" if table == "fts_tri" else "fts_tri"
        sql2 = f"""SELECT c.*, bm25({other}) AS score
                   FROM {other} JOIN cards c ON c.id = {other}.id
                   WHERE {other} MATCH ? ORDER BY score LIMIT 300"""
        rows = [dict(r) for r in c.execute(sql2, params)]

    def keep(r):
        if args.kind and r["kind"] != args.kind:
            return False
        if args.work and r["work"] != args.work:
            return False
        if args.level and (r["level"] or "") != args.level:
            return False
        if args.status and r["status"] != args.status:
            return False
        if r["status"] == "draft" and not args.include_draft:
            return False
        return True

    rows = [r for r in rows if keep(r)]
    # bm25 越小越相关 → 归一化后乘可信度权重
    if rows:
        best = min(r["score"] for r in rows)
        for r in rows:
            rel = 1.0 / (1.0 + (r["score"] - best))
            r["weight"] = TRUST.get(r["status"], 0.5)
            r["final"] = rel * r["weight"]
    rows.sort(key=lambda r: -r.get("final", 0))
    rows = rows[: args.limit]

    if args.json:
        out = [{
            "id": r["id"], "work": r["work"], "kind": r["kind"], "level": r["level"],
            "title": r["title"], "status": r["status"], "trust": TRUST_LABEL.get(r["status"]),
            "pages": jload(r["pages"], []), "sources": jload(r["sources"], []),
            "caveat": r["caveat"], "origin": r["origin"],
            "summary": (r["summary"] or "")[:400],
        } for r in rows]
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(f"查询：{args.query!r}  命中 {len(rows)} 条（默认已排除 draft）")
        for i, r in enumerate(rows, 1):
            pages = jload(r["pages"], [])
            pg = f"p.{pages[0]}" if len(pages) == 1 else (f"p.{pages[0]}–{pages[-1]}" if pages else "无页码")
            print(f"\n[{i}] {r['title']}   ({r['id']})")
            print(f"    可信度：{TRUST_LABEL.get(r['status'], r['status'])} · {r['kind']}"
                  + (f"/{r['level']}" if r['level'] else "") + f" · {r['work']} · {pg}")
            summary = re.sub(r"\s+", " ", (r["summary"] or ""))[:220]
            if summary:
                print(f"    摘要：{summary}…")
            src = jload(r["sources"], [])
            if src:
                s0 = src[0]
                grade = s0.get("grade") or "?"
                stext = str(s0.get("text") or "")
                print(f"    来源：[{grade}] {stext[:110]}")
            if r["caveat"]:
                print(f"    ⚠ {r['caveat']}")
    if not args.no_log:
        with con() as c2:
            for r in rows:
                c2.execute("INSERT INTO query_log(card_id, q) VALUES (?,?)", (r["id"], args.query))
            c2.commit()


def show_card(args):
    c = con()
    r = c.execute("SELECT * FROM cards WHERE id=?", (args.id,)).fetchone()
    if not r:
        sys.exit(f"没有这张卡：{args.id}")
    r = dict(r)
    print(f"# {r['title']}   [{r['id']}]")
    print(f"work={r['work']}  kind={r['kind']}  level={r['level']}  status={r['status']}"
          f"  ({TRUST_LABEL.get(r['status'])})")
    pages = jload(r["pages"], [])
    print(f"pages={pages}  updated={r['updated']}")
    print(f"origin={r['origin']}")
    for name in ("aliases", "terms", "symbols", "prereqs", "links"):
        v = jload(r[name], [])
        if v:
            print(f"{name}: {json.dumps(v, ensure_ascii=False)}")
    src = jload(r["sources"], [])
    if src:
        print("sources:")
        for s in src:
            print(f"  - [{s.get('grade') or '?'}] {s.get('text')}")
    if r["evidence_quote"]:
        print(f'evidence_quote: "{r["evidence_quote"]}"')
    if r["caveat"]:
        print(f"caveat: {r['caveat']}")
    print("\n---- 卡面 ----")
    print(r["summary"])


TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z\-]{1,}|[\u4e00-\u9fff]{2,8}")


def seeds_from_text(t, limit=10):
    """把一句话拆成可检索的种子词：拉丁词整取，中文取 2–8 字连续段。"""
    out = []
    for m in TOKEN_RE.finditer(t or ""):
        s = m.group(0)
        if s.lower() not in ("the", "and", "for", "with") and s not in out:
            out.append(s)
        if len(out) >= limit:
            break
    return out


def brief(args):
    c = con()
    lines = []
    if args.work:
        head = c.execute("SELECT * FROM cards WHERE id=?", (f"{args.work}.work",)).fetchone()
        own_all = [dict(x) for x in c.execute("SELECT * FROM cards WHERE work=? ORDER BY kind, id", (args.work,))]
        own = [r for r in own_all if r["status"] in ("verified", "checked")]
        title = head["title"] if head else None
        if not title:
            # 没有 work 级条目时，从 08_source_code 的目录名反推中文题名
            for d in sorted((REPO / "08_source_code").glob(f"{args.work}_*")):
                title = re.sub(r"^[A-Za-z0-9\-]+_", "", d.name)
                break
        title = title or args.work
        lines.append(f"# 阅读前置包：{title}（{args.work}）\n")
        if not own_all:
            lines.append("> 本作品暂无卡片；下面给跨书相关卡。\n")
        else:
            lines.append(f"> 本作品卡片 {len(own_all)} 张，其中已核 {len(own)} 张；下面另给跨书线索。\n")
        terms = []
        for r in own_all:
            terms += [t.get("en") or t.get("zh") for t in jload(r["terms"], []) if isinstance(t, dict)]
        seeds = [t for t in terms if t][:8]
        seeds += seeds_from_text(title)
        for r in own_all[:5]:
            seeds += seeds_from_text(r["title"], 4)
        seen_s, uniq = set(), []
        for s in seeds:
            k = s.lower()
            if k not in seen_s:
                seen_s.add(k)
                uniq.append(s)
        seeds = uniq[:14]
    else:
        toks = seeds_from_text(args.query) or [args.query.strip()]
        seeds = toks
        lines.append(f"# 阅读前置包：{args.query}\n")
        lines.append(f"> 检索词：{' / '.join(seeds)}（任一命中即列出，按可信度排序）\n")

    seen, found = set(), []
    for seed in seeds:
        q = fts_query(seed)
        table = "fts_tri" if CJK.search(seed) else "fts_uni"
        try:
            rows = c.execute(
                f"""SELECT c.*, bm25({table}) AS score FROM {table}
                    JOIN cards c ON c.id={table}.id WHERE {table} MATCH ?
                    AND c.status IN ('verified','checked') ORDER BY score LIMIT 8""", (q,))
        except sqlite3.OperationalError:
            continue
        for r in rows:
            r = dict(r)
            if r["id"] in seen or (args.work and r["work"] == args.work):
                continue
            seen.add(r["id"])
            found.append(r)
    found.sort(key=lambda r: -TRUST.get(r["status"], 0.5))
    lines.append("## 其他作品里可能相关（跨书线索）\n")
    if not found:
        lines.append("_没有命中：这部书的主题在本库里还没有已核卡片，可从零开始。_\n")
    for r in found[:20]:
        pages = jload(r["pages"], [])
        pg = f" p.{pages[0]}" if pages else ""
        lines.append(f"- **{r['title']}**（{r['work']}{pg}，{TRUST_LABEL.get(r['status'])}）"
                     f" — {re.sub(chr(10), ' ', (r['summary'] or ''))[:120]}")
    text = "\n".join(lines) + "\n"
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"已写入 {args.out}")
    else:
        print(text)


def gaps(args):
    """找“多部作品都提到、却没有独立术语卡/概念卡”的锚点。

    P1 以卡片 aliases 为术语来源（JSON 卡普遍没有 terms 字段）。
    """
    c = con()
    from collections import defaultdict
    alias_works = defaultdict(set)
    rows = [dict(r) for r in c.execute(
        "SELECT work, aliases, terms FROM cards WHERE status IN ('verified','checked')")]
    for r in rows:
        cands = []
        for a in jload(r["aliases"], []):
            cands.append(str(a))
        for t in jload(r["terms"], []):
            if isinstance(t, dict):
                cands.append(str(t.get("en") or t.get("zh") or ""))
        for a in cands:
            a = a.strip()
            if 2 <= len(a) <= 60:
                alias_works[a.lower()].add(r["work"])
    hot = [(k, len(v)) for k, v in alias_works.items() if len(v) >= args.min_works]
    hot.sort(key=lambda x: (-x[1], x[0]))
    print(f"跨 {args.min_works} 部以上作品出现的术语/别名：{len(hot)} 条")
    print("（这些是跨书对齐的锚点，也是最值得优先补「术语卡」的候选）\n")
    for k, n in hot[: args.limit]:
        print(f"  {n:>2} 部  {k}")


def stats(args):
    c = con()
    print(f"库：{DB}  ({DB.stat().st_size/1048576:.1f} MB)")
    print("\n== status ==")
    for r in c.execute("SELECT status, count(*) n FROM cards GROUP BY status ORDER BY n DESC"):
        print(f"  {r['status']:<10} {r['n']:>5}   {TRUST_LABEL.get(r['status'],'')}")
    print("\n== kind ==")
    for r in c.execute("SELECT kind, count(*) n FROM cards GROUP BY kind ORDER BY n DESC"):
        print(f"  {r['kind']:<10} {r['n']:>5}")
    print("\n== 卡片最多的 12 部作品 ==")
    for r in c.execute("SELECT work, count(*) n FROM cards GROUP BY work ORDER BY n DESC LIMIT 12"):
        print(f"  {r['work']:<12} {r['n']:>5}")
    n_idx = c.execute("SELECT count(*) FROM cards WHERE pages != '[]'").fetchone()[0]
    n_src = c.execute("SELECT count(*) FROM cards WHERE sources != '[]'").fetchone()[0]
    print(f"\n带页码（可回溯）: {n_idx}   带来源: {n_src}")
    print("\n== 风险队列（被查得多 × 未复核，前 10） ==")
    q = """SELECT c.id, c.title, c.status, count(l.card_id) n
           FROM query_log l JOIN cards c ON c.id=l.card_id
           WHERE c.status IN ('draft','disputed')
           GROUP BY c.id ORDER BY n DESC LIMIT 10"""
    rows = list(c.execute(q))
    if not rows:
        print("  （暂无：还没有被检索过的未复核卡）")
    for r in rows:
        print(f"  {r['n']:>3} 次  {r['status']:<8} {r['id']}  {r['title'][:40]}")


def verify(args):
    c = con()
    r = c.execute("SELECT * FROM cards WHERE id=?", (args.id,)).fetchone()
    if not r:
        sys.exit(f"没有这张卡：{args.id}")
    r = dict(r)
    pages = jload(r["pages"], [])
    src = jload(r["sources"], [])
    print(f"回源核对：{r['id']}  ({TRUST_LABEL.get(r['status'])})")
    print(f"  作品：{r['work']}   页码：{pages or '无'}")
    print(f"  卡面来源文件：{r['origin']}")
    if r["evidence_quote"]:
        print(f'  证据引文："<<{r["evidence_quote"]}>>"')
    if src:
        for s in src:
            print(f"  - [{s.get('grade') or '?'}] {s.get('text')}")
    roots = REPO / "kb" / "page_roots.json"
    if roots.exists() and pages:
        m = json.loads(roots.read_text(encoding="utf-8"))
        root = m.get(r["work"])
        if root:
            print(f"  页图根目录：{root}")
            for p in pages[:3]:
                cand = Path(root) / f"p{p:03d}.png"
                print(f"    {cand}  {'✅存在' if cand.exists() else '（未找到，页码换算可能不同）'}")
        else:
            print("  （该作品未配置页图根目录，见 kb/page_roots.json）")
    print("\n核对步骤：read_image 打开页图 → 与 evidence_quote/卡面公式逐字比对 → "
          "一致则改 status=verified 并更新 review.last_verified_at。")


def main():
    ap = argparse.ArgumentParser(prog="q.py", description="数译知识库查询器")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search", help="全文检索")
    s.add_argument("query")
    s.add_argument("--kind")
    s.add_argument("--work")
    s.add_argument("--level")
    s.add_argument("--status")
    s.add_argument("--limit", type=int, default=8)
    s.add_argument("--include-draft", action="store_true")
    s.add_argument("--json", action="store_true")
    s.add_argument("--no-log", action="store_true")
    s.set_defaults(func=search)

    s = sub.add_parser("card", help="看单卡")
    s.add_argument("id")
    s.set_defaults(func=show_card)

    s = sub.add_parser("brief", help="阅读前置包")
    s.add_argument("--work")
    s.add_argument("--query")
    s.add_argument("--out")
    s.set_defaults(func=brief)

    s = sub.add_parser("gaps", help="跨书缺口")
    s.add_argument("--min-works", type=int, default=3)
    s.add_argument("--limit", type=int, default=40)
    s.set_defaults(func=gaps)

    s = sub.add_parser("stats", help="库统计")
    s.set_defaults(func=stats)

    s = sub.add_parser("verify", help="回源核对")
    s.add_argument("id")
    s.set_defaults(func=verify)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
