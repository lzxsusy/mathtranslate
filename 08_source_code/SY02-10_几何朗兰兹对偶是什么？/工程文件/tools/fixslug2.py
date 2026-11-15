from pathlib import Path
import re
p = Path(r'<HOME>\Downloads\GL_work\源码\chunks\notes.tex')
s = p.read_text(encoding='utf-8')
out = []
for line in s.split('\n'):
    if line.count('&') == 2 and '+' in line and not line.startswith('\\'):
        cells = line.split('&')
        cell = cells[1]
        cell = cell.replace('\\allowbreak', '').replace('+', '+\u200b\\allowbreak ')
        cells[1] = cell
        line = '&'.join(cells)
    out.append(line)
p.write_text('\n'.join(out), encoding='utf-8')
print('rows patched:', sum(1 for l in out if 'allowbreak' in l))
