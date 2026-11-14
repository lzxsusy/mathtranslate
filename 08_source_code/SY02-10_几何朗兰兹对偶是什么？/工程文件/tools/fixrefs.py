from pathlib import Path
import re

p = Path(r'C:\Users\admin\Downloads\GL_work\源码\chunks\refs.tex')
s = p.read_text(encoding='utf-8')

subs = [
    ('https://doi-org.ezproxy.lib.utexas.edu/', 'https://doi.org/'),
    ('http://projecteuclid.org.ezproxy.lib.utexas.edu/', 'http://projecteuclid.org/'),
    ('https://www-ams-org.ezproxy.lib.utexas.edu/', 'https://www.ams.org/'),
    ('https://link-springer-com.ezproxy.lib.utexas.edu/', 'https://link.springer.com/'),
    ('.ezproxy.lib.utexas.edu', ''),
    ('Gelfand-Diki˘i', 'Gelfand-Dikii'),
    ('Tam´as', 'Tamás'),
    ('P˘adurariu', 'Pădurariu'),
    ('Fæ rgeman', 'Færgeman'),
    ('DpXq', r'D(X)'),
    ('Dp ˆ Xq', r'D(\hat X)'),
    ('GLp2q', r'\mathrm{GL}_2(\F_q)'),
]
for a, b in subs:
    s = s.replace(a, b)

# 仍未处理的 “pXq” 类：\url 内可能有的方括号/尖括号，交 xurl 处理
p.write_text(s, encoding='utf-8')
print('替换完成，剩余 ezproxy 出现次数:', s.count('ezproxy'))
print('剩余 ˘ 次数:', s.count('˘'), ' 剩余 ´ 次数:', s.count('´'), ' 剩余 pXq:', s.count('pXq'))
