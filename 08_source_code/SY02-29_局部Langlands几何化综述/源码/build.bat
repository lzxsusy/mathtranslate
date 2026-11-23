@echo off
rem build.bat —— 单章/整章编译入口（在 源码/ 下运行）
rem 用法：build.bat                      整书两遍（xelatex main ×2）
rem       build.bat check <file> [tag]   单章草稿编译（生成 _check[_tag].pdf）
rem       tag 用于并行：三个人同时 check 时各给自己一个 tag（a/b/c），互不覆盖。
setlocal
set MIKTEX=C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64
set PATH=%MIKTEX%;%PATH%
set PYTHONIOENCODING=utf-8

if /I "%~1"=="check" goto check
xelatex -interaction=nonstopmode -halt-on-error main.tex
if errorlevel 1 goto fail
xelatex -interaction=nonstopmode -halt-on-error main.tex
if errorlevel 1 goto fail
echo [OK] main.pdf
exit /b 0

:check
set TAG=%~3
if "%TAG%"=="" set JOB=_check
if not "%TAG%"=="" set JOB=_check_%TAG%
echo \documentclass[11pt,openany]{book}> %JOB%.tex
echo \input{preamble}>> %JOB%.tex
echo \begin{document}>> %JOB%.tex
echo \input{"%~2"}>> %JOB%.tex
echo \end{document}>> %JOB%.tex
xelatex -interaction=nonstopmode -halt-on-error -jobname=%JOB% %JOB%.tex
if errorlevel 1 goto fail
echo [OK] %JOB%.pdf
exit /b 0

:fail
echo [FAIL] 见 main.log / _check*.log
exit /b 1
