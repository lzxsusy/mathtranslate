# -*- coding: utf-8 -*-
"""ds_lint.py — 校验 datasets/ 下的 JSONL 记录。

用法：
    python tools/ds_lint.py [datasets 目录] [--quiet]

按目录判定类型（parallel/deepread/highlights/traces/kg/bench），
检查必填字段、长度上限、id 唯一、rights 规则、证据行号是否真实存在、
以及本机路径 / 口令 / 整章全文粘贴。退出码 0 表示通过。
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LIMITS = {
    "parallel": {"src_text": 600, "zh_text": 600, "why": 600, "total": 1400},
    "deepread": {"context": 800, "claim": 400, "why_this_matters": 600, "total": 6000},
    "highlights": {"what": 500, "why_hard": 600, "strategy": 600, "total": 3000},
    "kg": {"definition": 500, "total": 1500},
    "bench": {"question": 800, "reference_answer": 2000, "total": 4000},
    "math": {"statement": 4000, "context": 3000, "proof": 12000, "total": 24000},
}

MATH_KINDS = {"definition", "theorem", "claim", "construction", "example", "counterexample", "gap"}
MATH_VERIFY = {
    "kind": {"lean", "human", "none"},
    "status": {"checked", "sketch", "unchecked"},
}

REQUIRED = {
    "parallel": ["id", "pkg", "rights", "src_ref", "zh_ref", "src_text", "zh_text",
                 "why", "alignment", "status", "reviewed_by"],
    "deepread": ["id", "pkg", "rights", "claim", "claim_type", "context",
                 "proof_skeleton", "gap_filling", "why_this_matters", "prerequisites",
                 "pitfalls", "evidence", "difficulty", "confidence", "status", "reviewed_by"],
    "highlights": ["id", "pkg", "rights", "location", "kind", "what", "why_hard",
                   "strategy", "how_it_unlocks", "evidence", "status", "reviewed_by"],
    "traces": ["trace_id", "seq", "ts", "action", "observation", "outcome"],
    "kg": ["id", "pkg", "rights", "type", "evidence"],
    "bench": ["id", "pkg", "rights", "question", "kind", "rubric", "must_include",
              "difficulty", "evidence", "status", "reviewed_by"],
    "math": ["id", "kind", "lang", "statement", "context", "difficulty",
             "verification", "rights", "status", "reviewed_by"],
}

ID_RE = {
    "parallel": r"^[A-Z]{2}\d{2}-\d{2}\.p\d{4}$",
    "deepread": r"^[A-Z]{2}\d{2}-\d{2}\.d\d{3}$",
    "highlights": r"^[A-Z]{2}\d{2}-\d{2}\.h\d{3}$",
    "kg": r"^[A-Z]{2}\d{2}-\d{2}\.[a-z]\d{3,4}$",
    "bench": r"^[A-Z]{2}\d{2}-\d{2}\.b\d{3}$",
    "traces": r"^[A-Z]{2}\d{2}-\d{2}\.[a-z0-9-]+$",
    "math": r"^[A-Z]{2}\d{2}-\d{2}\.[a-z]\d{3}$",
}
PKG_RE = re.compile(r"^SY\d{2}-\d{2}$")
ARXIV_RE = re.compile(r"^(\d{4}\.\d{4,5}|[a-z-]+(\.[A-Z]{2})?/\d{7})(v\d+)?$")
BAD_PATTERNS = [
    (re.compile(r"[A-Za-z]:[\\/]+Users[\\/]+", re.I), "本机绝对路径"),
    (re.compile(r"Shuyi-Ocean-2026-9x7K|2918556466@qq\.com"), "敏感凭据"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "私钥"),
]


def die(msg, errors):
    errors.append(msg)


def check_file_ref(ref, where, errors, repo_root, label):
    fp = os.path.join(repo_root, ref.split(":")[0].replace("/", os.sep))
    if not os.path.isfile(fp):
        die("%s: %s 文件不存在 %s" % (where, label, ref), errors)
        return
    try:
        n = sum(1 for _ in io.open(fp, encoding="utf-8", errors="replace"))
    except OSError:
        return
    m = re.search(r":(\d+)(?:-(\d+))?$", ref)
    if m:
        hi = int(m.group(2) or m.group(1))
        if hi > n:
            die("%s: %s 行号越界 %s（文件共 %d 行）" % (where, label, ref, n), errors)


def check_ref(rec, path, errors, repo_root):
    src = rec.get("src_ref") or {}
    if not ARXIV_RE.match(str(src.get("arxiv", ""))):
        die("%s: src_ref.arxiv 不可解析：%s" % (path, src.get("arxiv")), errors)
    if src.get("pages") and (len(src["pages"]) != 2 or not all(isinstance(x, int) for x in src["pages"])):
        die("%s: src_ref.pages 须为两整数" % path, errors)
    zh = rec.get("zh_ref") or {}
    if not zh.get("file") or not isinstance(zh.get("line"), int):
        die("%s: zh_ref 缺 file/line" % path, errors)
    else:
        check_file_ref("%s:%d" % (zh["file"], zh["line"]), path, errors, repo_root, "zh_ref")


def check_evidence(rec, path, errors, repo_root):
    ev = rec.get("evidence")
    if not isinstance(ev, list) or not ev:
        die("%s: evidence 为空" % path, errors)
        return
    for item in ev:
        if not isinstance(item, dict) or "kind" not in item or "ref" not in item:
            die("%s: evidence 项缺 kind/ref" % path, errors)
            continue
        if item["kind"] == "file":
            check_file_ref(item["ref"], path, errors, repo_root, "evidence")


def lint_file(fp, kind, seen_ids, repo_root, errors, warnings):
    rel = os.path.relpath(fp, repo_root).replace("\\", "/")
    n = 0
    with io.open(fp, encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            n += 1
            try:
                rec = json.loads(line)
            except json.JSONDecodeError as e:
                die("%s:%d JSON 解析失败：%s" % (rel, lineno, e), errors)
                continue
            where = "%s:%d" % (rel, lineno)
            for key in REQUIRED[kind]:
                if key not in rec:
                    die("%s 缺字段 %s" % (where, key), errors)
            if kind != "traces":
                rid = rec.get("id", "")
                if not re.match(ID_RE[kind], rid):
                    die("%s id 不合规：%s" % (where, rid), errors)
                if rid in seen_ids:
                    die("%s id 重复：%s" % (where, rid), errors)
                seen_ids.add(rid)
                if kind != "traces" and kind != "math" and not PKG_RE.match(str(rec.get("pkg", ""))):
                    die("%s pkg 不合规：%s" % (where, rec.get("pkg")), errors)
                rights = str(rec.get("rights", ""))
                if not (rights == "self" or rights == "book" or rights.startswith("arxiv:")):
                    die("%s rights 非法：%s" % (where, rights), errors)
                if rights.startswith("arxiv:"):
                    aid = rights.split(":", 1)[1]
                    if not ARXIV_RE.match(aid):
                        die("%s rights 的 arXiv 号不可解析：%s" % (where, aid), errors)
                if rights == "book" and "/_internal/" not in rel.replace("\\", "/"):
                    die("%s rights=book 但不在 _internal/，不得发布" % where, errors)
                if kind == "parallel":
                    check_ref(rec, where, errors, repo_root)
                elif kind in ("deepread", "highlights", "bench"):
                    check_evidence(rec, where, errors, repo_root)
                elif kind == "math":
                    if rec.get("kind") not in MATH_KINDS:
                        die("%s math.kind 非法：%s" % (where, rec.get("kind")), errors)
                    if rec.get("lang") not in ("zh", "en"):
                        die("%s math.lang 非法：%s" % (where, rec.get("lang")), errors)
                    v = rec.get("verification")
                    if not isinstance(v, dict):
                        die("%s math.verification 不是对象" % where, errors)
                    else:
                        if v.get("kind") not in MATH_VERIFY["kind"]:
                            die("%s verification.kind 非法：%s" % (where, v.get("kind")), errors)
                        if v.get("status") not in MATH_VERIFY["status"]:
                            die("%s verification.status 非法：%s" % (where, v.get("status")), errors)
                        if v.get("kind") == "lean" and not v.get("artifact"):
                            die("%s verification.kind=lean 但缺 artifact" % where, errors)
            total = len(line)
            lim = LIMITS.get(kind, {}).get("total", 6000)
            if total > lim:
                die("%s 单条 %d 字，超过上限 %d（疑似整章粘贴）" % (where, total, lim), errors)
            for key, cap in LIMITS.get(kind, {}).items():
                if key == "total":
                    continue
                if key in rec and isinstance(rec[key], str) and len(rec[key]) > cap:
                    die("%s 字段 %s 超长 %d>%d" % (where, key, len(rec[key]), cap), errors)
            for pat, label in BAD_PATTERNS:
                if pat.search(line):
                    die("%s 含%s" % (where, label), errors)
    if kind == "traces":
        with io.open(fp, encoding="utf-8") as f:
            seqs = [json.loads(x)["seq"] for x in f if x.strip()]
        if seqs != sorted(seqs):
            die("%s seq 未单调递增" % rel, warnings)
    return n


def main():
    datasets = os.path.join(ROOT, "datasets")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    quiet = "--quiet" in sys.argv
    if args:
        datasets = os.path.abspath(args[0])
    kinds = {"parallel": "parallel", "deepread": "deepread", "highlights": "highlights",
             "traces": "traces", "kg": "kg", "bench": "bench", "math": "math"}
    errors, warnings = [], []
    seen_ids = set()
    total = 0
    for d, kind in kinds.items():
        base = os.path.join(datasets, d)
        if not os.path.isdir(base):
            continue
        for name in sorted(os.listdir(base)):
            if not name.endswith(".jsonl"):
                continue
            total += lint_file(os.path.join(base, name), kind, seen_ids, ROOT, errors, warnings)
    if not quiet:
        print("ds_lint: %d 条记录，%d 错误，%d 告警" % (total, len(errors), len(warnings)))
    for e in errors[:80]:
        print("ERROR", e)
    for w in warnings[:40]:
        print("WARN ", w)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
