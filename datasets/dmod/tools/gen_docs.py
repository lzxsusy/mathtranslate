#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""cards/ → taxonomy.md（分轨总表，追加在人工正文之后）与 MAP.md（依赖图）。

用法（在 datasets/dmod 下）：
    python tools/gen_docs.py

taxonomy.md 的手写正文（§1–§5）保持不变，本脚本只重写 `## 6. 卡片清单` 之后的部分。
"""
import glob
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TRACKS = [
    ('O', '预备：交换代数与维数'),
    ('A', '算子环与 $D(n)$-模'),
    ('B', '特征簇与完整模'),
    ('C', '$\\mathcal{D}_X$-模层'),
    ('D', '直像与逆像（六种运算）'),
    ('E', 'Bernstein 不等式与 Kashiwara'),
    ('F', '局部上同调与基变换'),
    ('G', '分类与联络'),
    ('H', '例子与计算'),
]
MARK = '## 6. 卡片清单'


def load():
    cards = []
    for p in sorted(glob.glob(os.path.join(ROOT, 'cards', '*', '*.json'))):
        with io.open(p, encoding='utf-8') as f:
            cards.append(json.load(f))
    return cards


def first_page(c):
    p = c['sources'][0]['pages']
    return p[0] if isinstance(p, list) else p


def table(cards):
    o = [MARK, '',
         '由 `tools/gen_docs.py` 生成，勿手改。“核验”列：E = 外部权威已核；S = 仅讲义依据（`source-only`）。', '']
    for t, name in TRACKS:
        group = [c for c in cards if c['track'] == t]
        if not group:
            continue
        o += ['### %s · %s（%d 张）' % (t, name, len(group)), '',
              '| 卡 | 标题 | 原书条目 | 页 | 核验 |', '| --- | --- | --- | --- | --- |']
        for c in group:
            v = (c.get('verification') or {}).get('status', '')
            mark = {'external-confirmed': 'E', 'source-only': 'S'}.get(v, '—')
            o.append('| `%s` | %s | %s | p.%s | %s |' % (
                c['id'], c['title'], c['sources'][0]['section'], first_page(c), mark))
        o.append('')
    return '\n'.join(o).rstrip() + '\n'


def map_md(cards):
    ids = {c['id'] for c in cards}
    track = {c['id']: c['track'] for c in cards}
    short = {c['id']: c['id'].split('/')[-1] for c in cards}
    o = ['# dmod 卡片依赖图（MAP）', '',
         '边 = `related`（A → B 读作「A 的卡引用 B」）；只画同轨或相邻轨的边，避免线团。', '',
         '```mermaid', 'graph LR']
    for c in cards:
        for r in c.get('related', []):
            if r in ids and r != c['id']:
                if track[r] == c['track'] or abs(ord(track[r]) - ord(c['track'])) == 1:
                    o.append('  %s[%s] --> %s[%s]' % (short[c['id']], short[c['id']], short[r], short[r]))
    o += ['```', '', '## 全图（含跨轨）', '', '| 卡 | 指向 |', '| --- | --- |']
    for c in cards:
        tgt = [short.get(r, r) for r in c.get('related', []) if r in ids and r != c['id']]
        if tgt:
            o.append('| `%s` | %s |' % (short[c['id']], '、'.join(tgt)))
    return '\n'.join(o).rstrip() + '\n'


def main():
    cards = load()
    p = os.path.join(ROOT, 'taxonomy.md')
    head = ''
    if os.path.exists(p):
        old = io.open(p, encoding='utf-8').read()
        head = old.split(MARK)[0]
    if not head.strip():
        head = '# D-模资料卡分类体系（dmod taxonomy v1）\n\n'
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(head.rstrip() + '\n\n' + table(cards))
    with io.open(os.path.join(ROOT, 'MAP.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(map_md(cards))
    print('taxonomy.md / MAP.md: %d cards' % len(cards))


if __name__ == '__main__':
    main()
