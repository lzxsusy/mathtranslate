# -*- coding: utf-8 -*-
"""glc1 资料卡校验 + 索引/核验表生成。

用法：
  python tools/lint_glc1.py            # 只校验
  python tools/lint_glc1.py --build    # 校验通过后重建 index.jsonl 与 verification.jsonl
"""
import json, os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, "cards")
TYPES = {"concept", "conjecture", "theorem", "definition", "example", "remark", "notation"}
TRACKS = set("ABCDEF")
STATUS = {"draft", "reviewed", "published"}
VSTATUS = {"source-only", "external-confirmed"}
BANNED = re.compile(
    r"\\(Bun|LS|LSr|LSB|LSBr|LG|LT|Lg|Dmod|Dmodh|IndCoh|Nilp|QCoh|Coh|Vect|Rep|Ran|Whit|Eis|Poinc|coeff|Mir|Sat|temp|coarse|restr|Gm|Ga|pt|CC|oblv|Idnv|Spec)\b"
)

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def check_card(c, ids):
    e, w = [], []
    def need(k, cond=True, msg=""):
        if not cond:
            e.append(f"缺字段/不合法: {k} {msg}")
    _id = c.get("id", "")
    need("id", isinstance(_id, str) and _id.startswith("glc1/") and _id.count("/") == 2, f"({_id!r})")
    need("type", c.get("type") in TYPES, repr(c.get("type")))
    need("track", c.get("track") in TRACKS, repr(c.get("track")))
    need("title", bool(c.get("title", "").strip()))
    need("aliases", isinstance(c.get("aliases"), list) and len(c["aliases"]) >= 1)
    s = c.get("summary", "")
    need("summary", bool(s.strip()))
    if len(s) > 120:
        (e if len(s) > 200 else w).append(f"summary 长度 {len(s)}（规范 ≤120）")
    q = c.get("question", "")
    need("question", q.strip().endswith(("？", "?")))
    d = c.get("definition") or {}
    need("definition.text", bool((d.get("text") or "").strip()))
    need("definition.notation", bool((d.get("notation") or "").strip()))
    need("key_points", isinstance(c.get("key_points"), list) and len(c["key_points"]) >= 3)
    need("formulas", isinstance(c.get("formulas"), list) and len(c["formulas"]) >= 1)
    need("pitfalls", isinstance(c.get("pitfalls"), list) and len(c["pitfalls"]) >= 1)
    rel = c.get("related") or []
    need("related", isinstance(rel, list) and len(rel) >= 2)
    for r in rel:
        if r not in ids:
            w.append(f"related 未解析: {r}")
    src = c.get("sources") or []
    need("sources", isinstance(src, list) and len(src) >= 1)
    for i, x in enumerate(src):
        for k in ("book", "section", "pages", "pdf_pages", "anchor"):
            if k not in x:
                e.append(f"sources[{i}] 缺 {k}")
        p, pp = x.get("pages"), x.get("pdf_pages")
        if isinstance(p, list) != isinstance(pp, list):
            e.append(f"sources[{i}] pages/pdf_pages 类型不一致")
        elif isinstance(p, list) and len(p) != len(pp):
            e.append(f"sources[{i}] pages/pdf_pages 长度不一致")
    need("rights", c.get("rights") == "rewritten", repr(c.get("rights")))
    st = c.get("status")
    need("status", st in STATUS, repr(st))
    for j, t in enumerate(c.get("theorems") or []):
        for k in ("name", "statement", "source"):
            if not (t.get(k) or "").strip():
                e.append(f"theorems[{j}] 缺 {k}")
        pr = t.get("proof") or {}
        ps = pr.get("status")
        if ps not in ("complete", "sketch"):
            e.append(f"theorems[{j}].proof.status 非法: {ps!r}")
        if ps == "sketch" and not (pr.get("gap_note") or "").strip():
            e.append(f"theorems[{j}] 是 sketch 但缺 gap_note")
        for k, sp in enumerate(pr.get("steps") or []):
            if not {"no", "text", "why"} <= set(sp):
                e.append(f"theorems[{j}].proof.steps[{k}] 缺 no/text/why")
    v = c.get("verification") or {}
    if st == "published" and not v:
        e.append("published 卡缺 verification")
    if v:
        if v.get("status") not in VSTATUS:
            e.append(f"verification.status 非法: {v.get('status')!r}")
        if st == "published" and v.get("status") == "source-only":
            e.append("published 卡不得是 source-only")
        if not (v.get("checked_on") or "").strip():
            e.append("verification 缺 checked_on")
        for k, ck in enumerate(v.get("checks") or []):
            if not {"source", "asserts", "verdict"} <= set(ck):
                e.append(f"verification.checks[{k}] 缺 source/asserts/verdict")
    blob = json.dumps(c, ensure_ascii=False)
    for m in set(BANNED.findall(blob)):
        e.append(f"出现译本宏 \\{m}（须展开成 \\operatorname 等）")
    if "$" not in blob:
        w.append("卡内没有行内公式")
    return e, w

def main():
    paths = sorted(glob.glob(os.path.join(CARDS, "**", "*.json"), recursive=True))
    cards = [load(p) for p in paths]
    ids = {c.get("id") for c in cards}
    errs, warns = 0, 0
    for p, c in zip(paths, cards):
        e, w = check_card(c, ids)
        name = os.path.basename(p)
        if e:
            errs += len(e)
            print(f"✗ {name}")
            for x in e:
                print("   ERROR:", x)
        if w:
            warns += len(w)
            print(f"· {name}")
            for x in w:
                print("   warn :", x)
        if not e and not w:
            print(f"✓ {name}")
    print(f"\n共 {len(cards)} 张；error {errs}；warn {warns}")
    if "--build" in sys.argv and errs == 0:
        with open(os.path.join(ROOT, "index.jsonl"), "w", encoding="utf-8", newline="\n") as f:
            for c in sorted(cards, key=lambda x: x["id"]):
                f.write(json.dumps({k: c[k] for k in ("id", "type", "track", "title", "summary")},
                                   ensure_ascii=False) + "\n")
        with open(os.path.join(ROOT, "verification.jsonl"), "w", encoding="utf-8", newline="\n") as f:
            for c in sorted(cards, key=lambda x: x["id"]):
                row = {"id": c["id"], "status": (c.get("verification") or {}).get("status", "source-only"),
                       "checked_on": (c.get("verification") or {}).get("checked_on", ""),
                       "checks": (c.get("verification") or {}).get("checks", [])}
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
        print("已重建 index.jsonl / verification.jsonl")
    return 1 if errs else 0

if __name__ == "__main__":
    sys.exit(main())
