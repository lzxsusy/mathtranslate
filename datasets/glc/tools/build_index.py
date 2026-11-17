#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""cards/*.json → index.jsonl（一行一卡）。

用法（在 datasets/glc 下）：
    python tools/build_index.py
"""
import glob
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def main():
    rows = []
    for p in sorted(glob.glob(os.path.join(ROOT, 'cards', '*', '*.json'))):
        with io.open(p, encoding='utf-8') as f:
            c = json.load(f)
        rows.append({
            'id': c['id'],
            'type': c['type'],
            'track': c['track'],
            'title': c['title'],
            'summary': c['summary'],
            'path': os.path.relpath(p, ROOT).replace('\\', '/'),
        })
    rows.sort(key=lambda r: r['id'])
    out = os.path.join(ROOT, 'index.jsonl')
    with io.open(out, 'w', encoding='utf-8', newline='\n') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    print('index.jsonl: %d cards' % len(rows))


if __name__ == '__main__':
    main()
