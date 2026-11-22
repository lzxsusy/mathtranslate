import fitz
BASE = r'C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论'
d = fitz.open(BASE + r'\源码\main.pdf')
toc = d.get_toc()
for lvl, title, page in toc:
    if lvl <= 2:
        print('%s%s  -> p%s' % ('  ' * (lvl - 1), title, page))
print('total pages', len(d))
