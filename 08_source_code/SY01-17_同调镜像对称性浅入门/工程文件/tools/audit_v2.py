# -*- coding: utf-8 -*-
"""v2.0 全书自动审计：结构、术语残留、索引、批注、交叉引用。

用法： python tools/audit_v2.py
输出： 控制台摘要 + work/audit_v2.md
"""
import glob
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(BASE, "chapters")
OUT = os.path.join(BASE, "work", "audit_v2.md")

lines = []


def w(s=""):
    lines.append(s)


# ---------- 结构统计 ----------
w("# v2.0 自动审计")
w()
w("| 章 | 行数 | 字符数 | 本节重点 | 章末评注 | Tutor Note | 索引条目 |")
w("|---|---|---|---|---|---|---|")
tot = dict(lines=0, chars=0, take=0, review=0, note=0, idx=0)
for f in sorted(glob.glob(os.path.join(CH, "ch*.tex"))):
    s = open(f, encoding="utf-8").read()
    n = os.path.basename(f)
    row = [
        s.count("\n"),
        len(s),
        len(re.findall(r"\\takeaway\{", s)),
        len(re.findall(r"\\chapterreview\{", s)),
        len(re.findall(r"% \[Tutor Note:", s)),
        len(re.findall(r"\\index\{", s)),
    ]
    for k, v in zip(["lines", "chars", "take", "review", "note", "idx"], row):
        tot[k] += v
    w("| %s | %d | %d | %d | %d | %d | %d |" % (n, *row))
w("| **合计** | %d | %d | %d | %d | %d | %d |" % (
    tot["lines"], tot["chars"], tot["take"], tot["review"], tot["note"], tot["idx"]))
w()

# ---------- 术语残留 ----------
w("## 旧术语残留检查（应全部为 0）")
w()
old = ["帐篷", "停止子", "托里克", "卷绕", "充足", "曲弯", "坐标角色", "本征丛", "摩天大楼"]
bad = {t: 0 for t in old}
for f in glob.glob(os.path.join(CH, "*.tex")):
    s = open(f, encoding="utf-8").read()
    for t in old:
        bad[t] += s.count(t)
w("| 旧词 | 残留数 |")
w("|---|---|")
for t in old:
    w("| %s | %d |" % (t, bad[t]))
w()

# ---------- 新术语一致性 ----------
w("## 新术语计数")
w()
new = ["wrapped", "partially wrapped", "thimble", "stop", "环簇", "丰富", "正合"]
cnt = {t: 0 for t in new}
for f in glob.glob(os.path.join(CH, "*.tex")):
    s = open(f, encoding="utf-8").read()
    for t in new:
        cnt[t] += s.count(t)
w("| 术语 | 出现次数 |")
w("|---|---|")
for t in new:
    w("| %s | %d |" % (t, cnt[t]))
w()

# ---------- 索引键与显示名一致性 ----------
w("## 索引键检查（拼音键不应仍指向旧译）")
w()
badkeys = []
for f in glob.glob(os.path.join(CH, "*.tex")):
    s = open(f, encoding="utf-8").read()
    for m in re.finditer(r"\\index\{([^}]*)\}", s):
        body = m.group(1).split("|")[0]
        if "@" in body:
            key, disp = body.split("@", 1)
        else:
            key = disp = body
        for old_k, old_disp in [("tuolike", "托里克"), ("lefschetzzhangpeng", "帐篷"),
                                ("juanrao", "卷绕"), ("tingzhizi", "停止子"),
                                ("qiandang", "恰当"), ("chongzu", "充足")]:
            if old_k in key or old_disp in disp:
                badkeys.append((os.path.basename(f), body))
w("异常条目数：%d" % len(badkeys))
for b in badkeys[:20]:
    w("- %s: %s" % b)
w()

# ---------- 交叉引用 ----------
w("## 交叉引用")
w()
labels = set()
refs = set()
for f in glob.glob(os.path.join(CH, "*.tex")) + [os.path.join(BASE, "main.tex"),
                                                 os.path.join(BASE, "references.tex")]:
    s = open(f, encoding="utf-8").read()
    labels |= set(re.findall(r"\\label\{([^}]*)\}", s))
    labels |= set(re.findall(r"\\begin\{[A-Za-z*]+\}\{(?:[^{}]|\{[^{}]*\})*\}\{([^{}]*)\}", s))
    refs |= set(re.findall(r"\\(?:ref|eqref)\{([^}]*)\}", s))
    refs |= set(re.findall(r"\\hyperref\[([^\]]*)\]", s))
undef = []
for r in refs:
    if not r or r.startswith("ref:"):
        continue
    if r in labels:
        continue
    # elegantbook 定理环境把 {name}{label} 的锚点自动加前缀（lem:/thm:/def:…），
    # 故一并接受“去掉前缀后能在 labels 中找到”的引用
    if r.split(":", 1)[-1] in labels:
        continue
    undef.append(r)
undefined = sorted(undef)
w("- label 数：%d，引用目标数：%d，未定义：%d" % (len(labels), len(refs), len(undefined)))
for u in undefined[:20]:
    w("  - %s" % u)
w()

# ---------- 附录批注同步 ----------
w("## 附录批注同步")
w()
notes = 0
for f in glob.glob(os.path.join(CH, "*.tex")):
    s = open(f, encoding="utf-8").read()
    notes += len(re.findall(r"% \[Tutor Note:", s))
app = os.path.join(BASE, "appendix_notes.tex")
appn = len(re.findall(r"\\noindent\\textbf", open(app, encoding="utf-8").read())) if os.path.exists(app) else -1
w("- 正文批注：%d；附录条目：%d" % (notes, appn))

md = "\n".join(lines) + "\n"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(md)
print(md)
