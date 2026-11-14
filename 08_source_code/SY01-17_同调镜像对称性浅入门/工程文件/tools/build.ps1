# 编译《同调镜像对称性浅入门》中译本
# 用法： pwsh -File tools/build.ps1 [-Chapter 3]
#   -Chapter N：只编译“主文档 + 第 N 章”的草稿（快速语法检查，输出 build/checkNN.pdf）
param(
    [int]$Chapter = 0
)

$ErrorActionPreference = "Continue"
$tex  = "<本地路径>"
$deps = "<本地路径>"
$env:PATH = "$tex;$env:PATH"
$env:TEXMFHOME = $deps

$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $root
New-Item -ItemType Directory -Force -Path build | Out-Null

if ($Chapter -gt 0) {
    # 单章草稿：抽取 main.tex 的导言区 + 指定章
    $nn = "{0:D2}" -f $Chapter
    $main = Get-Content main.tex -Raw -Encoding UTF8
    $head = $main.Substring(0, $main.IndexOf("\begin{document}"))
    $head += "`n\begin{document}`n\mainmatter`n\chapter{第 $Chapter 章草稿}`n\setcounter{chapter}{$($Chapter-1)}`n\input{chapters/ch$nn}`n\end{document}`n"
    Set-Content -Path "check$nn.tex" -Value $head -Encoding UTF8
    & xelatex -interaction=nonstopmode -halt-on-error -output-directory=build "check$nn.tex" *> "build/run-check$nn.txt"
    Remove-Item "check$nn.tex" -ErrorAction SilentlyContinue
    if ($LASTEXITCODE -ne 0) { Write-Host "FAILED check$nn" -ForegroundColor Red; exit 1 }
    Write-Host "OK check$nn.pdf" -ForegroundColor Green
    exit 0
}

& xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex *> build\pass1.log
if ($LASTEXITCODE -ne 0) { Write-Host "xelatex pass1 FAILED" -ForegroundColor Red; Get-Content build\pass1.log -Tail 30; exit 1 }

& makeindex -o build/main.ind build/main.idx *> build\makeindex.log
& xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex *> build\pass2.log
& xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex *> build\pass3.log
if ($LASTEXITCODE -ne 0) { Write-Host "xelatex pass3 FAILED" -ForegroundColor Red; Get-Content build\pass3.log -Tail 30; exit 1 }

# 质量检查
$log = Get-Content build\main.log -Raw -Encoding UTF8
$undef = ([regex]::Matches($log, "Reference .* undefined")).Count
$dup   = ([regex]::Matches($log, "destination with the same identifier")).Count
$over  = ([regex]::Matches($log, "Overfull \\hbox")).Count
$miss  = ([regex]::Matches($log, "Missing character")).Count
$pages = if ($log -match "Output written on build/main.pdf \((\d+) pages") { $Matches[1] } else { "?" }
Write-Host ("pages={0}  undefined_refs={1}  duplicate_dest={2}  overfull={3}  missing_glyph={4}" -f $pages, $undef, $dup, $over, $miss)
if ($undef -or $dup -or $miss) { Write-Host "QUALITY CHECKS FAILED" -ForegroundColor Red; exit 2 }
Write-Host "BUILD OK" -ForegroundColor Green
