# Harder–Narasimhan 截断与截断多边形

> `lafforgue02/concept/harder-narasimhan-truncation` · 轨道 A · 镜像对称与几何 Langlands · 状态 dev

> **先自测**：截断多边形 $p$ 为什么要「足够凸」，截断之后失去了什么、又得到了什么？

## 一句话

给秩 $r$ 丛按 Harder–Narasimhan 多边形排序，用足够凸的截断多边形 $p:[0,r]\to\mathbb R_+$ 切出 $\Cht^{r,\overline p\le p}$；这是有限型、承载不动点计数的开子叠。

## 定义

对 chtouca 中的丛 $\mathcal E$ 及其 Harder–Narasimhan 多边形 $\overline p:[0,r]\to\mathbb R$，条件 $\overline p\le p$（逐点比较）定义 $\Cht^{r}$ 的开子叠 $\Cht^{r,\overline p\le p}$。$p$ 称足够凸，若它使该开子叠有限型且在 $X\times X$ 上紧合。

**记号**：$p:[0,r]\to\mathbb R_+$，$p(0)=0$，$p$ 凸且递增；$\overline p$ 是具体 chtouca 的 HN 多边形。

## 要点（为什么需要它）

1. 截断是「按斜率排序后砍掉太不稳定的部分」，不是按次数砍；次数 $d$ 仍取遍 $\mathbb Z$。
2. $p$ 的凸性保证截断后仍对 Hecke 对应「局部」稳定，并在紧化边界上给出可计算的 DCN 分层。
3. 代价：截断开子叠不再被 Hecke 对应整体稳定；收益：有限型 + 不动点公式有意义。
4. 足够凸的阈值依赖 $X$ 的亏格，讲义明确写出「(en fonction du genre de $X$)」。

## 核心公式

$$
$\Cht^{r,\overline p\le p}_N/a^{\mathbb Z}=\coprod_{1\le d\le r|\deg(a)|}\Cht^{r,d,\overline p\le p}_N/a^{\mathbb Z}$$\overline p\le p$ 逐点比较，$p:[0,r]\to\mathbb R_+$$\ol{\Cht}^{\,r,d,\overline p\le p}$ 在 $X\times X$ 上紧合且光滑（$N=\varnothing$）
$$

$$
$\overline p\le p$ 逐点比较，$p:[0,r]\to\mathbb R_+$
$$

$$
$\ol{\Cht}^{\,r,d,\overline p\le p}$ 在 $X\times X$ 上紧合且光滑（$N=\varnothing$）
$$

## 定理与证明（或缺口）

### 截断的有限型性

若 $p$ 足够凸，则 $\Cht^{r,\overline p\le p}_N/a^{\mathbb Z}$ 有限型；其紧化 $\ol{\Cht}^{\,r,d,\overline p\le p}$ 在 $X\times X$ 上紧合且光滑。

> 证明状态：**sketch**。讲义只陈述结论；有限型的「有限段」论证与紧合性均引自 [Lafforgue 1997]，本译本未补证。

出处：`A p.9`

## 常见误解

- 「凸」是分段线性函数的凸性，不是几何图形的凸；原文 p.33 的一幅图与文字描述的凸性并不完全吻合，本译本照译并已在《疑点清单》登记。
- $p$ 的上界对 $[0,r]$ 全区间生效，只约束端点 $p(r)$ 是错的。

## 相关卡

[chtouca 的模叠 $\mathrm{Cht}^r$ 与 $\mathrm{Cht}^r_N$](../concepts/chtouca-moduli-stack.md) · [Hecke 对应与 Hecke 代数](../concepts/hecke-correspondence.md) · [从截断到紧化：三个对象与三次取舍](../derivations/truncation-to-compactification.md)

## 出处（印刷页）

- A p.9–10（A p.9）

> 说明：截断定义与命题取讲义 p.9；「足够凸依赖亏格」一句是 p.10 的原话。「代价/收益」两行是本卡对第 II 章动机的归纳（B 级）。
