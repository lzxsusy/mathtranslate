#!/usr/bin/env python
"""Build notes/annotations-index.md from section fragments (read-only on sections)."""
import os
import re
import json
from collections import Counter

SEC = r"asi2204-zh\sections"
OUT = r"asi2204-zh\notes\annotations-index.md"
ORDER = ["s01-intro", "s02a", "s02b", "s02c", "s02d", "s02e", "s02f", "s02g",
         "s02h", "s03a", "s03b", "s03c", "s03d", "s03e", "s03f", "s03g",
         "s04", "s05", "s06", "s07", "s08-refs"]
CATS = ["Tutor Note", "原文疑误", "存疑", "背景补充"]
ANN_RE = re.compile(r"^\s*%\s*\[(Tutor Note|原文疑误|存疑|背景补充)\s*[:：]\s*(.*)$")
ANY_BRACKET = re.compile(r"^\s*%\s*\[")
ANCHOR = re.compile(r"^\s*%\s*====")


def parse_file(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    anns = []
    i = 0
    while i < len(lines):
        m = ANN_RE.match(lines[i])
        if not m:
            i += 1
            continue
        cat = m.group(1)
        buf = [m.group(2).rstrip()]
        start = i + 1
        j = i + 1
        while j < len(lines):
            st = lines[j].strip()
            if not st.startswith("%"):
                break
            if ANY_BRACKET.match(st) or ANCHOR.match(st):
                break
            buf.append(re.sub(r"^\s*%\s?", "", st).rstrip())
            j += 1
        text = " ".join(x for x in buf if x).strip()
        text = re.sub(r"\]\s*$", "", text).strip()
        anns.append({"line": start, "cat": cat, "text": text})
        i = j
    return anns


def load_all():
    data = {}
    for name in ORDER:
        p = os.path.join(SEC, name + ".tex")
        if os.path.exists(p):
            data[name + ".tex"] = parse_file(p)
    return data


CJK = re.compile(r"[\u4e00-\u9fff]")
CJK_OR_PUNCT = "\u4e00-\u9fff，。；：、（）【】「」“”"


def sub_math(s):
    def repl(m):
        c = m.group(1)
        return "$" + c + "$" if len(c) <= 10 else "…"
    s = re.sub(r"<[^>]*>", "", s)
    s = re.sub(r"\$([^$]*)\$", repl, s)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"(?<=[" + CJK_OR_PUNCT + r"])\s+", "", s)
    s = re.sub(r"\s+(?=[" + CJK_OR_PUNCT + r"])", "", s)
    s = re.sub(r"\s+([）】」])", r"\1", s)
    s = re.sub(r"^[，、；：。！？\s]+", "", s)
    return s.strip()


REF_EQ = re.compile(r"(?:式\s*)?\((\d+\.[0-9A-Za-z]+)\)")
REF_FN = re.compile(r"脚注\s*(\d+)")
REF_PG = re.compile(r"第\s*(\d+)\s*页")


def ref_suffix(text, cur):
    eqs = []
    for r in REF_EQ.findall(text):
        if ("(%s)" % r) not in cur and r not in eqs:
            eqs.append(r)
    fns = []
    for r in REF_FN.findall(text):
        if ("脚注 %s" % r) not in cur and r not in fns:
            fns.append(r)
    pgs = []
    for r in REF_PG.findall(text):
        if ("第 %s 页" % r) not in cur and r not in pgs:
            pgs.append(r)
    suff = ""
    if eqs:
        suff += "（式 " + "、".join("(%s)" % e for e in eqs[:2]) + "）"
    if pgs:
        suff += "（第 %s 页）" % pgs[0]
    if not eqs and not pgs and fns:
        suff += "（脚注 %s）" % fns[0]
    return suff


LABELS = re.compile(r"^(推导补足|易错预警|物理图像|物理含义|物理直觉|提示|说明|术语提示|小结)\s*[:：]\s*")

MARKERS = ["应为", "印作", "印成", "原文作", "原文写", "写作", "漏", "多出",
           "多一个", "不一致", "疑为", "笔误", "疏漏", "误作", "缺", "语法",
           "不通"]


