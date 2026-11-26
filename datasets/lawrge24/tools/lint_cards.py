#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""lawrge24 资料卡 lint：结构 + 页码 + 逐字引文核对。

用法（仓库根目录）：
    python datasets/lawrge24/tools/lint_cards.py [--quiet]
退出码 0 = 无 error；1 = 有 error。warning 不计失败。
"""
import glob
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import pages as P  # noqa: E402

TRACKS = {"O", "A", "B", "C", "D", "E"}
CONCEPT_REQ = ["id", "type", "track", "title", "aliases", "summary", "question",
               "definition", "key_points", "formulas", "theorems", "pitfalls",
               "related", "sources", "rights", "status", "verification",
               "provenance_note"]
DERIV_REQ = ["id", "type", "track", "title", "aliases", "summary", "question",
             "goal", "setup", "steps", "result", "pitfalls", "related",
             "sources", "rights", "status", "verification", "provenance_note"]
BOOK = "LAWRGE 2024 Notes, Relative Langlands Duality (2024-12-03, 73 pp.)"
CJK = re.compile(r"[\u3400-\u9fff]")


def load():
    out = []
    for kind in ("concepts", "derivations"):
        for p in sorted(glob.glob(os.path.join(ROOT, "cards", kind, "*.json"))):
            with io.open(p, encoding="utf-8") as f:
                out.append((p, json.load(f)))
    return out


def cjk_len(s):
    return len(CJK.findall(s or ""))


def main():
    quiet = "--quiet" in sys.argv
    errors, warns = [], []
    cards = load()
    ids = [c["id"] for _, c in cards]
    seen = set()
    for i in ids:
        if i in seen:
            errors.append("重复 id: %s" % i)
        seen.add(i)
    page_cache = {}

    for p, c in cards:
        rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
        cid = c.get("id", "")
        typ = c.get("type")

        req = CONCEPT_REQ if typ == "concept" else DERIV_REQ
        for k in req:
            if k not in c:
                errors.append("%s: 缺字段 %s" % (rel, k))

        prefix = "lawrge/concept/" if typ == "concept" else "lawrge/deriv/"
        if not cid.startswith(prefix):
            errors.append("%s: id 前缀应为 %s (%s)" % (rel, prefix, cid))
        if os.path.splitext(os.path.basename(p))[0] != cid.rsplit("/", 1)[-1]:
            errors.append("%s: 文件名与 slug 不一致" % rel)
        if c.get("track") not in TRACKS:
            errors.append("%s: track 非法 (%s)" % (rel, c.get("track")))
        if c.get("rights") != "rewritten":
            errors.append("%s: rights 必须 rewritten" % rel)
        if c.get("status") not in ("draft", "reviewed", "published"):
            errors.append("%s: status 非法" % rel)
        if c.get("verification", {}).get("status") != "source-only":
            errors.append("%s: verification.status 应为 source-only" % rel)

        s = c.get("summary", "")
        if cjk_len(s) > 120:
            errors.append("%s: summary 汉字 %d > 120" % (rel, cjk_len(s)))
        if not s:
            errors.append("%s: summary 为空" % rel)
        if not str(c.get("question", "")).rstrip().endswith("？"):
            warns.append("%s: question 未以全角问号结尾" % rel)

        if typ == "concept":
            if len(c.get("key_points", [])) < 3:
                errors.append("%s: key_points < 3" % rel)
            if len(c.get("formulas", [])) < 1:
                errors.append("%s: formulas 为空" % rel)
            if not c.get("definition", {}).get("text"):
                errors.append("%s: definition.text 为空" % rel)
            for t in c.get("theorems", []):
                pr = t.get("proof", {})
                if pr.get("status") not in ("complete", "sketch", "gap"):
                    errors.append("%s: theorem proof.status 非法 (%s)" % (rel, pr.get("status")))
                if pr.get("status") in ("sketch", "gap") and not pr.get("gap_note"):
                    errors.append("%s: %s 证明缺 gap_note" % (rel, t.get("name", "?")))
                for st in pr.get("steps", []):
                    if set(st) != {"no", "text", "why"}:
                        errors.append("%s: 证明步骤字段应为 no/text/why" % rel)
                if not t.get("source"):
                    errors.append("%s: theorem 缺 source" % rel)
        else:
            if len(c.get("steps", [])) < 4:
                errors.append("%s: 推导 steps < 4" % rel)
            for st in c.get("steps", []):
                if set(st) != {"no", "text", "why", "locator", "provenance"}:
                    errors.append("%s: 推导步骤字段应为 no/text/why/locator/provenance" % rel)
                if st.get("provenance") not in ("A", "B", "C"):
                    errors.append("%s: 步骤 provenance 非法" % rel)
            if not c.get("goal") or not c.get("result"):
                errors.append("%s: goal/result 为空" % rel)
            if len(c.get("setup", [])) < 2:
                errors.append("%s: setup < 2" % rel)

        if len(c.get("pitfalls", [])) < 2:
            errors.append("%s: pitfalls < 2" % rel)
        rels = c.get("related", [])
        if len(rels) < 2:
            errors.append("%s: related < 2" % rel)
        for r in rels:
            if r == cid:
                errors.append("%s: related 指向自身" % rel)
            if r not in ids:
                errors.append("%s: related 指向不存在 %s" % (rel, r))

        if not c.get("sources"):
            errors.append("%s: sources 为空" % rel)
        for si, src in enumerate(c.get("sources", [])):
            for k in ("text", "book", "section", "pages", "pdf_pages", "anchor", "quote"):
                if k not in src:
                    errors.append("%s: source[%d] 缺 %s" % (rel, si, k))
            if src.get("text") != "A" or src.get("book") != BOOK:
                errors.append("%s: source[%d] text/book 不符" % (rel, si))
            pg = src.get("pages", [])
            pdf = src.get("pdf_pages", [])
            if not (isinstance(pg, list) and len(pg) == 2 and isinstance(pdf, list) and len(pdf) == 2):
                errors.append("%s: source[%d] pages/pdf_pages 应为两个整数" % (rel, si))
                continue
            if len(pg) != len(pdf):
                errors.append("%s: source[%d] pages/pdf_pages 长度不一致" % (rel, si))
            if pg[0] != pg[1]:
                errors.append("%s: source[%d] 一条 source 只引一页 (pages=%s)" % (rel, si, pg))
            n = int(pg[0])
            if not (1 <= n <= 73):
                errors.append("%s: source[%d] 页码越界" % (rel, si))
                continue
            if src.get("anchor") != "A p.%d" % n:
                errors.append("%s: source[%d] anchor 应为 A p.%d" % (rel, si, n))
            m = re.search(r"§\s*(\d+)", src.get("section", ""))
            if not m:
                errors.append("%s: source[%d] section 应为 §N" % (rel, si))
                continue
            if src.get("pdf_pages", [None])[0] != n:
                errors.append("%s: source[%d] pdf_pages 与 pages 不一致" % (rel, si))
            ch = int(m.group(1))
            if ch not in page_cache:
                page_cache[ch] = P.load_pages(ch)
            txt = page_cache[ch].get(n)
            q = src.get("quote", "")
            if txt is None:
                errors.append("%s: source[%d] §%d 无第 %d 页" % (rel, si, ch, n))
            else:
                if not (12 <= len(q) <= 120):
                    errors.append("%s: source[%d] quote 长度 %d 越界" % (rel, si, len(q)))
                if CJK.search(q):
                    errors.append("%s: source[%d] quote 含中文" % (rel, si))
                if P.norm(q) not in P.norm(txt):
                    errors.append("%s: source[%d] quote 未在 §%d p.%d 命中: %r"
                                  % (rel, si, ch, n, q[:40]))
            if not (isinstance(src.get("anchor"), str)):
                errors.append("%s: source[%d] anchor 非字符串" % (rel, si))

        if not c.get("provenance_note"):
            errors.append("%s: provenance_note 为空" % rel)

    if not quiet:
        for e in errors:
            print("ERROR " + e)
        for w in warns:
            print("WARN  " + w)
    print("cards=%d errors=%d warnings=%d" % (len(cards), len(errors), len(warns)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
