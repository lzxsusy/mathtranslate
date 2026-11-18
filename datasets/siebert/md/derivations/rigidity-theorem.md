# Polishchuk 刚性定理的证明骨架

> `siebert/deriv/rigidity-theorem` ｜ track F ｜ draft

**目标**：证明定理 6.4（Polishchuk 刚性定理）：$A_L$ 上保持内部次数、扩张既定 $m_2$ 的极小 $A_\infty$ 结构，在严格 $A_\infty$ 同构（$f_1=\id$）与缩放的意义下唯一；由此 $A_L$ 连同其内部次数与 $A_\infty$ 结构决定 $D^b(X)$ 的 $A_\infty$ 范畴结构，进而决定导出范畴。

**自测**：为什么 $A_L$ 上除 $m_2$ 以外的高阶运算在严格同构与缩放下是唯一的，而不是可以任意形变？

## 前提

- $X$ 为 $d$ 维光滑射影簇（$d\ge1$），$L$ 为甚丰线丛，且对所有 $p\in\ZZ$ 与 $q\ne0,d$ 有 $H^q(X,L^{\otimes p})=0$；$\langle L\rangle=\{L^n:n\in\ZZ\}\subset D^b_{\mathrm{dg}}(X)$ 分裂生成 $D^b(X)$。
- $A_L=\bigoplus_{p,q\in\ZZ}H^p(X,L^q)$（6.42），$R_L=\bigoplus_{n\ge0}H^0(X,L^n)\subset A_L$（6.43）；$A_L$ 带极小 $A_\infty$ 代数结构（$m_1=0$），$m_2$ 由杯积给出。
- 内部次数由 $L$ 的幂给出（Note 6.3）；$A_L=R\oplus M$，$R=\bigoplus_{q\ge0}H^0(X,L^q)$（次数 $0$）、$M=\bigoplus_{q\le0}H^d(X,L^q)$（次数 $d$），$m_n:A^{\otimes n}\to A[2-n]$（6.46–6.48）。
- Hochschild 复形 $C^n(A,M)=\Hom_k(A_+^{\otimes n},M)$ 带上边缘 $\delta$（6.45、6.53），双分次 $HH^n_{0,m}$；目标是把「两个扩张的差异」放进这些上同调群。

## 步骤

1. **约化到代数：把 $D^b(X)$ 换成 $A_L$ 上的 $A_\infty$ 代数。$A_L=\Hom^\bullet_{D^b_{\mathrm{dg}}(X)}(\bigoplus_qL^q,\bigoplus_qL^q)$，而 $\langle L\rangle$ 分裂生成 $D^b(X)$，故 $A_L$ 连同内部次数与 $A_\infty$ 结构刻画 $D^b(X)$ 的 $A_\infty$ 范畴结构。**  
   为什么：分裂生成意味着 $D^b(X)$ 的对象都由 $L^q$ 经扭曲（Tw）得到，态射由 $A_L$ 的 $A_\infty$ 双模结构给出；于是「范畴的唯一性」化为「代数 $A_L$ 上 $A_\infty$ 结构的唯一性」，这是把几何问题代数化的关键一步。  
   锚点：原书 p.103（6.42–6.43）（证据 A）

2. **次数分析：设 $m_n$ 与 $m'_n$ 是两个扩张，$m_1=m'_1=0$、$m_2=m'_2$。若输入 $a_1,\ldots,a_n$ 中有 $k$ 个属于 $M$（次数 $d$），则输入总次数 $kd$、输出次数 $kd+2-n$；由 $A$ 只有次数 $0$ 与 $d$，得 $kd+2-n=0$ 或 $(k-1)d+2-n=0$（6.49）。**  
   为什么：这是把「一般的 $n$」压缩到「$n\equiv2\pmod d$」的唯一依据：$m_n$ 非零的必要条件是次数匹配，而 $A$ 只有两个次数，故 $n=ld+2$（$l=k$ 或 $k-1$）。  
   锚点：原书 p.104（6.46–6.49）（证据 A）

3. **一阶差异是上闭链：若 $m_i=m'_i$（$i<n$），则 $c=m_n-m'_n$ 满足 $\delta c=0$，即 $c$ 是 Hochschild $n$-上闭链（6.45）；并记 $c\in C^n_{0,n-2}=C^{ld+2}_{0,ld}$（6.50）。**  
   为什么：把 $m_n$ 与 $m'_n$ 各自的 $A_\infty$ 关系相减，$i<n$ 的项因两个结构相同而全部相消，剩下的恰好是 $\delta c$ 的三项（左乘、相邻相乘、右乘）；故「差异」=「上闭链」，这是形变理论的入口。  
   锚点：原书 p.103–104（6.45、6.50）（证据 A）

