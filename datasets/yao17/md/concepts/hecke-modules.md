# Hecke 代数 H(G)、双陪集子代数与 「光滑表示 ≃ 非退化 Hecke 模」

> `yao17/concept/hecke-modules` · 轨道 自守侧 · 状态 dev

> **先自测**：H(G) 没有单位元，为什么还能有「非退化模 ≃ 光滑表示」的等价？Casselman 引理 2.2 又需要什么额外条件？

## 一句话

H(G) 是紧支局部常值函数的卷积代数；引理 2.1 给出 Rep^∞_G ≃ 非退化 H(G)-模，引理 2.2 把容许性换到有限维 H(G//K)-模上。

## 定义

取 Haar 测度使 $\mu(K_0)=1$。(1) $H(G)=\{f\colon G\to\mathbb C\ \text{紧支局部常值}\}$，卷积 $(f_1\ast f_2)(h)=\int_Gf_1(hg^{-1})f_2(g)dg$；(2) 对紧开子群 $K$，$H(G/\!/K)$ 是左右 $K$-不变的子代数，有双边单位 $e_K=\frac{1}{\Vol(K)}\mathbf 1_K$；(3) $H(G)$ 无单位，但 $H(G)=\bigcup_K H(G/\!/K)$，各 $H(G/\!/K)$ 的单位 $e_K$ 不同。引理 2.1：$\Rep^\infty_G\to\{\text{非退化 }H(G)\text{-模}\}$ 是范畴等价。

**记号**：$f\star v=\pi(f)v=\int_Gf(g)\pi(g)v\,dg$；非退化指 $H(G)V=V$；$e_{gK}=\frac{1}{\mu(K)}\mathbf 1_{gK}$。

## 要点（为什么需要它）

1. 引理 2.1 的逆函子靠一件小事：对任一 $m$，总可取足够小的 $K$ 使 $e_K\star m=m$，然后定义 $g\cdot m:=e_{gK}\star m$；良定义性用恒等式 $e_{gK'}\ast e_K=e_{gK}$（$K'\subset K$）。
2. 「作用律」是证明里唯一不平凡的地方：要证 $e_{g_1K'}\ast e_{g_2K}=e_{g_1g_2K}$，其中取 $K'=g_2Kg_2^{-1}\cap K$ 再缩小到稳定 $m'$；底本在 2.1.4 的注里给了更漂亮的说法：$H(G)\otimes_{H(G)}M\xrightarrow{\sim}M$ 是同构，于是借左作用搬来 $G$-作用。
3. 引理 2.2（Casselman）：固定 $K$，$V\mapsto V^K$ 给出「所有不可约子商都含 $K$-固定向量」的有限长容许表示与有限维 $H(G/\!/K)$-模的等价；不可约 $V$ 且 $V^K\neq 0$ 时 $V^K$ 是不可约 $H(G/\!/K)$-模。
4. 推论 2.3：若 $V$ 不可约光滑且 $H(G/\!/K)$ 交换，则 $V^K=0$ 或 $\dim V^K=1$——这条在 $G=\GL_n$、$K=\GL_n(\mathcal O_K)$ 时直接给出「非分歧表示」的整维性。

## 核心公式

$$
$(f_1\ast f_2)(h)=\int_Gf_1(hg^{-1})f_2(g)\,dg=\int_Gf_1(g)f_2(g^{-1}h)\,dg$$e_{gK'}\ast e_K=e_{gK}\quad(K'\subset K),\qquad H(G)=\bigcup_K H(G/\!/K)$$\Rep^\infty_G\ \simeq\ \{\text{非退化 }H(G)\text{-模}\},\qquad \Rep^{\mathrm{adm}}_G|_K\ \simeq\ H(G/\!/K)\text{-mod}^{\mathrm{f.d.}}$
$$

$$
$e_{gK'}\ast e_K=e_{gK}\quad(K'\subset K),\qquad H(G)=\bigcup_K H(G/\!/K)$
$$

$$
$\Rep^\infty_G\ \simeq\ \{\text{非退化 }H(G)\text{-模}\},\qquad \Rep^{\mathrm{adm}}_G|_K\ \simeq\ H(G/\!/K)\text{-mod}^{\mathrm{f.d.}}$
$$

## 定理与证明（或缺口）

### 引理 2.1（光滑表示与 Hecke 模的等价）

$\Rep^\infty_G\to\{H(G)\text{ 的非退化模}\}$，$V\mapsto V$ 配 $f\star v=\pi(f)v$，是范畴等价。

> 证明状态：**sketch**。底本给了全忠实性的断言与逆函子的完整构造思路，但「作用律」部分的细节以「有点 tricky」带过（p.13 末给出 $H(G)\otimes M\cong M$ 的替代论证）。

出处：`A §2.1.4 p.12–p.13`

### 引理 2.2（Casselman）

固定紧开 $K$：$V\mapsto V^K$ 从「有限长、所有不可约子商都有 $K$-固定向量」的容许表示等价到有限维 $H(G/\!/K)$-模；并给出不可约光滑表示与不可约 $H(G/\!/K)$-模的双射。

> 证明状态：**cited**。底本只陈述（Casselman 的标准结果），未给证明。

出处：`A §2.1.5 p.13`

## 常见误解

- $H(G)$ 无单位元，所以「模」必须是非退化的（$H(G)V=V$）；丢掉这条会得到没有对应表示的病态模。
- 引理 2.2 的条件「所有不可约子商都有 $K$-固定向量」不能省：否则 $V\mapsto V^K$ 会在含「无 $K$-固定向量」子商的表示上丢信息。

## 相关卡

[光滑表示、容许表示与反变对偶](../concepts/smooth-admissible.md) · [球面 Hecke 代数与 Satake 同构、非分歧表示](../concepts/satake.md) · [定理 2.5（光滑不可约 ⇒ 容许）、引理 2.6 与 Harish-Chandra 特征标](../concepts/harish-chandra-character.md)

## 出处（印刷页）

- A p.11–13（A p.12）

> 说明：定义与引理 2.1/2.2 取自 p.11–p.13；证明要点（$e_{gK'}\ast e_K=e_{gK}$、$H(G)\otimes M\cong M$）照 p.12–p.13 的观察 (3) 与末段注。
