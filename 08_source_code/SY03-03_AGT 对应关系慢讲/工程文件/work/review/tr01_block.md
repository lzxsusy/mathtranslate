# tr-01 块交叉校对报告（原文 pp.12–24）

校对者：tr-02　｜　校对对象：`work/src/chunks/tr01a.tex`(pp.12–15)、`tr01b.tex`(pp.16–19)、`tr01c.tex`(pp.20–24)
底本：`work/pages/p012.png … p024.png`（200 dpi 逐页）、`work/tools/crop.py` 放大裁图（500–1100 dpi）、`work/split/p012.txt … p024.txt`、`work/tags_bypage.txt`、`work/glossary.tsv`
**未修改任何 tr-01 文件**，本报告只列问题与改法。

---

## 0. 结论摘要

- **编号公式：15 条全部到位、与 `tags_bypage.txt` 逐页对应、无自造编号、无遗漏**（2.1、3.1–3.14）。§2 只有 (2.1)，`tr01a.tex` 的 `equation` 环境数 = 1，确认未给 §2 的无编号公式自造编号。
- **公式逐符号核对：15 条全部核对（远超要求的 ≥8 条），未发现任何符号/上下标/指标/符号字体错误**。其中 (3.7)(3.9)(3.13) 三条最长，单独放大复核。
- **结构：§2 的 2.1–2.4 四个 `\subsection` 位置正确（p.13/14/15/18）；Table 2 五行四列数据与原表逐格一致；Figure 2 用 `fig2.png` + `\figtitle{2}{…}` 且图注逐句对应；p.12 与 p.19 两个要点框完整译出。**
- **漏译：无**。pp.12–24 的全部正文段落、13 条脚注（原编号 14–26）、4 个习题（2.1、2.2、3.1、3.2）均已覆盖；与 `c01.tex` 的 p.12 边界无重复、无缺口。
- **术语：与 glossary 一致**；仅个别术语建议全书统一（见 §6 可选改）。
- **必须改：1 处**（`tr01b.tex` L119 要点框内的语法错误）。其余为可选/版式级建议。
- **附带发现并已修复 tr-02 自己的一处跨块重复**：p.24→p.25 的跨页句由 tr-01 正确写完，但 tr-02 的 `tr02a.tex` 开头原先仍带着该句在 p.25 的残片「在该规范群下带电的粒子。」，会重复。**已由本报告作者直接修正 `tr02a.tex`（不涉及 tr-01 文件）**，详见 §7.3。**这一条不影响 tr-01 的校对结论。**

---

## 1. 编号公式完整性核对

| 原文页 | tags_bypage 要求 | tr01 文件·位置 | 结果 |
|---|---|---|---|
| p.13 | 无 | tr01a 无 `equation` | ✅ 未造编号 |
| p.14 | 2.1 | tr01a L78–81 | ✅ |
| p.15 | 无 | tr01a 无 `equation` | ✅ |
| p.16–p.19 | 无 | tr01b 无 `equation`（`equation` 环境数 = 0） | ✅ |
| p.20 | 3.1 | tr01c L9–12（在 `% [原文 p.20]` 与 p.21 标记之间） | ✅ |
| p.21 | 3.2, 3.3, 3.4, 3.5, 3.6 | tr01c L33–74（均在 p.21 标记之后） | ✅ 五条齐全、顺序正确 |
| p.22 | 无 | tr01c 无 | ✅ |
| p.23 | 3.7, 3.8, 3.9, 3.10, 3.11, 3.12 | tr01c L99–161 | ✅ 六条齐全 |
| p.24 | 3.13, 3.14 | tr01c L167–179 | ✅ |

**汇总：** 15 个 `\tag{}`，`equation` 环境 15 个（tr01a 1 + tr01c 14），数量与内容一一对应；全文 **0 处 `\ref`/`\eqref`**（引用公式全部写成纯文本括号），**0 处自造编号**。原文 §2 的大量无编号公式（如 `dH = ddB = 0`、`(R^N)^5/S_N`、`g_{5d} ∼ L_5^{1/2}`、`Γ^{012345}ε = ε` 等）在译文中均按行内公式处理，**未擅自编号**——符合 STYLE_GUIDE §3。

