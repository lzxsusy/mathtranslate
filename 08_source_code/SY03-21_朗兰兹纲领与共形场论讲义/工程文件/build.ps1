# build.ps1 -- build both deliverable PDFs of the Frenkel lecture translation project.
# Usage:
#   .\build.ps1              # build main translation + reading notes
#   .\build.ps1 -MainOnly    # only the translation
#   .\build.ps1 -NotesOnly   # only the reading notes

param(
    [switch]$MainOnly,
    [switch]$NotesOnly
)

$ErrorActionPreference = "Continue"
$texbin = "<本地路径>"
$env:PATH = "$texbin;$env:PATH"
Set-Location -Path $PSScriptRoot

function Build-One([string]$name) {
    Write-Host "=== building $name ===" -ForegroundColor Cyan
    if (Test-Path "$name.aux") { Remove-Item "$name.aux" -ErrorAction SilentlyContinue }
    & latexmk -xelatex -interaction=nonstopmode -halt-on-error "$name.tex"
    $log = "$name.log"
    if (Test-Path $log) {
        $errs = Select-String -Path $log -Pattern '^! ' -AllMatches
        if ($errs) {
            Write-Host "!!! $name : LaTeX errors found:" -ForegroundColor Red
            $errs | ForEach-Object { Write-Host $_.Line }
            return $false
        }
        $out = Select-String -Path $log -Pattern 'Output written on' | Select-Object -Last 1
        if ($out) { Write-Host $out.Line -ForegroundColor Green } else { Write-Host "no Output written line" -ForegroundColor Yellow }
    }
    if (Test-Path "$name.pdf") { return $true } else { return $false }
}

$ok = $true
if (-not $NotesOnly) { if (-not (Build-One "main")) { $ok = $false } }
if (-not $MainOnly)  { if (-not (Build-One "notes_main")) { $ok = $false } }

if ($ok) { Write-Host "ALL OK" -ForegroundColor Green } else { Write-Host "BUILD FAILED" -ForegroundColor Red }
