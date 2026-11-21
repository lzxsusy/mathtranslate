# 几何 Langlands 对应

> `hausel22/concept/geometric-langlands-correspondence` · 轨道 A · 镜像对称与几何 Langlands · 状态 dev

> **先自测**：为什么自守那一侧是 $D$-模而不是函数？

## 一句话

几何 Langlands 对应把曲线上的 $\G$-局部系统变成 $\G^\vee$-丛模叠上的 holonomic $D$-模，并要求它是 Hecke 算子的特征层。

## 定义

对光滑射影曲线 $C$，Beilinson–Drinfeld 提出：由 $C$ 上的 $\G$-局部系统（Galois 表示的几何类比）出发，构造丛的模叠 $Bun_{\G^\vee}$ 上的 holonomic $D$-模（自守形式的几何类比），并要求它是某些 Hecke 算子的特征层。原文指出这一构造对 opers 已完成。

**记号**：$C$；$\G$-局部系统；$Bun_{\G^\vee}$；holonomic $D$-模；Hecke 算子；oper。

## 要点（为什么需要它）

1. 两侧的群是交叉的：局部系统在 $\G$ 侧，自守 $D$-模在 $\G^\vee$ 侧的丛模叠上。
2. 「特征层」是核心：Hecke 算子作用后只差一个特征值（这里是局部系统本身），这正是数域情形「自守表示是 Hecke 算子的特征向量」的几何化。
3. opers 是一类特殊的 $\G$-局部系统（带额外全纯结构），Beilinson–Drinfeld 只在这一类上完成了构造。
4. 本文的新视角：这个对应可以看成 $\M_\DR$ 与 $\M^\vee_\DR$ 之间的增强镜像对称（§2.5 首段末句）。

## 核心公式

$$
$$\{\text{$\G$-local systems on }C\}\rightsquigarrow\{\text{holonomic $D$-modules on }Bun_{\G^\vee}\}$$
$$

## 定理与证明（或缺口）

### Beilinson–Drinfeld 的 oper 情形

对 $C$ 上一类特定的 $\G$-局部系统（opers），存在 $Bun_{\G^\vee}$ 上的 holonomic $D$-模，它是 Hecke 算子的特征层。

> 证明状态：**sketch**。原文只在综述层面引用，未展开构造；一般局部系统的情形仍是猜想。

出处：`A p.2231`

## 常见误解

- 两侧的群写反：局部系统取自 $\G$，自守 $D$-模落在 $Bun_{\G^\vee}$ 上；写同一侧就变成了「几何 Satake」的内容。
- holonomic $D$-模不是「$D$-模的一个例子」，holonomic 是维数条件（特征簇 Lagrangian），少了它对应不成立。
- oper 不是「任意局部系统」：oper 带完整旗，是局部系统里的特殊一类，Beilinson–Drinfeld 只在这一类上完成构造。
- 「特征层」的特征值不是数，而是原局部系统本身；把它当标量是最常见的误读。

## 相关卡

[Langlands 对偶群 $\G^\vee$](../concepts/langlands-dual-group.md) · [增强镜像对称](../concepts/enhanced-mirror-symmetry.md) · [几何 Langlands 的经典极限 $\mathscr{S}$](../concepts/classical-limit-langlands.md) · [经典极限 $\mathscr{S}$ 与算子的交换](../derivations/s-intertwines-operators.md)

## 出处（印刷页）

- A p.2231（A p.2231）
- A p.2234–2235（A p.2234）

> 说明：A=原文 §2.2 的对应陈述与 §2.5 末句的「可理解为增强镜像对称」；B=把「特征层 = 特征向量几何化」这层意思补出来；C=holonomic 的维数含义是我们补的。最没把握处：opers 的精确定义原文未给，只说是「一类特定的局部系统」。
