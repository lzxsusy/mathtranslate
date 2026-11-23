# 局部化资料卡分类体系（mloc taxonomy v1）

底本：Miličić《Localization and Representation Theory of Reductive Lie Groups》，129 印刷页，6 章。
卡片依据本仓中译本（`../../08_source_code/SY07-11_局部化与约化李群的表示论（Miličić）/`）抽取。
印刷页 = PDF 页 − 4。

## 1. 轨道（track）

| track | 名称 | 覆盖章节 | 卡片主要回答什么 |
| --- | --- | --- | --- |
| `O` | 几何预备：旗簇与群作用 | 2 §1；4 §1 | 旗簇作为 Borel 子代数的簇、`b_x`/`n_x`/`B_x`、Bruhat 分解、`K`-轨道为何仿射嵌入 |
| `A` | 扭微分算子层 | 1 §1 | 扭层 `(D,i)` 是什么、为什么同构类由 `H^1(X,Z^1_X)` 分类、用可积层 `L` 去扭、反代数 `D^\circ` 的扭参数 |
| `B` | 齐性扭层与 `D_λ` | 1 §2；2 §1 | `(D,γ,α)` 三元组、`λ ↔` 层的双射、`D_λ = D_{X,λ+ρ}` 的约定、`U_θ = U(g)/J_θU(g)` |
| `C` | `D_λ`-模的上同调 | 2 §2–§6 | 平移原理、消没/非消没定理、Borel–Weil–Bott、`H^i(X,D_λ)` 的显式计算 |
| `D` | 局部化 | 3 §1–§2, §7, §9 | `∆_λ` 与 `Γ` 的伴随、反支配时 `V ≅ Γ∆_λ(V)`、`Γ∆_λ ≅` n-同调、支集与 n-同调 |
| `E` | 交织函子 | 3 §3–§6, §8 | 旗簇对应造出的 `I_w`、正合性、与 `∆/Γ` 的交换、单反射的显式公式、完整复形 |
| `F` | Harish-Chandra 模与层 | 4 全章 | `(g,K)` 对、HC 模 ↔ 带 `K`-等变结构的 D-模、HC 层的不可约性 |
| `G` | 最高权模与 Verma 模 | 5 §1 | 范畴 O 的最高权模、`M(λ)` 的泛性质与 `L(λ)`、BGG 反变形式、`Ext` 计算 |
| `H` | 广义 Verma 与 KL 算法 | 5 §2；6 全章 | `W^Θ` 的陪集分解、`M_p(λ)`、Hecke 代数与 KL 多项式、合成重数 |

轨道只表示主题归属，不表示难度。跨章卡片按**主要论证**所在章归档。

## 2. 卡片粒度

- 一张卡 = 一个可独立回答的问题；编号条目不必逐条成卡。
- 优先成卡：核心定义（扭层、齐性扭层、`D_λ`、`U_θ`、局部化函子、交织函子、HC 层、广义 Verma 模）、有完整证明的主定理（1.2、1.3、2.4、3.1、Borel–Weil–Bott、局部化的等价定理、KL 重数定理）、书中反复引用却没展开的工具（Bruhat 分解、Levi 分解、BGG 反变形式）。
- 概念卡要么有 `theorems[]` ≥1，要么本身就是定义卡；`proof.status = sketch` 时 `gap_note` 必须点名缺口。

## 3. 关联规则

- `related` ≥2：优先「上游依赖」与「下游应用」各一；跨库链接写全 id（如 `dmod/concept/holonomic-module`）。
- 与 dmod 的分工：通用 D-模概念只在 dmod 立卡，本库用 `related` 指过去；本库只收本书特有的构造。
- 例子卡用 `concept_refs` 指回概念卡。

## 4. 命名（slug）

- 概念卡：英文术语小写连字符，如 `twisted-sheaf-of-differential-operators`、`homogeneous-twisted-sheaf`、`d-lambda`、`localization-functor`、`intertwining-functor`、`harish-chandra-sheaf`、`generalized-verma-module`、`kazhdan-lusztig-algorithm`。
- 例子卡：`example-` 前缀，如 `example-d-lambda-on-p1`、`example-sl2-verma-module`。
- 同一概念的多个通行名进 `aliases`，slug 只用主名。
