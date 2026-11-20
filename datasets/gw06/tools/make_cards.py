# -*- coding: utf-8 -*-
"""生成并校验 gw06 资料卡：JSON → index.jsonl / verification.jsonl / md / MAP.md / taxonomy.md。

用法：
    python tools/make_cards.py            # 校验 + 写文件
    python tools/make_cards.py --check    # 只校验（CI 用，0 表示通过）
    python tools/make_cards.py --strict   # 把 WARN 也当失败

卡片是手写的 JSON，放在 cards/concepts/*.json 与 cards/corrections/*.json；
本脚本是唯一的生成入口，不要手改 index.jsonl / md/ / MAP.md / taxonomy.md。
"""
import glob
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                       # datasets/gw06
REPO = os.path.dirname(os.path.dirname(ROOT))      # 仓库根
SRC_PREFIX = '08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/'
BOOK = ('S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric '
        'Langlands Program（arXiv:hep-th/0612073v2）中译校订本')
ANN_TYPES = {'易错预警', '含糊点拨', '背景直觉'}
STATUSES = {'draft', 'reviewed', 'published'}
VERIF = {'external-confirmed', 'source-only', 'rejected'}
TRACK = re.compile(r'^(§[1-6](\.[0-9]+)?|附录[AB])$')
ANCHOR = re.compile(r'^(.*?):(\d+)-(\d+)$')

errors = []
warnings = []


def err(cid, msg):
    errors.append('[%s] %s' % (cid, msg))


def warn(cid, msg):
    warnings.append('[%s] %s' % (cid, msg))


def cjk_len(s):
    """汉字数（剔除 $...$ 数学与英文）。"""
    s = re.sub(r'\$[^$]*\$', '　', s)
    return sum(1 for ch in s if '\u4e00' <= ch <= '\u9fff')


def load():
    cards = []
    for sub in ('concepts', 'corrections'):
        for f in sorted(glob.glob(os.path.join(ROOT, 'cards', sub, '*.json'))):
            with io.open(f, encoding='utf-8') as fh:
                cards.append(json.load(fh))
    return cards


def check_anchor(cid, anchor):
    m = ANCHOR.match(anchor)
    if not m:
        err(cid, 'anchor 格式应为 path:a-b：%s' % anchor)
        return None
    path, a, b = m.group(1), int(m.group(2)), int(m.group(3))
    if not path.startswith(SRC_PREFIX):
        err(cid, 'anchor 必须指向 %s…：%s' % (SRC_PREFIX, path))
    full = os.path.join(REPO, path)
    if not os.path.exists(full):
        err(cid, 'anchor 文件不存在：%s' % path)
        return None
    with io.open(full, encoding='utf-8') as fh:
        n = sum(1 for _ in fh)
    if not (1 <= a <= b <= n):
        err(cid, 'anchor 行号越界：%d-%d（文件 %d 行）' % (a, b, n))
        return None
    return os.path.join(REPO, path), a, b


