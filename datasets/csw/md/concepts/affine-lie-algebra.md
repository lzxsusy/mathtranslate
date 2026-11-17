---
id: csw/concept/affine-lie-algebra
type: concept
track: E
---

# 仿射 Lie 代数与 OPE

> WZW 的对称代数是 $\hat{\mathfrak{g}}_k$：$[J^a_n,J^b_m]=if^{abc}J^c_{n+m}+kn\delta^{ab}\delta_{n+m,0}$；$k$ 就是 level。

**问题**：中心扩张的项 $kn\delta$ 从哪来？它为什么决定了 $c$ 与 $h$？

## 定义

由 WZW 的 Noether 流 $J^a(z)$ 的 Laurent 模式 $J^a_n$ 生成仿射代数 $\hat{\mathfrak{g}}_k$：$[J^a_n,J^b_m]=if^{abc}J^c_{n+m}+kn\delta^{ab}\delta_{n+m,0}$。等价地，OPE $J^a(z)J^b(w)\sim\frac{k\delta^{ab}}{(z-w)^2}+\frac{if^{abc}J^c(w)}{z-w}$。

*记号*：$k$ 是 level（整数）；$f^{abc}$ 是结构常数；$J^a_n$ 是流模式。

## 要点

- 中心项 $kn\delta^{ab}$ 是量子修正：经典流代数没有它。
- 它由 WZW 作用量的 level $k$ 决定，所以“中心扩张的系数 = level”。
- 对易关系的 $\delta_{n+m,0}$ 说明模式 $n$ 与 $-n$ 配对；真空模不变要求 $k$ 整。
- Virasoro 代数由 $J$ 的双线性（Sugawara）构造，中心荷 $c=k\dim G/(k+h^\vee)$。
- 表示论：可积最高权表示由 $(\lambda,\theta)\le k$ 截断。

## 关键公式

- $[J^a_n,J^b_m]=if^{abc}J^c_{n+m}+kn\delta^{ab}\delta_{n+m,0}$
- $J^a(z)J^b(w)\sim\frac{k\delta^{ab}}{(z-w)^2}+\frac{if^{abc}J^c(w)}{z-w}$

## WZW 的流代数

WZW 理论的 Noether 流满足 level $k$ 的仿射代数；其真空表示是可积最高权表示，$k$ 由作用量的 WZ 项系数给出。

**证明要点**（sketch）：

1. 从 $S_{WZW}$ 变分得守恒流 $J^a$。 *（WZW 的对称群是 $G_L\times G_R$。）*
2. 计算 $J^a(z)J^b(w)$ 的 OPE，单极点给结构常数，双极点给 $k\delta^{ab}$。 *（双极点来自作用量的动能项归一化。）*
3. 故流代数是 $\hat{\mathfrak{g}}_k$。 *（中心项系数就是 $k$。）*

> **缺口**：本文不证明流代数，只把它作为 WZW 的已知结构引用（p.360 附近）。

## 陷阱

- 不要把 $k$ 与中心荷 $c$ 混淆：$c$ 由 $k$ 与 $\dim G$、$h^\vee$ 共同决定。
- OPE 的系数约定因书而异（$2\pi$ 因子）；比较前对齐。
- 模式指标 $n$ 的符号约定（$J^a_n$ 是 $z^{n+1}$ 还是 $z^{-n-1}$）影响公式外观。

## 相关卡片

- [wzw-action](../concepts/wzw-action.md)
- [sugawara-construction](../concepts/sugawara-construction.md)
- [conformal-blocks](../concepts/conformal-blocks.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§2–3（WZW 流与仿射代数），印刷页 [359, 371] / PDF 页 [9, 21]（witten1989/sections/s03-knots.tex（§2.1）与 s05-hilbert.tex）

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
