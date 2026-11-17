#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""csw 资料卡 lint：结构与内容约束检查。

用法（在 datasets/csw 下）：
    python tools/lint_csw.py [--quiet]
退出码 0 = 无错误；1 = 有错误。warning 不算失败。
"""
import glob
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TRACKS = {'O', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'}
CONCEPT_REQ = ['id', 'type', 'track', 'title', 'aliases', 'summary', 'question',
               'definition', 'key_points', 'formulas', 'theorems', 'pitfalls',
               'related', 'sources', 'rights', 'status']
EXAMPLE_REQ = ['id', 'type', 'track', 'title', 'summary', 'question', 'concept_refs',
               'setup', 'computation', 'result', 'check', 'pitfalls', 'related',
               'sources', 'rights', 'status']


def load():
    paths = sorted(glob.glob(os.path.join(ROOT, 'cards', 'concepts', '*.json'))) + \
        sorted(glob.glob(os.path.join(ROOT, 'cards', 'examples', '*.json')))
    out = []
    for p in paths:
        with io.open(p, encoding='utf-8') as f:
            out.append((p, json.load(f)))
    return out


def main():
    quiet = '--quiet' in sys.argv
    errors, warns = [], []
    cards = load()
    ids = {c['id'] for _, c in cards}

    for p, c in cards:
        rel = os.path.relpath(p, ROOT)
        req = CONCEPT_REQ if c.get('type') == 'concept' else EXAMPLE_REQ
        for k in req:
            if k not in c:
                errors.append('%s: 缺字段 %s' % (rel, k))
        if not str(c.get('id', '')).startswith('csw/' + c.get('type', '') + '/'):
            errors.append('%s: id 前缀不匹配 (%s)' % (rel, c.get('id')))
        if c.get('track') not in TRACKS:
            errors.append('%s: track 非法 (%s)' % (rel, c.get('track')))
        if c.get('rights') != 'rewritten':
            errors.append('%s: rights 必须 rewritten' % rel)
        if c.get('status') not in ('draft', 'reviewed', 'published'):
            errors.append('%s: status 非法' % rel)
        lim = 120 if c.get('type') == 'concept' else 100
        if len(c.get('summary', '')) > lim:
            warns.append('%s: summary 超 %d 字 (%d)' % (rel, lim, len(c['summary'])))
        if c.get('type') == 'concept':
            if len(c.get('key_points', [])) < 3:
                errors.append('%s: key_points < 3' % rel)
            if not c.get('formulas'):
                errors.append('%s: formulas 为空' % rel)
            if len(c.get('pitfalls', [])) < 1:
                errors.append('%s: pitfalls 为空' % rel)
            for t in c.get('theorems', []):
                pr = t.get('proof', {})
                if pr.get('status') not in ('complete', 'sketch'):
                    errors.append('%s: theorem proof.status 非法' % rel)
                if pr.get('status') == 'sketch' and not pr.get('gap_note'):
                    warns.append('%s: sketch 证明缺 gap_note' % rel)
                for st in pr.get('steps', []):
                    if set(st) != {'no', 'text', 'why'}:
                        errors.append('%s: 证明步骤字段应为 no/text/why' % rel)
        else:
            if len(c.get('computation', [])) < 2:
                errors.append('%s: computation < 2 步' % rel)
            for st in c.get('computation', []):
                if set(st) != {'no', 'text', 'why'}:
                    errors.append('%s: computation 步字段应为 no/text/why' % rel)
            for r in c.get('concept_refs', []):
                if r not in ids:
                    errors.append('%s: concept_refs 指向不存在 %s' % (rel, r))
        if len(c.get('related', [])) < 2:
            errors.append('%s: related < 2' % rel)
        for r in c.get('related', []):
            if r not in ids:
                errors.append('%s: related 指向不存在 %s' % (rel, r))
        if not c.get('sources'):
            errors.append('%s: sources 为空' % rel)
        for s in c.get('sources', []):
            for k in ('book', 'section', 'pages', 'pdf_pages', 'anchor'):
                if k not in s:
                    errors.append('%s: source 缺 %s' % (rel, k))
            if isinstance(s.get('pages'), list) and isinstance(s.get('pdf_pages'), list):
                if len(s['pages']) != len(s['pdf_pages']):
                    errors.append('%s: pages/pdf_pages 长度不一致' % rel)

    if not quiet:
        for e in errors:
            print('ERROR ' + e)
        for w in warns:
            print('WARN  ' + w)
    print('cards=%d errors=%d warnings=%d' % (len(cards), len(errors), len(warns)))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
