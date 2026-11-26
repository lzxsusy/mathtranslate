# -*- coding: utf-8 -*-
"""给 chapters/lecture*.tex 的术语首次出现处插入 \\idx{...}，供 makeindex 建术语索引。
每个术语只插一次；跳过数学模式、注释行、\\chapter 行、含 \\znote/\\footnote 的行。
先备份到 _bak_idx/，失败可整体还原。"""
import io, os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "chapters")
BAK = os.path.join(ROOT, "_bak_idx")

TERMS = [
    "约化群", "阿代尔环", "阿代尔", "玉河数", "自守表示", "尖形式", "尖点的",
    "Eisenstein 级数", "抛物子群", "Levi 子群", "Hecke 代数", "Hecke 特征系统",
    "球 Hecke 代数", "新形式", "导子", "旁特征", "强重数一", "模形式",
    "模曲线", "椭圆曲线", "同源", "典范紧化", "几何模形式",
    "Eichler--Shimura 关系", "Eichler--Shimura 同构", "Hasse 不变量",
    "ordinary 曲线", "supersingular 曲线", "Serre 猜想",
    "Deligne--Serre 提升", "de Rham 表示", "Hodge--Tate 权",
    "Satake 参数", "Langlands 纲领", "Langlands 互反", "Langlands 群",
    "Buzzard--Gee 猜想", "Shimura 簇", "Shimura 数据", "自守向量丛",
    "旗簇", "典范模型", "局部系统", "非分歧",
]

files = sorted(
    f for f in os.listdir(CH) if f.startswith("lecture") and f.endswith(".tex")
)
os.makedirs(BAK, exist_ok=True)
for f in files:
    shutil.copy2(os.path.join(CH, f), os.path.join(BAK, f))

pending = {t: True for t in TERMS}
done = {}
for f in files:
    path = os.path.join(CH, f)
    lines = io.open(path, encoding="utf-8").read().split("\n")
    out = []
    for ln in lines:
        s = ln
        if pending and not s.lstrip().startswith("%") and "\\chapter" not in s \
           and "\\znote" not in s and "\\footnote" not in s:
            for term in list(pending):
                if term not in pending:
                    continue
                # 在数学模式外的位置找 term
                i = s.find(term)
                while i >= 0:
                    dollars = s[:i].count("$")
                    if dollars % 2 == 0 and "\\idx" not in s[max(0, i - 20):i + len(term) + 30]:
                        s = s[: i + len(term)] + "\\idx{" + term + "}" + s[i + len(term):]
                        done[term] = f
                        del pending[term]
                        break
                    i = s.find(term, i + 1)
        out.append(s)
    io.open(path, "w", encoding="utf-8").write("\n".join(out))

print("inserted:", len(done), "of", len(TERMS))
for t in TERMS:
    if t in pending:
        print("MISSING:", t)
for t, f in done.items():
    print(" ", t, "->", f)
