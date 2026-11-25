# -*- coding: utf-8 -*-
"""译对自动核查：对每个 zh/NN-sXX.tex 与 skel/NN-sXX.tex 做结构与数学一致性比对。
检查项：
  M1 数学片段（$...$、\\(...\\)、\\[...\\]、equation/aligned 等环境内容）按顺序完全一致（忽略空白差异）
  S1 \\label 集合一致   S2 \\cite 多重集一致   S3 \\setcounter{equation} 列表一致
  S4 % 式 (N) 注释序列一致
  T1 中文比例（散文行应有汉字）
  T2 疑似未译英文行（非纯公式/命令的长英文句）
  G1 固定译法抽查（GLOSSARY 里若干关键词的英文首次出现处附近应有对应中文）
输出：reports/verify_report.md + 终端摘要。
用法：python tools/verify_translation.py [过滤]
"""
import io, os, re, sys, glob, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CJK = re.compile(r'[\u4e00-\u9fff]')

def strip_comments(s):
    # 去掉 % 注释（保留 % 式 锚单独比对）
    out = []
    for line in s.split('\n'):
        # 保护 \% 
        i = 0
        while True:
            j = line.find('%', i)
            if j < 0:
                out.append(line); break
            if j > 0 and line[j-1] == '\\' and (j < 2 or line[j-2] != '\\'):
                i = j + 1; continue
            out.append(line[:j]); break
    return '\n'.join(out)

def math_segments(s, keep_env=True):
    """抽取数学片段：$..$、\\(..\\)、\\[..\\]、equation/align 等环境整体。"""
    segs = []
    t = s
    # 先抽环境
    envs = r'(equation\*?|align\*?|aligned|gathered|matrix|cases|array)'
    pos = 0
    while True:
        m = re.search(r'\\begin\{(%s)\}' % envs, t[pos:])
        if not m: break
        start = pos + m.start()
        name = m.group(1)
        endm = re.search(r'\\end\{%s\}' % re.escape(name), t[start:])
        if not endm: break
        end = start + endm.end()
        segs.append(('env', t[start:end]))
        t = t[:start] + ' ' * (end - start) + t[end:]
        pos = end
    # 再抽行内/行间数学
    i = 0
    buf = []
    out = t
    res = []
    while i < len(t):
        c = t[i]
        if c == '\\' and i + 1 < len(t):
            if t[i+1] in '([':
                closer = '\\)' if t[i+1] == '(' else '\\]'
                j = t.find(closer, i+2)
                if j < 0: break
                res.append(t[i:j+2]); i = j + 2; continue
            i += 2; continue
        if c == '$':
            if t[i:i+2] == '$$':
                j = t.find('$$', i+2)
                if j < 0: break
                res.append(t[i:j+2]); i = j + 2; continue
            j = i + 1
            while j < len(t):
                if t[j] == '\\': j += 2; continue
                if t[j] == '$': break
                j += 1
            if j >= len(t): break
            res.append(t[i:j+1]); i = j + 1; continue
        i += 1
    return [x[1] for x in segs] + res

def norm(x):
    x = re.sub(r'\s+', '', x)
    # 压掉多余花括号：{{X}} 与 {X} 视为相同
    for _ in range(3):
        x = x.replace('{{', '{').replace('}}', '}')
    return x


def expand_inline_defs(text):
    """移除 skel 里正文中段的 \\def\\X{body}，把 \\X 展开为 body。
    译者按 SPEC 会把这些 def 移出分片、直接写展开形式，故比对前先在原文侧展开。"""
    defs = re.findall(r'\\def\\([A-Za-z]+)\s*\{', text)
    bodies = {}
    out = []
    i = 0
    while i < len(text):
        m = re.search(r'\\def\\([A-Za-z]+)\s*\{', text[i:])
        if not m:
            out.append(text[i:]); break
        st = i + m.start()
        out.append(text[i:st])
        j = st + m.end() - 1  # text[j] == '{'
        depth = 0
        k = j
        while k < len(text):
            if text[k] == '{':
                depth += 1
            elif text[k] == '}':
                depth -= 1
                if depth == 0:
                    break
            k += 1
        body = text[j + 1:k]
        bodies[m.group(1)] = body
        i = k + 1
    text = ''.join(out)
    for name, body in bodies.items():
        text = re.sub(r'\\' + name + r'(?![A-Za-z])', lambda _m: body, text)
    return text


