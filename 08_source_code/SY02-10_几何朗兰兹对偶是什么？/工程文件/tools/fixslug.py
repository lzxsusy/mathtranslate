from pathlib import Path
import re

p = Path(r'<HOME>\Downloads\GL_work\源码\chunks\notes.tex')
s = p.read_text(encoding='utf-8')

# 表格中第二列的 nLab slug：允许在 + 处换行
def fix(m):
    slug = m.group(1)
    return slug.replace('+', '+\\allowbreak ')

# 只处理形如 “& quantum+geometric+Langlands+correspondence &” 的单元格
s = re.sub(r'& ([A-Za-z0-9][A-Za-z0-9+_.\-]*\+[A-Za-z0-9+_.\-]*) &', lambda m: '& ' + m.group(1).replace('+', '\\allowbreak +') + ' &', s)
p.write_text(s, encoding='utf-8')
print('ok')
