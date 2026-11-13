# -*- coding: utf-8 -*-
"""更新 catalog.json / CATALOG.md / gitee_shuyi README / MANIFEST.json / _build_summary.json。"""
import hashlib
import io
import json
import os

import pymupdf

SHU = r"<本地路径>"
GS = r"<本地路径>"
ARCH = r"<本地路径>"
PDF_NAME = "LHMS_局部同调镜像对称_中文译注本.pdf"
PDF = os.path.join(ARCH, "deliverable", PDF_NAME)
ID = "SY01-20"

# ---------- catalog.json ----------
cat_path = os.path.join(SHU, "catalog.json")
cat = json.load(io.open(cat_path, encoding="utf-8"))
doc = pymupdf.open(PDF)
first = " ".join(doc[0].get_text().split())[:400]
entry = {
    "id": ID,
    "theme": "01",
    "cn": "局部同调镜像对称",
    "orig": "Local Homological Mirror Symmetry",
    "author": "Si-Yang Liu; Kyungmin Rho",
    "pdf": PDF,
    "proj": ARCH,
    "kind": "译本",
    "tier": "A",
    "note": "arXiv:2611.07202v1，原文 56 页；中译注本 80 页，59 条译注 + 23 个概念框 + 8 处本节重点，附导读/术语表/页码对照表/译注索引/原文勘误表",
    "ok": True,
    "pages": doc.page_count,
    "first_text": first,
}
cat = [c for c in cat if c.get("id") != ID] + [entry]
json.dump(cat, io.open(cat_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---------- CATALOG.md ----------
md_path = os.path.join(SHU, "CATALOG.md")
md = io.open(md_path, encoding="utf-8").read()
rows = [l for l in md.splitlines() if l.startswith("| SY01-")]
last = rows[-1] if rows else None
newrow = "| %s | 局部同调镜像对称 | Local Homological Mirror Symmetry | %d | A |" % (ID, doc.page_count)
if last and last not in md:
    raise SystemExit("bad anchor")
if last:
    md = md.replace(last, last + "\n" + newrow, 1)
md = md.replace("（83 部 / 10,303 页）", "（84 部 / 10,383 页）")
md = md.replace("（19 部 / 1738 页）", "（20 部 / 1818 页）")
io.open(md_path, "w", encoding="utf-8").write(md)

# ---------- gitee README ----------
rp = os.path.join(GS, "00_README.md")
rd = io.open(rp, encoding="utf-8").read()
rd = rd.replace("从 83 部译本的 TeX 源码", "从 84 部译本的 TeX 源码")
rd = rd.replace("| `03_translations_meta/` | 83 部译本", "| `03_translations_meta/` | 84 部译本")
io.open(rp, "w", encoding="utf-8").write(rd)

# ---------- MANIFEST.json / _build_summary.json ----------
files = []
for root, dirs, fs in os.walk(GS):
    dirs[:] = [d for d in dirs if d != ".git"]
    for f in fs:
        p = os.path.join(root, f)
        rel = os.path.relpath(p, GS).replace(os.sep, "/")
        if rel in ("MANIFEST.json", "_build_summary.json"):
            continue
        b = open(p, "rb").read()
        files.append({"path": rel, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()[:16]})
files.sort(key=lambda x: x["path"])
total = sum(f["bytes"] for f in files)
json.dump({"files": len(files), "bytes": total, "items": files},
          io.open(os.path.join(GS, "MANIFEST.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def cnt(pref):
    return sum(1 for f in files if f["path"].startswith(pref))


summary = {
    "corpus_files": cnt("01_corpus_zh/"),
    "traj_files": cnt("02_trajectories/"),
    "translation_files": cnt("03_translations_meta/"),
    "playbook_files": cnt("04_playbook/"),
    "seminar_files": cnt("05_seminar_witten/"),
    "session_files": cnt("06_sessions_raw/"),
    "manifest_files": len(files),
    "total_bytes": total,
    "total_mb": round(total / 1048576.0, 1),
    "with_pdf": False,
}
json.dump(summary, io.open(os.path.join(GS, "_build_summary.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
print("catalog entries", len(cat), "pages", doc.page_count)
print(json.dumps(summary, ensure_ascii=True))
