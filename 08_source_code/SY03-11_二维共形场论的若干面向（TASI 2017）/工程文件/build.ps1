# 编译脚本（需要 TeX Live / MiKTeX）
# 用法：在 PowerShell 中执行  .\build.ps1
$ErrorActionPreference = "Stop"
Write-Host "==> 第 1 遍 xelatex"
xelatex -interaction=nonstopmode -halt-on-error main.tex
if ($LASTEXITCODE -ne 0) { Write-Host "第 1 遍失败，请查看 main.log"; exit 1 }
Write-Host "==> 第 2 遍 xelatex（目录/交叉引用/文献编号）"
xelatex -interaction=nonstopmode -halt-on-error main.tex
if ($LASTEXITCODE -ne 0) { Write-Host "第 2 遍失败，请查看 main.log"; exit 1 }
Write-Host "完成：main.pdf"
