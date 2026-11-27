---
id: page/kapustin-witten
kind: topic
title: Kapustin–Witten 理论：电磁对偶如何导出几何 Langlands
aliases: [Kapustin–Witten, KW 2006, 电磁对偶与几何 Langlands, Kapustin-Witten theory]
status: draft
version: 0.1
updated: 2026-11-27
covers: [geometry/geometric-langlands, geometry/bun-n, geometry/local-system, geometry/hecke-eigensheaf, geometry/d-module, geometry/affine-grassmannian, geometry/riemann-hilbert, algebra/langlands-correspondence, algebra/l-group, algebra/hecke-operator, qft/instanton]
compiled_from:
  - id: kw/concept/langlands-dual-group
    hash: pending
  - id: kw/concept/n4-sym-theory
    hash: pending
  - id: kw/concept/topological-twist
    hash: pending
  - id: kw/concept/canonical-parameter
    hash: pending
  - id: kw/concept/hitchin-moduli
    hash: pending
  - id: kw/deriv/sdual-mirror
    hash: pending
  - id: kw/concept/eigenbrane
    hash: pending
  - id: kw/deriv/gno-to-langlands
    hash: pending
  - id: kw/concept/canonical-coisotropic-brane
    hash: pending
readers: 研究生（懂层与叠、知道 Hitchin 模空间的定义；不要求量子场论背景）
rights: rewritten
---

# Kapustin–Witten 理论：电磁对偶如何导出几何 Langlands

> 本页是 page/geometric-langlands 的物理侧配套稿。数学页讲对应是什么、怎么证；本页只讲一件事：Kapustin 与 Witten 在 2006 年怎样用四维 $\mathcal N=4$ 超杨–米尔斯理论的电磁对偶“导出”这个对应，以及这条推导在哪里停下。

## 0. 一句话

把 $\mathcal N=4$ 超杨–米尔斯理论沿一条紧 Riemann 面 $C$ 紧化，并作适当的拓扑扭化，四维的 $S$-对偶就变成 Hitchin 模空间上的镜像对称；在这个二维理论里，Wilson 与 't Hooft 线算子变成作用在膜上的算子，它们的特征膜分别是 $C$ 上的局部系统与 $\operatorname{Bun}_G$ 上的 Hecke 特征 D-模。这就是几何 Langlands 对应的物理图像。

本页按这条链子的顺序走：对偶群（§1）→ 扭化（§2）→ 紧化（§3）→ 参数 $\Psi$（§4）→ 镜像（§5）→ 膜与线算子（§6）→ Hecke（§7）→ c.c. 膜与 D-模（§8）→ 全景与主断言（§9）→ 边界（§10）。只想看结论的读者可直接跳 §9。

## 1. 起点：Montonen–Olive 与 Langlands 对偶

四维 $\mathcal N=4$ 超杨–米尔斯理论是四维可能的最大超对称规范理论，有 16 个超荷。它的规范场是取值在 $\mathfrak g$ 中的联络，耦合常数与 $\theta$ 角合成复参数（KW 2006, §2.1, 印刷 p.10）：

> $\tau=\frac{\theta}{2\pi}+\frac{4\pi\mathrm i}{e^2}$　(2.12)

GNO 的分析表明，对偶之后的规范群不是 $G$ 而是它的“磁对偶群”——正是这一步促成了 Montonen 与 Olive 的电磁对偶猜想（§1, 印刷 p.3）。KW 开篇直接把这两件事并成一句（§1, 印刷 p.3）：

> For a gauge group $G$, the GNO dual group is actually the same as the Langlands dual group ${}^LG$, which plays an important role in formulating the Langlands conjectures.
>
> 译（本页）：规范群 $G$ 的 GNO 对偶群，正是 Langlands 对偶群 ${}^LG$——后者在表述 Langlands 猜想时举足轻重。

Montonen 与 Olive 猜的是：磁单极与规范粒子互换（最初只是 $\mathbb Z_2$）；把 $\theta$ 角纳入后，对偶扩展为 $\mathrm{SL}(2,\mathbb Z)$ 的作用（§1, 印刷 p.3–4），$S$ 生成元就是 $\tau\to-1/\tau$（(2.16), 印刷 p.11）。

二者相等不是巧合：GNO 对偶由“根与余根互换”算出，Langlands 对偶群也由根数据的对偶算出，两笔账是同一笔。KW 随即列出（Table 1, 印刷 p.3）：

