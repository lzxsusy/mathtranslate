# -*- coding: utf-8 -*-
"""Build glossary.tsv for SY02-08 v2.
Sources: GLOSSARY.md (frozen terms), original book text layer pNNN.txt (first-occurrence page),
01_corpus_zh/termbase.jsonl (conflict check).
"""
import json, os, re, unicodedata

WORK = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-08_圈群的Langlands对应"
ORIG = r"D:\C-Offload\Users\admin\Documents\deepseek-harness\default-workspace\frenkel-loop"
GLOSS = os.path.join(WORK, r"工程文件\work\GLOSSARY.md")
OUT = os.path.join(WORK, r"工程文件\work\glossary.tsv")
TERMBASE = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\01_corpus_zh\termbase.jsonl"


def norm_en(s):
    s = re.sub(r"\$[^$]*\$", " ", s)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if ch.isascii() and ch.isalnum())
    return s.lower()


def norm_zh(s):
    s = re.sub(r"\$[^$]*\$", "", s)
    s = re.sub(r"\\[a-zA-Z]+", "", s)
    s = s.replace("{", "").replace("}", "")
    return re.sub(r"[\s\-—–·,，。:：;；()（）\[\]【】]", "", s).lower()


rows = []
section = ""
for line in open(GLOSS, encoding="utf-8-sig"):
    line = line.rstrip("\n")
    m = re.match(r"^##\s+(.*)$", line)
    if m:
        section = m.group(1).strip()
        continue
    if not line.startswith("|"):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 2:
        continue
    if cells[0] in ("English", "---") or set(cells[0]) <= set("-: "):
        continue
    en, zh = cells[0], cells[1]
    note = cells[2] if len(cells) > 2 else ""
    if not en or not zh:
        continue
    # split compound entries when both sides split cleanly
    eparts = [x.strip() for x in en.split(" / ")]
    zparts = [x.strip() for x in zh.split(" / ")]
    if len(eparts) > 1 and len(eparts) == len(zparts):
        for e, z in zip(eparts, zparts):
            rows.append({"en": e, "zh": z, "note": note, "section": section})
    else:
        rows.append({"en": en, "zh": zh, "note": note, "section": section})

# dedupe identical (en, zh)
seen_pair = set()
uniq = []
for r in rows:
    k = (norm_en(r["en"]), norm_zh(r["zh"]))
    if k in seen_pair:
        continue
    seen_pair.add(k)
    uniq.append(r)
rows = uniq

# original pages normalized
pages = {}
for i in range(1, 407):
    p = os.path.join(ORIG, "text", "p%03d.txt" % i)
    try:
        pages[i] = norm_en(open(p, encoding="utf-8", errors="ignore").read())
    except FileNotFoundError:
        pass

# termbase index
tb = {}
for line in open(TERMBASE, encoding="utf-8"):
    try:
        d = json.loads(line)
    except Exception:
        continue
    if d.get("lang") != "en":
        continue
    k = norm_en(d.get("foreign", ""))
    if k:
        tb.setdefault(k, []).append(d)

out = []
missing = 0
for r in rows:
    key = norm_en(r["en"])
    first = None
    if len(key) >= 3:
        for pg in range(15, 402):
            if key in pages.get(pg, ""):
                first = pg
                break
    front = False
    if first is None:
        for pg in range(1, 15):
            if key and key in pages.get(pg, ""):
                first = pg
                front = True
                break
    if first is None:
        missing += 1
    printed = None
    for lo, hi, off in [(15, 139, -14), (140, 176, -13), (177, 231, -12),
                        (232, 260, -11), (261, 395, -10), (396, 401, -9)]:
        if first and lo <= first <= hi:
            printed = first + off
            break
    conflicts = []
    for d in tb.get(key, []):
        a, b = norm_zh(d.get("zh", "")), norm_zh(r["zh"])
        if a and b and a != b:
            conflicts.append("%s（%s）" % (d.get("zh"), d.get("pkg", "?")))
    flags = []
    if front:
        flags.append("首见在前置页")
    if missing:
        flags.append("未自动定位")
    if len(r["en"].split()) == 1 and len(key) <= 6:
        flags.append("常用词，页码待核")
    out.append([r["zh"], r["en"], str(first or ""), str(printed or ""),
                r["section"], r["note"], "; ".join(conflicts[:3]), "；".join(flags)])

# duplicate Chinese with different English
byzh = {}
for row in out:
    byzh.setdefault(norm_zh(row[0]), []).append(row[1])
for row in out:
    others = [e for e in byzh.get(norm_zh(row[0]), []) if e != row[1]]
    if others:
        row[7] = (row[7] + "；" if row[7] else "") + "同译名亦对应: " + ", ".join(others[:2])

out.sort(key=lambda x: (int(x[2]) if x[2] else 9999, x[1].lower()))
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("中文\t英文\t首次出现PDF页\t首次出现印刷页\t类别\t原表备注\t与termbase冲突\t标记\n")
    for row in out:
        f.write("\t".join(c.replace("\t", " ") for c in row) + "\n")

print("terms:", len(out), "no_page:", missing,
      "conflicts:", sum(1 for x in out if x[6]),
      "dup_zh:", sum(1 for x in out if "同译名" in x[7]))
for x in out:
    if x[6]:
        print("CONFLICT | " + " | ".join(x[:3] + [x[6]]))
