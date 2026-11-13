# -*- coding: utf-8 -*-
"""删除指定 chunk 中标题匹配的 conceptbox 块（含前后空行）。"""
import io
import sys

SRC = r"<本地路径>"


def balanced(s, i):
    d = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            d += 1
        elif c == "}":
            d -= 1
            if d == 0:
                return j
        j += 1
    return -1


def remove(name, title_part):
    p = SRC + "\\" + name + ".tex"
    s = io.open(p, encoding="utf-8").read()
    start = s.find("\\begin{conceptbox}")
    while start >= 0:
        k = s.find("{", start + len("\\begin{conceptbox}"))
        e = balanced(s, k)
        title = s[k + 1:e]
        if title_part in title:
            end = s.find("\\end{conceptbox}", e) + len("\\end{conceptbox}")
            # 吞掉尾随换行
            while end < len(s) and s[end] in "\r\n":
                end += 1
            s = s[:start] + s[end:]
            io.open(p, "w", encoding="utf-8").write(s)
            print("removed from %s: %s" % (name, title))
            return True
        start = s.find("\\begin{conceptbox}", start + 1)
    print("NOT FOUND in %s: %s" % (name, title_part))
    return False


if __name__ == "__main__":
    remove("ch08", "轨道范畴")
    remove("ch11", "轨道范畴")
    remove("ch14", "dg 范畴与")
