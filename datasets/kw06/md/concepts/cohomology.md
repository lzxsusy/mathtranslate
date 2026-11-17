# 上同调

> `kw/concept/cohomology` · 轨道 B · 扭化与拓扑 · 状态 dev

> **先自测**：上同调是什么，它在整条论证链里起什么作用？

## 一句话

$Q$-闭模 $Q$-恰当得到的商空间；扭化理论的物理态与算子就是 $Q$ 的上同调类，$Q$-恰当的量视为零。

## 定义

这里的上同调指幂零算子 $Q$ 的上同调 $H_Q=\ker Q/\operatorname{im}Q$。拓扑扭化规定物理态与可观测算子取 $Q$-上同调类，任何形如 $[Q,\mathcal O]$ 的项都视为零。

**记号**：$Q$ 标量超荷；$H_Q$；$\mathcal O$ 任意算子。

## 要点（为什么需要它）

1. 它把无穷维场论问题化为代数问题：只需看 $Q$-上同调类，度规与 $t$ 依赖都被模掉。
2. 线算子、膜算子与 Hecke 特征层的物理对应都要在 $Q$-上同调中表述。
3. $Q^2=0$ 是上同调有定义的前提，这解释了为什么必须扭化出标量超荷。
4. 不同 $t$ 下的上同调族由规范参数 $\Psi$ 标记，$\Psi$ 因此成为几何 Langlands 的坐标。

## 核心公式

$$
$$H_Q=\ker Q\,/\,\operatorname{im}Q,\qquad Q^2=0$$$$[Q,\mathcal O]\sim0\quad(\text{在 }H_Q\text{ 中})$$
$$

$$
$$[Q,\mathcal O]\sim0\quad(\text{在 }H_Q\text{ 中})$$
$$

## 定理与证明（或缺口）

### 物理态与算子取 $Q$-上同调

扭化理论中只考虑 $Q$-不变的路径积分、算子与态，并把 $[Q,\mathcal O]$ 视为零；可观测对象于是是 $Q$ 的上同调类。

> 证明状态：**gap**。原文 p.18 只作这一规定（『the interesting operators or states lie in suitable cohomology groups of Q』），未给证明；这是拓扑场论的标准构造。

出处：`B p.18`

### $Q$-上同调与上同调场论

对实 $t$，理论属于上同调场论（如 Donaldson 理论、二维 A-模型），配分函数可化为带符号的解数计数。

> 证明状态：**gap**。原文 p.27 把这作为『general framework of cohomological field theories』的普遍性质陈述并引 [59]，未给推导。

出处：`B p.27`

## 常见误解

- 把这里的上同调等同 de Rham 上同调：$Q$ 是奇超荷，不是外微分。
- 以为所有 $Q$-闭算子都可观测：模去 $Q$-恰当项后的类才有意义。
- 忽略 $Q$ 与 $t$ 的依赖：不同扭化参数给出不同的 $Q$ 与不同的上同调。

## 相关卡

[BRST 算子](../concepts/brst-operator.md) · [拓扑量子场论](../concepts/topological-qft.md) · [拓扑扭化](../concepts/topological-twist.md) · [c.c. A-膜、开弦代数与 A-膜→D-模](../derivations/a-to-dmod.md)

## 出处（印刷页）

- B p.18（B p.18）
- B p.27（B p.27）

> 说明：A=原文：Q-上同调的规定 (p.18)、上同调场论 (p.27)；C=整理：summary、key_points、pitfalls；定义中的同调代数为标准数学表述，原文只给物理规定。
