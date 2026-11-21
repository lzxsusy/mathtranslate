# work 目录说明

本目录只放**可入库**的施工文件。体积大、可再生的东西移到仓库外的
`C:\Users\admin\Downloads\BenZvi_LD_work\assets\`（`pages/`、`pdf/`）。

## 可再生资产（不入库）

| 目录 | 内容 | 重建命令（在 `工程文件/scripts/` 下） |
|---|---|---|
| `assets/pages/` | 原 PDF 逐页位图 `p001–p073.png`（170 dpi，1445×1870） | `python render_pages.py 170` |
| `assets/pdf/src.pdf` | 原 PDF 工作副本（裁图脚本的输入） | 从 `…\msg\file\2026-11\20-BenZvi_LAWRG2024_lectures.pdf` 复制 |

裁图脚本 `crop_ink.py PAGE X0 X1 Y0 Y1 NAME [DPI] [PAD]` 读 `../assets/pdf/src.pdf`，
输出到 `源码/figures/NAME.png`；`page_band_png.py` 读同一份 PDF，输出到 `work/bands/`
（`bands/` 也可随时删）。

## 入库文件

- `通读笔记.md`、`疑点清单.tsv`：开译闸门产物（通读笔记 mtime 早于所有 `源码/chunks/*.tex`）。
- `glossary.tsv`：术语冻结表。
- `figures.tsv`：插图清单（图名 / 原页码 / 裁图窗格 / 说明）。
- `chunk_map.tsv` 与 `原文/chNN.txt`：分块与原文文本层（仅供检索；**公式一律回页面图核对**）。
- `handoff/chNN.md`：块间交接记录（冻结写法、坑、下一块要点）。
