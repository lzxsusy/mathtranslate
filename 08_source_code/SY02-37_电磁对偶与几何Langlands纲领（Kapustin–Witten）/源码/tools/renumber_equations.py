# -*- coding: utf-8 -*-
"""按原文的节内顺序重排公式编号（\numberwithin{equation}{section}）。
原因：glshortspare.defs 里少数 label 名跨节复用，转换器据此写出的 % 式 (s.m) 注释与 \setcounter 落错节
（实测：eq:hombo 应为 (3.32) 却写成 (11.5)；07-s03、19-s07 另有 3 处）。原文公式是节内顺序编号，
所以按「节内出现顺序」重排是唯一正确的做法。
一并处理：行内注释 `text % 式 (a.b)`、独立注释行、\tag*{(a.b)}。
用法：python tools/renumber_equations.py [--dry]
"""
import io, glob, re, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files = sorted(glob.glob(os.path.join(ROOT, 'skel', '*.tex')))
dry = '--dry' in sys.argv

RE_COMMENT = re.compile(r'^(.*?)(% 式 \()\d+\.\d+(\))(\s*)$')
RE_SET = re.compile(r'^\\setcounter\{equation\}\{(\d+)\}$')
RE_TAG = re.compile(r'^\\tag\*\{\(\d+\.\d+\)\}$')

sec = None
n = 0
report = []
for f in files:
    lines = io.open(f, encoding='utf-8').read().split('\n')
    out = []
    i = 0
    changed = 0
    while i < len(lines):
        l = lines[i]
        if re.match(r'^\\section\{', l) or re.match(r'^\\section\*?\{', l):
            sec = int(re.search(r'-s(\d+)\.tex', f).group(1))
            n = 0
            out.append(l); i += 1; continue
        mc = RE_COMMENT.match(l)
        if mc:
            # 找后续第一个非空行，看是否是 setcounter
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            ms = RE_SET.match(lines[j]) if j < len(lines) else None
            n += 1
            out.append('%s%% 式 (%d.%d)%s' % (mc.group(1), sec, n, mc.group(4)))
            if ms:
                for k in range(i + 1, j):
                    out.append(lines[k])
                out.append('\\setcounter{equation}{%d}' % (n - 1))
                i = j + 1
            else:
                i += 1
            changed += 1
            continue
        if RE_TAG.match(l):
            n += 1
            out.append('\\tag*{(%d.%d)}' % (sec, n))
            changed += 1
            i += 1
            continue
        out.append(l); i += 1
    if changed:
        if not dry:
            io.open(f, 'w', encoding='utf-8').write('\n'.join(out))
        report.append((os.path.basename(f), changed))
for r in report:
    print('%-12s %d eqs' % r)
print('total files %d, total eqs %d, %s' % (len(report), sum(r[1] for r in report), 'dry' if dry else 'written'))
