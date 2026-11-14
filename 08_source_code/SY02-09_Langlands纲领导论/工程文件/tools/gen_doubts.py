# -*- coding: utf-8 -*-
"""生成 work/疑点清单.tsv（v2.0 §1.0 要求：位置/原文表述/类型/初步猜测/查证动作/结论/依据/状态）。
后续各讲报告交来后，用 append_doubts.py 追加；本脚本只负责初始化（含 L1 与术语两批）。"""
import os

HEADER = ["位置", "原文表述", "类型", "初步猜测", "查证动作", "结论", "依据", "状态"]

rows = [
    # ---- L1 逐页对照发现的疑点 ----
    ["L1 定理2.6 证明（lecture01.tex:131；原书 p8）",
     "原书 has a subgroup of order m1；旧译作「它有一个指数为 m1 的子群」",
     "术语/概念",
     "order=阶，不是指数；m1 整除 p1-1，指数为 m1 的子群是另一回事",
     "打开 work/orig_png/p008.png 看原句；复习群论：G 有阶 m 的子群 vs 指数 m 的子群",
     "确认应为「阶为 m1 的子群」；旧译误。已改译文正文并加 Tutor Note",
     "原书 p8 原文 order m1",
     "已解"],
    ["L1 笔记2.3 证明（原书 p6）",
     "原书把 θ 的余域写作 Z/mZ，同一段后文又说 θ 的像为 (Z/mZ)^x",
     "笔误",
     "余域应为 (Z/mZ)^x",
     "看图 orig_png/p006.png；对照命题 2.2 的陈述",
     "原书笔误；译文已按正确写法。已加 % [Tutor Note]",
     "原书 p6 / 命题 2.2",
     "已解"],
    ["L1 推论2.5 证明（原书 p7）",
     "原书右端写成 [Q(zeta_n):Q]·[Q(zeta_n):Q]（两次 zeta_n）",
     "笔误",
     "应为 [Q(zeta_m):Q][Q(zeta_n):Q]",
     "看图 orig_png/p007.png；由塔律核对",
     "笔误；译文正确。已加 Tutor Note",
     "原书 p7",
     "已解"],
    ["L1 定理2.6 证明（原书 p8）",
     "原书列式 1<=t<=sum_j m_j",
     "笔误",
     "应为 sum_j a_j（m_j 是分解后的指数，此处应取 a_j）",
     "看图 orig_png/p008.png；对照定理 2.6 陈述",
     "笔误；译文正确。已加 Tutor Note",
     "原书 p8",
     "已解"],
    ["L1 习题提示（原书 p8）",
     "原书 phi(m)=2 <=> m=4 或 6",
     "笔误",
     "漏了 m=3（phi(3)=2）",
     "逐个验算 phi(m)",
     "笔误；译文写「m=3,4,6」。已加 Tutor Note",
     "phi(3)=2",
     "已解"],
    ["L1 定理2.7（原书 p10）",
     "原书 Dirichlet 定理（模 b 的等差数列中含无穷多素数）未声明 b != 0",
     "笔误/跳步",
     "需 b != 0，否则同余式无意义",
     "看图 orig_png/p010.png",
     "原书缺条件；译文补上。已加 Tutor Note",
     "原书 p10",
     "已解"],
    # ---- 术语裁决 ----
    ["全书术语（lecture01/02，11 处）",
     "cyclotomic field 旧译「圆分域」",
     "术语",
     "应为「分圆域」（分圆多项式/分圆单位/分圆扩张 是标准译法）",
     "查本库 01_corpus_zh 的 zh_paragraphs.jsonl / termbase.jsonl（零命中，无先例）；查中文学界通行译名",
     "定案「分圆域」，已全局替换 11 处 + terminology.tsv 同步",
     "v2.0 §2 四问 + 中文学界惯例",
     "已解"],
    ["全书术语（lecture10/15/16，12 处）",
     "profinite 旧译「投有限」",
     "术语",
     "应为「射有限」（射有限群/射有限完备化）",
     "查本库术语既有先例（射有限群、射有限完备化均已入库）",
     "定案「射有限」，已全局替换 12 处",
     "本库术语先例",
     "已解"],
    ["L1 笔记2.3 / 阿贝尔化（lecture01.tex:74）",
     "一般群的阿贝尔化写作 G/[G,G]，但非 Hausdorff 情形需取闭包",
     "记号",
     "应为 G/closure([G,G])",
     "查 nLab abelianization 条目",
     "确认需取闭包；译注已说明",
     "nLab \"abelianization\"",
     "已解"],
]

p = r'<本地路径>'
with open(p, 'w', encoding='utf-8', newline='\n') as f:
    f.write('\t'.join(HEADER) + '\n')
    for r in rows:
        assert len(r) == 8, r
        f.write('\t'.join(r) + '\n')
print('wrote', p, len(rows), 'rows')
