#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把 资料卡/_partials/*.tsv 合并成五件套的机器可读层。

用法（在工程目录下）：
    python 资料卡/tools/build_cards.py

输入：资料卡/_partials/concept_*.tsv、stmt_*.tsv（表头见下）
输出：资料卡/01-概念.tsv、02-命题.tsv、index.jsonl、cards/concepts/*.json、
      cards/statements/*.json
校验：id 唯一、页码为整数、quote ≤120 字符、列数正确；有错直接非零退出。
"""
import csv
import glob
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 资料卡/
PART = os.path.join(ROOT, "_partials")

CONCEPT_COLS = ["id", "英文", "中文", "原书页", "PDF页", "一句话直觉",
                "精确陈述", "依赖", "quote", "状态"]
STMT_COLS = ["id", "编号", "块", "原书页", "PDF页", "类型", "假设", "结论",
             "证明骨架", "label", "依赖", "quote", "状态"]

ID_RE = re.compile(r"^SY02-27\.(concept|stmt)\.[A-Za-z0-9][A-Za-z0-9._-]*$")


def read_part(pattern, cols, label):
    rows, errors = [], []
    for path in sorted(glob.glob(os.path.join(PART, pattern))):
        with io.open(path, encoding="utf-8-sig", newline="") as fh:
            rd = csv.reader(fh, delimiter="\t")
            header = next(rd, None)
            if header != cols:
                errors.append("%s: 表头不符: %r" % (os.path.basename(path), header))
                continue
            for ln, row in enumerate(rd, 2):
                if not any(c.strip() for c in row):
                    continue
                if len(row) != len(cols):
                    errors.append("%s:%d 列数 %d != %d" % (path, ln, len(row), len(cols)))
                    continue
                d = dict(zip(cols, [c.strip() for c in row]))
                if not ID_RE.match(d["id"]):
                    errors.append("%s:%d 非法 id %s" % (path, ln, d["id"]))
                for k in ("原书页", "PDF页"):
                    if not re.match(r"^\d+$", d[k]):
                        errors.append("%s:%d %s 非整数: %s" % (path, ln, k, d[k]))
                if len(d["quote"]) > 120:
                    errors.append("%s:%d quote 超 120 字符（%d）" % (path, ln, len(d["quote"])))
                if d["quote"] not in ("-", "") and d["quote"] != d["quote"].strip():
                    pass
                if d["状态"] not in ("已核", "未复核"):
                    errors.append("%s:%d 状态非法: %s" % (path, ln, d["状态"]))
                q = d["quote"]
                if len(q) >= 2 and q[0] == '"' and q[-1] == '"':
                    d["quote"] = q[1:-1]
                rows.append(d)
    ids = {}
    for r in rows:
        if r["id"] in ids:
            errors.append("重复 id: %s（%s 与 %s）" % (r["id"], ids[r["id"]], r.get("块", "")))
        ids[r["id"]] = r.get("块", "")
    print("[%s] %d 行，%d 个错误" % (label, len(rows), len(errors)))
    return rows, errors


def write_tsv(path, cols, rows):
    with io.open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(cols)
        for r in rows:
            w.writerow([r[c] for c in cols])


def slug(s):
    return re.sub(r"[^A-Za-z0-9._-]+", "-", s).strip("-").lower()


def main():
    concepts, e1 = read_part("concept_*.tsv", CONCEPT_COLS, "概念")
    stmts, e2 = read_part("stmt_*.tsv", STMT_COLS, "命题")
    errors = e1 + e2

    concepts.sort(key=lambda r: (int(r["PDF页"]), r["id"]))
    stmts.sort(key=lambda r: (int(r["PDF页"]), r["id"]))

    write_tsv(os.path.join(ROOT, "01-概念.tsv"), CONCEPT_COLS, concepts)
    write_tsv(os.path.join(ROOT, "02-命题.tsv"), STMT_COLS, stmts)

    os.makedirs(os.path.join(ROOT, "cards", "concepts"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "cards", "statements"), exist_ok=True)
    index = []

    for r in concepts:
        tail = r["id"].split(".concept.", 1)[1]
        path = "cards/concepts/%s.json" % slug(tail)
        obj = {
            "id": r["id"],
            "type": "concept",
            "title": r["中文"],
            "aliases": [r["英文"]],
            "summary": r["一句话直觉"],
            "source": {
                "work": "SY02-27",
                "pages": [int(r["原书页"])],
                "pdf_pages": [int(r["PDF页"])],
                "quote": r["quote"],
            },
            "definition": r["精确陈述"],
            "depends_on": [] if r["依赖"] in ("-", "") else
                          [x.strip() for x in r["依赖"].split(",") if x.strip()],
            "rights": "rewritten",
            "status": "已核" if r["状态"] == "已核" else "未复核",
        }
        with io.open(os.path.join(ROOT, path), "w", encoding="utf-8") as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=2)
        index.append({
            "id": r["id"], "type": "concept", "title": r["中文"],
            "aliases": [r["英文"]], "summary": r["一句话直觉"],
            "pages": [int(r["原书页"])], "pdf_pages": [int(r["PDF页"])],
            "status": obj["status"], "path": path,
        })

    for r in stmts:
        tail = r["id"].split(".stmt.", 1)[1]
        path = "cards/statements/%s.json" % slug(tail)
        obj = {
            "id": r["id"],
            "type": "statement",
            "title": "%s %s" % (r["类型"], r["编号"]),
            "kind": r["类型"],
            "number": r["编号"],
            "block": r["块"],
            "source": {
                "work": "SY02-27",
                "pages": [int(r["原书页"])],
                "pdf_pages": [int(r["PDF页"])],
                "quote": r["quote"],
            },
            "hypotheses": r["假设"],
            "conclusion": r["结论"],
            "proof_skeleton": [x.strip() for x in r["证明骨架"].split("→") if x.strip()],
            "label": r["label"],
            "depends_on": [] if r["依赖"] in ("-", "") else
                          [x.strip() for x in r["依赖"].split(",") if x.strip()],
            "rights": "rewritten",
            "status": "已核" if r["状态"] == "已核" else "未复核",
        }
        with io.open(os.path.join(ROOT, path), "w", encoding="utf-8") as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=2)
        index.append({
            "id": r["id"], "type": "statement", "title": obj["title"],
            "number": r["编号"], "block": r["块"],
            "pages": [int(r["原书页"])], "pdf_pages": [int(r["PDF页"])],
            "status": obj["status"], "path": path,
        })

    align = os.path.join(ROOT, "alignment.jsonl")
    if os.path.exists(align):
        with io.open(align, encoding="utf-8") as fh:
            for ln in fh:
                if not ln.strip():
                    continue
                a = json.loads(ln)
                index.append({
                    "id": a["id"], "type": "alignment",
                    "title": a["id"].split(".align.", 1)[-1],
                    "concept": a.get("concept"), "pages": a["source"]["pages"],
                    "status": a.get("status", "gap"), "path": "alignment.jsonl",
                })

    with io.open(os.path.join(ROOT, "index.jsonl"), "w", encoding="utf-8") as fh:
        for it in index:
            fh.write(json.dumps(it, ensure_ascii=False) + "\n")

    print("[写出] 01-概念 %d 条，02-命题 %d 条，index %d 条" % (len(concepts), len(stmts), len(index)))
    if errors:
        print("[错误] %d 条：" % len(errors))
        for e in errors[:40]:
            print("  -", e)
        return 1
    print("[OK] 卡片机器层生成完毕")
    return 0


if __name__ == "__main__":
    sys.exit(main())
