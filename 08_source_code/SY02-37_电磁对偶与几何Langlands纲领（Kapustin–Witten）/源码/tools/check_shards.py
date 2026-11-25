# -*- coding: utf-8 -*-
"""逐片冒烟编译：每个 skel/NN-sXX.tex 单独套 preamble 编译一遍，报出错误。
   用法： python tools/check_shards.py [文件名过滤]
   产物： out/chk_<name>.tex / .log（成功则删除 tex，保留 log 供查）
"""
import io, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XELATEX = r"C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe"
OUT = os.path.join(ROOT, 'out')


def run_one(name):
    tex = os.path.join(ROOT, 'chk_%s.tex' % name[:-4])
    src = ('\\documentclass[11pt,a4paper]{article}\n'
           '\\input{preamble}\n'
           '\\begin{document}\n'
           '\\input{skel/%s}\n'
           '\\end{document}\n') % name
    io.open(tex, 'w', encoding='utf-8').write(src)
    p = subprocess.run([XELATEX, '-interaction=batchmode', '-file-line-error',
                        os.path.basename(tex)], cwd=ROOT, capture_output=True)
    log = io.open(tex[:-4] + '.log', encoding='utf-8', errors='replace').read()
    errs = []
    for m in re.finditer(r'^(?:\./)?([^\n:]+):(\d+): (.*)$', log, re.M):
        errs.append('%s:%s: %s' % (m.group(1), m.group(2), m.group(3).strip()))
    if not errs and ('!' in log):
        for m in re.finditer(r'^! (.*)$', log, re.M):
            errs.append('! ' + m.group(1))
    try:
        os.remove(tex)
    except OSError:
        pass
    return errs


if __name__ == '__main__':
    pat = sys.argv[1] if len(sys.argv) > 1 else ''
    names = sorted(n for n in os.listdir(os.path.join(ROOT, 'skel'))
                   if n.endswith('.tex') and pat in n)
    bad = 0
    for n in names:
        errs = run_one(n)
        if errs:
            bad += 1
            print('== %s : %d errors' % (n, len(errs)))
            for e in errs[:6]:
                print('   ', e)
    print('\n%d/%d shards with errors' % (bad, len(names)))
