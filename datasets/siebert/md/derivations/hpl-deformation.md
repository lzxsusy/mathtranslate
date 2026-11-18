# 用同调扰动引理把 Čech 模型搬到上同调上

> `siebert/deriv/hpl-deformation` ｜ track F ｜ draft

**目标**：用同调扰动引理把 Čech 模型 $\mathcal A=D^b_{\mathrm{dg}}(X)$（严格 dg 范畴）的运算转移到上同调 $H(\mathcal A)=D^b(X)$ 上，得到极小 $A_\infty$ 结构：$m_1=0$、$m_2=p\,m_2\,i$、高阶 $m_k$ 由带根带状树的递归给出，从而说明 $D^b(X)$ 上的 $A_\infty$ 结构一般不是 dg 的。

**自测**：从严格 dg 的 Čech 模型出发，$D^b(X)$ 上的 $A_\infty$ 结构为什么会长出非零的 $m_3,m_4,\ldots$？

## 前提

- $X$ 光滑射影，$\mathscr U=\{U_i\}$ 为有限仿射覆盖；$\mathcal A=D^b_{\mathrm{dg}}(X)$ 是 §2.1 的 Čech 模型：对象为局部自由层的有界复形，$\Hom^n=\bigoplus_{p+q=n}\check C^p(\mathscr U,\mathcal Hom^q)$，$m_1=\check\delta+d_{\mathcal Hom}$，$m_2(g,f)=(-1)^{\deg f}g\circ f$，且 $m_k=0$（$k\ge3$）。
- 目标范畴 $H(\mathcal A)=D^b(X)$：对象不变，态射取 $H^*(\Hom_{\mathcal A})$；要在这个范畴上重新定义 $m_k$ 使 $A_\infty$ 关系成立。
- 收缩数据（讲义只写 $\Pi,H$，这里拆成标准三元组）：$i:H^*(\Hom)\hookrightarrow\Hom$ 为闭代表元的含入（次数 $0$），$p:\Hom\twoheadrightarrow H^*(\Hom)$ 为取上同调类（次数 $0$），$h:\Hom\to\Hom[-1]$ 为同伦；满足 $pi=\id$、$ip-\id=m_1h+hm_1$、$hi=0$、$ph=0$、$h^2=0$、$hm_1h=h$。原书的 $\Pi=ip$、$H=h$。
- 树的约定：带根带状树 $T$ 有 $k$ 个叶子与若干内部顶点；内部顶点有 $r+1$ 条邻接边时放 $m_r$，内部边放 $h$，根边放 $p$；$m_{k,T}$ 记这棵树给出的复合。

## 步骤

1. **对每对对象选收缩数据 $(i,p,h)$，即把复形 $\Hom^\bullet$ 换成其上同调并记住「怎么换回去」；验证 $pi=\id$ 与 $ip-\id=m_1h+hm_1$。**  
   为什么：域上每个上同调类都能选一个闭代表元，故 $i$ 与 $p$ 可按线性代数直接取；$h$ 的存在正是「闭代表元子空间是直和项」的等价说法，而 6.31 就是这个直和分解的公式化。  
   锚点：原书 p.101（6.29–6.31）（证据 B）

2. **令 $\Hom_{\Pi\mathcal A}(X,Y)=\Pi\Hom_{\mathcal A}(X,Y)\subset\Hom_{\mathcal A}(X,Y)$（6.32），对象不变，得新范畴 $\Pi\mathcal A$；识别 $H(\Pi\mathcal A)=H(\mathcal A)$。**  
   为什么：$\Pi=ip$ 的像恰是每个上同调类的闭代表元，取 $\Pi$ 的像再取上同调与直接取上同调给出同一个向量空间；这一步保证「搬家」不改变同调层面。  
   锚点：原书 p.101（6.32）（证据 A）

3. **一阶运算：$m_1^\Pi=m_1$（式 6.33）；把 $\Pi\mathcal A$ 的态射等同于 $H(\mathcal A)$ 后 $m_1=0$，这就是「极小」的含义。**  
   为什么：$\Pi$ 的像由 $m_1$-闭元组成，而 $\Pi$ 又把 $m_1$ 的像杀掉（$\Pi m_1=0$ 由 $\Pi-\id=m_1h+hm_1$ 与 $\Pi$ 投影到 $\ker m_1$ 得到）；故在 $H(\mathcal A)$ 上 $m_1$ 作用为零。  
   锚点：原书 p.101（6.33）（证据 A）