| $G$ | ${}^LG$ |
|---|---|
| $\mathrm U(N)$ | $\mathrm U(N)$ |
| $\mathrm{SU}(N)$ | $\mathrm{PSU}(N)=\mathrm{SU}(N)/\mathbb Z_N$ |
| $\mathrm{Spin}(2n)$ | $\mathrm{SO}(2n)/\mathbb Z_2$ |
| $\mathrm{Sp}(n)$ | $\mathrm{SO}(2n+1)$ |
| $\mathrm{Spin}(2n+1)$ | $\mathrm{Sp}(n)/\mathbb Z_2$ |
| $\mathrm G_2,\ \mathrm E_8$ | 自对偶 |

对非单边（non-simply-laced）的群还要修正（印刷 p.11–12）：

> If $G$ is not simply-laced, then the $S$-transformation is not $\tau\to-1/\tau$. Rather, it is $\tau\to-1/n_g\tau$, where $n_g$ is 2 for $\mathrm F_4$ and 3 for $\mathrm G_2$.
>
> 译（本页）：$G$ 非单边时，$S$ 变换不是 $\tau\to-1/\tau$，而是 $\tau\to-1/(n_g\tau)$，其中 $n_g$ 对 $\mathrm F_4$ 取 $2$、对 $\mathrm G_2$ 取 $3$。

于是 $\mathrm G_2$、$\mathrm F_4$ 的对偶群不再是 $\mathrm{SL}(2,\mathbb Z)$ 而是 Hecke 群（印刷 p.12）；$\mathrm{Sp}(k)$ 与 $\mathrm{Spin}(2k+1)$ 因为两边 Lie 代数不同构，还要分别设 $\tau$ 与 $\tau'$，$S$ 给 $\tau=-1/(2\tau')$，并取 $n_g=2$。这些修正对后面 §5 的镜像陈述是必要的：$S$-对偶只在单边情形恰好是 $\tau\to-1/\tau$。对偶群见 {{entry:algebra/l-group}}，Langlands 对应的整体叙述见 {{entry:algebra/langlands-correspondence}}。

## 2. 第二步：用 GL 扭化造出拓扑场论

要把一个物理理论变成能定义“拓扑不变量”的对象，标准手续是扭化：把时空的旋转群换成对角嵌入的超对称 $R$-对称群的一部分，使得某个超荷 $Q$ 变成标量、$Q^2=0$，再取 $Q$-上同调。$\mathcal N=4$ 恰好有三种扭化（§3.1, 印刷 p.17）：

> $\mathcal N=4$ super Yang-Mills theory can be twisted in three ways to make a topological field theory. … The third twist … turns out to be the twist relevant to the geometric Langlands program, and we will call it the GL twist.
>
> 译（本页）：$\mathcal N=4$ 超杨–米尔斯理论有三种扭化方式可以得到拓扑场论。……第三种扭化……正是与几何 Langlands 纲领相关的那一种，我们称之为 GL 扭化。

GL 扭化把自旋群 $\mathrm{Spin}(4)=\mathrm{SU}(2)_\ell\times\mathrm{SU}(2)_r$ 以分块对角的方式嵌入 $R$-对称群 $\mathrm{Spin}(6)\cong\mathrm{SU}(4)_R$（(3.2), 印刷 p.18），并留下一个与这个嵌入交换的 $U(1)_K$（(3.3), 印刷 p.19）。扭化后的场只剩：规范场 $A$、取值在伴随表示的 1-形式 $\varphi$，以及两个实标量 $\sigma,\bar\sigma$（合起来是一个复标量及其共轭）；超荷按
$$6_v=(2,2)_0\oplus(1,1)_2\oplus(1,1)_{-2}$$
分解，$\varphi_{0},\dots,\varphi_{3}$ 成一个伴随 1-形式，$\sigma=(\varphi_4-\mathrm i\varphi_5)/\sqrt2$ 及其共轭是标量。这条分解对后文“膜的类型”很关键，细节见 {{entry:qft/instanton}} 与扭化卡。

## 3. 第三步：紧化到 $C$，得到 Hitchin 模空间

取四维流形 $M=\Sigma\times C$：$\Sigma$ 是二维时空，$C$ 是紧 Riemann 面（“紧化曲线”）。令 $C$ 的面积远小于 $\Sigma$，则低能有效理论是二维非线性 $\sigma$-模型，目标空间是 $C$ 上 $G$-Higgs 丛的模空间 $M_H=M_H(G,C)$（§4, 印刷 p.38–39）。$M_H$ 的点是 Hitchin 方程的解（(4.1), 印刷 p.39）：

