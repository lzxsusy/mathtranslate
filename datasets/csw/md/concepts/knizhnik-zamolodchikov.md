---
id: csw/concept/knizhnik-zamolodchikov
type: concept
track: E
---

# Knizhnik–Zamolodchikov 方程

> 共形块作为 $z_i$ 的函数满足 $\kappa\partial_{z_i}\Psi=\sum_{j\ne i}\frac{\Omega_{ij}}{z_i-z_j}\Psi$，$\kappa=k+h^\vee$。

**问题**：KZ 方程怎么从 WZW 的 Ward 恒等式推出来？为什么分母是 $k+h^\vee$？

## 定义

设 $\Psi(z_1,\dots,z_n)$ 是带插入 $(R_i)$ 的共形块。由 $\bar\partial$ 的零模条件与 Sugawara 的 $T$ 的 Ward 恒等式，得 KZ 方程 $\kappa\partial_{z_i}\Psi=\sum_{j\ne i}\frac{\Omega_{ij}}{z_i-z_j}\Psi$，其中 $\Omega_{ij}=\sum_aT^a_{(i)}T^a_{(j)}$，$\kappa=k+h^\vee$。

*记号*：$\Omega_{ij}$ 是第 $i,j$ 个标记点表示上的 Casimir 双线性；$\kappa$ 是有效 level。

## 要点

- KZ 是“全纯性 + 共形 Ward 恒等式”的联合结果：手征场只依赖 $z$，$T$ 的极点给出 $\partial_z$。
- $\kappa=k+h^\vee$ 来自 Sugawara 的归一化；把 $\kappa$ 写成 $k$ 是常见错误。
- 两点函数：$\Psi=(z_1-z_2)^{-2h_j}$，指数正是共形权（$SU(2)$、$k=1$ 时 $h_{1/2}=1/4$）。
- KZ 是平坦联络的方程：$\nabla\Psi=0$，其单值性给出共形块的表示（与 Hitchin 联络一致）。
- 在 $g=0$ 有显式形式；高亏格要加更多项，但仍是射影平坦联络。

## 关键公式

- $\kappa\partial_{z_i}\Psi=\sum_{j\ne i}\frac{\Omega_{ij}}{z_i-z_j}\Psi$
- $\kappa=k+h^\vee$
- $n=2:\ \Psi=(z_1-z_2)^{-2h_j}$

## KZ 方程的来源

WZW 共形块满足 KZ 方程，$\kappa=k+h^\vee$；该方程在 $g=0$ 时是共形块空间的射影平坦联络的显式形式。

**证明要点**（sketch）：

1. 共形块是全纯的：$\bar\partial\Psi=0$。 *（手征场只依赖 $z$。）*
2. 用 Sugawara 的 $T$ 与初级场 OPE，得到 $\partial_{z_i}\Psi$ 的表达式。 *（Ward 恒等式把 $T$ 的插入写成 $\partial_z$。）*
3. 整理得 $\kappa\partial_{z_i}\Psi=\sum\Omega_{ij}/(z_i-z_j)\Psi$，$\kappa=k+h^\vee$。 *（Sugawara 的归一化决定 $\kappa$。）*

> **缺口**：本文正文没有出现 KZ 方程；只说“带标记点时联络显式”，严格形式见河野。

## 陷阱

- 分母写 $k$ 会破坏 $SU(2)$、$k=1$ 的 $h_{1/2}=1/4$ 检验。
- $\Omega_{ij}$ 的符号取决于 $T^a$ 的厄米性与 $\bar\partial$ 的约定，数值检验前先对齐。
- KZ 只给全纯部分的方程；反全纯部分由共轭给出。

## 相关卡片

- [conformal-blocks](../concepts/conformal-blocks.md)
- [hitchin-connection](../concepts/hitchin-connection.md)
- [sugawara-construction](../concepts/sugawara-construction.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.2（射影平坦联络，BPZ [32]），印刷页 [369, 370] / PDF 页 [19, 20]（witten1989/sections/s04-canonical.tex（§3.2））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