def validate(cards, allow_missing_related=False):
    ids = [c['id'] for c in cards]
    if len(ids) != len(set(ids)):
        dup = sorted({x for x in ids if ids.count(x) > 1})
        err('-', 'id 重复：%s' % ','.join(dup))
    idset = set(ids)
    for c in cards:
        cid = c['id']
        slug = cid.split('/')[-1]
        typ = c.get('type')
        if typ not in ('concept', 'correction'):
            err(cid, 'type 只能是 concept / correction')
            continue
        if not cid.startswith('gw06/%s/' % typ):
            err(cid, 'id 前缀应为 gw06/%s/' % typ)
        if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', slug):
            err(cid, 'slug 只能小写字母数字连字符：%s' % slug)
        for f in ('id', 'type', 'track', 'title', 'summary', 'question',
                  'annotations', 'related', 'sources', 'rights', 'status',
                  'verification'):
            if not c.get(f):
                err(cid, '缺字段 %s' % f)
        if not TRACK.match(c.get('track') or ''):
            err(cid, 'track 应为 §N、§N.M 或 附录A/附录B：%r' % c.get('track'))
        if not (c.get('question') or '').endswith(('？', '?')):
            err(cid, 'question 已问号结尾')
        if cjk_len(c.get('summary') or '') > 120:
            err(cid, 'summary 汉字 %d > 120' % cjk_len(c['summary']))
        if c.get('rights') != 'rewritten':
            err(cid, 'rights 必须是 rewritten')
        if c.get('status') not in STATUSES:
            err(cid, 'status 非法：%r' % c.get('status'))
        if c.get('status') == 'published':
            err(cid, 'published 需 external-confirmed，本轮一律 reviewed')
        # annotations
        anns = c.get('annotations') or []
        if len(anns) < 1:
            err(cid, 'annotations 至少 1 条')
        for a in anns:
            if a.get('type') not in ANN_TYPES:
                err(cid, '批注类型非法：%r' % a.get('type'))
            if not a.get('title') or not a.get('text'):
                err(cid, '批注缺 title/text')
            elif cjk_len(a['text']) < 40:
                warn(cid, '批注「%s」只有 %d 汉字，偏薄' % (a['title'], cjk_len(a['text'])))
        # related
        rel = c.get('related') or []
        if len(rel) < 2:
            err(cid, 'related 至少 2 条')
        for r in rel:
            if r not in idset:
                if allow_missing_related:
                    warn(cid, 'related 暂未解析（分批写卡时正常）：%s' % r)
                else:
                    err(cid, 'related 无法解析：%s' % r)
            if r == cid:
                err(cid, 'related 不能指向自身')
        # sources
        srcs = c.get('sources') or []
        if not srcs:
            err(cid, 'sources 不能为空')
        for s in srcs:
            if not s.get('book'):
                err(cid, 'sources.book 不能为空')
            if not s.get('section'):
                err(cid, 'sources.section 不能为空')
            pages = s.get('pages') or []
            pdf = s.get('pdf_pages') or []
            if pages != sorted(pages) or pdf != sorted(pdf):
                err(cid, 'pages/pdf_pages 应递增')
            if pages and pdf != [p + 1 for p in pages]:
                err(cid, 'pdf_pages 必须 = pages + 1：%s vs %s' % (pages, pdf))
            if bool(pages) != bool(pdf):
                err(cid, 'pages 与 pdf_pages 必须同时给或同时空')
            got = check_anchor(cid, s.get('anchor') or '')
            if got and c.get('type') == 'correction':
                path, a, b = got
                with io.open(path, encoding='utf-8') as fh:
                    body = ''.join(fh.readlines()[a - 1:b])
                frag = (c.get('corrected') or '').strip()
                if frag and frag not in body:
                    warn(cid, 'corrected 片段不在 anchor 区间内，请核对')
        # type-specific
        if typ == 'concept':
            for f in ('aliases', 'definition', 'key_points', 'formulas', 'pitfalls'):
                if not c.get(f):
                    err(cid, '概念卡缺 %s' % f)
            if len(c.get('key_points') or []) < 3:
                err(cid, 'key_points 至少 3 条')
            if len(c.get('formulas') or []) < 1:
                err(cid, 'formulas 至少 1 条')
            if len(c.get('pitfalls') or []) < 2:
                err(cid, 'pitfalls 至少 2 条')
            if not (c.get('definition') or {}).get('text'):
                err(cid, 'definition.text 不能为空')
            for x in c.get('formulas') or []:
                if x.strip().startswith('$') or x.strip().endswith('$'):
                    err(cid, 'formulas 里不要带 $：%s' % x[:40])
        else:
            for f in ('location', 'original', 'corrected', 'why', 'note'):
                if not (c.get(f) or '').strip():
                    err(cid, '勘误卡缺 %s' % f)
            if (c.get('original') or '').strip() == (c.get('corrected') or '').strip():
                err(cid, 'original 与 corrected 相同')
            if cjk_len(c.get('why') or '') < 30:
                warn(cid, 'why 只有 %d 汉字，依据偏薄' % cjk_len(c.get('why') or ''))
        v = c.get('verification') or {}
        if v.get('status') not in VERIF:
            err(cid, 'verification.status 非法：%r' % v.get('status'))
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', v.get('checked_on') or ''):
            err(cid, 'verification.checked_on 应为 YYYY-MM-DD')
        if not v.get('checks'):
            err(cid, 'verification.checks 不能为空')


def render_md(c):
    L = ['# %s' % c['title'], '']
    L.append('- **id**：`%s`' % c['id'])
    L.append('- **类型**：%s' % c['type'])
    L.append('- **位置**：%s' % c['track'])
    L.append('- **问题**：%s' % c['question'])
    L += ['', '> %s' % c['summary'], '']
    if c['type'] == 'concept':
        L += ['## 定义', '', c['definition']['text'], '']
        if c['definition'].get('notation'):
            nt = c['definition']['notation']
            if isinstance(nt, list):
                L += ['**记号**：' + '、'.join(nt), '']
            else:
                L += ['**记号**：' + str(nt), '']
        L += ['## 关键点', ''] + ['- ' + x for x in c['key_points']] + ['']
        L += ['## 公式', ''] + ['```latex\n%s\n```' % x for x in c['formulas']] + ['']
        if c.get('theorems'):
            L += ['## 定理', '']
            for t in c['theorems']:
                L += ['**%s**：%s' % (t.get('name', ''), t.get('statement', '')), '']
                if t.get('proof'):
                    L += ['证明：%s（%s）' % (t['proof'].get('status', ''),
                                            t.get('source', '')), '']
                    for st in t['proof'].get('steps') or []:
                        L.append('%s. %s —— %s' % (st.get('no', ''), st.get('text', ''),
                                                   st.get('why', '')))
                    if t['proof'].get('gap_note'):
                        L += ['', '缺口：' + t['proof']['gap_note']]
                    L.append('')
        L += ['## 常见错误', ''] + ['- ' + x for x in c['pitfalls']] + ['']
    else:
        L += ['## 位置', '', c['location'], '']
        L += ['## 原文片段', '', '```latex\n%s\n```' % c['original'], '']
        L += ['## 改为', '', '```latex\n%s\n```' % c['corrected'], '']
        L += ['## 依据', '', c['why'], '']
        L += ['## 说明', '', c['note'], '']
    L += ['## 批注', '']
    for a in c['annotations']:
        L += ['### %s：%s' % (a['type'], a['title']), '', a['text'], '']
    L += ['## 出处', '']
    for s in c['sources']:
        pg = '；印刷页 %s / PDF 页 %s' % (s['pages'], s['pdf_pages']) if s.get('pages') else ''
        L.append('- %s %s%s；锚点 `%s`' % (s['book'], s['section'], pg, s['anchor']))
        if s.get('page_note'):
            L.append('- ' + s['page_note'])
    L += ['', '---', '',
          '权利：`rewritten`；核验：`%s`（%s）。' % (
              c['verification']['status'], c['verification']['checked_on']), '']
    return '\n'.join(L)


