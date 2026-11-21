# 镜像对称（三个方面）

> `hausel22/concept/mirror-symmetry` · 轨道 A · 镜像对称与几何 Langlands · 状态 dev

> **先自测**：同一个 Calabi–Yau 流形的「复几何」与「辛几何」为什么可以互换？

## 一句话

镜像对称把 Calabi–Yau 流形 X 的复几何与镜像流形 Y 的辛几何对应起来；本文按拓扑、同调、SYZ 三个方面使用它。

## 定义

设 $X$ 是复 $n$ 维 Calabi–Yau 流形（复结构 $I_X$、Kähler 形式 $\omega_X$，故也是辛形式）。镜像对称断言存在同维的镜像 Calabi–Yau 流形 $(Y,I_Y,\omega_Y)$，使以 $(X,\omega_X)$ 为目标的二维 $A$ 型非线性 $\sigma$ 模型与以 $(Y,I_Y)$ 为目标的 $B$ 型模型给出同一物理。数学侧面分三层：拓扑镜像对称是 Hodge 数相等 $h^{n-p,q}(X)=h^{p,q}(Y)$；同调镜像对称是范畴等价 $Fuk(X,\omega_X)\cong D^b(Y,I_Y)$；SYZ 镜像对称是同一底 $B\cong S^3$ 上的对偶特殊拉格朗日 $3$-环面纤维化。

**记号**：$X,Y$；$I_X,\omega_X,\Omega_X$；$h^{p,q}$；$Fuk(X,\omega_X)$；$D^b(Y,I_Y)$；$B\cong S^3$。

## 要点（为什么需要它）

1. 三个方面的强度递增：Hodge 数相等可以直接算；范畴等价是猜想；SYZ 给出几何上可检验的构造。
2. 本文真正要检验的对象不是抽象的三维 Calabi–Yau 对，而是 Hitchin 系统自动给出的那对特殊拉格朗日纤维化，见式 (2.2) 与 (2.3)。
3. SYZ 的底 $B\cong S^3$ 只对复三维 Calabi–Yau 成立；Hitchin 底 $\calA$ 是高维仿射空间，所以原文强调两者「在几何情境上并不相同」（§2.1 末）。
4. 拓扑镜像对称在本文是猜想 2.1，不是定理；$\SL_2$、$\SL_3$ 情形由 Hausel–Thaddeus 证明，$\SL_n$ 一般情形 2020 年由 Gröchenig–Wyss–Ziegler 用 $p$ 进积分证明。
5. 三方面共享同一个来源：$\sigma$ 模型的对偶把「复结构的模」与「辛结构的模」互换，这正是 Hitchin 系统超 Kähler 结构 $(I,J,K)$ 里 $I$ 与 $J$ 的关系。

## 核心公式

$$
$$h^{n-p,q}(X)=h^{p,q}(Y)$$$$Fuk(X,\omega_X)\cong D^b(Y,I_Y)$$
$$

$$
$$Fuk(X,\omega_X)\cong D^b(Y,I_Y)$$
$$

## 定理与证明（或缺口）

### Kontsevich 的同调镜像对称表述（1994）

对互为镜像的 Calabi–Yau 流形 $X,Y$，$X$ 的 Fukaya 范畴与 $Y$ 上凝聚层的导出范畴等价：$Fuk(X,\omega_X)\cong D^b(Y,I_Y)$。

> 证明状态：**sketch**。原文只引用这个表述，没有证明；它是猜想，且需要先固定「镜像对」的确切含义（原文用 SYZ 纤维化来固定）。

出处：`A p.2230`

## 常见误解

- Hodge 数相等要写成 $h^{n-p,q}(X)=h^{p,q}(Y)$：既翻转 $p,q$，又把 $p$ 换成 $n-p$；漏掉任一处都是错的。
- 不要把 SYZ 的 $B\cong S^3$ 一般地套到 Hitchin 底 $\calA$ 上：$\calA$ 的维数是 $(g-1)\dim\G$，不是 $3$。
- 拓扑镜像对称在本文是猜想 2.1，引用时不能说成「已证的定理」；只有 $\SL_2,\SL_3$ 与（2020 年后的）$\SL_n$ 一般情形是定理。
- $X$ 与 $Y$ 是同一个 $\sigma$ 模型的两个目标，不是「同一个流形的两种结构」；$\M_\Dol$ 与 $\M_\DR$ 才是同一流形的两个复结构。

## 相关卡

[同调镜像对称](../concepts/homology-mirror-symmetry.md) · [SYZ 镜像对称](../concepts/syz-mirror-symmetry.md) · [拓扑镜像对称](../concepts/topological-mirror-symmetry.md) · [Hitchin 系统](../concepts/hitchin-system.md)

## 出处（印刷页）

- A p.2230（A p.2230）
- A p.2231（A p.2231）

> 说明：A=原文 §2.1 的三方面划分与 §2.2 的 Kontsevich 表述；B=把三方面按「可算—猜想—构造」排成强弱阶梯；C=「三方面共享超 Kähler 结构」是我们对 §2.5 的归纳，原文未如此明说。最没把握处：SYZ 与 Hitchin 纤维化「几何情境不同」的确切含义，原文只有一句。
