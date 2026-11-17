---
id: glc/concept/truncated-hecke-relation
type: concept
track: D
---

# 截断的最高次 Hecke 关系

> Aut_E 应满足的 Hecke 特征性质中最高次的一条：沿 M↦M(−x) 拉回，次数平移 n 并扭转 det(E_x)。

**问题**：截断的最高次 Hecke 关系里，次数与扭转分别如何变化？

## 定义

设 $G=\operatorname{GL}_n$，$E$ 为 $X$ 上秩 $n$ 的局部系统，$\operatorname{Aut}_E$ 为所要构造的自守层。采用第 2 章的 Hecke 对应约定，截断的最高次 Hecke 关系为
\[
t_x^*\operatorname{Aut}^d_E\simeq\det(E_x)\otimes\operatorname{Aut}^{d+n}_E,
\]
其中 $t_x:\operatorname{Bun}_n^{d+n}\xrightarrow{\sim}\operatorname{Bun}_n^d$，$M\mapsto M(-x)$。等价地，
\[
(t_x)_!\operatorname{Aut}^{d+n}_E\simeq\det(E_x)^{-1}\otimes\operatorname{Aut}^d_E.
\]

*记号*：$E_x$ 为 $E$ 在点 $x$ 处的纤维（$n$ 维），$\det(E_x)$ 为其行列式（一维）；$t_x$ 由在 $x$ 处作 Hecke 修改 $M\mapsto M(-x)$ 得到。

## 要点

- 关系中的次数平移是 $d\mapsto d+n$，与最高次 Hecke 修改相符。
- 扭转因子 $\det(E_x)$ 依赖 $E$ 在 $x$ 的纤维，不能省略。
- 等价形式把 $t_x^*$ 换成 $(t_x)_!$，同时把扭转取逆。
- 这是讲义为 $\operatorname{Aut}_E$ 列出的三条所希望性质中的第 （3） 条，讲义没有在本章证明它。

## 关键公式

- $t_x^*\operatorname{Aut}^d_E\simeq\det(E_x)\otimes\operatorname{Aut}^{d+n}_E$
- $(t_x)_!\operatorname{Aut}^{d+n}_E\simeq\det(E_x)^{-1}\otimes\operatorname{Aut}^d_E$

## 易错点

- 不要把它误读为对一切 Hecke 修改成立：这里只涉及截断的最高次 Hecke 关系（$M\mapsto M(-x)$，次数平移 $n$）。
- 方向与次数不能写反：拉回 $t_x^*$ 把 $d+n$ 的次数送到 $d$，扭转是 $\det(E_x)$ 而不是其逆。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§5.1 回顾：从 Laumon 层到初步的自守层，p.33（PDF p.33），`源码/chapters/ch05.tex:17-25（§5.1 所希望的性质 （3））`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/Hecke+eigensheaf — The page says: 'A Hecke eigensheaf is an object that is taken to a tensor-multiple of itself under the integral transform induced by a Hecke correspondence.' It supports the general notion, but not the det(E_x) twist or the d→d+n degree shift.

## 关联

- `glc/concept/preliminary-automorphic-sheaf`
- `glc/concept/fourier-deligne-transform`
- `glc/concept/gl2-fourier-description`
