# -*- coding: utf-8 -*-
"""译文静态检查：禁用词、旧术语、\\cite、环境配平、页锚密度。
用法: python lint.py <源码目录>
输出: 工程文件/reports/lint.md（UTF-8），并把摘要打到 stdout（纯 ASCII）。
"""
import io, os, re, sys, glob

src = sys.argv[1] if len(sys.argv) > 1 else r"C:/Users/admin/Desktop/数译发布/gitee_shuyi/08_source_code/SY02-31_朗兰兹纲领II_朗兰兹对应的几何化/源码"

banned = [
    ("被……所", re.compile(r"被[^。，；]{0,12}所")),
    ("进行……的", re.compile(r"进行(?!中)[^。，；]{0,10}的")),
    ("对于……而言", re.compile(r"对于[^。，；]{0,12}而言")),
]
terms = [
    ("相干层", "凝聚层"),
    ("模栈", "模叠"),
    ("派生范畴", "导出范畴"),
    ("圆环空间", "环路空间"),
]
cite_re = re.compile(r"\\cite[a-z]*\{")
env_re = re.compile(r"\\(begin|end)\{([a-zA-Z*]+)\}")
ysrc_re = re.compile(r"\\ysrc\{(\d+)\}")

stack = []
skip_env = False
files = sorted(glob.glob(os.path.join(src, "**", "*.tex"), recursive=True))
rows = []
tot_banned = 0
tot_terms = 0
tot_cite = 0
tot_unbal = 0
ysrc_missing = []

for f in files:
    rel = os.path.relpath(f, src).replace("\\", "/")
    text = io.open(f, encoding="utf-8", errors="replace").read()
    body = re.sub(r"%.*", "", text)
    issues = []
    for name, rx in banned:
        ms = rx.findall(body)
        # 过滤掉合法的「被……所」极少见；这里全部报告，人工判定
        if ms:
            issues.append("%s x%d" % (name, len(ms)))
            tot_banned += len(ms)
    for old, new in terms:
        c = body.count(old)
        if c:
            issues.append("旧术语 %s→%s x%d" % (old, new, c))
            tot_terms += c
    c = len(cite_re.findall(body))
    if c:
        issues.append("\\\\cite x%d" % c)
        tot_cite += c
    # 环境配平按全书顺序跨片累计：一篇的证明常跨 chunk 断开，
    # 单片内 begin/end 数目不等是正常的，只有「栈顶不匹配」才是真错误。
    bad = None
    if "/chunks/" in rel.replace("\\", "/"):
        for m in env_re.finditer(body):
            kind, name = m.group(1), m.group(2)
            if kind == "begin":
                if not skip_env: stack.append(name)
            else:
                if stack and stack[-1] == name:
                    stack.pop()
                elif name in stack:
                    bad = name
                    break
                elif not skip_env:
                    bad = name
                    break
    if bad:
        issues.append("环境错配（%s）" % bad)
        tot_unbal += 1
    ys = [int(x) for x in ysrc_re.findall(body)]
    rows.append((rel, len(ys), ys, "; ".join(issues) if issues else "—"))

# 页锚连续性：按 chunk 文件名中的编号无法直接得页范围，这里只报页锚数与首末页
out = io.open(os.path.join(src, "..", "工程文件", "reports", "lint.md"), "w", encoding="utf-8")
out.write("# 译文静态检查（自动生成）\n\n")
out.write("| 文件 | 页锚数 | 首末页 | 问题 |\n|---|---|---|---|\n")
for rel, n, ys, iss in rows:
    span = "%d–%d" % (ys[0], ys[-1]) if ys else "—"
    out.write("| %s | %d | %s | %s |\n" % (rel, n, span, iss))
out.write("\n合计：文件 %d；禁用句式 %d；旧术语 %d；\\\\cite %d；环境不配平文件 %d。\n"
          % (len(rows), tot_banned, tot_terms, tot_cite, tot_unbal))
out.close()
print("files=%d banned=%d terms=%d cite=%d unbal=%d" % (len(rows), tot_banned, tot_terms, tot_cite, tot_unbal))
