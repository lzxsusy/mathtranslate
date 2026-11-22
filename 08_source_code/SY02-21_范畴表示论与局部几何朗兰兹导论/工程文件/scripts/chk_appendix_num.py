import re, fitz
BASE = r'C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论'
mine = fitz.open(BASE + r'\源码\main.pdf')
t = "\n".join(p.get_text() for p in mine)
orig = open(BASE + r'\工程文件\work\原文\full.txt', encoding='utf-8').read()

def items(s):
    return ['%s.%s' % (a, b) for a, b in re.findall(r'A\.(\d)\.(\d+)\.', s)]

def eqs(s):
    return re.findall(r'\((A\.\d+)\)', s)

for name, f in [('items A.x.y', items), ('eqs (A.n)', eqs)]:
    a, b = f(orig), f(t)
    print(name, 'orig', len(a), a)
    print(name, 'mine', len(b), b)
