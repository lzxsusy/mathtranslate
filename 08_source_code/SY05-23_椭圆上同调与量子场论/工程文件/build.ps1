# build.ps1 — 编译 SY05-23 中文译注本（Lead 独占，施工成员不要跑）
# 用法： powershell -ExecutionPolicy Bypass -File .\build.ps1
$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$src  = Join-Path $here '..\源码'
$out  = Join-Path $here '..\成品'
$pdf  = Join-Path $src 'main.pdf'
$log  = Join-Path $src 'main.log'

$xelatex = (Get-Command xelatex.exe -ErrorAction SilentlyContinue).Source
if (-not $xelatex) {
  $cand = '<本地路径>'
  if (Test-Path $cand) { $xelatex = $cand } else { throw 'xelatex not found' }
}
Write-Host "xelatex = $xelatex"
if (-not (Test-Path $out)) { New-Item -ItemType Directory -Path $out | Out-Null }
if (Test-Path $pdf) { Remove-Item $pdf -Force }

Push-Location $src
try {
  for ($pass = 1; $pass -le 2; $pass++) {
    Write-Host "--- pass $pass ---"
    & $xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex | Out-Null
    if ($LASTEXITCODE -ne 0) {
      Write-Host "!! xelatex failed on pass $pass (exit $LASTEXITCODE) — see 源码\main.log"
      Select-String -Path $log -Pattern '^.*:\d+: ', '^! ' | Select-Object -First 20 | ForEach-Object { Write-Host $_.Line }
      exit 1
    }
  }
} finally { Pop-Location }

if (-not (Test-Path $pdf)) { throw 'no main.pdf produced' }
Copy-Item $pdf (Join-Path $out 'SY05-23_椭圆上同调与量子场论_中文译注本.pdf') -Force
$size = (Get-Item $pdf).Length
$pages = (Select-String -Path $log -Pattern 'Output written on main\.pdf \((\d+) pages').Matches.Groups[1].Value
Write-Host ("OK  {0}  ({1:N0} bytes, {2} pages)" -f $pdf, $size, $pages)
# 残检：未定义引用 / 缺字
$bad = Select-String -Path $log -Pattern 'Missing character|Undefined control sequence|LaTeX Warning: Reference'
if ($bad) { Write-Host "!! warnings:"; $bad | Select-Object -First 10 | ForEach-Object { Write-Host ('   ' + $_.Line) } }
