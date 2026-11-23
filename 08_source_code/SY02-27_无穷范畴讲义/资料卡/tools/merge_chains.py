#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把 _partials/chains_[ABC].md 合并成 03-论证链.md，并统一链编号。

每份分块文件只应包含若干 `### 链 ...` 小节（可带一个 `## ...` 部分标题）；
本脚本按 A→B→C 顺序拼接，把所有 `### 链` 标题重排为“链 1”“链 2”……，
并在文件头写入统一口径。
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PART = os.path.join(ROOT, "_partials")

PREFACE = """# 03 论证链 · SY02-27《无穷范畴讲义》

> 口径：每条链按 `04_playbook/08_论证精读与知识网络.md` 的统一结构写——
> **问题 / 起点 / 步骤（带 warrant）/ 收口 / 反事实**；括号里的 `p.xxx` 是**原书页**
> （原书页 = PDF 页 − 该讲起始 PDF 页 + 1，起始页见 `工程文件/work/lecture_pages.tsv`）；
> `SY02-27.concept.*` / `SY02-27.stmt.*` 指向 `01-概念.tsv`、`02-命题.tsv`。
> 链的任务是回答「这本书的论证是怎么搭起来的」，不是复述目录：每条链都要能指出「缺了哪一步会断」。
> 全书 27 讲分三批读：第 1–9 讲（A）、第 10–18 讲（B）、第 19–27 讲（C），
> 各批 2–3 条链，共 {n} 条；Lead 合并并统一编号，正文未改动。

"""


def main():
    parts = []
    for path in sorted(glob.glob(os.path.join(PART, "chains_*.md"))):
        tag = os.path.basename(path)[len("chains_"):-len(".md")]
        parts.append((tag, io.open(path, encoding="utf-8").read().strip()))

    if not parts:
        print("[错误] 没有 chains_*.md")
        return 1

    counter = 0
    out = []
    for tag, text in parts:
        out.append("\n## %s 批\n" % tag)
        for line in text.splitlines():
            m = re.match(r"^#{2,3}\s*链", line)
            if m:
                counter += 1
                tail = line[m.end():].lstrip("：: 0123456789一二三四五六七八九十")
                line = "### 链 %d：%s" % (counter, tail) if tail else "### 链 %d" % counter
            elif line.startswith("# "):
                continue
            out.append(line)

    body = PREFACE.format(n=counter) + "\n".join(out).strip() + "\n"
    path = os.path.join(ROOT, "03-论证链.md")
    with io.open(path, "w", encoding="utf-8") as fh:
        fh.write(body)
    print("[写出] %s，共 %d 条链" % (path, counter))
    return 0


if __name__ == "__main__":
    sys.exit(main())
