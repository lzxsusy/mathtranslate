# ch04 校订日志（rv-ch04）

负责文件：`chapters/ch04.tex`；负责页码：PDF 227–302（第 4 章）。

## 已核对范围
- p227-236 ✅（块1，段落 id：ch04-intro-001 … intro-013、ch04-4.1-intro-001/002、ch04-4.1.1-001…008、ch04-4.1.2-001…010、ch04-4.1.3-001…010、ch04-4.1.4-001…008）

## 改动记录
| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 1 | ch04-intro-002 / ch04.tex L7 | "the only known mathematical descriptions of branes in non-perturbative string theory" | 在这里所讨论的非微扰弦理论中，已有的膜的数学描述 | 非微扰弦理论中唯一已知的膜的数学描述 | 误译 | "only known"（唯一已知）的量词丢失；"here 所讨论"亦非原文 |
| 2 | ch04-intro-010 / ch04.tex L31 | "Equivalences between derived categories of sheaves are known in the mathematics literature as Fourier-Mukai transforms." | 层的导出范畴之间的相应等价，在数学文献中，以 Fourier--Mukai 变换表述 | 层的导出范畴之间的等价，在数学文献中，称为 Fourier--Mukai 变换 | 误译 | "are known as"（被称为）被译成"以…表述"，术语定义句走形 |
| 3 | ch04-intro-012 / ch04.tex L37 | "But almost nothing is known about coherent sheaves or vector bundles on varieties of dimension three or more." + "there would be no known method for saying anything non-trivial about moduli spaces of coherent sheaves with those Chern classes" | 仍缺少统一有效的一般方法；…系统地描述…仍是困难问题 | 几乎一无所知。例如，如果在五次三维超曲面上固定一组 Chern 类，那么对于具有这些 Chern 类的凝聚层的模空间，没有任何已知的方法可以说出任何非平凡的东西 | 误译 | 两处均把"几乎一无所知 / 没有已知方法"弱化为"缺少统一方法 / 仍是困难问题"，改变了原文论断强度（P1） |
| 4 | ch04-4.1.2-002 / ch04.tex L134 | Example 4.8 原文止于 "induces a group homomorphism H_i(f): H_i(X)→H_i(Y)." | …同态 $H_i(f)\colon H_i(X)\to H_i(Y)$。对于同调有限生成的空间，它取值于这里的 Mod(Z)；对一般拓扑空间，目标是全部 Abel 群的范畴。 | …同态 $H_i(f)\colon H_i(X)\to H_i(Y)$。 | 漏译 | 后一句为译者自加的说明，原文无（属"中文多出原文没有的内容"） |
| 5 | ch04-4.1.2-005 / ch04.tex L163 | "a functor F: C(Q) → Mod(C) is a finite-dimensional representation of Q (see §4.2)" | 是 $Q$ 的逐顶点有限维表示，见§4.2；在有限箭图的情形中，这就是通常的有限维表示 | 是 $Q$ 的有限维表示，见§4.2。 | 漏译 | "逐顶点"及"有限箭图情形…"为原文所无的增补 |
| 6 | ch04-4.1.4-002 / ch04.tex L304 | "or more generally the category Mod(R) of finitely generated modules over a ring" | 或者更一般地，左 Noether 环上的有限生成模范畴；对于任意环，也可以使用全部左模的范畴 | 或者更一般地，环上的有限生成模范畴。 | 误译 | 原文只说"环上"，译文擅改为"左 Noether 环"并加一句原文没有的补充 |

## 待确认 / 未改（供 Lead 判断）
- ch04-intro-004 / L13："studying spaces on which X acts linearly" 译作"研究 X 在线性空间上的作用"，含义略偏（应是"研究 X 在其上线性作用的空间"），但可读通，未改。
- ch04-intro-003 / L10："an extremely radical extension" 译作"极其深刻的扩展"，"radical"宜为"根本性/激进"，属译法选择，未改。
- ch04-4.1.3-010 / L296："a ring with many identities" 译作"具有许多个局部恒等元的环"，多出"局部"，属轻微增词，未改。

