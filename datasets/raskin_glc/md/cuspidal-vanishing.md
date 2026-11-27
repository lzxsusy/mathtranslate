# 尖点层在 $d>2g-2$ 的 $!$-消没：命题 2.1.5 的拆解

- id：`raskin_glc/derivation/cuspidal-vanishing`
- 类型：derivation　轨道：B　状态：dev
- 一句话：把命题 2.1.5 拆成四步：扩张分裂、纤维识别为 $B H^0$、$B\mathbb{G}_a$ 的层范畴平凡、由 $q_{d,*}$ 等价推出 $p_d^!\mathcal{F}=0$。

**问题**：为什么「$\mathrm{CT}^d_*\mathcal{F}=0$」能反推出「$p_d^!\mathcal{F}=0$」，而不是只得到 $q_{d,*}$ 的核？

## 问题

设 $\mathcal{F}\in\operatorname{Shv}(\operatorname{Bun}_{\mathrm{PGL}_2})$ 为尖点层。证明：对 $d>2g-2$，$p_d^!\mathcal{F}\simeq 0$，其中 $p_d:\operatorname{Bun}^d_B\to\operatorname{Bun}_{\mathrm{PGL}_2}$。

## 设置

记 $q_d:\operatorname{Bun}^d_B\to\operatorname{Bun}^d_{\mathbb{G}_m}$。$\operatorname{Bun}^d_B$ 分类正合列 $0\to L\to\mathcal{E}\to\mathcal{O}\to 0$，$\deg L=d$。$\mathrm{CT}^d_*:=q_{d,*}p_d^!$。

## 步骤

1. **$d>2g-2$ 时，上述正合列自动分裂，故 $\operatorname{Bun}^d_B\to\operatorname{Bun}^d_{\mathbb{G}_m}$ 的纤维是 $\operatorname{Ext}^1(\mathcal{O},L)=H^1(X,L)$ 的分类叠。**

   依据：$\operatorname{Ext}^1(\mathcal{O},L)\cong H^1(X,L)$；$\deg L=d>2g-2=\deg\Omega$，故 $\deg(L^\vee\otimes\Omega)<0$，$H^1(X,L)^\vee\cong H^0(X,L^\vee\otimes\Omega)=0$，所有扩张分裂。

2. **该纤维作为叠同构于 $B H^0(X,L)$（或等价的 $B R\Gamma(X,L)[1]$），而不是 $B H^1(X,L)$。**

   依据：扩张分裂后，自同构群为 $\operatorname{Hom}(\mathcal{O},L)=H^0(X,L)$；$H^1=0$ 使 $R\Gamma(X,L)[1]$ 只在 $H^0$ 处有上同调。原文正文的 $B H^1$ 与脚注的 $R\Gamma[1]$ 应统一为 $B H^0$。

3. **对 $\pi:B\mathbb{G}_a\to\mathrm{pt}$，$\pi^*:\operatorname{Vect}\to\operatorname{Shv}(B\mathbb{G}_a)$ 与 $\pi_*$ 互为等价。**

   依据：$\mathbb{G}_a$ 作为 $k$ 上的群是可缩的（$k$ 代数闭、char $\e=0$ 的层论中 $\mathbb{G}_a$ 的 classifying stack 的层范畴平凡）；更一般地，$B\mathbb{G}_a$ 上的层由其在点上的纤维决定。

4. **$q_{d,*}$ 是等价，故 $\mathrm{CT}^d_*\mathcal{F}=q_{d,*}p_d^!\mathcal{F}\simeq 0$ 蕴含 $p_d^!\mathcal{F}\simeq 0$。**

   依据：第 3 步逐纤维应用：$q_d$ 是 $B\mathbb{G}_a$-gerbe，$q_{d,*}$ 与 $q_d^*$ 互为逆；$q_{d,*}$ 反映零对象。

## 结论

尖点性 $\mathrm{CT}_*\mathcal{F}=0$ 迫使 $\mathcal{F}$ 在所有 $d>2g-2$ 的 $\operatorname{Bun}^d_B$ 上 $!$-限制为零。

## 缺口/原文问题

- 原文正文写 $B H^1(X,L)$ 并说「$H^1(X,L)$ 可缩」，这与 $d>2g-2$ 时 $H^1=0$、$H^0\neq0$ 直接矛盾；脚注的 $R\Gamma(X,L)[1]$ 才是对的，但应展开为 $B H^0$。
- $q_{d,*}$ 为等价的论证依赖 $\operatorname{Shv}(B\mathbb{G}_a)\simeq\operatorname{Vect}$；这一步在 de Rham/ℓ-进/Betti 三种系数下都成立，但讲义未逐系数说明。

## 出处

- Sam Raskin 讲授、Lin Chen 笔记《Notes for "Geometric Langlands for Projective Curves"》（2025-07-07/11，18 页），§2.1，命题 2.1.5 及其证明，pp. 6；`源码/sections/s02-cusp.tex:L54-L92（Prop 2.1.5 证明）`
  > Proof. ... the fiber of q_d is B H^1(X,L). ... because H^1(X,L) is contractible.

## 相关卡

- `raskin_glc/concept/cuspidal-sheaf`
- `raskin_glc/concept/coefficient-functor`

## 核验（partial，2026-11-27）

- nLab / perverse sheaf：`not_applicable` — 页面只给反常层的范畴框架，不涉及 $B\mathbb{G}_a$ 的层范畴或 Ext 计算；本卡的技术步骤以原文与标准形变理论为准。

拆解按原文证明逻辑重排；第 2 步的 $B H^0$ 修正是本卡的核心发现。
