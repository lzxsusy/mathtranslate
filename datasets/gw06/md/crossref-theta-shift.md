# 译注把 θ 角平移的出处引成了 §2.4

- **id**：`gw06/correction/crossref-theta-shift`
- **类型**：correction
- **位置**：§2.2
- **问题**：为什么 $\eta\to\eta-\alpha$ 这条平移只能出自 §2.5 而不是 §2.4？

> 原译注把「$T:\theta\to\theta+2\pi$ 导出 $\eta\to\eta-\alpha$」归给 §2.4（电磁对偶），实际出自 §2.5 的式 (2.50)。

## 位置

§2.3 末条译注，s02a-definition.tex:281

## 原文片段

```latex
第~\ref{sec:2.4}~节由 $T:\theta\to\theta+2\pi$ 导出的平移 $\eta\to\eta-\alpha$
```

## 改为

```latex
第~\ref{sec:2.5}~节由 $T:\theta\to\theta+2\pi$ 导出的平移 $\eta\to\eta-\alpha$
```

## 依据

式 (2.50) 在 s02b-duality.tex:594 才出现，其正文即 $\eta\to\eta-\alpha$，并在随后两句说明它与 $\theta$ 项相消；§2.5 的标题就是「$\theta$ 角的平移」。§2.4「电磁对偶」只用到 $\Tr\alpha\mathfrak m$ 一类项，没有这条平移。译注内部的交叉引用指错，读者按图索骥会翻到一个不讲该变换的节。

## 说明

仅改译注里的 \ref 目标，未动正文；同一条译注中另一处「§2.4 作用量中」指 §2.4 本身，正确，保留。

## 批注

### 含糊点拨：为什么平移是 η−α 而不是 η

Witten 效应把四维 $\theta$ 角的平移 $\theta\to\theta+2\pi$ 与面算符参数的平移绑在一起：$\alpha$ 不动，而 $\eta$ 要减去 $\alpha$。用作用量看最清楚——$\theta$ 项与 $\Tr\alpha\mathfrak m$、$\Tr\alpha\eta$ 出现在同一处，$\theta$ 整平移一圈后，要维持配分函数不变只能让 $\eta$ 反向平移 $\alpha$。

## 出处

- S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric Langlands Program（arXiv:hep-th/0612073v2）中译校订本 §2.3；印刷页 [11] / PDF 页 [12]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s02a-definition.tex:278-284`
- 该句位于§2.3（小节的起始印刷页为第 11 页，PDF 第 12 页）。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
