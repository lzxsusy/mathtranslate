# xelatex 两遍 + 日志检查。用法：.\build.ps1   （若本机装有 TeX Live / MiKTeX）
$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot

if (-not (Get-Command xelatex -ErrorAction SilentlyContinue)) {
    Write-Host "未找到 xelatex。请先安装 TeX Live 或 MiKTeX，并确保 xelatex 在 PATH 中。" -ForegroundColor Red
    exit 1
}

for ($i = 1; $i -le 2; $i++) {
    Write-Host "=== xelatex 第 $i 遍 ===" -ForegroundColor Cyan
    xelatex -interaction=nonstopmode -halt-on-error main.tex | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "编译失败，见 main.log" -ForegroundColor Red
        Select-String -Path main.log -Pattern "^!|Error" | Select-Object -First 20
        exit 1
    }
}

Write-Host "=== 日志检查 ===" -ForegroundColor Cyan
$log = Get-Content main.log -Raw
$bad = @(
    @{k = "Undefined control sequence"; n = ([regex]::Matches($log, "Undefined control sequence")).Count},
    @{k = "LaTeX Warning: Reference"; n = ([regex]::Matches($log, "LaTeX Warning: Reference")).Count},
    @{k = "Overfull \hbox"; n = ([regex]::Matches($log, "Overfull \\hbox")).Count},
    @{k = "Missing character"; n = ([regex]::Matches($log, "Missing character")).Count}
)
foreach ($b in $bad) { "{0,-34} {1}" -f $b.k, $b.n }
if (Test-Path main.pdf) { "`nOK -> main.pdf ({0:N0} bytes)" -f (Get-Item main.pdf).Length }
