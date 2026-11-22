# -*- coding: utf-8 -*-
"""从原文导言区抽取宏定义（340-797 行）到 源码/preamble_macros.tex，
并剔除与 ctexart / 本文 preamble 冲突或不需要的行。"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, 'work', 'src', 'ZhiweiYunPCMI.tex')
DST = os.path.join(os.path.dirname(ROOT), '源码', 'preamble_macros.tex')

# 不需要 / 会冲突的行（整行匹配）
DROP_PATTERNS = [
    r'^\\def\\s[BCDEFGHIJKLMNOPQRSTUVWXYZ]\{',      # 保留，不丢；占位
]

HEADER = r'''% ============================================================
%  SY02-22《Springer 理论与轨道积分讲义》译稿：原文自定义宏
%  由 工程文件/scripts/port_orig_macros.py 从原文导言区（340--797 行）抽取，
%  只保留数学记号宏；原文的 \newtheorem、\usepackage、\swapnumbers、
%  subsubsection 重定义等已由 preamble.tex 统一处理。
% ============================================================

'''

def main():
    with open(SRC, encoding='utf-8') as f:
        lines = f.readlines()
    body = lines[339:797]
    out = []
    for ln in body:
        s = ln.rstrip('\n')
        # 跳过原文注释行里的排版残留
        if re.match(r'^\s*%+opening', s):
            continue
        if re.match(r'^\s*\\begin\{document\}', s):
            break
        out.append(s)
    text = HEADER + '\n'.join(out) + '\n'
    with open(DST, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    print('wrote', DST, len(text), 'chars', len(out), 'lines')


if __name__ == '__main__':
    main()
