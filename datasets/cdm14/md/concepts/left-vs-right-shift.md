# 左右 $t$-结构相差一个维数平移

> `cdm14/concept/left-vs-right-shift` · 轨道 D · 晶体上的 t-结构 · 状态 dev

> **先自测**：同一个范畴上的两个 $t$-结构，为什么恰好差维数？

## 一句话

光滑 $n$ 维时，$\Crys^l$ 的左 $t$-结构与 $\Crys^r$ 的右 $t$-结构相差 $[-n]$；一般拟紧情形差有界幅度。

## 定义

设 $X$ 光滑经典 $n$ 维。命题 4.4.2：$\mathcal F\in\Crys^l(X)^{\le0}\iff\mathcal F\in\Crys^r(X)^{\le -n}$。

**记号**：$\mathcal F$ 同时视为左右晶体（$\Upsilon$ 等价）。

## 要点（为什么需要它）

1. $\Upsilon_X$ 是 $\otimes\omega_X$，光滑 $n$ 维时 $\omega_X=\Omega^n_X$ 是线丛，故把 $\QCoh^{\le0}$ 送到 $\IndCoh^{\le -n}$。
2. 命题 4.4.4：拟紧 $X$ 上 $\mathrm{id}:\Crys^l(X)\to\Crys^r(X)$ 有有界上同调幅度（界依赖 $X$ 的嵌入维数）。
3. 推论 4.2.7：若 $Y_1\to Y_2$ 在既约经典层面同构，则两个 $t$-结构重合——平移消失。
4. 这个平移是「左 D-模 vs 右 D-模」在导出层面的影子：右 D-模对应 perverse $t$-结构。

## 核心公式

$$\mathcal F\in\Crys^l(X)^{\le0}\iff\mathcal F\in\Crys^r(X)^{\le -n}\qquad(\dim X=n\text{ 光滑})$$

## 定理与证明（或缺口）

### 维数平移（命题 4.4.2）

$X$ 光滑经典 $n$ 维时，左 $t$-结构与右 $t$-结构满足 $\Crys^l(X)^{\le0}=\Crys^r(X)^{\le -n}$。

> 证明状态：**sketch**。第 2 步「张量可逆层平移 $n$」原文只用一句「显然」，未展开 $\IndCoh$ 的 $t$-结构与 $\otimes\omega$ 的交互。

出处：`A p.35`

## 常见误解

- 平移是 $-n$ 不是 $+n$：$\omega_X$ 提高度数。
- 只在光滑时是干净的平移；奇异时只有有界幅度（命题 4.4.4）。

## 相关卡

[左 $t$-结构：把 $\QCoh$ 的 $t$-结构搬到 $\Crys^l$](../concepts/left-t-structure.md) · [右 $t$-结构：晶体上的「那个」$t$-结构](../concepts/right-t-structure.md) · [$\Upsilon$：左晶体与右晶体的比较](../concepts/upsilon-comparison.md)

## 出处（印刷页）

- A p.35–37（A p.35）

> 说明：A=命题 4.4.2 与 4.4.4；最没把握处：第 2 步「张量可逆层平移」的符号。