## 块2：p237–246 ✅
已核对段落 id：ch04-4.1.4-009…019、ch04-4.1.5-001…004、ch04-4.2-intro-001、ch04-4.2.1-001…004、ch04-4.2.2-001…006、ch04-4.2.3-001…007、ch04-4.2.4-001…003、ch04-4.2.5-001…005、ch04-4.2.6-001…002

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 7 | ch04-4.1.4-013 / L419 | "given a ring R ... Hence every R-module has a left resolution by projectives, and thus Mod(R) has enough projectives." | 每个对象都有射影左消解；对于这里的有限生成模范畴，当 $R$ 为左 Noether 环时，也可以取由有限生成自由模组成的消解。 | 每个对象都有射影左消解。 | 增译 | 该句原文无，且把"环"具体化为"左 Noether 环" |
| 8 | ch04-4.1.4-021 / L478（ex:4.23） | "is never of finite length" | 一般不是有限长度范畴 | 从不是有限长度范畴 | 误译 | never 被弱化为"一般不是" |
| 9 | ch04-4.2.2-006 / L631（prop:4.28） | "is isomorphic to the category of finitely generated left A(Q)-modules" | 与有限维左 $A(Q)$ 模范畴等价。如果 $Q$ 无有向循环，$A(Q)$ 有限维，此时，也就是有限生成左模的范畴。 | 与有限生成左 $A(Q)$ 模范畴同构。 | 误译 | finitely generated 误作"有限维"；isomorphic 误作"等价"；后句为译者自加 |
| 10 | ch04-4.2.4-002 / L719–723 | "Rep(Q,R) is equivalent to the category of finitely generated left modules over A(Q,R)" | 有限维的 Rep(Q,R)，与…的有限维左模范畴等价。如果这一商代数有限维，也就是其有限生成左模范畴。 | 有限维表示范畴 Rep(Q,R)，与…的有限生成左模范畴等价。 | 误译 | 同 #9；删译者增补句 |

块2 待确认（未改）：
- ch04-4.1.5-003（ex:4.24）：原文写 −⊗_A B : Mod(A)→Mod(B)，译文改为左模约定 B⊗_A −，并加"对于这里的左模约定""在交换环的情形中，也可以按通常顺序写为 −⊗_A B"，又把第二个函子加上"若 $A$ 是交换环"限制。属译者对左模约定的技术适配，未改。
- ch04-4.1.5-004（ex:4.25）：Mod(Z) 换成 Ab，并加"Ab 是全部 Abel 群的范畴，不限于有限生成群"。属说明性增补，未改。
- ch04-4.2.5-002：加"如果同一循环中，$a$ 出现多次，就将每次切开的贡献都计入"。原文无，但内容正确，未改。
- ch04-4.2.3-004（prop 4.30 证明）：加"非零表示""零表示取空滤过"；并将重编号写成 $i=0,\ldots,n$（原文 1≤i≤n，译文更正确）。未改。

## 块3：p247–256 ✅
已核对段落 id：ch04-4.2.6-003…009、ch04-4.3-intro-001、ch04-4.3.1-001…005、ch04-4.3.2-001…008、ch04-4.3.3-001…005、ch04-4.3.4-001…006、ch04-4.3.5-001…003（含 ex 4.34/4.35/4.39、prop 4.36/4.37、note 4.38、thm 4.41、ex 4.42/4.44）

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 11 | ch04-4.2.6-007 / L831（prop:4.37） | "(2) finitely generated G-equivariant C[x1,...,xn]-modules" | 底层复向量空间有限维的 $G$ 等变 $\mathbb{C}[x_1,\ldots,x_n]$ 模 | 有限生成的 $G$ 等变 $\mathbb{C}[x_1,\ldots,x_n]$ 模 | 误译 | finitely generated（有限生成）误作"底层向量空间有限维" |
| 12 | ch04-4.2.6-008 / L843–845（note:4.38） | "(3) G-equivariant coherent sheaves on affine space A^n." | …上具有零维支撑的 G 等变凝聚层。如果允许更一般的箭图表示，并相应地要求多项式模有限生成，则对应于 A^n 上的一般 G 等变凝聚层。 | …上的 $G$ 等变凝聚层。 | 增译 | 原文无"零维支撑"限制，末句整句为译者自加，且与原文不符 |
| 13 | ch04-4.2.6-006 / L823 | "in the examples above, the actions have been defined so that the standard coordinate axes will do" | 在上面的 Abel 群例子中，可以取由 $G$ 特征向量组成的基… | 在上面的例子中，可以取由 $G$ 特征向量组成的基，标准坐标轴正好满足要求。 | 病句 | 原文只说"上面的例子"，"Abel 群"是误加的限定 |
| 14 | ch04-4.3.3-005 / L1023（ex:4.42） | "If Z is a proper subvariety, then supp(I_Z) = X." | 对于不可约 $X$ 的真子簇 $Z$ | 对于 $X$ 的真子簇 $Z$ | 增译 | 原文无"不可约"假设，多出的限定收窄了命题 |
| 15 | ch04-4.3.3-005 / L1023（ex:4.42） | "ideal sheaves of points on surfaces or threefolds" | 曲面或三维流形上点的理想层 | 曲面或三维簇上点的理想层 | 术语 | threefold 指三维代数簇，非"三维流形" |

