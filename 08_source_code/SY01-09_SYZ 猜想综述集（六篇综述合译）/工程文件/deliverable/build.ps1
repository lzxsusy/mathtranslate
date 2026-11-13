# build.ps1 - SYZ survey collection mirror build
# lualatex cannot write .log on non-ASCII paths, and subprocesses cannot write Desktop.
# So mirror src/ + figures/ into an ASCII writable dir, compile there, copy PDF back.
# Usage: powershell -ExecutionPolicy Bypass -File work\src\build.ps1

$ErrorActionPreference = "Stop"

$Distro = "<本地路径>"
$Mirror = "<本地路径>"
$Passes = 3

$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$work = Split-Path -Parent $here
$root = Split-Path -Parent (Split-Path -Parent $here)
$figs = Join-Path $work "figures"
$deliv = Join-Path $root "deliverable"

$texe = Join-Path $Distro "lualatex.exe"
if (-not (Test-Path $texe)) { Write-Host "FATAL: lualatex not found: $texe"; exit 2 }

New-Item -ItemType Directory -Force $Mirror, "$Mirror\chunks", "$Mirror\figures", "$Mirror\tmp" | Out-Null
Get-ChildItem "$Mirror\chunks\*.tex" -ErrorAction SilentlyContinue | Remove-Item -Force
Copy-Item "$here\main.tex" $Mirror -Force
Copy-Item "$here\preamble.tex" $Mirror -Force
Copy-Item "$here\chunks\*.tex" "$Mirror\chunks\" -Force -ErrorAction SilentlyContinue
if (Test-Path $figs) { Copy-Item "$figs\*" "$Mirror\figures\" -Force -ErrorAction SilentlyContinue }

$env:PATH = "$Distro;" + $env:PATH
$env:TMP = "$Mirror\tmp"
$env:TEMP = "$Mirror\tmp"
$env:TMPDIR = "$Mirror\tmp"
Set-Location $Mirror

$t0 = Get-Date
for ($i = 1; $i -le $Passes; $i++) {
    & $texe -interaction=nonstopmode -file-line-error -synctex=0 main.tex | Out-Null
    $secs = [int]((Get-Date) - $t0).TotalSeconds
    Write-Host "pass $i exit=$LASTEXITCODE ($secs s)"
}

$logPath = Join-Path $Mirror "main.log"
if (-not (Test-Path $logPath)) { Write-Host "FATAL: main.log missing"; exit 3 }
Copy-Item $logPath (Join-Path $work "tmp\main.log") -Force

$log = Get-Content $logPath -Encoding UTF8 -Raw
$err = [regex]::Matches($log, "(?m)^[^\r\n]*?:\d+: ")
$fatal = [regex]::Matches($log, "(?m)^! ")
$undef = [regex]::Matches($log, "Undefined control sequence")
$miss = [regex]::Matches($log, "Missing character: There is no")
$over = [regex]::Matches($log, "Overfull \\hbox")
$warn = [regex]::Matches($log, "LaTeX Warning")
Write-Host "file:line=$($err.Count) fatal=$($fatal.Count) undefined=$($undef.Count) missingchar=$($miss.Count) overfull=$($over.Count) warnings=$($warn.Count)"
if ($fatal.Count -gt 0) {
    Write-Host "---- first fatal lines ----"
    ($fatal | Select-Object -First 12) | ForEach-Object { Write-Host $_.Value }
}

$pdf = Join-Path $Mirror "main.pdf"
if (Test-Path $pdf) {
    Copy-Item $pdf (Join-Path $here "main.pdf") -Force
    New-Item -ItemType Directory -Force $deliv | Out-Null
    Copy-Item $pdf (Join-Path $deliv "SYZ-syz-surveys_zh.pdf") -Force
    $size = (Get-Item $pdf).Length
    $total = [int]((Get-Date) - $t0).TotalSeconds
    Write-Host "main.pdf ok: $size bytes, total $total s"
    if ($err.Count + $fatal.Count -gt 0) { exit 1 }
    exit 0
} else {
    Write-Host "main.pdf MISSING"
    exit 4
}
