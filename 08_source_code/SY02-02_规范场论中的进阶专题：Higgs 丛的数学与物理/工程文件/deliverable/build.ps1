# 交付包根目录的一键编译入口（等价于 .\src\build.ps1）
# 用法： powershell -ExecutionPolicy Bypass -File .\build.ps1
# 说明：真正的编译逻辑在 .\src\build.ps1：把 src/ 与 src/figures/ 镜像到 ASCII 可写的
#       编译目录（默认 …\default-workspace\hb1907build）后跑 LuaLaTeX ×3，再把 main.pdf 拷回 src/。
#       之所以要镜像：本机实测 LuaLaTeX 不能在非 ASCII 路径写 .log、子进程不能写 Desktop。
$ErrorActionPreference = "Stop"
$src = Join-Path $PSScriptRoot "src\build.ps1"
if (-not (Test-Path $src)) { Write-Host "找不到 $src"; exit 1 }
& powershell -ExecutionPolicy Bypass -File $src
exit $LASTEXITCODE
