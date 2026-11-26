# Raskin《上同调类域论》资料卡 · 覆盖矩阵

讲义 23 讲、印刷页 1–115。下面这张矩阵回答的是「**每一讲要出什么类型的卡、覆盖哪些主题、最后落成了哪几张**」，最后一列回填已定稿的卡片 id。

记号：`✓` = 已出这类卡；`—` = 不单独出卡（内容并进相邻卡）。页码为底本印刷页（= 中文译本物理页 − 4）。

## 0. 总览

| 部分 | 印刷页 | track | 已落卡 | 状态 |
|---|---|---|---|---|
| 第 1–5 讲 局部类域论与希尔伯特符号 | 1–23 | `A` | 7（概念 5、勘误 2） | 完成 |
| 第 6–12 讲 同调代数工具 | 24–56 | `B` | 8（概念 3、推导 2、勘误 3） | 完成 |
| 第 13–17 讲 Tate 上同调与消没定理 | 57–75 | `C` | 5（概念 2、推导 1、勘误 2） | 完成 |
| 第 18 讲 范数群、Kummer 与存在定理 | 76–80 | `D` | 1（概念 1） | 完成（其余并入 A/C 两轨） |
| 第 19–23 讲 布劳尔群、两个不等式 | 81–107 | `E` | 6（概念 1、推导 2、勘误 3） | 完成 |
| 合计 | 1–107 | — | **27**（概念 12、推导 5、勘误 10） | lint 0 error / 0 warn |

## 1. 逐讲矩阵

| 讲 | 页 | track | 覆盖要点 | 概念 | 推导 | 勘误 | 已落卡 |
|---|---|---|---|---|---|---|---|
| 1 引言 | 1–5 | `A` | lcft / gcft 主定理的陈述形态；$n=2$ 的模型情形；断言 1.8 $\mathrm{Gal}_2(K)\cong(K^\times/(K^\times)^2)^\vee$ | ✓ | — | — | `concept/lcft-main-theorem` |
| 2 希尔伯特符号 | 6–9 | `A` | 定义 2.1；命题 2.3 双乘性；命题 2.9；定理 2.12 二次扩张的范数群 | ✓ | — | ✓ | `concept/hilbert-symbol`、`correction/bimultiplicativity` |
| 3 带驯分歧的范数群 | 10–13 | `A` | 驯分歧扩张里 $NL^\times$ 的显式计算；$\#\ker N$ 的夹逼 | ✓ | — | ✓ | `concept/tame-ramification`、`correction/ker-n-direction` |
| 4 整体类域论与二次互反律 | 14–18 | `A` | 二次互反律作为 lcft 的推论；希尔伯特符号的乘积公式 | ✓ | — | — | `concept/idele-class-group`（与第 5 讲共用） |
| 5 阿代尔配对 | 19–23 | `A` | 阿代尔配对（局部符号的乘积）非退化性与正合列 | ✓ | — | — | 同上 |
| 6 正合列与 Tate 上同调 | 24–28 | `B` | 定义 6.1 正合列；断言 6.3 蛇引理；引理 6.4 Euler 特征乘性；定理 6.5/6.6；断言 6.16 长正合列 | ✓ | ✓ | ✓ | `concept/tate-cohomology`、`deriv/tate-long-exact`、`correction/exactness-index` |
| 7 链复形与 Herbrand 商 | 29–33 | `B` | 定义 7.1 拟同构；引理 7.6；命题 7.7；引理 7.8 $\chi$ 的消没；命题 7.9 | ✓ | — | — | `concept/herbrand-quotient` |
| 8 Tate 上同调与逆向极限 | 34–37 | `B` | 定义 8.1；定理 8.2；命题 8.5 逆向极限与 $\hat H^i$ 交换 | — | — | — | 并入 `concept/tate-cohomology` |
| 9 希尔伯特定理 90 与上链复形 | 38–41 | `B` | 定理 9.2 $H^1(G,K^\times)=0$；定义 9.6 上链；定义 9.9 零伦；引理 9.10；命题 9.11 | ✓ | — | ✓ | `concept/hilbert-theorem-90`、`correction/homotopy-index` |
| 10 同伦、拟同构与余不变商 | 42–45 | `B` | 断言 10.1；引理 10.5 映射柱；断言 10.12 长正合列；定义 10.15 余不变商 | — | — | — | 并入 `concept/tate-cohomology` 与 `deriv/tate-long-exact` |
| 11 映射复形与投射消解 | 46–51 | `B` | 定义 11.6 投射消解；断言 11.11 比较引理 | — | — | — | 并入 `concept/herbrand-quotient` |
| 12 导出函子与显式投射消解 | 52–56 | `B` | 导出函子；显式投射消解里 $n$-上闭链所在的 $\Z[G^n]\otimes M$ | — | — | ✓ | `correction/cochain-group-ring` |
| 13 同伦余不变商、交换化与 Tate 上同调 | 57–61 | `C` | 定义 13.9；无界复形的 Tate 上同调；$M^{hG}$ 的方向（零阶为 $M^G$、一阶为 $H^1(G,M)$） | ✓ | — | ✓ | `concept/tate-cohomology-unbounded`、`correction/tate-superscript` |
| 14 Tate 上同调与 $K^{unr}$ | 62–65 | `C` | 定理 14.2；断言 14.6 用 Frobenius $x\mapsto x^q-x$ 判定消没 | — | — | — | 并入 `concept/tate-cohomology-unbounded` |
| 15 消没定理蕴含上同调类域论 | 66–69 | `C` | 断言 15.1/15.2 截断；定理 15.3/15.4/15.5；四项正合列 | ✓ | ✓ | — | `concept/vanishing-theorem`、`deriv/vanishing-implies-lcft` |
| 16 Tate 上同调群的消没 | 70–72 | `C` | 定理 16.3：$\hat H^{-1}$、$\hat H^0$ 的消没（限制与余限制的复合 = 乘以指数） | — | — | ✓ | `correction/corestriction` |
| 17 消没定理的证明 | 73–75 | `C` | 断言 17.2 范数群逼近；断言 17.3 主定理 | — | — | — | 并入 `concept/vanishing-theorem` |
| 18 范数群、Kummer 理论与投射有限上同调 | 76–80 | `D` | 定理 18.2 存在定理；推论 18.7 Kummer 配对；命题 18.13 投射有限上同调；定理 18.14 | ✓ | — | — | `concept/kummer-duality`、`concept/norm-group` |
| 19 布劳尔群 | 81–85 | `E` | 定义 19.1/19.3 $\Br^{coh}$；断言 19.4 图；定理 19.16；断言 19.17/19.18 | ✓ | — | — | `concept/brauer-group` |
| 20 第一不等式的证明 | 86–91 | `E` | 断言 20.1 正合列；定理 20.8 gcft 主定理；定理 20.9(1) $\chi(C_E)=n$；断言 20.13 蛇引理 | — | ✓ | ✓ | `deriv/first-inequality-herbrand`、`correction/gcft-diagram`、`correction/brauer-snake` |
| 21 阿廷与布劳尔互反律（上） | 92–95 | `E` | 定理 21.2 局部 Kronecker–Weber；引理 21.3；定理 21.4 Dwork–Lubin–Tate；断言 21.5 | — | — | — | 并入 `concept/brauer-group` 与 `deriv/second-inequality-descent` |
| 22 阿廷与布劳尔互反律（下） | 96–100 | `E` | Brauer 互反律；局部分支的 $\Z/2^{r-2}$ 结构 | — | — | — | 并入 `concept/brauer-group` |
| 23 第二不等式的证明 | 101–107 | `E` | 断言 23.1–23.11：从 $p$ 阶循环扩张下降到一般扩张 | — | ✓ | ✓ | `deriv/second-inequality-descent`、`correction/second-inequality-diagram` |

