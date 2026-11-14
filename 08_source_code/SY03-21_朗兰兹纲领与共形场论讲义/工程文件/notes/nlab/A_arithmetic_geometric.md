# nLab 调研稿 A：算术与几何基础概念

- 调研范围：Frenkel《朗兰兹纲领与共形场论讲义》（arXiv:hep-th/0512172）§1–§9 中 25 个算术／几何术语，按术语清单顺序排列，供译者撰写 [译注] 直接取材。
- 日期：2026-11-13。
- 来源：以 nLab 条目（ncatlab.org/nlab）为主，辅以 nLab 所引原始文献与 Wikipedia；nLab 无独立条目者已注明，并改引最接近的条目。

## 阿代尔环（adèle ring）

- **一句话定义**：整体域 $k$ 在全部位 $v$ 的完备化 $k_v$ 的「限制积」$\AD_k=\prod'_v k_v$，只允许有限个分量不适合赋值（范数 $>1$）。
- **来历**：1930 年代 Chevalley（1936）与 Weil（1938）为把类域论从「理想／伊代尔」语言改写成「所有完备化一起看」而引入；Tate 1950 年的论文把它变成 $\AD$ 上的调和分析。nLab 记：经典代数数论把数域嵌入其完备化的笛卡尔积，而限制积才是对的结构。
- **在讲义中的位置**：§1.6（`latex/en/e01b.tex:176`）把自守表示定义在 $GL_2(\AD_\Q)$ 上；§3.2（`e03a.tex:168`，尤其 205 行「key observation due to A. Weil」）用 $\Bun_n(\C)=GL_n(F)\backslash GL_n(\AD)/GL_n(\OO)$ 把双商「几何化」。索引 p.11、29。
- **原文为何未解释**：讲义默认读者熟悉限制积、$\AD$ 上的 Haar 测度与 $\OO=\prod_v\OO_v$；只学过理想语言的中文读者会卡在 $\prod'_v$ 与「有限个分量在 $\OO_v$ 外」这一条件上。
- **要点 / 常见误解**：
  - 它是限制积而非直积；$\AD_\Q\simeq\Q\otimes_\Z(\R\times\hat\Z)$，伊代尔群是其单位群。
  - $k$ 在 $\AD_k$ 中离散、$\AD_k/k$ 紧——这才是自守形式能谈「格」与「基本域」的原因；$\AD_k$ 作为可加群还是 Pontryagin 自对偶的。
  - 函数域情形每个分量就是曲线在一点的形式／穿孔圆盘，于是 $\AD$ 上的双商恰是向量丛的 Čech 描述——§3.2 的全部内容就是这句话。
- **nLab**：<https://ncatlab.org/nlab/show/ring+of+adeles>

## 自守表示（automorphic representation）

- **一句话定义**：$G(\AD)$ 在 $L^2(G(F)\backslash G(\AD))$ 的适当子空间（$K$-有限、$\mathfrak z$-有限、光滑）中的不可约子表示；经典自守形式是其 $K$-有限向量。
- **来历**：从 Poincaré 1880 年代的 Fuchs 函数与自守形式，经 Hecke 的模形式理论，到 1950–60 年代 Harish-Chandra、Gelfand–Graev 与 Langlands 把它表示论化；「自守表示」作为标准术语在 Langlands 纲领（1967 起）中定型。nLab 的 automorphic form 条即以此为主线，并引 Gelbart 1984 综述。
- **在讲义中的位置**：§1.6（`e01b.tex:176`）用 $GL_2(\AD_\Q)$ 的自守表示对应经典模形式；§2.3（`e02.tex:331`）函数域情形；§9.7（`e09d.tex:1` 起）用未分歧／分歧自守表示讲局部对应。索引 p.16。
- **原文为何未解释**：讲义直接使用「$f_\pi$ 是 $K$-有限向量」，不定义尖点性、离散谱与 $L^2$ 分解；读者不知道为何必须取 $K$-有限、为什么 $G(F)\backslash G(\AD)$ 上的函数能「编码一个表示」。
- **要点 / 常见误解**：
  - 它是表示，不是函数；「自守形式」是其中被 $K$ 固定的向量，两者不可互换。
  - 尖点（cuspidal）表示对应 $L^2$ 的离散部分；几何 Langlands 里它对应紧支撑的 $D$-模。
  - 未分歧表示 $\leftrightarrow$ 球向量 $\leftrightarrow$ 球 Hecke 代数的特征 $\leftrightarrow$ ${}^LG$ 的半单共轭类（Satake 参数），这是 §9.7 的起点。
  - 整体表示是局部表示的受限张量积 $\bigotimes'_x\pi_x$——这解释了为何几何化后变成「曲线每点粘一份局部数据」。
- **nLab**：<https://ncatlab.org/nlab/show/automorphic+representation>

## Galois 表示（Galois representation）

- **一句话定义**：绝对伽罗瓦群 $\Gal(\bar F/F)$（带 Krull 拓扑）到 $GL_n(\Ql)$ 或 $GL(V)$ 的连续同态。
- **来历**：19 世纪 Galois 理论；Artin 1920–30 年代系统研究伽罗瓦群在向量空间上的作用并定义 Artin L-函数；1950–60 年代随 Grothendieck 的 étale 上同调，$\ell$-adic 表示成为算术几何的中心对象（椭圆曲线的 $H^1_{\text{ét}}$ 给出二维表示即 §1.7 的例子）。
- **在讲义中的位置**：§1.1（`e01a.tex:1`）讨论 $\Gal(\bar\Q/\Q)$；§2.2（`e02.tex:206`）函数域版本；§1.7（`e01b.tex:511`）用 étale 上同调造二维表示；§3.1 把它翻成局部系统。索引 p.28（$\ell$-adic representation）。
- **原文为何未解释**：讲义不解释「连续」指 Krull 拓扑下的连续、为什么系数取 $\Ql$ 而不是 $\C$、以及「未分歧」的确切含义。
- **要点 / 常见误解**：
  - 连续性蕴含像落在某个 $GL_n(\Z_\ell)$ 的有限指数子群中（紧性），故表示「几乎」是整系数的。
  - 未分歧 $\Leftrightarrow$ 惯性群作用平凡 $\Leftrightarrow$ 由 Frobenius 的像（共轭类）决定。
  - 系数取 $\Ql$ 是为与 étale 上同调匹配；$p$-adic 与 $\ell$-adic 的取舍是技术性的，Langlands 对应的陈述与 $\ell$ 无关。
  - 几何侧的同义词就是「$X$ 上的局部系统」（§3.1），这是全文最重要的一次翻译。
