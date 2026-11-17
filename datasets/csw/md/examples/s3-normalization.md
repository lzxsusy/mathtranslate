---
id: csw/example/s3-normalization
type: example
track: G
---

# $Z(S^3)=S_{00}$ 的数值检验

> $Z(S^3)=\sqrt{\frac{2}{k+2}}\sin\frac{\pi}{k+2}$：$k=1$ 给 $1/\sqrt2$，$k=2$ 给 $1/2$。

**问题**：为什么 $S^3$ 的 CS 配分函数等于 $S_{00}$？用数值检验 $k=1,2$。

## 设定

$S^3$ 可看成 $S^2\times S^1$ 沿边界环面做手术；手术公式给 $Z(S^3)=S_{00}$（乘以适当的标架相位，标准标架下为 1）。

## 计算

1. 对 $SU(2)_k$，$S_{00}=\sqrt{\frac{2}{k+2}}\sin\frac{\pi}{k+2}$。 *（$j=l=0$ 代入正弦公式。）*
2. $k=1$：$\sqrt{2/3}\sin(\pi/3)=\sqrt{2/3}\cdot\frac{\sqrt3}2=\frac1{\sqrt2}$。 *（算术。）*
3. $k=2$：$\sqrt{2/4}\sin(\pi/4)=\frac1{\sqrt2}\cdot\frac{\sqrt2}2=\frac12$。 *（算术。）*

## 结果

$Z(S^3)_{k=1}=1/\sqrt2$，$Z(S^3)_{k=2}=1/2$。

## 核对

两者都满足 $|Z|\le1$ 且随 $k$ 增大振荡衰减（半经典极限）。

## 陷阱

- 常见错误：把 $k=1$ 的 $Z(S^3)$ 写成 $1/2$（那是 $k=2$ 的值）。
- 标架相位会引入 $e^{2\pi i\cdot\text{标架}\cdot c/24}$，标准 $S^3$ 取 1。

## 相关卡片

- [s-matrix](../concepts/s-matrix.md)
- [su2-k2-s-matrix](../examples/su2-k2-s-matrix.md)
- [surgery-formula](../concepts/surgery-formula.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§4.5（(4.51) 附近，p.393），印刷页 [393, 393] / PDF 页 [43, 43]（witten1989/sections/s08-calculability-c.tex（§4.5））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
