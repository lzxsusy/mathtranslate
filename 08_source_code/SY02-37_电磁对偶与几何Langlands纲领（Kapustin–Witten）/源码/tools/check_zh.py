# -*- coding: utf-8 -*-
"""逐片冒烟编译中文译稿 zh/NN-sXX.tex（用法同 check_shards：python tools/check_zh.py [过滤]）。
额外检查：译文里是否混入 Unicode 数学/排版命令禁用项、公式编号注释数是否与 skel 一致。"""
import io, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XELATEX = r"C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe"

BAD_CMDS = ['\\usepackage', '\\documentclass', '\\newcommand', '\\renewcommand', '\\def\\', '\\input{']
BAD_UNI = '−×≤≥≠∈∀∃∑∫∞∂∇√±∓⊗⊕⟨⟩'

def compile_one(name):
    tex = os.path.join(ROOT, 'chkz_%s.tex' % name[:-4])
    src = ('\\documentclass[11pt,a4paper]{article}\n'
           '\\input{preamble}\n'
           '\\begin{document}\n'
           '\\input{zh/%s}\n'
           '\\end{document}\n') % name
    io.open(tex, 'w', encoding='utf-8').write(src)
    subprocess.run([XELATEX, '-interaction=batchmode', '-file-line-error',
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

def lint(zh_path, skel_path):
    z = io.open(zh_path, encoding='utf-8').read()
    s = io.open(skel_path, encoding='utf-8').read()
    msg = []
    for c in BAD_CMDS:
        if c in z:
            msg.append('禁用命令出现: %s' % c)
    uni = sorted(set(ch for ch in z if ch in BAD_UNI))
    if uni:
        msg.append('Unicode 数学符号: %s' % ''.join(uni))
    # 编号锚一致性
    nz = len(re.findall(r'^% 式 \(', z, re.M))
    ns = len(re.findall(r'^% 式 \(', s, re.M))
    if nz != ns:
        msg.append('公式锚数不一致: skel=%d zh=%d' % (ns, nz))
    ncs = len(re.findall(r'\\setcounter\{equation\}', z))
    nss = len(re.findall(r'\\setcounter\{equation\}', s))
    if ncs != nss:
        msg.append('\\setcounter{equation} 数不一致: skel=%d zh=%d' % (nss, ncs))
    nl = len(re.findall(r'\\label\{', z)); nls = len(re.findall(r'\\label\{', s))
    if nl != nls:
        msg.append('\\label 数不一致: skel=%d zh=%d' % (nls, nl))
    nc = len(re.findall(r'\\cite\{', z)); ncs2 = len(re.findall(r'\\cite\{', s))
    if nc != ncs2:
        msg.append('\\cite 数不一致: skel=%d zh=%d' % (ncs2, nc))
    return msg

if __name__ == '__main__':
    pat = sys.argv[1] if len(sys.argv) > 1 else ''
    d = os.path.join(ROOT, 'zh')
    names = sorted(n for n in os.listdir(d) if n.endswith('.tex') and pat in n) if os.path.isdir(d) else []
    bad = 0
    for n in names:
        errs = compile_one(n)
        msg = lint(os.path.join(d, n), os.path.join(ROOT, 'skel', n))
        if errs or msg:
            bad += 1
            print('== %s' % n)
            for e in errs[:6]:
                print('    [编译]', e)
            for m in msg:
                print('    [规范]', m)
    print('\n%d/%d zh 文件有问题' % (bad, len(names)))
