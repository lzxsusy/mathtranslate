# 卡片清单与轨道（taxonomy）

> 本文件是 `validate_cards.py --strict` 的对照表：**用反引号写出的 id 必须真的有文件**。
> Phase 3 由 Lead 汇总 `产出\汇总\cards-chNN.tsv` 后填表；卡手按此表施工。

## 轨道

| track | 名称 | 覆盖 | 配额（概念） | 配额（例子） |
|---|---|---|---|---|
| A | 基础（跨章） | 模空间、稳定性、上同调、除子、线丛、Brill–Noether | 8–10 | 2 |
| 1 | Hitchin / TQFT | Hitchin 联络、Toeplitz、形变量子化、曲线算子 | 8 | 2 |
| 2 | Koszul 上同调 | K_{p,q}、合冲、闭链、四个猜想 | 12 | 3 |
| 3 | Reider / Thaddeus | Reider 定理、Thaddeus 对、稳定性 | 7 | 2 |
| 4 | 相交上同调 | 部分消奇异、ICT、等变上同调 | 6 | 1 |
| 5 | Beilinson–Drinfeld | 仿射/整体/卷积格拉斯曼、切片、纽结同调 | 8 | 2 |
| 6 | 算术方面 | Gerbe、扭曲层、Brauer 群、周期-指标、抛物丛 | 8 | 2 |
| 7 | α-稳定凝聚系 | 凝聚系、α-斜率、存在性、边界情形 | 8 | 2 |
| 8 | M-正则性 | GV-层、M-正则、Ishida、Fourier–Mukai | 9 | 2 |
| 9 | 可约曲线 | 斜率稳定、Hilbert 紧化、极限线性系 | 6 | 1 |

合计目标：概念 60–75，例子 15–20。

## 命名

- 概念卡：`grassmann/concept/<kebab-case-英文术语>`，如 `m-regular-sheaf`、`koszul-cohomology`。
- 例子卡：`grassmann/example/<内容>`，如 `sl2-two-point-collision`。
- 同一概念只许一张卡；近义术语进 `aliases`。跨章出现的同一对象归 `A` 轨道一张卡，`sources` 列多条。

## 卡片清单

<!-- 格式：| id | 标题 | 轨道 | 中译页 | 卡手 | -->

