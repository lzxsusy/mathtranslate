# 完全可积性与对易哈密顿量

> `gtgl15/concept/integrable-system` · 轨道 A · Hitchin 几何与谱曲线 · 状态 dev

> **先自测**：为什么这些哈密顿量自动对易，而它们的对易流又恰好沿着希钦纤维化运动？

## 一句话

$\MH$ 上有 $\frac12\dim_\mathbb{C}\MH$ 个 $I$-全纯、两两对易的哈密顿量（Casimir 乘上同调类积分），构成 Hitchin 完全可积系统。

## 定义

对 $SU(2)$，取 $H^1(C,T)$ 的一组基 $\alpha_a$，定义 $H_a=\int_C\alpha_a\wedge\operatorname{Tr}\varphi^2$。对一般 $G$，$H_{a,i}=\int_C\alpha_{a,i}P_i(\varphi)$，其中 $P_i$ 是 Casimir 不变量，$\alpha_{a,i}\in H^1(C,K^{1-d_i})$。这些 $(g-1)\dim G$ 个函数在 $\MH$ 上两两 Poisson 对易。

**记号**：$H_{a,i}$；$\alpha_{a,i}$；$P_i$；$\{\cdot,\cdot\}$。

## 要点（为什么需要它）

1. $H_{a,i}$ 只依赖 $\varphi_z$，而 $\varphi_z$ 在 $\mathcal W$ 上与自己 Poisson 对易，所以商之前对易。
2. 超凯勒商保持 Poisson 括号，故 $H_{a,i}$ 在 $\MH$ 上仍对易：这是 Hitchin 证明的核心。
3. 对易流的哈密顿量都是 $I$-全纯的，且都保持特征多项式（Hitchin 纤维化），所以流保持在纤维内。
4. 维数匹配：$\frac12\dim_\mathbb{C}\MH=\dim\mathcal V$，故对易函数恰好够多，系统完全可积。
5. 推论：一般纤维是复环面，且对 $\Omega_I$ Lagrangian（$\S2.5$）。

## 核心公式

$$
$$H_{a,i}=\int_C\alpha_{a,i}\,P_i(\varphi),\qquad \alpha_{a,i}\in H^1(C,K^{1-d_i})$$$$\{H_{a,i},H_{b,j}\}=0,\qquad \#\{H\}=\tfrac12\dim_\mathbb{C}\MH$$
$$

$$
$$\{H_{a,i},H_{b,j}\}=0,\qquad \#\{H\}=\tfrac12\dim_\mathbb{C}\MH$$
$$

## 定理与证明（或缺口）

### Hitchin 完全可积性

$\MH$ 上存在 $\frac12\dim_\mathbb{C}\MH$ 个独立的 $I$-全纯哈密顿量，两两对易，其公共水平集就是 Hitchin 纤维。

> 证明状态：**sketch**。原文 $\S2.5$ 给出思路，完整证明依赖 [13][21]。

出处：`A p.9`

## 常见误解

- 对易的是 $I$-全纯哈密顿量，不是实哈密顿量；两者不要混用。
- $\frac12\dim_\mathbb{C}\MH$ 指复维数的一半；若把 $\frac12\dim_\mathbb{R}\MH$ 当成个数，就 $=\dim_\mathbb{C}\MH$，比正确数目多出因子 2。
- 在奇异纤维（判别式上）流不再传递，完全可积性要逐纤维理解。
- 这些 $H$ 是全局定义的函数，但不能用它们把 $\MH$ 整体写成 $T^*\mathcal V$：$\mathcal V$ 是底，纤维才是环面。

## 相关卡

[希钦纤维化](../concepts/hitchin-fibration.md) · [希钦模空间 $\MH$](../concepts/hitchin-moduli.md) · [谱曲线](../concepts/spectral-curve.md) · [辛形式 $\Omega_I$ 与耦合常数](../concepts/symplectic-form.md) · [维数计数：$\sum(2d_i-1)=\dim G$](../derivations/dimension-count.md)

## 出处（印刷页）

- A p.8–10（A p.9 eq (2.7)）
- A p.8（A p.8 eq (2.6)）

> 说明：A=原文 $\S2.5$ 的哈密顿量构造（eq (2.7)）与对易性论证；B=把“超凯勒商保持括号”整理成独立一步；C=环面作用的陈述按标准可积系统语言补全。最没把握处：$\alpha_{a,i}\in H^1(C,K^{1-d_i})$ 的度数原文只写了一句。
