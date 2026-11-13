# -*- coding: utf-8 -*-
"""原文 vs 译文 结构对照：标签缺失、公式内容差异、引用键、图表、脚注。
输出 work/probe/structdiff.md 与 work/probe/labels_missing.tsv（按草稿文件分组）。
"""
import sys, os, re, glob, json
sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"<本地路径>"
SEC = os.path.join(ROOT, "sections")
REF = os.path.join(ROOT, "work", "ref")
OUT = os.path.join(ROOT, "work", "probe")

names = ["00-introduction","01-electromagnetic","02-multiplets","03-renormalization","04-pure-su2",
         "05-one-flavor","06-six-dimensions","07-higgs","08-two-three-flavors","09-gaiotto",
         "10-argyres-douglas","11-other-groups","12-su-n-duality","13-conclusions",
         "A-instantons","B-theory-zoo"]

B = chr(92)
def read(p):
    return open(p, encoding="utf-8").read()

def labels(t):
    return re.findall(re.escape(B)+"label"+re.escape("{")+r"([^}]+)\}", t)

def cites(t):
    res = []
    for m in re.finditer(re.escape(B)+r"cite[a-zA-Z]*\{([^}]*)\}", t):
        for k in m.group(1).split(","):
            k = k.strip()
            if k: res.append(k)
    return res

def envs(t, name):
    """提取 equation/align/figure/table 环境块（含标签）"""
    out = []
    pat = re.compile(re.escape(B)+"begin"+re.escape("{")+name+r"\*?\}(.*?)"+re.escape(B)+"end"+re.escape("{")+name+r"\*?\}", re.S)
    for m in pat.finditer(t):
        body = m.group(1)
        lab = re.search(re.escape(B)+"label"+re.escape("{")+r"([^}]+)\}", body)
        out.append((lab.group(1) if lab else None, body))
    return out

lines = []
def P(s=""):
    lines.append(s); print(s)

P("# 原文 vs 译文 结构对照（自动生成）")
P()
P("| 块 | 原文标签 | 译文标签 | 缺标签数 | 多余标签 | 公式_env(原/译) | align(原/译) | figure(原/译) | 脚注(原/译) |")
P("|---|---|---|---|---|---|---|---|---|")

missing_all = {}
for nm in names:
    ref = read(os.path.join(REF, nm + "-en.tex"))
    src = read(os.path.join(SEC, nm + ".tex"))
    lr, ls = labels(ref), labels(src)
    miss = [x for x in lr if x not in ls]
    extra = [x for x in ls if x not in lr]
    neq_r, neq_s = len(envs(ref, "equation")), len(envs(src, "equation"))
    nal_r, nal_s = len(envs(ref, "align")), len(envs(src, "align"))
    nfg_r, nfg_s = len(envs(ref, "figure")), len(envs(src, "figure"))
    nfn_r = len(re.findall(re.escape(B)+"footnote"+re.escape("{"), ref))
    nfn_s = len(re.findall(re.escape(B)+"footnote"+re.escape("{"), src))
    P(f"| {nm} | {len(lr)} | {len(ls)} | {len(miss)} | {len(extra)} | {neq_r}/{neq_s} | {nal_r}/{nal_s} | {nfg_r}/{nfg_s} | {nfn_r}/{nfn_s} |")
    if miss: missing_all[nm] = miss
    if extra: P(f"  - 多余标签：{extra}")

P()
P("## 缺失标签明细（草稿需补）")
for nm, ms in missing_all.items():
    P(f"### {nm}（{len(ms)}）")
    for x in ms: P(f"- {x}")
P()

# ---- 公式内容比对（按 label 对齐，用 difflib 相似度）----
import difflib
P("## 公式内容差异（按 label 对齐；相似度 < 0.97 者列出）")
low = []
for nm in names:
    ref = read(os.path.join(REF, nm + "-en.tex"))
    src = read(os.path.join(SEC, nm + ".tex"))
    # 收集所有 equation/align/multline 环境，按 label 映射正文
    def eqmap(t):
        m = {}
        for envname in ("equation","align","multline"):
            for lab, body in envs(t, envname):
                if lab:
                    b = re.sub(re.escape(B)+"label"+re.escape("{")+r"[^}]*\}", "", body)
                    b = re.sub(r"\s+", "", b)
                    m[lab] = b
        return m
    er, es = eqmap(ref), eqmap(src)
    for lab, body_r in er.items():
        if lab in es:
            ratio = difflib.SequenceMatcher(None, body_r, es[lab]).ratio()
            if ratio < 0.97:
                low.append((nm, lab, ratio, body_r[:160], es[lab][:160]))
P(f"共 {len(low)} 条相似度 < 0.97 的公式。")
for nm, lab, ratio, br, bs in low[:120]:
    P(f"- `{nm}` **{lab}** ratio={ratio:.3f}")
    P(f"    - 原文: `{br}`")
    P(f"    - 译文: `{bs}`")

with open(os.path.join(OUT, "structdiff.md"), "w", encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(lines))
print("\nwritten work/probe/structdiff.md ; 缺失标签块数:", len(missing_all), " 低相似公式:", len(low))
