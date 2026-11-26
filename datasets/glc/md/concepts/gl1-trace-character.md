---
id: glc/concept/gl1-trace-character
type: concept
track: A
---

# Hecke 特征层的迹函数是特征标

> 若特征值为 $\sigma$ 的 Hecke 特征层 $\mathcal{F}$ 在单位点常值，则 $f_{\mathcal{F}}(\mathcal{O}_X(v))=f_\sigma(v)$。

**问题**：Hecke 特征层的迹函数为什么是 $\operatorname{Pic}(X)$ 的特征标，它在素位处的值等于什么？

## 定义

设 $\mathcal{F}$ 是以秩一局部系统 $\sigma$ 为特征值的 Hecke 特征层（定义 1.1.3），并假设 $\mathcal{F}$ 在单位点 $\mathcal{O}_X\in\operatorname{Pic}_{X/k}$ 处的限制是常值层，从而相应函数将单位元映为 $1$。记 $f_{\mathcal{F}}(y)=\operatorname{Tr}(\operatorname{Fr}_y,\mathcal{F}_{\bar y})$ 为层的迹函数（Grothendieck 的层–函数对应），并在 $\operatorname{Pic}(X)=\operatorname{Pic}_{X/k}(k)$ 上令 $\xi=f_{\mathcal{F}}$。引理断言：$\xi$ 是特征标，且对每个素位 $v$ 有 $f_{\mathcal{F}}(\mathcal{O}_X(v))=f_\sigma(v)$。

*记号*：$\mathcal{O}_X\in\operatorname{Pic}_{X/k}$：单位点（平凡线丛），$\mathcal{O}_X(v)$：$v$ 处对应的线丛；$f_{\mathcal{F}}$：$\mathcal{F}$ 的迹函数；$\operatorname{Fr}_y$：$y$ 处的 Frobenius；$\mathcal{F}_{\bar y}$：几何点处的茎；$f_\sigma(v)=\operatorname{Tr}(\operatorname{Fr}_v,\sigma_{\bar v})$。

## 要点

- 在两个前提下（$\mathcal{F}$ 是以 $\sigma$ 为特征值的 Hecke 特征层；$\mathcal{F}$ 在单位点处为常值层），$\xi=f_{\mathcal{F}}$ 是 $\operatorname{Pic}(X)$ 上的特征标。
- 并且对每个素位 $v$ 有 $f_{\mathcal{F}}(\mathcal{O}_X(v))=f_\sigma(v)$，其中 $f_\sigma(v)=\operatorname{Tr}(\operatorname{Fr}_v,\sigma_{\bar v})$。
- 这条引理说明：Hecke 特征同构是类域论中乘法性方程与 Frobenius 特征值方程的层论替代。
- 单位点处的常值性假设保证相应函数把单位元映为 $1$，而「$\xi$ 是特征标」包含 $\xi(1)=1$ 这一条。

## 关键公式

- $f_{\mathcal{F}}(y):=\operatorname{Tr}(\operatorname{Fr}_y,\mathcal{F}_{\bar y})$
- $f_{\mathcal{F}}(\mathcal{O}_X(v))=f_\sigma(v)$
- $\rho(\operatorname{Fr}_v)=f_\sigma(v)=\operatorname{Tr}(\operatorname{Fr}_v,\sigma_{\bar v})$

## 定理与证明

### 引理 1.1.4（Hecke 特征层的迹是特征标）（要点（有缺口））

设 $\mathcal{F}$ 是以 $\sigma$ 为特征值的 Hecke 特征层，并假设 $\mathcal{F}$ 在单位点 $\mathcal{O}_X\in\operatorname{Pic}_{X/k}$ 处的限制是常值层，从而相应函数将单位元映为 $1$。在 $\operatorname{Pic}(X)=\operatorname{Pic}_{X/k}(k)$ 上令 $\xi=f_{\mathcal{F}}$。则 $\xi$ 是特征标，且对每个素位 $v$，$f_{\mathcal{F}}(\mathcal{O}_X(v))=f_\sigma(v)$。


> 缺口：讲义只述不证：§1.1 在陈述后仅说明它是类域论中乘法性与 Frobenius 特征值方程的层论替代，未写出证明步骤。

*出处*：引理 1.1.4 / 原书 p.7


## 易错点

- 结论只针对 $k$-点 $\operatorname{Pic}(X)=\operatorname{Pic}_{X/k}(k)$ 上的迹函数；$\mathcal{F}$ 本身活在相对 Picard 概形 $\operatorname{Pic}_{X/k}$ 上，两个对象不能混同。
- 单位点处「限制为常值层」是假设而非结论；去掉它，「相应函数把单位元映为 $1$」就不成立，特征标结论也随之失去前提。
- 对闭点也使用记号 $f_\sigma(v)$ 时，Frobenius 指相应的几何 Frobenius（讲义 p.6 的约定），不是任意提升。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§1.1 几何类域论，p.7（PDF p.7），`源码/chapters/ch01.tex:106-109（引理 1.1.4）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/Hecke+eigensheaf — 页面只给 Hecke 特征层的一般定义，未陈述引理 1.1.4 的迹函数为特征标，也未给出 f_F(O_X(v))=f_σ(v)。

## 关联

- `glc/concept/hecke-eigensheaf-gl1`
- `glc/concept/deligne-gl1-existence`
- `glc/concept/geometric-class-field-theory`
