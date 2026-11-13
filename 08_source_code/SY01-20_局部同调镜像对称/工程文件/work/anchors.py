# -*- coding: utf-8 -*-
"""解析 statement 编号（swapnumbers，共享计数器 [section]），并给出源码行。"""
import io, re, json

SRC = r"<本地路径>"
lines = io.open(SRC, encoding="utf-8").read().split("\n")

ENVS = ["thm", "dfn", "defn", "prp", "prop", "crl", "cor", "conj", "nota", "ques",
        "exmp", "example", "lmm", "lemma", "rmk", "cnv", "exer"]
NAMES = {"thm": "Theorem", "dfn": "Definition", "defn": "Definition", "prp": "Proposition",
         "prop": "Proposition", "crl": "Corollary", "cor": "Corollary", "conj": "Conjecture",
         "nota": "Notation", "ques": "Question", "exmp": "Example", "example": "Example",
         "lmm": "Lemma", "lemma": "Lemma", "rmk": "Remark", "cnv": "Convention",
         "exer": "Exercise"}

sec = 0
cnt = 0
appendix = False
app_sec = 0
res = []       # (number_str, name, env, line, label)
labels = {}
for no, raw in enumerate(lines, 1):
    line = raw
    # 跳过被注释的行
    stripped = line.lstrip()
    if stripped.startswith("%"):
        continue
    m = re.match(r"\s*<本地路径>", line)
    if m:
        appendix = True
        continue
    m = re.match(r"\s*<本地路径>", line)
    if m and "\\section{" in line:
        if appendix:
            app_sec += 1
            sec = app_sec
            cnt = 0
        else:
            sec += 1
            cnt = 0
        continue
    m = re.search(r"<本地路径>" + "|".join(ENVS) + r")\}", line)
    if m:
        env = m.group(1)
        cnt += 1
        if appendix:
            secstr = chr(ord("A") + sec - 1)
        else:
            secstr = str(sec)
        num = "%s.%d" % (secstr, cnt)
        res.append((num, NAMES[env], env, no, None))
    m = re.search(r"<本地路径>]*)\}", line)
    if m:
        labels[m.group(1)] = (len(res), no)

# 回填 label
out = []
for i, (num, name, env, no, _) in enumerate(res):
    out.append({"num": num, "name": name, "env": env, "line": no})
io.open(r"<本地路径>", "w", encoding="utf-8").write(
    json.dumps(out, ensure_ascii=False, indent=0))
io.open(r"<本地路径>", "w", encoding="utf-8").write(
    "\n".join("%s\t%d\t%d" % (k, v[0], v[1]) for k, v in sorted(labels.items())))
print("statements", len(out), "labels", len(labels))
