# SY02-39 · Drinfeld chtoucas 与 Langlands 对应（中译注本）

> Laurent Lafforgue, *Cours à l'Institut Tata sur les chtoucas de Drinfeld et la correspondance de Langlands*, IHES/M/02/45, Juin 2002，56 页法文讲义的中文译注本。

## 一句话

这是 Lafforgue 为 2001 年 2 月孟买 Tata 基础科学研究所十二小时课程写的法语笔记，用**六个章节把函数域上 Langlands 对应证明的骨架从头讲到尾**：截断多边形、chtouca 的紧化、边界上同调的可忽略性、本质上同调中的迹公式。它不替代作者的长文 [Lafforgue 2002]，而是进入那篇长文的最短路径。

## 目录

| 路径 | 内容 |
| --- | --- |
| `BRIEF.md` | 任务、交付物、验收标准、已知边界 |
| `工程文件/reports/01_通读笔记.md` | 底本信息、内容页表、三句话主旨、按章论证地图、写卡要点 |
| `工程文件/reports/02_疑点清单.tsv` | 16 行，列：位置 / 原文 / 类型 / 猜测 / 查证 / 结论 / 依据 / 状态 |
| `工程文件/reports/03_术语表.md` | 约 80 条冻结术语（法/英 → 中） |
| `工程文件/reports/04_交付核对.md` | 逐条验收的自检记录 |
| `工程文件/精选片段.md` | 8 条判定链：任务意图 / 关键动作 / 验证证据 / 结论 |
| `源码/` | 14 个 `.tex`，`xelatex main.tex` 两遍即成 PDF |
| `成品/` | `SY02-39_Drinfeld-chtoucas与Langlands对应_中译注本.pdf`（42 页） |

## 译本体例

- **章**：原文用罗马数字 I–VI 分章，译本用 `\thesection` 排成罗马数字，页眉左侧固定"Drinfeld chtoucas 与 Langlands 对应"。
- **无编号**：原文所有定理、命题、引理、定义都不编号，译本照办；因此本译本里没有"定理 3.2"这类引用，指称靠"第 III 章的那条命题"。
- **页锚**：每页起始处印灰色小字 `[p. n]`，$n$ 是**原书印刷页**。原书印刷页 = 底本 PDF 页 − 1（底本第 1 页是封面）。
- **不译词**：`chtouca`（Drinfeld 自造词，另有拼法 `shtuka`，本库 SY02-18 亦保留原文）、`fourre-tout`（Lafforgue 对"把所有截断紧化收作开子叠"的不分离叠的称呼）。
- **译注**：只写三类——易错预警、含糊点拨、背景直觉，一律用脚注，且必带 `[来源：…]` 或 `[译者按（上下文推断，无外部依据）：…]`。

## 编译

```bash
# 需要 XeLaTeX + ctex + amsmath + tikz-cd
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
```

当前状态：42 页，0 error，0 Overfull，0 未定义引用。

## 版权

底本为 IHES 公开预印本（IHES/M/02/45），版权归作者与 IHES。本译本是学术研读用途的中文译注，属演绎作品，非官方译本；如原作者或 IHES 有异议，将立即撤下。