> $F-\varphi\wedge\varphi=0,\qquad D\varphi=0,\qquad D\star\varphi=0$
>
> 译（本页）：曲率与 $\varphi$ 的自 commutator 相消，$\varphi$ 全纯且“共形”于度量的调和条件。

三个方程必须并列：只写前两式会漏掉 $D\star\varphi=0$，只写第一式与第三式会漏掉全纯性。$M_H$ 的（复）维数是 $(2g-2)\dim G$，其中 $g$ 是 $C$ 的亏格。

$M_H$ 是超凯勒流形，有一族复结构 $I_w$（$w\in\mathbb{CP}^1$），三个特殊点记作 $I,J,K$（(4.6), 印刷 p.43）。同一个光滑流形在这里有两种读法：

- 在复结构 $I=I_0$ 下，$M_H$ 是 $C$ 上 $G$-Higgs 丛的模空间；
- 在复结构 $J$ 下，$M_H$ 是 $C$ 上 $G$-局部系统的模空间 $Y$：稳定同态 $\vartheta:\pi_1(C)\to G_{\mathbb C}$ 的模空间（Corlette–Donaldson，印刷 p.51）。

这两个读法是 §5 镜像的几何基础：$S$-对偶在一边看到的是“方程”，在另一边看到的是“表示”。$M_H$ 的构造见 {{entry:geometry/local-system}}（局部系统侧）与 {{entry:geometry/riemann-hilbert}}（Riemann–Hilbert 对应）。

对一般的 $t$，KW 把这族二维模型统称为“广义 B-模型”（印刷 p.4）；A-模型与 B-模型只是 $\Psi=0$ 与 $\Psi=\infty$ 两个端点。这一点值得强调：几何 Langlands 用的并不是某个现成的 A-模型或 B-模型，而是一整族只有两个端点可命名的拓扑 $\sigma$-模型。

## 4. 第四步：一个参数 $\Psi$ 管住整族理论

扭化后的理论带一个连续参数：超荷取 $Q=uQ_\ell+vQ_r$，令 $t=v/u$。四维理论的可观测量只通过一个组合依赖 $t$ 与 $\tau$（(3.50), 印刷 p.35）：

> $\Psi=\frac{\tau+\bar\tau}{2}+\frac{\tau-\bar\tau}{2}\cdot\frac{t-t^{-1}}{t+t^{-1}}$

于是整族二维理论实际是一维族，参数 $\Psi\in\mathbb{CP}^1$；不同 $t$（乃至不同 $\tau$）只要给出同一个 $\Psi$，物理就相同。两个值特别重要（§3.2, 印刷 p.25；§5.3, 印刷 p.70）：

- $\Psi=\infty$：$t=\pm\mathrm i$，二维理论是复结构 $J$ 下的 B-模型；此时 (3.29) 等价于 $A+\mathrm i\varphi$ 复平坦，即四维流形上的复平坦 $G_{\mathbb C}$ 联络；
- $\Psi=0$：$t=1$、$\theta=0$，二维理论是复结构 $K$ 下的 A-模型。

KW 全篇就盯住这两个值（§5.3, 印刷 p.70）：

> In the rest of this paper except section 11.3, we focus primarily on the distinguished values $\Psi=0$ and $\Psi=\infty$, and the duality … that maps $\Psi\to-1/n_g\Psi$ and hence exchanges $\Psi=0$ and $\Psi=\infty$.
>
> 译（本页）：除 §11.3 外，本文余下部分主要盯住 $\Psi=0$ 与 $\Psi=\infty$ 这两个特殊值，以及把 $\Psi$ 送到 $-1/(n_g\Psi)$、从而交换这两个值的对偶。

请记住这条：**电与磁的线算子并不住在同一个二维模型里**——Wilson 算子在 $\Psi=\infty$（B-模型，$J$），'t Hooft 算子在 $\Psi=0$（A-模型，$K$）。$S$-对偶恰好把 $\Psi=\infty$ 送到 $\Psi=0$。这一点是后面所有“特征膜”陈述的准确含义。

## 5. 第五步：$S$-对偶就是镜像对称

把 $G$ 的理论与 ${}^LG$ 的理论并排，$S$-对偶给出（§5.2, 印刷 p.70）：

