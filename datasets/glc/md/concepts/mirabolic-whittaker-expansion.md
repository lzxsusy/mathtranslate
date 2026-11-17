---
id: glc/concept/mirabolic-whittaker-expansion
type: concept
track: C
---

# mirabolic Whittaker 展开（Piatetski-Shapiro–Shalika）

> 沿 Ṅ(F)\Q̇_1(F) 求和把整体 Whittaker 函数送到 mirabolic 商上的尖点函数；对 W_σ 该函数实际 Ġ(F) 不变，即尖点 Hecke 特征函数 f_σ。

**问题**：Whittaker 展开 φ 的求和指标是什么，Piatetski-Shapiro–Shalika 定理又补上了哪一条不变性？

## 定义

对 $\operatorname{GL}_n$，令 $Q_1=\begin{pmatrix}\operatorname{GL}_{n-1}&V_{n-1}\\0&1\end{pmatrix}$ 为 mirabolic 子群。典范映射为 $\varphi:C^\infty((\dot N(\mathbb{A}),\Psi)\backslash\dot G(\mathbb{A}))\xrightarrow{\sim}C^\infty(\dot Q_1(F)\backslash\dot G(\mathbb{A}))_{\mathrm{cusp}}$，$W\mapsto\left(g\mapsto\sum_{\gamma\in\dot N(F)\backslash\dot Q_1(F)}W(\gamma g)\right)$。等价地，该和就是相应离散商上的积分。

*记号*：$Q_1$ 为 mirabolic 子群（稳定一个非零线性泛函的极大抛物）；$V_{n-1}$ 为 $\operatorname{GL}_{n-1}$ 的标准表示；下标 $\mathrm{cusp}$ 表示尖点函数子空间。

## 要点

- 求和指标是 $\dot N(F)\backslash\dot Q_1(F)$（$Q_1$ 左作用、$N$ 在其内），不是 $\dot N(F)\backslash\dot G(F)$。
- 等价形式：因 $N\subset Q_1$，$(\operatorname{Av}_!W)(g)=\sum_{\gamma\in N(K)\backslash Q_1(K)}W(\gamma g)$；函数论情形尖点性使该求和收敛，几何上以一般位置约化模空间之间相应映射的 $!$ 推前替代。
- 对归一化的 Hecke 特征函数 $W_\sigma$，Piatetski-Shapiro–Shalika 自守性定理说明 $\varphi(W_\sigma)$ 实际上左 $\dot G(F)$ 不变；这就是尖点 Hecke 特征函数 $f_\sigma$。
- 几何形式：$\operatorname{Av}_!:D(\operatorname{Bun}_G^{N\text{-gen}})^{\mathrm{Wh}}\xrightarrow{\sim}D(\operatorname{Bun}_G^{Q_1\text{-gen}})_{\mathrm{cusp}}$，应与局部 Whittaker–Satake 等价及谱一侧一起理解。

## 关键公式

- $\varphi:C^\infty((\dot N(\mathbb{A}),\Psi)\backslash\dot G(\mathbb{A}))\xrightarrow{\ \sim\ }C^\infty(\dot Q_1(F)\backslash\dot G(\mathbb{A}))_{\mathrm{cusp}},\quad W\longmapsto\left(g\mapsto\sum_{\gamma\in\dot N(F)\backslash\dot Q_1(F)}W(\gamma g)\right)$
- $(\operatorname{Av}_!W)(g)=\sum_{\gamma\in N(K)\backslash Q_1(K)}W(\gamma g)$
- $\operatorname{Av}_!:D(\operatorname{Bun}_G^{N\text{-gen}})^{\mathrm{Wh}}\xrightarrow{\ \sim\ }D(\operatorname{Bun}_G^{Q_1\text{-gen}})_{\mathrm{cusp}}$

## 定理与证明

### Piatetski-Shapiro–Shalika 自守性定理（讲义引述）（要点（有缺口））

对归一化的 Hecke 特征函数 $W_\sigma$，$\varphi(W_\sigma)$ 实际上左 $\dot G(F)$ 不变；这就是尖点 Hecke 特征函数 $f_\sigma$。

1. 取 $W=W_\sigma$ 并作 mirabolic 求和得到 $\varphi(W_\sigma)$。  
   *为什么*：$\varphi$ 的定义（典范映射）。
2. 断言 $\varphi(W_\sigma)$ 左 $\dot G(F)$ 不变。  
   *为什么*：PS-S 自守性定理；讲义未给证明。

> 缺口：讲义只述不证；这是 [FGKV98] 的 Whittaker 比较所用的函数论输入。

*出处*：§3.5（原书 p.22）


## 易错点

- 求和的商是 $\dot N(F)\backslash\dot Q_1(F)$，不是 $\dot N(F)\backslash\dot G(F)$；后者既不对应 mirabolic 商，也不保证收敛。
- $\varphi$ 的像带下标 $\mathrm{cusp}$；PS-S 定理补的是 $f_\sigma$ 的左 $\dot G(F)$ 不变性，不是 $\varphi$ 的定义本身。
- 「等价地，该和就是相应离散商上的积分」：不要把这个和读成对 $\dot N(\mathbb{A})$ 的 Haar 积分，指标集是离散商。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§3.5 整体 Whittaker 函数与自守函数，p.21-22（PDF p.21-22），`源码/chapters/ch03.tex:95-105（§3.5）`

## 核验

状态：`source-only`（2026-11-18）
- FGKV98：https://arxiv.org/abs/alg-geom/9703022 — φ:C^∞(GL_n^J(A))_Ψ^{N^J(A)}→C^∞(GL_n^J(A))_{cusp}^{P_1^J(F)}，φ(f)(g)=Σ_{y∈N_{n-1}^J(F)\GL_{n-1}^J(F)}f((y 0;0 1)g)
- FGKV98：https://arxiv.org/abs/alg-geom/9703022 — TH0：PS-S 理论给出像落在尖点函数，且左 GL_n(F) 不变
- nLab：https://ncatlab.org/nlab/show/Whittaker+function — KP3：几何形式 Av_!:D(Bun_G^{N-gen})^Wh→D(Bun_G^{Q_1-gen})_cusp

## 关联

- `glc/concept/global-whittaker-function`
- `glc/concept/generic-reduction-whittaker`
- `glc/concept/degenerate-whittaker-characters`
