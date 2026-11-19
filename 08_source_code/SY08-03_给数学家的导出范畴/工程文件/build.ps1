# SY08-03 构建脚本（Windows / PowerShell）
# 用法：在 源码/ 目录下执行  powershell -ExecutionPolicy Bypass -File ..\工程文件\build.ps1
# 或在 工程文件/ 下执行   .\build.ps1
$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$src  = Join-Path $root '..\源码'
$xelatex = 'C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe'
if (-not (Test-Path $xelatex)) { $xelatex = 'xelatex' }

Push-Location $src
try {
    for ($i = 1; $i -le 2; $i++) {
        Write-Host "== xelatex pass $i =="
        & $xelatex -interaction=nonstopmode -halt-on-error main.tex | Out-Host
        if ($LASTEXITCODE -ne 0) { throw "xelatex pass $i failed (exit $LASTEXITCODE)" }
    }

    $log = Get-Content main.log -Raw -Encoding UTF8
    $errs = ([regex]::Matches($log, '(?m)^!')).Count
    $undef = ([regex]::Matches($log, 'undefined')).Count
    $over  = ([regex]::Matches($log, 'Overfull')).Count
    Write-Host "errors=$errs undefined=$undef overfull=$over"

    $pdf = Get-Item main.pdf
    Write-Host ("main.pdf  {0:N0} bytes  {1}" -f $pdf.Length, $pdf.LastWriteTime)

    if ($errs -gt 0 -or $undef -gt 0 -or $over -gt 0) { throw 'build check failed' }
}
finally {
    Pop-Location
}
