# 外部参照：Moore TASI、Schottenloher 第 11 章、Wang 讲义、nLab

> 2026-11-13 用户指示（m00629）：本地还有别人上课的 CS 讲义、**Moore 的讲义**（公认可查，不必通读，有疑惑去查）、**nLab 条目**可给指引、桌面上有一本「给数学家的共形场论」**有专门讲 Verlinde 公式的一章**。
> 本文件只做一件事：把这几份材料定位到「哪一问去查哪一页」。**它们不是原文**，引用时不得写成“Witten 说”。

---

## 1. Moore, *Introduction to Chern–Simons Theory*（TASI 2019）中译

**路径**：`<本地路径>`
（同文件另在 `<本地路径>`）
**规模**：234 页。**引用规则：一律用页脚页（= PDF 第 N 页），标「中译 p.N」；不要引 `chunks/*.tex` 头注的「原印刷页 / PDF」两列。**

**页码校准（2026-11-13 实测，task-15；方法：pypdf 提取全文 + 标题行扫描）**：
- 页脚 = PDF 页：第 1–8 页页脚依次为 1–8，全书 234 页连续无缺。
- 节标题落点与页脚一致：2.2.6→p.27、2.2.13→p.58、3.3.2→p.92、3.4→p.94、4→p.96、4.1.1→p.96、4.5→p.114。
- 头注两列都不可靠：`chunks/c12.tex` 头注「原印刷 96–106 / PDF 97–107」，实际 3.3.2 在 p.92（差 5 页）；`chunks/c01.tex` 头注「PDF 6–14」，第 6 页实为目录；`chunks/c29.tex` 头注「PDF 244–245」，全书仅 234 页。

| 查什么 | 节 | 书页 | 对应 Witten 本文 |
|---|---|---|---|
| 相空间量子化、Hamilton 约化（把约束当 moment map 商掉） | 2.2.6 | 27 | §3 (3.3) 辛商；补“为什么 F=0 是第一类约束” |
| 曲面上的平坦规范场空间 | 2.2.7 | 31 | §3 p.368 的 M = Hom(π₁Σ,G)/G |
| 环面平坦联络量子化（真实极化 / 相干态 / Landau / Heisenberg 四视角） | 2.2.8–2.2.12 | 38–57 | §4.3 genus-one Hilbert 空间；T² 上 dim H⁰=k 的另一种算法 |
| 曲线模空间上的物理态丛（射影平坦联络） | 2.2.13 | 58 | §3.2 p.369–371；把“只到射影”讲得最清楚的一段 |
| 线缺陷关联函数与标架反常 | 2.2.14 | 59 | §4.3 (4.20)–(4.21) 标架反常 |
| 标架反常与缎带（ribbon）结构 | 2.2.16 | 62 | 同上；连到 TQFT 的 ribbon 图 |
| 拓扑反常与归一化因子 N | 2.2.17 | 66 | §4.3 归一化因子；S¹×X 配分函数的整体相位 |
| 与有理共形场论的关系 | 2.3 | 70 起 | T3/T4 的接口 |
| 紧曲面 Σ²×R 的量子化 | 3.3.1 | 88 | §3 整体重做一遍（更几何） |
| 带穿孔曲面的量子化 | 3.3.2 | 92 | §3.3 Wilson 线/穿刺点 |
| 平坦规范场模空间的量子化与代数几何 | 3.4 | 94 | §3.2 稳定全纯丛、行列式线丛 |
| WZW 与 RCFT（WZ 项、Virasoro/仿射、最高权表示） | 4.1–4.5 | 96–124 | §5 CS/WZW 对偶的“WZW 侧” |

**关键词命中页（PDF 页，供 grep/跳读）**：几何量子化 28/116/119/164/176；极化 24/56/183；Verlinde 76/95/126–134/147–148/234；共形块 3/57/58/68/74/76/92–95/125/133。

**用法**：不通读。S2/S3/S5 各场遇到“约束怎么商掉”“为什么只到射影”“标架反常怎么进 q”三个卡点时各查一次即可。

---

## 2. Schottenloher, *A Mathematical Introduction to Conformal Field Theory* 第 11 章（中译）

**路径**：`<本地路径>`
**规模**：216 页（第二版）。**PDF 页 = 书页 + 12**。

第 11 章「Verlinde 公式的数学方面」，书 p.172–189（PDF 184–201）：

| 节 | 书页 | 内容 | 用途 |
|---|---|---|---|
| 11.1 表示模空间与 theta 函数 | 172 | 共形块 = 向量丛截面；theta 函数观点 | 把 §3.2 的“平坦丛 + 全纯截面”接到代数几何 |
| 11.2 Verlinde 公式 | 177 | 公式陈述 + 证明史 | **T4 收口的判据**：Verlinde 是物理结论，数学上是猜想 |
| 11.3 带标记点曲面的融合规则 | 178 | 融合规则 = 共形块空间的乘法 | 与 §3.4 Verlinde 代数对照 |
| 11.4 融合环上的组合学：Verlinde 代数 | 184 | 融合环、幂等元、Freed–Hopkins–Teleman | 给“为什么 S 对角化”一个代数解释 |

