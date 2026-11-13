# probe_env —— 能力探测实测记录（第 0 步，禁止猜测，全部为本机实测）

探测时间：2026-11-04 11:02–11:05（Asia/Shanghai）。命令与输出摘要如下。

## 1. TeX 工具链（不只看 PATH，扫了安装目录）

| 项 | 实测值 |
|---|---|
| `Get-Command xelatex,pdflatex,lualatex` | PATH 内**没有**（但机器上有） |
| 实际 TeX bin | `<本地路径>` |
| 引擎版本 | `This is LuaHBTeX, Version 1.24.0 (TeX Live 2026)`；`lualatex.exe` 存在 |
| 宏包规模 | 3481 包 / 1.52 GB（2026-11-03 补装，见《环境清单》） |
| **冒烟测试** | 骨架文档（ctex 中文 + amsmath + tcolorbox + hyperref + \tag）经 `build.ps1` 编译 3 遍：`file:line=0 fatal=0 undefined=0 missingchar=0 overfull=0`，PDF 132 KB ✅ |

## 2. Python 与 PDF 库

| 项 | 实测值 |
|---|---|
| Python | `<本地路径>`（3.12, win32） |
| PyMuPDF | `PyMuPDF 2.0: Python bindings for the MuPDF 1.28.5` ✅ |
| 其它 | pypdf / pikepdf / pdfplumber / reportlab / Pillow 均可用 |

## 3. 写盘与编译目录（本机三个硬约束，均实测）

| 项 | 实测结果 |
|---|---|
| PowerShell 写 `default-workspace` | OK |
| PowerShell 写 `Desktop` | OK（本会话政策 danger-full-access） |
| **`lualatex` 写非 ASCII 路径** | 按手册历史教训**不使用**：项目根虽在 Desktop，编译一律镜像到 ASCII 目录 |
| 编译镜像目录 | `<本地路径>`（ASCII，可写，✅ 已实测编译成功） |
| `TMP`/`TEMP` | `build.ps1` 内显式设为 `<镜像目录>\tmp` ✅ |

> 结论：**沿用手册 M2 的镜像编译**（把 `src/`、`chunks/`、`figures/` 复制到 ASCII 目录 → lualatex ×3 → 把 PDF 拷回 `src/`）。
> 本机 `build.ps1` 已实测可用，未出现 `I can't write on file main.log`。

## 4. 字体（中文）

| 项 | 实测值 |
|---|---|
| 方案 | LuaLaTeX + `ctex`（`\documentclass[11pt,a4paper]{article}` + `\usepackage[UTF8]{ctex}`） |
| 是否需要 fontconfig / `\setCJKmainfont` | **不需要**；ctex 自动取系统字体 ✅ |
| 首份成品验证 | 标题页「2d/4d 对应关系简述」、摘要、目录、页眉页码均正常渲染（已 read_image 目视） |

## 5. 底本文件

| 项 | 实测值 |
|---|---|
| 下载 | `https://arxiv.org/pdf/1608.02964v5` → `<本地路径>`（902,153 bytes） |
| 页数 / 版面 | **46 页**，612 × 792 pt（US Letter） |
| 元数据 | producer `pdfTeX-1.40.12`；title/author 字段为空（作者与标题从**首页文本**实测：Yuji Tachikawa / A brief review of the 2d/4d correspondences） |

## 6. 工具脚本（本项目 `work/tools/`，均已实跑）

`inspect_pdf.py`（底本尽调）→ `prep.py`（200dpi 页图 + 逐页文字层 + span 级 tag 提取）→
`fix_tags.py`（剔除 2 条行文引用，得 137 条真 tag）→ `crop.py`（高 dpi 裁图）→
`auto_figs.py` + `figs_manual.py`（13 幅图 500 dpi 裁取）→ `gen_refs.py`（77 条文献转录）→
`check.py`（Gate 1）→ `verify_pdf.py`（Gate 3）→ `gen_notes.py`（批注汇总）→ `pack.py`（打包）。

## 7. 未做/不适用

- 底本**没有**表格、附录、习题、要点框 → 相应的宏只保留备用，未使用。
- 底本**没有**位图（`get_images()` 全 46 页 = 0），13 幅图全为矢量 drawings（404 条曲线）→ 按 500 dpi 裁图为 PNG。
- 未做 OCR（本机无 Ghostscript/OCR，也不需要：文字层可用）。
