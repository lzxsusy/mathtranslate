# -*- coding: utf-8 -*-
import io, os, re, json, hashlib, glob, sys
ROOT = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\datasets"
PAGE = os.path.join(ROOT, "encyclopedia", "pages", "geometric-langlands.md")
txt = io.open(PAGE, encoding="utf-8").read()
lines = txt.splitlines()
out = []
def p(*a):
    out.append(" ".join(str(x) for x in a))

WORK = {"bzg": "benzvi_glc", "glc": "glc", "glc1": "glc1",
        "raskin_glc": "raskin_glc", "sy0246": "sy0246"}

def cardpath(cid):
    pre, rest = cid.split("/", 1)
    w = WORK.get(pre)
    if not w: return None
    hits = glob.glob(os.path.join(ROOT, w, "cards", "**", "*" + os.path.basename(json.dumps(rest)) + "*"), recursive=True)
    # simpler: try concepts then conjectures then theorem
    fn = rest.split("/")[-1] + ".json"
    hits = glob.glob(os.path.join(ROOT, w, "cards", "**", fn), recursive=True)
    return hits[0] if hits else None

# --- front matter
fm = txt.split("---", 2)[1]
cf = re.findall(r"- id: (\S+)\n\s+hash: (\S+)", fm)
p("compiled_from count =", len(cf))
bad = []
for cid, h in cf:
    f = cardpath(cid)
    if not f:
        bad.append((cid, "NOFILE", h)); continue
    d = hashlib.sha256(io.open(f, "rb").read()).hexdigest()[:16]
    if d != h: bad.append((cid, d, h))
p("hash bad =", len(bad), bad[:5])

ents = re.findall(r"^  - (\S+/\S+)$", fm, re.M)
p("entries count =", len(ents))
for e in ents:
    f = os.path.join(ROOT, "encyclopedia", "entries", e + ".json")
    if not os.path.exists(f): p("  ENTRY MISSING", e)
rel = re.search(r"related:\n((?:  - .*\n)+)", fm).group(1)
parents = re.search(r"parents:\n((?:  - .*\n)+)", fm).group(1)
for key, block in (("related", rel), ("parents", parents)):
    for m in re.finditer(r"- (page/\S+)", block):
        f = os.path.join(ROOT, "encyclopedia", "pages", m.group(1) + ".md")
        p("  %s %s exists=%s" % (key, m.group(1), os.path.exists(f)))

# --- links
dead = []
for m in re.finditer(r"\]\((<[^>]+>|[^)\s]+)\)", txt):
    t = m.group(1).strip("<>")
    if t.startswith(("http", "#", "mailto")): continue
    t = t.split("#")[0]
    f = os.path.normpath(os.path.join(os.path.dirname(PAGE), t))
    if not os.path.exists(f): dead.append((lines[txt[:m.start()].count("\n")+1][:40], t))
p("links dead =", len(dead))
for d in dead: p("  DEAD", d)

# --- card refs
refs = re.findall(r"\{\{card:([^}]+)\}\}", txt)
uniq = sorted(set(refs))
p("card refs =", len(refs), "unique =", len(uniq))
for c in uniq:
    if not cardpath(c): p("  CARD NOFILE", c)

# --- appendix B
start = txt.index("## 附录 B"); end = txt.index("## 附录 C")
bsec = txt[start:end]
b0 = txt[:start].count("\n")
rows = re.findall(r"^\| `([^`]+)` \| ([^|]*)\| \[([^\]]+)\]\(([^)]+)\) \| ([^|]*)\| ([^|]*)\|\s*$", bsec, re.M)
p("appendix B rows =", len(rows))
body = txt[:start]
for cid, concept, label, path, sec, pg in rows:
    f = os.path.normpath(os.path.join(os.path.dirname(PAGE), path))
    ok = os.path.exists(f)
    inbody = ("{{card:%s}}" % cid) in body
    cardpg = ""
    if ok:
        try:
            j = json.load(io.open(f, encoding="utf-8"))
            s = (j.get("sources") or [{}])[0]
            cardpg = "pages=%s pdf=%s anchor=%s" % (s.get("pages"), s.get("pdf_pages"), (s.get("anchor") or "")[:40])
            kid = j.get("id")
            if kid != cid: cardpg += " IDMISMATCH:%s" % kid
        except Exception as ex:
            cardpg = "JSONERR %s" % ex
    p("B|%s|exists=%s|inbody=%s|col=%s|%s" % (cid, ok, inbody, pg.strip(), cardpg))
io.open(os.path.join(os.path.dirname(PAGE), "work/survey-v1/_r2_check2.txt"), "w", encoding="utf-8").write("\n".join(out))
print("done", len(out))