> Thus $S$-duality implies that the B-model for $M_H(G,C)$ in complex structure $J$ is equivalent to the A-model for $M_H({}^LG,C)$ in complex structure $K$. If we combine $S$ with a transformation $I:\varphi\to\mathrm i\varphi$ that rotates complex structure $K$ back to complex structure $J$, we get a mirror symmetry that maps the B-model in complex structure $J$ to the A-model in complex structure $J$. So the complex manifolds $M_H(G,C)$ and $M_H({}^LG,C)$ are a mirror pair in complex structure $J$.
>
> 译（本页）：$S$-对偶给出：$M_H(G,C)$ 在复结构 $J$ 下的 B-模型，等价于 $M_H({}^LG,C)$ 在复结构 $K$ 下的 A-模型。再把 $S$ 与把 $K$ 转回 $J$ 的变换 $I:\varphi\mapsto\mathrm i\varphi$ 结合，就得到把 $J$ 下 B-模型送到 $J$ 下 A-模型的镜像对称；因此 $M_H(G,C)$ 与 $M_H({}^LG,C)$ 在复结构 $J$ 下互为镜像流形。

注意措辞：$S$-对偶本身给的是 $B_J(G)\cong A_K({}^LG)$；“镜像”要再复合一个把 $K$ 转回 $J$ 的自同构 $I$，而 $I$ 不保持那个理论族——原文紧接着说它“moves us out of the four-dimensional family of TQFT’s parametrized by CP¹”（印刷 p.70）。引文没有省略这一点，转述也不该省略。这是几何 Langlands 的物理源头：$S$-对偶交换 $G\leftrightarrow{}^LG$，镜像交换 A/B 模型，两者叠起来才把“对偶群”与“Hecke 特征层”接上。

## 6. 第六步：膜、线算子、特征膜

二维 $\sigma$-模型的对象是膜（brane），即带边界条件的开弦端点所扫出的子流形加丛。KW 按三个复结构 $I,J,K$ 把膜分成八类，记作 $(\varepsilon_I,\varepsilon_J,\varepsilon_K)$，$\varepsilon\in\{A,B\}$（§5.6, 印刷 p.77）。其中 $(B,B,A)$ 与 $(A,A,A)$ 两种不存在（脚注 24，印刷 p.78：在 $I,J$ 中全纯的子流形自动在 $K$ 中全纯），实际用到的是 $(B,B,B)$，以及 $(B,A,A),(A,B,A),(A,A,B)$ 这三种“恰好在一个复结构中是 B 型”的膜；另有 $(B,A,B)$、$(A,B,B)$ 两类（B 型出现在两个复结构中），本文基本不用。

线算子（Wilson 与 't Hooft）在四维里沿一维环路 $S\subset M$ 支撑。扭化之后它们仍是拓扑算子，作用在膜上：一个膜被线算子作用后若回到自身的倍数，就叫**特征膜**（eigenbrane，§6.4, 印刷 p.98–99）：

> A joint eigenbrane of the 't Hooft operators will be called a magnetic eigenbrane.
>
> 译（本页）：'t Hooft 算子的联合特征膜称为磁特征膜。

形式地，对一族线算子 $X_p$：$X_p\,\mathcal B\cong\mathcal B\otimes V_p$（(6.25), 印刷 p.97）；$V_p$ 局部与 $p$ 无关，但可能带整体单值，所以它是一族平坦丛的纤维。

“线算子作用在膜上”在二维里还有一层更具体的含义（§6.3, 印刷 p.90–91）：一条线算子把平面分成两个区域 $Y,Z$，翻转 $Z$ 的定向并“折叠”之后，它就成了乘积理论 $Y\otimes Z$ 里的一个边界条件——

> What we have now from an abstract point of view is a boundary condition in the tensor product theory $Y\otimes Z$. … So the line operator reduces in two dimensions to a $(Y,Z)$-brane.
>
> 译（本页）：抽象地说，我们现在得到的是张量积理论 $Y\otimes Z$ 中的一个边界条件。……于是线算子在二维中约化为一个 $(Y,Z)$-膜。

这条“折叠”把“算子”翻译成“边界条件”，也正是后面 Hecke 算子能变成膜上作用的原因：Hecke 修改发生在奇点处，而奇点附近的场论就是 $Y\otimes Z$ 的边界理论。

## 7. 第七步：'t Hooft 算子 = Hecke 算子

