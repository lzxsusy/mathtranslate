# build.ps1 -- one-click build + quality gate (SY05-26)
# Usage:  powershell -ExecutionPolicy Bypass -File <project>\build.ps1
# ASCII only on purpose: Windows PowerShell 5.1 misreads UTF-8 .ps1 without BOM.

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot          # project folder (contains the source dir)
if (Test-Path (Join-Path $root 'main.tex')) {
    $src = $root
} else {
    $cand = Get-ChildItem -Path $root -Directory |
            Where-Object { Test-Path (Join-Path $_.FullName 'main.tex') } |
            Select-Object -First 1
    if (-not $cand) { throw "cannot locate main.tex under $root" }
    $src = $cand.FullName
}
Push-Location $src
try {
    Write-Host "== build: $src\main.tex" -ForegroundColor Cyan
    for ($i = 1; $i -le 2; $i++) {
        & xelatex -interaction=nonstopmode -halt-on-error main.tex | Out-Null
        if ($LASTEXITCODE -ne 0) { throw "xelatex pass $i failed (exit $LASTEXITCODE); see main.log" }
        Write-Host "   pass $i ok"
    }

    $log = Get-Content main.log -Raw -Encoding UTF8
    $errors    = ([regex]::Matches($log, '(?m)^!')).Count
    $undef     = ([regex]::Matches($log, 'undefined')).Count
    $overfull  = ([regex]::Matches($log, 'Overfull')).Count
    $underfull = ([regex]::Matches($log, 'Underfull')).Count

    $pdf  = Get-Item main.pdf
    $info = (& pdfinfo main.pdf) -join "`n"
    $pages = if ($info -match 'Pages:\s+(\d+)') { $matches[1] } else { '?' }

    Write-Host ""
    Write-Host ("errors    : {0}" -f $errors)
    Write-Host ("undefined : {0}" -f $undef)
    Write-Host ("Overfull  : {0}" -f $overfull)
    Write-Host ("Underfull : {0}" -f $underfull)
    Write-Host ("PDF       : {0} pages, {1:N0} bytes, {2}" -f $pages, $pdf.Length, $pdf.LastWriteTime)

    if ($errors   -gt 0) { throw "quality gate failed: $errors error(s)" }
    if ($undef    -gt 0) { throw "quality gate failed: $undef undefined reference(s)" }
    if ($overfull -gt 0) { throw "quality gate failed: $overfull overfull box(es)" }
    Write-Host "quality gate passed (0 error / 0 undefined / 0 overfull)" -ForegroundColor Green
}
finally {
    Pop-Location
}
