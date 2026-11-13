# 本机三条硬约束（实测）：
#  (1) LuaTeX 在**非 ASCII 路径**（中文目录）下无法写 .log；
#  (2) 子进程（lualatex.exe）**不能写 Desktop**（只报 "I can't write on file main.log"），
#      但可写 default-workspace；
#  (3) TMP/TEMP 必须显式指向可写目录。
# 因此把 src/ 与 figures/ 镜像到 default-workspace 下的 ASCII 目录再编译，
# 编译成功后把 main.pdf 与 main.log 拷回 src\ 与 tmp\。
$ErrorActionPreference = "Continue"
$bin = "<本地路径>"
if (-not (Test-Path (Join-Path $bin "lualatex.exe"))) {
  $cands = @("<本地路径>",
             "C:\texlive\2026\bin\windows", "C:\texlive\2025\bin\windows")
  foreach ($c in $cands) { if (Test-Path (Join-Path $c "lualatex.exe")) { $bin = $c; break } }
}
$here = Split-Path -Parent $MyInvocation.MyCommand.Path   # ...\work\src
$work = Split-Path -Parent $here                          # ...\work
$root = "<本地路径>"   # ASCII 可写编译目录
New-Item -ItemType Directory -Force $root | Out-Null
New-Item -ItemType Directory -Force "$root\chunks" | Out-Null
New-Item -ItemType Directory -Force "$root\figures" | Out-Null
New-Item -ItemType Directory -Force "$root\tmp" | Out-Null

Copy-Item "$here\main.tex"   "$root\main.tex"   -Force
Copy-Item "$here\preamble.tex" "$root\preamble.tex" -Force
Copy-Item "$here\chunks\*.tex" "$root\chunks\" -Force
if (Test-Path "$work\figures\*.png") { Copy-Item "$work\figures\*.png" "$root\figures\" -Force }

$env:PATH = "$bin;$env:PATH"
$env:TMP = "$root\tmp"
$env:TEMP = $env:TMP
Set-Location $root

foreach ($i in 1..3) {
  & (Join-Path $bin "lualatex.exe") -interaction=nonstopmode -file-line-error main.tex | Out-Null
  Write-Host "==> pass $i exit=$LASTEXITCODE"
}
if (Test-Path "$root\main.log") {
  Copy-Item "$root\main.log" "$work\tmp\main.log" -Force
  $log = Get-Content "$root\main.log" -Encoding UTF8 -Raw
  $errLines = [regex]::Matches($log, "(?m)^[^\r\n]*?:\d+: .*$") | ForEach-Object { $_.Value }
  $fatal = [regex]::Matches($log, "(?m)^! .*$") | ForEach-Object { $_.Value }
  $undef = [regex]::Matches($log, "(?m)^! Undefined control sequence.*$")
  $missing = [regex]::Matches($log, "Missing character: There is no")
  $over = [regex]::Matches($log, "Overfull \\hbox")
  Write-Host "--- file:line errors: $($errLines.Count) ---"
  $errLines | Select-Object -First 30 | ForEach-Object { Write-Host $_ }
  Write-Host "--- '!' errors: $($fatal.Count); undefined: $($undef.Count); missing-char: $($missing.Count); overfull: $($over.Count) ---"
  $fatal | Select-Object -First 10 | ForEach-Object { Write-Host $_ }
}
if (Test-Path "$root\main.pdf") {
  $sz = (Get-Item "$root\main.pdf").Length
  Copy-Item "$root\main.pdf" "$here\main.pdf" -Force
  Write-Host "main.pdf = $sz bytes (copied to src\main.pdf)"
} else { Write-Host "main.pdf MISSING" }
