# =====================================================================
#  build.ps1 -- build the Chinese annotated translation of
#  Dan Xie, "General Argyres-Douglas Theory" (arXiv:1204.2270v2)
#
#  Usage:  powershell -ExecutionPolicy Bypass -File build.ps1
#  Output: ..\成品\广义 Argyres-Douglas 理论（中文译注本）.pdf
#  ASCII only on purpose: Windows PowerShell 5.1 misreads UTF-8 files
#  without a BOM, so no Chinese literal appears in this script.
# =====================================================================

$ErrorActionPreference = 'Stop'

$src   = Split-Path -Parent $MyInvocation.MyCommand.Path      # ...\源码
$root  = Split-Path -Parent $src                              # project root
$out   = Join-Path $root '成品'
$main  = 'main'
$pdfIn = Join-Path $src ($main + '.pdf')

# output name = project folder name without the "SYnn-nn_" prefix
$proj  = Split-Path -Leaf $root
if ($proj -match '^SY\d+-\d+_(.+)$') { $proj = $Matches[1] }
$pdfOut = Join-Path $out ($proj + '.pdf')

$env:PATH = 'C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64;' + $env:PATH
$xelatex  = 'C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe'
if (-not (Test-Path $xelatex)) { throw "xelatex not found: $xelatex" }

Push-Location $src
try {
    for ($pass = 1; $pass -le 2; $pass++) {
        Write-Host "== xelatex pass $pass =="
        & $xelatex -interaction=nonstopmode -halt-on-error ("{0}.tex" -f $main) | Out-Null
        if ($LASTEXITCODE -ne 0) {
            Write-Host "!! xelatex failed on pass $pass (exit $LASTEXITCODE)" -ForegroundColor Red
            Select-String -Path ("{0}.log" -f $main) -Pattern '^!' -Context 0,3 |
                Select-Object -First 8 | ForEach-Object { $_.Line }
            throw "build failed"
        }
    }

    $log = Get-Content ("{0}.log" -f $main) -Encoding UTF8 -Raw
    $report = @()

    $m = [regex]::Match($log, 'Output written on .*?\((\d+) pages')
    if ($m.Success) {
        $report += ("pages            : {0}" -f $m.Groups[1].Value)
        $pages = [int]$m.Groups[1].Value
    } else {
        $report += 'pages            : (not found in log)'
        $pages = 0
    }

    $missing = ([regex]::Matches($log, 'Missing character')).Count
    $report += ("missing chars    : {0}" -f $missing)

    $overfull = ([regex]::Matches($log, '^Overfull \hbox', 'Multiline')).Count
    $report += ("overfull hboxes  : {0}" -f $overfull)

    $underfull = ([regex]::Matches($log, '^Underfull \hbox', 'Multiline')).Count
    $report += ("underfull hboxes : {0}" -f $underfull)

    $undef = ([regex]::Matches($log, 'undefined')).Count
    $report += ("undefined refs   : {0}" -f $undef)

    if (-not (Test-Path $out)) { New-Item -ItemType Directory -Path $out | Out-Null }
    Copy-Item -Path $pdfIn -Destination $pdfOut -Force
    $report += ("copied to        : {0}" -f $pdfOut)

    Write-Host ''
    $report | ForEach-Object { Write-Host $_ }

    if ($missing -gt 0 -or $undef -gt 0) {
        Write-Host ''
        Write-Host 'WARNING: missing characters or undefined references -- inspect ' -NoNewline -ForegroundColor Yellow
        Write-Host ("{0}.log" -f $main) -ForegroundColor Yellow
        exit 2
    }
    if ($pages -lt 40) {
        Write-Host ("WARNING: only {0} pages; expected at least 40." -f $pages) -ForegroundColor Yellow
    }
    Write-Host 'OK' -ForegroundColor Green
}
finally {
    Pop-Location
}
