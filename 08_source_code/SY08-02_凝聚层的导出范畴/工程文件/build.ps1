# =====================================================================
#  build.ps1 —— 编译《凝聚层的导出范畴及其之间的等价》中文译注本
#  用法： powershell -ExecutionPolicy Bypass -File 工程文件\build.ps1
#  产物： build\main.pdf（同时覆盖 成品\*_中文译注本.pdf）
# =====================================================================
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot          # 工程根目录
$src  = Join-Path $root '源码'
$out  = Join-Path $root 'build'
New-Item -ItemType Directory -Force -Path $out | Out-Null

Push-Location $src
try {
    foreach ($i in 1..3) {
        Write-Host "== lualatex pass $i =="
        & lualatex -interaction=nonstopmode -halt-on-error "-output-directory=$out" main.tex | Out-Null
        if ($LASTEXITCODE -ne 0) { throw "lualatex 第 $i 遍失败，见 $out\main.log" }
    }
}
finally {
    Pop-Location
}

# ---- 终态断言 ----
$log   = Get-Content (Join-Path $out 'main.log') -Raw -Encoding UTF8
$pages = ([regex]::Match($log, 'Output written on main\.pdf \((\d+) pages')).Groups[1].Value
$bang  = ([regex]::Matches($log, '(?m)^!')).Count
$undef = ([regex]::Matches($log, 'Undefined control sequence')).Count
$miss  = ([regex]::Matches($log, 'Missing character')).Count
$over  = ([regex]::Matches($log, 'Overfull \\hbox')).Count

Write-Host ""
Write-Host "pages=$pages bang=$bang undef=$undef missingchar=$miss overfull=$over"
if ($bang -or $undef -or $miss -or $over) {
    Write-Warning '有未清零的错误或警告，请查看 build\main.log'
}

# ---- 回拷成品 ----
$pdf   = Join-Path $out 'main.pdf'
$final = Join-Path $root '成品\凝聚层的导出范畴_中文译注本.pdf'
New-Item -ItemType Directory -Force -Path (Split-Path $final) | Out-Null
Copy-Item $pdf $final -Force
Write-Host "成品： $final"
