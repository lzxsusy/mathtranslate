"""Extract every % [Tutor Note: ...] comment together with its yizhu box, and emit
REVIEW-NOTES.md (a reviewer index with sequential numbers, type, source page, text).

Usage: python tools/make_review_notes.py
"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ORDER = [
    "s00-front", "s01-intro", "s02a-abelian", "s02b-abelian2", "s03a-framing",
    "s03b-framing2", "s04a-hilbert", "s04b-hilbert2", "s05-wrapup",
]


def current_page(lines, idx):
    page = "题名页"
    for j in range(idx, -1, -1):
        m = re.search(r"%\s*====\s*原文\s*p\.(\d+)\s*====", lines[j])
        if m:
            page = m.group(1)
            break
    return page


def strip_tex(s):
    s = s.replace("\\%", "%")
    s = re.sub(r"\\(eqref|ref|cite)\{([^}]*)\}", r"⟨\2⟩", s)
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = s.replace("$", "")
    s = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{[^{}]*\})?", "", s)
    s = re.sub(r"[{}]", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def main():
    items = []
    for name in ORDER:
        path = os.path.join(ROOT, "sections", name + ".tex")
        if not os.path.exists(path):
            continue
        raw = open(path, encoding="utf-8").read()
        lines = raw.splitlines()
        for i, line in enumerate(lines):
            m = re.match(r"\s*%\s*\[Tutor Note:\s*([^\]]*)\]\s*(.*)$", line)
            if not m:
                continue
            typ, summary = m.group(1).strip(), m.group(2).strip()
            # find following yizhu env (within next 3 lines)
            body = ""
            for k in range(i, min(i + 6, len(lines))):
                if "\\begin{yizhu}" in lines[k]:
                    j = k
                    chunk = []
                    while j < len(lines) and "\\end{yizhu}" not in lines[j]:
                        chunk.append(lines[j])
                        j += 1
                    txt = "\n".join(chunk)
                    txt = txt.split("\\begin{yizhu}")[-1]
                    txt = re.sub(r"^\[[^\]]*\]", "", txt)
                    body = strip_tex(txt)
                    break
            items.append({"file": name, "line": i + 1, "type": typ,
                          "summary": summary, "body": body,
                          "page": current_page(lines, i)})

    out = ["# 译注与审校批注汇总（REVIEW-NOTES）", "",
           "本文件由 `tools/make_review_notes.py` 从 `sections/*.tex` 自动生成，"
           "编号与 PDF 中「译注 N」方框一致，可作快速索引。每条批注在源码中另有一行 "
           "`% [Tutor Note: 类型] 摘要` 注释，位置见下表「文件:行」。", "",
           f"共 {len(items)} 条。", "",
           "| # | 类型 | 位置 | 原文页 | 摘要 |", "|---|---|---|---|---|"]
    for n, it in enumerate(items, 1):
        it["n"] = n
        out.append(f"| {n} | {it['type']} | `{it['file']}.tex:{it['line']}` | p.{it['page']} | {it['summary']} |")
    out += ["", "---", ""]
    for it in items:
        out += [f"### 译注 {it['n']}（{it['type']}，原文 p.{it['page']}）", "",
                f"> {it['body']}", ""]
    path = os.path.join(ROOT, "REVIEW-NOTES.md")
    open(path, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"wrote {path}: {len(items)} notes")
    from collections import Counter
    print(Counter(it["type"] for it in items))


if __name__ == "__main__":
    main()
