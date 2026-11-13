# -*- coding: utf-8 -*-
"""qa_scan.py — 全书 QA 扫描（Lead 用；找"看得见但不会编译失败"的问题）

检查项：
 1. 数学里的英文 \text{...}（正文已译而公式内仍是英文 → 一致性瑕疵）
 2. 未翻译的整段英文（启发式：非注释、非数学、连续 60+ 字符以 ASCII 字母为主）
 3. \[ ... \] 里出现 \tag
 4. \eqref / \ref / \cite / \label 误用
 5. markdown 粗体 **
 6. 连续两个以上空格、行尾空格
 7. 批注里未成对的 $
 8. 常见的"中文夹半角标点"问题：中文字符后紧跟 , ; : ? ! 未用全角
"""
import glob, os, re, sys

ROOT = r"<本地路径>"


def strip_math(s):
    return re.sub(r"[$].*?[$]", lambda m: " ", s, flags=re.S)


def body_only(s):
    """去掉注释行"""
    return "\n".join(l for l in s.splitlines() if not l.lstrip().startswith("%"))


def has_cjk(s):
    return re.search(r"[\u4e00-\u9fff]", s) is not None


for f in sorted(glob.glob(os.path.join(ROOT, "src", "sec*.tex"))) + [os.path.join(ROOT, "src", "refs.tex")]:
    if not os.path.exists(f) or os.path.getsize(f) < 100:
        continue
    name = os.path.basename(f)
    s = open(f, encoding="utf-8").read()
    body = body_only(s)
    issues = []

    # 1. 数学里的英文 \text
    for m in re.finditer(r"<本地路径>]*)\}", body):
        if re.search(r"[A-Za-z]{3,}", m.group(1)):
            issues.append("数学内英文 \\text{%s}" % m.group(1)[:40])

    # 2. 未翻译英文整句
    for line in body.splitlines():
        t = strip_math(line)
        t = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^{}]*\})?", " ", t)
        t = re.sub(r"%.*", "", t)
        letters = len(re.findall(r"[A-Za-z]", t))
        cjk = len(re.findall(r"[\u4e00-\u9fff]", t))
        words = re.findall(r"[A-Za-z]{2,}", t)
        if letters > 70 and cjk == 0 and len(words) > 12:
            issues.append("疑似未译英文行：「%s」" % line.strip()[:70])
        elif letters > 90 and cjk < 10 and len(words) > 15:
            issues.append("疑似半未译行：「%s」" % line.strip()[:70])

    # 3. \[ \] 里有 tag
    for m in re.finditer(r"\\\[(.{0,600}?)\\\]", body, re.S):
        if "\\tag{" in m.group(1):
            issues.append("\\[ \\] 里出现 \\tag")

    # 4. eqref/ref/cite/label
    for cmd in ("\\eqref", "\\ref", "\\cite", "\\label"):
        if cmd in body:
            issues.append("误用 %s" % cmd)

    # 5. markdown 粗体
    if re.search(r"\*\*[^*\n]+\*\*", body):
        issues.append("markdown **粗体**")

    # 6. 行尾空格 / 双空格（中文行内）
    for i, line in enumerate(body.splitlines(), 1):
        if line.rstrip() != line and line.strip():
            issues.append("行尾空格 L%d" % i)
        if re.search(r"[\u4e00-\u9fff]  +[\u4e00-\u9fff]", line):
            issues.append("中文间多空格 L%d" % i)

    # 7. 批注里 $ 不成对
    for line in s.splitlines():
        if line.lstrip().startswith("%") and "[Tutor Note:" in line:
            n = len(re.findall(r"(?<!\\)\$", line))
            if n % 2:
                issues.append("批注 $ 不成对：「%s」" % line.strip()[:70])

    # 8. 中文后半角标点
    for m in re.finditer(r"[\u4e00-\u9fff]([,;:?!])", strip_math(body)):
        issues.append("中文后接半角 %r" % m.group(1))

    if issues:
        print("\n== %s ==" % name)
        seen = set()
        for it in issues:
            if it not in seen:
                seen.add(it)
                print("  -", it)
print("\nscan done")