- **nLab**：<https://ncatlab.org/nlab/show/Galois+representation>

## Frobenius 元（Frobenius element）

- **一句话定义**：有限域扩张 $\F_q\subset\F_{q^n}$ 的伽罗瓦群由 $x\mapsto x^q$ 生成；整体域在未分歧位 $v$ 的分解群里，这个自同构的提升类记 $\on{Fr}_v$，只作为共轭类有定义。
- **来历**：19 世纪末 Frobenius 在有限群与特征 $p$ 多项式的研究中注意到 $x\mapsto x^p$ 是环同态（「freshman's dream」，nLab 的 Frobenius morphism 条特别强调「只在正特征才成立」）；作为伽罗瓦群生成元是有限域理论的基石，20 世纪由 Artin、Hasse、Chevalley 用于类域论与 L-函数。
- **在讲义中的位置**：§1.3（`e01a.tex:262`）定义分解群、惯性群、未分歧位与 $\on{Fr}_v$；§3.3（`e03a.tex:331` 起）用几何 Frobenius 在茎上的迹把层变成函数；§9.7 用 $\on{Fr}_x$ 的共轭类陈述 Langlands 猜想。索引 p.13。
- **原文为何未解释**：读者缺三件事——素理想如何给出分解群、未分歧即惯性群平凡、不同素元的 Frobenius 互为共轭；也缺「为何取迹就得局部因子」。
- **要点 / 常见误解**：
  - $x\mapsto x^p$ 不是加法同态；正是「特征 $p$ 才成立」这一点使它成为算术几何的基本结构。
  - $\on{Fr}_v$ 依赖 $v$ 的嵌入与素元选取，故只是共轭类——这正是 Langlands 用「共轭类」作参数的根本原因。
  - 几何 Frobenius 作用在 $\ell$-adic 层的茎上，取迹得 $\F_q$-点上的函数，取交错和得 Grothendieck–Lefschetz 迹公式（§3.3）。
- **nLab**：nLab 无 ``frobenius+element`` 条目，重定向至 <https://ncatlab.org/nlab/show/Frobenius+morphism>

## 阿贝尔类域论（abelian class field theory, ACFT）

- **一句话定义**：描述整体域 $F$ 的最大阿贝尔扩张：$\Gal(F^{\mathrm{ab}}/F)\simeq F^\times\backslash\AD_F^\times$（整体—局部互反律）。
- **来历**：源于 Kronecker 与 Weber 的互反律研究（19 世纪下半叶），Hilbert 1897《Zahlbericht》系统化，Artin 1927 证明一般互反律，Chevalley 1930 年代用伊代尔重述，Tate 1950 年处理局部域。nLab 的 class field theory 条：基本（一维）理论源自 Kronecker、Weber，主要结果属 20 世纪上半叶（Hilbert、Artin、Tate、Hasse），且局部域与整体域情形差别很大。
- **在讲义中的位置**：§1.2（`e01a.tex:67`）给出 $\Q$ 的显式形式 $\Gal(\Q^{\mathrm{ab}}/\Q)\simeq\hat\Z^\times$ 与 Kronecker–Weber 定理；§1.4（`e01a.tex:398`）讨论「刚性化」。
- **原文为何未解释**：讲义假设读者见过互反律，但没说明伊代尔类群为何是「正确」的目标群，也没说明局部与整体如何拼接。
- **要点 / 常见误解**：
  - ACFT 就是 Langlands 对应在 $GL_1$ 情形的解；非阿贝尔猜想是它的 $GL_n$ 推广，不是另一套理论。
  - Artin 互反律的实质：Artin L-函数等于 Hecke L-函数。
  - 局部 ACFT（$\Gal(\bar F_v/F_v)^{\mathrm{ab}}\simeq F_v^\times$）与整体版本不是简单取积，中间要过「范数余核」。
  - §1.4 的「rigidification」是给同构加唯一性条件，不是「刚性局部系统」，见本稿 rigid local system 条。
- **nLab**：<https://ncatlab.org/nlab/show/class+field+theory>

## Langlands 对偶群（Langlands dual group, L-group）

- **一句话定义**：由 $G$ 的根数据取对偶（$X^*\leftrightarrow X_*$）所得约化群 $\hat G$，再与 Weil 群（或伽罗瓦群）作半直积得 ${}^LG=\hat G\rtimes W_F$。
- **来历**：Langlands 1967 年致 Weil 的信与 1970 年《Problems in the theory of automorphic forms》引入，原始名称是「L-group」。nLab 特别指出：**Langlands 本人既未引入也未使用「dual group」一词，原始文献只讲 L-group（Gelbart 1984, p.29）**。
- **在讲义中的位置**：§5.2（`e05.tex:105`）Satake 同构把球 Hecke 代数同构到 $R({}^LG)$；§8.6（`e08b.tex:309`）T-对偶与对偶群的出现——自由场实现中 ${}^LG$ 从 T-对偶中浮现；§9 全篇的 Hecke 本征值都取值于 ${}^LG$-局部系统。索引 p.3、58、59、100。
- **原文为何未解释**：讲义直接写 ${}^LG$ 而不给计算法则（$GL_n$ 自对偶、$SL_n\leftrightarrow PGL_n$、$Sp_{2n}\leftrightarrow SO_{2n+1}$），也不解释为什么 T-对偶会给出对偶群。
- **要点 / 常见误解**：
  - 对偶是根数据的对偶，不是 Pontryagin 对偶：$(G^\vee)^\vee=G$ 但对偶不涉及特征标群。
  - 数论情形两侧并不对称：nLab 强调 ${}^LG$ 只是从伽罗瓦表示构造自守 L-函数的部件；Langlands 2014 年致 Sarnak 的信说电—磁对偶／S-对偶与算术的函子性、互反律「quite different」。
  - 几何情形（Kapustin–Witten 2006）S-对偶使 $G\leftrightarrow{}^LG$ 真正对称地出现，这正是 §8.6 与 §6.3 的内容。
  - 记号变体：${}^LG$、$G^\vee$、$\hat G$ 常混用；本讲义用 ${}^LG$ 指含 Weil 群的完整 L-群。
- **nLab**：<https://ncatlab.org/nlab/show/Langlands+dual+group>（nLab 此页为 stub，主要信息在术语备注与 Langlands program 条）

## 局部系统（local system）