---

## 2. 公式逐符号核对（15 条全查）

核对方式：`crop.py` 从原 PDF 裁出公式区（500–1100 dpi）→ `read_image` 放大 → 与译文逐字符比对（含指标位置、上下标、花体/直立体、正负号、括号配对）。

| 式号 | 页 | 核对要点（逐条看过） | 结果 |
|---|---|---|---|
| **(2.1)** | p.14 | `H_{α_0α_1…α_k} := (k+1)! ∂_{[α_0}B_{α_1…α_k]} = ±i^{d/2+s}ε_{α_0…α_kβ_0…β_k}∂^{[β_0}B^{β_1…β_k]}`：`(k+1)!` 前缀、两侧下标串长度、`i` 的指数 `d/2+s`、`±`、方括号只套在 `β` 上（`∂^{[β_0}B^{β_1…β_k]}`）——全部一致 | ✅ |
| (3.1) | p.20 | `δℒ = Tδg + JδA = Tδg − J∂(δg) ≃ (T+∂J)δg`：三项符号与最后一个 `≃` 一致 | ✅ |
| (3.2) | p.21 | `so(1,3) × so(2)_twist × so(3)_R`（三个因子、下标 twist/R 的位置） | ✅ |
| (3.3) | p.21 | `T^{μν}_twist = T^{μν}_old + ¼(ε^{μρ}∂_ρJ^ν_{12} + ε^{νρ}∂_ρJ^μ_{12})`：`¼`、两项指标 `μρ/νρ` 对称、`J` 的上标 `ν/μ` 与下标 `12`——逐字符一致 | ✅ |
| (3.4) | p.21 | 两行：`(4,4) = ((2,1)_{1/2}⊕(1,2)_{−1/2})⊗(2_{1/2}⊕2_{−1/2}) = (2,1,2)_{1/2,1/2}⊕(2,1,2)_{1/2,−1/2}⊕(1,2,2)_{−1/2,1/2}⊕(1,2,2)_{−1/2,−1/2}`：⊗ 与 ⊕ 未混用、四个双下标符号逐个核对 | ✅ |
| (3.5) | p.21 | `(2,1;2)_1 ⊕ (2,1;2)_0 ⊕ (1,2;2)_0 ⊕ (1,2;2)_{−1}`：分号用法与四个 twist 电荷 `+1,0,0,−1` | ✅ |
| (3.6) | p.21 | `Q^{αA}_z, Q^{αA}, Q̄^{α̇A}, Q̄^{α̇A}_{z̄}`：放大确认**第 4 个是 `\bar Q` 带下标 `\bar z`**（不是 `\tilde`），且第 1 个的下标是 `z` 而非 `z̄` | ✅ |
| **(3.7)** | p.23 | 4 行 2 栏（左：`B, λ, Φ_8Φ_9Φ_{10}`；右：`Φ_z, Φ_z̄`）。逐项核对 `(3,1,1)_{0,0}⊕(1,3,1)_{0,0}⊕(2,2,1)_{±1,0}⊕(1,1,1)_{0,0}`、`(2,1,2)_{½,±½}⊕(1,2,2)_{−½,±½}`、`Φ_z := Φ_6+iΦ_7 ∈ (1,1,1)_{0,1}`、`(1,1,3)_{0,0}`、`Φ_z̄ := Φ_6−iΦ_7 ∈ (1,1,1)_{0,−1}`；**栏位对齐也照原图**（`Φ_z` 与 `λ` 同行、`Φ_z̄` 与 `Φ_8` 同行） | ✅ |
| (3.8) | p.23 | `Q̄^{α̇A}Φ_z = 0` | ✅ |
| **(3.9)** | p.23 | 两行 `gathered`：`Tr(Φ^j_z), j=2,3,4,…,N`（su(N)）与 `Tr(Φ^j_z), j=2,4,6,…,2N−2, and Pfaff(Φ_z)`（so(2N)）；`2N−2`、`Pfaff` 拼写（原式即 `Pfaff` 非 `Pfaffian`） | ✅ |
| (3.10) | p.23 | `det(X − Φ_z dz) = X^N − Σ_{j=2}^{N} O_j X^{N−j}`：求和上下限 `j=2`、`N`，`X^{N−j}` | ✅ |
| (3.11) | p.23 | `φ_j := ⟨O_j⟩`（`:=` 与尖括号） | ✅ |
| (3.12) | p.23 | `ε^{α̇β̇}ε^{AB}∂_{z̄}φ_j ∼ ⟨Q̄^{α̇A}(Q̄^{β̇B}_{z̄}O_j)⟩ + ⟨Q̄^{β̇B}_{z̄}(Q̄^{α̇A}O_j)⟩ = 0`：两个 ϵ 的指标 `α̇β̇/AB`、两个期望值中 `Q̄` 与 `Q̄_{z̄}` 的**次序相反**（原图如此）、`∂_{z̄}` 的下标 | ✅ |
| **(3.13)** | p.24 | 放大确认左端是**花体 ℬ**（`\cB`），非 𝒞；`⊕_{k=1}^{r}` 的上下限；`H^0(C, K^{⊗d_k})` 中 **⊗ 显式存在**、指数是 `d_k`（下标 k）；右半 `φ_j ∈ H^0(C, K^{⊗j})` 用 `j` 而非 `d_k`——与原文完全一致 | ✅ |
| (3.14) | p.24 | `F + [φ, φ̄] = 0,  ∂̄_Aφ = 0,  ∂_Aφ̄ = 0`：放大确认字母是 **`\varphi`（φ）而非 `\phi`**，第一条是 `[φ,φ̄]` 交换子、第二三条 `∂̄_A/∂_A` 方向相反 | ✅ |

