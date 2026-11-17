"""SY07-08 审计脚本。
用法: python check.py [源码目录]
检查: 未定义引用 / 重复 label / Overfull / 缺字 / 缺块 / 术语残留 / 译注来源 / 黑名单 / 条目与习题计数。
"""
import os
import re
import sys
import collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "源码")
CH = os.path.join(SRC, "chunks")

BLACK = re.compile(r"知乎|zhihu\.com|百度百科|baike\.baidu|CSDN|csdn\.net|简书|jianshu|公众号|mp\.weixin|bilibili|b站|个人博客")
FORBID = [
    ("旧术语 真态射", re.compile(r"真态射")),
    ("旧术语 前层（应为预层）", re.compile(r"前层")),
    ("eqnarray", re.compile(r"eqnarray")),
    ("手写条目编号", re.compile(r"\\begin\{(?:definition|proposition|theorem|lemma|corollary|example|remark|construction)\}\[[0-9]")),
    ("手写 qed", re.compile(r"\\qed\b")),
]
TNOTE_SRC = re.compile(r"\[(?:来源|依据|译者按)")
CJK = re.compile(r"[\u3000-\u303f\u4e00-\u9fff\uff00-\uffef]")
CJK2 = re.compile(r"[\u4e00-\u9fff] +[\u4e00-\u9fff]")
TERM_OLD = [
    ("旧术语 前层（presheaf 标准译名为预层）", re.compile(r"前层")),
    ("旧术语 定向集", re.compile(r"定向集")),
    ("旧术语 正向极限/正向系统", re.compile(r"正向(极限|系统)")),
    ("旧术语 环空间（应为环层空间）", re.compile(r"(?<!层)环空间")),
    ("旧术语 相联系的层", re.compile(r"相联系的层")),
    ("旧术语 逆向系（应为逆向系统）", re.compile(r"逆向系(?!统)")),
]

def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()

def main():
    problems = []
    info = []
    files = sorted(f for f in os.listdir(CH) if f.endswith(".tex")) if os.path.isdir(CH) else []
    if not files:
        print("!! chunks 目录为空"); return 1

    labels = collections.Counter()
    items = collections.Counter()
    exs = collections.Counter()
    tn = collections.Counter()
    idxkeys = {}
    refs = set()
    alltex = {}

    for f in files:
        p = os.path.join(CH, f)
        t = read(p)
        alltex[f] = t
        for m in re.finditer(r"\\label\{([^}]*)\}", t):
            labels[m.group(1)] += 1
        for m in re.finditer(r"\\begin\{(definition|proposition|theorem|lemma|corollary|example|remark|construction)\}", t):
            items[f] += 1
        for m in re.finditer(r"\\begin\{exercises\}", t):
            exs[f] += 1
        tn[f] = len(re.findall(r"\\begin\{tnote\}", t))
        for m in re.finditer(r"\\ref\{([^}]*)\}", t):
            refs.add(m.group(1))

        # 黑名单
        for m in BLACK.finditer(t):
            problems.append(f"[黑名单] {f}: …{t[max(0,m.start()-25):m.end()+25]}…")
        # 禁止项
        for name, rx in FORBID:
            for m in rx.finditer(t):
                line = t[:m.start()].count("\n") + 1
                problems.append(f"[{name}] {f}:{line}")
        # 译注缺来源
        for m in re.finditer(r"\\begin\{tnote\}(.*?)\\end\{tnote\}", t, re.S):
            body = m.group(1)
            line = t[:m.start()].count("\n") + 1
            if not TNOTE_SRC.search(body):
                problems.append(f"[译注无来源] {f}:{line}")
        # 文件头注释
        if not t.lstrip().startswith("%"):
            problems.append(f"[缺文件头注释] {f}")

        # —— 附加审计（2026-11-14 加）——
        # ① 数学模式里混入中文标点（会触发 Missing character）
        for m in re.finditer(r"\\\[(.*?)\\\]", t, re.S):
            seg = re.sub(r"\\text\{[^}]*\}", "", m.group(1))
            bad = [c for c in seg if c in "，。；：、（）「」"]
            if bad:
                line = t[:m.start()].count("\n") + 1
                problems.append(f"[数学模式中文标点] {f}:{line} {''.join(sorted(set(bad)))}")
        # ② 中文字符之间多余空格
        for m in CJK2.finditer(t):
            line = t[:m.start()].count("\n") + 1
            problems.append(f"[中文间空格] {f}:{line} …{t[max(0,m.start()-12):m.end()+12]}…")
        # ③ 引号风格（统一「」）
        if "\u201c" in t or "\u201d" in t:
            line = t[:t.index("\u201c" if "\u201c" in t else "\u201d")].count("\n") + 1
            problems.append(f"[引号应为「」] {f}:{line}")
        # ④ 索引键
        for m in re.finditer(r"\\idx\{([^}]*)\}\{([^}]*)\}", t):
            key, name = m.group(1), m.group(2)
            idxkeys.setdefault(key, set()).add(name)
            if key != key.lower():
                problems.append(f"[索引键含大写] {f}: \\idx{{{key}}}")
        # ⑤ 旧术语残留
        for label, rx in TERM_OLD:
            for m in rx.finditer(t):
                line = t[:m.start()].count("\n") + 1
                problems.append(f"[{label}] {f}:{line}")

    dup = [k for k, v in labels.items() if v > 1]
    for k in sorted(dup):
        problems.append(f"[重复 label] {k} ×{labels[k]}")
    for r in sorted(refs):
        if r not in labels:
            problems.append(f"[引用无目标] \\ref{{{r}}}")
    # 同一索引键指向不同显示名
    for k, names in sorted(idxkeys.items()):
        if len(names) > 1:
            problems.append(f"[索引键冲突] {k} → {'/'.join(sorted(names))}")

    # main.log 检查
    logp = os.path.join(SRC, "main.log")
    logstats = {}
    if os.path.exists(logp):
        log = read(logp)
        undef = re.findall(r"LaTeX Warning: Reference `([^']*)' on page (\d+) undefined", log)
        for r, pg in undef:
            problems.append(f"[未定义引用] {r} @p{pg}")
        logstats["Overfull"] = len(re.findall(r"Overfull \\hbox", log))
        logstats["Underfull"] = len(re.findall(r"Underfull \\hbox", log))
        logstats["缺字"] = len(re.findall(r"Missing character", log))
        logstats["页数"] = (re.search(r"Output written on main\.pdf \((\d+) pages", log) or [None, "?"])[1]
        if re.search(r"There were undefined references", log):
            problems.append("[未定义引用] 存在（见上）")
    else:
        info.append("main.log 不存在（未做整书编译）")

    print("== 块统计 ==")
    tot_i = tot_t = 0
    for f in files:
        tot_i += items[f]; tot_t += tn[f]
        print(f"  {f:22s} 条目 {items[f]:3d}  习题块 {exs[f]:2d}  译注 {tn[f]:2d}")
    print(f"  合计: 条目 {tot_i}, 译注 {tot_t}, label {sum(labels.values())}, 被引用 label {len(refs)}")
    if logstats:
        print("== 编译 ==")
        for k, v in logstats.items():
            print(f"  {k}: {v}")
    for s in info:
        print("  · " + s)
    print("== 问题 ==")
    if problems:
        for p in problems:
            print("  " + p)
        print(f"  共 {len(problems)} 条")
        return 1
    print("  无")
    return 0

if __name__ == "__main__":
    sys.exit(main())
