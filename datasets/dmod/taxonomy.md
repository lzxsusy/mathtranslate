# D-模资料卡分类体系（dmod taxonomy v1）

底本：Miličić《Lectures on the Algebraic Theory of D-Modules》，150 页，5 章 35 节，283 条编号条目。
卡片全部依据**校订批注本**（`../../08_source_code/SY07-10_D-模的代数理论讲义（Miličić）/`）抽取。
印刷页 = PDF 页 − 6（第 1 章第 1 页 = PDF 第 7 页），第 V 章止于印刷页 142。

## 1. 轨道（track）

| track | 名称 | 覆盖章节 | 卡片主要回答什么 |
| --- | --- | --- | --- |
| `O` | 预备：交换代数与维数 | I §1–§4 | Hilbert 多项式、Krull 维数、重数、滤过与 Artin–Rees 怎么算、为什么需要它们 |
| `A` | 算子环与 $D(n)$-模 | I §5–§6 | Weyl 代数 $\mathcal{D}(n)$ 的滤过、好滤过、Gröbner 式象征，$D(n)$-模为何诺特 |
| `B` | 特征簇与完整模 | I §7–§8, §13；III §3；V §1 | 特征簇是什么、为何是锥、完整（holonomic）模怎么定义、为什么有限长度 |
| `C` | $\mathcal{D}_X$-模层 | II 全章；III §1–§2, §4–§5 | 相对微分算子、$\mathcal{D}_X$ 的层化、光滑点处 $\mathrm{gr}\mathcal{D}_X\cong\mathrm{Sym}\,\mathcal{T}_X$、凝聚化函子 |
| `D` | 直像与逆像（六种运算） | I §9–§11；IV §1–§6 | $f_+$/$f^+$、$\mathcal{D}_{X\to Y}$-模、外张量积、投影公式，以及与 $Rf_*$、$Lf^*$ 的关系 |
| `E` | Bernstein 不等式与 Kashiwara | IV §7–§8；V §3, §6 | Bernstein 不等式的证明结构、完整模的直像仍完整（Kashiwara） |
| `F` | 局部上同调与基变换 | IV §9–§10；V §5 | $R\Gamma_Z$、局部化、Kashiwara 的基变换定理，非特征情形如何处理 |
| `G` | 分类与联络 | V §2, §4 | 1 维情形、平坦联络/局部系统、Riemann–Hilbert 对应与 Deligne 的存在性定理 |
| `H` | 例子与计算 | I §10.5, §12；II §2；V §2 | 射影空间、仿射直线、$A^1$ 上的具体例子，可逐行复算 |

轨道只表示**主题归属**，不表示难度；跨章卡片按其主要论证所在章归档（如「Kashiwara 定理」归 `E`，虽然它在 I §12 也有部分表述）。

## 2. 卡片粒度

- 一条带编号的 Lemma/Proposition/Theorem/Example 通常**不必**单独成卡；一张卡 = 一个可独立回答的问题。
- 优先成卡的对象：核心定义（特征簇、完整模、$\mathcal{D}_{X\to Y}$-模）、有完整证明的主定理（Bernstein 不等式、Kashiwara 定理、Artin–Rees）、讲义反复引用却没展开的工具（Krull 交定理、Hilbert 多项式、Gröbner 式象征）。
- 每张概念卡必须有 `theorems[]` 至少一条，或 `definition` 本身是定义卡；`proof.status = sketch` 时 `gap_note` 必须点名缺口与出处。

## 3. 关联规则

- `related` 至少 2 条，必须解析到本库已有 `id`；优先连「上游依赖」与「下游应用」各一。
- 同一 track 内允许单向链（`O → A → B → C → D → E`），跨 track 连接（`B ↔ C`、`D ↔ F`）必须显式写进 `related`。
- 例子卡（`type: example`）用 `concept_refs` 指回概念卡，不重复连接。

## 4. 命名（slug）

