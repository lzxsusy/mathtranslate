# -*- coding: utf-8 -*-
"""修复 harvmac 同名 \\eqn 造成的 label 冲突（流水线最后一步之一，幂等）。

问题：glshort.tex 里 \\eqn\\yty 出现两次——(4.24) 与 (5.3)。
converter 让 (4.24) 占用 label eq:yty，(5.3) 退化为 equation*+\\tag*{(5.3)}，
导致 §5 中三处本应指 (5.3) 的 \\eqref{eq:yty} 实际指向 (4.24)。

修法：给 (5.3) 加 \\label{eq:ytytag}，把 11-s05 / 12-s05 / 35-s12 三片里的
\\eqref{eq:yty} 改成 \\eqref{eq:ytytag}；zh/ 下同名分片同步改（若存在）。
"""
import io, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITES = ['11-s05.tex', '12-s05.tex', '35-s12.tex']
LABELED = '11-s05.tex'


def read(p):
    with io.open(p, encoding='utf-8') as f:
        return f.read()


def write(p, s):
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(s)


def patch_skel():
    changed = []
    p = os.path.join(ROOT, 'skel', LABELED)
    s = read(p)
    if r'\label{eq:ytytag}' not in s:
        old = '\\tag*{(5.3)}\n\\Gamma_{2367}\\epsilon=\\epsilon,'
        assert old in s, 'tag* (5.3) 锚点未找到，请检查 skel 是否被重跑'
        s = s.replace(old, '\\tag*{(5.3)}\n\\Gamma_{2367}\\epsilon=\\epsilon,\\label{eq:ytytag}', 1)
        write(p, s)
        changed.append('skel/' + LABELED)
    for name in SITES:
        p = os.path.join(ROOT, 'skel', name)
        s = read(p)
        n = s.count(r'\eqref{eq:yty}')
        if n:
            s = s.replace(r'\eqref{eq:yty}', r'\eqref{eq:ytytag}')
            write(p, s)
            changed.append('skel/%s (%d)' % (name, n))
    return changed


def patch_zh():
    changed = []
    for name in SITES:
        p = os.path.join(ROOT, 'zh', name)
        if not os.path.exists(p):
            continue
        s = read(p)
        if r'\eqref{eq:ytytag}' in s and r'\eqref{eq:yty}' not in s:
            continue
        n = s.count(r'\eqref{eq:yty}')
        if n:
            s = s.replace(r'\eqref{eq:yty}', r'\eqref{eq:ytytag}')
            write(p, s)
            changed.append('zh/%s (%d)' % (name, n))
    return changed


# 附加：图 label 同名冲突。glshort.tex 里 \ifig\namp 出现两次
# （§6 Fig.~4 与 §8 Fig.~11），converter 两次都生成 \label{fig:namp}，
# 导致 "Label fig:namp multiply defined"。§8 正文另有 \ref{fig:namp} 指向
# 自己那张图（21-s08:131），所以保留后者、把前者改名 fig:namp-four。
FIG_SITES = ['17-s06.tex']
FIG_OLD = r'\label{fig:namp}'
FIG_NEW = r'\label{fig:namp-four}  % 原文 \ifig\namp 同名重复（§6 Fig.~4 与 §8 Fig.~11），此处改名以免冲突'


def patch_fig():
    changed = []
    for sub in ('skel', 'zh'):
        for name in FIG_SITES:
            p = os.path.join(ROOT, sub, name)
            if not os.path.exists(p):
                continue
            s = read(p)
            if FIG_OLD not in s:
                continue
            s = s.replace(FIG_OLD, FIG_NEW, 1)
            write(p, s)
            changed.append(sub + '/' + name)
    return changed


if __name__ == '__main__':
    print('skel:', patch_skel())
    print('zh  :', patch_zh())
    print('fig :', patch_fig())
