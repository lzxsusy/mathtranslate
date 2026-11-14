# build.ps1 · SY01-23《Dirichlet 膜与镜像对称》
# 用法：在 源码/ 目录下执行  pwsh ./build.ps1
#       （工程文件/build.ps1 是同一份，供下载者直接使用）
# 产物：build/main.pdf

$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

$tex = "main.tex"
if (-not (Test-Path -LiteralPath $tex)) {
    if (Test-Path -LiteralPath "..\源码\$tex") {
        Set-Location -LiteralPath "..\源码"
    } else {
        throw "未找到 $tex；请在 源码/ 目录下运行本脚本。"
    }
}

New-Item -ItemType Directory -Force -Path build | Out-Null

function Run($exe, $args_) {
    Write-Host ">> $exe $args_" -ForegroundColor Cyan
    & $exe @args_
    if ($LASTEXITCODE -ne 0) { throw "$exe 失败（exit $LASTEXITCODE），见 build/main.log" }
}

Run xelatex @("-interaction=nonstopmode", "-halt-on-error", "-output-directory=build", $tex)
Run biber   @("--input-directory=.", "--output-directory=build", "build/main.bcf")
Run xelatex @("-interaction=nonstopmode", "-halt-on-error", "-output-directory=build", $tex)
Run xelatex @("-interaction=nonstopmode", "-halt-on-error", "-output-directory=build", $tex)

$pdf = "build/main.pdf"
if (-not (Test-Path -LiteralPath $pdf)) { throw "未生成 $pdf" }
$size = (Get-Item -LiteralPath $pdf).Length
Write-Host ""
Write-Host "完成：$pdf  $([math]::Round($size/1MB,2)) MB" -ForegroundColor Green
Write-Host "（期望 530 页 / 约 24.4 MB；页数核对：pdftoppm 或 pdfinfo 均可）"
