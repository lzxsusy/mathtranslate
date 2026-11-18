#!/usr/bin/env python3
"""把 annotations.json 里的校注插入各章 tex。

用法：
    python insert_annotations.py <源码目录> [annotations.json] [--dry]

规则（幂等，可重复运行）：
- `where=end`：插在该 `\\section{...}` 的末尾，即下一个 `\\section` 之前；若已是文件最后一节，追加到文件末尾。
- `where=before`：紧插在该 `\\section{...}` 之前。
- `anchor_section` 为空：跳过并报告（等人工指定锚点）。
- 已含同 topic 的注释（按前 16 字判定）则跳过。
"""
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def load(path):
    with io.open(path, encoding='utf-8') as f:
        return json.load(f)


def find_section(lines, title):
    pat = re.compile(r'^\s*\\section\*?\{' + re.escape(title))
    for i, ln in enumerate(lines):
        if pat.search(ln):
            return i
    return -1


def section_end(lines, start):
    for j in range(start + 1, len(lines)):
        if re.match(r'^\s*\\(section|chapter)\b', lines[j]):
            return j
    return len(lines)


def block(note):
    tex = note['tex'].strip()
    return ('\\begin{annote}\n' + tex + '\n\\end{annote}\n\n')


def main():
    src = sys.argv[1]
    jpath = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') \
        else os.path.join(HERE, '..', '..', '..', '工作副本_annotations.json')
    if not os.path.exists(jpath):
        jpath = os.path.join(os.path.dirname(HERE), 'annotations.json')
    dry = '--dry' in sys.argv
    notes = load(jpath)
    ok = skip = miss = 0
    for n in notes:
        path = os.path.join(src, 'chapters', n['file'])
        with io.open(path, encoding='utf-8') as f:
            lines = f.read().split('\n')
        text = '\n'.join(lines)
        probe = n['tex'][:16]
        if probe and probe in text:
            skip += 1
            continue
        if not n.get('anchor_section'):
            print('!! 缺锚点：%s %s' % (n['file'], n['id']))
            miss += 1
            continue
        i = find_section(lines, n['anchor_section'])
        if i < 0:
            print('!! 找不到节：%s  \\section{%s}' % (n['file'], n['anchor_section']))
            miss += 1
            continue
        at = i if n.get('where') == 'before' else section_end(lines, i)
        # 末尾插入时避免紧跟 \end{document}
        chunk = block(n).split('\n')
        if at > 0 and lines[at - 1].strip() == '':
            at -= 1
        lines[at:at] = chunk
        if not dry:
            with io.open(path, 'w', encoding='utf-8', newline='\n') as f:
                f.write('\n'.join(lines))
        ok += 1
        print('   + %s %s  →  %s 第 %d 行' % (n['file'], n['id'], n['anchor_section'], at + 1))
    print('---\n插入 %d，已存在跳过 %d，待定 %d' % (ok, skip, miss))


if __name__ == '__main__':
    main()
