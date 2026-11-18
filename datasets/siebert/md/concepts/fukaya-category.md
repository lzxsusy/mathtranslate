# Fukaya 范畴

> `siebert/concept/fukaya-category` ｜ track F ｜ draft

**一句话**：以 Lagrange 子流形为对象、以圆盘计数为高阶运算的 A∞ 范畴；导出化后得到三角范畴 D^bF(X)。

**自测**：为什么 Fukaya『范畴』的复合只在同伦意义下成立，却仍能当范畴来用？

## 定义

设 $(X,\omega)$ 紧、$c_1(X)=0$，取定向、自旋、分次且无障碍（无以 $L_i$ 为边界的非恒值全纯圆盘）的 Lagrange 子流形，并配 $U(1)$ 局部系统。$\mathcal F(X)$ 的对象是这些 $L$，态射 $\hom(L,L')=\CC^{L\cap L'}$（横截时，6.1），高阶运算\n$$m_k:\Hom(L_{k-1},L_k)\otimes\cdots\otimes\Hom(L_0,L_1)\longrightarrow\Hom(L_0,L_k)[2-k]$$\n由以 $L_0\cup\cdots\cup L_k$ 为边界的 $J$ 全纯圆盘计数给出（Def 6.2），系数在 Novikov 环 $\Lambda_{nov}$ 中。

记号：$m_k$ 的次数为 $2-k$；$\Lambda_{nov}=\{\sum a_iq^{\lambda_i}:\lambda_i\in\RR,\lambda_i\to+\infty\}$；$\mathrm{Tw}$ 扭曲复形；$\mathrm{Tw}^\Pi$ 分裂闭包（扭曲复形 + 幂等元像的完备化）。

## 要点

