# -*- coding: utf-8 -*-
"""打包 deliverable/"""
import os, shutil

ROOT = r"<本地路径>"
SRC = os.path.join(ROOT, "src")
DEL = os.path.join(ROOT, "deliverable")


def copytree(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def main():
    os.makedirs(DEL, exist_ok=True)
    shutil.copy2(os.path.join(SRC, "main.pdf"), os.path.join(DEL, "场论与拓扑学_中文译注本.pdf"))
    copytree(SRC, os.path.join(DEL, "src"))
    shutil.copy2(os.path.join(ROOT, "build.ps1"), os.path.join(DEL, "build.ps1"))
    log = os.path.join(SRC, "main.log")
    if os.path.exists(log):
        shutil.copy2(log, os.path.join(DEL, "compile.log"))
    md = os.path.join(ROOT, "work", "译注汇总.md")
    if os.path.exists(md):
        shutil.copy2(md, os.path.join(DEL, "译注汇总.md"))
    if os.path.exists(os.path.join(ROOT, "README.md")):
        shutil.copy2(os.path.join(ROOT, "README.md"), os.path.join(DEL, "README.md"))
    gl = os.path.join(ROOT, "work", "glossary.tsv")
    if os.path.exists(gl):
        shutil.copy2(gl, os.path.join(DEL, "术语对照表.tsv"))
    print("packed:", DEL)
    for f in sorted(os.listdir(DEL)):
        p = os.path.join(DEL, f)
        if os.path.isfile(p):
            print(f"  {f}  {os.path.getsize(p)//1024}KB")
        else:
            n = sum(len(fs) for _, _, fs in os.walk(p))
            print(f"  {f}/  {n} files")


if __name__ == "__main__":
    main()
