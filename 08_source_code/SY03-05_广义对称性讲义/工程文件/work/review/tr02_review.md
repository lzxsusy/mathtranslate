# tr-02（原文 pp.29–44，tag 3.7–3.107）交叉校对报告

校对者：tr-01　　校对日期：2026-11-04
受校文件：`work\src\chunks\tr02a.tex`（pp.29–33）、`tr02b.tex`（pp.34–39）、`tr02c.tex`（pp.39–44）
**本报告只提出问题，未改动 tr-02 的任何文件。**

## 0. 校对方法与证据等级

| 手段 | 说明 | 可信度 |
|---|---|---|
| PyMuPDF 字形探针 | 直接读原 PDF 每个 span 的**字体名**（`LMSans10` / `LMMathItalic10` / `LMMathSymbols10` / `MSBM10`）与 `origin_y`，可判定正体/斜体/花体/无衬线、上标/下标 | 最高（机器读出，非目视） |
| `crop.py` 裁图 | 指定 8 条必查式按 **800–900 dpi** 裁原图目视复核 | 高 |
| PyMuPDF 矢量绘图探针 | 读原 PDF 方框的 fill/stroke RGB 与包围盒，判定方框类型（橙色 Example / 绿色 Definition / 粉色 Note）与被夹点 | 最高 |
| 文字层对比 | `work\split\pNNN.txt` 逐页对照查漏译 | 中（数学不可信，仅用于词句/结构） |
| 脚本体检 | tag 清单/连续性、编码、环境配对、`$` 配对、禁项、整句英文残留 | 机械 |

## 1. 结论摘要

- **编号公式 101 条（3.7–3.107）齐全、连续、无重复、无自造**，与 `tags_bypage.txt` 逐页一致（p.43 原文无编号式，tr02c 亦无）。
- **公式逐符号核对 48 行（覆盖约 60 条编号式，含全部指定必查式 3.14/3.17/3.26/3.55/3.75–3.78/3.87/3.107），发现 1 处实质抄写错误：(3.101) 的圆盘应为下标 `D_2`，tr02c 写成上标 `D^2`。**
- **另 1 处必须改：全书 `D_p` 用字错误**——原文是**无衬线** `\mathsf{D}`（PDF 字体名 `LMSans10`，裁图目视亦确认），tr02a/b/c 共 **28 处**写成 `\mathrm{D}`；tr-01（9 处）与 tr-08（39 处）用的 `\mathsf{D}` 才是对的，tr-03 也有同样问题（24 处）。
- 结构（标题层级、9 个 examplebox + 1 个 definitionbox + 3 个 notebox 的类型与编号、方框跨页合并）、图 9/10/11 编号与图注、`\para` 行内小标题、强调（bold/italic）**全部正确**，未发现漏译、漏脚注。
- 边界：tr02a 开头与 tr-01 p.28 衔接无重复无缺口；tr02c 结尾 (3.107) 与 tr-03 的 (3.108) 衔接正确；p.38/39 例 3.9 方框**无重复、无丢失**。
- **「必须改」3 条**（M1 全书 D 字形 28 处；M2 (3.101) 下标；M3 与 M2 连带的批注事实错误），**「可选改」8 条**（图幅 2、标点 2、批注措辞 2、术语统一 1、排版 1）。

## 2. 编号完整性表

| 项 | 结果 |
|---|---|
| tag 总数 | **101**（tr02a 35 + tr02b 37 + tr02c 29）= 3.107−3.7+1 = 101 ✔ |
| 首/末 | 3.7（tr02a L5）/ 3.107（tr02c L194）✔ 首接 tr-01 的 3.6、末接 tr-03 的 3.108 ✔ |
| 缺号 | 0（脚本按页比对 `tags_bypage.txt`，pp.29–42、44 逐页吻合；p.43 原文无编号式，文件内亦无 `\tag`）✔ |
| 重号 | 0 ✔ |
| 自造号 | 0 ✔ |
| 多行公式单 tag | (3.51)、(3.68) 用 `align`+`\nonumber`，仅末行 `\tag`，与原文一致 ✔ |

逐页对照（原文/文件，两栏一致）：

| 页 | tags_bypage | 文件内实际 | 一致 |
|---|---|---|---|
| 29 | 3.7–3.10 | 3.7,3.8,3.9,3.10 | ✔ |
| 30 | 3.11–3.17 | 3.11…3.17 | ✔ |
| 31 | 3.18–3.24 | 3.18…3.24 | ✔ |
| 32 | 3.25–3.33 | 3.25…3.33 | ✔ |
| 33 | 3.34–3.41 | 3.34…3.41 | ✔ |
| 34 | 3.42–3.48 | 3.42…3.48 | ✔ |
| 35 | 3.49–3.53 | 3.49…3.53 | ✔ |
| 36 | 3.54–3.62 | 3.54…3.62 | ✔ |
| 37 | 3.63–3.67 | 3.63…3.67 | ✔ |
| 38 | 3.68–3.74 | 3.68…3.74 | ✔ |
| 39 | 3.75–3.82 | 3.75…3.82 | ✔ |
| 40 | 3.83–3.89 | 3.83…3.89 | ✔ |
| 41 | 3.90–3.97 | 3.90…3.97 | ✔ |
| 42 | 3.98–3.102 | 3.98…3.102 | ✔ |
| 43 | （无） | （无） | ✔ |
| 44 | 3.103–3.107 | 3.103…3.107 | ✔ |

