# build.ps1 -- mirror-compile for the 2d/4d correspondences Chinese annotated edition
# Hard constraints on this machine:
#   (1) lualatex cannot write .log under a non-ASCII path;
#   (2) subprocesses cannot write to the Desktop.
# => mirror src/ and figures/ into an ASCII writable dir, compile there, copy PDF back.
$ErrorActionPreference = "Stop"
$bin  = "<本地路径>"
$lua  = Join-Path $bin "lualatex.exe"
if (-not (Test-Path $lua)) { throw "lualatex.exe not found at $bin" }

$here = Split-Path -Parent $MyInvocation.MyCommand.Path      # ...\work\src
$work = Split-Path -Parent $here                              # ...\work
$root = "<本地路径>"

New-Item -ItemType Directory -Force $root, "$root\chunks", "$root\figures", "$root\tmp" | Out-Null
Copy-Item "$here\main.tex" $root -Force
Copy-Item "$here\preamble.tex" $root -Force
Copy-Item "$here\chunks\*.tex" "$root\chunks\" -Force
if (Test-Path "$work\figures") { Copy-Item "$work\figures\*" "$root\figures\" -Force }

$env:PATH = "$bin;" + $env:PATH
$env:TMP  = "$root\tmp"
$env:TEMP = "$root\tmp"
Set-Location $root

foreach ($i in 1..3) {
  & $lua -interaction=nonstopmode -file-line-error main.tex | Out-Null
  Write-Host ("==> pass {0} exit={1}" -f $i, $LASTEXITCODE)
}

if (-not (Test-Path "$root\main.log")) { Write-Host "NO LOG -- compilation did not run"; exit 1 }
Copy-Item "$root\main.log" "$work\tmp\main.log" -Force
$log   = Get-Content "$root\main.log" -Encoding UTF8 -Raw
$err   = [regex]::Matches($log, "(?m)^[^\r\n]*?:\d+: .*$")
$fatal = [regex]::Matches($log, "(?m)^! .*$")
$miss  = [regex]::Matches($log, "Missing character: There is no")
$over  = [regex]::Matches($log, "Overfull \\hbox")
$undef = [regex]::Matches($log, "Undefined control sequence")
Write-Host ("file:line={0}  fatal={1}  undefined={2}  missingchar={3}  overfull={4}" -f `
            $err.Count, $fatal.Count, $undef.Count, $miss.Count, $over.Count)
if ($err.Count -gt 0) { Write-Host "---- first 15 file:line errors ----"; $err | Select-Object -First 15 | ForEach-Object { Write-Host $_.Value } }
if ($fatal.Count -gt 0) { Write-Host "---- first 10 fatal ----"; $fatal | Select-Object -First 10 | ForEach-Object { Write-Host $_.Value } }
if ($undef.Count -gt 0) { Write-Host "---- undefined ----"; $undef | Select-Object -First 10 | ForEach-Object { Write-Host $_.Value } }
if ($miss.Count -gt 0) { Write-Host "---- missing char ----"; $miss | Select-Object -First 10 | ForEach-Object { Write-Host $_.Value } }
if ($over.Count -gt 0) { Write-Host "---- overfull ----"; $over | Select-Object -First 25 | ForEach-Object { Write-Host $_.Value } }

if (Test-Path "$root\main.pdf") {
  Copy-Item "$root\main.pdf" "$here\main.pdf" -Force
  $sz = (Get-Item "$here\main.pdf").Length
  Write-Host ("main.pdf OK  {0} bytes -> {1}\main.pdf" -f $sz, $here)
} else {
  Write-Host "main.pdf MISSING"
  exit 2
}
