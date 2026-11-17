---
id: csw/concept/flag-orbit-symplectic
type: concept
track: D
---

# 旗流形上的辛形式与轨道方法

> $G/T$ 上的辛形式 $\omega_\lambda(X,Y)=\frac12\langle\lambda,[X,Y]\rangle$ 由最高权给出；$G/T$ 就是这个权对应的余伴随轨道。

**问题**：$G/T$ 上的辛形式为什么由 $\lambda$ 决定？为什么 $G/T$ 是余伴随轨道？

## 定义

把 $G/T$ 等同于余伴随轨道 $\mathcal{O}_\lambda=G/T$（$\lambda$ 支配整）。其 Kirillov–Kostant–Souriau 辛形式在单位元处为 $\omega_\lambda(X,Y)=\frac12\langle\lambda,[X,Y]\rangle$，并 $G$-不变地延拓。积分归一化后 $[\omega_\lambda]=\lambda$。

*记号*：$\mathcal{O}_\lambda$ 是 $\lambda$ 的余伴随轨道；$\langle\cdot,\cdot\rangle$ 是 $\mathfrak{g}$ 与 $\mathfrak{g}^*$ 的配对。

## 要点

- $G/T$ 是旗流形，也是“最大”的余伴随轨道；$\lambda$ 决定辛形式。
- 轨道方法（Kirillov–Kostant–Souriau）说：不可约表示 = 轨道的几何量子化。
- 这就是 Witten 把“表示 $R$”看作“辛流形 $G/T$ 的量子化”的依据。
- 整性条件：$\lambda$ 为整权时 $[\omega_\lambda]$ 才整，才有预量子化线丛。
- 在 CS 里把 $G/T$ 的相空间与 $\Sigma$ 的相空间做直积（并做辛商），就得到扩大后的模空间 $M_{P_s,R_s}$。

## 关键公式

- $\omega_\lambda(X,Y)=\tfrac12\langle\lambda,[X,Y]\rangle$
- $[\omega_\lambda]=\lambda\in H^2(G/T,\mathbb{Z})$
- $\mathcal{O}_\lambda\cong G/T$

## 轨道与表示的对应

对支配整权 $\lambda$，余伴随轨道 $\mathcal{O}_\lambda\cong G/T$ 的几何量子化给出不可约表示 $R_\lambda$。

**证明要点**（sketch）：

1. $\mathcal{O}_\lambda$ 上的辛形式由 $\lambda$ 给出，且 $[\omega_\lambda]$ 整。 *（支配整权保证整性。）*
2. 预量子化线丛是 $\cL_\lambda$，Kähler 极化取 $G/T$ 的复结构。 *（$G/T$ 有自然的 $G$-不变复结构。）*
3. BWB 给出 $H^0=R_\lambda$，几何量子化与轨道方法一致。 *（这是轨道方法在紧群情形的经典结论。）*

> **缺口**：本文只说“$R$ 可看成某辛流形的量子化”，未逐条验证整性与极化。

## 陷阱

- 不要把 $G/T$ 的辛形式与 $\Sigma$ 的辛形式混淆：前者是表示的“内空间”，后者是规范场的相空间。
- $\lambda$ 必须支配且整，否则既无预量子化也有上同调跳变。
- 轨道方法的“量子化”在奇轨道上有额外选择（半形式），与 CS 主问题的半形式修正同源。

## 相关卡片

- [borel-weil-bott](../concepts/borel-weil-bott.md)
- [puncture-gauss-law](../concepts/puncture-gauss-law.md)
- [symplectic-quotient](../concepts/symplectic-quotient.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.3 旗流形与辛形式，印刷页 [371, 372] / PDF 页 [21, 22]（witten1989/sections/s05-hilbert.tex（§3.3））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
