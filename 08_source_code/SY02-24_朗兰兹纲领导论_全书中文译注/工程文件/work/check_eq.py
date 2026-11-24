# -*- coding: utf-8 -*-
r"""Equation-number reconciliation per chapter: \tag{...} in TeX vs (N.M) numbers seen in raw text."""
import os, re, io

BASE = os.path.dirname(os.path.abspath(__file__))
EN = os.path.join(BASE, 'en')
SRC = os.path.join(os.path.dirname(BASE), '..', '\u6e90\u7801', 'chapters')
NUM = re.compile(r'^\d+\.\d+$')

def key(s):
    a, b = s.split('.')
    return (int(a), int(b))

lines = []
for i in range(1, 13):
    nn = '%02d' % i
    t = io.open(os.path.join(SRC, 'ch%s.tex' % nn), encoding='utf-8').read()
    tags = [m.group(1).strip() for m in re.finditer(r'\\tag\{([^}]*)\}', t)]
    good = [x for x in tags if NUM.match(x)]
    bad = [x for x in tags if not NUM.match(x)]
    r = io.open(os.path.join(EN, 'ch%s_raw.txt' % nn), encoding='utf-8').read()
    rawn = {'%s.%s' % (m.group(1), m.group(2))
            for m in re.finditer(r'(?<![\d.])(\d{1,2})\.(\d{1,2})(?![\d])', r)}
    only_raw = sorted(rawn - set(good), key=key)
    only_tex = sorted(set(good) - rawn, key=key)
    dup = sorted({x for x in good if good.count(x) > 1}, key=key)
    lines.append('CH %s tags=%d(ok %d) raw=%d dup=%s nontag=%s'
                 % (nn, len(tags), len(good), len(rawn), dup or '-', bad or '-'))
    lines.append('  only_raw(%d): %s' % (len(only_raw), ' '.join(only_raw)))
    lines.append('  only_tex(%d): %s' % (len(only_tex), ' '.join(only_tex)))
    lines.append('  tags: %s' % ' '.join(good))

io.open(os.path.join(BASE, 'eq_report.txt'), 'w', encoding='utf-8').write('\n'.join(lines))
print('ok')