def write(path, text):
    d = os.path.dirname(path)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    with io.open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def main(argv):
    strict = '--strict' in argv
    check_only = '--check' in argv
    allow_missing = '--allow-missing-related' in argv
    cards = load()
    validate(cards, allow_missing)
    print('cards: %d（concept %d / correction %d）' % (
        len(cards), sum(1 for c in cards if c['type'] == 'concept'),
        sum(1 for c in cards if c['type'] == 'correction')))
    if errors:
        print('ERRORS %d' % len(errors))
        for e in errors:
            print('  ' + e)
    if warnings:
        print('WARNINGS %d' % len(warnings))
        for w in warnings:
            print('  ' + w)
    if errors or (strict and warnings):
        return 1
    if check_only:
        print('OK')
        return 0

    # 清理旧的生成产物
    md_dir = os.path.join(ROOT, 'md')
    for f in glob.glob(os.path.join(md_dir, '*.md')):
        os.remove(f)
    idx, ver, tax, maprows = [], [], {}, []
    for c in sorted(cards, key=lambda x: (x['track'], x['type'], x['id'])):
        slug = c['id'].split('/')[-1]
        src = c['sources'][0]
        write(os.path.join(md_dir, slug + '.md'), render_md(c))
        idx.append({'id': c['id'], 'type': c['type'], 'track': c['track'],
                    'title': c['title'], 'summary': c['summary'],
                    'section': src['section'], 'anchor': src['anchor'],
                    'pdf_pages': src.get('pdf_pages') or []})
        ver.append({'id': c['id'],
                    'status': c['verification']['status'],
                    'checked_on': c['verification']['checked_on'],
                    'checks': c['verification']['checks']})
        tax.setdefault(c['track'], []).append(c)
        maprows.append((c, src))
    write(os.path.join(ROOT, 'index.jsonl'),
          ''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in idx))
    write(os.path.join(ROOT, 'verification.jsonl'),
          ''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in ver))
    order = ['§1', '§2', '§2.1', '§2.2', '§2.3', '§2.4', '§2.5', '§2.6',
             '§3', '§3.1', '§3.2', '§3.3', '§3.4', '§3.5', '§3.6', '§3.7',
             '§3.8', '§3.9', '§4', '§4.1', '§4.2', '§4.3', '§4.4', '§4.5',
             '§4.6', '§5', '§5.1', '§5.2', '§5.3', '§6', '附录A', '附录B']

    def okey(t):
        return order.index(t) if t in order else 99
    L = ['# gw06 分类', '',
         '按位置分组；每张卡至少一条批注。共 %d 张（概念 %d、勘误 %d）。' % (
             len(cards), sum(1 for c in cards if c['type'] == 'concept'),
             sum(1 for c in cards if c['type'] == 'correction')), '']
    for t in sorted(tax, key=okey):
        L += ['## %s' % t, '']
        for c in tax[t]:
            L.append('- `%s` %s（%s）' % (c['id'], c['title'], c['type']))
        L.append('')
    write(os.path.join(ROOT, 'taxonomy.md'), '\n'.join(L))
    L = ['# gw06 卡片地图', '',
         '| 位置 | 类型 | 标题 | 节 | PDF 页 | 锚点 |', '|---|---|---|---|---|---|']
    for c, s in maprows:
        pdf = '、'.join(str(p) for p in (s.get('pdf_pages') or [])) or '—'
        L.append('| %s | %s | %s | %s | %s | `%s` |' % (
            c['track'], c['type'], c['title'], s['section'], pdf, s['anchor']))
    ncat = sum(1 for a in cards for _ in a['annotations'])
    L += ['', '共 %d 张：概念 %d、勘误 %d；批注 %d 条（易错预警 %d、含糊点拨 %d、背景直觉 %d）。' % (
        len(cards), sum(1 for c in cards if c['type'] == 'concept'),
        sum(1 for c in cards if c['type'] == 'correction'), ncat,
        sum(1 for a in cards for x in a['annotations'] if x['type'] == '易错预警'),
        sum(1 for a in cards for x in a['annotations'] if x['type'] == '含糊点拨'),
        sum(1 for a in cards for x in a['annotations'] if x['type'] == '背景直觉')), '']
    write(os.path.join(ROOT, 'MAP.md'), '\n'.join(L))
    print('写出 index.jsonl / verification.jsonl / md/ / MAP.md / taxonomy.md')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
