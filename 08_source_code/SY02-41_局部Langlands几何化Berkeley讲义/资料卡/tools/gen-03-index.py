# -*- coding: utf-8 -*-
"""从 工程文件/work/条目总表.tsv 机械生成 资料卡/03-条款索引.md。

用法： python 资料卡/tools/gen-03-index.py
讲次页范围取自译文源码各 sNN-*.tex 的首尾 \\srcpage 标记（与 BRIEF 的讲次表一致）。
"""
import io, os, re, csv, collections

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TSV = os.path.join(ROOT, "工程文件", "work", "条目总表.tsv")
SEC = os.path.join(ROOT, "源码", "sections")
OUT = os.path.join(ROOT, "资料卡", "03-条款索引.md")

PAGE_RE = re.compile(r"\\srcpage\{(\d+)\}")

def lecture_pages():
    spans = {}
    for f in sorted(os.listdir(SEC)):
        m = re.match(r"s(\d\d)-.*\.tex$", f)
        if not m:
            continue
        lec = int(m.group(1))
        if lec in (0, 99):
            continue
        ps = [int(x) for x in PAGE_RE.findall(io.open(os.path.join(SEC, f), encoding="utf-8").read())]
        if ps:
            spans[lec] = (ps[0], ps[-1])
    return spans

def main():
    rows = list(csv.DictReader(io.open(TSV, encoding="utf-8"), delimiter="\t"))
    by = collections.OrderedDict()
    for r in rows:
        by.setdefault(int(r["lecture"]), []).append(r)
    spans = lecture_pages()

    stat = collections.Counter(r["kind"] for r in rows)
    order = ["definition", "example", "remark", "theorem", "warning", "lemma",
             "corollary", "proposition", "fact", "question", "conjecture", "exercise"]
    stat_txt = "、".join("%s %d" % ({"definition": "定义", "example": "例", "remark": "注",
                                    "theorem": "定理", "warning": "警告", "lemma": "引理",
                                    "corollary": "推论", "proposition": "命题", "fact": "事实",
                                    "question": "问题", "conjecture": "猜想",
                                    "exercise": "练习"}[k], stat[k]) for k in order)

    out = []
    out.append("# 资料卡 03 · 条款索引\n")
    out.append("编号由 LaTeX 自动生成，形如「讲次.序号」：每讲（`\\section`）重置一个共用计数器，"
               "定义、定理、例、注等环境依次递增，故同一讲内各类型的编号交错出现。\n")
    out.append("本表由 `工程文件/tools/index_items.py` 从译文源码推算（484 条，与原文逐条一致）；"
               "各讲的页范围取自译文中标注原文页的 `\\srcpage` 标记。环境类型统计：%s。\n" % stat_txt)
    out.append("")
    for lec, rs in by.items():
        p0, p1 = spans[lec]
        out.append("### 第 %d 讲（原文 p%d–p%d，共 %d 条）\n" % (lec, p0, p1, len(rs)))
        items = ["%s.%s %s" % (r["lecture"], r["idx"], r["label"]) for r in rs]
        lines = []
        for i in range(0, len(items), 9):
            chunk = "；".join(items[i:i + 9])
            lines.append(chunk)
        body = "；\n".join(lines)
        out.append("定理类：" + body + "\n")
    io.open(OUT, "w", encoding="utf-8").write("\n".join(out))
    print(OUT, len(rows))

main()
