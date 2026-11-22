# 整体 Tate 论文与 adele 上的自守形式

> `lbook04/concept/ch6-global-tate` · 轨 T Tate 与迹公式 · 状态 reviewed · 核验 source-only

**问题：** Poisson 求和公式在 Tate 论文里用在哪一步，为什么它等价于 Hecke 的函数方程？

**一句话：** 把局部 zeta 积分张量到 $\mathbb A$ 上，Poisson 求和给出整体函数方程 $\Lambda(s,\omega)=\varepsilon(s,\omega)\Lambda(1-s,\omega^{-1})$；这就是 Tate 论文对 Hecke $L$ 函数的统一处理。

**别名：** `Tate 论文`、`整体函数方程`、`global zeta integral`

## 定义

$S(\mathbb A)$ 由可分解函数 $f=\bigotimes f_v$（几乎处处 $f_v=f_v^o$）张成。整体 zeta 积分 $z(s,\omega;f)=\int_{\mathbb A^\times}f(x)\omega\omega_s(x)d^\times x$ 在 $\operatorname{Re}s>1$ 收敛；引理 4.1 把局部分布张成整体分布，定理 4.2 得 $\dim S'(\omega)=1$ 且 $z_o=\bigotimes z_{o,v}$。取整体 $\psi=\prod\psi_v$（在 $k$ 上平凡），Poisson 求和给定理 4.3 $\widehat z(1-s,\omega^{-1})=z(s,\omega)$，即 $\Lambda(s,\omega)=\varepsilon(s,\omega)\Lambda(1-s,\omega^{-1})$。

**记号：** $S(\mathbb A)$：整体 Schwartz–Bruhat 空间；$|\cdot|_{\mathbb A}$；$\psi=\prod\psi_v$；$\Lambda(s,\omega)=\prod_v L_v(s,\omega_v)$；$\varepsilon(s,\omega)=\prod_v\varepsilon_v$。

## 要点

- 可分解函数在 $S(\mathbb A)$ 中稠密；整体分布由局部张量积生成（引理 4.1），故一维性从局部升到整体。
- 乘积公式 $\prod_v|x|_v=1$ 使 $\psi$ 的选取在整体 $\varepsilon$ 中消去（用 $(3.29)$）。
- $(4.3)$ $z=\Lambda z_o$，$(4.4)$ $\Lambda(s,\omega)=\prod_v L_v(s,\omega_v)$；定理 4.3 是 Poisson 求和与局部 $(3.23)$ 的直接推论。
- 推论 4.4：$\Lambda(s,\omega)=\varepsilon(s,\omega)\Lambda(1-s,\omega^{-1})$，$\varepsilon$ 为有限个因子的乘积（几乎处处 $1$）。

## 公式

$$
z(s,\omega;f)=\int_{\mathbb A^\times}f(x)\,\omega\omega_s(x)\,d^\times x
$$

$$
\Lambda(s,\omega)=\prod_v L_v(s,\omega_v)
$$

$$
\Lambda(s,\omega)=\varepsilon(s,\omega)\,\Lambda(1-s,\omega^{-1})
$$

## 易错点

- 整体 $\psi$ 必须在 $k$ 上平凡（即 $\psi(k)=1$），否则 Poisson 求和不成立；局部导子 $\nu_v$ 只在有限个位非零。
- $\Lambda$ 的收敛与延拓是两件事：积分只在 $\operatorname{Re}s>1$ 收敛，延拓靠 $z=\Lambda z_o$ 与 $z_o$ 的整性，不能直接对积分做解析延拓。

## 批注

**〔背景直觉〕Tate 论文的一句话**　把 Hecke 的「和 over 理想」换成「$\mathbb A^\times$ 上的积分」，于是局部问题（一维分布空间）与整体问题（Poisson 求和）分离；函数方程成为局部 $(3.23)$ 的乘积，这是全章的技术主线。

**〔含糊点拨〕自守形式在哪**　本章的 $\operatorname{GL}(1)$ 情形里，「自守形式」就是 $\mathbb A^\times$ 上满足 $\omega(k^\times)=1$ 的函数；真正的 $\operatorname{GL}(2)$ 自守形式与 Whittaker 模型要到第 7 章才出现（ch07.tex:409–429）。

## 相关

[[ch6-quasi-character]]、[[ch6-local-zeta]]、[[ch6-whittaker]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§4，原书 pp. 125–128（PDF pp. 130–133）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch06.tex:671-809`
