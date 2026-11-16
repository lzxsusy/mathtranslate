#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lint_geoq.py —— 几何量子化资料卡质检。

用法：
    python tools/lint_geoq.py cards                 # 全量质检
    python tools/lint_geoq.py cards --allow-missing # 起草阶段（允许 related 指向尚未写出的卡）
    python tools/lint_geoq.py cards --json          # 机器可读报告

检查项：
  1. JSON 可解析、必填字段、类型
  2. id 前缀 / slug / 文件名三者一致
  3. summary 长度（概念 ≤120、例子 ≤100 汉字，去掉空白与公式后计数）
  4. 页码：pages ⊆ [250,296]，pdf_pages 逐项 = pages+1 ⊆ [251,297]
  5. 证明：complete ≥2 步且 text/why 非空；sketch 必须有 gap_note
  6. 例子：computation ≥2 步；setup/result/check 非空
  7. 交叉引用可解析（--allow-missing 时只报未解析数）
  8. 重复 id、track 合法性、question 以问号结尾
"""
import argparse
import json
import re
import sys
from pathlib import Path

TRACKS = {"A", "B", "C", "D", "O"}
ID_RE = re.compile(r"^geoq/(concept|example)/([a-z0-9]+(?:-[a-z0-9]+)*)$")
ANCHOR_RE = re.compile(r"^ch05[ab]\.tex:\d+-\d+$")
BOOK_PAGES = (250, 296)
PDF_PAGES = (251, 297)


def text_len(s: str) -> int:
    s = re.sub(r"\$[^$]*\$", "", s or "")
    s = re.sub(r"\s+", "", s)
    return len(s)


def err(errors, path, msg):
    errors.append(f"{path.name}: {msg}")


def check_sources(errors, path, card, is_concept):
    srcs = card.get("sources")
    if not isinstance(srcs, list) or not srcs:
        err(errors, path, "sources 必须是非空数组")
        return
    for i, s in enumerate(srcs):
        tag = f"sources[{i}]"
        if not isinstance(s, dict):
            err(errors, path, f"{tag} 不是对象")
            continue
        for k in ("book", "section", "pages", "pdf_pages", "anchor"):
            if k not in s:
                err(errors, path, f"{tag} 缺字段 {k}")
        pages = s.get("pages")
        pdf = s.get("pdf_pages")
        if not (isinstance(pages, list) and len(pages) == 2 and all(isinstance(x, int) for x in pages)):
            err(errors, path, f"{tag}.pages 必须是两个整数")
            continue
        if not (isinstance(pdf, list) and len(pdf) == 2 and all(isinstance(x, int) for x in pdf)):
            err(errors, path, f"{tag}.pdf_pages 必须是两个整数")
            continue
        if not (BOOK_PAGES[0] <= pages[0] <= pages[1] <= BOOK_PAGES[1]):
            err(errors, path, f"{tag}.pages={pages} 越界（印刷页 {BOOK_PAGES[0]}–{BOOK_PAGES[1]}）")
        if pdf != [pages[0] + 1, pages[1] + 1]:
            err(errors, path, f"{tag}.pdf_pages={pdf} 应等于 pages+1={[pages[0]+1, pages[1]+1]}")
        if not (PDF_PAGES[0] <= pdf[0] <= pdf[1] <= PDF_PAGES[1]):
            err(errors, path, f"{tag}.pdf_pages={pdf} 越界（PDF 页 {PDF_PAGES[0]}–{PDF_PAGES[1]}）")
        anchor = s.get("anchor", "")
        if not ANCHOR_RE.match(anchor):
            err(errors, path, f"{tag}.anchor={anchor!r} 应形如 ch05a.tex:94-105")


def check_concept(errors, path, card):
    d = card.get("definition")
    if not isinstance(d, dict) or not str(d.get("text", "")).strip():
        err(errors, path, "definition.text 不能为空")
    elif not isinstance(d.get("notation", ""), str):
        err(errors, path, "definition.notation 必须是字符串")
    kp = card.get("key_points")
    if not (isinstance(kp, list) and len(kp) >= 3):
        err(errors, path, "key_points 至少 3 条")
    fm = card.get("formulas")
    if not (isinstance(fm, list) and len(fm) >= 1):
        err(errors, path, "formulas 至少 1 条")
    ths = card.get("theorems")
    if not (isinstance(ths, list) and ths):
        err(errors, path, "theorems 至少 1 条")
        return
    for i, th in enumerate(ths):
        tag = f"theorems[{i}]"
        if not isinstance(th, dict):
            err(errors, path, f"{tag} 不是对象")
            continue
        for k in ("name", "statement", "proof", "source"):
            if not str(th.get(k, "")).strip():
                err(errors, path, f"{tag}.{k} 不能为空")
        pr = th.get("proof")
        if not isinstance(pr, dict):
            err(errors, path, f"{tag}.proof 不是对象")
            continue
        status = pr.get("status")
        if status not in ("complete", "sketch"):
            err(errors, path, f"{tag}.proof.status={status!r} 应为 complete/sketch")
        steps = pr.get("steps")
        if not isinstance(steps, list):
            err(errors, path, f"{tag}.proof.steps 必须是数组")
            continue
        if status == "complete" and len(steps) < 2:
            err(errors, path, f"{tag} 标记 complete 但少于 2 步")
        for j, st in enumerate(steps):
            if not isinstance(st, dict):
                err(errors, path, f"{tag}.steps[{j}] 不是对象")
                continue
            if not isinstance(st.get("no"), int):
                err(errors, path, f"{tag}.steps[{j}].no 必须是整数")
            if not str(st.get("text", "")).strip():
                err(errors, path, f"{tag}.steps[{j}].text 不能为空")
            if not str(st.get("why", "")).strip():
                err(errors, path, f"{tag}.steps[{j}].why 不能为空")
        if status == "sketch" and not str(pr.get("gap_note", "")).strip():
            err(errors, path, f"{tag} 标记 sketch 但 gap_note 为空")


def check_example(errors, path, card):
    refs = card.get("concept_refs")
    if not (isinstance(refs, list) and refs):
        err(errors, path, "concept_refs 至少 1 条")
    for k in ("setup", "result", "check"):
        if not str(card.get(k, "")).strip():
            err(errors, path, f"{k} 不能为空")
    comp = card.get("computation")
    if not (isinstance(comp, list) and len(comp) >= 2):
        err(errors, path, "computation 至少 2 步")
        return
    for j, st in enumerate(comp):
        if not isinstance(st, dict):
            err(errors, path, f"computation[{j}] 不是对象")
            continue
        if not isinstance(st.get("no"), int):
            err(errors, path, f"computation[{j}].no 必须是整数")
        if not str(st.get("text", "")).strip():
            err(errors, path, f"computation[{j}].text 不能为空")
        if not str(st.get("why", "")).strip():
            err(errors, path, f"computation[{j}].why 不能为空")


def lint(root: Path, allow_missing: bool = False):
    errors, warnings = [], []
    cards = {}
    files = sorted((root / "concepts").glob("*.json")) + sorted((root / "examples").glob("*.json"))
    if not files:
        return ["没有找到任何卡片文件"], []
    for path in files:
        try:
            card = json.loads(path.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            err(errors, path, f"JSON 解析失败：{e}")
            continue
        cid = card.get("id", "")
        m = ID_RE.match(cid)
        if not m:
            err(errors, path, f"id={cid!r} 不合法")
            continue
        typ, slug = m.group(1), m.group(2)
        if path.stem != slug:
            err(errors, path, f"文件名 {path.stem!r} 与 id slug {slug!r} 不一致")
        expected_dir = "concepts" if typ == "concept" else "examples"
        if path.parent.name != expected_dir:
            err(errors, path, f"type={typ} 应放在 {expected_dir}/ 下")
        if cid in cards:
            err(errors, path, f"重复 id {cid}（另一份在 {cards[cid].name}）")
        cards[cid] = path

        if card.get("type") != typ:
            err(errors, path, f"type={card.get('type')!r} 与 id 前缀不符")
        if card.get("track") not in TRACKS:
            err(errors, path, f"track={card.get('track')!r} 不是 A/B/C/D/O")
        if not str(card.get("title", "")).strip():
            err(errors, path, "title 不能为空")
        al = card.get("aliases")
        if not (isinstance(al, list) and al):
            err(errors, path, "aliases 至少 1 条")
        limit = 120 if typ == "concept" else 100
        n = text_len(card.get("summary", ""))
        if n == 0:
            err(errors, path, "summary 不能为空")
        elif n > limit:
            err(errors, path, f"summary 长度 {n} 超过 {limit}")
        q = str(card.get("question", "")).strip()
        if not q:
            err(errors, path, "question 不能为空")
        elif not q.endswith(("？", "?")):
            warnings.append(f"{path.name}: question 建议以问号结尾")
        if card.get("rights") != "rewritten":
            err(errors, path, "rights 必须是 rewritten")
        if card.get("status") not in ("draft", "reviewed"):
            err(errors, path, "status 必须是 draft/reviewed")
        check_sources(errors, path, card, typ == "concept")
        if typ == "concept":
            check_concept(errors, path, card)
        else:
            check_example(errors, path, card)

    # 交叉引用
    missing = {}
    for cid, path in cards.items():
        card = json.loads(path.read_text(encoding="utf-8"))
        refs = list(card.get("related", []) or []) + list(card.get("concept_refs", []) or [])
        for r in refs:
            if not isinstance(r, str) or not ID_RE.match(r):
                err(errors, path, f"交叉引用 {r!r} 不是合法 id")
                continue
            if r == cid:
                err(errors, path, "related 引用了自己")
            if r not in cards:
                missing.setdefault(r, []).append(path.name)
    if missing:
        msg = f"有 {len(missing)} 个被引用 id 尚未建卡（--allow-missing 时仅提示）"
        if allow_missing:
            warnings.append(msg + "：" + ", ".join(sorted(missing)[:12]) + (" ..." if len(missing) > 12 else ""))
        else:
            for r, users in sorted(missing.items()):
                errors.append(f"未解析引用 {r}（被 {', '.join(users)} 引用）")
    return errors, warnings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default="cards")
    ap.add_argument("--allow-missing", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    root = Path(args.root)
    errors, warnings = lint(root, args.allow_missing)
    cards = list((root / "concepts").glob("*.json")) + list((root / "examples").glob("*.json"))
    if args.json:
        print(json.dumps({"files": len(cards), "errors": errors, "warnings": warnings}, ensure_ascii=False, indent=2))
    else:
        for w in warnings:
            print("WARN", w)
        for e in errors:
            print("ERROR", e)
        print(f"\n{len(cards)} 张卡，{len(errors)} 个错误，{len(warnings)} 个警告")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
