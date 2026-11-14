# 前言 + 第1章 校订日志（rv-preface-ch01）

负责文件：`chapters/preface.tex`、`chapters/ch01.tex`
负责页码：PDF 7–9（前言）、PDF 11–36（第1章）

## 已核对范围
- p007-009（前言，preface-001 … preface-016）✅ 2026-11-14
- p011-020（ch01-intro-001 … ch01-1.1.4-001）✅ 2026-11-14
- p021-030（ch01-1.1.4-002 … ch01-1.3-009）✅ 2026-11-14
- p031-036（ch01-1.3-010 … ch01-1.3.3-008，含猜想 1.5）✅ 2026-11-14（4 块全部完成）

## 改动记录

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 1 | preface-015 / preface.tex L49 | "We especially thank Lori Lejeune for **providing the artwork** in the book." | 我们特别感谢 Lori Lejeune 为本书**绘制**插图。 | 我们特别感谢 Lori Lejeune 为本书**提供**插图。 | 误译 | "providing the artwork" 只说提供图版，未说她亲手绘制；"绘制"多出了原文没有的信息 |
| 2 | ch01-1.1.4-001 / ch01.tex L198 | "This leads to equations of motion for the fields which arise from the open string, namely the data (M,E,∇)." | 即数据 $(M,E,\nabla)$**，**的运动方程 | 即数据 $(M,E,\nabla)$ 的运动方程 | 标点 | 全角逗号插在"的"字前，属明显错配，去掉该逗号（语义不变） |
| 3 | ch01-1.2.1-002 / ch01.tex L348 | "Each isotopy class of Lagrangian submanifolds contains either zero or one special Lagrangian, depending on a stability condition which varies with the complex structure of the underlying manifold."（p27，仅此一句） | …变化的稳定性条件**；在连通、可分次、Floer 上同调的障碍消失，且第二 Stiefel--Whitney 类来自环境流形的条件下，这个类中至多有一个光滑的特殊 Lagrange 代表。**因此… | …变化的稳定性条件。因此… | 多出内容（P1） | 英文无 Thomas–Yau 那串条件（连通/可分次/Floer 障碍/第二 Stiefel–Whitney 类），中译整句为原文所无；按 GUIDE P1"中文多出原文没有的内容"删去，保留"因此，所预期的图景是：每个这样的类中，或者没有特殊 Lagrange 子流形，或者只有一个"。**注意**：该句数学上正确（Thomas–Yau 图景），如 Lead 认为属"合理补偿"可整句恢复。 |
| 4 | ch01-1.3-007 / ch01.tex L424 | "In string theory, T-duality implies that R ≥ l_s" | T 对偶意味着**可以取** $R\geq l_s$ | T 对偶意味着 $R\geq l_s$ | 误译 | "implies that R ≥ l_s"是断言，不是"可以取"（模态弱化）；且后半句"任何 R<l_s 的理论都等价于 R>l_s"正是该断言的依据 |
| 5 | ch01-1.3-008 脚注 6 / ch01.tex L431 | "For comparison, the group Diff / Diff_0 ≅ SL(d, Z)." | 作为比较，**保定向线性大微分同胚所构成的群**为 $\operatorname{SL}(d,\mathbb{Z})$。 | 作为比较，$\operatorname{Diff}/\operatorname{Diff}_0\cong\operatorname{SL}(d,\mathbb{Z})$。 | 误译/漏译 | 原译把 Diff/Diff_0 说成"保定向线性大微分同胚"，既丢掉了商群 $\operatorname{Diff}/\operatorname{Diff}_0$，又把"大微分同胚"限定为"线性"，与原文不符 |
| 6 | ch01-1.3-010 / ch01.tex L437 | "the full closed string algebra contains the group algebra **C[Z^d] ⊕ C[Z^d]**" | 完整闭弦代数包含群代数 $\mathbb{C}[\mathbb{Z}^d\oplus\mathbb{Z}^d]$ | 完整闭弦代数包含群代数 $\mathbb{C}[\mathbb{Z}^d]\oplus\mathbb{C}[\mathbb{Z}^d]$ | 数学错误（P1） | 原文是两个群代数的直和 $\mathbb{C}[\mathbb{Z}^d]\oplus\mathbb{C}[\mathbb{Z}^d]$（分别对应动量与缠绕）；原译写成"直和群 $\mathbb{Z}^d\oplus\mathbb{Z}^d$ 的群代数"，即 $\mathbb{C}[\mathbb{Z}^{2d}]$，与原文的代数结构不同（后者同构于张量积而非直和） |

## 待确认 / 未改（供 Lead 判断）

