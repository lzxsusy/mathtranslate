# Hecke 对应与 Hecke 代数

> `lafforgue02/concept/hecke-correspondence` · 轨道 A · 镜像对称与几何 Langlands · 状态 dev

> **先自测**：Hecke 对应是怎么由双陪集造出来的，它为什么不直接给出 Hecke 代数在紧化上同调的作用？

## 一句话

双陪集 $K_TgK_T$ 给出 $\mathrm{Cht}^r$ 上的有限型对应；它稳定截断开子叠，但在紧化上只「在不动点附近」稳定，故不能直接给出 $\mathcal H^r_N$ 的模作用。

## 定义

设 $g=(g_x)_{x\in|X|}\in\mathrm{GL}_r(\mathbb A)$，$T\subset|X|$ 有限使 $g_x\in K_x$ 对 $x\notin T$。取 $K_T=\prod_{x\in T}\mathrm{GL}_r(\mathcal O_x)$，双陪集 $K_TgK_T$ 定义 $\Cht^r$ 上的对应，即两个投影给出的「修正」关系。$\mathcal H^r$ 是这些双陪集张成的代数；带水平 $N$ 时取 $\mathcal H^r_N=\mathcal H(\mathrm{GL}_r(\mathbb A),K_N)$。

**记号**：$\mathcal H^r_N$ 作用在 $L^2(\mathrm{GL}_r(F)\backslash\mathrm{GL}_r(\mathbb A)/K_N)$ 上；几何侧它作用在 $\Cht^r_N$ 的上同调上。

## 要点（为什么需要它）

1. 对应由 $g$ 与有限集 $T$ 决定，$T$ 之外 $g$ 落在极大紧子群，故对应是有限型的。
2. 它稳定 $\Cht^{r,\overline p\le p}$ 以外的部分：截断开子叠被 Hecke 对应**不**稳定，这是第 II 章要对付的核心困难。
3. 在紧化上，Hecke 对应只「在不动点附近」保持 chtouca 开集；每个 $f\in\mathcal H^r_N$ 单独作用，但它们不满足结合律，故不定义 $\mathcal H^r_N$ 的作用。
4. 正因如此，本质部分上的计算要靠迹公式（不动点 + Lefschetz），而不是靠群作用。

## 核心公式

$$
$\mathcal H^r_N=\mathcal H(\mathrm{GL}_r(\mathbb A),K_N)$，$K_N=\ker(\mathrm{GL}_r(\widehat{\mathcal O})\to\mathrm{GL}_r(\mathcal O_N))$$f\in\mathcal H^r_N$ 作用在 $H^*_c(\overline{\Cht}^{\,r,\overline p\le p}_N/a^{\mathbb Z})$ 上稳定性定理：$f$ 稳定开集 $\overline{\Cht}^{\,r,\overline p\le p'}_N/a^{\mathbb Z}$
$$

$$
$f\in\mathcal H^r_N$ 作用在 $H^*_c(\overline{\Cht}^{\,r,\overline p\le p}_N/a^{\mathbb Z})$ 上
$$

$$
稳定性定理：$f$ 稳定开集 $\overline{\Cht}^{\,r,\overline p\le p'}_N/a^{\mathbb Z}$
$$

## 定理与证明（或缺口）

### Hecke 对应的稳定性（第 II 章）

对每个 $f\in\mathcal H^r_N$，$f$ 稳定开集 $\overline{\Cht}^{\,r,\overline p\le p'}_N/a^{\mathbb Z}$（即退化子避开 $N$ 的紧化开集）。

> 证明状态：**gap**。讲义第 II 章只陈述该稳定性定理并给出用途，证明放在 [Lafforgue 1997][Lafforgue 1998]；本译本未补。

出处：`A p.13`

## 常见误解

- 不要以为 $\mathcal H^r_N$ 在紧化上同调有一个模作用：恰恰相反，逐元素作用存在但不结合，讲义在 p.10 明确否定了这一点。
- 「稳定开集」中的开集依赖 $p'$，而 $p'$ 由 $f$ 决定；把 $p$ 当成与 $f$ 无关的常数是常见误读。

## 相关卡

[chtouca 的模叠 $\mathrm{Cht}^r$ 与 $\mathrm{Cht}^r_N$](../concepts/chtouca-moduli-stack.md) · [Harder–Narasimhan 截断与截断多边形](../concepts/harder-narasimhan-truncation.md) · [本质同调上的迹公式](../concepts/trace-formula-essential-cohomology.md)

## 出处（印刷页）

- A p.7–13（A p.7）

> 说明：Hecke 对应的构造取讲义 p.7–8；「在不动点附近稳定」与「不定义 $\mathcal H^r_N$ 作用」两句是 p.10 的原话（A 级）。
