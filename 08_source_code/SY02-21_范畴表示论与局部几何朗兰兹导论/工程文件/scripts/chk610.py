import re, sys
import fitz

def numlist(text, pat):
    return re.findall(pat, text)

mine = fitz.open(r'C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论\源码\main.pdf')
t = "\n".join(p.get_text() for p in mine)
orig = open(r'C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论\工程文件\work\原文\full.txt', encoding='utf-8').read()

for pat, name in [(r'\b6\.10\.(\d+)\b', '6.10.x'), (r'\((6\.3\d)\)', '(6.3x)')]:
    a = sorted(set(numlist(orig, pat)), key=lambda x: int(x))
    b = sorted(set(numlist(t, pat)), key=lambda x: int(x))
    print(name, 'orig', len(a), a)
    print(name, 'mine', len(b), b)
