---
id: page/langlands-program
title: Langlands 纲领
aliases:
  - Langlands program
  - 朗兰兹纲领
kind: hub
status: draft
reviewed_by: []
reviewed_on: 2026-11-27
entries:
  - algebra/langlands-correspondence
  - algebra/l-group
  - algebra/automorphic-representation
  - algebra/hecke-operator
children:
  - page/geometric-langlands
order: 10
note: 本页只是导航骨架，正文待写；子页已有几何 Langlands 一页。
---

# Langlands 纲领

> 枢纽页（hub）。本页尚未撰写正文，只登记入口。任何数学陈述都应落在词条或子页上，本页不生产断言。

## 这是什么

Langlands 纲领猜测：整体域 $F$ 上约化群 $G$ 的自守表示，与 $F$ 的取值于对偶群 ${}^LG$ 的 Galois 表示之间存在自然对应。它有几个彼此平行、语言不同的分支。

## 分支

| 分支 | 自守侧 | 谱侧 | 本仓库入口 |
|---|---|---|---|
| 整体 Langlands（算术） | $G(\mathbb A_F)$ 的自守表示 | ${}^LG$ 的 Galois 表示 | {{entry:algebra/langlands-correspondence}} |
| 几何 Langlands（函数域、曲线） | $\operatorname{Bun}_G(X)$ 上的反常层 | $X$ 上的 $\hat G$-局部系统 | [几何 Langlands 对应：从 Drinfeld 到 FGV](geometric-langlands.md) |
| 局部 Langlands | 局部域上的表示 | Weil–Deligne 群的表示 | 待建 |

## 读法

先看几何那一页，因为它是目前本仓库材料最全、能把「对应」写成定理的分支；算术分支的词条还只有骨架。

## 尚未做完的事

- 整体 Langlands 的正文（词条 `algebra/langlands-correspondence` 仍为 draft）；
- 局部 Langlands 与 $p$-进 Langlands 的入口；
- 与 `page/geometric-langlands` 的互链验收。
