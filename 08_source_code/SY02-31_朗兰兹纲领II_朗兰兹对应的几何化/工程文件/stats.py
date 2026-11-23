# -*- coding: utf-8 -*-
"""生成 U03 数据与统计：逐块字数、页锚、定理环境、带号公式、译注。

用法（在工程根下）：python 工程文件/stats.py
输出：工程文件/reports/U03_数据与统计.md（同时打印纯 ASCII 摘要）
"""
import io, os, re, glob, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
chunks = sorted(glob.glob(os.path.join(root, "源码", "chunks", "*.tex")))

env_re = re.compile(r"\\begin\{(thm|prop|lem|cor|conj|defn|rem|exam|ques|claim|notn|hyp|fact|prob)\}\{([^}]*)\}")
tag_re = re.compile(r"\\tag\{")
ysrc_re = re.compile(r"\\ysrc\{(\d+)\}")
tn_re = re.compile(r"\\tn\{")
label_re = re.compile(r"\\label\{")

rows = []
tot = dict(files=0, chars=0, pages=0, stmt=0, tags=0, tn=0, labels=0)
for f in chunks:
    s = io.open(f, encoding="utf-8").read()
    ys = [int(x) for x in ysrc_re.findall(s)]
    st = env_re.findall(s)
    # 去掉注释行后计中文字符近似值
    body = "\n".join(l for l in s.split("\n") if not l.lstrip().startswith("%"))
    chars = len(re.sub(r"\s", "", body))
    r = dict(name=os.path.basename(f), chars=chars, span="%d–%d" % (ys[0], ys[-1]) if ys else "—",
             pages=len(ys), stmt=len(st), tags=len(tag_re.findall(s)), tn=len(tn_re.findall(s)),
             labels=len(label_re.findall(s)))
    rows.append(r)
    tot["files"] += 1; tot["chars"] += chars; tot["pages"] += r["pages"]
    tot["stmt"] += r["stmt"]; tot["tags"] += r["tags"]; tot["tn"] += r["tn"]; tot["labels"] += r["labels"]

out = io.open(os.path.join(root, "工程文件", "reports", "U03_数据与统计.md"), "w", encoding="utf-8")
out.write("# U03 数据与统计（自动生成）\n\n")
out.write("统计脚本：`工程文件/stats.py`；字数=去掉空白后的源码字符数（含 LaTeX 标记，仅用于横向比较）。\n\n")
out.write("| 块 | 页范围（印刷） | 页锚 | 字符 | 编号陈述 | 带号公式 | 译注 | \\label |\n")
out.write("|---|---|---|---|---|---|---|---|\n")
for r in rows:
    out.write("| %s | %s | %d | %d | %d | %d | %d | %d |\n" % (
        r["name"], r["span"], r["pages"], r["chars"], r["stmt"], r["tags"], r["tn"], r["labels"]))
out.write("| **合计** | — | **%d** | **%d** | **%d** | **%d** | **%d** | **%d** |\n" % (
    tot["pages"], tot["chars"], tot["stmt"], tot["tags"], tot["tn"], tot["labels"]))
out.write("\n块数 %d。\n" % tot["files"])
out.close()
print("files=%d chars=%d pages=%d stmt=%d tags=%d tn=%d labels=%d" % (
    tot["files"], tot["chars"], tot["pages"], tot["stmt"], tot["tags"], tot["tn"], tot["labels"]))
