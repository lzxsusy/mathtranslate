# =====================================================================
#  build.ps1 —— 一键编译（镜像编译：本机 lualatex 不能写中文路径/Desktop）
#  用法：
#    powershell -ExecutionPolicy Bypass -File build.ps1                       # 全书
#    powershell -ExecutionPolicy Bypass -File build.ps1 -Chunk ch02           # 只编某章（草稿自检）
#    powershell -ExecutionPolicy Bypass -File build.ps1 -Chunk ch02 -Root C:\...\mirror_tr1
#  并行铁律：每个成员必须用自己专属的 -Root，否则互相覆盖！
# =====================================================================
param(
  [string]$Chunk = "",
  [string]$Root  = "<本地路径>"
)
$ErrorActionPreference = "Continue"
$here = $PSScriptRoot
$src  = Join-Path $here "src"

# --- 1. 找 TeX bin ---
$binCands = @(
  "<本地路径>",
  "C:\texlive\2026\bin\windows",
  "<本地路径>"
)
$bin = $null
foreach ($c in $binCands) { if (Test-Path (Join-Path $c "lualatex.exe")) { $bin = $c; break } }
if (-not $bin) { Write-Host "FATAL: lualatex.exe not found"; exit 1 }

# --- 2. 准备镜像目录 ---
New-Item -ItemType Directory -Force $Root, "$Root\chunks", "$Root\figures", "$Root\frontmatter", "$Root\tmp" | Out-Null
Copy-Item "$src\main.tex","$src\preamble.tex" $Root -Force
if (Test-Path "$src\chunks")   { Copy-Item "$src\chunks\*.tex"   "$Root\chunks\"   -Force }
if (Test-Path "$src\figures")  { Copy-Item "$src\figures\*"      "$Root\figures\"  -Force }
if (Test-Path "$src\frontmatter") { Copy-Item "$src\frontmatter\*.tex" "$Root\frontmatter\" -Force }

$env:PATH = "$bin;$env:PATH"
$env:TMP  = "$Root\tmp"
$env:TEMP = "$Root\tmp"
Set-Location $Root

# --- 3. 草稿模式：只编译指定章 ---
$mainFile = "main.tex"
if ($Chunk -ne "") {
  $draft = @"
\documentclass[11pt,openany,UTF8]{ctexbook}
\input{preamble}
\begin{document}
\mainmatter
\InputIfFileExists{chunks/$Chunk}{}{}
\end{document}
"@
  Set-Content -Path "$Root\draft.tex" -Value $draft -Encoding UTF8
  $mainFile = "draft.tex"
}

# --- 4. 编译 ×3 ---
$passes = if ($Chunk -ne "") { 2 } else { 3 }
foreach ($i in 1..$passes) {
  & (Join-Path $bin "lualatex.exe") -interaction=nonstopmode -file-line-error $mainFile | Out-Null
  Write-Host ("==> pass {0} exit={1}" -f $i, $LASTEXITCODE)
}

# --- 5. 解析日志 ---
$job = [System.IO.Path]::GetFileNameWithoutExtension($mainFile)
$logPath = Join-Path $Root "$job.log"
if (-not (Test-Path $logPath)) { Write-Host "FATAL: no log"; exit 1 }
$log = Get-Content $logPath -Encoding UTF8 -Raw
$err   = [regex]::Matches($log, "(?m)^[^\r\n]*?:\d+: .*$").Count
$fatal = [regex]::Matches($log, "(?m)^! .*$").Count
$undef = [regex]::Matches($log, "(?m)^.*Undefined control sequence.*$").Count
$miss  = [regex]::Matches($log, "Missing character: There is no").Count
$over  = [regex]::Matches($log, "Overfull \\hbox").Count
$undefref = [regex]::Matches($log, "undefined references|Reference .* undefined").Count
Write-Host ("LOG  file:line={0}  fatal={1}  undefined={2}  missingchar={3}  overfull={4}  undefref={5}" -f $err,$fatal,$undef,$miss,$over,$undefref)
if ($err -gt 0) {
  Write-Host "---- first errors ----"
  Select-String -Path $logPath -Encoding UTF8 -Pattern "^[^\r\n]*?:\d+: " | Select-Object -First 12 | ForEach-Object { $_.Line }
}
if ($over -gt 0) {
  Select-String -Path $logPath -Encoding UTF8 -Pattern "Overfull \\hbox" | Select-Object -First 8 | ForEach-Object { $_.Line }
}
if ($miss -gt 0) {
  Select-String -Path $logPath -Encoding UTF8 -Pattern "Missing character" | Select-Object -First 8 | ForEach-Object { $_.Line }
}

if (-not (Test-Path (Join-Path $Root "$job.pdf"))) { Write-Host "PDF MISSING"; exit 1 }
if ($Chunk -ne "") {
  Copy-Item (Join-Path $Root "$job.pdf") (Join-Path $here "tmp_$Chunk.pdf") -Force
  Write-Host ("DRAFT PDF -> tmp_{0}.pdf" -f $Chunk)
} else {
  Copy-Item (Join-Path $Root "$job.pdf") (Join-Path $src "main.pdf") -Force
  Copy-Item $logPath (Join-Path $src "main.log") -Force
  $size = (Get-Item (Join-Path $src "main.pdf")).Length
  Write-Host ("PDF ok  size={0} bytes" -f $size)
}
if ($err -eq 0 -and $fatal -eq 0 -and $undef -eq 0 -and $miss -eq 0 -and $undefref -eq 0) { Write-Host "BUILD OK" } else { Write-Host "BUILD HAS ERRORS" }
