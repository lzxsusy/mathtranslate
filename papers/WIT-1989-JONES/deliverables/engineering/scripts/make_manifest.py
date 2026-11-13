#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成本项目的 manifest.json（可复现性清单）。

用法：
    python make_manifest.py <project_root> [--out manifest.json]

输出字段：
  generated_at, witten_sha256, files: [{path, bytes, sha256, layer}]

版权分层（copyright layer）：
  L0 —— 本项目原创：读书笔记源码、研讨班记录、脚本、清单
  L1 —— 译本/转述，需随附原文出处与许可说明
  L2 —— 第三方全文（不随仓库分发；若出现，只在"引用"意义上）
"""
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# 目录 -> 版权层（默认 L0）
LAYERS = {
    "materials": "L0",
    "sessions": "L0",
    "seminar": "L0",
    "deliverables": "L0",
    "source": "L1",
    "translation": "L1",
}

SKIP_DIRS = {".git", "__pycache__", "build", ".pytest_cache", "node_modules"}
SKIP_SUFFIXES = {".aux", ".log", ".out", ".toc", ".synctex.gz", ".fdb_latexmk", ".fls", ".bbl", ".blg"}


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def layer_for(rel: Path) -> str:
    return LAYERS.get(rel.parts[0], "L0") if rel.parts else "L0"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--out", default=None)
    ap.add_argument("--witten-tex", default=None, help="witten1989/deliver/witten.tex 用于记录源文件哈希")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    out = Path(args.out) if args.out else root / "manifest.json"
    files = []
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(root)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if p.suffix in SKIP_SUFFIXES or p.name.endswith(".synctex.gz"):
            continue
        if p == out or p.name == "manifest.json":
            continue
        files.append({
            "path": rel.as_posix(),
            "bytes": p.stat().st_size,
            "sha256": sha256_of(p),
            "layer": layer_for(rel),
        })

    doc = {
        "project": "WIT-1989-JONES",
        "title_zh": "量子场论与 Jones 多项式：读书笔记",
        "source_paper": {
            "author": "Edward Witten",
            "journal": "Commun. Math. Phys.",
            "volume": 121,
            "year": 1989,
            "pages_printed": "351-399",
        },
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "file_count": len(files),
        "total_bytes": sum(f["bytes"] for f in files),
        "files": files,
    }
    if args.witten_tex and Path(args.witten_tex).exists():
        wt = Path(args.witten_tex)
        doc["witten_tex_sha256"] = sha256_of(wt)
        doc["witten_tex_bytes"] = wt.stat().st_size

    out.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"写出 {out}：{len(files)} 个文件，{doc['total_bytes']} 字节")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