## 3. 逐符号核对表

证据：**字体探针**（F）= PyMuPDF span 字体名/坐标；**裁图**（C）= `crop.py` 800–900 dpi 目视。

| 式号 | 页 | 原文（探针/裁图读出） | tr-02 现状 | 判定 |
|---|---|---|---|---|
| 3.7 | 29 | `Q(O_p)=[O_p]∈D_p`，D 为 **LMSans10（无衬线）** | `Q(\cO_p)=[\cO_p]\in \mathrm{D}_p` | ✘ D 字形错（M1） |
| 3.8 | 29 | `D_1=Z,  D_{d−3}=Z.`，D 亦 LMSans10 | `\mathrm{D}_1=\Z,\quad\mathrm{D}_{d-3}=\Z` | ✘ 同上 |
| 3.11 | 30 | `A(x)→A(x)−dθ(x)/2π`（d 为斜体） | `A(x)\to A(x)-\frac{\dd\theta(x)}{2\pi}` | ✔（`\dd` 为工程约定，见注 A） |
| 3.12 | 30 | `ϕ(x)→e^{iqθ(x)}ϕ(x)`（e 斜体） | `\phi(x)\to\ee^{iq\theta(x)}\phi(x)` | ✔ |
| **3.14** | 30 | 裁图确认：`𝒲_q(L)=exp(2πiq∫_L A)→exp(−iq∫_{∂L}dθ)𝒲_q(L)=e^{−iqθ(x)}𝒲_q(L).` | 同左（`\cW_q`、`\dd\theta`、`\ee^{-iq\theta(x)}`） | ✔ |
| 3.15 | 30 | `ϕ(x)𝒲_q(L).` | `\phi(x)\cW_q(L)\,.` | ✔ |
| 3.16 | 30 | `𝒲_p∼𝒲_{p+nq},  ∀p∈Z.` | 同左 | ✔ |
| **3.17** | 30 | `D_1=Z/qZ≡Z_q`（**分式** Z 在 qZ 上；D 无衬线） | `\mathrm{D}_1=\frac{\Z}{q\Z}\equiv\Z_q` | 结构 ✔／D 字形 ✘（M1） |
| 3.18 | 31 | `G^{(1)}=D̂_1≅Z_q.` | `G^{(1)}=\widehat{\mathrm{D}}_1\cong\Z_q` | 同上 |
| **3.19** | 31 | 裁图确认：`U_n^{(e)}(Σ_{d−2})=exp((2πin/q)∫_{Σ_{d−2}}⋆F), n∈{0,1,···q−1}.`（2πin 在 q 上，**堆叠分式**） | `U_n^{(e)}(\Sigma_{d-2})=\exp\!\left(\frac{2\pi i n}{q}\int_{\Sigma_{d-2}}\star F\right), n\in\{0,\dots,q-1\}` | ✔ |
| **3.26** | 32 | `q_Φ=1`（**无**句末标点） | `q_\Phi=1` | ✔ |
| 3.30 | 32 | `(2π/q)∫a_1∪δb_{d−2}.` | `\frac{2\pi}{q}\int a_1\cup\delta b_{d-2}` | ✔ |
| 3.33 | 32 | `L=(v²/2)(dα−qA)∧⋆(dα−qA).` | `\mathcal{L}=\frac{v^2}{2}(\dd\alpha-qA)\wedge\star(\dd\alpha-qA)` | ✔ |
| 3.34 | 33 | `L=(q/2π)B∧dA.` | `\mathcal{L}=\frac{q}{2\pi}B\wedge \dd A` | ✔ |
| 3.43 | 34 | `G^{(1)}=Ẑ_{gcd(q_Φ,q_ψ)}=0.` | `G^{(1)}=\widehat{\Z}_{\gcd(q_\Phi,q_\psi)}=0` | ✔ |
| 3.45 | 34 | `Q_matter:=Span_Z{Q_1,Q_2,···,Q_m}.`（Span 正体、下标 Z） | `Q_{\mathrm{matter}}:=\mathrm{Span}_{\Z}\{Q_1,\dots,Q_m\}` | ✔ |
| 3.48 | 34 | `diag(q_1^D,···,q^D_{min(m,r)})⊂SNF(Q),` | 同左 | ✔ |
| 3.49/3.50 | 35 | `D_1=∏_{i=1}^{min(m,r)}Z_{q_i^D},`／`G^{(1)}=∏ Ẑ_{q_i^D},` | 同左 | 结构 ✔／D 字形 ✘ |
| 3.51 | 35 | 两行：`Ẑ_{q_i^D}≅Z_{q_i^D}, q_i^D>0,`／`Ẑ_0≅U(1).` | align 两行、末行 tag | ✔ |
| 3.52 | 35 | `G^{(d−3)}=U(1)^r.` | 同左 | ✔ |
| 3.54 | 36 | `q_1=(2,−1),  q_2=(−1,2)` | 同左 | ✔ |
| **3.55** | 36 | 裁图确认：`Q=((2,−1),(−1,2)).` | `\begin{pmatrix}2&-1\\-1&2\end{pmatrix}` | ✔ |
| 3.56 | 36 | `SNF(Q)=((3,0),(0,1)).` | 同左 | ✔ |
| 3.57 | 36 | `G^{(1)}=Ẑ_3×Ẑ_1=Z_3×Z_1=Z_3,` | 同左 | ✔ |
| 3.60–3.62 | 36 | `D_{d−3}=∏Z_{p_i^D},`／`diag(p^D)⊂SNF(P),`／`G^{(d−3)}=D̂_{d−3}=∏Ẑ_{p_i^D}.` | 同左 | 结构 ✔／D 字形 ✘ |
| **3.75** | 39 | `q=1,  p=2.` | `q=1\,,\qquad p=2\,.` | ✔ |
| **3.76** | 39 | `C=((1,0),(1,2)),` | `\begin{pmatrix}1&0\\1&2\end{pmatrix}` | ✔ |
| **3.77** | 39 | `SNF(C)=((1,0),(0,2)),` | 同左 | ✔ |
| **3.78** | 39 | `G^{(1)}=Z_2.` | `G^{(1)}=\Z_2` | ✔ |
| 3.79 | 39 | `𝒢=SU(2),`（𝒢 为花体，字体 MS） | `\cG=SU(2)` | ✔ |
| 3.80 | 39 | `𝒲_j=Tr_{R_j}𝒫 e^{2πi∫A},`（Tr 正体；𝒫 为**花体** P，字体 MS） | `\cW_j=\Tr_{R_j}\mathcal{P}\ee^{2\pi i\int A}` | ✔ |
| 3.81 | 39 | `j∈(1/2)Z.` | `j\in\frac{1}{2}\Z` | ✔ |
| **3.87** | 40 | 裁图确认：`D_1=Z_2.`（D 明显无衬线） | `\mathrm{D}_1=\Z_2` | 结构 ✔／D 字形 ✘ |
| 3.89 | 40 | `∫_{S²}F=m∈Z`（**无**标点） | `\int_{S^2}F=m\in\Z` | ✔ |
| 3.90 | 41 | `ϕ:U(1)→𝒢`（𝒢 花体） | `\phi : U(1)\to\cG` | ✔ |
| 3.91 | 41 | `U(1)_ϕ=Image(ϕ)⊆𝒢.` | `U(1)_\phi=\mathrm{Image}(\phi)\subseteq\cG` | ✔ |
| 3.93 | 41 | `ℋ_ϕ(M_{d−3}),`（花体 H） | `\cH_\phi(M_{d-3})` | ✔ |
| 3.95/3.96 | 41 | `ϕ:U(1)→𝒢=SU(2).`／`π_1(SU(2))=1,` | 同左 | ✔ |
| 3.97/3.98 | 41/42 | `D_{d−3}=1.`／`G^{(d−3)}=D̂_{d−3}=1.` | 同左 | 结构 ✔／D 字形 ✘ |
| 3.99 | 42 | `SO(3)=SU(2)/Z_2`（**行内**斜杠，非分式） | `SO(3)=SU(2)/\Z_2` | ✔ |
| **3.101** | 42 | **裁图 900 dpi**：`∫_{D_2} w_2=1∈Z/2Z≡Z_2` —— 圆盘是 **$D_2$（下标）**；紧接的散文句才写 $D^2$（上标，裁图确认） | `\int_{D^2}w_2=1\in\Z/2\Z\equiv\Z_2` | ✘ **必须改（M2）** |
| 3.102/3.103 | 42/44 | `𝒢=G/𝒵,`／`𝒢=SO(3), G=SU(2), 𝒵=Z_2,` | `\cG=G/\cZ`／`\cG=SO(3), G=SU(2), \cZ=\Z_2` | ✔ |
| 3.104 | 44 | `𝒢=SO(3)=SU(2)/Z_2`（**分式**） | `\cG=SO(3)=\frac{SU(2)}{\Z_2}` | ✔ |
| 3.105/3.106 | 44 | `Z_2⊂SU(2),`／`R_j→(−1)^{2j}R_j.` | 同左 | ✔ |
| **3.107** | 44 | 裁图确认：`R_j is an SO(3) representation ⇐⇒ j∈Z.`（原文用 `\Longleftrightarrow`） | `R_j\ \text{是}\ SO(3)\ \text{表示}\iff j\in\Z\,.` | ✔ |
| 3.58 | 36 | `M_i, 1≤i≤m,`（M 为斜体，**非**花体） | `$M_i$` | ✔ |
| (p.38) | 38 | 双荷算符 `𝒟_i`（字体 MS = 花体） | `\cD_i` | ✔（**勿误改为 `\mathsf`/`D`**） |
| (p.36) | 36 | `ℋ_i`（花体 H） | `\cH_i` | ✔ |

