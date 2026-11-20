import os, re, json, glob

ROOT = r"C:\Users\admin\Downloads\_mirror_review"
CH = os.path.join(ROOT, "chapters")
OCR = os.path.join(ROOT, "ocr2")
UN = os.path.join(ROOT, "units")
os.makedirs(UN, exist_ok=True)

ORDER = ["preface", "notation", "chapter01", "chapter02", "chapter03", "chapter04",
         "chapter05", "chapter06", "chapter07", "chapter08", "chapter09",
         "chapter10", "chapter11", "chapter12", "appendixA", "appendixB"]

TARGET_PAGES = 3   # pages per unit
records = []
uid = 0

for name in ORDER:
    path = os.path.join(CH, name + ".tex")
    lines = open(path, encoding="utf-8").read().split("\n")
    # segments: (page, start_idx, end_idx)
    segs = []
    cur_page = None
    cur_start = 0
    for i, ln in enumerate(lines):
        m = re.search(r"\\SourcePage\{(\d+)\}", ln)
        if m:
            if cur_page is not None:
                segs.append((cur_page, cur_start, i - 1))
            cur_page = int(m.group(1))
            cur_start = i
    if cur_page is not None:
        segs.append((cur_page, cur_start, len(lines) - 1))
    else:
        segs.append((None, 0, len(lines) - 1))

    # merge segments into units of TARGET_PAGES pages
    buf = []
    def flush():
        global uid
        if not buf:
            return
        uid += 1
        pages = [s[0] for s in buf if s[0] is not None]
        p0, p1 = (min(pages), max(pages)) if pages else (None, None)
        startl = buf[0][1]
        endl = buf[-1][2]
        body = "\n".join(lines[startl:endl + 1])
        fn = f"u{uid:02d}"
        hdr = (f"% UNIT {fn}  file=chapters/{name}.tex  lines={startl+1}-{endl+1}  "
               f"pages={p0}-{p1}\n")
        open(os.path.join(UN, fn + ".tex"), "w", encoding="utf-8").write(hdr + body)
        en = []
        if p0 is not None:
            for p in range(p0, p1 + 1):
                fp = os.path.join(OCR, f"p{p:03d}.txt")
                if os.path.exists(fp):
                    en.append(f"\n===== ORIGINAL PDF PAGE {p} =====\n" +
                              open(fp, encoding="utf-8").read())
        open(os.path.join(UN, fn + ".en.txt"), "w", encoding="utf-8").write(
            f"UNIT {fn} ORIGINAL ENGLISH (OCR) pages {p0}-{p1}\n" + "".join(en))
        records.append(dict(unit=fn, file=f"chapters/{name}.tex", chapter=name,
                            start=startl + 1, end=endl + 1, p0=p0, p1=p1,
                            zbytes=len(body.encode("utf-8")),
                            ebytes=sum(len(x.encode("utf-8")) for x in en)))
        buf.clear()

    for s in segs:
        if s[0] is None:
            buf.append(s)
            continue
        if buf and buf[-1][0] is not None and s[0] - buf[0][0] >= TARGET_PAGES:
            flush()
        buf.append(s)
    flush()

json.dump(records, open(os.path.join(UN, "manifest.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
for r in records:
    print(r["unit"], r["chapter"], f"L{r['start']}-{r['end']}", f"p{r['p0']}-{r['p1']}",
          f"zh={r['zbytes']//1024}K en={r['ebytes']//1024}K")
print("units:", len(records))
