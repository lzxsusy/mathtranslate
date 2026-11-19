# leanstmt 路线图：下一步该找哪些文献

目的不是把全部几何朗兰兹形式化（现在做不到），而是**按"陈述可落地的速度"排序**，
建设一条从「原文 → 翻译/阅读 → 语料 → 资料卡 → Lean 陈述」的生产线。
下面按**先做 / 缓做 / 暂不做**三分，每条给出：为什么、能产出什么、卡在哪。

## 〇、已落地（2026-11-19）

- **Witten 2008**（下栏 4.B）已做成 `leanstmt` 的 **B 批**：14 张卡（5 `certified` + 9 `gap`，轨道 `W08`）。
  certified 只有离散/代数影子（SL(N,ℂ) 中心 = μ_N、有限 Pontryagin 对偶两条、非正则奇点系数伸缩律、函数空间 currying）；
  本文主定理（Hitchin 纤维化上的镜像对称）如实进 G06 gap——它正好是 mathlib 缺口最深的一层。
  见 `datasets/leanstmt/README.md` 与 `workflow/PRODUCTION.md` §六。

## 一、先做（6–12 个月内，statements 能落在现有 mathlib 上）

### 1. GNO 1977：Gods, Nuyts, Olive, *Gauge theories and magnetic charge*
- 出处：Nucl. Phys. **B125** (1977) 1–28（DOI: 10.1016/0550-3213(77)90086-8）。
- 为什么先做：这是「't Hooft 磁通 / 磁荷量子化 / 对偶环面」的源头文献，全文大多是**群论级**陈述（权格、根格、character/cocharacter 格、ℤ_N 中心），篇幅短、定义清楚，正落在 mathlib 的基础设施（有限群、模、`ZMod`、`PontryaginDual`、`AddChar`）上。
- 可产出：30–40 条陈述（对偶环面 = Hom(Λ, U(1))、磁荷 = 反权、中心 ℤ_N、't Hooft 通量配对），其中至少一半可 `certified`；配套 1 个中文译注本（短，60 页内）+ 语料。
- 现在就能起的 3 条：`(Λ^*)dual ≃ T`（characters of dual torus = lattice）、`ZMod` 阶与卡数（已在本批 S01–S03）、`exp(2πi⟨·,·⟩)` 的配对非退化性。

### 2. Hitchin 1987：*The self-duality equations on a Riemann surface*
- 出处：Proc. London Math. Soc. (3) **55** (1987) 59–126。
- 为什么：原文把 **Hitchin 方程、完全可积性、谱曲线、阿贝尔化** 全部用明确方程写出来（§2–§7），是本库 SY03-20 的"另一半源头"。等式级陈述多，适合语料；Hitchin 纤维维数、谱曲线亏格这类现在只能进 gap 卡，但**方程与代数化约的部分可以形式化**（矩阵值微分、迹不变量、特征多项式——mathlib 的 `Matrix`/`Polynomial`/`Module` 足够）。
- 可产出：15–25 条（Hitchin 方程的定义、稳定条件、特征多项式系数、gauge 变换作用、约化到 SL_2 的平移），中文译注本（已有 Local 素材可对照）。

### 3. 't Hooft 1978 / 't Hooft–Polyakov 1974（磁单极与磁通）
- 出处：'t Hooft, *Magnetic monopoles in unified gauge theories*, Nucl. Phys. **B79** (1974) 276；Polyakov, JETP Lett. **20** (1974) 194。
- 为什么：这些是"磁荷 = 拓扑荷"的原始陈述，且是**点粒子/规范场**层面的，可以先用有限维/代数版本形式化（Dirac 量子化条件、ℤ_2 拓扑、圈数 winding number：mathlib 有 `AddCircle`、`Circle`、`FundamentalGroup` 的基础设施与 `ZMod`）。
- 可产出：10–15 条（Dirac 量子化 $eg\in 2\pi\mathbb Z$、winding number 取整、't Hooft–Polyakov 磁荷）。

