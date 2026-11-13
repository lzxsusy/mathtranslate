# -*- coding: utf-8 -*-
"""把中文句末的半角 '.' 归一为全角 '。'（只处理文字性位置，不动数学环境内的句点）。
安全集合：前一个字符属于 [汉字 （ ） 】 ” 」 』 $ }]，其中 $ 表示行内数学结尾、} 表示 \\cite{...} 等命令结尾。
"""
import sys, os, re, glob, shutil
sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"<本地路径>"
SEC = os.path.join(ROOT, "sections")
CJK = r"\u4e00-\u9fff"
PRE_CAP = "([" + CJK + "）】”」』$}])"

bak = os.path.join(ROOT, "work", "tmp", "sections_backup_before_punct")
if not os.path.exists(bak):
    shutil.copytree(SEC, bak)
    print("backup ->", bak)

files = sorted(glob.glob(os.path.join(SEC, "*.tex")))
tot = 0
for f in files:
    t = open(f, encoding="utf-8").read()
    # (1) 句点后跟空格 → '。'（去掉空格）
    t, n1 = re.subn(PRE_CAP + r"\.([ \t]+)", r"\1。", t)
    # (2) 句点后直接换行 → '。' + 换行
    t, n2 = re.subn(PRE_CAP + r"\.(\r?\n)", r"\1。\2", t)
    if n1 + n2:
        open(f, "w", encoding="utf-8", newline="\n").write(t)
    tot += n1 + n2
    print(f"  {os.path.basename(f):34s} 空格后={n1:4d}  换行={n2:3d}")
print("TOTAL:", tot)
