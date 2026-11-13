#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""collect_transnotes.py — 把所有块里的 \\transnote{...} 汇总成一份 Markdown。

用法
----
    python src/tools/collect_transnotes.py [输出路径] [块号 ...]

- 省略「输出路径」时写到 ``work/译注汇总_auto.md``。
- 省略「块号」时扫描 ``src/chunks/`` 下的全部 ``cNN.tex``；
  只验证指定块时可写成 ``... collect_transnotes.py work/out.md c00 c01 c02``。

每条译注收集三样东西：

1. 译注正文：按花括号配平截取，支持嵌套花括号（不截断在第一个 ``}``）；
2. 该注之前最近的 ``% ===== 原书 p.N =====`` 页标记；
3. 该注之前最近的环境标题（``\\begin{definition}[...]`` 等，取环境名与可选标题）
   以及最近的 ``\\subsection`` / ``\\section`` / 伪标题（``\\medskip\\noindent\\textbf{...}``）。

输出条目格式：``- p.N ｜ 环境/小节 ｜ 译注全文``。
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CHUNK_DIR = os.path.join(ROOT, "src", "chunks")
DEFAULT_OUT = os.path.join(ROOT, "work", "译注汇总_auto.md")

# 定理类环境的中文名（与 preamble.tex 的 \newtheorem 一致）
ENV_ZH = {
    "theorem": "定理",
    "proposition": "命题",
    "lemma": "引理",
    "corollary": "推论",
    "definition": "定义",
    "example": "例",
    "claim": "断言",
    "remark": "注",
    "conjecture": "猜想",
    "problem": "问题",
}

# 页标记只认「% ===== 原书 p.N =====」这种带等号装饰的注释行，
# 免得把正文里的（原书 p.11）之类误当成页标记。
PAGE_RE = re.compile(r"^[ \t]*%[ \t]*=+[ \t]*原书[ \t]*p\.[ \t]*([^\s=]+)", re.M)
# 前置页（c00）没有正文页码，页标记写作「% ===== FRONT MATTER (PDF 4) =====」。
FRONT_RE = re.compile(r"^[ \t]*%[ \t]*=+[ \t]*FRONT MATTER[ \t]*\(PDF[ \t]*(\d+)\)", re.M)
HEAD_RE = re.compile(r"\\(section|subsection)\*?[ \t]*\{")
ENV_RE = re.compile(r"\\begin\{(" + "|".join(ENV_ZH) + r")\}")
PSEUDO_RE = re.compile(r"\\noindent[ \t]*\\textbf[ \t]*\{")
NOTE_RE = re.compile(r"\\transnote[ \t]*\{")
CHUNK_ARG_RE = re.compile(r"c\d{2}(?:\.tex)?")


def squash(text):
    """把一段 LaTeX 源文本压成单行（保留 $...$ 与命令本身）。"""
    return " ".join(text.split())


def tidy(text):
    """压成单行后，去掉全角标点两侧因换行留下的空格（纯排版整理）。"""
    text = squash(text)
    text = re.sub(r"(?<=[，。；：、！？）】」》])\s+", "", text)
    text = re.sub(r"\s+(?=[，。；：、！？）】」》])", "", text)
    text = re.sub(r"(?<=[\u4e00-\u9fff])\s+(?=[\u4e00-\u9fff])", "", text)
    return text


def line_head(text, idx):
    """返回 idx 所在行的行首下标。"""
    return text.rfind("\n", 0, idx) + 1


def in_comment(text, idx):
    """idx 是否落在以 % 开头的注释行内。"""
    prefix = text[line_head(text, idx):idx].lstrip()
    return prefix.startswith("%")


def match_brace(text, i):
    """text[i] 必须是 '{'，返回与之配对的 '}' 下标；失败返回 -1。"""
    depth = 0
    j = i
    while j < len(text):
        c = text[j]
        if c == "\\":          # 跳过转义字符，\{ \} 不计入配平
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return j
        j += 1
    return -1


