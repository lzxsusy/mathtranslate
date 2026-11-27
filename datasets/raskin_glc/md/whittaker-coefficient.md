# Whittaker 系数与几何 Casselman–Shalika

- id：`raskin_glc/concept/whittaker-coefficient`
- 类型：concept　轨道：E　状态：dev
- 一句话：用 $\operatorname{Bun}^{\Omega}_N\to\mathbb{A}^1$ 与 $\exp$ 层定义 $\operatorname{coeff}_D$；FGV 的几何 Casselman–Shalika 定理把它写成「先做 Hecke 作用、再取 $\operatorname{coeff}_0$」。

**问题**：为什么一般约化群的 Whittaker 系数必须经过 $\check\rho(\Omega)$ 的扭化，而不能直接用在 $\operatorname{Bun}_B$ 上？

## 定义

设 $G$ 为分裂约化群，$N\subset G$ 为极大单幂子群，$T$ 为极大环面。令 $\check\rho(\Omega):=2\check\rho(\Omega^{1/2})$（固定 $\Omega$ 的平方根），并定义 $\operatorname{Bun}^{\Omega}_N:=\operatorname{Bun}_B\times_{\operatorname{Bun}_T}\{\check\rho(\Omega)\}$。对每个正单根 $\alpha_i$，$N\to\mathbb{G}_a$ 诱导 $\varphi_i:\operatorname{Bun}^{\Omega}_N\to\operatorname{Bun}^{\Omega}_{\mathbb{G}_a}\to H^1(X,\Omega)\cong\mathbb{A}^1$，令 $\varphi:=\sum_i\alpha_i\varphi_i$。定义 $\operatorname{coeff}_0(\mathcal{F}):=\mathbb{C}\cdot(\operatorname{Bun}^{\Omega}_N,p_N^!\mathcal{F}\otimes^!\varphi^!\exp)$。对 $D=\sum_i\check\lambda_i x_i$（$\lambda_i\in\check\Lambda^+$），把 $\check\rho(\Omega)$ 换成 $\check\rho(\Omega)(-D)$ 即得 $\operatorname{coeff}_D$。

记号：$\check\Lambda^+$ 为支配权；$\check\rho$ 为 Weyl 向量；$\Omega^{1/2}$ 为固定平方根；$p_N:\operatorname{Bun}_B\to\operatorname{Bun}_G$。

## 要点

- $\operatorname{Bun}^{\Omega}_N$ 不是 $\operatorname{Bun}_B$ 本身：它把 $T$-丛扭到 $\check\rho(\Omega)$，使每个正单根方向的 $\mathbb{G}_a$-扩张有正确的「中心荷」，从而 $\varphi$ 是良定义的。
- 对 $G=\mathbb{G}_m$，$\operatorname{Bun}^{\Omega}_N$ 退化为一点，$\operatorname{coeff}_D$ 就是线丛 $\mathcal{O}(-D)$ 处的 $!$-纤维；这是「Whittaker 系数」最简单的例子。
- 对 $G=\mathrm{PGL}_2$，$\check\rho(\Omega)=\Omega$，$\operatorname{Bun}^{\Omega}_N=\operatorname{Bun}^{\Omega(-D)}_N$，于是回到第三讲的 $\operatorname{coeff}_D$（例 5.1.3）。
- 几何 Casselman–Shalika（定理 5.1.4）：$\operatorname{coeff}_D(\mathcal{F})\cong\operatorname{coeff}_0(\mathrm{H}_{\boxtimes V_{\check\lambda_i},x}(\mathcal{F}))$；即「取第 $D$ 个 Whittaker 系数」等于「先沿 $D$ 做 Hecke 作用，再取常数项」。
- 对 Hecke 特征层 $\mathcal{F}_\sigma$，$\mathrm{H}_{\boxtimes V_{\check\lambda_i},x}(\mathcal{F}_\sigma)\cong\mathcal{F}_\sigma\otimes\bigotimes_i(V_{\check\lambda_i,\sigma})_{x_i}$，故 $\operatorname{coeff}_D(\mathcal{F}_\sigma)\cong\bigotimes_i(V_{\check\lambda_i,\sigma})_{x_i}$，回到 Goal 3.1.2 的一般 $G$ 版本。

## 公式

$$ \operatorname{coeff}_0(\mathcal{F})=\mathbb{C}\cdot\left(\operatorname{Bun}^{\Omega}_N,p_N^!\mathcal{F}\otimes^!\varphi^!\exp\right) $$

