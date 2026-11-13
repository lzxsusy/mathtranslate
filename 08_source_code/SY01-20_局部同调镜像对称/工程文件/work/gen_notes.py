# -*- coding: utf-8 -*-
"""从 chunks 抽取 yizhu / conceptbox / keytakeaways 标题，生成译注汇总 markdown。"""
import io
import os
import re

SRC = r"<本地路径>"
OUT = r"<本地路径>"
os.makedirs(os.path.dirname(OUT), exist_ok=True)


def balanced(s, i):
    """s[i] == '{'，返回匹配的 '}' 下标。"""
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return j
        j += 1
    return -1


rows = []
for i in range(15):
    name = "ch%02d" % i
    p = os.path.join(SRC, name + ".tex")
    if not os.path.isfile(p):
        continue
    s = io.open(p, encoding="utf-8").read()
    sec = ""
    sub = ""
    pos = 0
    # 顺序扫描 \section/\subsection 与三类框
    pat = re.compile(r"\\(section|subsection)\*?\{|<本地路径>|conceptbox|keytakeaways)\}")
    for m in pat.finditer(s):
        if m.group(1):
            k = m.end() - 1
            e = balanced(s, k)
            title = s[k + 1:e]
            if m.group(1) == "section":
                sec, sub = title, ""
            else:
                sub = title
        else:
            env = m.group(2)
            if env == "keytakeaways":
                rows.append((name, sec, sub, "本节重点", ""))
                continue
            k = s.find("{", m.end())
            if k < 0:
                continue
            e = balanced(s, k)
            title = s[k + 1:e]
            # 去掉 \emph 等宏
            title = re.sub(r"\\[a-zA-Z]+\s*", "", title).strip()
            rows.append((name, sec, sub, "译注" if env == "yizhu" else "概念回顾", title))

lines = ["# 译注与概念框汇总", "", "本表列出全书所有译注（橙色框）、概念回顾（紫色框）与本节重点（蓝色框）的标题及所在位置，便于检索。数目与正文一致，源文件见 `src/chunks/`.", ""]
lines.append("| # | 类型 | 标题 | 所在节 | 文件 |")
lines.append("|---|---|---|---|---|")
n = 0
for name, sec, sub, kind, title in rows:
    n += 1
    loc = sec + (" / " + sub if sub else "")
    lines.append("| %d | %s | %s | %s | %s |" % (n, kind, title, loc, name))
cnt_y = sum(1 for r in rows if r[3] == "译注")
cnt_c = sum(1 for r in rows if r[3] == "概念回顾")
cnt_k = sum(1 for r in rows if r[3] == "本节重点")
lines += ["", "统计：译注 %d 条，概念回顾 %d 条，本节重点 %d 处。" % (cnt_y, cnt_c, cnt_k), ""]
io.open(OUT, "w", encoding="utf-8").write("\n".join(lines))
print("rows", len(rows), "yizhu", cnt_y, "concept", cnt_c, "key", cnt_k)
