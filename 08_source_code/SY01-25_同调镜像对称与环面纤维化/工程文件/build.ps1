# =============================================================================
#  build.ps1 —— SY01-25《同调镜像对称与环面纤维化》中译注本
#  用法（在 工程文件 目录下）：powershell -ExecutionPolicy Bypass -File build.ps1
#  可选：-Clean  先删除 aux 中间文件；-Quick 只编译一遍
# =============================================================================
param(
    [switch]$Clean,
    [switch]$Quick
)

$ErrorActionPreference = 'Stop'
$root    = Split-Path -Parent $PSScriptRoot          # 项目根 SY01-25
$src     = Join-Path $root '源码'
$output  = Join-Path $root '成品'
$name    = 'Kontsevich-Soibelman_环面纤维化HMS_中文译注本'

$xelatex = 'C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe'
if (-not (Test-Path $xelatex)) { throw "找不到 xelatex: $xelatex" }

if (-not (Test-Path $output)) { New-Item -ItemType Directory -Path $output | Out-Null }

Push-Location $src
try {
    if ($Clean) {
        Get-ChildItem -File | Where-Object { $_.Extension -in '.aux', '.log', '.out', '.toc' } |
            Remove-Item -Force
    }

    $passes = if ($Quick) { 1 } else { 3 }
    for ($i = 1; $i -le $passes; $i++) {
        Write-Host "== xelatex 第 $i / $passes 遍 ==" -ForegroundColor Cyan
        & $xelatex -interaction=nonstopmode -halt-on-error 'main.tex' | Out-Null
        if ($LASTEXITCODE -ne 0) {
            Write-Host "编译失败，见 源码\main.log" -ForegroundColor Red
            Select-String -Path 'main.log' -Pattern '^!|^l\.\d+' | Select-Object -First 20 |
                ForEach-Object { Write-Host $_.Line }
            throw "xelatex 退出码 $LASTEXITCODE"
        }
    }

    $log = Get-Content 'main.log' -Raw -Encoding UTF8
    $over = [regex]::Matches($log, 'Overfull \\hbox').Count
    $under = [regex]::Matches($log, 'Underfull \\hbox').Count
    $undef = [regex]::Matches($log, 'Undefined control sequence').Count
    $miss  = [regex]::Matches($log, 'LaTeX Warning: Reference').Count
    Write-Host ("诊断：Overfull {0} 处，Underfull {1} 处，未定义命令 {2} 处，未解析引用 {3} 处" -f $over, $under, $undef, $miss)

    $pdf = Join-Path $src 'main.pdf'
    if (-not (Test-Path $pdf)) { throw '没有生成 main.pdf' }
    $dest = Join-Path $output "$name.pdf"
    Copy-Item $pdf $dest -Force
    Write-Host "成品：$dest" -ForegroundColor Green
}
finally {
    Pop-Location
}