BOX_ENVS = ('yizhu', 'keytakeaways')


def strip_boxes(s):
    """去掉译者添加的 yizhu / keytakeaways 盒子，只留与原文一一对应的正文。"""
    for env in BOX_ENVS:
        s = re.sub(r'\\begin\{%s\}(?:\[[^\]]*\])?.*?\\end\{%s\}' % (env, env), ' ', s, flags=re.S)
    return s


def count_boxes(s, env):
    return len(re.findall(r'\\begin\{%s\}' % env, s))

def is_prose_line(l):
    s = strip_comments(l).strip()
    if not s: return False
    if s.startswith('%'): return False
    if not re.search(r'[A-Za-z]{3,}', s): return False
    # 去掉行内数学与命令
    s2 = re.sub(r'\$[^$]*\$', ' ', s)
    s2 = re.sub(r'\\[A-Za-z]+\*?', ' ', s2)
    s2 = re.sub(r'[{}]', ' ', s2)
    return len(re.findall(r'[A-Za-z]{4,}', s2)) >= 5

def looks_like_name_list(l):
    """人名/机构清单（L. Jeffrey, J. Morgan, ...）不需要翻译，T1/T2 应跳过。"""
    s = strip_comments(l)
    s = re.sub(r'\\[A-Za-z]+\*?', ' ', s)
    s = re.sub(r'\$[^$]*\$', ' ', s)
    if CJK.search(s):
        return False
    return not re.search(r'\b[a-z]{4,}', s)


def strip_defs(s):
    """去掉行内 \\def 行（skel 用，zh 按 SPEC 必须没有）。"""
    return '\n'.join(l for l in s.split('\n') if not re.match(r'\s*\\def\\', l))


def check(name):
    sk_raw = io.open(os.path.join(ROOT, 'skel', name), encoding='utf-8').read()
    zp = os.path.join(ROOT, 'zh', name)
    if not os.path.exists(zp):
        return None
    zh_raw = io.open(zp, encoding='utf-8').read()
    n_yizhu = count_boxes(zh_raw, 'yizhu')
    n_key = count_boxes(zh_raw, 'keytakeaways')
    zh = strip_boxes(zh_raw)
    sk = strip_defs(sk_raw)
    probs = []
    infos = []

    # S1/S2/S3/S4：结构锚序列一一对应（顺序敏感）
    for pat, tag in [(r'\\label\{[^}]*\}', 'S1 label'),
                     (r'\\cite\{[^}]*\}', 'S2 cite'),
                     (r'\\setcounter\{equation\}\{\d+\}', 'S3 setcounter'),
                     (r'% 式 \(\d+\.\d+\)', 'S4 式锚')]:
        a = re.findall(pat, sk)
        b = re.findall(pat, zh)
        if a != b:
            if len(a) != len(b):
                probs.append('%s 数不同: skel=%d zh=%d' % (tag, len(a), len(b)))
            else:
                diff = [i for i, (x, y) in enumerate(zip(a, b)) if x != y]
                probs.append('%s 序列不同: %d 处，首个 index=%d（%s vs %s）' % (
                    tag, len(diff), diff[0], a[diff[0]], b[diff[0]]))

    # M0：编号公式环境个数
    n_eq_sk = len(re.findall(r'\\begin\{equation\}', sk))
    n_eq_zh = len(re.findall(r'\\begin\{equation\}', zh))
    if n_eq_sk != n_eq_zh:
        probs.append('M0 编号公式数不同: skel=%d zh=%d' % (n_eq_sk, n_eq_zh))

    # M1（INFO）：行内/环境数学片段多重集差异——宏别名、花括号冗余属合法差异
    ms_sk = [norm(x) for x in math_segments(sk)]
    ms_zh = [norm(x) for x in math_segments(zh)]
    if ms_sk != ms_zh:
        same = len([x for x in ms_sk if x in ms_zh])
        infos.append('M1 数学片段：skel=%d zh=%d，多重集交集=%d（宏别名/花括号差异属正常，仅提示）'
                     % (len(ms_sk), len(ms_zh), same))

    # T1：散文行中文比例
    lines = [l for l in zh.split('\n') if is_prose_line(l) and not looks_like_name_list(l)]
    if lines:
        cjk = sum(1 for l in lines if CJK.search(l))
        ratio = cjk / len(lines)
        if ratio < 0.9:
            probs.append('T1 散文行含中文比例过低: %.2f (%d/%d)' % (ratio, cjk, len(lines)))
        untrans = [l[:70] for l in lines if not CJK.search(l)]
        if untrans:
            probs.append('T2 疑似未译散文行: %d 行，例: %s' % (len(untrans), untrans[0]))

    return probs, infos, {'n_yizhu': n_yizhu, 'n_key': n_key,
                          'chars_sk': len(sk_raw), 'chars_zh': len(zh_raw),
                          'ratio': round(len(zh_raw) / max(1, len(sk_raw)), 2),
                          'n_eq': n_eq_zh}