- 概念卡：英文术语小写连字符，如 `characteristic-variety`、`holonomic-module`、`bernstein-inequality`、`kashiwara-theorem`、`artin-rees`。
- 例子卡：`example-` 前缀，如 `example-projective-space-d-module`。
- 同一概念若有多个通行名（holonomic / holonomic module / maximally overdetermined），`aliases` 收齐，slug 只用主名。

## 5. 与本库其他数据集的关系

- 结构沿用 [`../csw/SCHEMA.md`](../csw/SCHEMA.md) v1；生产流程见 [`workflow/PRODUCTION.md`](workflow/PRODUCTION.md)。
- `datasets/glc/` 是几何 Langlands 的资料卡库，与本库共享 `D`-模语言，交叉引用时直接写 `glc/concept/<slug>`，不复制卡片。

## 6. 卡片清单

由 `tools/gen_docs.py` 生成，勿手改。“核验”列：E = 外部权威已核；S = 仅讲义依据（`source-only`）。

### O · 预备：交换代数与维数（6 张）

| 卡 | 标题 | 原书条目 | 页 | 核验 |
| --- | --- | --- | --- | --- |
| `dmod/concept/artin-rees-lemma` | Artin–Rees 引理 | §2 局部环上模的维数 | p.7 | E |
| `dmod/concept/associated-graded-ring` | 伴随分次环 $\operatorname{Gr}D$ | §3 滤过环上模的维数 | p.9 | S |
| `dmod/concept/dimension-theory-of-filtered-modules` | 滤过模的维数与重数 | §3 滤过环上模的维数 | p.13 | S |
| `dmod/concept/good-filtration` | 好滤过 | §3 滤过环上模的维数 | p.10 | S |
| `dmod/concept/hilbert-polynomial` | Hilbert 多项式与 Poincaré 级数 | §1 Hilbert 多项式 | p.1 | S |
| `dmod/concept/krull-dimension-and-multiplicity` | Krull 维数与重数 | §2 局部环上模的维数 | p.7 | S |

### A · 算子环与 $D(n)$-模（6 张）

| 卡 | 标题 | 原书条目 | 页 | 核验 |
| --- | --- | --- | --- | --- |
| `dmod/concept/grobner-basis-symbol` | 符号理想与 Gröbner 基 | §7 特征簇 | p.29 | S |
| `dmod/concept/noetherianity-of-dn` | D(n) 的诺特性 | §3 滤过环上模的维数、§5 多项式系数微分算子环 | p.11 | S |
| `dmod/concept/order-filtration-of-dn` | $D(n)$ 的阶滤过与 Bernstein 滤过 | §5 多项式系数微分算子环 | p.19 | S |
| `dmod/concept/ring-of-differential-operators-polynomial` | 微分算子环 $\operatorname{Diff}_k(A)$ | §5 多项式系数微分算子环 | p.18 | S |
| `dmod/concept/symbol-and-principal-symbol` | 符号与主符号 | §5 多项式系数微分算子环 | p.19 | S |
| `dmod/concept/weyl-algebra` | Weyl 代数 $D(n)$ | §5 多项式系数微分算子环 | p.22 | S |

### B · 特征簇与完整模（9 张）

| 卡 | 标题 | 原书条目 | 页 | 核验 |
| --- | --- | --- | --- | --- |
| `dmod/concept/bernstein-dimension` | Bernstein 维数与重数 | §6 多项式系数微分算子环上的模 | p.24 | S |
| `dmod/concept/characteristic-ideal` | 特征理想 | §7 特征簇 | p.26 | S |
| `dmod/concept/characteristic-variety` | 特征簇（$D(n)$-模，第 I 章） | §7 特征簇 | p.25 | S |
| `dmod/concept/finite-length-of-holonomic` | 完整模的有限长度 | §8 完整模 | p.32 | S |
| `dmod/concept/holonomic-module` | 完整模（holonomic 模） | §8 完整模 | p.32 | E |
| `dmod/concept/holonomicity-under-tensor` | 外张量积下的完整性 | §9 外张量积 | p.36 | S |
| `dmod/concept/kashiwara-theorem-statement` | Kashiwara 定理（第 I 章 §12 的陈述） | §12 Kashiwara 定理 | p.49 | S |
| `dmod/concept/preservation-of-holonomicity` | 完整性的保持（第 I 章 §13） | §13 完整性的保持 | p.51 | S |
| `dmod/concept/singular-support` | 奇异支集 | §7 特征簇 | p.27 | S |

