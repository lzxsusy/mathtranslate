# 对偶环面纤维化与 T-对偶

> `gtgl15/concept/dual-torus-fibration` · 轨道 B · 对偶环面与 T-对偶 · 状态 dev

> **先自测**：为什么 4d 规范理论的 S-对偶在 Hitchin 系统里变成环面纤维的 T-对偶？

## 一句话

$\MH$ 的每个 Hitchin 纤维是复环面 $F$，其对偶环面 $F'$ 给出镜像一侧的纤维化；4d $\mathcal N=4$ 的 S-对偶表现为纤维上的 T-对偶加底空间对称。

## 定义

设 $\pi:\MH\to\mathcal V$ 的纤维为复环面 $F_\lambda$。对偶纤维 $F'_\lambda$ 由 $F_\lambda$ 的 flat $U(1)$ 特征标组成：$F'=\mathrm{Hom}(F,U(1))$ 或等价的 $\mathbb C^{r*}/\Lambda^*$。$F$ 与 $F'$ 之间存在 Poincaré 线丛 $\mathcal T\to F\times F'$，限制在每个 $F\times\{f'\}$ 上是平坦线丛。S-对偶把带耦合常数 $\tau$ 的理论送到 $1/\tau$ 的理论，在纤维上正是 $F\leftrightarrow F'$ 的 T-对偶，底空间 $\mathcal V$ 只作几何对称。这与 SYZ 镜像对称的陈述一致。

**记号**：$F,F'$；Poincaré 线丛 $\mathcal T$；$\Lambda,\Lambda^*$；distinguished point。

## 要点（为什么需要它）

1. 对偶环面 $F'$ 是 $F$ 的特征标环面；它不是 $F$ 本身，尺寸互换（半径 $R\leftrightarrow 1/R$）。
2. 对偶对 $(F,F')$ 由 Poincaré 线丛确定，且 $F\times F'$ 有唯一的 distinguished point（$\mathcal T$ 在其上平凡），这给复环面自然的阿贝尔簇结构。
3. S-对偶 = Hitchin 纤维上的 T-对偶 + 底 $\mathcal V$ 的几何对称（对 $SU(N)/PSU(N)$ 底空间相同）。
4. 对偶环面纤维化的“度规”由 $\Omega_I$ 与耦合常数 $\tau$ 决定：$\mathrm{Im}\,\tau$ 控制纤维的 Kähler 大小（$\S3.4$）。
5. U(1) 情形：$\mathrm{Jac}(C)$ 自对偶，对应 2d 环面 T-对偶的经典例子（$\S3.1$）。

## 核心公式

$$
$$F_\lambda=\mathbb C^r/\Lambda,\qquad F'_\lambda=\mathbb C^{r*}/\Lambda^{*},\qquad \mathcal T\to F\times F'$$$$\tau\leftrightarrow-\frac{1}{\tau}\ \ \text{(S-对偶)}\ \Longleftrightarrow\ \ F\leftrightarrow F'\ \ \text{(T-对偶)}$$
$$

$$
$$\tau\leftrightarrow-\frac{1}{\tau}\ \ \text{(S-对偶)}\ \Longleftrightarrow\ \ F\leftrightarrow F'\ \ \text{(T-对偶)}$$
$$

## 定理与证明（或缺口）

### S-对偶的 T-对偶解释

$SU(N)$ 与 $PSU(N)$ 的 $\mathcal N=4$ 理论 S-对偶，对应 Hitchin 纤维 $F_{SU(N)}$ 与 $F^{(0)}_{PSU(N)}$ 的对偶环面。

> 证明状态：**sketch**。原文把“S-对偶 = T-对偶”作为指导思想而非定理证明；逐纤维的数学陈述由 $\S3.2$–$\S3.3$ 支撑。

出处：`A p.25`

## 常见误解

- 对偶环面的复结构不是原环面复结构的简单共轭：它由 $\Omega_I$ 与 $\tau$ 共同决定。
- $\mathcal V$ 不参与对偶变换（对同底的对偶对）；把底空间也换掉是最常见的误读。
- distinguished point 依赖公理化的选择（Poincaré 线丛的平凡点），不是每个环面都天然有的。
- $U(N)$ 自对偶，$SU(N)$ 与 $PSU(N)$ 互换；不要写成 $SU(N)\leftrightarrow SU(N)$。

## 相关卡

[希钦纤维化](../concepts/hitchin-fibration.md) · [阿贝尔化与 Prym 簇](../concepts/abelianization-prym.md) · ['t Hooft flux 与 $PSU(N)$ 分量](../concepts/thooft-flux-psu.md) · [辛形式 $\Omega_I$ 与耦合常数](../concepts/symplectic-form.md) · [辛形式的周期匹配与 $S$-对偶 $=$ $T$-对偶](../derivations/symplectic-period-matching.md)

## 出处（印刷页）

- A p.22–23（A p.22）
- A p.23–25（A p.24 eq (3.2)）
- A p.25–26（A p.26 eq (3.6)）

> 说明：A=原文 §3 开篇的对偶环面定义、$\S3.1$ 的圆周/格例子、$\S3.2$ 的 $SU/PSU$ 对偶；B=把 S-对偶=T-对偶的指导思想拆成逐纤维陈述；C=SYZ 镜像的语言按标准背景补。最没把握处：distinguished point 与复结构的相容性原文只在 §3 开头一段带过。
