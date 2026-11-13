# -*- coding: utf-8 -*-
"""Gate3：回读成品 PDF，检查书签、关键文字、字体嵌入、编号覆盖。

用法: python tools\\gate3.py [--pdf src\\main.pdf]
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROBES = [
    '总导引', '流形', '纤维丛', '基础同伦论', '微分形式', '同调', '示性类',
    'Chern', '分类空间', '费米子', 'K 理论', '配边', '广义', '参考文献', '术语对照表',
    '定义 2.1', '定理 2.5', '例 2.19', '图 2.1', '表 9', '本节重点', '本章回顾与评注',
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pdf', default=os.path.join('src', 'main.pdf'))
    args = ap.parse_args()
    pdf = os.path.join(ROOT, args.pdf)
    import pymupdf

    doc = pymupdf.open(pdf)
    pages = doc.page_count
    toc = doc.get_toc()
    level1 = [t for t in toc if t[0] == 1]
    print('pages=%d  toc=%d  level1=%d' % (pages, len(toc), len(level1)))
    for lvl, title, page in level1:
        print('  L1 %-28s p.%d' % (title, page))

    text = []
    for i in range(pages):
        text.append(doc[i].get_text())
    whole = '\n'.join(text)
    # PDF 抽文本会在 CJK/拉丁之间插空格，探针一律去空白后比对
    flat = re.sub(r'\s+', '', whole)

    print('\n关键文字：')
    miss = []
    for p in PROBES:
        ok = re.sub(r'\s+', '', p) in flat
        if not ok:
            miss.append(p)
        print('  %-12s %s' % (p, 'OK' if ok else 'MISSING'))
    if miss:
        print('  缺失: %s' % '、'.join(miss))

    # 公式编号覆盖率：统计 chNN.tex 里的 \tag，逐个在 PDF 文本中找
    chunks = sorted(f for f in os.listdir(os.path.join(ROOT, 'src', 'chunks')) if f.endswith('.tex'))
    tags = []
    for f in chunks:
        src = open(os.path.join(ROOT, 'src', 'chunks', f), encoding='utf-8').read()
        tags += re.findall(r'<本地路径>]+\.[0-9]+)\}', src)
    absent = [t for t in tags if ('(%s)' % t) not in flat]
    print('\n编号公式：源码 %d 条，PDF 文本中缺 %d 条' % (len(tags), len(absent)))
    if absent:
        print('  缺失: %s' % ', '.join(absent[:30]))

    # 字体嵌入
    print('\n字体（前 12 个）：')
    fonts = set()
    for i in range(min(pages, 40)):
        for f in doc[i].get_fonts():
            fonts.add((f[3], f[1]))
    for name, typ in sorted(fonts)[:12]:
        print('  %-40s %s' % (name, typ))
    print('  共 %d 种字体' % len(fonts))

    # 图片数量
    n_img = sum(len(doc[i].get_images()) for i in range(pages))
    print('\n嵌入图片对象合计 %d 个（每页最多数个，含重复引用）' % n_img)
    return 0


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main())
