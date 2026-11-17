# 拓扑扭化

> `kw/concept/topological-twist` · 轨道 B · 扭化与拓扑 · 状态 dev

> **先自测**：拓扑扭化是什么，它在整条论证链里起什么作用？

## 一句话

把自旋群对角嵌入自旋群×R-对称群，重新分解超荷表示，使某个超荷成为标量并平方为零；不是截断，理论仍是同一个 $\mathcal N=4$。

## 定义

拓扑扭化指把四维自旋群换成对角嵌入 $\mathrm{Spin}'(4)\subset\mathrm{Spin}(4)\times\mathrm{Spin}(6)_R$，再按新的自旋群重新分解所有场与超荷。这样可选出 $\mathrm{Spin}'(4)$-不变的标量超荷 $Q$，使理论变成拓扑场论。

**记号**：$\kappa:\mathrm{Spin}(4)\to\mathrm{Spin}(6)$；$\mathrm{Spin}'(4)=(1\times\kappa)(\mathrm{Spin}(4))$；$K$ 为与嵌入交换的 $U(1)$ 生成元；$t=v/u\in\mathbb{CP}^1$。

## 要点（为什么需要它）

1. 没有它就没有标量超荷、没有 $Q^2=0$、也没有 $Q$-上同调，全文技术前提在此。
2. $\mathcal N=4$ 有三种不等价扭化，只有第三种（GL 扭化）与几何 Langlands 有关，故选哪种是实质性的。
3. $\kappa$ 的选择保留一个 $U(1)_K$，扭化后的超荷带 $K$ 荷，这允许 $(u,v)$ 组成的 $\mathbb{CP}^1$ 族存活。
4. 扭化后场重新组合成两个一形式与两个复标量，这是 Hitchin 方程与 $\Psi$ 参数的出发点。

## 核心公式

$$
$$\mathrm{Spin}'(4)=(1\times\kappa)(\mathrm{Spin}(4))\subset\mathrm{Spin}(4)\times\mathrm{Spin}(6)$$$$6_v=\wedge^2 4=(2,2)_0\oplus(1,1)_2\oplus(1,1)_{-2}$$$$\Gamma_{0145}\epsilon=\epsilon,\qquad \Gamma_{2367}\epsilon=\epsilon,\qquad \Gamma_{89}\epsilon=-\ii\epsilon$$
$$

$$
$$6_v=\wedge^2 4=(2,2)_0\oplus(1,1)_2\oplus(1,1)_{-2}$$
$$

$$
$$\Gamma_{0145}\epsilon=\epsilon,\qquad \Gamma_{2367}\epsilon=\epsilon,\qquad \Gamma_{89}\epsilon=-\ii\epsilon$$
$$

## 定理与证明（或缺口）

### 三种扭化

$\mathcal N=4$ 超杨–米尔斯理论有三种不等价扭化；两种给出 Donaldson 型瞬子不变量，第三种（GL 扭化）此前无应用，正是与几何 Langlands 相关的那一种。

> 证明状态：**gap**。原文 p.17 只陈述三分法并引文献 [45,52–57]，未给分类证明。

出处：`B p.17`

### 六维向量表示的分解

在 $\kappa$ 下 $4$ 分解为 $(2,1)_1\oplus(1,2)_{-1}$；取 $\wedge^2$ 得 $6_v=\wedge^2 4=(2,2)_0\oplus(1,1)_2\oplus(1,1)_{-2}$，故六个标量变成一个伴随一形式与两个复标量 $\sigma,\bar\sigma$。

1. 把 $\mathrm{SU}(4)_R$ 的 $4$ 按 $\mathrm{SU}(2)_\ell\times\mathrm{SU}(2)_r\times U(1)_K$ 写成 $(2,1)_1\oplus(1,2)_{-1}$。
   - *为什么*：这是 $\kappa$ 的定义方式：$\mathrm{SU}(2)_\ell\times\mathrm{SU}(2)_r$ 嵌入 $\mathrm{SU}(4)_R$ 后余下 $U(1)_K$（原文 p.18–19）。
2. 取 $\wedge^2$ 并分解：$6_v=\wedge^2 4=(2,2)_0\oplus(1,1)_2\oplus(1,1)_{-2}$。
   - *为什么*：$\wedge^2$ 是表示论恒等式，原文 p.19 正是这样算出 $K=0$ 的 $4_v$ 与 $K=\pm2$ 的两个标量。

出处：`B p.19 eq (3.3)`

## 常见误解

- 把扭化当成截断或投影：它是重新解释（重选对角子群），$\mathcal N=4$ 理论本身没有改变。
- 以为三种扭化等价：它们给出不同的拓扑理论，只有 GL 扭化通向几何 Langlands。
- 忽略 $t\leftrightarrow-t$ 的平凡等价性：$I(t)=-t$ 使 $t$ 与 $-t$ 理论相同，但要求两个不变超荷有相同 $K$ 荷（原文 p.22）。

## 相关卡

[$\mathcal N=4$ 超对称杨–米尔斯理论](../concepts/n4-sym-theory.md) · [R-对称](../concepts/r-symmetry.md) · [拓扑量子场论](../concepts/topological-qft.md) · [GL 扭化的构造：选哪个 Spin(4)](../derivations/twist-construction.md)

## 出处（印刷页）

- B p.17（B p.17）
- B p.18（B p.18 eq (3.2)）
- B p.19–21（B p.19–21）

> 说明：A=原文：三种扭化、$\kappa$ 与 (3.2)、$K$ 生成元 (3.3)、$6_v$ 分解、不变旋量条件 (3.11)（B p.17–21）；C=整理：summary、key_points、pitfalls；第二条定理的 complete 只因原文 p.19 明确展示了该表示论计算。
