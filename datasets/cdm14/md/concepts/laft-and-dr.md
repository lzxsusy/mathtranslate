# 局部几乎有限型（laft）与 $Y_{\mathrm{dR}}$ 的正性

> `cdm14/concept/laft-and-dr` · 轨道 A · de Rham 预栈与晶体定义 · 状态 dev

> **先自测**：为什么全书从 §2.2 起都假设 laft？

## 一句话

$\PreStk_{\mathrm{laft}}$ 是收敛、且各截断局部有限型的预栈；$\mathrm{dR}$ 把它留在其中并变成经典的。

## 定义

$Y\in\PreStk$ 属于 $\PreStk_{\mathrm{laft}}$，若 (i) $Y$ 收敛：$\Maps(S,Y)\simeq\lim_n\Maps({}^{\le n}S,Y)$；(ii) 每个截断 ${}^{\le n}Y$ 局部有限型：$S\mapsto\Maps(S,Y)$ 在 ${}^{\le n}\DGSch_{\mathrm{aff}}$ 上保滤过余极限。

**记号**：${}^{\le n}S$ 为 $n$-截断；${}^{\le n}\DGSch_{\mathrm{aff,ft}}$ 为有限型子范畴。

## 要点（为什么需要它）

1. laft = 收敛 + 逐截断有限型，是「由有限型仿射概形逼近」的技术条件。
2. 命题 1.3.3：$Y\in\PreStk_{\mathrm{laft}}\Rightarrow Y_{\mathrm{dR}}\in\PreStk_{\mathrm{laft}}$ 且 $Y_{\mathrm{dR}}$ 经典。
3. 正性 (b) 是关键：它让 $\QCoh(Y_{\mathrm{dR}})$ 与 $\IndCoh(Y_{\mathrm{dR}})$ 可用经典概形逼近，从而 $\Crys$ 有良好的 $t$-结构。
4. 该假设在 §6 被去掉（扭化对任意预栈定义），§7.2 起在扭情形恢复。

## 核心公式

$$\Maps(S,Y)\xrightarrow{\sim}\lim_{n\ge0}\Maps({}^{\le n}S,Y)$$

## 定理与证明（或缺口）

### $\mathrm{dR}$ 保持 laft（命题 1.3.3）

$Y\in\PreStk_{\mathrm{laft}}$ 时 $Y_{\mathrm{dR}}\in\PreStk_{\mathrm{laft}}$，且 $Y_{\mathrm{dR}}$ 是经典预栈。

> 证明状态：**sketch**。第 3 步引用 [GR1, 命题 6.8.2] 判断余极限的经典性，本文未复述其条件。

出处：`A p.14`

## 常见误解

- laft 不是「有限型」：它允许无穷维的预栈，只要被有限型截断逼近。
- 去掉 laft 后命题 1.3.3(b) 失效，$Y_{\mathrm{dR}}$ 可能非经典——这是 §3.4 反例的来源之一。

## 相关卡

[de Rham 预栈 $X_{\mathrm{dR}}$](../concepts/dr-prestack.md) · [左晶体：$\Crys^l(Y)=\QCoh(Y_{\mathrm{dR}})$](../concepts/left-crystal.md) · [dR 与极限交换、左 Kan 延拓表述](../derivations/dr-kan.md)

## 出处（印刷页）

- A p.14–15（A p.14）

> 说明：A=1.3.1 定义与命题 1.3.3；最没把握处：命题 1.3.3(a) 第二步的滤过极限论证细节。
