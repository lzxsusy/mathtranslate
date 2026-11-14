# -*- coding: utf-8 -*-
"""把本轮新定的术语追加进 src/terminology.tsv（去重）。"""
import os

P = r'<本地路径>'
ADD = [
    ("ramification index", "分歧指数"),
    ("residue field", "剩余域"),
    ("local reciprocity map", "局部互反映射"),
    ("global reciprocity map", "整体互反映射"),
    ("reciprocity map", "互反映射"),
    ("norm map", "范映射"),
    ("norm subgroup", "范数子群"),
    ("local Langlands correspondence", "局部Langlands对应"),
    ("unramified representation", "非分歧表示"),
    ("smooth representation", "光滑表示"),
    ("admissible representation", "可容许表示"),
    ("archimedean place", "阿基米德素位"),
    ("eigenform", "特征形式"),
    ("q-expansion", "q展开"),
    ("complex multiplication", "复乘"),
    ("finite etale cover", "有限平展覆盖"),
    ("categorification", "范畴化"),
    ("geometric class field theory", "几何类域论"),
    ("open compact subgroup", "开紧子群"),
    ("maximal compact subgroup", "极大紧子群"),
    ("Levi subgroup", "Levi子群"),
    ("affine flag variety", "仿射旗簇"),
    ("algebraic group", "代数群"),
    ("unipotent", "幺幂"),
    ("Satake transform", "Satake变换"),
    ("spherical function", "球函数"),
    ("automorphic quotient", "自守商"),
    ("adelic quotient", "阿代尔商"),
    ("geometric point", "几何点"),
    ("essentially small", "本质小"),
]

lines = open(P, encoding='utf-8').read().splitlines()
have = set()
for ln in lines[1:]:
    parts = ln.split('\t')
    if parts:
        have.add(parts[0].strip().lower())
added = []
for en, zh in ADD:
    if en.strip().lower() in have:
        continue
    lines.append('%s\t%s' % (en, zh))
    have.add(en.strip().lower())
    added.append((en, zh))
open(P, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
print('total lines:', len(lines))
print('added:', len(added))
for a in added:
    print('  +', a[1], '<-', a[0])