**行内公式抽查（另 12 处）**：`so(2,3)=sp(4,R)`、`so(2,4)=su(2,2)`、`so(2,6)=so*(8)`（p.13）；`(8_s,4)`、`so(6,2)×so(5)_R`（p.13）；`usp(4)=so(5)`、`∫ε^{μνρσ}F_{μν}F_{ρσ}d^4x`（p.14）；`F_{μν}=∓½ε_{μνρσ}F^{ρσ}`、`F=dA+A∧A`、`ε^{λμνρ}D_μF_{νρ}=0`、`D_μF^{μλ}=0`（p.15）；`(z,w)↦(e^{2πi/N}z, e^{−2πi/N}w)`（p.17）；`Γ^{012345}ε=ε`、`Γ^{23456789}ε=ε`（p.19）。以上均与图像一致。

---

## 3. 结构核对

| 项目 | 原文位置 | 译文位置 | 结果 |
|---|---|---|---|
| `\part{第一篇\quad Class S 理论}` | p.12 | tr01a L6 | ✅ 与 BRIEF 指定写法逐字一致 |
| `\section` §2「6d (2,0) SCFT of ADE type」 | p.12 | tr01a L8 | ✅ |
| `\subsection` 2.1 Superconformal algebras | **p.13** | tr01a L55 | ✅ 在 `% [原文 p.13]` 之后 |
| `\subsection` 2.2 Self-dual forms | **p.14** | tr01a L73 | ✅ 在 p.14 标记之后 |
| `\subsection` 2.3 Brane construction of 6d theories | **p.15** | tr01a L130 | ✅ 在 p.15 标记之后（原文页末） |
| `\subsection` 2.4 Codimension 2 and 4 defects | **p.18** | tr01b L54 | ✅ |
| `\section` §3「Class S theories from 6d」 | p.19 | tr01b L115 | ✅ |
| `\subsection` 3.1 Partial topological twist | p.20 | tr01c L2 | ✅ |
| `\subsection` 3.2 Coulomb branch | p.22 | tr01c L88 | ✅（块边界在 (3.14) 止，未越界到 3.2 之后） |
| **Table 2**（p.13） | p.13 | tr01a L30–45 | ✅ 见下 |
| **Figure 2**（p.19） | p.19 | tr01b L88–92 | ✅ 见下 |
| **p.12 要点框** | p.12 | tr01a L19–25 | ✅ 见下 |
| p.19 要点框 | p.19 | tr01b L117–125 | ✅ 五条要点全译 |
| 脚注 14–26（13 条） | pp.12–23 | tr01a 7 + tr01b 4 + tr01c 2 | ✅ 内容逐条对应 |
| 习题 2.1 / 2.2 / 3.1 / 3.2 | p.15 / p.19 / p.21 / p.23 | tr01a / tr01b / tr01c / tr01c | ✅ 编号与题文齐全 |

