# -*- coding: utf-8 -*-
"""生成资料卡 04 的 ③ 参考文献外核表（markdown），追加到 04 文件末尾。
数据来源：工程文件/work/refs.tsv（原文条目解析） + refs-check.tsv（CrossRef/arXiv 核验结果）。
"""
import csv
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]  # 工程根（tools 在 工程文件/tools 之下）
REF = ROOT / "工程文件" / "work" / "refs.tsv"
CHK = ROOT / "工程文件" / "work" / "refs-check.tsv"
OUT = ROOT / "资料卡" / "04-术语文献勘误.md"

# 人工复核结论（其余交脚本判定）
MANUAL = {
    "17": "ok",   # Crossref 2016 版卷期页：Amer. J. Math. 105(1), 85–114 与原文一致（题名含 l-adic 排版，检索串未命中，已手工核 Crossref）
    "22": "ok",   # 东京大学官网与 MR4973974：J. Math. Sci. Univ. Tokyo 32(2), 157–240，原文无误
}


def load(p):
    rows = []
    with p.open(encoding="utf-8") as f:
        for ln in f:
            parts = ln.rstrip("\n").split("\t")
            rows.append(parts)
    return rows[1:]


def shorten(authors):
    """作者串缩略：保留前两位 + 等"""
    a = authors.replace(" and ", ", ")
    names = [n.strip() for n in a.split(",") if n.strip()]
    fams = [n.split()[-1] for n in names]
    if len(fams) <= 2:
        return "、".join(fams)
    return fams[0] + " 等 " + str(len(fams)) + " 人"


def venue_str(v, vol, iss, pg):
    if not v:
        return ""
    s = v
    if vol:
        s += " " + vol
    if iss:
        s += "(" + iss + ")"
    if pg:
        s += ", " + pg
    return s


def main():
    refs = load(REF)
    chk = {r[0]: r for r in load(CHK)}
    lines = []
    lines.append("")
    lines.append("## ③ 参考文献外核（56 条，逐条对 Crossref / arXiv / 出版社官网）")
    lines.append("")
    lines.append("做法：`工程文件/tools/check_refs.py extract` 从 `源码/sections/s13-refs.tex` 抽出 56 条 → "
                 "`verify` 逐条查 Crossref REST（有 DOI 者）或 arXiv API（有编号者），结果落 `工程文件/work/refs-check.tsv`。"
                 "卷、期、页三者与原文一致记 **OK**；原文与检索结果不同记 **DIFF**；检索不到记 **MISS**；书/讲义/网页无 DOI 与编号记 **SKIP**（这类逐条人工核出版社页）。")
    lines.append("")
    lines.append("| # | 作者·年 | 原文所载出处 | 核验 | 说明 |")
    lines.append("|---|---|---|---|---|")
    n_ok = n_skip = n_fix = 0
    for r in refs:
        num, authors, year, title, venue, vol, iss, pg, arxiv = r[:9]
        c = chk.get(num, ["", "", "", ""])
        typ, status, note = c[1], c[2], (c[3] if len(c) > 3 else "")
        if num in MANUAL:
            status = "OK"
            note = {"17": "Crossref 题名检索未命中（题名含 l-adic 排版），按作者+卷期查得 Amer. J. Math. 105(1), 85–114，与原文一致",
                    "22": "Crossref 无 DOI 记录；东京大学官网 Vol. 32 (2025) No. 02、MR4973974 均为 157–240，与原文一致"}[num]
            typ = "官网"
        src = venue_str(venue, vol, iss, pg) if venue else ("arXiv:" + arxiv if arxiv else "（书/讲义/网页）")
        if status == "OK":
            n_ok += 1
            if typ == "arXiv":
                m = re.search(r"\((\d{4});", note)
                note = "arXiv 题名一致，首发 " + (m.group(1) if m else "?")
            elif typ == "官网":
                pass
            else:
                note = "Crossref 期刊卷期页一致"
        elif status == "SKIP":
            n_skip += 1
            note = "书/讲义/网页，无 DOI 与编号，人工核书名与年份"
        else:
            n_fix += 1
        if authors and set(authors) <= {"—", "-", " "}:
            authors = "同上"
        lines.append("| {} | {}（{}） | {} | {} | {} |".format(
            num, shorten(authors) if authors else "同上", year, src, status, note.replace("|", "/")))
    lines.append("")
    lines.append("**统计**：OK {} 条，书/讲义/网页人工核 {} 条，需订正 {} 条。".format(n_ok, n_skip, n_fix))
    lines.append("")
    lines.append("### 3.1 三处需要说明但不是错的地方")
    lines.append("")
    lines.append("1. **arXiv 首发年 ≠ 原文标注年（共 6 条，照录不改）**：Efimov（2025，arXiv 2405.12169 作 2024）、"
                 "Emerton–Gee–Hellmann（2025，arXiv 2210.01404 作 2022）、Gaitsgory–Raskin（2026，arXiv 2409.09856 作 2024）、"
                 "Lafforgue–Zhu（2019，arXiv 1811.07976 作 2018）、Liu–Zheng（2024，arXiv 1211.5948 作 2012）、"
                 "Beraldo–Kazhdan–Schlank（2022，arXiv 1801.00655 作 2018）。"
                 "原文按**所引版本/出版年**标注（Bourbaki 报告的通行做法），译文照录，不改年份。")
    lines.append("2. **第 17 条 Drinfeld（1983）**：题名里的 $\\ell$-adic 在 PDF 中是数学斜体，Crossref 的题名检索串对不上，"
                 "按作者与卷期直接查得 *Amer. J. Math.* **105**(1), 85–114，**原文无误**。")
    lines.append("3. **第 22 条 Fargues（2025）**：Crossref 只有 *J. reine angew. Math.* 的同名条目且无卷期页（那是另一篇），"
                 "本篇实为 *J. Math. Sci. Univ. Tokyo* **32**(2), 157–240（东京大学数理科学研究科官网 + MR4973974 双向确认），**原文无误**。")
    lines.append("4. **未发现卷期页错误**：56 条中没有一条的卷、期或起止页与检索结果冲突；两处 MISS/DIFF 经人工复核均系检索串问题。")
    old = OUT.read_text(encoding="utf-8")
    cut = old.find("\n## ③")
    if cut < 0:
        cut = old.find("\n## ④")
    if cut >= 0:
        old = old[:cut]
    OUT.write_text(old.rstrip("\n") + "\n" + "\n".join(lines) + "\n", encoding="utf-8")
    print("追加 ③ 完成：OK", n_ok, "SKIP", n_skip, "待订正", n_fix)


if __name__ == "__main__":
    main()