4. **二阶运算：$m_2^\Pi=\Pi\circ m_2$（式 6.34），即 $m_2=p\,m_2\,(i\otimes i)$——一条只有根的树：内部顶点放 $m_2$，根边放 $p$，两个叶子接 $i$ 进来的元素。**  
   为什么：两叶树只有一种形状（一个内部顶点、两条叶子边、一条根边），故二阶项没有 $h$ 插入的余地；6.34 省略 $i\otimes i$ 是因为它把定义域已经写成 $\Pi\Hom$，而 $\Pi=ip$、$pi=\id$ 把 $i$ 吸收了。  
   锚点：原书 p.101（6.34）（证据 B）

5. **高阶运算：对 $k\ge3$ 令 $m_k^\Pi=\sum_{T}m_{k,T}$，$T$ 过所有 $k$ 叶带根带状树，按 Feynman 规则（内部顶点 $m_r$、内部边 $h$、根端 $p$）复合（6.35）。**  
   为什么：$A_\infty$ 关系在 $k\ge3$ 时不再自动成立：$m_2$ 一般不结合，偏差必须由 $m_3$ 补偿；而所有可能的补偿方式恰好对应「在 $m_2$ 的复合树里插入若干次 $h$ 把中间结果搬回闭代表元」，这就是树求和。  
   锚点：原书 p.101（6.35）（证据 A）

6. **例（$k=6$）：取一棵带根带状树，其贡献为 $m_{6,T}(a_1,\ldots,a_6)=\Pi m_3(a_1,Hm_2(Hm_3(a_2,a_3,a_4),a_5),a_6)$（6.36）。**  
   为什么：这个例子把规则摊开：根端 $\Pi$、外层顶点 $m_3$、内部边两次插入 $H$、内层顶点 $m_3$ 与 $m_2$ 各一；可见高阶项就是 $m_r$ 与 $H$ 的交替复合，$k$ 越大树越多。  
   锚点：原书 p.102（例 6.3、图 6.7）（证据 A）

7. **验证 $A_\infty$ 关系（引理 6.2）：对每个 $k$ 考虑 $\mu_k=\sum_{T,e}\mu_{k,(T,e)}$（6.39），对内部边用 $\Pi-\id$ 与用 $m_1H+Hm_1$ 两种方式整理，得 $\mu_k=\mu_k^{m_1}+(\mu_k^\Pi-\mu_k^\id)$（6.40）；核对符号 $\mu_k=-\mu_k^\id$，于是 $\mu_k^{m_1}+\mu_k^\Pi=0$（6.41）。**  
   为什么：6.41 逐项就是 $m_k^\Pi$ 的 $A_\infty$ 关系：$\mu_k^{m_1}$ 收集所有「$m_1$ 作用在某个输入或输出上」的项，$\mu_k^\Pi$ 收集树求和项；两者相消即关系成立。用 $m_1H+Hm_1$ 替换 $\Pi-\id$ 是关键，它把「投影差」翻译成「$m_1$ 的复合」，才能与 $m_r$ 的 $A_\infty$ 关系对接。  
   锚点：原书 p.102（6.39–6.41）（证据 A）

8. **造拟等价（引理 6.3）：令 $i_1$ 为含入 $\Pi\mathcal A\hookrightarrow\mathcal A$，$i_k=\sum_T i_{k,T}$（$k\ge2$）与 $m_{k,T}$ 同构造但把根端的 $\Pi$ 换成 $H$（6.37–6.38）；则 $(i_k)$ 是 $A_\infty$ 函子，且在 $H$ 上诱导同构，故 $H(\mathcal A)\to\mathcal A$ 是 $A_\infty$ 拟等价。**  
   为什么：只有「存在拟等价」才能说 $H(\mathcal A)$ 上的极小结构与原来的 dg 结构是同一个对象的两种模型；否则搬过去的结构可能与原结构无关。$i_1$ 在 $H$ 上就是恒等，故可逆。  
   锚点：原书 p.102（Note 6.1、引理 6.3）（证据 A）

