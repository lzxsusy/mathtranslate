# -*- coding: utf-8 -*-
"""从 work/en/p381-386.txt 生成 源码/refs.tex（参考文献）。

只做机械清洗：合并跨行、修 TeX 重音（´e → é 等）、转义 & % # _。
条目仍以人名键 [xx] 开头，正文按字面引用，不用 \\cite。
"""
import io
import os
import re
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(os.path.dirname(HERE))
EN = os.path.join(PROJ, '工程文件', 'work', 'en')
OUT = os.path.join(PROJ, '源码', 'refs.tex')

ACC = {
    'a': 'a\u0301', 'e': 'e\u0301', 'i': 'i\u0301', 'o': 'o\u0301', 'u': 'u\u0301',
    'A': 'A\u0301', 'E': 'E\u0301', 'O': 'O\u0301', 'U': 'U\u0301',
    'c': 'c\u0301', 'y': 'y\u0301', 'n': 'n\u0301', 's': 's\u0301', 'z': 'z\u0301',
}


def fix_accents(s):
    # ´x / `x / ¨x / ˆx / ˜x  以及 x´ 之类
    def acute(m):
        return unicodedata.normalize('NFC', m.group(1) + '\u0301')
    s = re.sub(r'[\u00b4\u02ca]([aeiouAEIOUncszy])', acute, s)
    s = re.sub(r'`([aeiouAEIOU])', lambda m: unicodedata.normalize('NFC', m.group(1) + '\u0300'), s)
    s = re.sub(r'\u00a8([aeiouAEIOU])', lambda m: unicodedata.normalize('NFC', m.group(1) + '\u0308'), s)
    s = re.sub(r'\u02c6([aeiouAEIOU])', lambda m: unicodedata.normalize('NFC', m.group(1) + '\u0302'), s)
    s = re.sub(r'~([aeiouAEIOU])', lambda m: unicodedata.normalize('NFC', m.group(1) + '\u0303'), s)
    # 残留的单独重音符号
    s = s.replace('\u00b4', '').replace('`', '')
    return s


TEXESC = [('&', r'\&'), ('%', r'\%'), ('#', r'\#'), ('_', r'\_')]


def esc(s):
    for a, b in TEXESC:
        s = s.replace(a, b)
    return s


def main():
    lines = []
    for p in range(381, 387):
        f = os.path.join(EN, 'p%03d.txt' % p)
        if not os.path.exists(f):
            continue
        with io.open(f, encoding='utf-8') as fh:
            for ln in fh:
                ln = ln.rstrip('\n')
                if ln.startswith('## '):
                    lines.append(ln)
                    continue
                lines.append(ln.strip())

    entries = []
    cur = None
    for ln in lines:
        if not ln:
            continue
        if ln.startswith('## '):
            continue
        m = re.match(r'^\[([^\]]+)\]\s*(.*)$', ln)
        if m:
            if cur:
                entries.append(cur)
            cur = [m.group(1).strip(), m.group(2).strip()]
        elif cur is not None:
            cur[1] = (cur[1] + ' ' + ln).strip()
    if cur:
        entries.append(cur)

    out = ['% 本文件由 工程文件/scripts/make_refs.py 从原文 p.381–386 机械搬运，',
           '% 仅修重音与转义；人名/刊名保持原文。',
           '\\bdsection*{参考文献}', '',
           '\\begin{description}[leftmargin=3.2em,style=nextline,itemsep=2pt]']
    for key, txt in entries:
        txt = fix_accents(txt)
        # 去掉换行连字符已由合并处理；这里再把 "- " 误断修掉
        txt = re.sub(r'(\w)-\s+(\w)', r'\1-\2', txt)
        out.append('\\item[{[%s]}] %s' % (key, esc(txt)))
    out.append('\\end{description}')
    out.append('')
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('\n'.join(out))
    print('entries:', len(entries))
    for k, t in entries:
        print('[%s] %s' % (k, t[:90]))


if __name__ == '__main__':
    main()
