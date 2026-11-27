# -*- coding: utf-8 -*-
"""校验 leanstmt 卡片：字段完整、枚举合法、Lean 声明可 grep、sorry 数与状态一致。

用法：
  python tools/lint_cards.py cards --strict
  python tools/lint_cards.py cards          # 只报 error，不把 style 问题算失败
"""
from __future__ import annotations

import argparse
import glob
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED = {
    "id": str, "type": str, "title": str, "track": str, "source": dict,
    "natural_language": dict, "lean": dict, "dependencies": list, "hypotheses": list,
    "scope": str, "backtranslation": dict, "verification": dict, "gaps": list,
    "notes": str, "rights": str, "status": str,
}
SOURCE_KEYS = {"paper", "arxiv", "section", "pages", "anchor"}
NL_KEYS = {"zh", "en"}
LEAN_KEYS = {"file", "name", "statement", "imports"}
BT_KEYS = {"zh", "method", "reviewer"}
VER_KEYS = {"status", "toolchain", "mathlib_rev", "checked_at", "checker", "sorry_count"}

SCOPES = {"discrete-core", "algebraic-core", "arithmetic-core", "gap"}
VSTATUS = {"certified", "gap"}
STATUS = {"draft", "dev"}
SORRY_RE = re.compile(r"\bsorry\b")
COMMENT_RE = re.compile(r"/-.*?-/|--[^\n]*", re.S)


def strip_comments(text: str) -> str:
    """粗略剥掉 Lean 注释（与 check_lean.py 同一策略，够用）。"""
    return COMMENT_RE.sub(" ", text)


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip())


def count_sorry_in(text: str) -> int:
    """统计真正的 sorry 占位（先剥注释，避免文档里提到 sorry 被误计）。"""
    return len(SORRY_RE.findall(strip_comments(text)))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("subdir", nargs="?", default="cards")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    paths = sorted(glob.glob(os.path.join(ROOT, args.subdir, "**", "*.json"), recursive=True))
    errors: list[str] = []
    warnings: list[str] = []
    ids = set()
    for p in paths:
        rel = os.path.relpath(p, ROOT).replace("\\", "/")
        try:
            card = json.load(io.open(p, encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            errors.append(f"{rel}: JSON 解析失败：{e}")
            continue
        for k, typ in REQUIRED.items():
            if k not in card:
                errors.append(f"{rel}: 缺字段 {k}")
            elif not isinstance(card[k], typ):
                errors.append(f"{rel}: 字段 {k} 类型应为 {typ.__name__}")
        cid = card.get("id", "")
        if not re.fullmatch(r"leanstmt/[a-z0-9]+-[a-z0-9]+", cid):
            errors.append(f"{rel}: id 不合规：{cid!r}")
        if cid in ids:
            errors.append(f"{rel}: id 重复：{cid}")
        ids.add(cid)
        if card.get("type") != "statement":
            errors.append(f"{rel}: type 必须为 statement")
        for key, keys in (("source", SOURCE_KEYS), ("natural_language", NL_KEYS),
                          ("lean", LEAN_KEYS), ("backtranslation", BT_KEYS),
                          ("verification", VER_KEYS)):
            for k in keys:
                if k not in card.get(key, {}):
                    errors.append(f"{rel}: 缺字段 {key}.{k}")
        src = card.get("source", {})
        pages = src.get("pages")
        if not (isinstance(pages, list) and len(pages) == 2 and all(isinstance(x, int) for x in pages)):
            errors.append(f"{rel}: source.pages 必须是 [印刷页, 印刷页] 两个整数")
        elif pages[0] > pages[1]:
            errors.append(f"{rel}: source.pages 区间反了：{pages}")
        arx = src.get("arxiv", "")
        if not (re.fullmatch(r"arXiv:\d{4}\.\d{4,5}v\d+", arx)
                or re.fullmatch(r"arXiv:[a-z-]+(\.[A-Za-z-]+)?/\d{7}v\d+", arx)
                or arx.startswith(("Nucl. Phys.", "Lecture notes"))):
            errors.append(f"{rel}: source.arxiv 形如 arXiv:1506.04293v3（非 arXiv 源以出版信息起头）")
        if len(card.get("title", "")) > 40:
            warnings.append(f"{rel}: title 超过 40 字")
        if len(card.get("natural_language", {}).get("en", "")) > 200:
            warnings.append(f"{rel}: natural_language.en 超过 200 字符")
        if card.get("scope") not in SCOPES:
            errors.append(f"{rel}: scope 非法：{card.get('scope')!r}")
        if card.get("rights") != "rewritten":
            errors.append(f"{rel}: rights 必须为 rewritten")
        if card.get("status") not in STATUS:
            errors.append(f"{rel}: status 非法：{card.get('status')!r}")
        ver = card.get("verification", {})
        if ver.get("status") not in VSTATUS:
            errors.append(f"{rel}: verification.status 非法：{ver.get('status')!r}")
        if ver.get("status") == "gap":
            if card.get("scope") != "gap":
                errors.append(f"{rel}: verification.status=gap 时 scope 必须为 gap")
            if not card.get("gaps"):
                errors.append(f"{rel}: gap 卡必须给出 gaps[] 至少 1 条")
            if ver.get("sorry_count", 0) < 1:
                errors.append(f"{rel}: gap 卡 sorry_count 应 ≥ 1")
        if ver.get("status") == "certified":
            if ver.get("sorry_count", 0) != 0:
                errors.append(f"{rel}: certified 卡 sorry_count 必须为 0")
            if card.get("gaps"):
                errors.append(f"{rel}: certified 卡 gaps 必须为空")
        if not re.fullmatch(r"[0-9a-f]{40}", ver.get("mathlib_rev", "")):
            errors.append(f"{rel}: verification.mathlib_rev 必须是 40 位 commit")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", ver.get("checked_at", "")):
            errors.append(f"{rel}: verification.checked_at 必须 YYYY-MM-DD")
        # Lean 声明可 grep
        lean = card.get("lean", {})
        fpath = os.path.join(ROOT, lean.get("file", ""))
        if not os.path.isfile(fpath):
            errors.append(f"{rel}: lean.file 不存在：{lean.get('file')}")
            continue
        text = io.open(fpath, encoding="utf-8").read()
        full = lean.get("name", "")
        short = full.rsplit(".", 1)[-1]
        m = re.search(r"(?:theorem|lemma|def)\s+" + re.escape(short) + r"\b", text)
        if not m:
            errors.append(f"{rel}: 在 {lean.get('file')} 里找不到声明 {short}")
        else:
            # 粗略截取声明头，做归一化比对
            head = text[m.start():]
            stmt = lean.get("statement", "")
            stmt_body = stmt.split(":=", 1)[0]
            head_body = head.split(":=", 1)[0]
            if norm(stmt_body) not in norm(head_body).replace("theorem " + short, "theorem " + short):
                warnings.append(f"{rel}: lean.statement 与源文件声明头不完全一致（请人工核）")
        # sorry 计数（按文件里该声明所在文件的总数作上界校验）
        n_sorry = count_sorry_in(text)
        if ver.get("status") == "certified" and n_sorry > 0 and "Gaps" not in lean.get("file", ""):
            errors.append(f"{rel}: certified 卡所在文件出现 sorry")
    print(f"cards={len(paths)} ids={len(ids)} errors={len(errors)} warnings={len(warnings)}")
    for e in errors:
        print(f"ERROR {e}")
    if args.strict:
        for w in warnings:
            print(f"WARN  {w}")
    else:
        print(f"（{len(warnings)} 条 style 警告，用 --strict 显示）")
    print("OK" if not errors else "FAIL")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
