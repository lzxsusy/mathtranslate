import urllib.request
cands = ["relative+Langlands+program", "relative+Langlands", "Nahm+pole", "opers", "oper", "Whittaker+function", "geometric+class+field+theory"]
for c in cands:
    url = "https://ncatlab.org/nlab/show/" + c
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        r = urllib.request.urlopen(req, timeout=25)
        body = r.read().decode("utf-8", "ignore")
        print(c, r.status, "missing-page" if "does not exist" in body or "Create this page" in body else "OK", len(body))
    except Exception as e:
        print(c, "ERR", type(e).__name__, e)
