@echo off
chcp 65001 >nul
cd /d "%~dp0"
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
findstr /C:"! " main.log && echo [ERROR] 见上
findstr /C:"Overfull" main.log && echo [OVERFULL] 见上
echo done.
