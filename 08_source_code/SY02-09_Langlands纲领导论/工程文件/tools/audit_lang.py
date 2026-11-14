# -*- coding: utf-8 -*-
import re, os, glob, json, sys
base = r'<本地路径>'
files = sorted(glob.glob(os.path.join(base, '*.tex')))
pats = {
 '被所': r'被[^。，；]{1,20}所',
 '进行': r'进行[^。，；]{0,10}的',
 '对于而言': r'对于[^。，；]{1,25}而言',
 '使得得以': r'使得[^。，；]{0,15}得以',
 '以及': r'以及',
 'TutorNote': r'\[Tutor ?Note',
 'footnote': r'\\footnote',
 'zhushi': r'\\znote|begin\{zhushi\}',
 '连续的地': r'的[^。，；]{0,6}的[^。，；]{0,6}的',
 '硬编码ref': r'第\s*\d+(\.\d+)*\s*(节|讲|章)',
}
rows = []
for f in files:
    s = open(f, encoding='utf-8').read()
    n = os.path.basename(f)
    ch = re.search(r'\\chapter\{([^}]*)\}', s)
    row = {'file': n, 'title': ch.group(1) if ch else '', 'chars': len(s)}
    for k, p in pats.items():
        row[k] = len(re.findall(p, s))
    rows.append(row)
hdr = ['file','title','chars'] + list(pats)
print('\t'.join(hdr))
for r in rows:
    print('\t'.join(str(r.get(h,'')) for h in hdr))
tot = {k: sum(r[k] for r in rows) for k in pats}
print('TOTAL\t\t%d\t%s' % (sum(r['chars'] for r in rows), '\t'.join(str(tot[k]) for k in pats)))
