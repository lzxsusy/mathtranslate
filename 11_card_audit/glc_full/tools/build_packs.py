#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build one self-contained evidence pack per card.

Each pack holds, for a single card:
  1. the card JSON verbatim (the object under audit),
  2. the Chinese source-TeX slice named by sources[].anchor (with line numbers),
  3. the English original PDF page text for sources[].pages (+/- 1 page context),
  4. the titles of every `related` target (existence check).

Auditors read packs instead of hunting files; the packs are read-only evidence,
never a substitute for opening the PDF page when a formula looks off.
"""
import glob
import json
import os
import re

ROOT = r"C:/Users/admin/Desktop/数译发布/gitee_shuyi"
AUD = os.path.join(ROOT, "datasets/_audit/glc_full_2026-11-26")
PAGES = os.path.join(AUD, "tmp/pages")
TEXD = os.path.join(ROOT, "08_source_code/SY02-33_几何Langlands理论导论（陈麟）_中文译注校订版/源码/chapters")
OUT = os.path.join(AUD, "tmp/packs")


def slug(cid):
    return cid.replace("glc/concept/", "").replace("/", "__")


def tex_slice(anchor):
    m = re.search(r"(ch\d\d\.tex):(\d+)(?:-(\d+))?", anchor or "")
    if not m:
        return None
    f, a = m.group(1), int(m.group(2))
    b = int(m.group(3)) if m.group(3) else a
    path = os.path.join(TEXD, f)
    if not os.path.exists(path):
        return None
    lines = open(path, encoding="utf-8").read().split("\n")
    lo, hi = max(1, a - 3), min(len(lines), b + 3)
    body = "\n".join("%5d| %s" % (i, lines[i - 1]) for i in range(lo, hi + 1))
    return "%s:%d-%d  (context %d-%d of %d lines)\n%s" % (f, a, b, lo, hi, len(lines), body)


def page_text(n):
    p = os.path.join(PAGES, "p%03d.txt" % n)
    if not os.path.exists(p):
        return None
    return open(p, encoding="utf-8").read().rstrip()


def main():
    os.makedirs(OUT, exist_ok=True)
    cards = sorted(glob.glob(os.path.join(ROOT, "datasets/glc/cards/**/*.json"), recursive=True))
    by_id = {}
    for p in cards:
        d = json.loads(open(p, encoding="utf-8").read())
        by_id[d["id"]] = d

    index = []
    for p in cards:
        d = json.loads(open(p, encoding="utf-8").read())
        rel = os.path.relpath(p, ROOT).replace("\\", "/")
        parts = []
        parts.append("# EVIDENCE PACK — %s" % d["id"])
        parts.append("card path: `%s`\ntrack %s | status %s | %d bytes"
                     % (rel, d.get("track"), d.get("status"), os.path.getsize(p)))
        parts.append("## 1. CARD JSON (verbatim)\n\n```json\n%s\n```"
                     % json.dumps(d, ensure_ascii=False, indent=2))

        srcs = d.get("sources") or [{}]
        tex_blocks = []
        page_nums = []
        for s in srcs:
            t = tex_slice(s.get("anchor", ""))
            tex_blocks.append("anchor `%s` (%s)\n\n```\n%s\n```"
                              % (s.get("anchor", ""), s.get("section", ""), t or "ANCHOR DID NOT RESOLVE"))
            for k in (s.get("pages") or []):
                page_nums.append(int(k))
        parts.append("## 2. 中译源码锚点切片\n\n" + "\n\n".join(tex_blocks))

        want = set()
        for n in page_nums:
            want.update({n - 1, n, n + 1})
        blocks = []
        for n in sorted(want):
            t = page_text(n)
            if t:
                tag = "TARGET" if n in page_nums else "context"
                blocks.append("### PDF page %d (%s)\n\n```\n%s\n```" % (n, tag, t))
        parts.append("## 3. 英文原讲义 PDF 页文本（PDF 页 = 印刷页）\n\n" + "\n\n".join(blocks))

        rels = []
        for r in d.get("related") or []:
            tgt = by_id.get(r)
            rels.append("- `%s` → %s" % (r, ("EXISTS: " + tgt["title"]) if tgt else "**MISSING CARD**"))
        parts.append("## 4. related 目标\n\n" + ("\n".join(rels) if rels else "(none)"))

        # leak guard: no other card's verdict/audit text may sit in a pack
        text = "\n\n".join(parts) + "\n"
        fp = os.path.join(OUT, slug(d["id"]) + ".md")
        with open(fp, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        index.append({"id": d["id"], "path": rel, "pack": os.path.relpath(fp, ROOT).replace("\\", "/"),
                      "bytes": len(text.encode("utf-8")), "pdf_pages": sorted(set(page_nums))})

    with open(os.path.join(AUD, "tmp/packs/index.json"), "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(index, ensure_ascii=False, indent=2) + "\n")
    print("packs:", len(index), "total KB:", sum(i["bytes"] for i in index) // 1024,
          "max KB:", max(i["bytes"] for i in index) // 1024)


if __name__ == "__main__":
    main()
