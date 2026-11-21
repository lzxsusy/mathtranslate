# GMN1 中译 —— 一键编译
# 用法：powershell -ExecutionPolicy Bypass -File build.ps1
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$src  = Join-Path (Split-Path -Parent $root) "源码"
$xelatex = "C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe"

Push-Location $src
try {
    for ($i = 1; $i -le 3; $i++) {
        Write-Host "== xelatex pass $i =="
        & $xelatex -interaction=nonstopmode -halt-on-error main.tex | Out-Null
        if ($LASTEXITCODE -ne 0) { throw "xelatex 第 $i 遍失败，见 main.log" }
    }
    Copy-Item -Force main.pdf (Join-Path (Split-Path -Parent $src) "成品\_latest.pdf")
    Write-Host "OK -> 成品\_latest.pdf"
} finally {
    Pop-Location
}