**Table 2 逐格核对**（裁 p.13 表区 800 dpi 放大后与原表比对）：

| 行 | 超代数 | 共形代数 | R 对称代数 | Q&S | 结果 |
|---|---|---|---|---|---|
| 3d N≤8 | osp(N\|4) | sp(4,R) | so(N) | (4,N) | ✅ |
| 4d N≤3 | su(2,2\|N) | su(2,2) | su(N)⊕u(1) | (4,**N̄**)⊕(**4̄**,N) | ✅ 上划线齐全 |
| 4d N=4 | psu(2,2\|4) | su(2,2) | su(4) | (4,**4̄**)⊕(**4̄**,4) | ✅ |
| 5d N=1 | **f²(4)** | so(2,5) | su(2) | (8,2) | ✅ 原表确为 `f²(4)`（superscript 2），译文照抄并加批注 |
| 6d N≤2 | osp(8*\|2N) | so*(8) | usp(2N) | (8,2N) | ✅ |

列数 5（首列空表头）与原表一致；`\toprule/\midrule/\bottomrule` 位置与原表的三条横线一致（原表在 M5 与 M5' 行之间无横线，本表亦无——见下）。

**Figure 2**：`\includegraphics[width=0.45\textwidth]{fig2.png}` + `\figtitle{2}{…}`；`fig2.png` 已确认就是原 Figure 2（两族 M5 膜融合的复流形）；图注四句逐句对应，并正确处理了 "depicted horizontally/vertically"。

**p.12 要点框「Properties of X(g)」**：三条要点全部译出且语义完整（① IR 为 Cartan 中取值的阿贝尔自对偶二形式理论、模 Weyl 群；② 作为 5d N=2 SYM 的 UV 完备，半径 `g²_{5d}`；③ 余维 2 缺陷由幂零轨道标记、余维 4 由表示标记）。译者在框前加了一句说明（原文 "properties detailed to the right" → "详见下方要点框"），并留批注解释版式原因——**做法正确**。

**p.18 膜构型表**：`\begin{tabular}{l*{11}{c}l}`，13 列 = 1 标签 + 11 个坐标方向 + 1 箭头列，三行数据逐格核对（M5: `0 1 2 3 4 5 · · · · ·`；M5': `0 1 2 3 · · 6 7 · · ·`；M2: `0 1 · · · · · · · · 10`），**与原表完全一致**（含 x^{10} 在第 11 列）。

---

## 4. 漏译检查（pp.12–24 逐页）

逐页把 `split/pNNN.txt` 的段落/脚注/习题与译文对表，**全部覆盖，无整段遗漏**：

