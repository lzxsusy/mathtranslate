#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""package_rosetta.py — 组装《罗塞塔词典》交付目录

输出：KW06_work/交付/罗塞塔词典/
  成品/      词典 PDF、逻辑流程图 PDF、源码 zip
  源码/      main/preamble/front/appendix-*.tex、entries/、flow/*.tex
  工程文件/  SCHEMA/README/REF-TERMS/extract_report/TEST-QUESTIONS/tools/
  盲测/      题面、答卷、评分报告
"""
import io
import os
import shutil
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))          # rosetta/
BASE = os.path.dirname(ROOT)                                                 # KW06_work/
OUT = os.path.join(BASE, u'交付', u'罗塞塔词典')


def ensure(p):
    if not os.path.isdir(p):
        os.makedirs(p)


def copy(src, dst):
    if not os.path.exists(src):
        print('  skip (missing) %s' % os.path.basename(src))
        return
    ensure(os.path.dirname(dst))
    if os.path.isdir(src):
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
    else:
        shutil.copy2(src, dst)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    ensure(OUT)
    ensure(os.path.join(OUT, u'成品'))
    ensure(os.path.join(OUT, u'源码'))
    ensure(os.path.join(OUT, u'工程文件'))
    ensure(os.path.join(OUT, u'盲测'))

    # 成品
    copy(os.path.join(ROOT, 'main.pdf'), os.path.join(OUT, u'成品', u'KW06_罗塞塔词典_v1.0.pdf'))
    copy(os.path.join(ROOT, 'flow', 'flow.pdf'), os.path.join(OUT, u'成品', u'KW06_论证逻辑流程图_v1.0.pdf'))

    # 源码
    for f in ('main.tex', 'preamble.tex', 'front.tex', 'appendix-table.tex', 'appendix-bg.tex', 'appendix-flow.tex'):
        copy(os.path.join(ROOT, f), os.path.join(OUT, u'源码', f))
    copy(os.path.join(ROOT, 'entries'), os.path.join(OUT, u'源码', 'entries'))
    ensure(os.path.join(OUT, u'源码', 'flow'))
    for f in ('flow.tex',):
        copy(os.path.join(ROOT, 'flow', f), os.path.join(OUT, u'源码', 'flow', f))

    # 工程文件
    for f in ('SCHEMA.md', 'README.md', 'REF-TERMS.tsv', 'extract_report.txt', 'TEST-QUESTIONS.md'):
        copy(os.path.join(ROOT, f), os.path.join(OUT, u'工程文件', f))
    copy(os.path.join(ROOT, 'tools'), os.path.join(OUT, u'工程文件', 'tools'))

    # 盲测
    for f in ('BLIND-QUESTIONS.md', 'ANSWERS-round1.md', 'ANSWERS-round2.md', u'评分报告.md', 'DICTIONARY.txt'):
        copy(os.path.join(ROOT, 'blind', f), os.path.join(OUT, u'盲测', f))

    # 源码 zip
    zip_path = os.path.join(OUT, u'成品', u'KW06_罗塞塔词典_源码_v1.0.zip')
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        src_root = os.path.join(OUT, u'源码')
        for dirpath, _dirs, files in os.walk(src_root):
            for fn in files:
                full = os.path.join(dirpath, fn)
                rel = os.path.relpath(full, src_root)
                z.write(full, rel)
        for f in ('SCHEMA.md', 'README.md', 'REF-TERMS.tsv', 'TEST-QUESTIONS.md'):
            p = os.path.join(ROOT, f)
            if os.path.exists(p):
                z.write(p, 'engineering/' + f)
    print('packed -> %s' % OUT)
    for dirpath, dirs, files in os.walk(OUT):
        lvl = dirpath.replace(OUT, '').count(os.sep)
        print('  ' * lvl + os.path.basename(dirpath) + '/  (%d files)' % len(files))


if __name__ == '__main__':
    main()
