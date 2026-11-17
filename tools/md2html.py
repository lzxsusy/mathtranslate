#!/usr/bin/env python3
"""md2html.py — 把本库的 Markdown 文档渲染成站点页面（无外部依赖）。

用法：
    python tools/md2html.py <input.md> <output.html> [--title "页面标题"]

支持：ATX 标题、段落、无序/有序列表、表格（反引号内的 | 不分列）、
      围栏代码、引用、分隔线、行内 code / 粗体 / 斜体 / 删除线 / 链接。

设计原则：只为本库文档服务，宁可少支持，不要静默渲染错。
任何无法识别的块都退化成段落，绝不吞掉内容。
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path


# ---------- 行内 ----------

def inline(s: str) -> str:
    """先保护 code span，再转义 HTML，最后套用强调/链接。"""
    codes: list[str] = []

    def _stash(m: re.Match) -> str:
        codes.append(m.group(1))
        return f"\x00{len(codes) - 1}\x00"

    s = re.sub(r"`([^`]+)`", _stash, s)
    s = html.escape(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"~~([^~]+)~~", r"<del>\1</del>", s)

    def _restore(m: re.Match) -> str:
        return "<code>" + html.escape(codes[int(m.group(1))], quote=False) + "</code>"

    return re.sub(r"\x00(\d+)\x00", _restore, s)


# ---------- 表格 ----------

def split_cells(line: str) -> list[str]:
    """按 | 切列；反引号内的 | 不算分隔符。去掉首尾空单元。"""
    cells: list[str] = []
    buf: list[str] = []
    in_code = False
    for ch in line:
        if ch == "`":
            in_code = not in_code
            buf.append(ch)
        elif ch == "|" and not in_code:
            cells.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    cells.append("".join(buf))
    if cells and not cells[0].strip():
        cells = cells[1:]
    if cells and not cells[-1].strip():
        cells = cells[:-1]
    return [c.strip() for c in cells]


SEP_RE = re.compile(r"^\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
LIST_RE = re.compile(r"^(\s*)([-*+]|\d+\.)\s+(.*)$")
HEAD_RE = re.compile(r"^(#{1,6})\s+(.*)$")
HR_RE = re.compile(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$")


def is_block_start(line: str) -> bool:
    t = line.strip()
    return bool(
        not t
        or HEAD_RE.match(line)
        or HR_RE.match(line)
        or t.startswith("```")
        or t.startswith(">")
        or t.startswith("|")
        or LIST_RE.match(line)
    )


# ---------- 块 ----------

def convert(md: str) -> str:
    lines = md.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    i, n = 0, len(lines)

    while i < n:
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        # 围栏代码
        if line.strip().startswith("```"):
            lang = line.strip()[3:].strip()
            i += 1
            buf: list[str] = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            cls = f' class="language-{html.escape(lang)}"' if lang else ""
            out.append(f"<pre><code{cls}>" + html.escape("\n".join(buf)) + "</code></pre>")
            continue

        # 标题
        m = HEAD_RE.match(line)
        if m:
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>" + inline(m.group(2)) + f"</h{lvl}>")
            i += 1
            continue

        # 分隔线
        if HR_RE.match(line):
            out.append("<hr>")
            i += 1
            continue

        # 引用
        if line.lstrip().startswith(">"):
            buf = []
            while i < n and lines[i].lstrip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            paras: list[str] = []
            cur: list[str] = []
            for b in buf:
                if not b.strip():
                    if cur:
                        paras.append("<br>".join(cur))
                        cur = []
                else:
                    cur.append(inline(b))
            if cur:
                paras.append("<br>".join(cur))
            out.append("<blockquote>" + "".join(f"<p>{p}</p>" for p in paras) + "</blockquote>")
            continue

        # 表格
        if line.strip().startswith("|") and i + 1 < n and SEP_RE.match(lines[i + 1].strip()):
            header = split_cells(line)
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(split_cells(lines[i]))
                i += 1
            t = ["<table><thead><tr>"]
            t += [f"<th>{inline(c)}</th>" for c in header]
            t.append("</tr></thead><tbody>")
            for r in rows:
                t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue

        # 列表
        m = LIST_RE.match(line)
        if m:
            ordered = m.group(2).rstrip(".").isdigit()
            tag = "ol" if ordered else "ul"
            items: list[str] = []
            while i < n:
                mm = LIST_RE.match(lines[i])
                if not mm:
                    break
                items.append(inline(mm.group(3)))
                i += 1
            out.append(f"<{tag}>" + "".join(f"<li>{x}</li>" for x in items) + f"</{tag}>")
            continue

        # 段落：吃到下一个块起点
        buf = []
        while i < n and not (buf and is_block_start(lines[i])):
            buf.append(inline(lines[i]))
            i += 1
        out.append("<p>" + "<br>".join(buf) + "</p>")

    return "\n".join(out)


PAGE = """<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · 数译</title><link rel="stylesheet" href="./assets/style.css"></head>
<body>
<header class="top"><div class="wrap"><div class="brand">
  <div class="logo">译</div>
  <div><h1>{title}</h1><div class="sub">MEMORANDUM-01 · 强制前置读本 · 数译</div></div>
  <nav class="meta"><a href="./index.html">← 返回文献库</a><br>2026-11-18</nav>
</div></div></header>
<main class="wrap doc">
{body}
</main>
<footer><div class="wrap">数译 · 中文数学译注文献库 &nbsp;|&nbsp; 本页为内部方法论文档，可自由转载署名。</div></footer>
</body></html>
"""


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__)
        return 2
    src, dst = Path(argv[1]), Path(argv[2])
    title = "论证精读与语料生产的科学规程"
    if "--title" in argv:
        title = argv[argv.index("--title") + 1]
    body = convert(src.read_text(encoding="utf-8"))
    dst.write_text(PAGE.format(title=html.escape(title), body=body), encoding="utf-8")
    print(f"wrote {dst} ({dst.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
