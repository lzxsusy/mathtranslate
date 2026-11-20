# -*- coding: utf-8 -*-
"""页面口径核对（宽松版，只查硬错）。

硬查：sources.pdf_pages 必须等于 pages + 1（PDF 页 = 印刷页 + 1）。
参考：打印 anchor 起始行最近的页锚注释（200 行内）对应的印刷页，便于人工比对，
      不作失败判定——一个 anchor 区间常跨多页，而页锚注释只标在节首。
"""
import glob
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(ROOT))
ANCHOR_RE = re.compile(r'^08_source_code/([^/]+)/源码/(.+?):(\d+)-(\d+)$')
PAGE_RE = re.compile(r'%%\s*====\s*原文\s*(?:§[\dA-Z.]+|Appendix [AB])：PDF 第 (\d+) 页（印刷第 (\d+) 页）')


def main():
    hard = 0
    for p in sorted(glob.glob(os.path.join(ROOT, 'cards', '*', '*.json'))):
        with io.open(p, encoding='utf-8') as f:
            c = json.load(f)
        for s in c.get('sources') or []:
            pages = s.get('pages') or []
            pdf = s.get('pdf_pages') or []
            if pages and pdf != [x + 1 for x in pages]:
                print('ERR %s: pdf_pages=%s 不等于 pages+1' % (c['id'], pdf))
                hard += 1
            m = ANCHOR_RE.match(s.get('anchor', ''))
            if not m:
                print('ERR %s: anchor 格式不对' % c['id'])
                hard += 1
                continue
            fp = os.path.join(REPO, '08_source_code', m.group(1), '源码',
                              m.group(2).replace('/', os.sep))
            if not os.path.exists(fp):
                print('ERR %s: 找不到 %s' % (c['id'], m.group(2)))
                hard += 1
                continue
            a = int(m.group(3))
            lines = io.open(fp, encoding='utf-8').read().splitlines()
            if int(m.group(4)) > len(lines):
                print('ERR %s: anchor 行号超出文件（%s 行）' % (c['id'], len(lines)))
                hard += 1
                continue
            marks = [(i, int(mm.group(2))) for i, ln in enumerate(lines, 1)
                     for mm in [PAGE_RE.search(ln)] if mm]
            near = [(abs(i - a), pg) for i, pg in marks if abs(i - a) <= 200]
            if near and pages:
                pg = min(near)[1]
                flag = '' if abs(pg - pages[0]) <= 2 else '  <-- 相差 >2，请人工看'
                print('INFO %-46s 卡 %s  最近页锚 印刷 %d%s' % (c['id'], pages, pg, flag))
    print('pages check finished, hard issues: %d' % hard)
    return 1 if hard else 0


if __name__ == '__main__':
    sys.exit(main())
