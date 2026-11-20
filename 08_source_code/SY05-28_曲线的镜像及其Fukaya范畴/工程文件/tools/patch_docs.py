# -*- coding: utf-8 -*-
import io, os
os.chdir(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')))

p = '工程文件/README.md'
s = io.open(p, encoding='utf-8').read()
old = '  original/           底本 PDF 与 300 dpi 页面 PNG（只读，不入库改动）'
new = ('  original/           底本 PDF 与 300 dpi 页面 PNG（只读；按 L4 规则不入库，\n'
       '                     本地保留以备复核，见 `源码/.gitignore`）')
assert old in s
s = s.replace(old, new, 1)
io.open(p, 'w', encoding='utf-8', newline='\n').write(s)

p = '工程文件/reports/04_交付核对.md'
s = io.open(p, encoding='utf-8').read()
old = '| 10 | `源码/original/` | ✅ | 4 份 PDF + 31 张 300 dpi PNG，未改动 |'
new = ('| 10 | `源码/original/` | ✅ | 4 份 PDF + 31 张 300 dpi PNG，未改动；'
       '按 COMPLIANCE R1（L4 禁入）不入库，已在 `源码/.gitignore` 排除 |')
assert old in s
s = s.replace(old, new, 1)
io.open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('docs updated')
