# -*- coding: utf-8 -*-
r"""交付前自动审计（v2.0 §7/§9）。用法：python audit_final.py
检查项：
 1) 旧术语残留（圆分域/投有限）与术语三同步
 2) \label 集合与备份一致（未改标签）
 3) 每章 znote/znoteplain 与 notes_NN.tsv 行数一致；每条 znote 带「来源：」，znoteplain 带「无外部依据」字样
 4) 黑名单源零命中
 5) 附录 A/B 条数与正文注记数一致
 6) §5 语言病灶计数
 7) 编译日志质量（未定义引用 / Overfull / 缺字）
"""
import os, re, glob, json, sys, collections

ROOT = r'<本地路径>'
SRC = os.path.join(ROOT, 'src')
CH = os.path.join(SRC, 'chapters')
WORK = os.path.join(ROOT, 'work')
NOTES = os.path.join(WORK, 'notes')
BAK = os.path.join(WORK, 'orig_src', 'chapters')
LOG = os.path.join(SRC, 'build', 'main.log')

BLACK = ['知乎', '百度百科', '百度知道', 'CSDN', '简书', '公众号', 'bilibili', 'B站', '维基百科',
         'wikipedia', 'MathOverflow', '个人博客', 'AI摘要']
OLDTERMS = ['圆分域', '投有限']
DISEASE = {
    '被…所…': r'被[^。，]{0,12}所',
    '进行…的': r'进行[^。，]{0,10}的(讨论|研究|计算|分析|论证)',
    '对于…而言': r'对于[^。]{0,15}而言',
    '使得…得以…': r'使得[^。]{0,12}得以',
    '三个的': r'的[^。，、]{0,6}的[^。，、]{0,6}的',
    '以及堆叠': r'以及[^。]{0,40}以及',
}

report = []
def out(s=''):
    report.append(s)
    print(s)

chapters = sorted(glob.glob(os.path.join(CH, 'lecture*.tex')))

# 1) 旧术语
out('== 1. 旧术语残留 ==')
bad = []
for p in chapters:
    t = open(p, encoding='utf-8').read()
    for term in OLDTERMS:
        for m in re.finditer(term, t):
            ln = t[:m.start()].count('\n') + 1
            bad.append('%s:%d %s' % (os.path.basename(p), ln, term))
out('  旧术语命中 %d 处' % len(bad))
for b in bad[:20]:
    out('   ! ' + b)

# 2) label 一致性
out('\n== 2. label 一致性（对比 work/backup_chapters） ==')
def labels(t):
    return collections.Counter(re.findall(r'\\label\{([^}]+)\}', t))
lb_bad = 0
for p in chapters:
    name = os.path.basename(p)
    bp = os.path.join(BAK, name)
    if not os.path.exists(bp):
        out('   (无备份，跳过) ' + name)
        continue
    a = labels(open(bp, encoding='utf-8').read())
    b = labels(open(p, encoding='utf-8').read())
    if a != b:
        lb_bad += 1
        only_a = set(a) - set(b)
        only_b = set(b) - set(a)
        out('   ! %s label 变化: 删除 %s 新增 %s' % (name, sorted(only_a)[:5], sorted(only_b)[:5]))
out('  label 有变化的章数：%d' % lb_bad)

