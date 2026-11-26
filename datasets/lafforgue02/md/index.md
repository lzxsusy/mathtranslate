# Hausel ICM 2022（lafforgue02）资料卡索引

共 18 张：概念卡 14 张、推导卡 4 张。


## 轨道 A · 镜像对称与几何 Langlands


**概念卡**

- [chtouca 的模叠 $\mathrm{Cht}^r$ 与 $\mathrm{Cht}^r_N$](concepts/chtouca-moduli-stack.md) —— $\mathrm{Cht}^r$ 是秩 $r$ chtouca 的 DM 叠，$(\infty,0)$ 光滑地映到 $X\times X$、维数 $2r-2$；它是 $d$ 上无穷并，故非有限型——这正是要截断的理由。
- [完整同态（homomorphisme complet）](concepts/complete-homomorphism.md) —— 把 chtouca 定义里的「同构 $\tau\mathcal E\cong\mathcal E''$」放宽成同态 $\tau\mathcal E\Rightarrow\mathcal E''$，并记下逐级退化的数据 $(\mathcal L_s,\ell_s,v_s)$；这放宽后的模问题给出第 III 章的紧化。
- [Drinfeld chtouca（带水平结构）](concepts/drinfeld-chtouca.md) —— $X\times S$ 上一对秩 $r$ 丛的三角 $\mathcal E\to\mathcal E'\leftarrow\mathcal E''$ 加 $\tau\mathcal E\cong\mathcal E''$，修正只在 $\infty,0$ 两点；水平结构是 $N$ 处对 $\mathcal O^r$ 的平凡化。
- [fourre-tout（不分离的「杂物袋」叠）](concepts/fourre-tout.md) —— 第 III 章用一个不分离的叠 $\ol{\Cht}^{\,r}$ 把所有截断紧化都收作开子叠，讲义称之为 fourre-tout；它的边界分层给出 $\Cht^r_{\underline r}\to\Cht^{r_1}\times_X\cdots$ 的逐层分解。
- [Harder–Narasimhan 截断与截断多边形](concepts/harder-narasimhan-truncation.md) —— 给秩 $r$ 丛按 Harder–Narasimhan 多边形排序，用足够凸的截断多边形 $p:[0,r]\to\mathbb R_+$ 切出 $\Cht^{r,\overline p\le p}$；这是有限型、承载不动点计数的开子叠。
- [Hecke 对应与 Hecke 代数](concepts/hecke-correspondence.md) —— 双陪集 $K_TgK_T$ 给出 $\mathrm{Cht}^r$ 上的有限型对应；它稳定截断开子叠，但在紧化上只「在不动点附近」稳定，故不能直接给出 $\mathcal H^r_N$ 的模作用。
- [函数域上的 Langlands 对应（$\mathrm{GL}_r$）](concepts/langlands-correspondence-function-field.md) —— 对函数域 $F=\mathbb F_q(X)$：$\mathrm{GL}_r$ 的尖点自守表示与 $r$ 维 $\ell$-进 Weil 表示一一对应，且逐位点匹配局部对应与 $L$、$\varepsilon$ 因子。
- [配对 $L$-函数（fonction $L$ de paires）](concepts/lfunction-pairs.md) —— 可忽略部分的排除靠对数导数在 $|Z|<q^{-2+2\varepsilon}$ 内绝对收敛；这恰是配对 $L$-函数（自守侧与 Galois 侧各一对）的收敛性估计。
- [$r$-可忽略表示与本质上同调](concepts/r-negligible-representation.md) —— $r$-可忽略表示是 $q'^*\sigma_1\otimes q''^*\sigma_2$（$\dim\sigma_i<r$）的直和项；不是它的叫本质的。本质部分才承载 Langlands 对应的解。
- [本质同调上的迹公式](concepts/trace-formula-essential-cohomology.md) —— Hecke 代数在本质部分上的作用由一条「不动点定理」给出：对 $f\times\mathrm{Frob}_x^{-s/\deg x}$ 的迹写成 $q^{(r-1)s}\sum_\pi\mathrm{Tr}_\pi(f)$ 乘两个局部和。
- [紧合性的赋值判据](concepts/valuative-criterion-properness.md) —— 要证 $\ol{\Cht}^{\,r,d,\overline p\le p}$ 在 $X\times X$ 上紧合，只需对每个离散赋值环 $A$ 验证：任意 $K_A$-点都能延拓为 $A$-点；这一步把问题化成构造一个迭代 $\varphi$-格。

**推导卡**

- [为什么本质部分集中在中间次数 $2r-2$](derivations/essential-part-in-middle-degree.md) —— 用配对 $L$-函数的收敛性排除可忽略分量，再用权论证排除「权 $>0$」：本质部分只能出现在 $2r-2$，且是权 $0$ 纯的。
- [从截断读到 Langlands 对应：迹公式如何给出 $\sigma_\pi$](derivations/trace-from-truncation.md) —— 把迹公式右端的 $\mathrm{Tr}_\pi(f)$ 与左端的几何迹比对，逐个 $\pi$ 得到 $H_\pi$；再由 $H_\pi\cong q'^*\sigma\otimes q''^*\check\sigma$ 认出 $\sigma_\pi$，最后用 Chebotarev 得整体双射。
- [从截断到紧化：三个对象与三次取舍](derivations/truncation-to-compactification.md) —— 开叠光滑但不有限型、不动点计数无意义；截断后有限型、可数不动点但破坏 Hecke 稳定性；紧化后紧合光滑、Hecke 在不动点附近稳定，却不再有 $\mathcal H^r_N$ 的作用。

## 轨道 B · 拓扑镜像对称与 Hodge 数


**概念卡**

- [退化子（dégénérateur）](concepts/degenerator.md) —— 初等变换把一个迭代 $\varphi$-格换成另一个时，中间会出现一族「半退化」的对象，讲义称其成员为退化子；追踪这一族如何避开水平 $N$ 是全局稳定性定理的关键。
- [Hecke 对应的全局稳定性定理](concepts/global-stability-hecke.md) —— 若两个截断 chtouca 在 Hecke 意义下相互对应且都延拓到整族，则它们特殊化后的极点、零点与退化子只相差 Frob 的一个幂。
- [迭代 $\varphi$-格](concepts/iterated-phi-lattice.md) —— 在 chtouca 的一般纤维的 $\varphi$-空间里，$\varphi$-格是满足 $\varphi(M)\subset M$ 的格；迭代 $\varphi$-格再叠上 HN 滤过与完整同态，用来把「退化」变成可数对象。

**推导卡**

- [用赋值判据把紧合性化归为构造一个 $\varphi$-格](derivations/properness-by-valuative-criterion.md) —— 紧合性 $\rightsquigarrow$ 赋值判据 $\rightsquigarrow$ 一般纤维上的 $\varphi$-空间 $\rightsquigarrow$ 造一个满足 $p$ 的迭代 $\varphi$-格；第 V 章给路线，第 VI 章给构造。
