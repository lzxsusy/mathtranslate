@echo off
chcp 65001 >nul
rem 一键编译：XeLaTeX ×3（需 MiKTeX / TeX Live，含 ctex 宏包）
cd /d "%~dp0src"
set TMP=%~dp0build
set TEMP=%TMP%
if not exist "%TMP%" mkdir "%TMP%"
xelatex -interaction=nonstopmode -file-line-error main.tex
xelatex -interaction=nonstopmode -file-line-error main.tex
xelatex -interaction=nonstopmode -file-line-error main.tex
copy /y main.log ..\compile.log >nul
echo.
echo done: src\main.pdf
pause
