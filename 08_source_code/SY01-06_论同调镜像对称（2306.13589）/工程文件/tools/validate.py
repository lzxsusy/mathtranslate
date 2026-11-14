# -*- coding: utf-8 -*-
"""校验译文章节文件。用法：
   python validate.py <译文.tex> [<原始单元.tex>]
不传原始单元时只做结构与编码检查。"""
import re, sys, os, io

def read(p):
    return io.open(p, encoding='utf-8').read()

def brace_balance(t):
    # 去掉注释与转义
    depth = 0; bad = None
    i = 0; line = 1
    while i < len(t):
        c = t[i]
        if c == '\n':
            line += 1
        if c == '%':                      # 注释到行尾
            while i < len(t) and t[i] != '\n':
                i += 1
            continue
        if c == '\\':
            i += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth < 0 and bad is None:
                bad = line
        i += 1
    return depth, bad

def env_check(t):
    stack = []
    errs = []
    for m in re.finditer(r'\\(begin|end)\{([^}]*)\}', t):
        kind, name = m.group(1), m.group(2)
        ln = t[:m.start()].count('\n') + 1
        if kind == 'begin':
            stack.append((name, ln))
        else:
            if not stack:
                errs.append(f'L{ln}: \\end{{{name}}} 无匹配 begin')
            elif stack[-1][0] != name:
                errs.append(f'L{ln}: \\end{{{name}}} 与 L{stack[-1][1]} 的 \\begin{{{stack[-1][0]}}} 不匹配')
                stack.pop()
            else:
                stack.pop()
    for name, ln in stack:
        errs.append(f'L{ln}: \\begin{{{name}}} 未闭合')
    return errs

def keys(t, pat):
    return set(re.findall(pat, t))

LABEL = r'\\label\{([^}]*)\}'
REF   = r'\\(?:ref|eqref)\{([^}]*)\}'
CITE  = r'\\cite(?:\[[^\]]*\])?\{([^}]*)\}'
INDEX = r'\\index\{([^}]*)\}'

def main():
    if len(sys.argv) < 2:
        print('用法: python validate.py <译文.tex> [<原始单元.tex>]'); return 2
    zhp = sys.argv[1]
    orig = sys.argv[2] if len(sys.argv) > 2 else None
    t = read(zhp)
    name = os.path.basename(zhp)
    ok = True
    msgs = []

    # 编码
    msgs.append(('[OK] ', 'UTF-8 可读') if True else ('', ''))

    d, bad = brace_balance(t)
    if d != 0:
        ok = False
        msgs.append(('[FAIL]', f'花括号不平衡：净值 {d:+d}' + (f'（首次多余右括号在 L{bad}）' if bad else '')))
    else:
        msgs.append(('[OK]  ', '花括号配平'))

    errs = env_check(t)
    if errs:
        ok = False
        msgs.append(('[FAIL]', '环境不配对：\n        ' + '\n        '.join(errs[:10])))
    else:
        msgs.append(('[OK]  ', 'begin/end 环境全部配对'))

    n_notes = len(re.findall(r'% \[Tutor Note:', t))
    msgs.append(('[INFO]', f'[Tutor Note] 批注 {n_notes} 条'))
    if n_notes == 0:
        ok = False
        msgs.append(('[FAIL]', '缺少 [Tutor Note] 批注'))

    n_take = t.count('\\takeaway{')
    has_sec = re.search(r'\\section\{', t) is not None
    if has_sec and n_take == 0:
        ok = False
        msgs.append(('[FAIL]', '含 \\section 但缺少 \\takeaway{} 本节重点'))
    elif n_take:
        msgs.append(('[INFO]', f'\\takeaway 块 {n_take} 个'))

    # 未译英文句式启发式（排除 \text{}、\cite、\bibitem、注释行、环境名参数）
    body = re.sub(r'%[^\n]*', '', t)
    body = re.sub(r'\\(cite|ref|eqref|label|index|includegraphics|url|bibitem)(\[[^\]]*\])?\{[^}]*\}', ' ', body)
    body = re.sub(r'\\text\{[^}]*\}', ' ', body)
    body = re.sub(r'\\(begin|end)\{[^}]*\}', ' ', body)
    body = re.sub(r'\$[^$]*\$', ' ', body)
    body = re.sub(r'\\\[.*?\\\]', ' ', body, flags=re.S)
    body = re.sub(r'&', ' ', body)
    words = re.findall(r'\b(?:the|and|that|which|with|from|this|these|is a|there is|we have|such that|in order to|of the)\b', body, re.I)
    zh_chars = len(re.findall(r'[\u4e00-\u9fff]', t))
    msgs.append(('[INFO]', f'中文字符 {zh_chars} 个；残留英文功能词 {len(words)} 个'))
    if len(words) > 25:
        msgs.append(('[WARN]', '英文功能词偏多，可能有未翻译段落：' + ' '.join(sorted(set(w.lower() for w in words))[:12])))

    if orig:
        o = read(orig)
        for label, pat in (('label', LABEL), ('ref/eqref', REF), ('cite', CITE)):
            a, b = keys(o, pat), keys(t, pat)
            miss = a - b
            extra = b - a
            if miss:
                ok = False
                msgs.append(('[FAIL]', f'{label} 键缺失 {len(miss)} 个: {sorted(miss)[:8]}'))
            else:
                msgs.append(('[OK]  ', f'{label} 键全部保留 ({len(a)} 个)'))
            if extra:
                msgs.append(('[WARN]', f'{label} 键新增 {len(extra)} 个（应为 0）: {sorted(extra)[:8]}'))
        # 数学内容粗查：抽取所有 $...$ 与 \[...\] 逐一比对集合
        def maths(s):
            s = re.sub(r'%[^\n]*', '', s)
            out = set()
            out |= set(re.findall(r'\$\$.*?\$\$', s, flags=re.S))
            out |= set(re.findall(r'(?<!\\)\$[^$]*\$', s, flags=re.S))
            out |= set(re.findall(r'\\\[.*?\\\]', s, flags=re.S))
            return {re.sub(r'\s+', '', x) for x in out}
        mo = maths(o)
        if mo:
            mz = maths(t)
            keep = len(mo & mz)
            msgs.append(('[INFO]', f'行内/行间公式原样保留 {keep}/{len(mo)} ({100.0*keep/max(len(mo),1):.1f}%)'))
            if keep / len(mo) < 0.75:
                msgs.append(('[WARN]', '公式保留率偏低，请核对是否改动了数学内容'))

    print(f'=== 校验 {name} ===')
    for tag, m in msgs:
        print(f'{tag} {m}')
    print('=== 结论:', 'PASS' if ok else 'FAIL', '===')
    return 0 if ok else 1

if __name__ == '__main__':
    sys.exit(main())
