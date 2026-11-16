#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEM-GL2 门禁：schema / 长度 / 路径 / 配额 / 锚点格式 检查。

用法（在 work/ 目录下）：
  python tools/check_package.py --selftest
  python tools/check_package.py --corpus corpus --lectures lectures
  python tools/check_package.py --compliance --corpus corpus
退出码 0 = 全过；1 = 有 error。
"""
import argparse
import json
import re
import sys
from pathlib import Path

QUOTAS = {"reasoning": 3, "challenge": 1, "concept": 3, "crosswalk": 0,
          "misconception": 2, "qcard": 2, "meta": 1}
LECTURE_FILES = ["brief.md", "lecture.md", "challenges.md", "corpus.jsonl", "report.md"]
LECTURES = [f"U{i:02d}" for i in range(1, 9)]

ABS_PATH_RE = re.compile(
    r"(?:[A-Za-z]:[\\/](?:Users|admin|Desktop|dsh|Program|Windows|ProgramData|MiKTeX)"
    r"|/c/" r"Users/|/Users/[A-Za-z]|file:///)")
LOCATOR_RE = re.compile(r"^(A|B|C|D) p\.\d+( eq [0-9][0-9.]*)?$|^url:https?://\S+$")
QUOTE_MAX = 200
STR_MAX_DEFAULT = {"quote": 200, "claim": 120, "statement": 300, "definition_gist": 150,
                   "divergence": 200, "wrong_statement": 120, "why_wrong": 200,
                   "correct_version": 300, "trigger": 150, "question": 400,
                   "expected_answer": 300, "answer_short": 400, "objection": 400}

errors, warns = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warns.append(msg)


def load_schemas(schema_dir):
    out = {}
    for p in sorted(Path(schema_dir).glob("*.schema.json")):
        doc = json.loads(p.read_text(encoding="utf-8"))
        out[doc.get("x-type", p.stem.split(".")[0])] = doc
    if not out:
        err(f"找不到 schema：{schema_dir}")
    return out


def check_type(value, spec, path):
    t = spec.get("type")
    if t == "object":
        if not isinstance(value, dict):
            err(f"{path}: 应为 object")
            return
        for req in spec.get("required", []):
            if req not in value:
                err(f"{path}: 缺字段 {req}")
        for k, subspec in (spec.get("properties") or {}).items():
            if k in value:
                check_type(value[k], subspec, f"{path}.{k}")
    elif t == "array":
        if not isinstance(value, list):
            err(f"{path}: 应为 array")
            return
        if "minItems" in spec and len(value) < spec["minItems"]:
            err(f"{path}: 元素数 {len(value)} < {spec['minItems']}")
        for i, item in enumerate(value):
            check_type(item, spec.get("items", {}), f"{path}[{i}]")
    elif t == "string":
        if not isinstance(value, str):
            err(f"{path}: 应为 string")
            return
        if "enum" in spec and value not in spec["enum"]:
            err(f"{path}: 值 '{value}' 不在枚举 {spec['enum']}")
        if "const" in spec and value != spec["const"]:
            err(f"{path}: 应为常量 '{spec['const']}'")
        if "pattern" in spec and not re.fullmatch(spec["pattern"], value):
            err(f"{path}: 值 '{value}' 不匹配 {spec['pattern']}")
    elif t == "integer":
        if not isinstance(value, int) or isinstance(value, bool):
            err(f"{path}: 应为 integer")
        elif "minimum" in spec and value < spec["minimum"]:
            err(f"{path}: {value} < {spec['minimum']}")
        elif "maximum" in spec and value > spec["maximum"]:
            err(f"{path}: {value} > {spec['maximum']}")
    elif t == "boolean":
        if not isinstance(value, bool):
            err(f"{path}: 应为 boolean")


def check_lengths(rec, schema, where):
    mx = dict(STR_MAX_DEFAULT)
    mx.update(schema.get("x-max-lengths") or {})
    for k, lim in schema.get("x-max-lengths", {}).items():
        if isinstance(rec.get(k), str) and len(rec[k]) > lim:
            err(f"{where}: {k} 长度 {len(rec[k])} > {lim}")
    for k, v in rec.items():
        if k in (schema.get("x-max-lengths") or {}):
            continue
        if k in mx and isinstance(v, str) and len(v) > mx[k]:
            err(f"{where}: {k} 长度 {len(v)} > {mx[k]}")


def walk_quotes(obj, where):
    """所有 quote 字段 ≤200；evidence 的 locator 必须合规。"""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "quote" and isinstance(v, str) and len(v) > QUOTE_MAX:
                err(f"{where}: quote 长度 {len(v)} > {QUOTE_MAX}")
            if k == "locator" and isinstance(v, str):
                if not LOCATOR_RE.match(v):
                    err(f"{where}: locator '{v}' 格式不合规（应形如 'B p.148 eq 10.1' 或 'url:https://…'）")
            walk_quotes(v, where)
    elif isinstance(obj, list):
        for v in obj:
            walk_quotes(v, where)


def check_record(rec, schemas, where, seen_ids):
    t = rec.get("type")
    if t not in schemas:
        err(f"{where}: 未知 type={t!r}")
        return
    schema = schemas[t]
    check_type(rec, schema, where)
    check_lengths(rec, schema, where)
    walk_quotes(rec, where)
    lec = rec.get("lecture")
    if lec and str(lec) not in LECTURES:
        warn(f"{where}: lecture {lec} 不在 U01–U08（v2 单元）里")
    rnd = rec.get("round")
    if rnd is not None and lec and str(lec)[1:].isdigit() and int(str(lec)[1:]) != rnd:
        err(f"{where}: round={rnd} 与 lecture={lec} 不一致")
    rid = rec.get("id")
    if rid:
        if rid in seen_ids:
            err(f"{where}: id 重复 {rid}")
        seen_ids.add(rid)
    revs = rec.get("reviewers") or []
    if isinstance(revs, list):
        if len(set(revs)) < 2:
            err(f"{where}: reviewers 需 ≥2 个不同角色，实际 {revs}")
    s = json.dumps(rec, ensure_ascii=False)
    if ABS_PATH_RE.search(s):
        err(f"{where}: 含本机绝对路径")
    if t == "challenge":
        r = rec.get("response") or {}
        if r.get("verdict") == "revised" and not (r.get("diff") or {}).get("after"):
            err(f"{where}: revised 但缺 diff.after")
    if t == "reasoning":
        steps = rec.get("steps") or []
        if not any(s2.get("status") in ("dead_end", "unresolved") for s2 in steps):
            warn(f"{where}: 没有 dead_end/unresolved 步骤（本讲数据可能太'顺'）")


def records_from(paths):
    for p in paths:
        if not p.exists():
            err(f"文件不存在：{p}")
            continue
        with p.open(encoding="utf-8") as f:
            for ln, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    yield p, ln, json.loads(line)
                except json.JSONDecodeError as e:
                    err(f"{p}:{ln}: JSON 解析失败：{e}")


def find_jsonl(root):
    root = Path(root)
    if root.is_file():
        return [root]
    return sorted(root.rglob("*.jsonl"))


def summarize(records):
    from collections import Counter
    by_type = Counter(r.get("type") for r in records)
    by_lec = Counter(r.get("lecture") for r in records)
    print("  类型分布：" + "，".join(f"{k}={v}" for k, v in sorted(by_type.items())))
    print("  讲次分布：" + "，".join(f"{k}={v}" for k, v in sorted(by_lec.items())))
    return by_type, by_lec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schema", default=None)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--corpus", nargs="*")
    ap.add_argument("--lectures", nargs="*")
    ap.add_argument("--compliance", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    here = Path(__file__).resolve()
    schema_dir = Path(args.schema) if args.schema else here.parent.parent / "schema"
    schemas = load_schemas(schema_dir)
    if not schemas:
        print("FATAL: no schemas")
        return 1

    records = []
    if args.selftest:
        smp = here.parent.parent / "samples"
        files = sorted(Path(smp).glob("*.jsonl"))
        if not files:
            err(f"selftest: 找不到样例 {smp}")
        seen = set()
        for p, ln, rec in records_from(files):
            check_record(rec, schemas, f"{p.name}:{ln}", seen)
            records.append(rec)

    for c in args.corpus or []:
        seen = set()
        for p, ln, rec in records_from(find_jsonl(c)):
            check_record(rec, schemas, f"{p.name}:{ln}", seen)
            records.append(rec)

    for d in args.lectures or []:
        base = Path(d)
        # v2: 定稿每个单元一份平铺文件 U0X.md；兼容旧的 L*/ 目录结构
        flat = [u for u in LECTURES if (base / f"{u}.md").exists()]
        dirs = [p for p in base.glob("L*") if p.is_dir()]
        if not flat and not dirs:
            err(f"{base}: 找不到 U01.md…U08.md，也没有 L*/ 目录")
        for u in LECTURES:
            f = base / f"{u}.md"
            if f.exists():
                n = len(f.read_text(encoding="utf-8", errors="replace"))
                if n < 800:
                    err(f"{u}.md 只有 {n} 字符，定稿太薄（<800）")
        for lec in sorted(p.name for p in base.glob("L*") if p.is_dir()):
            miss = [f for f in LECTURE_FILES if not (base / lec / f).exists()]
            if miss:
                warn(f"{lec}: 缺文件 {miss}")
            cj = base / lec / "corpus.jsonl"
            if cj.exists():
                seen = set()
                cnt = {}
                for p, ln, rec in records_from([cj]):
                    check_record(rec, schemas, f"{lec}/corpus.jsonl:{ln}", seen)
                    records.append(rec)
                    cnt[rec.get("type")] = cnt.get(rec.get("type"), 0) + 1
                for t, need in QUOTAS.items():
                    if cnt.get(t, 0) < need:
                        err(f"{lec}: {t} 只有 {cnt.get(t, 0)} 条，配额 {need}")

    is_sample = any("samples" in str(c) for c in (args.corpus or []))
    if args.corpus and records and not is_sample:
        from collections import Counter, defaultdict
        cnt = defaultdict(Counter)
        for rec in records:
            lec = rec.get("lecture")
            if lec:
                cnt[lec][rec.get("type")] += 1
        for lec, c in sorted(cnt.items()):
            for t, need in QUOTAS.items():
                if need and c.get(t, 0) < need:
                    err(f"{lec}: {t} 只有 {c.get(t, 0)} 条，配额 {need}")

    if args.compliance:
        for i, rec in enumerate(records):
            s = json.dumps(rec, ensure_ascii=False)
            if ".pdf" in s.lower():
                err(f"compliance: 记录 {rec.get('id', i)} 引用了 pdf")
            if ABS_PATH_RE.search(s):
                err(f"compliance: 记录 {rec.get('id', i)} 含绝对路径")

    print(f"\n[schema] {schema_dir}  类型 {len(schemas)}")
    print(f"[records] {len(records)}")
    if records:
        summarize(records)
    for w in warns[:20]:
        print(f"  WARN  {w}")
    if len(warns) > 20:
        print(f"  ... 共 {len(warns)} 条 warning")
    if errors:
        print(f"\nFAILED: {len(errors)} error(s)")
        for e in errors[:30]:
            print(f"  ERROR {e}")
        if len(errors) > 30:
            print(f"  ... 共 {len(errors)} 条 error")
        return 1
    if args.selftest:
        print("\nSELFTEST OK")
    print(f"OK: 0 error（{len(records)} 条记录）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
