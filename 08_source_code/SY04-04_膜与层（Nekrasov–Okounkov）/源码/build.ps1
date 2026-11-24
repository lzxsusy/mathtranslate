# 一键编译（xelatex 两遍；MiKTeX / TeX Live 均可）
# 用法：cd 源码 ; powershell -NoProfile -ExecutionPolicy Bypass -File build.ps1
$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot

if (-not (Get-Command xelatex -ErrorAction SilentlyContinue)) {
    # 常见安装位置（含非默认盘符）：找到就临时加进 PATH
    $cands = @(
        "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64",
        "$env:ProgramFiles\MiKTeX\miktex\bin\x64",
        "$env:ProgramFiles\texlive\2025\bin\windows",
        "$env:ProgramFiles\texlive\2024\bin\windows"
    )
    foreach ($c in $cands) {
        if (Test-Path (Join-Path $c "xelatex.exe")) { $env:PATH = "$c;$env:PATH"; break }
    }
}
if (-not (Get-Command xelatex -ErrorAction SilentlyContinue)) {
    Write-Host "xelatex 不在 PATH 上：请安装 MiKTeX/TeX Live，或把 bin 目录加进 PATH。"
    exit 2
}

foreach ($i in 1..2) {
    Write-Host "== xelatex pass $i =="
    xelatex -interaction=nonstopmode -halt-on-error MDT_zh.tex | Out-Null
    if ($LASTEXITCODE -ne 0) { Write-Host "FAILED on pass $i -- see MDT_zh.log"; exit 1 }
}

$log = Get-Content MDT_zh.log -Raw
$pages = (Select-String -Path MDT_zh.log -Pattern 'Output written on .*\((\d+) pages' -AllMatches).Matches.Groups
Write-Host ("pages = " + (($pages | Where-Object { $_.Name -eq "1" }).Value -join ","))
Write-Host ("errors = " + ([regex]::Matches($log, "(?m)^!")).Count)
Write-Host ("undefined = " + ([regex]::Matches($log, "undefined")).Count)
Write-Host ("missing char = " + ([regex]::Matches($log, "Missing character")).Count)
Write-Host "done -> MDT_zh.pdf"
