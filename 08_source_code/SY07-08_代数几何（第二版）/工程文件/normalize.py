# -*- coding: utf-8 -*-
"""SY07-08 术语/索引键统一脚本。用法: python normalize.py [--apply]
默认 dry-run，只打印将要发生的替换计数。"""
import glob
import os
import re
import sys

ROOT = r"C:\Users\admin\Desktop\数译发布\shuyi\translations\SY07-08\源码\chunks"
APPLY = "--apply" in sys.argv
SKIP = {"c16", "c17", "c18", "c19"}  # 仍在翻译/重写中的块

# (名称, 正则, 替换)
RULES = [
    ("删除重复索引键 huankongjian", r"\\idx\{huankongjian\}\{环空间\}", ""),
    ("删除自造别名「或基扩张」", r"或基扩张", ""),
    ("前层→预层（presheaf 标准译名）", r"前层", "预层"),
    ("环空间→环层空间", r"环空间", "环层空间"),
    ("Noetherian→诺特", r"Noetherian", "诺特"),
    ("Noether→诺特", r"Noether", "诺特"),
    ("定向集→有向集", r"定向集", "有向集"),
    ("正向系统→有向系统", r"正向系统", "有向系统"),
    ("正向极限→有向极限", r"正向极限", "有向极限"),
    ("逆向系→逆向系统", r"逆向系(?!统)", "逆向系统"),
    ("相联系的层→相伴的层", r"相联系的层", "相伴的层"),
    ("笛卡尔方图→笛卡尔图", r"笛卡尔方图", "笛卡尔图"),
    ("ASCII Cech→\\v{C}ech", r"(?<!\\v\{)Cech", r"\\v{C}ech"),
    # 索引键规范化
    ("idx 支集 zhiji→zhiji2", r"\\idx\{zhiji\}\{支集\}", r"\\idx{zhiji2}{支集}"),
    ("idx 拟紧态射 nijin→nijintaishe", r"\\idx\{nijin\}\{拟紧态射\}", r"\\idx{nijintaishe}{拟紧态射}"),
    ("idx OX-模", r"\\idx\{OXmo\}", r"\\idx{oxmo}"),
    ("idx S-态射", r"\\idx\{S-taishe\}", r"\\idx{staishe}"),
    ("idx Segre 嵌入", r"\\idx\{Segreyuqianru\}", r"\\idx{segreyuqianru}"),
    ("idx S-概形", r"\\idx\{Sgaixing\}", r"\\idx{sgaixing}"),
    ("idx Picard 群", r"\\idx\{Picardqun\}", r"\\idx{picardqun}"),
    ("idx Čech 上同调群拼写", r"cechshangtongtiaoqun", "cechshangtongdiaoqun"),
    ("idx 素除子拼写", r"succhuzi", "suchuzi"),
    ("idx 平坦的→平坦态射", r"\{(平坦的)\}", "{平坦态射}"),
]

files = sorted(glob.glob(os.path.join(ROOT, "c*.tex")))
total = {}
changed_files = []
for f in files:
    name = os.path.basename(f)[:-4]
    if name in SKIP:
        continue
    s = open(f, encoding="utf-8").read()
    orig = s
    per = []
    for label, pat, rep in RULES:
        s2, n = re.subn(pat, rep, s)
        if n:
            per.append((label, n))
            total[label] = total.get(label, 0) + n
        s = s2
    if s != orig:
        changed_files.append((name, per))
        if APPLY:
            open(f, "w", encoding="utf-8", newline="\n").write(s)

print(("APPLIED" if APPLY else "DRY-RUN") + f"  files changed: {len(changed_files)}")
for name, per in changed_files:
    print(f"  {name:6s} " + ", ".join(f"{l}:{n}" for l, n in per))
print("\n--- totals ---")
for k, v in sorted(total.items(), key=lambda x: -x[1]):
    print(f"  {v:4d}  {k}")
