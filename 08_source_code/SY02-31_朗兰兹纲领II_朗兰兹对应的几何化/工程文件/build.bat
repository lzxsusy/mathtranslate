@echo off
REM SY02-31 编译脚本：XeLaTeX 三遍
setlocal
cd /d "%~dp0..\源码"
echo [1/3] xelatex pass 1
xelatex -interaction=nonstopmode -halt-on-error main.tex > build1.log 2>&1
if errorlevel 1 goto :fail
echo [2/3] xelatex pass 2
xelatex -interaction=nonstopmode -halt-on-error main.tex > build2.log 2>&1
if errorlevel 1 goto :fail
echo [3/3] xelatex pass 3
xelatex -interaction=nonstopmode -halt-on-error main.tex > build3.log 2>&1
if errorlevel 1 goto :fail
echo.
echo ==== audit ====
findstr /C:"Overfull" /C:"Underfull" /C:"Warning" /C:"Missing character" build3.log
echo.
echo OK: main.pdf
goto :eof

:fail
echo.
echo FAILED - see build1.log / build3.log
type build3.log 2>nul
exit /b 1
