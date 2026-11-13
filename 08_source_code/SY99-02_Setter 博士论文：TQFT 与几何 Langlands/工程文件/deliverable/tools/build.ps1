# =====================================================================
#  build.ps1 —— 一键编译（Lead 用）
#  用法：pwsh -File tools\build.ps1
#  产出：src\main.pdf、build\main.log → 复制为 compile.log
# =====================================================================
$ErrorActionPreference = "Continue"
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)  # proj\
$src  = Join-Path $root "src"
$build = Join-Path $root "build"
New-Item -ItemType Directory -Force $build | Out-Null
$env:TMP = $build; $env:TEMP = $build

# 1) 生成片段顺序
& "<本地路径>" `
   (Join-Path $root "tools\gen_order.py") | Out-Null

Push-Location $src
$pass = 0
foreach ($i in 1..3) {
  & xelatex -interaction=nonstopmode -file-line-error main.tex *> (Join-Path $build "xelatex_pass$i.out")
  $code = $LASTEXITCODE
  $pass = $i
  Write-Host "==> pass $i exit=$code"
}
Pop-Location

$logPath = Join-Path $src "main.log"
if (Test-Path $logPath) {
  Copy-Item $logPath (Join-Path $root "compile.log") -Force
  $log = Get-Content $logPath -Encoding UTF8 -Raw
  $fileline = [regex]::Matches($log, "(?m)^[^\r\n]*?:\d+: .*$")
  $fatal    = [regex]::Matches($log, "(?m)^! .*$")
  $undef    = [regex]::Matches($log, "Undefined control sequence")
  $missing  = [regex]::Matches($log, "Missing character: There is no")
  $undefref = [regex]::Matches($log, "Reference .* undefined")
  Write-Host "--- file:line errors: $($fileline.Count) ---"
  $fileline | Select-Object -First 25 | ForEach-Object { Write-Host $_.Value }
  Write-Host "--- '!' errors: $($fatal.Count); undefined ctrl: $($undef.Count); missing-char: $($missing.Count); undefined refs: $($undefref.Count) ---"
  $fatal | Select-Object -First 15 | ForEach-Object { Write-Host $_.Value }
  if ($undefref.Count -gt 0) { $undefref | Select-Object -First 5 | ForEach-Object { Write-Host $_.Value } }
  Write-Host ("--- pages: " + ([regex]::Match($log, "Output written on main.pdf \((\d+) pages").Groups[1].Value) + " ---")
}
$pdf = Join-Path $src "main.pdf"
if (Test-Path $pdf) {
  Write-Host ("main.pdf = " + (Get-Item $pdf).Length + " bytes")
} else { Write-Host "main.pdf MISSING" }
