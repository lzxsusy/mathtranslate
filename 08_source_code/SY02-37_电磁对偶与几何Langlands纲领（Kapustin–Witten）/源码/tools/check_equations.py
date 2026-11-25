# -*- coding: utf-8 -*-
"""公式保真核查：逐片比对 skel 与 zh 的 equation / equation* 环境内容。

归一化后比较（宏别名展开、空白压缩）。输出 reports/公式保真核查.md。
行内数学已由 verify_translation.py 以多重集形式提示，此处专注编号公式。
"""
import io, os, re, glob, difflib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALIAS = {
    r'\btwo': r'{\bf 2}', r'\bone': r'{\bf 1}', r'\b4': r'{\bf 4}', r'\bb4': r'{\bar\bf 4}',
    r'\k': 'b', r'\CMF': r'\cmmib F', r'\CF': r'{\cal F}', r'\VV': r'\eurm V',
    r'\CU': r'{\cal U}', r'\CA': r'{\cal A}', r'\CO': r'{\cal O}', r'\lie': r'{\cal L}',
    r'\MH': r'{\EUM}_H', r'\QQ': r'{\eurm Q}', r'\MHBAR': r'\M_H', r'\MHBARG': r'\MH(\bar G)',
}
ENV = re.compile(r'\\begin\{equation\*?\}(.*?)\\end\{equation\*?\}', re.S)
BOX = re.compile(r'\\begin\{(?:yizhu|keytakeaways)\}(?:\[[^\]]*\])?.*?\\end\{(?:yizhu|keytakeaways)\}', re.S)


def norm(x):
    x = re.sub(r'\s+', ' ', x).strip()
    for k, v in ALIAS.items():
        x = x.replace(k, v)
    return re.sub(r'\s+', ' ', x).strip()


def main():
    rows, total, bad_total = [], 0, 0
    for zp in sorted(glob.glob(os.path.join(ROOT, 'zh', '*.tex'))):
        name = os.path.basename(zp)
        sk = io.open(os.path.join(ROOT, 'skel', name), encoding='utf-8').read()
        zh = BOX.sub('', io.open(zp, encoding='utf-8').read())
        e1 = [norm(m) for m in ENV.findall(sk)]
        e2 = [norm(m) for m in ENV.findall(zh)]
        total += len(e1)
        if len(e1) != len(e2):
            rows.append((name, 'COUNT %d≠%d' % (len(e1), len(e2)), len(e1)))
            bad_total += 1
            continue
        diffs = []
        for i, (a, b) in enumerate(zip(e1, e2)):
            if a != b:
                sm = difflib.SequenceMatcher(None, a, b)
                desc = '; '.join('%s %r→%r' % (op, a[i1:i2], b[j1:j2])
                                 for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal')
                diffs.append('env#%d: %s' % (i, desc[:160]))
        if diffs:
            bad_total += 1
            rows.append((name, '%d 处差异；%s' % (len(diffs), ' | '.join(diffs[:3])), len(e1)))
        else:
            rows.append((name, '一致', len(e1)))

    out = os.path.join(ROOT, 'reports', '公式保真核查.md')
    with io.open(out, 'w', encoding='utf-8') as f:
        f.write('# 公式保真核查报告\n\n')
        f.write('工具：`tools/check_equations.py`。逐片把 `skel` 与 `zh` 的编号公式环境取出，\n'
                '做宏别名展开（`\\btwo`→`{\\bf 2}`、`\\k`→`b`、`\\MH`→`{\\EUM}_H` 等）与空白归一化后**逐字比较**。\n'
                '差异只允许是别名展开或空格；任何符号改动都会在此暴露。\n\n')
        f.write('| 分片 | 编号公式数 | 比对结果 |\n|---|---|---|\n')
        for name, res, n in rows:
            f.write('| %s | %d | %s |\n' % (name, n, res))
        f.write('\n合计：%d 片，%d 个编号公式；%d 片存在差异（见上）。\n'
                % (len(rows), total, bad_total))
    print('公式总数 %d，差异分片 %d，报告：%s' % (total, bad_total, out))


if __name__ == '__main__':
    main()