- **一句话定义**：局部常值层，即「系数系统」；连通情形等价于基本群到向量空间的表示，特征 0 下又等价于带平坦联络的向量丛（Riemann–Hilbert 对应）。
- **来历**：系数系统的朴素概念在 Leray 正式发表层论之前已在用（nLab 语）；Riemann–Hilbert 对应（Hilbert 1900 年第 21 问题；Kashiwara、Mebkhout 1980 年代证一般情形）把它与线性微分方程严格联系起来；「local system」作为术语随层论与 étale 上同调（Grothendieck 1950–60 年代）普及。
- **在讲义中的位置**：§3.1（`e03a.tex:7`）「Galois representations as local systems」把 $\Gal(\bar F/F)\to GL_n(\Ql)$ 解释为 $X$ 上的 $\Ql$-局部系统；§3.8 的 Hecke 本征值就是 ${}^LG$-局部系统；§9.6 处理任意局部系统。索引 p.33（含 $\ell$-adic、irreducible、ramified、trivial 等子条目）。
- **原文为何未解释**：§3.1 只给一句「局部常值层」，没讲三种图像的等价，也没讲分歧局部系统如何在几何侧定义（$\pi_1(X\bs S)$ 的表示）。
- **要点 / 常见误解**：
  - 三种等价图像（层／基本群表示／平坦联络）是读全文的翻译词典，§3.1、§3.4、§3.8 各用其中一种。
  - 几何 Langlands 的「${}^LG$-局部系统」= ${}^LG$-丛 + 平坦联络，是 $\Bun_G$ 上 Hecke 本征层的本征值。
  - 「trivial local system」「irreducible local system」在 §9 反复出现（索引 p.47），它们决定 Hecke 本征层是否存在、是否唯一。
  - 分歧局部系统需要 $\pi_1(X\bs S)$ 的表示，对应 §9.7–§9.8 的抛物结构。
- **nLab**：<https://ncatlab.org/nlab/show/local+system>

## $G$-丛模叠（moduli stack of $G$-bundles, $\Bun_G$）

- **一句话定义**：光滑射影曲线 $X$ 上 $G$-主丛的同构类的模叠；$G=GL_n$ 时即秩 $n$ 向量丛模叠 $\Bun_n$。
- **来历**：Grothendieck 在 FGA（1957–62）中用 Quot 格式构造模空间，GIT（Mumford 1965）与 Narasimhan–Seshadri（1965，稳定丛对应酉表示）给出稳定丛模空间；把 $\Bun_G$ 当作叠而不是粗模空间，是 1980–90 年代几何 Langlands 的需要（nLab 的 moduli space of bundles 条按此线索叙述）。
- **在讲义中的位置**：§3.2（`e03a.tex:168`）用 Weil 一致化把 $\Bun_n(\C)$ 等同于 $GL_n(F)\backslash GL_n(\AD)/GL_n(\OO)$；§6、§7.3（`e07a.tex:311`）把 Hecke 本征层与共形块放到 $\Bun_G$ 上；索引 p.64、39。
- **原文为何未解释**：读者缺「为何必须用叠（自同构群非平凡）」「$\Bun_G$ 的连通分支由 $\pi_1(G)$ 决定」「稳定性只在 $GL_n$ 等情形需要」这几点。
- **要点 / 常见误解**：
  - $\Bun_G$ 是 Artin 叠，不是概形；它的「点」带自同构，这正是 Hecke 函子能良好定义的原因。
  - 对 $\C$ 上曲线，Weil 一致化 $\Bun_n(\C)=GL_n(F)\backslash GL_n(\AD)/GL_n(\OO)$ 把「每点局部数据 + 整体粘合」写成双陪集——§3.2 的全部要点。
  - 在 $(\E)$ 处 $\Bun_G$ 的切空间是 $H^1(X,\g_\E)$，故 $T^*\Bun_G$ 正是 Higgs 丛模空间——这是 §9.5 讨论 Hitchin 系统的前提。
  - 几何 Langlands 的一侧是 $D^b(\Bun_G\text{-mod})$，另一侧是 $\Loc_{{}^LG}$ 上的拟凝聚层。
- **nLab**：<https://ncatlab.org/nlab/show/moduli+space+of+bundles>

## Hecke 算符与 Hecke 对应（Hecke operator / Hecke correspondence）

- **一句话定义**：Hecke 算符是双陪集 $K\backslash G(\AD)/K$ 中元素在自守形式上的卷积作用（经典 $T_p$，特征值 $a_p$）；Hecke 对应是它的代数几何版：$\Bun_G$ 上「在一点 $x$ 修改丛」的对应 $\H_x\subset\Bun_G\times\Bun_G$，并投影到 $X$。
- **来历**：Hecke 1936–37 年研究模形式的 Dirichlet 级数时引入 $T_p$；双陪集代数（Hecke 代数）由 Gelfand 学派 1950–60 年代抽象化，Satake 1963 给出球情形的结构定理；几何对应形式在 Drinfeld、Laumon、Beilinson–Drinfeld 的工作中成型（nLab 的 Hecke algebra 条按「卷积代数／双陪集」叙述，并指出 $p$ 进情形它充当李代数的替代品）。
- **在讲义中的位置**：§1.6（`e01b.tex:176` 起）经典 Hecke 算符与 $a_p$；§3.7（`e03b.tex:174`）「Hecke correspondences」把 $T_p$ 变成 $\Bun_G$ 上的对应与 Hecke 函子；§5.1–5.2 球 Hecke 代数；索引 p.22、31、44、45。
- **原文为何未解释**：§3.7 中「拉回—张量—推前」的操作出现得很快，读者不知道它就是把「$T_p f$ 的有限和」翻译成「在 $x$ 处换一个丛」。
- **要点 / 常见误解**：
  - 经典 $T_p$ 是 Hecke 对应的函数层面影子；对应层面是「除一点外同构的两个丛」构成的叠。
  - Hecke 函子 $H_x$ 把 $\Bun_G$ 上的 $D$-模送到 $\Bun_G\times X$（或按表示 $V$ 取 $\Bun_G$）上；Hecke 本征层就是它的本征对象。
  - $x$ 附近的局部模型是仿射 Grassmannian $\Gr=G((t))/G[[t]]$ 的轨道，这条线索把 §3.7 与 §5.4–5.6 连起来。
- **nLab**：<https://ncatlab.org/nlab/show/Hecke+algebra>（nLab 无独立的 Hecke operator 条目）

## Hecke 本征层（Hecke eigensheaf）

