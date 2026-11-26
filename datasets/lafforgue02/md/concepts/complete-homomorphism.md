# 完整同态（homomorphisme complet）

> `lafforgue02/concept/complete-homomorphism` · 轨道 A · 镜像对称与几何 Langlands · 状态 dev

> **先自测**：把「同构」放宽成「完整同态」，究竟补进了哪些数据，为什么这些数据足以让紧化光滑？

## 一句话

把 chtouca 定义里的「同构 $\tau\mathcal E\cong\mathcal E''$」放宽成同态 $\tau\mathcal E\Rightarrow\mathcal E''$，并记下逐级退化的数据 $(\mathcal L_s,\ell_s,v_s)$；这放宽后的模问题给出第 III 章的紧化。

## 定义

设 $\mathcal F,\mathcal E$ 是 $X\times S$ 上秩 $r$ 的丛。一个完整同态 $\mathcal F\Rightarrow\mathcal E$ 由以下数据组成：对每个 $1\le s<r$，一个可逆层 $\mathcal L_s$ 与截面 $\ell_s:\mathcal O_S\to\mathcal L_s$；以及对每个 $1\le s\le r$ 的同态 $v_s:\Lambda^s\mathcal F\otimes\bigotimes_{t<s}\mathcal L_t^{\otimes(s-t)}\to\Lambda^s\mathcal E$，满足若干相容条件（可逆处给出 $\mathcal F\to\mathcal E$ 的滤过同构）。型 $\underline r=(r=r_1+\cdots+r_k)$ 由「哪些 $\ell_s$ 为零」决定。

**记号**：$\mathcal F\Rightarrow\mathcal E$；层 $\mathcal L_s$、截面 $\ell_s$、同态 $v_s$；完整同态概形 $\Omega^r$。

## 要点（为什么需要它）

1. 放宽只发生在第 (iii) 条（$\tau\mathcal E\cong\mathcal E''$ 变成同态），前两条（丛与修正）不变；这样开子叠仍是原来的 chtouca。
2. 每级 $s$ 都记一个可逆层 $\mathcal L_s$ 与截面 $\ell_s$：$\ell_s\ne0$ 时该级是同构，$\ell_s=0$ 时该级退化——这就是边界的来源。
3. 型 $\underline r$ 由 $\ell_s$ 为零的位置决定（$s\in\underline r^-\cap\underline r^+$ 时 $\ell_s=0$），不同的型给出不同的边界分层。
4. $\Omega^r$ 是把 $M_r-\{0\}$ 逐次沿「秩 $\le1$、$\le2$、…」的矩阵闭子概形爆炸得到的概形，用来参数化这些 $(\mathcal L_s,\ell_s)$。

## 核心公式

$$
$v_s:\Lambda^s\mathcal F\otimes\bigotimes_{t<s}\mathcal L_t^{\otimes(s-t)}\longrightarrow\Lambda^s\mathcal E$，$1\le s\le r$$\Omega^r=\mathrm{Bl}_{\cdots}\cdots\mathrm{Bl}_{\{\mathrm{rg}\le1\}}(M_r-\{0\})$$\ell_s=0\iff s\in\underline r^-\cap\underline r^+$
$$

$$
$\Omega^r=\mathrm{Bl}_{\cdots}\cdots\mathrm{Bl}_{\{\mathrm{rg}\le1\}}(M_r-\{0\})$
$$

$$
$\ell_s=0\iff s\in\underline r^-\cap\underline r^+$
$$

## 定理与证明（或缺口）

### 完整同态的模解释

$S$ 上带完整同态 $\tau\mathcal E\Rightarrow\mathcal E''$ 的迭代 chtouca 之叠，恰是把第 (iii) 条由同构放宽为完整同态后的模问题的解；其开子叠（$\ell_s$ 全非零）就是原来的 $\Cht^{r,\ol p\le p}$。

> 证明状态：**sketch**。讲义给出构造与型的定义，相容条件的完整列表与 $\Omega^r$ 的爆炸细节只作提示，未逐条列出。

出处：`A p.22`

## 常见误解

- 「完整」不是「满」：complete 在这里指「把全部退化数据都记下来」，不是满射。
- 完整同态不是同态 $\mathcal F\to\mathcal E$：它是一族 $v_s$ 加上 $(\mathcal L_s,\ell_s)$，单看 $v_1$ 会丢掉边界信息。

## 相关卡

[fourre-tout（不分离的「杂物袋」叠）](../concepts/fourre-tout.md) · [迭代 $\varphi$-格](../concepts/iterated-phi-lattice.md) · [从截断到紧化：三个对象与三次取舍](../derivations/truncation-to-compactification.md)

## 出处（印刷页）

- A p.20–23（A p.22）

> 说明：完整同态的定义取讲义 p.20–22（$\Omega^r$ 的爆炸构造在 p.23）；相容条件讲义只列要点，本卡按原文的范围复述，未补全。
