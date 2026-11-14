# -*- coding: utf-8 -*-
r"""SY02-09 的 TeX 预清洗：在 _tex_clean.expand 之前去掉本工程自有宏。

本工程（Langlands 讲义译本）用到的宏与 SY01-23 不同：
  \znote{…} / \znoteplain{…}   学生向译注（长脚注）→ 整段丢弃（已逐条登记在 工程文件/notes/）
  \idx{…}                      索引 → 丢弃
  \sourcepage{n} \originalnumber{n} \lecturedate{…} → 丢弃
  \refitem{label}{文献}        → 丢弃（英文书目）
  \bref{label}{编号}           → 编号
  \eref{文}{label}             → 文
  \begin{definition*}{标题} … \end{definition*} → 去掉环境标记与标题
"""
import re


def _read_braces(s, i, open_ch='{', close_ch='}'):
    if i >= len(s) or s[i] != open_ch:
        return '', i
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == open_ch:
            depth += 1
        elif c == close_ch:
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    return s[i + 1:], len(s)


DROP_CMDS = {'znote', 'znoteplain', 'idx', 'sourcepage', 'originalnumber',
             'lecturedate', 'refitem', 'label', 'xchaptertitle', 'lref'}


def _drop(s, names):
    out = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == '\\':
            m = re.match(r'\\([A-Za-z]+)\*?', s[i:])
            if m and m.group(1) in names:
                j = i + m.end()
                while j < n and s[j] in ' \t':
                    j += 1
                while j < n and s[j] == '{':
                    _a, j = _read_braces(s, j)
                    while j < n and s[j] in ' \t':
                        j += 1
                i = j
                continue
        out.append(s[i])
        i += 1
    return ''.join(out)


KEEP_FIRST = re.compile(r'\\(?:bref|eref)\{([^{}]*)\}\{([^{}]*)\}')


def preclean(t):
    t = _drop(t, DROP_CMDS)
    # \bref{label}{编号} -> 编号；\eref{文}{label} -> 文
    t = re.sub(r'\\bref\{[^{}]*\}\{([^{}]*)\}', r'\1', t)
    t = re.sub(r'\\eref\{([^{}]*)\}\{[^{}]*\}', r'\1', t)
    # 带星号的环境与紧随其后的标题参数
    t = re.sub(r'\\(?:begin|end)\{[A-Za-z]+\*\}', '', t)
    t = re.sub(r'\\(?:begin|end)\{(?:property|corollary|note|problem|exercise|solution|'
               r'definition|theorem|proposition|lemma|example|remark|conjecture|proof|'
               r'references)\*?(?:\{[^{}]*\})?', '', t)
    t = t.replace('\\item', ' ')
    return t
