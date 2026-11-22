# -*- coding: utf-8 -*-
import pathlib, re

ROOT = pathlib.Path(r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-23_规范场论与几何朗兰兹的解析形式")
AUX = ROOT / "源码" / "main.aux"
CH = ROOT / "源码" / "chunks"
OUT = ROOT / "资料卡" / "03-条款索引.md"

# label -> (number, page); number/page never contain braces
labels = {}
for m in re.finditer(r"\\newlabel\{([^{}]+)\}\{\{([^{}]*)\}\{([^{}]*)\}", AUX.read_text(encoding="utf-8", errors="replace")):
    labels[m.group(1)] = (m.group(2), m.group(3))

rows, seen = [], set()
sec = sub = subsub = ""
for p in sorted(CH.glob("ch*.tex")):
    if p.name == "ch17.tex":
        continue
    for raw in p.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.rstrip("\r")
        m = re.match(r"\s*\\(section|subsection|subsubsection)\{", line)
        if m:
            level = m.group(1)
            title = line.split("{", 1)[1].split("\\label", 1)[0].strip().rstrip("}").strip()
            if level == "section":
                sec, sub, subsub = title, "", ""
            elif level == "subsection":
                sub, subsub = title, ""
            else:
                subsub = title
        for lm in re.finditer(r"\\label\{([^{}]+)\}", line):
            key = lm.group(1)
            if key in labels and key not in seen:
                seen.add(key)
                num, page = labels[key]
                pos = " / ".join(x for x in [sec, sub, subsub] if x)
                rows.append((key, num, page, pos, line.strip()[:110]))

out = ["# 资料卡 03 · 条款索引", "",
       "原文全部 `\\label` 与译文一一对应；编号与页码取译本编译产物（`源码/main.aux`，共 %d 条）。" % len(rows),
       "左列为译本编号，`label` 为源文件中的键，位置为所在章节，末列为该条款所在行的开头（公式环境通常只显示环境名）。", ""]
cur = None
for key, num, page, pos, snippet in rows:
    top = pos.split(" / ")[0] if pos else "（未分节）"
    if top != cur:
        cur = top
        out += [f"## {top}", "", "| 编号 | label | 页 | 位置 | 内容/所在行 |", "| --- | --- | --- | --- | --- |"]
    out.append(f"| {num} | `{key}` | {page} | {pos.replace('|', '/')} | `{snippet.replace('|', '/')}` |")
out.append("")
OUT.write_text("\n".join(out), encoding="utf-8")
print("wrote", OUT, "rows", len(rows))
