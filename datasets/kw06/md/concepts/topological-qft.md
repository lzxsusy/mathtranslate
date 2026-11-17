# 拓扑量子场论

> `kw/concept/topological-qft` · 轨道 B · 扭化与拓扑 · 状态 dev

> **先自测**：拓扑量子场论是什么，它在整条论证链里起什么作用？

## 一句话

只依赖流形光滑结构、不依赖度规的量子场论；存在标量超荷 $Q$ 使 $Q^2=0$ 且 $T_{\mu\nu}=\{Q,b_{\mu\nu}\}$，故配分函数与度规无关。

## 定义

拓扑量子场论是配分函数与关联函数不依赖度规（只依赖时空拓扑或光滑结构）的量子场论。在扭化构造中，这等价于存在标量超荷 $Q$ 满足 $Q^2=0$、能动张量为 $Q$-恰当，从而度规变化在 $Q$-上同调中为零。

**记号**：$Q$ 标量超荷；$b_{\mu\nu}$ 反对称张量；$T_{\mu\nu}$ 能动张量；$M$ 四维流形；$I=I_0+I_1+I_2$。

## 要点（为什么需要它）

1. 它是全文的产物：扭化后的 $\mathcal N=4$ 在每个 $t\in\mathbb{CP}^1$ 给出一个 TQFT，形成以 $\mathbb{CP}^1$ 为参数的 TQFT 族。
2. 因为不依赖度规，理论才能从 $\mathbb R^4$ 搬到任意四维流形，再紧化到曲面 $C$ 并读出 Hitchin 模空间。
3. $T_{\mu\nu}=\{Q,b_{\mu\nu}\}$ 是把『拓扑』变成计算的判据：所有度规依赖都是 $Q$-恰当的。
4. 若没有 TQFT 性质，$\Psi$ 参数与几何 Langlands 的复结构选择都无从定义。

## 核心公式

$$
$$T_{\mu\nu}=\{Q,b_{\mu\nu}\},\qquad Q^2=0$$$$I_2=-\Big(\frac{t-t^{-1}}{e^2(t+t^{-1})}-\frac{\ii\theta}{8\pi^2}\Big)\int_M\mathrm{Tr}\,F\wedge F$$
$$

$$
$$I_2=-\Big(\frac{t-t^{-1}}{e^2(t+t^{-1})}-\frac{\ii\theta}{8\pi^2}\Big)\int_M\mathrm{Tr}\,F\wedge F$$
$$

## 定理与证明（或缺口）

### 扭化作用量给出拓扑场论

扭化后的作用量 $I=I_0+I_1+I_2$ 的度规变化可写成 $\delta_t(\cdots)$（$Q$-恰当），且 $I_2$ 不含度规；故在闭四维流形上无插入的配分函数不依赖度规。

> 证明状态：**sketch**。原文 p.35 只断言『the change in I in a change in the metric is of the form δt(...)』与『I is the action of a topological field theory』，未展开配分函数不变性的证明；以下步骤为我们的整理。

出处：`B p.35 eq (3.49)`

### 配分函数与 $t$ 无关

闭四维流形上无插入的配分函数等于带符号的解数，随 $t$ 连续变形不变；由全纯性对复 $t$ 也成立。

> 证明状态：**sketch**。原文 p.27 说明这是上同调场论的普遍性质并说『by holomorphy』，未给完整证明。

出处：`B p.27`

## 常见误解

- 把『拓扑场论』理解为完全不含度规：度规仍出现在中间步骤，只是其变化是 $Q$-恰当的。
- 以为所有 $t$ 给出同一个二维理论：$t=\pm\ii$ 对应 B-模型型、实 $t$ 对应 A-模型型，复结构不同。
- 忘记扭化破坏幺正性：此类 TQFT 只在欧氏号差下有意义。

## 相关卡

[拓扑扭化](../concepts/topological-twist.md) · [BRST 算子](../concepts/brst-operator.md) · [上同调](../concepts/cohomology.md) · [二维理论：B-模型、A-模型与不变量 q](../derivations/two-d-theories.md)

## 出处（印刷页）

- B p.16（B p.16）
- B p.27（B p.27）
- B p.35（B p.35 eq (3.49)）

> 说明：A=原文：§3 引言、上同调场论 (p.27)、$I_0/I_1/I_2$ 与 (3.49)（B p.16–35）；C=整理：summary、key_points、pitfalls 与第一条定理的三步骨架（原文只作断言）。
