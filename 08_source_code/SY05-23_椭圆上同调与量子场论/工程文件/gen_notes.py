# -*- coding: utf-8 -*-
r"""gen_notes.py — 从 源码\ 各块抽取 % [Tutor Note: ...] 与 % [TODO-LEAD: ...]，
重新生成 工程文件\译注汇总.md（Lead 统稿用；保证条数与源码一致）。

用法（在 工程文件\ 目录下）： python gen_notes.py
"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "..", "源码")
OUT = os.path.join(ROOT, "译注汇总.md")

BLOCKS = [
    ("c01", "sec1.tex", "§1 引言（原文 p1–5，另含 p6 上半 §1.4–§1.5）"),
    ("c02", "sec2.tex", "§2 量子力学的同伦型（原文 p6–13）"),
    ("c03", "sec3.tex", "§3 超对称量子力学与 K 理论（原文 p13–19）"),
    ("c04", "sec4a.tex", "§4.1–§4.2（原文 p20–25）"),
    ("c05", "sec4b.tex", "§4.3–§4.5（原文 p25–30）"),
    ("c06", "refs.tex", "参考文献（原文 p30–34）"),
]


def extract(path):
    """返回 [(页码标记 or '', 批注正文)]，正文去掉 '% [Tutor Note:' 与结尾 ']'。"""
    try:
        with io.open(path, "r", encoding="utf-8") as f:
            lines = f.read().split("\n")
    except IOError:
        return []
    notes, page = [], ""
    i = 0
    while i < len(lines):
        ln = lines[i]
        m = re.match(r"^\s*%\s*\[原文 p\.(\d+)\]", ln)
        if m:
            page = m.group(1)
        m = re.match(r"^\s*%\s*\[(Tutor Note|TODO-LEAD):(.*)$", ln)
        if m:
            kind, acc = m.group(1), m.group(2)
            while acc.count("[") >= acc.count("]") or not acc.rstrip().endswith("]"):
                i += 1
                if i >= len(lines):
                    break
                acc += " " + lines[i].strip().lstrip("%").strip()
            acc = acc.rstrip()
            if acc.endswith("]"):
                acc = acc[:-1].rstrip()
            acc = re.sub(r"\s+", " ", acc).strip()
            notes.append((page, kind, acc))
        i += 1
    return notes


def main():
    rows, body = [], []
    total_tn = total_td = 0
    for code, fname, title in BLOCKS:
        notes = extract(os.path.join(SRC, fname))
        tn = [n for n in notes if n[1] == "Tutor Note"]
        td = [n for n in notes if n[1] == "TODO-LEAD"]
        total_tn += len(tn)
        total_td += len(td)
        rows.append("| %s | `%s` | %d | %d |" % (code, fname, len(tn), len(td)))
        body.append("## %s %s\n" % (code, title))
        if not tn and not td:
            body.append("（待补）\n")
            continue
        k = 0
        for page, kind, text in notes:
            if kind != "Tutor Note":
                continue
            k += 1
            where = ("（原文 p.%s）" % page) if page else ""
            body.append("%d. %s%s" % (k, where, text))
        body.append("")
        for page, kind, text in td:
            where = ("（原文 p.%s）" % page) if page else ""
            body.append("- **TODO-LEAD**%s：%s" % (where, text))
        body.append("")

    head = [
        "# 译注汇总 — SY05-23",
        "",
        "> 本文件由 `工程文件\\gen_notes.py` 从源码自动抽取，与源码中的 `% [Tutor Note: ...]` 批注逐条对应，条数一致。",
        "> 批注不进排版成品，只随源码交付；四类内容：可验证易错点、补省略论证、原文笔误、记号说明。",
        "",
        "| 块 | 文件 | Tutor Note | TODO-LEAD |",
        "|---|---|---|---|",
    ] + rows + [
        "| **合计** | | **%d** | **%d** |" % (total_tn, total_td),
        "",
        "---",
        "",
    ]
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(head + body).rstrip() + "\n")
    print("wrote %s | Tutor Note %d | TODO-LEAD %d" % (os.path.basename(OUT), total_tn, total_td))
    for r in rows:
        print("  ", r)


if __name__ == "__main__":
    main()
