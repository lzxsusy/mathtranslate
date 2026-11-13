# EN47 整书编译（Lead 用）
# 用法：pwsh -File build.ps1        （在工程根执行）
$ErrorActionPreference = "Continue"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$src  = Join-Path $root "src"
$out  = Join-Path $root "work\main_build"
$deliv= Join-Path $root "deliverable"
New-Item -ItemType Directory -Force $out   | Out-Null
New-Item -ItemType Directory -Force $deliv | Out-Null

Push-Location $src
$env:PYTHONIOENCODING = "utf-8"
for ($i = 1; $i -le 2; $i++) {
    Write-Host "=== xelatex pass $i ==="
    & xelatex -interaction=nonstopmode "-output-directory=$out" main.tex | Out-Null
}
Pop-Location

$log = Join-Path $out "main.log"
if (-not (Test-Path $log)) { Write-Host "NO LOG"; exit 1 }
$txt = Get-Content $log -Raw -Encoding UTF8
function Count($pat) { ([regex]::Matches($txt, $pat, "Multiline")).Count }
$errors  = Count "^!"
$over    = Count "^Overfull"
$under   = Count "^Underfull"
$undef   = Count "undefined"
$missing = Count "Missing character"
$pages = "?"
if ($txt -match "\((\d+) pages\)") { $pages = $Matches[1] }
Write-Host "pages=$pages errors=$errors overfull=$over underfull=$under undefined=$undef missing_char=$missing"
if ($errors -gt 0) {
    $m = [regex]::Match($txt, "(?m)^!.*(\n.*){0,8}")
    Write-Host "--- first error ---"; Write-Host $m.Value
}
$pdf = Join-Path $out "main.pdf"
if (Test-Path $pdf) {
    $dest = Join-Path $deliv "EN47_Landweber_K理论与椭圆算子_中文译注本.pdf"
    [System.IO.File]::Copy($pdf, $dest, $true)
    Write-Host "deliverable -> $dest"
}
