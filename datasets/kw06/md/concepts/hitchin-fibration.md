# Hitchin 纤维化

> `kw/concept/hitchin-fibration` · 轨道 C · 舞台：曲线与模空间 · 状态 dev

> **先自测**：Hitchin 纤维化的底和纤维分别是什么，它为什么导致完全可积？

## 一句话

把 $(E,\varphi)$ 送到 Casimir 不变量的映射 $\pi:M_H\to B$：底与一般纤维的复维都占一半、一般纤维是复环面，使其成为完全可积系统，也是 SYZ 镜像的几何基础。

## 定义

设 $G$ 的秩为 $r$、基本不变多项式为 $P_i$（相应次数 $d_i$），Hitchin 纤维化定义为 $\pi:M_H(G,C)\to B=\bigoplus_{i=1}^{r}H^0(C,K_C^{d_i})$，$(E,\varphi)\mapsto(P_1(\varphi),\dots,P_r(\varphi))$。它在复结构 $I$ 下全纯并且满射，底与一般纤维的复维都等于 $(g-1)\dim G=\frac{1}{2}\dim M_H$。一般纤维是紧复环面，并且对 $\omega_J,\omega_K$ 是 Lagrangian 子流形。

**记号**：$\pi:M_H\to B$；$B=\bigoplus_{i=1}^{r}H^0(C,K_C^{d_i})$；$P_i$：基本不变多项式；$\mathcal F_b=\pi^{-1}(b)$。$d_i$ 取次数（与 Witten 2015 式 (2.5)–(2.6) 的约定一致）；若改用指数 $d_i^{\mathrm{exp}}$（$=$ 次数 $-1$），底空间应写作 $\bigoplus_i H^0(C,K_C^{d_i^{\mathrm{exp}}+1})$，两种约定差 1。

## 要点（为什么需要它）

1. 把 $M_H$ 摊成「底 $\times$ 环面」：底记录 Casimir 不变量的值，纤维是可做 T-对偶的环面，这是 SYZ 图像的原型。
2. 维数账是核心：$\dim B=(g-1)\dim G=\frac{1}{2}\dim M_H$，所以独立 Hamilton 量的个数正好一半。
3. 纤维的紧性来自 $C$ 紧；正因如此，§4.3 才能用「全纯函数必来自底」完成完全可积性的论证。
4. Hitchin 第二纤维化（忘掉 $\varphi$ 的 $M_H\to M$）是另一个映射，不要与 $\pi$ 混淆。
5. 判别式轨迹上纤维退化，退化纤维是谱曲线技巧与镜像对称的入口。

## 核心公式

$$
$\pi:M_H\to B,\qquad (E,\varphi)\mapsto(P_1(\varphi),\dots,P_r(\varphi)),\qquad B=\bigoplus_{i=1}^{r}H^0(C,K_C^{d_i})$$\dim_{\mathbb C}B=(g-1)\dim G=\frac{1}{2}\dim_{\mathbb C}M_H,\qquad \sum_{i=1}^{r}(2d_i-1)=\dim G$$G=SU(2):\qquad B=H^0(C,K_C^2),\qquad \pi(E,\varphi)=\mathrm{Tr}\,\varphi^2$
$$

$$
$\dim_{\mathbb C}B=(g-1)\dim G=\frac{1}{2}\dim_{\mathbb C}M_H,\qquad \sum_{i=1}^{r}(2d_i-1)=\dim G$
$$

$$
$G=SU(2):\qquad B=H^0(C,K_C^2),\qquad \pi(E,\varphi)=\mathrm{Tr}\,\varphi^2$
$$

## 定理与证明（或缺口）

### Hitchin 纤维在 $\omega_J,\omega_K$ 下是 Lagrangian 子流形

对任意 $b\in B$，纤维 $\mathcal F_b=\pi^{-1}(b)$ 是 $M_H$ 的 Lagrange 子流形（对 $\Omega_I$，等价地对 $\omega_J,\omega_K$）。

1. 把 $\mathcal F_b$ 写成对易 Hamilton 量的等值面：$\mathcal F_b=\{H_k=h_k\}$，其中 $H_k$ 两两 Poisson 交换、代数独立。
   - *为什么*：纤维就是纤维化映射的等值集，而 $\pi$ 的各分量正是这些 Hamilton 量。
2. 对易函数定义的等值面是中间维数的，其切空间在 $\Omega_I$ 下迷向；等值面维数等于 $\dim B=\frac{1}{2}\dim M_H$，已达到最大迷向维数，故为 Lagrangian。
   - *为什么*：维数占一半加迷向性就等于 Lagrange，无需再做积分或分析。

出处：`B p.56`

### Hitchin 纤维化满射，且一般纤维维数为 $\dim B$

$\pi$ 是满射，且一般纤维的复维为 $(g-1)\dim G=\frac{1}{2}\dim M_H$。

> 证明状态：**sketch**。原文 p.54 只对 $G=SU(2)$ 用方程计数论证满射性，一般 $G$ 未证；「一般纤维维数」依赖 $\pi$ 全纯与半连续性，原文未展开。

出处：`B p.54`

## 常见误解

- 把 Hitchin 纤维化与 Hitchin 第二纤维化混淆：后者是忘掉 $\varphi$ 的 $M_H\to M$，不是 $\pi$。
- 以为纤维都是同一个固定环面：一般纤维是复环面的 torsor，没有自然原点，且在判别式轨迹上退化。
- 把底上线性函数的拉回当成 $M_H$ 的全部全纯函数：对易的 Hamilton 量只构成其中一半维数的子环。
- 以为 $\pi$ 处处光滑：在稳定与半稳定的边界上纤维化不光滑，本文只在一般点附近工作。

## 相关卡

[Hitchin 模空间](../concepts/hitchin-moduli.md) · [可积系统](../concepts/integrable-system.md) · [Hitchin 系统的完全可积性与 Lagrange 纤维](../derivations/hitchin-integrability.md) · [镜像对称（本文版本）](../concepts/mirror-symmetry.md)

## 出处（印刷页）

- B p.53（B p.53）
- B p.54–55（B p.54 eq (4.25)）
- B p.56（B p.56）

> 说明：A=原文（Hitchin 纤维化定义、$\sum(2d_i-1)=\dim G$、$\dim B=\frac{1}{2}\dim M_H$、满射性与 $2^{3g-3}$ 计数、纤维紧、纤维 Lagrangian）；B=由原文重建（torsor 与判别式轨迹的表述、与第二纤维化的区分）；C=标准背景（SYZ 镜像的框架，原文 §5 才用到）。