4. **同构只加上边缘：用保持低阶数据的严格 $A_\infty$ 同构（$f_1=\id$，$f_i=\id$ 对 $i<n$，$f_n$ 为新项）改变 $m_n$，只会把 $c$ 改成 $c+\delta f_n$。**  
   为什么：$A_\infty$ 函子方程在最低非平凡阶给出 $m'_n-m_n=\delta f_n$（符号由 Koszul 约定定）；因此 $[c]\in HH^n_{0,n-2}$ 与代表元、与同构的选取无关，是真正的形变不变量。  
   锚点：原书 p.104（§3.3 第 (ii) 条）（证据 A）

5. **计算 Hochschild 群（命题 6.5）：(i) 对所有 $l\ge1$ 及 $i<l(d+2)$，$HH^i_{0,ld}(A)=0$（6.57）；(ii) $\dim HH^{d+2}_{0,d}(A)\le1$。**  
   为什么：由第 2 步，非零差异只可能落在 $HH^{ld+2}_{0,ld}$；这一族群里除了 $l=1$ 的 $d+2$ 阶以外全部落在消失区，于是「无穷多个可能的形变参数」被压成「一个一维空间」。  
   锚点：原书 p.105（命题 6.5、6.57）（证据 A）

6. **推论 6.6：两个扩张严格 $A_\infty$ 同构，当且仅当 $[m_{d+2}-m'_{d+2}]=0\in HH^{d+2}_{0,d}(A)$（6.58）。证明是逐阶消去：在第一次不同的阶 $n=ld+2$，$l>1$ 时 $ld+2<l(d+2)$，由命题 6.5(i) 该类为零，可用同构消去；只剩 $l=1$。**  
   为什么：消去要求差异可写成上边缘，而上同调为零正是这个条件；归纳从低阶到高阶进行，每次用 $f_n$ 抹掉当前阶的差异，且不破坏更低阶（因为 $f_i=\id$）。  
   锚点：原书 p.105（推论 6.6、6.58）（证据 A）

7. **定理结论：由命题 6.5(ii) 与推论 6.6，要么所有高阶运算都能消去（结构可化为 $m_k=0,k>2$），要么非平凡结构在缩放意义下唯一——因为 $HH^{d+2}_{0,d}$ 至多一维，两个非零类只差一个标量，而该标量可由对 $A_L$ 的生成元作整体缩放吸收。**  
   为什么：一维性是「唯一到缩放」的全部内容：若 $\dim=2$ 就会有真正的模空间；若 $=0$ 则只能全消去。定理 6.4(i) 的「非平凡」条件把后一种可能排除，故剩下「唯一非零类」。  
   锚点：原书 p.105（定理 6.4 的证明）（证据 B）

8. **非平凡性（Note 6.6）：对光滑 $X$ 的典范结构 $[m_{d+2}]\ne0$，依据是取一点的理想层并作 Koszul 消解，得 $m_{d+2}\ne0$。**  
   为什么：没有这一步，定理 (i) 说的「非平凡」就可能是空的（结构全部可消去）；Koszul 消解给出显式的非零高阶运算，说明典范结构确实落在「一维非零类」这一支。  
   锚点：原书 p.105（Note 6.6）（证据 A）

9. **命题 6.5 的证明骨架：按输出次数分裂 $C^\bullet=C^\bullet(0)\oplus C^\bullet(d)$（6.59–6.61），得正合列 6.63；对 $C^\bullet(0)$ 按输出内部次数滤过（6.64–6.65），逐块识别 $(C^\bullet(0)_j,\delta_{j,j})=\Hom(K^\bullet_{l,j},R_j)[-l]$（6.67），$K^\bullet_l=B^\bullet(k,M,\ldots,M,k)$（6.68）为广义 bar 复形（6.69）；用双次数（6.70）得谱序列 $E_1$（6.71），由引理 6.7（$H^i(B^\bullet(M_1,M_2))=M$ 当 $i=-d-1$，否则 $0$，6.72）把 $E_1$ 化为更小的 $B^\bullet$，对 $n$ 归纳。**  
   为什么：这是把 $HH$ 计算归约到 bar 复形上同调的标准手法：$\delta$ 沿 $M$ 因子数不增，故可滤过；每消去一对 $M$ 因子 $n$ 严格下降，归纳终止，$l=1$ 时存活项给出 $\dim H^{d+2}(C^\bullet(0))\le1$。讲义注明这就是 Polishchuk 的命题 3.7。  
   锚点：原书 p.105–106（6.59–6.72）（证据 A）

## 结果

$A_L$ 上保持内部次数、扩张既定 $m_2$ 的极小 $A_\infty$ 结构，在严格 $A_\infty$ 同构（$f_1=\id$）与缩放下唯一（非平凡时）；严格同构的存在性完全由 $[m_{d+2}-m'_{d+2}]\in HH^{d+2}_{0,d}(A)$ 判定。于是 $D^b(X)\cong\operatorname{Tw}^\Pi\langle L\rangle$ 的 $A_\infty$ 范畴结构由 $A_L$ 这个 $A_\infty$ 代数决定：要证同调镜像对称，只需把两侧的环 $A_L$ 对齐并核对这一个高阶运算 $m_{d+2}$（Note 6.4）。

## 缺口

- 任务说明提到「$\mathrm{Hol}(\pi_0)$ 的 $A_\infty$ 结构与 $A_L$ 的 $A_\infty$ 结构同构 $\Rightarrow$ 导出范畴等价」，但讲义第 6 章通篇没有 $\mathrm{Hol}(\pi_0)$ 这个记号，也没有相应命题；讲义走的是 $A_L=\Hom^\bullet(\bigoplus L^q,\bigoplus L^q)$ 的路线。此处按讲义写，任务书中的说法待核对（可能指 B 模型一侧的某个全纯代数）。
- 「$\langle L\rangle$ 分裂生成 $D^b(X)$ $\Rightarrow$ $A_L$ 决定 $A_\infty$ 范畴」这一步讲义只用一句话带过（p.103），未证；严格陈述需要「Tw$^\Pi$ 的 Morita/导出等价」这类一般定理。
- 命题 6.5 的证明只给骨架：式 6.66、6.67 在原书与译文中都不完整；谱序列如何收敛回 $H^\bullet(C^\bullet)$、$l=1$ 时 $\dim H^{d+2}(C^\bullet(0))\le1$ 的具体计算、以及 $\delta_{j,j'}$ 的高阶项如何被吸收，均未展开。
- 定理 6.4 的条件在英文原文写「$q\ne0$」，译文改成「$q\ne0,d$」；由 $H^d(X,L^{\otimes p})\cong H^0(X,L^{\otimes(-p)})^*\ne0$，原文条件对 $d\ge1$ 不可能满足，译文更准——但这是译文对原文实质条件的修改，出版时需说明。
- 「缩放」的确切含义（对 $A_L$ 的生成元作整体标量重标？是否与内部次数相容？）讲义没有定义，只说「在缩放的意义下唯一」。

## 易错点

- 刚性定理不是说「$m_2$ 也唯一」：$m_2$ 是给定的杯积，定理只断言 $k>2$ 的高阶结构唯一（差缩放）。
- $HH^{d+2}_{0,d}$ 一维给出的是「唯一到标量」而非「严格唯一」；把「差一个缩放」说成「唯一」会在定理 6.4(i) 的条件上出错。
- 命题 6.5(ii) 的英文原文写 $\dim HH^{d+1}_{0,d}\le1$，与推论 6.6 的 $d+2$ 矛盾（原书笔误，译文已改 $d+2$）；引用原文时别照抄 $d+1$。
- bar 与 cobar 在原书里的用法与常见文献相反：6.51 的 $A_+\otimes\cdots\otimes A\to A\to k$ 叫 bar，6.53 的 $\Hom(A_+^{\otimes n},M)$ 复形叫 cobar；按原书读，别按名字猜。
- 「逐阶消去」需要 $l>1$ 时 $ld+2<l(d+2)$；$l=1$ 时等号成立，正好落在不消失的一维群里——这是整个证明的临界情形，不能一并消去。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 6 章 §3.1 约化到代数 $A_L$，p.103–103（原书 p.103）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 6 章 §3.2 $A_L$ 上的 $A_\infty$ 结构，p.103–103（原书 p.103）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 6 章 §3.6 刚性定理的证明，p.105–106（原书 p.105–106）

关联：`siebert/concept/hochschild-cohomology`、`siebert/concept/homological-mirror-symmetry`、`siebert/concept/fukaya-category`、`siebert/correction/polishchuk-numbering`

来源说明：原书 p.103–106 §3（6.42–6.72：$A_L$、Note 6.2–6.3、定理 6.4、命题 6.5、推论 6.6、Note 6.6）。Polishchuk 原文 arXiv:math/0302178（讲义 p.105 明确「这就是 Polishchuk 的命题 3.7」）；nLab「Hochschild cohomology」（last revised 2026-06-23）核对 bar 复形与双分次；nLab「homological mirror symmetry」（2024-04-01）核对该定理在 HMS 中的位置。$\mathrm{Hol}(\pi_0)$ 未在任何材料中出现，已在 gaps 中标注。
