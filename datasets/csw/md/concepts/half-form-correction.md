---
id: csw/concept/half-form-correction
type: concept
track: C
---

# 半形式修正与 $k\to k+h^\vee$

> 半形式修正：把 $\mathcal{L}^{\otimes k}$ 换成 $\mathcal{L}^{\otimes k}\otimes K^{1/2}$，令 $k\to k+h^\vee$。

**问题**：半形式修正为什么等于 level 平移 $h^\vee$？$K^{1/2}$ 什么时候存在？

## 定义

几何量子化的标准配方要求态是半形式值的截面：$\mathcal{H}=\Gamma_P(\mathcal{M},\mathcal{L}^{\otimes k}\otimes K^{1/2})$，其中 $K=\det T^{*}\mathcal{M}$ 是典范丛。在 CS 情形 $K^{1/2}=\mathcal{L}^{-h^\vee}$（对 $SU(2)$，$K^{1/2}=\mathcal{L}^{-2}$），于是 $\mathcal{L}^{\otimes k}\otimes K^{1/2}=\mathcal{L}^{\otimes(k-h^\vee)}$，等价于把有效 level 写成 $k+h^\vee$ 的共形场论。

*记号*：$K^{1/2}$ 是典范丛的平方根（metaplectic 修正）；$h^\vee$ 是对偶 Coxeter 数（$SU(N)$ 为 $N$）。

## 要点

- 半形式修正来自“焦散面附近的相位”：几何量子化要正确处理 Maslov 相位，必须开方。
- $K^{1/2}$ 存在需要 $c_1(K)$ 为偶；模空间上这个条件与 $h^\vee$ 的整性一致。
- 在 CS 里 $K=\mathcal{L}^{-2h^\vee}$（行列式线丛的负幂），所以 $K^{1/2}=\mathcal{L}^{-h^\vee}$，修正就是 level 平移。
- 修正后 $SU(2)$ 的有效 level 是 $k+2$，这解释了为什么 $q=e^{2\pi i/(k+2)}$，以及为什么可积表示数是 $k+1$。
- 本文在作用量层面没有显式写出 $K^{1/2}$；平移在 (2.16)(2.17) 与 (4.21) 以 $q$ 的形式出现。

## 关键公式

- $\mathcal{H}=\Gamma_P(\mathcal{M},\mathcal{L}^{\otimes k}\otimes K^{1/2})$
- $K^{1/2}=\mathcal{L}^{-h^\vee}$
- $k_{\mathrm{eff}}=k+h^\vee$（$SU(2)$：$k+2$）

## level 平移

在 $SU(2)$ CS 理论中，半形式修正把预量子化线丛 $\mathcal{L}^{\otimes k}$ 换成 $\mathcal{L}^{\otimes k}\otimes K^{1/2}=\mathcal{L}^{\otimes(k+2)}$，于是有效 level 为 $k+2$。

**证明要点**（sketch）：

1. $\mathcal{M}_J$ 的典范丛满足 $K=\mathcal{L}^{-2h^\vee}$。 *（这是模空间的标准事实（$\mathcal{M}$ 的 Kähler 形式是 $\mathcal{L}$ 的曲率）。）*
2. $SU(2)$ 时 $h^\vee=2$，故 $K^{1/2}=\mathcal{L}^{-2}$。 *（对偶 Coxeter 数 $SU(2)$ 为 2。）*
3. $\mathcal{L}^{\otimes k}\otimes\mathcal{L}^{-2}=\mathcal{L}^{\otimes(k-2)}$，与“有效 level $k+2$”的对偶描述一致：$q=e^{2\pi i/(k+2)}$。 *（共形场的 level 与线丛次数差一个 $h^\vee$，两种记法只是把 $h^\vee$ 放在哪边。）*

> **缺口**：本文没有在几何量子化语言里显式构造 $K^{1/2}$；修正的“机制”是后世解释，本卡按原文能与不能分开标注。

## 陷阱

- 不要把 $k_{\mathrm{eff}}=k+h^\vee$ 与原文的 $q=e^{2\pi i/(k+2)}$ 当成两个不同的理论：它们是同一件事的两种写法。
- $K^{1/2}$ 存在不是自动的：$c_1(K)$ 必须是偶类；在奇点处还要选 spin 结构。
- 半形式修正不改变大 $k$ 的 Weyl 律首项，只改变 $1/k$ 修正。

## 相关卡片

- [holomorphic-sections](../concepts/holomorphic-sections.md)
- [s-matrix](../concepts/s-matrix.md)
- [conformal-blocks](../concepts/conformal-blocks.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§2 单圈修正 (2.16)(2.17) 与 §4 (4.21)，印刷页 [359, 382] / PDF 页 [9, 32]（witten1989/sections/s02-weak-coupling.tex（2.16–2.17））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
