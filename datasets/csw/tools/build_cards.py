#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把 tools/_data*.py 里的卡片数据落成 cards/*.json 并生成 index.jsonl。

用法（在 datasets/csw 下）：
    python tools/build_cards.py
"""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import _data1, _data2, _data3, _data4, _data5  # noqa: E402

MODULES = [_data1, _data2, _data3, _data4, _data5]


MACRO = re.compile(r'\\c([HLME])(?![A-Za-z])')


def mathjs(obj):
    r"""把书内自定义宏换成 MathJax 标准写法（\cH -> \mathcal{H} 等）。"""
    if isinstance(obj, str):
        return MACRO.sub(r'\\mathcal{\1}', obj)
    if isinstance(obj, list):
        return [mathjs(x) for x in obj]
    if isinstance(obj, dict):
        return {k: mathjs(v) for k, v in obj.items()}
    return obj


def normalize(c):
    """补全证明步骤/计算步骤的编号，并把自定义宏换成标准宏。"""
    c = mathjs(c)
    if c.get('type') == 'concept':
        for t in c.get('theorems', []):
            steps = t.get('proof', {}).get('steps', [])
            for i, st in enumerate(steps):
                st.setdefault('no', i + 1)
    else:
        for i, st in enumerate(c.get('computation', [])):
            st.setdefault('no', i + 1)
    return c


def main():
    cards = []
    for m in MODULES:
        cards.extend(m.DATA)
    cards = [normalize(c) for c in cards]
    ids = set()
    for c in cards:
        if c['id'] in ids:
            raise SystemExit('duplicate id: %s' % c['id'])
        ids.add(c['id'])

    dirs = {
        'concept': os.path.join(ROOT, 'cards', 'concepts'),
        'example': os.path.join(ROOT, 'cards', 'examples'),
    }
    for d in dirs.values():
        os.makedirs(d, exist_ok=True)

    index = []
    for c in sorted(cards, key=lambda x: x['id']):
        slug = c['id'].split('/', 2)[-1]
        path = os.path.join(dirs[c['type']], slug + '.json')
        with io.open(path, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(c, f, ensure_ascii=False, indent=2)
            f.write('\n')
        index.append({
            'id': c['id'],
            'type': c['type'],
            'track': c['track'],
            'title': c['title'],
            'summary': c['summary'],
            'path': os.path.relpath(path, ROOT).replace('\\', '/'),
        })

    with io.open(os.path.join(ROOT, 'index.jsonl'), 'w', encoding='utf-8', newline='\n') as f:
        for row in index:
            f.write(json.dumps(row, ensure_ascii=False) + '\n')

    n_c = sum(1 for c in cards if c['type'] == 'concept')
    n_e = sum(1 for c in cards if c['type'] == 'example')
    print('wrote %d concept + %d example cards, index.jsonl %d rows' % (n_c, n_e, len(index)))


if __name__ == '__main__':
    main()
