# -*- coding: utf-8 -*-
"""从 source/PROGRESS.md 抽出 81 处已有译注，生成 产出/汇总/existing-notes.tsv。

    python tools\\extract_existing_notes.py

列：chapter  n  loc_book  loc_zh  detail
- chapter：「ch01」…「ch09」；n 为章内序号
- loc_book：译注条目的加粗小标题（一般形如「原书 p. 4，式 (3) 及随后两段」）
- loc_zh：按章的固定偏移把原书页折成中译页（ch1 +6、ch2 +5、ch3 +4、ch4 +3、ch5 +1、ch6 −1、ch7 −5、ch8 −6、ch9 −9）；无页码时留空
"""
import os
import re
import io
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "source", "PROGRESS.md")
OUT = os.path.join(ROOT, "产出", "汇总", "existing-notes.tsv")

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

OFFSET = {1: 6, 2: 5, 3: 4, 4: 3, 5: 1, 6: -1, 7: -5, 8: -6, 9: -9}
SEC_RE = re.compile(r"^### 第\s*(\d)\s*篇.*?共\s*(\d+)\s*处译注")
ITEM_RE = re.compile(r"^\s*\d+\.\s+(.*)$")
BOOKPAGE_RE = re.compile(r"原书\s*p{1,2}\.\s*(\d+)")
BOLD_RE = re.compile(r"^\*\*(.+?)\*\*\s*[：:]\s*(.*)$")


def clean(s):
    return re.sub(r"\s+", " ", s.replace("\t", " ")).strip()


def main():
    rows = []
    ch = None
    for ln in open(SRC, encoding="utf-8").read().splitlines():
        m = SEC_RE.match(ln)
        if m:
            ch = int(m.group(1))
            continue
        if ln.startswith("### ") or ln.startswith("## "):
            ch = None
            continue
        if ch is None:
            continue
        m = ITEM_RE.match(ln)
        if not m:
            continue
        body = m.group(1).strip()
        b = BOLD_RE.match(body)
        headline, detail = (b.group(1).strip(), b.group(2).strip()) if b else ("", body)
        loc_zh = ""
        pm = BOOKPAGE_RE.search(headline) or BOOKPAGE_RE.search(detail)
        if pm:
            loc_zh = "中译 p.%d" % (int(pm.group(1)) + OFFSET[ch])
        rows.append([ch, headline, loc_zh, clean(detail)])

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    cnt = {}
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("chapter\tn\tloc_book\tloc_zh\tdetail\n")
        for ch, headline, loc_zh, detail in rows:
            cnt[ch] = cnt.get(ch, 0) + 1
            f.write("ch%02d\t%d\t%s\t%s\t%s\n" % (ch, cnt[ch], clean(headline), loc_zh, detail))

    print("共 %d 条 → %s" % (len(rows), OUT))
    print("分章：" + "  ".join("ch%02d=%d" % (k, v) for k, v in sorted(cnt.items())))
    print("PROGRESS 自报合计 81 → 抽出 %d %s" % (len(rows), "✓" if len(rows) == 81 else "✗ 请人工核对"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
