---
id: glc/concept/local-whittaker-eigenfunction
type: concept
track: C
---

# 局部 Whittaker 特征函数（Casselman–Shalika）

> 在 Ġ(K_x)/Ġ(O_x) 上存在唯一归一化 Whittaker 函数 W_{γ,x}，由 W(1)=1、右 O_x 不变、Ṅ 等变与 Hecke 本征性刻画，其值由 Casselman–Shalika 公式给出。

**问题**：刻画 W_{γ,x} 的四条条件是什么，Casselman–Shalika 公式在优势余权上给出什么值？

## 定义

设 $\gamma\in\operatorname{GL}_n(\mathbb{Q}_\ell)$，例如上述归一化 Satake 参数 $\gamma_x$。在 $\dot G(K_x)/\dot G(\mathcal{O}_x)$ 上存在唯一归一化的 Hecke 特征 Whittaker 函数 $W_{\gamma,x}$，满足：(1) $W_{\gamma,x}(1)=1$，其中 $1$ 表示仿射 Grassmann 簇的基点；(2) 对 $h\in\dot G(\mathcal{O}_x)$，$W_{\gamma,x}(gh)=W_{\gamma,x}(g)$；(3) 对 $u\in\dot N(K_x)$，$W_{\gamma,x}(ug)=\Psi_x(u)W_{\gamma,x}(g)$；(4) 对每个 $0\le d\le n$，$T_x^dW_{\gamma,x}=q_x^{-d(d-1)/2}\operatorname{Tr}\bigl(\bigwedge^d\gamma\bigr)W_{\gamma,x}$。选取用来书写 $t_x^\lambda$ 的局部坐标后，Whittaker 双商以余权格为指标：$\dot N(K_x)\backslash\dot G(K_x)/\dot G(\mathcal{O}_x)\simeq\Lambda$，$\dot N(K_x)t_x^\lambda\dot G(\mathcal{O}_x)\leftrightarrow\lambda$。

*记号*：$\Lambda$ 为余权格；$t_x^\lambda$ 按所选局部坐标书写；$V^\lambda$（优势 $\lambda$）为最高权 $\lambda$ 的不可约 $\check G$ 表示；$\operatorname{Perv}^{\mathrm{Wh}}$、$D^{\mathrm{Wh}}$ 表示 Whittaker 等变（扭曲）版本的反常层与导出范畴。

## 要点

- 归一化在 $W(1)=1$：$1$ 是仿射 Grassmann 簇的基点。Hecke 本征性与等变性只把 $W$ 确定到标量，唯一性靠这一条。
- 特征值常数是 $q_x^{-d(d-1)/2}$，用 $\gamma$ 书写；与 §3.2 用 $\sigma(\operatorname{Fr}_x)$ 书写的 $q_x^{d(n-d)/2}$ 相容，差别来自 $\operatorname{Tr}(\bigwedge^d\gamma_x)=q_x^{d(n-1)/2}\operatorname{Tr}(\bigwedge^d\sigma(\operatorname{Fr}_x))$。
- Casselman–Shalika 公式：对余权 $\lambda=(\lambda_1,\ldots,\lambda_n)$，优势时 $W_{\gamma,x}(t_x^\lambda)=q_x^{-\sum_i(i-1)\lambda_i}\operatorname{Tr}(\gamma,V^\lambda)$，非优势时为 $0$。
- 范畴形式：$\operatorname{Perv}^{\mathrm{Wh}}(\dot{\operatorname{Gr}}_{G,x})\simeq\operatorname{Rep}(\check G)$，导出层面为 $D^{\mathrm{Wh}}(\dot{\operatorname{Gr}}_{G,x})\simeq D^b(\operatorname{Rep}(\check G))$；这是几何 Satake 的 Whittaker 形式。
- 公式中的和 $\sum_i(i-1)\lambda_i$ 不取绝对值：仅当 $\lambda$ 为有效优势权（$\lambda_n\ge 0$，如 $\lambda=(2,1,0)$）时各项非负、指数为负；一般优势权指数可正可负（$n=2$、$\lambda=(0,-1)$ 时指数为 $+1$），这与 Casselman–Shalika 公式的指数约定一致。

## 关键公式

