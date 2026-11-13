# =====================================================================
#  build.ps1 —— 一键编译（Zois, 18 Lectures on K-Theory 中译注本）
#
#  本机两条硬约束（实测，见《学术PDF翻译_标准作业手册 v2》M2）：
#   (1) LuaTeX 在非 ASCII 路径（中文目录）下可能无法写 .log；
#   (2) 子进程不能写 Desktop，但可写 default-workspace。
#  因此把 src/ 与 figures/ 镜像到 ASCII 可写目录再编译，成功后把 main.pdf 拷回 src\。
#
#  用法：powershell -ExecutionPolicy Bypass -File build.ps1
# =====================================================================
$ErrorActionPreference = "Continue"

function Find-TeXBin {
  $cands = @(
    "<本地路径>",
    "<本地路径>",
    "C:\texlive\2026\bin\windows",
    "C:\texlive\2025\bin\windows"
  )
  foreach ($c in $cands) {
    if (Test-Path (Join-Path $c "lualatex.exe")) { return $c }
  }
  throw "lualatex.exe not found in any candidate TeX bin directory"
}

$bin  = Find-TeXBin
$here = Split-Path -Parent $MyInvocation.MyCommand.Path      # ...\work\src
$work = Split-Path -Parent $here                             # ...\work
$root = "<本地路径>"

New-Item -ItemType Directory -Force "$root" | Out-Null
New-Item -ItemType Directory -Force "$root\chunks" | Out-Null
New-Item -ItemType Directory -Force "$root\figures" | Out-Null
New-Item -ItemType Directory -Force "$root\tmp" | Out-Null

Copy-Item "$here\main.tex"     "$root\main.tex"     -Force
Copy-Item "$here\preamble.tex" "$root\preamble.tex" -Force
Copy-Item "$here\chunks\*.tex" "$root\chunks\"      -Force -ErrorAction SilentlyContinue
Copy-Item "$work\figures\*"    "$root\figures\"     -Force -ErrorAction SilentlyContinue

$env:PATH = "$bin;$env:PATH"
$env:TMP  = "$root\tmp"
$env:TEMP = $env:TMP
Set-Location $root

foreach ($i in 1..3) {
  & (Join-Path $bin "lualatex.exe") -interaction=nonstopmode -file-line-error main.tex | Out-Null
  Write-Host "==> pass $i exit=$LASTEXITCODE"
}

if (Test-Path "$root\main.log") {
  New-Item -ItemType Directory -Force "$work\tmp" | Out-Null
  Copy-Item "$root\main.log" "$work\tmp\main.log" -Force
  $log = Get-Content "$root\main.log" -Encoding UTF8 -Raw
  $errLines = [regex]::Matches($log, "(?m)^[^\r\n]*?:\d+: .*$") | ForEach-Object { $_.Value }
  $fatal    = [regex]::Matches($log, "(?m)^! .*$")            | ForEach-Object { $_.Value }
  $missing  = [regex]::Matches($log, "Missing character: There is no")
  $overfull = [regex]::Matches($log, "Overfull \\hbox")
  $undef    = [regex]::Matches($log, "undefined references|Reference .* undefined|Undefined control sequence")
  Write-Host "--- file:line errors: $($errLines.Count); '!' errors: $($fatal.Count); missing-char: $($missing.Count); overfull: $($overfull.Count); undefined: $($undef.Count) ---"
  $errLines | Select-Object -First 20 | ForEach-Object { Write-Host $_ }
  $fatal    | Select-Object -First 10 | ForEach-Object { Write-Host $_ }
  $undef    | Select-Object -First 10 | ForEach-Object { Write-Host $_ }
  ($overfull | Select-Object -First 5) | ForEach-Object { Write-Host $_ }
}

if (Test-Path "$root\main.pdf") {
  $sz = (Get-Item "$root\main.pdf").Length
  Copy-Item "$root\main.pdf" "$here\main.pdf" -Force
  Write-Host "main.pdf = $sz bytes (copied to src\main.pdf)"
} else {
  Write-Host "main.pdf MISSING"
}
