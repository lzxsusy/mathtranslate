# -*- coding: utf-8 -*-
"""skel 后处理：
   1) harvmac 的字体切换写法 {\bf X} {\cal X} {\rm X} {\it X} → LaTeX 参数写法；
   2) 裸的公式标签引用（\toopme 之类，harvmac 里 \eqn\LABEL 会让 \LABEL 显示编号）
      → \eqref{eq:LABEL}。
   幂等：可反复跑。
"""
import io, glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP = {'bf': 'mathbf', 'cal': 'mathcal', 'rm': 'mathrm', 'it': 'mathit', 'sf': 'mathsf', 'tt': 'mathtt'}


def balanced_end(s, i):
    """s[i] == '{' → 返回匹配 '}' 的下标"""
    d = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == '{':
            d += 1
        elif c == '}':
            d -= 1
            if d == 0:
                return j
        j += 1
    return -1


def conv_switch_brace(s):
    """{\\bf X} / {\\bf{X}} / {\\bf \\bar 4} → \\mathbf{...}；反复跑到不再变化"""
    changed = True
    while changed:
        changed = False
        for sw, cmd in MAP.items():
            pat = re.compile(r'\{\\' + sw + r'(?![A-Za-z])\s*')
            m = pat.search(s)
            while m:
                j = m.end()
                if j < len(s) and s[j] == '{':
                    e = balanced_end(s, j)
                    if e < 0:
                        break
                    inner = s[j + 1:e]
                    k = e + 1
                    if k < len(s) and s[k] == '}':
                        s = s[:m.start()] + '\\' + cmd + '{' + inner + '}' + s[k + 1:]
                        changed = True
                        m = pat.search(s, m.start() + 2)
                        continue
                    break
                # 无内层花括号：从 j 扫到外层的 '}'
                d = 0
                k = j
                end = -1
                while k < len(s):
                    c = s[k]
                    if c == '\\':
                        k += 2
                        continue
                    if c == '{':
                        d += 1
                    elif c == '}':
                        if d == 0:
                            end = k
                            break
                        d -= 1
                    k += 1
                if end < 0:
                    break
                inner = s[j:end]
                s = s[:m.start()] + '\\' + cmd + '{' + inner + '}' + s[end + 1:]
                changed = True
                m = pat.search(s, m.start() + 2)
    return s


def conv_switch_bare(s):
    """\bf X → \mathbf{X}（X 为单个宏或单个字符；含 \bar 这类前缀时交给 brace 版）"""
    changed = True
    while changed:
        changed = False
        for sw, cmd in MAP.items():
            pat = re.compile(r'\\' + sw + r'(?![A-Za-z])\s+(\\[A-Za-z]+|[A-Za-z0-9])')
            m = pat.search(s)
            while m:
                arg = m.group(1)
                s = s[:m.start()] + '\\' + cmd + '{' + arg + '}' + s[m.end():]
                changed = True
                m = pat.search(s, m.start() + len(cmd) + 3)
    return s


def eq_labels():
    src = io.open(os.path.join(ROOT, 'src_orig', 'glshort.tex'), encoding='utf-8').read()
    return set(re.findall(r'\\eqn\*?\s*\\([A-Za-z][A-Za-z0-9]*)', src))


def conv_bare_eqref(s, labels):
    for lab in sorted(labels, key=len, reverse=True):
        pat = re.compile(r'\\' + lab + r'(?![A-Za-z])')
        s = pat.sub(r'\\eqref{eq:' + lab + '}', s)
    return s


def main():
    labels = eq_labels()
    files = sorted(glob.glob(os.path.join(ROOT, 'skel', '*.tex')))
    for f in files:
        s = io.open(f, encoding='utf-8').read()
        orig = s
        pass  # LaTeX2e 原生支持 {\bf x} {\cal X} 老式开关，无需转换
        if labels:
            s = conv_bare_eqref(s, labels)
        if s != orig:
            io.open(f, 'w', encoding='utf-8').write(s)
            print('patched', os.path.basename(f))


if __name__ == '__main__':
    main()