$$ \operatorname{Bun}^{\Omega}_N:=\operatorname{Bun}_B\times_{\operatorname{Bun}_T}\{\check\rho(\Omega)\} $$

$$ \operatorname{coeff}_D(\mathcal{F})\cong\operatorname{coeff}_0(\mathrm{H}_{\boxtimes V_{\check\lambda_i},x}(\mathcal{F})) $$

$$ \operatorname{coeff}_D(\mathcal{F}_\sigma)\cong\bigotimes_i(V_{\check\lambda_i,\sigma})_{x_i} $$

## 定理与证明状态

### 定义 5.1.1（Whittaker 系数函子）

上述 $\operatorname{coeff}_D:\operatorname{Shv}(\operatorname{Bun}_G)\to\operatorname{Vect}$ 对每个 $D=\sum\check\lambda_i x_i$ 有定义，称为 Whittaker 系数函子。

- 证明状态：`none`
- 说明：定义。
- 出处：§5.1，原文 p.16

### 定理 5.1.4（Frenkel–Gaitsgory–Vilonen，几何 Casselman–Shalika）

对 $D=\sum\check\lambda_i x_i$（$\lambda_i\in\check\Lambda^+$）与 $\mathcal{F}\in\operatorname{Shv}(\operatorname{Bun}_G)$，有 $\operatorname{coeff}_D(\mathcal{F})\cong\operatorname{coeff}_0(\mathrm{H}_{\boxtimes_i V_{\check\lambda_i},x}(\mathcal{F}))$。

- 证明状态：`cited`
- 说明：讲义只述定理；证明见 Frenkel–Gaitsgory–Vilonen 的原始论文与 Ngo–Polo 的几何 Casselman–Shalika 表述。
- 出处：§5.1，原文 p.16

### 定理 5.1.7（Beraldo, FGV）

当 $G=\mathrm{GL}_n$ 或 $\mathrm{PGL}_n$ 时，$\operatorname{coeff}^{\mathrm{ult}}$ 在尖点子范畴 $\operatorname{Shv}(\operatorname{Bun}_G)_{\mathrm{cusp}}$ 上全忠实。

- 证明状态：`cited`
- 说明：$\mathrm{PGL}_2$ 的证明模仿 Fourier 反演，$\mathrm{GL}_n$ 的证明模仿 Piatetski–Shapiro–Shalika；讲义未展开。
- 出处：§5.1，原文 p.17

## 易错点

- $\check\rho(\Omega)$ 不是 $\Omega$：对 $\mathrm{PGL}_2$ 恰好相等，但对一般 $G$ 差一个 Weyl 向量；写成 $\Omega$ 会丢掉单根方向的权重。
- $\Omega^{1/2}$ 必须预先固定；换一个平方根会把 $\operatorname{coeff}_D$ 整体乘以一个符号/二次特征。
- $D$ 的系数 $\check\lambda_i$ 取在支配权 $\check\Lambda^+$ 中，不是任意整数；这对应「最高权表示」的 Hecke 作用。
- $\operatorname{coeff}_D$ 的取值是向量空间；$\operatorname{coeff}^{\mathrm{ult}}$ 才是取值在 $\operatorname{Rep}(\check G)_{\mathrm{Ran}}$ 中的「终极」版本。

## 出处

- Sam Raskin 讲授、Lin Chen 笔记《Notes for "Geometric Langlands for Projective Curves"》（2025-07-07/11，18 页），§5.1 Whittaker 系数，pp. 16, 17；`源码/sections/s05-whittaker.tex:L38-L100（Definition 5.1.1 与 Theorem 5.1.4）`
  > Definition 5.1.1. ... coeff_D(F) := C · (Bun^Ω_N, p_N^!(F) ⊗^! φ^!(exp)).

## 相关卡

- `raskin_glc/concept/coefficient-functor`
- `raskin_glc/concept/hecke-eigensheaf`
- `raskin_glc/concept/categorical-geometric-langlands`

## 核验（partial，2026-11-27）

- nLab / geometric Langlands correspondence：`partial` — 页面提到几何 Langlands 的 Hecke 特征层框架，但未涉及 Whittaker 系数或几何 Casselman–Shalika；只能作为大背景。

Whittaker 系数的定义与 FGV 定理以原文为准；nLab 无对应条目。
