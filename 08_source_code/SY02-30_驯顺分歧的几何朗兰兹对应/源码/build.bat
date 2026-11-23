@echo off
REM build.bat —— 编译脚本（MiKTeX XeLaTeX）
REM 用法：
REM   build.bat            整书：xelatex x2
REM   build.bat full       整书：xelatex -> makeindex -> xelatex x2
REM   build.bat check <file> [tag]   单章快速编译（生成 _check[_tag].tex）
setlocal
set MIKTEX=C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64
set PATH=%MIKTEX%;%PATH%
set PYTHONIOENCODING=utf-8
cd /d "%~dp0"

if "%~1"=="check" goto check

xelatex -interaction=nonstopmode -halt-on-error main.tex
if errorlevel 1 goto fail
if "%~1"=="full" (
  makeindex main.idx
  xelatex -interaction=nonstopmode -halt-on-error main.tex
)
xelatex -interaction=nonstopmode -halt-on-error main.tex
if errorlevel 1 goto fail
echo BUILD OK
exit /b 0

:check
set F=%~2
set TAG=%~3
if "%TAG%"=="" set TAG=c
(
echo \documentclass[11pt,openany,oneside]{book}
echo \input{preamble}
echo \begin{document}
echo \input{%F%}
echo \end{document}
) > _check_%TAG%.tex
xelatex -interaction=nonstopmode -halt-on-error -jobname=_check_%TAG% _check_%TAG%.tex
if errorlevel 1 goto fail
echo CHECK OK
exit /b 0

:fail
echo BUILD FAILED
exit /b 1