几何 Langlands 的 Hecke 算子在 $\operatorname{Bun}_G$ 上作用；KW 的对应物作用在 $M_H$ 上、作用在 Higgs 丛上。§9 开篇（印刷 p.123）：

> The goal of the present section is to begin the study of the supersymmetric 't Hooft operators that appear at $\Psi=0$ … The main result will be to show that 't Hooft operators correspond to the Hecke operators of the geometric Langlands program.
>
> 译（本页）：本节开始研究出现在 $\Psi=0$ 的超对称 't Hooft 算子……主要结果是：'t Hooft 算子对应几何 Langlands 纲领的 Hecke 算子。

机制在 §10：带奇点的 't Hooft 算子由 Bogomolny 方程的解描述，奇点附近“插入”一个 Hecke 修改；U(N) 情形可以逐项算清（印刷 p.132–133），再推广到一般 $G$。$\Psi=0$ 时二维理论是 $K$ 下的 A-模型，'t Hooft 算子的特征膜——磁特征膜——因此就是 Hecke 特征层的物理版。Hecke 算子本身见 {{entry:algebra/hecke-operator}}，$G=\mathrm{GL}_n$ 时 Hecke 特征层的定义见 {{entry:geometry/hecke-eigensheaf}}。

## 8. 第八步：c.c. 膜把磁特征膜接到 D-模

到这里还差一步。磁特征膜住在 $M_H(G,C)$ 上，而几何 Langlands 的右端是 $\operatorname{Bun}_G$ 上的 D-模。§11 开篇（印刷 p.184）：

> A crucial ingredient is missing from what we have presented so far. … the magnetic eigenbranes that we get this way are branes of type $(A,B,A)$ on $M_H(G,C)$, while in the conventional statement of the geometric Langlands correspondence, the right hand side is supposed to involve instead a D-module on, roughly speaking, $M(G,C)$, the moduli space of $G$-bundles.
>
> 译（本页）：我们目前的叙述还缺一个关键部件。……这样得到的磁特征膜是 $M_H(G,C)$ 上的 $(A,B,A)$ 型膜，而几何 Langlands 对应的通常表述里，右端应当换成 $M(G,C)$（$G$-丛的模空间）上的 D-模。

这里要先处理一个原文自身的记法冲突，否则引用会出错。§11 开头（印刷 p.184）与 p.198 把 F 型膜记作 $(A,B,A)$，§12.4（印刷 p.217）却把 $(A,B,A)$ 这个名字给了 c.c. 膜，而 §12.3（印刷 p.215）构造的 F 型膜是 $(B,A,A)$：

> We can get branes of type $(B,A,A)$ by applying S-duality to branes of type $(B,B,B)$.
>
> 译（本页）：对 $(B,B,B)$ 型膜作 $S$-对偶，就得到 $(B,A,A)$ 型膜。

按几何判断：F 型膜的支撑是 Hitchin 纤维（在 $I$ 中全纯、在 $J,K$ 中 Lagrange）并带平坦 Chan–Paton 丛，所以它应当是 $(B,A,A)$；$(A,B,A)$ 则是 c.c. 膜。本文统一取“c.c. 膜 $=(A,B,A)$、F 型膜 $=(B,A,A)$”这套命名，§11 开头与印刷 p.198 的 $(A,B,A)$ 按笔误处理（这个冲突本身也记在审计档案里）。

KW 的补法是引入**典范余各向同性膜**（canonical coisotropic brane，简称 c.c. 膜）：它不是 Lagrange 膜，而是支撑在整个 $M_H$ 上的 A-膜。取 A-模型的辛形式为 $\omega=(\operatorname{Im}\tau)\,\omega_K$，则 (11.1) 有解
$$F=(\operatorname{Im}\tau)\,\omega_J\qquad (11.2)$$
（印刷 p.186）。它在三个复结构下的类型是 $(A,B,A)$：在 $I$ 与 $K$ 下是 A-膜（前者靠恒等式 $(\omega_I^{-1}\omega_J)^2=-1$，即 (11.5)），在 $J$ 下是 B-膜（$F$ 是 $(1,1)$ 型）。于是 c.c. 膜与磁特征膜都是 $K$ 下的 A-膜，可以谈它们之间的开弦：$(B_{\mathrm{cc}},B)$-strings 构成 $(B_{\mathrm{cc}},B_{\mathrm{cc}})$-strings 上的模（印刷 p.196），而后者是某个线丛的微分算子层（印刷 p.193–194）。

