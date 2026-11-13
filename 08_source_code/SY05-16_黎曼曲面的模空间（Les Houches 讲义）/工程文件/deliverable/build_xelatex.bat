@echo off
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