- **一句话定义**：$\Bun_G$ 上的 $D$-模（或反常层）$\F$，使每个 Hecke 函子 $H_x^V$ 作用后，$\F$ 只被乘上由某个 ${}^LG$-局部系统 $E$（经表示 $V$）决定的有限维向量空间，即「被送到自身的张量倍」。
- **来历**：Beilinson–Drinfeld 1990 年代几何 Langlands 的核心对象；nLab 的定义是「在 Hecke 对应诱导的积分变换下被送到自身的张量倍的对象」，并直接引 Frenkel 2005 讲义 §3.8。
- **在讲义中的位置**：§3.8（`e03b.tex:321`）猜想表述；§6.1（`e06.tex:10`）$\C$ 上版本；§9.4（`e09b.tex:1`）Hecke property；§9.6、§9.8 构造更一般的本征层。索引 p.4、45、46、49、64、65、100、105、112、116、118（全文最核心的概念之一）。
- **原文为何未解释**：§3.8 直接给定义，但没解释「为何本征值是局部系统而非标量」「为何要求对每个表示 $V$ 都给同构」，读者会觉得条件过强。
- **要点 / 常见误解**：
  - 本征值是 $X$ 上的 ${}^LG$-局部系统，不是 $\C$ 数——这是「$\Bun_G$ 上的对象对应 $X$ 上的局部数据」的唯一合理解释。
  - Hecke 本征层是几何 Langlands 猜想的具体载体：猜想说每个 ${}^LG$-局部系统都应有对应的本征层。
  - nLab 记录了 Kapustin–Witten 2006 的对照表：几何 Langlands $\leftrightarrow$ $N=4$ SYM 的 S-对偶，Hecke 本征层 $\leftrightarrow$ 磁本征膜（'t Hooft 算符的本征膜），局部系统 $\leftrightarrow$ 电本征膜。
- **nLab**：<https://ncatlab.org/nlab/show/Hecke+eigensheaf>

## 反常层（perverse sheaf）

- **一句话定义**：可构造层的有界导出范畴中由支撑／余支撑（perversity）条件截出的 abelian 子范畴，推广相交上同调。
- **来历**：Goresky–MacPherson 1970 年代做相交同调时为度量奇点的「坏程度」引入 perversity 参数（nLab 记为 1974–75 起）；Beilinson–Bernstein–Deligne 1982 年《Faisceaux pervers》（Astérisque 100）系统化。名字是 Deligne 起的，nLab 记 Grothendieck 在《Récoltes et semailles》里抱怨它「既非 perverse 也非 sheaf」。
- **在讲义中的位置**：§3.3 末（`e03a.tex:365` 起）先论证「导出范畴太大，需要一个自然的 abelian 子范畴使 Grothendieck 群单射」，§3.4（`e03a.tex:472`）「From perverse sheaves to $D$-modules」正式引入；索引 p.38。
- **原文为何未解释**：讲义只说「需要 abelian 子范畴」，不给 perversity 的支撑条件，读者无法自己验证某个层是否为反常层，也不知它与相交上同调的关系。
- **要点 / 常见误解**：
  - 它不是层，是复形范畴的对象；「perverse」没有任何道德含义（nLab 专门吐槽这个命名）。
  - 光滑簇上反常层就是（平移过的）局部系统；奇点处才显出与普通层的差别。
  - $\C$ 上正则全纯 $D$-模与反常层等价（Riemann–Hilbert，Kashiwara），故 §3.8 可以互换使用「$D$-模」与「反常层」。
  - Hecke 函子在反常层上的版本是几何 Satake 与 Hecke 本征层构造的常用语言。
- **nLab**：<https://ncatlab.org/nlab/show/perverse+sheaf>

## $D$-模（D-module）

- **一句话定义**：$X$ 上微分算子层 $D_X$ 的拟凝聚模；特征 0 下等价于带平坦（可积）联络的 $\OO_X$-模。
- **来历**：佐藤幹夫（Mikio Sato）1950 年代末–60 年代初研究超函数时引入（nLab 明言 "introduced by Mikio Sato"）；Bernstein 1971 建立六函子形式；Beilinson–Bernstein 1980 年代的局部化把 $D$-模与表示论联系起来。
- **在讲义中的位置**：§3.4–§3.6（`e03a.tex:472`、`e03b.tex:1`、101；§3.5 是线上的显式例子）；§6.4「$\D$-modules are D-branes?」；§7.4（`e07b.tex:1`）构造扭曲 $D$-模；索引 p.34、35。
- **原文为何未解释**：讲义假定读者知道 $D_X$ 的阶滤过、好滤过与特征簇，也不解释为什么几何 Langlands 用 $D$-模而非层。
- **要点 / 常见误解**：
  - 「$D$-模 = 平坦联络」只在特征 0 成立；正特征下 $D_X$ 非 Noether，还出现 $p$-曲率现象。
  - 几何 Langlands 选 $D$-模，是因为 Hecke 函子在其上定义良好，且与共形块（§7）天然衔接。
  - $\Bun_G$ 上的 $D$-模与反常层通过 Riemann–Hilbert 对应互换，两种语言在 §3.8 之后交替使用。
  - 临界水平的共形块给出 $\Bun_G$ 上的 $D$-模，这是 §7–§9 的主线（索引 p.85、86 的 critical level）。
  - 常见例子：$\OO_X$ 本身（平凡联络）、$\Omega_X$ 的分数幂（§8.3 的 oper 就作用在 $\Omega^{-(n-1)/2}$ 上）、以及线性微分方程的解给出的局部系统。
- **nLab**：<https://ncatlab.org/nlab/show/D-module>

## Fourier–Mukai 变换（Fourier–Mukai transform）

