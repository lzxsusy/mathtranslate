$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot          # qsg/
$ws = Split-Path -Parent $root                     # workspace
$texbin = Join-Path $ws '.texlive\2026\bin\windows'
if (-not (Test-Path (Join-Path $texbin 'xelatex.exe'))) {
    Write-Error "找不到 xelatex: $texbin"
}
$env:PATH = "$texbin;" + $env:PATH
$py = '<本地路径>'

Push-Location $root
try {
    & $py tools\make_main.py
    & xelatex -interaction=nonstopmode main.tex | Out-Null
    & xelatex -interaction=nonstopmode main.tex | Out-Null
    $pdf = Join-Path $root 'main.pdf'
    if (Test-Path $pdf) {
        $log = Get-Content (Join-Path $root 'main.log') -Encoding UTF8
        $errs = $log | Where-Object { $_ -match '^!' }
        if ($errs) {
            Write-Output "---- ERRORS ----"
            $errs | Select-Object -First 20
            exit 1
        }
        $pages = ($log | Select-String -Pattern 'Output written on .* \((\d+) pages' | Select-Object -Last 1).Matches.Groups[1].Value
        $size = [math]::Round((Get-Item $pdf).Length / 1MB, 2)
        Write-Output "BUILD OK: main.pdf  ${pages} pages, ${size} MiB"
    } else {
        Write-Output "BUILD FAILED: no main.pdf"
        exit 1
    }
} finally {
    Pop-Location
}
