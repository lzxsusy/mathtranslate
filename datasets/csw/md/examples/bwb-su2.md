---
id: csw/example/bwb-su2
type: example
track: D
---

# $SU(2)$ 的 BWB：$H^0(G/T,\mathcal{L}_j)=R_j$

> $SU(2)$ 的旗流形是 $S^2$；$H^0(S^2,\mathcal{L}_j)$ 的维数是 $2j+1$，即自旋 $j$ 表示。

**问题**：在 $S^2$ 上算 $\mathcal{L}_j$ 的全纯截面维数，验证 BWB。

## 设定

$G=SU(2)$，$T=U(1)$，$G/T=S^2$。最高权 $j$ 的线丛 $\mathcal{L}_j=\mathcal{O}(2j)$（度数 $2j$）。

## 计算

1. 由 Riemann–Roch 在 $S^2$ 上：$\dim H^0(\mathcal{O}(d))=d+1$（$d\ge0$）。 *（$S^2$ 的 $\deg K=-2$；RR：$\dim H^0=\deg\mathcal{O}(d)+1$。）*
2. 取 $d=2j$，得 $\dim=2j+1$。 *（代入。）*
3. $2j+1$ 正是自旋 $j$ 表示的维数，故 $H^0=R_j$。 *（Weyl 维数公式在 $SU(2)$ 给 $2j+1$。）*

## 结果

$\dim H^0(S^2,\mathcal{O}(2j))=2j+1=\dim R_j$。

## 核对

$j=\frac12$：$\dim=2$（自旋 $\frac12$ 表示）；$j=1$：$\dim=3$（伴随表示）。

## 陷阱

- 线丛的度数是 $2j$ 而不是 $j$：$S^2$ 上 $\omega$ 的积分归一化决定了这一点。
- 这里 $\lambda$ 直接是最高权，不加 $\rho$；加 $\rho$ 的是半形式修正。

## 相关卡片

- [borel-weil-bott](../concepts/borel-weil-bott.md)
- [kz-two-point](../examples/kz-two-point.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.3（BWB，p.372），印刷页 [372, 372] / PDF 页 [22, 22]（witten1989/sections/s05-hilbert.tex（§3.3））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
