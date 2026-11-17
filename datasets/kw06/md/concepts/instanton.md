# 瞬子

> `kw/concept/instanton` · 轨道 B · 扭化与拓扑 · 状态 dev

> **先自测**：瞬子是什么，它在整条论证链里起什么作用？

## 一句话

四维欧氏规范场的有限作用量经典解，以第二陈数 $k=\frac1{8\pi^2}\int\mathrm{Tr}\,F\wedge F$ 分类；$k\ne0$ 时扭化方程在 $t\ne0,\infty$ 无解，瞬子只在退化极限出现。

## 定义

瞬子是四维欧氏空间或流形上满足自对偶方程 $F=\pm\ast F$ 的有限作用量规范场构型，其拓扑荷是第二陈数 $k=\frac1{8\pi^2}\int\mathrm{Tr}\,F\wedge F$。本文中 $\theta$ 项以 $k$ 加权，而扭化方程的解只在 $t=0$ 或 $\infty$ 的退化极限允许 $k\ne0$。

**记号**：$k\in\mathbb Z$；$t$ 扭化参数；$V_\pm(t)$、$V_0$ 为 (3.29) 左端；$B(t)$ 为 (3.33) 左端。

## 要点（为什么需要它）

1. 它给 $\theta$ 角物理意义：路径积分按 $e^{\ii\theta k}$ 加权不同瞬子扇区，$\theta$ 的 $2\pi$ 周期由此而来。
2. 消失定理说明 $t\ne0,\infty$ 时解空间不受瞬子数影响，这是配分函数 $t$ 无关性的关键。
3. $t=0,\infty$ 对应瞬子/反瞬子极限，是 A-模型与 B-模型分界的几何线索。
4. 瞬子数也是四维拓扑荷，与 't Hooft 线的磁荷及单极子冒泡密切相关。

## 核心公式

$$
$$k=\frac1{8\pi^2}\int_M\mathrm{Tr}\,F\wedge F\in\mathbb Z$$$$\int_M\mathrm{Tr}\,F\wedge F=\int_M\mathrm{Tr}\big[V_+(t)\wedge V_+(-t^{-1})+V_-(t)\wedge V_-(-t^{-1})\big]$$
$$

$$
$$\int_M\mathrm{Tr}\,F\wedge F=\int_M\mathrm{Tr}\big[V_+(t)\wedge V_+(-t^{-1})+V_-(t)\wedge V_-(-t^{-1})\big]$$
$$

## 定理与证明（或缺口）

### 消失定理 1

设 $M$ 紧致无边、$E$ 为 $G$-丛且 $\int_M\mathrm{Tr}\,F\wedge F\ne0$，则对任意 $t\ne0,\infty$，方程 $V_+(t)=V_-(t)=V_0=0$ 无解。

1. 使用恒等式 (3.32)：$\int_M\mathrm{Tr}\,F\wedge F=\int_M\mathrm{Tr}[V_+(t)\wedge V_+(-t^{-1})+V_-(t)\wedge V_-(-t^{-1})]$。
   - *为什么*：原文 p.28 说该恒等式由分部积分直接得到，把拓扑荷写成 $V$ 的双线性式。
2. 若 $V_\pm(t)=V_0=0$，则 (3.32) 右端为零，故 $\int_M\mathrm{Tr}\,F\wedge F=0$。
   - *为什么*：直接把 $V=0$ 代入。
3. 这与假设 $\int\mathrm{Tr}\,F\wedge F\ne0$ 矛盾，故无解。
   - *为什么*：反证法。

出处：`B p.28 eq (3.32)`

### 消失定理 1$'$

若 $\int_M\mathrm{Tr}\,F\wedge F>0$，则方程除 $t=0$ 外无解；若 $<0$，则除 $t=\infty$ 外无解。

1. 若 $V_\pm(t)=V_0=0$，则 $B(t)=0$（$B$ 为 (3.33) 左端）。
   - *为什么*：原文 p.30 用 $B$ 的定义与第一恒等式。
2. $B$ 是正系数平方和，半正定；由 (3.34) 右端须半正定，迫使 $t$ 为 $f$ 的极小（$\int>0$）或极大（$\int<0$）。
   - *为什么*：原文 p.30 的半正定性论证。
3. $f(t)=(t-t^{-1})/(t+t^{-1})$ 的唯一极小在 $t=0$、唯一极大在 $t=\infty$，故 $t\ne0,\infty$ 无解。
   - *为什么*：$f$ 的单调性；原文 p.30 末句。

出处：`B p.30 eq (3.34)`

## 常见误解

- 把瞬子当成任意拓扑非平凡解：它是有限作用量的经典解，且只在欧氏号的 $F=\pm\ast F$ 方程下定义。
- 以为瞬子数可以随便取：$k$ 是整数，且是 $\theta$ 项的系数，决定了 $2\pi$ 周期性。
- 误以为 $k\ne0$ 时扭化方程总有解：消失定理表明 $t\ne0,\infty$ 时无解，只在退化极限出现。

## 相关卡

[$\theta$ 角](../concepts/theta-angle.md) · [$\mathcal N=4$ 超对称杨–米尔斯理论](../concepts/n4-sym-theory.md) · [Q-不变方程与消失定理](../derivations/vanishing-theorem.md) · [BPS 态](../concepts/bps-state.md)

## 出处（印刷页）

- B p.10（B p.10）
- B p.28（B p.28 eq (3.32)）
- B p.30（B p.30 eq (3.34)）

> 说明：A=原文：瞬子数=第二陈数 (p.10)、定理 1 与恒等式 (3.32) (p.28)、定理 1' 与 (3.34) (p.30)；C=整理：summary、key_points、pitfalls 与两条定理的步骤措辞（原文给了证明骨架，故标 complete）。