块3 待确认（未改）：
- ch04-4.3.2-006（凝聚层定义，L948–964）：译文加上"在这里的 Noether 代数簇上"并改写为"局部有有限表示"的双行公式，与原文"对足够小开集存在正合列"的表述结构不同（数学上等价），属译者重组，未动。
- ch04-4.3.2-008（L976）：原文 "(but not conversely!)" 译为"在更一般的非约化空间上，仅有纤维维数常值，还不足以反推局部自由"，属解释性增补。
- ch04-4.3.5-002（L1089–1095）：加"Chern--Weil 理论，给出整 Chern 类在实上同调中的表示"一句，原文无。
- ch04-4.3.1-004（L895）：射影簇态射的描述加了"相容的齐次局部表达式""没有公共零点的同次数齐次多项式"，为编者式补足。

## 块4：p257–266 ✅（无改动）
已核对段落 id：ch04-4.3.5-004/005、ch04-4.3.6-001…003、ch04-4.4-intro-001、ch04-4.4.1-001…011、ch04-4.4.2-001…012、ch04-4.4.3-001…008（含 ex 4.44(2)、Pic^0/Poincaré 丛、def:4.45、lem:4.46 及证明、def:4.chain-homotopy、lem:4.47、def:4.46 环局部化/Ore 条件、lem:4.48、平移函子与映射锥、ex:4.49、def:4.distinguished-triangle、def:4.triangulated-category、TR1(a)(b)）
本块逐段与原文比对，未发现漏译/误译/数学错误，未作 edit。

块4 待确认（未改）：
- ch04-4.3.5-005（L1113–1117）：加"选择基点及相应刚性化以后…""如果不指定刚性化…"，原文只说 Pic^0(X) 是 (fine) moduli space 及 P 不唯一，属译者补注（数学上成立）。
- ch04-4.4.2-009（L1282–1293）：原文 "there are elements t1,t2 ∈ S such that s1t1 = s2t2 and f1t1 = f2t2"，译文改为"$t_1,t_2\in A$，使 $s_1t_1=s_2t_2\in S$"，并加"必要时将共同右倍数再乘以 S 中的元素""在相应的饱和情形中…"；属对 Ore 局部化的更细陈述，未改。
- ch04-4.4.3-006（L1395–1397）：原文末句 "but as yet there is no clear idea what to replace it with" 译为"在本书讨论的传统框架中，仍然沿用这一公理化来组织所需结构"，语义替换。
- ch04-4.3.6-003（L1136–140）：公式中作 $g\in G$，原文为 $g\in\mathbb{C}[G]$（对生成元成立即可线性延拓，等价）。
- ch04-4.4.1-008（L1188–1195）：加"对于相容的三角剖分，可以使用共同细分，一般也可以通过共同的奇异链复形比较"，原文只有 "any two triangulations have a common resolution"。

## 块5：p267–276 ✅（无改动）
已核对段落 id：ch04-4.4.3-009/010/011、ch04-4.4.4-001…013、ch04-4.4.5-001…007、ch04-4.4.6-001…009、ch04-4.4.7-001…006、ch04-4.5-intro-001/002（含 TR2、TR3、TR4、def 4.50、lem 4.51 及证明、Ext 定义、ex 4.52、ex 4.53、谱序列、Yoneda 乘法、导出函子、def 4.54、ex 4.55、有界 t 结构、lem 4.56、def 4.57、prop 4.58、倾斜 L_S/R_S、§4.5 引言）
逐段与原文比对，未发现漏译/误译/数学错误，未作 edit。

