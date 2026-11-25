#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""benzvi_glc 资料卡 lint：结构、内容与核验状态检查。

用法（在 datasets/benzvi_glc 下）：
    python tools/lint_benzvi.py [--quiet]
退出码 0 = 无错误；1 = 有错误。warning 不算失败。
"""
import glob
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TRACKS = {'O', 'A', 'B', 'C', 'D', 'E'}
CONCEPT_REQ = ['id', 'type', 'track', 'title', 'aliases', 'summary', 'question',
               'definition', 'key_points', 'formulas', 'theorems', 'pitfalls',
               'related', 'sources', 'rights', 'status']


def load():
    paths = sorted(glob.glob(os.path.join(ROOT, 'cards', 'concepts', '*.json')))
    out = []
    for p in paths:
        with io.open(p, encoding='utf-8') as f:
            out.append((p, json.load(f)))
    return out


def load_verification():
    p = os.path.join(ROOT, 'verification.jsonl')
    out = {}
    if not os.path.exists(p):
        return out
    with io.open(p, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                rec = json.loads(line)
                out[rec['id']] = rec
    return out


def main():
    quiet = '--quiet' in sys.argv
    errors, warns = [], []
    cards = load()
    ids = {c['id'] for _, c in cards}
    ver = load_verification()

    for p, c in cards:
        rel = os.path.relpath(p, ROOT)
        for k in CONCEPT_REQ:
            if k not in c:
                errors.append('%s: 缺字段 %s' % (rel, k))
        if not str(c.get('id', '')).startswith('bzg/concept/'):
            errors.append('%s: id 前缀不匹配 (%s)' % (rel, c.get('id')))
        if c.get('track') not in TRACKS:
            errors.append('%s: track 非法 (%s)' % (rel, c.get('track')))
        if c.get('rights') != 'rewritten':
            errors.append('%s: rights 必须 rewritten' % rel)
        if c.get('status') not in ('draft', 'reviewed', 'published'):
            errors.append('%s: status 非法' % rel)
        if len(c.get('summary', '')) > 120:
            warns.append('%s: summary 超 120 字 (%d)' % (rel, len(c['summary'])))
        if not str(c.get('question', '')).rstrip().endswith('？'):
            warns.append('%s: question 未以全角问号结尾' % rel)
        if len(c.get('key_points', [])) < 3:
            errors.append('%s: key_points < 3' % rel)
        if len(c.get('formulas', [])) < 1:
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
            if not t.get('source'):
                errors.append('%s: theorem 缺 source' % rel)
        if len(c.get('related', [])) < 2:
            errors.append('%s: related < 2' % rel)
        for r in c.get('related', []):
            if r not in ids:
                errors.append('%s: related 指向不存在 %s' % (rel, r))
            if r == c.get('id'):
                errors.append('%s: related 指向自身' % rel)
        if not c.get('sources'):
            errors.append('%s: sources 为空' % rel)
        for s in c.get('sources', []):
            for k in ('book', 'section', 'pages', 'pdf_pages', 'anchor'):
                if k not in s:
                    errors.append('%s: source 缺 %s' % (rel, k))
            if isinstance(s.get('pages'), list) and isinstance(s.get('pdf_pages'), list):
                if len(s['pages']) != len(s['pdf_pages']):
                    errors.append('%s: pages/pdf_pages 长度不一致' % rel)
        v = c.get('verification') or ver.get(c.get('id'))
        if c.get('status') == 'published':
            if not v:
                errors.append('%s: published 但无 verification' % rel)
            elif v.get('status') == 'rejected':
                errors.append('%s: published 但核验为 rejected' % rel)
            elif v.get('status') == 'source-only':
                errors.append('%s: published 但仅有讲义依据（source-only）' % rel)
        if v and v.get('status') not in ('external-confirmed', 'source-only', 'rejected'):
            errors.append('%s: verification.status 非法 (%s)' % (rel, v.get('status')))

    if not quiet:
        for e in errors:
            print('ERROR ' + e)
        for w in warns:
            print('WARN  ' + w)
    print('cards=%d errors=%d warnings=%d' % (len(cards), len(errors), len(warns)))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
