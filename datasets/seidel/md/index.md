# Seidel 资料卡索引

共 70 张：概念 32　推导 8　勘误 30

| id | 标题 | track | 一句话 |
|---|---|---|---|
| [`seidel/concept/a-infinity-algebra`](concepts/a-infinity-algebra.md) | A∞ 代数 | A | 带一串多重线性运算 μ^d 的分次向量空间：μ¹ 是微分，μ² 是同伦意义下的乘法，高阶 μ^d 修正结合律的失效。 |
| [`seidel/concept/a-infinity-category`](concepts/a-infinity-category.md) | A∞ 范畴 | A | 对象之间的 hom 是分次向量空间，复合是一族满足 A∞ 关系的多重线性映射；定义不要求恒等态射，含幺性是可后加的结构。 |
| [`seidel/concept/directed-a-infinity-category`](concepts/directed-a-infinity-category.md) | 有向 A∞ 范畴 | A | 对象带偏序、反向 hom 全为零的严格含幺 $A_\infty$ 范畴；高阶运算被偏序切成有限块，故必拟同构于 hom 有限维的 dg 范畴。 |
| [`seidel/concept/exact-triangle`](concepts/exact-triangle.md) | 殊三角（正合三角） | A | 三角范畴里代替正合列的结构：X→Y→Z→TX，满足 TR1–TR4；在 Tw A 中由映射锥给出。 |
| [`seidel/concept/exceptional-object`](concepts/exceptional-object.md) | 例外对象与例外集 | A | 自同态只有单位元、其余 $\hom(E,E[i])$ 全为零的对象；一列这样的对象若彼此只有单向态射，就构成例外集。 |
| [`seidel/concept/homological-perturbation-lemma`](concepts/homological-perturbation-lemma.md) | 同调扰动引理 | A | 给定形变收缩与一个扰动，用显式级数把微分、链映射与同伦一起搬到小复形上；A∞ 版本即原书命题 1.12 的递归转移。 |
| [`seidel/concept/kadeishvili-theorem`](concepts/kadeishvili-theorem.md) | Kadeishvili 转移定理 | A | dg 代数（或 A∞ 代数）A∞ 拟同构于其同调：H(A) 上存在 A∞ 结构，μ¹=0，μ² 即同调的乘法，高阶项修正结合律。 |
| [`seidel/concept/karoubi-envelope`](concepts/karoubi-envelope.md) | Karoubi 完备化（幂等完备化） | A | 把每个幂等态射 $e$ 形式地分裂成对象 $(X,e)$；三角范畴的幂等完备化仍是三角范畴，且完备化函子保持三角结构（原书 p.56）。 |
| [`seidel/concept/mapping-cone`](concepts/mapping-cone.md) | 映射锥 | A | 零次上闭链 $c\in\hom^0(Y_0,Y_1)$ 的抽象映射锥：$\C(X)=\hom(X,Y_0)[1]\oplus\hom(X,Y_1)$，乘法由 (3.6) 中含 $c$ 的那一项修正。 |
| [`seidel/concept/operad`](concepts/operad.md) | 操作子（operad） | A | 用「n 元运算的合成法则」编码代数结构的语言；A∞ 操作子是结合操作子的 dg 分辨，其代数的 μ^d 正对应分辨的胞腔。 |
| [`seidel/concept/quasi-isomorphism`](concepts/quasi-isomorphism.md) | 拟同构 | A | 取同调后成为范畴同构的 $A_\infty$ 函子；若只要求同调范畴等价，则得到拟等价，它的逆只存在到同伦。 |
| [`seidel/concept/split-generation`](concepts/split-generation.md) | 分裂生成 | A | 最小的包含给定族的「分裂闭三角子范畴」就是全范畴；等价地，每个对象都是该族有限次锥与直和项的组合。 |
| [`seidel/concept/twisted-complex`](concepts/twisted-complex.md) | 扭曲复形 | A | 把链复形的分块微分换成满足广义 Maurer–Cartan 方程的下三角连接 δ；Tw A 由此容纳映射锥、直和与平移。 |
| [`seidel/concept/yoneda-embedding`](concepts/yoneda-embedding.md) | Yoneda 嵌入 | A | 把对象 Y 送到右 A∞ 模 hom_A(−,Y) 的全忠实 A∞ 函子；它给出自由（可表示）模，并把线性 A∞ 范畴嵌入 dg 模型。 |
| [`seidel/concept/brane-structure`](concepts/brane-structure.md) | 膜结构 | B | 把实值分次与 Pin 结构一起加在 Lagrangian 上；它使 Floer 复形有整数分次、模空间有定向。 |
| [`seidel/concept/determinant-line`](concepts/determinant-line.md) | 行列式线 | B | Fredholm 算子的行列式线 $\det(D)=\lambda^{\mathrm{top}}(\operatorname{coker}D)^\vee\otimes\lambda^{\mathrm{top}}(\ker D)$；Cauchy–Riemann 算子的行列式线为模空间提供定向。 |
| [`seidel/concept/exact-lagrangian`](concepts/exact-lagrangian.md) | 正合 Lagrangian 子流形 | B | Liouville 形式在 $L$ 上恰当：$\lambda|_L=da$。它排除非平凡全纯盘，使 Floer 理论只需处理条带，是全书的技术前提。 |
| [`seidel/concept/floer-complex`](concepts/floer-complex.md) | Floer 复形 | B | 由两条正合 Lagrangian 膜的横截交点生成的链复形，微分计数指数差 1 的全纯条带；其同调 HF* 在同痕下不变。 |
| [`seidel/concept/fukaya-category`](concepts/fukaya-category.md) | Fukaya 范畴 | B | 以紧致正合 Lagrangian 膜为对象、Floer 复形为 hom、全纯圆盘计数为高阶运算的 A∞ 范畴；只在同伦意义下含幺。 |
| [`seidel/concept/maslov-class`](concepts/maslov-class.md) | Maslov 类 | B | Lagrangian 切丛的分类映射从 Lagrangian Grassmannian 拉回万有生成元；它是环路 Maslov 指标的上同调版本，也是分次存在的障碍。 |
| [`seidel/concept/maslov-index`](concepts/maslov-index.md) | Maslov 指标与分次 | B | Lagrangian 子空间环路的拓扑绕数；它给出 Lagrange Grassmannian 的普适类，其为零是 Lagrangian 存在分次的障碍。 |
| [`seidel/concept/pin-structure`](concepts/pin-structure.md) | Pin 结构 | B | 正交标架丛到 Pin_n 主丛的提升；障碍是 w₂，存在时全体 Pin 结构恰构成 H¹(B;Z/2) 的 torsor。 |
| [`seidel/concept/serre-functor`](concepts/serre-functor.md) | Serre 函子 | B | 三角范畴上实现 Hom(X,Y)≅Hom(Y,SX)^∨ 的精确函子；Fukaya 范畴因 Poincaré 对偶带扭，只能以弱 Calabi–Yau 方式实现它。 |
| [`seidel/concept/spectral-flow`](concepts/spectral-flow.md) | 谱流 | B | 自伴 Fredholm 算子族随参数变化时特征值穿零的带符号净数；在 Lagrangian 路径上它等于 Maslov 指标，并识别 determinant line。 |
| [`seidel/concept/a-m-singularity`](concepts/a-m-singularity.md) | A_m 型奇点与 Milnor 纤维 | C | 由 $x_0^{m+1}+x_1^2+\cdots+x_n^2$ 的 Milnor 纤维得到的 Lefschetz 纤维化：消失圈按 $A_m$ 箭图相交，其 Fukaya 范畴由箭图代数与 length filtration 显式算出。 |
| [`seidel/concept/dehn-twist`](concepts/dehn-twist.md) | Dehn 扭转 | C | 沿 Lagrangian 球面 V 的余切邻域把纤维方向扭转一圈所得的 exact 辛自同构；它实现绕临界值的单值，并在同调上给出反射公式。 |
| [`seidel/concept/lefschetz-fibration`](concepts/lefschetz-fibration.md) | Lefschetz 纤维化 | C | 到 Riemann 面的 proper 全纯映射：临界点非退化、临界值有限，正则纤维光滑、临界纤维是单节点。 |
| [`seidel/concept/lefschetz-fibration-fukaya-category`](concepts/lefschetz-fibration-fukaya-category.md) | Lefschetz 纤维化的 Fukaya 范畴 | C | 把纤维中的 exact Lagrangian 膜沿纤维化提升、再取 Z/2 不变部分得到的 A∞ 范畴；纤维内一列消失球面 split-generate 它，并与全空间 F(X) 拟满忠实。 |
| [`seidel/concept/matching-cycle`](concepts/matching-cycle.md) | 匹配圈 | C | 连接两个临界值的匹配路径给出总空间中的 Lagrangian 球面：两个 thimble 沿公共消失圈粘合。 |
| [`seidel/concept/picard-lefschetz-formula`](concepts/picard-lefschetz-formula.md) | Picard–Lefschetz 公式 | C | 绕临界值一圈的单值在同调上的显式公式：沿消失圈做一次反射，$x\mapsto x\pm\langle x,\delta\rangle\delta$；它是 Dehn 扭转的同调影子。 |
| [`seidel/concept/thimble`](concepts/thimble.md) | 顶针（thimble） | C | 临界点上方沿道路的消失盘之并：全空间中的 Lagrangian $(n+1)$-球，边界是纤维中的消失圈。 |
| [`seidel/concept/vanishing-cycle`](concepts/vanishing-cycle.md) | 消失圈 | C | 沿消失路径平行移动的极限：临界点附近缩成一点的 Lagrangian 球面 $S^n$，位于光滑纤维中。 |
| [`seidel/deriv/directed-dg`](derivations/directed-dg.md) | directed A∞ 范畴为何可换成 dg 范畴 | A | 按 Cor 5.27：用 Yoneda 像进 $\mathrm{mod}(\B^!)$ 取 directed 子范畴，把 directed A∞ 范畴换成仍 directed、$\mu^{>2}=0$ 的 dg 范畴，并保住 hom 有限维。 |
| [`seidel/deriv/mapping-cone`](derivations/mapping-cone.md) | 把映射锥写成扭曲复形 | A | 取 $C=SX\oplus Y$、$\delta$ 的唯一非零块为 $S(f)$，验证 MC 方程与滤过，并读出 $H^0=\Cone(f)$。 |
| [`seidel/deriv/mu-d-grading`](derivations/mu-d-grading.md) | 为什么 μ^d 的次数是 2−d | A | 从分次与符号约定推出 A∞ 运算 μ^d 的次数：$\deg\mu^d=2-d$，并用 d=1,2,3 校验。 |
| [`seidel/deriv/split-generation`](derivations/split-generation.md) | 分裂闭包 $\Pi(\Tw\A)$ 与分裂生成 | A | $\Tw\A$ 只保证锥；幂等元的像要再取分裂闭包 $\Pi(\Tw\A)$，其存在唯一由 Lemma 4.7 给出，分裂生成由 Cor 4.9 判定。 |
| [`seidel/deriv/theorem-b-construction`](derivations/theorem-b-construction.md) | 定理 B：从 PL 数据构造 $\B$ | A | 由消失圈造出有限 directed A∞ 范畴 $\B_{1,!}$，并给出 $\F(X)\to\Tw\B_{1,!}$ 的上同调全忠实嵌入；$\Tw\B$ 含与 $\F(X)$ 拟等价的全子范畴。 |
| [`seidel/deriv/twisted-differential`](derivations/twisted-differential.md) | 扭曲复形的微分为何平方为零 | A | 展开 $d_T=d+\delta$ 的平方，把 $d_T^2=0$ 化为 $\delta$ 的广义 Maurer–Cartan 方程。 |
| [`seidel/deriv/lefschetz-induction`](derivations/lefschetz-induction.md) | 定理 A 的归纳路线 | C | 把 $X$ 写成 Lefschetz 纤维化，用超平面截面的 PL 数据归纳地计算 $X^1$ 的 Fukaya 范畴。 |
| [`seidel/deriv/mutation`](derivations/mutation.md) | Hurwitz 移动与变异 | C | 基本 Hurwitz 移动 (16.7) 在消失圈上是 Dehn twist、在范畴上是例外聚集的变异 (5.24)，即 $Q\Sigma^\#_{L_k\alpha}\cong L_kQ\Sigma^\#_\alpha$。 |
| [`seidel/correction/a01-introduction-49`](corrections/a01-introduction-49.md) | 译文修订 introduction.tex:49 | A | 初版「$\F(X)$ 与一个 态射空间有限维的 dg 范畴拟同构」改为「$\F(X)$ 与一个态射空间有限维的 dg 范畴拟同构」：译文衍字空格（排版笔误），中文不应断开；英文 p5 同一句无此空格。 |
| [`seidel/correction/a02-section-3-51`](corrections/a02-section-3-51.md) | 译文修订 section-3.tex:51 | A | 初版此处误译：全书仅此一处用 `\mathcal X`，`src\settings.tex` 也未定义 `\X`；英文原书对应式（合订本 L619）作 `Hom_{H(Q)}(X, Z⊗Y)`，且该同构链其余各项都用 `X` |
| [`seidel/correction/a03-section-4-19`](corrections/a03-section-4-19.md) | 译文修订 section-4.tex:19 | A | 初版「对任意 $A$，都有一个**自然的**分裂闭包构造」改为「**平凡的**」：英文 p55 作 tautological，指照定义写出即可、无需论证；「自然」在范畴论中是专门术语，此处误用会造成歧义。 |
| [`seidel/correction/a04-section-6-7`](corrections/a04-section-6-7.md) | 拟修订否决 a04-section-6-7 | A | 复核否决：初版「事实上」正确，原书 p87 实作 In fact，拟改「具体地说」所据的 Concretely 不存在；正文已恢复初版。 |
| [`seidel/correction/operad-shuyunpei`](corrections/operad-shuyunpei.md) | 术语：operad 由「运算胚」改为「操作子」 | A | 初版「运算胚」改为「操作子（operad）」：operad 的通行中文译名是「操作子」；「运算胚」不是标准术语，且「胚」在中文数学中另有 germ 的含义，易致误 |
| [`seidel/correction/a05-section-10-cd-10`](corrections/a05-section-10-cd-10.md) | 译文修订 section-10-cd.tex:10 | B | 初版把 pairs 误作「子对象」：「对子对象」改为「对子」；原书 p137 指每一对 $(L,\gamma)$ 的 Floer 数据，pairs 为复数名词，与 subobject 无关。 |
| [`seidel/correction/a05-section-10-cd-41`](corrections/a05-section-10-cd-41.md) | 译文修订 section-10-cd.tex:41 | B | 初版「$H^3(\pi_0(G);\pi_1(G))$ 中一个典范类」改为「$H^2(\pi_0(G);\pi_1(G))$ 中一个典范类」：同句英文作 in H²(π0(G);π1(G))；同段第 7 条把 $H^3(\Gamma;\HH^0(A,A)^\times)$ 一并改为 $H^2$。 |
| [`seidel/correction/a06-section-11-a-46`](corrections/a06-section-11-a-46.md) | 译文修订 section-11-a.tex:46 | B | 初版漏译「removing the sign」且保留符号因子；改为补出「（即去掉符号）」并删去 $(-1)^{\cdots}$ 因子：原书 p151 讲的是换用另一种约定，两处必须同时改。 |
| [`seidel/correction/a06-section-11-ef-123`](corrections/a06-section-11-ef-123.md) | 译文修订 section-11-ef.tex:123 | B | 初版「$\alpha(s)$ 有非零零空间」改为「有非平凡的零空间」：零空间永远含零向量，nonempty null space 指非零维；主语也应是 $s$ 而非「时刻」。 |
| [`seidel/correction/a06-section-11-gh-32`](corrections/a06-section-11-gh-32.md) | 译文修订 section-11-gh.tex:32 | B | 初版「类对」改为「这一对类」：原文 the pair $(\mu,w_2)$；「类对」不成词，且与后半句「由一个……映射表示」衔接生硬。 |
| [`seidel/correction/a06-section-11-jl-26`](corrections/a06-section-11-jl-26.md) | 译文修订 section-11-jl.tex:26 | B | 初版「虽大体令人满意，却并不完全令人满意」改为「虽大体令人满意，但并不完全」：原文 mostly but not entirely satisfactory，「令人满意」重复，删后保留余地的语气不变。 |
| [`seidel/correction/a07-section-12-ef-106`](corrections/a07-section-12-ef-106.md) | 译文修订 section-12-ef.tex:106 | B | 初版「$c_u$ 的末项 $\longrightarrow\R.$」改为「$\longrightarrow\K.$」：原书 p183 作 → K，同段链映射已取值于 K，$c_u$ 正是把 $|c|_\K$ 逐项求和的对象。 |
| [`seidel/correction/a07-section-12-gh-24`](corrections/a07-section-12-gh-24.md) | 译文修订 section-12-gh.tex:24 | B | 初版维数公式末项 $+d-2$ 改为 $+2-d$：原书 p184 作 $i(y_0)-\cdots-i(y_d)+2-d$，同段下一句与 $\mu^d$ 的次数要求都只能是 $+2-d$；颠倒次序会使维数公式与零维条件矛盾。 |
| [`seidel/correction/a07-section-12-gh-8`](corrections/a07-section-12-gh-8.md) | 译文修订 section-12-gh.tex:8 | B | 初版「$(z_3,\allowbreak \ldots,\allowbreak z_d)\subset(\partial D)^{d-2}$」改为「$\in(\partial D)^{d-2}$」：原书 p183 实印 $\subset$，但 $d-2$ 元组属于乘积空间而非其子集，系原书排印笔误（errata 未收，建议补录）。 |
| [`seidel/correction/a07-section-13-c-25`](corrections/a07-section-13-c-25.md) | 译文修订 section-13-c.tex:25 | B | 初版「图 13.2 把它画成两个竖直边相识别的正方形」改为「两个竖直边相粘合的正方形」：英文 p196 作 a square with the two vertical sides identified；「相识别」不成词，且与图 13.2 的构造不符。 |
| [`seidel/correction/a08-section-14-a-44`](corrections/a08-section-14-a-44.md) | 拟修订否决 a08-section-14-a-44 | B | 复核否决：初版「说明」正确，原书 p199 实作 explains，拟改「给出证明」所据的 gives a proof 不存在；正文已恢复初版。 |
| [`seidel/correction/a08-section-14-c-15`](corrections/a08-section-14-c-15.md) | 译文修订 section-14-c.tex:15 | B | 初版此处误译：英文 p203 作 “There is a Z worth of possible choices for σ” |
| [`seidel/correction/a09-section-16-ab-13`](corrections/a09-section-16-ab-13.md) | 译文修订 section-16-ab.tex:13 | C | 初版「唯一的嵌入 Lagrangian $(n+1)$ 维球」改为「……$(n+1)$ 维球体」：原书 p221 作 unique embedded Lagrangian $(n+1)$-ball；顶针是带边球体，边界才是球面，中文「球」易与 $S^{n+1}$ 混淆。 |
| [`seidel/correction/a09-section-16-ab-44`](corrections/a09-section-16-ab-44.md) | 译文修订 section-16-ab.tex:44 | C | 初版「嵌入的 $(n+1)$ 维球」改为「嵌入的 $(n+1)$ 维球体」：原书 p223 作 "τ'' is an embedded $(n+1)$-ball"；球体带边，边界才是球面。 |
| [`seidel/correction/a09-section-16-ab-51`](corrections/a09-section-16-ab-51.md) | 译文修订 section-16-ab.tex:51 | C | 初版「浸入而不必嵌入的 Lagrangian 球」改为「……Lagrangian 球体」：原书 p223 作 immersed, but not necessarily embedded, Lagrangian balls，指球体而非球面。 |
| [`seidel/correction/a09-section-16-ab-9`](corrections/a09-section-16-ab-9.md) | 译文修订 section-16-ab.tex:9 | C | 初版「$n\leq3$ 时可缩」改为「$n<3$ 时可缩」：原书 p221 作 "contractible for $n<3$"，只断言 $n=1,2$；译文把范围放宽到 $n\leq3$，超出原书结论，故改回。 |
| [`seidel/correction/a09-section-16-cd-10`](corrections/a09-section-16-cd-10.md) | 译文修订 section-16-cd.tex:10 | C | 初版「而 $-|\xi|/2$ 的时间 $2\pi$ 流成为对径映射」改为「而 $-|\xi|^2/2$ 的时间 $2\pi$ 流成为对径映射」：原书 p224 印作 $|\xi|^2/2$，译文回改以忠于原书；其与上下文矛盾处见注 A09-04。 |
| [`seidel/correction/a09-section-16-g-14`](corrections/a09-section-16-g-14.md) | 译文修订 section-16-g.tex:14 | C | 初版「的共形辛嵌入」改为「的共形辛嵌入 $\rho$」：原书 p231 同段后文以 $\rho$ 指称由引理 7.1 得到的嵌入，中文首次出现处未命名，读者无法对上。 |
| [`seidel/correction/a09-section-16-hi-65`](corrections/a09-section-16-hi-65.md) | 译文修订 section-16-hi.tex:65 | C | 初版 $S^{n+1}\subset\CC^{n+2}$ 改为 $S^n\subset\CC^{n+1}$：原书 p234 页图作 $\sqrt{1-s}\,S^n\subset\CC^{n+1}$；消失圈在 $2n$ 维全空间中是 $n$ 维球面。 |
| [`seidel/correction/a09-section-17-a-45`](corrections/a09-section-17-a-45.md) | 译文修订 section-17-a.tex:45 | C | 初版 (17.5) 左端漏写自变量，改为 $R(\partial_s,\partial_t)$：原书 p237 是曲率张量在 $(\partial_s,\partial_t)$ 上的取值，两边类型才相符。 |
| [`seidel/correction/a10-section-17-j-2`](corrections/a10-section-17-j-2.md) | 译文修订 section-17-j.tex:2 | C | 初版「\stref{例题}{17.15}适用」改为「17.14 适用」：原书 p261 作 "In the remaining case, Example 17.14 applies"；此句正讲例 17.14 的非平凡 Pin 结构结论。 |
| [`seidel/correction/a10-section-17-k-41`](corrections/a10-section-17-k-41.md) | 译文修订 section-17-k.tex:41 | C | 初版把同伦修正项误作 $k$，改为 $\kappa$：原书 p265 方框内第二式作 $\kappa(\epsilon_{\mathcal A}(c_0))$ 与 $\kappa(c_0)$，与前文「得到 $(\gamma,\kappa)$」一致；$k$ 是原链映射，$\kappa$ 是其修正。 |
| [`seidel/correction/a12-section-19-c-33`](corrections/a12-section-19-c-33.md) | 译文修订 section-19-c.tex:33 | C | 初版「反转定向」改为「反向」：原文 unique up to isotopy and orientation-reversal；这里反向的是匹配路径的参数方向，不是流形定向。 |
| [`seidel/correction/a12-section-20-b-20`](corrections/a12-section-20-b-20.md) | 译文修订 section-20-b.tex:20 | C | 初版「至少将 $A_\infty$ 结构变成严格含幺后如此」改为「至少在把 $A_\infty$ 结构做成严格含幺之后是如此」：原文 once one has made …，改后句子完整、once 从句对应。 |
| [`seidel/correction/lefschetz-thimble-dingzhen`](corrections/lefschetz-thimble-dingzhen.md) | 术语：Lefschetz thimble 由「指套」改为「顶针」 | C | 初版「指套」改为「顶针（thimble）」：thimble 的数学含义是临界点上方沿道路的消失盘，标准译名是「顶针」；「指套」是 finger cot，与数学对象无关 |
