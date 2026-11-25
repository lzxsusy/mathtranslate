# -*- coding: utf-8 -*-
"""组装 KW06_work/交付/ 交付目录（幂等，可反复跑）。

用法：python tools/package_delivery.py [--version v1.0]
"""
import io, os, shutil, subprocess, sys, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(ROOT, '交付')
VERSION = 'v1.0'
if '--version' in sys.argv:
    VERSION = sys.argv[sys.argv.index('--version') + 1]

MAIN_PDF = os.path.join(ROOT, 'main.pdf')
GUIDE_PDF = os.path.join(ROOT, '思路导读', 'main.pdf')
NOTES_PDF = os.path.join(ROOT, '注疏', '译注汇编.pdf')

FILES = {
    '工程文件': ['brief/BRIEF.md', 'brief/SPEC.md', 'brief/TRANSLATOR-TASK.md',
              'brief/GLOSSARY.tsv', 'brief/SECTION-MAP.md', 'brief/一页纸.md',
              'reports/插件使用日志.md', 'reports/插件评估报告.md',
              'reports/校对报告.md', 'reports/工程日志.md', 'README.md'],
    '翻译源码': ['main.tex', 'preamble.tex', 'macros.tex', 'macros-extra.tex',
              'front.tex', 'body.tex', 'refs.tex', 'shards.json', 'figures_map.json'],
}
DIRS = {
    '工程文件/logs': 'logs',
    '翻译源码/skel': 'skel',
    '翻译源码/zh': 'zh',
    '翻译源码/figures': 'figures',
    '翻译源码/tools': 'tools',
    '翻译源码/brief': 'brief',
}
SRC_EXTRA = ['src_orig/glshortspare.defs']


def copytree(src, dst, exts=None):
    os.makedirs(dst, exist_ok=True)
    n = 0
    for name in sorted(os.listdir(src)):
        p = os.path.join(src, name)
        if not os.path.isfile(p):
            continue
        if exts and not any(name.endswith(e) for e in exts):
            continue
        shutil.copy2(p, os.path.join(dst, name))
        n += 1
    return n


def main():
    if os.path.exists(DEST):
        shutil.rmtree(DEST)
    os.makedirs(os.path.join(DEST, '成品'))

    # 成品
    for src, name in [
        (MAIN_PDF, 'KW06_电磁对偶与几何Langlands纲领_中译注本_%s.pdf' % VERSION),
        (GUIDE_PDF, 'KW06_思路导读_%s.pdf' % VERSION),
        (NOTES_PDF, 'KW06_译注汇编_%s.pdf' % VERSION),
    ]:
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(DEST, '成品', name))
        else:
            print('缺少成品：', src)

    for sub, files in FILES.items():
        dst = os.path.join(DEST, sub)
        os.makedirs(dst, exist_ok=True)
        for rel in files:
            src = os.path.join(ROOT, rel.replace('/', os.sep))
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(dst, os.path.basename(rel)))
            else:
                print('缺少文件：', rel)

    for dstrel, srcrel in DIRS.items():
        src = os.path.join(ROOT, srcrel)
        dst = os.path.join(DEST, dstrel)
        if not os.path.isdir(src):
            print('缺少目录：', srcrel)
            continue
        if srcrel in ('skel', 'zh'):
            n = copytree(src, dst, exts=['.tex'])
        elif srcrel == 'tools':
            n = copytree(src, dst, exts=['.py', '.md'])
        elif srcrel == 'figures':
            n = copytree(src, dst, exts=['.png'])
        elif srcrel == 'logs':
            n = copytree(src, dst, exts=['.md'])
        else:
            n = copytree(src, dst, exts=['.md', '.tsv'])
        print('%s: %d 个文件' % (dstrel, n))

    # 原始 defs（编号映射证据）
    os.makedirs(os.path.join(DEST, '翻译源码', 'src_orig'), exist_ok=True)
    for rel in SRC_EXTRA:
        src = os.path.join(ROOT, rel.replace('/', os.sep))
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(DEST, '翻译源码', 'src_orig', os.path.basename(rel)))

    # 译对 / 注疏 / 思路导读
    os.makedirs(os.path.join(DEST, '译对'), exist_ok=True)
    for rel, name in [('reports/verify_report.md', '结构核查_report.md'),
                      ('reports/check_zh_summary.md', 'check_zh_逐片编译.md'),
                      ('reports/公式保真核查.md', '公式逐字核查.md'),
                      ('reports/人工抽校.md', '人工抽校.md')]:
        src = os.path.join(ROOT, rel.replace('/', os.sep))
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(DEST, '译对', name))
        else:
            print('缺少文件：', rel)

    os.makedirs(os.path.join(DEST, '注疏'), exist_ok=True)
    for rel in ['注疏/译注汇编.md', '注疏/原文疑误表.md', '注疏/stats.json']:
        src = os.path.join(ROOT, rel.replace('/', os.sep))
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(DEST, '注疏', os.path.basename(rel)))
    os.makedirs(os.path.join(DEST, '思路导读'), exist_ok=True)
    src = os.path.join(ROOT, '思路导读', 'main.tex')
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(DEST, '思路导读', '思路导读.tex'))

    # 源码 zip
    zpath = os.path.join(DEST, '成品', 'KW06_翻译源码_%s.zip' % VERSION)
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
        for base in ['翻译源码', '工程文件']:
            for dp, _, fns in os.walk(os.path.join(DEST, base)):
                for fn in fns:
                    full = os.path.join(dp, fn)
                    rel = os.path.relpath(full, DEST)
                    z.write(full, rel)
    print('打包：', zpath, os.path.getsize(zpath), 'B')


if __name__ == '__main__':
    main()
