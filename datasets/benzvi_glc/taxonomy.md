# benzvi_glc 卡片总表（taxonomy）

底本：David Ben-Zvi, *What is the Geometric Langlands Correspondence about?* (arXiv:2605.23167v1, 2026-05-22, 34 pp., CC BY 4.0)。

共 **42** 张概念卡；全部 `reviewed` + `source-only`，尚未做 nLab / Stacks Project 的外部逐条核验。

## 轨道分布

| 轨道 | 名称 | 数量 |
| --- | --- | ---: |
| O | 总览：主定理与证明地图 | 4 |
| A | 谱定理、Fourier 与 Mellin（Abel 玩具模型） | 8 |
| B | Bun_G、Hecke 与几何 Satake | 8 |
| C | 谱侧、Hitchin 与谱作用 | 8 |
| D | 因子化、相对 Langlands 与证明架构 | 8 |
| E | 分歧、局部/函数域与物理 | 6 |

## O · 总览：主定理与证明地图

| id | 标题 | 摘要 |
| --- | --- | --- |
| `bzg/concept/categorical-harmonic-analysis` | 范畴调和分析：从函数到层 | 把 Hilbert 空间换成导出范畴、算子换成函子、函数换成层，得到几何 Langlands 所需的“范畴调和分析”。 |
| `bzg/concept/glc-overview` | 几何 Langlands 对应：非阿贝尔的范畴 Fourier 变换 | 曲线 \(C\) 上 \(G\)-丛的自守层范畴与对偶群 \(\check G\) 的谱侧范畴之间的等价，是 Fourier 变换的非阿贝尔、范畴化版本。 |
| `bzg/concept/glc-statement` | 无分歧几何 Langlands 主定理（精确形式） | 无分歧情形下，Bun_G 上的层范畴等价于 Loc_Ǧ 上的 IndCoh_N，并保持 QCoh 作用。 |
| `bzg/concept/proof-map` | 五篇论文的证明架构 | 无分歧 GLC 的证明由五篇论文组成：构造 Langlands 函子、Kac–Moody 构造尖点层、Eisenstein 归纳、ambidexterity、重数一。 |

## A · 谱定理、Fourier 与 Mellin（Abel 玩具模型）

| id | 标题 | 摘要 |
| --- | --- | --- |
| `bzg/concept/algebraic-spectral-theorem` | 代数谱定理：自同态与 \(\operatorname{QCoh}(\mathbb C_t)\) | 有限维向量空间加上一个自同态，等价于 \(\mathbb C[t]\)-模，也就是 \(\mathbb A^1_t\) 上的拟凝聚层。 |
| `bzg/concept/betti-mellin` | Betti Mellin：\(\operatorname{Rep}(\mathbb Z)\) 与 \(\operatorname{QCoh}(\mathbb C^\times)\) | Z-表示等价于 C^×_t 上凝聚层；C^×_z 上局部系统也等价于 QCoh(C^×_t)。 |
| `bzg/concept/categorical-fourier` | 范畴化 Fourier 与 Fourier–Mukai 核 | 把积分核换成核层，积分变换就变成 Fourier–Mukai 函子；这是几何 Langlands 中“对偶”的技术原型。 |
| `bzg/concept/derham-mellin` | de Rham Mellin：\(D\)-模与 \(\operatorname{QCoh}(\mathbb C_s/\mathbb Z)\) | \(\mathbb C^\times_z\) 上的 \(D\)-模等价于 \(\mathbb C_s/\mathbb Z\) 上的拟凝聚层；微分算子 \(z\partial_z\) 对应乘以 \(s\)。 |
| `bzg/concept/fourier-transform` | Fourier 变换：平移与微分的对角化 | Fourier 变换把平移变成乘法、把微分变成乘以 \(t\)，从而同时对角化这些算子。 |
| `bzg/concept/gl1-betti-glc` | \(GL_1\) 的 Betti 几何 Langlands | GL_1 的 Betti GLC：Jac(C) 上的局部系统等价于 (C^×)^{2g} 上的凝聚层，由 Fourier–Mukai 实现。 |
| `bzg/concept/gl1-derham-glc` | \(GL_1\) 的 de Rham 几何 Langlands | GL_1 的 de Rham GLC：Jac(C) 上的 D-模等价于 Loc^{dR}_{GL_1} 上的凝聚层。 |
| `bzg/concept/spectral-theorem` | 谱定理：自伴算子与直积分 | Hilbert 空间上的自伴算子可以西等价于“乘以 \(t\)”的算子，空间分解为 \(\mathbb R\) 上的直积分。 |

