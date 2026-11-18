# -*- coding: utf-8 -*-
"""结构审计：括号/环境/数学模式/交叉引用/编码。用法：python tools/integrity_audit.py [章节目录]"""
import io
import os
import re
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '源码')
ENVS = ['lemma', 'theorem', 'proposition', 'corollary', 'definition', 'example',
        'remark', 'proof', 'enumerate', 'itemize', 'equation', 'aligned', 'cases',
        'matrix', 'pmatrix', 'bmatrix', 'annote', 'center', 'array', 'split',
        'gather', 'multline', 'description', 'quote', 'verbatim']


def strip_comments(s):
    out = []
    for line in s.split('\n'):
        m = re.search(r'(?<!\\)%', line)
        out.append(line[:m.start()] if m else line)
    return '\n'.join(out)


def check_file(path):
    errs = []
    raw = io.open(path, encoding='utf-8').read()
    s = strip_comments(raw)
    # 编码
    if '\ufffd' in raw:
        errs.append('UTF-8 替换字符 U+FFFD')
    if re.search(r'[ÃÂ][\u0080-\u00bf]|â€|ï¼', s):
        bad = set(re.findall(r'[ÃÂ][\u0080-\u00bf]|â€|ï¼', s))
        errs.append('疑似 UTF-8 被按 latin1 解码: ' + ' '.join(sorted(bad)))
    # 花括号（排除 \{ \}）
    t = re.sub(r'\\[{}]', '', s)
    if t.count('{') != t.count('}'):
        errs.append('花括号不平衡: { = %d, } = %d' % (t.count('{'), t.count('}')))
    # 数学模式 $ 与 $$
    no_dd = t.replace('$$', '')
    no_dollar = re.sub(r'(?<!\\)\$', '', t)
    n = len(t) - len(no_dollar)
    if n % 2 != 0:
        errs.append('行内 $ 计数为奇数: %d' % n)
    if len(t) - len(no_dd) != 4 * (t.count('$$')):
        pass
    # 环境配对
    for e in ENVS:
        b = len(re.findall(r'\\begin\{%s\}' % e, t))
        en = len(re.findall(r'\\end\{%s\}' % e, t))
        if b != en:
            errs.append('环境 %s 不平衡: begin %d / end %d' % (e, b, en))
    # 命令参数缺失
    for m in re.finditer(r'\\(section|chapter|label|ref|begin|end)\*?\s*(?=[^\[{*])', t):
        errs.append('命令 %s 缺参数（行 %d）' % (m.group(1), t[:m.start()].count('\n') + 1))
    # 控制序列后紧跟汉字（\item完整 → 未定义控制序列）
    for m in re.finditer(r'\\[a-zA-Z]+\*?(?=[\u4e00-\u9fff])', t):
        errs.append('控制序列后缺空格: %s（行 %d）' % (m.group(0), t[:m.start()].count('\n') + 1))
    return errs


def main():
    files = sorted(os.path.join(ROOT, f) for f in os.listdir(ROOT) if f.endswith('.tex'))
    total = 0
    labels, refs = {}, []
    for p in files:
        errs = check_file(p)
        for e in errs:
            print('%s: %s' % (os.path.basename(p), e))
        total += len(errs)
        s = io.open(p, encoding='utf-8').read()
        for m in re.finditer(r'\\label\{([^}]*)\}', s):
            labels[m.group(1)] = labels.get(m.group(1), 0) + 1
        refs += [(os.path.basename(p), m.group(1)) for m in re.finditer(r'\\(?:eq)?ref\{([^}]*)\}', s)]
    for k, v in labels.items():
        if v > 1:
            print('重复 label: %s ×%d' % (k, v))
            total += 1
    for f, r in refs:
        if r not in labels:
            print('%s: 未定义的 \\ref{%s}' % (f, r))
            total += 1
    print('---')
    print('文件 %d 个，问题 %d 处' % (len(files), total))
    return 1 if total else 0


if __name__ == '__main__':
    sys.exit(main())
