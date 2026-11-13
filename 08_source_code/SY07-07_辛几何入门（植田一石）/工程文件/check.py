# -*- coding: utf-8 -*-
"""Gate 1：源码静态检查（BOM / 乱码 / 花括号 / 环境配对 / 禁用命令 / 统计）。
用法：python check.py  → 全部通过退出码 0。
"""
import io, os, re, sys, glob, collections

ROOT = os.path.dirname(os.path.abspath(__file__))
CH = os.path.join(ROOT, 'src', 'chunks')

FORBIDDEN = [r'\cite', r'\label', r'\ref{', r'\input', r'\include{',
             r'\usepackage', r'\newcommand']
MOJI = set('鈥锛銆鍒鏂鐨鍔涘瀽鐞嗗鐨勶紝銆傦紵锝')

# 跨块配对例外：定理 6.3.1 的证明横跨 ch06a/ch06b，
# ch06b 首段用 \ifdefined\UEDAdraft\else\end{proof}\fi 在合并模式闭合
CROSS = {'ch06b': ('proof', -1)}


def read(p):
    with io.open(p, encoding='utf-8-sig') as f:
        return f.read()


def strip_comments(t):
    out = []
    for ln in t.splitlines():
        k = None
        for i, ch in enumerate(ln):
            if ch == '%':
                j = i - 1
                n = 0
                while j >= 0 and ln[j] == '\\':
                    n += 1
                    j -= 1
                if n % 2 == 0:
                    k = i
                    break
        out.append(ln if k is None else ln[:k])
    return '\n'.join(out)


def brace_balance(body):
    """跳过 \\{ \\} 等转义后的花括号计数。"""
    depth = 0
    i = 0
    while i < len(body):
        ch = body[i]
        if ch == '\\':
            i += 2
            continue
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth < 0:
                return -999
        i += 1
    return depth


def main():
    files = sorted(glob.glob(os.path.join(CH, '*.tex')))
    problems = []
    ntags = npages = 0
    for p in files:
        name = os.path.basename(p)[:-4]
        raw = open(p, 'rb').read()
        t = read(p)
        if raw[:3] == b'\xef\xbb\xbf':
            problems.append(f'{name}: UTF-8 BOM')
        bad = sorted(set(ch for ch in t if ch in MOJI))
        if bad:
            problems.append(f'{name}: 乱码字符 {bad[:5]}')
        body = strip_comments(t)
        d = brace_balance(body)
        if d != 0:
            problems.append(f'{name}: 花括号不平衡 ({d})')
        ob = collections.Counter(re.findall(r'<本地路径>]*)\}', body))
        eb = collections.Counter(re.findall(r'<本地路径>]*)\}', body))
        diff = {k: ob[k] - eb[k] for k in set(ob) | set(eb) if ob[k] - eb[k]}
        if name in CROSS:
            env, delta = CROSS[name]
            got = diff.pop(env, 0)
            if got != delta:
                problems.append(f'{name}: 跨块例外 {env} begin-end={got} 应为 {delta}')
        if diff:
            problems.append(f'{name}: 环境不配对 {diff}')
        for pat in FORBIDDEN:
            if pat in body:
                problems.append(f'{name}: 禁用命令 {pat}')
        ntags += len(re.findall(r'<本地路径>', body))
        npages += len(re.findall(r'% \[原文 p\.\d+', t))

    print(f'files={len(files)}  tags={ntags}  page-marks={npages}')
    if problems:
        print('PROBLEMS:')
        for s in problems:
            print('  -', s)
        print('STATUS: FAIL')
        return 1
    print('STATUS: OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())