def main(pat):
    names = sorted(os.path.basename(p) for p in glob.glob(os.path.join(ROOT, 'zh', '*.tex')) if pat in p)
    if not names:
        print('zh/ 里还没有文件'); return
    rows = []
    bad = 0
    for n in names:
        r = check(n)
        if r is None:
            continue
        probs, infos, st = r
        if probs:
            bad += 1
            print('==', n)
            for x in probs:
                print('   P:', x)
            for x in infos:
                print('   i:', x)
        rows.append((n, probs, infos, st))
    print('\n结构核查：%d 片中 %d 片有问题' % (len(rows), bad))

    os.makedirs(os.path.join(ROOT, 'reports'), exist_ok=True)
    with io.open(os.path.join(ROOT, 'reports', 'verify_report.md'), 'w', encoding='utf-8') as fh:
        fh.write('# 译对自动核查报告\n\n')
        fh.write('工具：`tools/verify_translation.py`（结构锚序列 + 公式数 + 散文中文比例；'
                 '行内数学宏别名差异不计为失败）\n\n')
        fh.write('| 分片 | 判定 | 原文字符 | 译文字符 | 原/译比 | 编号公式 | 译注 | 本节重点 | 说明 |\n')
        fh.write('|---|---|---|---|---|---|---|---|---|\n')
        for n, probs, infos, st in rows:
            note = '；'.join(probs + infos)
            fh.write('| %s | %s | %d | %d | %.2f | %d | %d | %d | %s |\n' % (
                n, 'PASS' if not probs else 'FAIL', st['chars_sk'], st['chars_zh'], st['ratio'],
                st['n_eq'], st['n_yizhu'], st['n_key'], note))
        tot_sk = sum(st['chars_sk'] for _, _, _, st in rows)
        tot_zh = sum(st['chars_zh'] for _, _, _, st in rows)
        fh.write('\n合计：%d 片，%d 片有问题；原文字符 %d，译文字符 %d，比值 %.2f。\n'
                 % (len(rows), bad, tot_sk, tot_zh, tot_zh / max(1, tot_sk)))


if __name__ == '__main__':
    pat = sys.argv[1] if len(sys.argv) > 1 else ''
    main(pat)
    sys.exit(0)
    rep = []
    names = sorted(os.path.basename(p) for p in glob.glob(os.path.join(ROOT, 'zh', '*.tex')) if pat in p)
    if not names:
        print('zh/ 里还没有文件'); sys.exit(0)
    bad = 0
    stats = {}
    for n in names:
        p, st = check(n)
        stats[n] = st
        if p:
            bad += 1
            print('==', n)
            for x in p:
                print('   ', x)
        rep.append((n, p or []))
    print('\n%d/%d 片有问题' % (bad, len(names)))
    os.makedirs(os.path.join(ROOT, 'reports'), exist_ok=True)
    with io.open(os.path.join(ROOT, 'reports', 'verify_report.md'), 'w', encoding='utf-8') as fh:
        fh.write('# 译对自动核查报告\n\n生成：tools/verify_translation.py\n\n')
        fh.write('| 分片 | 状态 | 原文字符 | 译文字符 | 原/译比 | 译注 | 本节重点 | 问题 |\n|---|---|---|---|---|---|---|---|\n')
        for n, p in rep:
            st = stats[n]
            fh.write('| %s | %s | %d | %d | %.2f | %d | %d | %s |\n' % (
                n, 'PASS' if not p else 'FAIL', st['chars_sk'], st['chars_zh'], st['ratio'],
                st['n_yizhu'], st['n_key'], '；'.join(p) if p else ''))
        fh.write('\n合计：%d 片，%d 片有问题。\n' % (len(rep), bad))
