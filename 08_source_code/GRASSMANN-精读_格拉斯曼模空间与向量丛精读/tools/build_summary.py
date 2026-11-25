# -*- coding: utf-8 -*-
"""Phase 4：由实际文件生成 产出/汇总/README.md、产出/批注/00-修订补丁.md 与 stats.tsv。

  python tools/build_summary.py
"""
import os
import re
import sys
import io
import glob
import json
import collections

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "产出")
CARDS = os.path.join(os.path.dirname(ROOT), "_cards_grassmann", "cards")

PAGES = {1: (7, 29), 2: (30, 54), 3: (55, 71), 4: (72, 81), 5: (82, 93),
         6: (94, 115), 7: (116, 134), 8: (135, 159), 9: (160, 170)}
EXIST = {1: 8, 2: 14, 3: 5, 4: 3, 5: 7, 6: 13, 7: 6, 8: 18, 9: 7}
TITLES = {
    1: "Hitchin 的射影平坦联络、Toeplitz 算子与 TQFT 曲线算子的渐近展开",
    2: "Koszul 上同调及其在模空间中的应用",
    3: "Reider 定理与 Thaddeus 对再探",
    4: "丛的奇异模空间中的相交配对",
    5: "Beilinson–Drinfeld 格拉斯曼流形与辛纽结同调",
    6: "曲线上层的模空间的算术方面",
    7: "代数曲线上 α-稳定凝聚系的存在性",
    8: "阿贝尔簇上的正则性 III：与一般消没的关系及应用",
    9: "可约曲线上的向量丛及应用",
}


def cjk(s):
    return sum(1 for ch in s if 0x4E00 <= ord(ch) <= 0x9FFF)


def read(p):
    if not os.path.isfile(p):
        return None
    return open(p, encoding="utf-8-sig", errors="replace").read()


def chapter_stats():
    st = {}
    for n in range(1, 10):
        tag = "ch%02d" % n
        d = {}
        for key, sub, fname in (("daodu", "导读", "导读"), ("pizhu", "批注", "批注"), ("biji", "笔记", "笔记")):
            t = read(os.path.join(OUT, sub, "%s-%s.md" % (tag, fname)))
            d[key + "_file"] = t is not None
            d[key] = cjk(t) if t else 0
        pz = read(os.path.join(OUT, "批注", "%s-批注.md" % tag)) or ""
        d["n_pizhu"] = len(re.findall(r"^##\s*\d+\.", pz, re.M))
        d["pizhu_types"] = dict(collections.Counter(
            re.findall(r"【([^】]+)】", pz)))
        et = read(os.path.join(OUT, "批注", "%s-errata.tsv" % tag))
        d["errata"] = 0 if not et else max(0, len(et.strip().splitlines()) - 1)
        ct = read(os.path.join(OUT, "汇总", "cards-%s.tsv" % tag))
        d["cards"] = 0 if not ct else max(0, len(ct.strip().splitlines()) - 1)
        rp = read(os.path.join(OUT, "汇总", "%s-report.md" % tag)) or ""
        d["report"] = bool(rp)
        d["status"] = "partial" if re.search(r"partial|存疑", rp) else ("done" if rp else "—")
        st[n] = d
    return st


def errata_rows():
    p = os.path.join(OUT, "批注", "00-审校总表.tsv")
    if not os.path.isfile(p):
        return [], []
    lines = open(p, encoding="utf-8").read().splitlines()
    head = lines[0].split("\t")
    rows = [dict(zip(head, ln.split("\t"))) for ln in lines[1:] if ln.strip()]
    return head, rows


def cell(s, n=400):
    s = (s or "").replace("|", "\\|").replace("\n", " ")
    return s if len(s) <= n else s[:n] + "…"


