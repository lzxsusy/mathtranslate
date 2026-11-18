#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""cards/*.json → md/concepts、md/examples（给人读的渲染版）。

用法（在 datasets/dmod 下）：
    python tools/render_md.py
"""
import glob
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def fmt_formula(f):
    f = f.strip()
    if f.startswith('$$') or f.startswith('$'):
        return '- ' + f
    return '- $%s$' % f


def render(c):
    o = ['---', 'id: %s' % c['id'], 'type: %s' % c['type'], 'track: %s' % c['track'], '---', '']
    o += ['# %s' % c['title'], '', '> %s' % c['summary'], '',
          '**问题**：%s' % c['question'], '']
    if c['type'] == 'concept':
        o += ['## 定义', '', c['definition']['text'], '',
              '*记号*：%s' % c['definition']['notation'], '', '## 要点', '']
        o += ['- ' + k for k in c['key_points']]
        o += ['', '## 关键公式', ''] + [fmt_formula(f) for f in c['formulas']]
        if c.get('theorems'):
            o += ['', '## 定理与证明', '']
            for t in c['theorems']:
                pr = t['proof']
                tag = {'complete': '完整', 'sketch': '要点（有缺口）'}.get(pr['status'], pr['status'])
                o += ['### %s（%s）' % (t['name'], tag), '', t['statement'], '']
                for st in pr.get('steps', []):
                    o += ['%d. %s  ' % (st['no'], st['text']),
                          '   *为什么*：%s' % st['why']]
                if pr.get('gap_note'):
                    o += ['', '> 缺口：%s' % pr['gap_note']]
                o += ['', '*出处*：%s' % t['source'], '']
    else:
        o += ['## 设定', '', c['setup'], '', '## 计算', '']
        for st in c['computation']:
            o += ['%d. %s  ' % (st['no'], st['text']), '   *为什么*：%s' % st['why']]
        o += ['', '## 结果', '', c['result'], '', '## 核对', '', c['check'], '',
              '**相关概念卡**：' + '、'.join(c['concept_refs'])]
    o += ['', '## 易错点', ''] + ['- ' + p for p in c['pitfalls']]
    o += ['', '## 出处', '']
    for s in c['sources']:
        o += ['- %s，%s，p.%s（PDF p.%s），`%s`' % (
            s['book'], s['section'],
            '-'.join(str(x) for x in (s['pages'] if isinstance(s['pages'], list) else [s['pages']])),
            '-'.join(str(x) for x in (s['pdf_pages'] if isinstance(s['pdf_pages'], list) else [s['pdf_pages']])),
            s['anchor'])]
    v = c.get('verification')
    if v:
        o += ['', '## 核验', '', '状态：`%s`（%s）' % (v['status'], v.get('checked_on', ''))]
        for ck in v.get('checks', []):
            o += ['- %s：%s — %s' % (ck.get('source'), ck.get('url'), ck.get('asserts'))]
    o += ['', '## 关联', ''] + ['- `%s`' % r for r in c['related']]
    return '\n'.join(o).rstrip() + '\n'


def main():
    n = 0
    for kind, sub in (('concept', 'concepts'), ('example', 'examples')):
        outdir = os.path.join(ROOT, 'md', sub)
        os.makedirs(outdir, exist_ok=True)
        for p in sorted(glob.glob(os.path.join(ROOT, 'cards', sub, '*.json'))):
            with io.open(p, encoding='utf-8') as f:
                c = json.load(f)
            with io.open(os.path.join(outdir, os.path.basename(p)[:-5] + '.md'),
                         'w', encoding='utf-8', newline='\n') as f:
                f.write(render(c))
            n += 1
    print('rendered %d cards' % n)


if __name__ == '__main__':
    main()
