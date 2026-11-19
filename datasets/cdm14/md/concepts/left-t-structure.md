# 左 $t$-结构：把 $\QCoh$ 的 $t$-结构搬到 $\Crys^l$

> `cdm14/concept/left-t-structure` · 轨道 D · 晶体上的 t-结构 · 状态 dev

> **先自测**：左 $t$-结构为什么是「最自然」的那一个？

## 一句话

$\Crys^l(Y)=\QCoh(Y_{\mathrm{dR}})$ 用 $\QCoh$ 的典范 $t$-结构；$\oblv^l$ 右 $t$-正合。

## 定义

$\QCoh(Z)$ 取典范 $t$-结构（由 $\varphi^*$ 逐点检测，$Z$ 为仿射时即后置凝聚链复形的 $t$-结构）。$\Crys^l(Y)=\QCoh(Y_{\mathrm{dR}})$ 上的左 $t$-结构即该 $t$-结构；$\oblv^l_Y$ 右 $t$-正合。

**记号**：$\Crys^l(Y)^{\le0}$、$\Crys^l(Y)^{\ge0}$。

## 要点（为什么需要它）

1. 定义对任意预栈 $Y$ 都成立，因为 $\QCoh(Y_{\mathrm{dR}})$ 总有典范 $t$-结构。
2. 命题 4.1.3：$Y$ 经典形式光滑时，$\mathcal M\in\Crys^l(Y)^{\le0}\iff\oblv^l_Y(\mathcal M)\in\QCoh(Y)^{\le0}$。
3. 左 $t$-结构与 $\Upsilon$ 的关系不是 $t$-正合的：光滑 $n$ 维时它把 $\le0$ 送到 $\le n$（命题 4.4.2）。
4. 左 $t$-结构对任意 DG 概形都有定义，但它在 $\Crys^r$ 上的对应物（右 $t$-结构）需要用 $\IndCoh$ 定义。

## 核心公式

$$\mathcal M\in\Crys^l(Y)^{\le0}\iff\oblv^l_Y(\mathcal M)\in\QCoh(Y)^{\le0}\quad(Y\text{ 经典形式光滑})$$

## 定理与证明（或缺口）

### 左 $t$-结构由遗忘函子检测（命题 4.1.3）

$Y$ 经典形式光滑时，$\mathcal M\in\Crys^l(Y)^{\le0}$ 当且仅当 $\oblv^l_Y(\mathcal M)\in\QCoh(Y)^{\le0}$。

> 证明状态：**sketch**。第 2 步的「忠实」不是范畴论意义，而是指 $t$-结构的检测；原文用全化逐项验证。

出处：`A p.30`

## 常见误解

- 左 $t$-结构不是「$\Crys^r$ 的右 $t$-结构取负」：两者相差维数平移（命题 4.4.2）。
- $\oblv^l$ 右 $t$-正合只对左 $t$-结构成立；换到右 $t$-结构就不对。

## 相关卡

[左晶体：$\Crys^l(Y)=\QCoh(Y_{\mathrm{dR}})$](../concepts/left-crystal.md) · [右 $t$-结构：晶体上的「那个」$t$-结构](../concepts/right-t-structure.md) · [$\Upsilon$：左晶体与右晶体的比较](../concepts/upsilon-comparison.md)

## 出处（印刷页）

- A p.30–31（A p.30）

> 说明：A=§4.1 定义与命题 4.1.3；最没把握处：命题 4.1.3 反向的下降论证。