## B · Bun_G、Hecke 与几何 Satake

| id | 标题 | 摘要 |
| --- | --- | --- |
| `bzg/concept/adelic-uniformization` | Adelic 双陪集与 \(\operatorname{Bun}_G\) | 在函数域情形，\(\operatorname{Bun}_G(C)\cong G(F)\backslash G(\mathbb A_F)/K\)；这是 adelic 双陪集描述。 |
| `bzg/concept/affine-grassmannian` | 仿射 Grassmannian \(\operatorname{Gr}_G=LG/LG_+\) | \(\operatorname{Gr}_G=LG/LG_+\) 是环路群的商，参数化 \(G\)-丛在一点附近的修改；它是 ind-概形。 |
| `bzg/concept/bun-g` | \(\operatorname{Bun}_G\)：\(G\)-丛的模叠 | \(\operatorname{Bun}_G(C)\) 是曲线 \(C\) 上 \(G\)-丛的模叠；它不是拟紧的，按度数有无穷多个连通分支。 |
| `bzg/concept/dual-group` | Langlands 对偶群 \(\check G\) 与根数据 | 对偶群 \(\check G\) 由 \(G\) 的根数据对偶得到：交换特征格与余权格，并交换根与余根。 |
| `bzg/concept/geometric-satake` | 几何 Satake 等价 | 几何 Satake 断言 \(\operatorname{Sph}_G\simeq \operatorname{Rep}(\check G)\) 为对称 monoidal 等价，从而由几何数据重构对偶群。 |
| `bzg/concept/hecke-operators` | Hecke 函子：在一点修改丛 | Hecke 函子在一点 \(x\) 修改 \(G\)-丛，并用 \(\check G\) 的表示给出一族作用在 \(\operatorname{Shv}(\operatorname{Bun}_G)\) 上的算子。 |
| `bzg/concept/picard-jacobian` | \(\operatorname{Pic}(C)\)、\(\operatorname{Jac}(C)\) 与度数 | Pic(C) ≅ Z × Jac(C)；Jac(C) 是 2g 维复环面，实同构于 (S^1)^{2g}。 |
| `bzg/concept/spherical-hecke-category` | 球 Hecke 范畴 \(\operatorname{Sph}_G\) | \(\operatorname{Sph}_G=\operatorname{Shv}(\operatorname{Gr}_G)^{LG_+}\) 是 \(LG_+\)-等变层范畴，带卷积 monoidal 结构。 |

## C · 谱侧、Hitchin 与谱作用

| id | 标题 | 摘要 |
| --- | --- | --- |
| `bzg/concept/abelianization` | 阿贝尔化与 Arinkin 渐近 | 阿贝尔化把 \(D\)-模送到 Higgs 侧的拟凝聚层，再送到 \(\operatorname{Loc}_{\check G}\)；它解释了 GLC 的奇异支撑。 |
| `bzg/concept/dolbeault-glc` | Dolbeault 几何 Langlands | Dolbeault GLC：Higgs_G 与 Higgs_Ǧ 上的凝聚层等价，即 Hitchin 系统的 SYZ 镜像。 |
| `bzg/concept/higgs-bundles` | Higgs 丛与 \(T^*\operatorname{Bun}_G\) | Higgs 丛是 \((E,\varphi)\)，其中 \(\varphi\in H^0(C,\operatorname{ad}E\otimes K_C)\)；它参数化 \(T^*\operatorname{Bun}_G\)。 |
| `bzg/concept/hitchin-fibration` | Hitchin 纤维化与谱曲线 | Hitchin 纤维化 \(h:\operatorname{Higgs}_G\to \mathcal A_G\) 把 Higgs 丛映到特征多项式，一般纤维是谱曲线的 Picard。 |
| `bzg/concept/indicoh-nilpotent-support` | \(\operatorname{IndCoh}_{\mathcal N}\) 与幂零奇异支撑 | \(\operatorname{IndCoh}_{\mathcal N}(\operatorname{Loc}_{\check G})\) 是允许“广义函数”的层范畴，只保留幂零方向上的奇异支撑。 |
| `bzg/concept/loc-g-betti` | Betti 特征簇 \(\operatorname{Loc}_{\check G}\) | \(\operatorname{Loc}_{\check G}(C)\) 是 \(\pi_1(C)\) 到 \(\check G\) 的表示模去共轭，等价于 \(2g\) 个矩阵满足乘积关系。 |
| `bzg/concept/loc-g-derham` | de Rham 局部系统与平坦联络 | de Rham 侧用 \(\check G\)-平坦联络代替 Betti 表示；解析上两者相同，代数上不同。 |
| `bzg/concept/spectral-action` | 谱作用定理 | QCoh(Loc_Ǧ) 作用在 Shv(Bun_G) 上，特征值由 Ǧ-局部系统给出。 |

