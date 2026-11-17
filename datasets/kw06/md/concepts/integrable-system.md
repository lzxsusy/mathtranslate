# 可积系统

> `kw/concept/integrable-system` · 轨道 C · 舞台：曲线与模空间 · 状态 dev

> **先自测**：为什么说 $M_H$ 上的 Hitchin 系统是完全可积的，它的纤维是什么？

## 一句话

有足够多（半维数）两两 Poisson 交换的 Hamilton 量的辛流形；$M_H$ 在复结构 $I$ 下完全可积，等值面就是 Hitchin 纤维，是紧复环面。

## 定义

辛流形 $(X,\omega)$ 上的 Hamilton 系统称为完全可积的，若存在 $\frac{1}{2}\dim_{\mathbb R}X$ 个代数独立、两两 Poisson 交换的函数 $H_1,\dots,H_n$，且它们生成的流完备。对 $M_H$ 取 $H_{\alpha,i}=\int_C\alpha\wedge P_i(\varphi)$（$\alpha\in H^1(C,K_C^{1-d_i})$），在 $\Omega_I$ 下验证两两交换，即得完全可积系统；其等值面就是 Hitchin 纤维 $\mathcal F_b$。

**记号**：$H_{\alpha,i}$；$\{H_{\alpha,i},H_{\beta,j}\}_{\Omega_I}=0$；$\mathcal F_b$：等值面（Hitchin 纤维）；$\Omega_I$：复结构 $I$ 下的全纯辛形式。

## 要点（为什么需要它）

1. 解释 Hitchin 纤维化为什么呈「半维底 + 半维环面纤维」：这正是完全可积系统的定义性结构。
2. 证据是原文的两步行论证：先在 $\mathcal W$ 上验证对易（Hamilton 量只依赖 $\varphi_z$），再经辛约化下降到 $M_H$。
3. 纤维的 Lagrange 性是对易性与中间维数的直接推论，也是 SYZ 的 T-对偶能在纤维上逐点进行的前提。
4. 它是全纯可积系统：Hamilton 量是 $I$-全纯的、$\Omega_I$ 是全纯辛形式；取实切片才回到通常的实 Hamilton 系统。

## 核心公式

$$
$H_{\alpha,i}=\int_C\alpha\wedge P_i(\varphi),\qquad \alpha\in H^1(C,K_C^{1-d_i})$$\{H_{\alpha,i},H_{\beta,j}\}_{\Omega_I}=0,\qquad G=SU(2):\quad H_a=\int_C\alpha_a\wedge\mathrm{Tr}\,\varphi^2$
$$

$$
$\{H_{\alpha,i},H_{\beta,j}\}_{\Omega_I}=0,\qquad G=SU(2):\quad H_a=\int_C\alpha_a\wedge\mathrm{Tr}\,\varphi^2$
$$

## 定理与证明（或缺口）

### Hitchin 的 Hamilton 量两两 Poisson 交换

对每个基本不变多项式 $P_i$ 与 $\alpha\in H^1(C,K_C^{1-d_i})$，函数 $H_{\alpha,i}=\int_C\alpha\wedge P_i(\varphi)$ 在 $M_H$ 上两两 Poisson 交换：$\{H_{\alpha,i},H_{\beta,j}\}_{\Omega_I}=0$。

1. 先在 $\mathcal W$ 上计算：$\Omega_I$ 使 $\varphi_z$ 与 $A_z$ 共轭、而 $\varphi_z$ 与自身交换；$H_{\alpha,i}$ 只依赖 $\varphi_z$ 不依赖 $A_z$，故在 $\mathcal W$ 上显然两两交换。
   - *为什么*：$\mathcal W$ 是仿射空间，Poisson 张量显式已知，计算不必先理解商。
2. 再下降到 $M_H$：把函数限制到 $\nu_I=0$ 并对 $G_{\mathbb C}$ 取辛约化；辛约化把 Poisson 交换的函数族送到 Poisson 交换的函数族。
   - *为什么*：交换性在超凯勒商下保持，这一步是整个论证的关键。
3. 数目核对：$\dim B=\frac{1}{2}\dim M_H$，这些函数代数独立且个数达到一半，配合纤维紧即得完全可积系统。
   - *为什么*：只有「足够多」才能使可积系统成立，否则只有一族对易函数。

出处：`B p.55`

### 完全可积推出纤维是 Lagrange 子流形

若 $M_H$ 在 $I$ 下完全可积，则 Hitchin 纤维 $\mathcal F_b$ 是 Lagrange 子流形（对 $\Omega_I$，等价地对 $\omega_J,\omega_K$）。

> 证明状态：**sketch**。原文 p.56 只说这是整个论证的推论并给出概要，未逐项验证切空间的迷向性。

出处：`B p.56`

## 常见误解

- 把「半维数个函数」当成任意一组函数：必须代数独立且两两 Poisson 交换，否则不叫可积。
- 把复可积系统与实可积系统混同：$M_H$ 上是全纯可积（全纯辛形式与全纯 Hamilton 量），取实切片才得到通常的实 Hamilton 系统。
- 以为可积性已经给出 S-对偶：§4.3 只造好 $G$ 一侧的纤维化与环面纤维，T-对偶与镜像要到 §5 才出现。
- 把纤维的紧性当成显然：纤维紧用的是 Hitchin 纤维化的具体构造，不是任意完全可积系统都有的性质。

## 相关卡

[Hitchin 纤维化](../concepts/hitchin-fibration.md) · [Hitchin 模空间](../concepts/hitchin-moduli.md) · [Hitchin 系统的完全可积性与 Lagrange 纤维](../derivations/hitchin-integrability.md) · [超凯勒流形](../concepts/hyperkahler-manifold.md)

## 出处（印刷页）

- B p.54–55（B p.54）
- B p.55（B p.55 eq (4.26)）
- B p.56（B p.56）

> 说明：A=原文（$H_{\alpha,i}=\int\alpha\wedge P_i(\varphi)$、$\mathcal W$ 上的对易性、辛约化保持对易、个数由维数计数保证、纤维紧与 Lagrange、实切片脚注）；B=由原文重建（可积系统定义与 Hitchin 构造的对接、迷向性的表述）；C=标准背景（Liouville 可积系统的一般定义）。
