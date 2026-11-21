# -*- coding: utf-8 -*-
"""GMN3 条款索引生成器：从成品 PDF 机械抽取全部编号公式的式号与页码。

规则（与 02_疑点清单.md 的实测一致）：
* 页面上的公式编号右对齐，行末形如 (3.12) 或 (F.4)；
* 只保留右边缘 x1 >= 515pt 的行（版心右界 521.6pt），左对齐的引用文本会被排除；
* 行首若含 CJK（正文里写「式 (3.35)」之类）也排除；
* 同一 (x.y) 只记一次（取最先出现者，正常情况下也只有一次）。

输出：
  eq_index.tsv   num<TAB>page        逐式一行，按 (节, 编号) 排序
  eq_table.md    按节/页分组的 markdown 片段，供 03-条款索引.md 拼接
并打印逐节统计与缺号检查，供卡片正文引用。

依赖：PyMuPDF。用法：
  python build_index.py            # 默认用本工程的成品 PDF
  python build_index.py --pdf <path>
"""
import argparse
import os
import re
import sys

try:
    import fitz  # PyMuPDF
except ImportError:  # pragma: no cover
    sys.exit("需要 PyMuPDF：pip install pymupdf")

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, "..", ".."))
DEFAULT_PDF = os.path.join(PROJ, "成品", "GMN3_带框BPS态_v1.0.pdf")

RIGHT_EDGE = 515.0          # pt，实测式号 x1≈521.6，左对齐文本远小于此
LINE_RE = re.compile(r"\(([0-9]{1,2}|[A-G])\.([0-9]{1,2})\)\s*$")
CJK_RE = re.compile(r"[\u3400-\u9fff\uff00-\uffef\u3000-\u303f]")

SEC_ORDER = {str(i): i for i in range(1, 14)}
for i, s in enumerate("ABCDEFG"):
    SEC_ORDER[s] = 100 + i

SEC_TITLE = {
    "1": "叙述式目录", "2": "超对称线算子", "3": "带框 BPS 态",
    "4": "形式线算子", "5": "与簇代数的关系", "6": "线算子与模空间上的全纯函数",
    "7": "六维视角", "8": "模空间与全纯函数的例子", "9": "$A_1$ 理论与叶层",
    "10": "$A_1$ 理论的例子", "11": "量子和乐", "12": "热带标签", "13": "开放问题",
    "A": "关于 $d=4$、$\\mathcal N=2$ 超对称的一些技术细节", "B": "线算子 vev 的全纯性",
    "C": "不动点方程", "D": "低能有效理论中的不动点方程", "E": "六维超对称",
    "F": "Fock--Goncharov 坐标与 traffic rules", "G": "$SU(2)$、$N_f=0$ 与切比雪夫多项式",
}


def extract(pdf_path):
    doc = fitz.open(pdf_path)
    found = {}          # num -> page
    dup = []
    for pno in range(doc.page_count):
        page = doc[pno]
        for blk in page.get_text("dict")["blocks"]:
            if blk.get("type") != 0:
                continue
            for line in blk["lines"]:
                text = "".join(s["text"] for s in line["spans"])
                m = LINE_RE.search(text)
                if not m:
                    continue
                x1 = line["bbox"][2]
                if x1 < RIGHT_EDGE:
                    continue
                if CJK_RE.search(text):
                    continue
                num = "%s.%s" % (m.group(1), m.group(2))
                if num in found:
                    dup.append((num, pno + 1, found[num]))
                    continue
                found[num] = pno + 1
    doc.close()
    return found, dup


def sort_key(num):
    sec, idx = num.split(".")
    return (SEC_ORDER.get(sec, 999), int(idx))


def check_continuity(found):
    """逐节检查编号 1..n 连续，返回 (缺失字典, 逐节最大号字典)。"""
    by_sec = {}
    for num in found:
        sec, idx = num.split(".")
        by_sec.setdefault(sec, set()).add(int(idx))
    missing, top = {}, {}
    for sec, idxs in by_sec.items():
        n = max(idxs)
        top[sec] = n
        miss = [i for i in range(1, n + 1) if i not in idxs]
        if miss:
            missing[sec] = miss
    return missing, top


def write_outputs(found, outdir):
    nums = sorted(found, key=sort_key)
    tsv = os.path.join(outdir, "eq_index.tsv")
    with open(tsv, "w", encoding="utf-8", newline="\n") as f:
        f.write("num\tpage\n")
        for num in nums:
            f.write("%s\t%d\n" % (num, found[num]))

    # 按 (节, 页) 分组，页内式号升序
    groups = {}
    for num in nums:
        sec = num.split(".")[0]
        groups.setdefault((SEC_ORDER.get(sec, 999), sec, found[num]), []).append(num)
    md = os.path.join(outdir, "eq_table.md")
    with open(md, "w", encoding="utf-8", newline="\n") as f:
        f.write("| 节 | 译本页 | 式号 |\n")
        f.write("|---|---|---|\n")
        prev_sec = None
        for (order, sec, page) in sorted(groups):
            label = ("§" + sec) if sec.isdigit() else ("附录 " + sec)
            sec_cell = label if sec != prev_sec else ""
            prev_sec = sec
            f.write("| %s | p%d | %s |\n" % (sec_cell, page, ", ".join(groups[(order, sec, page)])))
    return tsv, md, nums


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", default=DEFAULT_PDF)
    ap.add_argument("--outdir", default=HERE)
    args = ap.parse_args()
    if not os.path.exists(args.pdf):
        sys.exit("找不到 PDF：%s" % args.pdf)

    found, dup = extract(args.pdf)
    missing, top = check_continuity(found)
    tsv, md, nums = write_outputs(found, args.outdir)

    import fitz as _f
    pages = _f.open(args.pdf).page_count
    print("PDF       : %s" % args.pdf)
    print("页数       : %d" % pages)
    print("编号公式   : %d" % len(found))
    print("逐节计数   : " + ", ".join("%s=%d" % (s, top[s]) for s in
                                     sorted(top, key=lambda s: SEC_ORDER.get(s, 999))))
    print("缺号       : %s" % (missing if missing else "无"))
    print("重号       : %s" % (dup if dup else "无"))
    print("输出       : %s / %s" % (tsv, md))
    sec_count = {}
    for num in found:
        sec_count[num.split(".")[0]] = sec_count.get(num.split(".")[0], 0) + 1
    assert sum(sec_count.values()) == len(found)


if __name__ == "__main__":
    main()
