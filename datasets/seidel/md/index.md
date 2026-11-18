# Seidel 资料卡索引

共 54 张：概念 16　推导 8　勘误 30

| id | 标题 | track | 一句话 |
|---|---|---|---|
| [`seidel/concept/a-infinity-algebra`](concepts/a-infinity-algebra.md) | A∞ 代数 | A | 带一串多重线性运算 μ^d 的分次向量空间：μ¹ 是微分，μ² 是同伦意义下的乘法，高阶 μ^d 修正结合律的失效。 |
| [`seidel/concept/a-infinity-category`](concepts/a-infinity-category.md) | A∞ 范畴 | A | 对象之间的 hom 是分次向量空间，复合是一族满足 A∞ 关系的多重线性映射；恒等态射只在同伦意义下存在。 |
| [`seidel/concept/exact-triangle`](concepts/exact-triangle.md) | 殊三角（正合三角） | A | 三角范畴里代替正合列的结构：X→Y→Z→TX，满足 TR1–TR4；在 Tw A 中由映射锥给出。 |
| [`seidel/concept/karoubi-envelope`](concepts/karoubi-envelope.md) | Karoubi 完备化（幂等完备化） | A | 把每个幂等态射 e 形式地分裂成对象 (X,e)；三角范畴的幂等完备化仍是三角范畴，且函子保持三角结构。 |
| [`seidel/concept/split-generation`](concepts/split-generation.md) | 分裂生成 | A | 最小的包含给定族的「分裂闭三角子范畴」就是全范畴；等价地，每个对象都是该族有限次锥与直和项的组合。 |
| [`seidel/concept/twisted-complex`](concepts/twisted-complex.md) | 扭曲复形 | A | 把链复形的分块微分换成满足广义 Maurer–Cartan 方程的下三角连接 δ；Tw A 由此容纳映射锥、直和与平移。 |
| [`seidel/concept/brane-structure`](concepts/brane-structure.md) | 膜结构 | B | 把分次与相对 Pin 结构一起加在 Lagrangian 上；它使 Floer 复形有整数分次、模空间有定向。 |
| [`seidel/concept/determinant-line`](concepts/determinant-line.md) | 行列式线 | B | Fredholm 算子的行列式线 det(D)=λ^top ker D⊗(λ^top coker D)^∨；Cauchy–Riemann 算子的行列式线为模空间提供定向。 |
| [`seidel/concept/exact-lagrangian`](concepts/exact-lagrangian.md) | 正合 Lagrangian 子流形 | B | Liouville 形式在 L 上恰当：λ|_L=da。它排除非平凡全纯盘，使 Floer 理论只需处理条带，并让 L 获得分次。 |
| [`seidel/concept/floer-complex`](concepts/floer-complex.md) | Floer 复形 | B | 由两条 Lagrangian 的横截交点生成的链复形，微分计数指数差 1 的全纯条带；其同调 HF* 在同痕下不变。 |
| [`seidel/concept/fukaya-category`](concepts/fukaya-category.md) | Fukaya 范畴 | B | 以紧致分次 Lagrangian 膜为对象、Floer 复形为 hom、全纯圆盘计数为高阶运算的 A∞ 范畴；只在同伦意义下含幺。 |
| [`seidel/concept/maslov-index`](concepts/maslov-index.md) | Maslov 指标与分次 | B | Lagrangian 子空间环路绕固定子空间的拓扑绕数；对带分次的 Lagrangian，它给出每点的整值相位，决定 Floer 复形的分次。 |
| [`seidel/concept/lefschetz-fibration`](concepts/lefschetz-fibration.md) | Lefschetz 纤维化 | C | 到曲线的 proper 全纯映射：临界点非退化、临界值有限，纤维除临界值外光滑、临界纤维有单个节点。 |
| [`seidel/concept/matching-cycle`](concepts/matching-cycle.md) | 匹配圈 | C | 连接两个临界值的匹配路径在纤维中给出的 Lagrangian 球面，是相应 thimble 的边界。 |
| [`seidel/concept/thimble`](concepts/thimble.md) | 顶针（thimble） | C | 临界点上方沿道路的消失盘之并：全空间中的 Lagrangian 盘，边界是纤维中的消失圈。 |
| [`seidel/concept/vanishing-cycle`](concepts/vanishing-cycle.md) | 消失圈 | C | 绕临界值平行移动的极限：临界点附近缩成一点的球面 $S^{n-1}$，位于光滑纤维中，是 Lagrangian。 |
| [`seidel/deriv/directed-dg`](derivations/directed-dg.md) | directed A∞ 范畴为何可换成 dg 范畴 | A | 按对象排序、用严格单位元与下三角消去高阶运算，把 directed A∞ 范畴替换为同调等价的 dg 范畴。 |
| [`seidel/deriv/mapping-cone`](derivations/mapping-cone.md) | 把映射锥写成扭曲复形 | A | 取 $X=Y\oplus X$、$\delta$ 的唯一非零分量为 $f$，验证它满足 MC 方程，且 $H^0$ 是锥。 |
| [`seidel/deriv/mu-d-grading`](derivations/mu-d-grading.md) | 为什么 μ^d 的次数是 2−d | A | 从分次与符号约定推出 A∞ 运算 μ^d 的次数：$\deg\mu^d=2-d$，并用 d=1,2,3 校验。 |
| [`seidel/deriv/split-generation`](derivations/split-generation.md) | 分裂闭包与幂等元的实现 | A | 把幂等态射形式地添成对象：$e=e^2$ 的像由锥 $\Cone(e)$ 实现，故 $\Tw\A$ 已分裂闭。 |
| [`seidel/deriv/theorem-b-construction`](derivations/theorem-b-construction.md) | 定理 B：从 PL 数据构造 $\B$ | A | 以消失圈为对象造有限 A∞ 范畴 $\B$，证明它 directed，并给出 $\Tw\B$ 到 $\F(X)$ 的拟等价全子范畴。 |
| [`seidel/deriv/twisted-differential`](derivations/twisted-differential.md) | 扭曲复形的微分为何平方为零 | A | 展开 $d_T=d+\delta$ 的平方，把 $d_T^2=0$ 化为 $\delta$ 的广义 Maurer–Cartan 方程。 |
| [`seidel/deriv/lefschetz-induction`](derivations/lefschetz-induction.md) | 定理 A 的归纳路线 | C | 把 $X$ 写成 Lefschetz 纤维化，用超平面截面的 PL 数据归纳地计算 $X^1$ 的 Fukaya 范畴。 |
| [`seidel/deriv/mutation`](derivations/mutation.md) | Hurwitz 移动与变异 | C | 匹配路径的 Hurwitz 移动对应例外聚集的变异；这是把 PL 几何翻译成代数操作的枢纽。 |
| [`seidel/correction/a01-introduction-49`](corrections/a01-introduction-49.md) | 译文修订 introduction.tex:49 | A | 初版「$\F(X)$ 与一个 态射空间有限维的 dg 范畴拟同构」改为「$\F(X)$ 与一个态射空间有限维的 dg 范畴拟同构」：衍字空格（笔误），中文不应断开 |
| [`seidel/correction/a02-section-3-51`](corrections/a02-section-3-51.md) | 译文修订 section-3.tex:51 | A | 初版此处误译：全书仅此一处用 `\mathcal X`，`src\settings.tex` 也未定义 `\X`；英文原书对应式（合订本 L619）作 `Hom_{H(Q)}(X, Z⊗Y)`，且该同构链其余各项都用 `X` |
| [`seidel/correction/a03-section-4-19`](corrections/a03-section-4-19.md) | 译文修订 section-4.tex:19 | A | 初版「对任意 $A$，都有一个**自然的**分裂闭包构造」改为「对任意 $A$，都有一个**平凡的**分裂闭包构造」：英文 p55 为 "there is a **tautological** construction… |
| [`seidel/correction/a04-section-6-7`](corrections/a04-section-6-7.md) | 译文修订 section-6.tex:7 | A | 初版「事实上，它只由对象上的对合……」改为「具体地说，它只由对象上的对合……」：英文 p087 原文以 "Concretely," 起句，是「具体地说」而非「事实上」；「事实上」会把一句限定说明读成让步，与下文列举「对合… |
| [`seidel/correction/operad-shuyunpei`](corrections/operad-shuyunpei.md) | 术语：operad 由「运算胚」改为「操作子」 | A | 初版「运算胚」改为「操作子（operad）」：operad 的通行中文译名是「操作子」；「运算胚」不是标准术语，且「胚」在中文数学中另有 germ 的含义，易致误 |
| [`seidel/correction/a05-section-10-cd-10`](corrections/a05-section-10-cd-10.md) | 译文修订 section-10-cd.tex:10 | B | 初版此处误译：英文 "the Floer data for the pairs ((L0,γ0), φ(Ld,γd))" |
| [`seidel/correction/a05-section-10-cd-41`](corrections/a05-section-10-cd-41.md) | 译文修订 section-10-cd.tex:41 | B | 初版「$H^3(\pi_0(G);\pi_1(G))$ 中一个典范类」改为「$H^2(\pi_0(G);\pi_1(G))$ 中一个典范类」：同句英文本作 "in H 2.0.G/I 1.G//"；"对任意拓扑群都存在"的典… |
| [`seidel/correction/a06-section-11-a-46`](corrections/a06-section-11-a-46.md) | 译文修订 section-11-a.tex:46 | B | 初版此处误译：原书此处说的是「改用另一约定（removing the sign）」，即把式 (11.2) 的符号因子去掉 |
| [`seidel/correction/a06-section-11-ef-123`](corrections/a06-section-11-ef-123.md) | 译文修订 section-11-ef.tex:123 | B | 初版此处误译：原文为 those $s$ where $\alpha(s)$ has a nonempty null space |
| [`seidel/correction/a06-section-11-gh-32`](corrections/a06-section-11-gh-32.md) | 译文修订 section-11-gh.tex:32 | B | 初版此处误译：「类对」在中文里不成词（原文 the pair $(\mu,w_2)$），且与后半句「由一个……映射表示」衔接生硬 |
| [`seidel/correction/a06-section-11-jl-26`](corrections/a06-section-11-jl-26.md) | 译文修订 section-11-jl.tex:26 | B | 初版此处误译：原文 mostly but not entirely satisfactory |
| [`seidel/correction/a07-section-12-ef-106`](corrections/a07-section-12-ef-106.md) | 译文修订 section-12-ef.tex:106 | B | 初版此处误译：原书印刷页 183 作 `cu: o(Λ#_{y,0}, Λ#_{y,1}⊗λtop(Λ_{y,1})) → K` |
| [`seidel/correction/a07-section-12-gh-24`](corrections/a07-section-12-gh-24.md) | 译文修订 section-12-gh.tex:24 | B | 初版此处误译：原书印刷页 184 明确作 `i(y0) − i(y1) − ··· − i(yd) + 2 − d`；同段下一句「$i(y_0)=i(y_1)+\cdots+i(y_d)+2-d$」与 $\mu^d$… |
| [`seidel/correction/a07-section-12-gh-8`](corrections/a07-section-12-gh-8.md) | 译文修订 section-12-gh.tex:8 | B | 初版此处误译：原书印刷页 183 作 `(z3,…,zd) ∈ (∂D)^{d−2}`：这是一个 $d-2$ 元组，属于该乘积空间，不是它的子集 |
| [`seidel/correction/a07-section-13-c-25`](corrections/a07-section-13-c-25.md) | 译文修订 section-13-c.tex:25 | B | 初版「图 13.2 把它画成两个竖直边相识别的正方形」改为「改为「两个竖直边相粘合的正方形」」：英文为 `a square with the two vertical sides identified` |
| [`seidel/correction/a08-section-14-a-44`](corrections/a08-section-14-a-44.md) | 译文修订 section-14-a.tex:44 | B | 初版此处误译：英文 p199 作 “hence gives a proof of (14.3)” |
| [`seidel/correction/a08-section-14-c-15`](corrections/a08-section-14-c-15.md) | 译文修订 section-14-c.tex:15 | B | 初版此处误译：英文 p203 作 “There is a Z worth of possible choices for σ” |
| [`seidel/correction/a09-section-16-ab-13`](corrections/a09-section-16-ab-13.md) | 译文修订 section-16-ab.tex:13 | C | 初版「唯一的嵌入 Lagrangian $(n+1)$ 维球」改为「……$(n+1)$ 维球体」：原书 "unique embedded Lagrangian $(n+1)$-ball"；指套是球体（带边），其边界才是球面，… |
| [`seidel/correction/a09-section-16-ab-44`](corrections/a09-section-16-ab-44.md) | 译文修订 section-16-ab.tex:44 | C | 初版「嵌入的 $(n+1)$ 维球」改为「嵌入的 $(n+1)$ 维球体」：同上，指套的存在性论证中 $\Delta''_\gamma$ 是带边流形 |
| [`seidel/correction/a09-section-16-ab-51`](corrections/a09-section-16-ab-51.md) | 译文修订 section-16-ab.tex:51 | C | 初版「浸入而不必嵌入的 Lagrangian 球」改为「……Lagrangian 球体」：同上；该处讨论的是"球体（ball）的浸入"而非球面 |
| [`seidel/correction/a09-section-16-ab-9`](corrections/a09-section-16-ab-9.md) | 译文修订 section-16-ab.tex:9 | C | 初版此处误译：原书 Remark 16.1 印 "contractible for $n<3$"（p221 放大逐字确认）；$n=3$ 时该群不平凡，边界放错会连带后文"标架不重要"的适用范围 |
| [`seidel/correction/a09-section-16-cd-10`](corrections/a09-section-16-cd-10.md) | 译文修订 section-16-cd.tex:10 | C | 初版「而 $-」改为「\xi」：/2$ 的时间 $2\pi$ 流成为对径映射 |
| [`seidel/correction/a09-section-16-g-14`](corrections/a09-section-16-g-14.md) | 译文修订 section-16-g.tex:14 | C | 初版「的共形辛嵌入」改为「的共形辛嵌入 $\rho$」：原书同段后文以 $\rho$ 指称这个由引理 7.1 得到的嵌入（"independent of the choices of $(\phi^s)$, of the… |
| [`seidel/correction/a09-section-16-hi-65`](corrections/a09-section-16-hi-65.md) | 译文修订 section-16-hi.tex:65 | C | 初版此处误译：原书 p234 放大确认为 $S^n\subset\CC^{n+1}$；消失圈在 $2n$ 维全空间中是 $n$ 维球面，维数写错会破坏引理 16.15 的整个论证 |
| [`seidel/correction/a09-section-17-a-45`](corrections/a09-section-17-a-45.md) | 译文修订 section-17-a.tex:45 | C | 初版此处误译：(17.5) 原书左端是曲率张量在 $(\partial_s,\partial_t)$ 上的取值，译文漏掉自变量，等式两边类型不符 |
| [`seidel/correction/a10-section-17-j-2`](corrections/a10-section-17-j-2.md) | 译文修订 section-17-j.tex:2 | C | 初版「在剩下的情形中，\stref{例题}{17.15}适用」改为「在剩下的情形中，\stref{例题}{17.14}适用」：原书 p261 作 “In the remaining case, Example 17.14… |
| [`seidel/correction/a10-section-17-k-41`](corrections/a10-section-17-k-41.md) | 译文修订 section-17-k.tex:41 | C | 初版此处误译：原书 p265 方框内第二式为 $-\epsilon_{\mathcal A}(\kappa(\epsilon_{\mathcal A}(c_0)))+\kappa(c_0)=0$（已裁图放大核对） |
| [`seidel/correction/a12-section-19-c-33`](corrections/a12-section-19-c-33.md) | 译文修订 section-19-c.tex:33 | C | 初版此处误译：英文 p300 作 "unique up to isotopy and orientation-reversal" |
| [`seidel/correction/a12-section-20-b-20`](corrections/a12-section-20-b-20.md) | 译文修订 section-20-b.tex:20 | C | 初版此处误译：英文 p306 作 "at least once one has made the $A_\infty$-structure strictly unital" |
| [`seidel/correction/lefschetz-thimble-dingzhen`](corrections/lefschetz-thimble-dingzhen.md) | 术语：Lefschetz thimble 由「指套」改为「顶针」 | C | 初版「指套」改为「顶针（thimble）」：thimble 的数学含义是临界点上方沿道路的消失盘，标准译名是「顶针」；「指套」是 finger cot，与数学对象无关 |
