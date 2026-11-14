"""Build REVIEW-NOTES.md: index of every visible Tutor Note (yizhu box).

Reads the section fragments in assembly order, pairs each `% [Tutor Note: ...]`
comment with the following yizhu environment, numbers them exactly as the
compiled PDF does (global counter), and writes a Markdown index.
"""
import os
import re

ZH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SECT = os.path.join(ZH, "sections")
ORDER = ["s01-intro.tex", "s02-sca.tex", "s03a-tft.tex", "s03b-bmodel.tex",
         "s03c-example.tex", "s04a-ttstar.tex", "s04b-highergenus.tex"]

HEAD = re.compile(r"\\(section|subsection|subsubsection)\*?\{([^}]*)\}")
TN = re.compile(r"%\s*\[Tutor Note:\s*([^\]]*)\]\s*(.*)$")
YZ = re.compile(r"\\begin\{yizhu\}(?:\[([^\]]*)\])?(.*?)\\end\{yizhu\}", re.S)


def clean(s):
    s = re.sub(r"\\cite\{([^}]*)\}", lambda m: "[" + ", ".join(
        x.strip().replace("ref", "") for x in m.group(1).split(",")) + "]", s)
    s = re.sub(r"\\verb\|([^|]*)\|", r"`\1`", s)
    s = re.sub(r"\\textbf\{([^}]*)\}", r"**\1**", s)
    s = re.sub(r"\\emph\{([^}]*)\}", r"*\1*", s)
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s.strip()


def main():
    out = ["# 审校批注汇总（REVIEW-NOTES）", "",
           "本文件是译本中全部橙色「译注」方框的索引，编号与 PDF 编译结果的全局编号一致。",
           "权威内容在 `sections/*.tex` 源码中的 `yizhu` 环境；本文件便于快速浏览与检索。", ""]
    count = 0
    for fn in ORDER:
        path = os.path.join(SECT, fn)
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read()
        out.append(f"## {fn}")
        out.append("")
        cur_sec = ""
        pos = 0
        events = []
        for m in HEAD.finditer(text):
            events.append((m.start(), "head", m.group(2).strip()))
        for m in YZ.finditer(text):
            events.append((m.start(), "yizhu", m))
        for m in TN.finditer(text):
            events.append((m.start(), "tn", m.group(1).strip() + "｜" + m.group(2).strip()))
        events.sort(key=lambda e: e[0])
        pending_tn = ""
        for pos, kind, payload in events:
            if kind == "head":
                cur_sec = payload
                out.append(f"### {cur_sec}")
                out.append("")
            elif kind == "tn":
                pending_tn = payload
            else:
                m = payload
                count += 1
                typ = (m.group(1) or "").strip()
                body = clean(m.group(2))
                summary = pending_tn.split("｜", 1)[1] if "｜" in pending_tn else ""
                out.append(f"**译注 {count}**　`{typ}`　{summary}")
                out.append("")
                out.append(f"> {body.replace(chr(10), '  ' + chr(10) + '> ')}")
                out.append("")
                pending_tn = ""
    out.append(f"---")
    out.append(f"合计：{count} 条译注。")
    out.append("")
    p = os.path.join(ZH, "REVIEW-NOTES.md")
    open(p, "w", encoding="utf-8", newline="\n").write("\n".join(out))
    print("wrote", p, "notes:", count)


if __name__ == "__main__":
    main()
