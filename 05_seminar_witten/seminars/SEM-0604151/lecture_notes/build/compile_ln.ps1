# Compile the Kapustin-Witten lecture notes (ASCII only: PS 5.1 reads this as ANSI)
# Usage: powershell -NoProfile -ExecutionPolicy Bypass -File build\compile_ln.ps1
$ErrorActionPreference = 'Continue'
$Root = Split-Path -Parent $PSScriptRoot
$Src  = $Root
$Out  = Join-Path $Root 'build\out'
$Log  = Join-Path $Root 'build\ln.log'
New-Item -ItemType Directory -Force -Path $Out | Out-Null

$xelatex = 'C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe'
if (-not (Test-Path $xelatex)) { Write-Host "xelatex not found: $xelatex"; exit 1 }

Push-Location $Src
$xargs = @('-interaction=nonstopmode','-halt-on-error','-file-line-error',("-output-directory=" + $Out),'main.tex')
$rc = 0
for ($i = 1; $i -le 2; $i++) {
    & $xelatex @xargs *> $Log
    $code = $LASTEXITCODE
    Write-Host ("pass " + $i + " rc=" + $code)
    if ($code -ne 0) { $rc = $code; break }
}
Pop-Location

$pdf = Join-Path $Out 'main.pdf'
$text = ''
if (Test-Path $Log) { $text = Get-Content -Path $Log -Raw -ErrorAction SilentlyContinue }
$errors = ([regex]::Matches($text, '(?m)^!')).Count
$overfull = ([regex]::Matches($text, 'Overfull \\hbox')).Count
$underfull = ([regex]::Matches($text, 'Underfull \\hbox')).Count
$missing = ([regex]::Matches($text, 'Missing character')).Count
$pages = 0
if (Test-Path $pdf) {
    $pdfinfo = 'C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdfinfo.exe'
    if (Test-Path $pdfinfo) {
        $info = & $pdfinfo $pdf
        foreach ($line in $info) { if ($line -match '^Pages:\s+(\d+)') { $pages = [int]$Matches[1] } }
    }
    $dest = Join-Path $Src 'deliverables'
    New-Item -ItemType Directory -Force -Path $dest | Out-Null
    Copy-Item -Path $pdf -Destination (Join-Path $dest 'KW_lecture_notes.pdf') -Force
}

Write-Host ("pages    " + $pages)
Write-Host ("errors   " + $errors)
Write-Host ("overfull " + $overfull + " / underfull " + $underfull)
Write-Host ("missing  " + $missing)
if (Test-Path $pdf) { Write-Host ("pdf      " + $pdf + " (" + (Get-Item $pdf).Length + " bytes)") }
if ($rc -eq 0 -and $errors -gt 0) { $rc = 1 }
exit $rc
