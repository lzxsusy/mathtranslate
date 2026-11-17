---
id: glc/concept/degenerate-whittaker-characters
type: concept
track: C
---

# 退化 Whittaker 特征标与抛物子群

> N(𝔸) 上在 N(K) 上平凡、经简单根商分解的特征标由 N(K)^⊥ ≃ K^{⊕(n-1)} 参数化，其 T(K)-轨道与含 B 的抛物子群一一对应，共 2^{n-1} 个。

**问题**：N(K)^⊥ 中的 T(K)-轨道与抛物子群怎样对应，一共有多少个？

## 定义

$N(\mathbb{A})$ 上在 $N(K)$ 上平凡且经由简单根商分解的特征标，由简单根坐标控制：$N(K)^\perp:=\{\chi:N(\mathbb{A})\to\overline{\mathbb{Q}}_\ell^\times\mid\chi|_{N(K)}=1\}_{\mathrm{sr}}\simeq K^{\oplus(n-1)}$，这里「sr」表示简单根商。环面 $T(K)$ 通过简单根作用，所有坐标非零的开子集等同于 $T_{\mathrm{ad}}(K)$；因此 $T(K)$-轨道由哪些简单根坐标非零来标记。等价地，$\{N(K)^\perp\text{ 中的 }T(K)\text{ 轨道}\}\longleftrightarrow\{J\subset\operatorname{Dyn}(G)\}\longleftrightarrow\{P\mid B\subset P\subset G\}$，故有 $2^{n-1}$ 个轨道。对 Levi 子群为 $M$ 的抛物子群 $P$，令 $J(P)$ 为 $M$ 的简单根集合，以 $\Psi_P:N(\mathbb{A})\to\overline{\mathbb{Q}}_\ell^\times$ 表示一个代表特征标，其简单根坐标恰好在 $J(P)$ 上非零。

*记号*：$\operatorname{Dyn}(G)$ 为 $G$ 的 Dynkin 图（简单根集 $\Delta$ 的指标集）；$T_{\mathrm{ad}}=T/Z(G)$；一般位置特征标记作 $\Psi=\Psi_G$，零特征标对应 $P=B$ 的轨道。

## 要点

- 一般位置特征标为 $\Psi=\Psi_G$（对应 $J=\Delta$，即 $P=G$）；零特征标则是与 $P=B$ 相联系的轨道（对应 $J=\varnothing$）。
- 扩展的 Piatetski-Shapiro–Shalika 定理使用所有这些 Fourier 系数；这是讲义所引 [FGKV98] 中 Whittaker 比较背后的函数论输入。
- 存在 Fourier 系数映射 $C^\infty(Q(K)\backslash G(\mathbb{A}))\to\prod_{P\supset B}C^\infty((Z_M(K)\ltimes N(\mathbb{A}),\Psi_P)\backslash G(\mathbb{A}))$，其中 $Q=\begin{pmatrix}\operatorname{GL}_{n-1}&V\\0&\mathbb{G}_m\end{pmatrix}$ 为型 $(n-1,1)$ 的极大抛物子群，$Z_M$ 是 $P$ 的 Levi 子群的中心并稳定 $\Psi_P$。
- 限制到尖点部分后，所有退化分量都为零，并与 $P=G$ 的因子等同，即非退化 Whittaker 系数；从 $Q$ 转到 $Q_1$ 后恢复 §3.5 的 mirabolic 定理。

## 关键公式

- $N(K)^\perp:=\{\chi:N(\mathbb{A})\to\overline{\mathbb{Q}}_\ell^\times\mid\chi|_{N(K)}=1\}_{\mathrm{sr}}\simeq K^{\oplus(n-1)}$
- $\{N(K)^\perp\text{ 中的 }T(K)\text{ 轨道}\}\longleftrightarrow\{J\subset\operatorname{Dyn}(G)\}\longleftrightarrow\{P\mid B\subset P\subset G\}$
- $C^\infty(Q(K)\backslash G(\mathbb{A}))\longrightarrow\prod_{P\supset B}C^\infty((Z_M(K)\ltimes N(\mathbb{A}),\Psi_P)\backslash G(\mathbb{A}))$

## 定理与证明

### Fourier 系数映射与尖点部分的退化分量（讲义引述）（要点（有缺口））

存在上述 Fourier 系数映射；限制到尖点部分后，所有退化分量都为零，并与 $P=G$ 的因子等同，即非退化 Whittaker 系数。

1. 对每个含 $B$ 的抛物 $P$ 取特征标 $\Psi_P$ 与 $Z_M(K)$-约化，定义对应的 Fourier 系数。  
   *为什么*：轨道分类给出 $P\mapsto\Psi_P$ 的对应。
2. 限制到尖点函数，说明退化分量消失。  
   *为什么*：讲义直接断言，未给证明；这是扩展 PS-S 定理的内容。

> 缺口：讲义只述不证；作为 [FGKV98] 中 Whittaker 比较的函数论输入引用。

*出处*：§3.8（原书 p.24）


## 易错点

- $N(K)^\perp$ 不是 $N(K)$ 在某个对偶里的正交补，而是「在 $N(K)$ 上平凡的特征标」的集合，下标 sr 表示它经简单根商分解；只考虑这一类特征标。
- 轨道数 $2^{n-1}$ 数的是 $J\subset\operatorname{Dyn}(G)$ 的子集，即含 $B$ 的抛物子群个数；不要把它读成 $2^n$。
- $\Psi_P$ 只在 $J(P)$ 上非零，$J(P)$ 是 Levi $M$ 的简单根集合；对 $P=G$ 得 $J(P)=\Delta$（一般位置），对 $P=B$ 得 $J(P)=\varnothing$（零特征标）。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§3.8 退化特征标与抛物子群，p.24（PDF p.24），`源码/chapters/ch03.tex:152-163（§3.8）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/parabolic+subgroup — T(K)-轨道↔{J⊂Dyn(G)}↔{P|B⊂P⊂G}，共 2^{n-1} 个
- nLab：https://ncatlab.org/nlab/show/Whittaker+function — N(K)^⊥≃K^{⊕(n-1)}；退化特征标按单根坐标分类

## 关联

- `glc/concept/iterated-fourier-transform`
- `glc/concept/mirabolic-whittaker-expansion`
- `glc/concept/generic-reduction-whittaker`
