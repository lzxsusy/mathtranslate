#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把研讨班记录与材料导出为静态 HTML（用 pandoc；不装 pandoc 时跳过）。

用法：
    python export_html.py <project_root> [--out deliverables/engineering/site]

产物：
    site/index.html          —— 目录页
    site/sessions/*.html     —— 每场 transcript / one_pager
    site/materials/*.html    —— 文献表、教材核查、语境史
    site/notes/*.html        —— 读书笔记各章（从 tex 转，失败则跳过）

pandoc 不可用时返回码 2（不算失败，build.ps1 会当作可选步骤）。
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

INDEX_TMPL = """<!doctype html>
<html lang="zh"><head><meta charset="utf-8">
<title>{title}</title>
<style>body{{font-family:system-ui,"Segoe UI",sans-serif;max-width:900px;margin:2rem auto;line-height:1.6;padding:0 1rem}}
code{{background:#f3f3f3;padding:.1em .3em;border-radius:3px}}
a{{color:#1565c0}} h1{{border-bottom:1px solid #ddd;padding-bottom:.3em}}</style>
</head><body>
<h1>{title}</h1>
<p>{desc}</p>
<ul>{items}</ul>
</body></html>
"""


def pandoc_available() -> bool:
    return shutil.which("pandoc") is not None


def convert(md: Path, out_dir: Path, root: Path) -> bool:
    rel = md.relative_to(root)
    dst = out_dir / rel.with_suffix(".html")
    dst.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["pandoc", str(md), "-f", "markdown+pipe_tables", "-t", "html5",
           "--standalone", "--metadata", "lang=zh-CN", "-o", str(dst)]
    try:
        subprocess.run(cmd, check=True, capture_output=True, timeout=120)
        return True
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        print(f"WARN 转换失败 {rel}: {e}")
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    if not pandoc_available():
        print("WARN 未找到 pandoc，跳过 HTML 导出")
        return 2

    root = Path(args.root).resolve()
    out_dir = Path(args.out) if args.out else root / "deliverables" / "engineering" / "site"
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    sources = []
    for pat in ("sessions/*/transcript.md", "sessions/*/one_pager.md",
                "sessions/*/reports/*.md", "sessions/*/challenges/*.md",
                "materials/*.md", "seminar/*.md"):
        sources.extend(sorted(root.glob(pat)))

    ok = [p for p in sources if convert(p, out_dir, root)]
    items = "\n".join(
        f'<li><a href="{p.relative_to(root).with_suffix(".html").as_posix()}">{p.relative_to(root).as_posix()}</a></li>'
        for p in ok
    )
    (out_dir / "index.html").write_text(
        INDEX_TMPL.format(title="WIT-1989-JONES 研讨班",
                          desc="Witten (1989) Chern–Simons 与 Jones 多项式：会话记录与材料",
                          items=items),
        encoding="utf-8",
    )
    print(f"导出 {len(ok)}/{len(sources)} 个文件到 {out_dir}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
