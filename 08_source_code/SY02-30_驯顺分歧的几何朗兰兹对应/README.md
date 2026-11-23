# 《走向驯顺分歧的几何朗兰兹对应》中译注本

> 底本：Taeuk Nam, *Towards the Geometric Langlands Correspondence for Tame Ramification*,
> 哈佛大学博士学位论文，2026 年 4 月，导师 Dennis Gaitsgory，**127 页**
> （第 1 章 p.1；第 2 章 p.16；第 3 章 p.56；文献 p.126）。
> 底本电子版：DASH <https://dash.harvard.edu/handle/1/42744142>
> 发布编号：**SY02-30**（`08_source_code` 的 SY02 系列现有至 SY02-29）。
> 工程根：`C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-30_驯顺分歧的几何朗兰兹对应`

## 这是什么

这是本库**第一篇把「Iwahori 层级结构」真正做成因子化模范畴**的译本。

Nam 的博士论文把两件事缝在一起：一是 [Nam24] 证明 `D-mod(Bun^I_G)` 紧生成，二是
[Nam26] 把无分歧情形下的三个逐点等价（几何 Casselman–Shalika、Bezrukavnikov、
基本局部等价 FLE）升级为**在固定点 x₀ 处的因子化模范畴**的等价（AB、B、IFLE）。
本译本据此保留四层编号（如 `2.3.1.2`、`(3.4.9)`），页边给出印刷页锚 `p.N`，
读者可随时跳回原书。

本册在方法论上的位置：它是本库**第一次在译中系统性调用 dsh-kb 插件**的工程。
术语、旧译、nLab/Stacks 依据都走检索协议（`04_playbook/19_译中检索与冲突上报.md`），
插件数据的缺陷登记在 `_meta/冲突台账.tsv`（CF-2026-11-23-07、-08、-09 三条）。

## 目录

| 路径 | 内容 |
|---|---|
| `源码/` | LaTeX 源：`main.tex`、`preamble.tex`、`sections/s00`–`s99`、`build.bat` |
| `工程文件/BRIEF.md` | 施工手册（页映射、文件边界、质量门） |
| `工程文件/work/通读笔记.md` | 全书主旨、按节论证地图、体裁清单、阅读顺序、进度 |
| `工程文件/work/疑点清单.tsv` | 19 行疑点（16 已解 / 3 待核），八列 |
| `工程文件/work/glossary.tsv` | 69 条术语冻结表（四列，依据 A/B/I） |
| `工程文件/work/full_marked.txt` | 底本逐页抽取文本（上下标已标记），137 页 |
| `工程文件/work/extract.py` | 抽取脚本（`text` 出全文、`pages a b` 出页面 PNG） |
| `成品/` | 全本 PDF |

## 进度

| 部分 | 印刷页 | 状态 |
|---|---|---|
| 前置：摘要 + 译本说明 | p.v, p.iv | 完成 |
| 第 1 章 导引 | p.1–15 | 完成 |
| 第 2 章 紧生成 | p.16–55 | 完成 |
| 第 3 章 Iwahori 基本局部等价 | p.56–125 | 完成 |
| 文献表 | p.126–128 | 完成 |
| 整书编译 | — | 76 页，0 error / 0 Overfull / 0 undefined |

