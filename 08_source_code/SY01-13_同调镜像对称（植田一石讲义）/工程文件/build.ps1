# build.ps1 —— 编译 JP01 中译工程（xelatex 两遍），并把成品复制到 deliverable/
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$src  = Join-Path $root 'src'
$out  = Join-Path $root 'deliverable'
New-Item -ItemType Directory -Force -Path $out | Out-Null
$env:MIKTEX_AUTOINSTALL = 't'

# 同步插图：只拷 fig* / eq* 正式图，跳过译者临时裁图
$figSrc = Join-Path $root 'work\figures'
$figDst = Join-Path $src 'figures'
New-Item -ItemType Directory -Force -Path $figDst | Out-Null
if (Test-Path $figSrc) {
    Get-ChildItem $figSrc -File | Where-Object { $_.Name -match '^(fig|eq)' } |
        ForEach-Object { Copy-Item $_.FullName (Join-Path $figDst $_.Name) -Force }
}

Push-Location $src
try {
    foreach ($pass in 1..2) {
        Write-Host "=== xelatex 第 $pass 遍 ==="
        & xelatex -interaction=nonstopmode -halt-on-error main.tex | Out-Null
        if ($LASTEXITCODE -ne 0) {
            Write-Host "编译失败，日志尾部："
            Get-Content main.log -Tail 40
            throw "xelatex 退出码 $LASTEXITCODE"
        }
    }
    Copy-Item main.pdf (Join-Path $out '植田一石_同调镜像对称_中文译注本.pdf') -Force
    Write-Host "`nOK ->" (Join-Path $out '植田一石_同调镜像对称_中文译注本.pdf')
} finally {
    Pop-Location
}

$log = Get-Content (Join-Path $src 'main.log') -Raw
$pages = [regex]::Match($log, 'Output written on main\.pdf \((\d+) pages').Groups[1].Value
$over  = ([regex]::Matches($log, 'Overfull \\hbox')).Count
Write-Host "页数: $pages   Overfull hbox: $over"