真正把 D-模落在 $\operatorname{Bun}_G$ 上的，是下面这个几何事实（印刷 p.196）：$M_H$ 中由 $\varphi=0$ 定义的子流形，正是 $M(G,C)$ 的一个拷贝；它在 $K$ 与 $J$ 中是 Lagrange 的、在 $I$ 中是复的，所以本身是一个 $(B,A,A)$-膜。KW 的一般陈述是：$M_H(G,C)$ 上复结构 $K$ 的每个 A-膜都自然给出 $M(G,C)$ 上的 D-模（印刷 p.184）；落到这个拷贝上，c.c. 膜的开弦代数就是 $M(G,C)$ 上的扭化微分算子层——$\Psi=h$（$h$ 为 $G$ 的对偶 Coxeter 数）时扭化消失，恰好是普通微分算子（印刷 p.206）。

最小的例子是 $G=\mathrm{U}(1)$（印刷 p.200）：$(B_{\mathrm{cc}},B_{F_p})$-strings 给出 $\operatorname{Jac}(C)$ 上的 D-模，等价于 $\operatorname{Jac}(C)$ 上的平坦 $\mathbb C^*$ 联络；而平坦 $\mathbb C^*$ 联络又等同于 $H_1(\operatorname{Jac}(C),\mathbb Z)\to\mathbb C^*$ 的同态，$H_1(\operatorname{Jac}(C),\mathbb Z)\cong H_1(C,\mathbb Z)$ 由 Poincaré 对偶给出。这一步与数学侧的几何类域论（{{entry:geometry/geometric-class-field-theory}}）逐项对上。D-模的一般定义见 {{entry:geometry/d-module}}。这也说明 $\Psi$ 不只管二维模型，还管 D-模的扭化：$\Psi=h$（$h$ 为 $G$ 的对偶 Coxeter 数）时扭化消失，得到的是无扭的普通 D-模。

## 9. 全景：六个主要想法与主断言

KW 在导言里把全文压缩成六条（印刷 p.4–5）：

1. 扭化 $\mathcal N=4$ 得四维拓扑场论（§3）；
2. 沿 $C$ 紧化，得目标为 $M_H$ 的二维 $\sigma$-模型；对特殊参数，四维 $S$-对偶变成二维镜像对称（§4–5）；
3. Wilson 与 't Hooft 线算子是作用在膜上的拓扑算子，由此定义电/磁特征膜（§6）；
4. 电特征膜对应同态 $\pi_1(C)\to{}^LG_{\mathbb C}$（§8）；
5. 't Hooft 算子对应几何 Hecke 算子（§9–10）；
6. 借助 c.c. 膜，磁特征膜自然给出 $\operatorname{Bun}_G$ 上 D-模（§11）。

第 6 条落地后，主断言可以一句话说完（印刷 p.122）：

> The main claim of the geometric Langlands program is that a homomorphism $\vartheta:\pi_1(C)\to{}^LG_{\mathbb C}$ is associated in a natural way to a sheaf on $M(G,C)$ that is a Hecke eigensheaf and also a holonomic D-module.
>
> 译（本页）：几何 Langlands 纲领的主要断言是：同态 $\vartheta:\pi_1(C)\to{}^LG_{\mathbb C}$ 以自然的方式对应 $M(G,C)$ 上的一个层，它既是 Hecke 特征层，又是 holonomic D-模。

链条因此是：$S$-对偶 → 镜像 → 膜 → 线算子作用 → 电特征膜 = 局部系统 → 磁特征膜 = Hecke 特征层 → c.c. 膜 → $\operatorname{Bun}_G$ 上的 D-模。

## 10. 这条推导证明了什么、没有证明什么

先看 KW 自己划的边界（印刷 p.5）：

> One obvious gap in our analysis is that we consider only the unramified case of the geometric Langlands correspondence. … A second major gap is that we do not shed light on the utility of two-dimensional conformal field theory for the geometric Langlands program.
>
> 译（本页）：我们的分析有一个明显的缺口：只处理了几何 Langlands 对应的非分歧情形。……第二个重大缺口是：我们没有说明二维共形场论对几何 Langlands 纲领有什么用。

这两条边界按原文保留；本页不替 KW 补分歧情形，也不把二维 CFT 的路线算作它的功劳。

