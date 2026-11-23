# -*- coding: utf-8 -*-
"""把底本 PDF 抽成带上下标标记的纯文本，按讲分文件。

用法（在工程根目录下）：
    python 工程文件/tools/extract_src.py <source.pdf> <outdir>

输出：
    <outdir>/lecNN.txt           每讲一个文件，含 ===== PDF PAGE n ===== 分页标记
    <outdir>/../lecture_pages.tsv 讲号、起止页、页数
规则：
- 正文 10pt，上下标 7pt；按字号与基线相对位置还原 ^{} / _{}。
- 页眉（LECTURE n / 页码）丢弃。
- 脚注（页底 8pt，且以数字开头）保留为 [脚注 n] 段落。
"""
import sys, os, re
import pymupdf

LECTURES = [
    (1, "Introduction", 1, 7),
    (2, "Model categories", 8, 15),
    (3, "Simplicial sets", 16, 27),
    (4, "Quasi-categories", 28, 38),
    (5, "Quasi-category of quasi-categories", 39, 49),
    (6, "Limits and colimits: definition", 50, 57),
    (7, "Limits and colimits: functoriality", 58, 65),
    (8, "Limits and colimits: model categories", 66, 72),
    (9, "Limits and colimits: Kan extensions", 73, 79),
    (10, "Limits and colimits: commutativity", 80, 87),
    (11, "Yoneda lemma", 88, 96),
    (12, "Adjoint functors", 97, 103),
    (13, "Presentable infinity categories", 104, 109),
    (14, "Spectra", 110, 116),
    (15, "Stable infinity categories", 117, 123),
    (16, "t-structures", 124, 130),
    (17, "Derived infinity categories", 131, 138),
    (18, "Dold--Kan correspondence", 139, 145),
    (19, "Cartesian fibrations", 146, 152),
    (20, "Straightening and unstraightening", 153, 160),
    (21, "Infinity operads", 161, 168),
    (22, "Algebras", 169, 174),
    (23, "Modules I", 175, 179),
    (24, "Modules II", 180, 185),
    (25, "Lurie tensor products and smash products", 186, 192),
    (26, "Tensor products of infinity operads", 193, 198),
    (27, "E_infty rings", 199, 203),
]


def strip_noise(line):
    """合并被拆碎的上下标、清页眉、给项目符号补空格。"""
    line = re.sub(r"^LECTURE\s*\d+$", "", line).strip()
    line = re.sub(r"●(?=\S)", "● ", line)
    if not line:
        return line
    # 连续同类上下标成对合并：_{n}_{-}_{1} -> _{n-1}
    for mark in ("_", "^"):
        pat = re.compile(re.escape(mark) + r"\{([^{}]*)\}" + re.escape(mark) + r"\{([^{}]*)\}")
        prev = None
        while prev != line:
            prev = line
            line = pat.sub(lambda m: mark + "{" + m.group(1) + m.group(2) + "}", line)
    # 上下标紧跟字母时补空格：A_{∆}be -> A_{∆} be
    line = re.sub(r"([_^]\{[^{}]*\})([A-Za-z])", r"\1 \2", line)
    return line


def page_lines(page):
    """返回 (正文行列表, 脚注行列表)，每行是已带上下标标记的字符串。"""
    d = page.get_text("dict")
    h = page.rect.height
    body, foot = [], []
    for b in d["blocks"]:
        for ln in b.get("lines", []):
            spans = [s for s in ln["spans"] if s["text"]]
            if not any(s["text"].strip() for s in spans):
                continue
            y = ln["bbox"][1]
            # 页眉：顶部 5% 且字号 7
            if y < h * 0.06 and max(s["size"] for s in spans) < 8.5:
                continue
            # 纯页码行
            if len(spans) == 1 and re.fullmatch(r"\d+", spans[0]["text"].strip()):
                continue
            # 正文基线：取该行最大字号 span 的 origin.y
            big = max(spans, key=lambda s: s["size"])
            base = big["origin"][1]
            out = []
            for s in spans:
                t = s["text"]
                if not t.strip():
                    if out and not out[-1].endswith(" "):
                        out.append(" ")
                    continue
                sz = s["size"]
                oy = s["origin"][1]
                if sz <= 7.6 and big["size"] >= 9.4:
                    if oy < base - 1.4:
                        t = "^{" + t.strip() + "}"
                    elif oy > base + 1.2:
                        t = "_{" + t.strip() + "}"
                out.append(t)
            line = "".join(out)
            line = re.sub(r"\s+", " ", line).strip()
            line = strip_noise(line)
            if not line:
                continue
            first = spans[0]["text"].strip()
            is_foot = (y > h * 0.72 and max(s["size"] for s in spans) <= 8.3
                       and re.match(r"^[0-9]{1,2}[A-Z]?", first))
            if is_foot:
                n = re.match(r"^([0-9]{1,2})", first).group(1)
                rest = re.sub(r"^\s*[0-9]{1,2}\s*", "", line)
                foot.append(f"[脚注 {n}] {rest}")
            else:
                body.append(line)
    return body, foot


def main(pdf, outdir):
    os.makedirs(outdir, exist_ok=True)
    doc = pymupdf.open(pdf)
    assert len(doc) == 203, len(doc)
    rows = []
    for num, title, p0, p1 in LECTURES:
        chunks = [f"LECTURE {num}: {title}", f"底本 PDF 第 {p0}–{p1} 页", ""]
        for p in range(p0, p1 + 1):
            body, foot = page_lines(doc[p - 1])
            chunks.append(f"===== PDF PAGE {p} =====")
            chunks.extend(body)
            if foot:
                chunks.append("")
                chunks.extend(foot)
            chunks.append("")
        path = os.path.join(outdir, f"lec{num:02d}.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(chunks).rstrip() + "\n")
        rows.append((num, title, p0, p1, p1 - p0 + 1))
        print(f"lec{num:02d}.txt  pp.{p0}-{p1}  {p1-p0+1}p")
    with open(os.path.join(outdir, "..", "lecture_pages.tsv"), "w", encoding="utf-8") as f:
        f.write("lecture\ttitle\tpdf_start\tpdf_end\tpages\n")
        for r in rows:
            f.write("\t".join(map(str, r)) + "\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