def truncate(s, limit):
    if len(s) <= limit:
        return s
    if limit <= 1:
        return "…"
    s = s[:limit - 1]
    if s.count("$") % 2:
        i = s.rfind("$")
        if i > 0:
            s = s[:i]
    s = s.rstrip("，、；： （《「【")
    return s + "…"


def pick_factual_clause(t):
    clauses = re.split(r"[；。！？]", t)
    best, best_score = "", -1.0
    for c in clauses:
        cc = sub_math(c)
        if not cc:
            continue
        sc = 3.0 * sum(1 for k in MARKERS if k in c)
        sc += 0.4 * min(len(CJK.findall(cc)), 25)
        if sc > best_score:
            best, best_score = cc, sc
    return best


def summary(a):
    t = a["text"]
    if a["cat"] == "背景补充":
        body = ""
        for c in re.split(r"[；。！？]", t):
            cc = sub_math(c)
            if len(CJK.findall(cc)) >= 6:
                body = cc
                break
        s = truncate(body or sub_math(t), 40)
        return s or "（见原文注）"
    if a["cat"] in ("原文疑误", "存疑"):
        body = pick_factual_clause(t) or sub_math(t)
        s = truncate(body, 40)
        return s or "（见原文注）"
    label = ""
    m = LABELS.match(t)
    if m:
        label = m.group(1) + "："
        t = t[m.end():]
    clauses = re.split(r"[；。！？]", t)
    body = ""
    for c in clauses:
        cc = sub_math(c)
        if len(CJK.findall(cc)) >= 10:
            body = cc
            break
    if not body:
        best = ""
        for c in clauses:
            cc = sub_math(c)
            if len(CJK.findall(cc)) > len(CJK.findall(best)):
                best = cc
        body = best
    if not body:
        for c in clauses:
            cc = sub_math(c)
            if cc:
                body = cc
                break
    s = label + body
    suff = ref_suffix(a["text"], s)
    if suff:
        room = 40 - len(suff)
        s = truncate(s, room) + suff if room >= 8 else truncate(s, 40)
    else:
        s = truncate(s, 40)
    if not s:
        s = "（见原文注）"
    return s


THEMES = [
    ("拼写/语法", ["拼写", "漏写字母", "漏写", "拼作", "冠词", "复数不一致", "语法",
                "语序", "介词", "用词", "重复一次", "多出定冠词", "多出一个",
                "应为 \"", "quasihomogenous", "though of", "colliding",
                "homotopies", "depends on", "naturally have", "in at",
                "simply pair", "拼写错误", "英文用词"]),
    ("指标/次数", ["指标", "上下标", "下标", "上标", "指标重复", "移位", "幂次",
                "指数", "分次", "次数", "degree", "grading"]),
    ("符号笔误", ["符号", "笔误", "漏印", "横杠", "漏了", "应为", "写错", "误作",
                "印错", "字形", "之误", "记号"]),
    ("符号约定", ["约定", "归一化", "号差", "符号相反", "convention", "定义相差",
                "记号并不常见"]),
    ("排版/印样", ["排版", "排印", "印作", "印成", "原样", "缺字", "漏字", "标点",
                "括号", "断行", "对齐", "标记泄漏", "源文件标记"]),
]


def theme_of(text):
    best = ("其他/待归", 0)
    for name, kws in THEMES:
        score = sum(1 for k in kws if k in text)
        if score > best[1]:
            best = (name, score)
    return best[0]


def md_cell(s):
    s = s.replace("|", "\\|")
    s = s.replace("<", "&lt;").replace(">", "&gt;")
    return s


def md_text(s):
    s = s.replace("<", "&lt;").replace(">", "&gt;")
    return s


def tidy_full(text):
    t = re.sub(r"\s+", " ", text)
    t = re.sub(r"\s+([，。；：、）】」])", r"\1", t)
    t = re.sub(r"（\s+", "（", t)
    t = t.replace("； ", "；").strip()
    return md_text(t)


