#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数译知识库 · 建库器（P1）

把 kb/cards/*.jsonl 建成单文件 SQLite：kb/shuyi.db
  cards       结构化字段（一律合法 JSON 存列表字段）
  fts_uni     unicode61 分词（拉丁词）
  fts_tri     trigram 分词（中文子串检索，SQLite ≥3.34）
  query_log   检索日志 → 用于“被查得多 × 未复核”的风险加权审计

用法： python kb/build_kb.py [--rebuild]
"""
import json
import sqlite3
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
KB = REPO / "kb"
CARDS = KB / "cards"
CARDS5 = KB / "cards5"
DB = KB / "shuyi.db"

REQUIRED = ("id", "work", "kind", "title", "status", "origin")


def load_cards():
    seen = {}
    files = sorted(CARDS.glob("*.jsonl")) + sorted(CARDS5.glob("*.jsonl"))
    for p in files:
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                c = json.loads(line)
            except json.JSONDecodeError as exc:
                print(f"  ! 坏行 {p.name}: {exc}")
                continue
            missing = [k for k in REQUIRED if not c.get(k)]
            if missing:
                print(f"  ! 缺字段 {missing}: {c.get('id') or p.name}")
                continue
            if c["id"] in seen:
                print(f"  ! 重复 id，保留首个: {c['id']}")
                continue
            seen[c["id"]] = c
    return list(seen.values())


def norm_dashes(s: str) -> str:
    """把各种连字符/破折号归一成 ASCII '-'，否则 "Gromov–Witten"(en dash) 查不到 "Gromov-Witten" """
    return (s or "").replace("\u2013", "-").replace("\u2014", "-").replace("\u2010", "-").replace("\u2212", "-")


def fts_text(c):
    parts = [c.get("title") or "", c.get("title_en") or ""]
    parts += c.get("aliases") or []
    for t in (c.get("terms") or []):
        if isinstance(t, dict):
            parts += [str(v) for v in t.values() if v]
        else:
            parts.append(str(t))
    parts += c.get("symbols") or []
    parts.append(c.get("summary") or "")
    return norm_dashes(" ".join(x for x in parts if x))


def build(cards):
    if DB.exists():
        DB.unlink()
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.executescript("""
    PRAGMA journal_mode=WAL;
    CREATE TABLE cards(
      id TEXT PRIMARY KEY, work TEXT, kind TEXT, level TEXT,
      title TEXT, title_en TEXT, aliases TEXT, pages TEXT, prereqs TEXT,
      links TEXT, sources TEXT, evidence_quote TEXT, status TEXT,
      review TEXT, terms TEXT, symbols TEXT, caveat TEXT,
      updated TEXT, origin TEXT, summary TEXT
    );
    CREATE INDEX idx_cards_work ON cards(work);
    CREATE INDEX idx_cards_status ON cards(status);
    CREATE INDEX idx_cards_kind ON cards(kind);
    CREATE VIRTUAL TABLE fts_uni USING fts5(id UNINDEXED, body, tokenize='unicode61');
    CREATE VIRTUAL TABLE fts_tri USING fts5(id UNINDEXED, body, tokenize='trigram');
    CREATE TABLE query_log(
      n INTEGER PRIMARY KEY AUTOINCREMENT,
      card_id TEXT, q TEXT, ts TEXT DEFAULT (datetime('now','localtime'))
    );
    """)
    for c in cards:
        cur.execute(
            "INSERT OR REPLACE INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                c["id"], c["work"], c["kind"], c.get("level"),
                c["title"], c.get("title_en"),
                json.dumps(c.get("aliases") or [], ensure_ascii=False),
                json.dumps(c.get("pages") or []),
                json.dumps(c.get("prereqs") or [], ensure_ascii=False),
                json.dumps(c.get("links") or [], ensure_ascii=False),
                json.dumps(c.get("sources") or [], ensure_ascii=False),
                c.get("evidence_quote"),
                c["status"],
                json.dumps(c.get("review") or {}, ensure_ascii=False),
                json.dumps(c.get("terms") or [], ensure_ascii=False),
                json.dumps(c.get("symbols") or [], ensure_ascii=False),
                c.get("caveat"),
                c.get("updated") or "",
                c["origin"],
                c.get("summary") or "",
            ),
        )
        body = fts_text(c)
        cur.execute("INSERT INTO fts_uni(id, body) VALUES (?,?)", (c["id"], body))
        cur.execute("INSERT INTO fts_tri(id, body) VALUES (?,?)", (c["id"], body))
    con.commit()
    n = cur.execute("SELECT count(*) FROM cards").fetchone()[0]
    print(f"[build] {n} 张卡 → {DB}")
    for row in cur.execute("SELECT status, count(*) FROM cards GROUP BY status ORDER BY 2 DESC"):
        print(f"   status {row[0]:<10} {row[1]}")
    con.close()


def main():
    cards = load_cards()
    if not cards:
        print("kb/cards 为空，先跑 python kb/ingest.py all")
        sys.exit(1)
    build(cards)


if __name__ == "__main__":
    main()
