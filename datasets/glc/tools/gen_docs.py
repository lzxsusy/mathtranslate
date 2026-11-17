#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""cards/ → taxonomy.md（分轨总表）与 MAP.md（依赖图）。

用法（在 datasets/glc 下）：
    python tools/gen_docs.py
"""
import glob
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TRACKS = [
    ('O', '总览：几何 Langlands 的纲领'),
    ('A', '整体类域论与 Abel 侧'),
    ('B', 'Hecke 特征层、几何 Satake、Bun_G'),
    ('C', 'Whittaker 模型与 Laumon 层'),
    ('D', 'Fourier 变换、消失定理与洁净性'),
    ('E', '因子化、Ran 空间与 Aut_E'),
    ('F', '消失猜想、范畴猜想、Shv_Nilp'),
    ('G', '谱侧：QCoh、受限变体、Hitchin'),
    ('H', '局部等价、证明架构与整体定理'),
]


def load():
    cards = []
    for p in sorted(glob.glob(os.path.join(ROOT, 'cards', '*', '*.json'))):
        with io.open(p, encoding='utf-8') as f:
            cards.append(json.load(f))
    return cards


def first_page(c):
    s = c['sources'][0]
    p = s['pages']
    return p[0] if isinstance(p, list) else p


def taxonomy(cards):
    o = ['# glc 卡片总表（taxonomy）', '',
         '按轨道（track）分组。“核验”列：E = 外部权威已核；S = 仅讲义依据（`source-only`）；— = 待核。', '']
    for t, name in TRACKS:
        group = [c for c in cards if c['track'] == t]
        if not group:
            continue
        o += ['## %s · %s（%d 张）' % (t, name, len(group)), '',
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
    o = ['# glc 卡片依赖图（MAP）', '',
         '边 = `related`（A → B 读作「A 的卡引用 B」）。只画同轨或相邻轨的边，避免线团。', '', '```mermaid', 'graph LR']
    short = {}
    for c in cards:
        short[c['id']] = c['id'].split('/')[-1]
    for c in cards:
        for r in c.get('related', []):
            if r in ids and r != c['id']:
                same = r.split('/')[1] == c['id'].split('/')[1]
                if same or c['track'] == next(x['track'] for x in cards if x['id'] == r):
                    o.append('  %s[%s] --> %s[%s]' % (
                        short[c['id']], short[c['id']], short[r], short[r]))
    o += ['```', '']
    return '\n'.join(o)


def main():
    cards = load()
    with io.open(os.path.join(ROOT, 'taxonomy.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(taxonomy(cards))
    with io.open(os.path.join(ROOT, 'MAP.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(map_md(cards))
    print('taxonomy.md / MAP.md: %d cards' % len(cards))


if __name__ == '__main__':
    main()
