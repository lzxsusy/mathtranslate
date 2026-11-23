#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""冲突台账：登记、裁定、关单、校验。

用法：
  python tools/conflict_report.py add --kind C1 --severity P1 --target "T1094 stack" \
      --claim "..." --query "grep ..." --hits "..." [--source "..."] [--reporter lead]
  python tools/conflict_report.py list [--status open] [--severity P0] [--kind C1] [--query 词]
  python tools/conflict_report.py show --id CF-2026-11-23-01
  python tools/conflict_report.py close --id ... --status accepted|rejected|deferred|fixed \
      [--resolution "..."] [--resolver ...] [--evidence "..."] [--note "..."]
  python tools/conflict_report.py note --id ... --text "改了哪些文件、跑了什么闸门"
  python tools/conflict_report.py md                # 渲染 _meta/冲突台账.md 到 stdout
  python tools/conflict_report.py check             # 校验字段、id 唯一、md 是否同步
  python tools/conflict_report.py check --delivery  # 交付前：额外要求 P0 未处理数 = 0

台账：_meta/冲突台账.tsv（TAB 分隔，一行一冲突）
渲染：_meta/冲突台账.md（由 `md` 生成，不要手改）

规则（与 04_playbook/19_译中检索与冲突上报.md 一致）：
  - id 形如 CF-YYYY-MM-DD-NN，登记时自增；
  - kind 取 C1..C6；severity 取 P0..P3；status 取 open/accepted/rejected/deferred/fixed；
  - status=fixed 必须有 note（执行记录）；accepted/rejected 必须有 resolution；
  - target 若像仓库内路径，则在 check 时要求文件存在；
  - check 失败返回 1，成功返回 0。
