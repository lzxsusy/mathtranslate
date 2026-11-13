# 读书笔记编译脚本（LuaLaTeX ×2）
$ErrorActionPreference = "Continue"
$bin = "<本地路径>"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$root = "<本地路径>"
New-Item -ItemType Directory -Force $root | Out-Null
New-Item -ItemType Directory -Force "$root\tmp" | Out-Null
Copy-Item "$here\main.tex" "$root\main.tex" -Force
if (Test-Path "$here\notes") {
  New-Item -ItemType Directory -Force "$root\notes" | Out-Null
  Copy-Item "$here\notes\*" "$root\notes\" -Force -Recurse
}
$env:PATH = "$bin;$env:PATH"
$env:TMP = "$root\tmp"; $env:TEMP = $env:TMP
Set-Location $root
$lu = Join-Path $bin "lualatex.exe"
& $lu -interaction=nonstopmode -file-line-error main.tex *> $null
Write-Host "==> pass1 exit=$LASTEXITCODE"
& $lu -interaction=nonstopmode -file-line-error main.tex *> $null
Write-Host "==> pass2 exit=$LASTEXITCODE"
if (Test-Path "$root\main.log") {
  $t = Get-Content "$root\main.log" -Encoding UTF8 -Raw
  $err = [regex]::Matches($t, "(?m)^[^\r\n]*?:\d+: .*$")
  $fatal = [regex]::Matches($t, "(?m)^! .*$")
  Write-Host "--- file:line=$($err.Count) fatal=$($fatal.Count) ---"
  $err | Select-Object -First 15 | ForEach-Object { Write-Host $_.Value }
  $fatal | Select-Object -First 8 | ForEach-Object { Write-Host $_.Value }
}
if (Test-Path "$root\main.pdf") {
  Copy-Item "$root\main.pdf" "$here\notes.pdf" -Force
  Write-Host "notes.pdf = $((Get-Item "$here\notes.pdf").Length) bytes"
} else { Write-Host "main.pdf MISSING" }

