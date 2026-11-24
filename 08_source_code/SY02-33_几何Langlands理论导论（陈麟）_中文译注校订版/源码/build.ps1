$ErrorActionPreference = 'Stop'
Push-Location -LiteralPath $PSScriptRoot
try {
  New-Item -ItemType Directory -Path build -Force | Out-Null
  & xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
  if ($LASTEXITCODE -ne 0) { throw 'XeLaTeX failed.' }
  & biber --input-directory=build --output-directory=build main
  if ($LASTEXITCODE -ne 0) { throw 'Biber failed.' }
  & makeindex build/main.idx -o build/main.ind
  if ($LASTEXITCODE -ne 0) { throw 'MakeIndex failed.' }
  & xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
  if ($LASTEXITCODE -ne 0) { throw 'XeLaTeX failed.' }
  & makeindex build/main.idx -o build/main.ind
  & xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
  if ($LASTEXITCODE -ne 0) { throw 'XeLaTeX failed.' }
} finally { Pop-Location }