块5 待确认（未改）：
- ch04-4.4.5-002/004/005（L1608–1652）：原文 "A = Mod(R) is the category of modules for a ring R"、"LF = −⊗^L P: D(A) → D(A)"；译文改为"交换 Noether 环""有限生成模范畴"，并把导出函子定义域/值域改为 $D^-$（4.4.5-006 的 RF 用 $D^+$）。属译者按标准教材习惯作的系统性修正（数学正确），未动。
- ch04-4.4.6-005（ex:4.55，L1693–1699）：原文 $\mathcal{F}^{\perp}=\{E:H^i(E)=0 \text{ for all } i<0\}$，译文作 $i\le0$。按本处 $\perp$ 定义（右正交）与"心=$\mathcal{F}\cap\mathcal{F}^{\perp}[1]$"，译文 $i\le0$ 才是标准 t 结构（原文疑误）。
- ch04-4.5-intro-002（L1804）：原文 "a translation functor [1], translating complexes to the right"，译文作"将复形向左平移"；与 $M[n]^i=M^{i+n}$ 及通行的"左移"称法一致。
- ch04-4.4.4-011（ex:4.53，L1552–1561）：末尾加"不指定这些识别时，应按 $A,B$ 的同构及其对 $\eta$ 的相应作用，识别这些三元组"，原文无。
- ch04-4.4.4-005/006（L1495–1514）：加"图中以下标向左计数负次数项，$P_0=(\tau_{\le0}P)^0$"等下标约定说明，并把原文的 $E^n,E^1$ 改为 $E^{-n},E^{-1}$（与左端 $E^0$ 一致）；4.4.5-007 加"在相应有界或收敛条件下"。
- ch04-4.4.6-006（L1706–1716）：原文 "The proof is a good exercise in manipulating the definitions." 未译，改为 lemma 4.56 后的习题"运用定义证明引理4.56"。

## 块6：p277–286 ✅（无改动）
已核对段落 id：ch04-4.5-intro-003…006、ch04-4.5.1-001…008、ch04-4.5.2-001…008、ch04-4.6-intro-001、ch04-4.6.1-001…007、ch04-4.6.2-001…008（prop 4.59、prop 4.60、thm 4.61 五项相容关系、thm 4.62 长正合列、note 4.63、Čech 上同调与 prop 4.64、ex 4.65 指数正合列与 c₁、thm 4.66/4.67/4.68 Serre 对偶、def 4.69 导出对应、prop 4.70 核的复合、O_Δ 双边恒等、Euler 序列、prop 4.71 Koszul 消解、thm 4.72 Beilinson、cor 4.73 生成、note 4.74 对角线消解）
逐段比对原文，未发现漏译/误译/数学错误，未作 edit。

块6 待确认（未改）：
- ch04-4.5.2-006（thm:4.68，L2072–2085）：原文 "Let X be a smooth projective variety of dimension n"，译文加"连通"。
- ch04-4.5.1-006（prop:4.64，L1967–1976）：原文只说 "$\mathcal{U}$ 是仿射开集组成的覆盖"，译文加"在这里的分离代数簇上"（分离性为定理成立的标准前提）。
- ch04-4.5-intro-004（L1832–1839）：原文 "on the unbounded derived categories" 与 "projective resolutions ... are replaced by locally free resolutions"，译文写成"在适合的导出模层范畴中"并加"使用适当的平坦消解"，又补"特别地，在各种条件下，能够得到有界范畴上的函子"。
- ch04-4.6.1-002（eq:4.8 后，L2115–2121）：原文只给 $f_*(\alpha)=p_{Y*}(p_X^*(\alpha)\cup[\Gamma_f])$ 并说明 $[\Gamma_f]$ 为基本类，译文补"在光滑紧定向情形中，通过 Poincar\'e 对偶，用上同调表示这些运算"以及"按相应的 Gysin 约定理解"。
- ch04-4.6.1-007（L2160–2164）：原文为 "$\mathcal{E}\star\mathcal{O}_{\Delta_X}\cong\mathcal{E}$ 且 $\mathcal{O}_{\Delta_X}\star\mathcal{F}\cong\mathcal{F}$"，译文两式次序对调（两种写法在相应类型下都成立，且已有"在对应的两个组合有意义时"限定）。
- ch04-4.6.2-004（prop:4.71，L2217–2235）：原文未说明微分如何给出，译文补"各个微分由与 $s$ 收缩给出"。
- ch04-4.5.1-007（L1977–1979）：原文 "usually do for sufficiently fine coverings"，译文补"且对层无高次上同调的覆盖""局部可缩空间"。
- ch04-4.5-intro-006（thm:4.61，L1859–1899）：译文在定理前加"在前述函子保持有界凝聚对象的条件下，有以下自然同构"（原文明细写在各条中）。

