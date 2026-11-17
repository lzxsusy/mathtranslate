# $\theta$ 角

> `kw/concept/theta-angle` · 轨道 A · 四维物理与对偶 · 状态 dev

> **先自测**：$\theta$ 角是什么，它在整条论证链里起什么作用？

## 一句话

规范理论中 $\int\mathrm{Tr}\,F\wedge F$ 拓扑项的系数，以 $2\pi$ 为周期；它与 $1/e^2$ 组成复耦合 $\tau$，$T:\tau\mapsto\tau+1$ 就是把 $\theta$ 平移 $2\pi$。

## 定义

$\theta$ 角是四维规范理论作用量中拓扑项 $I_\theta=-\frac{\theta}{8\pi^2}\int\mathrm{Tr}\,F\wedge F$ 的系数。由于该积分是整值的第二陈数（瞬子数），$\theta$ 是周期为 $2\pi$ 的角变量。

**记号**：$\theta\sim\theta+2\pi$；$\tau=\theta/2\pi+4\pi\ii/e^2$；$k=\frac1{8\pi^2}\int\mathrm{Tr}\,F\wedge F\in\mathbb Z$。

## 要点（为什么需要它）

1. 只有把 $\theta$ 与 $e$ 合成 $\tau$，$\tau\to-1/\tau$ 才有意义，S-对偶才是 $\mathrm{SL}(2,\mathbb Z)$ 作用。
2. 它给瞬子数加权：路径积分按 $e^{\ii\theta k}$ 叠加各拓扑扇区，这是 $\theta$ 真空的物理来源。
3. 在扭化作用量中 $\theta$ 与 $t$ 组合成规范参数 $\Psi$，决定二维理论的复结构。
4. $T$ 变换是经典对称，为整个对偶群 $\Gamma$ 提供生成元。

## 核心公式

$$
$$I_\theta=-\frac{\theta}{8\pi^2}\int_M\mathrm{Tr}\,F\wedge F,\qquad \theta\sim\theta+2\pi$$$$\tau=\frac{\theta}{2\pi}+\frac{4\pi\ii}{e^2}\in\mathbb H$$
$$

$$
$$\tau=\frac{\theta}{2\pi}+\frac{4\pi\ii}{e^2}\in\mathbb H$$
$$

## 定理与证明（或缺口）

### $\theta$ 的 $2\pi$ 周期性

在 $\mathbb R^4$ 或 $H^2(M,\mathbb Z)=0$ 的四维流形上，$\theta$ 与 $\theta+2\pi$ 描述同一量子理论。

1. $\theta$ 项等于 $\theta$ 乘第二陈数 $k=\frac1{8\pi^2}\int\mathrm{Tr}\,F\wedge F$，而 $k$ 是整数。
   - *为什么*：原文 p.10 指出该积分整值，故拓扑项只以整数倍出现。
2. 量子理论只依赖作用量模 $2\pi$ 的整数倍，故 $\theta\mapsto\theta+2\pi$ 不改变 $e^{\ii I}$。
   - *为什么*：原文 p.10 明说 in quantum mechanics one only cares about the action modulo an integer multiple of 2π。

出处：`B p.10 eq (2.12)`

### $\tau$ 落在上半平面

$\tau=\theta/2\pi+4\pi\ii/e^2$ 的虚部为正，故 $\tau\in\mathbb H$，$\mathrm{SL}(2,\mathbb R)$ 通过分式线性变换作用其上。

> 证明状态：**gap**。原文 p.11 直接用『its imaginary part is positive』一句带过，未给证明。

出处：`B p.11`

## 常见误解

- 把 $\theta$ 当成普通耦合常数：它周期为 $2\pi$，只在拓扑项中出现，不是连续可调的相互作用强度。
- 以为 $\theta$ 不影响物理：在 $\theta$ 真空、瞬子求和以及扭化后的 $\Psi$ 参数中它都是实质的。
- 忽略 $H^2(M,\mathbb Z)=0$ 条件：原文 p.10 指出流形的一般化要考虑 $\pi_1(G)$，不能无条件使用 $2\pi$ 周期性。

## 相关卡

[S-对偶](../concepts/s-duality.md) · [瞬子](../concepts/instanton.md) · [$\mathcal N=4$ 超对称杨–米尔斯理论](../concepts/n4-sym-theory.md) · [典范参数 Ψ：定义、S 作用与消去 t](../derivations/canonical-parameter.md)

## 出处（印刷页）

- B p.9（B p.9 eq (2.11)）
- B p.10（B p.10 eq (2.12)）

> 说明：A=原文：拓扑项 (2.11)、$2\pi$ 周期性与 $\tau$ 定义 (2.12)（B p.9–11）；C=整理：summary、key_points、pitfalls；第一条定理的 status=complete 是因为原文 p.10 明写了两步论证（整值陈数、作用量模 $2\pi$）。
