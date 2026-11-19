# -*- coding: utf-8 -*-
"""交付前自检：黑名单、译注来源、标签一致、禁用句式、术语一致。
用法：python check.py   （在 工程文件/work/ 下运行）
"""
import io, os, re, sys, glob
sys.stdout.reconfigure(encoding='utf-8')

here = os.path.dirname(os.path.abspath(__file__))
base = os.path.abspath(os.path.join(here, '..', '..'))
src = os.path.join(base, '源码')
files = sorted(glob.glob(os.path.join(src, 'sections', '*.tex'))) + [os.path.join(src, 'main.tex')]
texts = {os.path.basename(p): io.open(p, encoding='utf-8').read() for p in files}
allt = '\n'.join(texts.values())

problems = []

# 1 黑名单
BLACK = ['知乎', '百度百科', '百度知道', 'CSDN', '简书', '公众号', '哔哩', 'bilibili', '新浪', '个人博客']
for name, t in texts.items():
    for w in BLACK:
        if w in t:
            problems.append('黑名单来源 %s: %s' % (name, w))

# 2 译注/概念卡片末句来源
for name, t in texts.items():
    for m in re.finditer(r'\\begin\{(yizhu|conceptbox)\}(?:\[[^\]]*\]|\{[^{}]*\})?(.*?)\\end\{\1\}', t, re.S):
        body = m.group(2).strip()
        if '[来源：' not in body and '[译者按' not in body:
            problems.append('缺来源标记 %s: %s' % (name, body[:40]))
        elif not re.search(r'\[(来源：|译者按).*\]\s*$', body, re.S):
            problems.append('来源标记不在末句 %s: %s' % (name, body[-40:]))

# 3 标签
clean = re.sub(r'\\verb\|[^|]*\|', '', allt)
defined = set(re.findall(r'\\label\{([^}]*)\}', clean))
refd = set(re.findall(r'\\(?:eq)?ref\{([^}]*)\}', clean))
for l in sorted(refd - defined):
    problems.append('引用未定义标签: %s' % l)
unused = sorted(defined - refd)
if unused:
    print('提示：定义了但未被引用（可接受，供外部索引）：', ', '.join(unused))

# 4 禁用句式
for pat in ['被[^。]{0,12}所', '进行[^。]{0,10}的(讨论|研究|分析)', '对于[^。]{0,12}而言']:
    for m in re.finditer(pat, allt):
        problems.append('禁用句式: %s' % m.group(0))

# 5 术语一致（附录 A vs 正文 \term）
gloss = os.path.join(here, 'glossary.tsv')
if os.path.exists(gloss):
    terms = set()
    for line in io.open(gloss, encoding='utf-8').read().splitlines()[1:]:
        parts = line.split('\t')
        if parts:
            for zh in re.split(r'[／/]', parts[0]):
                terms.add(re.sub(r'（[^）]*）', '', zh).strip())
    for m in re.finditer(r'\\term\{([^}]*)\}\{([^}]*)\}', allt):
        zh, en = m.group(1), m.group(2)
        if re.sub(r'（[^）]*）', '', zh).strip() not in terms:
            problems.append('术语未入表: %s / %s' % (zh, en))

print('\n== 检查结果 ==')
if problems:
    for p in problems:
        print('✗', p)
    print('共 %d 项问题' % len(problems))
    sys.exit(1)
print('✓ 黑名单 0 处；译注/概念卡片来源标记 100%；标签全部有定义；禁用句式 0 处；术语均有表。')
