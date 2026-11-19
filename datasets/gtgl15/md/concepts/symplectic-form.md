# 辛形式 $\Omega_I$ 与耦合常数

> `gtgl15/concept/symplectic-form` · 轨道 B · 对偶环面与 T-对偶 · 状态 dev

> **先自测**：为什么规范理论里看似平常的 $\int\operatorname{Tr}\delta\varphi\wedge\delta A$ 会成为 Hitchin 模空间上的全纯辛形式？

## 一句话

$\MH$ 上有全纯辛形式 $\Omega_I=\frac1\pi\int_C\operatorname{Tr}\delta\varphi_z\wedge\delta A_z$，且 $\Omega_I=\omega_J+i\omega_K$；它决定纤维上的辛结构和对偶的周期匹配。

## 定义

在 $\MH$ 上定义 $\Omega_I=\frac1\pi\int_C|d^2z|\operatorname{Tr}\delta\varphi_z\wedge\delta A_z$（短根长平方归一化为 2）。它是 $I$-全纯的闭 2-形式，并且 $\Omega_I=\omega_J+i\omega_K$，其中 $\omega_I,\omega_J,\omega_K$ 是超凯勒结构的三个 Kähler 形式。用谱曲线可以把它写成 $\Omega_I=\sum_a dH_a\wedge d\oint_\gamma\omega^a$，其中 $\omega^a=\partial\lambda/\partial H_a$，$\lambda=y\,dz$。耦合常数 $\tau=\theta/2\pi+4\pi i/e^2$ 控制 $\Omega_I$ 在纤维上的周期。

**记号**：$\Omega_I$；$\omega_I,\omega_J,\omega_K$；$\lambda=y\,dz$；$H_a$；$\tau$。

## 要点（为什么需要它）

1. $\Omega_I$ 是 $I$-全纯的：它是 $\MH$ 作为复流形的全纯辛形式，不只是实辛形式。
2. $\MH$ 是超凯勒流形：$\Omega_I=\omega_J+i\omega_K$，三个 Kähler 形式两两配对成复形式。
3. 在 Hitchin 纤维上 $\Omega_I$ 限制为零（纤维是 Lagrangian），这是 $\S2.5$ 的推论。
4. 用谱曲线写：$\Omega_I=\sum_a dH_a\wedge d\oint_\gamma\omega^a$，与 $H_a$ 的对易性一致（$\S3.4$）。
5. 归一化与耦合常数：$\Omega_I$ 的周期正比于 $\tau$ 的虚部；$S$-对偶交换 $\tau\leftrightarrow-1/\tau$ 即周期匹配。

## 核心公式

$$
$$\Omega_I=\frac1\pi\int_C|d^2z|\operatorname{Tr}\delta\varphi_z\wedge\delta A_z,\qquad \Omega_I=\omega_J+i\omega_K$$$$\Omega_I=\sum_a dH_a\wedge d\oint_\gamma\omega^a,\qquad \lambda=y\,dz,\ \ \omega^a=\frac{\partial\lambda}{\partial H_a}$$
$$

$$
$$\Omega_I=\sum_a dH_a\wedge d\oint_\gamma\omega^a,\qquad \lambda=y\,dz,\ \ \omega^a=\frac{\partial\lambda}{\partial H_a}$$
$$

## 定理与证明（或缺口）

### $\Omega_I$ 的全纯性与闭性

$\Omega_I$ 是 $\MH$ 上的全纯辛形式，且其限制在 Hitchin 纤维上为零。

> 证明状态：**sketch**。超凯勒商的辛形式下降是标准事实，原文只用一句带过（$\S2.2$）。

出处：`A p.6`

## 常见误解

- $\Omega_I$ 是复 2-形式，不是 $\omega_I$；三者关系是 $\Omega_I=\omega_J+i\omega_K$，不是 $\omega_J+i\omega_K$ 的实部。
- 系数 $1/\pi$ 与短根归一化绑定；换成别的归一化，$\tau$ 的周期也会变。
- $\Omega_I$ 在纤维上为零（Lagrangian），但在横向非零；不要因为“辛形式”就以为处处非退化。
- $\Omega_I$ 与 $\omega_I$ 是不同东西：\(\omega_I\) 是实 Kähler 形式，$\Omega_I$ 是复全纯形式。

## 相关卡

[超凯勒商与复结构 I、J、K](../concepts/hyperkahler-quotient.md) · [希钦方程](../concepts/hitchin-equations.md) · [完全可积性与对易哈密顿量](../concepts/integrable-system.md) · [对偶环面纤维化与 T-对偶](../concepts/dual-torus-fibration.md) · [辛形式的周期匹配与 $S$-对偶 $=$ $T$-对偶](../derivations/symplectic-period-matching.md)

## 出处（印刷页）

- A p.6（A p.6 eq (2.4)）
- A p.30–33（A p.31 eq (3.29)）
- A p.33–34（A p.33 eq (3.36)）

> 说明：A=原文 $\S2.2$ 的 eq (2.4)、$\S3.4$ 的谱曲线表达式与 $\S3.4.1$ 的规范理论比较；B=把全纯性/闭性/纤维零三步补全；C=$\tau$ 与周期匹配的定量关系按 $\S3.4.1$ 与 $\S7.1$ 脚注 24 整理。最没把握处：$1/\pi$ 归一化与短根长度的对应原文只在一处脚注说明。
