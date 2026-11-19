# 辛形式的周期匹配与 $S$-对偶 $=$ $T$-对偶

> `gtgl15/deriv/symplectic-period-matching` · 轨道 B · 对偶环面与 T-对偶 · 状态 dev · 4 步

> **要回答的问题**：怎样用 $\Omega_I$ 的周期积分说明 4d $S$-对偶在 Hitchin 纤维上就是 $T$-对偶？

## 一句话

用谱曲线写出 $\Omega_I=\sum dH_a\wedge d\oint_\gamma\omega^a$，纤维坐标由周期给出；$S$-对偶交换 $\tau\leftrightarrow-1/\tau$ 正是把周期与对偶周期互换，即纤维 $T$-对偶。

## 目标

把 $\Omega_I$ 用谱曲线的周期写出来，并说明 $S$-对偶的耦合常数变换对应周期的对偶变换。

## 前提

- $\lambda=y\,dz$ 是 $D$ 上的 Seiberg–Witten 微分；$H_a$ 是 Hitchin 可积系统的哈密顿量。
- $\omega^a=\partial\lambda/\partial H_a=-\partial P/\partial H_a\cdot dz/P'$ 是 $D$ 上的全纯微分。
- $\MH$ 的超凯勒结构给 $\Omega_I=\omega_J+i\omega_K$，在纤维方向为零（Lagrangian）。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 把 $\Omega_I$ 写成 $\Omega=\sum_a dH_a\wedge d\oint_\gamma\omega^a$（eq (3.29)），纤维坐标是周期 $\oint_\gamma\omega^a$。 | Abel–Jacobi 把纤维坐标实现为周期积分。 | `A p.31 eq (3.29)` | A·原文明确写了 |
| 2 | 等价地 $\Omega=\sum_a\sum_i n_i\, dH_a\wedge(\omega^a,dq_i)$（eq (3.31)），说明 $\Omega_I$ 只依赖底坐标 $H$ 与纤维周期。 | 这给出纤维上的平移不变辛结构。 | `A p.31 eq (3.31)` | A·原文明确写了 |
| 3 | 与规范理论侧比较：$\Omega_I=\frac1\pi\int_C\|d^2z\|\operatorname{Tr}\delta\varphi_z\delta A_z$（eq (3.36)），再用 $D$ 上数据写成 $\frac1\pi\int_D\delta y\,\delta a_z$（eq (3.37)）。 | 两种写法必须在同一个 $\Omega_I$ 上一致。 | `A p.33 eq (3.36)` | A·原文明确写了 |
| 4 | $S$-对偶把 $\tau$ 换成 $-1/\tau$，在纤维上正是把周期 $\oint_\gamma$ 与对偶周期互换，即 $F\leftrightarrow F'$ 的 $T$-对偶。 | 环面的 $T$-对偶交换半径/周期，与 $\tau\to-1/\tau$ 一致。 | `A p.34 eq (3.39)` | B·原文暗示、我们补的中间步 |

## 结论

$\Omega_I$ 的周期数据在 $S$-对偶下按 $\tau\leftrightarrow-1/\tau$ 变换，这正是 Hitchin 纤维的 $T$-对偶；逐纤维的周期匹配给出“$S$-对偶 $=$ $T$-对偶”的定量版本。

## 缺口

- 第 4 步的周期互换是定性陈述：原文 $\S3.4.1$ 只做了一致性核对，没有给出完整的模变换证明。

## 最容易讲错的地方

- $\Omega_I$ 在纤维上为零：周期匹配说的是 $\Omega_I$ 的横向部分，不是纤维内部的辛形式。
- $\tau\to-1/\tau$ 不是 $\tau\to1/\tau$：$S$-对偶带负号，符号来自 $\theta$ 角的变换。
- $\omega^a$ 是 $D$ 上的微分，不是 $C$ 上的；积分回路 $\gamma$ 在 $D$ 上。

## 相关卡

[辛形式 $\Omega_I$ 与耦合常数](../concepts/symplectic-form.md) · [对偶环面纤维化与 T-对偶](../concepts/dual-torus-fibration.md) · [完全可积性与对易哈密顿量](../concepts/integrable-system.md) · [谱曲线](../concepts/spectral-curve.md) · [希钦方程 = 超凯勒矩映射商](../derivations/hitchin-as-moment-map.md)

## 出处（印刷页）

- A p.30–33（A p.31 eq (3.29)）
- A p.33–34（A p.33 eq (3.36)）

> 说明：A3：eq (3.29)(3.31)(3.36)(3.37) 均在原文 $\S3.4$–$\S3.4.1$；B1：第 4 步的周期互换是整理时补的定性论证。最没把握处：$\tau$ 与周期归一化的精确系数原文散见 $\S3.4.1$ 与 $\S7.1$ 脚注 24。