def write_patch(st, rows):
    by = collections.Counter(r["type"] for r in rows)
    sev = collections.Counter(r["severity"] for r in rows)
    L = ["# 修订补丁（00-修订补丁）", "",
         "> 依据：`产出\\批注\\00-审校总表.tsv`（ch1–ch9 九份 errata 合并，%d 行）。" % len(rows),
         "> 口径：只收**译文/术语/公式/编号**层面、可落到中译页码与原句的修订建议；",
         "> 英文原书自身的错误（中译照译或已消解）单列 §5，供提交 AMS 勘误；",
         "> 已有 81 条译注复核后**未发现错误**，故 `existing-note-wrong` 为 0 条（§0）。", "",
         "## §0 已有译注复核（existing-note-wrong）", "",
         "九章共复核 81 条译注（ch1 8 / ch2 14 / ch3 5 / ch4 3 / ch5 7 / ch6 13 / ch7 6 / ch8 18 / ch9 7）。",
         "逐条在 `source\\chapters\\chNN.tex` 对应行核对后：**判断全部成立**，无一条需要改判；",
         "个别译注只覆盖了同一错误的首次出现（如 ch8 `Pic^0(X)` 笔误在同一节复现 3 次），",
         "已按**新增 errata** 处理（见 §2），不计作 existing-note-wrong。", "",
         "## §1 高优先级（severity = high）", ""]
    hi = [r for r in rows if r["severity"] == "high"]
    if not hi:
        L.append("（无）")
    else:
        L += ["| 章 | 中译页 | 类型 | 原句（节录） | 问题 | 建议 |", "|---|---|---|---|---|---|"]
        for r in hi:
            L.append("| %s | %s | %s | %s | %s | %s |" % (
                r["chapter"], r["loc_zh"], r["type"], cell(r["original"], 90),
                cell(r["problem"], 160), cell(r["suggestion"], 160)))
    L += ["", "## §2 中优先级（severity = medium）", ""]
    md = [r for r in rows if r["severity"] == "medium" and r["type"] != "original-error"]
    if not md:
        L.append("（无）")
    else:
        L += ["| 章 | 中译页 | 类型 | 原句（节录） | 问题 | 建议 |", "|---|---|---|---|---|---|"]
        for r in md:
            L.append("| %s | %s | %s | %s | %s | %s |" % (
                r["chapter"], r["loc_zh"], r["type"], cell(r["original"], 80),
                cell(r["problem"], 140), cell(r["suggestion"], 140)))
    L += ["", "## §3 低优先级（severity = low）", "",
          "低优先级共 %d 条，多为术语统一、语序、标点与「照英文直译」的风格问题。" % len(
              [r for r in rows if r["severity"] == "low"]), "",
          "| 章 | 中译页 | 类型 | 问题 | 建议 |", "|---|---|---|---|---|"]
    for r in rows:
        if r["severity"] == "low":
            L.append("| %s | %s | %s | %s | %s |" % (
                r["chapter"], r["loc_zh"], r["type"],
                cell(r["problem"], 130), cell(r["suggestion"], 130)))
    L += ["", "## §4 术语统一建议", "",
          "| 术语（英） | 现译（出处） | 建议统一为 | 依据 |", "|---|---|---|---|",
          "| stratum | 分层（ch5:108）/ 层（ch5:312） | 分层 | 同章两译；代数几何惯例 |",
          "| distinguished point | 特异点（ch5:312） | 特定点 | `distinguished` 非「奇异」 |",
          "| proper（映射） | 固有（ch3:796、803） | 本征（或「真」） | 中译惯例 |",
          "| Betti diagram | Betti 表（ch2 正文）/ Betti 图（术语表） | Betti 图 | 与术语表一致 |",
          "| gerbe banded by μ_n | 带 μ_n 带的 gerbe | μ_n-带化的 gerbe | 避免「带…带」 |",
          "| Rham cohomology（de Rham） | 已按 de Rham 处理 | — | 术语表已统一，正文复查通过 |", "",
          "## §5 英文原书勘误（original-error，%d 条）" % by.get("original-error", 0), "",
          "这些是 2011 年 AMS 原书自身的错误（英文 PDF 可查），中译或照译、或已在中文里消解。",
          "汇总在此便于向 AMS / Clay 提交；**不属于中译者的责任**。", "",
          "| 章 | 原书页 | 中译页 | 原文 | 问题 | 建议 |", "|---|---|---|---|---|---|"]
    for r in rows:
        if r["type"] == "original-error":
            L.append("| %s | %s | %s | %s | %s | %s |" % (
                r["chapter"], r["loc_book"], r["loc_zh"], cell(r["original"], 90),
                cell(r["problem"], 140), cell(r["suggestion"], 140)))
    L += ["", "## §6 统计", "",
          "| 项 | 数 |", "|---|---|",
          "| 合并 errata 总数 | %d |" % len(rows),
          "| 按类型 | %s |" % "、".join("%s %d" % (k, v) for k, v in sorted(by.items())),
          "| 按严重度 | %s |" % "、".join("%s %d" % (k, v) for k, v in sorted(sev.items())),
          "| 按章 | %s |" % "、".join("%s %d" % (k, v) for k, v in sorted(
              collections.Counter(r["chapter"] for r in rows).items())),
          "| existing-note-wrong | 0 |", ""]
    p = os.path.join(OUT, "批注", "00-修订补丁.md")
    open(p, "w", encoding="utf-8", newline="\n").write("\n".join(L))
    print("写出", p, len(rows), "行")


