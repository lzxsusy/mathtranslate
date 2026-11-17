---
id: glc/concept/cleanness-expected
type: concept
track: D
---

# 洁净性（第 5 章的预期陈述）

> 第 5 章提出的预期：j_{k,!}F_k 在 Bun_k∩C_k 上洁净；若 F_k 单反常则延拓仍单，加条件后应扩到整个 C_k。

**问题**：定理 5.7.1 为什么只是「预期陈述」，它的证明在哪里给出？

## 定义

设 $1\le k<n$，$F_k$ 为 §5.5 的朴素迭代所定义的层，$j_k:\operatorname{Coh}'_k\hookrightarrow\operatorname{Coh}_k^+$ 为开嵌入，$C_k\subset\operatorname{Coh}_k$ 为 §5.6 的开子叠。

*记号*：「洁净」指 $j_{k,!}F_k\to j_{k,*}F_k$ 为同构；$\operatorname{Bun}_k\cap C_k$ 是 $C_k$ 中 $M_k$ 为向量丛的部分。

## 要点

- 陈述只在 $\operatorname{Bun}_k\cap C_k$ 上断言洁净性（即 $M_k$ 无挠的部分）。
- 若 $F_k$ 是 $C'_k$ 上的单反常层，则洁净延拓仍为单层。
- 在 $C_k$ 的定义中加入额外条件后，同样的洁净性将在整个 $C_k$ 上成立。
- 本节说明洁净性的输入是 Gaitsgory 关于平均函子的消失定理。

## 关键公式

- $j_{k,!}F_k$ 在 $\operatorname{Bun}_k\cap C_k\subset\operatorname{Coh}_k$ 上洁净

## 定理与证明

### 洁净性（预期陈述）（要点（有缺口））

对 $1\le k<n$，延拓 $j_{k,!}F_k$ 至少在 $\operatorname{Bun}_k\cap C_k\subset\operatorname{Coh}_k$ 上洁净。

1. 讲义在本节只陈述这一预期，不在此证明。  
   *为什么*：本节的任务是提出目标并引出平均函子消失定理这一输入。
2. 把证明留给第 6 章：定理 6.2.1 在 $\overline C'_k$ 上证明洁净性，模 §7 的因子化恒等式。  
   *为什么*：第 6 章用消失定理按挠长归纳证明。

> 缺口：讲义只述不证；$\overline C'_k$ 上的完整证明见 §6.2 定理 6.2.1，其中还需先用 §7 的因子化恒等式。

*出处*：定理 5.7.1 / 原书 p.35


## 易错点

- 不要把 5.7.1 与 6.2.1 当成同一条：5.7.1 只在 $\operatorname{Bun}_k\cap C_k$ 上断言且未证；6.2.1 在 $\overline C'_k$ 上证明。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§5.7 洁净性与平均消失，p.35（PDF p.35），`源码/chapters/ch05.tex:100-105（定理 5.7.1）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/geometric+Langlands+correspondence — The page does not state Theorem 5.7.1.

## 关联

- `glc/concept/cleanness-theorem`
- `glc/concept/averaging-functor`
- `glc/concept/vanishing-theorem`
