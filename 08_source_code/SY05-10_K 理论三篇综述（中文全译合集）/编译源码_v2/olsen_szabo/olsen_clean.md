



**摘要**

本文详细综述了超弦理论中 D-膜拓扑分类的近期进展。文章首先对拓扑 K-理论的技术与应用作了一个完整而自足的介绍，随后描述了 K-理论的经典构造与近期把 D-膜实现为快子孤子的做法之间的联系——后者来自高维不稳定膜系统（即不稳定膜的束缚态）的构造。文中说明 K-理论形式体系如何自然地重现已知的 BPS 与非 BPS D-膜谱，以及如何系统地用它来预言新状态的存在。重点在于对 D-膜的若干新解释：把它们看作其他膜世界体上的传统拓扑孤子；数学形式体系如何被用来推导超对称膜与非 BPS 膜上的规范场内容；以及 K-理论如何预言各超弦理论之间及其 D-膜谱之间的新关系。文中还讨论了对偶对称性作为 K-群的自然同构的实现，介绍了与标准上同调分类的关系并用之导出 D-膜荷的显式公式，此外还简要描述了 K-理论预言的某些弦论构造。

## 引言与概述

第二次超弦革命（综述参见 [Mrev]）伴随着如下认识而来：十维中所有五个自洽的超弦理论（Type I、Type IIA/B、杂化 $SO(32)$/$E_8 \times E_8$）连同十一维超引力，都只不过是一个被称为 M-理论的单一十一维量子理论的不同微扰展开 [wittenM]。其证据来自各种非微扰对偶关系，这些关系把 M-理论模空间中对应于各个不同弦理论的不同角落彼此联系起来。经典的例子是 Type IIB 超弦的自对偶性 [schwarz]，以及 Type I 与 $SO(32)$ 杂化弦之间的对偶性 [wittenM,polwitten]。

对偶猜想的新的推动力来自如下认识：某些非微扰自由度，即所谓的 Dirichlet $p$-膜（简称 D$p$-膜），带有 Type II 超弦理论中关闭弦 Ramond-Ramond（RR）扇区的 $p+1$-形式规范势的荷 [polchinski]。D$p$-膜是超对称的延展客体，它们在时空中构成 $p+1$ 维超曲面，开弦的端点可以附着于其上（并满足 Dirichlet 边界条件）。可以把它们看成时空中的拓扑缺陷，它们给出了弦孤子的显式实现 [duffrev]。关键的观察 [polchinski] 是：D-膜所具有的性质恰好足以补全对偶多重态，而这些多重态的其他成员是基本弦态与普通的场论孤子。D-膜由此为弦对偶性提供了一幅更完整、更细致的动力学图景。它们还为黑洞量子力学以及极短距离尺度下时空的本性提供了令人惊讶的新洞见。

D-膜的一个重要性质是：它们是 BPS 态的例子，而 BPS 态的特征在于其质量完全由它相对于某个规范场的荷所决定。它们构成弦理论超对称代数的超短多重态，因而稳定并受到保护，不受量子辐射修正的影响。因此，它们的性质可以在弱耦合下于给定理论中作微扰分析，然后再外推到强耦合；在强耦合下它们可被重新解释为对偶理论的非微扰位形。曾有一段时间人们认为，正是这种通过非重整化定理保护 D-膜位形的超对称性质，对于保证其稳定性、并提供对对偶猜想的恰当非微扰检验是至关重要的。

然而，在过去一年半里，这幅 D-膜的图景发生了剧烈的变化。人们注意到 [senbps]，超弦理论的谱中可以包含并不具有 BPS 性质、但仍然稳定的态，因为它们是该理论中携带某一组守恒量子数的最轻的态，而这些量子数阻止它们衰变。这类稳定的非 BPS 态可以用标准的弦微扰论来研究，其性质可在弱耦合下确定。最近人们认识到 [sentachyon]–[bg]：当把这些态外推到强耦合时，所得的非微扰位形在各方面都表现得像普通的 D-膜（近期综述参见 [senrev]）。这就在超出 BPS 位形层次上，为非微扰对偶猜想提供了一个高度非平凡的检验。例如，这一想法可以应用到非 BPS 层次的杂化弦-Type I 对偶性上 [seninst,senparticle]。$SO(32)$ 杂化弦包含一些并非超对称的态，但它们稳定，因为它们是携带 $SO(32)$ 规范群旋量表示量子数的最轻的态。结果表明，相应的、作为 $SO(32)$ 旋量的非微扰稳定位形，正是来自 Type I 的 D-弦与反 D-弦的束缚态（该束缚态缠绕在一个圆上，且世界体上带有一条取 ${\mathbb{Z}}_2$ 值的 Wilson 线）的那个客体。这对 D-弦紧密结合，形成一个孤子扭结，其行为完全像一个 D-粒子，但它携带一个取 ${\mathbb{Z}}_2$ 值的非可加荷，从而阻止人们堆叠出非 BPS D-膜。

一般来说，这种理解 D-膜及其守恒荷的新视角，把膜看作更高维的不稳定膜系统（例如膜-反膜对）的世界体中的拓扑缺陷。这类系统不稳定，是因为其谱中包含一个不被通常 GSO 投影去掉的快子态。然而，尚不清楚这些模式究竟是系统中无法治愈的不稳定性，还是在动力学中扮演着更微妙的角色。最近人们对弦论快子有了更好的理解 [senbps]–[seninst],[gbs]–[tachrecent]；新的看法是：在 D-膜与反 D-膜之间伸展（或把不稳定膜与其自身连接起来）的开弦的快子模式是一种 Higgs 型激发，它会发展出稳定的真空期望值，于是不稳定态衰变到稳定态。不稳定 D-膜的位形有时可以携带更低维的 D-膜荷，因此当快子场滚到其势的极小值、该态发生衰变时，它留下的态与真空位形相差一个更低维的 D-膜荷。于是所得的稳定态就包含了对应于稳定 D-膜的拓扑缺陷。

除了产生新的 D-膜位形之外，通过快子凝聚过程来构造膜的束缚态这一做法，也可以对已知的超对称膜谱实施。这导致不同类型的 D-膜之间出现各种新的联系，即所谓的“降维关系”[sendescent],[witten]–[os]。这些关系构成了一张由 BPS 膜与非 BPS 膜之间映射组成的非凡网络，提供了思考 D-膜起源的多种不同方式，并可能带来对各类 D-膜动力学及其在弦论与 M-理论中作用的更好理解。Type II 超弦理论的情形如图 1 所示 [sendescent,senrev]。如果我们考虑 Type IIB 弦理论（$p$ 为奇数）中的一个 D$p$-膜与反 D$p$-膜（简称 D$\overline{p}$-膜）束缚态对，那么其开弦谱包含一个快子激发，其基态对应于超对称真空位形。然而，人们也可以考虑膜-反膜对上的快子扭结解，它描述 IIB 理论的一个非 BPS D$(p-1)$-膜。这个系统的世界体场论中同样包含一个快子激发，因此可以考虑该 D$(p-1)$-膜上的快子扭结解，它给出 IIB 的一个 BPS D$(p-2)$-膜。



FIGPLACEHOLDER1



另一组关系来自用算符 ${(-1)^{F_{\mathrm L}}}$ 对 $p$-$\overline{p}$ 膜对取商，该算符在基本弦世界面的左行部分对所有 Ramond 扇区态作用为 $-1$，而让所有其他扇区保持不变。特别地，它把 D-膜与其反膜互换，因此膜-反膜对在 ${(-1)^{F_{\mathrm L}}}$ 下不变，取该位形的商是有意义的。对开弦谱的细致研究表明，其结果是一个 IIA 的非超对称 D$p$-膜，而再用 ${(-1)^{F_{\mathrm L}}}$ 取一次商则给出 IIB 的一个超对称 $p$-膜 [sendescent,daspark]。当与 Type IIB 和 IIA 理论之间通常的 $T$-对偶变换 [Tduality] 结合起来时，我们发现 Type II 超弦理论中任何 $p$-膜位形都可以由任何更高维的膜位形得到。特别地，Type II 理论的所有膜都从一个 D9-D$\overline{9}$ 对的束缚态降维而来。于是所有可能的稳定 D-膜都表现为充满时空的 D9-膜上世界体快子 Higgs 场的拓扑缺陷，从而这个充满时空的膜系统提供了一个普适的介质，在其中所有稳定 D-膜荷都由传统的拓扑孤子携带。

Type II 超弦理论中一个 BPS D$p$-膜与关闭弦 $p+1$-形式 RR 势 $C^{(p+1)}$ 的标准耦合由作用量 [polchinski] 描述：

$$
S_{(p)}=\mu_{(p)}\int\limits_{{\mathcal M}_p}C^{(p+1)}
$$

其中 $\mu_{(p)}$ 是 $p$-膜的 $p+1$-形式荷。此外，D$p$-膜世界体流形 ${\mathcal M}_p$ 上的拓扑荷通过推广的 Wess-Zumino 型作用量与时空 RR 场耦合 [li,douglasinst]（这里我们采用 $2\pi\alpha'=1$ 的弦单位，并略去对 Neveu-Schwarz 二形式场 $B$ 以及对由非零流形曲率引起的修正项的依赖）：

$$
S_{\mathrm WZ}^{(p)}=\mu_{(p)}\int\limits_{{\mathcal M}_p}\mathrm{tr}\left(\mbox{e}^F\right)\wedge\sum_{p'} C^{(p'+1)}
$$

其中 $F$ 是某个生活在 ${\mathcal M}_p$ 上的规范场的场强。这些规范场的性质取决于 D-膜的位形。当 $N$ 个膜被无限靠近彼此时，它们一般的 $U(1)^N$ 规范对称性被增强为 $G=U(N)$ [wittenp]。这就带来了把各种维数的超对称规范理论嵌入弦论的可能性（综述参见 [gaugerev]）。耦合（式）还允许对拓扑荷作另一种解释，即把它看作由于高维膜世界体中存在低维膜而产生的 RR 荷 [douglasinst,strom]。这使得人们可以按照世界体缺陷对 RR 荷作拓扑分类 [semz]，其精神与上文所述十分相似。

事实上，把不稳定膜位形中的快子重新理解为开弦态谱中的 Higgs 型激发，这导致当把 D-膜视为快子孤子时对所得膜荷的拓扑分类。一般来说，这些客体的拓扑荷由齐性空间 $G/H$ 的同伦群决定，其中 $G$ 是紧 Lie 群，$H$ 是 $G$ 的闭子群。纤维化

$$
H~\stackrel{i}{\hookrightarrow}~G~\stackrel{\pi}{\longrightarrow}~G/H
$$

（其中 $i$ 是包含映射、$\pi$ 是典范投影）诱导出同伦群的长正合序列

$$
\dots~\longrightarrow~\pi_{n-1}(H)~{\stackrel{i^*}{\longrightarrow}}~
\pi_{n-1}(G)~{\stackrel{\pi^*}{\longrightarrow}}~\pi_{n-1}(G/H)~{\stackrel{\partial^*}{\longrightarrow}}~\pi_{n-2}(H)~\longrightarrow~\dots \ .
$$

在当前情形下，$G$ 是给定膜位形的世界体规范群，而快子标量场 $T$ 是把规范对称性破缺到子群 $H$ 的 Higgs 场。快子孤子必须伴随一个相应的、位于规范群未破缺子群中的世界体规范场 $A$，其拓扑荷与之相配，才能使得所诱导的低维膜的单位世界体能量有限。可以论证 [senbps,seninst]，膜世界体场论容许有限能量的静态孤子解，这些解在无穷远处具有渐近的纯规范位形：

$$
T\simeq T_v\,U~~~~~~,~~~~~~A\simeq i\,U^{-1}\,dU
$$

其中 $T_v$ 是常数，$U$ 是取值于 $G/H$ 的函数，对应于从世界体孤子的渐近边界到真空空间 $G/H$ 的群流形的恒等映射（具有给定的缠绕数）。这导致所有场位形构成的空间中出现拓扑上不同的扇区，而区分这些扇区的荷取值于真空流形的相应同伦群中。确切地说，如果所诱导的膜位形在更高维世界体中具有余维 $n$，则相应的孤子携带取值于 $\pi_{n-1}(G/H)$ 的拓扑荷。这个同伦群可以用正合序列（式）来计算 [semz]（例如，若所诱导的边界同态 $\partial^*$ 是平凡映射，从而 $\ker\partial^*=\pi_{n-1}(G/H)$，则 $\pi_{n-1}(G/H)=\pi_{n-1}(G)/\pi_{n-1}(H)$）。

耦合（式）似乎意味着：既然无质量 RR 场 $C^{(p+1)}$ 是微分形式，D-膜的 RR 荷就由上同调类决定，即由把 $C^{(p+1)}$ 在时空流形 $X$ 的适当闭链上积分来决定。然而，把 D-膜荷解释为拓扑荷的新观点实际上提示了一种不同的刻画（至少在所有时空维数都远大于弦标度、从而不会出现新的弦论现象时是如此）。让我们考虑 Type IIB 超弦理论，并回到用 $N$ 个 9-膜与 $M$ 个 $\overline{9}$-膜的位形来实现 RR 荷这一做法。Type II 理论没有规范群，因此为了抵消蝌蚪（tadpole）反常，9-膜与 $\overline{9}$-膜的数目必须相同，$N=M$。9-膜与 $\overline{9}$-膜充满时空流形 $X$。$N$ 个 9-膜的系统携带一个 $U(N)$ 规范丛 $E$，$N$ 个 $\overline{9}$-膜的系统携带一个 $U(N)$ 规范丛 $F$。因此 $9-\overline{9}$-膜系统可以由一对 $U(N)$ 向量丛 $(E,F)$ 来标记，它们刻画了对应于该孤子的规范场位形。

现在我们要确定，两对这样的丛 $(E,F)$ 与 $(E',F')$ 在什么时候应被视为等价。如果它们确定孤子的同一个拓扑类，就应当被视为相同。结果表明，基本的等价关系是膜-反膜对的产生与湮灭。$9-\overline{9}$ 与 $\overline{9}-9$ 开弦具有相反的 GSO 投影，因此无质量矢量场被投影掉，而快子模式存活下来 [gbs]。如上文所讨论的，人们猜测与快子相关的不稳定性代表着朝膜-反膜对湮灭方向的流动，也就是说，通过给快子场一个合适的期望值，人们可以回到没有这对膜的真空态 [senbps]–[seninst]。于是，如果我们添加同样数目 $M$ 的 9-膜与 $\overline{9}$-膜，并在它们上面带有相同的 $U(M)$ 规范丛 $H$，那么与伸展在 9-膜和 $\overline{9}$-膜之间的开弦相联系的快子场是一个平凡丛的截面，因此它可以在 $9-\overline{9}$ 世界体上处处凝聚到其势的极小值。我们假定任何这样的膜-反膜对的集合都可以被产生和湮灭，从而该位形等价于不携带任何 D-膜荷的真空（这很像普通量子场论中的情形）。我们得出结论：添加这样的对不会影响孤子的拓扑类，即对任何这样的丛 $H$，对 $(E,F)$ 都可以光滑地形变到对 $(E\oplus H,F\oplus H)$。因此，就守恒的 D-膜荷——系统在光滑形变下不变的一个性质——而言，我们得出结论：RR 荷的拓扑分类方式是给定一对 $U(N)$ 向量丛 $(E,F)$，并服从等价关系

$$
(E,F)\sim(E\oplus H,F\oplus H)
$$

其中 $H$ 是任意 $U(M)$ 向量丛。可以说（这一点很快就会说清楚），D-膜荷由 9-膜与反 9-膜上 Chan-Paton 规范丛之间的“差”所决定。

上述数学条件定义了时空 $X$ 所谓的 K-理论群 ${\mathrm K}(X)$。D-膜荷取值于时空的 K-理论这一提议最初是在 [witten] 中提出的，随后在 [horava,os],[garcia]–[vancea] 中得到推广。然而，上文讨论的 D-膜态孤子描述并不是 RR 荷应当用 K-理论而非上同调来理解的最早证据。此前最有力的提议 [minmoore] 是一个观察（它推广了 [li,douglasinst,strom,cheung] 中较早的计算）：当一个 D-膜缠绕时空的子流形 $Y$ 时，它的 RR 荷依赖于 $Y$ 的几何、其法丛的几何以及 $Y$ 上的规范场，其方式提示 D-膜荷取值于 ${\mathrm K}(X)$。与 K-理论有关的其他较早线索可见于 [horavaeq,quivers]。

上文针对充满时空的膜所给出的论证清楚表明：当一个 D-膜缠绕时空 $X$ 的子流形 $Y$ 时，它的荷由群 ${\mathrm K}(Y)$ 分类。[witten] 的深刻观察之一是：存在一个标准的 K-理论构造，称为 Thom 同构，它把 ${\mathrm K}(Y)$ 嵌入 ${\mathrm K}(X)$，并且等价于上文描述的 D-膜的束缚态构造，从而等价于用 9-膜与反膜来表示所有膜。这样，人们就得到了用底层时空流形的拓扑对 D-膜荷的完整分类。K-理论中与上述孤子构造平行的主要特征，是它与同伦理论的密切关系。此外，另一个标准的 K-理论构造，即所谓的 Atiyah-Bott-Shapiro 构造，可用来获得生活在给定 D-膜上的经典规范场位形的显式形式。这些非凡的事实已被用来重现 [seninst] 中发现的 Type I 非 BPS D-粒子的构造，并预言 Type I 理论谱中以及另一些超弦理论谱中新 D-膜的存在（Type I D-弦的同伦孤子构造最早是在 [dufflu] 中给出的）。确实，时空的 K-群可以比相应的上同调群一般得多。在许多情形下，K-群可以有挠而相应的上同调群无挠，这就为某些 D-膜（例如 Type I 的 0-膜）携带挠荷这一事实提供了自然的解释 [minmoore]。近期对这些新的 Type I 客体的弦论构造 [frau] 展示了 K-理论形式体系所能引出的强预言。此外，对于超对称 D-膜的谱（其 RR 荷取整数值），存在一个到上同调的映射，称为 Chern 同态，从而与由耦合（式）到时空 RR 场所得出的预期建立了联系。


### 提纲

在本文中我们将综述拓扑 K-理论的数学形式体系，以及它作为超弦理论中 D-膜拓扑分类之系统工具的应用。就 K-理论在弦论中的应用而言，它如今正处于数学物理的前沿；而尽管上同调与微分几何对大多数理论物理学家来说已相当熟悉，K-理论或许仍显得颇为晦涩，因此我们试图把数学与物理融合在一起，使 K-理论作为分类工具的自然性一目了然。主要目的是把所有相关的数学材料汇集于一处，其表述方式应当能为相当广泛的弦论学家与数学家读者群所接受。本综述的水准定位于：具有较好代数拓扑与微分几何背景（达到 [文献] 一书与 [文献] 综述文章的水平）的弦论学家，以及具有弦论初步背景（达到 [文献] 一书的水平）的数学家。更多的参考文献与背景将在行文中给出。

在简要勾勒本文结构之前，让我们先指出本综述中的若干省略之处，它们也可被视为进一步研究的方向。在整个综述中，我们只考虑 Neveu-Schwarz $B$-场的曲率在上同调意义下为平凡的超弦紧化。把这一二形式场纳入框架所引起的问题在 [文献] 中已有讨论，而目前对于这些情形下究竟应当采用何种适当的 K-理论尚未完全理解。近期 [文献] 中已出现朝这一方向的一些进展。与此问题相关的是如何正确地把 $S$-对偶纳入 K-理论的表述，特别是 Type IIB 超弦理论自对偶性的描述。[文献] 的分析是朝这一方向的第一步。另一个相关方面是与 M-理论的正确构造建立联系。M-膜的描述已在 [文献] 中讨论，而 Matrix Theory 中的相应关系见 [文献]。采用 [文献] 中基于{\it 代数} K-理论的方法，可能与 [文献] 中基于非交换几何的 Matrix Theory 紧化所用规范丛有密切关联。这些问题迄今都还没有以 K-理论表述的自然描述。我们希望本文的阐述除了为读者提供进一步钻研该主题所需的工具之外，还能引发对此类问题的细致探讨。最后我们指出，下文中给出的分析仅意在对各种弦论中膜的谱作拓扑分类。第二步——本综述不予涉及——是实际执行 K-理论形式体系所预言的 D-膜的弦论构造，从而描述其动力学，尤其是对于新的非 BPS 态。这在 [文献]--[文献],[文献] 中有所论述。的确，D-膜的 K-理论分类已揭示了弦论中许多有趣的新效应与新构造。为使表述尽可能自足，我们在此只简要提及此类内容。

本综述的结构如下。在第 2 节中，我们对拓扑 K-理论的思想与基本构造作详尽而自足的介绍。这一节处理的是后续各节将要用到的形式体系中的数学要点。文中描述了许多计算 K-群的工具，它们对我们将要讨论的各种超弦应用尤为有用。此外，这些工具还将给出各种不同超弦理论之间许多出人意料的联系。此处假定读者具备良好的代数拓扑与纤维丛理论基础。在第 3 节中我们开始用 K-理论对 D-膜作分类，从最简单的 Type IIB 超弦理论情形入手。我们先简要描述膜-反膜对的相关物理。更多细节请读者参阅原始论文 [文献]--[文献] 以及近期综述 [文献]。随后我们描述束缚态构造，以及它如何自然地导致与 K-理论的相应联系，这部分大体上遵循 [文献]。在第 4 节中我们对 Type IIA 超弦理论执行类似的构造。Type IIA D-膜的相关 K-理论由 [文献] 提出，并在 [文献] 中得到详细发展。在第 5 节中我们转向 Type I 超弦理论，其中预言了新的非 BPS D-膜，同样在很大程度上遵循 [文献]。在第 6 节中我们把注意力转向 orbifold 与 orientifold 超弦理论。Orbifold 在 [文献] 中处理，而 orientifold 在 [文献] 中描述。Type I 理论的各种 $T$-对偶 orientifold 在 [文献] 中讨论。最后，我们在第 7 节中结束分析，描述当把时空与世界体嵌入的整体拓扑考虑在内时所引起的对前述构造的修正。这里我们给出束缚态构造的整体版本，如 [文献] 所述，并强调与先前平坦流形情形相比必须考虑的额外结构以及须加留意之处。接着我们描述适用于一般超弦紧化的适当 K-理论 [文献]，并引入与 Dirac 算子指标理论的有用联系——后者一直处在理论物理许多应用的前沿（全面综述见 [文献]）。随后我们应用这些想法来描述 D-膜著名的 $T$-对偶变换如何被表示为 K-群的自然同构 [文献]。我们以可视为本文所讨论材料之来源的 [文献] 的 K-理论荷公式的推导来结束本综述。该公式给出了 RR 荷的 K-理论与上同调描述之间的显式关系，从而使人能够用在时空流形上积分的密度显式计算 D-膜荷。

## 拓扑 K-理论的基本要素

K-理论最初由 Grothendieck 于 1950 年代在 Riemann-Roch 定理的一种替代表述中引入（见 [文献]）。随后在 1960 年代由 Atiyah 与 Hirzebruch 发展，他们首次引入了拓扑空间 $X$ 的一般 K-理论群 ${\mathrm K}(X)$ [文献]。此后，K-理论已成为拓扑学、微分几何与代数学许多领域不可或缺的工具。一般而言，拓扑 K-理论可视为向量丛的上同调理论，它强调的是当向量丛的秩变大时变得突出的那些特征。事实上，它是{\it 广义}上同调理论的一个例子，因为 K-理论并不满足上同调理论的全部 Eilenberg-Steenrod 公理 [文献]（它满足除维数公理以外的全部公理，而维数公理事先定义了由单点构成的拓扑空间的上同调，例如 $H^n({\mathrm pt}, {\mathbb{Z}})=\delta^[n,0]\,{\mathbb{Z}}$）。这一篇幅颇长的节将综述我们后文所需的数学材料的核心，在第 3 节之前不会提及物理。我们不会给出材料的完整综述，而只聚焦于那些在超弦应用中有所用的方面。关于本主题更完整的阐述，读者可参阅 [文献]--[文献] 这些著作，下文所引定理的证明也可在其中找到。

### Grothendieck 群

在本小节中我们将从一个抽象的表述出发，它将自然地导致群 ${\mathrm K}(X)$ 的定义。尽管这一形式体系对该定义并非真正必需，但它日后会派上用场；而且正是这一表述使人能够把拓扑空间的 K-理论推广到更奇特的群，例如向量空间、$C^*$-代数等的 K-理论，这些在 K-理论一般形式体系未来对弦论与 M-理论的应用中可能证明是重要的。设 ${\mathcal A}$ 为一个交换幺半群，即一个带有加法的集合，它满足群的全部公理，唯一可能的例外是逆元的存在性。人们可以通过如下构造自然地联系到 ${\mathcal A}$ 的一个交换群 $S({\mathcal A})$。考虑笛卡尔积幺半群 ${\mathcal A}\times{\mathcal A}$ 上的等价关系 $\sim$：若存在元素 $G\in {\mathcal A}$ 使得

$$
E+F'+G=F+E'+G\ .
$$

则称 $(E,F)\sim (E', F')$。于是交换群 $S({\mathcal A})$——称为 ${\mathcal A}$ 的{\it 对称化}——被定义为这类对子的等价类的集合：

$$
S({\mathcal A})={\mathcal A}\times{\mathcal A}/\sim\ .
$$

对子 $(E,F)$ 的等价类记作 $[(E,F)]$，而该元素在 $S({\mathcal A})$ 中的逆为 $[(F,E)]$。这源于如下事实：对任意 $E\in {\mathcal A}$，$[(E,E)]$ 是 $S({\mathcal A})$ 中零元素的代表。$S({\mathcal A})$ 的另一种定义是在 ${\mathcal A}\times{\mathcal A}$ 中使用等价关系：若存在 $G,H\in{\mathcal A}$ 使得

$$
(E,F)+(G,G)=(E',F')+(H,H)\ .
$$

则称 $(E,F)\sim (E',F')$。作为一个简单例子，对 ${\mathcal A}={\mathbb{Z}}^+$（加法下的非负整数），有 $S({\mathcal A})={\mathbb{Z}}$。又对 ${\mathcal A}={\mathbb{Z}}-\{0\}$（乘法下的交换幺半群），有 $S({\mathcal A})={\mathbb{Q}} -\{0\}$。

幺半群 ${\mathcal A}$ 的完备化 $S({\mathcal A})$ 可由如下泛性质刻画。对任意交换群 $\mathcal G$，以及底层幺半群的任意同态 $f:{\mathcal A}\to{\mathcal G}$，存在唯一的同态 $\tilde{f}:S({\mathcal A})\to\mathcal G$ 使得 $\tilde{f}\circ s=f$，其中 $s$ 是由 $s(E)=[(E,0)]$ 定义的自然映射 ${\mathcal A}\rightarrow S({\mathcal A})$。这意味着 $S({\mathcal A})$ 是由交换幺半群 ${\mathcal A}$ 所能构造出的“最小”交换群，并特别地蕴含：若 $\mathcal A$ 本身是群，则 $S({\mathcal A})=\mathcal A$。一般而言，这一性质蕴含映射 ${\mathcal A}\rightarrow S({\mathcal A})$ 是从交换幺半群范畴到交换群范畴的共变函子，即若 $\gamma: {\mathcal A}\rightarrow {\mathcal B}$ 是幺半群的任意同态，则存在唯一的群同态 $s(\gamma):S({\mathcal A})\rightarrow S({\mathcal B})$ 使得下图交换：

$$
{\begin{array}{ccc}
{\mathcal A}&\stackrel{\gamma}{\longrightarrow}&{\mathcal B}\\&
&\\{\scriptstyle s}\downarrow& &\downarrow{\scriptstyle s}\\&
&\\S({\mathcal A})&\stackrel{s(\gamma)}{\longrightarrow}&S({\mathcal B})\end{array}}
$$

并且满足 $s(\gamma\circ\gamma')=s(\gamma)\circ s(\gamma')$，$s({\mathrm Id}_{{\mathcal A}})={\mathrm Id}_{S({\mathcal A})}$（这里 ${\mathrm Id}_{\mathcal A}$ 表示 ${\mathcal A}$ 上的恒等态射）。

这一构造的一个重要应用例子是：${\mathcal C}$ 为加法范畴，$\Phi({\mathcal C})$ 为元素 $E\in{\mathcal C}$ 的同构类的集合，我们将其记作 $[E]$。若定义 $[E]+[F]\equiv [E\oplus F]$（这是良定义的，因为 $E\oplus F$ 的同构类只依赖于 $E$ 与 $F$ 的同构类），则 $\Phi({\mathcal C})$ 成为交换幺半群。${\mathcal C}$ 的{\it Grothendieck 群}定义为 ${\mathrm K}({\mathcal C})=S(\Phi({\mathcal C}))$。注意 ${\mathrm K}({\mathcal C})$ 的每个元素都可写成形式差 $[E]-[F]$，且 ${\mathrm K}({\mathcal C})$ 中 $[E]-[F]=[E']-[F']$ 当且仅当存在 $G\in{\mathcal C}$ 使得 $E\oplus F'\oplus G \cong E'\oplus F\oplus G$。还要注意 $[E]=[F]$ 当且仅当存在 $G\in{\mathcal C}$ 使得 $E\oplus G \cong F \oplus G$。作为一个简单例子，设 ${\mathbb{F}}$ 为代数域（例如 ${\mathbb{F}}={\mathbb{R}}$ 或 ${\mathbb{C}}$），并设 ${\mathcal C}$ 为 ${\mathbb{F}}$ 上有限维向量空间的范畴，其态射为线性变换。于是，由于这类有限维向量空间由其维数唯一刻画，$\Phi({\mathcal C})={\mathbb{Z}}^+$，从而 ${\mathrm K}({\mathcal C})={\mathbb{Z}}$。

### 群 ${\mathrm K}(X)$

我们将把上一小节的构造用于紧流形上向量丛的分类。设 $X$ 为紧流形，${\mathcal C}={\mathrm Vect}(X)$ 为 $X$ 上复向量丛关于丛态射与 Whitney 和的加法范畴（后文我们还将考虑实与四元数向量丛）。定义 $I^k$ 为 $X$ 上秩为 $k$ 的平凡丛，即 $I^k\cong X\times {\mathbb{C}}^k$。全体向量丛的空间可如下划分为等价类。若存在正整数 $j,k$ 使得

$$
E\oplus I^j\cong F\oplus I^k\ ,
$$

则称 $X$ 上的丛 $E$ 与丛 $F$ {\it 稳定等价}，记作 $E\sim F$。${\mathrm Vect}(X)/\sim$ 中相应的等价类称为稳定等价类。容易看出，若 $E,F$ 与 $G$ 是 $X$ 上的向量丛，则

$$
E\oplus G\cong F\oplus G ~~~~\Rightarrow E\sim F\ ,
$$

即 $E$ 与 $F$ 稳定等价。证明中用到如下事实：存在丛 $G'$ 使得 $G\oplus G'$ 平凡（按 Swan 定理，这要求 $X$ 是紧 Hausdorff 流形）。然而，不能由（上式）的左端推出 $E$ 与 $F$ 作为向量丛同构。例如，取 $E=T{\mathbf S}^n$，即 $n$-球面 ${\mathbf S}^n$ 的切丛，以及 $G=N({\mathbf S}^n,{\mathbb{R}}^{n+1})$，即 ${\mathbf S}^n$ 在 ${\mathbb{R}}^{n+1}$ 中的法丛。$G$ 有一个由外向单位法向量给出的整体截面，这蕴含它是平凡的，$N({\mathbf S}^n,{\mathbb{R}}^{n+1})\cong I^1$。此外我们有通常的关系

$$
I^{n+1}\cong T{\mathbb{R}}^{n+1}\cong E\oplus G\cong E\oplus I^1\ .
$$

然而 $E=T{\mathbf S}^n$ 一般并不平凡，因此不等于 $I^n$（事实上 $T{\mathbf S}^n$ 只在可平行化球面对应的 $n=1,3,7$ 情形下平凡）。所以一般而言，$T{\mathbf S}^n$ 只是稳定平凡的。

这个例子表明，$X$ 上向量丛的空间在 Whitney 和下不是群，而只是幺半群，因为对向量丛没有定义减法。利用前述设置可如下构造一个群。紧流形 $X$ 的{\it K-群}定义为范畴 ${\mathrm Vect}(X)$ 的 Grothendieck 群，${\mathrm K}(X)\equiv {\mathrm K}({\mathrm Vect}(X))$，或

$$
{\mathrm K}(X)={\mathrm Vect}(X)\times {\mathrm Vect}(X)/\sim\ ,
$$

其中我们在 ${\mathrm Vect}(X)\times {\mathrm Vect}(X)$ 中按如下方式定义了等价关系：若存在向量丛 $G\in {\mathrm Vect}(X)$ 使得

$$
E\oplus F' \oplus G \cong E' \oplus F \oplus G\ ,
$$

则 $(E,F)\sim (E',F')$。${\mathrm K}(X)$ 的一个等价定义是：对任意丛 $H$，丛对 $(E,F)$ 被视为等价于 $(E\oplus H,F\oplus H)$。该群也常常使用记号 ${\mathrm K}^0(X)$ 或 ${\mathrm KU}(X)$。${\mathrm K}(X)$ 的元素写作 $[(E,F)]$。在 ${\mathrm K}(X)$ 中单位（零）元素是 $[(E,E)]$，因此类 $[(E,F)]$ 的逆是 $[(F,E)]$。于是任何元素 $[(E,F)]$ 都可等同于 $[E]-[F]$，其中 $[E]=[(E,I^n)]$。此外，${\mathrm K}(X)$ 中 $[E]=[F]$ 当且仅当 $E$ 与 $F$ 稳定等价。${\mathrm K}(X)$ 的元素称为{\it 虚丛}。映射 $X\rightarrow {\mathrm K}(X)$ 是从紧拓扑空间范畴到交换群范畴的反变函子，即若 $f:X\rightarrow Y$ 连续，则它诱导 $Y$ 上向量丛的通常拉回映射，从而诱导映射 $f^*:{\mathrm Vect}(Y)\rightarrow {\mathrm Vect}(X)$，进而给出同态 ${\mathrm K}(Y)\rightarrow{\mathrm K}(X)$。

K-群具有如下重要的同伦不变性质。考虑两个同伦的映射 $f,g: X\rightarrow Y$。则对任意向量丛 $E\rightarrow Y$，存在 $X$ 上向量丛的同构：

$$
f^*E\cong g^*E\ .
$$

由此可得 $f$ 与 $g$ 在 K-群上诱导的映射相同：

$$
s(f)=s(g):{\mathrm K}(Y)\longrightarrow {\mathrm K}(X)\ .
$$

例如，若 $X$ 是可缩为一点的紧流形，则可推得 ${\mathrm K}(X)={\mathrm K}({\mathrm pt})= {\mathbb{Z}}$。从几何上看，这表达了众所周知的事实：可缩空间 $X$ 上的任何向量丛必然平凡，因而 $X$ 相应的 K-理论也平凡。

### 约化 K-理论

一点上的向量丛只是一个向量空间，因此 ${\mathrm K}({\mathrm pt})={\mathbb{Z}}$，这一事实促使我们引入约化 K-理论：在其中由单点构成的拓扑空间具有平凡上同调，$\widetilde{{\mathrm K}}({\mathrm pt})=0$，从而对任何可缩空间 $X$ 也有 $\widetilde{{\mathrm K}}(X)=0$。让我们固定 $X$ 的一个基点，并考虑收缩映射与包含映射：

$$
p:X\longrightarrow {\mathrm pt}~~~~,~~~~i:{\mathrm pt}\hookrightarrow X\ .
$$

这些映射分别诱导相应 K-群的上满同态与单同态：

$$
p^*:{\mathrm K}({\mathrm pt})= {\mathbb{Z}}\longrightarrow {\mathrm K}(X)~~~~,~~~~i^*:
{\mathrm K}(X)\longrightarrow {\mathrm K}({\mathrm pt})= {\mathbb{Z}}\ .
$$

于是我们得到群的正合列：

$$
\begin{matrix}
0 &\longrightarrow {\mathbb{Z}}\stackrel{p^*}{\longrightarrow} {\mathrm K}(X)\longrightarrow \widetilde{{\mathrm K}}(X)\longrightarrow 0 \\
0 &\longrightarrow \widetilde{{\mathrm K}}(X)\longrightarrow {\mathrm K}(X)\stackrel{i^*}{\longrightarrow} {\mathbb{Z}}\longrightarrow 0\ .
\end{matrix}
$$

这些序列有标准的分裂，故同态 $i^*$ 是 $p^*$ 的左逆。映射 $i^*$ 的核，等价地映射 $p^*$ 的余核，称为{\it 约化 K-理论群}，记作 $\widetilde{{\mathrm K}}(X)$，

$$
\widetilde{{\mathrm K}}(X)= \ker i^*={\mathrm coker}\,p^*
$$

因此我们有基本分解

$$
{\mathrm K}(X)= {\mathbb{Z}}\oplus \widetilde{{\mathrm K}}(X)\ .
$$

给定向量丛 $E\rightarrow X$，令 $E_x$ 表示 $E$ 在 $x\in X$ 上的纤维。我们通过 $\mathrm{rk}(x)=\dim_{{\mathbb{C}}} E_{x}$ 定义{\it 秩函数} $\mathrm{rk}:X\rightarrow {\mathbb{Z}}^+$。由于 $E$ 局部平凡，秩函数是局部常值的，而 $X$ 上全体局部常值的 ${\mathbb{Z}}^+$ 值函数在逐点加法下构成一个交换幺半群 $H^0(X, {\mathbb{Z}}^+)$。映射 $\mathrm{rk}$ 自然延拓为群同态

$$
\begin{matrix}
\mathrm{rk}: {\mathrm K}(X)&\longrightarrow H^0(X,{\mathbb{Z}})\\
\mathrm{rk}\Bigl([E]-[F]\Bigr)&=\mathrm{rk}(E)-\mathrm{rk}(F)\ .
\end{matrix}
$$

整数（上式）称为 $[(E,F)]\in {\mathrm K}(X)$ 的{\it 虚拟维数}。令 ${\mathrm K}'(X)=\ker\,\mathrm{rk}$。则短正合列

$$
0\longrightarrow {\mathrm K}'(X)\longrightarrow {\mathrm K}(X)\stackrel{\mathrm{rk}}
{\longrightarrow}H^0(X,{\mathbb{Z}})\longrightarrow 0
$$

有标准的分裂（即 $\mathrm{rk}$ 有右逆），因此若 $X$ 连通，则 $H^0(X,{\mathbb{Z}})= {\mathbb{Z}}$，且

$$
\widetilde{{\mathrm K}}(X)= {\mathrm K}'(X)=\ker\,\mathrm{rk}\ .
$$

在此情形，$\widetilde{{\mathrm K}}(X)$ 是 ${\mathrm K}(X)$ 中虚拟维数为零的元素的子群（即由等秩向量丛对 $[(E,F)]$ 的等价类组成）。基本的例子是：对任意正整数 $n$，$\widetilde{{\mathrm K}}({\mathbf S}^{2n})={\mathbb{Z}}$ 以及 $\widetilde{{\mathrm K}}({\mathbf S}^{2n+1})=0$（这些群在第 2.7 节中计算）。注意秩函数（上式）自然地给出 $X$ 的第零 \v{C}ech 上同调群中的一个赋值 $\mathrm{ch}_0(E)$，它只依赖于向量丛 $E$ 在 ${\mathrm K}(X)$ 中的稳定等价类。这是 Chern 特征的首个基本例子，将在第 7.1 节中讨论。

对于后文各节所给出的 K-理论的物理应用，我们将主要在具有紧支集的 K-理论中工作。这意味着对每个类 $[(E,F)]$，存在映射 $T:E\to F$，它在某个开集 $U\subset X$ 之外是向量丛的同构，而 $U$ 的闭包 $\overline U$ 是紧的。这一条件自动蕴含 $E$ 与 $F$ 具有相同的秩，因此我们主要处理约化 K-群 $\widetilde{{\mathrm K}}(X)$。相应的虚丛于是可表示为

$$
\Bigl[(E\,,\,F)\Bigr]=\Bigl[(\ker T\,,\,{\mathrm coker}\,T)\Bigr]
$$

当 $X$ 非紧时，我们定义 ${\mathrm K}(X)=\widetilde{{\mathrm K}}(X^+)$，其中 $X^+$ 是 $X$ 的单点紧化。


### 高阶 K-理论与 Bott 周期性

从 ${\mathrm K}(X)$ 出发，有一种自然的方式来定义所谓的“高阶”K-群。这些群由一个正整数 $n=0,1,2,\ldots$ 标记，并按
$${\mathrm K}^{-n}(X)={\mathrm K}(\Sigma^nX)\ ,$$
来定义，其中 $\Sigma^nX\equiv{\mathbf S}^n\wedge X$ 是拓扑空间 $X$ 的第 $n$ 次约化悬挂（reduced suspension）。这里 $X\wedge Y= X\times Y/ (X\vee Y)$ 是 $X$ 与 $Y$ 的 smash 积，而 $X\vee Y$ 是它们的约化并（reduced join），即把两个空间中各取一个基点等同起来所得的不交并，它可以看作笛卡尔积 $X\times Y$ 的子空间 $X\times{\mathrm pt}\amalg{\mathrm pt}\times Y$。对于 $X={\mathbf S}^n$，即 $n$-球面，有 $\Sigma{\mathbf S}^n={\mathbf S}^1\wedge{\mathbf S}^n\cong {\mathbf S}^{n+1}$。另一种方式是，高阶 K-群可以通过*悬挂同构*来定义：
$${\mathrm K}^{-n}(X)={\mathrm K}(X\times {\mathbb{R}}^n)\ ,$$
其中始终理解为使用的是具有紧支集的 K-理论。与通常的上同调理论不同，由于基本的*Bott 周期性定理*：
$${\mathrm K}^{-n}(X)={\mathrm K}^{-n-2}(X)\ ,$$
人们并不能以这种方式生成无穷多个高阶 K-群；该定理断言复 K-理论函子 ${\mathrm K}^{-n}$ 以周期 2 为周期。对约化函子 $\widetilde{{\mathrm K}}^{-n}$ 同样成立，因为与上式类似的定义对约化 K-理论也适用。然而，高阶约化 K-群与非约化 K-群按照
$${\mathrm K}^{-n}(X)=\widetilde{{\mathrm K}}^{-n}(X)\oplus {\mathrm K}^{-n}({\mathrm pt})$$
而有所不同。由于 ${\mathrm K}({\mathrm pt})={\mathbb{Z}}$、${\mathrm K}^{-1}({\mathrm pt})=0$，利用 Bott 周期性我们看到：当 $n$ 为偶数时，这两类群相差一个子群 ${\mathbb{Z}}$（正如（式）中那样）；而当 $n$ 为奇数时，它们完全相同，从而 $\widetilde{{\mathrm K}}^{-1}(X)={\mathrm K}^{-1}(X)$。这里基本的例子是：对任意正整数 $n$，${\mathrm K}^{-1}({\mathbf S}^{2n})=0$，而 ${\mathrm K}^{-1}({\mathbf S}^{2n+1})={\mathbb{Z}}$。

注意，对于把 $X$ 分解为开子空间的不交并的任意分解 $X=X_1\amalg X_2\amalg\cdots\amalg X_n$，$X_i$ 到 $X$ 的包含映射诱导出 K-群的一个分解
${\mathrm K}^{-n}(X)={\mathrm K}^{-n}(X_1)\oplus{\mathrm K}^{-n}(X_2)\oplus\cdots\oplus{\mathrm K}^{-n}(X_n)$
（这可由如下事实推出：$X$ 上的丛可以由它到各个 $X_i$ 的限制来刻画）。然而，这对约化 K-函子并不成立，因为例如 $\widetilde{{\mathrm K}}({\mathbf S}^0)={\mathbb{Z}}$，而 $\widetilde{{\mathrm K}}({\mathrm pt})=0$。更一般地，给定局部紧空间 $X$ 的两个*闭*子空间 $X_1$ 与 $X_2$，且 $X=X_1\cup X_2$，则存在长正合序列
$$\begin{matrix}
& &\ldots\longrightarrow{\mathrm K}^{-n-1}(X_1)\oplus{\mathrm K}^{-n-1}(X_2)
\stackrel{v}{\longrightarrow}
{\mathrm K}^{-n-1}(X_1\cap X_2)\longrightarrow\\
& &~~~~~~\stackrel{\zeta}{\longrightarrow}{\mathrm K}^{-n}(X_1\cup X_2)
\stackrel{u}{\longrightarrow}{\mathrm K}^{-n}(X_1)\oplus {\mathrm K}^{-n}(X_2)
\stackrel{v}{\longrightarrow}{\mathrm K}^{-n}(X_1\cap X_2)\longrightarrow\ldots\ ,
\end{matrix}$$
其中 $\zeta$ 是 zig-zag 同态，$u$ 与 $v$ 由
$u([E])=\left([E|_{X_1}],[E|_{X_2}]\right)$ 和 $v([E_1],[E_2])
=[E_1|_{X_1\cap X_2}]-[E_2|_{X_1\cap X_2}]$ 定义。相应于 $X$ 的两个*开*子空间 $U_1$ 与 $U_2$（$X=U_1\cup U_2$）的长正合序列为
$$\begin{matrix}
& &\ldots\longrightarrow{\mathrm K}^{-n-1}(U_1)\oplus{\mathrm K}^{-n-1}(U_2)\longrightarrow
{\mathrm K}^{-n-1}(U_1\cup U_2)\longrightarrow\\
& &~~~~~~\longrightarrow{\mathrm K}^{-n}(U_1\cap U_2)
\longrightarrow{\mathrm K}^{-n}(U_1)\oplus {\mathrm K}^{-n}(U_2)
\longrightarrow{\mathrm K}^{-n}(U_1\cup U_2)\longrightarrow\ldots\ .
\end{matrix}$$
这后两个序列是上同调中通常的 Mayer-Vietoris 长正合序列的类比。

### 乘法结构

如同任何上同调理论一样，${\mathrm K}(X)$ 与 $\widetilde{{\mathrm K}}(X)$ 实际上是环。在此情形下，乘法由 $X\times X$ 上向量丛的张量积 $E\otimes F$ 诱导：
$${\mathrm K}(X)\otimes_{{\mathbb{Z}}}{\mathrm K}(X)\longrightarrow{\mathrm K}(X)\ ,$$
并且定义为
$$\Bigl[(E\,,\,F)\Bigl]\otimes\Bigl[(E'\,,\,F')\Bigr]\equiv
\Delta^*\Bigl[(E\otimes E'\oplus F\otimes F'\,,\, E\otimes F'\oplus F\otimes
E')\Bigr]$$
其中 $\Delta:X\to X\times X$ 是对角映射。这个乘法来自把 $[(E,F)]=[E]-[F]$ 写出来，并形式地使用张量积作用在虚拟丛上的分配律。注意它作用在 $[(E,F)]$ 上时，就好像 $E$ 是玻色性的、而 $F$ 是费米性的一样。因此它是 ${\mathbb{Z}}_2$-分次张量积的一个例子。还存在另一种乘积，称为外张量积或*cup 积*，它是一个同态
$${\mathrm K}(X)\otimes_{{\mathbb{Z}}}{\mathrm K}(Y)\longrightarrow {\mathrm K}(X\times Y)$$
定义如下。考虑典范投影
$\pi_{X}:X\times Y\rightarrow X$ 与 $\pi_Y:X\times Y\rightarrow Y$。
这些投影按照
$$\pi_X^{*}:{\mathrm K}(X)\rightarrow {\mathrm K}(X\times Y)\ \ , \ \
\pi_Y^{*}:{\mathrm K}(Y)\rightarrow {\mathrm K}(X\times Y)\ .$$
在 K-群之间诱导出同态。于是 $([E],[F])\in {\mathrm K}(X)\otimes_{\mathbb{Z}}{\mathrm K}(Y)$ 的 cup 积就是 ${\mathrm K}(X\times Y)$ 中的类 $[E]\otimes [F]$，其中
$$[E]\otimes [F]\equiv\pi_X^{*}\Bigl([E]\Bigr)\otimes \pi_Y^{*}\Bigl([F]\Bigr)\ .$$

现在考虑典范的单射包含映射与满射投影映射：
$$X\vee Y \hookrightarrow X\times Y \longrightarrow X\wedge Y\ .$$
函子 $\widetilde{{\mathrm K}}^{-n}$ 是反变的，因此，正如在任何上同调理论中那样，这诱导出 K-群的一个分裂短正合序列
$$0\longrightarrow \widetilde{{\mathrm K}}^{-n}(X\wedge Y) \longrightarrow
\widetilde{{\mathrm K}}^{-n}(X\times Y)
\longrightarrow \widetilde{{\mathrm K}}^{-n}(X\vee Y) \longrightarrow 0\ ,$$
由此可得
$$\begin{matrix}
\widetilde{{\mathrm K}}^{-n}(X\times Y)&=& \widetilde{{\mathrm K}}^{-n}(X\wedge Y)\oplus
\widetilde{{\mathrm K}}^{-n}(X\vee Y)\\
&=& \widetilde{{\mathrm K}}^{-n}(X\wedge Y)\oplus \widetilde{{\mathrm K}}^{-n}(X)\oplus
\widetilde{{\mathrm K}}^{-n}(Y)\ .
\end{matrix}$$
公式（上式）对于计算笛卡尔积的 K-群特别有用。作为一个重要的例子，考虑 $Y={\mathbf S}^1$ 的情形，此时我们得到
$$\begin{matrix}
\widetilde{{\mathrm K}}(X\times {\mathbf S}^1)&=& \widetilde{{\mathrm K}}(X\wedge {\mathbf
S}^1)\oplus \widetilde{{\mathrm K}}(X)\oplus
\widetilde{{\mathrm K}}({\mathbf S}^1)\\
&=& {\mathrm K}^{-1}(X)\oplus \widetilde{{\mathrm K}}(X)\ ,
\end{matrix}$$
因为 $\widetilde{{\mathrm K}}({\mathbf S}^1)=0$ 且 $\widetilde{{\mathrm K}}({\mathbf S}^1\wedge X)={\mathrm K}^{-1}(X)$。确切地说，典范包含 $i:X\hookrightarrow X\times {\mathbf S}^1$ 诱导出投影 $i^*: \widetilde{{\mathrm K}}(X\times {\mathbf S}^1)\rightarrow
\widetilde{{\mathrm K}}(X)$，使得 $\ker i^*= {\mathrm K}^{-1}(X)$。换句话说，${\mathrm K}^{-1}(X)$ 可以与 $\widetilde{{\mathrm K}}(X\times {\mathbf S}^1)$ 中那些限制到 $X\times
{\mathrm pt}$ 上为零的 K-理论类的集合等同起来。同样地，
$$\begin{matrix}
{\mathrm K}^{-1}(X\times {\mathbf S}^1)&=& {\mathrm K}^{-1}(X\wedge {\mathbf
S}^1)\oplus {\mathrm K}^{-1}(X)\oplus
{\mathrm K}^{-1}({\mathbf S}^1)\\
&=& \widetilde{{\mathrm K}}(X)\oplus{\mathrm K}^{-1}(X)\oplus{\mathbb{Z}}\ ,
\end{matrix}$$
其中我们用到了 Bott 周期性。

约化 K-理论上的 cup 积（式）的作用也可以利用（式）与（式）推出，从而得到
$$\left(\widetilde{{\mathrm K}}(X)\otimes_{{\mathbb{Z}}}\widetilde{{\mathrm K}}(Y)\right)\oplus{\mathcal R}
\longrightarrow \widetilde{{\mathrm K}}(X\wedge Y)\oplus {\mathcal R}\ ,$$
其中 ${\mathcal R}=\widetilde{{\mathrm K}}(X)\oplus\widetilde{{\mathrm K}}(Y)\oplus{\mathbb{Z}}$。由于群 ${\mathcal R}$ 出现在（式）的两边，我们可以通过适当的限制把它消去，从而得到同态
$$\widetilde{{\mathrm K}}(X)\otimes_{{\mathbb{Z}}}\widetilde{{\mathrm K}}(Y)\longrightarrow \widetilde{{\mathrm K}}(X\wedge Y)\ .$$
当 ${\mathrm K}(X)$ 或 ${\mathrm K}(Y)$ 是自由阿贝尔群时，（式）与（式）中的映射是同构。

人们也可以按照一种能追踪该理论乘法结构的方式来计算 ${\mathrm K}^{-n}(X\times Y)$。定义 ${\mathrm K}^\#(X)$ 为 ${\mathbb{Z}}_2$-分次环 ${\mathrm K}^\#(X)={\mathrm K}(X)\oplus
{\mathrm K}^{-1}(X)$。于是，只要 ${\mathrm K}^\#(X)$ 或 ${\mathrm K}^\#(Y)$ 是自由生成的，我们就得到上同调 Künneth 定理的 K-理论类比：
$${\mathrm K}^\#(X\times Y)={\mathrm K}^\#(X)\otimes_{{\mathbb{Z}}} {\mathrm K}^\#(Y)\ .$$
（在一般情形下，上式右端还有修正项，用以计入 K-群的挠子群 [atiyahkun]。）具体地，上式给出
$$\begin{matrix}
{\mathrm K}(X\times Y)&=&\Bigl({\mathrm K}(X)\otimes_{\mathbb{Z}}{\mathrm K}(Y)\Bigr)
\oplus\Bigl({\mathrm K}^{-1}(X)\otimes_{\mathbb{Z}}{\mathrm K}^{-1}(Y)\Bigr)\ ,\\
{\mathrm K}^{-1}(X\times Y)&=&\Bigl({\mathrm K}(X)\otimes_{\mathbb{Z}}{\mathrm K}^{-1}(Y)\Bigr)
\oplus\Bigl({\mathrm K}^{-1}(X)\otimes_{\mathbb{Z}}{\mathrm K}(Y)\Bigr)\ .
\end{matrix}$$
例如，由于 $Y={\mathbf S}^1$ 的 K-群是自由生成的，利用 ${\mathrm K}({\mathbf S}^1)={\mathrm K}^{-1}({\mathbf S}^1)={\mathbb{Z}}$，我们再次得到（式）与（式）。类似地，在（式）中取 $Y={\mathbf S}^{2n}$ 与 $Y={\mathbf S}^{2n+1}$ 得到
$$\begin{matrix}
{\mathrm K}(X\times {\mathbf S}^{2n})&=& {\mathrm K}(X)\oplus {\mathrm K}(X)\ ,\\
{\mathrm K}(X\times {\mathbf S}^{2n+1})&=&{\mathrm K}(X)\oplus{\mathrm K}^{-1}(X)\ ,
\end{matrix}$$
作为 ${\mathrm K}(X)$-模。

若取 $Y={\mathbf S}^2$，则（式）与（式）中的映射实际上是同构，它们可以等同于约化 K-群与非约化 K-群的 Bott 周期性。在（式）中以 $X$ 的第 $n$ 次约化悬挂取代 $X$，给出
$$\widetilde{{\mathrm K}}(\Sigma^nX)\otimes_{\mathbb{Z}}\widetilde{{\mathrm K}}({\mathbf S}^2)
=\widetilde{{\mathrm K}}(\Sigma^nX\wedge{\mathbf S}^2)\ ,$$
由此得到同构
$$\alpha\,:\,\widetilde{{\mathrm K}}^{-n}(X)\otimes_{\mathbb{Z}}\widetilde{{\mathrm K}}({\mathbf S}^2)~
\stackrel{\approx}{\longrightarrow}~\widetilde{{\mathrm K}}^{-n-2}(X)\ .$$
$\widetilde{{\mathrm K}}({\mathbf S}^2)={\mathbb{Z}}$ 的生成元 $[{\mathcal N}_{\mathbb{C}}]-[I^1]$ 可以这样来描述：取 ${\mathcal N}_{\mathbb{C}}$ 为复射影空间 ${\mathbb{C}} P^1$ 上的典范线丛，它与分类 Dirac 单极子的 Hopf 纤维化 ${\mathbf S}^3\to
{\mathbf S}^2$ 相关联 [husemoller,trautman]。同构（式）于是由映射
$$\Bigl[(E\,,\,F)\Bigr]\longmapsto \alpha\Bigl[(E\otimes {\mathcal N}_{\mathbb{C}}\,,\,
F\otimes {\mathcal N}_{\mathbb{C}})\Bigr]\ ,$$
给出，其中 $[(E,F)]\in \widetilde{{\mathrm K}}^{-n}(X)$。

### 相对 K-理论

我们现在来定义相对 K-群 ${\mathrm K}(X,Y)$，它依赖于空间对 $(X,Y)$，其中 $Y$ 是 $X$ 的闭子流形；它的类可以与 $X/Y$ 上的丛对等同起来。若 $Y\neq
\emptyset$，则拓扑陪集 $X/Y$ 定义为把 $Y$ 收缩成一点之后的空间 $X$。若 $Y$ 为空，我们把 $X/Y$ 等同于 $X$ 的一点紧化 $X^+$。

首先我们说明，在给定 $X$ 上的向量丛 $E$ 之后，如何描述商空间 $X/Y$ 上的向量丛。设 $\alpha$ 是 $E$ 在 $Y\subset X$ 上的一个平凡化，即同构 $\alpha:
E|_{Y}\stackrel{\approx}{\rightarrow}Y\times V$。在 $E|_{Y}$ 上定义等价关系：$e\in E|_Y$ 与 $e'\in E|_Y$ 等价，当且仅当
$$\pi\circ\alpha(e)=\pi\circ\alpha(e')\ ,$$
其中 $\pi:Y\times V\rightarrow V$ 是典范投影。这个等价关系把 $E$ 限制到 $Y$ 上之后相对于平凡化 $\alpha$ 处于“同一水平”的点等同起来。然后我们把这个关系平凡地延拓到整个 $E$。可以证明，相应的等价类集合 $E_{\alpha}$ 是 $X/Y$ 上的一个向量丛，其同构类只依赖于平凡化 $\alpha$（$E$ 在 $Y\subset X$ 上）的同伦类。事实上，商空间 $X/Y$ 上的向量丛与 $X$ 上限制到 $Y$ 为平凡丛的向量丛之间存在一一对应。

*相对 K-群*现在定义为
$${\mathrm K}(X,Y)\equiv \widetilde{{\mathrm K}}(X/Y)\ .$$
于是 ${\mathrm K}(X,Y)$ 是空间对 $(X,Y)$ 的反变函子，并且由于
${\mathrm K}(X)=\widetilde{{\mathrm K}}(X^+)$（回忆 ${\mathrm K}(X)= \widetilde{{\mathrm K}}(X)\oplus {\mathrm K}({\mathrm
pt})$），我们有 ${\mathrm K}(X,\emptyset)={\mathrm K}(X)$。*切除定理*断言投影 $\pi:X\rightarrow X/Y$ 诱导出同构
$$\pi^*: {\mathrm K}(X/Y, {\mathrm pt})\stackrel{\approx}{\longrightarrow}{\mathrm K}(X,Y)\ .$$
同样地，可以通过
$${\mathrm K}^{-n}(X,Y)={\mathrm K}(X\times {\mathbf B}^n,X\times {\mathbf S}^[n-1]\cup Y\times {\mathbf
B}^n)\ ,$$
来定义高阶相对 K-群，其中 ${\mathbf B}^n=\{ x\in {\mathbb{R}}^n: | x|\leq1\}$ 是 ${\mathbb{R}}^n$ 中的单位球，而 ${\mathbf S}^[n-1]=\partial{\mathbf B}^n$。或者，也有悬挂同构
$${\mathrm K}^{-n}(X,Y)={\mathrm K}\Bigl((X-Y)\times {\mathbb{R}}^n\Bigr)\ .$$
相对 K-群具有通常的 Bott 周期性：
$${\mathrm K}^{-n}(X,Y)= {\mathrm K}^{-n-2}(X,Y)\ .$$

设 $i:Y\rightarrow X$ 与 $j:(X,\emptyset)\rightarrow (X,Y)$ 为包含映射。则存在正合序列
$${\mathrm K}(X,Y)\stackrel{j^*}{\longrightarrow} {\mathrm K}(X)\stackrel{i^*}{\longrightarrow}
{\mathrm K}(Y)\ .$$
若 $Y$ 还带有基点，则序列
$${\mathrm K}(X,Y)\longrightarrow \widetilde{{\mathrm K}}(X)\longrightarrow \widetilde{{\mathrm K}}(Y)$$
是正合的。更一般地，K-群最重要的性质之一是它们具有切除性质，这意味着它们满足 Barratt-Puppe 长正合序列：
$$\begin{matrix}
\ldots\longrightarrow{\mathrm K}^{-n-1}(X)\longrightarrow
{\mathrm K}^{-n-1}(Y)\stackrel{\partial^*}{\longrightarrow}
{\mathrm K}^{-n}(X,Y)\longrightarrow
{\mathrm K}^{-n}(X)\longrightarrow{\mathrm K}^{-n}(Y)
\stackrel{\partial^*}{\longrightarrow}\ldots\ ,
\end{matrix}$$
其中 $\partial$ 是边界同态。长正合序列（上式）把 $X$ 与 $Y\subset X$ 的 K-群联系起来，正是在这个意义上 K-理论类似于上同调理论。利用 Bott 周期性，这个序列可以令人惊讶地截断为六项正合序列。若 $Y$ 是 $X$ 的收缩（即包含映射 $i:Y\to X$ 有左逆），则序列（式）分裂，给出
$${\mathrm K}^{-n}(X)={\mathrm K}^{-n}(X,Y)\oplus{\mathrm K}^{-n}(Y)\ .$$

相对 K-理论的概念可以按照一种在后续讨论中有用的方式重新表述。设 $\Gamma(X,Y)$ 是三元组 $(E,F;\alpha)$ 的集合，其中 $E,F\in {\mathrm
Vect}(X)$，而 $\alpha: E|_{Y}\stackrel{\approx}{\rightarrow}F|_{Y}$ 是限制到 $Y$ 上的向量丛同构。若存在同构 $f: E\stackrel{\approx}{\rightarrow} E'$ 与 $g:
F\stackrel{\approx}{\rightarrow}F'$，使得图
$${\begin{array}{ccc}
E|_{Y}&\stackrel{\alpha}{\longrightarrow}&F|_{Y}\\&
&\\{\scriptstyle f|_{Y}}\downarrow& &\downarrow{\scriptstyle g|_{Y}}\\&
&\\E'|_{Y}&\stackrel{\alpha'}{\longrightarrow}&F'|_{Y}\end{array}}$$
交换，则称两个这样的三元组 $(E,F;\alpha)$ 与 $(E',F';\alpha')$ 同构。若 $E\cong F$ 且 $\alpha$ 在 $E|_{Y}$ 的自同构群内同伦于 ${\mathrm Id}_{E|_{Y}}$，则称三元组 $(E,F;\alpha)$ 是*初等的*。$(E,F;\alpha)$ 与 $(E',F';\alpha')$ 的和定义为
$$(E,F;\alpha)\oplus(E',F';\alpha')
\equiv(E\oplus E', F\oplus F'; \alpha\oplus\alpha')\ ,$$
在这一运算下 $\Gamma(X,Y)$ 成为阿贝尔幺半群。现在考虑 $\Gamma(X,Y)$ 中的如下等价关系。只要存在两个初等三元组 $(G,H;\beta)$ 与 $(G',H';\beta')$，使得
$$(E,F;\alpha)\oplus(G,H;\beta)\cong(E',F';\alpha')\oplus(G',H';\beta')\ ,$$
我们就认为三元组 $(E,F;\alpha)$ 与 $(E',F';\alpha')$ 等价。在运算
$\oplus$ 之下，这些三元组的等价类集合（我们记为
$[E,F;\alpha]$）成为阿贝尔群，它可以与相对 K-群等同起来，即 ${\mathrm K}(X,Y)=\Gamma(X,Y)/\sim$。
注意，$[E,F;\alpha]=0$ 于 ${\mathrm K}(X,Y)$ 中，当且仅当存在向量丛 $G,H\in {\mathrm Vect}(X)$ 以及丛同构 $u:E\oplus G
\rightarrow H$、$v: F\oplus G\rightarrow H$，使得 $v|_{Y}\circ
(\alpha\oplus {\mathrm Id}_{G|_{Y}})\circ u^{-1}|_{Y}$ 在 $H|_{Y}$ 的自同构群内同伦于
${\mathrm Id}_{H|_{Y}}$。此外，$[E,F;\alpha]+[F,E;\alpha^{-1}]=0$。还要注意，在这个形式体系中，群 ${\mathrm K}(X)$ 可以描述为三元组 $[E,F;\alpha]$ 的集合，其中
$\alpha:E\stackrel{\approx}{\rightarrow} F$ 是定义在 $X$ 的一点紧化的无穷远点之邻域内的丛同构。这正是（式）中所作的陈述。

${\mathrm K}(X,Y)$ 的基本性质如下。第一，若 $\alpha,\alpha'$ 是如上所述的同构 $E|_{Y}\stackrel{\approx}{\rightarrow}F|_{Y}$，且 $\alpha$ 与 $\alpha'$ 在从 $E|_{Y}$ 到 $F|_{Y}$ 的同构之间同伦，则 $[E,F;\alpha]=[E,F;\alpha']$。
其次，当 $[E,F;\alpha]$ 与 $[F,G;\beta]$ 是 ${\mathrm K}(X,Y)$ 的元素时，它们的和由关系
$[E,F;\alpha]+[F,G;\beta]=[E,G;\beta\circ\alpha]$ 给出。第三，${\mathrm K}(X,Y)$ 中的两个元素确定同一个等价类
$[E,F;\alpha]=[E',F';\alpha']$，当且仅当存在三元组
$(G,G;{\mathrm Id}_{G|_{Y}})$ 与 $(G',G';{\mathrm Id}_{G'|_{Y}})$，以及映射
$f: E\oplus G\rightarrow E'\oplus G'$、$g: F\oplus G\rightarrow F'\oplus G'$，使得图
$${\begin{array}{ccc}
(E\oplus G)|_{Y}&\stackrel{\alpha\oplus {\mathrm Id}_{G|_Y}}{\longrightarrow}&
(F\oplus G)|_{Y}\\&
&\\{\scriptstyle f|_{Y}}\downarrow& &\downarrow{\scriptstyle g|_{Y}}\\&
&\\(E'\oplus G')|_{Y}&\stackrel{\alpha'\oplus {\mathrm Id}_{G'|_Y}}
{\longrightarrow}&(F'\oplus
G')|_{Y}\end{array}}$$
交换。此外，cup 积自然地延拓到相对 K-理论，给出唯一的双线性同态
$${\mathrm K}(X,Y)\otimes_{{\mathbb{Z}}}{\mathrm K}(X',Y')\longrightarrow
{\mathrm K}(X\times X',X\times Y'\cup Y\times X')\ .$$
这与前面在 $Y=Y'=\emptyset$ 时引入的 cup 积一致。具体地，两个 K-理论类 $[E,F;\alpha]$ 与
$[E',F';\alpha']$ 的乘积，是利用向量丛对上的乘积（式）以及乘积同构
$$\beta=\left( \begin{array}{cc}\alpha\otimes{\mathrm Id} & {\mathrm Id}
\otimes\alpha'^{\dagger}\\
{\mathrm Id}\otimes\alpha' &-\alpha^{\dagger}\otimes{\mathrm Id}
\end{array}\right)\ .$$
作用在（式）上而得到的（注意这需要对所涉及的丛引入纤维度量）。

作为一个简单的例子，考虑 $X={\mathbf B}^2$ 与 $Y={\mathbf S}^1\subset {\mathbb{R}}^2$ 的情形。取 $E=F={\mathbf B}^2\times
{\mathbb{C}}$，并对 $x\in {\mathbf S}^1\subset {\mathbf B}^2$ 令 $\alpha(x,z)=(x,xz)$，以此定义 $[E,F;\alpha]\in
{\mathrm K}({\mathbf B}^2, {\mathbf S}^1)$。结果发现 $[E,F;\alpha]$ 是 ${\mathrm K}({\mathbf B}^2,
{\mathbf S}^1)= {\mathbb{Z}}$ 的生成元。这是我们遇到的第一个 ABS 构造的实例，它将在 2.8 节中描述。作为另一个例子，考虑复射影空间 $X={\mathbb{C}} P^2$ 与 $Y={\mathbb{C}}
P^1$。如前所述，$\widetilde{{\mathrm K}}({\mathbf S}^2)=
{\mathbb{Z}}$ 的一个非平凡生成元由 ${\mathbb{C}} P^1$ 上的典范线丛给出，它是 ${\mathbb{C}} P^2$ 上典范线丛的限制。由此可知，映射 ${\mathrm K}(X)\rightarrow {\mathrm K}(Y)$ 是满射。此外，
${\mathrm K}^{-1}({\mathbf S}^2)=0$ 且 ${\mathrm K}(X,Y)=\widetilde{{\mathrm K}}({\mathbf S}^4)={\mathbb{Z}}$。由（式）我们于是得到分裂短正合序列
$$0\longrightarrow \widetilde{{\mathrm K}}({\mathbf S}^4)\longrightarrow {\mathrm K}({\mathbb{C}} P^2)
\longrightarrow{\mathrm K}({\mathbb{C}} P^1)\longrightarrow 0\ ,$$
从而 ${\mathrm K}({\mathbb{C}} P^2)=\widetilde{{\mathrm K}}({\mathbf S}^4)\oplus{\mathrm K}({\mathbb{C}} P^1)
={\mathbb{Z}}\oplus{\mathbb{Z}}\oplus{\mathbb{Z}}$。


### 计算 K-群

在本小节中，我们将说明如何把 K-群计算为某些分类空间的同伦群，而这些分类空间往往存在有限维的近似。最基本的情形是约化 K-群 $\widetilde{{\mathrm K}}(X)$，因为非约化 K-群可由分解（式）计算，而更高阶的 K-群由（式）中的悬挂给出。设 ${\mathrm Vect}_k(X)$ 为秩为 $k$ 的复向量丛 $E_k\rightarrow X$ 的同构类的集合。于是我们有包含序列 $\ldots\subset {\mathrm Vect}_k(X)\subset {\mathrm Vect}_{k+1}(X)\subset\ldots$，其中的映射为 $E_k\mapsto E_k\oplus I^1$。若 $[E_k]\in {\mathrm Vect}_k(X)$，则 $[E_k]-[I^k]\in \ker\,\mathrm{rk}= {\mathrm K}'(X)$。映射 $[E_k]\mapsto [E_k]-[I^k]$ 实际上是阿贝尔幺半群的同构 ${\mathrm Vect}(X)\rightarrow {\mathrm K}'(X)$，因此 ${\mathrm Vect}(X)\equiv\bigcup_{k=0}^{\infty}{\mathrm Vect}_k(X)$ 是一个阿贝尔群。

秩为 $k$ 的复向量丛 $E_k$ 具有结构群 $GL(k,{\mathbb{C}})$（即纤维自同构群）；在 $X$ 上选取度量、从而在 $E_k$ 的纤维上诱导出 Hermite 内积之后，该结构群可约化为酉子群 $U(k)$。$E_k$ 的*分类空间*是复 Grassmann 流形：

$$
{\mathrm Gr}(k,m;{\mathbb{C}})=\frac{U(m)}{U(m-k)\times U(k)}\ ,  \ \ \ m>k+n\ ,
$$

其中 $n\equiv\dim X$。按照微分几何的一个标准定理，在 ${\mathrm Gr}(k,m;{\mathbb{C}})$ 上存在所谓秩为 $k$ 的万有丛 $Q(k,m;{\mathbb{C}})$，其拉回可生成诸如 $E_k$ 这样的向量丛。这意味着对某个连续映射 $f: X\rightarrow{\mathrm Gr}(k,m;{\mathbb{C}})$（$m>k+n$）有 $f^*Q(k,m;{\mathbb{C}})\cong E_k$。此外，这个同构只依赖于 $f$ 的同伦类。因此，丛 $E_k$ 按照 $[X,{\mathrm Gr}(k,m;{\mathbb{C}})]$ 中的同伦类来分类。

同样，我们有自然的包含 $\ldots \subset{\mathrm Gr}(k,m;{\mathbb{C}})\subset {\mathrm Gr}(k,m+1;{\mathbb{C}})\subset \ldots$，于是取归纳极限便得到 $U(k)$ 丛的分类空间：

$$
BU(k)\equiv \bigcup_{m=k+n+1}^{\infty}{\mathrm Gr}(k,m;{\mathbb{C}})
$$

使得

$$
{\mathrm Vect}_k(X)=\Bigl[X\,,\,BU(k)\Bigr]
$$

以及

$$
{\mathrm K}'(X)= {\mathrm Vect}(X)=\Bigl[X\,,\,BU(\infty)\Bigr]\ ,
$$

其中 $BU(\infty)=\bigcup_{k=1}^{\infty}BU(k)$。注意，若 $X$ 紧致，则 ${\mathrm K}(X)= H^0(X,{\mathbb{Z}})\oplus {\mathrm K}'(X)$（依据（式）），且 $H^0(X,{\mathbb{Z}})= [X,{\mathbb{Z}}]$。这意味着

$$
{\mathrm K}(X)=\Bigl[X\,,\,{\mathbb{Z}}\Bigr]\oplus
\Bigl[X\,,\,BU(\infty)\Bigr]=\Bigl[X\,,\,{\mathbb{Z}}\times BU(\infty)\Bigr]\ .
$$

然而结果表明，当秩 $k$ 增大时情况会有所简化。这就引出了*稳定范围*的概念。令 $k_0=[(n+1)/2]$。则对所有 $k>k_0$，存在秩为 $k_0$ 的丛 $F_{k_0}$，使得 $E_k\cong F_{k_0}\oplus I^{k-k_0}$。这意味着稳定范围内的任何向量丛 $E_k$ 都稳定等价于另一个秩更低（$k_0$）的丛 $F_{k_0}$。于是 $E_k$ 与 $F_{k_0}$ 属于同一稳定等价类，并对应 ${\mathrm K}'(X)$ 中完全相同的元素；也就是说，就 K-理论而言，考虑很高秩的丛并不能带来任何新东西，因为一旦达到稳定范围，再增大秩 $k$ 也不会得到新的 K-理论元素。注意，在稳定范围内，两个同秩的向量丛稳定等价当且仅当它们同构。这意味着对所有 $k>\frac{1}{2}n$ 有 ${\mathrm K}'(X)= {\mathrm Vect}_k(X)$，或 ${\mathrm K}'(X)= [X, BU(k)]$。因此，只要 $X$ 连通，我们就有

$$
\widetilde{{\mathrm K}}(X)=\Bigl[X\,,\,BU(k)\Bigr]\ .
$$

让我们考虑一些简单的例子。直接令人感兴趣的情形是 $X={\mathbf S}^[n]$，此时对所有 $k> n/2$ 有 $\widetilde{{\mathrm K}}(X)= [{\mathbf S}^n,BU(k)]= \pi_n(BU(k))$。我们可以用上下两个半球 ${\mathbf S}^n_{\pm}$ 覆盖 ${\mathbf S}^n$。由于 ${\mathbf S}^n_{\pm}$ 是可缩的，所有丛 $E_k|_{{\mathbf S}^n_{\pm}}$ 都是平凡的，从而由重叠区域 ${\mathbf S}^n_{+}\cap {\mathbf S}^n_{-}$ 上单个 $U(k)$ 值的过渡函数 $g$ 决定。但 ${\mathbf S}^n_{+}\cap {\mathbf S}^n_{-}\cong {\mathbf S}^[n-1]$，所以 $g$ 决定了一个从 ${\mathbf S}^[n-1]$ 到 $U(k)$ 的映射，即 $\pi_{n-1}(U(k))$ 中的一个元素。正是 $\pi_{n-1}(U(k))$ 的这个元素决定了丛 $E_k\in {\mathrm Vect}({\mathbf S}^n)$，并因而决定了 $\widetilde{{\mathrm K}}({\mathbf S}^n)$ 的一个元素，于是

$$
\widetilde{{\mathrm K}}({\mathbf S}^n)= \pi_{n-1}\Bigl(U(k)\Bigr)\ , \ \ \ \ k>n/2\ .
$$

特别地，我们有

$$
\widetilde{{\mathrm K}}({\mathbf S}^n)= \pi_{n-1}\Bigl(U(\infty)\Bigr)\ ,
$$

其中 $U(\infty)=\bigcup_{k=1}^{\infty}U(k)$。诸如 $U(k)$ 这类经典 Lie 群的同伦群已被广泛研究。尽管 $\pi_{n-1}(U(k))$ 并非对所有 $n,k$ 都已知，但恰恰是在稳定范围 $k>n/2$ 内我们才有完整的分类。注意由（式），（式）实际上是断言 $[{\mathbf S}^n,BU(k)]\cong[{\mathbf S}^[n-1],U(k)]$。这可由以下事实推出。首先，

$$
\Bigl[{\mathbf S}^n\,,\,BU(k)\Bigr]=\Bigl[\Sigma{\mathbf S}^[n-1]\,,\,BU(k)\Bigr]
=\Bigl[{\mathbf S}^[n-1]\,,\,\Omega BU(k)\Bigr]\ ,
$$

其中 $\Omega^n Y$ 表示拓扑空间 $Y$ 的第 $n$ 次迭代环路空间。同构 $[{\mathbf S}^[n-1],U(k)]\cong[{\mathbf S}^[n-1],\Omega BU(k)]$ 现在可由空间 $\Omega BU(k)$ 与 $U(k)$ 具有相同同伦型这一事实推出。这意味着环路空间算子 $\Omega$ 可以被看作分类空间算子 $B$ 的某种同伦逆。正是这一陈述构成了经典 Lie 群的 Bott 周期定理的原始内容 [bott]。

作为另一个例子，在 ${\mathbb{R}}^n$ 中取 $X={\mathbf B}^n$ 而 $Y={\mathbf S}^[n-1]=\partial {\mathbf B}^n$。拓扑陪集 ${\mathbf B}^n/{\mathbf S}^[n-1]$ 可等同于 ${\mathbf S}^n$，这诱导出从 ${\mathbf S}^[n]_{+}/{\mathbf S}^[n-1]\cong {\mathbf B}^[n]/{\mathbf S}^[n-1]$ 到 ${\mathbf S}^[n]$ 的同胚。于是由切除定理可得

$$
{\mathrm K}({\mathbf B}^[n],{\mathbf S}^[n-1])={\mathrm K}({\mathbf B}^[n]/{\mathbf S}^[n-1],{\mathrm pt})=\widetilde{{\mathrm K}}({\mathbf S}^[n])=\pi_{n-1}\Bigl(U(\infty)\Bigr)\ .
$$

例如，${\mathrm K}({\mathbf B}^{2},{\mathbf S}^{1})=\pi_1(U(\infty))= \pi_1(U(1))= {\mathbb{Z}}$。


### Clifford 代数与 Atiyah-Bott-Shapiro 构造

在本小节中我们将讨论 Clifford 代数与旋量表示同 K-理论的关系。对 Clifford 代数的分析非常简单，许多 K-理论结果一旦翻译成这种代数语言就变得透明。我们先描述与向量空间 $V={\mathbb{R}}^{r+s}$ 及其上二次型 $q(x)=x_1^{2}+\ldots +x_r^{2}-x_{r+1}^{2}-\ldots -x_{r+s}^{2}$ 相伴的 Clifford 代数 $C\ell_{r,s}$，该二次型在 $O(r,s)$-旋转下不变。存在自然嵌入 $V\hookrightarrow C\ell_{r,s}$，而抽象的单位代数 $C\ell_{r,s}$ 由 $V$ 的任意 $q$-正交归一基 $\Gamma_1,\ldots ,\Gamma_{r+s}$ 生成，并满足关系
$$
\Gamma_i\Gamma_j+\Gamma_j\Gamma_i~=~\left\{\begin{array}{cll}-2\delta_{ij}~~~~&,
&~~i\leq r\\+2\delta_{ij}~~~~&,&~~i > r\end{array}\right.
$$
代数（式）的最小表示由维数为 $2^{\left[\frac{r+s}{2}\right]}$ 的 Dirac 矩阵构成。

映射 $x\mapsto -x$（$x\in V$）可延拓为自同构 $\eta: C\ell_{r,s}\rightarrow C\ell_{r,s}$。由于 $\eta^2={\mathrm Id}$，这导致分解
$$
C\ell_{r,s}=C\ell_{r,s}^+\oplus C\ell_{r,s}^-\ ,
$$
其中 $C\ell_{r,s}^{\pm}=\left\{\phi\in C\ell_{r,s}\,:\,
\eta(\phi)=\pm\phi\right\}$ 是 $\eta$ 的本征空间。由此可得
$$
C\ell_{r,s}^{\alpha}\cdot C\ell_{r,s}^{\beta}
\subset C\ell_{r,s}^{\alpha\beta}\ ,
$$
其中 $\alpha,\beta=\pm$。于是 $C\ell_{r,s}$ 的相伴分次代数自然同构于外代数 $\Lambda^*V$，即由（式）定义的 Clifford 乘法是由二次型 $q$ 所确定的外乘法的自然增强。事实上存在典范的向量空间同构 $\Lambda^*V\stackrel{\approx}{\rightarrow}C\ell_{r,s}$，从而对一切 $n\geq 0$ 有自然嵌入 $\Lambda^nV\subset C\ell_{r,s}$。

自旋群 $Spin(r,s)\subset C\ell_{r,s}$ 的维数为 $2^{r+s}$，它经由嵌入 ${\mathbf S}^{r+s-1}\subset V\subset C\ell_{r,s}$ 由 Clifford 代数的乘法单位群得到。它是群 $SO(r,s)$ 的双重覆盖，这由正合序列
$$
1\longrightarrow{\mathbb{Z}}_2\longrightarrow Spin(r,s)\longrightarrow SO(r,s)
\longrightarrow 1
$$
表达。与 $C\ell_{n,0}$ 相伴的自旋群是 $Spin(n)$，它是球面 ${\mathbf S}^[n-1]$ 的等距群 $SO(n)$ 的双重覆盖。我们将使用简写 $C\ell_n\equiv C\ell_{n,0}$ 与 $C\ell_n^{*}\equiv C\ell_{0,n}$。作为一个简单例子，$C\ell_1$ 由单位元与一个满足 $\Gamma^2=-1$ 的元素 $\Gamma$ 生成，故 $C\ell_1\cong{\mathbb{C}}$。类似地容易看出 $C\ell^*_{1}\cong{\mathbb{R}}\oplus{\mathbb{R}}$。

在典范同构 $C\ell_n\cong \Lambda^*{\mathbb{R}}^n$ 下，Clifford 乘法具有特别漂亮的形式。对 $x\in{\mathbb{R}}^n$，我们通过
$$
\begin{matrix}
x\,\neg\,(x_1\wedge\cdots\wedge x_p)=\sum_{m=1}^[p](-1)^{m+1}\,
\sum_{i=1}^[n]x^i(x_m)^i\,
x_1\wedge\cdots\wedge x_{m-1}\wedge x_{m+1}\wedge\cdots\wedge x_p\ .
\end{matrix}
$$
定义内乘 $x\,\neg:\Lambda^p{\mathbb{R}}^n\rightarrow\Lambda^[p-1]{\mathbb{R}}^n$。由于对一切 $\omega\in\Lambda^p{\mathbb{R}}^n$ 与一切 $y\in\Lambda^q{\mathbb{R}}^n$ 有 $x\,\neg\,(\omega\wedge y)=(x\,\neg\,\omega)\wedge y+(-1)^p
\omega\wedge(x\,\neg\,y)$，这定义了该代数的一个斜导子。此外对一切 $x\in{\mathbb{R}}^n$ 有 $(x\,\neg)^2=0$，于是内乘可普适地延拓为双线性映射 $\Lambda^*{\mathbb{R}}^n\otimes\Lambda^*{\mathbb{R}}^n\rightarrow
\Lambda^*{\mathbb{R}}^n$。现在容易证明，$x\in{\mathbb{R}}^n$ 与 $\phi\in C\ell_n$ 之间的 Clifford 乘法相对于典范同构 $C\ell_n\cong\Lambda^*{\mathbb{R}}^n$ 可以写成
$$
x\cdot\phi=x\wedge\phi-x\,\neg\,\phi\ ,
$$
的形式。

对任意一对正整数 $(r,s)$，代数 $C\ell_{r,s}$ 都有显式的表示，即表为域 ${\mathbb{R}}$、${\mathbb{C}}$ 或 ${\mathbb{H}}$ 之一上的矩阵代数。最初几个例子容易手工构造，例如
$$
\begin{matrix}
C\ell_{1,0} &= {\mathbb{C}}\ , \qquad C\ell_{0,1} = {\mathbb{R}}\oplus{\mathbb{R}}\ ,\\
C\ell_{2,0} &= {\mathbb{H}}\ , \qquad C\ell_{0,2} = {\mathbb{R}}(2)\ ,\\
C\ell_{1,1} &= {\mathbb{R}}(2)\ ,
\end{matrix}
$$
其中 ${\mathbb{F}}(m)$ 表示元素取在代数域 $\mathbb{F}$ 中的 $m\times m$ 矩阵所成的 ${\mathbb{R}}$-代数。Clifford 代数的完全分类则通过下列周期关系（对任意 $n,r,s\geq 0$ 成立）得到：
$$
\begin{matrix}
C\ell_{n,0}\otimes C\ell_{0,2}&=&C\ell_{0,n+2}\ ,\\
C\ell_{0,n}\otimes C\ell_{2,0}&=&C\ell_{n+2,0}\ ,\\
C\ell_{r,s}\otimes C\ell_{1,1}&=&C\ell_{r+1,s+1}\ ,
\end{matrix}
$$
以及
$$
\begin{matrix}
C\ell_{n,0}\otimes C\ell_{8,0}&=&C\ell_{n+8,0}\ ,\\
C\ell_{0,n}\otimes C\ell_{0,8}&=&C\ell_{0,n+8}\ ,
\end{matrix}
$$
其中
$$
C\ell_{8,0}=C\ell_{0,8}={\mathbb{R}}(16)\ .
$$
利用这些关系与（式）可以写出全部 Clifford 代数 $C\ell_{r,s}$，它们总结于下表中。

表：$0\leq r,s\leq 8$ 的实 Clifford 代数 $C\ell_{r,s}$。

| $s$ | $r=0$ | $r=1$ | $r=2$ | $r=3$ | $r=4$ |
|---|---|---|---|---|---|
| 0 | ${\mathbb{R}}$ | ${\mathbb{C}}$ | ${\mathbb{H}}$ | ${\mathbb{H}}\oplus{\mathbb{H}}$ | ${\mathbb{H}}(2)$ |
| 1 | ${\mathbb{R}}\oplus{\mathbb{R}}$ | ${\mathbb{R}}(2)$ | ${\mathbb{C}}(2)$ | ${\mathbb{H}}(2)$ | ${\mathbb{H}}(2)\oplus{\mathbb{H}}(2)$ |
| 2 | ${\mathbb{R}}(2)$ | ${\mathbb{R}}(2)\oplus{\mathbb{R}}(2)$ | ${\mathbb{R}}(4)$ | ${\mathbb{C}}(4)$ | ${\mathbb{H}}(4)$ |
| 3 | ${\mathbb{C}}(2)$ | ${\mathbb{R}}(4)$ | ${\mathbb{R}}(4)\oplus{\mathbb{R}}(4)$ | ${\mathbb{R}}(8)$ | ${\mathbb{C}}(8)$ |
| 4 | ${\mathbb{H}}(2)$ | ${\mathbb{C}}(4)$ | ${\mathbb{R}}(8)$ | ${\mathbb{R}}(8)\oplus{\mathbb{R}}(8)$ | ${\mathbb{R}}(16)$ |
| 5 | ${\mathbb{H}}(2)\oplus{\mathbb{H}}(2)$ | ${\mathbb{H}}(4)$ | ${\mathbb{C}}(8)$ | ${\mathbb{R}}(16)$ | ${\mathbb{R}}(16)\oplus{\mathbb{R}}(16)$ |
| 6 | ${\mathbb{H}}(4)$ | ${\mathbb{H}}(4)\oplus{\mathbb{H}}(4)$ | ${\mathbb{H}}(8)$ | ${\mathbb{C}}(16)$ | ${\mathbb{R}}(32)$ |
| 7 | ${\mathbb{C}}(8)$ | ${\mathbb{H}}(8)$ | ${\mathbb{H}}(8)\oplus{\mathbb{H}}(8)$ | ${\mathbb{H}}(16)$ | ${\mathbb{C}}(32)$ |
| 8 | ${\mathbb{R}}(16)$ | ${\mathbb{C}}(16)$ | ${\mathbb{H}}(16)$ | ${\mathbb{H}}(16)\oplus{\mathbb{H}}(16)$ | ${\mathbb{H}}(32)$ |

| $s$ | $r=5$ | $r=6$ | $r=7$ | $r=8$ |
|---|---|---|---|---|
| 0 | ${\mathbb{C}}(4)$ | ${\mathbb{R}}(8)$ | ${\mathbb{R}}(8)\oplus{\mathbb{R}}(8)$ | ${\mathbb{R}}(16)$ |
| 1 | ${\mathbb{H}}(4)$ | ${\mathbb{C}}(8)$ | ${\mathbb{R}}(16)$ | ${\mathbb{R}}(16)\oplus{\mathbb{R}}(16)$ |
| 2 | ${\mathbb{H}}(4)\oplus{\mathbb{H}}(4)$ | ${\mathbb{H}}(8)$ | ${\mathbb{C}}(16)$ | ${\mathbb{R}}(32)$ |
| 3 | ${\mathbb{H}}(8)$ | ${\mathbb{H}}(8)\oplus{\mathbb{H}}(8)$ | ${\mathbb{H}}(16)$ | ${\mathbb{C}}(32)$ |
| 4 | ${\mathbb{C}}(16)$ | ${\mathbb{H}}(16)$ | ${\mathbb{H}}(16)\oplus{\mathbb{H}}(16)$ | ${\mathbb{H}}(32)$ |
| 5 | ${\mathbb{R}}(32)$ | ${\mathbb{C}}(32)$ | ${\mathbb{H}}(32)$ | ${\mathbb{H}}(32)\oplus{\mathbb{H}}(32)$ |
| 6 | ${\mathbb{R}}(32)\oplus{\mathbb{R}}(32)$ | ${\mathbb{R}}(64)$ | ${\mathbb{C}}(64)$ | ${\mathbb{H}}(64)$ |
| 7 | ${\mathbb{R}}(64)$ | ${\mathbb{R}}(64)\oplus{\mathbb{R}}(64)$ | ${\mathbb{R}}(128)$ | ${\mathbb{C}}(128)$ |
| 8 | ${\mathbb{C}}(64)$ | ${\mathbb{R}}(128)$ | ${\mathbb{R}}(128)\oplus{\mathbb{R}}(128)$ | ${\mathbb{R}}(256)$ |

由该表可以观察到 Clifford 代数的一些额外内禀对称性，例如
$$
\begin{matrix}
C\ell_{r,s}&=&C\ell_{r-4,s+4}\ ,\\
C\ell_{r,s+1}&=&C\ell_{s,r+1}\ ,
\end{matrix}
$$
它们也可由 $C\ell_{r,s}$ 的定义直接证明。

我们现在描述与球面上复向量丛的 K-理论相关的复化 Clifford 代数。实 Clifford 代数 $C\ell_{r,s}$ 的复化是 ${\mathbb{C}}$-代数 ${\mathbb{C}}\ell_{r,s}=C\ell_{r,s}\otimes_{{\mathbb{R}}}{\mathbb{C}}$，它也可视为与向量空间 ${\mathbb{C}}^{r+s}$ 及二次型 $q$ 的复化 $q\otimes{\mathbb{C}}$ 相伴的 Clifford 代数。由于 ${\mathbb{C}}$ 上一切非退化二次型都等价，我们有同构序列
$$
{\mathbb{C}}\ell_n\cong C\ell_{n,0}\otimes_{{\mathbb{R}}} {\mathbb{C}} \cong
C\ell_{n-1,1}\otimes_{{\mathbb{R}}}{\mathbb{C}}
\cong \cdots \cong C\ell_{0,n}\otimes_{{\mathbb{R}}}{\mathbb{C}}\ ,
$$
这使得复化 Clifford 代数的分类简单得多，因为它意味着 ${\mathbb{C}}\ell_{r,s}$ 只依赖于 $r$ 与 $s$ 之和：$C\ell_{r,s}\otimes_{{\mathbb{R}}}{\mathbb{C}}\cong {\mathbb{C}}\ell_{r+s}$。由此还可推出 ${\mathbb{C}}\ell_n$ 的周期性为
$$
{\mathbb{C}}\ell_{n+2}\cong {\mathbb{C}}\ell_n\otimes_{{\mathbb{C}}}{\mathbb{C}}\ell_2\ ,
$$
其中 ${\mathbb{C}}\ell_2={\mathbb{C}}(2)$。（我们将看到这一周期性与球面复 K-理论的 Bott 周期性有关。）利用这些恒等式容易导出下表中复化 Clifford 代数的清单。

表：$1\leq n \leq 8$ 的复化 Clifford 代数 ${\mathbb{C}}\ell_n$。

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| ${\mathbb{C}}\ell_n$ | ${\mathbb{C}}\oplus{\mathbb{C}}$ | ${\mathbb{C}}(2)$ | ${\mathbb{C}}(2)\oplus{\mathbb{C}}(2)$ | ${\mathbb{C}}(4)$ | ${\mathbb{C}}(4)\oplus{\mathbb{C}}(4)$ | ${\mathbb{C}}(8)$ | ${\mathbb{C}}(8)\oplus{\mathbb{C}}(8)$ | ${\mathbb{C}}(16)$ |

Clifford 代数的大多数重要应用都来自对其表示的细致理解，以及通过限制得到其相应自旋群的表示论。这些性质由刚才给出的分类便相当容易推出。对任意代数域 ${\mathbb{F}}$，我们把 Clifford 代数的 ${\mathbb{F}}$-表示定义为一个同态 $\rho: C\ell\longrightarrow
{\mathrm End}_{\mathbb{F}}(W)$，取值于 ${\mathbb{F}}$ 上有限维向量空间 $W$ 的线性变换的自同态代数（此处 $C\ell$ 可以是 $C\ell_{r,s}$ 或 ${\mathbb{C}}\ell_n$）。特别地，$\rho$ 对一切 $\phi,\psi\in C\ell$ 满足性质 $\rho(\phi\psi)=\rho(\phi)\circ\rho(\psi)$。这样 $W$ 就成为 ${\mathbb{F}}$ 上的 Clifford 模。对 $\phi\in C\ell$，$\rho(\phi)$ 在 $w\in W$ 上的作用记为
$$
\rho(\phi)(w)\equiv\phi\cdot w\ ,
$$
习惯上称为 Clifford 乘法。

如上所示，某些 Clifford 代数的不可约表示的张量积给出另一个不可约 Clifford 模（例如见（式）与（式））。然而一般说来 $C\ell_n\otimes C\ell_m$ 并不是 Clifford 代数，因此为了在 Clifford 代数的表示中找到乘法结构，自然要考虑一类特殊的 Clifford 模。为此，我们把 $C\ell_n$ 的 ${\mathbb{Z}}_2$-分次模 $W$ 定义为具有分解 $W=W^+\oplus W^-$ 且满足
$$
C\ell_n^{\alpha}\cdot W^{\beta}\subset W^{\alpha\beta}\ ,
$$
的模，其中 $\alpha,\beta=\pm$。一个重要的分次来自相应自旋群的手征分次。给定定向向量空间 $V$ 的一个正向、$q$-正交归一基 $\Gamma_i$，我们通过手征元素
$$
\Gamma_c=\Gamma_1\cdots\Gamma_{r+s}\ .
$$
定义 $C\ell_{r,s}$ 的定向体积元 $\Gamma_c$。令 $n=r+s$，该体积元满足
$$
\begin{matrix}
(\Gamma_c)^2&=&(-1)^{\frac{n(n+1)}{2}+s}\ ,\\
x\,\Gamma_c&=&(-1)^[n-1]\,\Gamma_c\,x \ , \ \ \forall x\in{\mathbb{R}}^n\ ,
\end{matrix}
$$
这表明当 $n$ 为奇数时 $\Gamma_c$ 位于 $C\ell_{r,s}$ 的中心，而当 $n$ 为偶数时 $\Gamma_i\Gamma_c=\Gamma_c
\,\eta(\Gamma_i)$。因此当 $n$ 为偶数时，存在由 $\Gamma_c$ 的 $\pm 1$ 本征空间诱导的手征分次。

让我们先对实 Clifford 代数 $C\ell_{r,s}$ 的表示进行分类。该代数的实表示按显然的方式构造。另一方面，${\mathbb{C}}$-表示则如下构造。回顾复向量空间不过是一个实向量空间 $W$ 连同满足 $J^2=-{\mathrm Id}$ 的实线性映射 $J:W\rightarrow W$。于是 $C\ell_{r,s}$ 的复表示是一个与复结构交换的实表示 $\rho: C\ell_{r,s}\rightarrow {\mathrm
End}_{{\mathbb{R}}}(W)$：
$$
\rho(\phi)\circ J=J\circ\rho(\phi)\ .
$$
类似地可定义 $C\ell_{r,s}$ 的四元数表示。通过限制，代数 $C\ell_n$ 的表示给出自旋群的重要表示。$Spin(n)$ 的实旋量表示定义为同态
$$
\Delta_n: Spin(n)\longrightarrow GL_{\mathbb{R}}(W)\ ,
$$
它由把不可约实表示 $C\ell_n\rightarrow{\mathrm End}_{{\mathbb{R}}}(W)$ 限制到 $Spin(n)\subset C\ell_n$ 得到。可以证明当 $n\neq 0$ (mod 4) 时表示 $\Delta_n$ 或者不可约，或者是两个等价不可约表示的直和，而后一种情形恰在 $n\equiv 1$ 或 2 (mod 8) 时出现。在其余情形存在分解
$$
\Delta_{4m}=\Delta_{4m}^+\oplus\Delta_{4m}^-\ ,
$$
其中 $\Delta_{4m}^{\pm}=\frac12(1\pm\Gamma_c)\Delta_{4m}$ 是 $Spin(4m)$ 的不等价不可约表示。于是这些旋量模的实性性质便容易推出。唯一的实旋量模（更确切地说，唯一作为实表示之复化出现的模）是 $\Delta_{8k\pm1},\Delta_{8k}^\pm$，而表示 $\Delta_{8k+3},\Delta_{8k+4}^\pm,\Delta_{8k+5}$ 是四元数 Clifford 模的限制。其余模 $\Delta_{8k+2}^\pm,\Delta_{8k+6}^\pm$ 是复的。

我们可以类似地对复化 Clifford 代数 ${\mathbb{C}}\ell_n$ 的表示进行分类。我们把 $Spin(n)$ 的复表示定义为同态
$$
\Delta^{{\mathbb{C}}}_n: Spin(n)\longrightarrow GL_{{\mathbb{C}}}(W)\ ,
$$
它由把不可约复表示 ${\mathbb{C}}\ell_n
\rightarrow {\mathrm End}_{{\mathbb{C}}}(W)$ 限制到 $Spin(n)\subset{\mathbb{C}}\ell_n$ 得到。与实情形类似，可以证明当 $n$ 为奇数时表示 $\Delta_n^{{\mathbb{C}}}$ 不可约，而当 $n$ 为偶数时存在分解
$$
\Delta_{2m}^{{\mathbb{C}}}=\Delta_{2m}^{{\mathbb{C}} +}\oplus
\Delta_{2m}^{{\mathbb{C}} -}\ ,
$$
其中 $\Delta_{2m}^{{\mathbb{C}}\pm}=\frac12(1\pm i^m\,\Gamma_c)
\Delta_{2m}^{{\mathbb{C}}}$，即分解为 $Spin(n)$ 的两个不等价不可约复表示的直和。

最后我们来到与 K-理论的联系，这通过经典的 Atiyah-Bott-Shapiro (ABS) 构造 [abs] 实现，它把 Clifford 模的 Grothendieck 群与球面的 K-理论联系起来。为此我们将采用 2.6 节引入的相对 K-群 ${\mathrm K}(X,Y)$ 的定义，即等价类 $[E,F;\alpha]$ 构成的群，其中 $\alpha$ 是向量丛 $E$ 与 $F$ 限制到 $Y$ 上时的同构。设 ${\mathrm R}[Spin(n)]$ 是 $Spin(n)$ 的复表示环，即由不可约复表示生成的交换幺半群、关于 $Spin(n)$-模的直和与张量积所构造的 Grothendieck 群。（我们将在 6.1 节更一般地描述表示环。）设 $W=W^+\oplus W^-$ 是 Clifford 代数 $C\ell_n$ 上的 ${\mathbb{Z}}_2$-分次模。我们于是把元素
$$
\varphi(W)=[E^+,E^-;\mu]\in {\mathrm K}({\mathbf B}^n,{\mathbf S}^[n-1])\ ,
$$
联系到分次模 $W$，其中 $E^{\pm}\equiv {\mathbf B}^n\times W^{\pm}$ 是平凡乘积丛，而 $\mu:E^+\rightarrow E^-$ 是由 Clifford 乘法给出的 ${\mathbf S}^[n-1]$ 上的同构：
$$
\mu(x,w)\equiv (x,x\cdot w)\ \ , \ \ x\in {\mathbf S}^[n-1]\ .
$$
注意，由于球体 ${\mathbf B}^n$ 可缩，其上一切丛都平凡，全部拓扑都位于同伦非平凡映射 $\mu:E^+\rightarrow E^-$ 在 ${\mathbf S}^[n-1]$ 上的绕数之中。现在容易证明元素 $\varphi(W)$ 只依赖于分次模 $W$ 的同构类，而且映射 $W\mapsto\varphi(W)$ 是加性同态。因此映射（式）给出同态
$$
\varphi:{\mathrm R}\Bigl[Spin(n)\Bigr]
\longrightarrow {\mathrm K}({\mathbf B}^n,{\mathbf S}^[n-1])\ .
$$
通过限制，自然包含 $i:{\mathbb{R}}^n\hookrightarrow {\mathbb{R}}^{n+1}$ 诱导满同态 $i^*:{\mathrm R}[Spin(n+1)]\rightarrow {\mathrm R}[Spin(n)]$。于是同态（式）下降为同态 $\varphi_n:{\mathrm R}[Spin(n)]/i^*\,{\mathrm R}[Spin(n+1)]\rightarrow
{\mathrm K}({\mathbf B}^n,{\mathbf S}^[n-1])$，而后者结果是分次环同构 [abs]：
$$
{\mathrm R}\Bigl[Spin(n)\Bigr]\,/\, i^*\,{\mathrm R}\Bigl[Spin(n+1)\Bigr]
\stackrel{\approx}{\longrightarrow}\widetilde{{\mathrm K}}({\mathbf S}^[n])
$$
（式）中的群当 $n$ 为偶数时同构于 ${\mathbb{Z}}$，而当 $n$ 为奇数时按上述 Clifford 模的分类为零。同构（式）由 ${\mathbf S}^n$ 上的主 $Spin(n)$ 丛生成：
$$
Spin(n)\hookrightarrow Spin(n+1)\longrightarrow {\mathbf S}^n\ .
$$

这一定理还给出 $\widetilde{{\mathrm K}}({\mathbf S}^{2n})$ 的显式生成元，它们通过 Clifford 代数的表示来定义。例如，设 ${\mathcal S}={\mathcal S}^+\oplus{\mathcal S}^-$ 是 ${\mathbb{C}}\ell_{2n}$ 的基本 ${\mathbb{Z}}_2$-分次表示空间。存在同构 ${\mathrm R}[Spin(2n)]\cong{\mathbb{Z}}\oplus{\mathbb{Z}}$，其生成元由 ${\mathcal S}$ 及其“翻转” $\widetilde{\mathcal S}$ 给出，后者是交换了各因子的同一个分次模（这对应于 ${\mathbb{R}}^{2n}$ 中定向的反转）。于是 $i^*\,{\mathrm R}[Spin(2n+1)]\cong{\mathbb{Z}}_{\mathrm diag}$ 的生成元是 $[{\mathcal S}]+[\widetilde{\mathcal S}]$。因此群 $\widetilde{{\mathrm K}}({\mathbf
S}^{2n})={\mathbb{Z}}$ 由元素
$$
\varphi_{{\mathbb{C}}}^{(n)}=[{\mathcal S}^+,{\mathcal S}^-;\mu]\ ,
$$
生成，其中 $\mu_x:{\mathcal S}^+\rightarrow {\mathcal S}^-$ 表示用 $x\in{\mathbb{R}}^{2n}$ 作 Clifford 乘法。以 $\Gamma_i$ 记 ${\mathcal S}$ 的生成元，则包含 ${\mathbb{R}}^{2n}\hookrightarrow {\mathbb{C}}\ell_{2n}$ 连同 Clifford 乘法的定义（式）表明 $\mu_x$ 可由 $x=\sum_ix^i\,\Gamma_i\in{\mathbb{R}}^{2n}$ 的普通矩阵乘法表示：
$$
\mu_x(w)=\left(
\sum_{i=1}^{2n}x^i\,\Gamma_i\right)w\ \ , \ \ x^i\in{\mathbb{R}}\ .
$$
此外，由（式）可知同构 $\mu_x$ 的平方就是乘以向量 $x\in{\mathbb{R}}^{2n}$ 的范数：
$$
\mu_x\circ\mu_x(w)=-|x|^2\,w\ .
$$
注意球面的 Bott 周期性 $\widetilde{{\mathrm K}}({\mathbf S}^n)=\widetilde{{\mathrm K}}({\mathbf
S}^{n+2})$ 现在可由复化 Clifford 代数的周期性（式）导出。此外，利用 Clifford 模的结构，容易借助杯积证明
$$
\varphi_{{\mathbb{C}}}^{(n)}=\left(\varphi_{{\mathbb{C}}}^{(1)}
\right)^n\ .
$$

## Type IIB D-膜与 ${\mathrm K}(X)$

我们现在开始描述 K-理论在超弦理论中 D-膜荷分类方面的系统应用。本节先从 IIB 型理论开始，因为对它可作最简单的分析。II 型超弦是有向的，因此其 Chan-Paton 丛具有酉结构群。除了关于 D-膜的新的思考方式与构造方式之外，K-理论形式体系只是重现了已知的稳定膜荷谱。不过，我们下面给出的分析容易推广到更复杂的情形，在那里我们将看到 K-理论给出真正新的预言，而且它还提供了很好的自洽性检验，说明这一数学形式体系确实是正确的。

我们将在本节证明群 ${\mathrm K}(X)$ 分类了时空流形 $X$ 上 IIB 型超弦理论中的 D-膜 [witten]。更确切地说，IIB 型 D-膜的 RR 荷由其横向空间的 K-理论类来度量，因此例如 $\widetilde{{\mathrm K}}({\mathbf S}^n)$ 分类了平坦 ${\mathbb{R}}^{10}$ 上 IIB 型弦理论中的 $(9-n)$-膜。相应的 K-群由 2.7 节所述的同伦论确定：
$$
\widetilde{{\mathrm K}}({\mathbf S}^n)=\pi_{n-1}\Bigl(U(k)\Bigr)\ ,\ \ \ \ k>n/2\ .
$$
取归纳极限有
$$
\widetilde{{\mathrm K}}({\mathbf S}^n)=\pi_{n-1}\Bigl(U(\infty)\Bigr)\ ,
$$
其中 $U(\infty)=\bigcup_kU(k)$ 是无限酉群。Bott 周期性断言相应的同伦群 $\pi_n(U(\infty))$ 以 2 为周期：
$$
\pi_n\Bigl(U(\infty)\Bigr)=\pi_{n+2}\Bigl(U(\infty)\Bigr)\ ,
$$
或
$$
\widetilde{{\mathrm K}}({\mathbf S}^n)=\widetilde{{\mathrm K}}({\mathbf S}^{n+2})\ .
$$
由这一点以及 $\widetilde{{\mathrm K}}({\mathbf S}^0)={\mathbb{Z}}, \widetilde{{\mathrm K}}({\mathbf S}^1)=0$，可得 IIB 型超弦理论中 D-膜的完全分类，它总结于下表中。

表：由 $\widetilde{{\mathrm K}}({\mathbf S}^n)$ 得到的 IIB 型超弦理论中的 D-膜谱。

| D-膜 | D9 | D8 | D7 | D6 | D5 | D4 | D3 | D2 | D1 | D0 | D(--1) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 横向空间 | ${\mathbf S}^0$ | ${\mathbf S}^1$ | ${\mathbf S}^2$ | ${\mathbf S}^3$ | ${\mathbf S}^4$ | ${\mathbf S}^5$ | ${\mathbf S}^6$ | ${\mathbf S}^7$ | ${\mathbf S}^8$ | ${\mathbf S}^9$ | ${\mathbf S}^{10}$ |
| $\widetilde{{\mathrm K}}({\mathbf S}^n)$ | ${\mathbb{Z}}$ | 0 | ${\mathbb{Z}}$ | 0 | ${\mathbb{Z}}$ | 0 | ${\mathbb{Z}}$ | 0 | ${\mathbb{Z}}$ | 0 | ${\mathbb{Z}}$ |

该表只是反映了 IIB 型理论仅对奇数 $p$ 才有稳定 D$p$-膜这一事实。这样就重新得到了 IIB 型 BPS 膜荷的通常谱。


### 膜-反膜系统

D-膜荷的 K-理论描述背后的物理，关键在于用高维膜与反膜来重新解释膜。因此，我们首先简要回顾超弦理论中膜-反膜对的性质。该系统是不稳定的，原因是在那些从膜（相应地，反膜）出发、终止于反膜（相应地，膜）的开弦激发中存在一个快子模 [gbs]。看出这一性质的最简单方式，是借助边界态形式（参见 [divecchia] 及其中的参考文献）。一个稳定的超对称 D$p$-膜可以由如下边界态来代表和描述：

$$
|Dp\rangle=|Dp\rangle_{\mathrm{NS}}\pm |Dp\rangle_{\mathrm{RR}}\ ,
$$

它是*闭*弦理论希尔伯特空间中的一个特定相干态。它表示一个 D$p$-膜所发射的闭弦模的源。边界态（式）由一个部分 $|Dp\rangle_{\mathrm{NS}}$ 与一个属于 RR 扇区的部分 $|Dp\rangle_{\mathrm{RR}}$ 组成，前者是基本弦世界面 NS-NS 扇区的闭弦态的源。（式）中的相对符号把膜与其反膜区分开来，二者带有相反的 RR 荷。计入闭弦 GSO 投影后，得到如下分解：

$$
\begin{matrix}
|Dp\rangle_{\mathrm{NS}}&=\frac{1}{2}\,\Bigl(|Dp,+\rangle_{\mathrm{NS}}-
|Dp,-\rangle_{\mathrm{NS}}\Bigr)\ ,\\
|Dp\rangle_{\mathrm{RR}}&=\frac{1}{2}\,\Bigl(|Dp,+\rangle_{\mathrm{RR}}+
|Dp,-\rangle_{\mathrm{RR}}\Bigr)\ ,
\end{matrix}
$$

其中 $\pm$ 标记适用于 D$p$-膜的边界条件的两种可能实现。分解（式）计入了对弦世界面上四种自旋结构的求和。

边界态形式使我们能够容易地计算始于并止于一个 D$p$-膜上的开弦谱。这可以通过计算边界态与自身的树级两点函数（柱面振幅），并经由模变换把结果重新表达为开弦态上的一圈迹（环面振幅）来得到：

$$
\int\limits_0^{\infty}d\tau~\left\langle Dp,\alpha\left|
\,e^{-\pi\tau(L_0+\tilde{L}_0)}\right|Dp,\beta\right\rangle
=V_p\int\limits_0^{\infty}\frac{dt}{t}~{\mathrm Tr}_{\mathrm open}\left(e^{-2\pi
    tL_0}\right) \ ,
$$

其中 $V_p$ 是（无限的）世界体体积，$\alpha,\beta=\pm$。（式）中出现的开弦扇区既依赖于闭弦扇区，也依赖于自旋结构 $\alpha,\beta$。特别重要的是开弦 NS 与 NS$(-1)^F$ 偶自旋结构，它们分别对应于 $\alpha=\beta$ 的闭弦 NS-NS 与 RR 扇区。NS 扇区由此以通常的方式被 GSO 投影，即 NS-NS+RR=NS+NS$(-1)^F$。这导致众所周知的事实：对所有偶自旋结构贡献的求和为零，因此始于并止于一个 D$p$-膜上的开弦谱是超对称的，并且没有快子。

然而，如果我们转而考虑一个由一个 D$p$-膜和一个反-D$p$-膜（我们也将称之为 D$\overline{p}$-膜）组成的系统，那么 RR 扇区对（式）的贡献变号，而 NS 开弦扇区具有“错误”的 GSO 投影，即 NS-NS -- RR=NS--NS$(-1)^F$。开弦谱因此出现一个快子，这一事实正是膜-反膜对不稳定的原因。这一特征是该系统位于一个势阱顶部这一事实的推论，而正是 $p-\overline{p}$ 系统中这个快子场的存在，建立了与 K-理论的联系。

我们可以选取膜-反膜对的开弦 Chan-Paton 规范群 $U(2)$ 的一个合适基，在其中对角矩阵代表始于并止于同一膜或同一反膜的开弦激发，而非对角矩阵代表在膜与其反膜之间（取给定定向）伸展的弦态。于是，产生相应 $p-\overline{p}$ 快子开弦态的快子顶点算符为

$$
\begin{matrix}
V_T(z)&=e^{ik_aX^a(z)}\otimes\left(\begin{array}{cc}0 & 1\\ 0 &
  0\end{array}\right)\ ,\\
V_{T^\dagger}(z)&=e^{ik_aX^a(z)}\otimes\left(\begin{array}{cc}0 &
  0\\ 1 & 0\end{array}\right)\ ,
\end{matrix}
$$

其中 $X^a(z)$ 是世界面玻色场，$k_a$ 是沿 D$p$-膜世界体的动量。由（式）中 Chan-Paton 矩阵的结构可以立刻看出，唯一非零的关联函数是那些含有相同数目 $T$ 与 $T^\dagger$ 顶点算符的关联函数。若 $T(x)$ 与 $T^\dagger(x)$ 表示生活在 D$p$-膜与反-D$p$-膜系统世界体上的复快子场，则存在如下形式的快子势：

$$
V(TT^\dagger)=\sum_{n=2}^{\infty}c_n\left(TT^\dagger\right)^n \ .
$$

这意味着快子势只依赖于 $T$ 的模：

$$
V(T)=V(|T|^2)\ .
$$

非平凡快子势 $V(T)$ 的存在意味着，简单地叠加一个 D$p$-膜与一个 D$\overline{p}$-膜并不能达到稳定构型，因为该系统正坐在一个快子势阱的顶部。该系统的最低能量构型（即稳定构型）通过让快子滚落到其势的极小值 $T_0$ 而得到。由（式）可知，这些点位于由方程

$$
|T|=T_0 \ .
$$

所描述的圆上。注意，就*实*快子场 $t=T+T^\dagger$ 而言，快子势是 $t$ 的偶函数：

$$
V(t)=V(-t)\ ,
$$

而相应的极小值总是成对出现，即 $\pm\,t_0$。

此外，可以论证：当快子凝聚到其某个真空期望值时，凝聚体的负势能密度与 $p-\overline{p}$ 对的张力所伴随的正能量密度恰好相消：

$$
2{\mathcal T}_p+V(T_0)=0\ ,
$$

其中 ${\mathcal T}_p$ 是 $p$-膜张力。这表明快子基态与超对称真空构型不可区分，因为它既不带任何荷，也不带任何能量。于是，在这些情形下，膜-反膜对经由快子凝聚所达到的稳定构型不是别的，正是真空态。然而，除了考虑快子基态之外，人们还可以在膜-反膜世界体上构造快子孤子解。这将在下一小节中进行，那里我们将看到 K-理论形式的一个惊人特征：它为经典快子孤子场 $T(x)$ 提供了一个非常显式的形式。

上面所描述的 GSO 投影的反转可以如下形式化。$p-\overline{p}$ 对的开弦激发的端点带有一个荷，该荷取值于一个二维量子希尔伯特空间。这种波函数的第一分量可视为玻色的，代表（比如说）终止于 $p$-膜上的开弦；而第二分量是费米的，代表终止于 $\overline{p}$-膜上的开弦。$p-\overline{p}$ 开弦具有非对角的 Chan-Paton 波函数，它们在算符

$$
(-1)^F=\sigma_3=\left(\begin{array}{cc}1
& 0\\ 0 &- 1\end{array}\right)\ ,
$$

的伴随作用之下为奇，因此被 GSO 投影算符

$$
P_{\mathrm GSO}=\frac12\,\Bigl(1+(-1)^F\Bigr)
$$

所移除。另一方面，$p-p$ 与 $\overline{p}-\overline{p}$ 开弦具有对角的 Chan-Paton 波函数。它们在 $(-1)^F$ 下为偶，因此被 GSO 投影（式）选出。具有一个玻色与一个费米 Chan-Paton 态，导致带有规范超群 $U(1|1)$ 的 $p-\overline{p}$ 世界体规范对称性。然而，由于 GSO 投影，$U(1|1)$ 的非对角费米规范场并不存在，从而导致无质量矢量多重态以通常的方式被消去。$p-\overline{p}$ 世界体上剩余的玻色场反而构成一种结构，其最低模对应于 $X$ 上的超联络 [quillen]：

$$
{\mathcal A}=\left( \begin{array}{cc}A^+ & T\\ T^{\dagger} &A^-
\end{array}\right)\ ,
$$

其中 $A^\pm$ 分别是 $p$-膜与 $\overline{p}$-膜的玻色与费米 Chan-Paton 态的丛 $E$ 与 $F$ 上的规范场。$p-\overline{p}$ 快子场 $T$ 被视为一个映射 $T:E\rightarrow F$，而其伴随之 $T^{\dagger}$ 是一个映射 $T^{\dagger}: F\rightarrow E$。或者，$T$ 可视为 $E\otimes F^*$ 的一个截面，$T^{\dagger}$ 为 $E^*\otimes F$ 的一个截面，其中 $E^*={\mathrm Hom}_{\mathbb{C}}(E,\mathbb{C})$ 是 $E$ 的对偶矢量丛。超联络（式）最近在 [kenwil] 中被用于把 RR 场与世界体规范场的通常 Wess-Zumino 耦合推广到膜-反膜系统（另见 [bcr]）。当我们在第 7 节讨论指标理论时，它将起关键作用。


## 束缚态构造

我们下面将讨论如何构造快子孤子解，并说明这种构造等价于 ABS 同态——它把 ${\mathrm K}(Y)$ 中的类映到 ${\mathrm K}(X)$ 中的类，其中 D-膜缠绕在时空 $X$ 的子流形 $Y$ 上。在第 7 节之前，我们只处理平坦时空以及拓扑平凡的世界体积嵌入 $Y\hookrightarrow X$。我们先在 Type IIB 超弦理论中把一个稳定的 $p$-膜构造为一个 $(p+2)$-膜与一个与之重合的 $\overline{(p+2)}$-膜的束缚态。为此，我们考虑一对伸展在子流形 ${\mathbb{R}}^{p+3}\subset X$ 上的无穷大 $(p+2)$ 膜-反膜对。由于快子的存在，除非存在某种拓扑障碍，这个系统倾向于自我湮灭。这一障碍由 K-理论群 ${\mathrm K}(X)$ 来度量。

在 $(p+2)-\overline{(p+2)}$ 对上，存在一个 $U(1)\times U(1)$ 规范场 $(A^+,A^-)$ 以及一个带相应荷 $(1,-1)$ 的快子场 $T$。这意味着世界体积场论中快子场的动能项具有形式 $|(\partial_i-iA_i^++iA_i^-)T|^2$。我们考虑一个涡旋，其中 $T$ 在一个余维为二的子流形 ${\mathbb{R}}^{p+1}\subset {\mathbb{R}}^{p+3}$ 上取零值，我们把这个子流形解释为 $p$-膜的世界体积。我们假定当 $|x|\rightarrow \infty$ 时 $|T(x)|$ 趋于其真空期望值 $T_0$（在差一个规范变换的意义下）。$T$ 是一个复标量场，因此它可以绕其取零值的余维 2 轨迹（等价地，在 $|x|=\infty$ 处）带有绕数。最基本的情形是绕数为 1，此时 $T$ 把膜-反膜对的 $U(1)\times U(1)$ 规范对称性破缺到对角 $U(1)$ 子群。为使单位 $p$-膜世界体积的能量有限（即有有限的张力），破缺后的 $U(1)$ 群中必须有一单位磁通，这可以通过给 $(p+2)-\overline{(p+2)}$ 对世界体积上的规范场 $A^+-A^-$ 在无穷远处赋予一单位拓扑荷来实现。因此非零的渐近场位形取如下形式

$$
T\simeq T_0~\mbox{e}^{i\theta}~~~,~~~A_\theta^+-A_\theta^-\simeq1~~~~~~{\mathrm for}
{}~~r\to\infty \ ,
$$

其中 $(r,\theta)$ 是二维横向空间 ${\mathbb{R}}^{p+3}-{\mathbb{R}}^{p+1}$ 上的极坐标。于是世界体积场论中的动能项与势能项在 $r\to\infty$ 时都衰减得足够快，从而给出快子场的一个静态有限能量的涡旋位形。这个系统带有一单位的 $p$-膜荷，但在膜与反膜之间其 $(p+2)$-膜荷为零。由于 $T$ 除在涡旋核心 ${\mathbb{R}}^{p+1}$ 附近之外处处趋于其真空期望值，系统除在 $T$ 取零值的轨迹附近之外处处看起来像真空。这个孤子因而描述了 Type IIB 弦论中一个稳定的、有限能量的 $p$-膜。通过研究描述这个解的边界共形场论，可以证明这个孤子与 Type IIB 超弦理论中的 D$p$-膜不可区分，它只是时空 $X$ 中同一拓扑缺陷的另一种表示。

很容易把这个构造推广到 $k>1$ 的 $(p+2k)$ 膜-反膜对。我们先由一对 $(p+2)$ 膜-反膜构造出 $p$-膜，再把其中的 $(p+2)$ 膜与反膜分别构造为一对 $(p+4)$ 膜-反膜的束缚态，如此继续。再经过 $k-2$ 步之后，我们就得到由 $2^[k-1]$ 对 $(p+2k)$-膜与反膜构成的 $p$-膜。然而，这种“逐步”的束缚态构造破坏了明显的时空对称性，并限制了这一形式体系可能的应用。我们希望能有一种直接展示系统全部对称性的构造。K-理论的形式体系恰恰在这里起核心作用。

为把这些构造与 K-理论联系起来，我们回顾第 1 节：使 tadpole 反常相消的 Type IIB $9-\overline{9}$-膜位形的 D-膜荷，由时空 $X$ 的约化 K-理论群 $\widetilde{{\mathrm K}}(X)$ 分类。$\widetilde{{\mathrm K}}(X)$ 中的每个类由数目相等的 $N$ 个 9-膜与 $N$ 个缠绕 $X$ 的 $\overline{9}$-膜代表，${\mathrm K}(X)$ 中的类则由 9-膜与 $\overline{9}$-膜上 Chan-Paton 规范丛之差 $[E]-[F]$ 给出。终结于这些膜一切可能配对上的开弦给出一个 $U(N)\times U(N)$ 规范场，以及一个处于规范群双基本表示 ${\mathbf N}\otimes\overline{\mathbf N}$ 中的快子场 $T$。虽然我们不知道快子势的确切形式，但可以论证在极小点 $|T|=T_0$ 处 $T_0$ 的所有本征值都相等。这来自把膜-反膜对分离开的可能性。于是快子凝聚 $T_0$ 把世界体积规范对称性从 $U(N)\times U(N)$ 破缺到对角 $U(N)$ 子群。

我们现在把 Type IIB 理论的一个稳定 D-膜构造为 $N$ 个 9-膜与 $N$ 个 $\overline{9}$-膜组成的系统的束缚态，该系统在 $Y$ 附近局部地像一个拓扑稳定的快子场涡旋。数目 $N$ 稍后将由 ABS 构造的数学确定。$T_0$ 的稳定值（即能量极小的快子场的规范轨道）活于真空流形

$$
{\mathcal V}_{\mathrm IIB}(N)=\frac{U(N)\times U(N)}{U(N)_{\mathrm diag}}\cong U(N)\ .
$$

因此，当把 $T$ 看作这一描述中的 Higgs 场时，它支持余维 $2k$ 的稳定拓扑缺陷，这些缺陷由真空流形的非平凡同伦群分类：

$$
\pi_{2k-1}\Bigl({\mathcal V}_{\mathrm IIB}(N)\Bigr)= \pi_{2k-1}\Bigl(U(N)\Bigr)=
{\mathbb{Z}}\ , \ \ \ \ N>k\ .
$$

于是对于一个缠绕子流形 ${\mathbb{R}}^{p+1}\subset X$ 的 $p$-膜，我们取 $T(x)$ 在余维 $2k=9-p$ 上取零值，并让它在 $|x|\rightarrow \infty$ 时趋于其真空轨道，在它取零值的轨迹 ${\mathbb{R}}^{p+1}$ 周围带有非零的拓扑扭曲，并在无穷远处具有给定的绕数。这些位形按映射 ${\mathbf S}^{2k-1}\rightarrow U(N)$ 的同伦类、或按 K-理论类作拓扑分类：

$$
\widetilde{{\mathrm K}}({\mathbf S}^{2k})= \pi_{2k-1}\Bigl(U(N)\Bigr)= {\mathbb{Z}}\ , \ \ \ \
\forall N>k\ .
$$

注意 D-膜荷是由世界体积的横向空间（通过添加无穷远点而紧致化）的约化 K-群标记的。这个结果使同伦理论（即拓扑缺陷的分类）与 K-理论（即充满时空的膜的位形在相差对产生与湮灭下的分类）之间的关系变得显然。正如上一小节所讨论的，对应于 $T$ 的真空凝聚的负能量密度，与缠绕 $X$ 的 $9-\overline{9}$ 膜系统非零张力带来的正能量密度大小相等。这意味着离束缚态核心远处总能量密度迅速趋于零，位形非常接近超对称真空。因此，快子凝聚留下了一个缠绕在 $Y={\mathbb{R}}^{p+1}$ 上的客体，它携带缠绕 $Y$ 的超对称 D$p$-膜的荷。

嵌入 ${\mathrm K}(Y)\hookrightarrow {\mathrm K}(X)$ 在数学上由第 2.8 节描述的 K-理论 ABS 构造实现。（这是一个前推映射的例子，我们将在第 7 节回到它。）它对应于把描述缠绕 $Y$ 的 D-膜的非平凡类映到一个类，在其中它对应于缠绕时空 $X$ 的 9-膜 $\overline{9}$-膜位形的束缚态。对于 $X$ 中余维 $2k$ 的 $Y$，这个构造选出 $9-\overline{9}$-膜对数目所偏好的值 $N=2^[k-1]$（回忆这正是先前“逐步”构造的预言），而且它通过 Clifford 乘法给出快子涡旋位形（即 $\pi_{2k-1}(U(N))$ 的生成元）一个特别简单、自然且有用的表示。考虑横向空间的旋转群 $SO(2k)$，它是 $Y\subset X$ 的法丛的保向自同构群。它有两个不等价的正、负手征复旋量表示 $\Delta_{2k}^{{\mathbb{C}}\pm}$，其维数为 $2^[k-1]$。它们给出两个旋量丛 ${\mathcal S}^{\pm}\rightarrow Y$，后者可以延拓到 $X$ 中 $Y$ 的一个邻域（模掉某些整体障碍，我们将在第 7 节描述）。因此它们定义一个 K-理论类 $[{\mathcal S}^+]-[{\mathcal S}^-]\in \widetilde{{\mathrm K}}(X)$，其中 $E={\mathcal S}^+$ 是 9-膜所携带的 Chan-Paton 丛，$F={\mathcal S}^-$ 是上述束缚态构造中 $\overline{9}$-膜所携带的丛。

9-膜世界体积 $X$ 的规范对称性是 $U(2^[k-1])\times U(2^[k-1])$，而快子场是一个映射 $T: {\mathcal S}^+\rightarrow {\mathcal S}^-$。设 $\Gamma_1, \ldots , \Gamma_{2k}$ 为 $\Delta_{2k}^{{\mathbb{C}}+}\oplus\Delta_{2k}^{{\mathbb{C}}-}$ 的生成元，它们可以看作映射 ${\mathcal S}^+\oplus {\mathcal S}^- \rightarrow {\mathcal S}^+\oplus {\mathcal S}^-$。设 $(x^1,\ldots , x^{2k})\in {\mathbf S}^{2k-1}\subset{\mathbb{R}}^{2k}$。那么，利用第 2.8 节的构造，我们通过 Clifford 乘法定义快子场

$$
T(x)=f(x)\,\mu_x=f(x)\,\sum_{i=1}^{2k}\Gamma_i\,x^i\ ,
$$

其中 $f(x)$ 是一个收敛因子，具有渐近行为

$$
\lim_{x\in Y}f(x)={\mathrm const.}~~~~~~,~~~~~~
\lim_{|x|\rightarrow\infty}f(x)=\frac{T_0}{|x|}\ ,
$$

它保证在离涡旋核心远处 $T(x)$ 取值于 IIB 真空流形（式），而快子孤子定域在子流形 $x^i=0, i=1,\ldots, 2k$ 上。下文我们通常不显式写出这种收敛因子。场 $T(x)$ 的绕数为 1 [bfn]，并且按照 ABS 构造，它生成 $\pi_{2k-1}(U(2^[k-1]))= {\mathbb{Z}}$，或等价地 ${\mathrm K}({\mathbf B}^{2k},{\mathbf S}^{2k-1})={\mathbb{Z}}$。

K-理论类的精确映射 ${\mathrm K}(Y)\hookrightarrow {\mathrm K}(X)$ 由杯积（式）给出：

$$
\begin{matrix}
\lambda\,:\,\widetilde{{\mathrm K}}(Y)\otimes_{\mathbb{Z}}
{\mathrm K}({\mathbf B}^{2k},{\mathbf S}^{2k-1})&\stackrel{\approx}{\longrightarrow}
{\mathrm K}(Y\times{\mathbf B}^{2k},Y\times{\mathbf S}^{2k-1})\\
\Bigl[(E\,,\,F)\Bigr]&\longmapsto
\lambda\left[(E\otimes{\mathcal S}^+
\oplus F\otimes{\mathcal S}^-\,,\,E\otimes{\mathcal S}^-\oplus
F\otimes{\mathcal S}^+)\right]
\end{matrix}
$$

其中 $[(E,F)]\in\widetilde{{\mathrm K}}(Y)$，并且我们用到了任意 $m$ 的 ${\mathrm K}({\mathbf S}^m)$ 都是自由阿贝尔群这一事实。

可以验证，这种“一次性”构造等价于先前“逐步”构造。这一事实来自复化 Clifford 代数的周期性性质（式），或等价地来自复 K-理论的 Bott 周期性。也就是说，把 $p$-膜 $\overline{p}$-膜对的束缚态经快子凝聚变成 $p-2$-膜的过程，可以看作时空 K-理论群 $\widetilde{{\mathrm K}}(X)\rightarrow \widetilde{{\mathrm K}}(X)$ 上的 Bott 周期性同构，后者又可借助 ABS 映射描述为

$$
\begin{matrix}
\left[({\mathcal S}_{2k}^+\,,\,{\mathcal S}_{2k}^-)\right]&\longmapsto&\left[\left({\mathcal S}_{2k}^+\otimes({\mathcal S}_2^+\oplus{\mathcal S}_2^-)\,,\,{\mathcal S}_{2k}^-\otimes({\mathcal S}_2^+\oplus{\mathcal S}_2^-)\right)\right]\\
T_{2k}&\longmapsto&\begin{pmatrix}T_{2k}\otimes {\mathbb{I}}_2&{\mathbb{I}}_{2k}\otimes T_2^\dagger\\ {\mathbb{I}}_{2k}\otimes T_2&-T_{2k}^\dagger\otimes {\mathbb{I}}_2\\\end{pmatrix}\ ,
\end{matrix}
$$

其中 ${\mathbb{I}}_N$ 表示 $N\times N$ 单位矩阵，$[{\mathcal S}_{2k}^+,{\mathcal S}_{2k}^-;T_{2k}]$ 是上面的 $\widetilde{{\mathrm K}}(X)$ 的生成元。这里

$$
T_2(x)=\sigma_1\,x^1+\sigma_2\,x^2=
\left( \begin{array}{cc}0 & x^1+ix^2\\
x^1-ix^2&0
\end{array}\right)
$$

是余维 2 的快子场，它生成真空流形 ${\mathcal V}_{\mathrm IIB}(1)=\frac{U(1)\times U(1)}{U(1)_{\mathrm diag}}\cong U(1)$ 的稳定同伦群；而 $\sigma_i$ 始终表示标准的 $SU(2)$ Pauli 自旋矩阵。另外，如第 2.5 节末尾所示，$p-2$-膜可以等同于 $p-\overline{p}$-膜世界体积中的一个 Dirac 磁单极涡旋 [trautman]。这一等同与世界体积孤子的拓扑稳定性 $\pi_1(U(1))={\mathbb{Z}}$ 相容。此外，它还把世界体积场论中规范场位形的显式形式确定为 [wuyang]

$$
A_\phi^\pm=0~~~~~~,~~~~~~A_\theta^\pm=\pm\,\frac{1\mp\cos\phi}{\sin\phi}
$$

其中 $(\theta,\phi)$ 是横向空间 ${\mathbf S}^2$ 上的角坐标，而膜-反膜指标 $\pm$ 现在标记相应的上、下半球 ${\mathbf S}_\pm^2$。

因此，上述位形的 $p$-膜荷等于一，而所有更高维与更低维的荷都为零（这也可借助规范场诱导的膜荷公式来验证）。注意 $T: E\rightarrow F$ 在无穷远处是平凡的（那里系统类似真空），并且在无穷远处的一个邻域内是同构 $E\cong F$。这意味着 K-理论类 $[(E,F)]$ 被假定为在无穷远处与真空等价，即人们可以通过无穷远处的快子凝聚弛豫到真空。因此，给定超对称真空位形的激发的 RR 荷，最好通过从其 K-理论类中减去真空的 K-理论类来度量。于是真空激发的 RR 荷取值于具有紧支集的 K-理论中。

## Type IIA 的 D-膜与 ${\mathrm K}^{-1}(X)$

本节我们将说明，Type IIA 超弦理论中的 D-膜荷由高阶 K-群 ${\mathrm K}^{-1}(X)$ 分类 [witten, horava]。我们仍然只是复现 Type IIA 理论众所周知的谱，但我们将对 D-膜的构造以及 Type II 各理论中膜之间的相互关系获得许多新见解。此外，我们还将发现束缚态构造的一些值得注意的应用。

### 群 ${\mathrm K}^{-1}(X)$

${\mathrm K}^{-1}(X)$ 有许多等价定义，每一种都在不同情形下有用。11 维的“M-理论”定义已在第 2.4 与 2.5 节给出。在这个定义中，高阶 K-群 ${\mathrm K}^{-1}(X)$ 是 $\widetilde{{\mathrm K}}(X\times {\mathbf S}^1)$ 中分类十维时空 $X$ 上 Type IIA 弦论 RR 荷的子群。因此很自然地想把这里的 ${\mathbf S}^1$ 解释为在联系 11 维 M-理论与十维 Type IIA 超弦理论时所用的紧化圆。然而，并不存在充满时空的 M-膜，即不存在已知的 10-膜，M-理论中也不存在膜的层级结构。所以目前还不清楚如何解释分类 Type IIA 弦论 D-膜荷所需的 $X$ 的十一维延拓。正是出于这些物理上的理由，人们希望有群 ${\mathrm K}^{-1}(X)$ 的其他表述。

${\mathrm K}^{-1}(X)$ 的“弦论”定义，即不涉及 $X$ 的 11 维延拓的定义，类似于第 2.6 节引入的相对 K-理论的定义，可以陈述如下。设 $E\in{\mathrm Vect}(X)$，并设 $\alpha: E\stackrel{\approx}{\longrightarrow} E$ 是向量丛 $E$ 的一个自同构。若存在向量丛同构 $h:E\stackrel{\approx}{\longrightarrow} F$ 使下图交换，则称两个对 $(E,\alpha)$ 与 $(F,\beta)$ 同构：

$$
{\begin{array}{ccc}
E&\stackrel{h}{\longrightarrow}&F\\&
&\\{\scriptstyle\alpha}\downarrow& &\downarrow{\scriptstyle\beta}\\&
&\\E&\stackrel{h}{\longrightarrow}&F\end{array}}
$$

即 $\beta\circ h=h\circ\alpha$。用 $(E\oplus F, \alpha\oplus\beta)$ 定义两个对 $(E,\alpha)$ 与 $(F,\beta)$ 的和。若 $\alpha$ 在 $E$ 的自同构中同伦于 ${\mathrm Id}_{E}$，则称对 $(E,\alpha)$ 是初等的。若存在两个初等对 $(G,\gamma)$ 与 $(H,\delta)$ 使得

$$
(E\oplus G,\alpha\oplus\gamma)\cong
(F\oplus H, \beta\oplus\delta)\ .
$$

则称两个对 $(E,\alpha)$ 与 $(F,\beta)$ 等价，记作 $(E,\alpha) \sim (F,\beta)$。对的等价类 $[(E,\alpha)]$ 的集合定义一个阿贝尔群，它正是 ${\mathrm K}^{-1}(X)$。类 $[(E,\alpha)]$ 的逆是 $-[(E,\alpha)]=[(E,\alpha^{-1})]$。为证明这一点，我们需要说明 $(E\oplus E,\alpha\oplus\alpha^{-1})$ 是初等对，为此可以写出

$$
\alpha\oplus\alpha^{-1}=\left( \begin{array}{cc}\alpha & 0\\
0&\alpha^{-1}\end{array}\right)=
\left(\begin{array}{cc}0 & -\alpha\\ \alpha^{-1}&0
\end{array}\right)
\left(\begin{array}{cc}0 & 1\\ -1&0\end{array}\right)\ .
$$

利用分解

$$
\left(\begin{array}{cc}0 & -\alpha\\ \alpha^{-1}&0\end{array}\right)
=\left(\begin{array}{cc}1 & -\alpha\\ 0&1\end{array}\right)
\left(\begin{array}{cc}1 & 0\\ \alpha^{-1}&1\end{array}\right)
\left(\begin{array}{cc}1 & -\alpha\\ 0&1\end{array}\right)\ ,
$$

我们可以定义连续映射 $\sigma:[0,1]\rightarrow {\mathrm Aut}(E\oplus E)$ 为

$$
\sigma(t)=\left(\begin{array}{cc}1 & -t\alpha\\ 0&1\end{array}\right)
\left(\begin{array}{cc}1 & 0\\ t\alpha^{-1}&1\end{array}\right)
\left(\begin{array}{cc}1 & -t\alpha\\ 0&1\end{array}\right)
$$

其中 $\sigma(0)={\mathrm Id}_{E\oplus E}$，而 $\sigma(1)$ 与（式）相符。由此可知（式）在 $E\oplus E$ 的自同构中同伦于 ${\mathrm Id}_{E\oplus E}$，从而 $\alpha\oplus\alpha^{-1}$ 也如此。更一般地，可以证明 $[(E,\alpha)]+[(E,\beta)]=[(E,\alpha\circ\beta)]=[(E,\beta\circ\alpha)]$。注意第 2.6 节中关于相对 K-理论的类似陈述可以用同样的方式证明。

为说明这个阿贝尔群确实是 ${\mathrm K}^{-1}(X)$，我们只需证明：两个自同构 $\alpha,\beta$ 确定 ${\mathrm K}^{-1}(X)$ 中的同一个类，即 $[(E,\alpha)]=[(F,\beta)]$，当且仅当存在向量丛 $G\in {\mathrm Vect}(X)$ 使得 $\alpha\oplus {\mathrm Id}_{F}\oplus {\mathrm Id}_{G}$ 与 ${\mathrm Id}_{E}\oplus \beta \oplus {\mathrm Id}_{G}$ 在 $E\oplus F\oplus G$ 的自同构中同伦。为此，我们先证明：$[(E,\alpha)]=0$ 当且仅当存在向量丛 $G\in{\mathrm Vect}(X)$ 使得 $\alpha\oplus {\mathrm Id}_{G}$ 在 $E\oplus G$ 的自同构中同伦于 ${\mathrm Id}_{E\oplus G}$。的确，若 $[(E,\alpha)]=0$，则存在初等对 $(G,\gamma)$ 与 $(G',\gamma')$ 以及同构 $h:E\oplus G\stackrel{\approx}{\longrightarrow}G'$，使下图交换：

$$
{\begin{array}{ccc}
E\oplus G&\stackrel{h}{\longrightarrow}&G'\\&
&\\{\scriptstyle\alpha\oplus\gamma}\downarrow& &
\downarrow{\scriptstyle\gamma'}\\&
&\\E\oplus G&\stackrel{h}{\longrightarrow}&G'\end{array}}
$$

于是 $\alpha\oplus {\mathrm Id}_G$ 同伦于 $\alpha\oplus\gamma=h^{-1}\circ\gamma'\circ h$。后者又同伦于 $h^{-1}\circ{\mathrm Id}_{G'}\circ h={\mathrm Id}_{E\oplus G}$，这就证明了该断言。逆命题是显然的。回到原来的断言，我们考虑满足 $[(E,\alpha)]=[(F,\beta)]$ 的两个类。那么 $[(E,\alpha)]-[(F,\beta)]=[(E\oplus F,\alpha\oplus\beta^{-1})]=0$，并且正如刚才所论证的，存在向量丛 $G$ 使 $\alpha\oplus\beta^{-1}\oplus {\mathrm Id}_G$ 同伦于 ${\mathrm Id}_{E\oplus F\oplus G}$。把这一同伦等价与 ${\mathrm Id}_E\oplus\beta\oplus{\mathrm Id}_G$ 复合，即可看出 $\alpha\oplus{\mathrm Id}_F\oplus{\mathrm Id}_G$ 与 ${\mathrm Id}_E\oplus\beta\oplus{\mathrm Id}_G$ 同伦。逆命题同样是显然的。

这一 ${\mathrm K}^{-1}(X)$ 的“弦论”定义以及上面描述的性质，可以推广为与任何作为阿贝尔幺半群的范畴 ${\mathcal C}$ 相联系的高阶 Grothendieck 群 ${\mathrm K}^{-1}({\mathcal C})$。我们关于 ${\mathrm K}^{-1}(X)$ 的第三个、也是最后一个定义，把“M-理论”定义与“弦论”定义联系起来，从而表明它们精确等价。再次回到 ${\mathrm K}^{-1}(X)$ 作为 $\widetilde{{\mathrm K}}(X\times{\mathbf S}^1)$ 的子群的定义，我们把 $(E,\alpha)$ 等同于 $(E_{\alpha},E_{{\mathrm Id}_{E}})$，其中 $E_{\alpha}$ 是 ${\mathbf S}^1\times X$ 上的向量丛，其全空间为 $[0,1]\times E$ 模去对所有 $v\in E$ 的等同 $(0,v)\equiv(1,\alpha(v))$。

为把 ${\mathrm K}^{-1}(X)={\mathrm K}(\Sigma X)$ 与同伦理论联系起来，我们使用第 2.7 节（式）之后所陈述的观察。由此可知存在自然同构

$$
{\mathrm K}^{-1}(X)=\Bigl[X\,,\,U(\infty)\Bigr]\ ,
$$

其中 $U(\infty)=\bigcup_{k=1}^{\infty}U(k)$ 是无限酉群。特别地，可以证明

$$
{\mathrm K}^{-1}({\mathbf S}^n)= \pi_{n-1}\Bigl({\mathrm Gr}(k,2k;{\mathbb{C}})
\Bigr)\ , \ \ \ \ k>n\ ,
$$

其中

$$
{\mathrm Gr}(k,2k;{\mathbb{C}})=\frac{U(2k)}{U(k)\times U(k)}\ ,
$$

而 $k>n$ 定义了 ${\mathrm K}^{-1}(X)$ 的稳定范围。


### IIA 型弦理论中的不稳定 9-膜

为了把 IIA 型理论中的超对称 $p$-膜描述为时空 $X$ 的某个 K-理论群的元素，我们不得不转而考察不稳定 9-膜的束缚态。如果我们放宽通常的要求——即 D-膜保持原初超对称的一半，并携带一单位相应的 RR 荷——那么 $p$ 为奇数的 IIA 型 $p$-膜就被允许存在，特别地我们就有了填满时空的 9-膜。这些态是超弦理论中非超对称的不稳定激发，因为连接一个 9-膜到自身的开弦谱中总是存在一个快子。因此 IIA 型的 9-膜高度不稳定，我们预期它们应当通过填满时空的世界体上的快子凝聚而迅速衰变到超对称真空（相应的 IIA 型超引力中没有 RR 场会与任何此类守恒荷耦合）。

但和前面一样，不稳定的 D-膜位形可以携带低维的 D-膜荷，于是当快子滚落到其势能的最低点、该态衰变时，它留下一个与真空相差一个低维 D-膜荷的超对称态，也就是说该态衰变为一个超对称的 D-膜位形，从而可以把一个超对称 D-膜态表示为原始不稳定膜系统的束缚态。

注意，利用上一节的构造，可以用 8-膜与 $\overline{8}$-膜的束缚态给出一种表示。然而这样的构造并不可取，因为它破坏了部分显式的时空对称性（体现在对 $X$ 的 8-膜世界体子流形的选择上），并且限制了以此方式所能研究的膜的动力学。因此我们将给出一种保持全部时空对称性显式的弦论构造。

D9-膜的边界态 $|D9\rangle$ 作为 IIA 型闭弦 Hilbert 空间中的相干态，具有如下形式
$$
|D9\rangle=|D9,+ \rangle_{{\mathrm NS}}-|D9,-\rangle_{{\mathrm NS}}\ ,
$$
其中 $|D9,\pm\rangle_{{\mathrm NS}}$ 是在 $X$ 的全部时空坐标上施加 Neumann 边界条件的两种可能实现。由于
$$
(-1)^{F_{L,R}}|D9,\pm\rangle_{{\mathrm R}}=|D9,\mp\rangle_{{\mathrm R}}\ ,
$$
态 $|D9,\pm\rangle_{{\mathrm R}}$ 的任何组合都不在 IIA 型 GSO 投影算符 $\frac14(1-(-1)^{F_L})(1+(-1)^{F_R})$ 下不变，因此 D9-膜边界态中没有 RR 分量。但这只意味着没有 RR 快子（tadpole），因而对 IIA 型的 9-膜不会出现与 RR tadpole 相关的时空反常；也就是说，与 IIB 型的情形不同（那里 9-膜的数目必须等于 $\overline{9}$-膜的数目），IIA 型 9-膜的数目不受任何限制。此外，9-膜不携带守恒荷，在 IIA 型中 9-膜与 $\overline{9}$-膜之间没有区别。

在环面振幅 $\langle D9|D9\rangle$ 的开弦道中没有 GSO 投影，因此在 NS 扇区中，连接一个 9-膜到自身的开弦将同时包含超对称 D-膜会含有的 $U(1)$ 规范场 $A_{\mu}$，以及对于超对称膜本会被 GSO 投影消除的快子场 $T$。此外，在开弦的 Ramond 扇区中，基态旋量的两种时空手征性 $\mathrm{ch}i, \mathrm{ch}i'$ 都被保留。我们可以把这一构造推广到 $N$ 个重合 9-膜的情形。此时无质量态与快子态的自由开弦谱给出填满时空的世界体上如下的低能场内容：一个 $U(N)$ 规范场 $A_{\mu}$，一个处于 $U(N)$ 伴随表示中的快子场 $T$，以及两个处于 $U(N)$ 伴随表示中、时空手征性相反的手征费米子场 $\mathrm{ch}i,\mathrm{ch}i'$。这可以与 IIB 型的情形相比较：那里 $N$ 对 9-膜与 $\overline{9}$-膜给出的谱由一个 $U(N)\times U(N)$ 规范场和一个处于 $U(N)\times U(N)$ 双基本表示中的快子场组成。

注意 $N=1$ 的情形是“退化”的，将在后面第 4.4 节中单独处理。还要注意，IIA 型超弦理论中 $N$ 个 9-膜上的场内容与一个 11 维系统的十维分解相符：$A_M=(A_{\mu},T)$ 是一个 11 维的 $U(N)$ 规范场，$\Psi=(\mathrm{ch}i,\mathrm{ch}i')$ 是一个处于 $U(N)$ 伴随表示中的 32 分量旋量场。这表明最低的开弦态具有隐藏的 11 维对称性。它暗示了与 M-理论的可能联系，这与上一小节中所描述的 K-群 ${\mathrm K}^{-1}(X)$ 的性质相一致。

考虑 IIA 型超弦理论中 $N$ 个 9-膜的位形，允许 9-膜从真空中产生与湮灭到真空。一个{\it 基本}的 9-膜位形是指迅速衰变到超对称真空、因而不包含任何低维 D-膜荷的位形。任何缠绕时空 $X$ 的 $N'$ 个 9-膜的基本位形都给出一个 $U(N')$ 丛 $F$，连同 $F$ 上的一个 $U(N')$ 规范场 $A$，以及一个处于 $U(N')$ 伴随表示中的快子场 $T$。低维 D-膜荷的有无由此由快子凝聚 $T_0$ 来度量。于是，和前面一样，我们假定带有快子场 $T$ 的丛 $E$ 可以通过只涉及 9-膜产生与湮灭的过程形变为一个同构于 $E\oplus F$ 的丛，其中 $F$ 是某个基本 9-膜位形的 Chan-Paton 丛。

因此我们考虑带快子凝聚的 9-膜的等价类集合，允许基本 9-膜位形从真空中产生与湮灭到真空。一个 9-膜位形由此定义了一个元素 $[(E,\alpha)]\in {\mathrm K}^{-1}(X)$，其中 $E$ 是由 $N$ 个不稳定 IIA 型 9-膜系统所携带的秩为 $N$ 的 Chan-Paton 丛。我们将在下面看到，自同构 $\alpha$ 由
$$
\alpha=-\exp(\pi i\,T) \ ,
$$
给出，并且它通过 $E$ 上的自然伴随作用（共轭）而作用。这里 $T$ 是 9-膜世界体上的伴随 $U(N)$ 快子场。因此，在允许基本 9-膜产生与湮灭的意义下的可能 9-膜位形由 ${\mathrm K}^{-1}(X)$ 分类。把这一点与 IIB 型的情形相比较是富有启发的：那里 ${\mathrm K}(X)= {\mathbb{Z}}\oplus \widetilde{{\mathrm K}}(X)$，D-膜荷由约化 K-理论群 $\widetilde{{\mathrm K}}(X)$ 分类，而 tadpole 反常抵消要求 9-膜的数目等于 $\overline{9}$-膜的数目（这里 ${\mathbb{Z}}$ 中的整数一般地是 9-膜数目与 $\overline{9}$-膜数目之差）。在 IIA 型理论中，我们有 $\widetilde{{\mathrm K}}^{-1}(X)= {\mathrm K}^{-1}(X)$，对 IIA 型 9-膜的数目没有 tadpole 限制。此外，如前面所计算的，我们有
$$
\begin{matrix}
\widetilde{{\mathrm K}}({\mathbf S}^{2n})&= {\mathbb{Z}}\ \ , \ \ \widetilde{{\mathrm K}}({\mathbf S}^{2n+1})~=~0\\
{\mathrm K}^{-1}({\mathbf S}^{2n+1})&= {\mathbb{Z}}\ \ , \ \ {\mathrm K}^{-1}({\mathbf S}^{2n})~=~0\ .
\end{matrix}
$$
这反映了如下事实：IIB 型含有 $p$ 为奇数的超对称 $p$-膜，而 IIA 型含有 $p$ 为偶数的超对称 $p$-膜。注意在这一语言中，Bott 周期性就是“只存在两种 II 型超弦理论”这一陈述。

### 束缚态构造

现在我们将给出时空 $X$ 中余维为奇数、世界体为 $Y$ 的 $p$-膜作为不稳定 IIA 型 9-膜束缚态的一个显式束缚态构造。这将表明 ${\mathrm K}^{-1}(X)$ 确实分类了 IIA 型超弦理论中的 D-膜荷。这一束缚态构造正是 ABS 构造的类比，只不过现在把 $\widetilde{{\mathrm K}}(Y)$ 中的类映射到 K-理论中 ${\mathrm K}^{-1}(X)$ 的类。这表明，凡能用稳定的低维膜做到的事，都能用 IIA 型理论的不稳定 9-膜做到。

考虑 $N$ 个不稳定 9-膜组成的系统。规范群是 $U(N)$，快子场位于 $U(N)$ 的伴随表示 ${\mathbf N}\otimes \overline{\mathbf N}$ 中，快子势为 $V(T)=V(-T)$。如果我们假定 $T$ 凝聚到其某一真空期望值 $T=T_0$，并且与凝聚相关的负能量密度抵消与 9-膜张力相关的正能量密度，如同（式）中那样，那么该 9-膜系统就完全湮灭到超对称真空中，因而是一个基本位形。一般地，$T$ 有滚落到其势 $V(T)$ 的极小值并破坏部分 $U(N)$ 规范对称性的倾向。精确的对称性破缺模式取决于 $T_0$ 本征值的结构，即取决于快子势的精确形式。例如，考虑对称的快子势
$$
V(T)=-m^2\,{\mathrm tr}\,T^2+\lambda^2\,{\mathrm tr}\,T^4+\ldots\ ,
$$
这是从开弦微扰论树级圆盘振幅的结构所预期的。在此情形下，对角化后 $T_0=T_v\cdot{\mathrm diag}(\pm 1,\pm1,\ldots, \pm 1)$。来自具有多于一个边界的世界的对上述势的修正给出如下形式的项
$$
\delta V(T)=\tilde{\lambda}^2\left[{\mathrm tr}\,T^2\right]^2+\ldots
$$
可以证明，若 $\lambda^2\geq 0$ 且 $\tilde{\lambda}^2>0$，则快子势的极小值 $T_0$ 仍然只有两个不同的本征值 $\pm\,T_v$。

此后我们假定所考虑的 9-膜系统具有快子凝聚 $T_0$，其正本征值与负本征值数目相同。于是 9-膜的数目为 $2N$，规范群 $U(2N)$ 破缺为 $U(N)\times U(N)$。IIA 型的真空流形因此是
$$
{\mathcal V}_{\mathrm IIA}(2N)=\frac{U(2N)}{U(N)\times U(N)}\ ,
$$
它参数化了快子场的稳定涡旋型位形。在这样一个稳定涡旋的核心之外（在 $|x|\rightarrow\infty$ 处），快子场趋近其真空期望值。这定义了一个映射 ${\mathbf S}^m\rightarrow {\mathcal V}_{\mathrm IIA}(2N)$，其中球面 ${\mathbf S}^m$ 渐近地包围时空 $X$ 中余维为 $m+1$ 的稳定涡旋的核心。因此，稳定的快子涡旋由
$$
{\mathrm K}^{-1}({\mathbf S}^{m+1})=
\pi_{m}\Bigl({\mathcal V}_{\mathrm IIA}(2N)\Bigr)=\left\{
\begin{array}{cll}{\mathbb{Z}}~~~~&,&~~m=2k\\
0~~~~&,&~~m=2k+1\end{array}\right.
$$
中的类来参数化。由此我们看到，IIA 型系统在奇数余维 $2k+1$ 处表现出稳定的束缚态。注意 9-膜上快子场的 IIA 型真空流形（式）是 $X$ 上复向量丛的分类空间 $BU(\infty)$ 的有限维近似。

现在我们将显式构造束缚态快子涡旋，并把它解释为 IIA 型理论的超对称 D$(2p)$-膜。和前面一样，K-理论为用于构建束缚态的 9-膜数目 $2N$ 选取了一个优先的自然值（这个数目与“逐步”构造中会得到的数目相同）。也就是说，余维 $2k+1$ 中的束缚态最有效地由 $2N=2^k$ 个 9-膜来描述。于是稳定的快子涡旋在拓扑上由同伦群
$$
\pi_{2k}\Bigl({\mathcal V}_{\mathrm IIA}(2^k)\Bigr)= {\mathbb{Z}}\ .
$$
分类。我们同样可以显式构造对应于该同伦群生成元的经典快子孤子场。$2^k$ 个 9-膜的填满时空的世界体支撑着一个 $U(2^k)$ Chan-Paton 丛，我们把它等同于横向空间中旋转群 $SO(2k+1)$ 的旋量丛 ${\mathcal S}$，该群的 $2^k$ 维旋量表示是不可约的。快子场于是由
$$
T(x)=\sum_{i=1}^{2k+1}\Gamma_i\, x^i\ ,
$$
给出，其中 $\Gamma_i$ 是 $SO(2k+1)$ 的 Dirac 矩阵，$x^i$ 是横向空间中的局部坐标。快子场是一个映射 $T: {\mathcal S}\rightarrow{\mathcal S}$，并且它渐近地取值于 IIA 型真空流形（式）中。这应与 IIB 型的情形相对照：那里快子场渐近地取值于 IIB 真空流形（式）中，原因是对应于旋转群 $SO(2k)$ 与 $SO(2k+1)$ 的 Clifford 代数表示具有不同的结构。

在现在的情形中我们还可以走得更远，显式构造出生活在 9-膜上、并且由于施加于整个系统的有限能量条件而必须伴随上述快子涡旋出现的非平凡 $U(2^k)$ 规范场位形。存在一个自然映射
$$
\pi_{2k-1}\left(U(2^[k-1])\right)\longrightarrow
\pi_{2k}\left({\mathcal V}_{1}(2^k)\right)\ ,
$$
它由快子生成元的变换
$$
T_{\mathrm IIB}(x)=\sum_{i=1}^{2k}\Gamma_i\,x^i~~\longmapsto~~
T_{\mathrm IIA}(x)=T_{\mathrm IIB}(x)+x^{2k+1}\,\sigma_3\otimes{\mathbb{I}}_{2^[k-1]}\ .
$$
定义。这里 $T_{\mathrm IIB}(x)$ 是 IIB 快子场，它被构造为非平凡 $U(2^k)$ 规范场的未破缺部分。像前面那样把球面分解为 ${\mathbf S}^{2k}={\mathbf S}_+^{2k}\cup {\mathbf S}_-^{2k}$，其中 ${\mathbf S}^{2k-1}={\mathbf S}_+^{2k}\cap {\mathbf S}_-^{2k}$，则 ${\mathbf S}_{\pm}^{2k}$ 上的规范场在拓扑上是平凡的，可以利用赤道 ${\mathbf S}^{2k-1}$ 上的过渡函数把它们拼接起来，得到 ${\mathbf S}^{2k}$ 上具有适当磁荷的整体规范场。这个大规范变换正是 $T_{\mathrm IIB}(x)$，而 $U(2^[k-1])\times U(2^[k-1])$ 的未破缺长程规范场对应于一个广义磁单极子的规范场。

利用 $T_{\mathrm IIA}^2=|x|^2$，可以证明 [bfn,horava]，丛自同构（式）实际上就是同伦群 $\pi_{2k+1}(U(2^k))$ 的生成元，并且在远离涡旋核心处 $T_{\mathrm IIA}(x)\in{\mathcal V}_{\mathrm IIA}(2^k)$。这诱导出自然映射
$$
\pi_{2k}\left({\mathcal V}_{\mathrm IIA}(2^k)\right)\longrightarrow
\pi_{2k+1}\left(U(2^k)\right)\ ,
$$
它由
$$
T_{\mathrm IIA}~~\longmapsto~~\alpha=-\exp(\pi i\,T_{\mathrm IIA})\ .
$$
定义。于是快子凝聚表示相对 K-理论群 ${\mathrm K}^{-1}({\mathbf B}^{2k+1},{\mathbf S}^{2k})= {\mathbb{Z}}$ 的生成元，而上述束缚态构造正是 ABS 构造的类比，只不过现在把 $\widetilde{{\mathrm K}}(Y)$ 中的类映射到 ${\mathrm K}^{-1}(X)$ 中，其中 $Y$ 在由 IIA 型理论的不稳定 9-膜所缠绕的时空流形 $X$ 中具有奇数余维。同样，精确的嵌入由杯积（式）给出为
$$
\begin{matrix}
\widehat{\lambda}\,:\,\widetilde{{\mathrm K}}(Y)\otimes_{\mathbb{Z}}
{\mathrm K}^{-1}({\mathbf B}^{2k+1},{\mathbf S}^{2k})&\stackrel{\approx}{\longrightarrow}
{\mathrm K}^{-1}(Y\times{\mathbf B}^{2k+1},Y\times {\mathbf S}^{2k})\\
\Bigl[(E\,,\,F)\Bigr]&\longmapsto\widehat{\lambda}
\left[\Bigl((E\otimes{\mathcal S})_{{\mathrm Id}_E\otimes\alpha}
\,,\,(F\otimes{\mathcal S})_{{\mathrm Id}_F\otimes\alpha}\Bigr)\right]
\end{matrix}
$$
对 $[(E,F)]\in \widetilde{{\mathrm K}}(Y)$ 成立。

这样我们就得到了 IIA 型与 IIB 型中束缚态构造的一个层级，由维数递增的膜系统表示，其世界体规范群构成一个自然的层级
$$
U(1)\subset U(1)\times U(1)\subset U(2)\subset U(2)\times U(2)\subset U(4)
\subset U(4)\times U(4)\subset \cdots \ .
$$
这一性质导致 D-膜之间通常的降维关系 [sendescent,os]。在这一层级中，用稳定膜对给出的束缚态构造与用不稳定膜给出的束缚态构造交替出现。它表明，II 型超弦理论的一个超对称 D$p$-膜可以构造为不稳定 D$(p+1)$-膜世界体上的快子扭结（见下一小节），或者构造为一个 $(p+2)$-膜 $\overline{(p+2)}$-膜对中的束缚态涡旋，又或者构造为两个不稳定 $(p+3)$-膜的束缚态，如此等等。这一过程一直持续到抵达填满时空的维数，从而最终得到一种所有时空对称性都显式的、用 9-膜表述的构造。

作为一个简单例子，考虑余维 $2k+1=3$ 的情形。此时 K-理论规范群是 $U(2)$，作用在两个不稳定 9-膜上，其在 $U(2)$ 的 ${\mathbf2}$ 表示中的 Chan-Paton 丛被等同于横向空间旋转群 $SO(3)$ 的旋量丛 ${\mathcal S}$。取标准 Pauli 自旋矩阵 $\sigma_i$ 作为 $SO(3)$ 的 Dirac 矩阵，给出
$$
T(x)=\sum_{i=1}^3\sigma_i\, x^i =
\left( \begin{array}{cc}x^3 & x^1+ix^2\\ x^1-ix^2&-x^3
\end{array}\right)\ .
$$
快子场（式）表示一个涡度为 1 的涡旋。有限能量条件把它与非平凡的 $U(2)$ 规范场
$$
\begin{matrix}
A_i(x)&=\frac1{|x|^2}\left(1-\frac{|x|}{\sinh|x|}\right)
\sum_{j=1}^3\, \Gamma_{ij}\,x^j\\
\Gamma_{ij}&\equiv\frac{1}{2}\Bigl[\sigma_i\,,\,\sigma_j\Bigr]
=\sum_{k=1}^3\epsilon_{ijk}\,\sigma^k\ .
\end{matrix}
$$
联系起来。除从 $SU(2)$ 到 $U(2)$ 规范理论的平凡提升之外，这不过就是 $3+1$ 维中的 't~Hooft-Polyakov 磁单极子 [tpmon]，其中（式）里的收敛因子就是 't~Hooft-Polyakov ansatz 的通常 BPS 解。这个单极子把 IIA 型超弦理论的一个超对称稳定 D$(2p)$-膜表示为两个不稳定 D$(2p+3)$-膜的束缚态。另一方面，（式）中的对角块表示由一对 D$(2p+3)$-膜构造出一个 D$(2p+2)$-膜和一个 D$\overline{(2p+2)}$-膜（见下一小节），而非对角块则把 D$(2p)$-膜表示为一个 D$(2p+2)$-膜-反膜对的束缚态（参见式）。这同样是 II 型超弦理论中降维关系的一个例子 [sendescent,os]。

### IIA 型弦理论中的畴壁

余维 1（即 $k=0$）的情形是“退化”的，我们现在就来讨论它。按照一般处方，这表示 IIA 型理论中一个稳定的 8-膜（或 $\overline{8}$-膜），它由 $2^k=1$ 个 9-膜的快子扭结构造而成。规范群是 $U(1)$，快子场是一个荷为 0 的实标量场，由
$$
T(x)=\frac{\pm\,T_0\,x^9}{\sqrt{1+(x^9)^2}}\ ,
$$
给出，因为现在只有一个 $\Gamma$-矩阵，它可以取为 $1\times1$ 单位矩阵。这里 $x^9$ 是横向于扭结核心的坐标，该扭结代表时空中的一个畴壁。（式）中的符号区分 8-膜与 $\overline{8}$-膜，它对应于畴壁两侧快子场渐近值之差 $T(-\infty)-T(+\infty)$ 的符号。注意由一个 9-膜只能构造一个 8-膜或 $\overline{8}$-膜。在此情形下 $U(1)$ 规范群没有对称性破缺，我们剩下的就是一个 $U(1)$ 规范理论和一个可以凝聚到两个真空期望值 $\pm\,T_0$ 中任一个的快子场。单个 9-膜的真空流形的有关同伦群是
$$
\pi_0\Bigl(O(1)\Bigr)=\pi_0\Bigl(\{ \pm\,T_0\}\Bigr)= {\mathbb{Z}}_2\ ,
$$
因此没有足够的空间容纳本应由 ${\mathbb{Z}}$ 分类的预期守恒 8-膜 RR 荷。所以，每一个单独的 8-膜和 $\overline{8}$-膜都需要它自己的 9-膜；于是，要容纳 8-膜荷的完整 K-理论群 ${\mathrm K}^{-1}({\mathbf S}^1)= {\mathbb{Z}}$，最小的 9-膜系统需要无穷多个填满时空的膜。

更一般地，如果快子势被安排得使 $N$ 个 9-膜世界体上的快子场凝聚到其真空期望值 $T_0$，其中 $N-n$ 个正本征值和 $n$ 个负本征值，那么
$$
T_0=T_v
\left( \begin{array}{cc}{\mathbb{I}}_{N-n} & 0\\ 0 & -{\mathbb{I}}_{n}
\end{array}\right)
$$
且 $U(N)$ 规范对称性破缺为 $U(N-n)\times U(n)$。如同 $N=1$ 的情形，对 $N>1$，快子场形成余维 1 的扭结。假定 $T$ 的所有本征值都对应于定域在 $X$ 中一个共同的余维 1 畴壁 $Y$ 上的扭结。那么在 $Y$ 附近局部地我们可以把快子场写成
$$
T(x)=
\left( \begin{array}{cc}\frac{T_v\,x^9}{\sqrt{1+(x^9)^2}}\,{\mathbb{I}}_{N-n}& 0\\
0&-\frac{T_v\,x^9}{\sqrt{1+(x^9)^2}}\,{\mathbb{I}}_{n}\end{array}\right)\ ,
$$
它描述了 $N-n$ 个 8-膜和 $n$ 个 $\overline{8}$-膜，它们的世界体都重合地缠绕 $Y$。更一般的、彼此分离的 8-膜与 $\overline{8}$-膜位形可以通过让每个本征值沿着时空 $X$ 中各自独立的余维 1 子流形为零来构造。同样，人们无法把多于 $N$ 个 8-膜和 $\overline{8}$-膜表示为 $N$ 个 9-膜的束缚态，因为那样就得通过添加其他 9-膜来做 K-理论的“稳定化”，以使有关的同伦群保持在稳定范围内。


### 应用于矩阵理论

考虑 ${\mathbb{R}}^{10}$（或其某种紧化）上 IIA 型超弦理论中的 $N$ 个 D0-膜。每个 D0-膜都可以表示为 16 个不稳定的、充满时空的 9-膜的束缚态，这些 9-膜的世界体场论包含一个 $U(16)$ 规范场、一个处于 $U(16)$ 伴随表示的快子场 $T$，以及两个处于 $U(16)$ 伴随表示、时空手征性相反的手征费米子场 $\mathrm{ch}i, \mathrm{ch}i'$。在每个稳定的类点孤子核心附近，快子场可表示为

$$
T(x)=\sum_{i=1}^9\Gamma_i\, x^i\ ,
$$

其中 $\Gamma_i$ 是涡旋核心横向空间旋转群 $SO(9)$ 的 Dirac 矩阵。该场生成同伦群

$$
\pi_8\Bigl({\mathcal V}_{\mathrm IIA}(16)\Bigr)= {\mathbb{Z}}\ \ \ \ ,\ \ \ \
{\mathcal V}_{\mathrm IIA}(16)=\frac{U(16)}{U(8)\times U(8)}\ .
$$

此外，非平凡的长程规范场在 $T(x)$ 给出的单位涡度之外，还为每个 D0-膜产生一个“磁荷”。

这 16 个 9-膜处于 $U(16)$ 规范群的 ${\mathbf16}$ 表示中；在代表 D0-膜的广义磁单极-涡旋位形背景下，该表示被等同于 $SO(9)$ 的旋量表示 ${\mathbf16}$。（这推广了三维的 't Hooft-Polyakov 单极子，那里 $SU(2)$ 规范群的 ${\mathbf3}$ 表示被等同于空间旋转群 $SO(3)$ 的旋量表示。）K-理论意味着，稳定的弦论孤子携带一单位 D0-膜荷，因而把 D0-膜表示成 16 个不稳定 9-膜的束缚态。K-理论还意味着，${\mathbb{R}}^{10}$ 中 D0-膜世界线的平凡拓扑并不需要通过添加额外 9-膜来“稳定化”位形（即使在 ${\mathbb{R}}^{10}$ 的紧化中这也是对的）。因此在这种束缚态构造中，我们从不需要假定世界线 $Y$ 是连通的；此时旋量丛 ${\mathcal S}$ 实际上沿 $Y$ 平凡，因而可作为平凡丛延拓到 $X$ 上。换言之，我们不必为每一个额外的 D0-膜引入一组新的 16 个 9-膜，因此*任意*由 $N$ 个 D0-膜组成的系统都可以表示为固定的 16 个不稳定、充满时空的 9-膜系统中的束缚态。

于是，给定仅用 16 个 IIA 型 9-膜描述的多 D0-膜态，我们可以在取定义矩阵理论的习惯 Sen-Seiberg 标度极限时跟踪这一 9-膜位形 [seiberg]。矩阵理论于是可表述为 16 个不稳定 9-膜充满时空的世界体上稳定孤子的理论。这种把矩阵理论解释成固定规范群的规范理论中涡旋的做法，使人可以在不改变规范群秩的情况下改变系统中 D0-膜的数目 $N$。在矩阵理论的传统表述中，大-$N$ 极限要求把规范群秩不同的理论相互联系起来，因此很难理解不同 $N$ 值的系统如何相关（例如通过某种重整化群方法）。但把 D0-膜作磁涡旋的 K-理论构造对任意 $N$ 值都保持规范群固定。总之，矩阵理论的动力学看来就包含在 16 个不稳定 9-膜世界体上磁涡旋的物理之中，而后者在低能下由 $U(16)$ 规范理论描述。

## I 型 D-膜与 ${\mathrm KO}(X)$

在利用 II 型理论熟悉了束缚态构造以及用它们把 D-膜描述成新的孤子物体的做法之后，我们现在开始考虑更复杂的超弦理论，在其中 K-理论形式会给出一些出人意料的预言。本节我们处理 I 型理论，从而与弦论中非 BPS 态的原始构造建立联系。I 型超弦是无向的，其超对称真空位形的规范群为 $SO(32)$，这要求真空态中始终存在 32 个充满时空的膜。因此相应的 Chan-Paton 规范丛的 K-理论需要对第 2 节所述内容作某种精细化。正是这一差别将导致 I 型理论中远为丰富的 D-膜荷谱。

### 群 ${\mathrm KO}(X)$

考虑 I 型超弦理论中由 $N$ 个 9-膜和 $M$ 个 $\overline{9}$-膜组成的系统。蝌蚪反常抵消现在要求 $N-M=32$，并且膜支撑一个 $SO(N)$ 丛 $E$，反膜支撑一个 $SO(M)$ 丛 $F$。由于膜-反膜的创生与湮灭，我们把丛对 $(E,F)$ 与 $(E\oplus H,F\oplus H)$ 等同，其中 $H$ 为任意 $SO(K)$ 丛。带有这一等价关系的对 $(E,F)$ 定义了时空 $X$ 的实 K-群 ${\mathrm KO}(X)$。把 $F$ 换成 $F\oplus I^{32}$ 便知，蝌蚪反常抵消的 9-膜与 $\overline{9}$-膜的位形由约化实 K-理论群 $\widetilde{{\mathrm KO}}(X)$ 分类。进一步，由束缚态构造可知，I 型超弦理论的 D-膜位形由具有紧支撑的 ${\mathrm KO}(X)$ 分类 [witten]。

我们关于 ${\mathrm K}(X)$ 所说的几乎一切都可照搬到实 K-理论。然而重要的变化在于与同伦论的关系。也就是说，对 $k>n=\dim X$（即 ${\mathrm KO}(X)$ 的稳定范围），有

$$
\widetilde{{\mathrm KO}}(X)=\Bigl[X\,,\,BO(k)\Bigr]\ ,
$$

其中 $BO(k)=\bigcup_{m>k+n}{\mathrm Gr}(k,m;{\mathbb{R}})$ 是结构群为 $O(k)$ 的实向量丛的分类空间，而实 Grassmann 流形为

$$
{\mathrm Gr}(k,m;{\mathbb{R}})=\frac{O(m)}{O(m-k)\times O(k)}\ , \ \ \ \ m>k+n\ .
$$

对 $X={\mathbf S}^n$ 现在有

$$
\widetilde{{\mathrm KO}}({\mathbf S}^n)=\pi_n\Bigl(BO(k)\Bigr)=\pi_{n-1}\Bigl(O(k)\Bigr)\ ,\
\ \ \  k>n\ ,
$$

而该群分类平坦 ${\mathbb{R}}^{10}$ 上 I 型弦论中的 $(9-n)$-膜荷。正交群的稳定同伦与酉群的稳定同伦大不相同。例如，

$$
\begin{eqnarray}
\pi_0\Bigl(O(k)\Bigr)&=&{\mathbb{Z}}_2\ ,\ \ \ \ k\geq 1\\
\pi_1\Bigl(O(k)\Bigr)&=&{\mathbb{Z}}_2\ ,\ \ \ \ k\geq 3\\
\pi_2\Bigl(O(k)\Bigr)&=&0\ ,\ \ \ \ k\geq 4\\
\pi_3\Bigl(O(k)\Bigr)&=&{\mathbb{Z}}\ , \ \ \ \ k\geq 5\ .
\end{eqnarray}
$$

注意，把 9-膜位形与 ${\mathrm KO}(X)$ 等同起来其实并不需要膜-反膜湮灭。这源于以下事实：当 $\dim X=10$ 时，$X$ 上的 $SO(32)$ 丛由 $\pi_n(SO(32))$（$n\leq 9$）分类。这些同伦群总处于稳定范围内，因此 $X$ 上所有 $SO(32)$ 丛都自动由 $\widetilde{{\mathrm KO}}(X)$ 分类。

Bott 周期性定理现在指出，$O(\infty)$ 的同伦群具有周期*八*的周期性：

$$
\pi_n\Bigl(O(\infty)\Bigr)=\pi_{n+8}\Bigl(O(\infty)\Bigr)\ ,
$$

相应地有八个更高次的 ${\mathrm KO}$-群，它们按 2.4 节所述用纬垂来定义，并且满足

$$
\widetilde{{\mathrm KO}}^{-n}(X)=\widetilde{{\mathrm KO}}^{-n-8}(X)\ ,
$$

而如通常那样 ${\mathrm KO}^{-n}(X)=\widetilde{{\mathrm KO}}^{-n}(X)\oplus{\mathrm KO}^{-n}({\mathrm pt})$。特别地，对 $X={\mathbf S}^n$ 有

$$
\widetilde{{\mathrm KO}}({\mathbf S}^n)=\widetilde{{\mathrm KO}}({\mathbf S}^{n+8})\ .
$$

周期性（式）可由 KO-理论的 ABS 构造导出。设 ${\mathrm RO}[Spin(n)]$ 为旋量群 $Spin(n)$ 的实表示环，它由不可约实表示生成。那么仿照 2.8 节，存在一个自然同态

$$
\varphi: \, {\mathrm RO}\Bigl[Spin(n)\Bigr]\longrightarrow
{\mathrm KO}({\mathbf B}^n, {\mathbf S}^[n-1])
$$

它下降为分次环同构

$$
{\mathrm RO}\Bigl[Spin(n)\Bigr]\,/\, i^*\,{\mathrm RO}\Bigl[Spin(n+1)\Bigr]
\stackrel{\approx}{\longrightarrow}\widetilde{{\mathrm KO}}({\mathbf S}^[n]) \ .
$$

利用实 Clifford 代数的周期性（式），即可立即得到（式）。

同构（式）也可用来展示诸如（式）中那些额外的 ${\mathbb{Z}}_2$ 值荷如何出现在 I 型理论的 D-膜谱中。例如，考虑（式）中 $n=1$ 的情形。由于 $C\ell_1={\mathbb{C}}$，$C\ell_1$-模就是复向量空间，而同构 ${\mathrm RO}[Spin(1)]\stackrel{\approx}{\rightarrow}{\mathbb{Z}}$ 由取复维数生成。类似地，由于 $C\ell_2={\mathbb{H}}$，$C\ell_2$-模是四元数向量空间，${\mathrm RO}[Spin(2)]\stackrel{\approx}{\rightarrow}{\mathbb{Z}}$ 来自取四元数维数。映射 $i^*:\, {\mathrm RO}[Spin(2)]\rightarrow{\mathrm RO}[Spin(1)]$ 通过把四元数向量空间在标量限制下视为复向量空间来实现。这不过是由乘以 2 给出的映射 ${\mathbb{Z}}\rightarrow{\mathbb{Z}}$，因为复维数是四元数维数的两倍。由此得到 $\widetilde{{\mathrm KO}}({\mathbf S}^1)={\mathbb{Z}}/2{\mathbb{Z}}={\mathbb{Z}}_2$。此外，（式）右端的生成元可以方便地用旋量模和 Clifford 乘法映射表示。例如，若 ${\mathcal S}={\mathcal S}^+\oplus{\mathcal S}^-$ 是 $C\ell_{4m}$ 的基本分次模，则

$$
\varphi^{(4m)}_{{\mathbb{R}}}=[{\mathcal S}^+,{\mathcal S}^-;\mu]
$$

是群 $\widetilde{{\mathrm KO}}({\mathbf S}^{4m})={\mathbb{Z}}$ 的生成元，其中 $\mu_x:{\mathcal S}^+\rightarrow {\mathcal S}^-$ 仍表示乘以 $x\in{\mathbb{R}}^{4m}$ 的 Clifford 乘法。利用 Clifford 模结构与上积，我们同样容易算出

$$
\varphi_{{\mathbb{R}}}^{(8n)}=\left(\varphi_{{\mathbb{R}}}^{(8)}\right)^n \ \ \ ,
\ \ \ 4\varphi_{{\mathbb{R}}}^{(8)}=\left(\varphi_{{\mathbb{R}}}^{(4)}\right)^2\ .
$$

新的挠 KO-群还修改了第 2 节所述的多种乘积关系。例如 Künneth 公式（式）对球面一般并不必成立，因为 ${\mathrm KO}({\mathbf S}^n)$ 未必是自由生成的。尽管如此，例如（式）的类比仍可由（式）得到，从而有

$$
\widetilde{{\mathrm KO}}(X\times {\mathbf S}^1)=\widetilde{{\mathrm KO}}^{-1}(X)\oplus
\widetilde{{\mathrm KO}}(X)\oplus{\mathbb{Z}}_2\ .
$$

### 束缚态构造

我们只需知道前八个 KO-群，即可确定 I 型超弦理论中（BPS 与非 BPS）D-膜的完整谱。该谱见表 1。

| D-膜 | D9 | D8 | D7 | D6 | D5 | D4 | D3 | D2 | D1 | D0 | D(-1) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 横向空间 | ${\mathbf S}^0$ | ${\mathbf S}^1$ | ${\mathbf S}^2$ | ${\mathbf S}^3$ | ${\mathbf S}^4$ | ${\mathbf S}^5$ | ${\mathbf S}^6$ | ${\mathbf S}^7$ | ${\mathbf S}^8$ | ${\mathbf S}^9$ | ${\mathbf S}^{10}$ |
| $\widetilde{{\mathrm KO}}({\mathbf S}^n)$ | ${\mathbb{Z}}$ | ${\mathbb{Z}}_2$ | ${\mathbb{Z}}_2$ | 0 | ${\mathbb{Z}}$ | 0 | 0 | 0 | ${\mathbb{Z}}$ | ${\mathbb{Z}}_2$ | ${\mathbb{Z}}_2$ |

[表：来自 $\widetilde{{\mathrm KO}}({\mathbf S}^n)$ 的 I 型 D-膜谱。]

表中包含 I 型理论众所周知的稳定 BPS D9-膜、D5-膜和 D-弦（带整数值荷）。D0-膜是 ${\mathbb{Z}}_2$ 带电的 D-粒子，它稳定但非 BPS，最早在 [senbps] 中发现。D8、D7 与 D(--1) 膜是 K-理论的新预言 [witten]，它们意味着 I 型理论的谱应包含新的 ${\mathbb{Z}}_2$ 带电、稳定但非 BPS 的 8-膜、7-膜与瞬子。这一新的 I 型谱已在 [frau] 中用边界态形式算出，从而明确证实了 K-理论的预言。由于 D9、D5 与 D1 膜都携带 RR 荷，它们由如下形式的边界态描述

$$
|Dp\rangle =|Dp\rangle_{{\mathrm NS}}
\pm |Dp\rangle_{{\mathrm R}}\ ,\ \ \ \ p=1,5,9 \,
$$

其余非 BPS D-膜不携带任何 RR 荷，故其边界态为

$$
|Dp\rangle = |Dp\rangle_{{\mathrm NS}}\ ,\ \ \ \ p=-1,0,7,8\ ,
$$

并且它们自身就是自己的反膜。注意，非 BPS D-膜的显式边界态描述证明了表 1 中所有荷都由开弦可以附着的时空缺陷携带。

I 型理论可以看作 IIB 型超弦理论由反转基本弦世界面定向的世界面宇称算符 $\Omega$ 所作的 orientifold 投影。orientifold 群 $\Omega$ 对 Chan-Paton 丛的作用是反线性的，即 $E\stackrel{\Omega}{\rightarrow} \overline{E}$，其中 $\overline{E}\cong E^*$ 是通过对 $E$ 的转移函数取复共轭所得的共轭丛。因此只有实丛能在 orientifold 投影下存活，导致 I 型系统由实虚丛的 ${\mathrm KO}$-理论描述。对 $p=1,5,9$，相应的 IIB 型 RR 荷在 $\Omega$-投影下不变，即 $\Omega|Dp\rangle_{\mathrm R}=|Dp\rangle_{\mathrm R}$。相应的 I 型束缚态构造于是就是 IIB 型构造的 orientifold 投影。人们可以用最低可能维数的单个 BPS 膜-反膜对的束缚态来描述非 BPS 膜。对 $p=0,8$，不存在 IIB 型 RR 荷，边界态自动在 $\Omega$ 下为偶。D0（相应地 D8）膜是 I 型 D1--D$\overline{1}$（相应地 D9--D$\overline{9}$）系统世界体上快子场中的拓扑稳定扭结，带有 ${\mathbb{Z}}_2$ 值 Wilson 线（参看 4.4 节）。对 $p=-1,7$，$\Omega$ 把 IIB 型 $p$-膜与 $\overline{p}$-膜互换，即 $\Omega|Dp\rangle_{\mathrm R}=-|Dp\rangle_{\mathrm R}$，因此 $p$-膜-反膜位形是 $\Omega$-不变的。于是 I 型 D$(-1)$（相应地 D7）膜是 IIB 中 D(--1)--D$\overline{(-1)}$（相应地 D7--D$\overline{7}$）系统的 orientifold 投影。在后两种情形，我们可以把相应的 I 型边界态用 IIB 理论的边界态写成

$$
|Dp\rangle_{\mathrm I}= |Dp\rangle_{\mathrm IIB} + |D\overline{p}\rangle_{\mathrm IIB}
=|Dp\rangle_{{\mathrm NS}}\ ,\ \ \ \ p=-1,7\ .
$$

然后可以证明，不稳定 $p-\overline{p}$ 态中存在的 IIB 型快子被 $\Omega$ orientifold 投影消除 [frau]，从而得到一个稳定的孤子态。由这些束缚态构造还可以立即推出非 BPS D-膜的世界体场论，特别是表 2 所列的世界体规范群，下面我们将明确演示。

| D-膜 | D0 | D1 | D5 | D7 | D8 | D9 |
|---|---|---|---|---|---|---|
| 规范群 | ${\mathbb{Z}}_2$ | ${\mathbb{Z}}_2$ | $USp(2)$ | $U(1)$ | ${\mathbb{Z}}_2$ | ${\mathbb{Z}}_2$ |

[表：I 型 D-膜的世界体规范群。]

本节余下部分我们将利用 I 型超弦理论的 KO-理论结构来描述其 D-膜谱的若干方面。我们将逐个考虑各类孤子，并讨论各维数所特有的性质。

### I 型 D-瞬子

I 型超弦的微扰对称群其实应视为 $O(32)$ 而不是 $SO(32)$，因为行列式为 $-1$ 的正交变换 ${\mathcal O}$ 即 $\det{\mathcal O}=-1$ 是 I 型微扰论的对称性；也就是说，$O(32)$ 的中心元 $-1$ 在微扰谱上平凡地作用，故相应对称群为 $O(32)/{\mathbb{Z}}_2$。这一事实与 I 型超弦微扰规范群的出现方式相联系，后者局部同构于 $SO(32)$。然而与 $SO(32)$ 杂化弦的 $S$-对偶意味着行列式为 $-1$ 的变换 ${\mathcal O}$ 其实并不是对称性。这便意味着必定存在某种非微扰效应，把群 $O(32)$ 破缺到其连通子群 $SO(32)$，而这正是与 $\pi_9(SO(32))={\mathbb{Z}}_2$ 相联系的 ${\mathbb{Z}}_2$ 带电规范瞬子。文献 [witten] 用指标论论证证明了这一点，即球面 ${\mathbf S}^{10}$ 上的非平凡丛的特征是相应手征 Dirac 算符具有奇数个费米零模（指标论与 K-理论的关系将在 7.4 节讨论）。I 型 D-瞬子来自 Chan-Paton 丛为 $({\mathcal S}^+,{\mathcal S}^-)$ 的 IIB 型 9-膜-反膜对的束缚态，而反 D-瞬子具有规范丛 $({\mathcal S}^-,{\mathcal S}^+)$。这里 ${\mathcal S}^{\pm}$ 是 $SO(10)$ 通常的 16 维复手征旋量表示。orientifold 投影通过复共轭作用，因而反转手征性 ${\mathcal S}^+\leftrightarrow {\mathcal S}^-$（等价地反转 9-膜与 $\overline{9}$-膜），从而把 I 型理论中的瞬子与反瞬子等同起来。对 I 型超弦与 KO-理论，规范丛必须是*实*的，因此我们取 I 型 9-膜 Chan-Paton 丛按旋量模 ${\mathcal S}={\mathcal S}^+\oplus {\mathcal S}^-$ 变换；在把复表示向量空间于标量限制下视为实空间之后，该旋量模成为 $SO(32)$ 唯一的不可约实 32 维旋量表示。因此 $(-1)$-膜由 32 个 Chan-Paton 丛为 $({\mathcal S},\overline{\mathcal S})$ 的 $9-\overline{9}$ 膜对以及一个快子场 $T(x)=\sum_i\Gamma_i\,x^i$ 描述。

### I 型 D-粒子

${\mathrm KO}({\mathbb{R}}^9)$（或 $\widetilde{{\mathrm KO}}({\mathbf S}^9)$）的一个元素由 ${\mathbb{R}}^9$ 上一对平凡 $SO(N)$ 丛 $(E,F)$ 以及一个在无穷远处为同构的丛映射 $T:E\rightarrow F$ 描述，并要求旋转群 $SO(9)$ 以旋量表示作用于 $E$ 与 $F$ 的纤维。对 KO-理论，我们必须使用实旋量表示，而 $SO(9)$ 有唯一的这种不可约表示 ${\mathcal S}$，其维数为 16。因此 $E$ 与 $F$ 的秩为 16，并在 $SO(9)$ 旋转下像 ${\mathcal S}$ 一样变换。快子场于是由（式）给出。

我们可以把这一 K-理论构造与 [seninst] 中 I 型 D-粒子的原始构造作比较。为此我们把坐标与 $\Gamma$-矩阵作 $8+1$ 维分解。取 $SO(9)$ 的一个 $SO(8)$ 子群，在此分解下记 $x=(x^a,x^9)$，其中 $a=1,\ldots, 8$。$SO(9)$ 的旋量表示 ${\mathcal S}$ 在此分解下按 $SO(8)$ 分解为 ${\mathcal S}={\mathcal S}^+\oplus {\mathcal S}^-$，其中 ${\mathcal S}^{\pm}$ 是 $SO(8)$ 的实八维手征旋量表示。把 $SO(8)$ 的 Dirac 矩阵写成 $\Gamma_a: {\mathcal S}^-\rightarrow {\mathcal S}^+$ 与 $(\Gamma_a)^{\top}:{\mathcal S}^+\rightarrow{\mathcal S}^-$。于是由（式）可得快子场的分解为（见（式））

$$
T(x)=\left( \begin{array}{cc}x^9\,{\mathbb{I}}_{16}& \sum_a\Gamma_a\,x^a\\
\sum_a(\Gamma_a)^{\top}\,x^a&-x^9\,{\mathbb{I}}_{16}
\end{array}\right)\ .
$$

通过 $\overline{9}$-膜上 Chan-Paton 因子的基变换

$$
\sigma_1\otimes{\mathbb{I}}_{16}=\left(
\begin{array}{cc}0&{\mathbb{I}}_{16}\\{\mathbb{I}}_{16}&0
\end{array}\right)
$$

得到

$$
T(x)~\longmapsto~(\sigma_1\otimes{\mathbb{I}}_{16})\,T(x)\,(\sigma_1\otimes{\mathbb{I}}_{16})=
\left( \begin{array}{cc} \sum_a\Gamma_a\,x^a & x^9\,{\mathbb{I}}_{16}\\ -x^9\,{\mathbb{I}}_{16}
&\sum_a(\Gamma_a)^{\top}\,x^a
\end{array}\right)\ .
$$

这里的对角块代表两个解耦的系统，各含八个 $9-\overline{9}$ 对。第一组八个 $9-\overline{9}$ 对具有快子场

$$
T_s(x^a)=\sum_{a=1}^8\Gamma_a\,x^a\ ,
$$

而第二组的快子场为 $(T_s)^\top$。但 $T_s$ 描述的是位于 $x^1=\ldots=x^8=0$ 的 D-弦（见下文 5.6 节）；又因为 $(T_s)^\top$ 是把 $T_s$ 中的 9-膜与 $\overline{9}$-膜交换所得，故快子场 $(T_s)^\top$ 描述位于 $x^1=\ldots=x^8=0$ 的反 D-弦。这正是 [senbps] 中用重合的 D-弦与反 D-弦构造 I 型 D-粒子的做法。非对角块对应于一个余维一的快子场，它连接 D-弦与反 D-弦，并在反射 $x^9\rightarrow -x^9$ 下为奇。这恰恰是 [seninst] 中构造的 D1--D$\overline{1}$ 快子场的孤子位形。于是，K-理论形式也可用来给出非 BPS 态的弦论构造。

D-粒子携带的旋量量子数在这一框架中也自然出现。如 [seninst] 所示，I 型 0-膜按 $SO(32)$ 的旋量表示变换，这与 I 型超弦的非微扰规范群其实是 $SO(32)$ 的旋量覆盖 $Spin(32)/{\mathbb{Z}}_2$ 这一事实相符。在上述构造中，这一点可从以下事实看出：$\overline{9}$-膜的 Chan-Paton 因子产生一个 $SO(32)$ 向量的费米零模，其量子化给出 $SO(32)$ 的旋量表示（这里再次用到指标论事实：${\mathbf S}^9$ 上非平凡 $SO(32)$ 丛的特征是相应 Dirac 算符具有奇数个费米零模）[witten]。此外，给定 $N$ 个重合的 I 型 0-膜，快子顶点算符（在零像中）具有形式

$$
V(\Lambda)=\psi~\mbox{e}^{ik_0X^0(z)}\otimes\Lambda\ ,
$$

其中 $\Lambda$ 是作用于 Chan-Paton 因子的 $N\times N$ 矩阵，$\psi$ 是世界面费米场。$\Omega$ 投影把 $\Lambda\rightarrow \Lambda^\top$。因此，若 $\Lambda^\top=-\Lambda$，则 $V(\Lambda)$ 在 $\Omega$ 下为奇，快子态在 $\Omega$-投影下存活。反对称矩阵 $\Lambda$ 总有偶数个非零本征值，于是每一对描述一对 0-膜走向湮灭的流。这意味着 D-粒子数只在模 2 意义下守恒，与 $\widetilde{{\mathrm KO}}({\mathbf S}^9)={\mathbb{Z}}_2$ 相符。类似的论证适用于 I 型 D-瞬子。


### I 型弦理论中的畴壁

I 型 D8-膜由 $\widetilde{{\mathrm KO}}({\mathbf S}^1)=\pi_0(O(32))={\mathbb{Z}}_2$ 描述，它通过平凡丛 $E, F\rightarrow {\mathbb{R}}^1$ 以及在无穷远处可逆的快子场 $T:E\to F$ 来表示。与 4.4 节一样，8-膜是一个畴壁，位于 $x^9=0$，由单个 $9-\overline{9}$ 对连同快子场（式）构造而成，该快子场在壁的一侧为正、在另一侧为负。然而，与 4.4 节的情形不同，这里由束缚态构造产生的 ${\mathbb{Z}}_2$ 取值荷是非常自然的。看出这一点的一种方式是借助 Bott 周期性映射（式），它可以如下描述。取 $[(E_0,F_0)]\in \widetilde{{\mathrm KO}}({\mathbf S}^n)$，其快子映射为 $T_0:E_0\rightarrow F_0$，并通过设置

$$E=E_0\otimes ({\mathcal S}^+\oplus {\mathcal S}^-)\ \ \ \ , \ \ \ \
F=F_0\otimes ({\mathcal S}^+\oplus {\mathcal S}^-)\ ,$$

来构造 $[(E,F)]\in \widetilde{{\mathrm KO}}({\mathbf S}^{n+8})$，其中 ${\mathcal S}^{\pm}$ 是 $SO(8)$ 的手征旋量表示，其 Dirac 矩阵为 $\Gamma_a: {\mathcal S}^-\rightarrow {\mathcal S}^+$。令 $x^a$ 表示 ${\mathbb{R}}^{n+8}$ 的最后八个坐标。快子场则如前所述由杯积给出：

$$T(x)=\left( \begin{array}{cc}T_0\otimes{\mathbb{I}}_{16}&{\mathrm Id}\otimes
\sum_a\Gamma_a\,x^a\\
{\mathrm Id}\otimes\sum_a(\Gamma_a)^\top\,x^a&-T_0\otimes{\mathbb{I}}_{16}
\end{array}\right)\ .$$

例如，取 $n=1$ 便得到快子场（式），其中对角矩阵代表 16 个 8-膜与 $\overline{8}$-膜，而非对角项对应于用 $8-\overline{8}$ 膜对构造 D-粒子的束缚态构造。因此，8-膜与 0-膜之间的关系（式）是 I 型超弦理论中 Bott 周期性映射的典型例子。

另一方面，KO-群的 Bott 周期性同构（式）来自把 $\widetilde{{\mathrm KO}}^{-n}(X)$ 的一个元素与 $\widetilde{{\mathrm KO}}({\mathbf S}^8)={\mathbb{Z}}$ 的生成元 $[{\mathcal N}_{{\mathbb{R}}}]-[I^8]$ 作杯积，其中 ${\mathcal N}_{\mathbb{R}}$ 是与实 Hopf 纤维化 ${\mathbf S}^{15}\rightarrow {\mathbf S}^8$ 相联系的实射影空间 ${\mathbb{R}} P^8$ 上的秩 7 Hopf 丛。这表明，在 I 型超弦理论中，用 $p+8$-$\overline{p+8}$ 膜对构造 $p$-膜，是由一个 D-弦孤子位形决定的，该位形给出了 $Spin(8)$ 瞬子的显式物理实现。相应的八维非平凡规范联络以及与之相伴的旋量结构可在 [hopf8] 中找到。这确定了生活在 $p+8$-$\overline{p+8}$ 膜对上的世界体积规范场的显式形式，这些规范场是保证快子场在无穷远附近协变常值、从而产生有限能量孤子 $p$-膜位形所必需的，正如 [hopf8] 所给出的

$$A_i^-(x)=0~~~~~~,~~~~~~
A_i^+(x)=-2i\,\sum_{j=1}^8\Gamma_{ij}\,\frac{x^j}{(1+|x|^2)^2}\ ,$$

其中 $\Gamma_{ij}$ 是 $Spin(8)$ 的生成元。这些规范场位形具有 $Spin(9)$ 对称性（从而保持显式的时空对称性），并携带单位拓扑荷。类似的论证适用于非 BPS D7-膜。

### I 型 D-弦

现在我们将把 I 型 D-弦展示为 9-膜与 $\overline{9}$-膜的束缚态，它位于 ${\mathbb{R}}^{10}$ 中 $x^1=\ldots =x^8=0$ 处，世界体积坐标为 $(x^0,x^9)$。保持 D-弦世界面不动的旋转群是 $SO(8)$，它旋转矢量 $x=(x^1,\ldots, x^8)$。$SO(8)$ 的两个旋量表示 ${\mathcal S}^{\pm}$ 都是八维的，其 Dirac 矩阵为 $\Gamma_a: {\mathcal S}^+\rightarrow {\mathcal S}^-$。因此我们考虑八个 9-膜与八个 $\overline{9}$-膜的位形，其规范丛平凡，但旋转群 $SO(8)$ 作用在 Chan-Paton 丛上：9-膜的秩八丛按 ${\mathcal S}^+$ 变换，$\overline{9}$-膜的则按 ${\mathcal S}^-$ 变换。快子场于是由（式）给出，而映射 $x\mapsto\sum_a\Gamma_a\,x^a/|x|$ 是 $\pi_7(SO(8))={\mathbb{Z}}$ 的生成元。与 4.5 节一样，在这个束缚态构造中不出现整体阻碍，因为 I 型时空 $X$ 是 spin 流形，可定向的二维 D-弦世界面也是（束缚态构造的整体版本将在 7.3 节给出）。上述构造中也不需要假定 D-弦世界体积是连通的。这意味着任意（互不相交的）D-弦集合都可以由八个 $9-\overline{9}$ 对的位形来表示，而无需为每条 D-弦再引入八个额外的对。这与 IIB 型情形形成对照：那里时空 $X$ 不必容许 spin 结构，一般必须通过添加额外的 $9-\overline{9}$ 对来进行 K-理论稳定化。

考察我们上面描述的一些规范孤子，并结合 I 型理论与 $Spin(32)/{\mathbb{Z}}_2$ 杂化弦理论之间的 $S$-对偶来看，是很有意思的。I 型 D-瞬子、D-粒子和 D-弦在杂化弦微扰论中都是显然可见的。D-弦等价于微扰杂化弦 [polwitten]，因此微扰杂化弦的第二量子化 Fock 空间可以完全由八个 $9-\overline{9}$ 膜对的位形来描述。（注意，对杂化 Matrix 弦理论也可以得到与 4.5 节类似的结论。）D-粒子是 $SO(32)$ 旋量表示中的一个规范孤子，就像基本杂化弦谱中的某些粒子一样。最后，D-瞬子给出了一种破坏 $O(32)$ 的不连通分支的机制，而这种对称性破缺在杂化弦微扰论中是显然可见的。因此，从杂化弦的角度看，这三个非微扰客体可以连续地连接到普通的微扰客体上。我们还注意到，上述所有束缚态构造（如同前几节的那些）都保持 D-膜横向空间的显式对称性。此外，为消除反常而必须添加的额外 32 个 9-膜给出一个 $SO(32)$ 规范对称性，它在上述构造中不起任何作用。束缚态构造利用额外的膜-反膜对来扩大规范群，从而使 $SO(32)$ 不变性显式可见。

### I 型 D5-膜与群 ${\mathrm KSp}(X)$

群 ${\mathrm KSp}(X)$ 对用辛规范丛量子化的 I 型 D-膜进行分类。辛规范对称性的出现可以从 [gimonpol] 的分析中理解（另见 [quivers]），其中世界面算子乘积展开的封闭性要求被证明会对离散规范对称性在 Chan-Paton 丛上的作用施加严格限制。特别地，世界面宇称算子 $\Omega$ 的平方作用在 Chan-Paton 指标上为

$$\Omega^2\,:\,~~~~|Dp;ab\rangle~\longmapsto~\sum_{a',b'}\left
(\gamma_\Omega^2\right)^{a'}_a\,\left|
Dp;a'b'\right\rangle\,\left(\gamma_\Omega^{-2}\right
)^{b'}_b=(\pm i)^{(9-p)/2}\,|Dp;ab\rangle$$

其中 $a,b$ 是 IIB 理论中一个 D$p$-膜态的开弦端点 Chan-Paton 标号，$\gamma_{\Omega}$ 表示 orientifold 群在 Chan-Paton 规范群中的伴随表示。虽然 9-膜具有标准的正交子群投影（如 tadpole 反常抵消所要求），但（式）表明，当作用在例如 5-膜上时 $\Omega^2=-1$（对相应的快子顶点算子 [witten] 也是如此）。因此 5-膜必须用伪实规范丛来量子化，即在 9-膜和 $\overline{9}$-膜上结构群为 $Sp(2N)$ 的 Chan-Paton 丛。另一种解释 [witten] 利用了这样一个事实：I 型 5-膜等价于占据真空的充满时空的 9-膜上的瞬子 [witteninst]。快子场把 9-$\overline{9}$ 膜位形的 $SO(4N)\times SO(4N)$ 规范对称性破缺到对角子群 $SO(4N)_{\mathrm diag}$，随后又被瞬子场进一步破缺到 $Sp(2N)$。（注意，对于单位 5-膜数目的位形，至少需要 $4N=4$ 个充满时空的膜-反膜对。）注意，（式）也解释了 I 型理论中稳定 BPS D-膜的标准谱，以及表中列出的世界体积规范群。

对于 ${\mathrm KSp}(X)$，与同伦论的联系由

$$\widetilde{{\mathrm KSp}}({\mathbf S}^n)=\pi_{n-1}\Bigl(Sp(k)\Bigr) \ , \ \ \ \ k>n/4\ ,$$

给出，其中 $k>n/4$ 定义了 ${\mathrm KSp}(X)$ 的稳定范围。如前，

$$\widetilde{{\mathrm KSp}}({\mathbf S}^n)=\pi_{n-1}\Bigl(Sp(\infty)\Bigr)\ ,$$

其中 $Sp(\infty)=\bigcup_kSp(k)$ 是无限辛群。在这种情况下 Bott 周期性取特殊形式

$$\pi_n\Bigl(Sp(\infty)\Bigr)=\pi_{n+4}\Bigl(O(\infty)\Bigr)\ ,$$

从而

$$\widetilde{{\mathrm KSp}}({\mathbf S}^n)=\widetilde{{\mathrm KO}}({\mathbf S}^{n+4})\ .$$

因此，辛 K-理论中的任何计算都可以化归为实 K-理论中的计算。相应膜荷的完整谱可在表中找到，它表明超对称 D-膜的谱保持不变，而稳定非 BPS 态的谱与先前不同。

[表：I 型弦理论中采用辛规范丛的 D-膜谱。]

| D-膜 | D9 | D8 | D7 | D6 | D5 | D4 | D3 | D2 | D1 | D0 | D(-1) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 横向空间 | ${\mathbf S}^0$ | ${\mathbf S}^1$ | ${\mathbf S}^2$ | ${\mathbf S}^3$ | ${\mathbf S}^4$ | ${\mathbf S}^5$ | ${\mathbf S}^6$ | ${\mathbf S}^7$ | ${\mathbf S}^8$ | ${\mathbf S}^9$ | ${\mathbf S}^{10}$ |
| $\widetilde{{\mathrm KSp}}({\mathbf S}^n)$ | ${\mathbb{Z}}$ | 0 | 0 | 0 | ${\mathbb{Z}}$ | ${\mathbb{Z}}_2$ | ${\mathbb{Z}}_2$ | 0 | ${\mathbb{Z}}$ | 0 | 0 |

同构（式）来自与秩 2 瞬子丛 ${\mathcal N}_{{\mathbb{H}}}$ 的类作杯积，该丛与伪实 Hopf 纤维化 ${\mathbf S}^7\rightarrow{\mathbf S}^4$ 相联系，即 ${\mathbb{C}} P^3$ 上秩 2 的全纯向量丛 [trautman]。因此，BPS $p$-膜与 BPS $p+4$-膜之间的关系是一个 5-膜孤子，它可以被等同于 $SU(2)$ Yang-Mills 瞬子场。例如，考虑 $5-\overline{5}$ 膜对世界体积中的一条 I 型 D-弦 [senbps]。世界体积规范对称性是 $SO(4)=SU(2)\times SU(2)$，快子场在其 ${\mathbf2}\otimes\overline{\mathbf2}$ 表示中变换。$\Omega$-投影把 5-膜位形的真空流形确定为 $SU(2)=Sp(1)$。D-弦的拓扑稳定性由同伦群 $\pi_3(SU(2))={\mathbb{Z}}$ 保证。当对场施加如下渐近形式时（类似于上式），相应的 5+1 维世界体积场论中存在有限能量的静态类弦解：

$$T\simeq T_v\,U~~~~,~~~~A^-\simeq0~~~~,~~~~A^+\simeq i\,dU\,U^{-1} \ .$$

这里 $U$ 是一个 $SU(2)$ 矩阵值函数，对应于从五维类弦位形的渐近边界 ${\mathbf S}^3$ 到 $SU(2)$ 群流形 ${\mathbf S}^3$ 的（单位绕数的）恒等映射。于是该弦孤子携带 1 单位瞬子数（生活在 5-膜上），已知它是 I 型超弦理论中 D-弦荷的源 [douglasinst,witteninst]。辛规范丛 K-理论的进一步应用将在第 6 节讨论。

### I 型与 II 型超弦理论之间的关系

K-理论形式体系已经给出了给定超弦理论中 D-膜之间的许多不同关系。事实证明，它还提供了 I 型理论与 II 型理论之间的新关系，下面我们接着简要描述。首先注意，4.4 节和 5.5 节中描述的余维 1 情形实际上是带有离散纤维 ${\mathbb{Z}}_2$ 的基本 Hopf 纤维化 ${\mathbf S}^1\rightarrow {\mathbf S}^1$ 的实现 [trautman]。把 I 型非 BPS 膜构造为膜-反膜对的扭结的一个例子，当然是 [seninst] 中从 D-弦-反 D-弦对构造 I 型 D-粒子的原始构造。${\mathbf S}^1$ 的双重覆盖对应于膜对，而快子场的绕数由纤维的同伦群（式）标记，该纤维对应于离散规范变换 $T\rightarrow -T$（因此 D-弦携带 ${\mathbb{Z}}_2$ 取值的 Wilson 线）。与 ${\mathrm KO}({\mathbf B}^1,{\mathbf S}^0)={\mathbb{Z}}_2$ 的生成元 $\omega$ 作杯积，便实现了 ${\mathbb{Z}}_2$ 取值的 KO-理论类在 ${\mathrm KO}(Y)\to{\mathrm KO}(Y\times{\mathbf B}^1,Y\times{\mathbf S}^0)$ 上所需的 ABS 映射。

一般来说，Hopf 纤维化

$${\mathbf S}^[n-1]~\hookrightarrow~{\mathbf S}^{2n-1}~\longrightarrow~{\mathbf S}^n$$

仅当 $n=1,2,4,8$ 时才是非平凡的，此时其纤维 ${\mathbf S}^[n-1]$ 是可平行化球面 [karoubi,husemoller]。这一拓扑事实与如下代数性质有关：实数域上只有四个赋范可除代数，分别对应于实数、复数、四元数和八元数（或 Cayley 数）。在这种情况下，决定相应拓扑孤子场的纤维化分类映射由主 $Spin(n)$ 丛（式）确定，并且是

$$\pi_{n-1}\Bigl(Spin(n)\Bigr)\,/\,\pi_{n-1}\Bigl(Spin(n-1)\Bigr)~
=~\left\{\begin{array}{cll}{\mathbb{Z}}_2~~~~&,&~~n=1\\{\mathbb{Z}}~~~~&,
&~~n=2,4,8\end{array}\right.$$

的生成元。正如我们所见，这四个 Hopf 纤维化决定了 I 型与 II 型超弦理论中 D-膜的所有基本束缚态构造，因此这些理论中 D-膜荷的完整谱依赖于只有四个这样的纤维化这一事实。对于 $n\neq 1$，相应孤子的拓扑荷由 Pontryagin 数密度给出，它正比于 $\mathrm{tr}(F^{n/2})$，其中 $F$ 是相关拓扑非平凡规范场位形的曲率。对于 $n=1$，荷由 ${\mathbb{Z}}_2$ 取值的 Wilson 线确定，如 [senbps] 中那样。这一特征用 II 型理论中的磁单极子来确定弦孤子，而在 I 型理论中我们得到的是作为扭结的非 BPS 膜、作为 $SU(2)$ 瞬子的 BPS 膜，以及作为 $Spin(8)$ 瞬子的 BPS 与非 BPS 膜。这一拓扑性质用更常规的孤子实现了所有 D-膜，并且还确定了生活在膜世界体积上的非平凡规范场的显式形式。因此，所有基本 D-膜构造、以及 I 型与 II 型超弦理论中 D-膜荷的完整谱，都相当自然地由四个非平凡 Hopf 纤维化 [os] 决定，它们由此为这两类弦理论之间提供了非平凡的联系。

从各类 K-理论之间存在的关系还可以推出一些进一步的联系。给定复向量丛 $E$，对应 $E\mapsto\overline{E}$ 在群 ${\mathrm K}(X)$ 上诱导一个对合。此外，实向量丛与复向量丛范畴上的实化函子与复化函子 $r$ 与 $c$ 诱导相应 K-群的同态。第一个把每个复向量丛对应到其底层的实向量丛，第二个把每个实向量丛 $E$ 对应到复向量丛 $E\otimes_{{\mathbb{R}}}{\mathbb{C}}\cong E\oplus E$。于是 I 型与 IIB 型理论的 K-群之间存在自然同态

$${\mathrm K}(X)\stackrel{r^*}{\longrightarrow}{\mathrm KO}(X)\stackrel{c^*}{\longrightarrow}
{\mathrm K}(X)\ .$$

注意复合 $r^*\circ c^*$ 是乘以 2，而 $(c^*\circ r^*)([E])=[E\oplus E]$。例如，考虑 $\widetilde{{\mathrm K}}({\mathbf S}^4)={\mathbb{Z}}$ 的生成元，即上面描述的伪实 $SU(2)$ 瞬子丛。要把它实现为标记 I 型 5-膜荷的 $\widetilde{{\mathrm KO}}({\mathbf S}^4)={\mathbb{Z}}$ 的生成元，必须把它嵌入正交结构群 $SO(4)=SU(2)\times SU(2)$ 中以使其成为实丛。在 $SO(4)$ 中的嵌入使荷加倍，因为（式）中从 ${\mathrm KO}({\mathbf S}^4)$ 到 ${\mathrm K}({\mathbf S}^4)$ 的自然映射是乘以 2，所以 I 型 5-膜的 RR 荷是 IIB 型 5-膜的两倍。这些事实可以看作自然周期性同构 [karoubi]

$${\mathrm KO}^{-n}(X,Y)\otimes_{{\mathbb{Z}}}{\mathbb{Z}}\left[\mbox{$\frac{1}{2}$}\right]=
{\mathrm KO}^{-n-4}(X,Y)\otimes_{\mathbb{Z}}{\mathbb{Z}}\left[\mbox{$\frac{1}{2}$}\right]\ ,$$

$${\mathrm K}^{-n}(X,Y)\otimes_{{\mathbb{Z}}}{\mathbb{Z}}\left[\mbox{$\frac{1}{2}$}\right]=
\left({\mathrm KO}^{-n}(X,Y)\oplus{\mathrm KO}^{-n-2}(X,Y)\right)\otimes_{{\mathbb{Z}}}
{\mathbb{Z}}\left[\mbox{$\frac{1}{2}$}\right]$$

的特例，它们可以用与 $SU(2)$ 瞬子丛的类作杯积来证明。更一般地，I 型与 II 型理论由正合列

$${\mathrm KO}^{-n-1}(X,Y)\stackrel{c^*}{\longrightarrow}{\mathrm K}^{-n-1}(X,Y)
\stackrel{r^*\circ\beta}{\longrightarrow}{\mathrm KO}^{-n+1}(X,Y)
\stackrel{\otimes\omega}{\longrightarrow}{\mathrm KO}^{-n}(X,Y)
\stackrel{r^*}{\longrightarrow}{\mathrm K}^{-n}(X,Y)$$

相联系，其中 $\beta:{\mathrm K}^{-n-1}(X,Y)\to{\mathrm K}^{-n+1}(X,Y)$ 是 Bott 周期性同构。

## 轨形与 orientifold 上的 D-膜

在本节中，我们将分析 II 型与 I 型理论的轨形（orbifold）和 orientifold 中 D-膜的性质。我们将看到，这一分类的自然 K-理论框架是等变 K-理论，它计入了时空上的群作用。等变 K-理论在数学中极受关注，因为它把上同调与群表示论融为一体。因此它对拓扑学和群论都具有核心重要性。下面我们将看到，它还导致这些理论中 D-膜谱的一些非平凡方面。


### 等变 K-理论

考虑轨道流形 $X/G$ 上的 IIB 型超弦理论，其中 $G$ 是 $X$ 的有限对称群。在本小节中我们将表明，$X/G$ 上的 D-膜由所谓 $X$ 的 $G$-等变 K-理论群来分类 [segal]。该群的定义如下。设 $X$ 是光滑流形，$G$ 是作用在 $X$ 上的群（一般地 $G$ 或为有限群，或为紧 Lie 群）。在这种情形下，我们说 $X$ 是一个{\it $G$-流形}，并把 $G$-作用 $G\times X\rightarrow X$ 写作 $(g,x)\mapsto g\cdot x$。两个 $G$-流形之间的{\it $G$-映射} $f:X\rightarrow Y$ 是与 $X$ 和 $Y$ 上 $G$-作用交换的光滑映射：

$$
f(g\cdot x)=g\cdot f(x)\ .
$$

换言之，$f$ 是 $G$-等变的。{\it $G$-丛} $E_G\rightarrow X$ 是主纤维丛 $E\rightarrow X$，其中 $E$ 是 $G$-流形，且典范的纤维投影 $\pi$ 是 $G$-映射，即对一切 $v\in E,\ g\in G$ 都有 $\pi(g\cdot v)=g\cdot \pi(v)$。$X$ 上 $G$-丛之间的{\it $G$-同构} $E_G\rightarrow F_G$ 是既为丛同构又为 $G$-映射的映射。这些条件定义了 $G$-空间 $X$ 上 $G$-等变丛的范畴。相应的 Grothendieck 群称为 $G$-等变 K-理论 ${\mathrm K}_{G}(X)$，即 ${\mathrm K}_{G}(X)$ 由带 $G$-作用的丛对 $(E,F)$ 组成，模去等价关系 $(E,F)\sim (E\oplus H, F\oplus H)$，其中 $H$ 是 $X$ 上任一 $G$-丛。

$X/G$ 上的 D-膜位形被理解为 $X$ 上 $G$-不变的 D-膜位形 [quivers]，即把轨道流形时空视为一个 $G$-空间。我们假定 $X$ 被赋予一个定向与一个自旋结构，二者都在 $G$ 下保持不变。给定一个 D-膜位形，即一个虚丛 $[(E,F)]$，我们可以假定 $G$ 作用在 $(E,F)$ 上，因为规范丛可以以完全 $G$-不变的方式构造。在快子凝聚中，我们假定丛对 $(H,H)$ 只有在 $G$ 以相同方式作用于 $H$ 的两个副本时才能被产生与湮灭（否则所需的快子场将不是 $G$-不变的）。于是我们得出结论：对轨道流形 $X/G$ 上的 IIB 型超弦，D-膜荷取值于 ${\mathrm K}_G(X)$。对 IIA 型类似地有 ${\mathrm K}^{-1}_{G}(X)$，而对 I 型我们得到 ${\mathrm KO}_{G}(X)$（这里 ${\mathrm K}_G^{-1}(X)\equiv {\mathrm K}_{G}(\Sigma X)={\mathrm K}_{G}({\mathbf S}^1\wedge X)$，其中 $G$ 平凡地作用在 ${\mathbf S}^1$ 上）。

设 $V_I$ 表示群 $G$ 的不可约有限维复表示向量空间。如同第 2.8 节那样，$G$-模的加法范畴关于向量空间直和的同构类 $[V_I]$，即满足 $[V_I]+[V_J]=[V_I\oplus V_J]$ 者，生成一个交换幺半群。相应的 Grothendieck 群 ${\mathrm R}(G)$ 称为群 $G$ 的{\it 表示环}。按照第 2.1 节的描述，${\mathrm R}(G)$ 的每个元素都可表为形式差 $[V_I]-[V_J]$，其中 $[V_I]$ 与 $[V_J]$ 是 $G$ 的有限维表示的等价类。于是 $[V_I]-[V_J]=[V_I']-[V_J']$ 当且仅当 $V_I\oplus V_J'$ 与 $V_I'\oplus V_J$ 酉等价。一如既往，向量空间的张量积 $V_I\otimes V_J$ 在 ${\mathrm R}(G)$ 上诱导出一个交换环结构。例如，设 $G={\mathbf S}^1$，并用 $y^m$ 记由

$$
\varphi_m(\sigma)\,z=\mbox{e}^{im\sigma}\,z\ , \ \ \ \ z\in {\mathbf S}^1\ ,
$$

定义的一维表示，其中 $\sigma\in{\mathbb{R}}$。那末容易看出，紧群 ${\mathbf S}^1=U(1)$ 的表示环是变量 $y$ 的形式 Laurent 多项式环：

$$
{\mathrm R}({\mathbf S}^1)={\mathbb{Z}}\left[y,y^{-1}\right]\ .
$$

循环子群 ${\mathbb{Z}}_n\subset {\mathbf S}^1$ 的表示环是 $n$ 个整数群的直和：

$$
{\mathrm R}({\mathbb{Z}}_n)={\mathbb{Z}}^{\oplus n}\ ,
$$

而环面群 ${\mathbf T}^n=U(1)^n$ 的表示环是 $n$ 个变量 $y_1,\ldots ,y_n$ 的形式 Laurent 多项式环：

$$
{\mathrm R}({\mathbf T}^n)={\mathbb{Z}}\left[y_1,y_2,\ldots,y_n,
(y_1y_2\cdots y_n)^{-1}\right]\ .
$$

一般地，对任何单连通 Lie 群 $G$，${\mathrm R}(G)$ 是 ${\mathbb{Z}}$ 上以 ${\mathrm rank}(G)$ 个生成元生成的多项式环 [segalR]。

对 ${\mathrm R}(G)$ 还有一种更熟悉的描述，即借助群 $G$ 的特征标空间。$G$-模 $V_I$ 的同构类完全由其特征标映射 $\mathrm{ch}i_{V_I}:G\to{\mathbb{C}}$ 决定，该映射由 $\mathrm{ch}i_{V_I}(g)=\mathrm{tr}_{V_I}(g)$ 定义。由于特征标具有性质 $\mathrm{ch}i_{V_I\oplus V_J}=\mathrm{ch}i_{V_I}+\mathrm{ch}i_{V_J}$、$\mathrm{ch}i_{V_I\otimes V_J}=\mathrm{ch}i_{V_I}\mathrm{ch}i_{V_J}$ 以及 $\mathrm{ch}i_{V_I}(hgh^{-1})=\mathrm{ch}i_{V_I}(g)$，可知映射 $V_I\mapsto\mathrm{ch}i_{V_I}$ 把 ${\mathrm R}(G)$ 等同于 $G$ 上 $G$-不变复值函数环的一个子环。我们将看到，表示环正确地纳入了由 $G$ 在 $X$ 上的作用所诱导的镜像膜荷的结构。

若 $G$ 平凡地作用于时空 $X$，则

$$
{\mathrm K}_G(X)={\mathrm K}(X)\otimes {\mathrm R}(G)\ ,
$$

其中 ${\mathrm K}(X)$ 是 $X$ 的通常 K-群。这可由以下事实推出：对平凡 $G$-作用，$G$-丛 $E$ 可分解为

$$
E\cong \bigoplus_{I}{\mathrm Hom}_G(E_I,E)\otimes E_I\ ,
$$

其中 $E_I=X\times V_I$ 是以 $V_I$ 为纤维的 $X$ 上平凡丛。更一般地，对任何紧 $G$-空间 $X$，坍缩映射 $X\rightarrow$ pt 在 ${\mathrm K}^\#_{G}(X)$ 上诱导出一个 ${\mathrm R}(G)$-模结构，使得 ${\mathrm R}(G)$ 成为等变 K-理论中的系数环（而不像通常情形那样只是 ${\mathbb{Z}}$）。${\mathrm K}_G$-函子享有我们在前几节中描述的通常 K-函子的大部分性质。此外，${\mathrm K}_{G}$ 关于群同态是函子性的。在这个意义上，${\mathrm K}_{G}(X)$ 是两个重要分类群 ${\mathrm K}(X)$ 与 ${\mathrm R}(G)$ 的推广，因而等变 K-理论把 K-理论与群表示论统一了起来。事实上，平凡空间 $X={\mathrm pt}$ 给出 ${\mathrm K}_G(X)={\mathrm R}(G)$，而平凡群 $G={\mathrm Id}$ 给出 ${\mathrm K}_G(X)={\mathrm K}(X)$。一个有用的“切除型”计算特征是：若 $H$ 是 $G$ 的闭子群，则对任何 $H$-空间 $X$，包含映射 $i:H\hookrightarrow G$ 诱导同构 $i^*:{\mathrm K}_{G}(G\times_HX)\stackrel{\approx}{\longrightarrow}{\mathrm K}_H(X)$。

若群 $G$ 自由地作用在 $X$ 上（即没有不动点），则 $X/G$ 也是拓扑空间，其 $G$-等变 K-理论就是

$$
{\mathrm K}_G(X)={\mathrm K}(X/G)\ .
$$

然而一般地 $X/G$ 并不是拓扑空间（更谈不上光滑流形），等变上同调要复杂得多。此时计算等变 K-理论的一个有用定理是第 2.6 节引入的六项正合列：

$$
{\begin{array}{ccccc}
{\mathrm K}_{G}^{-1}(X,Y)&\longrightarrow&{\mathrm K}_{G}^{-1}(X)&\longrightarrow&
{\mathrm K}_{G}^{-1}(Y)\\&
& & &\\{\scriptstyle\partial^*}\uparrow& & &
&\downarrow{\scriptstyle\partial^*}\\& & &
&\\ {\mathrm K}_{G}(Y)&\longleftarrow&{\mathrm K}_{G}(X)&\longleftarrow&{\mathrm K}_{G} (X,Y)\end{array}}
$$

其中 $Y$ 是局部紧 $G$-空间 $X$ 的闭 $G$-子空间，相对 K-理论由 ${\mathrm K}_{G}^{-n}(X,Y)=\widetilde{{\mathrm K}}_{G}^{-n}(X/Y)$ 定义（当商空间有意义时）。使用这一正合列的好处在于，可以取 $Y$ 为群作用在 $X$ 上的不动点集，于是商空间 $X/Y$ 上的 $G$-作用自由，其等变上同调便可如（式）那样作为其关于 $G$ 的商空间的通常上同调来计算。

从现在起，我们假定 $G$ 是时空流形 $X$ 的有限离散对称群。在 $X/G$ 的任何轨道流形奇点之外，D-膜荷按（式）分类，给出通常的 II 型谱，只需计入由 $G$-作用联系起来的镜像。因此我们想弄明白膜-反膜对在奇点处如何行为。为此我们需要知道轨道流形投影如何在 Chan-Paton 因子上实现。由轨道流形奇点中 D-膜的一般理论可知 [gimonpol,quivers]，$G$ 对 Chan-Paton 指标的作用由

$$
g\cdot{\mathcal X}(\Lambda)={\mathcal X}(\gamma_g\,\Lambda)\ ,
$$

给出，其中 $\Lambda$ 是场 $\mathcal X$ 的 Chan-Paton 因子，$\gamma_g$ 是 $g\in G$ 在 Chan-Paton 规范群中的表示。（一个例子是我们在第 3.1 节末尾所描述的 GSO 投影的作用。）特别地，如同向量势 $A_i(x)$ 一样，快子场在 $G$-轨道流形投影下以伴随表示变换，即它是 $G$-等变的：

$$
g\,:\,~~~~T(x)~~\longmapsto~~\gamma_g~T\left(g^{-1}\cdot x\right)
\,(\gamma_g)^{-1}\ .
$$

这样一来，快子场既可视为 $G$-丛映射 $T: E_G\rightarrow F_G$，也可等价地视为 $G$-丛 $(E\otimes F^*)_G$ 的 $G$-截面。

在轨道流形奇点上用 $9-\overline{9}$ 膜对来考虑膜荷时，与先前的讨论类似，只是现在要计入 $G$-作用下诱导的镜像，即在轨道流形奇点处，每个膜对都有 $|G|$ 个镜像对。$X/G$ 中世界体谱的向量多重态所给出的规范场定义了相应 Chan-Paton 丛的联络 $A_i(x)$。GSO 投影消去快子自由度，只留下向量多重态与超多重态的 quiver 结构 [quivers]。然而，当重合的膜与反膜缠绕轨道流形时空的子流形 $Y/G$ 时，快子场仍被 GSO 投影保留，而无质量向量多重态被投影掉，即 $G$-作用与 GSO 投影交换。$N$ 个缠绕 $Y\subset X$ 的膜的世界体场论由 $Y$ 上的 Chan-Paton 丛 $E$ 描述，其结构群为 $\prod_{I}U(Nn_I)$，其中 $n_I$ 是 $G$ 的第 $I$ 个正则表示的维数。无穷远处的真空位形现在以 $G$-等变的方式用 $G$ 的特征标重新表述。于是，只要（式）成立，所得的 $G$-不变真空便可经由快子凝聚达到。束缚态构造现在可以完全像前面那样进行。利用等变 K-理论在轨道流形上构造 D-膜的一些显式例子可在 [garcia] 中找到。

然而结果表明，对于足够“正则”的轨道流形，等变 K-理论其实并不提供按通常上同调理论或 K-理论尚未描述的新信息或新态 [gukov]。例如，等变 Bott 周期性 $\widetilde{{\mathrm K}}_G({\mathbf S}^{p+2})=\widetilde{{\mathrm K}}_G({\mathbf S}^p)$ 意味着 $\widetilde{{\mathrm K}}_G({\mathbf S}^{2k})=\widetilde{{\mathrm K}}_G({\mathbf S}^{0})={\mathrm R}(G)$，典型地给出通常 RR 荷的 $|G|$ 个副本。在等变情形，Bott 周期性定理把不同的 $|G|$ 个膜的集合相互联系起来，其中 $|G|$ 是轨道流形中镜像的数目。作为例证，考虑 ${\mathbf AdS}_5\times {\mathbf S}^5$ 上 IIB 型超引力的 ${\mathbb{Z}}_3$ AdS-轨道流形，它与边界上的 ${\mathcal N}=1$ 超共形场论对偶，后者是置于轨道流形奇点处 $N$ 个平行 D3-膜世界体上的 $SU(N)^3$ 规范理论 [lawrence]。超引力视界是透镜空间

$$
{\mathcal H}={\mathrm L}^2(3)\equiv{\mathbf S}^5/{\mathbb{Z}}_3\ .
$$

边界理论中的延展物体被理解为缠绕 ${\mathcal H}$ 中闭链的 IIB 型膜。视界的非平凡同调群为

$$
H_1({\mathcal H})=H_3({\mathcal H})={\mathbb{Z}}_3\ ,
$$

它们分别对应于缠绕 ${\mathcal H}$ 的一个一维闭链与一个三维闭链的 D3-膜与 D5-膜。然而还有缠绕三维闭链的 NS5-膜，对应于边界超共形场论的离散对称群 $({\mathbb{Z}}_3\times{\mathbb{Z}}_3)\,\rtimes{\mathbb{Z}}_3$。透镜空间 ${\mathcal H}$ 的 K-群为 [kambe]

$$
{\mathrm K}({\mathcal H})={\mathbb{Z}}_3\oplus{\mathbb{Z}}_3\cong H^{\mathrm even}({\mathcal H},{\mathbb{Z}})\ ,
$$

其中 $H^{\mathrm even}$ 表示通常上同调环中偶次元素的子环。于是 K-群正确地计入了 D3-膜与 D5-膜的挠荷，却遗漏了 NS5-膜那非交换的 ${\mathbb{Z}}_3$ 值荷。这毫不奇怪，因为拓扑 K-理论总带有底层的{\it 交换}环结构，并不计入 Neveu-Schwarz $B$-场（等价地，IIB 型超弦理论的 $S$-对偶对称性）[witten]。对这个特定的轨道流形例子，K-理论与通常上同调理论完全一致，并不给我们提供新的对象。这个例子属于特定的一类：其时空流形双有理等价于一个光滑环面簇，而对该簇 K-群是无挠的，因而将在第 7.1 节讨论的 Chern 特征标给出与相应上同调环的同构 [gukov]。鉴于这一特点，我们现在把注意力转向 orientifold，此时 $G$ 在 $X$ 上的离散几何作用还伴随着超弦理论上的世界面对称作用。


### 实 K-理论

实 KR-理论 [atiyahreal] 是一种广义 K-理论，它把复 K-理论、实 KO-理论（以及四元数 KSp-理论和自共轭 KSC-理论）同等变 K-理论融合在一起。我们将把上面的轨形构造特殊化到 $G={\mathbb{Z}}_2$ 的情形，于是空间 $X$ 被赋予一个对合，即一个满足 $\tau^2={\mathrm Id}_{X}$ 的同胚 $\tau: X\rightarrow X$。除等变上同调之外，我们还对世界面宇称变换 $\Omega$ 的作用取商。$\Omega$ 反转弦的定向，并在 $X$ 上的规范丛 $E$ 上诱导一个与 $\tau$ 交换的反线性对合。在作 $\Omega$ 的 orientifold 投影时（在 $X$ 上的 IIB 型弦论中），我们需要保留在 $\Omega$ 投影下实际上为偶的那些 K-理论类。由于 $\Omega$ 通过复共轭作用在 9-膜（以及 $\overline{9}$-膜）的 Chan-Paton 丛上，我们考虑一个作用在规范丛纤维上的诱导反线性对合 $\tau^*:E_x\rightarrow E_{\tau(x)}$，满足 $(\tau^*)^2=1$，它把 $E$ 映为其复共轭丛 $\overline{E}$。于是 $\tau^*(E)\cong \overline{E}$，其中同构 $\psi:\tau^*(E)\rightarrow \overline{E}$ 满足 $(\psi\tau^*)^2={\mathrm Id}$。现在我们在这种向量丛的范畴上定义一个等价关系：对任意同样被对合 $\tau^*$ 映为其复共轭的丛 $H$，令 $(E,F)\sim (E\oplus H,F\oplus H)$。$X$ 上所有带对合的虚拟丛的 Grothendieck 群称为实 K-群 ${\mathrm KR}(X)$。

如同通常做法，人们通过

$$
\widetilde{{\mathrm KR}}^{-m}(X)=\widetilde{{\mathrm KR}}(X\wedge {\mathbf S}^m)\ ,
$$

定义高阶群 ${\mathrm KR}^{-m}(X)$，其中 $X$ 上的对合 $\tau$ 通过在 ${\mathbf S}^m$ 上的平凡作用延拓到 $X\wedge {\mathbf S}^m$。更一般地，可以把定义（式）推广到 $\tau$ 在其上非平凡作用的球面。设 ${\mathbb{R}}^[p,q]$ 是 $p+q$ 维实空间，其中的对合表现为对最后 $q$ 个坐标的反射，即对 $(x,y)\in {\mathbb{R}}^p\times{\mathbb{R}}^q$ 有 $\tau:(x,y)\mapsto (x,-y)$。设 ${\mathbf S}^[p,q]$ 是 ${\mathbb{R}}^[p,q]$ 中关于 ${\mathbb{R}}^p\times{\mathbb{R}}^q$ 上平坦欧氏度量的 $p+q-1$ 维单位球面。有了这些定义，我们可以按照

$$
\widetilde{{\mathrm KR}}^[p,q](X)=\widetilde{{\mathrm KR}}(X\wedge{\mathbb{R}}_+^[p,q])\ ,
$$

定义一个双参数的高阶 KR-群族，或者利用悬置同构写成

$$
{\mathrm KR}^[p,q](X)={\mathrm KR}(X\times {\mathbb{R}}^[p,q])\ .
$$

由这些定义有

$$
{\mathrm KR}^{-n}(X)={\mathrm KR}^[n,0](X)\ .
$$

KR-理论中的 Bott 周期性取如下形式

$$
\begin{matrix}
{\mathrm KR}^[p,q](X)&=&{\mathrm KR}^{p+1,q+1}(X)\ ,\\
{\mathrm KR}^{-m}(X)&=&{\mathrm KR}^{-m-8}(X)\ .
\end{matrix}
$$

关系（式）意味着 ${\mathrm KR}^[p,q](X)={\mathrm KR}^[q-p](X)$，因此 ${\mathrm KR}^[p,q](X)$ 只依赖于差 $p-q$。关系（式）则表明 ${\mathrm KR}^[p,q](X)$ 只依赖于该差模 8。这意味着人们可以把负维球面定义为 KR-理论中带对径对合的球面，其中 ${\mathbf S}^[n,0]$ 等同于 ${\mathbf S}^[n-1]$，而 ${\mathbf S}^{0,n}$ 等同于 ${\mathbf S}^{-n-1}$。注意，若我们把 ${\mathbb{R}}^{1,1}={\mathbb{C}}$ 与由复共轭作用的对合 $\tau$ 等同起来，则 $(1,1)$ 周期性定理（式）取特别漂亮的形式

$$
{\mathrm KR}(X)={\mathrm KR}(X\times{\mathbb{C}})\ ,
$$

对任意局部紧空间 $X$ 成立。

由于下列内部对称性，KR-理论是 K-理论和 KO-理论的推广。若对合 $\tau$ 在 $X$ 上平凡作用，则

$$
\begin{matrix}
{\mathrm KR}^{-m}(X\times {\mathbf S}^{0,1})&=&{\mathrm K}^{-m}(X)\ ,\\
{\mathrm KR}^{-m}(X)&=&{\mathrm KO}^{-m}(X)\ .
\end{matrix}
$$

关系（式）来自如下事实：空间 $X\times {\mathbf S}^{0,1}$ 可以等同于 $X$ 的双重覆盖 $\tilde{X}=X\amalg X$，其中 $\tau$ 通过交换 $\tilde{X}$ 中两份 $X$ 而作用。特别地，若 $X^{\tau}$ 记映射 $\tau:X\rightarrow X$ 的不动点集，则

$$
{\mathrm KR}^{-n}(X^{\tau})={\mathrm KO}^{-n}(X^{\tau})\ ,
$$

因为对合 $\tau$ 在不动点上平凡作用。实 K-理论中还有许多其他这类内部对称性，来自负维球面的使用。利用域 ${\mathbb{R}}$、${\mathbb{C}}$ 和 ${\mathbb{H}}$ 中的乘法映射以及 (1,1) 周期性，可以建立如下同构 [atiyahreal]

$$
{\mathrm KR}(X\times {\mathbf S}^{0,p})=
{\mathrm KR}^{-2p}(X\times{\mathbf S}^{0,p})\ ,
$$

分别对应 $p=1,2$ 和 4。$p=1$ 时的这个同构给出复 Bott 周期性定理，而实周期性定理可由 $p=4$ 的情形推出。事实上存在通常的自然同构

$$
{\mathrm KR}^{-n}(X\times{\mathbf S}^{0,p})=
{\mathrm KR}^{-n}(X)\oplus{\mathrm KR}^{p+1-n}(X)\ ,
$$

对所有 $p\geq 3$ 成立。$p=2$ 的情形特殊，此时不存在到 $X$ 的 KR-群的分解，将在第 6.5 节讨论。同样，第 2 节中讨论的大部分性质在实情形下都有显然的对应物。特别地，第 2 节中导出的乘积公式也可以推广到 KR-理论（正如它们对 KO-理论所做的那样）。例如，重复导致（式）的步骤，在 $\tau$ 对 $X$ 平凡作用时我们可以得到乘积公式

$$
\begin{matrix}
\widetilde{{\mathrm KR}}^{-1}(X\times{\mathbf S}^{1,1})&=&\widetilde{{\mathrm KR}}^{-1}
(X\wedge{\mathbf S}^{1,1})\oplus\widetilde{{\mathrm KR}}^{-1}(X)\oplus
\widetilde{{\mathrm KR}}^{-1}({\mathbf S}^{1,1})\\
&=&\widetilde{{\mathrm KR}}^{1,1}(X)\oplus\widetilde{{\mathrm KO}}^{-1}(X)
\oplus{\mathbb{Z}}\\
&=&\widetilde{{\mathrm KO}}(X)\oplus\widetilde{{\mathrm KO}}^{-1}(X)\oplus{\mathbb{Z}}\ ,
\end{matrix}
$$

其中我们用了 $(1,1)$ 周期性、关系（式）以及如下事实

$$
\widetilde{{\mathrm KR}}^{-1}({\mathbf S}^{1,1})={\mathrm KR}^{-1+1}({\mathrm pt})
={\mathrm KO}({\mathrm pt})={\mathbb{Z}} \ .
$$

对 $X={\mathbf S}^n$，周期性定理（式）也可以由实 K-理论的 ABS 构造推出。为此，我们对实空间 ${\mathbb{R}}^[n,m]$ 定义一个双参数的 Clifford 代数族 $C\ell({\mathbb{R}}^[n,m])$，即与 ${\mathbb{R}}^{n+m}$ 相联系的通常代数，再配上由 $\tau$ 在 ${\mathbb{R}}^[n,m]$ 上的作用生成的一个对合。$C\ell({\mathbb{R}}^[n,m])$ 上的实模则是带有保持 Clifford 乘法的 ${\mathbb{C}}$-反线性对合的有限维表示。相应的表示环 ${\mathrm R}[Spin(n,m)]$ 自然同构于由空间 ${\mathbb{R}}^n\oplus{\mathbb{R}}^m$（其二次型具有 Lorentz 号差 $(n,m)$）的 Clifford 代数的不可约实模 $\Delta_{n,m}$ 生成的 Grothendieck 群，如第 2.8 节那样。ABS 映射现在就是分次环同构 [lawson, atiyahreal]

$$
{\mathrm KR}({\mathbb{R}}^[n,m])~\cong~{\mathrm R}\Bigl[Spin(n,m)\Bigr]\,/
\,i^*\,{\mathrm R}\Bigl[Spin(n+1,m)\Bigr]~=~{\mathrm KO}^[n-m]({\mathbf S}^0)\ ,
$$

其中最后一个等式用了周期性关系（式）、（式）和（式）。这个同构把（式）左端的群与 Clifford 代数 $C\ell_{n,m}$ 联系起来，于是拓扑的 $(1,1)$ 周期性（式）可由代数的 $(1,1)$ 周期性（式）推出。

下面我们讨论如何用实 K-理论对 $\Omega$-orientifold 中的 D-膜作分类。一般地，$G$ 在 $X$ 上作用的不动点集是若干 $p+1$ 维平面，称为 orientifold $p$-平面，简称 O$p$-平面。它们决定了给定轨形的奇点。对目前的 orientifold 群作用，这些对象是非动力学的，但它们本身具有 D-膜的许多性质。例如，它们带 RR 荷，并且有轻的开弦态连接它们与 D-膜，这增强了位于 orientifold 平面上重合膜的规范对称性。具有非平凡规范对称性意味着这些理论的超对称真空态必须包含 32 个 D$p$-膜，才能使真空呈中性（这同样是蝌蚪反常抵消的要求）。我们想确定局域在 $X/\Omega\cdot G$ 的 orientifold 平面上的稳定（但可能非 BPS）态的荷。注意，远离 orientifold 平面时，我们可以把时空流形 $X$ 看作由双重覆盖 $\tilde{X}\rightarrow X$ 表示，orientifold 群 $\Omega\cdot G$ 把 $\tilde{X}$ 的两个不连通分支相互映照。利用（式），我们看到远离 O$p$-平面时理论看起来就像普通的 II 型超弦理论。因此我们只关心局域在奇异的 O$p$-平面上的态会怎样。

由周期性关系（式）和（式），我们可以相当一般地证明

$$
{\mathrm KR}({\mathbb{R}}^[d-p,9-d])={\mathrm KR}({\mathbb{R}}^{2d-p-1,0})\ ,
$$

其中我们把时空 $X$ 等同于实空间 ${\mathbb{R}}^{d+1}\times({\mathbb{R}}^{9-d}/\Omega\cdot{\mathcal I}_{9-d})$，${\mathcal I}_{9-d}$ 是作用在横向空间 $9-d$ 个坐标上的反射 $\tau$。KR-群（式）分类局域在 orientifold $d$-平面上的 D$p$-膜荷。在（式）右端，KR-对合平凡作用，于是

$$
{\mathrm KR}({\mathbb{R}}^[d-p,9-d])={\mathrm KO}({\mathbf S}^{2d-p-1})\ .
$$

在（式）中令 $d=9$ 给出通常分类 I 型超弦理论中 D$p$-膜荷的群 ${\mathrm KO}({\mathbf S}^{9-p})$。令 $d=8$ 则给出

$$
{\mathrm KR}^{-1}({\mathbb{R}}^[d-p-1,1])={\mathrm KO}^{-1}({\mathbf S}^{15-p})
={\mathrm KO}({\mathbf S}^{8-p})\ ,
$$

即 I 型荷谱移动一位。在下一小节将证明，时空流形 $X$ 上 I 型理论的 $T$-对偶由 ${\mathrm KR}^{-1}(X)$ 分类，这与（式）一致。一般地，对给定的 orientifold 平面维数 $d$，可以用（式）以及相应的 KO-群表，配上适当的周期移动，读出位于 $d$-平面上的 D-膜的荷。例如 $d=5$ 时得到局域在 O5-平面上的稳定 D-膜荷的分类。该谱类似 I 型弦论的谱：有一个带 ${\mathbb{Z}}$ 荷的 D-弦、一个带 ${\mathbb{Z}}_2$ 荷的规范孤子和一个带 ${\mathbb{Z}}_2$ 荷的规范瞬子。该谱与用 IIB 型 $p$-膜-反膜对构造 orientifold $p$-膜的束缚态构造完全一致，也与结果（式）一致，后者表明快子模只有在 $p=-1,7$ 时才被 $\Omega$ 投影去掉。对 IIA 型 orientifold 可以作类似分析。

KR-理论 $(1,1)$ 周期性还可以给出物理解释 [os]。考虑 II 型 $\Omega\cdot{\mathcal I}_m$ orientifold 中余维 $n+m$ 的 $p$-膜。$p$-膜的荷由快子场诱导，该快子场由横向空间 ${\mathbb{R}}^[n,m]$ 上的 Clifford 乘法给出，即 $T(x)=\sum_i\Gamma_i\,x^i$，其中 $\Gamma_i$ 是旋量模 $\Delta_{n,m}$ 的生成元，它生成 $\widetilde{{\mathrm KR}}({\mathbb{R}}^[n,m])$。在 ABS 同构（式）下，这个 KR-理论类通过杯积与 $\widetilde{{\mathrm KR}}({\mathbb{C}} P^1)={\mathbb{Z}}$ 的 Hopf 生成元（带由反线性复共轭对合诱导的自然实结构）相乘，或等价地与承载旋量表示 $\Delta_{1,1}$ 的旋量丛相乘。这给出一个类，其快子场生成新横向空间 ${\mathbb{R}}^{n+1,m+1}$ 的 KR-群。这个类表示 $\Omega\cdot{\mathcal I}_{m+1}$ orientifold 中的一个 $p-2$-膜。由这一数学事实可以推出 II 型 orientifold 理论的一个新的降维关系：在 II 型 $\Omega\cdot{\mathcal I}_{m+1}$ orientifold 中局域于 O$(8-m)$-平面的 $p-2$-膜，被构造为位于 II 型 $\Omega\cdot{\mathcal I}_m$ orientifold 中 O$(9-m)$-平面之上的 $p$-$\overline{p}$ 对束缚态的快子孤子。这把 II 型 orientifold 的膜实现为 orientifold 中膜-反膜对世界体内的等变磁单极子，而该 orientifold 的不动点平面的维数高一维。前者的 orientifold 有 $2^m$ 个 O$(8-m)$-平面，每个带 RR 荷 $-2^{3-m}$；后者有 $2^{m+1}$ 个 O$(9-m)$-平面，荷为 $-2^{4-m}$。在快子凝聚过程中，不动点平面的数目加倍，而它们的荷通过荷转移（经由等变磁单极子）与经由 orientifold 平面的维数约化的联合操作降低一个因子 2。一个例子是 IIB 型理论中位于 orientifold 5-平面之上的 D5-膜组成的非 BPS 态 [senbps]，它可以由 IIA 型理论中 orientifold 6-平面上一对 D7-D$\overline{7}$ 膜经快子凝聚构造出来。8 个各带荷 $-2$ 的 O$6$-平面被转移到 16 个荷为 $-1$ 的 O$5$-平面。

### I 型$\,^\prime$ D-膜与 ${\mathrm KR}^{-1}(X)$

I 型$\,^\prime$ 超弦理论是 I 型理论的 $T$-对偶，它可以作为 IIA 型弦论的 $X/\Omega\cdot {\mathcal I}_1$ 形式的 orientifold 得到。该理论包含不稳定的充满时空的 9-膜，其组态在模去基本 9-膜的创生与湮灭之后分类所有 D-膜荷。用 K-理论的语言，这对应于群 ${\mathrm KR}^{-1}(X)$，或等价类 $[(E,\alpha)]$ 的群，其中 $E$ 是带有与 orientifold 群交换的对合的实丛，$\alpha$ 是 $E$ 的也保持 orientifold 群作用的自同构。在 I 型$\,^\prime$ 弦论中，$E$ 等同于充满时空的 9-膜世界体上的 Chan-Paton 丛。在 orientifold 平面上，规范对称性从 $U(N)$ 约化为 $O(N)$。每个单独的低维膜都表示为一定数目的不稳定 I 型$\,^\prime$ 9-膜的束缚态。快子凝聚要求尊重 ${\mathbb{Z}}_2$ orientifold 对称性（如（式）那样），对应于一个 ${\mathbb{Z}}_2$-等变磁单极子。我们将在下一小节更详细地讨论后一个性质。


### II 型 orientifold 的束缚态构造

对 $m$-环面 ${\mathbf T}^m$ 上的 I 型理论作 $T$-对偶变换，得到 ${\mathbf T}^m/\Omega\cdot{\mathcal I}_m$ 上的 II 型 orientifold。本节我们将借助 K-理论性质描述这类 orientifold 理论的若干方面，从而推广上一小节的讨论。特别地，我们将说明该形式体系如何使人自然地导出 I 型理论的 $T$-对偶理论中快子凝聚的完整真空流形集合（见表 7），并由此得到这些模型中 D-膜的世界体积场内容。

| $m$ | 实旋量模 | 维数 | 真空流形 | 对偶理论 |
|---|---|---|---|---|
| 0 | --- | --- | $O(N)$ | I 型 |
| 1 | $\Delta_1$ | 1 | $\frac{O(2N)}{O(N)\times O(N)}$ | I$\,^\prime$ 型 |
| 2 | $\Delta^+_2\oplus\Delta^-_2$ | 2 | $\frac{U(2N)}{O(2N)}$ | ${\mathbf T}^2/\Omega\cdot{\mathcal I}_2$ 上的 IIB |
| 3 | $\Delta_3\oplus\Delta_3$ | 4 | $\frac{Sp(2N)}{U(2N)}$ | ${\mathbf T}^3/\Omega\cdot{\mathcal I}_3$ 上的 IIA |
| 4 | $\Delta^\pm_4\oplus\Delta^\pm_4$ | 4 | $Sp(2N)$ | $K3$ 上的 IIA |
| 5 | $\Delta_5\oplus\Delta_5$ | 8 | $\frac{Sp(4N)}{Sp(2N)\times Sp(2N)}$ | $K3\times{\mathbf S}^1$ 上的 IIB |
| 6 | $\Delta^+_6\oplus\Delta^-_6$ | 8 | $\frac{U(8N)}{Sp(4N)}$ | ${\mathbf T}^6/\Omega\cdot{\mathcal I}_6$ 上的 IIB |
| 7 | $\Delta_7$ | 8 | $\frac{O(16N)}{U(8N)}$ | ${\mathbf T}^7/\Omega\cdot{\mathcal I}_7$ 上的 IIA |
| 8 | $\Delta^+_8\oplus\Delta^-_8$ | 8 | $O(16N)$ | ${\mathbf T}^8/{\mathbb{Z}}_2$ 上的 IIA |

[表：时空 $X=Y\times {\mathbf T}^{1,m}$ 上的 II 型 orientifold 理论，其 D-膜荷由群 ${\mathrm KR}^{-m}(X)$ 分类。表中对每种情形列出一般的对偶 orbifold 模型（第 5 列），以及 $2^{[m/2]+1}N$ 个充满时空的 9-膜世界体积中快子凝聚所对应的真空流形（第 4 列），该真空流形的稳定同伦群与 ${\mathrm KR}^{-m}(X)$ 一致。第 2 列列出相应的实旋量模，它被用来把 I 型理论的每个 KO-理论类映为 orientifold 的相应 KR-理论类。它们的维数（第 3 列）决定了 K-理论稳定化所要求的、束缚态构造中 9-膜数目应增加的量。]

（超弦紧致化将在第 7 节以更一般的方式讨论。）与普通 II 型理论中快子凝聚的两个唯一真空流形（式）与（式）形成对照，如今出现的丰富结构是 KO- 与 KR-函子 8 重周期性的结果。用迭代环路空间来说，$\Omega^nBO(k)$ 与 $\Omega^{n+8}BO(k)$ 具有相同的同伦型，而 $0\leq m\leq 7$ 时的 $\Omega^mO(k)$ 与表 7 第四列所给李群的环路空间具有相同的同伦型 [bott]。因此，II 型 orientifold 的真空流形是 KO-理论同伦性质的十分自然的推论。事实上，这些世界体积规范对称性的辨认，是纯粹由 K-理论作出的真正的新预言。此外，8 的周期性也与如下事实相符：II 型 orientifold 的区分性质与对偶性的循环，在紧致化环面 ${\mathbf T}^8$ 上重新开始。（关于 II 型 orientifold 及其模空间性质的简明综述可见 [mukhi]。）在本小节余下的部分，我们将对这些稳定同伦性质的出现给出一些物理解释。更多细节可见 [os]。

在 ${\mathbf T}^1={\mathbf S}^1$ 上作 $T$-对偶变换后，如上一小节所述，超弦理论就成为 I$\,^\prime$ 型理论。I 型与 I$\,^\prime$ 型之间的映射，类似于 II 型超弦理论中 $T$-对偶把 IIB 型映为 IIA 型的映射。诱导出的荷取值于更高阶的 KO-群 $\widetilde{{\mathrm KO}}^{-1}({\mathbf S}^{l+1})$，由此我们辨认出表 7 第二行中的真空流形。接下来考虑 I 型理论的环面紧致化，它与 ${\mathbf T}^2/{\mathbb{Z}}_2$ orientifold 上的 IIB 型超弦理论 $T$-对偶。其中有 $N$ 对 7-$\overline{7}$ 膜-反膜对，它们用 $2N$ 对 9-$\overline{9}$ 膜-反膜对来描述，而这些膜-反膜对正是原 I 型理论中 D-膜束缚态构造所用到的。于是在对偶的 orientifold 模型中，低维膜可以由 7-膜出发、用前面描述的“下降”（descent）程序构造出来。表 7 第三行中出现酉群 $U(2N)$，则源于以下事实。回忆 2.8 节：手征旋量模 $\Delta_2^\pm$ 是复的，因此为了保持 I 型理论的实性（reality）性质，所需的那一个通过两个 I 型理论 K-群之间的杯积把我们联系起来的映射，必须相对于实旋量模 $\Delta_2^+\oplus\Delta_2^-$ 来取，如（式）所示。束缚态构造所需的 9-膜总数，由原来的 9-膜数目乘以旋量表示的维数（表 7 第 3 列）给出。因此相关的同伦是相对于一个酉对称空间定义的。物理上，酉规范对称性的出现仍可由（式）理解：它在 7-膜上导致不相容性，因此 7-膜要用未投影的酉规范丛来量子化。于是，虽然充满时空的 9-膜上的朴素规范群是 $O(2N)\times O(2N)\subset O(4N)$，但 IIB 7-膜上不相容的 $\Omega$-投影把对称性增强为 $U(2N)$。所需的快子场 $T(x)$ 必须相对 orientifold 投影是 ${\mathbb{Z}}_2$-等变的（以便所得低维膜组态在 ${\mathbb{Z}}_2$-作用下不变），亦即它按 orientifold 群像（式）那样变换。如 [witten] 所示，$p$-$\overline{p}$ 膜-反膜对的快子顶点算符在 $\Omega^2$ 作用下获得相位 $(\pm i)^{7-p}$。对 7-膜而言，该算符在 $\Omega^2$ 下为偶，因而真空期望值 $T_0$ 的本征值是实的。于是快子场把 $U(2N)$ 规范对称性破缺到其正交子群 $O(2N)$，诱导出的膜荷由绕 ${\mathbf T}^2/{\mathbb{Z}}_2$ 上 IIB orientifold 的真空流形 $U(2N)/O(2N)$ 的绕数标记。注意，一般地，$X=Y\times {\mathbf T}^{1,m}$ 上的 II 型 orientifold 由 KR-群 ${\mathrm KR}^{-m}(X)$ 描述。实现 I 型理论与 orientifold 理论之间 $T$-对偶的 KO-群与 KR-群之间的显式关系，将在 7.4 节描述。

对 $m=3$，我们得到 ${\mathbf T}^3$ 上的 I$\,^\prime$ 型理论，它与 IIA 型超弦理论的 ${\mathbf T}^3/{\mathbb{Z}}_2$ orientifold $T$-对偶。表 7 中辛规范群的出现，源于如下数学事实：复旋量模 $\Delta_3$ 是某个四元数 Clifford 模的限制，因此 9-膜上旋量丛的适当增广是相对于秩 4 实表示 $\Delta_3\oplus\Delta_3$ 来取的。这意味着现在有 $4N$ 个不稳定的 9-膜，其世界体积规范对称为 $Sp(2N)$。这一被增强的 $Sp(2N)$ 对称性来自给定的 I$\,^\prime$ 型 $p-3$-膜用 6-$\overline{6}$ 膜-反膜对表示的中间表示 [os]，并且用 5-膜很容易理解，如我们在 5.7 节所讨论的。同样由 ${\mathbb{Z}}_2$-等变性，快子场把该规范群破缺到其复子群 $U(2N)$，于是真空流形为 $Sp(2N)/U(2N)$。表 7 的其余部分可由类似论证推出。注意，在 $m=4$ 紧致化之后旋量模与真空流形结构的变化，与如下性质一致：此时 orientifold 平面开始获得分数 RR 荷，从而导致这些弦理论具有非常不同的模空间 [mukhi]。

在表 7 最后一列，我们还标出了与 I 型理论给定环面紧致化相应的对偶超弦紧致化（见 [mukhi] 及其中的文献）。对 $m=4,5$ 和 8 的情形我们看到，I 型理论（或相应 II 型 orientifold）的模空间实际上非微扰地对偶于 II 型超弦理论的一个通常的{\it orbifold}。相应的 ${\mathbb{Z}}_2$-等变 K-群已在 [os] 中用乘积公式（式）与（式）以及六项正合列（式）算出（另见后面 6.6 节末的计算）。这给出了一种启发式地检验所述对偶的办法。然而，对偶操作涉及 II 型理论的一次中间 $S$-对偶变换，而它在 K-理论框架内的描述目前尚不清楚（再次见后面 6.6 节的讨论）。因此人们并不能得到相应 K-群的同构，尽管朴素地会期望如此。K-群的 $T$-对偶变换将在 7.4 节描述。

在辨认出 II 型 orientifold 模型的真空流形之后，我们现在来描述其场内容，此时必须谨慎地辨认相关真空流形的适当同伦。Real 向量丛的分类空间在 [krclass] 中描述。考虑 IIB 型理论的一个 orientifold，以及一组世界体积规范对称为 $U(N)\times U(N)$ 的膜-反膜对。$U(N)$ 规范群带有其厄米共轭对合，使得不动点集为实子群 $O(N)$。快子场 $T$ 相对 orientifold 群是等变的，因此

$$T(x,-y)=T(x,y)^*$$

其中 $(x,y)\in{\mathbb{R}}^n\oplus{\mathbb{R}}^m$ 是到诱导的低维膜组态横向空间的坐标。它把世界体积规范对称性破缺到 $U(N)_{\mathrm diag}$。由（式）生成的相关同伦群，来自把 ${\mathbb{R}}^[n,m]$ 的单点紧致化分解为上下两个半球（如 2.7 节所述），使得快子场是重叠区域上的转移函数。于是 D-膜荷居于横向空间的 KR-群中，即

$$\widetilde{{\mathrm KR}}({\mathbb{R}}^[n,m])=\pi_{n,m}\Bigl(U(N)\Bigr)_{\mathrm R}$$

其中同伦群由满足（式）的 Real 等变性条件的映射 ${\mathbf S}^[n,m]\to U(N)$ 定义。KR-理论中稳定同伦的精化 Bott 周期性定理则写为

$$\pi_{n,m}\Bigl(U(\infty)\Bigr)_{\mathrm R}=
\pi_{n+1,m+1}\Bigl(U(\infty)\Bigr)_{\mathrm R}$$

类似地，可以把 Real K-群 $\widetilde{{\mathrm KR}}^{-1}({\mathbb{R}}^[n,m])=\widetilde{{\mathrm KR}}({\mathbb{R}}^{n+1,m})$ 与复 Grassmann 流形 $U(2N)/[U(N)\times U(N)]$ 的稳定等变同伦联系起来。注意，这些情形中生活在膜世界体积上的规范场也必须满足与（式）类似的等变性条件。这些评注澄清了 orbifold 与 orientifold 理论束缚态构造中“等变孤子”（equivariant soliton）一词的含义。

### $\widetilde{\mathrm I}$ 型 D-膜与 ${\mathrm KSC}(X)$

I$\,^\prime$ 型超弦理论有两个 orientifold O$8^-$ 平面，各自带 $-8$ 单位 RR 荷。I$\,^\prime$ 型有一个自然的推广，即把它的一个 O$8^-$ 平面换成一个 O$8^+$ 平面，后者带 RR 荷 $+8$，并用辛规范丛（即 $\Omega^2=-1$）来量子化。该理论不需要任何 D8-膜就能使超对称真空呈电中性，因此它没有规范群，但其谱中仍含有有趣的稳定非 BPS D-膜。为分类 D-膜荷，较方便的做法是从该理论的 $T$-对偶出发，这已在 [wittenvec] 中给出。该理论通过将圆周上 IIB 型的一个 ${\mathbb{Z}}_2$ 对称性规范化（gauging）而得到，该对称性由世界面宇称 $\Omega$ 与沿圆周平移半个周长的组合实现。这个理论通常称为 $\widetilde{\mathrm I}$ 型。因此 $\widetilde{\mathrm I}$ 型 D-膜荷的自然 K-群是 ${\mathrm KR}(X\times {\mathbf S}^{0,2})$；当 $X$ 上的对合作用平凡时，已知它同构于 $X$ 上自共轭丛的 K-群 KSC$(X)$ [atiyahreal]。后一群可如下定义。设 $X$ 是带有对合 $\tau$ 的紧致 Real 流形。$X$ 上的{\it 自共轭}丛是一个复向量丛 $E$ 连同同构 $\alpha: E\stackrel{\approx}{\longrightarrow}\overline{(\tau^* E)}$。自共轭 K-理论 KSC$(X)$ 于是定义为由自共轭丛的范畴生成的 Grothendieck 群。

我们先证明

$${\mathrm KR}(X\times {\mathbf S}^{0,2})={\mathrm KSC}(X) \ .$$

考虑空间 $X\times{\mathbf S}^{0,2}$，并把圆周 ${\mathbf S}^{0,2}$ 分解为两半 ${\mathbf S}^{0,2}_{\pm}$，满足 ${\mathbf S}^{0,2}_+\cap{\mathbf S}^{0,2}_-=\{\pm 1\}$。如通常那样，$X\times{\mathbf S}^{0,2}$ 上的一个 Real 向量丛 $E$ 等价于指定 $X\times{\mathbf S}^{0,2}_+$ 上的一个复向量丛 $E_+$（即 $E$ 的相应限制）连同同构

$$\psi: E|_{X\times\{ +1\}}\stackrel{\approx}{\longrightarrow}
\tau^*(\overline{E}|_{X\times\{ -1\}}) \ .$$

由于 $X\times\{ +1\}$ 是 $X\times{\mathbf S}^{0,2}_+$ 的形变收缩核，我们实际上有同构 $E_+|_{X\times\{ -1\}}\stackrel{\approx}{\longrightarrow}E_+|_{X\times\{ +1\}}$，且它在同伦意义下唯一。这意味着给定 $\psi$ 在同伦意义下等价于给出同构 $\alpha: E\stackrel{\approx}{\longrightarrow}\overline{(\tau^* E)}$。换言之，$X\times{\mathbf S}^{0,2}$ 上 Real 丛的同构类与 $X$ 上自共轭丛的同伦类一一对应。取 $\tau$ 为平凡，我们就得到 ${\mathrm KR}(X\times{\mathbf S}^{0,2})$ 与紧致流形 $X$ 上带有反线性自同构 $\alpha:E\stackrel{\approx}{\longrightarrow}E$ 的向量丛 $E$ 的 K-理论之间所要的对应。

利用这一等价性，$\widetilde{\mathrm I}$ 型超弦理论的 D-膜荷谱可用 [green] 的结果算出，并总结于下表。

| D-膜 | D8 | D7 | D6 | D5 | D4 | D3 | D2 | D1 | D0 | D(--1) |
|---|---|---|---|---|---|---|---|---|---|---|
| 横向空间 | ${\mathbf S}^1$ | ${\mathbf S}^2$ | ${\mathbf S}^3$ | ${\mathbf S}^4$ | ${\mathbf S}^5$ | ${\mathbf S}^6$ | ${\mathbf S}^7$ | ${\mathbf S}^8$ | ${\mathbf S}^9$ | ${\mathbf S}^{10}$ |
| $\widetilde{{\mathrm KSC}}({\mathbf S}^n)$ | ${\mathbb{Z}}$ | ${\mathbb{Z}}_2$ | 0 | ${\mathbb{Z}}$ | ${\mathbb{Z}}$ | ${\mathbb{Z}}_2$ | 0 | ${\mathbb{Z}}$ | ${\mathbb{Z}}$ | ${\mathbb{Z}}_2$ |

[表：由 $\widetilde{{\mathrm KSC}}({\mathbf S}^n)$ 得到的 $\widetilde{\mathrm I}$ 型超弦理论中的 D-膜谱。]

这表明 K-理论预言了 $\widetilde{\mathrm I}$ 型理论中一个有趣的 BPS 与非 BPS 态谱。分析相应的群 $\widetilde{{\mathrm KO}}({\mathbf S}^n)$ 与 $\widetilde{{\mathrm KSp}}({\mathbf S}^n)$ [bgh]，就能正确计入其荷分布在两类 O8-平面上的稳定 BPS D-膜。另一方面，在某一类奇异平面附近局部稳定的、带 ${\mathbb{Z}}_2$ 荷的非 BPS D-膜，可能由于完整时空中的其他奇异性而变得不稳定 [bgh]。例如，分析 $\widetilde{{\mathrm KO}}({\mathbf S}^n)$ 表明存在一个非 BPS D6-膜，它在 O8$^-$-平面附近局部稳定，因为 orientifold 投影去掉了 D6-膜镜像 D$\overline{6}$-膜系统中存在的快子模。然而在 O8$^+$-平面处 orientifold 投影不同，于是快子不再被去掉，该非 BPS D6-膜在整体理论中也不再稳定。表中取 ${\mathbb{Z}}_2$ 值的荷，正是那些整体稳定的非 BPS 态。

自共轭向量丛的分类空间 $BSC(k)$ 在 [green] 中描述，因此 KSC-群与同伦论通过

$${\mathrm KSC}(X)=\Bigl[X\,,\,BSC(\infty)\Bigr] \ .$$

相联系。另一方面，与同伦论的联系也可由 KR-理论表示推出，由此我们可以辨认 $\widetilde{\mathrm I}$ 型理论中 D-膜的相关束缚态构造。由（式）可知自共轭 K-理论的 Bott 周期为 4。回忆群 ${\mathrm KR}^{-4}(X\times{\mathbf S}^{0,2})$ 把辛投影联系到 $\Omega$。因此 KSC-理论的 4 重周期性表明 $\widetilde{\mathrm I}$ 型的对偶同时具有 O8$^-$ 与 O8$^+$ 平面，因为这意味着正交与辛规范群在该模型中以同等地位出现。一般地，自共轭 K-理论通过以下长正合列与复、实及四元数 K-理论紧密相连 [anderson]：

$$\begin{matrix}
&\ldots\longrightarrow
{\mathrm K}^{-n-1}(X)\longrightarrow{\mathrm K}^{-n-1}(X)\longrightarrow{\mathrm KSC}^{-n}(X)
\longrightarrow{\mathrm K}^{-n}(X)\longrightarrow\\
&~~~~~~\longrightarrow{\mathrm K}^{-n}(X)\longrightarrow\ldots\\
&\ldots\longrightarrow{\mathrm K}^{-n-1}(X)\longrightarrow
{\mathrm KO}^{-n}(X)\oplus{\mathrm KSp}^{-n}(X)\longrightarrow{\mathrm K}^{-n}(X)\longrightarrow\\
&~~~~~~\longrightarrow{\mathrm KSC}^{-n-2}(X)\longrightarrow\ldots\\
&\ldots\longrightarrow
{\mathrm KSC}^{-n-1}(X)\longrightarrow{\mathrm K}^{-n}(X)\longrightarrow{\mathrm KO}^{-n}(X)\oplus
{\mathrm KSp}^{-n}(X)\longrightarrow\\
&~~~~~~\longrightarrow{\mathrm KSC}^{-n}(X)\longrightarrow\ldots
\end{matrix}$$

这些正合列可由 Barratt-Puppe 正合列（式）的 KR 版本以及切除定理（式）应用于对 $(X\times{\mathbf S}^{0,p},X\times{\mathbf S}^{0,q})$（分别取 $(p,q)=(2,1)$、$(3,1)$ 和 $(3,2)$）而建立。这些序列说明：荷由给定 KSC-群分类的 D-膜组态的对称性，如何与 I 型和 II 型弦的 K-理论中出现的规范对称性网络相关联。这些相互关系可能有助于把上述分析推广到其他没有向量结构的 I 型模型 [wittenvec]。


### Hopkins 群 ${\mathrm K}_{\pm}(X)$

本小节我们将研究 IIB 型超弦理论的 orientifold，它们通过对合 $\tau\cdot{(-1)^{F_{\mathrm L}}}$ 作商而得到，其中 $F_{\mathrm L}$ 是左行时空费米子数算符。算符 ${(-1)^{F_{\mathrm L}}}$ 使 RR 扇区中所有时空场变号，因此一个 BPS D-膜的 RR 荷变号，并在 ${(-1)^{F_{\mathrm L}}}$ 作用下被映到它的反膜。在此情形，$X/\tau\cdot{(-1)^{F_{\mathrm L}}}$ 上的 D-膜位形与 $X$ 上那些 K-理论类在 ${\mathbb{Z}}_2$ 作用下为奇的位形相联系。这意味着 $\tau^*$ 把对 $(E,F)$ 映为 $(F,E)$，即存在同构 $\psi:(E,F)\stackrel{\approx}{\longrightarrow}(\tau^*(F),\tau^*(E))$，满足 $(\psi\tau^*)^2={\mathrm Id}$。平凡对是 $(H,H)$，其中 $H\cong\tau^*(H)$。相应的 Grothendieck 群称为 Hopkins 群，记作 ${\mathrm K}_{\pm}(X)$ [witten,gukov]。

可以证明，群 ${\mathrm K}_{\pm}(X)$ 可以用通常的等变 K-理论来计算，即
$$
\widetilde{{\mathrm K}}_{\pm}(X)={\mathrm K}^{-1}_{{\mathbb{Z}}_2}(X\times{\mathbb{R}}^{0,1})\ ,
$$
其中循环群 $G={\mathbb{Z}}_2$ 在 $X\times{\mathbb{R}}^{0,1}$ 上的作用，是 $\tau$ 在 $X$ 上的作用与 ${\mathbb{R}}^{0,1}$ 的一个反定向对称作用的乘积。上式的正确性可以这样来论证：把 ${\mathrm K}_{\pm}(X)$ 定义为一个满足正合序列的（广义）上同调理论，
$$
\ldots\longrightarrow{\mathrm K}^{-n}_{{\mathbb{Z}}_2}(X)\longrightarrow{\mathrm K}^{-n}(X)
\longrightarrow{\mathrm K}^{-n}_{\pm}(X)\longrightarrow\ldots \ .
$$
把（上式）与关于对 $(M,A)=(X\times{\mathbb{R}}^{0,1},X\times({\mathbb{R}}^{0,1}-{\mathrm  pt}))$ 的六项正合序列（式）相比较，就得到如下一对正合序列：
$$
{\begin{array}{ccccccccc}
{\mathrm K}^{-n}_{{\mathbb{Z}}_2}(X)&\rightarrow&{\mathrm K}^{-n}(X)&
\rightarrow&{\mathrm K}^{-n}_{\pm}(X)&\rightarrow&{\mathrm K}^{-n-1}_{{\mathbb{Z}}_2}(X)&
\rightarrow&{\mathrm K}^{-n-1}(X)\\ & & & & & & & &\\\parallel& &\parallel& &\downarrow&
&\parallel& &\parallel\\ & & & & & & & &\\
{\mathrm K}^{-n}_{{\mathbb{Z}}_2}(A)&\rightarrow&{\mathrm K}^{-n-1}_{{\mathbb{Z}}_2}(M,A)&
\rightarrow&{\mathrm K}^{-n-1}_{{\mathbb{Z}}_2}(X\times{\mathbb{R}}^{0,1})&
\rightarrow&{\mathrm K}^{-n-1}_{{\mathbb{Z}}_2}(A)&
\rightarrow&{\mathrm K}^{-n}_{{\mathbb{Z}}_2}(M,A)\end{array}} \ .
$$
对（上式）应用五项引理（five-lemma），即（式）中两个正合序列之间的四个同构蕴涵着余下的中间那个竖直映射也是同构 [spanier]，我们就得到（式）。也可以给出一个独立的代数论证，它利用相应 Clifford 代数的自同构群 [gukov]。

对于形如 $X={\mathbb{R}}^{d+1}\times({\mathbb{R}}^{9-d}/{(-1)^{F_{\mathrm L}}}\cdot{\mathcal I}_{9-d})$ 的 orientifold，一个 orientifold $d$-平面上的相应 D$p$-膜荷取值于 $\widetilde{{\mathrm K}}_{\pm}({\mathbb{R}}^[d-p,9-d])$。由于（式）的右端表示复向量丛范畴上的一个等变函子，我们可以利用乘以 ${\mathbb{C}}$ 或 ${\mathbb{C}}/{\mathbb{Z}}_2$ 的悬浮同构来导出周期性
$$
\widetilde{{\mathrm K}}_{\pm}({\mathbb{R}}^[p,q])=\widetilde{{\mathrm K}}_{\pm}({\mathbb{R}}^{p,q+2})\ \ \ ,
\ \ \ \widetilde{{\mathrm K}}_{\pm}({\mathbb{R}}^[p,q])=\widetilde{{\mathrm K}}_{\pm}({\mathbb{R}}^{p+2,q})\ .
$$
这蕴涵 $\widetilde{{\mathrm K}}_{\pm}({\mathbb{R}}^[d-p,9-d])$ 只依赖于 $p$ 与 $d$ 的奇偶性。先设 $d$ 是偶数。此时利用（式）与（式）可以算出
$$
\widetilde{{\mathrm K}}_{\pm}({\mathbb{R}}^[d-p,9-d])={\mathrm K}^{-1}_{{\mathbb{Z}}_2}({\mathbb{R}}^[d-p,10-d])
={\mathrm K}^[p-1]_{{\mathbb{Z}}_2}({\mathrm pt})=
\left\{\begin{array}{cl}{\mathrm R}[{\mathbb{Z}}_2]&~~~~,~~p~~{\mathrm odd}\\0&~~~~,
{}~~p~~{\mathrm even}\end{array}\right.\ ,
$$
其中 ${\mathrm R}[{\mathbb{Z}}_2]={\mathbb{Z}}\oplus{\mathbb{Z}}$ 是循环群 ${\mathbb{Z}}_2$ 的表示环。于是，当 $d$ 为偶数时，我们得到定域在奇维 orientifold 平面上的、$p$ 为奇的 BPS D$p$-膜荷的标准谱（表示环 ${\mathrm R}[{\mathbb{Z}}_2]$ 计入了由给定对合所诱导的镜像膜荷）。$d$ 为奇数的情形要稍微复杂一些。为此，我们把六项正合序列（式）应用于对 $({\mathbf B}^[d-p,9-d],{\mathbf S}^[d-p,9-d])$，得到
$$
\ldots\stackrel{\partial^*}{\longrightarrow}
{\mathrm K}^{-p}_{{\mathbb{Z}}_2}({\mathbf B}^{0,9-d+1},{\mathbf S}^{0,9-d+1})\longrightarrow
{\mathrm K}^{-p}_{{\mathbb{Z}}_2}({\mathbf B}^{0,9-d+1})\stackrel{i^*}{\longrightarrow}
{\mathrm K}^{-p}({\mathbb{R}} P^{9-d})\stackrel{\partial^*}{\longrightarrow}\ldots
$$
这里我们用了悬浮同构，且 ${\mathbb{R}} P^{9-d}={\mathbf S}^{0,9-d+1}/{\mathbb{Z}}_2$ 是实射影空间。（上式）中的第一个 K-群同构于我们所感兴趣的 Hopkins 群 $\widetilde{{\mathrm K}}_{\pm}({\mathbb{R}}^[d-p,9-d])$。对第二个 K-群，我们利用球 ${\mathbf B}^{0,9-d+1}$ 是等变可缩的这一事实，得到 ${\mathrm K}^{-p}_{{\mathbb{Z}}_2}({\mathbf B}^{0,9-d+1})={\mathrm K}^{-p}_{{\mathbb{Z}}_2}({\mathrm pt})=\delta^{p,{\mathrm even}}\,{\mathrm R}[{\mathbb{Z}}_2]$。正合序列（式）由此把所关心的 K-群与实射影空间的上同调联系起来 [karoubi]：
$$
{\mathrm K}^{-p}({\mathbb{R}} P^{9-d})=\delta^{p,{\mathrm even}}\,{\mathbb{Z}}\oplus{\mathbb{Z}}_{2^r}\ ,
$$
其中 $r=\left[\frac{9-d}{2}\right]$。对环结构的细致分析表明，（式）中的满射 $i^*$ 把 ${\mathrm K}^{-p}_{{\mathbb{Z}}_2}({\mathbf B}^{0,9-d+1})$ 的两个生成元都映入 ${\mathrm K}^{-p}({\mathbb{R}} P^{9-d})$ 的生成元，即 $i^*$ 是这些 K-群的自由部分的满射。于是序列（式）的正合性蕴涵
$$
{\mathrm K}^{-p}_{{\mathbb{Z}}_2}({\mathbf B}^{0,9-d+1})={\mathrm K}^{-p}({\mathbb{R}} P^{9-d})\,/\,
{\mathrm K}^{-p}_{{\mathbb{Z}}_2}({\mathbf B}^{0,9-d+1},{\mathbf S}^{0,9-d+1})\oplus{\mathbb{Z}}_{2^r} \ ,
$$
由此我们最终得到，当 $d$ 为奇数时
$$
\widetilde{{\mathrm K}}_{\pm}({\mathbb{R}}^[d-p,9-d])=
\left\{\begin{array}{cll}{\mathbb{Z}}~~~~&,&~~p~~{\mathrm even}\\0~~~~&,
&~~p~~{\mathrm odd}\end{array}\right.\ ,
$$

作为一个例子，我们看到 O5-平面上的 D-粒子携带取整数值的荷。该位形与相应 $\Omega\cdot{\mathcal I}_4$ orientifold 的 O5-平面上的稳定非 BPS D-粒子互为 $S$-对偶 [sentachyon,senparticle]。这里出现的表面矛盾源于一个通常的事实：如第 6.4 节所述，K-理论只对弱弦耦合下拓扑稳定对象的荷作分类。如何让 K-理论正确地纳入 IIB 型超弦理论的 $S$-对偶对称性，迄今仍是一个未解决的问题。注意，（式）中的膜荷与 IIA 型超弦理论的膜荷相一致这一点，在当前情形下可以追溯到 IIB 型 orientifold 的边界态，其形式为 [sentachyon,senparticle]
$$
|\widetilde{Dp}\rangle
=\mbox{$\frac{1}{2}$}\,\Bigl(|Up,+\rangle_{{\mathrm NS}}-|Up,-\rangle_{{\mathrm NS}}\Bigr)
+\mbox{$\frac{1}{2}$}\,\Bigl(|Tp,+\rangle_{{\mathrm R}}+|Tp,-\rangle_{{\mathrm R}}\Bigr)\ ,
$$
其中 $T$ 与 $U$ 标记 ${(-1)^{F_{\mathrm L}}}$ orientifold 投影下闭弦 Hilbert 空间的扭曲扇区与无扭曲扇区。边界态（式）与通常 IIA 型 D$p$-膜的边界态形式完全相同。

与 IIA 型理论的关系也可以通过在上述构造中取 $d=0$ 来看出。此时我们只是用算符 ${(-1)^{F_{\mathrm L}}}$ 对 IIB 型理论作商，而众所周知这把它映入 IIA 型超弦理论。一般地，用 ${(-1)^{F_{\mathrm L}}}$ 对 II 型谱作 $m$ 次商这一操作确定了一个映射 [os]
$$
\widetilde{{\mathrm K}}^{-n}(X)\longrightarrow\widetilde{{\mathrm K}}^{-n-1}_{{\mathbb{Z}}_2}(X\times{\mathbb{R}}^{0,m})\ ,
$$
其中现在 ${\mathbb{Z}}_2$ 只作为 ${\mathbb{R}}^{0,m}$ 上的反射而作用。（式）的右端可以用六项正合序列（式）来计算。例如，对 $m=1$，我们在（式）中考虑对 $(X\times{\mathbb{R}}^{0,1}, X\times\{0\})$。此时商空间 $X\times{\mathbb{R}}^{0,1}/X\times\{0\}$ 同伦于两份 $X\times{\mathbb{R}}$，它们被对合相互交换。由于 ${\mathbb{Z}}_2$ 在该商空间上的作用是自由的，等变 K-群可以利用 K-函子的同伦不变性与悬浮同构算出：
$$
{\mathrm K}_{{\mathbb{Z}}_2}^{-n-1}\Bigl((X\times{\mathbb{R}})\amalg(X\times{\mathbb{R}})\Bigr)
={\mathrm K}^{-n-1}(X\times{\mathbb{R}})={\mathrm K}^{-n}(X)\ .
$$
在 $X\times\{0\}$ 上 ${\mathbb{Z}}_2$ 作用是平凡的，因此
$$
{\mathrm K}_{{\mathbb{Z}}_2}^{-n-1}\Bigl(X\times\{0\}\Bigr)={\mathrm K}^{-n-1}(X\times{\mathrm pt})\otimes
{\mathrm R}[{\mathbb{Z}}_2]\ .
$$
最后，由于在此情形 $X\times\{0\}$ 是 $X\times{\mathbb{R}}^{0,1}$ 的等变收缩核，我们有 $\ker\partial^*={\mathrm K}_{{\mathbb{Z}}_2}^{-n-1}(X\times\{0\})$，于是（式）中的水平正合序列分裂。一般的结果便是
$$
\widetilde{{\mathrm K}}^{-n-1}_{{\mathbb{Z}}_2}(X\times{\mathbb{R}}^{0,m})
=\left(\widetilde{{\mathrm K}}^{-n-1}(X)\otimes {\mathrm
R}[{\mathbb{Z}}_2]\right)\oplus\widetilde{{\mathrm K}}^{-n-m-1}(X)
\ .
$$
（上式）中的群 $\widetilde{{\mathrm K}}^{-n-1}(X)$ 来自 ${\mathbb{Z}}_2$ 作用的平凡部分，因而表示无扭曲的膜荷。另一部分 $\widetilde{{\mathrm K}}^{-n-m-1}(X)$ 来自 ${\mathbb{Z}}_2$ 作用的自由部分，表示扭曲扇区。

$n=0$、$m=1$ 的情形对应于用 ${(-1)^{F_{\mathrm L}}}$ 对 IIB 型理论作商的结果 [os]。于是，（式）中到第一个因子的投影表示把作商后的 IIB 型膜位形凝聚到相应的 IIA 型 D-膜上（连同上 ${(-1)^{F_{\mathrm L}}}$ 投影下的镜像）。（式）中的第二个直和项表示 ${(-1)^{F_{\mathrm L}}}$ 商的扭曲扇区，在映到 IIA 型理论的映射中它应当被适当地投影掉。再作一次 ${(-1)^{F_{\mathrm L}}}$ 商相应于在（式）中取 $n=1$、$m=2$，它把理论映回 IIB 型，同时把同一组扭曲荷投影掉。关于用 K-理论类显式构造这些映射的更多细节可在 [os] 中找到。这一 K-理论构造与 [daspark] 中的边界态描述一致，也与 [sendescent] 中对 II 型 $p-\overline{p}$-膜位形开弦谱的分析一致。在前一情形中已经表明，用算符 ${(-1)^{F_{\mathrm L}}}$ 对闭超弦 Hilbert 空间作商的结果投影到所有 IIB 型 $p$-膜边界态的 NS-NS 部分，扭曲扇区没有贡献。结果便是形如（式）的边界态，如第 4 节所讨论的，它可以通过快子凝聚衰变为稳定的 IIA 型 D$(p-1)$ 位形。另一方面，$p$-膜与 $\overline{p}$-膜的叠加可以用边界态来描述（参见（式）与（式））
$$
|Dp\rangle+|D\overline{p}\rangle=|Dp,+\rangle_{{\mathrm NS}}-
|Dp,-\rangle_{{\mathrm NS}}\ ,
$$
它由此产生与上面所得相同的位形。在这些情形中，K-理论构造表明，对填满时空的 IIB 型 9-膜作 ${(-1)^{F_{\mathrm L}}}$ 商，会留下数目相等的（全同的）9-膜与 $\overline{9}$-膜，它们正是构造 $p-\overline{p}$ 膜对的束缚态时所用的 [os]。这再次与最终通过快子凝聚达到的 IIA 型 $p-1$-膜位形完全一致。${(-1)^{F_{\mathrm L}}}$ 映射作为 K-理论群上典范投影的自然性，只不过表明了一个事实：如 [daspark] 所讨论的，${(-1)^{F_{\mathrm L}}}$ 作为 II 型超弦理论的真正非微扰对称性而起作用。

## 整体方面

上一节结束了我们对用拓扑 K-理论分类 D-膜的各种方式的普遍分析。在现阶段人们还想研究许多更奇特的理论，例如由算符 $\Omega\cdot{(-1)^{F_{\mathrm L}}}\cdot{\mathcal I}_m$ 作商而产生的 orientifold。然而，相应于这类对合的（等变）K-群尚未被很好地理解（一些讨论见 [gukov,os]），这样的分析必须等待数学文献的进一步发展。我们要指出，后一类 orientifold 对于更彻底地描述上文第 6.2--6.4 节的 II 型 orientifold 也很重要：严格说来，$\Omega\cdot{\mathcal I}_m$ orientifold 投影应当伴随算符 $(-1)^{\frac{1}{2}(9-p)(8-p)F_{\mathrm L}}$ 对 D$p$-膜态的作用，才能保持 ${\mathbb{Z}}_2$-等变结构。可能存在基于{\it 代数} K-理论的方法，它们也能用来纳入 $S$-对偶以及 M-膜的构造，正如 [vancea] 最近所讨论的。我们在此不追究这类问题，它们充其量仍处于非常初步的阶段。取而代之，在本最后一节中我们将分析：当我们计入（可能非平凡的）时空 $X$ 的整体拓扑以及相应的膜世界体嵌入时，会出现哪些有趣的 D-膜位形。

### Chern 特征

在着手描述 D-膜的整体方面及其相应的束缚态构造（我们将在第 7.3 节开始这一工作）之前，我们首先还需要一些数学上的准备。在处理一个空间的各种整体性质时，除了相应 Chan-Paton 丛的 K-理论之外，我们还将不得不考虑流形的上同调。K-理论之所以在各种应用中如此有用，其中一个特征便是存在 Chern 特征同态，它通过把环 ${\mathrm K}^\#(X)$ 与通常的上同调环 $H^\#(X)$ 联系起来，从而在 K-理论与普通上同调理论之间提供了一条纽带（这里我们主要处理 \v{C}ech 上同调）。本小节我们将描述拓扑 K-理论中 Chern 特征的构造。

设 $E$ 是紧拓扑空间 $X$ 上秩为 $k$ 的复向量丛。我们可以给 $E$ 联系上某些上同调类 $c_n(E)\in H^{2n}(X,{\mathbb{Z}})$，称为 $E$ 的{\it Chern 示性类}，它们度量向量丛的扭曲，其定义如下。如同第 2.7 节那样，我们考虑分类空间 $BU(k)$ 上的万有丛 $Q(k,\infty;{\mathbb{C}})$，其拉回生成诸如 $E$ 这样的向量丛，即对某个映射 $f:\, X\rightarrow BU(k)$ 有 $E=f^*Q(k,\infty;{\mathbb{C}})$。分类空间的上同调环 $H^\#(BU(k),{\mathbb{Z}})$ 有偶次生成元 $c_n(Q(k,\infty;{\mathbb{C}}))$，它们在 $f$ 下的拉回恰是 $E$ 的示性类：
$$
c_n(E)\equiv f^*c_n\Bigl(Q(k,\infty;{\mathbb{C}})\Bigr)\in H^{2n}(X,{\mathbb{Z}})\ .
$$
这些示性类的基本性质如下：

- (i) $c_0(E)=1\in H^0(X,{\mathbb{Z}})$。
- (ii) 对一切 $l\geq 0$，$c_l(E\oplus F)=\sum_{n+m=l}c_n(E)\wedge c_m(F)$。
- (iii)（自然性）若 $f:Y\rightarrow X$ 是连续映射，则 $c_n(f^*E)=f^*c_n(E)$。

对秩为 $k$ 的丛 $E$，{\it 全 Chern 类}定义为
$$
c(E)=1+c_1(E)+\ldots+c_k(E)\ ,
$$
而由上面性质 (ii) 可知 $c(E)$ 在 Whitney 和下是乘性的，
$$
c(E\oplus F)=c(E)\wedge c(F) \ ,
$$
特别地，我们可以援引{\it 分裂原理}，它断言 $E$ 总是一些复线丛 ${\mathcal L}_n$ 的 Whitney 和（更确切地说，$E$ 是另一个空间上某个为线丛之和的向量丛的拉回）[karoubi]，并取
$$
E={\mathcal L}_1\oplus{\mathcal L}_2\oplus\cdots\oplus{\mathcal L}_k\ .
$$
于是有
$$
c(E)=\prod_{n=1}^kc({\mathcal L}_n)=\prod_{n=1}^k(1+\lambda_n)\ ,
$$
其中我们定义了 $\lambda_n\equiv c_1({\mathcal L}_n)$。这就给出 $E$ 的 Chern 类用 2-上闭链 $\lambda_n$ 的初等对称函数表示的显式表达式：
$$
\begin{matrix}
c_1(E)&=\sum_n\lambda_n\\
c_2(E)&=\sum_{n<m}\lambda_n\wedge\lambda_m\\
&\cdots\\
c_m(E)&=\sum_{n_1<n_2<\cdots<n_m}\lambda_{n_1}\wedge \lambda_{n_2}\wedge\cdots
\wedge \lambda_{n_m}\\
&\cdots\\
c_k(E)&=\lambda_1\wedge
\lambda_2\wedge\cdots\wedge \lambda_k\ .
\end{matrix}
$$

向量丛 $E$ 的{\it Chern 特征}现定义为
$$
\mathrm{ch}(E)=\sum_{n=1}^k\mbox{e}^{\lambda_n}\in H^\#(X,{\mathbb{Q}})\ ,
$$
它可以看作这些示性类的生成函数。注意它取值于有理上同调 $H^\#(X,{\mathbb{Q}})=H^\#(X,{\mathbb{Z}})\otimes_{\mathbb{Z}}{\mathbb{Q}}$，因此 $\mathrm{ch}(E)$ 探测不到上同调的任何挠子群。利用（式），非齐次上闭链（式）的 $2m$ 次部分 $\mathrm{ch}_m(E)$ 可以用 $E$ 的示性类写出。例如，
$$
\mathrm{ch}(E)\equiv\sum_{m\geq0}\mathrm{ch}_m(E)=k+c_1(E)+\frac12\Bigl(c_1(E)\wedge c_1(E)
-2c_2(E)\Bigr)+\dots \ .
$$
类 $c_m(E)$（因而 Chern 特征）的定义可以推广到秩不必为常数的丛。为此，把 $X$ 划分成开子集 $X_i$，使 $E|_{X_i}$ 的秩为常数，然后把 $c_m(E)$ 定义为满足 $c_m(E)|_{X_i}=c_m(E|_{X_i})$ 的唯一上同调类。

Chern 特征具有如下性质：

- (i) $\mathrm{ch}_0(E)=\mathrm{rk}(E)\in H^0(X,{\mathbb{Z}})$。
- (ii) $\mathrm{ch}(E\oplus F)=\mathrm{ch}(E)+\mathrm{ch}(F)$。
- (iii) $\mathrm{ch}(E\otimes F)=\mathrm{ch}(E)\wedge\mathrm{ch}(F)$。
- (iv)（自然性）对任意连续映射 $f:Y\rightarrow X$，$\mathrm{ch}(f^*E)=f^*\,\mathrm{ch}(E)$。

这些性质蕴涵 Chern 特征尊重向量丛范畴上的半环结构。注意性质 (i) 与（式）中定义的秩函数建立了明确的联系，即虚拟维数定义了零次的一个示性类。事实上，我们可以用 Chern 特征给出 ${\mathrm K}(X)$ 与上同调环 $H^\#(X)$ 之间的一个完备映射。即，对虚拟丛 $[(E,F)]\in{\mathrm K}(X)$，我们定义同态
$$
\begin{matrix}
\mathrm{ch}:\, {\mathrm K}(X)&\longrightarrow H^\#(X,{\mathbb{Q}})\\
\mathrm{ch}\Bigl(\left[E\right]-\left[F\right]\Bigr)&= \mathrm{ch}(E)-\mathrm{ch}(F)\ .
\end{matrix}
$$
只要在 ${\mathrm K}(X)$ 中 $[(E,F)]=[(G,H)]$ 蕴涵 $\mathrm{ch}(E)-\mathrm{ch}(F)=\mathrm{ch}(G)-\mathrm{ch}(H)$，该映射就是良定义的。这一点确实成立，是 Chern 特征在 Whitney 和下的行为 (ii) 的推论。对于 $X={\mathbf S}^{2n}$ 这一特殊情形，映射 ch 是到 $H^\#({\mathbf S}^{2n},{\mathbb{Z}})$ 上的同构。更一般地，可以证明 [atiyahhirz]，相应的映射
$$
\mathrm{ch}:\, {\mathrm K}(X)\otimes_{{\mathbb{Z}}}{\mathbb{Q}}\longrightarrow H^{\mathrm even}(X,{\mathbb{Q}})
\equiv\bigoplus_{n\geq0}H^{2n}(X,{\mathbb{Q}})
$$
是同构，而且该映射还可延拓为环同构
$$
\mathrm{ch}:\, {\mathrm K}^\#(X)\otimes_{{\mathbb{Z}}}{\mathbb{Q}} \stackrel{\approx}{\longrightarrow}
H^\#(X,{\mathbb{Q}})
$$
它把 ${\mathrm K}^{-1}(X)\otimes_{{\mathbb{Z}}}{\mathbb{Q}}$ 映到 $H^{\mathrm odd}(X,{\mathbb{Q}})$ 上。

在 $X$ 为光滑流形的情形，Chern 特征有一个有用的显式描述。我们假定 $E$ 是配备 Hermite 联络 $\nabla_{E}$ 的光滑向量丛，其曲率为 $\nabla^2_{E}$。于是 Chern 特征 $\mathrm{ch}(E)\in H^\#(X,{\mathbb{R}})$ 可以由闭的非齐次微分形式表示：
$$
\mathrm{ch}(E)={\mathrm tr}\,\exp\left(\nabla_{E}^2/2\pi i\right)\ .
$$
在此情形，上面出现的 $\lambda_n$ 是二形式 $\nabla_E^2/2\pi i$ 的斜本征值。为得到 $X$ 的数值不变量，我们考虑一个闭 deRham 流 $\delta_Y$，它是以 delta 函数为支撑的、代表嵌入子流形 $Y\stackrel{i}{\hookrightarrow}X$ 的 Poincar\'e 对偶的上同调类的代表元。于是我们可以给 $Y$ 联系上一个映射 $I_Y:\,{\mathrm K}^\#(X)\to{\mathbb{C}}$，它由 deRham 上同调上的自然双线性配对定义：
$$
I_Y(E)=\Bigl\langle\delta_Y\,,\,\mathrm{ch}(E)\Bigr\rangle_{\mathrm DR}
\equiv\int\limits_X\delta_Y\wedge\mathrm{ch}(E)=\int\limits_Yi^*\,\mathrm{ch}(E)\ .
$$


### Thom 同构

在本小节中，我们将描述 Thom 同构，它把流形 $X$ 的 K-理论与 $X$ 上复向量丛的全空间的 K-理论联系起来。一般说来，这使我们能够用简单得多的底空间来计算某些相对复杂的空间的 K-群。例如，实射影空间的 K-群（式）可以通过底空间 $X={\mathrm pt}$ 上某个适当全空间的 K-理论来确定。用这种方式可以确定射影空间的全部 K-群（此类计算的细节见 [karoubi]）。我们将先描述上同调层面的映射，然后转向 K-理论层面的描述。Thom 同构在我们第 7.5 节关于膜反常的讨论中将起重要作用。

设 $X$ 是 $n$ 维定向流形，$H^\#(X)$ 是它的上同调环（考虑紧支集上同调环即可）。微分拓扑的一个著名结果是 Poincaré 对偶，它给出一个典范同构
$$
{\mathcal D}_X:\, H^p(X)\stackrel{\approx}{\longrightarrow} H_{n-p}(X)\ ,
$$
对所有 $p=0,1,\ldots, n$ 成立。现在考虑另一个 $m$ 维流形 $Y$，并设 $f:Y\rightarrow X$ 连续。那么对所有 $p\geq m-n$ 存在一个线性映射，称为 Gysin 同态：
$$
f_{!}:\,H^[p](Y)\longrightarrow H^{p-(m-n)}(X)\ ,
$$
它定义为使得下图
$$
{\begin{array}{ccc}
H^p(Y)&\stackrel{{\mathcal D}_Y }{\longrightarrow}&H_{m-p}(Y)\\&
&\\{\scriptstyle f_{!}}\downarrow& &\downarrow{\scriptstyle f_*}\\&
&\\H^{p-(m-n)}(X)&\stackrel{{\mathcal
D}_X^{-1}}{\longleftarrow}&H_{m-p}(X)\end{array}}
$$
交换，即满足 $f_{!}={\mathcal D}_X^{-1}\,f_*\,{\mathcal D}_Y$。这里 $f_*$ 是作用在同调上的自然前推映射。这一构造的一个重要应用实例是 $Y$ 为 $X$ 上纤维维数为 $k$ 的定向向量丛 $E$ 的情形。此时我们考虑典范投影映射 $\pi:E\rightarrow X$ 以及零截面的嵌入 $i:X\rightarrow E$。它们诱导同调上的映射，且 $\pi_*i_*={\mathrm Id}$，于是
$$
\begin{matrix}
\pi_{!}:\, H^{p+k}(E)&\stackrel{\approx}{\longrightarrow}
H^p(X)\ ,\\
i_{!}:\, H^p(X)&\stackrel{\approx}{\longrightarrow}
H^{p+k}(E)\ ,
\end{matrix}
$$
对所有 $p$ 都是同构。Gysin 映射 $\pi_{!}$ 可以看作沿 $E\to X$ 的纤维积分。容易看出 $\pi_{!}i_{!}={\mathrm Id}$，因此 $\pi_{!}=(i_{!})^{-1}$。映射（式）称为定向向量丛 $E$ 的 Thom 同构。

Thom 同构（式）的一个重要特例是 $p=0$ 的情形。这定义了一个映射 $H^0(X)\rightarrow H^k(E)$，于是 $1\in H^0(X)$ 的像由此确定了一个上同调类
$$
\Phi[E]=i_!(1)\in H^k(E)\ ,
$$
它称为 $E$ 的 Thom 类。Thom 同构（式）于是由与该类取杯积生成：
$$
i_!(\omega)=\pi^*(\omega)\wedge\Phi(E)\ .
$$
这个上同调类将在第 7.5 节起核心作用。它与（偶维）实向量丛 $E\rightarrow X$（秩 $k=2m$）的 Euler 类 $\mathrm{ch}i(E)$ 有关，后者是取值于 $H^{2m}(X)$ 的丛的示性类。它可以定义为 Thom 类沿零截面的拉回：
$$
\mathrm{ch}i(E)=i^*\,\Phi[E]\ .
$$
当 $E$ 是秩为 $k$ 的复向量丛时，$E$ 的 Euler 类定义为其底实丛 $E_r$（实秩 $2k$）的 Euler 类：$\mathrm{ch}i(E)\equiv \mathrm{ch}i(E_r)$。此外，在这种情况下可以证明 $E$ 的 Euler 类与最高 Chern 类一致：
$$
\mathrm{ch}i(E)=c_k(E)=\prod_{n=1}^k\lambda_n\ .
$$
若向量丛 $E$ 的（实）秩与 $X$ 的维数一致，则还可以引入 Euler 数 $e(E)$，它定义为 Euler 类在同调闭链 $[X]$ 上的取值：
$$
e(X)=\mathrm{ch}i(E)[X]=\int\limits_X\mathrm{ch}i(E)\ .
$$
此外，若 $X$ 紧致，则对所有 $\phi\in H^\#(X)$ 有恒等式 [lawson]
$$
i^*\,i_!(\phi)=\mathrm{ch}i(E)\wedge\phi\ ,
$$
它来自 Euler 类可表为 $\mathrm{ch}i(E)=i^*\,i_!(1)$ 这一事实。这些上同调类的另一重要性质是：若 $s:X\to E$ 是 $E$ 的任意截面，则 $s^*\Phi[E]$ 是闭形式，其上同调类与 Euler 类一致。由此还可推出 $s^*\Phi[E]=\delta_{{\mathcal Z}(s)}$，其中 ${\mathcal Z}(s)\stackrel{i}{\hookrightarrow}X$ 是截面 $s$ 的零点集，于是
$$
\int\limits_{{\mathcal
    Z}(s)}i^*\,\omega=\int\limits_Xs^*\,\Phi[E]\wedge\omega\ .
$$

现在我们来描述 K-理论中的 Thom 同构；借助 Chern 特征，它可以与上面的上同调 Thom 同构相联系。设 $E\rightarrow X$ 是 $X$ 上的复向量丛。则 ${\mathrm K}^\#(E)$ 自然地是 ${\mathrm K}^\#(X)$-模，具有结合且分配的模乘法
$$
{\mathrm K}^\#(X)\otimes_{\mathbb{Z}}{\mathrm K}^\#(E)\longrightarrow {\mathrm K}^\#(E)\ ,
$$
它按照同态序列
$$
{\mathrm K}^\#(X)\otimes_{\mathbb{Z}}{\mathrm K}^\#(E)\longrightarrow{\mathrm K}^\#(X\times E)\longrightarrow
{\mathrm K}^\#(E)\ .
$$
定义。这里第一个映射由杯积诱导，第二个映射是映射 $\pi\times {\mathrm Id}$ 在 K-理论上的拉回。一个重要例子是 $E=I^m=X\times{\mathbb{C}}^m$ 为 $X$ 上平凡复向量丛的情形。定义 $\omega\in{\mathrm K}(E)$ 为类
$$
\omega=
\Bigl[\pi^*\Lambda^{\mathrm even}E\,,\,\pi^*\Lambda^{\mathrm odd}E\,;\,\mu\Bigr]\ ,
$$
其中 $\pi^*\Lambda E$ 是 $E$ 上的平凡 $m$-平面丛，$\Lambda^{\mathrm even,odd}E$ 表示对应于 $E$ 的偶次与奇次外积丛。同构 $\mu$ 由
$$
\mu_{x,v}(\phi)=v\wedge\phi-v^\dagger\,\neg\,\phi\ ,
$$
对 $(x,v)\in X\times{\mathbb{C}}^m$ 与 $\phi\in\pi^*\Lambda^{\mathrm even}E$ 定义。利用等同 ${\mathbb{R}}^{2m}\cong{\mathbb{C}}^m$ 并选取典范定向，该元素可写为
$$
\omega=[{\mathcal S}^+,{\mathcal S}^-;\mu]\ ,
$$
其中 ${\mathcal S}={\mathcal S}^+\oplus{\mathcal S}^-$ 是不可约复分次 $C\ell_{2m}$-模（平凡地延拓到 $X$ 上），于是按（式）有 $\mu_{x,v}(\phi)=v\cdot\phi$，即与通常的 Clifford 乘法一致。基本的 Bott 周期性定理随后蕴涵：${\mathrm K}^\#(E)$ 是以 $\omega$ 为生成元的秩 1 自由 ${\mathrm K}^\#(X)$-模，因此 $\omega$ 给出丛 $E$ 的一个 K-理论定向。

现在考虑 $X$ 上一般的（可能非平凡的）复向量丛。我们说 $\omega\in {\mathrm K}(E)$ 是一个 Bott 类，如果 $\omega$ 在 $E$ 于闭子集 $C\subset X$ 上的任意局部平凡化中都确定一个 K-理论定向，即只要 $E|_C$ 平凡，${\mathrm K}^\#(E|_C)$ 就是由 $\omega$ 生成的自由 ${\mathrm K}^\#(C)$-模。可以证明 [karoubi,lawson]，任何 Bott 类都是 $E$ 的 K-理论定向。特别地，若 $E\rightarrow X$ 是紧空间 $X$ 上的复 Hermitian 向量丛，则类
$$
\Lambda_{-1}(E)=\Bigl[\pi^*\Lambda^{\mathrm even}E\,,\,
\pi^*\Lambda^{\mathrm odd}E\,;\,\mu\Bigr]\in
{\mathrm K}(E)\ ,
$$
其中 $\mu_v(\phi)=v\wedge\phi-v^\dagger\,\neg\,\phi$，定义了 $E$ 的 K-理论定向。这可由上面的例子得到，该例表明 $\Lambda_{-1}(E)$ 是 Bott 类。K-群元素（式）是向量丛 $E$ 的 K-理论 Thom 类，它是自然的且可乘的：
$$
\Lambda_{-1}(E\oplus F)=\Lambda_{-1}(E)\otimes\Lambda_{-1}(F) \ .
$$
通过与之取杯积可知，由
$$
i_{!}(\alpha)=\pi^*(\alpha)\otimes\Lambda_{-1}(E)\ \ , \ \ \alpha\in{\mathrm K}(X)\ ,
$$
定义的映射 $i_!:{\mathrm K}(X)\rightarrow {\mathrm K}(E)$ 是同构。这就是复 K-理论中的 Thom 同构。当 $X={\mathrm  pt}$ 是仅由单点构成的空间、$E={\mathbb{C}}^n$ 是 $X$ 上的平凡丛时，Thom 同构就是 Bott 周期性以
$\widetilde{{\mathrm K}}({\mathbf S}^{2n})={\mathbb{Z}}$ 形式的陈述。这来自 ${\mathrm K}(X)={\mathrm K}({\mathrm pt})={\mathbb{Z}}$ 与
${\mathrm K}(E)={\mathrm K}({\mathbb{C}}^n)=\widetilde{{\mathrm K}}({\mathbf S}^{2n})$。更一般地，取 $E=I^m=X\times{\mathbb{C}}^m$ 并用 ${\mathbb{R}}^{2m}
\cong{\mathbb{C}}^m$，Thom 同构就是 Bott 周期性以悬置同构（式）形式的陈述。更多的例子与应用，以及 KO-理论与 KR-理论中 Thom 同构的描述，见 [karoubi,lawson]。

K-理论 Thom 同构与上同调 Thom 同构之间的关系可描述如下。设 $E\to X$ 是秩为 $m$ 的复向量丛，并设 $i_!^{\mathrm K}:{\mathrm K}(X)\to{\mathrm K}(E)$ 与
$i_!^[H]:H^\#(X,{\mathbb{Q}})\to H^\#(E,{\mathbb{Q}})$ 分别是 K-理论与上同调中的 Thom 同构。我们引入自然的、可乘的 Todd 类 ${\mathrm Td}(E)\in H^{\mathrm even}(X,{\mathbb{Q}})$：
$$
\begin{matrix}
{\mathrm Td}(E)&=\prod_{n=1}^m\frac{\lambda_n}{1-\mbox{e}^{-\lambda_n}}\\
&=1+\mbox{$\frac12$}\,c_1(E)+\mbox{$\frac1{12}$}\,\Bigl(c_1(E)\wedge
c_1(E)+c_2(E)\Bigr)+\ldots \ .
\end{matrix}
$$
于是对每个类 $\omega\in{\mathrm K}(X)$，有公式：
$$
\mathrm{ch}\Bigl(i_!^{\mathrm K}(\omega)\Bigr)=i_!^[H]\Bigl(\mathrm{ch}(\omega)\wedge
{\mathrm Td}(E)\Bigr) \ .
$$

Thom 同构还使我们能够构造一个 K-理论的 Gysin 映射，它将是下一小节提出的整体束缚态构造中的关键要素。考虑余维为偶数 $2k$ 的子流形 $Y$ 在 $X$ 中的嵌入 $f:Y\hookrightarrow X$。（限制为嵌入并非必要，但为简单起见作此假设。）$Y$ 在 $X$ 中的法丛 $N(Y,X)$ 可通过向量丛的短正合列定义：
$$
0\longrightarrow TY\stackrel{f_*}{\longrightarrow} TX\longrightarrow
N(Y,X)\longrightarrow0
$$
它把 $X$ 的切丛分解为 $TX=TY\oplus N(Y,X)$。这将法丛等同于 $Y$ 在 $X$ 中的管状邻域（这意味着在 $X$ 上选取合适的度量，并把 $N(Y,X)$ 定义为 $X$ 中到 $Y$ 的距离 $<\epsilon$ 的全体点，$\epsilon$ 充分小），也等同于 $Y$ 上的丛 $f^*(TX)/TY$。向量丛 $N(Y,X)$ 的结构群为 $SO(2k)$，我们假设它可整体延拓到 $Spin(2k)$，即 $N(Y,X)$ 容许 spin 结构。（同样，这一要求可以放宽，但我们把该讨论推迟到下一小节。）给定 Thom 同构 $i_!:{\mathrm K}(Y)\to{\mathrm K}(N(Y,X))$，我们便定义 Gysin 同态为
$$
f_*=j_*\circ i_!:\, {\mathrm K}(Y)\longrightarrow{\mathrm K}(X)
$$
其中 $j_*$ 由局部紧空间的态射 $N(Y,X)\stackrel{j}{\hookrightarrow}X$ 诱导。映射 $f_*$ 不依赖于管状邻域的选取，并且只依赖于 $f$ 的同伦类。其基本性质如下。首先，若 $f:Y\to X$ 与 $g:Z\to Y$ 是两个嵌入，则 $(f\circ g)_*=f_*\circ g_*$。此外还有恒等式
$$
f_*(\omega\otimes f^*\alpha)=f_*(\omega)\otimes\alpha \ ,\ \ \
\forall\omega\in{\mathrm K}(Y),\alpha\in{\mathrm K}(X)
$$
以及，若 $X$ 紧致，
$$
f^*\circ f_*(\omega)=\mathrm{ch}i\Bigl(N(Y,X)\Bigr)\otimes\omega
$$
其中 K-理论 Euler 类定义为相应 K-理论 Thom 类在零截面上的限制。以同样的方式，可以构造 KO-理论的 Gysin 同态，但附加要求 $\dim X-\dim Y\equiv0~{\mathrm mod}\,8$ 且 $N(Y,X)$ 容许 spin 结构。


### 束缚态构造的整体版本

我们迄今所描述的束缚态构造只适用于时空 $X$ 中的局部情形。在本小节中，我们将讨论把整体拓扑纳入考虑时出现的各种特征。我们将只对 Type IIB 超弦理论详述细节，因为对其他弦理论的推广将是显然的。为此，我们必须小心处理 $X$ 中 D-膜世界体积的（非平凡）法丛的拓扑，因而必须借助上一小节所讨论的 Thom 同构与 Gysin 映射来更仔细地处理它。

事实上，映射（式）是 Thom 同构的局部版本，其中横截空间 ${\mathbf S}^{2k}$ 被等同于 $Y$ 在 $X$ 中的法丛，而 $Y\times{\mathbf B}^{2k}$ 被等同于 $Y$ 在时空中的一个小邻域。于是在整体意义上，把 Thom 同构 $f_!:{\mathrm K}(Y)\stackrel{\approx}{\to}{\mathrm K}(X)$ 应用于法丛 $N(Y,X)\stackrel{\pi}{\to}Y$ 便给出映射

$$
[E]\longmapsto f_![E]=\pi^*\Bigl([E]\Bigr)\otimes\Lambda_{-1}\Bigl(N(Y,X)\Bigr)
\ .
$$

法丛的 Thom 类的一个代表此时由上文的 ABS 构造给出。然而，要实现映射（式）需要把丛 $\pi^*E$ 延拓到整个 $X$ 上，这需要对法丛拓扑作特殊的谨慎处理，我们下面就来讨论。主要想法是：那些阻止 ABS 类 $[{\mathcal S}^+,{\mathcal S}^-;\mu]$ 生成 ${\mathrm K}(X)$ 中一个 K-理论类的整体障碍，通常可以通过成核（nucleating）额外的 9-膜与 $\overline{9}$-膜来消除。在某些情形下（下面将要描述），人们必须在 K-理论意义下稳定化原有的 9-膜与 $\overline{9}$-膜组态，即通过成对产生额外的 $9-\overline{9}$-膜组态，从而得到 K-理论类为 $[{\mathcal S}^+\oplus H,{\mathcal S}^-\oplus H;\mu\oplus{\mathrm Id}]$ 的 $9-\overline{9}$-膜对组态。这一构造随后将表明，在整体意义上，时空 $X$ 中的膜荷总可以由 9-膜与 $\overline{9}$-膜的组态来描述 [witten]，因而由 ${\mathrm K}(X)$ 分类。

让我们从余维 2 的情形开始。回忆在平坦膜世界体积的情形，为构造一个 $p$-膜，我们需要一个 $p+2$-膜-反膜对，包裹时空 $X$ 的一个子流形 ${\mathbb{R}}^{p+3}$，它给出一个 $U(1)\times U(1)$ 规范场以及一个荷为 $(1,-1)$ 的快子场 $T$。$T$ 在一个余维 2 的子空间上为零，该子空间被等同于 $p$-膜的世界体积，并把规范对称性从 $U(1)\times U(1)$ 破缺到 $U(1)$。对于整体构造，设 $Y\subset Z$ 是 $p$-膜的世界体积流形，嵌入在时空的 $p+3$ 维子流形 $Z$ 中。为构造这样的 $p$-膜，我们考虑 $Z$ 上的一个 $p+2$-膜-反膜对。设 ${\mathcal L}$ 是 $Z$ 上的复线丛，$\mu$ 是 ${\mathcal L}$ 的一个在 $Y$ 上为零的截面。通过在 $p+2$-膜上放置一个 $U(1)$ 规范场（其 $p$-膜荷与 $Y$ 上 $p$-膜的荷相同），并在 $\overline{p+2}$-膜上放置一个平凡 $U(1)$ 规范场，该系统便可被解释为包裹 $Y$ 的 $p$-膜。

然而，包裹 $Y$ 的 $p$-膜一般还带有低维的膜荷 $p-2,p-4,\dots$，它们依赖于 $Y$ 上线丛 ${\mathcal K}$ 的选取。若线丛 ${\mathcal K}$ 可延拓到 $Z$ 上，则包裹 $Y$ 的 $p$-膜由在 $p+2$ 膜上取丛 ${\mathcal L}\otimes{\mathcal K}$、在 $\overline{p+2}$ 膜上取丛 ${\mathcal K}$ 来描述。若 ${\mathcal K}$ 无法延拓，则人们使用下面这个经典的 K-理论构造 [abs]。

设 $Y'$ 是 $Y$ 在 $Z$ 中的管状邻域，其闭包记为 $\overline{Y}$，其边界为 $\partial Y$。若 $E$ 与 $F$ 是 $Y$ 上同秩的丛，则它们决定 $\widetilde{{\mathrm K}}(Y)$ 的一个元素。包含映射 $i:\,Y\hookrightarrow\overline{Y}$ 随后诱导出 K-理论上的一个映射，使得 $(E,F)$ 也定义 $\widetilde{{\mathrm K}}(\overline{Y})$ 的唯一元素。快子场是一个映射 $T:E\longrightarrow F$，除在一个闭包 $\overline{U}$ 为紧的开集 $U\subset X$ 之外，它是向量丛的同构。现在假设 $T$ 也是 $\overline{Y}$ 上的快子场，且在 $\partial{Y}$ 上是同构。在这种情况下可以构造自然的映射 $\widetilde{{\mathrm K}}(\overline{Y})\hookrightarrow\widetilde{{\mathrm K}}(Z)$，表明包裹 $Y$ 的 D-膜由 ${\mathrm K}(Z)$ 分类，正如所愿。这个映射可描述如下。设 $Z'=Z-Y'$。若能把丛 $F$ 从 $\partial Y$ 延拓到整个 $Z'$，则 $F$ 便定义在整个 $Z$ 上。由于 $E$ 与 $F$ 在 $\partial Y$ 上同构（在映射 $T$ 之下），此时 $E$ 也可延拓到 $Z'$ 上，于是 $(E,F)$ 将定义 $\widetilde{{\mathrm K}}(Z)$ 的一个元素。若 $F$ 不能延拓到 $Z$ 上，则我们可以用 Swan 定理构造 $Y$ 上的丛 $H$，使 $F\oplus H$ 平凡（假定 $Y$ 紧），因而在 $\overline{Y}$ 上也平凡。现在我们作替换 $E\rightarrow E\oplus H$、$F\rightarrow F\oplus H$ 与 $T\rightarrow T\oplus{\mathrm Id}$。于是我们可以把 $F\oplus H$ 延拓到 $Z$ 上，并通过在 $Z'$ 上令 $E\oplus H$ 等于 $F\oplus H$ 来延拓它，于是 $(E\oplus H, F\oplus H)$ 定义 $\widetilde{{\mathrm K}}(Z)$ 的一个元素。总之，若 ${\mathcal K}$ 不能延拓到 $Z$ 上，则改而寻找 $Y$ 上的丛 $H$ 使 ${\mathcal K}\oplus H$ 平凡。此时丛 ${\mathcal L}\otimes{\mathcal K}\oplus H$ 可以延拓到 $Z$ 上。若我们现在考虑 $Z$ 上规范丛为 ${\mathcal L}\otimes{\mathcal K}\oplus H$ 的一族 $p+2$-膜，以及 $Z$ 上丛为 ${\mathcal K}\oplus H$ 的一族 $\overline{p+2}$-膜，再加上一个在 $Y$ 附近等于 $T\oplus{\mathrm Id}$、在 $Y'$ 之外处于真空规范轨道中的快子场，则该系统描述 $Y$ 上规范丛为 ${\mathcal K}$ 的 $p$-膜。

在 $Y$ 于 $X$ 中余维大于 2 的情形，做法如下。设 $Y$ 在 $X$ 中余维为 $2k$。它在 $X$ 中的法丛 $N(Y,X)$ 的结构群为 $SO(2k)$。首先假设 $N(Y,X)$ 是 spin 流形，即其第二 Stiefel-Whitney 类在 $H^2(N(Y,X),{\mathbb{Z}}_2)$ 中为零，$w_2(N(Y,X))=0$。则与这 $2^[k-1]$ 个 $9-\overline{9}$-膜对相伴，我们得到一对旋量丛 ${\mathcal S}^{\pm}$，它们被等同于 9-膜上的规范丛。如通常那样，快子场是映射 $T:\, {\mathcal S}^-\rightarrow {\mathcal S}^+$，满足

$$
T(x)=\sum_{i=1}^{2k}\Gamma_i\, x^i\ \ \ \ , \ \ x\in Y'
$$

而该系统描述包裹在 $Y$ 上的 $p$-膜。若 ${\mathcal S}^-$ 可延拓，则此组态可延拓到 $X$ 上。否则可找到丛 $H$ 使 ${\mathcal S}^-\oplus H$ 可延拓，然后作替换 $({\mathcal S}^+,{\mathcal S}^-)\rightarrow({\mathcal S}^+\oplus H,{\mathcal S}^-\oplus H)$ 以及 $T\rightarrow T\oplus{\mathrm Id}$。类似地，对于带线丛 ${\mathcal K}$ 的 $p$-膜，我们从丛对 ${\mathcal K}\otimes{\mathcal S}^{\pm}$ 出发，并使用刚给出的同一构造。

现在让我们放松 $N(Y,X)$ 为 spin 流形这一要求。根据 [sharpe2] 的分析，对于宇宙学常数消失的 Type II 紧化，包裹超对称闭链的 D-膜的法丛总是容许 spin$^c$ 结构。这意味着，法丛的结构群不再能延拓为 $Y$ 上的主 $Spin(2k)$ 丛，而是延拓为 $Spin^c(2k)$，其中 $Spin^c(n)=Spin(n)\times_{{\mathbb{Z}}_2}U(1)$ 是乘积群 $Spin(n)\times U(1)$ 按等价关系 $(p,z)\sim(-p,-z)$ 取商，并且它按分裂正合列

$$
1\longrightarrow U(1)\longrightarrow Spin^c(n)\longrightarrow SO(n)
\longrightarrow1 \ .
$$

覆盖旋转群 $SO(n)$。

spin$^c$ 结构存在的判据可表述如下。考虑分裂正合列

$$
0\longrightarrow{\mathbb{Z}}\stackrel{\times2}{\longrightarrow}{\mathbb{Z}}\longrightarrow
{\mathbb{Z}}_2\longrightarrow 0\ ,
$$

其中第三个映射是模 2 约化。此序列在上同调中给出长正合列

$$
\ldots\longrightarrow H^n(X,{\mathbb{Z}})\stackrel{\times2}{\longrightarrow}
H^n(X,{\mathbb{Z}})\longrightarrow H^n(X,{\mathbb{Z}}_2)\stackrel{\beta}{\longrightarrow}
H^{n+1}(X,{\mathbb{Z}})\longrightarrow\ldots
$$

其中映射 $\beta$ 称为 Bockstein 同态。$\beta$ 的核是 $H^\#(X,{\mathbb{Z}}_2)$ 中那些作为整上同调类的模 2 约化的类。若 $w_n\in H^n(X,{\mathbb{Z}}_2)$ 表示 $X$ 的第 $n$ 个 Stiefel-Whitney 类，则 $W_n\equiv\beta(w_{n-1})$ 衡量第 $(n-1)$ 个 Stiefel-Whitney 类是否为某个整类的模 2 约化。法丛 $N(Y,X)$ 容许 spin$^c$ 结构当且仅当 $W_3(N(Y,X))=0$（从而特别地，任何 spin 流形都典范地是 spin$^c$ 流形）。由于 $X$ 是 spin 流形，$w_1(X)=w_2(X)=0$，且 $Y$ 可定向，$w_1(Y)=0$，利用全 Stiefel-Whitney 类的乘性 [witten] 容易证明 $w_2(N(Y,X))=w_2(Y)$，从而也有 $W_3(N(Y,X))=W_3(Y)$。因此 $N(Y,X)$ 容许 spin$^c$ 结构仅当 $p$-膜世界体积流形 $Y$ 容许。

$N(Y,X)$ 上 spin$^c$ 结构的存在对束缚态构造意味着以下特征。设 $U_i$ 是 $X$ 的开覆盖。${\mathcal S}^+$ 在 $U_i\cap U_j$ 上的转移函数 $g_{ij}$ 便是映射 $g_{ij}:\, U_i\cap U_j\rightarrow Spin(2k)$。spin 结构的存在等价于二上闭链

$$
\varphi_{ijk}\equiv g_{ij}g_{jk}g_{ki}:\, U_i\cap U_j\cap U_k\longrightarrow
{\mathbb{Z}}_2\ ,
$$

在 $H^2(X,{\mathbb{Z}}_2)$ 中为零。这定义了一个上同调类 $[\varphi]\in H^2(X,{\mathbb{Z}}_2)$，它恰在 $N(Y,X)$ 为 spin 流形时为零；而若 $[\varphi]$ 是 $H^2(X,{\mathbb{Z}})$ 中某个整类的模 2 约化，则 $N(Y,X)$ 容许 spin$^c$ 结构。设 ${\mathcal L}$ 是对应于这个整类的复线丛（即 $c_1({\mathcal L})$ 等于 $H^2(X,{\mathbb{Z}})$ 中的这个元素），并设 $\gamma_{ij}:\, U_i\cap U_j\rightarrow {\mathbf S}^1$ 是 ${\mathcal L}$ 的转移函数。假设我们想求 ${\mathcal L}$ 的一个平方根，即线丛 ${\mathcal L}^{1/2}$ 满足 ${\mathcal L}^{1/2}\otimes{\mathcal L}^{1/2}={\mathcal L}$。那么由于 $U_i\cap U_j$ 可缩，我们可以定义平方根 $\tilde{\gamma}_{ij}\equiv\pm\sqrt{\gamma_{ij}}:\, U_i\cap U_j\rightarrow {\mathbf S}^1$。存在相容的一组转移函数 $\tilde{\gamma}_{ij}$ 的障碍是二上闭链

$$
\varphi'_{ijk}\equiv\tilde{\gamma}_{ij}\tilde{\gamma}_{jk}
\tilde{\gamma}_{ki}:\, U_i\cap U_j\cap U_k\longrightarrow {\mathbb{Z}}_2
=\ker\sigma
$$

其中 $\sigma$ 是对应于分裂正合列

$$
0\longrightarrow{\mathbb{Z}}_2\longrightarrow{\mathbf
  S}^1\stackrel{\sigma}{\longrightarrow}
{\mathbf S}^1\longrightarrow 0 \ .
$$

的映射 $\sigma(z)\equiv z^2$。类 $[\varphi']\in H^2(X,{\mathbb{Z}}_2)$ 是 $[\tilde\gamma]\in H^1(X,{\mathbf S}^1)$ 在相应长正合列下的上边缘。事实上，考虑如下交换图：

$$
{\begin{array}{ccccc}
H^1(X,{\mathbf S}^1)&\stackrel{\sigma}{\longrightarrow}&H^1(X,{\mathbf S}^1)
&\stackrel{\varphi'}{\longrightarrow}&H^2(X,{\mathbb{Z}}_2)\\&
&\\\downarrow\approx& &\downarrow\approx& &\parallel \\&
&\\H^2(X,{\mathbb{Z}})&\stackrel{\times2}{\longrightarrow}&H^2(X,{\mathbb{Z}})
&\stackrel{\rho}{\longrightarrow}&H^2(X,{\mathbb{Z}}_2)\end{array}}
$$

由此可得 $[\varphi']=\rho(c_1({\mathcal L}))=[\varphi]$，因此 $[\varphi']+[\varphi]=0$，或等价地

$$
c_1({\mathcal L})\equiv w_2\Bigl(N(Y,X)\Bigr)~~{\mathrm mod}~2 \ .
$$

这意味着，虽然我们无法整体构造旋量丛、也无法整体构造复线丛 ${\mathcal L}^{1/2}$，我们却能构造它们的张量积。因此，spin$^c$ 结构的存在意味着 ${\mathcal L}^{1/2}\otimes{\mathcal S}^{\pm}$ 作为向量丛存在，尽管 ${\mathcal L}^{1/2}$ 与 ${\mathcal S}^{\pm}$ 本身并不存在。这又意味着，若 $N(Y,X)$ 是 spin$^c$ 丛，则我们可以完全像 spin 丛情形那样进行，由对 $({\mathcal L}^{1/2}\otimes{\mathcal S}^+, {\mathcal L}^{1/2}\otimes{\mathcal S}^-)$ 确定 ${\mathrm K}(X)$ 的一个元素，并代表包裹在 $Y$ 上的一个 D-膜。


### 紧化与 $T$-对偶

$T$-对偶变换把 Type IIA 超弦理论映射为 Type IIB 超弦理论；若该变换沿垂直于膜世界体的方向进行，则在此变换下 D$p$-膜被映射为 D$(p-1)$-膜。由于 Type IIB 膜由 ${\mathrm K}(X)$ 分类，而 Type IIA 膜由 ${\mathrm K}^{-1}(X)$ 分类，因此在 K-群层面上研究 $T$-对偶的作用是很自然的 [bgh,hori,os]。为此，我们需要理解如何用 K-理论来度量时空紧化上的 D-膜荷，以及如何实现相应 K-群之间的自然同构。

我们首先需要解释 Fredholm 算子的指标理论与拓扑 K-理论之间的密切关联，下一小节也将用到它。作用在可分 Hilbert 空间 ${\mathcal H}$ 上的{\it Fredholm 算子} ${\mathcal T}$，是指其核与余核均为 $\mathcal H$ 的有限维子空间的有界线性算子。因此这类算子具有良定义的{\it 指标}：

$$
\mathrm{ind}\,{\mathcal T}=\dim\ker{\mathcal T}-\dim{\mathrm coker}\,{\mathcal T}\ ,
$$

它在任意紧算子 ${\mathcal A}$ 的扰动下保持不变，

$$
\mathrm{ind}({\mathcal T}+{\mathcal A})=\mathrm{ind}\,{\mathcal T}\ .
$$

此外，若 ${\mathcal S}$ 是一个在算子范数下与 ${\mathcal T}$ 足够接近的有界算子，则 ${\mathcal S}$ 也是 Fredholm 算子，且 $\mathrm{ind}\,{\mathcal T}=\mathrm{ind}\,{\mathcal S}$。

这些性质的重要性源于这样一个事实：人们也可以用 Fredholm 算子来描述群 ${\mathrm K}(X)$。为此，令 ${\mathcal F}$ 为 ${\mathcal H}$ 上带有算子范数拓扑的 Fredholm 算子空间。那么（式）定义了一个连续映射

$$
\mathrm{ind}:\, {\mathcal F}\longrightarrow{\mathbb{Z}}\ ,
$$

可以证明它诱导出双射

$$
\pi_0({\mathcal F})\longrightarrow{\mathbb{Z}}
$$

即 ${\mathcal F}$ 的连通分支集合与整数之间的双射。更一般地，令 $X$ 为紧致拓扑空间，并考虑从 $X$ 到 ${\mathcal F}$ 的映射的同伦类所构成的集合 $[X,{\mathcal F}]$。由于两个 Fredholm 算子的乘积仍是 Fredholm 算子，$\left[X,{\mathcal F}\right]$ 是一个幺半群。可以证明存在同构：

$$
\left[X,{\mathcal F}\right]\stackrel{\approx}{\longrightarrow}{\mathrm K}(X)\ ,
$$

它可以如下描述。设 ${\mathcal T}_x$ 是由参数 $x\in X$ 标记的一族连续 Fredholm 算子，则向量空间族 $\ker{\mathcal T}_x$ 构成 $X$ 上的向量丛 $\ker{\mathcal T}$。这一陈述对 ${\mathcal T}$ 的余核同样成立，于是可以把算子族 ${\mathcal T}_x$ 的指标定义为类

$$
{\mathrm Index}\,{\mathcal T}\equiv\Bigl[(\ker{\mathcal T}\,,\,
{\mathrm coker}\,{\mathcal T})\Bigr]\in {\mathrm K}(X)\ .
$$

注意这与（式）中所建立的对应关系相类似。在这种对应下，${\mathcal F}$ 中算子的复合对应于 ${\mathrm K}(X)$ 中的加法，而伴随对应于求逆。特别地，当 $X$ 为一点时（从而 ${\mathrm K}(X)={\mathbb{Z}}$），同构（式）正是指标映射（式）。换言之，K-理论类（式）的虚拟维数与（式）中定义的指标一致：

$$
\mathrm{ch}_0({\mathrm Index}\,{\mathcal T})
=\mathrm{ind}\,{\mathcal T}\ .
$$

此外，Fredholm 算子的同伦类集合定义了 K-同调群 ${\mathrm K}_0(X)$。与 K-理论的对偶由如下自然双线性配对给出

$$
\Bigl([E]\,,\,[{\mathcal F}]\Bigr)\longmapsto\mathrm{ind}\,{\mathcal F}_{E}\in{\mathbb{Z}}
$$

其中 $[E]\in{\mathrm K}(X)$，而 ${\mathcal F}_E={\mathcal F}_{E,E}$ 表示 Fredholm 算子 ${\mathcal F}$ 在向量丛 $E\to X$ 的平方可积截面所构成的 Hilbert 空间 ${\mathcal H}=L^2(\Gamma(X,E))$ 上的作用，即 ${\mathcal F}:\Gamma(X,E)\to\Gamma(X,E)$。

就当前目的而言，我们将关注把这些想法应用于一类特殊的算子，即与自旋流形 $X$ 上向量丛相伴的 Dirac 算子。Dirac 算子是伪微分椭圆算子的例子，当被视为 Hilbert 空间上的算子时，它们就是 Fredholm 算子。为此，我们考虑 ${\mathcal F}=iD/\,:\Gamma(X,{\mathcal S}_E^+)\to\Gamma(X,{\mathcal S}_E^-)$ 的情形，其中 $E\to X$ 是一个（偶数秩的）实自旋丛，而 ${\mathcal S}_E^\pm$ 是由 $E$ 提升得到的相应扭曲手征旋量丛。于是 Chern 特征（式）（连同 7.2 节末尾引入的 Gysin 映射的一个版本）允许人们把用 K-理论类定义的 $iD/\,$ 的解析指标映射为可以用上同调示性类表示的拓扑指标。其结果是著名的 Atiyah-Singer 指标定理 [atiyahsing]：

$$
\mathrm{ind}\,iD/\,=-\int\limits_X\mathrm{ch}(E)\wedge\widehat{A}(TX)
$$

其中向量丛 $E$ 的 Dirac 亏格定义为

$$
\begin{matrix}
\widehat{A}(E)&=\prod_n\frac{\lambda_n/2}{\sinh(\lambda_n/2)}\\
&=1-\frac1{24}\,p_1(E)+\frac1{5760}
\,\Bigl(7p_1(E)\wedge p_1(E)-4p_2(E)\Bigr)+\dots
\end{matrix}
$$

而 $p_n(E)=(-1)^nc_{2n}(E\otimes_{\mathbb{R}}{\mathbb{C}})$ 是 $E$ 的第 $n$ 个 Pontryagin 类。该指标公式的一个重要特例，是通过取 $E=TX$ 为流形 $X$ 的切丛而得到的。此时 Euler 数（式）可以用 $X$ 的 Euler-Poincaré 示性数表示：

$$
e(X)=\dim{\mathrm K}(X)\otimes_{\mathbb{Z}}{\mathbb{Q}}-\dim{\mathrm K}^{-1}(X)\otimes_{\mathbb{Z}}{\mathbb{Q}}\ .
$$

我们可以应用这些想法，对作用在各种超弦理论 K-理论类上的 $T$-对偶给出一种指标论的解释 [hori]。这一分析的基本动机是 RR 张量场在 $T$-对偶下的变换公式 [bho]。可以证明，形如 ${\mathbf T}^n\times M$ 的时空上的 RR 场，与 $\widehat{\mathbf T}^n\times M$ 上 $T$-对偶理论的 RR 场（其中 $\widehat{\mathbf T}^n$ 是 ${\mathbf T}^n$ 的对偶环面）按照如下方式相联系（在不存在 Neveu-Schwarz $B$-场的情况下）：

$$
\widehat{H}=\int\limits_{{\mathbf T}^n}\mathrm{ch}({\mathcal P})\wedge H\ ,
$$

其中 $H=\sum_pH^{(p+2)}$ 是规范不变的总 RR 场强。这里

$$
\mathrm{ch}({\mathcal P})=\exp\left(\sum_{i=1}^nd\widehat{y}_i\wedge dy^i\right)
$$

是 $\widehat{\mathbf T}^n
\times{\mathbf T}^n$ 上 Poincaré（复线）丛 $\mathcal P$ 的 Chern 特征，其中 $y^i$ 与 $\widehat{y}_i$ 分别是 ${\mathbf T}^n$ 与 $\widehat{\mathbf T}^n$ 上的对偶坐标。Poincaré 丛定义为平凡丛 ${\mathbf T}^n\times({\mathbb{R}}^n)^*\times{\mathbb{C}}$ 按秩为 $n$ 的格 $2\pi\Lambda
^*$（其中 ${\mathbf T}^n={\mathbb{R}}^n/2\pi\Lambda$）的作用 $(x,x^*,z)\mapsto(x,x^*+m^*,\mbox{e}^{im_i^*
x^i}z)$ 所取的商。关系（式）令人想起族指标理论 [atiyahsing] 中出现的公式，即由 $\widehat{\mathbf T}^n$ 参数化的一族 ${\mathbf T}^n$ 上的 Dirac 算子（该族由 $\widehat{\mathbf T}^n
\times{\mathbf T}^n$ 上的丛 $\mathcal P$ 所承载）所对应的公式。这促使人们去寻找用 K-理论对变换性质（式）作出相对简单的解释，从而为 D-膜（它们是 RR 场的源）提供类似的变换规则。

作为示例，让我们考虑 Type IIB 超弦理论紧化在圆 ${\mathbf S}^1$ 上的 D-膜情形。此时时空为 ${\mathbf S}^1\times M$，其中 $M$ 是九维流形，而对偶几何为 $\widehat{\mathbf S}^1\times M$。如通常一样，Type IIB 的 D-膜被构造为 $9-\overline{9}$-膜的结合态，带有 Chan-Paton 丛 ${\mathcal S}^\pm$、规范联络 $A^\pm$ 以及快子场 $T:\,
{\mathcal S}^+\rightarrow{\mathcal S}^-$。我们用缠绕在 ${\mathbf S}^1$ 上的 D1-膜来探测该系统，于是对偶系统是在 $\widehat{\mathbf S}^1\times
M$ 中运动的 D0-膜。来自 $1-9$ 与 $1-\overline{9}$ 弦的费米子模的质量矩阵由 Dirac 算子给出

$$
iD/\,=\left( \begin{array}{cc}D_+& -T^\dagger\\
T&-D_-\end{array}\right)=
\left( \begin{array}{cc}\partial_y-ia&0\\ 0&-\partial_y+ia
\end{array}\right)+{\mathcal A}\ .
$$

这里 $D_\pm=\partial_y+A^\pm_y-ia$ 是 ${\mathbf S}^1$ 上与丛 ${\mathcal S}^\pm\otimes{\mathcal P}$ 上的联络 $A^\pm_y-ia$ 耦合的 Dirac 算子，其中 ${\mathcal P}$ 是 ${\mathbf S}^1\times
\widehat{\mathbf S}^1$ 上曲率为 $-ida\wedge dy$ 的 Poincaré 丛。算子（式）可以解释为 $9-\overline{9}$-膜上被超联络（式）扭曲、并与探测 D-弦耦合的通常 Dirac 算子。它也可以解释为 $T$-对偶化系统的不稳定 Type IIA 9-膜的快子场 [hori]，此时 D$p$-膜上的 Wilson 线被映射为 D$(p-1)$-膜的位置（参见式）。

由于 $iD/\,$ 是斜伴随算子，作为 ${\mathrm K}({\mathbf S}^1\times M)$ 的元素，它的指标恒为零。相反，可以证明 [atiyahsing]，通过如下构造，指标取值于该族的参数空间的高阶 K-群 ${\mathrm K}^{-1}(\widehat{\mathbf S}^1\times M)$ 之中。给定由 $x\in W=\widehat{\mathbf S}^1\times M$ 标记的斜伴随 Fredholm 算子族 $iD/\,(x)$，可以在 $[-\frac{\pi}{2},\frac{\pi}{2}]\times W$ 上定义一族算子

$$
i\widetilde{D/\,}(t,x)=-\sin t+iD/\,(x)\cos t\ .
$$

它不再是斜伴随算子，因此可以有互不相同的核与余核。此外，由于 $i\widetilde{D/\,}
(-\frac{\pi}{2},x)=-i\widetilde{D/\,}(\frac{\pi}{2},x)=1$，其核与余核在 $t=\pm\frac{\pi}{2}$ 处同构，因此
${\mathrm Index}\,i\widetilde{D/\,}\in{\mathrm K}([-\frac{\pi}{2},\frac{\pi}{2}]\times W,
\partial[-\frac{\pi}{2},\frac{\pi}{2}]\times W)={\mathrm K}^{-1}(W)$。由此推出，$T$-对偶决定了一个映射：

$$
{\mathrm K}({\mathbf S}^1\times M)\longrightarrow{\mathrm K}^{-1}(\widehat{\mathbf S}^1\times M)
$$

它可以被等同于如下同态序列：

$$
{\mathrm K}({\mathbf S}^1\times M)\stackrel{\otimes[{\mathcal P}]}{\longrightarrow}
{\mathrm K}({\mathbf S}^1\times\widehat{\mathbf S}^1\times M)
\stackrel{{\mathrm Index}\,iD/\,}{\longrightarrow}{\mathrm K}^{-1}(\widehat{\mathbf S}^1\times
M) \ ,
$$

其中最后一个映射由 $[(E,F)]\mapsto{\mathrm Index}\,iD/\,_{E,F}$ 定义。以类似的方式可以构造逆映射，因此变换（式）实际上是 K-群的同构。为了把变换（式）与（式）作比较，我们用族指标定理计算指标，得到

$$
\mathrm{ch}({\mathrm Index}\,iD/\,_{E\otimes{\mathcal P}})=\int\limits_{{\mathbf S}^1}\mathrm{ch}(E\otimes{\mathcal
P})\wedge
\widehat{A}(T{\mathbf S}^1)
$$

其中 $\widehat{A}(T{\mathbf S}^1)=1$，且 $\mathrm{ch}(E\otimes{\mathcal
P})=\mathrm{ch}(E)\wedge\mathrm{ch}({\mathcal P})$。由于 ${\mathbf S}^1$ 的 K-群是无挠的，Chern 特征（式）是同构到 $H^{\mathrm even}
({\mathbf S}^1,{\mathbb{Q}})$ 的子环 $H^{\mathrm even}({\mathbf S}^1,{\mathbb{Z}})$ 上的同构，这就建立了与公式（式）的联系。这一构造可以推广到 $n$-环面 ${\mathbf T}^n$ 上的紧化，从而定义映射
${\mathrm K}^{-m}({\mathbf T}^n\times M)\longrightarrow
{\mathrm K}^{-m-1}(\widehat{\mathbf T}^n\times M)$。类似的论证可以应用于实向量丛 [atiyahsing]，给出适用于 Type I 与 Type II orientifold 理论的 KR-群上的相应映射。

还有另一种用{\it 相对} K-理论来看待 $T$-对偶同构的方式 [bgh]。考虑一个维数为 $d$ 的一般紧化流形 $Z$。我们想要确定非紧空间 ${\mathbb{R}}^{9-d}$ 中所有余维为 $m$ 的 D-膜荷。这些荷来自缠绕 $Z$ 的非平凡闭链的 D-膜，也来自位于 $Z$ 中特定点的 D-膜。如通常一样，人们考虑有限能量的位形，因此只考虑那些在横截空间 ${\mathbb{R}}^m$ 中渐近地与真空等价的位形。于是，通过在无穷远处添加一份紧化流形 $Z$ 的拷贝，把 ${\mathbb{R}}^m$ 替换为它的单点紧化 ${\mathbf S}^m$。这恰好对应于考虑取值在相对 K-群（式）中的荷（取 $Y=Z$、$X={\mathbf S}^m\times
Z$）。因此，举例来说，对于 Type IIB 超弦理论在子流形 $Z$ 上的紧化，D-膜荷由 ${\mathrm K}({\mathbf S}^m\times Z,Z)$ 分类，而对 Type IIA 紧化则由 ${\mathrm K}^{-1}({\mathbf S}^m\times Z,Z)$ 分类。又如，考虑 Type II 在 $n$-环面 ${\mathbf T}^n$ 上的紧化。通过迭代关系（式）、（式）与（式），容易导出自然同构

$$
\begin{matrix}
{\mathrm K}(M\times{\mathbf T}^n,{\mathbf
T}^n)&=\bigoplus_{k=0}^n\widetilde{{\mathrm K}}^{-k}(M)^{\oplus\binom{n}{k}}
=~\widetilde{{\mathrm K}}(M)^{\oplus2^[n-1]}\oplus{\mathrm K}^{-1}(M)^{\oplus2^[n-1]}\\
&\cong{\mathrm K}^{-1}(M\times{\mathbf T}^n,{\mathbf T}^n)\ .
\end{matrix}
$$

从这个观点看，Type II 的 $T$-对偶是复 K-理论 2 周期性的一个推论。此外，由（式）我们看到，在 $n=1$ 时 K-群的同构（式）之下，$\widetilde{\mathrm K}(M)\otimes_{\mathbb{Z}}{\mathrm K}({\mathbf
S}^1)$ 被映射为 $\widetilde{\mathrm K}(M)\otimes_{\mathbb{Z}}{\mathrm K}^{-1}({\mathbf S}^1)$，其中求和项 ${\mathrm K}({\mathbf
S}^1)$ 与 ${\mathrm K}^{-1}({\mathbf S}^1)$ 互换。由此推出，$T$-对偶交换缠绕与未缠绕的 D-膜位形。对于 $n>1$，分解（式）给出由缠绕在环面 ${\mathbf
T}^n$ 各不同闭链上的高维超对称膜所产生的预期膜荷简并度 $2^[n-1]$。这可以归因于 $T$-对偶映射生成了目标空间对偶群 $O(n,n,{\mathbb{Z}})$ 的旋量表示，这与 $O(n,n,{\mathbb{Z}})$ 分别以正手征与负手征旋量表示作用在 IIA 与 IIB 的 RR 势上这一事实相符。与上同调理论预言的完全一致，再一次是 ${\mathbf T}^n$ 的整数 K-群与相应整数上同调环之间 Chern 同构的推论。

这一分析同样可以推广到其他弦理论。例如，我们可以写下 Type I 理论在环面上紧化的 D-膜荷与相应的 Type II orientifold 紧化的 D-膜荷之间的显式 $T$-对偶同构。利用分解（式）在 KO-理论中的类比以及（式），我们可以迭代地计算出 Type I 理论紧化所对应的群

$$
{\mathrm KO}(M\times{\mathbf T}^n,{\mathbf
T}^n)=\bigoplus_{k=0}^n\widetilde{\mathrm KO}^{-k}(M)^{\oplus\binom{n}{k}}
$$

而对于相应的 $T$-对偶 orientifold 理论，我们可以用（式）得到

$$
\begin{matrix}
{\mathrm KR}^{-n}(M\times{\mathbf T}^{1,n},{\mathbf T}^{1,n})&=
\bigoplus_{k=0}^n\widetilde{\mathrm KR}^[n,k](M)^{\oplus\binom{n}{k}}~=~\bigoplus_{k=0}^n\widetilde{\mathrm KO}^[k-n](M)^{\oplus\binom{n}{k}}\\
&\cong{\mathrm KO}(M\times{\mathbf T}^n,{\mathbf T}^n) \ .
\end{matrix}
$$

其中我们用了 KR-对合在 $M$ 上平凡地作用这一事实。相应的 BPS 与 ${\mathbb{Z}}_2$ 非 BPS D-膜的谱再次与各种缠绕膜的简并度一致。与 Type II 情形相比，分解（式）之所以复杂，源于 KO 与 KR-群的 8 周期性，如 6.4 节所讨论的那样。在这些情形中，精确记录 D-膜荷需要“D-膜转移”的概念：位于某个 orientifold 平面上的 D-膜，通过一个高一维的缠绕 D-膜而被“转移”到另一个 orientifold 平面上。这是为了补偿 K-理论谱（式）中看起来缺失的 ${\mathbb{Z}}_2$ 荷所必需的（更多细节见 [bgh]）。

$T$-对偶同构还可以给出其他 K-理论的解释。在 [sharpe] 中讨论了如何用 K-理论的全纯版本（更确切地说，凝聚层与局部自由层的 Grothendieck 群）来描述缠绕在复簇的复子流形上的 Type II D-膜，这种描述进一步编码了膜世界体上联络的选取，并且讨论了如何用 Fourier-Mukai 变换来理解 $T$-对偶的作用（另见 [hori]）。在 [os] 中，$T$-对偶被解释为 Type II 与 Type I 理论的有限维真空流形的稳定同伦群的弱 Bott 周期性序列的一个推论（参见 6.4 节）。


### D-膜反常

在本综述的最后一部分，我们将推导当 D$p$-膜包裹时空 $X$ 的子流形 $Y$ 时其荷的显式公式。局域地看，这个公式源于普通上同调理论；但正如我们将要展示的，一旦把整体拓扑考虑在内，该表达式所涉及的量最自然地要用 K-理论来理解 [minmoore]，其精神与我们此前关于 D-膜荷的讨论完全一致。基本思想来自这样一个事实：偶数维流形上的 Weyl 费米子，其作用量总会给出由著名的下降公式所描述的反常变分 [atiyahdescent]。该公式用费米子所携带的规范群表示以及相应的 Yang-Mills 联络和引力联络来确定反常。只要 D-膜包裹弯曲流形的非平凡超对称闭链，同样的现象就会出现，因为其法丛的扭曲可以在其世界叶场论中诱导出手征不对称性。这些手征反常的形式可以通过考察位于两个膜相交处的场内容来推得，其中包含手征费米子。反常项于是来自旋量丛与两个 D-膜上的 Chan-Paton 向量丛的张量积。膜相交处的反常零模来自世界叶场论的无质量激发谱，该谱由规范群 $U(N_1)\times U(N_2)$ 在相交膜世界叶上的混合扇区表示 ${\mathbf N}_1\otimes\overline{\mathbf N}_2$ 与 $\overline{\mathbf N}_1\otimes{\mathbf N}_2$ 中的 Weyl 费米子组成。因此，要使理论无反常，就需要向 D-膜作用量中加入 Wess-Zumino 项。这些诱导出的项意味着 D-膜上的拓扑缺陷（例如瞬子或磁单极子）携带着由自身拓扑量子数决定的 RR 荷 [semz,witteninst]。

设 $f:Y\hookrightarrow X$ 是把 $p+1$ 维膜世界叶 $Y$ 嵌入 IIB 型超弦理论的时空流形 $X$ 的嵌入映射。反常的 D-膜耦合取 Wess-Zumino 型作用量的形式，

$$
S_Y=\int\limits_Yf^*\,C\wedge {\mathcal Y}(\nabla_E^2,g)\ ,
$$

其中 $C=\sum_pC^{(p+1)}$ 是总 RR 形式势，${\mathcal Y}(\nabla_E^2,g)$ 是 D-膜源场，它是 $Y$ 上 Yang-Mills 场强与引力曲率的规范多项式。这里 $\nabla_E$ 是膜上 $U(N)$ 规范丛 $E$ 的 Hermitian 曲率，而 $g$ 是时空度规在 $Y$ 上的限制。D-膜上的反常来自其无质量费米子模的手征不对称性，这些模与相应的开弦 Ramond 扇区的基态一一对应。开弦量子化要求 Ramond 基态是从时空切丛 $TX$ 提升的旋量丛与一个位于膜规范群 $U(N)$ 的伴随表示 ${\mathbf N}\otimes\overline{\mathbf N}$ 中的向量丛的张量积的截面，这正是通常 Chan-Paton 因子的纳入方式所要求的。GSO 投影限制费米子具有确定的 $SO(9,1)$ 手征性。当 $Y$ 在 $X$ 中的法丛平凡、从而 $TX=TY$ 时，标准指标论计算给出

$$
{\mathcal Y}_0(\nabla_E^{2},g)=\mathrm{ch}(E)\wedge f^*\sqrt{\widehat{A}(TX)}\ .
$$

然而，在法丛非平凡的情形下，上同调类（式）需要被精细化；正如我们将要展示的，这一精细化导出的 D-膜 RR 荷公式最自然地要用 K-理论类而非上同调类来理解。假定 $N(Y,X)$ 容许一个 spin 结构，就可以确定与 $N(Y,X)$ 相关联的旋量丛的费米子量子数。当 $N(Y,X)\neq \emptyset$ 时，在世界叶 Lorentz 群 $Spin(1,p)$ 与限制到 $N(Y,X)$ 的时空 Lorentz 群 $Spin(9-p)$ 之下，费米子具有量子数 $(+,+)\oplus(-,-)$。若法丛是平坦的，则世界叶场论中的左行与右行费米子被同等对待，理论是非手征的。然而，当 $N(Y,X)$ 具有非零曲率时，膜世界叶上会诱导出手征不对称性，$(+,+)$ 与 $(-,-)$ 量子数之间就出现了区别。

众所周知，偶数维流形 $X$ 上 Dirac 算符的指标给出 $X$ 上 Dirac 旋量的微扰手征规范反常。对应于 $X$ 切丛的正、负手征旋量丛 ${\mathcal S}_{TX}^{\pm}$ 可以用从 $Y$ 在 $X$ 中的切丛与法丛提升的正、负手征旋量丛 ${\mathcal S}_{TY}^{\pm}$ 与 ${\mathcal S}_{N(Y,X)}^{\pm}$ 来分解：

$$
{\mathcal S}_{TX}^{\pm}=\left[{\mathcal S}_{TY}^{\pm}\otimes
{\mathcal S}_{N(Y,X)}^{+}
\right]\oplus\left[{\mathcal S}_{TY}^{\mp}\otimes
{\mathcal S}_{N(Y,X)}^{-}\right]
$$

带电且约化后的费米子的 Dirac 算符通过如下二项复形作用在丛（式）的截面上：

$$
iD/\,:\, \Gamma(Y,E^+)\longrightarrow \Gamma(Y,E^-)\ ,
$$

其中

$$
E^{\pm}=\left(\left[{\mathcal S}_{TY}^{\pm}\otimes
{\mathcal S}_{N(Y,X)}^{+}\right]\oplus\left[{\mathcal S}_{TY}^{\mp}\otimes
{\mathcal S}_{N(Y,X)}^{-}\right]\right)\otimes E\ .
$$

对二项复形（式）应用标准指标定理给出

$$
\begin{matrix}
\mathrm{ind}\,iD/\,&=&(-1)^{\frac{(p+1)(p+2)}{2}}\int\limits_Y\mathrm{ch}(E)\wedge
\left[\mathrm{ch}(S_{TY}^+)-\mathrm{ch}(S_{TY}^-)\right]\\
&& \wedge\left[\mathrm{ch}(S_{N(Y,X)}^+)-\mathrm{ch}(S_{N(Y,X)}^-)\right]
\wedge\frac{{\mathrm Td}(TY)}{\mathrm{ch}i(TY)}
\end{matrix}
$$

其中 $\sqrt{{\mathrm Td}(TY\otimes_{\mathbb{R}}{\mathbb{C}})}=\widehat{A}(TY)$ 且 $\mathrm{ch}(S_E^\pm)=\prod_n\mbox{e}^{\pm\lambda_n/2}$。利用恒等式

$$
\mathrm{ch}(S_{E}^+)-\mathrm{ch}(S_{E}^-)=\frac{\mathrm{ch}i(E)}{\widehat{A}(E)}
$$

它对任意可定向实 spin 丛 $E$ 成立，我们看到，由法丛拓扑导致的（式）的恰当修正是

$$
{\mathcal Y}(\nabla_E^2,g)={\mathcal Y}_0(\nabla_E^2,g)\wedge
\left[\widehat{A}\Bigl(N(Y,X)\Bigr)\right]^{-1} \ .
$$

在得到（式）时，我们利用适当的 deRham 流 $\delta_Y$ 把（式）改写为 $X$ 上的积分，并使用第 7.2 节的讨论（参见式）写出

$$
\delta_Y\wedge\mathrm{ch}i\Bigl(N(Y,X)\Bigr)
=\delta_Y\wedge\delta_Y\ .
$$

最后，如同总 Chern 类一样，Dirac 亏格是乘性示性类，因此 $\widehat{A}(TX)=\widehat{A}(TY)\wedge\widehat{A}(N(Y,X))$，而方程（式）可以写为

$$
{\mathcal Y}(\nabla^2_E,g)=\mathrm{ch}(E)\wedge\sqrt{\frac{\widehat{A}(TY)}
{\widehat{A}\Bigl(N(Y,X)\Bigr)}}\ .
$$

现在我们将用 K-理论的语言描述反常耦合如何影响膜荷。为得到 D-膜荷，我们研究由 RR 张量场的完整作用量给出的 RR 运动方程与 Bianchi 恒等式：

$$
S=-\frac{1}{4}\int\limits_{X}H(C)\wedge\,^*H(C)
-\frac{\mu_{(p)}}{2}\int\limits_X\delta_Y\wedge f^*C\wedge {\mathcal
Y}(\nabla_E^{2},g)\ ,
$$

其中 $H(C)$ 是 $C$ 的曲率。于是，对给定的 $(p+1-m)$ 形式势，运动方程与 Bianchi 恒等式为

$$
\begin{matrix}
d\,^*H(C)&=&\mu_{(p)}\,\delta_Y\wedge {\mathcal Y}(\nabla_E^{2},g)\\
dH(C)&=&-\mu_{(p)}\,\delta_Y\wedge \overline{{\mathcal Y}}(\nabla_E^{2},g)\ ,
\end{matrix}
$$

其中 $\overline{{\mathcal Y}}$ 由 ${\mathcal Y}$ 对 Chan-Paton 规范群表示取复共轭得到（注意 $c_n(\overline{E})=(-1)^nc_n(E)$，因此当 $E\cong\overline{E}$ 且 $n$ 为奇数时，Chern 类是挠上同调类）。由方程（式）可知，定义在（式）右端的电荷向量 $Q\in H^\#(X)$ 的公式为

$$
Q=f_{!}\left(\mathrm{ch}(E)\wedge\widehat{A}(TY)
\wedge\frac{1}{f^*\sqrt{\widehat{A}(TX)}}\right)\ ,
$$

其中 $f_!: H^[n](Y,{\mathbb{Z}})\rightarrow H^{n+9-p}(X,{\mathbb{Z}})$ 是按（式）所定义的作用在上同调上的（前推）Gysin 映射。从 D-膜上世界叶场论的角度看，（式）右端的示性类 ${\mathcal Y}(\nabla^2_{E},g)$ 度量的是一个引力/Yang-Mills“瞬子”的拓扑荷。由方程（式）我们看到，$\delta_Y\wedge {\mathcal Y}$ 可以看作一个“胖” D$(p-m)$-膜的膜流，该膜束缚在 D$p$-膜上并在其上延展开来。当瞬子收缩到零尺度时，${\mathcal Y}$ 获得一个 delta 函数奇性，于是量 $\delta_Y\wedge {\mathcal Y}$ 的行为就恰如一个膜流。关于法丛 $N(Y,X)$ 的扭曲修改诱导荷的一些具体例子，见 [cheung]。

为把类（式）写成更具启发性的形式，我们利用以方程（式）形式给出的上同调 Thom 同构以及恒等式

$$
f_!f^*\phi={\mathcal D}_0\wedge\phi\ ,
$$

其中 $\phi\in H^\#(X,{\mathbb{Z}})$，${\mathcal D}_0$ 是零截面的 Poincaré 对偶。于是有

$$
Q=f_!\left(\mathrm{ch}(E)\wedge\widehat{A}(TY)\right)
\wedge\frac{1}{\sqrt{\widehat{A}(TX)}}\ .
$$

现在应用 Riemann-Roch 定理的 Atiyah-Hirzebruch 版本 [karoubi]，它给出（见方程（式））

$$
f_!\left(\mathrm{ch}(E)\wedge\widehat{A}(TY)\right)=
\mathrm{ch}(f_!E)\wedge\widehat{A}(TX)\ ,
$$

其中 $f_![E]\in {\mathrm K}(X)$ 是利用 Thom 同构（式）定义的。由（式）可知，作为 $H^\#(X)$ 的元素，与包裹时空中超对称闭链 $f:Y\hookrightarrow X$、Chan-Paton 丛为 $E\rightarrow Y$ 的 D-膜相关联的 RR 荷由下式给出

$$
Q=\mathrm{ch}(f_!E)\wedge\sqrt{\widehat{A}(TX)}\ .
$$

利用 Chern 同构（式），结果（式）有一个非常自然的 K-理论解释。上同调环 ${\mathrm K}(X)\otimes_{\mathbb{Z}}{\mathbb{Q}}$ 与 $H^{\mathrm even}(X,{\mathbb{Q}})$ 上都定义有自然的内积。在 $H^{\mathrm even}(X,{\mathbb{Q}})$ 上，双线性形式由方程（式）给出，而 ${\mathrm K}(X)$ 上的配对由 Dirac 算符的指标给出（参见方程（式））：

$$
\Bigl\langle [E]\,,\,[F]\Bigr\rangle_{{\mathrm K}}=\mathrm{ind}\,iD/\,_{E\otimes F}
$$

利用 Atiyah-Singer 指标定理（式），它可以借助 deRham 内积写成

$$
\biggl\langle [E]\,,\,[F]\biggr
\rangle_{{\mathrm K}}=\left\langle\mathrm{ch}(E)\wedge\sqrt{\widehat{A}(TX)}\,,
\,\mathrm{ch}(F)\wedge\sqrt{\widehat{A}(TX)}
\,\right\rangle_{\mathrm DR}\ .
$$

这意味着修改后的 Chern 同构

$$
[E]\longmapsto\mathrm{ch}(E)\wedge\sqrt{\widehat{A}(TX)}
$$

关于 ${\mathrm K}(X)$ 与 $H^\#(X)$ 上的自然内积是一个等距。因此，结果（式）与 D-膜荷由 $f_![E]\in {\mathrm K}(X)$ 给出这一事实完全一致，并且它还给出了以 K-理论上的 Chern 特征同态表示的膜荷显式公式。把（式）在时空流形 $X$ 的适当闭链上积分，如（式）那样，就能得到 D$p$-膜的各种 $p'$-膜荷。


## 致谢

我们感谢 J. Correia、P. Di Vecchia、T. Harmark、G. Landi、A. Liccardo、R. Marotta、N. Obers、J.L. Petersen、B. Pioline 和 P. Townsend，他们就本综述所讨论的各个主题提出的问题与评论，促使我们澄清了若干方面的内容。R.J.S. 感谢 G. Semenoff 在不列颠哥伦比亚大学（University of British Columbia）给予的热情接待，本工作即在那里完成。R.J.S. 还要感谢 1999 年夏季在不列颠哥伦比亚大学举办的 PIms/APCTP/CRM 研讨会“粒子、场与弦 '99”（Particles, Fields and Strings '99）的组织者与参与者，感谢他们提供了富有启发的工作环境。R.J.S. 的工作部分由加拿大自然科学与工程研究理事会（Natural Sciences and Engineering Research Council of Canada）资助。
