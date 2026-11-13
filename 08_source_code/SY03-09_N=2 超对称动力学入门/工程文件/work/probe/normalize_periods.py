# -*- coding: utf-8 -*-
"""全角句号归一（草稿正文用半角 '.' 作汉语句号）——先 dry-run 统计，再落盘。
规则：把「中文/闭括号/引号/行内数学 $...$ / \\cite{} \\ref{} \\eqref{} 等右花括号」之后的
'.' + 空白 改为 '。' + 空白；不动小数（1.5）、缩写（i.e. / e.g. / Fig.）、URL、作者缩写。
"""
import sys, os, re, glob, shutil
sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"<本地路径>"
SEC = os.path.join(ROOT, "sections")
APPLY = ("--apply" in sys.argv)

CJK = r"\u4e00-\u9fff"
# 前一个字符允许集合：汉字、全角闭括号/引号、$（行内数学末尾）、}（命令参数末尾）、）】”」』
PRE = re.compile(r"([" + CJK + r"）】”」』\$}])\.(?=\s)")
# 统计：'.' 前的字符类型
def prev_char_kind(t, i):
    if i <= 0: return "BOF"
    c = t[i-1]
    if re.match("[" + CJK + "]", c): return "CJK"
    if c in "）】”」』": return "CJKCLOSE"
    if c == "$": return "MATH$"
    if c == "}": return "BRACE}"
    if c == ")": return "paren)"
    if c.isdigit(): return "digit"
    if c.isalpha(): return "alpha"
    return "other:" + c

files = sorted(glob.glob(os.path.join(SEC, "*.tex")))
total = {}
per_file = {}
for f in files:
    t = open(f, encoding="utf-8").read()
    kinds = {}
    for m in re.finditer(r"\.(?=\s)", t):
        k = prev_char_kind(t, m.start())
        kinds[k] = kinds.get(k, 0) + 1
        total[k] = total.get(k, 0) + 1
    per_file[os.path.basename(f)] = kinds

print("=== '.'+空白 的前置字符类型统计 ===")
for k, v in sorted(total.items(), key=lambda kv: -kv[1]):
    print(f"  {k:12s} {v:5d}")
print("\n每文件（只列 CJK / CJKCLOSE / MATH$ / BRACE} 四类）:")
for name, kinds in per_file.items():
    print(f"  {name:34s} CJK={kinds.get('CJK',0):4d} close={kinds.get('CJKCLOSE',0):3d} math={kinds.get('MATH$',0):4d} brace={kinds.get('BRACE}',0):3d}")

if APPLY:
    # 备份
    bak = os.path.join(ROOT, "work", "tmp", "sections_bak_semicolon")
    if not os.path.exists(bak):
        shutil.copytree(SEC, bak)
    tot = 0
    for f in files:
        t = open(f, encoding="utf-8").read()
        t2, n = PRE.subn(lambda m: m.group(1) + "。", t)
        if n:
            open(f, "w", encoding="utf-8", newline="\n").write(t2)
        tot += n
        print(f"  {os.path.basename(f):34s} -> {n} 处")
    print("TOTAL converted:", tot)