其次要分清“物理推导”与“数学证明”。KW 给出的是物理图像与一致性论证：镜像对称、膜的谱、开弦代数都是物理语言；它解释了**为什么**这个对应会出现，但不构成数学证明。数学侧：

- $G=\mathrm{GL}_n$ 的非分歧情形由 Frenkel–Gaitsgory–Vilonen（2002, arXiv:math/0012255）证明：每个不可约秩 $n$ 局部系统都有非零的 Hecke 特征反常层，且逐分支不可约；
- 一般约化群、特征 $0$ 的完整等价（$D(\operatorname{Bun}_G)\simeq\operatorname{IndCoh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{{}^LG})$）由 Gaitsgory–Raskin 五部曲（2024–2026，即 2024 三篇、2025b、2026）证明；特征 $p\gg0$ 的情形由 Gaitsgory–Raskin 2025a（arXiv:2508.02237）证明，谱侧须换成 $\operatorname{LocSys}'$。Scholze 的 Bourbaki 1252 号报告（2026，§2 定理 2.11、2.12，p.18）给了完整叙述与来源链。

所以更准确的表述是：KW 提供的是**物理侧的证据与机制**，数学侧的证据是另一条独立路线；两条路线在“对应存在且由 ${}^LG$-局部系统标号”这一点上汇合。本页不把 KW 的论证当作证明，也不把 GR 的证明说成“物理推出”。

## 11. 术语对照与读法

| KW 2006 | 数学侧 |
|---|---|
| 局部系统 $\vartheta:\pi_1(C)\to{}^LG_{\mathbb C}$，点 $x(\vartheta)\in M_H({}^LG,C)$ | 谱侧对象，$\operatorname{LocSys}_{{}^LG}$ |
| 电特征膜（zerobrane 在 $M_H({}^LG,C)$ 上） | 谱侧的“点”，对应 $\vartheta$ |
| 磁特征膜（$M_H(G,C)$ 上 $F$ 型膜，即 $(B,A,A)$：$I$ 中全纯、$J,K$ 中 Lagrange） | Hecke 特征层，$F$ 型膜经 c.c. 膜变换给 D-模 |
| 't Hooft 算子 | Hecke 算子 |
| $S$-对偶（$\Psi\to-1/(n_g\Psi)$） | Langlands 对偶 $G\leftrightarrow{}^LG$；二维侧是镜像对称 |
| c.c. 膜（$(A,B,A)$） | D-模的“量子化支撑”；开弦代数 = 微分算子 |

读法建议：§1–§4 先建立“对偶群—扭化—紧化—$\Psi$”四件事，再读 §5 的镜像；§6–§8 是物理侧的主体，配数学页 §2–§3 一起看；§9 是全景；§10 决定你引用时该说“物理图像”还是“定理”。相关词条：{{entry:geometry/bun-n}}、{{entry:geometry/geometric-langlands}}、{{entry:geometry/affine-grassmannian}}（Hecke 对应的几何舞台）、{{entry:algebra/spherical-hecke-algebra}}（局部 Hecke 代数）。

## 12. 证据

本页所有 KW 引文都以 2006 年原文（arXiv:hep-th/0604151）为准；页码为印刷页，换算关系是“PDF 页 = 印刷页 + 1”。

| 本页位置 | KW 位置 | 依据 |
|---|---|---|
| §1 对偶群 | §1, 印刷 p.3；§2.1, p.10–12 | “GNO dual group is … the Langlands dual group”；(2.12)、(2.16)、(2.17) |
| §2 扭化 | §3.1, 印刷 p.17–19 | 三种扭化、GL twist、(3.2)、(3.3) |
| §3 紧化 | §4, 印刷 p.38–39；§4.2, p.51 | (4.1)、$\dim M_H$、$J$ 下 $M_H\cong Y$ |
| §4 参数 $\Psi$ | §3.5, 印刷 p.35；§5.3, p.70 | (3.50)、$\Psi=\infty$ 与 $\Psi=0$ |
| §5 镜像 | §5.2, 印刷 p.70–71 | $B_J(G)\cong A_K({}^LG)$、mirror pair |
| §6 膜与线算子 | §5.6, 印刷 p.77–78；§6.4, p.97–99 | 膜的分类、(6.25)、特征膜定义 |
| §7 't Hooft–Hecke | §9 开篇, 印刷 p.123；§10, p.148 起 | 't Hooft 算子 ↔ Hecke 算子 |
| §8 c.c. 膜与 D-模 | §11, 印刷 p.184–206 | (11.2)、$(B_{\mathrm{cc}},B)$-strings、p.200 的 $\mathrm U(1)$ 例、p.206 的 $\Psi=h$ |
| §9 六条与主断言 | 印刷 p.4–5、p.122 | 六条主要想法、main claim |
| §10 边界 | 印刷 p.5 | 两个 gap |

