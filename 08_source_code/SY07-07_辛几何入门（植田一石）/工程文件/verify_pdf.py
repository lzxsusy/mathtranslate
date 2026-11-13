# -*- coding: utf-8 -*-
"""Gate 2：成品 PDF 结构与内容校验（页数 / 书签 / 公式号 / 插图 / 字体嵌入 / 缺字）。
用法：python verify_pdf.py [pdf 路径]  → 全部通过退出码 0。
"""
import io, os, re, sys, glob, collections
import pymupdf

ROOT = os.path.dirname(os.path.abspath(__file__))
CH = os.path.join(ROOT, 'src', 'chunks')
PDF = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    ROOT, 'deliverable', '辛几何入门_中文译注本.pdf')

EXPECT_PAGES = 224
EXPECT_BOOKMARKS = 125
EXPECT_FIGS = {  # 插图所在页（印刷页序）
    'fig2.1': 17, 'fig2.2': 18, 'fig2.3': 23, 'fig2.4': 30, 'fig9.1': 147,
}
EXPECT_CHAPTERS = ['译校说明', '前言', '第1章', '第2章', '第3章', '第4章', '第5章',
                   '第6章', '第7章', '第8章', '第9章', '第10章', '后记',
                   '附录 A', '附录 B', '参考文献']


def collect_tags():
    tags = []
    for p in sorted(glob.glob(os.path.join(CH, '*.tex'))):
        t = io.open(p, encoding='utf-8-sig').read()
        tags += re.findall(r'<本地路径>]*)\}', t)
    return tags


def main():
    problems = []
    if not os.path.exists(PDF):
        print('PDF 不存在:', PDF)
        return 1
    doc = pymupdf.open(PDF)
    text = [doc[i].get_text() for i in range(doc.page_count)]

    if doc.page_count != EXPECT_PAGES:
        problems.append(f'页数 {doc.page_count} != {EXPECT_PAGES}')
    toc = doc.get_toc()
    if len(toc) != EXPECT_BOOKMARKS:
        problems.append(f'书签 {len(toc)} != {EXPECT_BOOKMARKS}')
    top = [t[1] for t in toc if t[0] == 1]
    for kw in EXPECT_CHAPTERS:
        if not any(kw in s for s in top):
            problems.append(f'书签缺章：{kw}')

    # 公式号：每个源码 \tag 的编号应作为（N）出现在正文
    tags = collect_tags()
    flat = ''.join(t.replace('\n', '') for t in text)
    missing = []
    for tg in tags:
        tg = tg.strip()
        if not tg:
            continue
        if f'({tg})' not in flat:
            missing.append(tg)
    if missing:
        problems.append(f'{len(missing)} 个公式号未出现在 PDF：{missing[:8]}')

    # 插图：每张图所在页应含内嵌位图
    for key, pg in EXPECT_FIGS.items():
        if pg < 1 or pg > doc.page_count or not doc[pg - 1].get_images():
            problems.append(f'{key} 应在第 {pg} 页且含位图')

    # 字体全部嵌入、无 Type3
    pages_fonts = collections.Counter()
    for i in range(doc.page_count):
        for f in doc[i].get_fonts():
            pages_fonts[(f[3], f[4])] += 1
    bad_fonts = [k for k in pages_fonts if 'Type3' in k[1] or not k[1]]
    if bad_fonts:
        problems.append(f'未嵌入或 Type3 字体：{bad_fonts[:4]}')

    # 缺字 / 未定义引用痕迹
    if any('Missing character' in t for t in text):
        problems.append('PDF 内出现 Missing character 文本')
    if '??' in flat:
        problems.append('出现未定义引用 "??"')

    print(f'pages={doc.page_count}  bookmarks={len(toc)}  tags={len(tags)}/{len(tags) - len(missing)} present')
    print(f'figures={len(EXPECT_FIGS)}  fonts={len(pages_fonts)}  bytes={os.path.getsize(PDF)}')
    for kw in EXPECT_CHAPTERS:
        print(f'  chapter {kw}: OK' if any(kw in s for s in top) else f'  chapter {kw}: MISSING')
    if problems:
        print('PROBLEMS:')
        for s in problems:
            print('  -', s)
        print('STATUS: FAIL')
        return 1
    print('STATUS: OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())
