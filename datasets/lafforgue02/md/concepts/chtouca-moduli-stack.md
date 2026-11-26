# chtouca 的模叠 $\mathrm{Cht}^r$ 与 $\mathrm{Cht}^r_N$

> `lafforgue02/concept/chtouca-moduli-stack` · 轨道 A · 镜像对称与几何 Langlands · 状态 dev

> **先自测**：chtouca 的模空间是什么类型的对象，它到 $X\times X$ 的态射有几维、为什么非有限型？

## 一句话

$\mathrm{Cht}^r$ 是秩 $r$ chtouca 的 DM 叠，$(\infty,0)$ 光滑地映到 $X\times X$、维数 $2r-2$；它是 $d$ 上无穷并，故非有限型——这正是要截断的理由。

## 定义

$\mathrm{Cht}^r$ 是秩 $r$ 的 chtouca 之叠，$\mathrm{Cht}^r_N$ 是带水平结构 $N$ 者之叠，两者都是 Deligne–Mumford 意义下的代数叠；$(\infty,0):\mathrm{Cht}^r\to X\times X$ 是维数 $2r-2$ 的光滑态射。$\mathrm{Cht}^r$ 按次数 $d=\deg\mathcal E$ 分解为无穷并 $\coprod_{d\in\mathbb Z}\mathrm{Cht}^{r,d}$。

**记号**：$\Cht^r=\coprod_d\Cht^{r,d}$；$a$ 是 $X$ 上次数 $>0$ 的可逆层，$a^{\mathbb Z}$ 通过张量积作用在每个 $\Cht^{r,d}$ 上。

## 要点（为什么需要它）

1. 光滑不等于紧合：$(\infty,0)$ 光滑，但 $\Cht^r$ 不在 $X\times X$ 上紧合，也不有限型。
2. 非有限型的根源是次数 $d$ 可任意大：$\Cht^r$ 是 $\mathrm{GL}_r$ 的 chtouca 在全部次数上的并，而每个 $\Cht^{r,d}$ 才是有限型的候选。
3. 取商 $\Cht^r/a^{\mathbb Z}$ 把次数差掉，但维数仍随 $d$ 变；因此不动点计数必须先固定截断多边形 $p$。
4. 带水平结构 $N$ 时，$\Cht^r_N\to\Cht^r\times_{X\times X}(X-N)\times(X-N)$ 是 $\mathrm{GL}_r(\mathcal O_N)$-主丛，因而可表、有限、étale Galois。

## 核心公式

$$
$\mathrm{Cht}^r=\coprod_{d\in\mathbb Z}\mathrm{Cht}^{r,d}$$(\infty,0):\Cht^r\to X\times X$ 光滑，维数 $2r-2$$\Cht^r_N\to\Cht^r\times_{X\times X}(X-N)\times(X-N)$ 是 $\mathrm{GL}_r(\mathcal O_N)$-主丛
$$

$$
$(\infty,0):\Cht^r\to X\times X$ 光滑，维数 $2r-2$
$$

$$
$\Cht^r_N\to\Cht^r\times_{X\times X}(X-N)\times(X-N)$ 是 $\mathrm{GL}_r(\mathcal O_N)$-主丛
$$

## 定理与证明（或缺口）

### 截断开子叠的有限型性

对足够凸的截断多边形 $p$，$\Cht^{r,\overline p\le p}_N/a^{\mathbb Z}$ 是有限型且分离的，并在 $X\times X$ 上紧合（无水平情形）。

> 证明状态：**sketch**。本卡按讲义陈述复述；讲义把证明完全交给 [Lafforgue 1997]，本译本亦未补。

出处：`A p.9`

## 常见误解

- $\Cht^r$ 上「$a^{\mathbb Z}$-商」不等于「取有限型」：商掉次数不改变每个纤维的维数随 $d$ 发散的事实。
- 无水平（$N=\varnothing$）与有水平（$N\ne\varnothing$）的紧合性不同：前者紧合光滑，后者只紧合不光滑，需再取「退化子避开 $N$」的开集。

## 相关卡

[Drinfeld chtouca（带水平结构）](../concepts/drinfeld-chtouca.md) · [Harder–Narasimhan 截断与截断多边形](../concepts/harder-narasimhan-truncation.md) · [Hecke 对应与 Hecke 代数](../concepts/hecke-correspondence.md)

## 出处（印刷页）

- A p.6–9（A p.6）

> 说明：叠性质与维数出自讲义 p.6；非有限型与截断后有限型的命题出自 p.9–10。$d$ 的并式为讲义 p.8 的写法。
