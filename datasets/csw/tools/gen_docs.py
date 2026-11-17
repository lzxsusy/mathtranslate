#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""从 cards/ 生成 taxonomy.md 与 MAP.md（避免手工维护表格与依赖图）。

用法（在 datasets/csw 下）：
    python tools/gen_docs.py
"""
import glob
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TRACKS = [
    ('O', '总览'),
    ('A', '三维理论：作用量、level、Wilson 线'),
    ('B', '相空间：约束、辛商、平坦联络模空间'),
    ('C', '几何量子化机器：预量子化、极化、全纯截面、半形式'),
    ('D', 'Wilson 线的穿刺点与 Borel–Weil–Bott'),
    ('E', 'WZW 一侧：仿射代数、Sugawara、共形块、KZ、融合'),
    ('F', '对偶与映射类群'),
    ('G', '计算：手术、S 矩阵、Verlinde、Jones'),
    ('H', '边界：CS/WZW 与 AdS₃/CFT₂ 的区别'),
]


def load():
    cards = []
    for p in sorted(glob.glob(os.path.join(ROOT, 'cards', '*', '*.json'))):
        with io.open(p, encoding='utf-8') as f:
            cards.append(json.load(f))
    return cards


def taxonomy(cards):
    out = ['# csw 卡片总表（taxonomy）', '',
           '按轨道（track）分组。“证明”列：complete = 卡内给出完整步骤；sketch = 给要点并标缺口。', '']
    for t, name in TRACKS:
        group = [c for c in cards if c['track'] == t]
        out.append('## %s · %s（%d 张）' % (t, name, len(group)))
        out.append('')
        out.append('| id | 标题 | 类型 | 说明 |')
        out.append('| --- | --- | --- | --- |')
        for c in sorted(group, key=lambda x: x['id']):
            out.append('| `%s` | %s | %s | %s |' % (
                c['id'], c['title'], 'concept' if c['type'] == 'concept' else 'example',
                c['summary'].replace('|', '\\|')))
        out.append('')
    out.append('## 例子卡（按依赖的概念排序）')
    out.append('')
    out.append('| id | 标题 | 依赖概念 |')
    out.append('| --- | --- | --- |')
    for c in sorted([c for c in cards if c['type'] == 'example'], key=lambda x: x['id']):
        refs = '、'.join('`%s`' % r.split('/')[-1] for r in c['concept_refs'])
        out.append('| `%s` | %s | %s |' % (c['id'], c['title'], refs))
    out.append('')
    return '\n'.join(out)


def map_md(cards):
    out = ['# csw 卡片依赖图（MAP）', '',
           '箭头 `A --> B` 表示“读 B 之前建议先读 A”（取 `related` 边）。同轨道内的边用实线，跨轨道用虚线。', '',
           '```mermaid', 'graph LR']
    by_id = {c['id']: c for c in cards}
    for c in cards:
        a = c['id'].split('/')[-1]
        for r in c.get('related', []):
            if r not in by_id:
                continue
            b = r.split('/')[-1]
            cross = c['track'] != by_id[r]['track']
            out.append('  %s %s %s' % (a, '-.->' if cross else '-->', b))
    out += ['```', '', '## 建议阅读顺序（按轨道）', '']
    for t, name in TRACKS:
        group = [c for c in cards if c['track'] == t]
        if not group:
            continue
        out.append('- **%s %s**：%s' % (t, name, ' → '.join('`%s`' % c['id'].split('/')[-1] for c in sorted(group, key=lambda x: x['id']))))
    out.append('')
    return '\n'.join(out)


def main():
    cards = load()
    with io.open(os.path.join(ROOT, 'taxonomy.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(taxonomy(cards))
    with io.open(os.path.join(ROOT, 'MAP.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(map_md(cards))
    print('wrote taxonomy.md (%d cards) and MAP.md' % len(cards))


if __name__ == '__main__':
    main()
