# $\Crys^r(X)$ 的左完备性

> `cdm14/concept/left-completeness` · 轨道 D · 晶体上的 t-结构 · 状态 dev

> **先自测**：左完备性为什么对导出范畴的「取极限」论证是必需的？

## 一句话

右 $t$-结构下 $\Crys^r(X)$ 左完备；拟紧时 $\Crys(X)$ 在左 $t$-结构下也左完备。

## 定义

$t$-结构左完备指 $\bigcap_n\mathcal C^{\le -n}=0$ 且 $\mathcal C\to\lim_n\mathcal C^{\le n}$ 是等价。

**记号**：$\Crys^r(X)$ 取右 $t$-结构；$\Crys(X)$ 取左 $t$-结构。

## 要点（为什么需要它）

1. 推论 4.5.2：$X$ 光滑经典仿射时 $\ind^r_X(\mathcal O_X)$ 是紧投射生成元，故左完备。
2. 推论 4.5.4：任意 DG 概形 $X$，$\Crys^r(X)$ 在右 $t$-结构下左完备（Zariski 局部 + 闭浸入光滑 $Z$）。
3. 推论 4.5.7：拟紧 $X$ 时 $\Crys(X)$ 在左 $t$-结构下也左完备。
4. 左完备性是命题 4.7.3（导出范畴 = 心上的导出范畴）的前提之一。

## 核心公式

$$\Crys^r(X)\xrightarrow{\sim}\lim_n\tau^{\le n}\Crys^r(X)$$

## 定理与证明（或缺口）

### 右 $t$-结构左完备（推论 4.5.4）

任意 DG 概形 $X$，$\Crys^r(X)$ 在其右 $t$-结构下左完备。

> 证明状态：**sketch**。第 2 步「反射左完备性」需要 $i_{\mathrm{dR},*}$ 保极限，原文只用一句话带过。

出处：`A p.37`

## 常见误解

- 左完备 ≠ 右完备：右完备自动成立（注 4.5.5），左完备需要证明。
- 不同 $t$-结构下的左完备性不能混用：$\Crys(X)$ 用左 $t$-结构，$\Crys^r(X)$ 用右 $t$-结构。

## 相关卡

[右 $t$-结构：晶体上的「那个」$t$-结构](../concepts/right-t-structure.md) · [$\Crys^r(X)$ 是其心上的导出范畴](../concepts/abelian-heart.md) · [粗糙归纳与 Gorenstein 条件](../concepts/coarse-induction.md)

## 出处（印刷页）

- A p.37–38（A p.37）

> 说明：A=§4.5 的推论 4.5.2/4.5.4/4.5.7；最没把握处：第 2 步「反射」的细节。
