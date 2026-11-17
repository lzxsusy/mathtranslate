---
id: csw/example/su2-torus-theta
type: example
track: C
---

# $SU(2)$ 环面：$k$ 个截面，半形式后 $k+1$

> $SU(2)_k$ 环面模空间是枕头套；$\cL^{\otimes k}$ 给 $k$ 个截面，加半形式后 $k+1$。

**问题**：为什么 $SU(2)$ 的环面维数是 $k+1$ 而不是 $k$？多出来的 1 从哪里来？

## 设定

取 $G=SU(2)$、$\Sigma=T^2$。平坦 $SU(2)$ 联络模 $SU(2)$ 共轭，得枕头套 $T^2/\{\pm1\}$（轨形，4 个 $\mathbb{Z}_2$ 点）。线丛 $\cL$ 的 $k$ 次幂给 $k$ 个 theta 级数；半形式修正取 $K^{1/2}=\cL^{-2}$。

## 计算

1. $\cM_J$ 的 Kähler 形式 $\omega$ 的类给预量子化 $\cL$；$\cL^{\otimes k}$ 的全纯截面是 $k$ 个 theta 函数（同 $U(1)$ 但模 $\mathbb{Z}_2$）。 *（枕头套上的 theta 函数是 $U(1)$ theta 函数的 $\mathbb{Z}_2$ 不变部分。）*
2. 半形式修正把线丛换成 $\cL^{\otimes k}\otimes K^{1/2}=\cL^{\otimes(k-2)}$（因为 $K^{1/2}=\cL^{-2}$）。 *（$SU(2)$ 的 $h^\vee=2$。）*
3. 因此有效 level 是 $k+2$，可积表示是 $j=0,\frac12,\dots,\frac{k+1}2$，共 $k+2$ 个；但环面共形块只取到 $\dim=k$ 的 $\cL^{\otimes k}$ 部分加上半形式，得 $k+1$。 *（环面维数等于有效 level 的可积表示数减一（除去 $j=\frac{k+1}2$ 的边界贡献）。）*

## 结果

$\dim\cH(T^2)=k$（只用 $\cL^{\otimes k}$）；半形式后为 $k+1$（$=k+2-1$）。$k=1$：$\dim=2$；$k=2$：$\dim=3$。

## 核对

$k=1$ 时 $SU(2)_1$ 的有效 level 3 有两个可积表示 $j=0,\frac12$，环面维数 2；与 $\dim\cH(T^2)=k+1=2$ 一致。$k=2$ 时 $j=0,\frac12,1$ 三个，维数 3。

## 陷阱

- 不要写“环面维数 = $k$”就完事：物理 Hilbert 空间（带半形式）是 $k+1$。
- $g=1$ 时 $(2g-2)d=0$，但模空间不是点（枕头套），维数公式失效。

## 相关卡片

- [pillowcase-dimension](../examples/pillowcase-dimension.md)
- [half-form-correction](../concepts/half-form-correction.md)
- [abelian-torus-dimension](../examples/abelian-torus-dimension.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§4.3（环面，p.385）与 (4.21)，印刷页 [385, 382] / PDF 页 [35, 32]（witten1989/sections/s06-calculability-a.tex（§4.3））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
