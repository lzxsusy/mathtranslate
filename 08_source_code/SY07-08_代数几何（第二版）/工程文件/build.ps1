param([switch]$Quick)
# SY07-08 build: xelatex -> makeindex -> xelatex x2 -> copy deliverable
$ErrorActionPreference = 'Continue'
$env:PATH = 'C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\;' + $env:PATH

$root = Split-Path -Parent $PSScriptRoot
$src  = Join-Path $root ([char]0x6E90 + [char]0x7801)          # 源码
$out  = Join-Path $root ([char]0x6210 + [char]0x54C1)          # 成品
Set-Location $src

function Run-XeLaTeX([string]$Tag) {
    Write-Host "== xelatex ($Tag)" -ForegroundColor Cyan
    & xelatex -interaction=nonstopmode -file-line-error main.tex 2>&1 | Out-File -FilePath "build_$Tag.log" -Encoding utf8
    if ($LASTEXITCODE -ne 0) { Write-Host "   exit=$LASTEXITCODE" -ForegroundColor Yellow }
}

Run-XeLaTeX 'pass1'
if (-not $Quick) {
    if (Test-Path main.idx) {
        Write-Host '== makeindex' -ForegroundColor Cyan
        & makeindex main.idx 2>&1 | Out-File -FilePath 'makeindex.log' -Encoding utf8
    }
}
Run-XeLaTeX 'pass2'
if (-not $Quick) { Run-XeLaTeX 'pass3' }

Write-Host ''
Write-Host '---- summary ----' -ForegroundColor Green
$log = Get-Content -LiteralPath 'main.log' -Encoding UTF8
foreach ($pat in @('Output written', 'LaTeX Warning: There were undefined references', 'Overfull \\hbox', 'Underfull \\hbox', 'Missing character')) {
    $n = ($log | Select-String -Pattern $pat).Count
    Write-Host ("{0,5}x  {1}" -f $n, $pat)
}
$log | Select-String -Pattern 'Output written' | ForEach-Object { Write-Host $_.Line }

if (Test-Path 'main.pdf') {
    $name = 'SY07-08_' + [string][char]0x4EE3 + [char]0x6570 + [char]0x51E0 + [char]0x4F55 + '_' +
            [char]0x4E2D + [char]0x6587 + [char]0x8BD1 + [char]0x6CE8 + [char]0x672C + '.pdf'
    $dest = Join-Path $out $name
    Copy-Item 'main.pdf' $dest -Force
    Write-Host ("copied -> " + $dest) -ForegroundColor Green
}
