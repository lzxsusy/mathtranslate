#!/usr/bin/env python3
# R2 审核用探针：front matter 校验、卡/链接/引文清单
import hashlib, json, re, sys
from pathlib import Path

REPO = Path(r"C:\Users\admin\Desktop\数译发布\gitee_shuyi")
PAGE = REPO / "datasets/encyclopedia/pages/geometric-langlands.md"
text = PAGE.read_text(encoding="utf-8")
lines = text.splitlines()

# --- front matter ---
end = text.find("\n---", 3)
fm = text[3:end]
body = text[end+4:]
bstart = text[:end+4].count("\n")  # body line offset

def section(name):
    m = re.search(rf"^{name}:\s*\n((?:\s+-.*\n)+)", fm, re.M)
    return [x.strip()[2:].strip() for x in m.group(1).splitlines()] if m else []

entries = section("entries")
related = section("related")
parents = section("parents")
print("entries:", len(entries))
for e in entries:
    p = REPO / "datasets/encyclopedia/entries" / (e + ".json")
    print(("  OK  " if p.exists() else "  MISS"), e)

# compiled_from
cf = re.findall(r"- id:\s*(\S+)\s*\n\s*hash:\s*([0-9a-f]+)", fm)
print("compiled_from:", len(cf))
cards = {}
for f in (REPO / "datasets").glob("*/cards/**/*.json"):
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
    except Exception:
        continue
    if d.get("id"):
        cards[d["id"]] = f
bad = 0
for cid, h in cf:
    p = cards.get(cid)
    if not p:
        print("  UNKNOWN", cid); bad += 1; continue
    real = hashlib.sha256(p.read_bytes()).hexdigest()[:16]
    if real != h:
        print("  HASH", cid, h, "!=", real, p.name); bad += 1
print("compiled_from bad:", bad)

# related/parents
for name, lst in (("related", related), ("parents", parents)):
    for r in lst:
        rel = r.split("/", 1)
        p1 = REPO / "datasets/encyclopedia/pages" / (r[len("page/"):] + ".md") if r.startswith("page/") else None
        print(("  OK  " if p1 and p1.exists() else "  MISS"), name, r, "->", p1)

# --- body: card refs, citations, links with line numbers ---
print("\n== card refs by line ==")
for i, ln in enumerate(lines):
    for m in re.finditer(r"\{\{card:([^}]+)\}\}", ln):
        print(f"{i+1}\t{m.group(1)}")
print("\n== citations by line ==")
for i, ln in enumerate(lines):
    for m in re.finditer(r"〔([^〕]+)〕", ln):
        print(f"{i+1}\t{m.group(1)}")
print("\n== all ]( ) links ==")
for i, ln in enumerate(lines):
    for m in re.finditer(r"\]\(([^)]*)\)", ln):
        print(f"{i+1}\t{m.group(1)}")