- **一句话定义**：以 $\K\in D(X\times Y)$ 为核的函子 $D(X)\to D(Y)$，$\F\mapsto Rq_*(p^*\F\otimes\K)$——积分变换的范畴化。
- **来历**：Mukai 1981 年对偶 abelian 簇 $X,\hat X$ 与 Poincaré 线丛的情形（nLab：原始 FM 变换正是此特例）；Laumon 1980 年代推广为「generalized Fourier transform」用于函数域 Langlands；几何 Langlands 的阿贝尔情形（Laumon 1985／1996、Rothstein 1996）正是用它证明的。
- **在讲义中的位置**：§4.4–4.5（`e04.tex:225`、395）几何 ACFT 的证明（Laumon–Rothstein 定理）；§6.2（`e06.tex:186`）「非阿贝尔版本？」——沿 Hitchin 纤维化做 FM；索引 p.54、66、100、113。
- **原文为何未解释**：讲义没讲「为何核取 Poincaré 线丛就把 $\Bun$ 上的对象送到对偶侧」，也没讲迹映射与相对 Poincaré 丛的几何来源。
- **要点 / 常见误解**：
  - 与经典 Fourier 变换的词典：函数 $\leftrightarrow$ 层、积分 $\leftrightarrow$ 推前、乘法 $\leftrightarrow$ 张量核、平移 $\leftrightarrow$ 挠。
  - 对 abelian 簇它是范畴等价（Fourier–Mukai 对偶），这正是 $GL_1$ 情形几何 Langlands 的证明。
  - 非阿贝尔情形没有现成的 FM 变换，§6.2 的 Hitchin 纤维化类比只是启发，不是证明（讲义明确把「非阿贝尔 FM」列为猜想性设想）。
  - 技术上它把「挠（twist）」与「张量积」互换，这正是与经典 Fourier 变换「平移 $\leftrightarrow$ 乘法」对应的地方。
- **nLab**：<https://ncatlab.org/nlab/show/Fourier-Mukai+transform>

## 几何 Langlands 对应（geometric Langlands correspondence）

- **一句话定义**：猜想：$\Bun_G$ 上 $D$-模的导出范畴与 ${}^LG$-局部系统模叠上拟凝聚层的导出范畴等价（Arinkin–Gaitsgory 2012 用幂零 ind-对象与稳定 $(\infty,1)$-范畴精化）。
- **来历**：函数域类比下由 Beilinson–Drinfeld 1990 年代提出；nLab 原文：「原始版本的猜想（going back to Beilinson–Drinfeld 9x，reviewed for instance in Frenkel 05）断言……两边的导出范畴等价」；阿贝尔情形由 Laumon（1985、1996）与 Rothstein（1996）用 Fourier–Mukai 证明；原版一般不成立，Arinkin–Gaitsgory 2012 给出修正。
- **在讲义中的位置**：§3.8（`e03b.tex:321`）表述；§6.1（`e06.tex:10`）$\C$ 上版本；§9 用共形块构造 opers 对应的本征层，§9.6 推广到任意局部系统。索引 p.4、46、65、114、116。
- **原文为何未解释**：讲义按「逐点构造 Hecke 函子」讲，没有完整写出范畴等价形式，读者难以看出「为什么是 ${}^LG$ 而不是 $G$」。
- **要点 / 常见误解**：
  - 「几何化」的四步翻译：函数 $\to$ 层、Hecke 算符 $\to$ Hecke 函子、本征函数 $\to$ 本征层、伽罗瓦表示 $\to$ 局部系统。
  - $G\leftrightarrow{}^LG$ 的互换只在几何情形（S-对偶）对称出现；数论情形并非如此（nLab 引 Langlands 2014 致 Sarnak 的信）。
  - 现状：$GL_1$／环面已证；一般 $G$ 仍是猜想；本讲义 §9 的构造只覆盖 opers（$\Loc$ 的半维子空间），§9.6 才推广到任意局部系统。
  - 常见误解：把「几何 Langlands」当成「数论 Langlands 的几何证明」——它是另一个猜想，只是在函数域类比下对应。
- **nLab**：<https://ncatlab.org/nlab/show/geometric+Langlands+correspondence>

## 仿射 Grassmannian（affine Grassmannian）

- **一句话定义**：$\Gr_G=G((t))/G[[t]]$，loop group 的旗簇，是 ind-概形；其 $R$-点参数化 $R((t))^n$ 中的格。
- **来历**：作为 loop group 的齐性空间在 1980 年代 Kac–Moody 表示论中出现；1990 年代 Beilinson–Drinfeld 把它作为几何 Satake 与 Hecke 对应的几何载体。nLab 主要引 Zhu 2016 的讲义（arXiv:1603.05593）作定义来源。
- **在讲义中的位置**：§5.4–5.5（`e05.tex:308`、451，球 Hecke 代数的范畴化与 $PGL_2$ 例子）；§7 中用「一点版本」$G(\ppart)/G[[t]]$（`e07a.tex:412`）；索引 p.61、62、82、109。
- **原文为何未解释**：§5.5 直接用 $\Gr$ 的 $G[[t]]$-轨道分解（轨道由支配余权标号），但没说明为何轨道有限、为何轨道闭包给出偏序。
- **要点 / 常见误解**：
  - 它是 ind-scheme 而非概形；「无穷维」带来技术麻烦（需要 ind-构造与反常层）。
  - 轨道 $\Gr^{\check\lambda}=G[[t]]\cdot t^{\check\lambda}$ 由支配余权 $\check\lambda\in X_*(T)^+$ 标号，$\Gr^{\check\lambda}\simeq G[[t]]/G[[t]]_{\check\lambda}$。
  - $G[[t]]$-等变反常层范畴 $\simeq\Rep({}^LG)$ 就是几何 Satake 等价（§5.6）。
  - 直观：$\Gr$ 是「$G$-丛在一点处的局部行为」的模空间，Hecke 对应的纤维就是它。
  - $GL_n$ 情形最具体：$\Gr_{GL_n}$ 的点就是 $\C((t))^n$ 中的 $\C[[t]]$-格，Zhu 2016 的定义正是从「格的 $R$-族」出发。
  - 它不是有限型的：$\Gr=\bigcup_{\check\lambda}\Gr^{\check\lambda}$，每个轨道闭包 $\ol{\Gr}^{\check\lambda}$ 才是有限型的射影簇（$GL_n$ 时是部分旗簇）。
- **nLab**：<https://ncatlab.org/nlab/show/affine+Grassmannian>

## 球 Hecke 代数（spherical Hecke algebra）