## 2. 跨讲的三张主卡

三张卡不是某一讲的裁切，而是一条主线的落点，`sources` 故意跨讲：

| 卡 | 覆盖讲次 | 意义 |
|---|---|---|
| `concept/lcft-main-theorem` | 1、2、19、20 | 局部主定理三件套（$\Gal^{\mathrm{ab}}\cong K^\times/NL^\times$、$\widehat{K^\times}\cong\Gal^{\mathrm{ab}}$、$\Br^{coh}\cong\Q/\Z$）的对照表 |
| `concept/norm-group` | 3、10、17、18 | 范数群从「计算」到「存在定理」的整条线 |
| `deriv/herbrand-quotient-multiplicativity` | 6、7、9 | 从有限长复形的指标计算一路推到 $\chi(L^\times)=[L:K]$ |

## 3. 未落卡的页

印刷页 108–115（第 23 讲末尾与参考文献）、以及各处过渡段没有单独落卡：这些页要么是结论的复述（已并入相邻卡），要么是习题集引用与书目。第 8、10、11、14、17、21、22 讲各有一到两个主题并进相邻卡，原因写在对应行的「已落卡」列。

## 4. 勘误卡的分布

10 张勘误卡对应 `工程文件/ERRATA.md` 里的 22 条「原文疑误」中的 10 条（其余 12 条属记号或下标重排，一句话即可说明，不值得单独成卡），另有 4 条图复原与 2 条原注、1 条「已核」不进卡：

| 讲 | 勘误卡 | 底本性错误 |
|---|---|---|
| 2 | `correction/bimultiplicativity` | 双乘性解释句把第二个方程也印成 $ax^2+by^2$ |
| 3 | `correction/ker-n-direction` | $\#\ker N$ 的界方向反了 |
| 6 | `correction/exactness-index` | 引理 6.4 的指标链自相矛盾 |
| 9 | `correction/homotopy-index` | 零伦公式的下标错位一位 |
| 12 | `correction/cochain-group-ring` | $n$-上闭链所在的项印成 $\Z[G]\otimes M$ |
| 13 | `correction/tate-superscript` | $M^{hG}$ 三处印成 $M_{hG}$ |
| 16 | `correction/corestriction` | 「膨胀」应为「余限制」 |
| 20 | `correction/gcft-diagram` | 定理 20.8 印成 $\Gal^{\mathrm{ab}}(G)$（$G$ 未定义） |
| 20 | `correction/brauer-snake` | 断言 20.13 的交换图缺零行零列、$\varphi/\psi$ 位置不明 |
| 23 | `correction/second-inequality-diagram` | 断言 23.10 的花括号标签被误读成同层箭头 |

（本表与 `ERRATA.md` 的编号顺序不一致：`ERRATA.md` 按讲次与译稿行号排列，本表按讲次排列；同一讲内按出现顺序。）
