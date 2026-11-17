---
id: csw/concept/prequantization-determinant-line
type: concept
track: C
---

# 预量子化：行列式线丛

> 在模空间上取行列式线丛 $\mathcal{L}$（Quillen 度规）；$c_1(\mathcal{L})=[\omega]$，所以 $[\mathcal{L}^{\otimes k}]=k[\omega]$，整性自动满足。

**问题**：为什么 CS 的预量子化不需要 Weil–Kostant 的整性条件？行列式线丛的曲率为什么正好是辛形式？

## 定义

设 $\pi:\mathcal{E}\to M$ 是模空间上的全纯向量丛族（纤维是 $\bar\partial$ 的核/余核），行列式线丛 $\mathcal{L}=\det(\ker\bar\partial)^*\otimes\det(\operatorname{coker}\bar\partial)$。它带 Quillen 度规与相容联络，其曲率为 $F_\nabla=-2\pi i\,\omega$（适当归一化）。因此取 $\mathcal{L}^{\otimes k}$ 就得到曲率 $k\omega$ 的预量子化线丛。

*记号*：$\mathcal{L}$ 是行列式线丛；$\omega$ 是模空间的 Kähler 形式；$k$ 是 CS level，整性由大规范变换保证。

## 要点

- 预量子化的核心条件 $[\omega]\in H^2(M,\mathbb{Z})$ 在这里不是假设，而是构造：行列式线丛的 $c_1$ 自动整。
- Quillen 度规的曲率由 $\bar\partial$ 族的指标定理给出，正好等于模空间的 Kähler 形式。
- 取 $\mathcal{L}^{\otimes k}$ 相当于把 level 提到 $k$：作用量的 $k$ 与线丛的次数是同一个整数。
- 这就是 Witten 说的“用行列式线丛绕过 Weil–Kostant”：不需要先验地检查整性，线丛是构造性存在的。
- 代价：模空间有奇点时，行列式线丛的构造要小心（可约联络处），本文不处理。

## 关键公式

- $\mathcal{L}=\det(\ker\bar\partial)^*\otimes\det(\operatorname{coker}\bar\partial)$
- $F_\nabla=-2\pi i\,\omega$
- $c_1(\mathcal{L}^{\otimes k})=k[\omega]$

## 行列式线丛的第一陈类

在光滑模空间上，行列式线丛 $\mathcal{L}$ 的第一陈类等于 Kähler 形式 $[\omega]$（归一化相差常数 $2\pi$）。

**证明要点**（sketch）：

1. 对全纯族 $\bar\partial_s$，曲率 $F_\nabla=\partial\bar\partial\log\det\Delta$（Quillen）。 *（行列式线丛的联络由 $\bar\partial$ 的族决定，Quillen 度规给出曲率。）*
2. 由指标定理，$\partial\bar\partial\log\det\Delta$ 的积分给出模空间的 Kähler 类。 *（这是 Quillen 定理与 Grothendieck–Riemann–Roch 的二维情形。）*
3. 故 $c_1(\mathcal{L})=[\omega]$，取 $k$ 次幂得 $k[\omega]$。 *（线丛的 $c_1$ 相加，次数即 $k$。）*

> **缺口**：本文直接引用行列式线丛与 Quillen 度规（文献 [33][34]），未证明曲率公式；奇点处需相交上同调。

## 陷阱

- 不要把 $\mathcal{L}^{\otimes k}$ 里的 $k$ 与丛的“规范固定”混淆：这里的 $k$ 就是 CS 作用量的整数 level。
- $[\omega]$ 整并不意味着任意 $k$ 都能用：半形式修正会把有效 level 提到 $k+h^\vee$，别把两个 $k$ 混用。
- 行列式线丛的曲率有 $2\pi$ 因子，视归一化而定；比较 $c_1$ 与 $[\omega]$ 前先对齐 $\omega$ 的归一化。

## 相关卡片

- [holomorphic-sections](../concepts/holomorphic-sections.md)
- [polarization](../concepts/polarization.md)
- [half-form-correction](../concepts/half-form-correction.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.1 预量子化与行列式线丛，印刷页 [368, 369] / PDF 页 [18, 19]（witten1989/sections/s04-canonical.tex（§3.1））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
