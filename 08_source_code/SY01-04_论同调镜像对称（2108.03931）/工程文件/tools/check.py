#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""静态自检：LaTeX 结构、引用、标签、图文件、翻译腔禁用词。

用法：
    python tools/check.py src/chapters/ch02.tex
    python tools/check.py src            # 扫整个 src 目录（合并检查 \\ref/\\label）
"""
import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGS = os.path.join(ROOT, "figures")
# 源码目录：开发布局为 ROOT/src，交付布局为 ROOT 本身
SRC = os.path.join(ROOT, "src") if os.path.isdir(os.path.join(ROOT, "src")) else ROOT

FORBIDDEN = ["被……所", "进行……的讨论", "进行……的计算", "对于……而言", "使得……得以"]

def strip_comments(text):
    out = []
    for line in text.splitlines():
        # 去掉未转义的 %
        res, i, n = [], 0, len(line)
        while i < n:
            c = line[i]
            if c == "\\" and i + 1 < n:
                res.append(line[i:i+2]); i += 2; continue
            if c == "%":
                break
            res.append(c); i += 1
        out.append("".join(res))
    return "\n".join(out)

def check_braces(text, path, errs):
    depth = 0
    line = 1
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c == "\n":
            line += 1
        elif c == "\\" and i + 1 < n:
            i += 2; continue
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth < 0:
                errs.append(f"{path}:{line}: 多余的 '}}'")
                depth = 0
        i += 1
    if depth != 0:
        errs.append(f"{path}: 花括号不平衡（剩余 {depth} 个 '{{'）")

def check_envs(text, path, errs):
    stack = []
    for m in re.finditer(r"\\(begin|end)\{([^}]*)\}", text):
        kind, name = m.group(1), m.group(2).strip()
        line = text[:m.start()].count("\n") + 1
        if kind == "begin":
            stack.append((name, line))
        else:
            if not stack:
                errs.append(f"{path}:{line}: 多余的 \\end{{{name}}}")
            elif stack[-1][0] != name:
                errs.append(f"{path}:{line}: \\end{{{name}}} 与第 {stack[-1][1]} 行的 \\begin{{{stack[-1][0]}}} 不匹配")
                stack.pop()
            else:
                stack.pop()
    for name, line in stack:
        errs.append(f"{path}:{line}: \\begin{{{name}}} 未闭合")

def check_dollars(text, path, errs):
    # 粗检：未转义的 $ 计数应为偶数
    cnt = 0
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if c == "\\" and i + 1 < n:
            i += 2; continue
        if c == "$":
            cnt += 1
        i += 1
    if cnt % 2:
        errs.append(f"{path}: '$' 数目为奇数（{cnt}），可能行内公式未闭合")

def check_leftright(text, path, errs):
    left = len(re.findall(r"\\left(?![a-zA-Z])", text))
    right = len(re.findall(r"\\right(?![a-zA-Z])", text))
    if left != right:
        errs.append(f"{path}: \\left 与 \\right 数目不等（{left} vs {right}）")
    bl = len(re.findall(r"\\bigl", text)); br = len(re.findall(r"\\bigr", text))
    if bl != br:
        errs.append(f"{path}: \\bigl 与 \\bigr 数目不等（{bl} vs {br}）")

def collect_refs_labels(files):
    labels, refs, cites = {}, {}, {}
    for f in files:
        raw = open(f, encoding="utf-8").read()
        text = strip_comments(raw)
        for m in re.finditer(r"\\label\{([^}]*)\}", text):
            labels.setdefault(m.group(1), []).append(os.path.basename(f))
        for m in re.finditer(r"\\(?:ref|eqref|autoref|pageref)\{([^}]*)\}", text):
            refs.setdefault(m.group(1), []).append(os.path.basename(f))
        for m in re.finditer(r"\\cite\{([^}]*)\}", text):
            for k in m.group(1).split(","):
                cites.setdefault(k.strip(), []).append(os.path.basename(f))
    return labels, refs, cites

def check_file(path, labels_global, cite_keys, errs):
    raw = open(path, encoding="utf-8").read()
    text = strip_comments(raw)
    check_braces(text, path, errs)
    check_envs(text, path, errs)
    check_dollars(text, path, errs)
    check_leftright(text, path, errs)
    for bad in FORBIDDEN:
        if bad.replace("……", "") in raw or bad in raw:
            errs.append(f"{path}: 禁用翻译腔『{bad}』")
    for m in re.finditer(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", text):
        fn = m.group(1).strip()
        base = os.path.basename(fn)
        if not os.path.exists(os.path.join(FIGS, base)):
            errs.append(f"{path}: 图片不存在 figures/{base}")
    for m in re.finditer(r"\\cite\{([^}]*)\}", text):
        for k in m.group(1).split(","):
            k = k.strip()
            if cite_keys is not None and k and k not in cite_keys:
                errs.append(f"{path}: 未定义的引用键 \\cite{{{k}}}")
    # 硬编码编号（提示，不算错）
    for m in re.finditer(r"(定理|引理|命题|推论|定义|注|例)\s*\d+\.\d+", text):
        pass

def main():
    args = sys.argv[1:]
    if not args:
        args = [SRC]
    targets = []
    for a in args:
        if os.path.isdir(a):
            targets += sorted(glob.glob(os.path.join(a, "**", "*.tex"), recursive=True))
        else:
            targets.append(a)
    # 全局标签与文献键
    src_dir = SRC
    all_tex = sorted(glob.glob(os.path.join(src_dir, "**", "*.tex"), recursive=True))
    labels, refs, cites = collect_refs_labels(all_tex)
    cite_keys = set()
    refs_tex = os.path.join(src_dir, "refs.tex")
    if os.path.exists(refs_tex):
        for m in re.finditer(r"\\bibitem\[[^\]]*\]\{([^}]*)\}", open(refs_tex, encoding="utf-8").read()):
            cite_keys.add(m.group(1))
    errs = []
    for t in targets:
        if not os.path.exists(t):
            errs.append(f"{t}: 文件不存在")
            continue
        check_file(t, labels, cite_keys, errs)
    # 全局
    for r, fs in refs.items():
        if r not in labels:
            errs.append(f"未定义的 \\ref{{{r}}}（出现在 {sorted(set(fs))}）")
    for lab, fs in labels.items():
        if len(fs) > 1:
            errs.append(f"重复的 \\label{{{lab}}}（{fs}）")
    if cite_keys:
        for c, fs in cites.items():
            if c and c not in cite_keys:
                errs.append(f"未定义的文献键 {c}（{sorted(set(fs))}）")
    print(f"扫描 {len(targets)} 个文件；标签 {len(labels)} 个；引用 {len(refs)} 个；文献键 {len(cites)} 个")
    if errs:
        print(f"发现 {len(errs)} 个问题：")
        for e in errs:
            print("  -", e)
        sys.exit(1)
    print("OK 静态检查通过")

if __name__ == "__main__":
    main()