- p.12：§1 末段尾巴在 `c01.tex`（`c01` 尾部确有该段，tr01a 从头起写，**无重复、无缺口** ✅）；Part I、§2 标题、首段、要点框、"Despite its stringy construction…" 段、后续两段 —— 齐。
- p.13：Table 2 + 表题、"In this section we describe…" 段、2.1 标题与三段、"Supercharges of this algebra…"（跨到 p.14）—— 齐。
- p.14：2.2 标题、导语段、`\para{Abelian self-dual forms.}` 全段、(2.1)、三条说明段、`\para{Compactifying on a circle.}` 段、p.14 末句 —— 齐。
- p.15：KK 模段、Exercise 2.1（3 小问）、`\para{Nonabelian theory.}` 全段、2.3 标题、小弦理论段、第一条 bullet、脚注 20 —— 齐。
- p.16：第二条 bullet、"These approaches teach us…"、`\para{Fivebranes in IIA or M-theory.}` 两段、术语评注段、ABJM bullet、脚注 21/22/23 —— 齐。
- p.17：ABJM 收尾、M5 bullet、"Consequences of the M-theory construction" 两段、`\para{IIB strings.}`、"As understood in [163]…"、"Moving along the vacuum moduli space…"、脚注 24 —— 齐。
- p.18：p.17 末段的续句、SO(4) 段、2.4 标题、膜表、表后说明段、M2 段、"The way it is written here…"、两处 bullet 的第一条 —— 齐。
- p.19：Figure 2 + 图注、第二条 bullet、Exercise 2.2、§3 标题、要点框、"Our next task…" —— 齐。
- p.20：3.1 标题、导语段、`\para{Generalities on topological twist.}` 全段、(3.1)、4 个说明段 —— 齐。
- p.21：(3.1) 之后 "In the second step…"、拓扑扭曲重定义段、能动张量职责段、超荷段、TQFT 收尾、`\para{Partial topological twist of 6d theories.}`、(3.2)(3.3)、ϵ 定义、Exercise 3.1、超对称追踪段、(3.4)(3.5)(3.6) —— 齐。
- p.22：α,α̇,A 指标说明段、中间两个超荷段、零尺寸极限段 + 脚注 25、3.2 标题、Coulomb 分支算子段、"Importantly…" 段、"General supersymmetry considerations…" 段、`\para{Coulomb branch operators.}` 段头 —— 齐。
- p.23：(3.7) 上下文、`Q̄` 断言的推理句、"Really, we should be working with…" 段、(3.9)、Casimir 阶数句、全纯微分段、(3.10)、Exercise 3.2、`\para{Coulomb branch.}`、(3.11)、反交换子推导、(3.12)、脚注 26 —— 齐。
- p.24："The first term vanishes…" 段、(3.13)、K 与 H^0 说明段、`\para{Hitchin system.}` 两段 + (3.14)、`\para{Comment on the IR behaviour.}` 两段 —— 齐（块末句起于 p.24、收于 p.25 首行，译文已写完该句并留边界批注 ✅）。

---

## 5. 术语一致性（对照 glossary）

| 英文 | glossary | tr01 用法 | 结果 |
|---|---|---|---|
| puncture | 穿刺点 | 穿刺点 | ✅ |
| tinkertoy | tinkertoy（保留） | tinkertoy | ✅ |
| Coulomb branch / Higgs branch | Coulomb 分支 / Higgs 分支 | 同 | ✅ |
| hypermultiplet / tensor multiplet / vector multiplet | 超多重态 / 张量多重态 / 矢量多重态 | 同 | ✅ |
| nilpotent orbit | —（新） | 幂零轨道 | ✅ 一致 |
| little string theory | 小弦理论 | 小弦理论 | ✅ |
| ALE space | ALE 空间（渐近局部欧氏） | ALE 空间 | ✅ |
| orbifold | 轨形（orbifold） | 轨形 / 轨形化 | ✅ |
| resolution | 消解 | 消解 | ✅ |
| Young diagram | 杨图 | 杨图 | ✅ |
| partition（整数分拆） | 分拆 | 分拆 | ✅ |
| canonical bundle / line bundle | —（新） | 典范丛 / 线丛 | ✅ |
| superconformal algebra | —（新） | 超共形代数 | ✅ |
| improvement transformation | —（新） | 改进变换（首现注英文） | ✅ |
| class S / SCFT / BPS / SYM / QFT / VEV / ABJM | 保留 | 保留 | ✅ |

