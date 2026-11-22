import re, fitz, io, sys
BASE = r'C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论'
d = fitz.open(BASE + r'\源码\main.pdf')

item_re = re.compile(r'^(?:(定理|引理|推论|命题|猜想|注|例|定义)\s*)?(\d{1,2}|A)\.(\d{1,2})\.(\d{1,2})\.?')
eq_re = re.compile(r'\((\d{1,2}|A)\.(\d{1,2})\)$')

rows = []
for pno in range(len(d)):
    for line in d[pno].get_text().split('\n'):
        s = line.strip()
        m = item_re.match(s)
        if m:
            kind = m.group(1) or '段'
            if m.group(2) == 'A' and pno + 1 < 80:
                continue
            rest = s[m.end():].strip()
            rest = re.sub(r'^\([^)]*\)\.?\s*', '', rest)
            rows.append((m.group(2), m.group(3), m.group(4), kind, pno + 1, rest[:46]))
            continue
        m2 = eq_re.search(s)
        if m2 and len(s) < 95:
            rows.append((m2.group(1), m2.group(2), '', 'Eq', pno + 1, '(%s.%s)' % (m2.group(1), m2.group(2))))

seen = set(); uniq = []
for r in rows:
    key = (r[0], r[1], r[2])
    if r[3] == 'Eq':
        key = ('eq', r[0], r[1], '')
    if key in seen:
        continue
    seen.add(key); uniq.append(r)

groups = []  # [(label, [rows])]
cur = None
for r in uniq:
    if r[3] != 'Eq':
        lbl = ('附录 A.%s' % r[1]) if r[0] == 'A' else ('§%s.%s' % (r[0], r[1]))
        if cur is None or cur[0] != lbl:
            cur = (lbl, [])
            groups.append(cur)
    groups[-1][1].append(r)

buf = []
ni = ne = 0
for lbl, rs in groups:
    buf.append('\n### %s\n' % lbl)
    for sec, sub, k, kind, page, text in rs:
        if kind == 'Eq':
            buf.append('- 公式 %s' % text); ne += 1
        else:
            buf.append('- %s %s.%s.%s（p%d）%s' % (kind, sec, sub, k, page, text)); ni += 1
print('\n'.join(buf))
print('\nTOTAL items %d eqs %d groups %d' % (ni, ne, len(groups)))
