# 学术语境调研：Frenkel《朗兰兹纲领与共形场论讲义》

**对象**：E. Frenkel, *Lectures on the Langlands Program and Conformal Field Theory*, arXiv:hep-th/0512172（2005 年 12 月提交）
**调研**：disc ｜ **日期**：2026-11-13 ｜ **用途**：《朗兰兹纲领与共形场论》中文译注本「学术语境」部分素材

## 0. 方法与边界

本文回答两件事：这份讲义在互联网上被谁、在什么场合引用与推荐；2005 年之后这一交叉领域的关键进展。凡事实性断言均附链接；未能核实而只能推断处，一律标「推测」。检索手段包括 arXiv、INSPIRE、Semantic Scholar、Crossref、zbMATH 的元数据接口、Stack Exchange API 与网页检索；抓取失败的站点在 §1.5 逐条说明，不作「不存在」的断言。

## 一、互联网上的讨论与引用语境

### 1.1 文本的基本事实

- arXiv 摘要自述：这是一份「自足」的讲稿，主要写给物理学家，「只需很少的数学背景」。[arXiv:hep-th/0512172](https://arxiv.org/abs/hep-th/0512172)
- INSPIRE 记录给出两个来源场合：2003 年 Les Houches 暑期学校（会议记录 C03-03-09.2）与 2005-04-08 普林斯顿 DARPA「Langlands Program and Physics」工作坊（C05-04-08.3），共 128 页；2007 年由 Springer 收入论文集，占 pp. 387–533，DOI 10.1007/978-3-540-30308-4_11。[INSPIRE API](https://inspirehep.net/api/arxiv/hep-th/0512172) 出版版跨 147 页，与 arXiv 的 128 页不同，差异性质未核实（推测为排版与增补）。
- 作者主页上的版本文件名为 `houches.pdf`，与讲义源自 Les Houches 讲席相合。[math.berkeley.edu/~frenkel/houches.pdf](https://math.berkeley.edu/~frenkel/houches.pdf)
- AIM（American Institute of Mathematics）的 sl2x「collected works」项目提供了按节切分的 HTML 版，说明它被当作可长期引用的文本处理。[AIM sl2x](https://sl2x.aimath.org/development/collectedworks/htmlpaper/hep-th_0512172/theindex.html)
- 截至检索时，INSPIRE 引用计数 111，不含自引 99。[INSPIRE](https://inspirehep.net/api/arxiv/hep-th/0512172)

### 1.2 谁在引用、在什么场合

**（1）数学家把它当「入门读物」。** 最有力的证词来自 Langlands 本人：在 2012 年《A Prologue to "Functoriality and Reciprocity" Part I》里，他把本讲义连同另两份文献、以及作者写给他的信，称为自己「进入几何理论的入门」。[DOI:10.2140/PJM.2012.260.583](https://doi.org/10.2140/PJM.2012.260.583)

Witten 2015 年的《More On Gauge Theory And Geometric Langlands》把它列为几何 Langlands 的导论性文献，讨论 Deligne 的交换情形论证时也注明「见该文」。[arXiv:1506.04293](https://arxiv.org/abs/1506.04293)

需要「可读的 Langlands 引论」的数学作者同样用它：Movshev 在《Duality for finite Gelfand pairs》里写「see [8] for an accessible introduction to Langlands theory」；Candelas–de la Ossa–McGovern（2024）推荐其 §3.1 为「相对易读的引论」。这两条上下文取自 Semantic Scholar 的引用上下文接口，[引用者列表](https://api.semanticscholar.org/graph/v1/paper/arXiv:hep-th/0512172/citations?fields=title,year,authors,contexts&limit=100)。

**（2）综述作者把它当「标准综述」。** Teschner 关于几何 Langlands 与 CFT 的综述反复写「see [8] for a review」[arXiv:1707.07873](https://arxiv.org/abs/1707.07873)；Balasubramanian–Teschner 讨论 Beilinson–Drinfeld 路线时同样指向它[arXiv:1702.06499](https://arxiv.org/abs/1702.06499)；最新的 Abedin–Felder–Windesheim（2025）写「关于几何 Langlands 对应与共形场论的联系，综述见 [15]」[arXiv:2509.02368](https://arxiv.org/abs/2509.02368)；Aganagic–Frenkel–Okounkov 引它作为综述性文献并沿用其 $W_k$ 代数约定[arXiv:1701.03146](https://arxiv.org/abs/1701.03146)。

**（3）物理学家把它当「进入几何 Langlands 的物理侧跳板」。** Kapustin–Witten 2007 年那篇奠基性长文的参考文献里就列了本讲义（INSPIRE 记录 700424），说明在物理学家把几何 Langlands 重写为 $\mathcal{N}=4$ 超对称规范论的对偶之前，这份讲义已是他们手边的入口。[hep-th/0604151](https://arxiv.org/abs/hep-th/0604151) 此后 Elliott–Yoo 讨论量子几何 Langlands 范畴时把概念溯源到 [Fre07][arXiv:2008.10988](https://arxiv.org/abs/2008.10988)，Khan–Zeng（2025）在顶点代数语境里引 [Fre05][arXiv:2502.13227](https://arxiv.org/abs/2502.13227)。

**（4）物理学哲学也用它。** Weatherall 讨论电磁对偶的哲学文章引 Frenkel (2007)，用它说明物理对偶与几何 Langlands 的对应关系。[DOI:10.1086/710630](https://doi.org/10.1086/710630)

**（5）课堂与讨论班。** UCLA 的 Rouquier 在 2020 年春「Introduction to the Geometric Langlands Program」（285P）参考书目中列了本讲义，与 Gaitsgory、Ben-Zvi 的笔记并列。[课程页](https://www.math.ucla.edu/~rouquier/langlands.html) Ben-Zvi 的 GRASP 讲义页则是同领域另一常被推荐的入口。[GRASP](https://web.ma.utexas.edu/users/benzvi/Langlands.html)

**（6）问答网站上有逐页使用的痕迹。** MathOverflow 2018 年问题《Examples of function fields Langlands for small genus (≤2)》开篇即说「关于函数域 Langlands 的讲解见 Frenkel 这篇文章」，并具体引到 §2.2（p.27）、§2.3（p.29）与 p.32，把它当教科书用。[MO 300985](https://mathoverflow.net/questions/300985) 2012 年问题《How does one understand geometric CFT in terms of modularity?》则把它列入自己查阅的三份主要文献。[MO 100977](https://mathoverflow.net/questions/100977)

**（7）博客。** Peter Woit 在 Not Even Wrong 的《Geometric Langlands and QFT》（2007-11-30）里记录了 IAS 的「Gauge Theory and Representation Theory」会议，并在回复读者时推荐「Ben-Zvi 的几何 Langlands 网站 + Frenkel 的几篇长综述」作为最好的入门——推荐的是 Frenkel 的综述性写作整体，并未单独点名这份讲义。[Woit, p=624](https://www.math.columbia.edu/~woit/wordpress/?p=624)

**（8）引用者分布（小结）。** 把上面这些例子按领域归类：数学（Langlands 本人、Movshev、Candelas 等、Rouquier 的课程书单）、物理（Kapustin–Witten、Witten、Aganagic–Frenkel–Okounkov、Elliott–Yoo、Khan–Zeng）、物理学哲学（Weatherall）、综述写作（Teschner 两篇、Abedin–Felder–Windesheim）四类大致平分。这与「111 次引用」的绝对数字放在一起颇有意思：作为一篇 128 页的讲稿，它的引用数在 INSPIRE 里并不惊人，但引用者名单里有 Langlands 与 Witten，且被反复用「review」「introduction」这类词描述。衡量它的指标不是引用数，而是它作为「入口」的位置。

### 1.3 它被当作什么来用

四类角色，边界并不严格：

1. **给物理学家的几何 Langlands 入门**——摘要自述的定位，也是 Witten、Movshev 与课程大纲的实际用法；
2. **Les Houches / DARPA 讲稿**——两个会议场合决定了它「课堂讲义」而非「研究论文」的体例：背景铺垫多、证明少；
3. **「共形场论一侧」的标准综述**——覆盖 Beilinson–Drinfeld 的 Kac–Moody 局部化、conformal blocks、以及把 Hecke 特征层实现为 D-模这条路线，而这正是 2024 年证明最终整合的两条路线之一（见 §2）；
4. **与 Kapustin–Witten 对照的读物**——两者时间上前后脚（讲义 2005-12，KW 2006-04），且 KW 直接引用它；读者自然并读：讲义讲「CFT 如何给出几何 Langlands」，KW 讲「同一个对应如何从四维规范论的对偶读出」。

### 1.4 公开的批评、勘误与疑难

本轮检索没有找到针对这份讲义的公开勘误或系统性批评，也没有发现修订说明文件。但有三点「时代性疑难」值得译注本指出：

1. **精确表述晚于讲义。** 讲义写作时，几何 Langlands 猜想尚无今天通行的精确形式；2012 年 Arinkin–Gaitsgory 引入奇异支撑，才给出「带幂零奇异支撑的 ind-coherent sheaves」这一表述。[arXiv:1201.6343](https://arxiv.org/abs/1201.6343) 因此讲义中「猜想应当如何陈述」的段落，今天读需对照 2012 年后的版本，而不能当作定稿。
2. **该猜想现在已成定理。** 2024 年 Gaitsgory–Raskin 团队的五篇论文（合计 >800 页）宣布在 $\mathbb{C}$ 上、非分歧情形完成证明。[IHES 公告](https://www.ihes.fr/en/gaitsgory-glc/) 讲义里以「open problem」身份出现的内容，其地位已改变。
3. **CFT 路线曾被看作「另一条更难走的路」，结果被证明不可或缺。** IHES 的说明中，Gaitsgory 明确说 2024 年的证明同时使用了 Drinfeld–Laumon 的 Whittaker 路线与 Beilinson–Drinfeld 的 Kac–Moody 局部化（即 CFT）路线，「我们把两种方法互相对撞」[IHES](https://www.ihes.fr/en/gaitsgory-glc/)。这既是对讲义视角的「追认」，也提示读者：讲义对 CFT 路线的强调在 2005 年是前瞻性的，而非过时。

另有一处不算错误、但值得提醒：讲义自称「只需很少数学背景」，实际阅读门槛因人而异——MathOverflow 上确实有读者按页引用它，但那是已具备代数几何与表示论背景的读者。

### 1.5 检索到与未检索到的

- **n-Category Café**：未取得直接讨论本讲义的证据。多次抓取 `golem.ph.utexas.edu` 的检索页与帖子均失败（fetch failed），因此只能记为「未取得证据」，不能断言不存在。
- **Physics Stack Exchange**：用站内 `/search/excerpts` 检索「Langlands conformal field theory reference」「hep-th/0512172」无相关命中；只找到与本讲义无直接引用关系的邻近材料——Braverman 2011 年提问 Kapustin–Witten 扭化是否给出良定义的 TQFT（24 赞）。[PSE 27370](https://physics.stackexchange.com/questions/27370)
- **Terence Tao 博客**：本轮以「Tao + Langlands」为线索的检索未发现讨论这份讲义的页面；这只是检索覆盖问题，不构成不存在断言。
- 中文互联网未做系统检索（不在本任务范围），如需可另开一轮。

### 1.6 「被推荐」与「被使用」是两种证据

Woit 的推荐是本讲义最典型的「被推荐」样本：他给读者的建议是 Frenkel 的「几篇长综述」，而不是单独这一篇。这说明在 2007 年的语境里，Frenkel 的综述写作是一个整体品牌，本讲义是其中的长篇之一，读者被引导去读的是「Frenkel 式导引」而不是某一份具体文档。相反，MathOverflow 300985 那种「§2.2 见 p.27」的引法属于「被使用」：提问者已越过入门阶段，把它当工具书核对具体陈述。

两种证据对译注本的意义不同：「被推荐」支撑的是「为什么值得译」——它在社群里的定位是入口；「被使用」支撑的是「正文里的具体论断有人核对过」——它有读者按页对照过。本调研里「被使用」的硬证据集中在函数域 Langlands 与几何 CFT 两节，恰好也是讲义技术含量最高、最值得下注释功夫的两节。这一重合不是巧合：能被按页引用的段落，通常就是同行真正在用的段落。

## 二、2005 年之后的进展：简明年表

- **2007｜Kapustin–Witten**：把四维 $\mathcal{N}=4$ 超对称 Yang–Mills 在 Riemann 面上扭化紧化，使几何 Langlands 的 Hecke 特征层与 D-模从规范论的 $S$-对偶中自然出现；CNTP 1 (2007) 1–236。[arXiv:hep-th/0604151](https://arxiv.org/abs/hep-th/0604151)｜[DOI:10.4310/CNTP.2007.v1.n1.a1](https://doi.org/10.4310/CNTP.2007.v1.n1.a1)
- **2008｜Ngô Bảo Châu**：证明 Lie 代数情形的基本引理，核心工具是 Hitchin 纤维化的几何与阿贝尔化，为自守形式侧补上长期悬置的技术基石。[arXiv:0801.0446](https://arxiv.org/abs/0801.0446)
- **2012｜Arinkin–Gaitsgory**：为拟光滑 DG 栈上的相干层定义奇异支撑，并用它给出几何 Langlands 猜想的现代精确表述。[arXiv:1201.6343](https://arxiv.org/abs/1201.6343)
- **2015｜Witten 再论**：在《More On Gauge Theory And Geometric Langlands》里继续发展规范论视角，并把本讲义当作几何 Langlands 的导论引用。[arXiv:1506.04293](https://arxiv.org/abs/1506.04293)
- **2016→2021｜Fargues–Scholze**：在 Fargues–Fontaine 曲线上建立 $p$ 进几何 Langlands 的基础——$\mathrm{Bun}_G$ 上的 $\ell$-进层范畴、几何 Satake、$L$-参数栈；2016 年先有 overview，正文 2021 年首发、2024 年定稿（356 页）。[arXiv:1602.00999](https://arxiv.org/abs/1602.00999)｜[arXiv:2102.13459](https://arxiv.org/abs/2102.13459)
- **2017｜物理侧的综述化**：Teschner、Balasubramanian–Teschner 等把量子几何 Langlands 与共形场论、可积模型的关系写成综述，本讲义被当作该主题的标准综述反复引用。[arXiv:1707.07873](https://arxiv.org/abs/1707.07873)｜[arXiv:1702.06499](https://arxiv.org/abs/1702.06499)
- **2010 年代–2020 年代｜Gaitsgory 及其合作者**：把 $\mathbb{C}$ 上非分歧情形的证明拆成五篇——构造函子；Kac–Moody 局部化与 FLE；与抛物诱导的相容性；ambidexterity；重数一定理——由 Arinkin、Beraldo、Campbell、Chen、Faergeman、Gaitsgory、Lin、Raskin、Rozenblyum 合写。[GLC 主页](https://people.mpim-bonn.mpg.de/gaitsgde/GLC/)
- **2024 年｜五篇论文公开**：即上条五篇，合计 >800 页，宣称证明（categorical, unramified）几何 Langlands 猜想，覆盖 $\mathbb{C}$ 上 de Rham 与 Betti 两种设定。[GLC](https://people.mpim-bonn.mpg.de/gaitsgde/GLC/)
- **2024-08-05｜IHES 公告**：以《On the Proof of the Geometric Langlands Correspondence》为题介绍该工作，Gaitsgory 撰文解释两条历史路线的整合，并说明下一步是 ramified 情形。[IHES](https://www.ihes.fr/en/gaitsgory-glc/)
- **2024-09｜相对几何 Langlands**：Ben-Zvi–Sakellaridis–Venkatesh 提出「相对 Langlands 对偶」，把几何 Langlands 推广到带对称子群/球子群的情形。[arXiv:2409.04677](https://arxiv.org/abs/2409.04677)
- **2024-11｜社区盘点「下一步」**：MathOverflow 上关于新证明含义与推论的提问中，Ben-Zvi 的回答（31 赞）列出未解方向：其他层论设定（Dolbeault/Donagi–Pantev、motivic）、quantum GL、relative GLC、ramification、local GLC（loop group 表示的 2-范畴）、3-流形不变量、Etingof–Frenkel–Kazhdan 的解析 Langlands、Scholze 的 twistor $\mathbb{P}^1$、char $p$ 的 étale 非分歧情形、Fargues–Fontaine 曲线/Fargues–Scholze、以及 de Rham 的 $p$ 进情形（Emerton–Gee stack）；Will Sawin 在评论中补充：证明本身难以移植到 $p$ 进，但其中的想法可能经 Fargues–Scholze 影响 $p$ 进局部 Langlands。[MO 481662](https://mathoverflow.net/questions/481662)
- **2025｜教科书化**：Abedin–Felder–Windesheim 的综述仍以本讲义为「几何 Langlands 与 CFT 的联系」的综述入口，说明二十年后它还在承担导引功能。[arXiv:2509.02368](https://arxiv.org/abs/2509.02368)

### 2.1 关于「Ngô–Yun」一条的核实说明

任务要求列入「Ngô–Yun 关于 Hitchin 系统与基本引理的工作」。我做了三轮检索（arXiv 全库标题检索「Hitchin fibrations」「abelianization」、Crossref 按作者+题名检索、网页精确短语检索），**没有**找到一篇题为《Hitchin fibrations, abelianization, and the fundamental lemma》的 Ngô–Yun 论文，也没有可核实的 arXiv 编号。Crossref 里确有 2026 年 Princeton University Press 出版的同名书（DOI 10.1515/9780691293141），但其作者字段显示为 X. Griffin Wang，与 Ngô–Yun 不符，不能据此归属。为不编造，本节只写两条可核实的关联：

- Ngô 2008 年的基本引理证明本身就以 Hitchin 纤维化的几何为核心 [arXiv:0801.0446](https://arxiv.org/abs/0801.0446)；
- Yun 的《Langlands duality and global Springer theory》（Compositio 2010）把整体 Springer 理论用于 Hitchin 纤维化的阿贝尔化，是主题上最接近的可核实工作（zbMATH 06051028）。

若译注本确需写 Ngô–Yun 的合作论文，建议由项目负责人提供准确出处后再补；此条标为「待核实」。

### 2.2 三条主线如何汇合

把 2005 年讲义与 2024 年证明对照，可以看到三条线的合流：**（i）CFT 线**——Beilinson–Drinfeld 的 Kac–Moody 局部化与 conformal blocks，讲义的主线；**（ii）Whittaker 线**——Drinfeld–Laumon 的显式构造，讲义亦有交代；**（iii）层论线**——Arinkin–Gaitsgory 的奇异支撑给出正确表述；IHES 的说明还指出，「带幂零奇异支撑」这一条件 Laumon 在 1987 年已认识到，后来又被 Ben-Zvi–Nadler–Yun 在拓扑语境中重新发现。2024 年的证明，本质上是把（i）（ii）放进（iii）提供的正确范畴里互相对撞。

### 2.3 这份讲义在今天的位置

2005 年时，它大概是唯一一篇把二维 CFT 与几何 Langlands 系统连起来的长篇讲义：既讲 Langlands 对应的函数域原型，也讲 Beilinson–Drinfeld 的 Kac–Moody 局部化如何从 CFT 造出 Hecke 特征层。2024 年之后，它的双重身份更清楚了：

- 作为**历史文献**，它记录了几何 Langlands 猜想被精确表述之前的物理学直觉，也记录了 CFT 路线在证明完成前近二十年就被认真对待的事实；
- 作为**入口**，它仍是「物理学家想懂几何 Langlands」时被推荐的第一批文本之一（§1.2 的引用证据）。

对译注本来说，这意味着注释的重点不该是「纠正 2005 年的说法」，而是标出哪些说法后来被精化、哪些直觉后来被证明。前者需要 2012 年与 2024 年的文献作对照，后者需要 §2.2 的路线图作背景——两者都可以做成脚注，而不必改动译文正文。

## 三、对译注工作的几点建议

1. 术语表宜并列「2005 年用法」与「今日通行表述」，例如 Hecke 特征层与「带幂零奇异支撑的 ind-coherent sheaf」之间的对应关系。
2. 凡讲义把某事称为「猜想」，译注应加脚注，说明其 2012 年后的精确形式与 2024 年后的定理地位。
3. §1.4 的三点疑难可直接做成「时代错位」提示框。
4. 定位上可以放心写：这份讲义是「物理学家进入几何 Langlands 的标准入口」兼「CFT 路线的标准综述」——两点都有硬证据（摘要自述、Witten/KW/Teschner 的引用）。
5. 建议附一张「延伸阅读」表：本讲义相关章节 → 2012 年后的精确表述 → 2024 年证明的对应论文，让愿意深入的读者能顺着读下去。§2 的年表可以直接改写成这张表的骨架。
6. 引用统计（111 次）与「被反复称为 review」这一点，可在译者前言里用一句话交代，用来解释为什么这份讲义值得整本翻译，而不是只译其中的数学部分。

## 四、来源清单

- 讲义本身：<https://arxiv.org/abs/hep-th/0512172>；作者主页 PDF <https://math.berkeley.edu/~frenkel/houches.pdf>；INSPIRE 元数据 <https://inspirehep.net/api/arxiv/hep-th/0512172>；AIM 分节 HTML <https://sl2x.aimath.org/development/collectedworks/htmlpaper/hep-th_0512172/theindex.html>
- 引用上下文汇总：<https://api.semanticscholar.org/graph/v1/paper/arXiv:hep-th/0512172/citations?fields=title,year,authors,contexts&limit=100>
- Langlands 2012：<https://doi.org/10.2140/PJM.2012.260.583>｜Witten 2015：<https://arxiv.org/abs/1506.04293>｜Teschner 2017：<https://arxiv.org/abs/1707.07873>｜Balasubramanian–Teschner 2017：<https://arxiv.org/abs/1702.06499>｜Abedin–Felder–Windesheim 2025：<https://arxiv.org/abs/2509.02368>｜Aganagic–Frenkel–Okounkov 2017：<https://arxiv.org/abs/1701.03146>｜Candelas 等 2024：<https://arxiv.org/abs/2410.07107>｜Elliott–Yoo 2020：<https://arxiv.org/abs/2008.10988>｜Khan–Zeng 2025：<https://arxiv.org/abs/2502.13227>｜Weatherall：<https://doi.org/10.1086/710630>
- 课程与讲义页：<https://www.math.ucla.edu/~rouquier/langlands.html>｜<https://web.ma.utexas.edu/users/benzvi/Langlands.html>
- 问答与博客：<https://mathoverflow.net/questions/300985>｜<https://mathoverflow.net/questions/100977>｜<https://mathoverflow.net/questions/481662>｜<https://www.math.columbia.edu/~woit/wordpress/?p=624>｜<https://physics.stackexchange.com/questions/27370>
- 2005 年后文献：KW <https://arxiv.org/abs/hep-th/0604151>；Ngô <https://arxiv.org/abs/0801.0446>；Arinkin–Gaitsgory <https://arxiv.org/abs/1201.6343>；Fargues–Scholze overview <https://arxiv.org/abs/1602.00999> 与正文 <https://arxiv.org/abs/2102.13459>；GLC 五篇 <https://people.mpim-bonn.mpg.de/gaitsgde/GLC/>；IHES 公告 <https://www.ihes.fr/en/gaitsgory-glc/>；相对 Langlands <https://arxiv.org/abs/2409.04677>
