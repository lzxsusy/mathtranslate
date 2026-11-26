# fourre-tout（不分离的「杂物袋」叠）

> `lafforgue02/concept/fourre-tout` · 轨道 A · 镜像对称与几何 Langlands · 状态 dev

> **先自测**：为什么要造一个不分离的「fourre-tout」，它比直接造紧化多解决了什么？

## 一句话

第 III 章用一个不分离的叠 $\ol{\Cht}^{\,r}$ 把所有截断紧化都收作开子叠，讲义称之为 fourre-tout；它的边界分层给出 $\Cht^r_{\underline r}\to\Cht^{r_1}\times_X\cdots$ 的逐层分解。

## 定义

fourre-tout 指 $\ol{\Cht}^{\,r}=\coprod_d\ol{\Cht}^{\,r,d}$，即 $X$ 上「迭代 chtouca」的叠：它把每个截断多边形对应的紧化作为开子叠容纳其中。它是一个局部有限型、**不分离**的代数叠，带态射 $\ol{\Cht}^{\,r}\to X\times X\times(\mathbb A^1/\mathbb G_m)^{r-1}$，后者用划分 $\underline r=(r=r_1+\cdots+r_k)$ 给边界分层编号。

**记号**：$\ol{\Cht}^{\,r}$；分层 $\Cht^r_{\underline r}$，开分层 $\Cht^r_{\underline 0}=\Cht^r$。

## 要点（为什么需要它）

1. motivation：不同的截断多边形给出不同的紧化，它们彼此并不相容；先把它们全部放进同一个（不分离的）叠里，再在它里面按 $p$ 切出各自的开紧化。
2. 代价是不分离——叠不再是分离的，因此不能再直接谈「紧合」；紧合性要在切出的开子叠上逐条验证（第四章）。
3. 收益是分层结构清楚：$\Cht^r_{\underline r}$ 覆盖边界，且每个分层带有限、满、根式的态射到低秩 chtouca 的乘积，使归纳得以进行。
4. 「迭代 chtouca」是 fourre-tout 的几何内容：每条 chtouca 的数据都被替换为一串完整同态与可逆层，沿划分逐段记录退化。

## 核心公式

$$
$\ol{\Cht}^{\,r}=\coprod_{d}\ol{\Cht}^{\,r,d}$，局部有限型、不分离$\ol{\Cht}^{\,r}\to X\times X\times(\mathbb A^1/\mathbb G_m)^{r-1}$$\Cht^r_{\underline r}\to\Cht^{r_1}\times_X{}^{r_2}\Cht\times_X\cdots\times_X{}^{r_k}\Cht$ 有限、满、根式
$$

$$
$\ol{\Cht}^{\,r}\to X\times X\times(\mathbb A^1/\mathbb G_m)^{r-1}$
$$

$$
$\Cht^r_{\underline r}\to\Cht^{r_1}\times_X{}^{r_2}\Cht\times_X\cdots\times_X{}^{r_k}\Cht$ 有限、满、根式
$$

## 定理与证明（或缺口）

### 边界分层的逐层分解

$\ol{\Cht}^{\,r}\to X\times X\times(\mathbb A^1/\mathbb G_m)^{r-1}$ 关于划分 $\underline r$ 的纤维是局部闭分层 $\Cht^r_{\underline r}$；开分层 $\Cht^r_{\underline 0}=\Cht^r$；其余各分层带有限满根式态射到 $\Cht^{r_1}\times_X\cdots\times_X\Cht^{r_k}$。

> 证明状态：**sketch**。讲义只陈述该命题（p.26）并说明由构造给出，未逐条验证根式性；本卡按陈述复述。

出处：`A p.26`

## 常见误解

- 不要把它当成某个 $p$ 的紧化：fourre-tout 本人不紧合、不分离，紧化是它里面的开子叠。
- $\ol{\Cht}^{\,r}$ 的「点」是带完整同态的迭代结构，不是普通 chtouca 加一个边界点；把它当「chtouca 的紧化点」会读错分层。

## 相关卡

[完整同态（homomorphisme complet）](../concepts/complete-homomorphism.md) · [chtouca 的模叠 $\mathrm{Cht}^r$ 与 $\mathrm{Cht}^r_N$](../concepts/chtouca-moduli-stack.md) · [从截断到紧化：三个对象与三次取舍](../derivations/truncation-to-compactification.md)

## 出处（印刷页）

- A p.19–26（A p.19）

> 说明：「fourre-tout」的定义与用途取引言 p.2 与第 III 章 p.19–20；分层与根式态射取 p.26。术语保留法文原词不译，理由见译本《译者说明》。
