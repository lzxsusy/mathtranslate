# Siebert《镜像对称》资料卡索引

共 75 张：概念 46　推导 14　勘误 15

| id | 标题 | track | 一句话 |
|---|---|---|---|
| [`siebert/concept/a-model`](concepts/a-model.md) | A 模型（辛侧） | A | 拓扑扭曲的辛侧理论，只依赖 $(X,\omega)$；其 Yukawa 耦合 $5+\sum N_dd^3q^d$ 是 $d$ 次有理曲线的 GW 生成函数。 |
| [`siebert/concept/b-model`](concepts/b-model.md) | B 模型（复结构侧） | A | 拓扑扭曲的复结构侧理论，只依赖 $(X,I)$；其 Yukawa 耦合由全纯三形式的周期 $\int\Omega^\nu\wedge\partial_z^3\Omega^\nu$ 给出。 |
| [`siebert/concept/griffiths-transversality`](concepts/griffiths-transversality.md) | Griffiths 横截性 | A | Gauss–Manin 联络把 Hodge 滤过恰好降一阶：$\nabla F^k\subseteq F^{k-1}\otimes\Omega^1$；由此 $W_0=W_1=W_2=0$，$W_4=2W_3'$。 |
| [`siebert/concept/hodge-diamond`](concepts/hodge-diamond.md) | Hodge 菱形 | A | 把 $h^{i,j}=\dim H^j(X,\Omega_X^i)$ 排成菱形，Serre 对偶与复共轭给出两重对称；五次超曲面的中间两行是 $1/101,101/1$。 |
| [`siebert/concept/local-mirror-symmetry`](concepts/local-mirror-symmetry.md) | 局部镜像对称 | A | 大复结构极限附近的局部模型 u₁u₂u₃u₄=z：消失环面 T³、极大单值 N=T−I，以及单值与 Kähler 侧杯积的对应。 |
| [`siebert/concept/mirror-map`](concepts/mirror-map.md) | 镜像映射 | A | 用周期比 $w=\varphi_1/\varphi_0$ 定义 $q=e^{2\pi iw}$，把镜像族的复结构模与五次超曲面的 Kähler 模接起来；$q=cz+O(z^2)$。 |
| [`siebert/concept/mirror-quintic`](concepts/mirror-quintic.md) | 镜像五次超曲面 | A | 把 Fermat 五次对 (Z/5)³ 取商再消解奇点，得 h^{1,1}=101、h^{2,1}=1 的流形；100 个例外除子来自 10 条曲线与 10 个点。 |
| [`siebert/concept/picard-fuchs-equation`](concepts/picard-fuchs-equation.md) | Picard–Fuchs 方程 | A | 镜像五次超曲面的周期所满足的四阶常微分方程 [θ⁴−5z∏(5θ+i)]φ=0，由 Griffiths 极点阶数约化算出。 |
| [`siebert/concept/quintic-threefold`](concepts/quintic-threefold.md) | 五次三维超曲面 | A | P⁴ 中的五次超曲面：h^{1,1}=1、h^{2,1}=101，形变模空间维数 101，可由 Euler 序列与余法序列直接算出。 |
| [`siebert/concept/yukawa-coupling`](concepts/yukawa-coupling.md) | Yukawa 耦合 | A | Calabi–Yau 上的三点函数：A 模型是曲线计数 5+Σd³n_d q^d/(1−q^d)，B 模型是 ∫Ω∧∂³Ω，镜像映射使两者相等。 |
| [`siebert/concept/deligne-mumford-stack`](concepts/deligne-mumford-stack.md) | Deligne–Mumford 叠 | B | 对角可表、拟紧分离、带平展图册的代数叠；稳定曲线的模叠是典型例子，其自同构群有限。 |
| [`siebert/concept/etale-local`](concepts/etale-local.md) | 平展局部与下降 | B | 「平展局部」指在平展覆盖上逐块成立；平展拓扑要求平坦且非分歧，比 Zariski 细、比平坦（fpqc）粗，是叠的定义所依赖的拓扑。 |
| [`siebert/concept/moduli-space`](concepts/moduli-space.md) | 模空间与模函子 | B | 模空间是表示模函子的概形：$T\to M$ 的映射分类 $T$ 上的族；曲线模函子 $F_g$ 因存在等平凡族而不可表，只能改用叠。 |
| [`siebert/concept/representable-morphism`](concepts/representable-morphism.md) | 可表态射 | B | 叠的态射 $f:\mathcal F\to\mathcal G$ 可表，指沿任意概形 $B\to\mathcal G$ 的纤维积仍是概形；于是概形态射的性质可沿 $f$ 搬到叠上。 |
| [`siebert/concept/stable-curve`](concepts/stable-curve.md) | 稳定曲线 | B | 稳定曲线是几何纤维连通、一维、至多结点、且每条光滑有理分支至少带 3 个特殊点的曲线；它与「自同构群有限」等价。 |
| [`siebert/concept/stack`](concepts/stack.md) | 叠 | B | 群胚值的平展层：既记住对象也记住对象间的同构；模问题里同构类集合不可表，正是靠它救回来。 |
| [`siebert/concept/expected-dimension`](concepts/expected-dimension.md) | 预期维数 | C | 虚拟基本类所在的维数阶：$\rank F_0-\rank F_1+\dim Y$，即形变空间秩减障碍空间秩；可为零甚至为负。 |
| [`siebert/concept/gromov-witten-invariant`](concepts/gromov-witten-invariant.md) | Gromov–Witten 不变量 | C | 稳定映射模叠上的虚拟积分：亏格零超曲面情形化为 M̄₀(Pⁿ⁺¹,d) 上的 Chern 类，n_d 数有理曲线。 |
| [`siebert/concept/gysin-map`](concepts/gysin-map.md) | Gysin 拉回（局部完全交的 Umkehr 映射） | C | 对局部完全交嵌入 $\iota$，先把类推到法丛、再与零截面相交，得到降低 $d$ 阶的类；形变到法锥保证它只依赖锥。 |
| [`siebert/concept/intrinsic-normal-cone`](concepts/intrinsic-normal-cone.md) | 内蕴法锥 | C | 把局部法锥按切丛的平移作用取商，得到与嵌入无关的锥叠；虚拟基本类就从这个锥经零截面的 Gysin 拉回得到。 |
| [`siebert/concept/obstruction-theory`](concepts/obstruction-theory.md) | 障碍理论与余切复形 | C | 把形变与障碍线性化为两项局部自由复形到余切复形的态射；$h^0$ 同构、$h^{-1}$ 满射，虚拟维数就是这两项的秩差。 |
| [`siebert/concept/stable-map`](concepts/stable-map.md) | 稳定映射 | C | 带标记结点曲线到靶空间的映射，只要求被收缩分支上的自同构有限；这样得到的模叠固有分离，但一般不光滑、维数也偏大。 |
| [`siebert/concept/virtual-fundamental-class`](concepts/virtual-fundamental-class.md) | 虚拟基本类 | C | 由完美障碍理论造出的类：把障碍锥用 Gysin 拉回，得到维数正确的『虚拟』基本类，用来定义 GW 不变量。 |
| [`siebert/concept/affine-toric-variety`](concepts/affine-toric-variety.md) | 仿射环面簇 | D | 有理多面尖锥给出的 $\Spec k[\sigma^{\vee}\cap M]$：正规、$d$ 维、含环面为开稠密子概形，其定义理想是二项式生成的环面理想。 |
| [`siebert/concept/divisor-class-group`](concepts/divisor-class-group.md) | 除子类群、Cartier 除子与 Picard 群 | D | 环面簇的 $\operatorname{Pic}$ 是分段线性函数模整体线性函数：$\varphi\in\mathrm{PL}(\Sigma)$ 给出 $T$ 不变 Cartier 除子 $\sum\varphi(v_i)D_i$，而 $\operatorname{Cl}$ 是 Weil 除子模有理等价。 |
| [`siebert/concept/fan`](concepts/fan.md) | 扇与环面簇的整体化 | D | 环面簇由「扇」拼出：把 $N_{\RR}$ 中彼此沿共同面相接的尖锥族按 $U_{\sigma\cap\sigma'}$ 粘合，得到概形 $X(\Sigma)$；支撑覆盖全空间时即为完备。 |
| [`siebert/concept/monoid`](concepts/monoid.md) | 幺半群与格点幺半群 | D | 带单位元的结合乘法集合；凸锥的整点是饱和幺半群，Gordan 引理保证它有限生成，故其幺半群环是有限型代数。 |
| [`siebert/concept/rational-polyhedral-cone`](concepts/rational-polyhedral-cone.md) | 有理多面锥 | D | 由 $M_{\QQ}$ 中有限个向量张成的闭凸锥；对偶锥刻画面与极射线，Gordan 引理把它换成有限生成性。 |
| [`siebert/concept/toric-variety`](concepts/toric-variety.md) | 环面簇 | D | 仿射环面簇 = Spec k[σ^∨∩M]；把锥粘成扇就得到整体环面簇，锥的面与轨道闭包一一对应。 |
| [`siebert/concept/weil-divisor-toric`](concepts/weil-divisor-toric.md) | 环面簇上的 Weil 除子 | D | 扇的每条射线给出一个 $d-1$ 维轨道闭包，即环面素除子 $D_i$；$T$ 不变 Weil 除子是这些 $D_i$ 的整系数组合，$\operatorname{div}\chi^m=\sum\langle m,v_i\rangle D_i$。 |
| [`siebert/concept/batyrev-mirror-construction`](concepts/batyrev-mirror-construction.md) | Batyrev 镜像构造 | E | 用反身多胞体造 Fano 环面簇，取 MPCP 细分得 crepant 消解，再用反典范丛的一般截面切出 Calabi–Yau 超曲面；对偶多胞体一侧给出镜像族。 |
| [`siebert/concept/broken-line`](concepts/broken-line.md) | 折线 | E | 沿壁结构逐段行进的路径：在腔室内走直线，穿壁时按壁穿越展开并重选单项式；对其求和给出广义 $\theta$ 函数。 |
| [`siebert/concept/crepant-resolution`](concepts/crepant-resolution.md) | 保典范消解 | E | 保持典范类不变的消解 $K_Y=f^*K_X$；环面情形由 MPCP 细分实现，使反身多胞体对应的奇异环面簇上 $K=0$ 的超曲面族得以建立。 |
| [`siebert/concept/reflexive-pair`](concepts/reflexive-pair.md) | 反身多胞体对 | E | 一对互为极对偶的格多胞体，两侧都把原点放在内部、侧面到原点整距离为 1；它们给出互为镜像的两个 Calabi–Yau 超曲面族。 |
| [`siebert/concept/reflexive-polytope`](concepts/reflexive-polytope.md) | 反身多胞体 | E | 内部只有原点一个格点、每个侧面到原点整距离为 1 的格多胞体；极多胞体仍是格多胞体，对应 Fano 环面簇与 Calabi–Yau 超曲面族。 |
| [`siebert/concept/theta-function`](concepts/theta-function.md) | 广义 $\theta$ 函数 | E | 对渐近方向为 $m$ 的折线求和所得的 $\mathcal X^\circ$ 上正则函数；其乘法给出内蕴镜像映射的环结构，并被用作重建族的齐次坐标。 |
| [`siebert/concept/wall-structure`](concepts/wall-structure.md) | 壁结构 | E | 在 $B$ 上指定一族带函数的余维一多面体块；沿壁穿越给出环面模型间的自同构，绕接合部复合为恒等即相容，从而决定镜像族。 |
| [`siebert/concept/cech-model`](concepts/cech-model.md) | Čech 模型（$D^b(X)$ 的 dg 增强） | F | 用有限仿射覆盖的 Čech 上链搭出 $D^b(X)$ 的 dg 范畴：态射是 Čech 与内部 Hom 的双分次全复形，故取上同调后还要靠 HPL 补高阶运算。 |
| [`siebert/concept/dg-category`](concepts/dg-category.md) | 微分分次范畴（dg 范畴） | F | 把 Hom 集换成复形、复合换成满足分次 Leibniz 法则的映射；它是 $k>2$ 时 $m_k=0$ 的 $A_\infty$ 范畴，取上同调后高阶信息全丢。 |
| [`siebert/concept/enhanced-triangulated-category`](concepts/enhanced-triangulated-category.md) | 增强三角范畴 | F | 把三角范畴的 Hom 群提升为复形、好三角提升为映射锥的数据；原书用它把 $\operatorname{Tw}^\Pi\mathcal F(X)$ 与 $D^b(Y)$ 放到同一层比较。 |
| [`siebert/concept/fukaya-category`](concepts/fukaya-category.md) | Fukaya 范畴 | F | 以 Lagrange 子流形为对象、以圆盘计数为高阶运算的 A∞ 范畴；导出化后得到三角范畴 D^bF(X)。 |
| [`siebert/concept/hochschild-cohomology`](concepts/hochschild-cohomology.md) | Hochschild 上同调 | F | 以 $C^n(A,M)=\Hom_k(A_+^{\otimes n},M)$ 为上链、$\delta$ 为上边缘的复形的上同调；两个 $A_\infty$ 结构逐阶之差正是它的上闭链。 |
| [`siebert/concept/homological-mirror-symmetry`](concepts/homological-mirror-symmetry.md) | 同调镜像对称 | F | D^bF(X)≃D^b(Y) 的 A∞ 等价：不止 Yukawa 耦合相等，而是整个导出范畴等价，故所有关联量自动匹配。 |
| [`siebert/concept/homological-perturbation-lemma`](concepts/homological-perturbation-lemma.md) | 同调扰动引理（HPL） | F | 在收缩数据 $p,i,h$ 下把复形的微分与高阶运算搬到上同调上：$m_2=p\,m\,i$，$m_k$ 由带根带状树的求和递归给出。 |
| [`siebert/concept/calabi-yau-manifold`](concepts/calabi-yau-manifold.md) | Calabi–Yau 流形 | O | 紧 Kähler 流形且典范丛全纯平凡（K_X≅O_X，等价于 c₁=0）；加上 b₁=0 与不可约，其和乐群落在 SU(n) 内。 |
| [`siebert/concept/mirror-symmetry`](concepts/mirror-symmetry.md) | 镜像对称 | O | 一对 Calabi–Yau 流形交换 A 模型与 B 模型的对应：数值形态是 Yukawa 耦合相等，同调形态是 Fukaya 范畴与导出范畴等价。 |
| [`siebert/deriv/mirror-map-periods`](derivations/mirror-map-periods.md) | 由周期与镜像映射读出 Gromov–Witten 数 $n_1,n_2,n_3$ | A | 把 $\varphi_0,\varphi_1$ 与 $W_3$ 组装成 $q$ 级数，与 $5+\sum d^3n_dq^d/(1-q^d)$ 比较，读出 $n_1,n_2,n_3$。 |
| [`siebert/deriv/picard-fuchs-derivation`](derivations/picard-fuchs-derivation.md) | 镜像五次超曲面的 Picard–Fuchs 方程的推导 | A | 由 Griffiths 极点阶数约化与 rank-4 局部系统推出镜像族的四阶 Picard–Fuchs 算子 $\theta^4-5z\prod_{j=1}^4(5\theta+j)$。 |
| [`siebert/deriv/quintic-h11-count`](derivations/quintic-h11-count.md) | 五次三维超曲面的 Hodge 数与 $h^1(\Theta_X)$ 的计算 | A | 用 Euler 序列、余法序列与弱 Lefschetz 定理算出五次三维超曲面的 $h^{1,1}=1$、$h^{2,1}=101$，并验证 $h^1(\Theta_X)=101$。 |
| [`siebert/deriv/dm-stack-from-groupoid`](derivations/dm-stack-from-groupoid.md) | 从模函数到叠：为什么模问题要取群胚值 | B | 集合值模函数 $F_g$ 因自同构导致等平凡族而不可表；把它换成群胚值的模群胚，再补上平展下降条件，就得到叠。 |
| [`siebert/deriv/stable-curve-automorphism`](derivations/stable-curve-automorphism.md) | 自同构有限为什么推出 M̄_g 是 DM 叠 | B | 稳定曲线至多结点、每条有理分支至少 3 个特殊点，故自同构群有限；用 $n$-典范嵌入造出有限型平展图册，再让稳定子有限翻译成对角非分歧，得到 DM 叠。 |
| [`siebert/deriv/behrend-fantechi`](derivations/behrend-fantechi.md) | Behrend–Fantechi 定义：由完美障碍理论造虚拟基本类 | C | 两步：完美障碍理论把内蕴法锥嵌进向量丛叠，再用零截面的 Gysin 拉回把锥推成虚拟基本类，维数即秩差。 |
| [`siebert/deriv/gw-virtual-class`](derivations/gw-virtual-class.md) | 超曲面亏格零 GW 不变量为什么需要虚拟基本类 | C | 次数 $d$ 的稳定映射模空间实际维数不小于预期、预期还能为负，所以不变量必须靠虚拟基本类而不是拓扑基本类来定义。 |
| [`siebert/deriv/polytope-to-fan`](derivations/polytope-to-fan.md) | 由多胞体经法扇构造投影环面簇与丰除子 | D | 满维整多胞体 $\Xi$ 的每个面给出一个法锥，全体取负拼成法扇 $\Sigma_\Xi$；$X(\Xi)=X(\Sigma_\Xi)$ 由齐次坐标环的 $\Proj$ 实现，$\OO(1)$ 就是对应顶点的丰除子。 |
| [`siebert/deriv/toric-p2`](derivations/toric-p2.md) | 由扇构造 $\PP^2$ 并读出环面不变除子的相交数 | D | 用三条射线给出的完备扇把三个仿射图按 $u_0=x_1/x_0$ 之类的坐标变换粘成 $\PP^2$，再由 $\operatorname{Cl}=\ZZ H$ 与次数映射读出 $H^2=1$、$D_i\cdot D_j=1$、$D_i^2=1$。 |
| [`siebert/deriv/dwork-a1`](derivations/dwork-a1.md) | Dwork 型四次族在 $t=0$ 的退化与 $24$ 个 $A_1$ 奇点 | E | 四次族 $t\sum z_i^4+\prod z_i$ 在 $t=0$ 化为 $\prod z_i=0$，即 $4$ 个 $\PP^2$ 之并；总空间沿 $6$ 条 $\PP^1$ 的每一条出现 $4$ 个 $A_1$ 奇点，共 $6\cdot4=24$ 个三维 $A_1$。 |
| [`siebert/deriv/mumford-degeneration`](derivations/mumford-degeneration.md) | Mumford 型环面退化的构造 | E | 从凸集 $\Omega$ 的有理多面体分解出发取锥得环面族 $\pi:X(\Sigma_{\mathscr P})\to\mathbb A^1$：一般纤维是乘积，中心纤维是顶点对应的环面簇之并，重数由顶点的分母给出。 |
| [`siebert/deriv/scattering-consistency`](derivations/scattering-consistency.md) | 为什么壁结构必须满足所有余维的相容性 | E | 只查余维 $0$、$1$ 只能局部粘合；绕接合部（余维 $2$）穿一圈的复合一般不为恒等，必须由散射插入新壁逐阶修正，否则沿不同路径得到不同模型、族不自洽。 |
| [`siebert/deriv/hpl-deformation`](derivations/hpl-deformation.md) | 用同调扰动引理把 Čech 模型搬到上同调上 | F | 先把 dg 范畴的态射换成收缩数据 $p,i,h$，再用带根带状树求和定义 $m_k$：$m_1=0$、$m_2=p\,m\,i$，高阶项递归地插入 $h$。 |
| [`siebert/deriv/rigidity-theorem`](derivations/rigidity-theorem.md) | Polishchuk 刚性定理的证明骨架 | F | 把 $A_L=R\oplus M$ 上的 $A_\infty$ 结构逐阶差异化成 Hochschild 上闭链，用 $HH^i_{0,ld}$ 的消失把问题压到 $HH^{d+2}_{0,d}$ 的一维，从而结构唯一到缩放。 |
| [`siebert/correction/group-zn-subgroup`](corrections/group-zn-subgroup.md) | 镜像构造中 $(\mathbb{Z}/5)^3$ 子群的层级与唯一性 | A | 「保持全纯体积形式的子群」在 $(\mathbb{Z}/5)^5$ 层面不能唯一钉住 $G$；补出 $G\subset(\mathbb{Z}/5)^4$ 与「固定一个坐标」。 |
| [`siebert/correction/monodromy-term`](corrections/monodromy-term.md) | 「单值化」应为「单值变换」（monodromy） | A | 第 1 章把 monodromy 译成「单值化」，与 uniformization 的固定译名冲突；应改为「单值变换」，正文 4 处并同步索引。 |
| [`siebert/correction/etale-vs-flat-local`](corrections/etale-vs-flat-local.md) | 「平坦局部」应为「平展局部」 | B | 初版把 étale locally 译成「平坦局部」，丢掉「非分歧」这一半，等于把平展拓扑换成平坦拓扑；本章的层条件与下降全是按平展拓扑写的。 |
| [`siebert/correction/fully-faithful`](corrections/fully-faithful.md) | 「充分忠实」应为「完全忠实」 | B | 初版把 fully faithful 译成「充分忠实」，丢掉「完全（full）」这一半；fully faithful = 忠实且完全，正是定理 2.10 里对齐自同构的那一步。 |
| [`siebert/correction/order-vs-power`](corrections/order-vs-power.md) | 「阶为 $a$」应为「满足 $\varphi^a=\mathrm{id}$」 | B | 初版把「满足 $\varphi^a=\mathrm{id}$ 的自同构」译成「阶为 $a$ 的自同构」，把「$a$ 是某个周期」加强成「$a$ 是最小正周期」，例 2.3 可用的 $a$ 因此被无谓砍掉。 |
| [`siebert/correction/local-isomorphic`](corrections/local-isomorphic.md) | 「局部可通过」应为「局部同构于」（刚化空间） | C | 原文是「局部同构于刚化空间」，译成「局部可通过……来描述」把结构断言弱化成了存在性陈述。 |
| [`siebert/correction/prop-3-12-lci`](corrections/prop-3-12-lci.md) | 命题 3.12：假设从「局部完全交」被收窄成「光滑」 | C | 讲义原文假设是局部完全交，初版译成「光滑从而为局部完全交」，把命题的适用范围改小了。 |
| [`siebert/correction/k-valued-points`](corrections/k-valued-points.md) | 「$K$ 值点的集合」漏译「（即概形论意义下的点）」 | D | 初版把「$K$ 值点的集合」直接译出，漏掉原文括注「the scheme theoretic points」；补回后才不会被读成 $X$ 的普通点集。 |
| [`siebert/correction/polytope-vertices`](corrections/polytope-vertices.md) | 式 (4.94) 不补 $=[-1,1]^3$：顶点集不等于多胞体 | D | $\conv\{(\pm1,\pm1,\pm1)\}$ 中三元组已取遍 8 种符号组合，凸包就是立方体，原式完整；补上 $=[-1,1]^3$ 是把「顶点集」偷换成「多胞体」。 |
| [`siebert/correction/very-ample-term`](corrections/very-ample-term.md) | 「非常丰」应统一为「甚丰」（very ample） | D | 全书把 ample 译「丰」、very ample 译「甚丰」；第 4 章命题 4.20 的证明里新出现「非常丰」是漏统一，改回「甚丰」。 |
| [`siebert/correction/dwork-pencil`](corrections/dwork-pencil.md) | 「Dwork 笔形」→「Dwork 族」（pencil） | E | 原文 Dwork pencil 的 pencil 指参数族（严格说是一维线性系），初译「笔形」读作笔画的形状，与术语表已立的「Dwork 族」不一致。 |
| [`siebert/correction/quadric-curve`](corrections/quadric-curve.md) | 「二次曲面退化族」→「二次曲线退化族」（conic） | E | conic 是 $\PP^2$ 中的二次曲线（一维），二次曲面是 $\PP^3$ 中的二次超曲面（二维）；式 5.42 是 $\PP^2$ 里的曲线族，初译「二次曲面」把维数抬了一维。 |
| [`siebert/correction/coboundary-term`](corrections/coboundary-term.md) | 「上边界」→「上边缘」（coboundary） | F | coboundary 的通行中文是「上边缘」，与 cocycle「上闭链」成对；初版作「上边界」，会与拓扑的 boundary 混同。 |
| [`siebert/correction/perfect-vs-compact`](corrections/perfect-vs-compact.md) | 「完美复形 ↔ 紧对象」方向写反 | F | 原文说「完美复形就是紧对象」（perfect $\Rightarrow$ compact），初版译文写成「紧对象是完美复形」，把蕴含方向颠倒；拟凝聚层导出范畴里紧性还需 qcqs 条件。 |
| [`siebert/correction/polishchuk-numbering`](corrections/polishchuk-numbering.md) | Polishchuk 命题编号 3.1 → 3.7 | F | 译文把 bar 复形计算引作 Polishchuk 的命题 3.1，原文是 Proposition 3.7；引错号会让读者按号查找时找不到对应结论。 |
