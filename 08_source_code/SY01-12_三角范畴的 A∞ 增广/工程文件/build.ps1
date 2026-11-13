# build.ps1 —— JP07 一键编译（整书两遍 xelatex，产物复制到 deliverable/）
# 用法：powershell -ExecutionPolicy Bypass -File build.ps1
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

$out = Join-Path $root 'work\main_build'
New-Item -ItemType Directory -Force $out | Out-Null
$outArg = $out.Replace('\', '/')
New-Item -ItemType Directory -Force (Join-Path $root 'deliverable') | Out-Null

Push-Location (Join-Path $root 'src')
foreach ($run in 1, 2) {
    Write-Host "=== xelatex pass $run ==="
    & xelatex -interaction=nonstopmode "-output-directory=$outArg" main.tex | Out-Null
    if (-not (Test-Path (Join-Path $out 'main.pdf'))) {
        Write-Host "FAILED: no main.pdf after pass $run; see work/main_build/main.log"
        Pop-Location
        exit 1
    }
}
Pop-Location

$log = Join-Path $out 'main.log'
$txt = Get-Content $log -Raw -Encoding UTF8
$errs   = ([regex]::Matches($txt, '(?m)^!')).Count
$over   = ([regex]::Matches($txt, 'Overfull \\hbox')).Count
$undef  = ([regex]::Matches($txt, 'Reference .* undefined')).Count
$miss   = ([regex]::Matches($txt, 'Missing character')).Count
Write-Host "errors=$errs overfull=$over undefined=$undef missing_char=$miss"

$pdf = Join-Path $out 'main.pdf'
$dest = Join-Path $root 'deliverable\梶浦宏成_三角圏のA∞増強について_中文译注本.pdf'
Copy-Item $pdf $dest -Force
Write-Host "deliverable -> $dest"
