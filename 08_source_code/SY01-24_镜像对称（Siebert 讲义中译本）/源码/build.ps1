$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSVersion.Major -lt 7) { throw '请使用 PowerShell 7 运行本脚本。' }
$texBin = 'C:\Users\Administrator\AppData\Local\Programs\TeXLive\2026\bin\windows'
$xe = Join-Path $texBin 'xelatex.exe'
$bib = Join-Path $texBin 'biber.exe'
if (-not (Test-Path -LiteralPath $xe)) { $xe = (Get-Command xelatex -ErrorAction Stop).Source }
if (-not (Test-Path -LiteralPath $bib)) { $bib = (Get-Command biber -ErrorAction Stop).Source }
Push-Location -LiteralPath $PSScriptRoot
try {
    & $xe -interaction=nonstopmode -halt-on-error main.tex
    if ($LASTEXITCODE -ne 0) { throw '第一遍 XeLaTeX 编译失败，请查看 main.log。' }
    & $bib main
    if ($LASTEXITCODE -ne 0) { throw 'Biber 编译失败，请查看 main.blg。' }
    & $xe -interaction=nonstopmode -halt-on-error main.tex
    if ($LASTEXITCODE -ne 0) { throw '第二遍 XeLaTeX 编译失败，请查看 main.log。' }
    & $xe -interaction=nonstopmode -halt-on-error main.tex
    if ($LASTEXITCODE -ne 0) { throw '第三遍 XeLaTeX 编译失败，请查看 main.log。' }
    Write-Host '已生成 main.pdf；中文索引由 imakeidx 自动编译。'
} finally { Pop-Location }
