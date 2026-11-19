# de Rham 预栈 $X_{\mathrm{dR}}$

> `cdm14/concept/dr-prestack` · 轨道 A · de Rham 预栈与晶体定义 · 状态 dev

> **先自测**：$X_{\mathrm{dR}}$ 到底丢掉了 $X$ 的什么、又保留了什么？

## 一句话

把测试环先约化成既约经典环、再取 $X$ 的预栈；它记的是 $X$ 的「无穷小邻域」信息。

## 定义

对 $Y\in\PreStk$，定义 $Y_{\mathrm{dR}}(S):=Y({}^{\mathrm{cl,red}}S)$，其中 ${}^{\mathrm{cl,red}}S=\mathrm{red}(\pi_0(S))$ 是 $S$ 的既约经典化。等价地，$Y_{\mathrm{dR}}$ 是 ${}^{\mathrm{cl,red}}Y$ 沿 $\mathrm{redSch}_{\mathrm{aff}}\hookrightarrow \DGSch_{\mathrm{aff}}$ 的右 Kan 延拓。

**记号**：$\mathrm{dR}:\PreStk\to\PreStk$；$p_{\mathrm{dR},Y}:Y\to Y_{\mathrm{dR}}$。

## 要点（为什么需要它）

1. 定义只依赖 $\pi_0$ 的既约化，所以 $Y_{\mathrm{dR}}$ 看不见幂零元与高阶同伦群——这正是「无穷小」的含义。
2. 函子 $\mathrm{dR}$ 与极限、余极限都交换（引理 1.1.4），因此可以逐对象地算。
3. 对 $Y\in\PreStk_{\mathrm{laft}}$，$Y_{\mathrm{dR}}$ 仍在 $\PreStk_{\mathrm{laft}}$ 中，而且是经典的（命题 1.3.3）。
4. $p_{\mathrm{dR},Y}$ 的 Čech 神经每项 $Y_i/Y_{\mathrm{dR}}$ 是 $Y_i$ 沿主对角线的形式完备化（1.2.2）。

## 核心公式

$$Y_{\mathrm{dR}}(S)=Y({}^{\mathrm{cl,red}}S),\qquad {}^{\mathrm{cl,red}}S=\mathrm{red}(\pi_0(S))$$

## 定理与证明（或缺口）

### $\mathrm{dR}$ 保极限与余极限（引理 1.1.4）

函子 $\mathrm{dR}:\PreStk\to\PreStk$ 与极限、余极限交换。

1. $\PreStk=\mathrm{Funct}((\DGSch_{\mathrm{aff}})^{\mathrm{op}},\infty\text{-}\Grpd)$ 中的极限与余极限逐对象计算。
   - *为什么*：函子范畴的极限逐对象给出。
2. 每个对象上 $Y\mapsto Y({}^{\mathrm{cl,red}}S)$ 只是把 $S$ 换成 ${}^{\mathrm{cl,red}}S$ 再取值，逐对象复合保极限与余极限。
   - *为什么*：${}^{\mathrm{cl,red}}$ 是逐对象的环运算。

出处：`A p.12`

## 常见误解

- $Y_{\mathrm{dR}}$ 不是 $Y$ 的形式完备化；它是「对所有测试对象先约化」的预栈，形式完备化只出现在 Čech 神经的每一项上。
- 定义里先取 $\pi_0$ 再约化，顺序不能反：$\mathrm{red}(\pi_0(S))$ 丢掉高阶同伦群。

## 相关卡

[经典形式光滑的预栈](../concepts/classically-formally-smooth.md) · [局部几乎有限型（laft）与 $Y_{\mathrm{dR}}$ 的正性](../concepts/laft-and-dr.md) · [dR 与极限交换、左 Kan 延拓表述](../derivations/dr-kan.md)

## 出处（印刷页）

- A p.12–13（A p.12）

> 说明：A=§1.1 定义与引理 1.1.4；最没把握处：右 Kan 延拓表述与逐对象定义等价的细节。
