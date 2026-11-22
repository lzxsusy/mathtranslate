import io
p = r'C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论\源码\chunks\ch23.tex'
s = io.open(p, encoding='utf-8').read()
a = r'\on{\acute{e}tale}'
b = r'\text{étale}'
n = s.count(a)
s = s.replace(a, b)
io.open(p, 'w', encoding='utf-8').write(s)
print('replaced', n)
print('remaining acute:', s.count('acute'))
