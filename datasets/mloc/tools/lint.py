#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mloc 资料卡 lint：结构、内容、页码对齐与核验状态检查。

用法（在 datasets/mloc 下）：
    python tools/lint.py [--quiet]
退出码 0 = 无错误；1 = 有错误。warning 不算失败。
"""
import glob
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PREFIX = 'mloc/'
PAGE_DELTA = 4          # 印刷页 = PDF 页 − 4
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


def as_list(x):
    return x if isinstance(x, list) else [x]


def main():
    quiet = '--quiet' in sys.argv
    errors, warns = [], []
    cards = load()
    ids = {c['id'] for _, c in cards}
    ver = load_verification()

    def strings(o):
        if isinstance(o, str):
            yield o
        elif isinstance(o, dict):
            for v in o.values():
                yield from strings(v)
        elif isinstance(o, list):
            for v in o:
                yield from strings(v)

    for p, c in cards:
        rel = os.path.relpath(p, ROOT)
        typ = c.get('type')
        # JSON 里若把 LaTeX 宏写成单个反斜杠（\rho、\right、\n 等），
        # 解析后字符串会带控制字符：这类损坏必须挡住。
        for s in strings(c):
            for ch in s:
                if ord(ch) < 32 and ch not in '\n\t':
                    errors.append('%s: 字符串含控制字符 %s（LaTeX 宏漏了转义）'
                                  % (rel, hex(ord(ch))))
                    break
            else:
                continue
            break
        req = CONCEPT_REQ if typ == 'concept' else EXAMPLE_REQ
        for k in req:
            if k not in c:
                errors.append('%s: 缺字段 %s' % (rel, k))
        if not str(c.get('id', '')).startswith(PREFIX + str(typ) + '/'):
            errors.append('%s: id 前缀不匹配 (%s)' % (rel, c.get('id')))
        if c.get('track') not in TRACKS:
            errors.append('%s: track 非法 (%s)' % (rel, c.get('track')))
        if c.get('rights') != 'rewritten':
            errors.append('%s: rights 必须 rewritten' % rel)
        if c.get('status') not in ('draft', 'reviewed', 'published'):
            errors.append('%s: status 非法' % rel)
        lim = 120 if typ == 'concept' else 100
        if len(c.get('summary', '')) > lim:
            warns.append('%s: summary 超 %d 字 (%d)' % (rel, lim, len(c['summary'])))
        if not str(c.get('question', '')).rstrip().endswith(('？', '?')):
            warns.append('%s: question 未以问号结尾' % rel)
        if typ == 'concept':
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
        else:
            if len(c.get('computation', [])) < 2:
                errors.append('%s: computation < 2 步' % rel)
            for st in c.get('computation', []):
                if set(st) != {'no', 'text', 'why'}:
                    errors.append('%s: computation 步字段应为 no/text/why' % rel)
            for r in c.get('concept_refs', []):
                if r.startswith(PREFIX) and r not in ids:
                    errors.append('%s: concept_refs 指向不存在 %s' % (rel, r))
        if len(c.get('related', [])) < 2:
            errors.append('%s: related < 2' % rel)
        for r in c.get('related', []):
            if r.startswith(PREFIX) and r not in ids:
                errors.append('%s: related 指向不存在 %s' % (rel, r))
            if r == c.get('id'):
                errors.append('%s: related 指向自身' % rel)
        if not c.get('sources'):
            errors.append('%s: sources 为空' % rel)
        for s in c.get('sources', []):
            for k in ('book', 'section', 'pages', 'pdf_pages', 'anchor'):
                if k not in s:
                    errors.append('%s: source 缺 %s' % (rel, k))
            ps, qs = as_list(s.get('pages')), as_list(s.get('pdf_pages'))
            if len(ps) != len(qs):
                errors.append('%s: pages/pdf_pages 长度不一致' % rel)
            for a, b in zip(ps, qs):
                if isinstance(a, int) and isinstance(b, int) and b - a != PAGE_DELTA:
                    errors.append('%s: pages/pdf_pages 差不是 %d (%s/%s)' % (rel, PAGE_DELTA, a, b))
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