## 结果

$H(D^b_{\mathrm{dg}}(X))=D^b(X)$ 上得到极小 $A_\infty$ 结构：$m_1=0$，$m_2=p\,m_2^{\check C}\,(i\otimes i)$（即把 Čech 模型的复合经收缩搬到上同调），$m_k=\sum_T m_{k,T}$（$k\ge3$）由树求和递归给出；并且 $H(\mathcal A)\to\mathcal A$ 是 $A_\infty$ 拟等价。因此 $D^b(X)$ 上的 $A_\infty$ 结构由 Čech 模型唯一决定（差拟等价），而它一般不是 dg 的：$m_k^\Pi\ne0$ 恰恰是「Čech 模型的严格结合律在上同调层面失效」的度量。

## 缺口

- 讲义只给「证明概要」：6.39–6.41 的符号核对、树的双射（同一棵树的不同平面嵌入如何计数、是否重复）都没有写清；例 6.3 只给一棵树。
- 讲义没有写 $i,p,h$ 三元组与收缩恒等式，只写 $\Pi$ 与 $H$；本卡按 nLab 版 HPL 的标准数据补全，需核对与原书 6.31 的对应（$\Pi=ip$，且 6.31 的 $\Pi-\id=m_1H+Hm_1$ 与 $ip-\id=m_1h+hm_1$ 一致）。
- 收敛性未讨论：无穷树求和要求滤过有界、$h$ 降低滤过且 $\Phi(1+d^\tau\Phi)^r$ 可和（nLab 版的条件）；在 Čech 模型上 $\check C^p$ 的 $p$-滤过是否满足，讲义未验证。
- $\Pi$ 的选取依赖「闭代表元」的选择，不同选择给出的 $m_k^\Pi$ 只差 $A_\infty$ 同构；讲义未证这一点（引理 6.2–6.3 只保证同一选择下成立）。
- 「$m_2^\Pi=\Pi\circ m_2$」与「$m_2=p\,m\,i$」的等价只在把定义域限制到 $\Pi\Hom$ 后成立；若把 $m_2^\Pi$ 看成 $\Hom\otimes\Hom$ 上的映射，必须显式写 $i\otimes i$，讲义未提醒。

## 易错点

- $m_2=p\,m\,i$ 里的 $i$ 是 $i\otimes i$（两个变量各插一个 $i$），不是单个 $i$；写错会使复合的次数不对。
- 高阶项不是「任选一棵树」：求和过所有 $k$ 叶带根带状树，包括平面嵌入不同的树，且每棵树的叶子顺序与输入顺序一致。
- $h$ 不唯一，但它只影响中间代表元的选取；最终 $m_k^\Pi$ 的同伦类与 $A_\infty$ 同构类不依赖 $h$（讲义未证，属标准事实）。
- 极小（$m_1=0$）是在 $H(\mathcal A)$ 上说的；若把 $\Pi\mathcal A$ 当成 $\mathcal A$ 的子范畴，$m_1$ 并不为零，只是其像被 $\Pi$ 杀掉。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 6 章 §2.2 同调扰动引理，p.101–102（原书 p.101–102）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 6 章 §2.1 导出范畴的 Čech 模型，p.100–101（原书 p.100–101）

关联：`siebert/concept/homological-perturbation-lemma`、`siebert/concept/cech-model`、`siebert/concept/dg-category`、`siebert/concept/hochschild-cohomology`

来源说明：原书 p.101–102 §2.2（定理 6.1 的构造：6.29–6.41、例 6.3、引理 6.2–6.3）、p.100–101 §2.1（Čech 模型的 $m_1,m_2$）。nLab「homological perturbation theory」（last revised 2025-04-12）给出标准收缩数据 $(f,\nabla,\Phi)$ 与 $f\nabla=1$、$\nabla f=1+d\Phi+\Phi d$、$\Phi^2=0$、$\Phi d\Phi=-\Phi$，据此把讲义的 $(\Pi,H)$ 补成 $(p,i,h)$；nLab「A-infinity algebra」（2026-07-09）核对树公式即 $A_\infty$ 关系的展开。
