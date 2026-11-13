# =====================================================================
#  build.ps1 —— 编译并统计（xelatex 两遍）
# =====================================================================
$ErrorActionPreference = 'Stop'
$xelatex = '<本地路径>'
$root = $PSScriptRoot
$src  = Join-Path $root 'src'
$deliv = Join-Path $root 'deliverable'
if (-not (Test-Path $deliv)) { New-Item -ItemType Directory -Path $deliv | Out-Null }

Push-Location $src
foreach ($run in 1, 2) {
    Write-Host "== xelatex pass $run =="
    & $xelatex -interaction=nonstopmode -halt-on-error main.tex | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "xelatex 失败（pass $run）。日志尾部："
        Get-Content main.log -Tail 40
        Pop-Location
        exit 1
    }
}
Pop-Location

$log = Join-Path $src 'main.log'
$text = Get-Content $log -Raw -Encoding utf8
$pages = ([regex]::Match($text, 'Output written on main\.pdf \((\d+) pages')).Groups[1].Value
$overfull = ([regex]::Matches($text, 'Overfull \\hbox')).Count
$undef = ([regex]::Matches($text, 'Undefined control sequence')).Count
$missing = ([regex]::Matches($text, 'Missing character')).Count
Write-Host "pages=$pages  Overfull=$overfull  Undefined=$undef  MissingChar=$missing"
if ($overfull -gt 0) { Select-String -Path $log -Pattern 'Overfull \\hbox' | Select-Object -First 20 | ForEach-Object { $_.Line } }
if ($missing -gt 0) { Select-String -Path $log -Pattern 'Missing character' | Select-Object -First 20 | ForEach-Object { $_.Line } }

$pdf = Join-Path $src 'main.pdf'
$out = Join-Path $deliv '植田一石_镜像对称与Lagrange环面纤维化_中文译注本.pdf'
Copy-Item $pdf $out -Force
Write-Host "-> $out"
