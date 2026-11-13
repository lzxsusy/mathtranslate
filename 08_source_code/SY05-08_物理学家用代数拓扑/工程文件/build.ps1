# =====================================================================
#  build.ps1 —— 一键编译（MiKTeX + xelatex，可直接在中文路径下编译）
#  用法：
#     powershell -ExecutionPolicy Bypass -File build.ps1                # 整书
#     powershell -ExecutionPolicy Bypass -File build.ps1 -Chunk ch02    # 只编译某一块（草稿自检）
#  注：本机 MiKTeX xelatex 已实测可在中文路径、Desktop 下编译。
# =====================================================================
param(
  [string]$Chunk = ""
)
$ErrorActionPreference = "Continue"
$here = $PSScriptRoot
$src  = Join-Path $here "src"

# --- 1. 找 TeX bin ---
$binCands = @(
  "<本地路径>",
  "C:\texlive\2026\bin\windows"
)
$bin = $null
foreach ($c in $binCands) { if (Test-Path (Join-Path $c "xelatex.exe")) { $bin = $c; break } }
if (-not $bin) { Write-Host "FATAL: xelatex.exe not found"; exit 1 }
$xelatex = Join-Path $bin "xelatex.exe"

$env:PATH = "$bin;$env:PATH"
Set-Location $src

# --- 2. 草稿模式：只编译指定 chunk ---
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
  Set-Content -Path (Join-Path $src "draft_$Chunk.tex") -Value $draft -Encoding UTF8
  $mainFile = "draft_$Chunk.tex"
}

# --- 3. 编译 ---
$passes = if ($Chunk -ne "") { 2 } else { 3 }
foreach ($i in 1..$passes) {
  & $xelatex -interaction=nonstopmode -file-line-error $mainFile | Out-Null
  Write-Host ("==> pass {0} exit={1}" -f $i, $LASTEXITCODE)
}

# --- 4. 解析日志 ---
$job = [System.IO.Path]::GetFileNameWithoutExtension($mainFile)
$logPath = Join-Path $src "$job.log"
if (-not (Test-Path $logPath)) { Write-Host "FATAL: no log"; exit 1 }
$log = Get-Content $logPath -Encoding UTF8 -Raw
$fileline = [regex]::Matches($log, "(?m)^[^\r\n]*?:\d+: .*$").Count
$fatal    = [regex]::Matches($log, "(?m)^! .*$").Count
$miss     = [regex]::Matches($log, "Missing character: There is no").Count
$over     = [regex]::Matches($log, "Overfull \\hbox").Count
$undefref = [regex]::Matches($log, "undefined references|Reference .* undefined").Count
Write-Host ("LOG  file:line={0}  fatal={1}  missingchar={2}  overfull={3}  undefref={4}" -f $fileline,$fatal,$miss,$over,$undefref)

if (-not (Test-Path (Join-Path $src "$job.pdf"))) { Write-Host "PDF MISSING"; exit 1 }
if ($Chunk -ne "") {
  Copy-Item (Join-Path $src "$job.pdf") (Join-Path $here "work\tmp_$Chunk.pdf") -Force
  Write-Host ("DRAFT PDF -> work\tmp_{0}.pdf" -f $Chunk)
} else {
  $pdfSrc = Join-Path $src "$job.pdf"
  $pdfDst = Join-Path $src "main.pdf"
  if (-not [string]::Equals($pdfSrc, $pdfDst, [StringComparison]::OrdinalIgnoreCase)) {
    Copy-Item $pdfSrc $pdfDst -Force
  }
  if ($logPath -ne (Join-Path $src "main.log")) {
    Copy-Item $logPath (Join-Path $src "main.log") -Force
  }
  $size = (Get-Item (Join-Path $src "main.pdf")).Length
  Write-Host ("PDF ok  size={0} bytes" -f $size)
  if ($fileline -eq 0 -and $fatal -eq 0 -and $miss -eq 0) { Write-Host "BUILD OK" } else { Write-Host "BUILD HAS ERRORS" }
}
