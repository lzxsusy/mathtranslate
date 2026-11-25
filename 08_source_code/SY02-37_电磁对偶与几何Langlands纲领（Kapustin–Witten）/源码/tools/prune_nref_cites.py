# -*- coding: utf-8 -*-
"""剔除 harvmac \\nref 造成的多余引用标记。

背景：harvmac 的 \\nref\\KEY{...} 只是「登记参考文献」——已用出版版 PDF 逐页核实，
正文在这些位置不打印任何编号（例如 §1 开头 \nref\\drinfeld/\nref\\lafforgue，
PDF 里只有后面 \\refs{...} 处的 [2,3]）。原转换器误把 \\nref 当成 \\ref，
为每处生成了 \\cite{refN}，全书共 82 处，渲染成孤立的 [N]。

本脚本对比「旧 skel（含多余 cite）」与「新 skel（已修正）」的 \\cite 序列，
把被删掉的对应项从 zh/*.tex 里同步剔除（zh 的 cite 序列与旧 skel 完全一致，
这是 verify_translation.py 的 S2 项已逐片验证过的）。
"""
import io, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLD = os.path.join(ROOT, 'skel_before_nref')
NEW = os.path.join(ROOT, 'skel')
ZH = os.path.join(ROOT, 'zh')

CITE = re.compile(r'\\cite\{[^}]*\}')


def cites(s):
    return CITE.findall(s)


def removed_indices(old, new):
    """old/new 为 cite 词表；返回 old 中被删除的下标（顺序保持）。"""
    out, i, j = [], 0, 0
    while i < len(old) and j < len(new):
        if old[i] == new[j]:
            i += 1
            j += 1
        else:
            out.append(i)
            i += 1
    out.extend(range(i, len(old)))
    return out


def prune_zh(path, drop):
    s = io.open(path, encoding='utf-8').read()
    spans = [m.span() for m in CITE.finditer(s)]
    if len(spans) != len(drop) + 0 and drop and len(spans) <= max(drop):
        print('  !! %s cite 数 %d 不足（需删到下标 %d）' % (os.path.basename(path), len(spans), max(drop)))
    # 从后往前删，避免位移
    for idx in sorted(drop, reverse=True):
        if idx >= len(spans):
            continue
        a, b = spans[idx]
        # 连带吃掉同一行上该 cite 前后多余空白：若整行只剩 cite，则删整行
        ls = s.rfind('\n', 0, a) + 1
        le = s.find('\n', b)
        le = len(s) if le < 0 else le
        line = s[ls:le]
        rest = (line[:a - ls] + line[b - ls:]).replace(' ', '')
        if rest == '':
            s = s[:ls] + s[le + 1:]
        else:
            s = s[:a] + s[b:]
    io.open(path, 'w', encoding='utf-8', newline='\n').write(s)


def main():
    total = 0
    for name in sorted(os.listdir(NEW)):
        if not name.endswith('.tex'):
            continue
        op = os.path.join(OLD, name)
        if not os.path.exists(op):
            continue
        old = cites(io.open(op, encoding='utf-8').read())
        new = cites(io.open(os.path.join(NEW, name), encoding='utf-8').read())
        drop = removed_indices(old, new)
        if not drop:
            continue
        zp = os.path.join(ZH, name)
        if not os.path.exists(zp):
            print('%s 待译，跳过（交付后重跑本脚本）' % name)
            continue
        zh_cites = cites(io.open(zp, encoding='utf-8').read())
        if zh_cites != old:
            print('%s !! zh cite 序列与旧 skel 不一致，跳过（需人工看）' % name)
            continue
        prune_zh(zp, drop)
        total += len(drop)
        print('%s 删除 %d 处 cite' % (name, len(drop)))
    print('合计删除 %d 处' % total)


if __name__ == '__main__':
    main()