## 块7：p287–296 ✅
已核对段落 id：ch04-4.6.3-001…004（prop:4.75 点层基、thm:4.76 判据）、ch04-4.6.4-001…005（thm:4.77 Poincaré 丛、thm:4.78 Mukai、K3 稳定层模空间）、ch04-4.6.5-001…005（thm:4.79 Bondal–Orlov 翻缩/翻转、def:4.80 K 等价、conj:4.81、4.6.5-005）、ch04-4.6.6-001…006（thm:4.82 Orlov、thm:4.83、thm:4.84）、ch04-4.7-intro-001、ch04-4.7.1-001…005（SL(2,C) 有限子群分类、表1 五个 Kleinian 奇点方程与 Dynkin 图、thm:4.85 McKay 图）、ch04-4.7.2-001…006（Gorenstein、def:4.crepant-resolution、principle:4.86、eq:4.9–4.11、Fourier–Mukai 函子）、ch04-4.7.3-001…005（McKay 箭图表示、维数向量、ex:4.87、GIT 与稳定参数 Θ）

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 16 | ch04-4.6.4-003 / L2345 | "This is a symmetry that has no counterpart in 'classical' geometry; in particular, it is not induced by a classical symmetry or correspondence on the elliptic curve!" | 这一对称，并不来自椭圆曲线的通常几何自同构，也不能仅靠原来的子簇对应来解释。 | 这一对称，在“经典”几何中没有对应物；特别地，它并非由椭圆曲线上的经典对称或对应诱导得到。 | 漏译+误译 | 前半句"在经典几何中没有对应物"整句未译；后半 "not induced by" 被弱化为"不能仅靠……来解释" |
| 17 | ch04-4.7.3-005 / L2566 | $\Theta=\{\theta\in\operatorname{Hom}_{\mathbb{Z}}(\bigoplus_\rho\mathbb{Z}\rho,\mathbb{Q}):\sum_\rho\dim(\rho)\theta(\rho)=0\}$ | `\operatorname{Hom}_{\mathbb{Z}}!\left(` | `\operatorname{Hom}_{\mathbb{Z}}\left(` | 录入残留 | 宏后多出一个 "!"，会排出 Hom_Z!(，属排版错误 |

块7 待确认（未改）：
- ch04-4.6.3-004（thm:4.76，L2303–2319）：译文在条件中加"连通"，并在 (1) 后补"对于 $P=Q$，$i<0$ 或 $i>\dim X$ 的这些态射也为零"（原文未写，数学上成立）。
- ch04-4.6.4-005（thm:4.78，L2350–2357）：译文把条件细化为"固定数值类与极化的稳定无挠层的非空连通二维射影细模空间"，"固定数值类与极化""非空连通"原文未逐字给出，属为使定理精确而补。
- ch04-4.6.6-001（thm:4.82，L2406）：原文只说 "an exact equivalence ... commuting with Serre functors"，译文加"复线性的"。
- ch04-4.6.6-006（L2433–2440）：原文 "the group Auteq(D^b(X)) is conjectured to have a description as the fundamental group of the complement of a hyperplane arrangement"（K3 情形），译文改写成"保持所讨论稳定性分支、并在同调上作用平凡的自等价子群，猜想可以通过相应超平面配置补集的基本群来刻画"，语义被具体化。
- ch04-4.7.2-005（L2517–2523）：原文明说 "Consider the commutative diagram"，译文补"泛层将支撑在纤维积 $Y\times_X\mathbb{A}^n$ 上，因此，限制到它的支集以后，两个到 $X$ 的复合相同"，属解释性增补。
- ch04-4.7.3-002（L2538–2544）：译文加"即对应于群的正则表示的重数向量"（$\alpha=(\dim\rho)_{\rho}$ 确为正则表示的重数向量），原文无。
- ch04-4.7.3-004（ex:4.87，L2552–2560）：关系式原文作 $x_{(j+1)j}y_{j(j-1)}-y_{(j+1)j}x_{j(j-1)}$，译文按"左到右复合"写成 $y_{j(j-1)}x_{(j+1)j}-x_{j(j-1)}y_{(j+1)j}$，仍是同一对路径之差，未改。

## 块8：p297–302 ✅（第4章末）
已核对段落 id：ch04-4.7.3-006…012（def:4.theta-stability、thm:4.88 King、note:4.89、ex:4.90 G-Hilb、ex:4.91 Z/3 腔室与表2）、ch04-4.7.4-001…008（eq:4.13、thm:4.92、note:4.93、证明、note:4.94、ex:4.95 与表3、cor:4.96、note:4.97）

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 18 | ch04-4.7.3-006 / L2576 | "The subset V(I_R)^ss_θ ⊆ V(I_R) parameterizing θ-semistable representations of (Q,R) forms a dense open subset" | 半稳定表示，形成开子集 $V(I_R)^{\mathrm{ss}}_\theta$。 | 半稳定表示，形成稠密开子集 $V(I_R)^{\mathrm{ss}}_\theta$。 | 漏译 | "dense"（稠密）丢失；该集合在 V(I_R) 中稠密是 GIT 商存在的前提 |

块8 待确认（未改）：
- ch04-4.7.3-008（thm:4.88，L2589–2594）：原文 "is the fine moduli space of θ-stable representations of (Q,R) with dimension vector α" 到此为止，译文加"采用通常的整体线丛等价或相应刚性化"。
- ch04-4.7.3-010（note:4.89，L2610）：原文 "the action of H on V(I_R) arises from the D-term (which is often described ... via a moment map)"，译文作"群作用的 GIT 处理，与 D 项及其矩映射描述相联系"，由"来自"弱化为"相联系"。
- ch04-4.7.4-003（note:4.93，L2686–2691）：原文用 "because dim(Y×_X Y) is at most twice the dimension of the exceptional locus; this equals one for n = 2 and two for n = 3" 论证，译文展开为"对角分支 n 维 + 例外轨迹的乘积"；并把 "for example dim(Y×_X Y)=6 for isolated singularities A^4/G" 泛化为"某些孤立四维商奇点"。数学上成立，属改写。
- ch04-4.7.4-008（note:4.97，L2789–2793）：原文只说 "has also been established as an equivalence of derived categories for finite subgroups G ⊂ Sp(n,C)"，译文加"存在保典消解时的"。
- p301（表3，tex L2707–2779 内）：该页英文原文未收进 chunk（p300 之后直接跳到 p302，pdftotext 未出表格页），表3 的 3×3 条目未能与原文逐项核对，仅核对了表后两段计算（Φ_θ(O_E(−3)[2])、Φ_{θ'}(Ω¹_E(1)[1])）与原文一致。

## Lead 定夺（2026-11-14，块3/块7/块8 待确认归档）
1. ch04-4.3.2-006（L948–964）凝聚层定义被重组为"局部有有限表示"双行公式：**保留译文**，数学等价，记为"可接受的等价改写"。
2. ch04-4.6.4-005（thm:4.78，L2350–2357）与 ch04-4.7.3-008（thm:4.88，L2589–2594）译文自加的限定：**保留**，记为"译者补充的适用条件（比原文更严谨）"。须在报告汇总中注明：**原文本身缺这些条件**——thm 4.78 原文只说 "the fine two-dimensional projective moduli space of stable torsion-free sheaves"，未写"固定数值类与极化""非空连通"；thm 4.88 原文只说 "the fine moduli space of θ-stable representations of (Q,R) with dimension vector α"，未写整体线丛等价/刚性化。
3. ch04-4.4.5-002/004/005（L1608–1652）把 $A=\operatorname{Mod}(R)$ 改成"交换 Noether 环上的有限生成模范畴"、$D$ 改写为 $D^-/D^+$：**保留**，记为"系统性术语规范化"。
4. ch04-4.5-intro-002（L1804）"translating complexes to the right" → "向左平移"：**保留译文**，注"原文用词与通行约定相反，译文按 $M[n]^i=M^{i+n}$ 的通行叫法处理"。
5. p301 表3：由 Lead 直接渲染原书该页核对，本日志不列。

## 结论
块1–块8 全部完成（p227–302），改动 18 条已落盘并复核，待确认项均经 Lead 定夺（见上）。