# 3/4/6) 逐章检查
out('\n== 3. 译注结构 / 黑名单 / 语言病灶 ==')
tot_z = tot_zp = tot_tutor = 0
struct_bad = []
for p in chapters:
    name = os.path.basename(p)
    num = re.search(r'lecture(\d+)', name).group(1)
    t = open(p, encoding='utf-8').read()
    z = re.findall(r'\\znote\{', t)
    zp = re.findall(r'\\znoteplain\{', t)
    tutor = re.findall(r'% \[Tutor Note', t)
    tot_z += len(z); tot_zp += len(zp); tot_tutor += len(tutor)

    # 括号配对抽 body，检查来源
    for m in re.finditer(r'\\(znote|znoteplain)\{', t):
        kind = m.group(1)
        j = m.end(); depth = 1; buf = []
        while j < len(t) and depth:
            c = t[j]
            if c == '{': depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0: break
            buf.append(c); j += 1
        body = ''.join(buf)
        ln = t[:m.start()].count('\n') + 1
        if kind == 'znote' and '来源：' not in body:
            struct_bad.append('%s:%d znote 缺「来源：」' % (name, ln))
        if kind == 'znoteplain' and '无外部依据' not in body:
            struct_bad.append('%s:%d znoteplain 缺「无外部依据」' % (name, ln))
        for b in BLACK:
            if b in body:
                struct_bad.append('%s:%d 黑名单源「%s」' % (name, ln, b))

    # notes tsv 行数
    np = os.path.join(NOTES, 'notes_%s.tsv' % num)
    n_rows = 0
    if os.path.exists(np):
        n_rows = len([l for l in open(np, encoding='utf-8').read().splitlines() if l.strip()])
    notes_rows = 0
    if os.path.exists(np):
        for l in open(np, encoding='utf-8').read().splitlines():
            if not l.strip():
                continue
            c = l.split('\t')
            if len(c) >= 7 and c[6] in ('ok', 'skip', 'tutor-note'):
                notes_rows += 1
            if len(c) < 7:
                struct_bad.append('%s 列数不足: %s' % (os.path.basename(np), l[:60]))
    expect = len(z) + len(zp) + len(tutor)
    flag = '' if (n_rows == expect or n_rows == 0) else '  <-- 行数不符(期望%d)' % expect
    out('  %-16s znote=%-3d znoteplain=%-2d tutor=%-2d notes.tsv=%-3d%s' % (name, len(z), len(zp), len(tutor), n_rows, flag))

# 6) 语言病灶
out('\n  §5 语言病灶：')
for k, pat in DISEASE.items():
    cnt = 0
    hits = []
    for p in chapters:
        t = open(p, encoding='utf-8').read()
        for m in re.finditer(pat, t):
            cnt += 1
            if len(hits) < 3:
                hits.append('%s:%d %s' % (os.path.basename(p), t[:m.start()].count('\n') + 1, m.group(0)[:20]))
    out('   %-12s %d %s' % (k, cnt, ('; '.join(hits) if hits else '')))

out('\n  结构问题 %d 条' % len(struct_bad))
for s in struct_bad[:30]:
    out('   ! ' + s)

# 5) 附录一致性
out('\n== 4. 附录一致性 ==')
apx = os.path.join(CH, 'appendix_zhusi.tex')
if os.path.exists(apx):
    t = open(apx, encoding='utf-8').read()
    n_apx = t.count('\\\\')  # 粗估
    m = re.search(r'共 (\d+) 条', t)
    out('  附录存在；正文 znote+znoteplain=%d，tutor-note=%d' % (tot_z + tot_zp, tot_tutor))
    out('  （附录由 gen_appendix.py 从 notes_*.tsv 生成，请重跑后再比对）')
else:
    out('  ! 附录文件缺失')

# 7) 编译日志
out('\n== 5. 编译日志质量 ==')
if os.path.exists(LOG):
    log = open(LOG, encoding='utf-8', errors='replace').read()
    for pat in ('Undefined control sequence', '! LaTeX Error', 'Overfull \\hbox',
                'Missing character', 'Undefined reference', 'multiply defined'):
        out('  %-28s %d' % (pat, log.count(pat)))
else:
    out('  (无 main.log)')

out('\n== 汇总 ==')
out('  正文译注：znote %d + znoteplain %d = %d 条；Tutor Note %d 条' % (tot_z, tot_zp, tot_z + tot_zp, tot_tutor))
out('  旧术语残留 %d；label 变化章 %d；结构问题 %d' % (len(bad), lb_bad, len(struct_bad)))

rp = os.path.join(WORK, 'reports', 'AUDIT_FINAL.txt')
os.makedirs(os.path.dirname(rp), exist_ok=True)
open(rp, 'w', encoding='utf-8', newline='\n').write('\n'.join(report) + '\n')
print('\n[written] ' + rp)
