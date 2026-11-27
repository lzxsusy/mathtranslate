# -*- coding: utf-8 -*-
"""从译稿源文件推算编号条目表：讲次 / 共用计数器序号 / 环境类型 / 原文页 / 首句。

用法：
  python 工程文件/tools/index_items.py            # 打印 TSV 到 stdout
  python 工程文件/tools/index_items.py --md 03    # 生成资料卡 03 的 markdown 片段

只依赖正文结构：\\section 开启新讲（计数器归零），\\srcpage{N} 记录当前原文页，
各定理类环境按出现顺序递增计数（与 LaTeX 的 [theorem] 共用计数器一致）。
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEC = os.path.join(ROOT, "源码", "sections")

ENVS = {
    "theorem": "定理",
    "proposition": "命题",
    "lemma": "引理",
    "corollary": "推论",
    "definition": "定义",
    "example": "例",
    "construction": "构造",
    "question": "问题",
    "remark": "注",
    "conjecture": "猜想",
    "hope": "期望",
    "warning": "警告",
    "notation": "记号",
    "fact": "事实",
    "exercise": "练习",
}

SEC_RE = re.compile(r"^\\section\[")
PAGE_RE = re.compile(r"\\srcpage\{(\d+)\}")
BEGIN_RE = re.compile(r"\\begin\{(" + "|".join(ENVS) + r")\}")


def clean(text):
    t = text.replace("\n", " ")
    t = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", t)
    t = re.sub(r"[{}$\\]", "", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def scan(path):
    """返回 [(讲次, 序号, 类型, 页, 首句)]，讲次 = 该文件内 \\section 出现次序（从 1 起）。"""
    s = io.open(path, encoding="utf-8").read()
    lines = s.split("\n")
    lec = 0
    idx = 0
    page = 0
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if SEC_RE.match(line):
            lec += 1
            idx = 0
        m = PAGE_RE.search(line)
        if m:
            page = int(m.group(1))
        m = BEGIN_RE.search(line)
        if m:
            kind = m.group(1)
            idx += 1
            body = []
            j = i + 1
            while j < len(lines) and ("\\end{%s}" % kind) not in lines[j]:
                body.append(lines[j].strip())
                j += 1
            first = clean(" ".join(body))[:70]
            out.append((lec, idx, kind, page, first))
            i = j
        i += 1
    return out


def main():
    files = sorted(f for f in os.listdir(SEC) if re.match(r"s\d\d-.*\.tex$", f))
    rows = []
    for f in files:
        fnum = int(f[1:3])
        for r in scan(os.path.join(SEC, f)):
            rows.append((f,) + (fnum,) + r[1:])

    if "--md" in sys.argv:
        # 按讲次分组，输出「### §N.M」不好定位，这里按讲输出
        cur = None
        for f, lec, idx, kind, page, first in rows:
            key = (f, lec)
            if key != cur:
                print("")
                print("### %s（第 %d 节）" % (f, lec))
                print("")
                cur = key
            print("- %d.%d %s（p.%d）：%s" % (lec, idx, ENVS[kind], page, first))
        return

    print("file\tlecture\tidx\tkind\tlabel\tpage\tfirst")
    for f, lec, idx, kind, page, first in rows:
        print("%s\t%d\t%d\t%s\t%s\t%d\t%s" % (f, lec, idx, kind, ENVS[kind], page, first))


if __name__ == "__main__":
    main()
