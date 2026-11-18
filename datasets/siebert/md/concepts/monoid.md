# 幺半群与格点幺半群

> `siebert/concept/monoid` ｜ track D ｜ draft

**一句话**：带单位元的结合乘法集合；凸锥的整点是饱和幺半群，Gordan 引理保证它有限生成，故其幺半群环是有限型代数。

**自测**：为什么环面簇的坐标环要写成格点幺半群的幺半群环，而不是任意一个有限生成代数？

## 定义

幺半群是带单位元 $1$、乘法满足结合律的集合；环面几何里用的是加法幺半群 $S\subset M$：$0\in S$ 且 $S+S\subset S$。若 $C\subset M_{\RR}$ 是凸锥，则整点集 $C\cap M$ 对加法封闭、含原点，是幺半群。它还是饱和的：对 $m\in M$ 与正整数 $\lambda$，$\lambda m\in C\cap M$ 蕴含 $m\in C\cap M$。锥不含非零线性子空间时，其可逆元群平凡。

记号：$M\simeq\ZZ^{d}$ 是秩 $d$ 的自由阿贝尔群，$N=\Hom_{\ZZ}(M,\ZZ)$；$S=C\cap M$；$k[S]$ 是幺半群环；$\mathrm{Mon}$ 是幺半群范畴，$\Hom_{\Mon}$ 记其态射集。

## 要点

- 锥 $C$ 的整点集 $C\cap M$ 自动对加法封闭且含原点，故是幺半群；$C$ 凸时还饱和（引理 4.1）。可逆元群平凡当且仅当 $C$ 不含非零线性子空间，这一点让「环面」$\Spec k[M]$ 能真的嵌进去。
- 饱和性要单独验，不能从「幺半群」推出：$M=\ZZ$、$P=2\NN+3\NN$ 中 $2\in P$ 而 $1\notin P$，故 $P$ 不饱和（例 4.1）。
- 有限生成是另一件事：锥由构成格基的 $d$ 个向量生成（行列式 $\pm1$）时 $C\cap M\simeq\NN^{d}$；否则是带关系的有限生成幺半群，如 $\NN^{3}/\bigl((0,k+1,0)\sim(1,0,1)\bigr)$（例 4.2）。
- 有限生成 $+$ 饱和 $\Rightarrow$ $k[C\cap M]$ 正规；Gordan 引理正是补上有限生成的那一步（要求 $C$ 有理多面）。
- 有限生成性可以失败：$C=\{0\}\cup(\RR_{\ge0}\times\RR_{>0})$ 的整点幺半群不有限生成，所有 $(a,1)$ 都得当生成元（例 4.3），因为这个 $C$ 不是有理多面锥。

## 公式

$S=\sigma^{\vee}\cap M,\qquad \lambda m\in S\ \text{且}\ \lambda\in\ZZ_{>0}\ \Longrightarrow\ m\in S$
$C\cap M=\langle(0,1),(1,0),(k+1,-1)\rangle\simeq\NN^{3}/\bigl((0,k+1,0)\sim(1,0,1)\bigr)$
$k[S]=\Bigl\{\sum_{m\in S}a_m\chi^{m}:a_m\in k\Bigr\},\qquad \chi^{m}\chi^{m'}=\chi^{m+m'}$

## 定理与证明

### 引理 4.1：凸锥的整点是饱和幺半群

若 $C\subset M_{\RR}$ 是凸锥，则 $(C\cap M,+)$ 是饱和幺半群，加法单位元为原点且交换。

（none；来源：原书 p.59）


缺口：讲义只作陈述，未写证明。证明是逐条验证：$C$ 含 $0$ 故 $0\in C\cap M$；$C$ 凸锥故 $a,b\in C$ 蕴含 $a+b\in C$，加法交换；$\lambda m\in C$ 且 $C$ 对正数倍封闭，故 $m\in C$，即饱和。

### 命题 4.2（Gordan 引理）

若 $C\subset M_{\RR}$ 是有理多面锥，则 $C\cap M$ 有限生成。等价地，$k[C\cap M]$ 是有限生成 $k$ 代数。

（complete；来源：原书 p.60）

1. 把生成向量按正整数倍放大，使 $m_1,\ldots,m_r\in M$；放大只改生成元、不改 $C$。  
   为什么：$C$ 的定义只要求 $m_i\in M_{\QQ}$，而整数格点论证需要生成元落在 $M$ 里。
2. 令 $K=\{\sum_i t_im_i:0\le t_i\le1\}\subset M_{\RR}$，它是紧集，故 $K\cap M$ 有限。  
   为什么：有限性是结论的核心，而紧集的格点只有有限多个，这是唯一用到紧性的地方。
3. 断言 $K\cap M$ 生成 $C\cap M$：对 $u=\sum r_im_i$（$r_i\ge0$）写 $r_i=s_i+t_i$，$s_i\in\NN$、$t_i\in[0,1)$，则 $u=\sum s_im_i+\sum t_im_i$，第一项由 $m_i$（$\in K\cap M$）生成，第二项落在 $K\cap M$。  
   为什么：把任意格点拆成「整数部分 $+$ 紧集里的小数部分」，就把生成集缩到有限集 $K\cap M$。

## 易错点

- 「幺半群」不等于「群」：$C\cap M$ 一般没有加法逆元；写成 $\Spec k[C\cap M]$ 时，逆元缺失正是它比环面 $\Spec k[M]$ 多出边界的来源。
- 饱和与有限生成互相独立：例 4.1 的 $2\NN+3\NN$ 有限生成但不饱和；例 4.3 的锥既非有理多面也不有限生成。不要用一个去推另一个。
- $(\pm1,\pm1,\pm1)$ 这类写法里 $\pm$ 是逐坐标独立取的，不是整体取两个符号；这在顶点集与多胞体的区分上会反复出现。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 4 章 §1 幺半群与锥，p.59–60（原书 p.59–60）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 4 章 §2 幺半群环，p.60–60（原书 p.60）

关联：`siebert/concept/rational-polyhedral-cone`、`siebert/concept/affine-toric-variety`、`siebert/concept/toric-variety`

来源说明：原书 p.59–60（§1 幺半群与锥、§2 幺半群环：Def 4.1、引理 4.1、例 4.1–4.3、Def 4.2）。核过 nLab「monoid」（last revised 2026-11-07：集合带结合乘法与单位元，即 unital associative magma）；nLab 无「monoid ring」条目，有限生成性依原文与 Gordan 引理；Stacks Project 无对应章节。
