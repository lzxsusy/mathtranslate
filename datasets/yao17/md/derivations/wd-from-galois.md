# 从 ℓ 进表示造出 (ρ, N)：引理 1.5 的构造五步

> `yao17/deriv/wd-from-galois` · 轨道 Weil–Deligne 侧 · 状态 dev · 5 步

> **要回答的问题**：给定 ρ:G_K→GL_n(Q̄_ℓ)，具体怎么变出一对 (ρ, N)？N 为什么一定幂零、又为什么满足 ρ(τ)Nρ(τ)^{-1}=q^{-n}N？

## 一句话

把 ℓ 进表示先模 ℓ、再沿惯性群的 ℓ 进商分解，取 N=log ρ(σ) 即得 Weil–Deligne 表示。

## 目标

对任意 ρ:G_K→GL_n(Q̄_ℓ)，构造 $N$ 使 $(\rho,N)$ 是 Weil–Deligne 表示，即引出理 1.5 的满性。

## 前提

- $K$ 是 $p$ 进局部域，$p\neq\ell$，$q$ 为剩余域大小；$G_K$ 是绝对 Galois 群，$I_K$ 是惯性群，$P_K$ 是野惯性群。
- $\rho\colon G_K\to\GL_n(\overline{\mathbb Q}_\ell)$ 是连续表示；$t_\ell\colon I_K\to\mathbb Z_\ell(1)$ 是惯性群的驯商同构。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 取 $G_K$ 在 $\overline{\mathbb Q}_\ell^n$ 中的稳定 $\mathcal O_L$ 格 $\Lambda$（$L/\mathbb Q_\ell$ 充分大，$\mathcal O_L$ 是其整数环），模 $\ell$ 得 $\rho_\Lambda\colon G_K\to\Aut_{\mathbb F_\ell}(\Lambda/\ell)$。 | 模 $\ell$ 把「$\ell$ 进」信息压成有限域上作用，使后面的核与商都是 pro-$\ell$ 群，从而可以由 $t_\ell$ 参数化。 | `A p.7` | A·原文明确写了 |
| 2 | 置 $G_{K''}=\ker\rho_\Lambda$。它是指标有限的闭正规子群，故 $K''/K$ 是有限扩张；记 $q_{K''}$ 为 $K''$ 的剩余域大小。 | 指标有限保证「模 $\ell$ 的核」仍是一个开子群，后续的惯性群 $I_{K''}$ 才有意义。 | `A p.7` | A·原文明确写了 |
| 3 | 由 $\rho_\Lambda\|_{I_{K''}}$ 的核是 pro-$\ell$ 群，得 $\rho\colon I_{K''}\to\GL_n(\overline{\mathbb Q}_\ell)$ 通过 $t_\ell\colon I_{K''}\to\mathbb Z_\ell(1)$ 分解，即存在 $g\in\GL_n(\overline{\mathbb Q}_\ell)$ 与 $a\in\mathbb Z_\ell$ 使 $\rho\|_{I_{K''}}=\exp(t_\ell\cdot g)$。 | 这一步是全部构造的核心：惯性群在 $\ell$ 进表示上的作用由单个幂零「生成元」$g$ 决定，$N$ 就取它。 | `A p.7` | A·原文明确写了 |
| 4 | 取 $t_\ell$ 的一个拓扑生成元 $\sigma\in I_{K''}$（即 $t_\ell(\sigma)=1$），令 $N=\log\rho(\sigma)$。由于 $\rho(\sigma)$ 幂幺，$N$ 是幂零矩阵。 | $\sigma$ 的选取不唯一，但换一个生成元只差整数倍，$N$ 相应乘标量；配合下面的共轭关系可证 $(\rho,N)$ 良定。 | `A p.8` | A·原文明确写了 |
| 5 | 对 $\sigma\in I_{K''}$ 与 $\tau\in G_K$，由 $\tau\sigma\tau^{-1}$ 的 $t_\ell$ 像得 $\rho(\tau)N\rho(\tau)^{-1}=\|\Art\tau\|^{-1}N$；把 $\rho$ 用半单部分 $r$ 与局部类域论 $\Art$ 改写，即得 $r(\tau)N r(\tau)^{-1}=q^{-n}N$，其中 $n$ 由 $r(\tau)$ 在 $\|\cdot\|$ 上的取值决定。 | 这条共轭关系正是定义 1.1.3 的 (iii)；它保证了 $N$ 落在 $r$ 的「$-2$ 权重」部分，是 Weil–Deligne 表示定义中不可省的一环。 | `A p.8` | A·原文明确写了 |

## 结论

每给一个 $\rho\colon G_K\to\GL_n(\overline{\mathbb Q}_\ell)$ 就能造出 $(\rho,N)$：$\rho$ 取半单部分、$N=\log\rho(\sigma)$，且 $N$ 幂零并满足 $\rho(\tau)N\rho(\tau)^{-1}=q^{-n}N$。故引理 1.5 的映射 $\rho\mapsto(\rho,N)$ 是满的，配合引理 1.2 的单性即得 $\WD$ 是范畴等价（推论 1.7）。

## 缺口

- 第 5 步的 $|\Art\tau|^{-1}$ 到 $q^{-n}$ 的换算底本只写「由此得到」，未逐步展开 $\Art$ 与 $|\cdot|$ 的相容性。
- $N$ 与生成元选取的无关性（换 $\sigma$ 只改标量）底本作显然处理。

## 最容易讲错的地方

- 第 3 步的核「是 pro-$\ell$ 群」用的是 $\Lambda/\ell$ 上作用为平凡，而非 $\rho$ 本身；若一开始就对 $\rho$ 取核会得到平凡群，什么都推不出来。
- $N=\log\rho(\sigma)$ 需要 $\rho(\sigma)$ 幂幺（即 $\equiv1\bmod\ell$ 的 $\ell$ 元素），这一步依赖第 3 步的分解，不能对任意 $\rho(\sigma)$ 直接取对数。
- 共轭关系里出现的是半单部分 $r$ 而不是 $\rho$ 本身；底本在 p.8 明说「$\rho$ 换成其半单化不影响 $N$ 的共轭关系」。

## 相关卡

[Weil–Deligne 表示 (ρ, N) 及其基本性质](../concepts/wd-representation.md) · [Grothendieck 单值化定理、WD 函子与惯性类型](../concepts/wd-functor.md) · [φ-半单（Frobenius 半单）与引理 1.2](../concepts/frobenius-semisimple.md)

## 出处（印刷页）

- A p.7–8（A p.7）

> 说明：五步构造依底本引理 1.5 的证明整理（p.7–p.8）；底本证明较简，第 3、5 步的细节由我们补足并标注为「我们的整理」。