## D · 因子化、相对 Langlands 与证明架构

| id | 标题 | 摘要 |
| --- | --- | --- |
| `bzg/concept/beilinson-bernstein` | Beilinson–Bernstein 局部化 | Beilinson–Bernstein 局部化把 Lie 代数表示变成旗簇/\(\operatorname{Bun}_G\) 上的 \(D\)-模，是 Kac–Moody 构造的执行机制。 |
| `bzg/concept/eisenstein-series` | Eisenstein 级数与抛物诱导 | Eisenstein 级数从 Levi 子群的抛物诱导构造，提供 GLC 的归纳步骤，把一般情形归约到尖点情形。 |
| `bzg/concept/factorization` | 因子化与 \(E_n\) 结构 | Hecke 范畴在曲线上的不同点之间满足因子化/交换性，用 \(E_n\)-operad 与因子化同调组织。 |
| `bzg/concept/feigin-frenkel` | Feigin–Frenkel 定理 | 临界水平 Kac–Moody 代数的中心同构于 opers 上的函数，从而把表示论参数与 Langlands 参数连接起来。 |
| `bzg/concept/kac-moody-opers` | Kac–Moody 局部化与 opers | 用临界水平 Kac–Moody 表示与 Beilinson–Bernstein 局部化构造尖点层；其对偶参数是 opers。 |
| `bzg/concept/relative-langlands` | 相对 Langlands 与 periods | 相对 Langlands 研究自守形式上的“测量”（periods），并把它们与谱侧的对应测量匹配；L-函数只是其中一例。 |
| `bzg/concept/theta-series` | \(\Theta\)-级数与局部-整体兼容 | \(\Theta\)-级数把局部数据在整体对称群上平均，是 periods 满足局部-整体兼容/因子化的具体机制。 |
| `bzg/concept/whittaker-period` | Whittaker period 与白光 | Whittaker period 是 GLC 中的“白光”：它把单位元处的 δ-函数送到谱侧的常数函数，用来归一化并证明单射性。 |

## E · 分歧、局部/函数域与物理

| id | 标题 | 摘要 |
| --- | --- | --- |
| `bzg/concept/function-field-langlands` | 函数域 Langlands 与 Weil 罗塞塔 | 函数域 Langlands 通过 Frobenius 迹把几何 Langlands 的范畴分解退化为经典自守形式分解。 |
| `bzg/concept/local-langlands` | 局部 Langlands 与 Fargues–Scholze | 局部 Langlands 把 \(G(F)\) 的表示范畴与 Langlands 参数联系起来；Fargues–Scholze 把它实现为 Fargues–Fontaine 曲线上的几何 Langlands。 |
| `bzg/concept/low-genus` | 低亏格与可积系统 | 在亏格 0/1 时 GLC 的两侧变成显式经典对象，并与 Gaudin、Calogero–Moser 等量子可积系统相连。 |
| `bzg/concept/physics-s-duality` | S-对偶、Kapustin–Witten 与 3-流形 | Kapustin–Witten 说明 GLC 来自 4d \(\mathcal N=4\) 超 Yang–Mills 的 S-对偶，经扭曲与降维得到 2d TQFT 的边界条件范畴。 |
| `bzg/concept/quantum-glc` | 量子几何 Langlands | 量子 GLC 是 GLC 的形变：用扭曲 \(D\)-模/量子群替换通常层范畴，关于 \(G\) 与 \(\check G\) 对称。 |
| `bzg/concept/ramified-glc` | 分歧几何 Langlands | 分歧 GLC 允许局部系统在标记点有极点/分歧；Bezrukavnikov 的 tame 几何 Satake 给出部分框架，但一般情形仍 open。 |
