# 编译 witten9301042-zh/main.tex → build/main.pdf（两遍以生成目录）
# 用法：pwsh -File build.ps1
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$tec = "<本地路径>"
$env:TECTONIC_CACHE_DIR = "<本地路径>"

& $tec -X compile "$root\main.tex" --outdir "$root\build" --keep-intermediates --keep-logs 2>&1 |
    Where-Object { $_ -notmatch "Fontconfig error" }

if ($LASTEXITCODE -ne 0) {
    Write-Host "COMPILE FAILED" -ForegroundColor Red
    exit 1
}
Write-Host "OK -> $root\build\main.pdf" -ForegroundColor Green