> 注 A：原文正文的微分 `d`、自然常数 `e` 均为**数学斜体**，本译本按 STYLE_GUIDE §3 统一用 `\dd`、`\ee`（正体）。tr-02 与 tr-01、全库一致，**不算错**。

## 4. 结构核对

### 4.1 标题层级（用字号核实：`LMRoman12-Bold`=12.0pt→`\subsection`；`LMRoman10-Bold`=10.9pt→`\subsubsection`）

| 原文标题 | 页 | 字号 | 应为 | tr-02 现状 | 判定 |
|---|---|---|---|---|---|
| 3.2 Abelian Gauge Theories | 29 | 12 Bold | `\subsection` | tr02a L22 `\subsection{Abel 规范理论}` | 层级 ✔／用词见 O1 |
| 3.2.1 Maxwell Theory with Single Matter Field | 29 | 10.9 Bold | `\subsubsection` | tr02a L26 | ✔ |
| 3.2.2 Maxwell Theory with Multiple Matter Fields | 33 | 10.9 | `\subsubsection` | tr02a L190 | ✔ |
| 3.2.3 Multiple Abelian Gauge Fields | 34 | 10.9 | `\subsubsection` | tr02b L17 | ✔（用词见 O1） |
| 3.2.4 Including Magnetic Matter | 36 | 10.9 | `\subsubsection` | tr02b L104 `纳入磁物质` | ✔ |
| 3.2.5 Including Dyonic Matter | 37 | 10.9 | `\subsubsection` | tr02b L164 `纳入双荷物质` | ✔ |
| 3.3 Non-Abelian Gauge Theories | 39 | 12 Bold | `\subsection` | tr02c L5 `\subsection{非 Abel 规范理论}` | 层级 ✔／用词见 O1 |
| 3.3.1 Pure SU(2) Yang-Mills Theory | 39 | 10.9 | `\subsubsection` | tr02c L9 | ✔ |
| 3.3.2 Pure SO(3) Yang-Mills Theory | 44 | 10.9 | `\subsubsection` | tr02c L174 | ✔ |