def main():
    data = load_all()
    files = list(data.keys())
    lines = []
    w = lines.append

    totals = Counter()
    for f in files:
        totals.update(a["cat"] for a in data[f])

    w("# 审校批注索引（annotations index）")
    w("")
    w("> 本索引由 `asi2204-zh/sections/*.tex` 自动提取（只读生成），按分片顺序列出全部审校批注。")
    w("> 每条含：分片文件名（小节标题）、源码行号、类别、一句话摘要（≤40 字；式号/页码/脚注在可行时以「（式 (x.y)）」「（第 N 页）」「（脚注 N）」标出）。")
    w("> 完整技术内容请回到源码对应行；「原文疑误」与「存疑」的完整内容另见第 3 节。")
    w("")
    w("**规模**：%d 个分片，共 %d 条批注 —— Tutor Note %d、原文疑误 %d、存疑 %d、背景补充 %d。"
      % (len(files), sum(totals.values()), totals["Tutor Note"],
         totals["原文疑误"], totals["存疑"], totals["背景补充"]))
    w("")
    w("## 1. 批注清单（按分片顺序）")
    w("")
    for f in files:
        w("### %s" % f)
        w("")
        w("| 行 | 类别 | 摘要 |")
        w("|---:|---|---|")
        for a in data[f]:
            cell = md_cell(summary(a))
            if len(cell) > 40:
                cell = cell[:39] + "…"
            w("| %d | %s | %s |" % (a["line"], a["cat"], cell))
        w("")

    # 2 statistics
    w("## 2. 统计")
    w("")
    w("### 2.1 各分片批注数量")
    w("")
    w("| 分片 | Tutor Note | 原文疑误 | 存疑 | 背景补充 | 合计 |")
    w("|---|---:|---:|---:|---:|---:|")
    for f in files:
        c = Counter(a["cat"] for a in data[f])
        w("| %s | %d | %d | %d | %d | %d |"
          % (f, c["Tutor Note"], c["原文疑误"], c["存疑"], c["背景补充"], len(data[f])))
    w("| **全书合计** | **%d** | **%d** | **%d** | **%d** | **%d** |"
      % (totals["Tutor Note"], totals["原文疑误"], totals["存疑"],
         totals["背景补充"], sum(totals.values())))
    w("")
    # theme classification
    typo = [(f, a) for f in files for a in data[f] if a["cat"] == "原文疑误"]
    doubt = [(f, a) for f in files for a in data[f] if a["cat"] == "存疑"]
    tcnt = Counter(theme_of(a["text"]) for _, a in typo)
    dcnt = Counter(theme_of(a["text"]) for _, a in doubt)
    w("### 2.2 「原文疑误 + 存疑」按主题的粗略分类")
    w("")
    w("> 关键词法粗分类，每条只计入一个主类；主题间存在交叉，仅用于评审定位。")
    w("")
    w("| 主题 | 原文疑误 | 存疑 | 合计 |")
    w("|---|---:|---:|---:|")
    names = [n for n, _ in THEMES] + ["其他/待归"]
    for n in names:
        if tcnt.get(n, 0) + dcnt.get(n, 0) == 0:
            continue
        w("| %s | %d | %d | %d |" % (n, tcnt.get(n, 0), dcnt.get(n, 0),
                                     tcnt.get(n, 0) + dcnt.get(n, 0)))
    w("| **合计** | **%d** | **%d** | **%d** |" % (len(typo), len(doubt), len(typo) + len(doubt)))
    w("")

    # 3 full typo + doubt
    w("## 3. 原文疑误与存疑汇总（供评审阅读）")
    w("")
    w("> 完整内容按文件分组列出；仅整理空白，未改动技术结论。")
    w("")
    for f in files:
        sel = [a for a in data[f] if a["cat"] in ("原文疑误", "存疑")]
        if not sel:
            continue
        w("### %s" % f)
        w("")
        for a in sel:
            w("- **第 %d 行（%s）**：%s" % (a["line"], a["cat"], tidy_full(a["text"])))
        w("")

    open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("wrote", OUT)
    print("files", len(files), "total", sum(totals.values()),
          "TN", totals["Tutor Note"], "typo", totals["原文疑误"],
          "doubt", totals["存疑"], "bg", totals["背景补充"])
    print("themes typo", dict(tcnt))
    print("themes doubt", dict(dcnt))


if __name__ == "__main__":
    main()
