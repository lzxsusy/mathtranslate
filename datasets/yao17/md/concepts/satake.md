# 球面 Hecke 代数与 Satake 同构、非分歧表示

> `yao17/concept/satake` · 轨道 自守侧 · 状态 dev

> **先自测**：为什么 H(G//C) 对 GL_n 是交换的？Satake 同构在这个具体情形下写成什么？「非分歧表示」由此得到什么结构？

## 一句话

H(G//C) 交换，且 ≅ C[t_1^{±1},…,t_n^{±1}]^{S_n}；故不可约容许 π 的 π^C 或为 0 或一维，「非分歧」即 π^C≠0。

## 定义

设 $G=\GL_n(K)$，$C=\GL_n(\mathcal O_K)$ 是极大紧开子群，则 $H(G/\!/C)\xrightarrow{\sim}\mathbb C[t_1^{\pm1},\dots,t_n^{\pm1}]^{S_n}$，特别地交换。更一般地，$G$ 分裂约化、$C$ 超特殊时，经典 Satake 同构为 $H(G/\!/C)\xrightarrow{\sim}(\mathcal O\hat T)^W$，其中 $\hat T=\Spec\mathbb C[\Lambda]$，$\Lambda$ 是余权格，$W$ 是 Weyl 群。由推论 2.3，不可约容许 $\pi$ 的 $\pi^C$ 或为 0 或一维；称 $\pi$ 非分歧（unramified），若 $\pi^C\neq 0$。

**记号**：$t_i$ 是 $\mathrm{diag}(\varpi,\dots,\varpi,1,\dots,1)$ 型双陪集的像；$\Lambda$ 是余权格，$\mathcal O\hat T=\mathbb C[\Lambda]$。

## 要点（为什么需要它）

1. Gelfand 技巧给出 GL_n 情形的交换性：$C\backslash G/C\cong G\backslash(G/C\times G/C)$，而 $G/C$ 参数化 $K^n$ 中的格子，故双陪集 = 一对格子的相对位置；$(\Lambda,\Lambda')$ 与 $((\Lambda')^\vee,\Lambda^\vee)$ 相对位置相同，于是卷积可交换——底本说这证明「几乎同义反复」。
2. Satake 同构的一般形式 $(\mathcal O\hat T)^W$ 说明球面 Hecke 代数是「余权环的 Weyl 不变量」，其极大谱是 $\hat T/W$——这就是 Satake 参数（半单共轭类）的栖身处。
3. 非分歧表示的定义 $\pi^C\neq0$ 与「$\pi$ 有一维 $C$-固定子空间」等价（推论 2.3），故非分歧表示必是某个未分歧主序列的不可约商；底本的原始定义只用到 $\dim\pi^C=1$ 这一点。
4. 对 GL_n，$H(G/\!/C)$ 同构于对称多项式环，故 $\pi$ 的非分歧性完全由「$\pi^C$ 上的 $H(G/\!/C)$-作用给出的 $n$ 个特征标 $t_i$」编码，这组 $t_i$ 就是 Satake 参数。

## 核心公式

$$
$H(G/\!/C)\xrightarrow{\ \sim\ }\mathbb C[t_1^{\pm1},\dots,t_n^{\pm1}]^{S_n}$$H(G/\!/C)\xrightarrow{\ \sim\ }(\mathcal O\hat T)^W,\qquad \hat T=\Spec\mathbb C[\Lambda]$$C\backslash G/C\ \cong\ G\backslash(K^n\text{ 中的格子对}),\qquad (\varphi\ast\psi)(\Lambda,\Lambda')=\sum_{\Lambda''}\varphi(\Lambda,\Lambda'')\psi(\Lambda'',\Lambda')$
$$

$$
$H(G/\!/C)\xrightarrow{\ \sim\ }(\mathcal O\hat T)^W,\qquad \hat T=\Spec\mathbb C[\Lambda]$
$$

$$
$C\backslash G/C\ \cong\ G\backslash(K^n\text{ 中的格子对}),\qquad (\varphi\ast\psi)(\Lambda,\Lambda')=\sum_{\Lambda''}\varphi(\Lambda,\Lambda'')\psi(\Lambda'',\Lambda')$
$$

## 定理与证明（或缺口）

### 推论 2.3 + 推论-定义（非分歧表示）

$V\in\Rep^\infty_G$ 不可约且 $H(G/\!/K)$ 交换 $\Rightarrow$ $V^K=0$ 或 $\dim V^K=1$；取 $K=C=\GL_n(\mathcal O_K)$ 时称 $V^C\neq0$ 的 $\pi$ 为非分歧。

1. 由引理 2.2(2)，不可约 $V$ 且 $V^K\neq0$ 时 $V^K$ 是不可约 $H(G/\!/K)$-模。
   - *为什么*：Casselman 引理把 $K$-固定向量上的作用精确化为 $H(G/\!/K)$-模结构，且不可约性传递。
2. 若 $H(G/\!/K)$ 交换，则其任一不可约模都是一维的（Schur 引理：交换代数的不可约模 = 其特征标）。
   - *为什么*：允许用 Schur 引理，因为 $V^K$ 已是有限维 $H(G/\!/K)$-模，不依赖定理 2.5。

出处：`A §2.1.6 p.14`

## 常见误解

- Satake 同构的交换性依赖 $C$ 是超特殊（hyperspecial）的；换成一般极大紧子群 $K$，$H(G/\!/K)$ 未必交换，推论 2.3 也就用不上。
- 非分歧是「存在非零 $C$-固定向量」，不是「$\pi$ 本身非分歧扩张」；对应到 Galois 侧是 $\rec_n(\pi)$ 在 $I_K$ 上平凡（$N=0$ 且 $\rho|_{I_K}=0$），两者不可混淆。

## 相关卡

[Hecke 代数 H(G)、双陪集子代数与 「光滑表示 ≃ 非退化 Hecke 模」](../concepts/hecke-modules.md) · [光滑表示、容许表示与反变对偶](../concepts/smooth-admissible.md) · [局部 Langlands 对应：定理 2.13 的五条性质](../concepts/llc-statement.md)

## 出处（印刷页）

- A p.14（A p.14）

> 说明：Satake 同构、Gelfand 技巧与推论-定义照 p.14；「Satake 参数 = 双陪集代数的特征标 $t_i$」的解释是我们的判断（底本未在 §2.1 展开 Satake 参数）。
