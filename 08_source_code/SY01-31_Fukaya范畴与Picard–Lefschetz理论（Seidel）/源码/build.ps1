$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSVersion.Major -lt 7) { throw 'PowerShell 7 required.' }
Set-Location -LiteralPath $PSScriptRoot
$seidelXeLaTeX = 'C:\Users\Administrator\AppData\Local\Programs\TeXLive\2026\bin\windows\xelatex.exe'
if (-not (Test-Path -LiteralPath $seidelXeLaTeX)) { $seidelXeLaTeX = 'xelatex' }
& $seidelXeLaTeX -interaction=nonstopmode -halt-on-error main.tex
if ($LASTEXITCODE -ne 0) { throw 'First XeLaTeX pass failed; see main.log.' }
1..2 | ForEach-Object {
    if (Test-Path -LiteralPath 'main.idx') {
        & makeindex main.idx
        if ($LASTEXITCODE -ne 0) { throw 'Index build failed.' }
    }
    & $seidelXeLaTeX -interaction=nonstopmode -halt-on-error main.tex
    if ($LASTEXITCODE -ne 0) { throw 'XeLaTeX pass failed; see main.log.' }
}
