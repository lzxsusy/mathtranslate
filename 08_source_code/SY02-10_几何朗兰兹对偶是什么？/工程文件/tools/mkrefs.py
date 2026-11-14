# -*- coding: utf-8 -*-
"""Parse the reference list out of full.txt and emit refs.tex (plain list, labels as in original)."""
import re

src = open(r"C:\Users\admin\Downloads\GL_work\full.txt", encoding="utf-8").read()
i = src.index("References\n[AB83]")
tail = src[i:]
tail = re.sub(r"===== PAGE \d+ =====", "", tail)
tail = re.sub(r"\nTHE GEOMETRIC LANGLANDS CORRESPONDENCE\n\d+\n", "\n", tail)
tail = re.sub(r"\nDAVID BEN-ZVI\n", "\n", tail)

parts = re.split(r"\n(?=\[[A-Za-z][^\]]{0,12}\])", tail)
entries = []
for p in parts:
    m = re.match(r"\[([^\]]+)\]\s*(.*)", p.strip(), re.S)
    if not m:
        continue
    key, body = m.group(1).strip(), m.group(2)
    body = re.sub(r"\s+", " ", body).strip()
    # repair PDF line-break artifacts
    body = body.replace("https: //", "https://").replace("http: //", "http://")
    body = body.replace("/ abs/", "/abs/").replace("/ current-events", "/current-events")
    body = body.replace("URL: ", "").replace("URL:", "")
    body = re.sub(r"([A-Za-z])- ([a-z])", r"\1\2", body)
    body = re.sub(r"(\d)\. (\d{4,5})", r"\1.\2", body)
    body = re.sub(r"\. (\d{4,5})\.", r".\1.", body)
    # mojibake for accents
    for a, b in [("´c", "ć"), ("´C", "Ć"), ("Z¨urich", "Zürich"), ("¨u", "ü"),
                 ("¨a", "ä"), ("¨o", "ö"), ("´e", "é"), ("´E", "É"), ("`E", "È"),
                 ("Mirkovi´c", "Mirković"), ("Mirkovi´ć", "Mirković")]:
        body = body.replace(a, b)
    body = body.replace("GLpnq", r"$GL_n(q)$")
    body = body.replace("g_{F_q}", r"$g_{\mathbb{F}_q}$")
    body = re.sub(r"\[([A-Za-z][^\]]{0,10})\]", r"[\1]", body)
    entries.append((key.replace("`", "+"), body))

def esc(s):
    urls = []
    def keep(m):
        urls.append(m.group(1))
        return "@@URL%d@@" % (len(urls) - 1)
    s = re.sub(r"(https?://[^\s,;]+)", keep, s)
    s = s.replace("&", r"\&").replace("%", r"\%").replace("#", r"\#")
    s = s.replace("_", r"\_")
    for idx, u in enumerate(urls):
        u2 = u.replace("_", r"\_").replace("%", r"\%").replace("#", r"\#")
        s = s.replace("@@URL%d@@" % idx, r"\url{%s}" % u2)
    return s

out = [r"\section*{参考文献}", r"\addcontentsline{toc}{section}{参考文献}",
       r"\begin{list}{}{\leftmargin=4.2em\labelwidth=3.8em\labelsep=0.4em\itemindent=0em\parsep=0.35em}"]
for k, b in entries:
    out.append(r"\item[{%s}] %s" % (k, esc(b)))
out.append(r"\end{list}")
open(r"C:\Users\admin\Downloads\GL_work\源码\chunks\refs.tex", "w", encoding="utf-8").write("\n".join(out))
print("entries:", len(entries))