### 4.2 图（编号/文件名/图注）

| 图 | 页 | 原图自然尺寸（400 dpi 裁图反算） | tr-02 用法 | 图注 | 判定 |
|---|---|---|---|---|---|
| 图 9 | 30 | 700×121 px → **126 pt × 22 pt** | `\includegraphics[width=0.62\textwidth]{fig9.png}` | 与原文一致（"电荷为 q 的物质场 φ 给出…端点的非真局域算符"） | 编号/图注 ✔／**图幅过大见 O4** |
| 图 10 | 43 | 911×685 px → **164 pt × 123 pt** | `[width=0.52\textwidth]{fig10.png}` | 与原文一致（含 "小 2 维圆盘 $D_2$"、"阻碍把 SO(3) 规范场提升为 SU(2)"） | 编号/图注 ✔／**图幅偏大见 O5** |
| 图 11 | 43 | 2181×1070 px → **393 pt × 193 pt** | `[width=0.92\textwidth]{fig11.png}` | 与原文一致（$f_1f_2f_3$、$\tilde f_i$、$w_2$） | ✔ |

### 4.3 方框（用原 PDF 的 fill/stroke RGB + 包围盒判定，非目测）

| 原文方框 | 页（原文 y 范围） | 原框样式（实测 RGB） | 应为 | tr-02 现状 | 判定 |
|---|---|---|---|---|---|
| Example 3.1 | 29 (162–357) | 边框 (1.00,0.90,0.80) + 标题条 (1.00,0.90,0.80) | `examplebox` | L11 | ✔ |
| Definition 3.2 | 30 (171–229) | 绿色 (0.667,0.820,0.788) + 标题条 | `definitionbox` | L44 | ✔ |
| Example 3.2 | 31 (281–567) | 橙 + 标题条 | `examplebox` | L97 | ✔ |
| Example 3.3 | 31 (589–712) → 32 (87–276) | 橙 + 标题条，**跨页** | 合并一个 | L114 一个 | ✔ |
| Example 3.4 | 32 (304–665) → 33 (87–199) | 橙 + 标题条，**跨页** | 合并一个 | L141 一个 | ✔ |
| Example 3.5 | 34 (96–265) | 橙 + 标题条 | `examplebox` | L3 | ✔ |
| Smith Normal Form | 35 (96–345) | 边框 (1.00,0.80,0.80) + **粉色标题条**（y 87–109, w 119.5） | `notebox` | L44 | ✔ |
| Example 3.6 | 35 (607–708) → 36 (87–328) | 橙 + 标题条，**跨页** | 合并一个 | L77 一个 | ✔ |
| Example 3.7 | 37 (154–379) | 橙 + 标题条 | `examplebox` | L134 | ✔ |
| Example 3.8 | 37 (406–600) | 橙 + 标题条 | `examplebox` | L146 | ✔ |
| **Example 3.9** | **38 (526–712) → 39 (87–289)** | 橙 + 标题条，**跨 p.38/39** | 合并一个 | tr02b L197 一个，含 (3.73)–(3.78) | ✔ **无重复无丢失** |
| 't Hooft Operators and Cocharacters | 40 (627–712) → 41 (87–439) | 粉框 + 粉色标题条，**跨页** | `notebox` 合并 | tr02c L64 一个 | ✔ |
| Obstruction Classes | 42 (548–685) → **p.43 是整页图** → 44 (87–248) | 粉框 + 粉色标题条，**跨页（被插图页夹断）** | 合并一个 | tr02c L140 一个（含 (3.102)、(3.103)） | ✔ |

