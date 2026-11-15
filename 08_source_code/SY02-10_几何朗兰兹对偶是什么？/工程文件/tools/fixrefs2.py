from pathlib import Path
import re

p = Path(r'<HOME>\Downloads\GL_work\源码\chunks\refs.tex')
s = p.read_text(encoding='utf-8')

# 1) 撇号后多余空格：Jong’ s → Jong’s
s = s.replace('\u2019 s', '\u2019s').replace("' s", "'s")
# 2) “单词.数字年份”：correspondence.2021 → correspondence. 2021（只在小写字母后动）
s = re.sub(r'(?<=[a-z])\.(?=\d{4}\b)', '. ', s)
# 3) 弯引号不配对
s = s.replace('the \u201d small\u201d fle', 'the \u201csmall\u201d fle')
# 4) 重音符号缺失
s = s.replace("Progr\\'es", 'Progrès')
# 5) 双空格压成单空格
s = re.sub(r'(?<![\\{])  +(?![}])', ' ', s)

p.write_text(s, encoding='utf-8')
print('ok')
