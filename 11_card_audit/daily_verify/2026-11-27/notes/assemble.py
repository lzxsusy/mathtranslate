# -*- coding: utf-8 -*-
"""把 lead 手写记录与 subagent 返回的 JSON 数组合并成 records.jsonl。"""
import io, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
DATE = "2026-11-27"

def load_part(p):
    if not os.path.exists(p):
        return []
    txt = io.open(p, encoding="utf-8").read().strip()
    if not txt:
        return []
    if txt.startswith("["):
        return json.loads(txt)
    return [json.loads(l) for l in txt.splitlines() if l.strip()]

def normalize_aspect(a):
    """把子代理写的自由格式 aspect 归一化到 playbook 的 A/B/C 词表。"""
    s = str(a or "").strip().lower()
    for pre in ("a.", "b.", "c.", "a:", "b:", "c:"):
        if s.startswith(pre):
            s = s[len(pre):].strip()
    if "internal" in s or "related" in s:
        return "internal"
    if "consistency" in s and not s.startswith("math"):
        return "internal"
    if "math" in s:
        return "math"
    if any(k in s for k in ("source", "anchor", "quote", "page", "section", "citation")):
        return "sources"
    for k in ("definition", "theorem", "formula", "example"):
        if k in s:
            return k
    return "math"

def main():
    rows = []
    for name in ("head.jsonl", "partA.json", "partB.json", "partC.json", "partD.json"):
        rows += load_part(os.path.join(HERE, name))
    rows.sort(key=lambda r: r["n"])
    sample = json.load(io.open(os.path.join(HERE, "sample.json"), encoding="utf-8"))
    order = [c["id"] for c in sample["items"]]
    n = 1
    for r in rows:
        assert r["n"] == n, (r["n"], n)
        assert r["id"] == order[n - 1], (r["id"], order[n - 1])
        r["date"] = DATE
        r.setdefault("unverifiable_aspects", [])
        r.setdefault("notes", "")
        for c in r["checks"]:
            c["aspect"] = normalize_aspect(c.get("aspect", ""))
            c.setdefault("verdict", "ok")
            if not c.get("detail"):
                bits = [c.get("finding", "")]
                if c.get("page"):
                    bits.append("页：" + str(c["page"]))
                if c.get("source"):
                    bits.append("源：" + str(c["source"]))
                c["detail"] = "；".join(b for b in bits if b)
            c.pop("finding", None)
            c.pop("basis", None)
            c.pop("page", None)
            c.pop("source", None)
        n += 1
    assert len(rows) == 20, len(rows)
    out = os.path.join(HERE, "records.jsonl")
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("wrote", out, len(rows))

if __name__ == "__main__":
    main()
