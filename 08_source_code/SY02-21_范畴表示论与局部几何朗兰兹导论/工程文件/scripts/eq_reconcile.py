import re, io, fitz
BASE = r'C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论'
orig = io.open(BASE + r'\工程文件\work\原文\full.txt', encoding='utf-8').read()
d = fitz.open(BASE + r'\源码\main.pdf')
mine = "\n".join(p.get_text() for p in d)

pat = re.compile(r'\((A|[1-6])\.(\d{1,2})\)')

def seq(s):
    return [m.group(1) + '.' + m.group(2) for m in pat.finditer(s)]

a, b = seq(orig), seq(mine)
sa, sb = set(a), set(b)
print('orig eqs:', len(sa), 'mine eqs:', len(sb))
print('missing in mine:', sorted(sa - sb, key=lambda x: (x.split('.')[0], int(x.split('.')[1]))))
print('extra in mine:', sorted(sb - sa, key=lambda x: (x.split('.')[0], int(x.split('.')[1]))))
