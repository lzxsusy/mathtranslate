# -*- coding: utf-8 -*-
import re
p = r'<HOME>\Downloads\GL_work\源码\chunks\notes.tex'
s = open(p, encoding='utf-8').read()

old_spec = (r'p{0.28\linewidth}>{\raggedright\arraybackslash}p{0.26\linewidth}'
            r'>{\raggedright\arraybackslash}p{0.09\linewidth}'
            r'>{\raggedright\arraybackslash}p{0.26\linewidth}')
new_spec = (r'p{0.26\linewidth}>{\raggedright\arraybackslash}p{0.24\linewidth}'
            r'>{\raggedright\arraybackslash}p{0.13\linewidth}'
            r'>{\raggedright\arraybackslash}p{0.26\linewidth}')
print('spec found:', old_spec in s)
s = s.replace(old_spec, new_spec)

out, rows = [], 0
for line in s.split('\n'):
    if line.rstrip().endswith('\\\\') and line.count('&') == 3:
        parts = [x.strip() for x in line.rstrip()[:-2].split('&')]
        if re.fullmatch(r'\d{4}-\d{2}-\d{2}', parts[2]):
            parts[2] = r'\mbox{%s}' % parts[2]
            rows += 1
        out.append(' & '.join(parts) + r' \\')
    else:
        out.append(line)

open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
print('mbox rows', rows)