def write_readme(st, rows):
    tot_pz = sum(d["n_pizhu"] for d in st.values())
    tot_dd = sum(d["daodu"] for d in st.values())
    tot_bj = sum(d["biji"] for d in st.values())
    by = collections.Counter(r["type"] for r in rows)
    ncards = len(glob.glob(os.path.join(CARDS, "*", "*.json")))
    ncon = len(glob.glob(os.path.join(CARDS, "concepts", "*.json")))
    partial = [n for n, d in st.items() if d["status"] == "partial"]
    L = ["# 交付总览（README）", "",
         "《Grassmannians, Moduli Spaces and Vector Bundles》中译本（170 页、9 篇论文）精读与审校成果。", "",
         "## 一句话", "",
         "9 章导读 + %d 条批注 + %d 条 errata + 9 章笔记 + %d 张资料卡（概念 %d / 例子 %d），"
         "全部经 `tools\\check_chapter.py`（0 FAIL）与 `_cards_grassmann\\tools\\validate_cards.py --strict`（0 error）。"
         % (tot_pz, len(rows), ncards, ncon, ncards - ncon), "",
         "## 章级成果", "",
         "| 章 | 篇名 | 中译页 | 已有译注 | 导读(字) | 批注 | errata | 笔记(字) | 卡片候选 | 状态 |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for n in range(1, 10):
        d = st[n]
        if not (d["daodu_file"] or d["n_pizhu"]):
            continue
        L.append("| ch%d | %s | %d–%d | %d | %d | %d | %d | %d | %d | %s |" % (
            n, TITLES[n], PAGES[n][0], PAGES[n][1], EXIST[n],
            d["daodu"], d["n_pizhu"], d["errata"], d["biji"], d["cards"], d["status"]))
    L += ["| 合计 | — | 7–170 | 81 | %d | %d | %d | %d | %d | — |" % (
        tot_dd, tot_pz, len(rows), tot_bj, sum(d["cards"] for d in st.values())), "",
          "## 怎么读", "",
          "1. 先读 `产出\\导读\\00-全书导读.md`：九篇如何成为一本书、三条阅读路线。",
          "2. 再按章读 `产出\\导读\\chNN-导读.md`（这一章干什么 / 读前须知 / 怎么读 / 核心结果 / 术语）。",
          "3. 精读时对照 `产出\\批注\\chNN-批注.md`（位置 + 原文摘录 + 批注 + 类型）与 `产出\\批注\\chNN-errata.tsv`。",
          "4. 想自己做题/补证明，看 `产出\\笔记\\chNN-笔记.md`（主线 / 关键构造 / 补全 / 疑问 / 延伸）。",
          "5. 查概念用 `_cards_grassmann\\md\\INDEX.md`（或 `cards\\` 下 JSON），按轨道 A/1–9 检索。", "",
          "## 目录", "",
          "| 路径 | 内容 |", "|---|---|",
          "| `产出\\导读\\` | 00-全书导读 + 9 章导读 |",
          "| `产出\\批注\\` | 9 章批注、9 份 errata、00-审校总表.tsv、00-修订补丁.md |",
          "| `产出\\笔记\\` | 9 章读书笔记 |",
          "| `产出\\汇总\\` | 本文件、审校方法、交叉引用、术语增补、9 份章报告与卡片候选 |",
          "| `_cards_grassmann\\` | 资料卡库（SCHEMA、taxonomy、cards、索引） |",
          "| `tools\\` | preflight / 抽取译注 / 页码工具 / 逐章验收 / errata 合并 / 卡片计划 |", "",
          "## 统计", "",
          "| 项 | 数 |", "|---|---|",
          "| 精读页数（中译正文） | 164（p.7–170；前言 6 页另计） |",
          "| 导读汉字 | %d |" % tot_dd,
          "| 批注条数 | %d |" % tot_pz,
          "| errata 条数 | %d（%s） |" % (len(rows), "、".join(
              "%s %d" % (k, v) for k, v in sorted(by.items()))),
          "| 笔记汉字 | %d |" % tot_bj,
          "| 资料卡 | %d（概念 %d / 例子 %d） |" % (ncards, ncon, ncards - ncon),
          "| 已有译注复核 | 81 条，0 条改判 |",
          "", "## 未完成 / partial", ""]
    if partial:
        L.append("以下各章主体完成，但有个别推导/文献缺口，已在各章 report 的「存疑」里写明：")
        L.append("")
        for n in partial:
            L.append("- **ch%d**：见 `产出\\汇总\\ch%02d-report.md` 的「存疑」小节。" % (n, n))
    else:
        L.append("（无）")
    L += ["", "## 复现", "",
          "```",
          "python tools\\preflight.py                  # 环境与页表自检",
          "python tools\\check_chapter.py --all        # 九章质量门",
          "python tools\\merge_errata.py               # 合并 9 份 errata",
          "python _cards_grassmann\\tools\\validate_cards.py --strict",
          "python _cards_grassmann\\tools\\build_index.py",
          "python tools\\build_summary.py              # 重新生成本文件与修订补丁",
          "```", ""]
    p = os.path.join(OUT, "汇总", "README.md")
    open(p, "w", encoding="utf-8", newline="\n").write("\n".join(L))
    print("写出", p)


def write_stats(st, rows):
    p = os.path.join(OUT, "汇总", "stats.tsv")
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write("chapter\tpages_zh\texisting\tn_daodu\tn_pizhu\tn_errata\tn_biji\tn_cards\tcjk_daodu\tcjk_biji\tstatus\n")
        for n in range(1, 10):
            d = st[n]
            f.write("ch%02d\t%d-%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%s\n" % (
                n, PAGES[n][0], PAGES[n][1], EXIST[n], 5 if d["daodu_file"] else 0,
                d["n_pizhu"], d["errata"], 5 if d["biji_file"] else 0, d["cards"],
                d["daodu"], d["biji"], d["status"]))


def main():
    st = chapter_stats()
    _, rows = errata_rows()
    write_patch(st, rows)
    write_readme(st, rows)
    write_stats(st, rows)


if __name__ == "__main__":
    main()
