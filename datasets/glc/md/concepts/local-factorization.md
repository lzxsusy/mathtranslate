---
id: glc/concept/local-factorization
type: concept
track: C
---

# 局部化与不交支撑的因子化（引理 4.7.1）

> 不交支撑处直和 $\operatorname{Tor}_x^a\times\operatorname{Tor}_y^b\simeq\operatorname{Tor}_{ax+by}^{a+b}$；单点支撑处即局部反常对象。

**问题**：为什么 $\mathcal{L}_E^d$ 的结构归约为单点处的 $\mathcal{L}_{E,x}^d[-d]$，不交支撑的因子化又给出什么同构？

## 定义

以 $x$ 表示 $X$ 的一个几何点，令 $i_x:\operatorname{Tor}_x^d\hookrightarrow\operatorname{Tor}^d$ 为 $s_d$ 在 $d\cdot x$ 上的纤维，它分类支撑于 $x$ 的长度 $d$ 挠层；置 $\mathcal{L}_{E,x}^d:=i_x^*\mathcal{L}_E^d$。由于这一纤维在对称幂方向上余维为 $d$，局部反常对象是 $\mathcal{L}_{E,x}^d[-d]$。引理 4.7.1（不交支撑的因子化）：若 $x\ne y$，直和给出 $\operatorname{Tor}_x^a\times\operatorname{Tor}_y^b\xrightarrow{\sim}\operatorname{Tor}_{ax+by}^{a+b}$ 与 $\mathcal{L}_{E,x}^a\boxtimes\mathcal{L}_{E,y}^b\xrightarrow{\sim}\mathcal{L}_{E,ax+by}^{a+b}$；更一般地，对具有不同支撑点的除子 $D=\sum_x d_x x$，有 $\prod_x\operatorname{Tor}_x^{d_x}\xrightarrow{\sim}\operatorname{Tor}_D^d$ 与 $\boxtimes_x\mathcal{L}_{E,x}^{d_x}\simeq\mathcal{L}_{E,D}^d$。

*记号*：$i_x$ 为闭浸入（纤维）；$s_d:\operatorname{Tor}^d\to X^{(d)}$ 为支撑映射；$\boxtimes$ 为外张量积；$D=\sum_x d_x x$ 为有效除子，$d=\deg D$。

## 要点

- 局部化把整体对象切成「支撑固定为 $x$」的一片：$\operatorname{Tor}_x^d$ 就是 $s_d$ 在 $d\cdot x$ 处的纤维，因此 $\mathcal{L}_{E,x}^d$ 是拉回而非新的构造。
- 移位 $[-d]$ 的来源是余维：纤维在对称幂方向的余维为 $d$，反常层沿闭浸入拉回要按余维移位才回到反常位置。
- 引理说不同支撑处的直和把叠与层都乘起来：$\operatorname{Tor}_x^a\times\operatorname{Tor}_y^b\to\operatorname{Tor}_{ax+by}^{a+b}$ 是「两个挠层直和」；层的同构说明 $\mathcal{L}_E$ 在这类点上也是外张量积。
- 于是计算整体 $\mathcal{L}_E^d$ 只需算单点的 $\mathcal{L}_{E,x}^d[-d]$；§4.8–§4.9 正是这样做，并最终由 Springer 理论给出 $B_{\lambda,x}$ 的分解。

## 关键公式

- $i_x:\operatorname{Tor}_x^d\hookrightarrow\operatorname{Tor}^d,\qquad \mathcal{L}_{E,x}^d:=i_x^*\mathcal{L}_E^d$
- $\mathcal{L}_{E,x}^d[-d]\in\operatorname{Perv}(\operatorname{Tor}_x^d)$
- $\operatorname{Tor}_x^a\times\operatorname{Tor}_y^b\xrightarrow{\sim}\operatorname{Tor}_{ax+by}^{a+b},\qquad \mathcal{L}_{E,x}^a\boxtimes\mathcal{L}_{E,y}^b\xrightarrow{\sim}\mathcal{L}_{E,ax+by}^{a+b}\qquad(x\ne y)$
- $\prod_x\operatorname{Tor}_x^{d_x}\xrightarrow{\sim}\operatorname{Tor}_D^d,\qquad \boxtimes_x\mathcal{L}_{E,x}^{d_x}\simeq\mathcal{L}_{E,D}^d$

## 定理与证明

### 引理 4.7.1（不交支撑的因子化）（要点（有缺口））

若 $x\ne y$，直和给出 $\operatorname{Tor}_x^a\times\operatorname{Tor}_y^b\xrightarrow{\sim}\operatorname{Tor}_{ax+by}^{a+b}$ 与 $\mathcal{L}_{E,x}^a\boxtimes\mathcal{L}_{E,y}^b\xrightarrow{\sim}\mathcal{L}_{E,ax+by}^{a+b}$；对具有不同支撑点的除子 $D=\sum_x d_x x$ 有 $\prod_x\operatorname{Tor}_x^{d_x}\xrightarrow{\sim}\operatorname{Tor}_D^d$ 与 $\boxtimes_x\mathcal{L}_{E,x}^{d_x}\simeq\mathcal{L}_{E,D}^d$。

1. 对支撑不交的两个挠层取直和，得支撑为 $ax+by$、长度为 $a+b$ 的挠层，给出叠的同构。  
   *为什么*：支集不交时直和的长度相加，这是引理第一式的全部内容。
2. 层的同构来自 $\mathcal{L}_E$ 在直和点处的外张量积结构。  
   *为什么*：讲义以 $\xrightarrow{\sim}$ 直接陈述，未构造该同构。
3. 对多个互异支撑点归纳，得乘积公式与 $\boxtimes_x$ 的公式。  
   *为什么*：由二元的同构归纳即得，讲义只写结果。

> 缺口：讲义只述不证：该引理没有证明，且层的同构（而不只是叠的同构）是作为断言给出的。

*出处*：§4.7 引理 4.7.1（原书 p.30）


## 易错点

- 移位是 $-d$ 而不是 $+d$：纤维余维为 $d$，沿闭浸入拉回时要按余维负移位，才使 $[-d]$ 后的对象仍是反常层。
- $\operatorname{Tor}_x^d$ 只记支撑恰好为 $x$ 的挠层（$s_d$ 在 $d\cdot x$ 处的纤维），不是「含 $x$ 的支撑」；含重数奇点的对象属于 $\operatorname{Tor}^{d,\mathrm{rss}}$ 之外的分层。
- 因子化要求 $x\ne y$（支撑不交）；$x=y$ 时直和仍在同一纤维内，得到的是局部分层的叠加而不是乘积分解。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§4.7 归约到单点处的局部挠层，p.30（PDF p.30），`源码/chapters/ch04.tex:113-125（§4.7）`

## 核验

状态：`external-confirmed`（2026-11-18）
- FGKV98：https://arxiv.org/abs/alg-geom/9703022 — 卡里引理 4.7.1 的 ⊠ 分解与原文逐字同式：『I^*_{(m_i),(x_i)}(L_E) ≃ L_{E,m_1,x_1} ⊠ … ⊠ L_{E,m_k,x_k}』（不同支撑点的挠层直和 ↔ 层的张量积）。
- FGKV98：https://arxiv.org/abs/alg-geom/9703022 — 卡里『纤维在对称幂方向余维 d，故局部反常对象是 L_{E,x}^d[-d]』对应原文『the shifts in degrees are due to the fact that the stack Coh_{n,m}(x) has dimension −m』。

## 关联

- `glc/concept/laumon-sheaf`
- `glc/concept/local-laumon-formula`
- `glc/concept/b-lambda-ic`