- **一句话定义**：$\mathcal H(G,K)=C_c^\infty(K\backslash G(F)/K)$（$K=G(\OO)$）在卷积下的代数；对 $p$ 进群充当李代数的替代品。
- **来历**：Gelfand 学派 1950–60 年代研究 $p$ 进群表示时引入双陪集代数；Satake 1963 年证明它交换并与 ${}^LG$ 的表示环同构。nLab 在 geometric Satake equivalence 条开头即以此定义，并提到交换性来自「Gelfand trick」。
- **在讲义中的位置**：§5.1（`e05.tex:9`）「spherical Hecke algebra for arbitrary reductive group」；§5.2（`e05.tex:105`）Satake 同构；§9.7（`e09d.tex:16` 起）用其交换性说明未分歧表示有唯一的球向量。索引 p.22、30。
- **原文为何未解释**：读者缺「为什么卷积代数会交换」（Gelfand trick：双不变函数在换位下不变）与「为什么它对应 ${}^LG$ 的表示环」这两步。
- **要点 / 常见误解**：
  - 一般卷积代数非交换；球 Hecke 代数交换是定理而非定义的一部分。
  - Satake 同构 $\mathcal H\otimes\Z[q^{\pm1/2}]\simeq R({}^LG)\otimes\Z[q^{\pm1/2}]$ 把「球函数」翻译成「对偶群表示的特征标」。
  - 未分歧表示 $\leftrightarrow$ $\mathcal H$ 的特征 $\leftrightarrow$ ${}^LG$ 的半单共轭类（Satake 参数），这是 §9.7 局部对应的基础。
  - 几何版本把 $\mathcal H$ 换成 $\Gr$ 上的等变反常层范畴（§5.4 的「范畴化」）。
- **nLab**：nLab 无 ``spherical+Hecke+algebra`` 独立条目，相关定义见 <https://ncatlab.org/nlab/show/geometric+Satake+equivalence> 与 <https://ncatlab.org/nlab/show/Hecke+algebra>

## 几何 Satake 等价（geometric Satake equivalence）

- **一句话定义**：$\Gr_G$ 上 $G[[t]]$-等变反常层的范畴与 $\Rep({}^LG)$ 的范畴作为对称 monoidal 范畴等价。
- **来历**：猜想由 Beilinson–Drinfeld 与 Lusztig 在 1990 年代提出，Mirković–Vilonen 2007 年证明（Ginzburg 1995 年的 loop group 反常层工作亦有贡献）；它是球 Hecke 代数 Satake 同构的范畴化（nLab 的 geometric Satake equivalence 条）。
- **在讲义中的位置**：§5.4（`e05.tex:308`）「Categorification of the spherical Hecke algebra」、§5.6（`e05.tex:505`）「The geometric Satake equivalence」；索引 p.63。
- **原文为何未解释**：讲义只给陈述与「用卷积范畴」的提示，不讲 Mirković–Vilonen 的循环族论证，读者看不出这是把 Satake 同构「升维」而非新猜想。
- **要点 / 常见误解**：
  - 「范畴化」= 把交换代数同构提升为 monoidal 范畴等价；卷积 $\leftrightarrow$ $\Rep({}^LG)$ 的张量积。
  - $GL_n$ 情形把 $\Gr$ 的轨道与 $GL_n$ 的表示对上（Schur–Weyl 型），是理解一般情形的最好入口。
  - 它既解释 §5 的球 Hecke 代数，也为 §7–§9 用共形块构造 Hecke 本征层提供表示论输入。
  - 常见误解：以为它是「几何版本的 Satake 同构」而已——它额外给出范畴层面的等价，因而能作用于层与 $D$-模。
  - monoidal 单位是 $\Gr$ 的 IC 层（对应平凡表示）；验证单位与结合性恰好是证明中最费工的部分。
- **nLab**：<https://ncatlab.org/nlab/show/geometric+Satake+equivalence>

## opers

- **一句话定义**：曲线 $X$ 上 ${}^LG$-丛带平坦联络与一个 Borel 约化，使联络在 Borel 商中的像落入特定的「负一阶」分布；$SL_2$ 情形即射影联络 $\partial_t^2-v(t)$。
- **来历**：Drinfeld–Sokolov 1981 年为构造一般单李代数的 $n$-KdV 型方程引入矩阵微分算子的标准形；Beilinson–Drinfeld 1990 年代把它抽象为「曲线上的 oper」（讲义 §8.3 归功 Drinfeld–Sokolov，见 `e08a.tex:354`）。nLab 无独立条目。
- **在讲义中的位置**：§8.3（`e08a.tex:333`）定义（$SL_n$ 情形、规范变换、一般 $\g$）；§9.1–9.2 用 opers 参数化中心特征并构造 $D$-模；§9.6（`e09c.tex:1`）推广为「带奇点的 opers」以覆盖任意局部系统。索引 p.6、56、68、90，另有 oper bundle p.93。
- **原文为何未解释**：讲义用「规范等价类」定义 oper，但没解释为何 $SL_n$-oper 恰是 $n$ 阶微分算子、为何 $\on{Op}_G(X)$ 是仿射空间。
- **要点 / 常见误解**：
  - oper 不是「算子」的泛称，而是带 Borel 约化的特定联络；$SL_n$ 情形与 $n$ 阶微分算子一一对应。
  - $\on{Op}_{{}^LG}(X)$ 对光滑射影曲线是仿射空间；$\on{Op}_{{}^LG}(D)$ 与中心 $\zz(\ghat)$ 的谱同构（Feigin–Frenkel、Beilinson–Drinfeld），这是 §8.3–§9.1 的关键定理。
  - opers 只占全部 ${}^LG$-局部系统的半维子空间（`e09c.tex:7` 明说），故 §9 的构造只解决了一半的几何 Langlands。
  - §9.6 的「带奇点 opers」$\on{Op}_{{}^L\g}(D_x)_{\cla}$ 由 Beilinson–Drinfeld 引入（讲义引 \cite{F:flag} Sect. 2.3、\cite{FG}）。
- **nLab**：nLab 无 ``oper`` 条目，相关讨论见 <https://ncatlab.org/nlab/show/geometric+Langlands+correspondence>

## Hitchin 纤维化（Hitchin fibration）

