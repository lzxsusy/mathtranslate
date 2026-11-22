import fitz, sys, re
p = sys.argv[1]; pg = int(sys.argv[2]); pat = sys.argv[3]
d = fitz.open(p)
page = d[pg-1]
for b in page.get_text("dict")["blocks"]:
    for l in b.get("lines", []):
        for s in l["spans"]:
            if re.search(pat, s["text"]):
                print(repr(s["text"][:60]), "|font=", s["font"], "|size=", round(s["size"],2), "|flags=", s["flags"])
