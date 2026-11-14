# -*- coding: utf-8 -*-
"""生成 work/notes/notes_01.tsv（L1 样板：8 条译注 + 6 条 Tutor Note 登记）。"""
import os

rows = [
    ("01", "完美域", "lecture01.tex:22", "B/nLab", "https://ncatlab.org/nlab/show/perfect+field", "2017-07-21", "ok"),
    ("01", "Krull拓扑", "lecture01.tex:37", "B/nLab", "https://ncatlab.org/nlab/show/profinite+group", "2025-07-01", "ok"),
    ("01", "可分闭包", "lecture01.tex:45", "B/nLab", "https://ncatlab.org/nlab/show/separable+closure", "2026-04-15", "ok"),
    ("01", "阿贝尔化", "lecture01.tex:74", "B/nLab", "https://ncatlab.org/nlab/show/abelianization", "2026-01-21", "ok"),
    ("01", "分裂域", "lecture01.tex:79", "B/nLab", "https://ncatlab.org/nlab/show/splitting+field", "2026-06-08", "ok"),
    ("01", "Dirichlet L-级数", "lecture01.tex:139", "B/nLab", "https://ncatlab.org/nlab/show/L-function", "2024-07-07", "ok"),
    ("01", "逆Galois问题", "lecture01.tex:141", "B/nLab", "https://ncatlab.org/nlab/show/inverse+Galois+problem", "2023-05-27", "ok"),
    ("01", "射有限完备化", "lecture01.tex:176", "B/nLab", "https://ncatlab.org/nlab/show/profinite+group", "2025-07-01", "ok"),
    ("01", "原书 p6：theta 的余域前后不一致", "lecture01.tex:87", "A/原书",
     "原书 p6 将 theta 的余域写作 Z/mZ，紧接着又说其像为 (Z/mZ)^x；译文按正确的 (Z/mZ)^x 处理。", "-", "tutor-note"),
    ("01", "原书 p7：推论 2.5 次数公式重复 zeta_n", "lecture01.tex:114", "A/原书",
     "原书 p7 右端误写作 [Q(zeta_n):Q]·[Q(zeta_n):Q]；译文按 [Q(zeta_m):Q][Q(zeta_n):Q] 处理。", "-", "tutor-note"),
    ("01", "原书 p8：定理 2.6 证明下界写错", "lecture01.tex:127", "A/原书",
     "原书 p8 下界误写作 1<=t<=sum_j m_j，与 m_j 含义不符；译文按 sum_j a_j 处理。", "-", "tutor-note"),
    ("01", "原书 p8：order m_1 旧译误作指数", "lecture01.tex:131", "A/原书",
     "原书 p8 作 has a subgroup of order m_1，旧译误作「指数为 m_1 的子群」；本轮已改正译文正文。", "-", "tutor-note"),
    ("01", "原书 p10：Dirichlet 定理未声明 b != 0", "lecture01.tex:137", "A/原书",
     "原书 p10 未声明 b != 0，而 b=0 时同余式无意义；译文补上。", "-", "tutor-note"),
    ("01", "原书 p8：习题提示漏 m=3", "lecture01.tex:149", "A/原书",
     "原书 p8 习题提示作「m=4 或 6」，漏了 m=3（phi(3)=2）；译文已补正。", "-", "tutor-note"),
]

p = r'<本地路径>'
os.makedirs(os.path.dirname(p), exist_ok=True)
with open(p, 'w', encoding='utf-8', newline='\n') as f:
    for r in rows:
        assert len(r) == 7, r
        f.write('\t'.join(r) + '\n')
print('wrote', p, len(rows), 'rows')
