# -*- coding: utf-8 -*-
r"""收尾用：给 glossary.tsv 与 疑点清单.tsv 追加条目（幂等：已存在的 key 跳过）。"""
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WORK = os.path.join(ROOT, "work")

GLOSS = os.path.join(WORK, "glossary.tsv")
QUES = os.path.join(WORK, "疑点清单.tsv")

NEW_GLOSS = [
    ("Tate cycle", "Tate 轮", "A（Milne 等通行译法）", "§5.2"),
    ("cycle class map", "轮类映射", "A", "§5.2"),
    ("perfectly smooth", "完全光滑", "B（Stacks Project 00T6 的 perfect morphism）", "§5.1"),
    ("prestack", "预叠", "A", "§4.1"),
    ("torsor", "主丛", "A（SY02-17 同）", "§4.1"),
    ("inner twist", "内扭曲", "A", "§5.1"),
    ("Rapoport–Zink uniformization", "Rapoport–Zink 均化", "A", "§5.1"),
    ("Shimura set", "Shimura 集", "A", "§5.1"),
    ("superspecial", "超特殊", "A", "§5.1"),
    ("crystal", "晶体", "A", "§5.1"),
    ("fiber product", "纤维积", "A", "§5.1"),
    ("Hecke correspondence", "Hecke 对应", "A", "§5.1"),
    ("Shimura datum", "Shimura 数据", "A", "§5.1"),
    ("reflex field", "反射域", "A", "§5.1"),
    ("Newton stratification", "Newton 分层", "A", "§5.2"),
    ("basic Newton stratum", "基本 Newton 层", "A", "§5.2"),
    ("Borel–Moore homology", "Borel–Moore 同调", "A", "§5.2"),
    ("cohomological correspondence", "上同调对应", "A", "§6.1"),
    ("base changeable", "可基变换", "I（本文自定术语，原文加粗定义）", "§6.1"),
    ("support of a correspondence", "对应的支撑", "A", "§6.1"),
    ("enhancement", "增强", "B（nLab enhancement）", "§6.2"),
    ("homotopy category", "同伦范畴", "A", "§4"),
    ("nearly coherent functor", "近循环函子", "I（Fargues–Scholze 原文用语）", "§4"),
    ("geometric Satake equivalence", "几何 Satake 等价", "A（SY02-17 同）", "§1"),
    ("spherical Hecke algebra", "球面 Hecke 代数", "A", "§2.1"),
    ("cocharacter", "余特征标", "A（原记号兼指余权）", "§2.1"),
    ("uniformizer", "一致化元", "A", "§2.1"),
    ("modification", "修正", "I（原文 modification，Beilinson–Drinfeld 用语）", "§2.1"),
    ("perfection", "完全化", "B（Stacks Project 0EVU）", "§2.1"),
    ("jet group", "射流群", "A", "§2.1"),
    ("loop group", "环路群", "A", "§2.1"),
    ("partial Frobenius", "部分 Frobenius", "A", "§3.2"),
    ("universal homeomorphism", "泛同胚", "I（本文用语）", "§3.2"),
]

NEW_Q = [
    ("Q30", "2075", r"\Sht_{\mu_1|\mu_2}^{\loc(m_1.n_1)}",
     "交换图中该记号的指标分隔符写作句点 m_1.n_1，全篇其余处均为逗号",
     "照原文写句点，加译者按说明应为逗号", "errata E16", "已解"),
    ("Q31", "2573", r"\bibitem[DM]{DM} ... LNM 900 (1982), 101?228.",
     "页码区间写成 101?228，问号应为短横",
     "书目保留原样（不改书目文字），登记 errata", "errata E20", "已解"),
    ("Q32", "2597", r"\bibitem[HTX]{HTX} ... Alegbra and Number Theory 11",
     "期刊名拼作 Alegbra，应为 Algebra",
     "书目保留原样，登记 errata", "errata E21", "已解"),
]


def append_gloss():
    rows = [l.rstrip("\n").split("\t") for l in io.open(GLOSS, encoding="utf-8") if l.strip()]
    have = {r[0] for r in rows}
    add = [r for r in NEW_GLOSS if r[0] not in have]
    with io.open(GLOSS, "a", encoding="utf-8") as f:
        for r in add:
            f.write("\t".join(r) + "\n")
    print("glossary +%d -> %d" % (len(add), len(rows) + len(add)))


def append_ques():
    rows = [l.rstrip("\n").split("\t") for l in io.open(QUES, encoding="utf-8") if l.strip()]
    have = {r[0] for r in rows}
    add = [r for r in NEW_Q if r[0] not in have]
    with io.open(QUES, "a", encoding="utf-8") as f:
        for r in add:
            f.write("\t".join(r) + "\n")
    print("疑点 +%d -> %d" % (len(add), len(rows) + len(add)))


append_gloss()
append_ques()
