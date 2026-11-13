# -*- coding: utf-8 -*-
"""把误插到数学模式里的全角句号 '。' 还原为 '.'。
用状态机识别：行内 $...$、行间 \\[ ... \\]、以及 equation/align/gather/multline/eqnarray 环境（含 * 版）。
"""
import sys, os, re, glob
sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"<本地路径>"
SEC = os.path.join(ROOT, "sections")
B = chr(92)

ENVS = ["equation","align","gather","multline","eqnarray","alignat","flalign"]
beg_re = re.compile("(" + re.escape(B) + r"begin\{(" + "|".join(ENVS) + r")\*?\})")
end_re = re.compile(re.escape(B) + r"end\{(" + "|".join(ENVS) + r")\*?\}")

def fix_file(path):
    t = open(path, encoding="utf-8").read()
    n = len(t)
    out = []
    i = 0
    in_disp = None       # 环境名
    in_inline = False
    in_bracket = False
    fixed = 0
    while i < n:
        # 行间环境开始
        if not in_inline and not in_disp and not in_bracket:
            m = beg_re.match(t, i)
            if m:
                out.append(m.group(1)); i = m.end(); in_disp = m.group(2); continue
            if t.startswith(B + "[", i):
                out.append(B + "["); i += 2; in_bracket = True; continue
        if in_disp:
            m = end_re.match(t, i)
            if m:
                out.append(m.group(0)); i = m.end(); in_disp = None; continue
            if t.startswith("。", i):
                out.append("."); i += 1; fixed += 1; continue
            out.append(t[i]); i += 1; continue
        if in_bracket:
            if t.startswith(B + "]", i):
                out.append(B + "]"); i += 2; in_bracket = False; continue
            if t.startswith("。", i):
                out.append("."); i += 1; fixed += 1; continue
            out.append(t[i]); i += 1; continue
        # 行内数学
        if t[i] == "$":
            if t.startswith("$$", i):
                out.append("$$"); i += 2; continue
            if i > 0 and t[i-1] == B:
                out.append("$"); i += 1; continue
            in_inline = not in_inline
            out.append("$"); i += 1; continue
        if in_inline and t.startswith("。", i):
            out.append("."); i += 1; fixed += 1; continue
        out.append(t[i]); i += 1
    if fixed:
        open(path, "w", encoding="utf-8", newline="\n").write("".join(out))
    return fixed

tot = 0
for f in sorted(glob.glob(os.path.join(SEC, "*.tex"))):
    k = fix_file(f)
    tot += k
    if k:
        print(f"  {os.path.basename(f):34s} -> 还原 {k} 处")
print("TOTAL reverted:", tot)
