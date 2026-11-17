# BPS 态

> `kw/concept/bps-state` · 轨道 A · 四维物理与对偶 · 状态 dev

> **先自测**：BPS 态是什么，它在整条论证链里起什么作用？

## 一句话

质量等于中心荷模的态（$M=|Z|$），保持部分超对称；其质量受保护，因此 BPS 谱是检验 S-对偶、确定超荷相因子的精确工具。

## 定义

BPS 态是满足 $M=|Z|$ 的粒子态，其中 $Z$ 是超代数中心荷。这类态保持部分超对称，质量不受量子修正，故其谱可作为对偶两边的精确比较对象。

**记号**：$Z$ 中心荷；$(n,m)$ 电/磁荷；$\tilde\varphi$ Coulomb 分支标量；$M$ 质量。

## 要点（为什么需要它）

1. 它是 S-对偶唯一可精确检验的量子数据：对偶两边的 BPS 谱必须一致。
2. 中心荷 $Z$ 是 $\tau,\tilde\varphi$ 与电荷的函数，BPS 质量公式把 $\mathrm{SL}(2,\mathbb Z)$ 的算术作用变成可测的质量谱。
3. 在扭化理论中，BPS 型方程（如 (3.29)）的解正是构造拓扑不变量与线算子的基本对象。
4. 保持部分超对称使多重态变短，这正是质量受保护的原因。

## 核心公式

$$
$$\{Q^i_{\dot A},Q^j_{\dot B}\}=\epsilon_{\dot A\dot B}\epsilon^{ij}Z$$$$Z=\sqrt{\frac{2}{\operatorname{Im}\tau}}\,\tilde\varphi\cdot(\tilde n+\tau\tilde m),\qquad M=|Z|$$
$$

$$
$$Z=\sqrt{\frac{2}{\operatorname{Im}\tau}}\,\tilde\varphi\cdot(\tilde n+\tau\tilde m),\qquad M=|Z|$$
$$

## 定理与证明（或缺口）

### BPS 质量公式

BPS 态的质量由中心荷给出 $M=|Z|$，其中 $Z=\sqrt{2/\operatorname{Im}\tau}\,\tilde\varphi\cdot(\tilde n+\tau\tilde m)$。

> 证明状态：**gap**。原文 p.14–15 只说『examining the mass formula for BPS states』并给出 (2.18)(2.22)，未推导 $M=|Z|$ 本身（这是 BPS 定义的标准内容）。

出处：`B p.15 eq (2.22)`

### $N=2$ 子代数的中心荷

取一对右旋超荷 $Q^i_{\dot A}$ 的 $N=2$ 子代数，则 $\{Q^i_{\dot A},Q^j_{\dot B}\}=\epsilon_{\dot A\dot B}\epsilon^{ij}Z$，中心荷由电/磁荷与 $\tilde\varphi$ 给出。

> 证明状态：**gap**。原文 p.14 直接写出 (2.18) 并说明其来自中心扩张，未给证明。

出处：`B p.14 eq (2.18)`

## 常见误解

- 把 BPS 条件当成平凡结果：普通态只满足 $M\ge|Z|$，BPS 态要求等号成立。
- 以为 BPS 质量公式对所有态成立：只有 BPS 态的质量被中心荷固定。
- 忽略 $\operatorname{Im}\tau$ 因子：$Z$ 的归一化依赖 $\tau$，S-对偶下 $Z$ 还带相因子 (2.24)。

## 相关卡

[S-对偶](../concepts/s-duality.md) · [电磁对偶](../concepts/electromagnetic-duality.md) · [超荷](../concepts/supercharge.md) · [瞬子](../concepts/instanton.md)

## 出处（印刷页）

- B p.14（B p.14 eq (2.18)）
- B p.15（B p.15 eq (2.22)）

> 说明：A=原文：N=2 子代数 (2.18)、中心荷 (2.22) 与 Coulomb 分支设定（B p.14–15）；C=整理：summary、key_points、pitfalls；$M=|Z|$ 按 BPS 定义整理，原文未展开。