- $W_{\gamma,x}(t_x^\lambda)=\begin{cases}q_x^{-\sum_i(i-1)\lambda_i}\operatorname{Tr}(\gamma,V^\lambda), & \lambda\ \text{优势},\\ 0, & \text{否则},\end{cases}$
- $T_x^dW_{\gamma,x}=q_x^{-d(d-1)/2}\operatorname{Tr}\bigl(\bigwedge^d\gamma\bigr)W_{\gamma,x},\qquad 0\le d\le n$
- $\dot N(K_x)\backslash\dot G(K_x)/\dot G(\mathcal{O}_x)\simeq\Lambda$
- $\operatorname{Perv}^{\mathrm{Wh}}(\dot{\operatorname{Gr}}_{G,x})\simeq\operatorname{Rep}(\check G),\qquad D^{\mathrm{Wh}}(\dot{\operatorname{Gr}}_{G,x})\simeq D^b(\operatorname{Rep}(\check G))$

## 定理与证明

### 局部 Whittaker 函数的存在唯一性与 Casselman–Shalika 公式（要点（有缺口））

存在唯一的归一化 Whittaker 函数 $W_{\gamma,x}$ 满足上述 (1)–(4)；其显式值由 Casselman–Shalika 公式给出：优势 $\lambda$ 时 $W_{\gamma,x}(t_x^\lambda)=q_x^{-\sum_i(i-1)\lambda_i}\operatorname{Tr}(\gamma,V^\lambda)$，否则为 $0$。几何形式是 Satake 的 Whittaker 实现 $\operatorname{Perv}^{\mathrm{Wh}}(\dot{\operatorname{Gr}}_{G,x})\simeq\operatorname{Rep}(\check G)$。

1. 在双商 $\dot N(K_x)\backslash\dot G(K_x)/\dot G(\mathcal{O}_x)\simeq\Lambda$ 上用 $W(1)=1$ 与等变性把 $W$ 化为 $\Lambda$ 上的函数。  
   *为什么*：双商以余权格为指标，$t_x^\lambda$ 给出代表元。
2. 要求 (4) 的 Hecke 本征性确定这些值。  
   *为什么*：讲义断言存在唯一，未写出递推。
3. 用 Casselman–Shalika 公式显式写出优势 $\lambda$ 上的值。  
   *为什么*：讲义直接给出公式，未推导。

> 缺口：讲义只叙述存在唯一性与公式，未给证明；几何形式（Satake 的 Whittaker 实现）在讲义中引 [FGKV98]。

*出处*：§3.4（原书 p.21）


## 易错点

- 公式只对优势 $\lambda$ 给出非零值；把 $\lambda$ 任意取会得到 $0$，这不是公式失效。
- $V^\lambda$ 是 $\check G$ 的不可约表示，而 $\gamma$ 是 $\operatorname{GL}_n(\overline{\mathbb{Q}}_\ell)$ 的元素；对 $G=\operatorname{GL}_n$ 二者同为 $\operatorname{GL}_n$，但不要把它读成某个 $G$-模上的作用。
- 「唯一」是在 $W(1)=1$ 的归一化下；只要求 (2)(3)(4) 时解还差一个标量（与 §3.2 末尾「球面向量相差标量、Whittaker 归一化定标量」一致）。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§3.4 局部 Whittaker 特征函数，p.21（PDF p.21），`源码/chapters/ch03.tex:68-82（§3.4）`

## 核验

状态：`source-only`（2026-11-18）
- FGKV98：https://arxiv.org/abs/alg-geom/9703022 — 四条归一化性质：W(1)=1、右 GL_n^J(O_x) 不变、Ψ_x 等变、T_x^iW=q_x^{-i(i-1)/2}Tr(Λ^iγ)W；CS 值 q_x^{n(λ)}Tr(γ,V^λ)
- FGKV98：https://arxiv.org/abs/alg-geom/9703022 — CS 公式的 q^{-(μ,ρ)} 形式与唯一性
- FGKV98：https://arxiv.org/abs/alg-geom/9703022 — 卡3 KP4：「λ 为优势权时各项非负，指数为负」

## 关联

- `glc/concept/whittaker-character`
- `glc/concept/global-whittaker-function`
- `glc/concept/classical-hecke-eigenfunction`
