---
id: csw/example/su2-k2-s-matrix
type: example
track: G
---

# $SU(2)$、$k=2$ 的 $S$ 矩阵

> $k=2$ 的可积表示 $j=0,\frac12,1$；$S$ 是 $3\times3$ 对称矩阵，$S_{00}=\frac12$，$S^2=1$。

**问题**：用正弦公式算 $k=2$ 的 $3\times3$ $S$ 矩阵，并验证 $S^2=1$、$S^2=(ST)^3$。

## 设定

取 $SU(2)_2$：$k=2$，可积表示 $j=0,\frac12,1$。共形权 $h_j=\frac{j(j+1)}{k+2}=\frac{j(j+1)}4$：$h_0=0$，$h_{1/2}=\frac3{16}$，$h_1=\frac12$；中心荷 $c=\frac{3k}{k+2}=\frac32$。

## 计算

1. 归一化：$S_{jl}=\sqrt{\frac{2}{k+2}}\sin\frac{\pi(2j+1)(2l+1)}{k+2}=\frac1{\sqrt2}\sin\frac{\pi(2j+1)(2l+1)}4$。 *（$\sqrt{2/4}=1/\sqrt2$；$2j+1$ 与 $2l+1$ 取 $1,2,3$。）*
2. 逐项：$(1,1)\Rightarrow\sin\frac\pi4=\frac{\sqrt2}2$，$S_{00}=\frac12$；$(1,2)\Rightarrow\sin\frac\pi2=1$，$S_{0,1/2}=\frac1{\sqrt2}$；$(2,2)\Rightarrow\sin\pi=0$，$S_{1/2,1/2}=0$；$(2,3)\Rightarrow\sin\frac{3\pi}2=-1$，$S_{1/2,1}=-\frac1{\sqrt2}$；$(3,3)\Rightarrow\sin\frac{9\pi}4=\frac{\sqrt2}2$，$S_{11}=\frac12$。 *（每个矩阵元只用正弦特殊值；$9\pi/4$ 与 $\pi/4$ 同值。）*
3. 整理得对称矩阵 $S=\frac12\begin{pmatrix}1&\sqrt2&1\\\sqrt2&0&-\sqrt2\\1&-\sqrt2&1\end{pmatrix}$，直接乘得 $S^2=1$。 *（$S$ 对称；$k=2$ 时 $S^2=1$。）*

## 结果

$S=\frac12\begin{pmatrix}1&\sqrt2&1\\\sqrt2&0&-\sqrt2\\1&-\sqrt2&1\end{pmatrix}$，$S$ 对称、$S^2=1$，$S_{00}=\frac12$。

## 核对

$Z(S^3)=S_{00}=1/2$，与 $\sqrt{\frac{2}{k+2}}\sin\frac{\pi}{k+2}=\frac1{\sqrt2}\sin\frac\pi4=\frac12$ 一致。

## 陷阱

- 归一化易错：$k=2$ 时 $\sqrt{2/(k+2)}=1/\sqrt2$，不是 $\sqrt2$。
- $S_{1/2,1/2}=0$ 是对的：$(2j+1)(2l+1)=4$，$\sin\pi=0$。
- 指标只取可积表示 $j\le k/2$；$k=2$ 时 $j=0,\frac12,1$ 共 3 个。

## 相关卡片

- [s-matrix](../concepts/s-matrix.md)
- [s3-normalization](../examples/s3-normalization.md)
- [level-shift-check](../examples/level-shift-check.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§4.5（$S$ 矩阵与 $Z(S^3)$，p.388–393），印刷页 [388, 393] / PDF 页 [38, 43]（witten1989/sections/s08-calculability-c.tex（§4.5））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
