# build.ps1 —— 编译 JP11 中译工程（xelatex 两遍），并把成品复制到 deliverable/
# 用法：powershell -NoProfile -ExecutionPolicy Bypass -File .\build.ps1
$root = $PSScriptRoot
$src  = Join-Path $root 'src'
$out  = Join-Path $root 'deliverable'
New-Item -ItemType Directory -Force -Path $out | Out-Null
$env:MIKTEX_AUTOINSTALL = 't'

Push-Location $src
try {
    foreach ($pass in 1..2) {
        Write-Host "=== xelatex pass $pass ==="
        cmd /c "xelatex -interaction=nonstopmode -halt-on-error main.tex > build_last.txt 2>&1"
        if ($LASTEXITCODE -ne 0) {
            Write-Host "COMPILE FAILED, log tail:"
            Get-Content main.log -Tail 60
            throw "xelatex exit code $LASTEXITCODE"
        }
    }
    Copy-Item main.pdf (Join-Path $out '植田一石_镜像对称与K3曲面_中文译注本.pdf') -Force
    Write-Host "`nOK ->" (Join-Path $out '植田一石_镜像对称与K3曲面_中文译注本.pdf')
} finally {
    Pop-Location
}

$log = Get-Content (Join-Path $src 'main.log') -Raw
$pages = [regex]::Match($log, 'Output written on main\.pdf \((\d+) pages').Groups[1].Value
$over  = ([regex]::Matches($log, 'Overfull \\hbox')).Count
$undef = ([regex]::Matches($log, 'Undefined control sequence')).Count
$miss  = ([regex]::Matches($log, 'Missing character')).Count
Write-Host "pages: $pages   Overfull hbox: $over   Undefined: $undef   Missing char: $miss"