- **一句话定义**：$T^*\Bun_G$（Higgs 丛模空间）到 Hitchin 空间 $H_G=\bigoplus_i H^0(X,\Omega_X^{\otimes d_i})$ 的映射 $p:(\E,\varphi)\mapsto$（$\varphi$ 的特征多项式系数），是完全可积系统。
- **来历**：Hitchin 1987 年在自对偶方程与谱曲线观点下定义（nLab 称「the landmark Hitchin 87」）；Beilinson–Drinfeld 揭示它在几何 Langlands 中的地位；Ngô Bảo Châu（与 Laumon 合作）用 Hitchin 纤维化证明 Fundamental Lemma，获 2010 年 Fields 奖。
- **在讲义中的位置**：§9.5（`e09b.tex:226`）「Quantization of the Hitchin system」：$p:T^*\Bun_G\to H_G$、Hitchin 空间、全局幂零锥；§6.2、§6.4（`e06.tex:511` 起）用 Hitchin 纤维化讲非阿贝尔 Fourier–Mukai 与 D-膜。索引 p.71、111。
- **原文为何未解释**：讲义假定读者知道 $T^*\Bun_G$ 即 Higgs 丛模空间、$p$ 的一般纤维是 Prym 簇，直接进入量子化。
- **要点 / 常见误解**：
  - Hitchin 映射给出完全可积系统：$H_G$ 上的函数给出 $T^*\Bun_G$ 上对易的哈密顿量。
  - 一般纤维是 Prym 簇（对 $GL_n$）或仿射 Jacobi 型；奇异纤维与全局幂零锥（`e09b.tex:370`）是其重要结构。
  - §9.5 的量子化（$H_G$ 上的函数 $\to$ $\Bun_G$ 上的对易算符）是 §9 构造 Hecke 本征层的技术核心。
  - Ngô 的证明（2010）在 $\C$ 上用 Hitchin 纤维化的支撑理论，是「几何 Langlands 工具反向解决数论问题」的著名例子。
  - $H_G$ 的线性坐标恰是 $\varphi$ 的特征多项式系数（$GL_n$ 时为 $\tr\wedge^k\varphi$，$k=1,\dots,n$），故 Hitchin 映射就是「取特征值」。
- **nLab**：<https://ncatlab.org/nlab/show/Hitchin+fibration>

## 谱曲线与 cameral cover（spectral curve / cameral cover）

- **一句话定义**：谱曲线是 Lax 矩阵特征多项式 $\det(\varphi-t)=0$ 在 $T^*X$ 中的零点轨迹（$X$ 的 $n$ 重覆盖）；cameral cover 是对一般 $G$ 用 Cartan 商 $\mathfrak t/W$ 代替特征值所得的 $W$-伽罗瓦覆盖。
- **来历**：谱曲线来自经典可积系统的 Lax pair 方法（19 世纪–1970 年代），Hitchin 1987 给出几何解释（nLab 的 spectral curve 条）；cameral cover 由 Donagi 1990 年代引入（《Spectral covers》1995，年份待核），用于一般 $G$ 的 Hitchin 系统与 Ngô 的证明。
- **在讲义中的位置**：§6.2（`e06.tex:511–524`）——讲义唯一出现「spectral curves」之处：非阿贝尔 Fourier–Mukai 沿 Hitchin 纤维化进行，纤维是「谱曲线的广义 Prym 簇」，并提到对偶 Hitchin 纤维化；**cameral cover 在讲义全文中不出现、索引中也没有**（译者可加注补充）。
- **原文为何未解释**：读者缺「谱曲线 = 特征值曲线」这一直观，也不清楚「沿 Hitchin 纤维做 Fourier–Mukai」是阿贝尔情形 FM 变换的高维类比。
- **要点 / 常见误解**：
  - $SL_n$／$GL_n$：$\det(\varphi-t)=0$ 定义 $n$ 重覆盖 $\tilde X\to X$，$\varphi$ 的系数给出 $H_G$ 的坐标。
  - $Sp(m,\C)$ 的谱曲线是超椭圆曲线（nLab 特别指出）；其他群要用 cameral cover，其伽罗瓦群是 Weyl 群 $W$。
  - cameral cover 比谱曲线更细：谱曲线是 cameral cover 在 $W$ 作用下的某个商／关联覆盖。
  - 常见误解：把 cameral cover 当成「另一种谱曲线」——对 $GL_n$ 二者一致，对一般 $G$ 不同。
- **nLab**：<https://ncatlab.org/nlab/show/spectral+curve>（cameral cover 无独立条目）

## 分歧与抛物结构（ramification / parabolic structure）

- **一句话定义**：分歧：覆盖在分支点处叶片合并，伽罗瓦侧即惯性群非平凡；抛物结构：曲线带标记点、每点给一个旗（抛物丛），是分歧在 $\Bun_G$ 侧的对应物。
- **来历**：分歧是 Riemann 面理论的基本概念（19 世纪）；抛物丛由 Mehta–Seshadri 1980 年引入（年份待核）；几何 Langlands 的分歧版本由 Beilinson–Drinfeld 与 Frenkel 发展，讲义 §9.7 明确「following the ideas of \cite{FG}」。
- **在讲义中的位置**：§9.7（`e09d.tex:1`）从局部 Langlands 对应、Iwahori 子群、仿射 Hecke 代数讲到抛物结构；§9.8（`e09d.tex:221`）分歧局部系统的 Hecke 本征层。索引 p.117（admissible、local Langlands）、p.118（parabolic structure）。
- **原文为何未解释**：讲义默认读者懂「Iwahori 子群 = Borel 在 $G(\OO)$ 中的原像」「驯分歧 $\leftrightarrow$ Iwahori 不变向量非零」，从分歧直接跳到仿射 Hecke 代数。
- **要点 / 常见误解**：
  - 未分歧 $\leftrightarrow$ $G(\OO)$-不变向量非零；驯分歧（tame）$\leftrightarrow$ Iwahori 不变向量非零；野分歧需要更深结构。
  - 抛物 $\Bun_G$（带标记点与旗）上的 Hecke 本征层对应分歧局部系统，构造比未分歧情形复杂，需要扭曲 $D$-模（§7.4）。
  - 常见误解：以为分歧只是「技术性的坏点」；在几何 Langlands 中它恰恰是局部对应最丰富的地方。
- **nLab**：<https://ncatlab.org/nlab/show/ramification>

## 刚性局部系统（rigid local system）

- **一句话定义**：Katz 意义下：$\P^1\bs S$ 上的局部系统，其单值表示在固定各局部单值共轭类的变形空间中是孤立的（无连续变形），即「刚性」。
- **来历**：Katz 1990 年代研究 $\ell$-adic 局部系统的刚性（《Rigid Local Systems》，Annals of Mathematics Studies 139，1996），动机是分类超几何型局部系统与超几何函数。
- **在讲义中的位置**：**讲义未使用这一术语，索引中也没有**。最接近的是 §1.4「Rigidifying ACFT」（`e01a.tex:398`）的「刚性」：那是给 ACFT 同构添加唯一性条件（在伽罗瓦群中固定一个子集后同构唯一），可视为囊括所有互反律（`_orig_text.txt:871–873`），与 Katz 的刚性局部系统不是同一概念。建议译者在此加注区分。
- **原文为何未解释**：术语本身不在讲义中；读者若从别处见到「rigid local system」，容易误以为与 §1.4 的 rigidity 相关。
- **要点 / 常见误解**：
  - §1.4 的 rigidity 是「互反律的精确化条件」，与单值表示的变形刚性无关。
  - Katz 刚性对几何 Langlands 有意义（刚性局部系统常可用 opers 或超几何函数显式构造），但 Frenkel 讲义未展开。
  - 两处「rigid」切勿混为一谈：一处修饰「同构／条件」，一处修饰「局部系统」。
