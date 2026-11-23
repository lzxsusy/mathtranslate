# 《局部 Langlands 对应的几何化》中译注本

> 底本：Laurent Fargues, Peter Scholze, *Geometrization of the local Langlands correspondence*,
> arXiv:2102.13459v4（2024-11-27），**356 页**。
> 工程根：`C:\Users\admin\Downloads\FarguesScholze_局部朗兰兹几何化`
> 发布编号：**SY02-26**（已核：`RELEASE_REGISTER.csv` 现有到 SY02-24，`08_source_code/` 里 SY02-25 已被「顶点代数与代数曲线（第二版）」占用）

## 这是什么

这是「老蓝子钢铃」（朗兰兹纲领）语料库的**算术侧地基**：Fargues–Scholze 把局部 Langlands 对应
搬到 Fargues–Fontaine 曲线上，用 ℓ-进层、diamond、shtuka 模空间重写了整个局部对应。
这篇 356 页是本领域公认的"离谱"文本——不是因为写错，而是因为压缩：

- 它要求三套语言同时在线：p-进几何（diamond / v-层 / 完美胚空间）、几何表示论（Bun_G / Hecke / Satake）、
  以及 Langlands 对偶本身（L-参数 / 谱作用 / Bernstein 中心）；
- 大量证明只给"可以逐字搬到 Fargues–Fontaine 曲线"的一句话，实际搬过去要重写整章；
- 术语还没有稳定中译（diamond、shtuka、prism 这些，学界仍在混用）。

所以本工程的产出不是"一版通顺译文"，而是**可追溯的译注本**：每处术语、每个跳步、每处疑似笔误，
都留一条带来源的译注；读者据此能回到原文与文献，而不是只能信译者。

## 目录

| 路径 | 内容 |
|---|---|
| `00_原文/` | 底本只读副本（不入仓） |
| `01_pages/pNNN.txt` | 逐页文本（索引级，公式不可信） |
| `源码/` | LaTeX 源：main.tex、preamble.tex、sections/、figures/ |
| `工程文件/BRIEF.md` | **施工手册**（路线、页映射、文件所有权、质量门、交付注意事项） |
| `工程文件/SPEC.md` | LaTeX 体例规范（照抄骨架） |
| `工程文件/work/` | 通读笔记、疑点清单、glossary、symbols、trace |
| `工程文件/reports/` | 分章报告（编号对齐、核对页、疑点、遗留） |
| `资料卡/` | 概念卡/推导卡（JSON，供语料与检索） |
| `deliverable/` | 成品 PDF |

## 进度

| 阶段 | 内容 | 状态 |
|---|---|---|
| Phase 0 | 通读笔记 + 疑点清单 + 术语表/符号表 | 进行中（2026-11-23） |
| Phase 1 | Chapter I 样板章（p.7–44） | 待 Phase 0 |
| Phase 2 | Chapter II–VII 逐章 | 待 |
| Phase 3 | 全书统稿/编译/索引 | 待 |
| Phase 4 | 资料卡 + 入仓（08_source_code + datasets/fs21） | 待 |

## 怎么编译

```bat
cd 源码
build.bat                        :: 整书两遍，产出 main.pdf
build.bat check sections\s01-chI-1.tex   :: 单章自检，产出 _check.pdf
```

## 纪律

一切按 `工程文件/BRIEF.md` 执行；翻译纪律的母本是发布仓 `04_playbook/01_数学文献翻译纪律.md`
（v2.1：先通读后落笔、译注必须带来源、来源白名单 nLab/Stacks/ProofWiki、黑名单知乎等）。
