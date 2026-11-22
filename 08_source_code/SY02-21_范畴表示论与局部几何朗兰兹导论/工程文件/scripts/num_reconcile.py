import re, io, fitz
BASE = r'C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论'
orig = io.open(BASE + r'\工程文件\work\原文\full.txt', encoding='utf-8').read()
d = fitz.open(BASE + r'\源码\main.pdf')
mine = "\n".join(p.get_text() for p in d)

pat = re.compile(r'(?<![\d.])([1-6A])\.(\d{1,2})\.(\d{1,2})\.')

def seq(s):
    return [m.group(1) + '.' + m.group(2) + '.' + m.group(3) for m in pat.finditer(s)]

a, b = seq(orig), seq(mine)
print('orig items:', len(a))
print('mine items:', len(b))
# compare as sets first
sa, sb = set(a), set(b)
print('missing in mine:', sorted(sa - sb)[:20], len(sa - sb))
print('extra in mine:', sorted(sb - sa)[:20], len(sb - sa))
print('orig first 12:', a[:12])
print('mine first 12:', b[:12])
