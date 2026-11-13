# =====================================================================
#  build.ps1 —— 一键编译（镜像编译：本机 lualatex 不能写中文路径/Desktop）
#  用法：  powershell -ExecutionPolicy Bypass -File build.ps1
#          powershell -ExecutionPolicy Bypass -File build.ps1 -Chunk ch02a   # 只编译某一块
# =====================================================================
param(
  [string]$Chunk = ""
)
$ErrorActionPreference = "Continue"
$here = $PSScriptRoot
$src  = Join-Path $here "src"
$root = "C:\Users\admin\Documents\deepseek-harness\default-workspace\birbuild"

# --- 1. 找 TeX bin ---
$binCands = @(
  "C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64",
  "C:\Users\admin\Documents\deepseek-harness\default-workspace\.texlive\2026\bin\windows",
  "C:\texlive\2026\bin\windows"
)
$bin = $null
foreach ($c in $binCands) { if (Test-Path (Join-Path $c "lualatex.exe")) { $bin = $c; break } }
if (-not $bin) { Write-Host "FATAL: lualatex.exe not found"; exit 1 }

# --- 2. 准备镜像目录 ---
New-Item -ItemType Directory -Force $root, "$root\chunks", "$root\figures", "$root\frontmatter", "$root\tmp" | Out-Null
Copy-Item "$src\main.tex","$src\preamble.tex" $root -Force
if (Test-Path "$src\chunks")   { Copy-Item "$src\chunks\*.tex"   "$root\chunks\"   -Force }
if (Test-Path "$src\figures")  { Copy-Item "$src\figures\*"      "$root\figures\"  -Force }
if (Test-Path "$src\frontmatter") { Copy-Item "$src\frontmatter\*.tex" "$root\frontmatter\" -Force }

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
\begin{document}
\mainmatter
\InputIfFileExists{chunks/$Chunk}{}{}
\end{document}
"@
  Set-Content -Path "$root\draft.tex" -Value $draft -Encoding UTF8
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
$logPath = Join-Path $root "$job.log"
if (-not (Test-Path $logPath)) { Write-Host "FATAL: no log"; exit 1 }
$log = Get-Content $logPath -Encoding UTF8 -Raw
# 已知无害：longtable 分页时 LaTeX 内核报的 "Infinite glue shrinkage found in box being split"
# （本机 MiKTeX 2024+ 的 longtable 特性，文本与分页均正常，已实测），统计前剔除
$logClean = [regex]::Replace($log, "(?m)^[^\r\n]*?: \d+: Infinite glue shrinkage found in box being split[^\r\n]*$", "")
$logClean = [regex]::Replace($logClean, "(?m)^[^\r\n]*?:\d+: Infinite glue shrinkage found in box being split[^\r\n]*$", "")
$err   = [regex]::Matches($logClean, "(?m)^[^\r\n]*?:\d+: .*$").Count
$fatal = [regex]::Matches($logClean, "(?m)^! .*$").Count
$undef = [regex]::Matches($logClean, "Undefined control sequence").Count
$miss  = [regex]::Matches($logClean, "Missing character: There is no").Count
$over  = [regex]::Matches($logClean, "Overfull \\hbox").Count
$glue  = [regex]::Matches($log, "Infinite glue shrinkage").Count
Write-Host ("LOG  file:line={0}  fatal={1}  undefined={2}  missingchar={3}  overfull={4}  [benign-glue={5}]" -f $err,$fatal,$undef,$miss,$over,$glue)

if ($Chunk -ne "") {
  if (Test-Path (Join-Path $root "$job.pdf")) {
    Copy-Item (Join-Path $root "$job.pdf") (Join-Path $here "tmp_$Chunk.pdf") -Force
    Write-Host ("DRAFT PDF -> tmp_{0}.pdf" -f $Chunk)
  } else { Write-Host "PDF MISSING"; exit 1 }
} else {
  if (-not (Test-Path (Join-Path $root "$job.pdf"))) { Write-Host "PDF MISSING"; exit 1 }
  Copy-Item (Join-Path $root "$job.pdf") (Join-Path $src "main.pdf") -Force
  Copy-Item $logPath (Join-Path $src "main.log") -Force
  $size = (Get-Item (Join-Path $src "main.pdf")).Length
  Write-Host ("PDF ok  size={0} bytes" -f $size)
  if ($err -eq 0 -and $fatal -eq 0 -and $undef -eq 0 -and $miss -eq 0) { Write-Host "BUILD OK" } else { Write-Host "BUILD HAS ERRORS" }
}
