# -*- coding: utf-8 -*-
"""把 源码/units/*.tex 装配成 源码/chapters/chNN.tex。

用法：
    python 工程文件/scripts/assemble.py --check    # 只报告缺哪些单元
    python 工程文件/scripts/assemble.py            # 重写 chapters/ch01..ch10.tex

章文件只做两件事：写 \bdchap（章标题）与按序 \input 各单元。
单元文件自己带 \bdsec 与 \SourcePage，因此装配是无损拼接。
"""
import glob
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(os.path.dirname(HERE))
UNITS = os.path.join(PROJ, '源码', 'units')
CHDIR = os.path.join(PROJ, '源码', 'chapters')

CHAPTERS = [
    (0, 'intro', '引论', 0),
    (1, 'stack', '栈上的微分算子', 1),
    (2, 'quant', 'Hitchin 哈密顿量的量子化', 2),
    (3, 'oper', 'Oper', 3),
    (4, 'pfaff', 'Pfaffian 及其相关', 4),
    (5, 'hecke', 'Hecke 特征 D-模', 5),
    (6, 'hecke2', 'Hecke 性质 II', 6),
    (7, 'appstack', '附录：代数栈上的 D-模理论与 Hecke 模式', 7),
    (8, 'ins5', '待插入 5.x 的材料', 8),
    (9, 'ins6', '待插入第 6 节的材料', 9),
    (10, 'ins6b', '待插入第 6 节的材料（续）', 10),
]


def main():
    check_only = '--check' in sys.argv
    only = None
    for i, a in enumerate(sys.argv):
        if a.startswith('--only='):
            only = {int(x) for x in a.split('=', 1)[1].split(',') if x.strip()}
    missing = []
    for num, label, title, _ in CHAPTERS:
        pat = os.path.join(UNITS, 'ch%02d_u*.tex' % num)
        files = sorted(glob.glob(pat))
        if num == 0:
            files = []  # 第 0 章由 chapters/ch00.tex 手写，不参与装配
        if not files and num != 0:
            missing.append('ch%02d' % num)
        if check_only or num == 0:
            continue
        if only is not None and num not in only:
            continue
        out = ['%% 本文件由 工程文件/scripts/assemble.py 生成，勿手改。']
        has_chap = any('\\bdchap' in io.open(f, encoding='utf-8').read() for f in files)
        if not has_chap:
            out.append('\\bdchap{ch:%s}{%s}' % (label, title))
        out.append('')
        for f in files:
            out.append('\\input{units/%s}' % os.path.basename(f)[:-4])
        path = os.path.join(CHDIR, 'ch%02d.tex' % num)
        with io.open(path, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write('\n'.join(out) + '\n')
        print('wrote chapters/ch%02d.tex  (%d units)' % (num, len(files)))
    if missing:
        print('缺单元：', ', '.join(missing))
    return 0


if __name__ == '__main__':
    sys.exit(main())