### 4.4 `\para` 行内小标题（原文为 `LMRoman10-Bold` 段首粗体）

原文粗体 runhead 全表 vs tr-02：`Setup.`(29)、`Constructing Non-Genuine Local Operators Using Matter Field.`(29)、`Screenings.`(30)、`Electric 1-Form Symmetry.`(31)、`Magnetic (d−3)-Form Symmetry.`(33)、`Wilson Line Operators.`(39)、`Constructing Non-Genuine Local Operators Using Field Strength.`(39)、`Screenings of Wilson Lines.`(40)、`Electric 1-Form Symmetry.`(40)、`'t Hooft Operators.`(40)、`Screenings of 't Hooft Operators.`(41)、`Magnetic (d−3)-Form Symmetry.`(42)、`Topological Codimension-2 Operators.`(42)、`Wilson Line Operators.`(44)
→ tr02a/b/c 共 14 个 `\para{}`，**一一对应、无缺无多** ✔（tr02b 全片无 `\para` 亦正确：pp.34–39 原文无段首粗体）

### 4.5 强调（bold / italic）逐一核对
原文字体探针确认的强调：`greatest common divisor (gcd)`(33,bold)、`Smith normal form`(34,bold)、`cocharacter`(41,bold)、`Gukov-Witten operator`、`Dirac string`(42,bold)、`second Stiefel-Whitney class`(44,bold)、`second Stiefel-Whitney class`(42,**italic**)、`winding number`(41,**italic**)、`dyonic 1-form symmetry group`(38,bold)。
→ tr-02 的 `\textbf`/`\emph` 用法与之**完全对应** ✔（含 p.42 用 `\emph`、p.44 用 `\textbf` 的区分）。

## 5. 漏译核对

逐页把 `split\p029–p044.txt` 与文件对照（正文、脚注、方框标题与内容、图注）：

- **正文**：16 页逐段对上，**未发现整句/整段缺失**；两处原文自身瑕疵照译且已加注 —— p.31 的 "as **they they** have a non-trivial linking"（重复 they，tr02a L95 批注准确，我 800 dpi 裁图复核确认原文如此）、p.43 图 11 图注 "equal to **the the** identity in 𝒢"（tr02c L171 批注准确，我核对文字层与字形确认）。
- **脚注**：原文 pp.29–44 共 3 条脚注 —— p.29 "The unit charge under the U(1) gauge group…"（tr02a L28 ✔）、p.35 "In Mathematica the appropriate command is SmithDecomposition"（tr02b L45 ✔）、p.42 "This terminology was introduced in [74]…"（tr02c L122 ✔）。**3/3 齐全**。
- **交叉引用编号**：本块对**块外**公式的引用共 7 处 —— p.30「(3.4) 附近定义的」、p.31「(2.55) 中所描述」与「(2.55) 中其他的余维-2 算符」（2 处）、p.34「(3.151)」、p.36「(3.153)」、p.37「(3.90)」、p.40「(2.81) 附近」、p.42「(4.31) 附近」；逐个与原文数字核对**全部一致** ✔。块内互引（如 (3.51)、(3.50)、(3.87)、(3.88)、(3.98)）亦与原文一致 ✔。
- **文献引用**：本块原文只有 3 处文献引用 —— p.38「As is well-known from **[77]**」、p.42 正文「Gukov–Witten operator **[78,79]**」、p.42 脚注「introduced in **[74]**」，tr-02 编号与原文**逐一一致** ✔（tr02a 片内原文无文献引用，文件内亦无）。

## 6. 术语一致性（对照 `glossary.tsv`）

| 英文 | glossary | tr-02 用词 | 判定 |
|---|---|---|---|
| higher-form symmetry / 0-/1-/p-form | 高阶形式对称性 / p-形式对称性 | 同 | ✔ |
| screening / completely screened | 屏蔽 / 完全屏蔽 | 同 | ✔ |
| genuine / non-genuine operator | 真算符 / 非真算符 | 非真局域算符 | ✔ |
| Wilson line/operator、't Hooft operator | Wilson 线/算符、't Hooft 算符 | 同 | ✔ |
| monopole | 磁单极子 | 磁单极子（'t Hooft–Polyakov 磁单极子） | ✔ |
| dyonic | 双荷 | 双荷 | ✔ |
| vev | —（新） | 真空期望值（vev） | ✔ 建议补 glossary |
| charge matrix / Smith normal form | —（新） | 荷矩阵 / Smith 标准形（SNF） | ✔ 内部完全一致（6 处全用「标准形」），建议补 glossary |
| cocharacter | —（新） | 余特征标 | ✔ 内部一致（4 处），建议补 glossary |
| Gukov–Witten operator / Dirac string | —（新） | Gukov–Witten 算符 / Dirac 弦 | ✔ |
| obstruction class / Stiefel–Whitney | Stiefel–Whitney 类 ✔ | 阻碍类 / 第二 Stiefel–Whitney 类 | ✔ |
| Higgsing | Higgs 化 | Higgs 化 | ✔ |
| Lagrangian | —（新） | Lagrange 量 | ✔（与 tr-01 一致） |
| Coulomb phase | —（新） | Coulomb 相 | ✔ |
| **abelian** | **缺词条** | **tr-02 用「Abel」（15 处）**，tr-01/04/06–08 用「阿贝尔」，lead 的 c01 用「Abel」 | ⚠ **全书不统一，须 Lead 裁决（O1）** |

