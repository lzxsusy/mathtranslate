@echo off
setlocal
cd /d "%~dp0"
set XELATEX=xelatex
where xelatex >nul 2>nul || set XELATEX="C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe"
%XELATEX% -interaction=nonstopmode -halt-on-error main.tex
if errorlevel 1 goto :fail
%XELATEX% -interaction=nonstopmode -halt-on-error main.tex
if errorlevel 1 goto :fail
%XELATEX% -interaction=nonstopmode -halt-on-error main.tex
if errorlevel 1 goto :fail
echo.
echo Build OK: main.pdf
exit /b 0
:fail
echo.
echo Build FAILED - see main.log
exit /b 1