- **nLab**：nLab 无 ``rigid+local+system`` 条目（已实测 404），相关背景见 <https://ncatlab.org/nlab/show/local+system>

## Weil 猜想（Weil conjectures）

- **一句话定义**：有限域 $\F_q$ 上代数簇 $X$ 的有理点数猜想组：Weil zeta 函数是有理函数、满足函数方程，且零点／极点的绝对值满足「黎曼假设」。
- **来历**：Weil 1949 年（Bull. AMS《Numbers of solutions of equations in finite fields》）提出；Dwork 1960 年证有理性；Grothendieck 1960 年代建 étale 上同调使除黎曼假设外各条形式化；Deligne 1974 年（Publ. IHES 43）证明黎曼假设。
- **在讲义中的位置**：讲义正文未展开，仅参考文献 [46]（Freitag–Kiehl《Etale Cohomology and the Weil conjecture》）出现（`_orig_text.txt:7314`）；其方法体现在 §3.3（`e03a.tex:289` 起）的 Grothendieck fonctions-faisceaux 字典与 Grothendieck–Lefschetz 迹公式。
- **原文为何未解释**：读者不知道几何 Langlands 用层的最终动机来自 Weil 猜想：上同调把点数计数变成 Frobenius 在层上同调上的迹，而「好」的层范畴（反常层）正是为了让「层 $\mapsto$ 函数」单射。
- **要点 / 常见误解**：
  - 四条：有理性、函数方程、黎曼假设、Betti 数的解释；nLab 指出除 RH 外都可从「合适的上同调理论」形式推出。
  - $X$ 的 zeta 函数可写成 $\prod_i\det(1-\on{Fr}\,t\,|\,H^i)^{-1}$，这正是 Frobenius 特征值（$a_p$）成为 Langlands 核心数据的原因。
  - 常见误解：以为 Weil 猜想只关乎点数——它实际奠定了「用上同调研究算术」的范式（Grothendieck 的动机）。
- **nLab**：<https://ncatlab.org/nlab/show/Weil+conjecture>

## Shimura–Taniyama–Weil 猜想（模性定理）

- **一句话定义**：$\Q$ 上每条椭圆曲线 $E$（导子 $N_E$）都来自一个尖点形式 $f\in S_2(\Gamma_0(N_E))$，且 $a_p(f)=a_p(E)$ 对所有素数 $p$ 成立。
- **来历**：谷山丰 1955 年提出，志村五郎与 Weil 在 1950–60 年代精确化（Weil 1967）；半稳定情形由 Wiles 1995（与 Taylor 1995）证明，全定理由 Breuil–Conrad–Diamond–Taylor 2001 证明。nLab 的 modularity theorem 条即 Taniyama–Shimura 的重定向目标。
- **在讲义中的位置**：§1.7（`e01b.tex:511`）「Elliptic curves and Galois representations」：用 $H^1_{\text{ét}}(E_{\bar\Q},\Ql)$ 的二维表示与模形式匹配；引言 `e00.tex:263`、435；索引 p.18、24。
- **原文为何未解释**：讲义只把它当「Langlands 对应的已证特例」，没讲它在 $GL_2$ 情形等价于「二维奇伽罗瓦表示都是模的」，也没展开与 Fermat 大定理的关系。
- **要点 / 常见误解**：
  - 它是 Langlands 对应在 $n=2$、$F=\Q$、$G=GL_2$ 的特例；$a_p$ 匹配即 Frobenius 特征值匹配。
  - Wiles 的半稳定情形已足以推出 Fermat 大定理，这是它最著名的应用。
  - 常见误解：以为它只关于「椭圆曲线与模形式」——本质是「二维伽罗瓦表示的自守性」，可推广到更多域（实二次域等，Freitas–Le Hung–Siksek）。
  - 水平 $N_E$ 由 $E$ 的导子决定，它同时编码坏约化的素数及其类型——这是「对几乎所有 $p$ 匹配」之所以能精确化的地方。
- **nLab**：<https://ncatlab.org/nlab/show/modularity+theorem>

## Drinfeld–Laumon 与 Lafforgue 的函子性

- **一句话定义**：函数域上 Langlands 对应的证明路线：Drinfeld 1980 年代对 $GL_2$ 用 shtuka 证明；Laumon 1987 用推广的 Fourier 变换处理一般 $GL_n$ 的表述；Lafforgue 2002 对任意 $GL_n$ 完成证明。
- **来历**：Drinfeld 1970–80 年代（$GL_2$，1983 年论文）；Laumon 1987（Duke，《Correspondance de Langlands géométrique pour les corps de fonctions》，年份待核）；Lafforgue 2002（Invent. Math.，《Chtoucas de Drinfeld et correspondance de Langlands》），同年获 Fields 奖。nLab 无独立条目。
- **在讲义中的位置**：§2.4（`e02.tex:532`）函数域上的 Langlands 对应；§3.8（`e03b.tex:384`）明确「$GL_n$ 情形的表述归功于 Drinfeld 和 Laumon \cite{Laumon:cor1}」；§4 引 Laumon 三篇；§2.1（`e02.tex:17`）提到 Drinfeld 证 $GL_2$、Lafforgue 证一般 $GL_n$。
- **原文为何未解释**：讲义只用一句话归功，没解释 shtuka 是什么、Laumon 变换如何化归、Lafforgue 的贡献为何是「函子性」而非对应本身。
- **要点 / 常见误解**：
  - 函数域是几何 Langlands 的试验场：曲线上的向量丛＋Frobenius 结构使「几何方法」可用。
  - Drinfeld 的 shtuka（F-层）是带 Frobenius 结构的向量丛，可看作函数域的「椭圆曲线」推广；Laumon 的 Fourier 变换是几何 Langlands 中 FM 变换的先声。
  - Lafforgue 证明的是 $GL_n$ 的 Langlands 对应（含函子性），不是一般约化群。
  - 常见误解：把 Drinfeld–Laumon 当作「一个定理」——它是「Drinfeld 的 $GL_2$ + Laumon 的化归 + Lafforgue 的 $GL_n$」三段历史。
- **nLab**：nLab 无 ``Drinfeld-Laumon`` 条目（已实测 404），相关背景见 <https://ncatlab.org/nlab/show/Langlands+program>
