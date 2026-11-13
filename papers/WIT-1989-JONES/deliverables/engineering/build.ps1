# =============================================================================
#  WIT-1989-JONES 一键构建
#  用法（项目根目录）： powershell -NoProfile -ExecutionPolicy Bypass -File deliverables\engineering\build.ps1
#  可选参数： -SkipPdf  -SkipHtml
#  环境变量： WITTEN_TEX（原文译本 witten.tex 的路径，用于公式锚点核对）
# =============================================================================
param(
    [switch]$SkipPdf,
    [switch]$SkipHtml
)

$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$note = Join-Path $root 'deliverables\reading_note'
$eng  = Join-Path $root 'deliverables\engineering'
$wittenDefault = 'C:\Users\admin\Documents\deepseek-harness\default-workspace\witten1989\deliver\witten.tex'
$wittenTex = if ($env:WITTEN_TEX) { $env:WITTEN_TEX } else { $wittenDefault }

function Find-Python {
    if ($env:PYTHON) { return $env:PYTHON }
    $candidates = @(
        'C:\Users\admin\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe',
        'python', 'python3'
    )
    foreach ($c in $candidates) {
        try {
            $p = Get-Command $c -ErrorAction Stop
            return $p.Source
        } catch { }
    }
    throw '找不到 python。请设置 $env:PYTHON。'
}

$py = Find-Python
Write-Host "== python: $py"
Write-Host "== 项目根: $root"

# 1) 校验 claims/questions
Write-Host "`n[1/5] 校验 claims/questions"
& $py (Join-Path $eng 'scripts\check_claims.py') $root
if ($LASTEXITCODE -ne 0) { throw 'check_claims.py 失败' }

# 2) 校验公式锚点（依赖 witten1989 译本源码；不在则跳过）
Write-Host "`n[2/5] 校验公式锚点"
$wittenTexAlt = (Resolve-Path $wittenTex -ErrorAction SilentlyContinue)
if ($wittenTexAlt) {
    & $py (Join-Path $eng 'scripts\check_anchors.py') $root --tex $wittenTexAlt.Path
    if ($LASTEXITCODE -ne 0) { throw 'check_anchors.py 失败' }
} else {
    Write-Warning "未找到 $wittenTex，跳过锚点校验"
}

# 3) 编译读书笔记（两遍）
if (-not $SkipPdf) {
    Write-Host "`n[3/5] 编译读书笔记"
    Push-Location $note
    try {
        xelatex -interaction=nonstopmode main.tex | Out-Null
        xelatex -interaction=nonstopmode main.tex | Out-Null
        if (-not (Test-Path 'main.pdf')) { throw '编译失败：没有 main.pdf' }
        Write-Host "  ok main.pdf ($((Get-Item main.pdf).Length) 字节)"
    } finally {
        Pop-Location
    }
} else {
    Write-Host "`n[3/5] 跳过 PDF"
}

# 4) 生成 manifest.json
Write-Host "`n[4/5] 生成 manifest.json"
$manifestArgs = @((Join-Path $eng 'scripts\make_manifest.py'), $root)
if ($wittenTexAlt) { $manifestArgs += @('--witten-tex', $wittenTexAlt.Path) }
& $py @manifestArgs
if ($LASTEXITCODE -ne 0) { throw 'make_manifest.py 失败' }

# 5) 导出 HTML（pandoc 可选）
if (-not $SkipHtml) {
    Write-Host "`n[5/5] 导出 HTML"
    & $py (Join-Path $eng 'scripts\export_html.py') $root
    if ($LASTEXITCODE -eq 2) { Write-Warning '未装 pandoc，跳过 HTML' }
} else {
    Write-Host "`n[5/5] 跳过 HTML"
}

Write-Host "`n完成。产物："
Write-Host "  笔记 PDF : $(Join-Path $note 'main.pdf')"
Write-Host "  manifest : $(Join-Path $root 'manifest.json')"
Write-Host "  HTML     : $(Join-Path $eng 'site\index.html')"
