import re, fitz, io, sys
BASE = r'C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论'
d = fitz.open(BASE + r'\源码\main.pdf')

item_re = re.compile(r'^(?:(定理|引理|推论|命题|猜想|注|例|定义)\s*)?(\d{1,2}\.\d{1,2}\.\d{1,2})\.\s*(.*)$')
eq_re = re.compile(r'\((\d{1,2}\.\d{1,2})\)\s*$')
sec_re = re.compile(r'^(\d{1,2})\.\s+(\S.*)$')

out = []
for pno in range(len(d)):
    txt = d[pno].get_text()
    for line in txt.split('\n'):
        line = line.strip()
        m = item_re.match(line)
        if m:
            kind = m.group(1) or '段'
            out.append(('item', pno + 1, m.group(2), kind, m.group(3)[:48]))
            continue
        m2 = eq_re.search(line)
        if m2 and len(line) < 90:
            out.append(('eq', pno + 1, m2.group(1), '', line[:40]))

for kind, page, num, t, txt in out:
    print('%s\tp%d\t%s\t%s\t%s' % (kind, page, num, t, txt))
print('TOTAL items', sum(1 for x in out if x[0] == 'item'), 'eqs', sum(1 for x in out if x[0] == 'eq'))
