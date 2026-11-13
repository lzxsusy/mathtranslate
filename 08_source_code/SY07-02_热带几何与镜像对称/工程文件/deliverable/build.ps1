$ErrorActionPreference = "Continue"
$here = $PSScriptRoot
$src = Join-Path $here "src"
$figs = Join-Path $here "work\figures"
$bin = "<本地路径>"
if (-not (Test-Path (Join-Path $bin "lualatex.exe"))) {
  $cands = @("<本地路径>", "C:\texlive\2026\bin\windows", "C:\texlive\2025\bin\windows")
  foreach ($c in $cands) { if (Test-Path (Join-Path $c "lualatex.exe")) { $bin = $c; break } }
}
if (-not (Test-Path (Join-Path $bin "lualatex.exe"))) { Write-Host "lualatex NOT FOUND"; exit 1 }
$build = "<本地路径>"
New-Item -ItemType Directory -Force "$build\chunks" | Out-Null
New-Item -ItemType Directory -Force "$build\figures" | Out-Null
New-Item -ItemType Directory -Force "$build\tmp" | Out-Null
Copy-Item "$src\main.tex" "$build\main.tex" -Force
Copy-Item "$src\preamble.tex" "$build\preamble.tex" -Force
if (Test-Path "$src\chunks\*.tex") { Copy-Item "$src\chunks\*.tex" "$build\chunks\" -Force }
if (Test-Path "$figs") { Copy-Item "$figs\*" "$build\figures\" -Force }
$env:PATH = "$bin;$env:PATH"
$env:TMP = "$build\tmp"
$env:TEMP = $env:TMP
Set-Location $build
foreach ($i in 1..3) {
  & (Join-Path $bin "lualatex.exe") -interaction=nonstopmode -file-line-error main.tex | Out-Null
  Write-Host "==> pass $i exit=$LASTEXITCODE"
}
if (Test-Path "$build\main.log") {
  Copy-Item "$build\main.log" "$here\work\tmp\main.log" -Force
  $log = Get-Content "$build\main.log" -Encoding UTF8 -Raw
  $errLines = [regex]::Matches($log, "(?m)^[^\r\n]*?:\d+: .*$") | ForEach-Object { $_.Value }
  $fatal = [regex]::Matches($log, "(?m)^! .*$") | ForEach-Object { $_.Value }
  $missing = [regex]::Matches($log, "Missing character: There is no")
  Write-Host "--- file:line errors: $($errLines.Count) ---"
  $errLines | Select-Object -First 40 | ForEach-Object { Write-Host $_ }
  Write-Host "--- '!' errors: $($fatal.Count); missing-char: $($missing.Count) ---"
  $fatal | Select-Object -First 15 | ForEach-Object { Write-Host $_ }
}
if (Test-Path "$build\main.pdf") {
  $sz = (Get-Item "$build\main.pdf").Length
  Copy-Item "$build\main.pdf" "$src\main.pdf" -Force
  Write-Host "main.pdf = $sz bytes (copied to src\main.pdf)"
} else { Write-Host "main.pdf MISSING" }