"""

from __future__ import annotations

import argparse
import datetime as _dt
import os
import re
import sys

try:  # Windows 控制台默认 GBK，会把中文输出写成乱码甚至抛错
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # pragma: no cover
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TSV = os.path.join(ROOT, "_meta", "冲突台账.tsv")
MD = os.path.join(ROOT, "_meta", "冲突台账.md")

COLS = [
    "id", "date", "reporter", "kind", "severity", "target", "claim",
    "query", "hits", "source", "status", "resolution", "resolver", "resolved", "note",
]
KINDS = ["C1", "C2", "C3", "C4", "C5", "C6"]
SEV = ["P0", "P1", "P2", "P3"]
STATUS = ["open", "accepted", "rejected", "deferred", "fixed"]
ID_RE = re.compile(r"^CF-(\d{4}-\d{2}-\d{2})-(\d{2})$")

# target 里出现这些扩展名或斜杠，就当作仓库内路径检查存在性
PATH_HINT = re.compile(r"(^|[/\\])[\w.-]+\.(tex|json|tsv|md|py|csv)$|[/\\]")


def _clean(s: str) -> str:
    return (s or "").replace("\t", " ").replace("\r", " ").replace("\n", " ").strip()


def load() -> list[dict]:
    if not os.path.exists(TSV):
        return []
    rows = []
    with open(TSV, encoding="utf-8", newline="") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        if header != COLS:
            raise SystemExit(f"[err] 台账表头不符。期望 {COLS}，实际 {header}")
        for line in fh:
            if not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            parts += [""] * (len(COLS) - len(parts))
            rows.append(dict(zip(COLS, parts)))
    return rows


def save(rows: list[dict]) -> None:
    os.makedirs(os.path.dirname(TSV), exist_ok=True)
    with open(TSV, "w", encoding="utf-8", newline="") as fh:
        fh.write("\t".join(COLS) + "\n")
        for r in rows:
            fh.write("\t".join(_clean(r.get(c, "")) for c in COLS) + "\n")


def next_id(rows: list[dict], today: str) -> str:
    used = {r["id"] for r in rows}
    n = 1
    while f"CF-{today}-{n:02d}" in used:
        n += 1
    return f"CF-{today}-{n:02d}"


def render_md(rows: list[dict]) -> str:
    order = {s: i for i, s in enumerate(["open", "accepted", "deferred", "rejected", "fixed"])}
    rows = sorted(rows, key=lambda r: (r["severity"], order.get(r["status"], 9), r["id"]))
    open_rows = [r for r in rows if r["status"] in ("open", "accepted", "deferred")]
    p0 = [r for r in open_rows if r["severity"] == "P0"]
    out = []
    out.append("# 冲突台账（自动生成）")
    out.append("")
    out.append("> 源文件 `_meta/冲突台账.tsv`；本文件由 `python tools/conflict_report.py md --write` 生成，**不要手改**。")
    out.append("> 规则见 [`04_playbook/19_译中检索与冲突上报.md`](../04_playbook/19_译中检索与冲突上报.md)。")
    out.append("")
    out.append(f"- 条目：{len(rows)}（未闭环 {len(open_rows)}，其中 P0 {len(p0)}）")
    out.append("")
    if p0:
        out.append("## ⚠ P0 未闭环（不许带着交付）")
        out.append("")
        for r in p0:
            out.append(f"- `{r['id']}`（{r['kind']}，{r['status']}）：{r['target']} — {r['claim']}")
        out.append("")
    out.append("## 未闭环")
    out.append("")
    out.append("| id | 级 | 类 | 对象 | 问题 | 状态 |")
    out.append("|---|---|---|---|---|---|")
    for r in open_rows:
        out.append(f"| {r['id']} | {r['severity']} | {r['kind']} | {r['target']} | {r['claim']} | {r['status']} |")
    out.append("")
    out.append("## 已闭环")
    out.append("")
    out.append("| id | 级 | 类 | 对象 | 裁定 | 裁定人 |")
    out.append("|---|---|---|---|---|---|")
    for r in [x for x in rows if x["status"] in ("fixed", "rejected")]:
        out.append(f"| {r['id']} | {r['severity']} | {r['kind']} | {r['target']} | {r['resolution']} | {r['resolver']} |")
    out.append("")
    return "\n".join(out) + "\n"


def cmd_add(a) -> int:
    rows = load()
    today = a.date or _dt.date.today().isoformat()
    if a.kind not in KINDS:
        raise SystemExit(f"[err] kind 必须是 {KINDS}")
    if a.severity not in SEV:
        raise SystemExit(f"[err] severity 必须是 {SEV}")
    row = {c: "" for c in COLS}
    row.update(
        id=next_id(rows, today), date=today, reporter=a.reporter or "unknown",
        kind=a.kind, severity=a.severity, target=a.target, claim=a.claim,
        query=a.query, hits=a.hits, source=a.source or "", status="open",
    )
    rows.append(row)
    save(rows)
    print(f"[add] {row['id']}  {row['severity']}/{row['kind']}  {row['target']}")
    return 0


def cmd_list(a) -> int:
    rows = load()
    if a.status == "open_only":
        rows = [r for r in rows if r["status"] in ("open", "accepted", "deferred")]
    elif a.status:
        rows = [r for r in rows if r["status"] == a.status]
    if a.severity:
        rows = [r for r in rows if r["severity"] == a.severity]
    if a.kind:
        rows = [r for r in rows if r["kind"] == a.kind]
    if a.query:
        q = a.query.lower()
        rows = [r for r in rows if q in " ".join(r.values()).lower()]
    if not rows:
        print("[list] 无条目")
        return 0
    for r in rows:
        print(f"{r['id']}  {r['severity']}/{r['kind']}/{r['status']:<8}  {r['target']}  —  {r['claim']}")
    print(f"[list] {len(rows)} 条")
    return 0


def cmd_show(a) -> int:
    for r in load():
        if r["id"] == a.id:
            for c in COLS:
                print(f"{c:>11}: {r[c]}")
            return 0
    print(f"[err] 无此 id: {a.id}")
    return 1


def cmd_close(a) -> int:
    rows = load()
    if a.status not in STATUS:
        raise SystemExit(f"[err] status 必须是 {STATUS}")
    for r in rows:
        if r["id"] != a.id:
            continue
        r["status"] = a.status
        if a.resolution:
            r["resolution"] = a.resolution
        if a.resolver:
            r["resolver"] = a.resolver
        if a.evidence:
            r["note"] = (r["note"] + "；" if r["note"] else "") + f"证据：{a.evidence}"
        if a.note:
            r["note"] = (r["note"] + "；" if r["note"] else "") + a.note
        if a.status in ("accepted", "rejected", "deferred", "fixed") and not r["resolved"]:
            r["resolved"] = _dt.date.today().isoformat()
        if a.status == "fixed" and not r["note"]:
            raise SystemExit("[err] status=fixed 必须给 --note（改了哪些文件、跑了什么闸门）")
        if a.status in ("accepted", "rejected") and not r["resolution"]:
            raise SystemExit("[err] accepted/rejected 必须给 --resolution")
        save(rows)
        print(f"[close] {r['id']} → {r['status']}")
        return 0
    print(f"[err] 无此 id: {a.id}")
    return 1


def cmd_note(a) -> int:
    rows = load()
    for r in rows:
        if r["id"] == a.id:
            r["note"] = (r["note"] + "；" if r["note"] else "") + a.text
            save(rows)
            print(f"[note] {r['id']}")
            return 0
    print(f"[err] 无此 id: {a.id}")
    return 1


def cmd_md(a) -> int:
    text = render_md(load())
    if getattr(a, "write", False):
        os.makedirs(os.path.dirname(MD), exist_ok=True)
        with open(MD, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print(f"[md] 已写入 {os.path.relpath(MD, ROOT)}（UTF-8）")
        return 0
    sys.stdout.write(text)
    return 0


def cmd_check(a) -> int:
    rows = load()
    errs, warns = [], []
    seen = set()
    for r in rows:
        rid = r["id"]
        if not ID_RE.match(rid):
            errs.append(f"{rid}: id 格式不符 CF-YYYY-MM-DD-NN")
        if rid in seen:
            errs.append(f"{rid}: id 重复")
        seen.add(rid)
        if r["kind"] not in KINDS:
            errs.append(f"{rid}: kind 非法 {r['kind']!r}")
        if r["severity"] not in SEV:
            errs.append(f"{rid}: severity 非法 {r['severity']!r}")
        if r["status"] not in STATUS:
            errs.append(f"{rid}: status 非法 {r['status']!r}")
        if r["status"] == "fixed" and not r["note"]:
            errs.append(f"{rid}: fixed 但无 note")
        if r["status"] in ("accepted", "rejected") and not r["resolution"]:
            errs.append(f"{rid}: {r['status']} 但无 resolution")
        if r["status"] in ("fixed", "rejected") and not r["resolver"]:
            warns.append(f"{rid}: {r['status']} 但未记 resolver")
        for c in ("claim", "query", "hits", "target"):
            if not r[c]:
                errs.append(f"{rid}: 必填列 {c} 为空")
        tgt = r["target"]
        if PATH_HINT.search(tgt):
            cand = tgt.split(":")[0].strip()
            cand = cand.split(" ")[0] if " " in cand and not os.path.exists(os.path.join(ROOT, cand)) else cand
            if cand and not os.path.exists(os.path.join(ROOT, cand)):
                errs.append(f"{rid}: target 指向的文件不存在：{cand}")

    open_p0 = [r for r in rows if r["severity"] == "P0" and r["status"] in ("open", "accepted", "deferred")]
    if open_p0:
        msg = "P0 未闭环 " + ", ".join(r["id"] for r in open_p0)
        (errs if a.delivery else warns).append(msg)

    # md 同步
    md_path = MD
    if os.path.exists(md_path):
        with open(md_path, encoding="utf-8") as fh:
            on_disk = fh.read()
        if on_disk != render_md(rows):
            errs.append("_meta/冲突台账.md 与 tsv 不同步，请重跑 `python tools/conflict_report.py md --write`")
    elif rows:
        errs.append("_meta/冲突台账.md 不存在（有台账行时必须渲染一份）")

    for w in warns:
        print(f"[warn] {w}")
    for e in errs:
        print(f"[err] {e}")
    if errs:
        print(f"[fail] {len(errs)} 处问题，{len(rows)} 行台账")
        return 1
    print(f"[ok] 台账 {len(rows)} 行（未闭环 {sum(1 for r in rows if r['status'] in ('open','accepted','deferred'))}，P0 未闭环 {len(open_p0)}）")
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="冲突台账（译中检索与冲突上报）")
    sub = p.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("add", help="登记一条冲突")
    pa.add_argument("--kind", required=True)
    pa.add_argument("--severity", required=True)
    pa.add_argument("--target", required=True)
    pa.add_argument("--claim", required=True)
    pa.add_argument("--query", required=True)
    pa.add_argument("--hits", required=True)
    pa.add_argument("--source", default="")
    pa.add_argument("--reporter", default="")
    pa.add_argument("--date", default="")
    pa.set_defaults(func=cmd_add)

    pl = sub.add_parser("list", help="列出条目")
    pl.add_argument("--status", default="", help="open/accepted/rejected/deferred/fixed；写 open_only 列出未闭环")
    pl.add_argument("--severity", default="")
    pl.add_argument("--kind", default="")
    pl.add_argument("--query", default="")
    pl.set_defaults(func=cmd_list)

    ps = sub.add_parser("show", help="显示一条")
    ps.add_argument("--id", required=True)
    ps.set_defaults(func=cmd_show)

    pc = sub.add_parser("close", help="裁定/关单")
    pc.add_argument("--id", required=True)
    pc.add_argument("--status", required=True)
    pc.add_argument("--resolution", default="")
    pc.add_argument("--resolver", default="")
    pc.add_argument("--evidence", default="")
    pc.add_argument("--note", default="")
    pc.set_defaults(func=cmd_close)

    pn = sub.add_parser("note", help="追加执行记录")
    pn.add_argument("--id", required=True)
    pn.add_argument("--text", required=True)
    pn.set_defaults(func=cmd_note)

    pm = sub.add_parser("md", help="渲染 markdown（默认 stdout；--write 直接写 _meta/冲突台账.md）")
    pm.add_argument("--write", action="store_true", help="以 UTF-8 写入 _meta/冲突台账.md")
    pm.set_defaults(func=cmd_md)

    pk = sub.add_parser("check", help="校验台账")
    pk.add_argument("--delivery", action="store_true", help="交付前模式：P0 未闭环即失败")
    pk.set_defaults(func=cmd_check)

    a = p.parse_args(argv)
    return a.func(a)


if __name__ == "__main__":
    sys.exit(main())
