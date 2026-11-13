# -*- coding: utf-8 -*-
r"""打包交付：deliverable/{pdf, src/, build脚本, compile.log, 译注汇总.md, README.md}
用法：python tools/pack.py
"""
import sys, io, os, shutil, glob
sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"<本地路径>"
ROOT = os.path.abspath(ROOT)
OUT = os.path.join(os.path.dirname(ROOT), "deliverable")
PDF = os.path.join(ROOT, "src", "main.pdf")
NAME = "Setter_thesis_中文译注本.pdf"

os.makedirs(OUT, exist_ok=True)
shutil.copy2(PDF, os.path.join(OUT, NAME))

src = os.path.join(OUT, "src")
if os.path.isdir(src):
    shutil.rmtree(src)
os.makedirs(os.path.join(src, "chunks"))
os.makedirs(os.path.join(src, "figures"))
for f in glob.glob(os.path.join(ROOT, "src", "*.tex")):
    shutil.copy2(f, src)
for f in glob.glob(os.path.join(ROOT, "src", "chunks", "*.tex")):
    shutil.copy2(f, os.path.join(src, "chunks"))
for f in glob.glob(os.path.join(ROOT, "src", "figures", "*.png")):
    shutil.copy2(f, os.path.join(src, "figures"))

tools = os.path.join(OUT, "tools")
if os.path.isdir(tools):
    shutil.rmtree(tools)
shutil.copytree(os.path.join(ROOT, "tools"), tools,
                ignore=shutil.ignore_patterns("tmp_*.py", "__pycache__"))

for f, dst in ((os.path.join(ROOT, "compile.log"), "compile.log"),
               (os.path.join(ROOT, "译注汇总.md"), "译注汇总.md"),
               (os.path.join(ROOT, "README.md"), "README.md"),
               (os.path.join(ROOT, "probe.md"), "probe.md"),
               (os.path.join(ROOT, "tags.txt"), "tags.txt"),
               (os.path.join(ROOT, "glossary.tsv"), "glossary.tsv"),
               (os.path.join(ROOT, "STYLE_GUIDE.md"), "STYLE_GUIDE.md")):
    if os.path.exists(f):
        shutil.copy2(f, os.path.join(OUT, dst))

build = """@echo off
chcp 65001 >nul
rem 一键编译：XeLaTeX ×3（需 MiKTeX / TeX Live，含 ctex 宏包）
cd /d "%~dp0src"
set TMP=%~dp0build
set TEMP=%TMP%
if not exist "%TMP%" mkdir "%TMP%"
xelatex -interaction=nonstopmode -file-line-error main.tex
xelatex -interaction=nonstopmode -file-line-error main.tex
xelatex -interaction=nonstopmode -file-line-error main.tex
copy /y main.log ..\\compile.log >nul
echo.
echo done: src\\main.pdf
pause
"""
io.open(os.path.join(OUT, "build_xelatex.bat"), "w", encoding="utf-8", newline="\r\n").write(build)

print("packed to", OUT)
for root, dirs, files in os.walk(OUT):
    lvl = root[len(OUT):].count(os.sep)
    print("  " * lvl + os.path.basename(root) + "/", f"({len(files)} files)")
