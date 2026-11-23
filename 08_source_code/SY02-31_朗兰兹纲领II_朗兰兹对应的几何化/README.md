# SY02-31《朗兰兹纲领 II：朗兰兹对应的几何化》中文译注本

> 底本：Pierre-Henri Chaudouard, Wee Teck Gan, Tasho Kaletha, Yiannis Sakellaridis (eds.),
> *The Langlands Program II. Geometrization of the Langlands Correspondence*,
> Proceedings of Symposia in Pure Mathematics 112.2, American Mathematical Society, 2025.
> 583 个 PDF 页（印刷页 iii–xi、1–568）。
> 本库不发布成品 PDF（R3），只发布 LaTeX 源码、工程文件与资料卡。

## 一句话

2022 年 IHES 朗兰兹纲领暑期学校会议录的第二卷：六篇文章从参数叠上的凝聚层、曲线模叠、
$p$-进 Langlands 范畴化、凝聚/可构造比较与导出结构五个角度，讲「朗兰兹对应的几何化」。

## 怎么编译

```bat
cd 工程文件
build.bat
```

或手工：

```bash
cd 源码
xelatex main.tex && xelatex main.tex && xelatex main.tex
```

引擎 XeLaTeX（MiKTeX 4.18），中文用 `ctexbook` + `fontset=windows`（宋体/黑体/楷体）。

## 目录

| 路径 | 内容 |
|---|---|
| `源码/main.tex` | 主文件，按 PDF 页序 \input 47 个分片 |
| `源码/preamble.tex` | 版式、定理环境、页锚、术语宏 |
| `源码/front/` | 前言、译者说明、全书导读 |
| `源码/chunks/` | 分片译文 `ch-aX-YY.tex`（aX=第 X 篇，YY=片号） |
| `工程文件/BRIEF.md` | 项目身份、结构、页范围表、交付勾选 |
| `工程文件/STATUS.md` | 当前状态与待办 |
| `工程文件/work/glossary.tsv` | 术语表（约 190 条，含等级与依据） |
| `工程文件/work/通读笔记.md` | 通读分级记录与逐篇速读 |
| `工程文件/work/疑点清单.tsv` | 疑点、查证动作与结论 |
| `工程文件/reports/` | 六篇分篇报告与编译审计 |
| `资料卡/` | 00 速览、01 概念、02 命题、03 论证链、04 术语文献勘误 |
| `对齐卡/` | 形式化对齐卡 |

## 页锚与编号

译文每页起始处的切口侧灰色小字是**底本印刷页码**；`PDF 页 = 印刷页 + 13`。
定理、命题、公式、节号一律沿用底本编号，不重排，便于与原书对照。

## 权利

底本为在版图书，著作权归原作者与 AMS。本译本是演绎作品，仅供学习研究，不替代原书；
权利人通知即撤下。见 `投稿信息.md`。
