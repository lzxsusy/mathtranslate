# Raskin《上同调类域论》资料卡索引

共 27 张：概念 12　推导 5　勘误 10

| id | 标题 | track | 一句话 |
|---|---|---|---|
| [`raskin_lcft/concept/hilbert-symbol`](concepts/hilbert-symbol.md) | 希尔伯特符号 | A | K^×/(K^×)^2 上的双乘配对：若 b 是 K(√a)/K 的范数则取 1，否则取 −1。n=2 的 lcft 全部内容都装在这个符号里。 |
| [`raskin_lcft/concept/idele-class-group`](concepts/idele-class-group.md) | 伊代尔类群 | A | 整体域 F 的伊代尔群模去主伊代尔 A_F^×/F^×；它是 gcft 的主角，代替局部情形里的 K^×。 |
| [`raskin_lcft/concept/lcft-main-theorem`](concepts/lcft-main-theorem.md) | 局部类域论主定理（lcft） | A | 非阿基米德局部域上，有限阿贝尔扩张的 Galois 群同构于范数商群：Gal(L/K) ≅ K^×/NL^×；取极限即 Gal(K^ab/K) ≅ K̂^×。 |
| [`raskin_lcft/concept/norm-group`](concepts/norm-group.md) | 范数群 | A | K^× 中形如 NL^× 的开子群；局部类域论的本质断言是「范数群 ↔ 有限阿贝尔扩张」的反序一一对应。 |
| [`raskin_lcft/concept/tame-ramification`](concepts/tame-ramification.md) | 驯分歧与单位群的范数满射 | A | 驯分歧扩张里，单位群的范数映射是满射，因此范数判定完全落到剩余域上；这是第 3 讲能算清范数群的钥匙。 |
| [`raskin_lcft/concept/herbrand-quotient`](concepts/herbrand-quotient.md) | Herbrand 商 | B | 循环群上 Tate 上同调的阶之比 χ(M)=#Ĥ⁰/#Ĥ¹；它对短正合列乘性，且有限模上恒为 1，于是把无限模的问题化成有限模。 |
| [`raskin_lcft/concept/hilbert-theorem-90`](concepts/hilbert-theorem-90.md) | 希伯特定理 90（Tate 上同调版） | B | 循环扩张上 Ĥ¹(G,L^×)=0；等价形式是「范数 1 的元素都是 y/σy」。它是 lcft 里唯一无条件成立的消没。 |
| [`raskin_lcft/concept/tate-cohomology`](concepts/tate-cohomology.md) | Tate 上同调（有限群） | B | 把通常上同调在 i=0 处用范数替换，得到对一切整数 i 有定义的 Ê⁰、Ê¹；好处是 Tate 长正合列可以穿过 −1。 |
| [`raskin_lcft/concept/tate-cohomology-unbounded`](concepts/tate-cohomology-unbounded.md) | 无界复形的 Tate 上同调 | C | 对无界复形，用同伦余不变商 X_hG 与 Hom 复形 X^hG 定义整数次上（下）同调，H_1(G,Z)=G^ab 是第一个例子。 |
| [`raskin_lcft/concept/vanishing-theorem`](concepts/vanishing-theorem.md) | 消没定理 | C | 消没定理：[(L⊗_K K^unr)^×]_tG 同伦等价于 0；它是 lcft 的引擎，把范数群问题化为纯局部计算。 |
| [`raskin_lcft/concept/kummer-duality`](concepts/kummer-duality.md) | Kummer 理论与范数群的存在定理 | D | 当 μ_n ⊆ K 时，(K^×)^n 是范数群，K^×/(K^×)^n 与 n 挠群对偶；这条对偶是存在定理（18.2）的引擎。 |
| [`raskin_lcft/concept/brauer-group`](concepts/brauer-group.md) | 布劳尔群 | E | Br^coh(K)=H²(Gal(K̄/K),K̄^×) 与中心可除代数的相似类群 Br^csa(K) 同构，非阿基米德局部域上二者都同构于 Q/Z。 |
| [`raskin_lcft/deriv/herbrand-quotient-multiplicativity`](derivations/herbrand-quotient-multiplicativity.md) | Herbrand 商的乘性：从正合列乘性到 χ(L^×)=n | B | 把「正合列的指标乘性」（引理 6.4）逐层提升为 Herbrand 商的乘性（引理 7.6），再用有限模 χ=1 算出 χ(L^×)=n。 |
| [`raskin_lcft/deriv/tate-long-exact`](derivations/tate-long-exact.md) | Tate 长正合列怎么组装 | B | 从通常上同调长正合列出发，在 −1、0 两处补上范数与增广理想的项，拼成贯穿整数次的 Tate 长正合列。 |
| [`raskin_lcft/deriv/vanishing-implies-lcft`](derivations/vanishing-implies-lcft.md) | 消没定理如何推出上同调型局部类域论 | C | 把 L^× 换成 (L⊗K^unr)^×，用消没定理把它的 Tate 上同调全部打死，于是只剩 Z[2] 的贡献，得到 Ê^i(L^×)≅Ê^{i−2}(Z)。 |
| [`raskin_lcft/deriv/first-inequality-herbrand`](derivations/first-inequality-herbrand.md) | 第一不等式的证明：χ(C_E)=n | E | 用阿代尔分解把 χ(A_E^×) 算成 n 的倍数，再用 0→E_S^×→A_{E,S}^×→C_E→0 与「格的 Herbrand 商相等」得到 χ(C_E)=n。 |
| [`raskin_lcft/deriv/second-inequality-descent`](derivations/second-inequality-descent.md) | 第二不等式的证明：从 p 阶循环扩张下降到任意扩张 | E | 先对含 μ_p 的 p 阶循环扩张证，再用「加 p 次根」的下降（断言 23.10 的四角图）去掉 μ_p 假设，最后由 23.11 推到任意次数。 |
| [`raskin_lcft/correction/bimultiplicativity`](corrections/bimultiplicativity.md) | 双乘性的解释句把 ax²+bcy² 印成 ax²+by² | A | 原文解释双乘性时把两个方程印成同一个 ax²+by²=1；正确者第一式左边应为 ax²+bcy²=1，否则整句变成同义反复。 |
| [`raskin_lcft/correction/ker-n-direction`](corrections/ker-n-direction.md) | 定理 3.3 证明里 #ker N 的不等号方向反了 | A | 原文写 #ker(N) ≤ (q²−1)/(q−1)，但范数像含于 F_q^×，故应 ≥；真正给出 ≤ 的是 x^{q+1}−1 的次数，两侧夹逼才得 q+1。 |
| [`raskin_lcft/correction/cochain-group-ring`](corrections/cochain-group-ring.md) | n-上闭链所在的项印成 Z[G]⊗M | B | 说「位于 Z[G]⊗M 的微分核中的元素叫 n-上闭链」时，该复形第 n 项其实是 Z[G^n]⊗M；Z[G]⊗M 只对应 n=1。 |
| [`raskin_lcft/correction/exactness-index`](corrections/exactness-index.md) | 引理 6.4（正合列的指标乘性）指标链自相矛盾 | B | 原文指标链把 #X_{n−1} 写了两次、两端差一个因子；正确归纳是拆成前段正合列与 0→ker d→X_{n−1}→X_n→0 两条。 |
| [`raskin_lcft/correction/homotopy-index`](corrections/homotopy-index.md) | 定义 9.9 的零伦公式指标整体位移一位 | B | 原文写 d_i h_{i+1}+h_i d_{i+1}=f_{i+1}，按此式 f 的下标与两边不匹配；标准约定是 f_i=d_{i−1}h_i+h_{i+1}d_i。 |
| [`raskin_lcft/correction/corestriction`](corrections/corestriction.md) | 定理 16.3 证明里的「膨胀」应为「余限制」 | C | 定理 16.3 在非正规子群 H⊆G 上做范数，只有 res 与 cor 有定义且复合等于乘以指数；「膨胀」只对正规子群有定义。 |
| [`raskin_lcft/correction/tate-superscript`](corrections/tate-superscript.md) | M_{hG} 应为 M^{hG}（同伦不变子模） | C | 该复形是 Hom_G(P_G^can,M)，其零阶上同调是不变子模 M^G、一阶是通常 H¹；故应记上标 M^{hG} 而非下标。 |
| [`raskin_lcft/correction/brauer-snake`](corrections/brauer-snake.md) | 断言 20.13 的蛇引理交换图缺端点 0 | E | 原文交换图只画出主体方块，缺最上一行 0→0→0 与各行端点 0，读者看不出「ψ 同构」来自蛇引理；译文按原图补齐。 |
| [`raskin_lcft/correction/gcft-diagram`](corrections/gcft-diagram.md) | 定理 20.8 印作 Gal^ab(G)，G 全书未定义 | E | gcft 主定理左端印成 Gal^ab(G)，而 G 全书未定义；按上下文应为 Gal(F̄/F)^ab，右端帽子罩整个商群。 |
| [`raskin_lcft/correction/second-inequality-diagram`](corrections/second-inequality-diagram.md) | 断言 23.10 四角图的左端花括号标签易被误读 | E | 原图左端用花括号把上、下两个 Br(F/E) 括在一起并标乘以 [F(ζ_p):F]；该标签属于左列两条竖直箭头的复合，不是同层箭头间的映射。 |
