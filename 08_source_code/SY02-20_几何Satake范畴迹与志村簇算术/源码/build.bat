@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
set XELATEX=C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe
if not exist "%XELATEX%" set XELATEX=xelatex
echo [1/2] xelatex main.tex
"%XELATEX%" -interaction=nonstopmode main.tex >nul
echo [2/2] xelatex main.tex
"%XELATEX%" -interaction=nonstopmode main.tex >nul
echo.
findstr /C:"Output written" main.log
findstr /B /C:"!" main.log
echo done.
endlocal
