# Drinfeld chtouca（带水平结构）

> `lafforgue02/concept/drinfeld-chtouca` · 轨道 A · 镜像对称与几何 Langlands · 状态 dev

> **先自测**：Drinfeld 的 chtouca 由哪几条数据组成，水平结构又加在哪一处？

## 一句话

$X\times S$ 上一对秩 $r$ 丛的三角 $\mathcal E\to\mathcal E'\leftarrow\mathcal E''$ 加 $\tau\mathcal E\cong\mathcal E''$，修正只在 $\infty,0$ 两点；水平结构是 $N$ 处对 $\mathcal O^r$ 的平凡化。

## 定义

对 $\mathbb F_q$-概形 $S$，$S$ 上秩 $r$ 的 chtouca 是：$X\times S$ 上秩 $r$ 的丛 $\mathcal E$；$\mathcal E$ 的一次修正，即嵌入 $\mathcal E\xrightarrow{j}\mathcal E'\xleftarrow{t}\mathcal E''$，使 $\mathrm{Coker}\,j$ 与 $\mathrm{Coker}\,t$ 支撑于两个态射 $\infty,0:S\to X$ 的图像上且在 $\mathcal O_S$ 上可逆；以及同构 $\tau\mathcal E=(\mathrm{Id}_X\times\mathrm{Frob}_S)^*\mathcal E\xrightarrow{\sim}\mathcal E''$。水平结构 $N$ 是一个同构 $v:\mathcal E_N\xrightarrow{\sim}\mathcal O^r_{N\times S}$，并要求它在 $\mathcal E'_N,\mathcal E''_N$ 上诱导的平凡化与 $v$、$\tau v$ 相容。

**记号**：$\mathcal E\hookrightarrow\mathcal E'\hookleftarrow\mathcal E''\xleftarrow{\sim}\tau\mathcal E$ 常简记作 $\tilde{\mathcal E}$；$\mathrm{Cht}^r$、$\mathrm{Cht}^r_N$ 分别为秩 $r$ 的 chtouca 与带水平结构 $N$ 的 chtouca 之叠。

## 要点（为什么需要它）

1. 三条数据缺一不可：丛 $\mathcal E$；只在 $\infty,0$ 两点做修正的三角 $\mathcal E\to\mathcal E'\leftarrow\mathcal E''$；Frobenius 拉回与 $\mathcal E''$ 的同构。
2. 修正的余核必须「在 $\mathcal O_S$ 上可逆」，这一条把 chtouca 与任意的初等变换区分开：每一处修正恰好是秩 $1$ 的。
3. 水平结构不是 $\mathcal E$ 一个丛的平凡化，而是整条三角在 $N$ 上的相容平凡化——所以 $\mathrm{Cht}^r_N\to\mathrm{Cht}^r\times_{X\times X}(X-N)\times(X-N)$ 是 $\mathrm{GL}_r(\mathcal O_N)$-主丛。
4. 本讲义只在 $\mathrm{GL}_r$ 情形使用 chtouca；$\mathrm{chtouca}$ 与 $\mathrm{shtuka}$ 是同一对象的两种拼法，本译本保留原文不译（与本库 SY02-18 一致）。

## 核心公式

$$
$\mathcal E\xrightarrow{j}\mathcal E'\xleftarrow{t}\mathcal E''$，$\tau\mathcal E=(\mathrm{Id}_X\times\mathrm{Frob}_S)^*\mathcal E\xrightarrow{\sim}\mathcal E''$$v:\mathcal E_N=\mathcal E\otimes_{\mathcal O_X}\mathcal O_N\xrightarrow{\sim}\mathcal O^r_{N\times S}$$\mathrm{Cht}^r_N\to\mathrm{Cht}^r\times_{X\times X}(X-N)\times(X-N)$ 是 $\mathrm{GL}_r(\mathcal O_N)$-主丛
$$

$$
$v:\mathcal E_N=\mathcal E\otimes_{\mathcal O_X}\mathcal O_N\xrightarrow{\sim}\mathcal O^r_{N\times S}$
$$

$$
$\mathrm{Cht}^r_N\to\mathrm{Cht}^r\times_{X\times X}(X-N)\times(X-N)$ 是 $\mathrm{GL}_r(\mathcal O_N)$-主丛
$$

## 定理与证明（或缺口）

### chtouca 的模性质

$\mathrm{Cht}^r$ 与 $\mathrm{Cht}^r_N$ 是 Deligne–Mumford 意义下的代数叠；$(\infty,0):\mathrm{Cht}^r\to X\times X$ 是维数 $2r-2$ 的光滑态射；$\mathrm{Cht}^r_N\to\mathrm{Cht}^r\times_{X\times X}(X-N)\times(X-N)$ 可表、有限、étale Galois，群为 $\mathrm{GL}_r(\mathcal O_N)$。

> 证明状态：**sketch**。讲义未证明，只作为已知事实列出；本条按讲义原文复述，细节需回 [Lafforgue 2002] 或 Drinfeld 原始文献。

出处：`A p.6`

## 常见误解

- 别把 chtouca 当成 Higgs 丛或向量丛的推广：它的定义里同时有 $\mathcal E'$ 与 $\mathcal E''$ 两个修正，缺一个就退化成平凡对象。
- 水平结构要在 $\mathcal E,\mathcal E',\mathcal E''$ 三者上同时相容（$v$ 与 $\tau v$ 同汇于 $\mathcal O^r_{N\times S}$），只要求 $\mathcal E$ 平凡化是错的。
- $\infty$ 与 $0$ 是两个点态射 $S\to X$，「两点」是随 $S$ 变的，不是 $X$ 上固定的两个闭点。

## 相关卡

[chtouca 的模叠 $\mathrm{Cht}^r$ 与 $\mathrm{Cht}^r_N$](../concepts/chtouca-moduli-stack.md) · [Hecke 对应与 Hecke 代数](../concepts/hecke-correspondence.md) · [函数域上的 Langlands 对应（$\mathrm{GL}_r$）](../concepts/langlands-correspondence-function-field.md)

## 出处（印刷页）

- A p.5–6（A p.6）

> 说明：定义与叠性质全部照讲义 p.5–6 陈述（A 级）。「修正余核可逆」一句的解释性译注属上下文推断（B 级），讲义未展开。
