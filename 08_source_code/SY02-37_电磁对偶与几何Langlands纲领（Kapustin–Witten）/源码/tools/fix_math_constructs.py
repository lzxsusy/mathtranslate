# -*- coding: utf-8 -*-
"""处理行内数学里残留的 harvmac 对齐构造：
     \\matrix{a&b\\cr c&d\\cr}  → \\begin{matrix}a&b\\\\c&d\\end{matrix}
     \\cases{...\\cr ...}      → \\begin{cases}...\\\\...\\end{cases}
   这些原本被转换器当作「数学内容原样保留」遮罩掉了，需要单独扫一遍。
   另：图 caption 里的空行（\\par）会打断 \\caption，压成空格。
   幂等：可反复跑；steps/harvmac2tex 之后执行。
"""
import io, glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENVS = {'matrix': 'matrix', 'cases': 'cases', 'pmatrix': 'pmatrix'}


def balanced(s, i):
    """s[i]=='{' → 返回匹配 '}' 的下标，找不到 -1"""
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


def conv_align_constructs(s):
    for name, env in ENVS.items():
        pat = re.compile(r'\\' + name + r'(?![A-Za-z])\s*\{')
        m = pat.search(s)
        while m:
            i = s.index('{', m.start())
            j = balanced(s, i)
            if j < 0:
                break
            inner = s[i + 1:j]
            inner = re.sub(r'\\cr(?![A-Za-z])', r'\\\\', inner)
            s = s[:m.start()] + '\\begin{%s}%s\\end{%s}' % (env, inner, env) + s[j + 1:]
            m = pat.search(s, m.start() + len(env) + 8)
    return s


def fix_caption_paragraphs(s):
    """caption 里出现空行 / \\par 时压平（caption 参数不能分段）"""
    out = []
    i = 0
    pat = re.compile(r'\\caption(?:\[[^\]]*\])?\{')
    while True:
        m = pat.search(s, i)
        if not m:
            out.append(s[i:])
            break
        j = balanced(s, m.end() - 1)
        if j < 0:
            out.append(s[i:])
            break
        body = s[m.end():j]
        body2 = re.sub(r'\n\s*\n', ' ', body)
        body2 = re.sub(r'\\par\b', ' ', body2)
        out.append(s[i:m.end()])
        out.append(body2)
        i = j
    return ''.join(out)


def main():
    for f in sorted(glob.glob(os.path.join(ROOT, 'skel', '*.tex'))):
        s = io.open(f, encoding='utf-8').read()
        o = s
        s = conv_align_constructs(s)
        s = fix_caption_paragraphs(s)
        if s != o:
            io.open(f, 'w', encoding='utf-8').write(s)
            print('patched', os.path.basename(f))


if __name__ == '__main__':
    main()