## 7. 边界接缝

| 接缝 | 检查结果 |
|---|---|
| tr-01（p.28 图 8 结束）→ tr02a（p.29「也就是说，一个 p 维算符…」） | **无重复、无缺口**。原文 p.28 整页只有图 8，p.29 首句 "That is, the charge of a p-dimensional operator…" 是 (3.6) 之后的续接句；tr-01 未写 (3.7)，tr02a 未重写 p.27 内容 ✔ |
| tr02a（p.33，(3.41)）→ tr02b（p.34，例 3.5） | 无缺口。p.33 末为 (3.41)，p.34 首为 "Example 3.5" ✔ |
| **tr02b（p.39，例 3.9 方框 +(3.78)）→ tr02c（p.39，3.3 标题 +(3.79)）** | **无重复、无丢失**。例 3.9 方框整体在 tr02b 内（原文方框 y 526→712 + 87→289，全部落在 tr02b）；tr02c 从 3.3 标题起笔 ✔ |
| tr02c（p.44，(3.107)）→ tr-03（p.45，(3.108)） | **无重复、无缺口**。原文 p.44 正文止于 (3.107)；p.45 首为 "Electric 1-Form Symmetry. As discussed above, all integer spin Wilson lines…"；tr03a 首行即 `\para{电 1-形式对称性。}如上文所讨论…` ✔ |

## 8. 必须改（3 项）

### M1【全书统一 + 原文形体】`\mathrm{D}` 应为 `\mathsf{D}`（tr02a/b/c 共 28 处）

- **页码/式号**：p.29 (3.7)(3.8)；p.30 (3.17)；p.31 (3.18)；p.33 (3.39)(3.40)；p.34 (3.46)(3.47)；p.35 (3.49)(3.50)；p.36 (3.60)(3.61)(3.62)；p.38 (3.71)(3.72)；p.40 (3.87)(3.88)；p.41 (3.97)；p.42 (3.98)。
- **原文**：`D_p` 的 D 是**无衬线正体**。证据两条：(a) PyMuPDF 读出该字形的字体名为 **`LMSans10-Regular`**（同页其余数学字母为 `LMMathItalic10`，`\mathbb` 为 `MSBM10`）；(b) p.40 (3.87) 900 dpi 裁图中 D 与相邻斜体 $G$、serif $Z$ 对比明显无衬线。
- **现状（逐行计数，共 28 处）**：
  - tr02a **11 处**：L5×1、**L9×4**（该行是批注，含 `\mathrm{D}_p`×2、`\mathrm{D}_1`、`\mathrm{D}_{d-3}`）、L14×2、L78、L85、L206、L210；
  - tr02b **9 处**：L31、L35、L59、L118、L124、L126、L188、L192、L226（各 1）；
  - tr02c **8 处**：L51、L53、L55、L57、L59、L113、L119、L197（各 1）。
- **可直接替换**：三个文件内**全局** `\mathrm{D}` → `\mathsf{D}`（即 `\mathrm{D}_p`→`\mathsf{D}_p`、`\widehat{\mathrm{D}}_1`→`\widehat{\mathsf{D}}_1`、`\mathrm{D}_{d-3}`→`\mathsf{D}_{d-3}`；批注行 L9 也一并换，保持与正文一致）。
- **注意事项（勿误改）**：p.38 的双荷算符 `\cD_i` 原文确为**花体** $\mathcal{D}$（字体名 `LMMathSymbols10`），保持 `\cD_i`；圆盘 `D^2`/`D_2` 与电荷矩阵 $P$、$M_i$ 是**数学斜体**，不动。
- **旁证（供 Lead 统筹）**：tr-01（9 处）与 tr-08（39 处）已用 `\mathsf{D}`；tr-03 有 **24 处**同样的 `\mathrm{D}`，建议一并处理。

### M2【抄写错误】(3.101) 的圆盘应为下标 `D_2`

- **页码/式号**：p.42 (3.101)。
- **原文（900 dpi 裁图）**：`∫_{D_2} w_2 = 1 ∈ Z/2Z ≡ Z_2` —— 积分下标的 D 与 2 **同为下标**（span 探针：`D` origin_y=389.73/size 7.97，`2` origin_y=390.83/size 5.98，二者都在基线 380.89 之下；若为 $D^2$ 则 2 的 origin_y 应**小于** D 的）。图 10 图注同样写 `D_2`。
- **原文四处写法全表（均经探针/裁图核实，原文本身 2:2 混用）**：
  | 位置 | 原文写法 | 证据 |
  |---|---|---|
  | 图 10 **图内标注** | $D^2$（上标） | 1000 dpi 裁图；span: D oy=213.61、`2` oy=209.65（高于 D） |
  | 图 10 **图注** | $D_2$（下标） | span: D oy=276.52、`2` oy=278.15（低于 D） |
  | p.42 **散文句** "a small disk $D^2$ intersecting…" | $D^2$（上标） | 700 dpi 裁图 |
  | **(3.101) 公式** | **$D_2$（下标）** | 900 dpi 裁图 + span 探针 |
