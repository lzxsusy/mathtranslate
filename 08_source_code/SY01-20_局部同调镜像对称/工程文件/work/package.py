# -*- coding: utf-8 -*-
"""把 LHMS 工程打包进 归档 / shuyi / gitee_shuyi 三个位置。"""
import io
import os
import shutil

LH = r"<本地路径>"
ARCH = r"<本地路径>"
SHU = r"<本地路径>"
GS_SC = r"<本地路径>"
GS_META = r"<本地路径>"
PDF_NAME = "LHMS_局部同调镜像对称_中文译注本.pdf"
PDF = os.path.join(LH, "out", PDF_NAME)
TEX = os.path.join(LH, "out", "2611.07202v1_zh.tex")
BIB = os.path.join(LH, "out", "2611.07202v1_zh.bib")
INFO = os.path.join(LH, "docs", "投稿信息.md")


def cp(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)


def copytree(src, dst, skip=()):
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in skip]
        rel = os.path.relpath(root, src)
        target = dst if rel == "." else os.path.join(dst, rel)
        os.makedirs(target, exist_ok=True)
        for f in files:
            shutil.copy2(os.path.join(root, f), os.path.join(target, f))


# 1. 归档
copytree(os.path.join(LH, "src"), os.path.join(ARCH, "src"), skip=("figures",))
copytree(os.path.join(LH, "src", "figures"), os.path.join(ARCH, "src", "figures"))
cp(PDF, os.path.join(ARCH, "deliverable", PDF_NAME))
for f in ("README.md", "阅读参考指南.md", "译注与概念框汇总.md", "工程总结.md", "投稿信息.md"):
    cp(os.path.join(LH, "docs", f), os.path.join(ARCH, "deliverable", f))
copytree(os.path.join(LH, "work"), os.path.join(ARCH, "work"),
         skip=("check", "__pycache__", "origbuild", "figures"))
os.makedirs(os.path.join(ARCH, "review"), exist_ok=True)

# 2. shuyi/translations/SY01-20
copytree(os.path.join(LH, "src"), os.path.join(SHU, "源码"), skip=("figures",))
copytree(os.path.join(LH, "src", "figures"), os.path.join(SHU, "源码", "figures"))
cp(PDF, os.path.join(SHU, "源码", PDF_NAME))
cp(PDF, os.path.join(SHU, "成品", PDF_NAME))
cp(INFO, os.path.join(SHU, "投稿信息.md"))

# 3. gitee_shuyi/08_source_code
cp(TEX, os.path.join(GS_SC, "源码", "2611.07202v1_zh.tex"))
cp(BIB, os.path.join(GS_SC, "源码", "2611.07202v1_zh.bib"))
cp(INFO, os.path.join(GS_SC, "投稿信息.md"))
copytree(os.path.join(LH, "work"), os.path.join(GS_SC, "工程文件", "work"),
         skip=("check", "__pycache__", "origbuild", "figures"))
for f in ("README.md", "阅读参考指南.md", "译注与概念框汇总.md", "工程总结.md"):
    cp(os.path.join(LH, "docs", f), os.path.join(GS_SC, "工程文件", f))

# 4. gitee_shuyi/03_translations_meta
copytree(os.path.join(LH, "src"), os.path.join(GS_META, "源码"), skip=("figures",))
copytree(os.path.join(LH, "src", "figures"), os.path.join(GS_META, "源码", "figures"))
cp(INFO, os.path.join(GS_META, "投稿信息.md"))

print("done")
for p in (ARCH, SHU, GS_SC, GS_META):
    n = sum(len(f) for _, _, f in os.walk(p))
    print(n, "files in", os.path.basename(p))
