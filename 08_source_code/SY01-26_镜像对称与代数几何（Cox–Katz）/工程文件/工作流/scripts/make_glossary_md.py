"""Generate 成品/SY01-26_术语表.md from glossary.tsv + first-occurrence scan."""
import io
import os
import re

WORK = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.join(
    r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code",
    "SY01-26_镜像对称与代数几何（Cox–Katz）",
)

ORDER = (["preface", "notation"] + ["chapter%02d" % i for i in range(1, 13)]
         + ["appendixA", "appendixB"])

CHAP_NAME = {"preface": "前言", "notation": "符号表",
             "appendixA": "附录 A", "appendixB": "附录 B"}


def chap_label(name):
    if name in CHAP_NAME:
        return CHAP_NAME[name]
    m = re.match(r"chapter(\d+)", name)
    return "第 %d 章" % int(m.group(1)) if m else name


rows = []
with io.open(os.path.join(WORK, "glossary.tsv"), encoding="utf-8") as f:
    header = f.readline()
    for line in f:
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 3:
            continue
        rows.append(parts)

# scan first occurrences
text_by_chap = {}
for name in ORDER:
    p = os.path.join(WORK, "chapters", name + ".tex")
    if not os.path.exists(p):
        continue
    lines = io.open(p, encoding="utf-8").read().split("\n")
    page = None
    entries = []
    for ln in lines:
        m = re.search(r"\\SourcePage\{(\d+)\}", ln)
        if m:
            page = int(m.group(1))
        entries.append((page, ln))
    text_by_chap[name] = entries

def first_occurrence(zh):
    if not zh:
        return None, ""
    cands = [zh, zh.replace("–", "--"), zh.replace("–", "-")]
    for name in ORDER:
        for page, ln in text_by_chap.get(name, []):
            if "\\SourcePage" in ln:
                continue
            if any(c and c in ln for c in cands):
                return page, chap_label(name)
    return None, ""

out = []
out.append("# SY01-26《镜像对称与代数几何》术语表")
out.append("")
out.append("- 底本：David A. Cox, Sheldon Katz, *Mirror Symmetry and Algebraic Geometry*, "
           "AMS Mathematical Surveys and Monographs 66, 1999。")
out.append("- 条目：%d 条。首现页为原书 PDF 物理页（= 译本 `\\SourcePage{N}`，印刷页 + 23）。" % len(rows))
out.append("- 裁决口径见同目录《术语对照与冲突.md》：monodromy 一律「单值性」，pencil「线性系」，"
           "「虚拟基本类」按仓库主流写法（原译「虚基本类」140 处已统一）。")
out.append("- 保留本书用法并在冲突表说明的：消失圈、代数叠、多胞形、自反多胞形。")
out.append("")
out.append("| # | 中文 | 英文 | 首现页 | 章 | 说明 |")
out.append("|---|---|---|---|---|---|")
for i, parts in enumerate(rows, 1):
    while len(parts) < 8:
        parts.append("")
    en, zh, mode, grade, sense, first, banned, note = parts[:8]
    if not first:
        pg, chap = first_occurrence(zh)
        first = "p%d" % pg if pg else ""
    else:
        chap = ""
        m = re.match(r"p?(\d+)", first)
        if m:
            pg = int(m.group(1))
            for name in ORDER:
                entries = text_by_chap.get(name, [])
                if entries and any(p == pg for p, _ in entries):
                    chap = chap_label(name)
                    break
    bits = []
    if sense:
        bits.append(sense)
    if banned:
        bits.append("禁用：" + banned)
    if note:
        bits.append(note)
    out.append("| %d | %s | %s | %s | %s | %s |" % (i, zh, en, first, chap, "；".join(bits)))

dst = os.path.join(PROJ, "成品", "SY01-26_术语表.md")
io.open(dst, "w", encoding="utf-8").write("\n".join(out) + "\n")
print("wrote", dst, len(rows), "terms")