- preface-002：英文 "manifolds of special holonomy" 译作"特殊完整群流形"。术语表 holonomy-group→完整群，ch07 亦用"特殊完整群度量"，故判为全书统一译法，不改（若 Lead 统一改为"特殊和乐流形"需全章批量处理）。
- preface-001：英文 "It was run jointly by the organizers of two concurrent workshops … in collaboration with Arthur Jaffe"；原译"时任 Clay 数学研究所主席的 Arthur Jaffe 也参与了合作"把 Jaffe 处理成合作方之一，语义可通，未改。
- preface-008："The task was carried out … on the basis of cross-reading and comments made by all of the authors" 译作"根据所有作者相互审读后提出的意见完成"；"cross-reading" 含"交叉审读"之意，现译可通，未改。
- ch01-1.1.3-001：英文 "We can now explain our definition of a Dirichlet brane as an allowed end point for an open string." 原译"现在可以解释**为什么**将 Dirichlet 膜定义为开弦所允许的端点"。"why"是译者加的语感，严格说是"解释我们这一（把膜定义为端点的）定义的做法"，属可接受的行文处理，未改。
- ch01-1.1.1-012：英文 "These are referred to as "branes" (short for membranes)." 原译"这些解称为"brane"，是"membrane"的简称，中文称为"膜"。"末句"中文称为"膜""是译者补的说明性文字，非原文内容，但属术语交代，未删。
- **ch01-1.1.4-009 / ch01.tex L238**：原书 p22 扫描图确认为 "Let n = dim_ℝ M"（已看图核实，非 pdftotext 误读），译文作"令 $n=\dim_{\mathbb{C}}X$"。但同节 (4) "r + n = dim_ℝ M" 只在 n=dim_C X 时自洽（Lagrange 情形 r=0，dim_ℝ M=n），原文自身矛盾，译文取了数学自洽的值。**未改**，请 Lead 定夺是否回改为 $\dim_{\mathbb{R}}M$。
- **ch01-1.3-008 / ch01.tex L431**：原书 p30 扫描图确认为 "isomorphic to **SO**(d,d;ℤ)"，译文作 $\operatorname{O}(d,d;\mathbb{Z})$（标准 T 对偶群为 O(d,d;ℤ)）。与原文不一致但数学更标准，**未改**，请 Lead 定夺。
- **ch01-1.1.4-013 / ch01.tex L270**：英文仅 "Equivalently, one requires ker ω_M to be an integrable distribution on M"；译文多出"$\ker\omega_M$ 的秩等于 $M$ 在 $X$ 中的余维数；在此情形下"一句。数学正确（余各向同性子流形的 $\ker\omega_M=(TM)^{\omega}$ 维数确等于余维数），属译者补充的等价性说明，未删（若从严按"多出内容"处理可删去该分句）。
- **ch01-1.2.1-001/002 / ch01.tex L345、L348**：英文 "isotopy classes of Lagrangians"，译文作"Hamilton 同痕类"（两处一致）。Floer 理论中标准对象本为 Hamiltonian 同痕类，译者加了"Hamilton"，未改。
- **ch01-1.3-011 / ch01.tex L440**：英文仅括注 "(technically, the Virasoro operator L0 + L̄0)"；译文展开成"选定时间单位，并除去与态无关的真空能量平移后，这个算符由 Virasoro 算符 $L_0+\overline{L}_0$ 给出"，增加了"选单位/减去真空能量平移"两点说明（数学上正确）。属对同一括注的展开解释，未删，供 Lead 判断是否从简。
- **ch01-1.3-011 公式 (1.6)(1.7) 与 $H$ / ch01.tex L441-L453**：原文 (1.7) 为 $L^2=\sum g_{ij}w^iw^j$、$H=\Delta_g+L^2+\cdots$；译文取 $L^2=(2\pi)^2\sum g_{ij}w^iw^j$、$H=\Delta_g+L^2/(2\pi)^2+\cdots$。已核算：两者给出的 $H$ 完全一致（译文的 $L^2$ 只是把 $X\sim X+2\pi$ 归一化下测地线长度平方的 $(2\pi)^2$ 显式写出），(1.6) 用 $g^{ij}$ 与 Laplacian 谱一致，自洽且数学正确，**不改**。
- ch01-1.3.2-003 / L491-493：英文 "According to McLean's theorem (§6.1.1)" 译作"根据 McLean 定理，见\BookSectionRef{sec:6.1.1}{6.1.1}"，指向正确，括注改为正文插入语属合理处理，未改。

## Lead 裁决（2026-11-14，逐条回复，均不再改动）

1. ch01-1.1.4-009 $n=\dim_{\mathbb C}X$：**保留译文**。原书 "Let n = dim_ℝ M" 与同节 (4) "$r+n=\dim_{\mathbb R}M$" 自相矛盾，只在 n=dim_C X 时成立 → 原文疑误，译文按数学自洽处理是正确的。
2. ch01-1.3-008 $\operatorname{O}(d,d;\mathbb Z)$：**保留 O**（T 对偶标准群），与原文 SO 的偏差属有意修正。
3. ch01-1.1.4-013 "$\ker\omega_M$ 的秩等于余维数"：**保留**，属可保留的译注（正确且不改变原意）。
4. "isotopy classes"→"Hamilton 同痕类"：保留（与全书术语一致）。
5. "(technically, L0+L̄0)" 的展开：保留。
6. 公式 (1.6)(1.7)/$H$：不改，已自洽。
7. "special holonomy"→"特殊完整群"：保留（与 glossary 一致）。
8. 改动 #3（删 Thomas–Yau 整句）：**维持删除**（GUIDE P1：不得多出原文没有的内容）。

→ 结论：本轮 6 处改动全部维持，无回退；7 条待确认项按上述裁决归档，ch01/preface 校对闭环。