未发现同一术语在 tr01 内部出现两种译法（"轨形化"与"轨形"是动词/名词之别，可接受）。

---

## 6. 问题清单

### 6.1 必须改（1 处）

**M1. `tr01b.tex` L119（§3 要点框第 1 条）：语法错误「（带一个扭曲地）约化」**

- 原文（p.19）："Reducing (with a twist) the 6d theory $\cX(\fg)$ on a punctured Riemann surface $C$ gives a 4d $\cN=2$ theory."
- 现状：`\item 把 6d 理论 $\cX(\fg)$（带一个扭曲地）约化在带穿刺点的黎曼面 $C$ 上，就得到 4d $\cN=2$ 理论。`
- 问题：「地」被关在全角括号里，全句读不通（"带一个扭曲地"不成词）。
- 改法（任选一）：
  1. `把 6d 理论 $\cX(\fg)$ 带一个扭曲地约化在带穿刺点的黎曼面 $C$ 上，就得到 4d $\cN=2$ 理论。`
  2. `把 6d 理论 $\cX(\fg)$（带一个扭曲）约化在带穿刺点的黎曼面 $C$ 上，就得到 4d $\cN=2$ 理论。`
  3. `把 6d 理论 $\cX(\fg)$ 作一个扭曲后约化在带穿刺点的黎曼面 $C$ 上，就得到 4d $\cN=2$ 理论。`
  推荐 3（中文最顺，且 "with a twist" 的语义不丢）。

### 6.2 可选改（8 处，不影响正确性）

**O1. 列表跨文件断裂（tr01a L134–136 ↔ tr01b L2–4；tr01b L83–85 ↔ L94–96）**
原文 p.15→p.16 的**同一个** itemize（两条 bullet）在译文里被文件边界切成两个 `itemize`，编译后第二条 bullet 会多出一段列表间距。p.18–19 那一处中间夹着 Figure 2 浮体，保持现状即可（LaTeX 本来也无法在 itemize 内插浮动图）。
改法（任选）：① 把 tr01a 末尾的 `\end{itemize}` 移到 tr01b 第二条 bullet 之后（即 tr01a 结尾不闭合、tr01b 开头直接 `\item`，仅靠合成后的文件才平衡）；② 由 Lead 合成时手工合并这两段。

**O2. `\part` 会渲染出双重编号（tr01a L6）**
`\part{第一篇\quad Class S 理论}` 在 article 类下会印出两行：「Part 1」+「第一篇　Class S 理论」——"Part" 与「第一篇」语义重复。
改法：若希望只留中文，写 `\part{Class S 理论}`（自动的 "Part 1" 充当编号）；若接受现状也可读。**共 3 处 `\part`（tr01/tr03/tr05），建议 Lead 一次性裁定。**

**O3. Table 2 表题位置（tr01a L44）**
原文表题在表**上方**；`\tabtitle{2}{…}` 写在 `\bottomrule` 之后，渲染在表**下方**。若追求贴近原版式，把 `\tabtitle{2}{…}` 移到 `\toprule` 之前即可（`\caption*` 在 table 浮体内放上方/下方都合法）。

**O4. 「我们断言」vs 原文 "We deduce that"（tr01c L110）**
`(3.8)` 前一句原文是 "We deduce that"，"断言"（assert）语义偏强，建议改「我们由此推断」或「因此得出」。

**O5. 公式引用格式全书统一（tr01 全文，如 L92/L166/L196 的「(3.13)」）**
tr01 一律用裸括号「(3.13)」，而 STYLE_GUIDE §3 的示例是「式 (3.13)」。建议 Lead 定一个全书口径（注意：tr-02 自己的块里也是混用的），统一后再全书替换。

