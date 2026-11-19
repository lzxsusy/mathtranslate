# $\Crys^r(X)$ 是其心上的导出范畴

> `cdm14/concept/abelian-heart` · 轨道 D · 晶体上的 t-结构 · 状态 dev

> **先自测**：为什么这个等价对「用 Abel 范畴做同调代数」如此关键？

## 一句话

仿射 DG 概形 $X$ 上，$\Crys^r(X)$ 等价于其 $t$-结构心上的（有界）导出范畴。

## 定义

设 $X$ 仿射 DG 概形。命题 4.7.3：自然函子 $D(\Crys^r(X)^{\heartsuit})\to\Crys^r(X)$ 是等价。

**记号**：$D(-)$ 为 Abel 范畴的导出范畴；$\Crys^r(X)^{\heartsuit}$ 为右 $t$-结构的心。

## 要点（为什么需要它）

1. 先验只有 $D(\mathcal A)^+\to\mathcal C^+$（[Lu2, 定理 1.3.2.2] 的箭头反转），要延拓到全体需要左完备性。
2. 证明分三步：光滑经典（$\ind^r(\mathcal O_X)$ 是紧投射生成元）、一般（闭浸入光滑 $Z$，内射对象）、左完备化（Ext 维数有界）。
3. 推论：$\Crys^r(X)^{\heartsuit}$ 局部 Noether，$\Crys^r(X)$ 有有限上同调维数（注 4.7.8）。
4. 这是 §5.5 把晶体与 D-模在 Abel 层面比较的技术基础。

## 核心公式

$$D\big(\Crys^r(X)^{\heartsuit}\big)\xrightarrow{\sim}\Crys^r(X)$$

## 定理与证明（或缺口）

### 心上的导出范畴（命题 4.7.3）

$X$ 仿射 DG 概形时，$D(\Crys^r(X)^{\heartsuit})\to\Crys^r(X)$ 是等价。

> 证明状态：**sketch**。第 2 步「内射对象」的构造在原文 §4.7.5 只给轮廓，具体取 $I:=i^{\dagger,r}(J)$ 需验证内射性。

出处：`A p.40`

## 常见误解

- 等价是 $D(\heartsuit)\to\Crys^r$，不是 $\Crys^r\to D(\heartsuit)$；方向由 $t$-结构给出。
- 只对仿射 $X$ 陈述；一般 $X$ 需先下降。
- 心的「局部 Noether」是推论，不是定义。

## 相关卡

[右 $t$-结构：晶体上的「那个」$t$-结构](../concepts/right-t-structure.md) · [$\Crys^r(X)$ 的左完备性](../concepts/left-completeness.md) · [晶体与 D-模：经典等价](../concepts/crystals-vs-dmodules.md)

## 出处（印刷页）

- A p.40–41（A p.40）

> 说明：A=命题 4.7.3 与注 4.7.8；最没把握处：第 2 步内射对象的内射性验证。
