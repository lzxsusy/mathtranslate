# 右 $t$-结构：晶体上的「那个」$t$-结构

> `cdm14/concept/right-t-structure` · 轨道 D · 晶体上的 t-结构 · 状态 dev

> **先自测**：为什么右 $t$-结构比左 $t$-结构更「好用」？

## 一句话

用 $\oblv^r_X$ 把 $\IndCoh(X)$ 的 $t$-结构拉回，定义 $\Crys^r(X)$ 的右 $t$-结构；$\ind^r$ 与 $i_{\mathrm{dR},*}$ 都是 $t$-正合的。

## 定义

对 DG 概形 $X$，定义 $\Crys^r(X)^{\ge0}:=\{\mathcal M\mid\oblv^r_X(\mathcal M)\in\IndCoh(X)^{\ge0}\}$，称为（晶体上的）右 $t$-结构。

**记号**：$\Crys^r(X)^{\heartsuit}$ 为其心。

## 要点（为什么需要它）

1. 右 $t$-结构与滤过余极限相容，且是 Zariski 局部的（4.2.3）。
2. 命题 4.2.9：$\ind^r_X$ 是 $t$-正合的——这是右 $t$-结构好用的核心。
3. 命题 4.2.5：闭浸入 $i:X\hookrightarrow Z$ 的左伴随 $i_{\mathrm{dR},*}$ 是 $t$-正合的。
4. 推论 4.2.7：若 $Y_1\to Y_2$ 在既约经典层面是同构，则左右两个 $t$-结构重合。

## 核心公式

$$\Crys^r(X)^{\ge0}:=\{\mathcal M\mid\oblv^r_X(\mathcal M)\in\IndCoh(X)^{\ge0}\}$$

## 定理与证明（或缺口）

### $\ind^r_X$ 的 $t$-正合性（命题 4.2.9）

$\ind^r_X:\IndCoh(X)\to\Crys^r(X)$ 对右 $t$-结构是 $t$-正合的。

> 证明状态：**sketch**。第 3 步「$\ind^r_X$ 右 $t$-正合」原文来自 4.2.8 的伴随性，未单独证明。

出处：`A p.33`

## 常见误解

- 右 $t$-结构的定义用 $\oblv^r$（$\IndCoh$ 侧），不是 $\oblv^l$。
- $\Crys^r(X)^{\heartsuit}$ 不是「$\QCoh(X)^{\heartsuit}$ 加一个连接」，而是 $\IndCoh$ 侧的心。
- 右 $t$-结构只在 $X$ 为 DG 概形/indscheme 时定义，且要 laft。

## 相关卡

[右晶体：$\Crys^r(X)=\IndCoh(X_{\mathrm{dR}})$](../concepts/right-crystal.md) · [左 $t$-结构：把 $\QCoh$ 的 $t$-结构搬到 $\Crys^l$](../concepts/left-t-structure.md) · [命题 4.2.11：$\oblv^r$ 的 $t$-正合性与有界幅度](../derivations/right-t-exact.md) · [$\Crys^r(X)$ 是其心上的导出范畴](../concepts/abelian-heart.md)

## 出处（印刷页）

- A p.31–33（A p.31）

> 说明：A=§4.2 的定义、命题 4.2.5/4.2.9 与推论 4.2.7；最没把握处：命题 4.2.9 第 3 步的「右 t-正合」来源。
