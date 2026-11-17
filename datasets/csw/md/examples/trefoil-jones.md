---
id: csw/example/trefoil-jones
type: example
track: G
---

# 三叶结的 Jones 多项式

> $V_{\text{trefoil}}(t)=-t^{-4}+t^{-3}+t^{-1}$；它是 $SU(2)$、$k$ 足够大时的 Wilson 线期望值。

**问题**：用拆接关系算三叶结的 Jones 多项式，并与 CS 的 Wilson 线期望值对照。

## 设定

三叶结的标准投影有 3 个交叉；用 Kauffman bracket 状态和或 Jones 拆接关系 $t^{-1}V(L_+)-tV(L_-)=(t^{1/2}-t^{-1/2})V(L_0)$ 递归。

## 计算

1. 从平凡纽结 $V=1$ 出发，对三叶结的 3 个交叉依次做拆接，归到平凡链环。 *（每次拆接把交叉换成 0 或 ∞ 光滑化。）*
2. 整理得 $V_{\text{trefoil}}(t)=-t^{-4}+t^{-3}+t^{-1}$（右手三叶结；左手取 $t\to t^{-1}$）。 *（标准结果，可与 Kauffman bracket 的状态和互验。）*
3. 在 CS 里，这个多项式是 $SU(2)$、定义表示、$k$ 足够大时的 $\langle W_{1/2}(K)\rangle_{S^3}$，$t=q=e^{2\pi i/(k+2)}$。 *（$q$ 由 level 给出；有限 $k$ 时有截断修正。）*

## 结果

$V_{\text{trefoil}}(t)=-t^{-4}+t^{-3}+t^{-1}$；$t=q=e^{2\pi i/(k+2)}$ 时是 CS 的 Wilson 线期望值（大 $k$ 极限）。

## 核对

$t=1$ 时 $V=-1+1+1=1$，与“平凡化”一致（$V(1)=1$）；$|V(t)|$ 在 $|t|=1$ 上有界，符合多项式不变量。

## 陷阱

- 左右手三叶结的 Jones 多项式互为 $t\to t^{-1}$，别混。
- 有限 $k$ 时 CS 期望值不等于 Jones 多项式：需要截断/量子群修正。

## 相关卡片

- [jones-from-cs](../concepts/jones-from-cs.md)
- [wilson-line](../concepts/wilson-line.md)
- [s-matrix](../concepts/s-matrix.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§1（(1.6)）与 §4.6（p.394），印刷页 [356, 394] / PDF 页 [6, 44]（witten1989/sections/s09-applications.tex（§4.6））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