| id | 标题 | 轨道 | 中译页 | 卡手 |
|---|---|---|---|---|
| `grassmann/concept/alpha-stable-coherent-system` | α-稳定凝聚系 | 7 | 116 | 种子（Lead） |
| `grassmann/concept/coherent-system` | 凝聚系 | 7 | 116 | 种子（Lead） |
| `grassmann/concept/jordan-holder-filtration` | Jordan–Hölder 滤过与 S-等价 | 7 | 116 | 种子（Lead） |
| `grassmann/concept/berezin-toeplitz-quantization` | Berezin–Toeplitz 形变量子化 | 1 | 7 | 甲 |
| `grassmann/concept/curve-operator` | 曲线算子 | 1 | 7 | 甲 |
| `grassmann/concept/formal-hitchin-connection` | 形式 Hitchin 联络 | 1 | 7 | 甲 |
| `grassmann/concept/formal-trivialization` | 形式平凡化 | 1 | 7 | 甲 |
| `grassmann/concept/hitchin-connection` | Hitchin 联络 | 1 | 7 | 甲 |
| `grassmann/concept/rigid-kahler-family` | 刚性 Kähler 族 | 1 | 7 | 甲 |
| `grassmann/concept/toeplitz-operator` | Toeplitz 算子 | 1 | 7 | 甲 |
| `grassmann/concept/verlinde-bundle` | Verlinde 丛 | 1 | 7 | 甲 |
| `grassmann/example/factorization-along-a-curve` | 沿曲线的因子化 | 1 | 7 | 甲 |
| `grassmann/example/holonomy-star-product` | 和乐函数星积与 Goldman 括号 | 1 | 7 | 甲 |
| `grassmann/concept/koszul-cohomology` | Koszul 上同调 | A | 跨章 | 甲 |
| `grassmann/concept/bogomolov-inequality` | Bogomolov 不等式 | 3 | 55 | 甲 |
| `grassmann/concept/bridgeland-stability-condition` | Bridgeland 稳定性条件 | 3 | 55 | 甲 |
| `grassmann/concept/central-charge-and-phase` | 中心荷与相位 | 3 | 55 | 甲 |
| `grassmann/concept/reiders-theorem` | Reider 定理 | 3 | 55 | 甲 |
| `grassmann/concept/thaddeus-pair` | Thaddeus 对 | 3 | 55 | 甲 |
| `grassmann/concept/torsion-pair-and-tilt` | 挠对与倾斜 | 3 | 55 | 甲 |
| `grassmann/concept/wall-and-wall-crossing` | 墙与穿墙 | 3 | 55 | 甲 |
| `grassmann/example/s-half-dichotomy` | 半稳定二分法（$s=1/2$） | 3 | 55 | 甲 |
| `grassmann/example/slope-comparison-semicircle` | 半圆盘内的斜率比较 | 3 | 55 | 甲 |
| `grassmann/concept/affine-grassmannian` | 仿射格拉斯曼流形 | A | 跨章 | 甲 |
| `grassmann/concept/gv-sheaf` | GV-层 | A | 跨章 | 甲 |
| `grassmann/concept/clifford-index` | Clifford 指标 | 2 | 30 | 乙 |
| `grassmann/concept/graded-minimal-resolution-and-betti-numbers` | 极小分次自由分解与分次 Betti 数 | 2 | 30 | 乙 |
| `grassmann/concept/greens-conjecture` | Green 猜想 | 2 | 30 | 乙 |
| `grassmann/concept/greens-dimension-formula` | Green 维数公式 | 2 | 30 | 乙 |
| `grassmann/concept/kernel-bundle` | 核丛 | 2 | 30 | 乙 |
| `grassmann/concept/koszul-cycle` | Koszul 闭链与退化轨迹 | 2 | 30 | 乙 |
| `grassmann/concept/koszul-duality` | Koszul 对偶 | 2 | 30 | 乙 |
| `grassmann/concept/maximal-rank-conjecture` | 极大秩猜想 | 2 | 30 | 乙 |
| `grassmann/concept/minimal-syzygy-conjecture` | 极小合冲猜想 | 2 | 30 | 乙 |
| `grassmann/concept/property-np` | 性质 (N_p) | 2 | 30 | 乙 |
| `grassmann/concept/slope-of-effective-divisor` | 有效除子的斜率 | 2 | 30 | 乙 |
| `grassmann/example/degree-6-genus-3-quadric` | (6,3,3) 上二次曲面上的曲线 | 2 | 30 | 乙 |
| `grassmann/example/enriques-babbage-petri` | Enriques–Babbage–Petri 定理即 K_{1,2}=0 | 2 | 30 | 乙 |
| `grassmann/example/max-noether-theorem` | Max Noether 定理即 K_{0,2}=0 | 2 | 30 | 乙 |
| `grassmann/concept/brill-noether-number` | Brill–Noether 数 β | 7 | 116 | 乙 |
| `grassmann/concept/dual-span` | 对偶张成 | 7 | 116 | 乙 |
| `grassmann/concept/existence-region-d0` | $d_0$ 与存在域 $U(n,d,k)$ | 7 | 116 | 乙 |
| `grassmann/concept/model-theorem` | 模型定理 | 7 | 116 | 乙 |
| `grassmann/concept/petri-curve` | Petri 曲线 | 7 | 116 | 乙 |
| `grassmann/concept/petri-map` | Petri 映射 | 7 | 116 | 乙 |
| `grassmann/example/example-genus-10-d0` | $g=10$、$(2,12,4)$ 的 $d_0$ 例子（例 7.5） | 7 | 116 | 乙 |
| `grassmann/example/example-non-stability-large-alpha` | 大 $\alpha$ 下不半稳定的例子（例 5.3） | 7 | 116 | 乙 |
| `grassmann/concept/factorization-property` | 因子分解性质 | 5 | 82 | 丙 |
| `grassmann/concept/geometric-satake-correspondence` | 几何 Satake 对应 | 5 | 82 | 丙 |
| `grassmann/concept/global-convolution-grassmannian` | 整体卷积格拉斯曼流形 | 5 | 82 | 丙 |
| `grassmann/concept/global-singular-grassmannian` | 整体奇异格拉斯曼流形 | 5 | 82 | 丙 |
| `grassmann/concept/hecke-modification` | Hecke 修正与 Hecke 型 | 5 | 82 | 丙 |
| `grassmann/concept/local-convolution-grassmannian` | 局部卷积格拉斯曼流形 | 5 | 82 | 丙 |
| `grassmann/concept/partial-grothendieck-resolution-and-nilpotent-slice` | 部分 Grothendieck 解消与幂零切片 | 5 | 82 | 丙 |
| `grassmann/example/comparison-theorem-with-slices` | 与切片解消的比较定理 | 5 | 82 | 丙 |
| `grassmann/example/sl2-two-point-collision` | SL2 两点碰撞的最小例子 | 5 | 82 | 丙 |
| `grassmann/concept/continuously-globally-generated` | 连续整体生成 | 8 | 135 | 丙 |
| `grassmann/concept/m-regular-sheaf` | $M$-正则层 | 8 | 135 | 丙 |
| `grassmann/concept/m-regularity-index` | $M$-正则性指标 $m(L)$ | 8 | 135 | 丙 |
| `grassmann/concept/m-theta-regular` | $m$-$\Theta$-正则性 | 8 | 135 | 丙 |
| `grassmann/concept/nefness-of-gv-sheaves` | GV-层的 nef 性 | 8 | 135 | 丙 |
| `grassmann/concept/picard-bundle` | Picard 丛 | 8 | 135 | 丙 |
| `grassmann/concept/semihomogeneous-bundle` | 半齐次向量丛 | 8 | 135 | 丙 |
| `grassmann/concept/torsion-freeness-criterion` | $M$-正则性的无挠判别 | 8 | 135 | 丙 |
| `grassmann/example/elliptic-curve-regularity` | 椭圆曲线上的指标计算 | 8 | 135 | 丙 |
| `grassmann/example/verlinde-bundle-regularity` | Verlinde 丛的正则性阈值 | 8 | 135 | 丙 |
| `grassmann/concept/balanced-action` | 平衡作用 | 4 | 72 | 丁 |
| `grassmann/concept/extended-moduli-space` | 扩张模空间 | 4 | 72 | 丁 |
| `grassmann/concept/intersection-pairing-via-vm` | 用 V_M 表示的相交配对 | 4 | 72 | 丁 |
| `grassmann/concept/kirwan-map-and-class-d` | Kirwan 映射与正根类 | 4 | 72 | 丁 |
| `grassmann/concept/partial-desingularization` | 部分消奇异 | 4 | 72 | 丁 |
| `grassmann/concept/residue-formula-for-pairings` | 配对的留数公式 | 4 | 72 | 丁 |
| `grassmann/example/wall-crossing-term-m20` | M(2,0) 的穿墙项 | 4 | 72 | 丁 |
| `grassmann/concept/faddeev-index` | Faddeev 指标 | 6 | 94 | 丁 |
| `grassmann/concept/gerbe-banded-by-mu-n` | $\mu_n$-带化的 gerbe | 6 | 94 | 丁 |
| `grassmann/concept/isotrivial-family` | 等平凡族 / 簇的形式 | 6 | 94 | 丁 |
| `grassmann/concept/parabolic-bundle` | 抛物丛与抛物次数 | 6 | 94 | 丁 |
| `grassmann/concept/period-and-index` | 周期与指标 | 6 | 94 | 丁 |
| `grassmann/concept/ramification-sequence` | 分歧正合列 | 6 | 94 | 丁 |
| `grassmann/concept/root-stack` | 根叠 | 6 | 94 | 丁 |
| `grassmann/concept/twisted-sheaf` | 扭曲层 | 6 | 94 | 丁 |
| `grassmann/example/bicyclic-algebra-faddeev-4` | Faddeev 指标 4 的双四元数例子 | 6 | 94 | 丁 |
| `grassmann/example/isotrivial-torelli` | 等平凡 Torelli 定理 | 6 | 94 | 丁 |
| `grassmann/concept/brill-noether-locus-on-reducible-curves` | 可约曲线上的 Brill–Noether 簇 | 9 | 160 | 丁 |
| `grassmann/concept/hilbert-compactification` | Hilbert 紧化与 Hilbert 稳定性 | 9 | 160 | 丁 |
| `grassmann/concept/limit-linear-series-higher-rank` | 高秩极限线性系 | 9 | 160 | 丁 |
| `grassmann/concept/maximal-subbundle-and-langes-conjecture` | 极大子丛与 Lange 猜想 | 9 | 160 | 丁 |
| `grassmann/concept/reducible-nodal-curve-and-dual-graph` | 可约结点曲线与对偶图 | 9 | 160 | 丁 |
| `grassmann/concept/slope-stable-torsion-free-sheaf` | 斜率稳定无挠层与深度 1 | 9 | 160 | 丁 |
| `grassmann/example/limit-linear-series-on-a-chain-of-five-elliptic-curves` | 五条椭圆曲线链上的极限线性系算例 | 9 | 160 | 丁 |

合计：概念 73 张（含 3 张种子）、例子 17 张。

## 去重记录

| 被并/被丢弃 | 处理 | 理由 |
|---|---|---|
| grassmann/concept/alpha-stability（ch7 候选） | 不单独建卡 | 与种子卡 grassmann/concept/alpha-stable-coherent-system 同一对象，其 aliases 已收 alpha-stability |
| `grassmann/concept/coherent-system`（ch7 候选） | 不建卡 | 已有种子卡 |
| ch1 `Verlinde bundle`（概念）/ ch8 `Verlinde bundles`（例子） | 分别保留 | 一为构造、一为正则性阈值计算，内容不重复 |
