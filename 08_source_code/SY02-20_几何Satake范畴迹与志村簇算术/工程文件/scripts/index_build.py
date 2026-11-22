# -*- coding: utf-8 -*-
r"""生成条款索引：编号、类别、译本页、label 键。

- 编号按章节计数器与定理/公式计数器模拟（同 sim_numbering.py）。
- label 只取对象自身环境内部的那个（用环境栈配对 \begin/\end）。
- 页取自 源码/main.aux；没给 \label 的对象页取前一个对象的页，页码加 *。

用法：python index_build.py > ../work/条款索引数据.tsv
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PROJ = os.path.dirname(ROOT)
AUX = os.path.join(PROJ, "源码", "main.aux")
CHUNKS = os.path.join(PROJ, "源码", "chunks")

NAME = {
    "thm": "定理", "theorem": "定理",
    "prop": "命题", "proposition": "命题",
    "lem": "引理", "lemma": "引理", "sublem": "子引理", "sublemma": "子引理",
    "lem-def": "引理-定义",
    "cor": "推论", "corollary": "推论",
    "conj": "猜想", "conjecture": "猜想",
    "example": "例", "ex": "例", "exs": "例",
    "remark": "注", "rmk": "注",
    "dfn": "定义", "definition": "定义",
    "construction": "构造", "notation": "记号", "convention": "约定",
    "hypothesis": "假设",
}
EQ = ("equation", "align", "gather", "multline", "eqnarray")
THM_ENVS = "|".join(sorted(NAME, key=len, reverse=True))

aux = open(AUX, encoding="utf-8", errors="replace").read()
page_of = {}
for m in re.finditer(r"\\newlabel\{([^}]*)\}\{\{([^}]*)\}\{([^}]*)\}", aux):
    key, page = m.group(1), m.group(3)
    if page.isdigit():
        page_of[key] = int(page)

text = ""
for p in sorted(glob.glob(os.path.join(CHUNKS, "ch*.tex"))):
    for raw in open(p, encoding="utf-8").read().split("\n"):
        text += ("" if raw.lstrip().startswith("%") else re.sub(r"(?<!\\)%.*", "", raw)) + "\n"

EV = re.compile(r"\\(begin|end)\{(%s|%s)\}|\\(section|subsection)\s*\{"
                % (THM_ENVS, "|".join(EQ)))

sec = sub = sss = eqs = 0
stack = []      # [(env, obj_index)]
objs = []       # [编号, 类别, label]
for m in EV.finditer(text):
    if m.group(3):                      # \section / \subsection
        head = text[m.start():m.start() + 40]
        if m.group(3) == "section":
            sec += 1
            sub = sss = eqs = 0
        else:
            sub += 1
            sss = eqs = 0
        continue
    kind, env = m.group(1), m.group(2)
    if kind == "end":
        if stack and stack[-1][0] == env:
            stack.pop()
        continue
    # begin
    if env in EQ:
        n = text[m.end():m.end() + 2]
        if n.startswith("*"):
            stack.append((env + "*", None))
            continue
        eqs += 1
        objs.append(["%d.%d.%d" % (sec, sub, eqs), "公式", None])
        stack.append((env, len(objs) - 1))
    elif env in NAME:
        sss += 1
        objs.append(["%d.%d.%d" % (sec, sub, sss), NAME[env], None])
        stack.append((env, len(objs) - 1))
    else:
        stack.append((env, None))

# 环境内部的 label
for m in re.finditer(r"\\label\{([^}]*)\}", text):
    # 找出包含该位置的栈状态：重新扫描太慢，改为在前一步记录每个 label 的归属
    pass

# 第二遍：带位置地重扫，遇 label 时取栈顶对象
sec = sub = sss = eqs = 0
stack = []
pos = 0
objs = []
EV2 = re.compile(r"\\(begin|end)\{(%s|%s)\}|\\(section|subsection)\s*\{|\\label\{([^}]*)\}"
                 % (THM_ENVS, "|".join(EQ)))
for m in EV2.finditer(text):
    if m.group(4) is not None:          # label
        for env, idx in reversed(stack):
            if idx is not None:
                if objs[idx][2] is None:
                    objs[idx][2] = m.group(4)
                break
        continue
    if m.group(3):
        if m.group(3) == "section":
            sec += 1
            sub = sss = eqs = 0
        else:
            sub += 1
            sss = eqs = 0
        continue
    kind, env = m.group(1), m.group(2)
    if kind == "end":
        if stack and stack[-1][0] in (env, env + "*"):
            stack.pop()
        continue
    if env in EQ:
        if text[m.end():m.end() + 2].startswith("*"):
            stack.append((env + "*", None))
            continue
        eqs += 1
        objs.append(["%d.%d.%d" % (sec, sub, eqs), "公式", None])
        stack.append((env, len(objs) - 1))
    elif env in NAME:
        sss += 1
        objs.append(["%d.%d.%d" % (sec, sub, sss), NAME[env], None])
        stack.append((env, len(objs) - 1))
    else:
        stack.append((env, None))

prev_page = 1
for num, kind, key in objs:
    page = page_of.get(key) if key else None
    if page is None:
        page, mark = prev_page, "*"
    else:
        prev_page, mark = page, ""
    print("%s\t%s\t%d%s\t%s" % (num, kind, page, mark, key or "-"))
