# 编译脚本（本机环境：工作区内便携 TeX Live 2026；用 LuaLaTeX，因为 xdvipdfmx 会崩）
# 用法：在 PowerShell 中执行  .\build.ps1
$ErrorActionPreference = "Stop"
$cands = @(
    "<本地路径>",
    "<本地路径>"
)
$bin = $cands | Where-Object { Test-Path (Join-Path $_ "lualatex.exe") } | Select-Object -First 1
if (-not $bin) { Write-Host "未找到 TeX 安装，请安装 TeX Live 或 TinyTeX"; exit 1 }
$env:PATH = "$bin;$env:PATH"

foreach ($i in 1..3) {
    Write-Host "==> 第 $i 遍 lualatex"
    & (Join-Path $bin "lualatex.exe") -interaction=nonstopmode main.tex | Out-Null
    if ($LASTEXITCODE -ne 0) { Write-Host "第 $i 遍失败，请查看 main.log"; exit 1 }
}
Write-Host "完成：main.pdf"
