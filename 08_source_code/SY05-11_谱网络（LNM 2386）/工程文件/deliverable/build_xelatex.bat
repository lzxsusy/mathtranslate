@echo off
REM 一键编译（Windows）。注意：项目路径必须全 ASCII；TMP 必须指到可写目录。
setlocal
cd /d "%~dp0src"
set TMP=%~dp0tmp
set TEMP=%TMP%
if not exist "%TMP%" mkdir "%TMP%"
set XELATEX=C:\Users\admin\Documents\deepseek-harness\default-workspace\texlive\bin\windows\xelatex.exe
"%XELATEX%" -interaction=nonstopmode -file-line-error main.tex
"%XELATEX%" -interaction=nonstopmode -file-line-error main.tex
echo.
echo Done. Check main.pdf
pause
