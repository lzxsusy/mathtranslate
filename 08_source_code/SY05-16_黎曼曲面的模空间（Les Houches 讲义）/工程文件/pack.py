# -*- coding: utf-8 -*-
"""pack.py — 打包 deliverable/（交付契约）

产出：
  deliverable/
    黎曼曲面的模空间_中文译注本.pdf
    src/                    全部 .tex
    main.tex
    build_xelatex.bat       一键编译
    compile.log             真实编译日志
    译注汇总.md
    ERRATA.md
    README.md               已填统计数字
"""
import os, re, shutil, sys

ROOT = r"<本地路径>"
DEST = os.path.join(ROOT, "deliverable")
PDF = os.path.join(ROOT, "main.pdf")

# ---- 统计 ----
import pymupdf
doc = pymupdf.open(PDF)
pages = len(doc)
notes = 0
np_ = os.path.join(ROOT, "译注汇总.md")
if os.path.exists(np_):
    m = re.search(r"\*\*共 (\d+) 条批注", open(np_, encoding="utf-8").read())
    if m:
        notes = int(m.group(1))

# ---- README 替换 ----
readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
readme = readme.replace("{{PAGES}}", str(pages)).replace("{{NOTES}}", str(notes))

BAT = r"""@echo off
rem 一键编译：XeLaTeX ×2（必须先设可写的 TMP，本机曾因 TMP 不可用导致 xdvipdfmx 崩溃）
chcp 65001 >nul
setlocal
set "HERE=%~dp0"
set "TMP=%HERE%tmp"
set "TEMP=%TMP%"
set "TMPDIR=%TMP%"
if not exist "%TMP%" mkdir "%TMP%"
set "XELATEX=G:\texlive\2026\bin\windows\xelatex.exe"
if not exist "%XELATEX%" (
  echo [ERROR] 找不到 %XELATEX%
  echo 请修改本脚本里的 XELATEX 变量为你的 xelatex 绝对路径。
  exit /b 1
)
"%XELATEX%" -interaction=nonstopmode -file-line-error main.tex
"%XELATEX%" -interaction=nonstopmode -file-line-error main.tex
if exist main.pdf (
  echo [OK] main.pdf 已生成
) else (
  echo [FAIL] 未生成 main.pdf，请看 main.log
)
endlocal
"""

if os.path.exists(DEST):
    shutil.rmtree(DEST)
os.makedirs(os.path.join(DEST, "src"))

shutil.copy2(PDF, os.path.join(DEST, "黎曼曲面的模空间_中文译注本.pdf"))
shutil.copy2(os.path.join(ROOT, "main.tex"), DEST)
shutil.copy2(os.path.join(ROOT, "compile.log"), DEST)
open(os.path.join(DEST, "build_xelatex.bat"), "w", encoding="utf-8-sig", newline="\r\n").write(BAT)
for f in ["译注汇总.md", "ERRATA.md", "README.md"]:
    p = os.path.join(ROOT, f)
    if os.path.exists(p):
        if f == "README.md":
            open(os.path.join(DEST, f), "w", encoding="utf-8", newline="\n").write(readme)
        else:
            shutil.copy2(p, DEST)
for f in sorted(os.listdir(os.path.join(ROOT, "src"))):
    if f.endswith(".tex"):
        shutil.copy2(os.path.join(ROOT, "src", f), os.path.join(DEST, "src", f))

print("deliverable/ 已生成：%d 页 PDF，%d 条批注" % (pages, notes))
for r, d, fs in os.walk(DEST):
    for f in fs:
        p = os.path.join(r, f)
        print("  %-58s %8d B" % (os.path.relpath(p, ROOT), os.path.getsize(p)))
