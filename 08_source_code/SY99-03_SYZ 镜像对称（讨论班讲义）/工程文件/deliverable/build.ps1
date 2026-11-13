# 一键编译（wrapper）：调用 src\build.ps1，编译产物拷回 src\main.pdf
powershell -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot 'src\build.ps1')