**三条可直接引用的判断**：
1. Verlinde 公式在物理上是结论，在数学上是**猜想**（1988 年时）；
2. 证明线：Tsuchiya–Ueno–Yamada (1989) → Faltings (1994) “达到某种终结”；
3. 原话（书 p.213，nLab 亦引）：“Several mathematicians have worked on the problem of proving the Verlinde formula, starting with [TUY89] and coming to a certain end with [Fal94]. These proofs are all quite difficult to understand.”

**用法**：S5（T4）收口时必查一次，用来给 Witten §3.4/§4.5 的推导定级——Witten 给的是物理推导，不是 Faltings 的代数证明。

---

## 3. Yuchen Wang, *Notes on Chern–Simons Theory*（2024-09-10）

**路径**：`<本地路径>`
**规模**：22 页；自述基于 Witten 1989。

**用途**：紧凑骨架。适合在写读书笔记 §2（CS 作用量与 k 量子化）前 10 分钟过一遍，检查自己有没有漏步骤。
**注意**：2024 年课程讲义，非同行评议；只作骨架，不作证据。
（同目录 `chern1.pdf` 是 Chern 1944 Gauss–Bonnet 原文，与本文无关。）

---

## 4. nLab 条目（指引用，引用需写访问日期）

| 条目 | URL | 查什么 |
|---|---|---|
| Chern-Simons theory | https://ncatlab.org/nlab/show/Chern-Simons+theory | 现代范畴化视角、与 TQFT 的关系 |
| geometric quantization | https://ncatlab.org/nlab/show/geometric+quantization | 预量子化→极化→量子态的完整链条 |
| prequantization | https://ncatlab.org/nlab/show/prequantization | 整性条件与线丛的层论表述 |
| polarization | https://ncatlab.org/nlab/show/polarization | 实极化/复极化/Kähler 极化的精确定义 |
| space of states (in geometric quantization) | https://ncatlab.org/nlab/show/space+of+states+%28in+geometric+quantization%29 | 极化截面的严格定义 |
| Borel-Weil-Bott theorem | https://ncatlab.org/nlab/show/Borel-Weil-Bott+theorem | §3.3 把表示 R 实现为 G/T 量子化的定理依据 |
| Verlinde formula | https://ncatlab.org/nlab/show/Verlinde+formula | 公式的多种等价表述 + 证明文献 |
| modular tensor category | https://ncatlab.org/nlab/show/modular+tensor+category | T4/T5 的代数语言 |
| Reshetikhin-Turaev construction | https://ncatlab.org/nlab/show/Reshetikhin-Turaev+construction | Witten 构造的严格化版本 |
| Wess-Zumino-Witten model | https://ncatlab.org/nlab/show/Wess-Zumino-Witten+model | T3 的 WZW 侧 |

**已实读的两页**（2026-11-13）：
- **Verlinde formula**：Idea 段：“a Verlinde formula gives the dimension of a space of states of Chern-Simons theory… equivalently computes the dimension of spaces of non-abelian theta functions, the dimension of objects in a modular tensor category”；证明列 TUY89 (Adv. Stud. Pure Math. 16 (1989) 297–372)、Faltings (J. Alg. Geom. 3 (1994) 347–374)、Huang (PNAS 102 (2005) 5352)。
- **polarization**：实极化 = 被拉格朗日子流形叶状化；一般极化 = 复化切丛 T_C X 的 involutive Lagrangian 子丛（Bates–Weinstein def. 7.4）；Kähler 极化 = (1,0)/(0,1) 分解；量子态 = 沿叶协变常数的截面；另有 Bohr–Sommerfeld 叶、metaplectic correction 条目。

---

## 5. 使用纪律（五条）

1. **只查不读**：Moore 与 nLab 是“查证工具”，不是阅读任务；每场最多占 20 分钟。
2. **标注格式**：`[Moore 中译 p.N]`（页脚页 = PDF 页）、`[Schottenloher §11.2 / p.177]`、`[nLab: polarization, 2026-11-13]`。不得写成 `[src p.N]`（那是 Witten 原文专用），也不得引 chunks 头注的「原印刷页」。
3. **教材说 ≠ 原文说**：凡“Witten 断言 X”，必须回到 `witten1989\pages\` 页图或 `deliver\witten.tex` 行号。
4. **证明级别的区分**：Schottenloher 说 Verlinde 是猜想、Faltings 才证；Witten §4.5 给的是物理证明。写笔记时必须分开标“作者证明 / 他人定理 / 我们推导”。
5. **不引二手转述**：nLab 给的文献卷页可直接抄进文献表（已核过的），但“nLab 说……”只能作线索，不作证据。

---

## 6. 待核

- [x] Moore 中译页码偏移 —— 已校准（2026-11-13，task-15）：页脚页 = PDF 页 = 引用页；chunks 头注的「原印刷页 / PDF」两列均不可靠（c12 差约 5 页、c29 声称超出 234 页），详见 §1 校准注。
- [ ] Schottenloher 11.2 是否给出公式的完整陈述（还是只给证明史）。
- [ ] nLab 各条目最近修订日期（引用时逐个记）。
