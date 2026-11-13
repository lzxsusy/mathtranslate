# -*- coding: utf-8 -*-
"""chunks 自检：编号公式、环境配对、文件编码、禁则写法。"""
import re, sys, io, os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
CH = os.path.join(ROOT, 'src', 'chunks')
EXPECT_TAGS = [str(i) for i in range(1, 28)]
EXPECT_SECTIONS = 5   # 第 1–5 节；参考文献用 \section*

errors, warns = [], []

files = sorted(glob.glob(os.path.join(CH, 'c*.tex')))
if not files:
    print('未找到 chunks'); sys.exit(1)

all_tags = []
for path in files:
    name = os.path.basename(path)
    raw = open(path, 'rb').read()
    if raw.startswith(b'\xef\xbb\xbf'):
        errors.append(f'{name}: 含 UTF-8 BOM')
    if b'\r' in raw:
        errors.append(f'{name}: 含 CR（须为 LF）')
    txt = raw.decode('utf-8')

    # 环境配对
    stack = []
    for m in re.finditer(r'\\(begin|end)\{([^}]*)\}', txt):
        kind, env = m.group(1), m.group(2)
        if kind == 'begin':
            stack.append(env)
        else:
            if not stack:
                errors.append(f'{name}: 多余的 \\end{{{env}}}')
            elif stack[-1] != env:
                errors.append(f'{name}: 环境错配 \\end{{{env}}}（栈顶 {stack[-1]}）')
                stack.pop()
            else:
                stack.pop()
    for env in stack:
        errors.append(f'{name}: \\begin{{{env}}} 未闭合')

    # 编号公式
    tags = re.findall(r'<本地路径>]*)\}', txt)
    all_tags += tags
    if '\\begin{equation}' in txt and '\\tag' not in txt:
        warns.append(f'{name}: 有 equation 环境但无 \\tag')

    # 禁用写法
    for pat, msg in [(r'\\documentclass', 'chunks 内不得有 \\documentclass'),
                     (r'\\usepackage', 'chunks 内不得有 \\usepackage'),
                     (r'<本地路径>', 'chunks 内不得有 document 环境'),
                     (r'<本地路径>', '用纯文本 [AAK]，不要 \\cite'),
                     (r'<本地路径>', '用纯文本式号，不要 \\ref'),
                     (r'<本地路径>', '不要 \\label'),
                     (r'\*\*', '残留 markdown 粗体'),
                     (r'^#+\s', '残留 markdown 标题'),
                     (r'```', '残留 markdown 代码块')]:
        if re.search(pat, txt, re.M):
            errors.append(f'{name}: {msg}')

    # 行内/行间数学里的全角标点
    for m in re.finditer(r'(?<!\\)\$(.+?)(?<!\\)\$', txt, re.S):
        seg = m.group(1)
        bad = [c for c in seg if c in '，。；：（）「」、']
        if bad:
            errors.append(f'{name}: 数学模式内出现全角标点 {bad}：{seg[:40]}')
    # 美元符号成对（粗检）
    for i, line in enumerate(txt.split('\n'), 1):
        if re.search(r'(?<!\\)\$', line) and (len(re.findall(r'(?<!\\)\$', line)) % 2 == 1):
            if '\\[' not in line and '\\]' not in line:
                warns.append(f'{name}:{i}: 该行 $ 数为奇数（跨行公式请确认）')
    # 每页标记
    print('{}: tags={} sections={}'.format(
        name, len(tags), len(re.findall(r'^<本地路径>', txt, re.M))))

secs = sum(len(re.findall(r'^<本地路径>', open(p, encoding='utf-8').read(), re.M)) for p in files)
if secs != EXPECT_SECTIONS:
    errors.append(f'\\section 数量 = {secs}，期望 {EXPECT_SECTIONS}')
if sorted(all_tags, key=lambda s: (len(s), s)) != EXPECT_TAGS:
    missing = [t for t in EXPECT_TAGS if t not in all_tags]
    dup = [t for t in set(all_tags) if all_tags.count(t) > 1]
    extra = [t for t in all_tags if t not in EXPECT_TAGS]
    if missing: errors.append(f'缺编号公式：{missing}')
    if dup:     errors.append(f'重复编号：{dup}')
    if extra:   errors.append(f'多出编号：{extra}')
else:
    # 顺序检查（跨文件按文件名 c00.. 拼接）
    nums = [int(t) for t in all_tags]
    if nums != sorted(nums):
        errors.append(f'编号公式顺序错乱：{nums}')

for e in errors: print('ERROR', e)
for w in warns:  print('WARN ', w)
print(f'--- {len(errors)} errors, {len(warns)} warnings ---')
sys.exit(1 if errors else 0)
