import sys, re, io
sys.stdout.reconfigure(encoding="utf-8")
import pymupdf

PDF = r"<本地路径>"
OUT = r"<本地路径>"
TXT = r"<本地路径>"

doc = pymupdf.open(PDF)
lines = []
for pno in range(165, 170):
    page = doc[pno - 1]
    d = page.get_text("dict")
    for b in d["blocks"]:
        if b["type"] != 0:
            continue
        for l in b["lines"]:
            txt = "".join(s["text"] for s in l["spans"]).strip()
            if not txt:
                continue
            if re.fullmatch(r"\d+", txt):      # 页脚页码
                continue
            if txt == "Bibliography":
                continue
            lines.append(txt)

# 合并被行尾断开的条目
entries = []
cur = None
for ln in lines:
    m = re.match(r"^\[(\d+)\]\s*(.*)$", ln)
    if m:
        if cur:
            entries.append(cur)
        cur = [m.group(1), m.group(2)]
    elif cur:
        cur[1] += " " + ln
if cur:
    entries.append(cur)

def clean(s):
    s = re.sub(r"(\w)-\s+(\w)", r"\1\2", s)     # 连字符断行
    s = re.sub(r"-\s+(\w)", r"-\1", s)
    s = s.replace("¨a", "ä").replace("¨o", "ö").replace("¨u", "ü").replace("¨A", "Ä")
    s = s.replace("´e", "é").replace("´a", "á").replace("´o", "ó")
    s = s.replace("hepth/", "hep-th/")
    s = re.sub(r"\s+", " ", s).strip()
    return s

out_entries = [(n, clean(t)) for n, t in entries]
print("entries:", len(out_entries))
missing = [i for i in range(1, 65) if str(i) not in {n for n, _ in out_entries}]
print("missing numbers:", missing)

with io.open(TXT, "w", encoding="utf-8", newline="\n") as f:
    for n, t in out_entries:
        f.write(f"[{n}] {t}\n")

tex = ["% ============================================================",
       "%  参考文献（Bibliogrpahy, 原文印刷 pp.155–159）——保留英文原貌",
       "%  编号 [1]–[64] 与原文正文引用一致（手工编号，不用 \\cite）",
       "% ============================================================",
       "", "\\chapter*{参考文献}", ""]
for n, t in out_entries:
    t2 = t.replace("&", "\\&").replace("%", "\\%").replace("#", "\\#").replace("_", "\\_")
    tex.append(f"\\refitem{{{n}}}{{{t2}}}")
    tex.append("")
with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(tex) + "\n")
print("written", OUT)