### C · $\mathcal{D}_X$-模层（12 张）

| 卡 | 标题 | 原书条目 | 页 | 核验 |
| --- | --- | --- | --- | --- |
| `dmod/concept/characteristic-variety-sheaf` | 特征簇（$\mathcal D_X$-模层，第 III 章） | 第 III 章 §3 特征簇 | p.83 | S |
| `dmod/concept/coherator` | 凝聚化函子（coherator）$Q_X$ | 第 III 章 §4 Coherentor（凝聚化函子） | p.86 | S |
| `dmod/concept/coherent-d-module` | 凝聚 $\mathcal D_X$-模 | 第 III 章 §2 凝聚 $\mathcal D_X$-模 | p.79 | E |
| `dmod/concept/d-module-on-projective-space` | 射影空间上的 $D$-模 | 第 III 章 §5 射影空间上的 $D$-模 | p.90 | S |
| `dmod/concept/dz-structure-sheaf` | 局部微分算子层 $\mathcal D_X$ | 第 II 章 §1 代数簇上的微分算子 | p.55 | S |
| `dmod/concept/finite-length-sheaf` | 有限长度 $\mathcal D_X$-模 | 第 III 章 §2 凝聚 $\mathcal D_X$-模 | p.79 | S |
| `dmod/concept/graded-dz-on-smooth` | 光滑簇上的分次层 $\operatorname{Gr}\mathcal D_X$ | 第 II 章 §3 光滑簇上的微分算子层 | p.73 | S |
| `dmod/concept/module-over-algebraic-variety` | 代数簇上的模与拟凝聚性 | 第 III 章 §1 拟凝聚 $\mathcal D_X$-模 | p.77 | E |
| `dmod/concept/quasi-coherent-d-module` | 拟凝聚 $\mathcal D_X$-模 | 第 III 章 §1 拟凝聚 $\mathcal D_X$-模 | p.77 | E |
| `dmod/concept/relative-differential-operators` | 相对微分算子的一阶部分 | 第 II 章 §1 代数簇上的微分算子（含译者注） | p.55 | E |
| `dmod/concept/smooth-point` | 光滑点 | 第 II 章 §2 代数簇的光滑点 | p.62 | S |
| `dmod/concept/support-and-irreducibility` | 支集与不可约性 | 第 III 章 §1 拟凝聚 $\mathcal D_X$-模 | p.77 | S |

### D · 直像与逆像（六种运算）（10 张）

| 卡 | 标题 | 原书条目 | 页 | 核验 |
| --- | --- | --- | --- | --- |
| `dmod/concept/bimodule-dx-to-y` | 相对双模 $\mathcal D_{X\to Y}$ | §1 双模 $\mathcal D_{X\to Y}$ | p.99 | S |
| `dmod/concept/cohomological-dimension-of-i-plus` | $i^+$ 的左同调维数 | §10 逆像（同调维数） | p.41 | S |
| `dmod/concept/derived-inverse-image` | 导出逆像 $L\varphi^+$ | §3 逆像函子（导出化） | p.105 | S |
| `dmod/concept/direct-image-functor` | 直像函子 $\varphi_+$ | §5 直像函子 | p.111 | E |
| `dmod/concept/direct-image-of-immersion` | 浸入的直像 | §6 浸入的直像 | p.115 | S |
| `dmod/concept/external-tensor-product` | 外张量积 $M\boxtimes N$ | §9 外张量积 | p.36 | S |
| `dmod/concept/inverse-image-functor` | 逆像函子 $\varphi^+$ | §3 逆像函子 | p.105 | E |
| `dmod/concept/projection-formula` | 投影公式 | §4 投影公式 | p.109 | E |
| `dmod/concept/six-operations` | D-模的六种运算 | §1 六运算批注（校订批注） | p.99 | E |
| `dmod/concept/standard-filtration-of-dx-to-y` | $\mathcal D_{X\to Y}$ 的标准滤过 | §1 双模 $\mathcal D_{X\to Y}$ 的滤过 | p.99 | S |

