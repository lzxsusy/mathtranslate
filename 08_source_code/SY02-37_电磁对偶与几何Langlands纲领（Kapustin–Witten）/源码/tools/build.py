# -*- coding: utf-8 -*-
"""KW06 中译注本构建：汇总 36 片 → body.tex → xelatex 三遍。
   用法：
     python tools/build.py            # 有 zh/NN-sXX.tex 就用译文，没有就退回 skel（英文）
     python tools/build.py --zh-only  # 只收已译出的片段（未译片段留空，用于中途检查）
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XELATEX = r"C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe"


def shards():
    names = sorted(n for n in os.listdir(os.path.join(ROOT, 'skel')) if n.endswith('.tex'))
    return names


def build_body(zh_only=False):
    lines = ['%% 自动生成：请勿手改（由 tools/build.py 生成）', '']
    used_zh = used_en = missing = 0
    for n in shards():
        zh = os.path.join(ROOT, 'zh', n)
        if os.path.exists(zh):
            lines.append('\\input{zh/%s}' % n[:-4])
            used_zh += 1
        elif zh_only:
            missing += 1
            lines.append('%% [待译] %s' % n)
        else:
            lines.append('\\input{skel/%s}' % n[:-4])
            used_en += 1
    io.open(os.path.join(ROOT, 'body.tex'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    return used_zh, used_en, missing


def run(passes=3):
    for i in range(passes):
        p = subprocess.run([XELATEX, '-interaction=nonstopmode', '-file-line-error', 'main.tex'],
                           cwd=ROOT, capture_output=True)
        out = (p.stdout or b'').decode('utf-8', 'replace')
        # -file-line-error 的输出形如 `refs.tex:3: LaTeX Error: ...`（有的引擎带 ./ 前缀），
        # 旧判据只认 `^!` 和 `^\./`，漏掉了不带前缀的 file:line: 错误（曾导致 106 个
        # refs.tex 的 \mathbf 文本模式错误被报成 errors=0）。
        errs = [l for l in out.splitlines()
                if l.startswith('!') or re.match(r'^(?:\./)?\S+?:\d+: ', l)]
        print('--- pass %d: exit=%s errors=%d' % (i + 1, p.returncode, len(errs)))
        if errs:
            for l in errs[:25]:
                print('   ', l)
            break
    pdf = os.path.join(ROOT, 'main.pdf')
    if os.path.exists(pdf):
        print('PDF:', pdf, os.path.getsize(pdf), 'bytes')
    log = os.path.join(ROOT, 'main.log')
    if os.path.exists(log):
        s = io.open(log, encoding='utf-8', errors='replace').read()
        m = re.findall(r'Output written on main\.pdf \((\d+) pages', s)
        if m:
            print('pages:', m[-1])
        w = re.findall(r'^(!|LaTeX Warning: .*|Overfull \\hbox)', s, re.M)
        print('warnings(head):', w[:10])


if __name__ == '__main__':
    zh_only = '--zh-only' in sys.argv
    z, e, mi = build_body(zh_only)
    print('shards: zh=%d en=%d missing=%d' % (z, e, mi))
    run()
