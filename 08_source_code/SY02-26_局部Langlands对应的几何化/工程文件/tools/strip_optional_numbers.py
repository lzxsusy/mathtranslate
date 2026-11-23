# -*- coding: utf-8 -*-
"""把 \begin{env}[I.x.y] 的可选编号参数挪成注释。

动机：preamble 已让定理环境自动编号（\thechapter Roman + [section] 计数器），
与原文号一致；再手写 [I.x.y] 就会印成「定理 I.6.5（I.6.5）」。
但原编号是译手核对过的对照信息，不能丢——改成行尾注释 `% 原编号 I.x.y`，
既不再重复打印，又留着可 grep。
"""
import io
import os
import re
import sys

SEC = r"C:\Users\admin\Downloads\FarguesScholze_局部朗兰兹几何化\源码\sections"
ENVS = ("theorem", "proposition", "lemma", "corollary", "definition", "example",
        "construction", "question", "remark", "conjecture")
pat = re.compile(r"\\begin\{(" + "|".join(ENVS) + r")\}\[([^\]]*)\]")


def main():
    files = sorted(f for f in os.listdir(SEC) if f.endswith(".tex"))
    total = 0
    for f in files:
        p = os.path.join(SEC, f)
        s = io.open(p, encoding="utf-8").read()
        hits = []

        def rep(m):
            hits.append(m.group(2))
            return "\\begin{%s}%% 原编号 %s" % (m.group(1), m.group(2))

        new = pat.sub(rep, s)
        if hits:
            io.open(p, "w", encoding="utf-8", newline="\n").write(new)
            print("%-22s 去掉 %2d 处可选编号" % (f, len(hits)))
            total += len(hits)
    print("合计 %d 处" % total)


if __name__ == "__main__":
    main()