### E · Bernstein 不等式与 Kashiwara（5 张）

| 卡 | 标题 | 原书条目 | 页 | 核验 |
| --- | --- | --- | --- | --- |
| `dmod/concept/bernstein-dimension-bound` | Bernstein 维数下界 $d(M)\ge n$ | §6 多项式系数微分算子环上的模（定理 6.3） | p.24–25 | S |
| `dmod/concept/bernstein-inequality` | Bernstein 不等式 | §7 Bernstein 不等式 | p.119–120 | S |
| `dmod/concept/holonomic-defect` | 完整亏格 $\operatorname{holdef}$ | §6 浸入的直像（定义与推论 4.6.9） | p.119 | S |
| `dmod/concept/holonomicity-preserved-by-direct-image` | 完整模在直像下的保持（第 V 章） | §3 完整性与直像 | p.139–141 | E |
| `dmod/concept/kashiwara-theorem` | Kashiwara 定理（第 IV 章：$i_+$ 与 $i^!$ 互逆） | §8 闭浸入与 Kashiwara 定理 | p.124 | E |

### F · 局部上同调与基变换（5 张）

| 卡 | 标题 | 原书条目 | 页 | 核验 |
| --- | --- | --- | --- | --- |
| `dmod/concept/base-change-for-d-modules` | $\mathcal D$-模的基变换（方图与两种特例） | §10 基变换 | p.128–130 | S |
| `dmod/concept/kashiwara-base-change` | Kashiwara 基变换（闭浸入情形） | §10 基变换（定理 4.10.2 的证明） | p.130–132 | S |
| `dmod/concept/local-cohomology-d-module` | $\mathcal D$-模的局部上同调 $R\Gamma_Y$ | §9 $\mathcal D$-模的局部上同调 | p.124–125 | E |
| `dmod/concept/non-characteristic-restriction` | 非特征限制（逆像的完整性） | §6 完整性与逆像 | p.140–141 | S |
| `dmod/concept/support-localization` | 支集局部化 $\Gamma_{[Y]}$ | §8 闭浸入与 Kashiwara 定理 | p.123–124 | S |

### G · 分类与联络（5 张）

| 卡 | 标题 | 原书条目 | 页 | 核验 |
| --- | --- | --- | --- | --- |
| `dmod/concept/deligne-regular-singular` | Deligne 正则奇点定理 | V §4 不可约完整模的分类，批注 | p.140 | E |
| `dmod/concept/flat-connection` | 平坦联络（可积联络） | V §2 联络（Connections） | p.135 | E |
| `dmod/concept/irreducible-holonomic-classification` | 不可约完整模的分类 | V §4 不可约完整模的分类 | p.139 | S |
| `dmod/concept/local-system` | 局部系（局部常值层） | V §2 联络（Connections），批注 | p.136 | E |
| `dmod/concept/riemann-hilbert-correspondence` | Riemann–Hilbert 对应 | V §2 联络（Connections），批注 | p.136 | E |

### H · 例子与计算（3 张）

| 卡 | 标题 | 原书条目 | 页 | 核验 |
| --- | --- | --- | --- | --- |
| `dmod/concept/d-module-on-affine-line` | 仿射直线上的 $\mathcal D$-模 | I §8 完整模 | p.33 | S |
| `dmod/example/example-d-module-on-projective-space` | 射影空间 $P^n$ 上拟凝聚 $\mathcal D$-模的整体截面 | III §5 射影空间上的 D-模 | p.91 | S |
| `dmod/example/example-euler-operator-on-a1` | $\mathbb A^1$ 上 Euler 算子 $z\partial-\alpha$ 的 $\mathcal D$-模 | I §8 完整模，例 | p.34 | S |