- **现状**：tr02c L134 `\int_{D^2}w_2=1\in\Z/2\Z\equiv\Z_2 \tag{3.101}` —— 写成**上标**。
- **可直接替换**（L134 整行）：
  ```
    \int_{D_2}w_2=1\in\Z/2\Z\equiv\Z_2 \tag{3.101}
  ```

### M3【批注与事实相反】tr02c L171 关于 $D_2$/$D^2$ 的说法要改（与 M2 同一条批注）

- **原文事实（四处写法，均经探针/裁图核实）**：p.42 **散文句**写 `$D^2$`（上标，裁图确认："a small disk $D^2$ intersecting $\Sigma_{d-2}$ at a point"）；**(3.101) 与图 10 的图注都写 `$D_2$`（下标）**；而 **图 10 的图内标注写 `$D^2$`（上标，已烘焙进 `fig10.png`，不需也无法改）**。原文确实混用，但**混用位置与该批注所说的相反**：(3.101) 是下标，不是上标。
- **现状**（tr02c L171 末两句）："再注：原文图 10 的图注把圆盘写成 `$D_2$`（下标），而正文 (3.101) 写成 `$D^2$`（上标），原文两处混用，译文照抄。"——其中"正文 (3.101) 写成 $D^2$"**不成立**；"译文照抄"也不成立（译文 (3.101) 被抄成了 $D^2$）。同句前半 "(3.101) 中的 $w_2$ 正是它与 $D^2$ 的配对值" 也需同步改。
- **可直接替换**（L171 批注末尾两句改为）：
  ```
  …(3.101) 中的 $w_2$ 正是它与 $D_2$ 的配对值 $1\in\Z_2$。再注：原文对同一个对象混用两种写法，且四种场合并不一致——图 10 图内的标注与 p.42 的散文句 "a small disk $D^2$ intersecting $\Sigma_{d-2}$ at a point" 用 $D^2$（上标），而图 10 的图注与公式 (3.101) 用 $D_2$（下标）；译文各处分别照原文保留，未作统一。]
  ```

## 9. 可选改（8 项）

### O1【全书术语】abelian：`Abel` vs `阿贝尔`
- **页码**：p.29 (3.2 标题)、p.34 (3.2.3 标题)、p.39 (3.3 标题) 及正文。
- **现状**：tr-02 全用「Abel」，共 **15 处** —— tr02a 2 处（L22、L24）；tr02b **10 处**（L17、L19×2、L25、L29、L110×2、L166、L169、L186）；tr02c 3 处（L5、L7、L62）。而 tr-01（21 处）、tr-04（5 处）、tr-06、tr-07、tr-08 用「阿贝尔」；**lead 的 c01 自己也用「Abel」（4 处）**；glossary 无 abelian 词条。
- **建议**：由 Lead 定一个（数学文献惯例为「阿贝尔」），写入 glossary，然后**全库**统一——不要只让 tr-02 单方面改，否则仍是混用。
- **若决定用「阿贝尔」，tr-02 的最小改法（全局替换即可，共 15 处）**：`Abel` → `阿贝尔`，`非 Abel` → `非阿贝尔`（即 `\subsection{Abel 规范理论}`→`\subsection{阿贝尔规范理论}`、`\subsubsection{多个 Abel 规范场}`→`\subsubsection{多个阿贝尔规范场}`、`\subsection{非 Abel 规范理论}`→`\subsection{非阿贝尔规范理论}`，正文里「Abel 规范理论/Abel 群/非 Abel 规范群」同理）。注意 tr02b L19 与 L110 各含 2 个 `Abel`，不要漏。

### O2【图幅】图 9 被放大 2.25 倍
- **页码**：p.30 图 9。原图自然尺寸 **126 pt × 22 pt**（`fig9.png` 700×121 px @400 dpi）。
- **现状**：tr02a L40 `\includegraphics[width=0.62\textwidth]{fig9.png}` ≈ 284 pt，放大 2.25×，线条与字号会明显变粗。
- **可直接替换**：`\includegraphics[width=0.28\textwidth]{fig9.png}`（≈128 pt，与原书 1:1）。

### O3【图幅】图 10 被放大 1.45 倍
- **页码**：p.43 图 10。原图 **164 pt × 123 pt**（`fig10.png` 911×685 px @400 dpi）。
- **现状**：tr02c L161 `width=0.52\textwidth` ≈ 238 pt。
- **可直接替换**：`\includegraphics[width=0.36\textwidth]{fig10.png}`（≈165 pt）。图 11（原 393 pt，现 0.92\textwidth≈421 pt）基本 1:1，**不改**。