## 13. 外部对照

- **nLab**（`ncatlab.org/nlab/show/Kapustin-Witten+TQFT`）：叙述与 KW 一致——$I$ 是 Higgs 丛、$J/K$ 是局部系统、c.c. 膜给出 D-模。两处措辞要小心：(a) nLab 写“canonical isotropic brane”，KW 原文是 canonical **coisotropic** brane（c.c. 膜），后者支撑维数高于中维、不可能是 isotropic；(b) nLab 把 zerobrane 放在 $M_H({}^LG)$ 上，这与 KW §8 原文一致，不要误记成 $M_H(G)$；但它接着说“把 $\mathcal A$ 看成复结构 $I$ 下的 A-膜”，与 KW 的“$K$ 下 A-膜”命名不同，引用时以 KW 的 $I,J,K$ 为准。
- **香蕉空间**（bananaspace.org）：本次自动抓取被 Cloudflare 403 挡住，未采用。按 `04_playbook/27` §6，它本来也只能作术语方位的参考，不作证据。
- **Kapustin 讲义**（ctqm.au.dk/research/MCS/LectureNotesKapustin.pdf）：同一份讲义里 Hitchin 方程有两种写法——四维的 $F-\varphi\wedge\varphi+\star D\varphi=0,\ D\star\varphi=0$，与二维曲线上的三式 $F-\varphi\wedge\varphi=0,\ D\varphi=0,\ D\star\varphi=0$；后者与 KW (4.1) 一致。
- **UCLA 讲义**（`mirror.pdf`）：(3.133)–(3.139) 的推导与“最重要的取值是 $t=\pm\mathrm i$（以及 $t=\pm1$）”一语，支持 §4 的 $\Psi=\infty$ 与 $B$-模型配对。
- **$SU(4)$ 的表示**（adscft.org）：$\mathbf 4=[1,0,0]$、$\bar{\mathbf 4}=[0,0,1]$，支持 §2 的 $6_v$ 分解与超荷标号。

以上外部源只用来做交叉核对；凡与 KW 原文冲突处，以原文为准，并在正文中明说冲突（例如 c.c. 与 isotropic）。

## 14. 引用与出处

- A. Kapustin, E. Witten, *Electric–Magnetic Duality and the Geometric Langlands Program*, arXiv:[hep-th/0604151](https://arxiv.org/abs/hep-th/0604151)，231 页。本页页码均为印刷页：**PDF 页 = 印刷页 + 1**；逐页文本已抽到 `C:\Users\admin\Downloads\_kw_audit\pages\pNNN.txt`（`p{印刷页+1}.txt`），引文可逐字复核。
- nLab, *Kapustin–Witten TQFT*：[ncatlab.org/nlab/show/Kapustin-Witten+TQFT](https://ncatlab.org/nlab/show/Kapustin-Witten+TQFT)；本地转储 `07_refs_nlab/pages/Kapustin-Witten_TQFT.md`。
- A. Kapustin, *Lecture notes on topological field theory and geometric Langlands*：[ctqm.au.dk/research/MCS/LectureNotesKapustin.pdf](https://ctqm.au.dk/research/MCS/LectureNotesKapustin.pdf)（Hitchin 方程的两种写法，见 §13）。
- UCLA 镜像对称讲义 `mirror.pdf`（(3.133)–(3.139)、`t = ±i` 与 B-模型的对应）。
- adscft.org，$SU(4)$ 表示约定：$\mathbf 4=[1,0,0]$、$\bar{\mathbf 4}=[0,0,1]$。
- D. Gaitsgory, S. Raskin 等（GR 五部曲，2024–2026；正特征另见 2025a）与 P. Scholze, *Geometric Langlands*, Séminaire Bourbaki 1252 (2026)：本仓库中译注本 `08_source_code/SY02-45_Scholze布尔巴基1252几何Langlands的证明/`（定理 2.11、2.12，p.18）。
- 本页的逐卡审计与错误案例：`datasets/kw06/AUDIT-2026-11-27.md`（同一批 KW 资料卡的 106 条修正记录）。
