# 环境探测（实测）

## TeX
- lualatex exists: True
- This is LuaHBTeX, Version 1.24.0 (TeX Live 2026)
- build dir writable: True / True
- work dir writable: True
- deliverable writable: True

## Python / PDF libs
- python: 3.12.14 @ <本地路径>
- pymupdf: 2.0
- pypdf: ok
- pikepdf: ok
- pdfplumber: ok

## ctex / fonts 冒烟（3 行文档，由 build.ps1 落实验证）

## 已知本机硬约束（手册 M1/M2）
- lualatex 不能写非 ASCII 路径的 .log；子进程不能写 Desktop
- 编译必须在 default-workspace\syzbuild 镜像目录进行，PDF 拷回
- TMP/TEMP 显式指向 syzbuild\tmp
- 日志用 Out-Null，不重定向到 <jobname>.out
## 冒烟编译
- pass 1: exit=0
- pass 2: exit=0
- pass 3: exit=0
- smoke.pdf: True size=44784
- log errors: file:line=0 fatal=0
- missing char=0