def match_bracket(text, i):
    """text[i] 必须是 '['，返回与之配对的 ']' 下标；花括号内的方括号不计入配平。

    这样 ``[{... [CLS11][Proposition 4.3.3] ...}]`` 也能被完整取出。
    """
    depth_brace = 0
    depth_bracket = 0
    j = i
    while j < len(text):
        c = text[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth_brace += 1
        elif c == "}":
            depth_brace -= 1
        elif c == "[":
            depth_bracket += 1
        elif c == "]":
            depth_bracket -= 1
            if depth_bracket == 0:
                return j
        j += 1
    return -1


def strip_outer_braces(title):
    """去掉标题最外面一层花括号（源文件用 [{...}] 保护含方括号的标题）。"""
    if title.startswith("{") and title.endswith("}"):
        if match_brace(title, 0) == len(title) - 1:
            return title[1:-1].strip()
    return title


def heading_events(text):
    """收集所有小节/章标题与伪标题，返回按位置排序的 [(pos, 标题), ...]。"""
    events = []
    for m in HEAD_RE.finditer(text):
        if in_comment(text, m.start()):
            continue
        brace = text.find("{", m.start())
        end = match_brace(text, brace)
        if end < 0:
            continue
        events.append((m.start(), squash(text[brace + 1:end])))
    for m in PSEUDO_RE.finditer(text):
        if in_comment(text, m.start()):
            continue
        brace = text.find("{", m.start())
        end = match_brace(text, brace)
        if end < 0:
            continue
        events.append((m.start(), squash(text[brace + 1:end])))
    events.sort()
    return events


def env_events(text):
    """收集所有定理类环境的开始位置与「环境名（可选标题）」。"""
    events = []
    for m in ENV_RE.finditer(text):
        if in_comment(text, m.start()):
            continue
        name = ENV_ZH[m.group(1)]
        k = m.end()
        while k < len(text) and text[k] in " \t":
            k += 1
        title = ""
        if k < len(text) and text[k] == "[":
            end = match_bracket(text, k)
            if end > 0:
                title = strip_outer_braces(squash(text[k + 1:end]))
        events.append((m.start(), name + ("（%s）" % title if title else "")))
    return events


def last_before(events, pos):
    """取 events 中位置小于 pos 的最后一项；没有则返回空串。"""
    found = ""
    for at, label in events:
        if at >= pos:
            break
        found = label
    return found


def page_events(text):
    """收集页标记事件，返回按位置排序的 [(pos, 页码标签), ...]。

    正文页写作「原书 p.N」，前置页（c00）写作「前N」，N 是 PDF 页号。
    """
    events = [(m.start(), m.group(1)) for m in PAGE_RE.finditer(text)]
    events += [(m.start(), "前" + m.group(1)) for m in FRONT_RE.finditer(text)]
    events.sort()
    return events


def page_before(text, pos):
    """取 pos 之前最近的页标记页码；没有则返回空串。"""
    return last_before(page_events(text), pos)


def note_events(text):
    """按出现顺序返回 [(pos, 译注正文), ...]，正文按花括号配平截取。"""
    notes = []
    for m in NOTE_RE.finditer(text):
        if in_comment(text, m.start()):
            continue
        brace = m.end() - 1          # NOTE_RE 以 \{ 结尾，故这里就是 '{'
        end = match_brace(text, brace)
        if end < 0:
            sys.stderr.write("警告：%s 有一处 \\transnote 花括号不配平，已跳过\n"
                             % os.path.basename(text))
            continue
        notes.append((m.start(), tidy(text[brace + 1:end])))
    return notes


def chunk_files(names):
    """返回要扫描的文件列表；names 为空时取全部 cNN.tex。"""
    if not names:
        files = [f for f in os.listdir(CHUNK_DIR) if re.fullmatch(r"c\d{2}\.tex", f)]
    else:
        files = [n if n.endswith(".tex") else n + ".tex" for n in names]
    return sorted(files, key=lambda f: int(f[1:3]))


def main(argv):
    out_path = DEFAULT_OUT
    rest = list(argv)
    if rest and not CHUNK_ARG_RE.fullmatch(rest[0]):
        out_path = rest.pop(0)
    files = chunk_files(rest)

    blocks = []          # [(块名, [(页码, 定位, 正文), ...]), ...]
    total = 0
    for fname in files:
        path = os.path.join(CHUNK_DIR, fname)
        if not os.path.exists(path):
            sys.stderr.write("警告：找不到 %s，已跳过\n" % path)
            continue
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        heads = heading_events(text)
        envs = env_events(text)
        items = []
        for pos, body in note_events(text):
            page = page_before(text, pos) or "—"
            env = last_before(envs, pos)
            head = last_before(heads, pos)
            if env and head:
                where = env + " · " + head
            else:
                where = env or head or "—"
            items.append((page, where, body))
            total += 1
        blocks.append((fname[:-4], items))
        print("%s：%d 条" % (fname[:-4], len(items)))

    lines = [
        "# 译注汇总（自动生成）",
        "",
        "> 由 `src/tools/collect_transnotes.py` 生成，扫描 `src/chunks/c*.tex`。",
        "> 条目格式：`- p.N ｜ 环境/小节 ｜ 译注全文`。",
        "> `p.前N` 表示前置页（N 为 PDF 页号，c00 用 FRONT MATTER 标记）；`p.—` 表示该处无页标记。",
        "",
    ]
    for name, items in blocks:
        lines.append("## %s（%d 条）" % (name, len(items)))
        lines.append("")
        if not items:
            lines.append("（本块无译者注）")
            lines.append("")
            continue
        for page, where, body in items:
            lines.append("- p.%s ｜ %s ｜ %s" % (page, where, body))
        lines.append("")

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")

    print("合计：%d 条" % total)
    print("输出：%s" % out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
