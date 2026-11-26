# -*- coding: utf-8 -*-
"""Independent re-verification of every page/locator edit (lead, second pass).

For each edit to sources[].pages / pdf_pages / theorems[0].source we recompute,
from the *unedited* anchors in the same card and the translation's srcpage
markers, which printed pages the anchor lines occupy, then compare with the page
numbers the fixed card claims.  Differences are printed with the TeX lines that
fall on the differing page, so that "background only" vs "statement itself" can
be judged without trusting the original auditor.

Also checks that every claimed page exists and that its page header equals the
printed page number (offset-0 convention).
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mech_checks as M

AUD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = M.REPO
PAGES = os.path.join(AUD, "tmp", "pages")
TEXMAP = M.tex_page_map()

def pdf_page(n):
    p = os.path.join(PAGES, "p%03d.txt" % n)
    return open(p, encoding="utf-8", errors="replace").read() if os.path.exists(p) else ""

def tex_lines(ch, a, b):
    fn = os.path.join(M.CH_DIR, "ch%02d.tex" % ch)
    lines = open(fn, encoding="utf-8").read().splitlines()
    return lines[a-1:b]

def anchor_pages(card):
    """page -> list of 'chNN:line' that live there, from all sources[].anchor"""
    out = {}
    for s in card.get("sources", []):
        refs, _hints = M.parse_anchor(s.get("anchor", ""))
        for ch, rngs in refs:
            for a, b in rngs:
                for ln in range(a, b + 1):
                    p = TEXMAP[ch].get(ln)
                    if p:
                        out.setdefault(p, []).append("ch%02d:%d" % (ch, ln))
    return out

def claimed_pages(field, after):
    if isinstance(after, list):
        return [int(x) for x in after]
    return [int(x) for x in re.findall(r"p\.?\s*(\d+)", str(after))]

def main():
    fx = json.load(open(os.path.join(AUD, "fix_log.json"), encoding="utf-8"))
    rows, diffs = [], []
    for f in fx["fixes"]:
        card = json.load(open(os.path.join(REPO, f["path"]), encoding="utf-8"))
        ap = anchor_pages(card)
        for e in f["edits"]:
            fld = e["field"]
            if not (fld.startswith("sources") or fld.startswith("theorems[0].source")):
                continue
            cp = claimed_pages(fld, e["after"])
            hdr_ok = all(re.search(r"(?m)^\s*%d\s" % p, pdf_page(p)) for p in cp)
            missing = sorted(set(ap) - set(cp))
            row = {"id": f["id"], "field": fld, "claimed": cp,
                   "anchor_pages": sorted(ap), "header_ok": hdr_ok,
                   "anchor_pages_not_claimed": missing}
            rows.append(row)
            if missing:
                detail = []
                for p in missing:
                    chl = ap[p][:6]
                    ref = chl[0].split(":")
                    ch, ln = int(ref[0][2:]), int(ref[1])
                    snippet = " / ".join(s.strip()[:70] for s in tex_lines(ch, ln, ln) if s.strip())
                    first = " ".join(pdf_page(p).splitlines()[:2])[:80]
                    detail.append({"page": p, "tex": chl[:4], "tex_first": snippet, "pdf_first": first})
                diffs.append({"id": f["id"], "field": fld, "claimed": cp, "missing": detail})
    print("locator edits:", len(rows), "| header mismatch:", [r for r in rows if not r["header_ok"]])
    print("edits whose claimed pages do not cover every anchor page:", len(diffs))
    for d in diffs:
        print("\n##", d["id"].split("/")[-1], d["field"], "claimed", d["claimed"])
        for m in d["missing"]:
            print("  page", m["page"], "lines", m["tex"], "| TEX:", m["tex_first"])
            print("            PDF:", m["pdf_first"])
    json.dump({"rows": rows, "diffs": diffs}, open(os.path.join(AUD, "tmp", "reverify_pages.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("\n->", os.path.join(AUD, "tmp", "reverify_pages.json"))

if __name__ == "__main__":
    main()
