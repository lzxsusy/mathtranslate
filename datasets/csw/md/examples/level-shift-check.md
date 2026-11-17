---
id: csw/example/level-shift-check
type: example
track: C
---

# 半形式修正的数值检验：$k$ 与 $k+2$

> 对比“$k$ 个 theta 截面”与“$k+1$ 个可积表示”：多出的 1 来自半形式 $K^{1/2}=\mathcal{L}^{-2}$，即 $k\to k+2$。

**问题**：用 $k=1,2,3$ 的数值验证：环面维数 $k+1$ 与有效 level $k+2$ 的可积表示数 $k+2$ 相差 1。

## 设定

$SU(2)_k$：可积表示数 $=k+1$（$j=0,\dots,\frac k2$）；环面态空间维数（含半形式）$=k+1$；有效 level $k+2$ 的可积表示数 $=k+2$。

## 计算

1. $k=1$：$\mathcal{L}^{\otimes1}$ 给 1 个 theta 截面；半形式 $K^{1/2}=\mathcal{L}^{-2}$ 后为 $\mathcal{L}^{\otimes(k+2)}$，环面维数 $k+1=2$。 *（$K^{1/2}=\mathcal{L}^{-h^\vee}$，$SU(2)$ 的 $h^\vee=2$。）*
2. $k=2$：$\mathcal{L}^{\otimes2}$ 给 2 个；半形式后维数 $k+1=3$。 *（同一条平移公式。）*
3. 与有效 level $k+2$ 的可积表示数比较：共 $k+2$ 个表示（$j=0,\dots,\frac{k+1}2$）；环面维数 $k+1$ 比它少 1。 *（$k=1$：2 vs 3；$k=2$：3 vs 4；$k=3$：4 vs 5。）*

## 结果

$\dim\mathcal{H}(T^2)=k+1$；有效 level $k+2$ 的可积表示数为 $k+2$；两者差 1。

## 核对

$k=1$：$2=3-1$；$k=2$：$3=4-1$；$k=3$：$4=5-1$。三个值全部吻合。

## 陷阱

- 不要把可积表示数与环面态空间维数混为一谈：一般差 1。
- 有效 level 是 $k+2$，不是 $k$；半形式修正就在这一步。
- 只有 $SU(2)$ 用 $+2$；一般群用 $+h^\vee$。

## 相关卡片

- [half-form-correction](../concepts/half-form-correction.md)
- [su2-torus-theta](../examples/su2-torus-theta.md)
- [su2-k2-s-matrix](../examples/su2-k2-s-matrix.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§4.3 与 (4.21)（p.382–385），印刷页 [382, 385] / PDF 页 [32, 35]（witten1989/sections/s06-calculability-a.tex（§4.3））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
