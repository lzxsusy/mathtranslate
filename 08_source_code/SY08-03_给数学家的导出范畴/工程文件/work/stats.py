# -*- coding: utf-8 -*-
"""统计源码与成品数据 -> deliverable/统计数据.txt"""
import io, os, re, glob

here = os.path.dirname(os.path.abspath(__file__))
base = os.path.abspath(os.path.join(here, '..', '..'))
src = os.path.join(base, '源码')
pdf = os.path.join(src, 'main.pdf')

tex_files = sorted(glob.glob(os.path.join(src, '**', '*.tex'), recursive=True))
total_chars = 0
cjk = 0
for p in tex_files:
    t = io.open(p, encoding='utf-8').read()
    total_chars += len(t)
    cjk += len(re.findall(r'[\u4e00-\u9fff]', t))


def count(pattern):
    n = 0
    for p in tex_files:
        n += len(re.findall(pattern, io.open(p, encoding='utf-8').read()))
    return n


pages = 0
size = 0
if os.path.exists(pdf):
    size = os.path.getsize(pdf)
    import subprocess
    gs = r'C:/Users/admin/AppData/Local/Programs/tools/bin/gswin64c.exe'
    try:
        out = subprocess.run([gs, '-q', '-dNOSAFER', '-dNODISPLAY', '-c',
                              '(main.pdf) (r) file runpdfbegin pdfpagecount = quit'],
                             cwd=src, capture_output=True, text=True, timeout=60)
        pages = int(out.stdout.strip() or 0)
    except Exception:
        pages = 0

rows = [
    ('源码 .tex 文件数', len(tex_files)),
    ('源码总字符', total_chars),
    ('中文字符', cjk),
    ('译注（yizhu）', count(r'\\begin\{yizhu\}')),
    ('校勘框（kanwu）', count(r'\\begin\{kanwu\}')),
    ('概念卡片（conceptbox）', count(r'\\begin\{conceptbox\}')),
    ('本节重点（keytakeaways）', count(r'\\begin\{keytakeaways\}')),
    ('定理/定义/例/注环境', count(r'\\begin\{(thm|lemma|prop|cor|definition|eg|remark)\}')),
    ('编号公式', count(r'\\begin\{equation\}')),
    ('TikZ 图', count(r'\\begin\{tikzpicture\}')),
    ('PDF 页数', pages),
    ('PDF 字节', size),
]

out = os.path.join(base, '工程文件', 'deliverable', '统计数据.txt')
with io.open(out, 'w', encoding='utf-8', newline='\n') as f:
    f.write('SY08-03 给数学家的导出范畴 · 统计数据\n')
    f.write('生成时间：2026-11-20\n\n')
    for k, v in rows:
        f.write('%-28s %s\n' % (k, v))
print('ok')