- A∞ 关系：$m_1^2=0$（$m_1$ 是微分）、$m_1$ 是 $m_2$ 的分次导子、$m_2$ 不必结合而 $m_3$ 给出结合性的同伦，一般关系见（6.10）（p.98）。
- 先验只是预范畴：横截相交时 $\Hom(L,L)=\CC^{L\cap L}$ 没有单位元可言，须用 Hamilton 扰动 $\varphi_1(L')\pitchfork L$；所得范畴在典范 A∞ 拟等价下良定义（p.99）。
- $H(\mathcal F(X))$ 是幺范畴（c-unital：存在 $e_L$ 在 $m_2$ 下是单位、且以它为输入时 $k>2$ 的 $m_k$ 为零），并与某严格幺 A∞ 范畴 A∞ 拟等价（p.99–100）。
- 导出化：$\mathrm{Tw}\mathcal F(X)$ 的对象由 $\Delta=(\delta_{ij})$（$j\ge i$ 时 $\delta_{ij}=0$，严格下三角）与 Maurer–Cartan 方程 $\sum_{r\ge1}m_r(\Delta,\ldots,\Delta)=0$ 描述（6.17）。
- 高亏格情形没有定义（讲义脚注：还没有人敢定义）；本卡只涉及亏格零。

## 公式

$$\hom(L,L')=\CC^{L\cap L'}$$
$$m_k:\Hom(L_{k-1},L_k)\otimes\cdots\otimes\Hom(L_0,L_1)\to\Hom(L_0,L_k)[2-k]$$
$$\sum_{r\ge1}m_r(\Delta,\ldots,\Delta)=0\qquad(\text{Maurer–Cartan})$$
$$\Lambda_{nov}=\Bigl\{\sum_{i\ge0}a_iq^{\lambda_i}:\lambda_i\in\RR,\ \lambda_i\to+\infty,\ a_i\in\ZZ\Bigr\}$$

## 定理与证明

### Thm 6.1：同调扰动引理（HPL）

对任意域上的 A∞ 范畴 $\mathcal A$，其同调 $H(\mathcal A)$ 上存在 $m_1=0$ 的 A∞ 范畴结构（极小 A∞ 结构），并有 A∞ 拟等价 $H(\mathcal A)\to\mathcal A$。

（sketch；来源：原书 p.101–102（Thm 6.1、Lemma 6.2–6.3））

1. 对每对对象选投影 $\Pi:\Hom\to\Hom$（次数 0、$\Pi^2=\Pi$，像是闭代表元）与同伦 $H$，使 $\Pi-\id=m_1H+Hm_1$（6.31）。  
   为什么：这就是 Hodge 理论里的『投影到调和代表元 + 同伦』，是把复形传上同调的标准工具。
2. 在上同调上定义 $m_k^\Pi=\sum_Tm_{k,T}$（$T$ 遍历带根带状树），内部顶点放 $m_r$、内部边放 $H$、根端放 $\Pi$（6.35）。  
   为什么：树公式保证新运算满足 A∞ 关系，且与原来的 $m_2$ 在上同调层一致。
3. 用 $\Pi-\id=m_1H+Hm_1$ 的两种整理方式比较，得 $\mu_k^{m_1}+\mu_k^\Pi=0$，这正是 $m_k^\Pi$ 的 A∞ 关系（Lemma 6.2）；再用 $i_k$（根端换成 $H$）构造拟等价（Lemma 6.3）。  
   为什么：两种整理分别按边与按内部顶点分类，差额恰好是 A∞ 关系。

缺口：讲义给了完整证明的骨架（6.39–6.41）与树公式，但符号核对（分次符号）只写『核对后』。

### A∞ 关系的头几条

$m_1^2=0$；$m_1m_2=m_2(m_1\otimes\id+\id\otimes m_1)$；$m_2(\id\otimes m_2-m_2\otimes\id)=m_1m_3+m_3(m_1\otimes\id\otimes\id+\id\otimes m_1\otimes\id+\id\otimes\id\otimes m_1)$。

（complete；来源：原书 p.98（6.7–6.10））

1. 在一般 A∞ 关系（6.10）中取 $k=1$：唯一合法的指标是 $(p,q)=(1,0)$，得 $m_1(m_1(a_1))=0$。  
   为什么：求和条件 $p\ge1,q\ge0,p+q\le k$ 在 $k=1$ 时只允许 $p=1,q=0$。
2. 取 $k=2$：合法项为 $p=1$ 与 $p=2,q=0,1$，整理即得分次 Leibniz 规则。  
   为什么：这正是『$m_1$ 是 $m_2$ 的导子』的展开。
3. 取 $k=3$：$p=1,2,3$ 的项给出 $m_1m_3$ 与三个 $m_3(m_1\otimes\cdots)$，$p=2$ 的两项给出 $m_2(\id\otimes m_2-m_2\otimes\id)$。  
   为什么：这就是 $m_3$ 作为『结合性同伦』的精确含义。

## 易错点

- $m_2$ 不必结合：把它当严格范畴会丢掉 $m_3$；只有取上同调 $H(\mathcal F(X))$（此时 $m_1=0$）之后才是普通范畴。
- 系数是 Novikov 环/域而不是 $\CC$：圆盘面积可以任意小，普通幂级数不收敛，$q^{\lambda}$ 形式参数不可省。
- 无障碍（unobstructed）条件不能省：存在以 $L$ 为边界的非恒值全纯圆盘时，$m_0$ 出现、$m_1^2=0$ 失效，A∞ 结构要加 $m_0$（『有障碍』）。
- $\mathcal F(X)$ 本身不是三角范畴：必须先取 $\mathrm{Tw}$、再取 $H^0$、再加幂等元（$\mathrm{Tw}^\Pi$），否则同调镜像的陈述无法写出来。
- 对象带 $U(1)$ 局部系统与分次结构，换这些数据会改变 $\mathcal F(X)$；不要把它当成『只由 Lagrange 子流形决定』的范畴。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 6 章 §1 概览，p.95–100（原书 p.95–100）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 6 章 §2 导出范畴的微分分次增强与同调扰动引理，p.100–102（原书 p.100–102）

关联：`siebert/concept/homological-mirror-symmetry`、`siebert/concept/mirror-symmetry`、`siebert/concept/gromov-witten-invariant`

来源说明：原书 p.95–102（6.1–6.18、Def 6.1–6.2、例 6.1–6.3、Thm 6.1、Lemma 6.2–6.3）。nLab「Fukaya category」（last revised 2026-01-17）核过对象/态射与 A∞ 约定；Stacks Project 无对应章节。
