# =====================================================================
#  build.ps1 —— 一键编译（镜像编译：本机 TeX 不能写中文路径/Desktop）
#  用法：  powershell -ExecutionPolicy Bypass -File build.ps1
#          powershell -ExecutionPolicy Bypass -File build.ps1 -Chunk ch02    # 只编译某一块（草稿自检）
#  说明：每个 chunk 草稿用独立镜像目录 fukaya 以外的新目录 uedabuild_<chunk>，
#        可让多名译者并行自检而互不干扰。
# =====================================================================
param(
  [string]$Chunk = ""
)
$ErrorActionPreference = "Continue"
$here = $PSScriptRoot
$src  = Join-Path $here "src"
$base = "<本地路径>"
$tag  = if ($Chunk -ne "") { "uedabuild_" + $Chunk } else { "uedabuild" }
$root = Join-Path $base $tag

# --- 1. 找 TeX bin（优先 TeX Live 2026 的 xelatex）---
$binCands = @(
  "<本地路径>",
  "C:\texlive\2026\bin\windows",
  "<本地路径>"
)
$bin = $null
foreach ($c in $binCands) { if (Test-Path (Join-Path $c "xelatex.exe")) { $bin = $c; break } }
if (-not $bin) { Write-Host "FATAL: xelatex.exe not found"; exit 1 }

# --- 2. 准备镜像目录 ---
New-Item -ItemType Directory -Force $root, "$root\chunks", "$root\figures", "$root\frontmatter", "$root\tmp" | Out-Null
Copy-Item "$src\main.tex","$src\preamble.tex" $root -Force
if (Test-Path "$src\chunks")   { Copy-Item "$src\chunks\*"   "$root\chunks\"   -Force -ErrorAction SilentlyContinue }
if (Test-Path "$src\figures")  { Copy-Item "$src\figures\*"  "$root\figures\"  -Force -ErrorAction SilentlyContinue }
if (Test-Path "$src\frontmatter") { Copy-Item "$src\frontmatter\*" "$root\frontmatter\" -Force -ErrorAction SilentlyContinue }

$env:PATH = "$bin;$env:PATH"
$env:TMP  = "$root\tmp"
$env:TEMP = "$root\tmp"
Set-Location $root

# --- 3. 草稿模式：只编译指定 chunk ---
$mainFile = "main.tex"
if ($Chunk -ne "") {
  $draft = @"
\documentclass[11pt,openany,UTF8]{ctexbook}
\input{preamble}
\def\UEDAdraft{}% 草稿模式标记：跨块环境（如 ch06a→ch06b 的 proof）在草稿模式自行闭合
\begin{document}
\mainmatter
\InputIfFileExists{chunks/$Chunk}{}{}
\end{document}
"@
  Set-Content -Path "$root\draft.tex" -Value $draft -Encoding UTF8
  $mainFile = "draft.tex"
}

# --- 4. 编译 ×3（含 makeindex）---
$passes = if ($Chunk -ne "") { 2 } else { 3 }
foreach ($i in 1..$passes) {
  & (Join-Path $bin "xelatex.exe") -interaction=nonstopmode -file-line-error $mainFile | Out-Null
  Write-Host ("==> pass {0} exit={1}" -f $i, $LASTEXITCODE)
  if ($i -eq 1 -and (Test-Path (Join-Path $bin "makeindex.exe")) -and (Test-Path "$root\main.idx")) {
    & (Join-Path $bin "makeindex.exe") -q main.idx | Out-Null
  }
}

# --- 5. 解析日志 ---
$job = [System.IO.Path]::GetFileNameWithoutExtension($mainFile)
$logPath = Join-Path $root "$job.log"
if (-not (Test-Path $logPath)) { Write-Host "FATAL: no log"; exit 1 }
$log = Get-Content $logPath -Encoding UTF8 -Raw
$err   = [regex]::Matches($log, "(?m)^[^\r\n]*?:\d+: .*$").Count
$fatal = [regex]::Matches($log, "(?m)^! .*$").Count
$undef = [regex]::Matches($log, "(?m)^.*Undefined control sequence.*$").Count
$miss  = [regex]::Matches($log, "Missing character: There is no").Count
$over  = [regex]::Matches($log, "Overfull \\hbox").Count
$undefref = [regex]::Matches($log, "undefined references|Reference .* undefined").Count
Write-Host ("LOG  file:line={0}  fatal={1}  undefined={2}  missingchar={3}  overfull={4}  undefref={5}" -f $err,$fatal,$undef,$miss,$over,$undefref)
if ($err -gt 0) { Write-Host "--- first errors ---"; (Get-Content $logPath -Encoding UTF8 | Select-String -Pattern ":\d+: " | Select-Object -First 12) | ForEach-Object { Write-Host $_.Line } }

if (-not (Test-Path (Join-Path $root "$job.pdf"))) { Write-Host "PDF MISSING"; exit 1 }
if ($Chunk -ne "") {
  Copy-Item (Join-Path $root "$job.pdf") (Join-Path $here "tmp_$Chunk.pdf") -Force
  Write-Host ("DRAFT PDF -> tmp_{0}.pdf" -f $Chunk)
} else {
  Copy-Item (Join-Path $root "$job.pdf") (Join-Path $src "main.pdf") -Force
  Copy-Item $logPath (Join-Path $src "main.log") -Force
  $size = (Get-Item (Join-Path $src "main.pdf")).Length
  Write-Host ("PDF ok  size={0} bytes" -f $size)
  if ($err -eq 0 -and $fatal -eq 0 -and $undef -eq 0 -and $miss -eq 0) { Write-Host "BUILD OK" } else { Write-Host "BUILD HAS ERRORS" }
  if ($Chunk -eq "") { Copy-Item (Join-Path $root "$job.pdf") (Join-Path $here "deliverable\辛几何入门_中文译注本.pdf") -Force -ErrorAction SilentlyContinue }
}
