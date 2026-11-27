# SY02-44 几何朗兰兹笔记：扩展 Whittaker 范畴（中文译注）

D. Gaitsgory, *Notes on Geometric Langlands: The Extended Whittaker Category*（2010 年 12 月 2 日，17 页，pdfTeX 预印本）的中文译注本。译文 24 页（含译者说明、目录、译注与文献），译注 23 条。

## 文件

| 路径 | 内容 |
|---|---|
| `工程文件/deliverable/SY02-44_Gaitsgory_扩展Whittaker范畴_中文译注.pdf` | 成品 PDF（24 页） |
| `成品/` | 同上（本地副本；仓库级 `.gitignore` 忽略 `成品/*.pdf`，随仓的是 `deliverable/`） |
| `工程文件/BRIEF.md` | 工程简述、范围、验收标准 |
| `工程文件/STYLE_GUIDE.md` | 语言与排版细则 |
| `工程文件/README.md` | 本文件 |
| `工程文件/00_开工必读.md` | 开工清单（通读→疑点→术语→开译） |
| `工程文件/通读笔记.md`、`疑点清单.tsv`、`术语表.tsv`、`符号表.tsv` | 见 `work/` 下的同名底稿 |
| `工程文件/译注汇总.md` | 23 条译注的总表 |
| `工程文件/公式核对记录.md` | 逐条公式与页图核对表 |
| `工程文件/工程总结.md` | 流程、工具链、质量数据、取舍与遗留 |
| `源码/main.tex` | 主控文件（版式、宏、字体） |
| `源码/chapters/` | 按原书节切分的译文章节（可独立编译） |
| `工程文件/work/pages/p01.png`–`p17.png` | 150 dpi 原书页图（公式核对依据） |
| `工程文件/work/en_raw.txt` | 英文文本提取件（仅作行文索引，符号不可信） |

## 编译

```
cd 源码
xelatex main.tex
xelatex main.tex
xelatex main.tex
```

需 xelatex、ctex、Noto Serif SC / Noto Sans SC、tikz/tikz-cd。成品 24 页，0 error、0 Overfull、0 Underfull、0 缺字、0 未定义引用。

## 说明

- 版式沿用本译丛既有的 ctexbook 模板：A4、11 pt、左边距 2.8 cm、右边距 2.6 cm。
- 原书的节号、「编号段」编号与定理类编号共用一套数字，译文照旧；原书编号的公式只有 (4.1)、(4.2)、(7.1)、(8.1) 四条，译文只给这四条编号。
- 原文笔误按「保留原文、另加译注」处理，共 14 处，明细见 `work/疑点清单.tsv`。
- 底本为作者自印的预印本，权利归原作者（L2 公开·受限，权利人通知即撤下）；成品随仓公开。
