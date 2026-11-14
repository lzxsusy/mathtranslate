# =====================================================================
#  build.ps1 —— 一键编译（LuaLaTeX ×3）
#
#  用法：  powershell -ExecutionPolicy Bypass -File build.ps1
#  两种布局都支持：
#    (A) 项目工程布局：本脚本在 <work>\src\ 下（main.tex / preamble.tex / chunks/ 同目录）
#    (B) 交付包布局  ：本脚本在交付根目录，源码在 .\src\ 下
#
#  本机实测两条硬约束：
#   (1) LuaTeX 在**非 ASCII 路径**（中文目录）下无法写 .log；
#   (2) 子进程（lualatex.exe）**不能写 Desktop**（只会报 "I can't write on file main.log"），
#       但可写 default-workspace。
#  因此把 src/ 与 figures/ 镜像到 ASCII 可写目录再编译，编译成功后把 main.pdf 拷回。
# =====================================================================
$ErrorActionPreference = "Continue"

$bin = "<本地路径>"
if (-not (Test-Path (Join-Path $bin "lualatex.exe"))) {
  $cands = @("<本地路径>",
             "C:\texlive\2026\bin\windows", "C:\texlive\2025\bin\windows")
  foreach ($c in $cands) { if (Test-Path (Join-Path $c "lualatex.exe")) { $bin = $c; break } }
}

$here = Split-Path -Parent $MyInvocation.MyCommand.Path
if (Test-Path (Join-Path $here "main.tex")) {
  $src = $here                                   # 布局 A：脚本在 src\ 下
  $work = Split-Path -Parent $here
} else {
  $src = Join-Path $here "src"                   # 布局 B：脚本在交付根目录
  $work = $here
}
if (-not (Test-Path (Join-Path $src "main.tex"))) {
  Write-Host "ERROR: 找不到 main.tex（已查 $src）。请在 src\ 或交付根目录运行本脚本。"
  exit 1
}

$root = "<本地路径>"
New-Item -ItemType Directory -Force $root | Out-Null
New-Item -ItemType Directory -Force "$root\chunks" | Out-Null
New-Item -ItemType Directory -Force "$root\figures" | Out-Null
New-Item -ItemType Directory -Force "$root\tmp" | Out-Null

Copy-Item "$src\main.tex"     "$root\main.tex"     -Force
Copy-Item "$src\preamble.tex" "$root\preamble.tex" -Force
Copy-Item "$src\chunks\*.tex" "$root\chunks\"      -Force
$fig = "$src\figures"
if (-not (Test-Path $fig)) { $fig = Join-Path $work "figures" }
if (Test-Path $fig) { Copy-Item "$fig\*" "$root\figures\" -Force }

$env:PATH = "$bin;$env:PATH"
$env:TMP = "$root\tmp"
$env:TEMP = $env:TMP
Set-Location $root

foreach ($i in 1..3) {
  & (Join-Path $bin "lualatex.exe") -interaction=nonstopmode -file-line-error main.tex | Out-Null
  Write-Host "==> pass $i exit=$LASTEXITCODE"
}

if (Test-Path "$root\main.log") {
  New-Item -ItemType Directory -Force (Join-Path $work "tmp") | Out-Null
  Copy-Item "$root\main.log" (Join-Path $work "tmp\main.log") -Force
  Copy-Item "$root\main.log" (Join-Path $src "compile.log") -Force
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
  Copy-Item "$root\main.pdf" (Join-Path $src "main.pdf") -Force
  Write-Host "main.pdf = $sz bytes (copied to $src\main.pdf)"
} else { Write-Host "main.pdf MISSING" }
