# 一键重建：先生成（译注宏 / 附录 A、B / 译注清单），再编译两遍
# 用法：powershell -ExecutionPolicy Bypass -File 工程文件\tools\build.ps1
$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)   # SY05-25
$tools = Join-Path $root '工程文件\tools'
$src = Join-Path $root '源码'
$out = Join-Path $root '成品'

$py = '<HOME>\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe'
if (-not (Test-Path $py)) { $py = 'python' }

$xelatex = '<HOME>\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe'
if (-not (Test-Path $xelatex)) { $xelatex = 'xelatex' }

Write-Host '[1/3] 生成译注宏与附录 ...'
& $py (Join-Path $tools 'gen_tables.py')

Write-Host '[2/3] xelatex ×2 ...'
Push-Location $src
try {
    & $xelatex -interaction=nonstopmode main.tex | Out-Null
    & $xelatex -interaction=nonstopmode main.tex | Out-Null
    $log = Get-Content -Raw -Encoding UTF8 (Join-Path $src 'main.log')
    $bad = @()
    if ($log -match 'Overfull \\hbox') { $bad += 'Overfull hbox' }
    if ($log -match 'Missing character') { $bad += 'Missing character' }
    if ($log -match 'undefined') { $bad += 'undefined reference' }
    if ($log -match '(?m)^! ') { $bad += 'TeX error' }
    if ($bad.Count -gt 0) { Write-Warning ("日志仍有问题: " + ($bad -join ', ')) }
    else { Write-Host '      日志干净（仅 Underfull）。' }
} finally { Pop-Location }

Write-Host '[3/3] 复制成品 ...'
if (-not (Test-Path $out)) { New-Item -ItemType Directory -Path $out | Out-Null }
Copy-Item (Join-Path $src 'main.pdf') (Join-Path $out 'witten-0802.0999-zh.pdf') -Force
Write-Host ("完成：" + (Join-Path $out 'witten-0802.0999-zh.pdf'))