### 4. 现代"陈述密集"综述（不做全文形式化，做语料 + 资料卡 + 挑选条目）
- A. Frenkel, *Langlands program and conformal field theory*（arXiv:hep-th/0512172，90 余页）——本库已有中译，statement 密度高，是"该形式化什么"的选题地图。
- B. Witten 2008, *Mirror symmetry, Hitchin's equations, and Langlands duality*（arXiv:0802.0999）——本库有原文，是 SY03-20 的直接前身，属同一选题簇。**（已落地为 B 批 14 卡，见上栏〇）**
- C. Frenkel–Witten 2007, *Geometric endoscopy and mirror symmetry*（arXiv:0710.5939）。
- D. Ben-Zvi, *What is a geometric Langlands dual?*（本库已有译注）。
- E. 陈麟《Introduction to Geometric Langlands Theory》（清华 2023，本库 `datasets/glc` 154 卡）与袁耀《Langlands 纲领导论》（SY02-09）——**只做"语料与资料卡"，不做形式化**，因为它们进入 Hitchin 模空间 / D-模 / 曲线亏格层，全部是 gap。
- 这些综述的用途：用它们把"原文陈述 → 中文 → 资料卡"的链条跑熟，并从中挑 5–10 条能下放到有限/组合层级的陈述。

## 二、缓做（需要自建定义或等 mathlib 长大）

| 文献 | 为什么缓 | 需要的上游基础设施 |
| --- | --- | --- |
| Beilinson–Drinfeld《Quantization of Hitchin's integrable system and Hecke eigensheaves》 | 陈述层级过深（D-模、特征簇、op） | 代数曲线亏格/除子、D-模、栈 |
| Kapustin–Witten 2006（本库 kw06 67 卡） | 物理陈述天然是"两维 TQFT 的范畴"级别 | 曲线模空间、TQFT 公理的 Lean 化 |
| Gaiotto–Witten 系列 | 边界条件的 S-对偶在 2d-4d 系统里，当前无对应形式框架 | 超对称表示、层化不变量 |
| Frenkel 2005 全文形式化 | 同上，规模过大 | ——（但可抽条目，见上一栏 4.A） |
| Lin Chen GLC / 袁耀 Langlands | 同上（已做资料卡） | 曲线、Hitchin、D-模 |

## 三、暂不做
- 把整篇 Witten 2015 或 KW06 全文形式化（条目过多、gap 比例过高，产物会大部分是 `sorry`，反而稀释语料价值）。
- 竞赛/教材级重复（Lean 社区已有大量），除非用于校准工具链。
- 自造定义冒充 mathlib（违反 `SCHEMA.md` 纪律 3）。

## 四、下一批（batch 2）建议的 12–20 条陈述簇

按"能真实 `certified`"排序，建议从这三簇各取几条：

1. **对偶环面与 Pontryagin 对偶**（GNO 1977）：`T^* = Hom(Λ^*, U(1))`、`Λ^* ≃ Hom(T, U(1))`、T-duality = pairing 的非退化性。mathlib 有 `PontryaginDual`、`AddChar`；需核实 `ZMod`/`Circle` 级别的可用性。
2. **权格与根格 / Langlands 对偶根系统**（Borel–Weil 侧）：simple roots、dominant weights、Weyl 群作用于权格、Cartan 矩阵的对称化。mathlib 的 `RootSystem` 只有部分，需先核实哪些已在（这是最高价值的自建层，因为后面所有几何朗兰兹都依赖它）。
3. **Hecke 修正的组合核**（GL_n）：相对位置（仿射 Grassmannian 的胞腔）在 GL_n 上就是**格链 / Smith 标准形**，完全可以用 `Matrix` + `ZMod`/`ℤ` 形式化：`{lattice chains} ↔ {relative position = Smith normal form of M}`。这条最"便宜"、最有教育价值，建议优先。

## 五、给译者/资料卡的衔接规则

- 每翻译完一篇，先产出 `statements.tsv`（id / kind / 中文陈述 / 原文定位 / 依赖 / 拟形式化难度），**再**决定哪些做卡、哪些只做语料。
- 资料卡里的"定理陈述"必须带原文页/式锚（本库已有规矩），形式化卡直接以该锚为 `source`。
- 形式化卡与翻译工程互链：SY03-20 是 `leanstmt` 的源工程之一（本批 12 条即来自它）；后续每部译注本都在 `投稿信息.md` 里注明"是否已成为 leanstmt 的源"。
