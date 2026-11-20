# -*- coding: utf-8 -*-
import io, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'reports'))
p = '02_疑点清单.tsv'
s = io.open(p, encoding='utf-8').read()
s = s.replace('\t笔迹\t', '\t笔误\t')
s = s.replace('\t未解', '\t待核')
# 给 $A^1$ 那一条补上交代
s = s.replace('保留 $A^1$ 原记号，批注说明字迹与含义均不确定',
              '保留 $A^1$ 原记号；含义不明，译文照录并在批注中说明；不影响任何计算')
io.open(p, 'w', encoding='utf-8').write(s)
rows = [l for l in s.split('\n') if l.strip()]
print('rows', len(rows))
from collections import Counter
print(Counter(l.split('\t')[-1] for l in rows[1:]))
