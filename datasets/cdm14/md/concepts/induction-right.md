# 右晶体的归纳函子 $\ind^r_X$

> `cdm14/concept/induction-right` · 轨道 C · 下降性质与归纳函子 · 状态 dev

> **先自测**：为什么 $\Crys^r(X)$ 的紧对象可以由 $\Coh(X)$ 生成？

## 一句话

$\oblv^r_X$ 有左伴随 $\ind^r_X:\IndCoh(X)\to\Crys^r(X)$，它把 $\IndCoh(X)$ 张成 $\Crys^r(X)$，并给出单子性。

## 定义

$p_s,p_t:X\times_{X_{\mathrm{dR}}}X\to X$ 都是 ind-固有的，故 $p_i^!$ 有左伴随 $(p_i)_*^{\IndCoh}$。定义 $\ind^r_X:\IndCoh(X)\to\Crys^r(X)$ 为 $\oblv^r_X$ 的左伴随。

**记号**：$\oblv^r_X\circ\ind^r_X\simeq(p_t)_*^{\IndCoh}\circ p_s^!$（命题 3.3.2(b)）。

## 要点（为什么需要它）

1. 命题 3.3.2(a)：$\oblv^r_X$ 有左伴随 $\ind^r_X$；这是「晶体由 $\IndCoh(X)$ 归纳而来」的精确含义。
2. 命题 3.3.2(b)：$\oblv^r_X\circ\ind^r_X\simeq(p_t)_*^{\IndCoh}\circ p_s^!$，即归纳后再遗忘 = 沿群胚传递再推回。
3. 命题 3.3.2(c)：$(\ind^r_X,\oblv^r_X)$ 是单子的：$\Crys^r(X)$ 等价于 $\IndCoh(X)$ 上该单子的模。
4. 推论 3.3.3：$\Crys^r(X)$ 紧生成，生成元为 $\ind^r_X(\Coh(X))$。

## 核心公式

$$\ind^r_X\;\dashv\;\oblv^r_X,\qquad \oblv^r_X\circ\ind^r_X\simeq(p_t)_*^{\IndCoh}\circ p_s^!$$

## 定理与证明（或缺口）

### 单子性（命题 3.3.2(c)）

伴随对 $(\ind^r_X,\oblv^r_X)$ 是单子的；$\Crys^r(X)$ 等价于 $\IndCoh(X)$ 上单子 $\oblv^r_X\circ\ind^r_X$ 的模范畴。

> 证明状态：**sketch**。第 2 步的 Beck–Chevalley 验证在原文中占一整段，这里只记其用到的两个引理。

出处：`A p.28`

## 常见误解

- $\ind^r_X$ 不是「取常层」：它把 $\IndCoh(X)$ 的对象沿 $p_s^!$ 推到群胚上再推回。
- 单子性用的是 $\oblv^r$ 保守，而不是 $\oblv^l$；两者不可替换。
- $\ind^r_X$ 只在 $X$ 为 DG 概形/indscheme 时定义，$X$ 为一般预栈时要先化到仿射。

## 相关卡

[右晶体：$\Crys^r(X)=\IndCoh(X_{\mathrm{dR}})$](../concepts/right-crystal.md) · [无穷小群胚 $X\times_{X_{\mathrm{dR}}}X\rightrightarrows X$](../concepts/infinitesimal-groupoid.md) · [命题 3.3.2 的证明：全化 + Barr–Beck–Lurie](../derivations/right-induction.md) · [粗糙归纳与 Gorenstein 条件](../concepts/coarse-induction.md)

## 出处（印刷页）

- A p.28–29（A p.28）

> 说明：A=§3.3 的命题 3.3.2 与推论 3.3.3；最没把握处：单子性证明中 Beck–Chevalley 的具体交换图。
