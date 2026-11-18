# 子复形上的 $\mathcal{A}_\infty$-代数结构

`kshms/concept/thm-03-subcomplex-a-inf-structure` · track D（Morse 机器） · 原文 定理 3

**问题**　把一个 $\mathcal{A}_\infty$-代数压到子复形 $B$ 上，高阶复合该怎么定义，才能仍然得到一个 $\mathcal{A}_\infty$-代数？

**摘要**　设 $B=\operatorname{Im}\Pi$ 是 $\mathcal{A}_\infty$-代数 $A$ 上幂等投影的像，且 $1-\Pi=dH+Hd$；把平面树的尾顶点配 $i$、旧顶点配 $m_k$、新顶点配 $H$、根配 $p$ 所得的 $m_n^B$ 满足 $\mathcal{A}_\infty$-约束。

**别名**　Theorem 3 ($A_\infty$-structure on a subcomplex)；同调扰动定理的树形式；子复形上的高阶复合 $m_n^B$

## 陈述

序列 $m_n^B$，$n\ge1$，给出 $B$ 上的一个 $\mathcal{A}_\infty$-代数结构。

## 记号

$(A,m_n)$：非幺 $\mathcal{A}_\infty$-代数；$\Pi:A\to A$：零次线性映射，$d\Pi=\Pi d$、$\Pi^2=\Pi$（$d=m_1$）；$H:A\to A[-1]$：满足 $1-\Pi=dH+Hd$ 的同伦；$B=\operatorname{Im}\Pi$，$i:B\to A$ 为嵌入、$p:A\to B$ 为投影，$\Pi=i\circ p$；$m_1^B=p\circ m_1\circ i$，$m_2^B=p\circ m_2\circ(i\otimes i)$，$m_n^B=\sum_T\pm m_{n,T}$（$n\ge3$，$T$ 取遍有 $n+1$ 个尾顶点、内顶点度数 $\ge2$ 的定向平面树）。

## 要点

- $m_{n,T}$ 的定义要用「插入新顶点」的树 $\bar T$：在 $T$ 的每条内边上插入一点并配以 $H$，尾顶点配 $i$，旧顶点配 $m_k$（$k$ 为该顶点度数），根配 $p$，再沿树向根复合。
- 结论是 $(m_n^B)_{n\ge1}$ 满足 $\mathcal{A}_\infty$-约束 $d(m_n^B)=m_n^{B,\Pi}$，其中 $m_n^{B,\Pi}$ 与 $m_n^B$ 的差别只是把某个新顶点上的 $H$ 换成 $\Pi$。
- 证明对同一个和 $\hat m_n^B=\sum_T\sum_{e\in E(\bar T)}\pm m_{n,\bar T_e}$ 作两种计算：用 $1-\Pi=dH+Hd$ 得一式，用 $A$ 的 $\mathcal{A}_\infty$-关系得另一式。
- 这是定理 2 中「把 de Rham 范畴压到 Morse 复形」的代数内核，也是本节后续「存在典范 $\mathcal{A}_\infty$-态射 $B\to A$」的基础。

## 公式

$$m_n^B=\sum_T\pm m_{n,T}\quad(n\ge3)$$

$$d(m_n^B)=m_n^{B,\Pi}$$

$$\hat m_n^B=d(m_n^B)-m_n^{B,\Pi}+m_n^{B,1}=m_n^{B,1}$$

## 证明（sketch）

1. 把每个被加项 $m_{n,T}$ 换成在一族树 $\{\bar T_e\}_{e\in E(\bar T)}$ 上的项 $m_{n,\bar T_e}$：$\bar T_e$ 由 $\bar T$ 在边 $e$ 的内部插入新顶点 $w_e$ 得到，$w_e$ 配以 $d=m_1$，其余配置不动；对全部树与边求和得 $\hat m_n^B$。

   *为什么*：这样每个被加项多出一个 $d$，使得同一个和可以从「微分作用在复合上」与「$\mathcal{A}_\infty$-关系」两个方向各算一次。

2. 用关系式 $1-\Pi=dH+Hd$ 计算 $\hat m_n^B$，得 $\hat m_n^B=d(m_n^B)-m_n^{B,\Pi}+m_n^{B,1}$。

   *为什么*：把新顶点上的 $d$ 与 $H$、$\Pi$、$1$ 三种可能配对分别归并：配 $H$ 给出 $d(m_n^B)$ 的边界项，配 $\Pi$ 给出 $m_n^{B,\Pi}$，配 $1$ 给出 $m_n^{B,1}$。

3. 用 $A$ 的 $\mathcal{A}_\infty$-结构计算同一个 $\hat m_n^B$：$d(m_j)$ 是 $m_l$（$l<j$）的二次表达式，逐树归并后得 $\hat m_n^B=m_n^{B,1}$。

   *为什么*：这是 $A$ 上 $\mathcal{A}_\infty$-约束的直接展开：$d$ 作用在内顶点 $m_j$ 上产生把该顶点劈成两个低阶顶点的树，正是 $m_n^{B,1}$ 的全部被加项。

4. 两式相减得 $d(m_n^B)=m_n^{B,\Pi}$，这正是族 $(m_n^B)_{n\ge1}$ 的 $\mathcal{A}_\infty$-约束，定理得证。

   *为什么*：$m_n^{B,1}$ 在两次计算中相同而被消去，剩下的等式对每个 $n\ge2$ 给出所需的约束，$n=1$ 的情形由命题「$m_1^B$ 是 $B$ 中的微分」保证。

> 缺口：原文标题即「证明概要」（ch07.tex:95），并明言「证明相当直接，因此我们只简要说明计算的主要步骤」；逐树的正负号约定与边界项的完整核对未写出，属同调扰动理论的标准计算，可参 [GS]（Gugenheim–Stasheff）与 [Me]（Merkulov）。

## 易错点

- $m_n^B$ 的和取遍所有内顶点度数 $\ge2$ 的定向平面树，且每棵树须先在每条内边插入新顶点；省掉插入这一步会得到不满足约束的复合。
- 约束不是 $d(m_n^B)=0$，而是 $d(m_n^B)=m_n^{B,\Pi}$：右端仍含 $\Pi$，它把 $B$ 之外的成分投影掉；把右端写成零是常见错误。
- $H$ 只要求 $1-\Pi=dH+Hd$，并不与 $d$ 或 $\Pi$ 交换；把 $H$ 当成「同伦逆」会算错符号。

## 相关卡

- `kshms/concept/dfn-03-nonunital-a-inf-algebra`
- `kshms/concept/thm-02-morse-de-rham-equivalence`
- `kshms/concept/lem-02-projection-operator`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §6.4（原文 p.42）；锚点 `源码/chunks/ch07.tex:91-124（定理 3 及证明概要）`

> 原文 p42（§6.4）；$m_n^B$ 的定义在同小节前文（ch07.tex:14-29），证明概要续至原文 p43–p44（ch07.tex:95-124）。
