# =====================================================================
#  build.ps1 -- mirror build (two hard constraints on this machine):
#  (1) LuaTeX cannot write .log under a non-ASCII path;
#  (2) child processes cannot write to Desktop.
#  So src/ + figures/ are mirrored to an ASCII writable dir under
#  default-workspace, compiled there, and main.pdf is copied back.
#  usage: powershell -ExecutionPolicy Bypass -File work\src\build.ps1
# =====================================================================
$ErrorActionPreference = "Continue"
$bin = "<本地路径>"
if (-not (Test-Path (Join-Path $bin "lualatex.exe"))) {
  $cands = @("C:\texlive\2026\bin\windows", "C:\texlive\2025\bin\windows",
             "<本地路径>")
  foreach ($c in $cands) { if (Test-Path (Join-Path $c "lualatex.exe")) { $bin = $c; break } }
}
$here  = Split-Path -Parent $MyInvocation.MyCommand.Path      # ...\work\src (or deliverable root)
if (-not (Test-Path (Join-Path $here "main.tex"))) {
  if (Test-Path (Join-Path $here "src\main.tex")) { $here = Join-Path $here "src" }
}
$work  = Split-Path -Parent $here                            # ...\work
$proj  = Split-Path -Parent $work                            # project root
$root  = "<本地路径>"
New-Item -ItemType Directory -Force -Path $root | Out-Null
New-Item -ItemType Directory -Force -Path "$root\chunks" | Out-Null
New-Item -ItemType Directory -Force -Path "$root\figures" | Out-Null
New-Item -ItemType Directory -Force -Path "$root\tmp" | Out-Null

Copy-Item -Path @("$here\main.tex", "$here\preamble.tex") -Destination $root -Force
Copy-Item -Path "$here\chunks\*.tex" -Destination "$root\chunks\" -Force
if (Test-Path "$work\figures\*.png") {
  Copy-Item -Path "$work\figures\*.png" -Destination "$root\figures\" -Force
} elseif (Test-Path "$here\figures\*.png") {
  Copy-Item -Path "$here\figures\*.png" -Destination "$root\figures\" -Force
}

$env:PATH = "$bin;$env:PATH"
$env:TMP  = "$root\tmp"
$env:TEMP = $env:TMP
Set-Location $root

foreach ($i in 1..3) {
  & (Join-Path $bin "lualatex.exe") -interaction=nonstopmode -file-line-error main.tex | Out-Null
  Write-Host "==> pass $i exit=$LASTEXITCODE"
}
if (Test-Path "$root\main.log") {
  New-Item -ItemType Directory -Force -Path "$work\tmp" | Out-Null
  Copy-Item "$root\main.log" "$work\tmp\main.log" -Force
  $log = Get-Content "$root\main.log" -Encoding UTF8 -Raw
  $errLines = [regex]::Matches($log, "(?m)^[^\r\n]*?:\d+: .*$") | ForEach-Object { $_.Value }
  $fatal    = [regex]::Matches($log, "(?m)^! .*$") | ForEach-Object { $_.Value }
  $missing  = [regex]::Matches($log, "Missing character: There is no")
  $overfull = [regex]::Matches($log, "Overfull \\hbox")
  $undef    = [regex]::Matches($log, "Undefined control sequence")
  Write-Host "--- file:line errors: $($errLines.Count) ---"
  $errLines | Select-Object -First 40 | ForEach-Object { Write-Host $_ }
  Write-Host "--- bang errors: $($fatal.Count); Undefined: $($undef.Count); missing-char: $($missing.Count); Overfull: $($overfull.Count) ---"
  $fatal | Select-Object -First 20 | ForEach-Object { Write-Host $_ }
}
if (Test-Path "$root\main.pdf") {
  $sz = (Get-Item "$root\main.pdf").Length
  Copy-Item "$root\main.pdf" "$here\main.pdf" -Force
  New-Item -ItemType Directory -Force -Path "$proj\deliverable" | Out-Null
  Copy-Item "$root\main.pdf" "$proj\deliverable\_build_main.pdf" -Force
  Write-Host "main.pdf = $sz bytes (copied to src\main.pdf)"
} else { Write-Host "main.pdf MISSING" }
