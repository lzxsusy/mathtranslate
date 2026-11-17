#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把 cards/*.json 渲染成人类可读的 markdown（md/concepts、md/examples）。

用法（在 datasets/csw 下）：
    python tools/render_md.py
"""
import glob
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TITLE = 'Chern–Simons 理论与共形场论资料卡'


def render(c):
    out = []
    out.append('---')
    out.append('id: %s' % c['id'])
    out.append('type: %s' % c['type'])
    out.append('track: %s' % c['track'])
    out.append('---')
    out.append('')
    out.append('# %s' % c['title'])
    out.append('')
    out.append('> %s' % c['summary'])
    out.append('')
    out.append('**问题**：%s' % c['question'])
    out.append('')
    if c['type'] == 'concept':
        d = c['definition']
        out.append('## 定义')
        out.append('')
        out.append(d['text'])
        out.append('')
        out.append('*记号*：%s' % d['notation'])
        out.append('')
        out.append('## 要点')
        out.append('')
        for k in c['key_points']:
            out.append('- ' + k)
        out.append('')
        if c.get('formulas'):
            out.append('## 关键公式')
            out.append('')
            for f in c['formulas']:
                out.append('- $%s$' % f if not f.startswith('$') else '- %s' % f)
            out.append('')
        for t in c.get('theorems', []):
            out.append('## %s' % t['name'])
            out.append('')
            out.append(t['statement'])
            out.append('')
            pr = t['proof']
            if pr['status'] == 'complete':
                out.append('**证明**：')
                out.append('')
                for st in pr['steps']:
                    out.append('%d. %s *（%s）*' % (st['no'], st['text'], st['why']))
            else:
                out.append('**证明要点**（sketch）：')
                out.append('')
                for st in pr['steps']:
                    out.append('%d. %s *（%s）*' % (st['no'], st['text'], st['why']))
                if pr.get('gap_note'):
                    out.append('')
                    out.append('> **缺口**：%s' % pr['gap_note'])
            out.append('')
    else:
        out.append('## 设定')
        out.append('')
        out.append(c['setup'])
        out.append('')
        out.append('## 计算')
        out.append('')
        for st in c['computation']:
            out.append('%d. %s *（%s）*' % (st['no'], st['text'], st['why']))
        out.append('')
        out.append('## 结果')
        out.append('')
        out.append(c['result'])
        out.append('')
        out.append('## 核对')
        out.append('')
        out.append(c['check'])
        out.append('')
    out.append('## 陷阱')
    out.append('')
    for p in c['pitfalls']:
        out.append('- ' + p)
    out.append('')
    out.append('## 相关卡片')
    out.append('')
    for r in c['related']:
        slug = r.split('/')[-1]
        kind = 'concepts' if '/concept/' in r else 'examples'
        out.append('- [%s](../%s/%s.md)' % (slug, kind, slug))
    out.append('')
    out.append('## 来源')
    out.append('')
    for s in c['sources']:
        out.append('- %s，%s，印刷页 %s / PDF 页 %s（%s）' % (
            s['book'], s['section'], s['pages'], s['pdf_pages'], s['anchor']))
    out.append('')
    out.append('---')
    out.append('*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*')
    out.append('')
    return '\n'.join(out)


def main():
    n = 0
    for p in sorted(glob.glob(os.path.join(ROOT, 'cards', '*', '*.json'))):
        with io.open(p, encoding='utf-8') as f:
            c = json.load(f)
        kind = 'concepts' if c['type'] == 'concept' else 'examples'
        outdir = os.path.join(ROOT, 'md', kind)
        os.makedirs(outdir, exist_ok=True)
        slug = c['id'].split('/')[-1]
        with io.open(os.path.join(outdir, slug + '.md'), 'w', encoding='utf-8', newline='\n') as f:
            f.write(render(c))
        n += 1
    print('rendered %d md files' % n)


if __name__ == '__main__':
    main()