**O6. `tr01a.tex` L82–90 批注可补半句**
该批注已正确指出「原文 $k!$ 应为 $k$」并推出 $(\dd\Lambda)_{\alpha_1\dots\alpha_k}=k\,\partial_{[\alpha_1}\Lambda_{\alpha_2\dots\alpha_k]}$，但没点明**原文同一句的 "for any $k$-form $\Lambda$" 也是笔误**（若 $\Lambda$ 是 $k$-形式，$\dd\Lambda$ 就是 $(k+1)$-形式，与“给 $B_{\alpha_1\dots\alpha_k}$ 加上…”矛盾；应为 $(k-1)$-形式）。建议在批注里加一句点明，正文仍照译（符合 §9.1）。

**O7. 两个脚注的挂点（tr01a L10）**
`…说“标记。”\footnote{…}\textsuperscript{,}\footnote{…}` 把 14、15 两个标记挂在**句号之后**，原文挂在 "simply-laced" 上。内容无误；若要版式更贴原书，可把这两个 `\footnote` 移到「（simply-laced）」之后。另注：`\textsuperscript{,}` 是可行但略 hack 的写法，编译后应抽查是否印成「¹⁴,¹⁵」。

**O8. 术语「二闭链」（tr01b L41 起，two-cycle）**
glossary 未收，tr01 用「二闭链」。建议 Lead 在 glossary 里补一条并统一（备选：二维闭链 / 二圈）。同类待补术语：典范丛、线丛、超共形代数、改进变换、幂零轨道、相对量子场论。

---

## 7. 顺带核对到的跨块一致性（供 Lead 参考）

1. **脚注编号自洽**：`c01.tex` 有 **13** 条 `\footnote`，而原文 p.12 起首条脚注是 **14** —— 编号正好接上 ✅。这意味着 pp.1–11 的 13 条脚注必须一条不漏（我抽查了 c01 的脚注内容与原文 p.1–11 的编号逻辑，未发现缺号）。**建议编译后抽查一次正文脚注号是否出现偏移**（任何一块漏一条，其后全部脚注号都会错位）。
2. **p.12 边界干净**：`c01.tex` 结尾正是原文 p.12 顶部两行（"…is the right one for some readers. I apologize…topological strings."），tr01a 从 `\part` 起写，无重复句 ✅。
3. **p.24/p.25 边界（发现并已修复 tr-02 侧重复）**：原文最后一句起于 p.24 "At particular points on the Coulomb branch there are additional massless"、收于 p.25 "particles charged under this gauge group."。**tr-01 按「跨页句开始者写完」把整句写完了**（tr01c 末句："在 Coulomb 分支的特定点处还有额外的无质量粒子，它们带这个规范群的荷。"）——**做法正确**。但 tr-02 的 `tr02a.tex` 开头原本仍带着 p.25 的残句「在该规范群下带电的粒子。」，会造成重复。**该重复已在本次校对中由 tr-02 修正**（tr02a.tex L4 现从 "Coulomb 分支通常还带有一些更为奇异的点…" 起）；tr-02 侧 tag/页标注自检重跑通过。请 Lead 合成后确认该处只出现一次。
4. **编号公式首尾衔接**：tr-01 止于 (3.14)，tr-02 起于 (3.15) ✅（已在 tr-02 侧核对）。

---

## 8. 校对方法与可复现性

- 编译前静态检查：`python work/tmp/check.py <file>`（BOM/CRLF、花括号与 `$` 配对、`\begin/\end` 配对、tag 清单、`% [原文 p.N]` 清单、Tutor Note 计数、禁用命令）。tr01 三文件结果：括号平衡、`$` 成对、环境闭合、无禁用命令、无 U+FFFD、**0 处 `\ref`**。
- 公式核对：`python work/tools/crop.py <页> <x0> <y0> <x1> <y1> <out>.png [dpi]`，dpi 取 700–1100；裁图存于 `work/tmp/r_*.png`（如需复查可直接看这些图）。
- 本次裁图清单（供 Lead 复核）：`r_313.png`(3.13)、`r_314.png`(3.14)、`r_35.png`(3.4 局部)、`r_36.png`(3.6)、`r_33.png`(3.3)、`r_eps2.png`(ϵ 定义)、`r_table2b.png`(Table 2)。
