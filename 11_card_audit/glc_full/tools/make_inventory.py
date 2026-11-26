#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the 154-card inventory and the 8 audit groups for the glc full audit.

Groups are contiguous chapter blocks so each auditor reads one dense region of
the source (ch01..ch16), which keeps the notation and numbering consistent
within a group.  Group membership is frozen into groups/A<n>.txt.
"""
import glob
import hashlib
import json
import os
import re

ROOT = r"C:/Users/admin/Desktop/数译发布/gitee_shuyi"
AUD = os.path.join(ROOT, "datasets/_audit/glc_full_2026-11-26")

BLOCKS = [
    ("A1", ["01", "02"]),
    ("A2", ["03", "04"]),
    ("A3", ["05", "06"]),
    ("A4", ["07", "08"]),
    ("A5", ["09", "10"]),
    ("A6", ["11", "12"]),
    ("A7", ["13", "14"]),
    ("A8", ["15", "16"]),
]


def chap_of(card):
    blob = json.dumps(card, ensure_ascii=False)
    hits = re.findall(r"ch(\d\d)\.tex", blob)
    if not hits:
        return "??"
    first = (card.get("sources") or [{}])[0].get("anchor", "")
    m = re.search(r"ch(\d\d)\.tex", first)
    return m.group(1) if m else hits[0]


def main():
    paths = sorted(glob.glob(os.path.join(ROOT, "datasets/glc/cards/**/*.json"), recursive=True))
    rows = []
    for p in paths:
        raw = open(p, "rb").read()
        d = json.loads(raw.decode("utf-8"))
        srcs = d.get("sources") or [{}]
        rows.append({
            "id": d["id"],
            "type": d["type"],
            "track": d["track"],
            "status": d["status"],
            "title": d["title"],
            "chapter": chap_of(d),
            "anchor": srcs[0].get("anchor", ""),
            "pages": srcs[0].get("pages", []),
            "pdf_pages": srcs[0].get("pdf_pages", []),
            "section": srcs[0].get("section", ""),
            "n_sources": len(srcs),
            "path": os.path.relpath(p, ROOT).replace("\\", "/"),
            "sha256_12": hashlib.sha256(raw).hexdigest()[:12],
            "bytes": len(raw),
        })

    inv = {
        "set": "glc",
        "generated_at": "2026-11-26",
        "repo_root": ROOT,
        "source_pdf": "datasets/_audit/glc_full_2026-11-26/tmp/glc.pdf",
        "source_tex_project": "08_source_code/SY02-33_几何Langlands理论导论（陈麟）_中文译注校订版/源码",
        "page_convention": "PDF page = printed page (verified: p11 header '11' carries Conjecture 1.5.1)",
        "n_cards": len(rows),
        "cards": rows,
    }
    os.makedirs(os.path.join(AUD, "groups"), exist_ok=True)
    with open(os.path.join(AUD, "sample_inventory.json"), "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(inv, ensure_ascii=False, indent=2) + "\n")

    by_chap = {}
    for r in rows:
        by_chap.setdefault(r["chapter"], []).append(r)

    manifest = {}
    for name, chaps in BLOCKS:
        sel = []
        for c in chaps:
            sel.extend(by_chap.get(c, []))
        sel.sort(key=lambda r: (r["chapter"], r["path"]))
        manifest[name] = {
            "chapters": chaps,
            "n": len(sel),
            "paths": [r["path"] for r in sel],
            "ids": [r["id"] for r in sel],
        }
        with open(os.path.join(AUD, "groups", name + ".txt"), "w", encoding="utf-8", newline="\n") as f:
            for r in sel:
                f.write(r["path"] + "\n")

    with open(os.path.join(AUD, "groups", "manifest.json"), "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: v["n"] for k, v in manifest.items()}, ensure_ascii=False))
    print("total", sum(v["n"] for v in manifest.values()))


if __name__ == "__main__":
    main()
