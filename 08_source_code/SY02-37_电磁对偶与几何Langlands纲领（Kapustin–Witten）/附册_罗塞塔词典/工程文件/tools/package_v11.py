# -*- coding: utf-8 -*-
"""打包 v1.1 交付：详册 v1.1（罗塞塔词典）+ 核心词典 v1.0。

用法：python rosetta/tools/package_v11.py
"""
import os, shutil, glob, io

ROOT = r'C:\Users\admin\Downloads\KW06_work'
ROS = os.path.join(ROOT, 'rosetta')
CORE = os.path.join(ROOT, 'core')
OUT = os.path.join(ROOT, '交付')


def clean_dir(d):
    if os.path.isdir(d):
        shutil.rmtree(d)
    os.makedirs(d)


def cp(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.isdir(src):
        shutil.copytree(src, dst, dirs_exist_ok=True)
    elif os.path.exists(src):
        shutil.copy2(src, dst)
        return True
    return False


def zipdir(srcdir, zpath):
    shutil.make_archive(zpath, 'zip', srcdir)


# ---------------- 详册 v1.1 ----------------
ros_out = os.path.join(OUT, '罗塞塔词典')
clean_dir(ros_out)

# 成品
cp(os.path.join(ROS, 'main.pdf'), os.path.join(ros_out, '成品', 'KW06_罗塞塔词典_v1.1.pdf'))
cp(os.path.join(ROS, 'flow', 'flow.pdf'), os.path.join(ros_out, '成品', 'KW06_论证逻辑流程图_v1.1.pdf'))

# 源码
for f in ['preamble.tex', 'main.tex', 'front.tex', 'appendix-table.tex', 'appendix-bg.tex',
          'appendix-sym.tex', 'appendix-flow.tex', 'SCHEMA.md', 'README.md', 'REF-TERMS.tsv',
          'TEST-QUESTIONS.md', 'extract_report.txt']:
    cp(os.path.join(ROS, f), os.path.join(ros_out, '源码', f))
cp(os.path.join(ROS, 'entries'), os.path.join(ros_out, '源码', 'entries'))
cp(os.path.join(ROS, 'flow'), os.path.join(ros_out, '源码', 'flow'))
cp(os.path.join(ROS, 'tools'), os.path.join(ros_out, '工程文件', 'tools'))

# 盲测
bsrc = os.path.join(ROS, 'blind')
bdst = os.path.join(ros_out, '盲测')
os.makedirs(bdst, exist_ok=True)
for f in glob.glob(os.path.join(bsrc, '*.md')) + glob.glob(os.path.join(bsrc, '*.txt')):
    cp(f, os.path.join(bdst, os.path.basename(f)))

# 源码 zip + 报告
zipdir(os.path.join(ros_out, '源码'), os.path.join(ros_out, '成品', 'KW06_罗塞塔词典_v1.1_源码'))
print('rosetta done:', len(glob.glob(os.path.join(ros_out, '**', '*'), recursive=True)))

# ---------------- 核心词典 v1.0 ----------------
core_out = os.path.join(OUT, '核心词典')
clean_dir(core_out)

cp(os.path.join(CORE, 'main.pdf'), os.path.join(core_out, '成品', 'KW06_核心罗塞塔词典_v1.0.pdf'))
cp(os.path.join(CORE, 'stone-onepage.pdf'), os.path.join(core_out, '成品', 'KW06_核心石碑一页版_v1.0.pdf'))

for f in ['preamble.tex', 'main.tex', 'front.tex', 'c1-duality.tex', 'c2-branes.tex',
          'c3-langlands.tex', 'appendix-stone.tex', 'stone-onepage.tex', 'SCHEMA.md', 'README.md']:
    cp(os.path.join(CORE, f), os.path.join(core_out, '源码', f))

cb = os.path.join(CORE, 'blind')
if os.path.isdir(cb):
    for f in glob.glob(os.path.join(cb, '*.md')) + glob.glob(os.path.join(cb, '*.txt')):
        cp(f, os.path.join(core_out, '盲测', os.path.basename(f)))

zipdir(os.path.join(core_out, '源码'), os.path.join(core_out, '成品', 'KW06_核心罗塞塔词典_v1.0_源码'))
print('core done:', len(glob.glob(os.path.join(core_out, '**', '*'), recursive=True)))

# 顶层 README
io.open(os.path.join(OUT, '附册说明.md'), 'w', encoding='utf-8', newline='\n').write(
    '# 附册说明（SY02-37）\n\n'
    '- `罗塞塔词典/`：详册 v1.1，87 页，108 条词条 + 三附录（对照总表 / 背景术语 / 论证逻辑流程图）\n'
    '- `核心词典/`：核心词典 v1.0，24 页，15 条 nLab 式核心词条 + 石碑总表 + 一页版石碑\n\n'
    '两者关系：详册供查阅，核心词典供搭骨架；核心词典每条 700–1200 字、按「定义—陈述—证明/构造—例—状态」写。\n')
print('ALL OK')
