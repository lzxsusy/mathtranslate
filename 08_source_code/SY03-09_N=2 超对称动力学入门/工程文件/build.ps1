# Build script: XeLaTeX + makeindex + XeLaTeX x2, then copy PDF back.
# Why mirror: on this machine xelatex cannot write .log under non-ASCII paths,
# and child processes cannot write to Desktop; so we mirror to an ASCII work dir.
$ErrorActionPreference = "Continue"
$bin  = "<本地路径>"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$root = "<本地路径>"
New-Item -ItemType Directory -Force $root | Out-Null
New-Item -ItemType Directory -Force "$root\tmp" | Out-Null

Copy-Item "$here\main.tex" "$root\main.tex" -Force
Copy-Item "$here\preamble.tex" "$root\preamble.tex" -Force
Copy-Item "$here\macros.tex" "$root\macros.tex" -Force
Copy-Item "$here\references.tex" "$root\references.tex" -Force
Copy-Item "$here\young-kugo.sty" "$root\young-kugo.sty" -Force
Copy-Item "$here\index.ist" "$root\index.ist" -Force
Copy-Item "$here\texglyphlist.txt" "$root\texglyphlist.txt" -Force
Copy-Item "$here\index-terms.json" "$root\index-terms.json" -Force -ErrorAction SilentlyContinue
foreach ($d in @("sections","figures")) {
  New-Item -ItemType Directory -Force "$root\$d" | Out-Null
  if (Test-Path "$here\$d") { Copy-Item "$here\$d\*" "$root\$d\" -Force -Recurse -ErrorAction SilentlyContinue }
}

$env:PATH = "$bin;$env:PATH"
$env:TMP = "$root\tmp"
$env:TEMP = $env:TMP
Set-Location $root
$xe = Join-Path $bin "xelatex.exe"
$mi = Join-Path $bin "makeindex.exe"

& $xe -interaction=nonstopmode -file-line-error main.tex *> $null
Write-Host "==> pass1 exit=$LASTEXITCODE"
if (Test-Path "$root\main.idx") {
  & $mi -s index.ist main.idx *> $null
  Write-Host "==> makeindex exit=$LASTEXITCODE"
}
& $xe -interaction=nonstopmode -file-line-error main.tex *> $null
Write-Host "==> pass2 exit=$LASTEXITCODE"
& $xe -interaction=nonstopmode -file-line-error main.tex *> $null
Write-Host "==> pass3 exit=$LASTEXITCODE"

if (Test-Path "$root\main.log") {
  New-Item -ItemType Directory -Force "$here\work\tmp" | Out-Null
  Copy-Item "$root\main.log" "$here\work\tmp\main.log" -Force
  $t = Get-Content "$root\main.log" -Encoding UTF8 -Raw
  $err   = [regex]::Matches($t, "(?m)^[^\r\n]*?:\d+: .*$")
  $fatal = [regex]::Matches($t, "(?m)^! .*$")
  $undef = [regex]::Matches($t, "(?m)^! Undefined control sequence.*$")
  $miss  = [regex]::Matches($t, "Missing character: There is no")
  $over  = [regex]::Matches($t, "Overfull \\hbox")
  Write-Host "--- file:line=$($err.Count) fatal=$($fatal.Count) undefined=$($undef.Count) missingchar=$($miss.Count) overfull=$($over.Count) ---"
  $err | Select-Object -First 25 | ForEach-Object { Write-Host $_.Value }
  $fatal | Select-Object -First 10 | ForEach-Object { Write-Host $_.Value }
  $miss | Select-Object -First 10 | ForEach-Object { Write-Host $_.Value }
}
if (Test-Path "$root\main.pdf") {
  $sz = (Get-Item "$root\main.pdf").Length
  Copy-Item "$root\main.pdf" "$here\main.pdf" -Force
  if (Test-Path "$root\main.idx") { Copy-Item "$root\main.idx" "$here\main.idx" -Force }
  if (Test-Path "$root\main.ind") { Copy-Item "$root\main.ind" "$here\main.ind" -Force }
  Write-Host "main.pdf = $sz bytes (copied back)"
} else { Write-Host "main.pdf MISSING" }
