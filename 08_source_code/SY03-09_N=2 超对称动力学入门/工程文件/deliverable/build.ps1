# One-click build entry for the deliverable (same as .\src\build.ps1).
# Usage: powershell -ExecutionPolicy Bypass -File .\build.ps1
# The real logic lives in .\src\build.ps1: it mirrors src/ + src/figures/ to an ASCII-writable
# build directory (default: ...\default-workspace\n2build), runs XeLaTeX + makeindex + XeLaTeX x2,
# then copies main.pdf back into src/.
$ErrorActionPreference = "Stop"
$src = Join-Path $PSScriptRoot "src\build.ps1"
if (-not (Test-Path $src)) { Write-Host "missing $src"; exit 1 }
& powershell -ExecutionPolicy Bypass -File $src
exit $LASTEXITCODE
