$ErrorActionPreference = 'Stop'
Push-Location -LiteralPath $PSScriptRoot
try {
    New-Item -ItemType Directory -Path 'build' -Force | Out-Null
    & xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
    if ($LASTEXITCODE -ne 0) { throw 'XeLaTeX failed.' }
    & makeindex -o build/main.ind build/main.idx
    if ($LASTEXITCODE -ne 0) { throw 'makeindex failed.' }
    & xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
    if ($LASTEXITCODE -ne 0) { throw 'XeLaTeX failed.' }
    & xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
    if ($LASTEXITCODE -ne 0) { throw 'XeLaTeX failed.' }
    Write-Output 'PDF: build/main.pdf'
} finally {
    Pop-Location
}
