# -*- coding: utf-8 -*-
"""校验 ch15.tex 译文与原文 GLDraft_D.tex:3540-3802 的一致性（v2）"""
import re, sys, collections, difflib
sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-23_规范场论与几何朗兰兹的解析形式"
ORIG = ROOT + r"\工程文件\work\原文\GLDraft_D.tex"
NEW  = ROOT + r"\源码\chunks\ch15.tex"

def read(p): return open(p, encoding="utf-8").read()
orig = "\n".join(read(ORIG).splitlines()[3539:3802])   # 3540..3802
new  = read(NEW)

def strip_comments(s):
    out = []
    for line in s.split("\n"):
        m = re.search(r"(?<!\\)%", line)
        out.append(line[:m.start()] if m else line)
    return "\n".join(out)

def strip_arg(s, cmd):
    """删除 \\cmd{...}（支持嵌套花括号）"""
    out = []; i = 0
    while True:
        j = s.find(cmd + "{", i)
        if j < 0: out.append(s[i:]); break
        out.append(s[i:j])
        k = j + len(cmd) + 1; depth = 1
        while k < len(s) and depth:
            if s[k] == "\\": k += 2; continue
            if s[k] == "{": depth += 1
            elif s[k] == "}": depth -= 1
            k += 1
        i = k
    return "".join(out)

def strip_env(s, name):
    return re.sub(r"\\begin\{%s\}.*?\\end\{%s\}" % (name, name), " ", s, flags=re.S)

new_core = strip_env(strip_arg(new, "\\zy"), "yizhu")

def split_display(s):
    blocks = []
    pat = re.compile(r"\\begin\{(equation|align|eqnarray|gather|multline|displaymath|split)\*?\}.*?\\end\{\1\*?\}", re.S)
    def rep(m):
        blocks.append(m.group(0)); return "\n@@D%d@@\n" % (len(blocks)-1)
    rest = pat.sub(rep, s)
    b2 = []
    pat2 = re.compile(r"\\be(\b|(?=[^a-zA-Z])).*?\\ee", re.S)
    def rep2(m):
        b2.append(m.group(0)); return "\n@@B%d@@\n" % (len(b2)-1)
    rest = pat2.sub(rep2, rest)
    return blocks + b2, rest

def inline_math(s):
    segs = []; i = 0; buf = []; inside = False; n = len(s)
    while i < n:
        c = s[i]
        if c == "\\": 
            if inside: buf.append(s[i:i+2])
            i += 2; continue
        if c == "$":
            if inside: segs.append("".join(buf)); buf = []; inside = False
            else: inside = True
            i += 1; continue
        if inside: buf.append(c)
        i += 1
    if inside: segs.append("<<UNCLOSED>>" + "".join(buf))
    return segs

def norm(x): return re.sub(r"\s+", " ", x).strip()

def keys(s, cmd): return re.findall(r"\\%s\{([^}]*)\}" % cmd, s)

def env_balance(s):
    stack = []; errs = []
    for m in re.finditer(r"\\(begin|end)\{([^}]*)\}", s):
        ln = s[:m.start()].count("\n")+1
        if m.group(1) == "begin": stack.append((m.group(2), ln))
        else:
            if not stack: errs.append("多余的 \\end{%s} 行%d" % (m.group(2), ln))
            elif stack[-1][0] != m.group(2):
                errs.append("不匹配 \\begin{%s}(行%d) vs \\end{%s}(行%d)" % (stack[-1][0], stack[-1][1], m.group(2), ln)); stack.pop()
            else: stack.pop()
    for nm, ln in stack: errs.append("未关闭 \\begin{%s} 行%d" % (nm, ln))
    return errs

def brace_balance(s):
    depth = 0; bad = []; i = 0
    while i < len(s):
        c = s[i]
        if c == "\\": i += 2; continue
        if c == "{": depth += 1
        elif c == "}":
            depth -= 1
            if depth < 0: bad.append("行%d 多余 }" % (s[:i].count("\n")+1)); depth = 0
        i += 1
    if depth: bad.append("末尾仍有 %d 个未闭合 {" % depth)
    return bad

print("="*72)
print("原文(3540-3802) 行数 %d ; 译文行数 %d" % (len(orig.split("\n")), len(new.split("\n"))))

print("\n[1] label 序列")
lo, ln = keys(orig, "label"), keys(new, "label")
print("  原:", lo); print("  译:", ln); print("  一致:", lo == ln)

print("\n[2] ref 多重集 (排除译注后)")
ro, rn = keys(orig, "ref"), keys(new_core, "ref")
print("  一致:", collections.Counter(ro) == collections.Counter(rn))
for k in sorted(set(ro) | set(rn)):
    if ro.count(k) != rn.count(k): print("   差异 %-12s 原 %d / 译 %d" % (k, ro.count(k), rn.count(k)))

print("\n[3] cite")
co, cn = keys(orig, "cite"), keys(new_core, "cite")
print("  原:", co); print("  译:", cn); print("  正文一致:", collections.Counter(co) == collections.Counter(cn))

print("\n[4] includegraphics:", re.findall(r"\\includegraphics(\[[^]]*\])?\{([^}]*)\}", orig),
      "|", re.findall(r"\\includegraphics(\[[^]]*\])?\{([^}]*)\}", new))

# ---- 公式块：按顺序逐一比较 ----
ob, orest = split_display(strip_comments(orig))
nb, nrest = split_display(strip_comments(new_core))
print("\n[5] 公式块数 原 %d / 译 %d" % (len(ob), len(nb)))
sm = difflib.SequenceMatcher(None, [norm(x) for x in ob], [norm(x) for x in nb])
bad = 0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal": continue
    bad += 1
    print("  !! %s 原[%d:%d] 译[%d:%d]" % (tag, i1, i2, j1, j2))
    for x in ob[i1:i2]: print("     原: %s" % norm(x))
    for x in nb[j1:j2]: print("     译: %s" % norm(x))
print("  公式块全部一致:", bad == 0)

# ---- 行内数学：多重集比较 ----
om = [norm(x) for x in inline_math(orest)]
nm = [norm(x) for x in inline_math(nrest)]
print("\n[6] 行内数学片段数 原 %d / 译 %d" % (len(om), len(nm)))
cm_o, cm_n = collections.Counter(om), collections.Counter(nm)
extra_o = cm_o - cm_n; extra_n = cm_n - cm_o
print("  原文有而译文缺/少:")
for k, v in extra_o.items(): print("     [%d×] %s" % (v, k))
print("  译文有而原文无/多:")
for k, v in extra_n.items(): print("     [%d×] %s" % (v, k))

print("\n[7] 结构检查")
print("  环境配对:", env_balance(new) or "OK")
print("  花括号:", brace_balance(new) or "OK")
c = len(re.findall(r"(?<!\\)\$", new))
print("  $ 个数 %d (%s)" % (c, "偶" if c % 2 == 0 else "!!奇!!"))
print("  yizhu: begin %d / end %d" % (new.count("\\begin{yizhu}"), new.count("\\end{yizhu}")))
print("  \\zy 数:", len(re.findall(r"\\zy\{", new)))

print("\n[8] 段落/空行结构")
print("  原文段落(空行分隔)数:", len([p for p in orig.split("\n\n") if p.strip()]),
      " 译文:", len([p for p in new.split("\n\n") if p.strip()]))