### O4【标点】(3.9) 第二行末尾原无逗号
- **页码**：p.29 (3.9)。原文 `G^{(1)} = U(1),  G^{(d−3)} = U(1)`（第二行**无**句末标点）。
- **现状**：tr02a L18 `G^{(1)}=U(1)\,,\qquad G^{(d-3)}=U(1)\,, \tag{3.9}` 多一个逗号。
- **可直接替换**（L18）：
  ```
    G^{(1)}=U(1)\,,\qquad G^{(d-3)}=U(1) \tag{3.9}
  ```

### O5【标点】(3.74) 原文句末有句点
- **页码**：p.38 (3.74)。原文 `q_ϕ = 1 .`（探针显示末尾有 math 句点，与 (3.26) 的 `q_Φ = 1`（无句点）不同）。
- **现状**：tr02b L204 `q_\phi=1 \tag{3.74}` 无句点。
- **可直接替换**：
  ```
    q_\phi=1\,. \tag{3.74}
  ```

### O6【批注措辞】tr02a L178 关于 (3.30) 的 `δ` 的批注可写得更准
- **原文**：p.32 (3.30) `(2π/q)∫a_1∪δb_{d−2}`，其中 `δ` 就是 §2.3 (2.83) 明确规定的「外微分的离散版本」（上链复形的余边界算子），本身无歧义。
- **现状问题**：① 该批注先把 `δ` 假想成 Hodge 余微分再排除，读者会以为原文有歧义；② "此式与 (3.34) 的连续表述 … **互为对偶写法**" 不准确——正文 L173 已正确说明 (3.34) 是 (3.30) 的**连续表述**（continuous presentation），不是"对偶写法"。
- **可直接替换**（L178 整行）：
  ```
  % [Tutor Note: p.32 式 (3.30) 中的 $\delta$ 就是 §2.3 (2.83) 规定的“外微分的离散版本”，即上链复形的余边界算子，把 $(d-2)$-上链映到 $(d-1)$-上链，故 $a_1\cup\delta b_{d-2}$ 是 $d$-上链、可在 $d$ 维上求和。切勿把它与 Hodge 余微分 $\delta=\pm\star\dd\star$ 混淆：后者把 2-形式降次，$a_1\wedge\delta b_{d-2}$ 只会有 $(d-2)$ 次，积分不成。(3.34) 则是 (3.30) 在连续语言下的等价表述（正文 L173 已如此说明），$q/2\pi$ 系数与之对应。]
  ```

### O7【批注措辞】tr02c L53-55 把原文 "two non-trivial equivalence classes" 判为「笔误」语气可放软
- **原文**：p.40 "…can be chosen as representatives of **the two non-trivial equivalence classes** of line operators forming the group $\widehat G^{(1)}=D_1$."（800 dpi 裁图确认原文字面如此）。
- **现状**：tr02c L55 批注写「"non-trivial" 疑为笔误——平凡 Wilson 线代表的正是两个类中的平凡类，只有自旋-1/2 那个类才是非平凡的」。判断方向可以（字面确实与"其中一个类是平凡类"相抵），但定性为"笔误"偏强，且译文已照原文写「两个非平凡等价类」，与批注的口径不一致（读者会疑惑）。
- **建议替换**（L55 末句）：
  ```
  …另注：p.40 正文 “the two non-trivial equivalence classes” 的字面是“两个非平凡等价类”，但其中一个是平凡 Wilson 线所在的类，故此处 “non-trivial” 更可能只是强调这两类互不相同（=“两个不同的等价类”），而非断言两类都非平凡；译文按字面保留原文措辞。
  ```

### O8【排版】tr02c 页标记顺序（p.44 → p.43 → p.44）
- **页码**：pp.42–44 的「阻碍类」方框被 p.43 整页插图夹断。
- **现状**：tr02c 把方框合并写出后，才排 p.43 的两幅图，于是文件内 `% [原文 p.44]`（L146）→`% [原文 p.43]`（L158）→`% [原文 p.44]`（L173）出现回退，且 p.44 标记两次。文件头已说明，**不影响正确性**。
- **建议（任选其一）**：① 保持现状但在 L158 处把标记写成 `% [原文 p.43]（原文此页为两幅整页插图，见图 10、图 11；“阻碍类”方框跨 p.42→p.44）`；② 或把两幅 `figure` 移到「阻碍类」方框**之前**（图 10 的首次引用在 p.42 方框前的正文 "见图 10"，图 11 的引用在方框内 "见图 11"），这样页序单调、与首引位置也更贴。

---

## 附：脚本体检结果（供 Lead 复核）

```
tr02a.tex  bytes=13630 BOM=False CRLF=False FFFD=0 tags=35 first=3.7  last=3.41
           begin=41 end=41 env栈=空  $=188(偶)  禁项=无  notes=8  pageMarks=5
tr02b.tex  bytes=12910 BOM=False CRLF=False FFFD=0 tags=37 first=3.42 last=3.78
           begin=48 end=48 env栈=空  $=172(偶)  禁项=无  notes=6  pageMarks=6
tr02c.tex  bytes=12693 BOM=False CRLF=False FFFD=0 tags=29 first=3.79 last=3.107
           begin=33 end=33 env栈=空  $=250(偶)  禁项=无  notes=4  pageMarks=7
总 tag=101  连续性异常=0  重复 tag=0  整句未译=0
```
