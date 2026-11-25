# -*- coding: utf-8 -*-
"""对账参考文献：逐条比较原文 amsrefs 的 \\bib 条目与译本的 \\bibitem。

只做机械核对，不作判断。分两级：
  硬问题 —— 出版年、丛书/卷、书名、eprint 链接；这些缺了条目不可用。
  可选项 —— note 附注（题献、附录说明等）与「以出版社代替丛书」的写法；不影响可用性。

输出 work/bib_report.txt。
用法：cd 工程文件/scripts && python check_bib.py
"""
import re
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 工程文件/
ROOT = os.path.dirname(BASE)                                          # 工程根
SRC_ORIG = os.path.join(BASE, "work", "原文", "main.tex")
SRC_TRANS = os.path.join(ROOT, "源码", "chunks", "ch21.tex")
OUT = os.path.join(BASE, "work", "bib_report.txt")


def strip_braces(s):
    return s.replace("{", "").replace("}", "")


def parse_bib_blocks(text):
    """返回 [(key, {field: value})]。

    原文条目形如 \\bib{KEY}{type}{  field={..}, ... }，
    字段值可能跨行并含嵌套花括号，故手工配对。
    """
    entries = []
    i = 0
    n = len(text)
    head = re.compile(r"\\bib\{([^}]*)\}\{([^}]*)\}\{")
    while True:
        m = head.search(text, i)
        if not m:
            break
        key = m.group(1).strip()
        j = m.end()
        depth = 1
        start = j
        while j < n and depth > 0:
            c = text[j]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            j += 1
        body = text[start:j - 1]
        fields = {}
        k = 0
        fb = re.compile(r"([A-Za-z]+)\s*=\s*\{")
        while True:
            fm = fb.search(body, k)
            if not fm:
                break
            name = fm.group(1)
            p = fm.end()
            d = 1
            s = p
            while p < len(body) and d > 0:
                c = body[p]
                if c == "{":
                    d += 1
                elif c == "}":
                    d -= 1
                p += 1
            val = body[s:p - 1]
            fields.setdefault(name, val)
            k = p
        entries.append((key, fields))
        i = j
    return entries


def parse_bibitems(text):
    """返回 [(key, line)]。"""
    items = []
    for m in re.finditer(r"\\bibitem\{([^}]*)\}(.*)", text):
        items.append((m.group(1).strip(), m.group(2).strip()))
    return items


def norm(s):
    s = s.replace("\\'e", "e").replace("\\'E", "E").replace("{\\'e}", "e")
    s = s.replace("--", "-").replace("~", " ")
    s = re.sub(r"\\[A-Za-z]+", "", s)
    return strip_braces(s)


def book_field(f, name):
    """从 book={...} 里取子字段（series/title/volume/publisher）。"""
    book = f.get("book", "")
    m = re.search(name + r"\s*=\s*\{([^{}]*)\}", book)
    return m.group(1).strip() if m else ""


def main():
    with open(SRC_ORIG, encoding="utf-8") as f:
        orig_text = f.read()
    with open(SRC_TRANS, encoding="utf-8") as f:
        trans_text = f.read()

    orig = dict(parse_bib_blocks(orig_text))
    trans = parse_bibitems(trans_text)
    tmap = dict(trans)
    # Z14 在原文里写成 \bib{Z14}{article}{{ AUTHOR=...}}，多一层括号，字段解析会漏；
    # 只用 key 集合核对它，字段人工看。
    all_orig_keys = re.findall(r"\\bib\{([^}]*)\}", orig_text)

    hard = []
    soft = []

    for key, f in orig.items():
        if key not in tmap:
            continue
        line = tmap[key]
        nline = norm(line).lower()
        h, s = [], []

        date = strip_braces(f.get("date", "")).strip()
        for y in re.findall(r"\d{4}", date):
            if y not in nline:
                h.append("缺年 %s" % y)
                break

        series = strip_braces(f.get("series", "")).strip() or book_field(f, "series")
        volume = strip_braces(f.get("volume", "")).strip() or book_field(f, "volume")
        publisher = strip_braces(f.get("publisher", "")).strip() or book_field(f, "publisher")
        if series:
            head4 = norm(series)[:4].lower()
            if head4 and head4 not in nline:
                if publisher and norm(publisher).split(",")[0].lower() in nline:
                    s.append("以出版社代替丛书 %s" % series)
                else:
                    h.append("缺丛书 %s" % series)
        if volume and volume not in nline:
            h.append("缺卷 %s" % volume)

        title = book_field(f, "title")
        if title:
            nt = norm(title).strip().lower()
            if len(nt) > 6 and nt not in nline:
                h.append("缺书名 %s" % title[:40])

        eprint = strip_braces(f.get("eprint", "")).strip() or strip_braces(f.get("url", "")).strip()
        if eprint:
            host = norm(re.sub(r"^https?://", "", eprint)).rstrip("/").lower()
            if host and host not in nline:
                h.append("缺链接 %s" % eprint[:60])

        note = strip_braces(f.get("note", "")).strip()
        if note and norm(note)[:10].lower() not in nline:
            s.append("缺附注 %s" % note[:40])

        if h:
            hard.append((key, h, f, line))
        elif s:
            soft.append((key, s, f, line))

    lines = []
    lines.append("参考文献对账（原文 amsrefs \\bib  vs  译本 \\bibitem）")
    lines.append("原文条目 %d，译本条目 %d（字段可解析者 %d）"
                 % (len(all_orig_keys), len(trans), len(orig)))
    lines.append("")
    missing = [k for k in all_orig_keys if k not in tmap]
    extra = [k for k in tmap if k not in all_orig_keys]
    lines.append("原文有、译本无：%s" % (", ".join(missing) if missing else "无"))
    lines.append("译本有、原文无：%s" % (", ".join(extra) if extra else "无"))
    lines.append("")

    def dump(title, rows):
        lines.append(title)
        lines.append("-" * 78)
        for key, flags, f, line in rows:
            lines.append("")
            lines.append("[%s] %s" % (key, "；".join(flags)))
            lines.append("  原文：date=%s series=%s vol=%s pages=%s"
                         % (strip_braces(f.get("date", "")),
                            strip_braces(f.get("series", "")) or book_field(f, "series"),
                            strip_braces(f.get("volume", "")) or book_field(f, "volume"),
                            strip_braces(f.get("pages", ""))))
            lines.append("  译本：%s" % line[:200])
        if not rows:
            lines.append("  无")
        lines.append("")

    dump("一、硬问题（年月/丛书/卷/书名/链接）", hard)
    dump("二、可选项（附注题献、以出版社代替丛书；不影响可用性，酌情补）", soft)

    lines.append("-" * 78)
    lines.append("硬问题 %d 条，可选项 %d 条" % (len(hard), len(soft)))

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("written:", OUT)
    print("orig=%d trans=%d hard=%d soft=%d" % (len(orig), len(trans), len(hard), len(soft)))


if __name__ == "__main__":
    main()
