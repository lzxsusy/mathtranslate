# 扭晶体上的两个 $t$-结构

> `cdm14/concept/twisted-t-structure` · 轨道 G · 扭晶体 · 状态 dev

> **先自测**：扭化会不会破坏 $t$-结构？

## 一句话

扭情形同样有左/右两个 $t$-结构；$\ind^{T,r}$ $t$-正合，$\oblv^{T,r}$ 有界，且 $\Crys^{T,r}(X)$ 左完备。

## 定义

$\Crys^{T,l}(Y)$ 取左 $t$-结构（来自 $\QCoh^T$）；$\Crys^{T,r}(X)$ 取右 $t$-结构（来自 $\IndCoh^T$）。

**记号**：$\Crys^{T,r}(X)^{\heartsuit}$ 为扭心。

## 要点（为什么需要它）

1. 命题 7.4.3(a)：$\ind^{T,r}_X$ 是 $t$-正合的；(b) 拟紧 $X$ 时 $\oblv^{T,r}_X$ 有界幅度。
2. 命题 7.4.5：$\Crys^T(X)$ 上左右 $t$-结构相差有界幅度；$\oblv^{T,l}_X$ 有界。
3. 引理 7.4.7：形式完备化上 $\oblv^{T,r}_Y$ 是 $t$-正合的。
4. 命题 7.4.11：右 $t$-结构左完备；$X$ 仿射时 $D(\Crys^{T,r}(X)^\heartsuit)\to\Crys^{T,r}(X)$ 是等价。

## 核心公式

$$\ind^{T,r}_X\ \text{是 }t\text{-正合的},\qquad D\big(\Crys^{T,r}(X)^{\heartsuit}\big)\xrightarrow{\sim}\Crys^{T,r}(X)$$

## 定理与证明（或缺口）

### 扭心上的导出范畴（命题 7.4.11(b)）

$X$ 仿射时，$D(\Crys^{T,r}(X)^{\heartsuit})\to\Crys^{T,r}(X)$ 是等价。

> 证明状态：**sketch**。第 3 步「套用」需要逐条核对假设（左完备、Ext 有界），原文只写「同命题 4.7.3」。

出处：`A p.63`

## 常见误解

- 扭情形不能直接引用非扭命题；有些结论在注 7.3.1 的条件下才成立。
- $\oblv^{T,l}$ 有界，$\oblv^{T,r}$ 只在拟紧时有界——两者不对称。

## 相关卡

[扭晶体：$\Crys^{T,l}$ 与 $\Crys^{T,r}$](../concepts/twisted-crystals.md) · [右 $t$-结构：晶体上的「那个」$t$-结构](../concepts/right-t-structure.md) · [$\Crys^r(X)$ 是其心上的导出范畴](../concepts/abelian-heart.md)

## 出处（印刷页）

- A p.61–64（A p.61）

> 说明：A=§7.4 的命题 7.4.3/7.4.5/7.4.11；最没把握处：第 3 步逐条假设的核对。
