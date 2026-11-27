# -*- coding: utf-8 -*-
"""校验 records.jsonl 的 card_says / evidence.quote 是否逐字可查（lead 自用）。"""
import io, json, re, sys, os, unicodedata

TXT = {
    "siebert": "siebert", "ggl08": "ggl08", "gtgl15": "gtgl15", "kw06": "kw06",
    "ggl09": "ggl09",
    "functoriality": "functoriality", "dmod": "dmod", "kshms": "kshms",
    "lbook04": "lbook", "gw06": "gw06", "glc": "glc", "benzvi_glc": "benzvi",
    "sy0238": "sy0238",
}
BASE = "C:/Users/admin/AppData/Local/Temp/cardverify/"

def norm(s):
    s = s or ""
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace("−", "-")
    s = re.sub(r"\s+", "", s)
    return s.lower()

def load_text(setname):
    if setname == "lbook04":
        parts = []
        for f in ("lb_ch3.txt", "lb_ch9.txt"):
            p = "C:/Users/admin/AppData/Local/Temp/vfyc/" + f
            if os.path.exists(p):
                parts.append(io.open(p, encoding="utf-8", errors="replace").read())
        return norm("\n".join(parts)) if parts else None
    f = TXT.get(setname)
    if not f:
        return None
    p = BASE + f + ".txt"
    if not os.path.exists(p):
        return None
    return norm(io.open(p, encoding="utf-8", errors="replace").read())

def main(path):
    rows = [json.loads(l) for l in io.open(path, encoding="utf-8") if l.strip()]
    cache = {}
    bad = 0
    for r in rows:
        card = norm(io.open(os.path.join(".", r["path"]), encoding="utf-8").read())
        t = cache.get(r["set"], False)
        if t is False:
            t = cache[r["set"]] = load_text(r["set"])
        for j, iss in enumerate(r.get("issues") or []):
            if norm(iss["card_says"]) not in card:
                bad += 1
                print("!! n=%d card_says NOT in card [%s]: %s" % (r["n"], iss["field"], iss["card_says"][:90]))
            for k, e in enumerate(iss["evidence"]):
                q = norm(e["quote"])
                if e.get("kind") == "internal":
                    if q not in card:
                        bad += 1
                        print("!! n=%d internal quote NOT in card: %r" % (r["n"], e["quote"][:90]))
                    continue
                if len(q) < 8:
                    print("?? n=%d quote too short: %r" % (r["n"], e["quote"]))
                    continue
                if t is None:
                    print("-- n=%d no local text (%s), quote skipped: %r" % (r["n"], r["set"], e["quote"][:60]))
                elif q not in t:
                    bad += 1
                    print("!! n=%d quote NOT found (%s) [%s]: %r" % (r["n"], r["set"], e["ref"], e["quote"][:110]))
        print("== n=%d %s | %s | issues=%d" % (r["n"], r["id"], r["verdict"], len(r.get("issues") or [])))
    print("BAD =", bad)

if __name__ == "__main__":
    main(sys.argv[1])
