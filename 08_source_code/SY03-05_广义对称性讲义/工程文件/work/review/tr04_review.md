# tr-04 块交叉校对报告

- 校对对象：`work/src/chunks/tr04a.tex`（pp.61–66）、`tr04b.tex`（pp.67–71）、`tr04c.tex`（pp.72–76）
- 原文范围：pp.61–76；tag 区间 4.3–4.78（76 条）；图 12–16；表：无
- 校对者：tr-03（**只读校对，未改动 tr-04 的任何文件**）
- 方法：
  1. `work/tags_bypage.txt` 逐页核号（pp.61–76，含无公式页 p.65/p.69/p.73）；
  2. 逐页 `work/pages/pNNN.png` 整页比对结构；关键公式用 `tools/crop.py` 在 600–800 dpi 下裁图逐符号复核（26 条）；
  3. `work/split/pNNN.txt` 与 tr04 译文逐页对照查漏译；
  4. 用 PyMuPDF 抽取每页彩色矩形的填充色，核对彩色方框的**类型与跨页断点**（见 §3）；并扫描全文确认 pp.61–76 **没有脚注**；
  5. `work/full.txt` 中 `Statement/Definition/Example N.M:` 清单与 tr04 的方框逐一对账。

---

## 0. 结论摘要

- **编号公式：76 条 = 4.3–4.78，与 `tags_bypage.txt`（pp.61–76）逐页一一对应，无缺、无重、无跳、无自造编号。**（p.65/p.69/p.73 原文本身无编号公式，tr04 亦无。）
- **抽查 26 条编号公式逐符号核对，全部与原文一致**；Lead 指定的 4.3 / 4.10 / 4.21 / 4.32 / 4.35 / 4.47 / 4.51 / 4.56 / 4.72 / 4.76 / 4.78 全部通过，另加 4.5、4.18、4.28、4.30、4.34、4.41、4.45、4.46、4.48、4.55、4.60、4.62/4.63、4.66、4.70、4.74。
- **结构全部正确**：4.2/4.2.1（p.67）、4.2.2（p.74）三个标题层级正确；图 12–16 编号、图注、位置正确；方框 16 个（1 蓝 Statement + 5 绿 Definition + 7 橙 Example + 3 粉 notebox）与环境类型逐一对上，跨页断开的 3 个方框（例 4.4、例 4.7、"Other Types of Anomalies"）已按规范合并。
- **漏译：无。** pp.61–76 逐页对照 split 文字层，段、句、图注、方框内文、无编号公式全部有对应译文。
- **发现 2 条批注有实质性错误（必须改）**，另有 1 条批注的"核对办法"句错误（必须改），1 条批注指标笔误（必须改）；公式本体、正文译文、结构与编号**均无错误**。
- 术语：本块内部一致；跨块有 3 组不一致（cocycle、obstruction、non-Abelian），属项目级 glossary 问题，建议 Lead 冻结后统一。
- **结论：译文与公式可验收；4 处批注需按 §6 修正后入库。**

---

## 1. 编号完整性表

| 页 | `tags_bypage.txt` | tr04 实际 | 所在文件 | 结果 |
|---|---|---|---|---|
| p.61 | 4.3–4.8（6 条） | 4.3–4.8 | tr04a | ✅ |
| p.62 | 4.9–4.15（7 条） | 4.9–4.15 | tr04a | ✅ |
| p.63 | 4.16–4.21（6 条） | 4.16–4.21 | tr04a | ✅ |
| p.64 | 4.22–4.30（9 条） | 4.22–4.30 | tr04a | ✅ |
| p.65 | 无编号公式（仅图 12） | 0 | tr04a | ✅ |
| p.66 | 4.31–4.33（3 条） | 4.31–4.33 | tr04a | ✅ |
| p.67 | 4.34–4.37（4 条） | 4.34–4.37 | tr04b | ✅ |
| p.68 | 4.38–4.43（6 条） | 4.38–4.43 | tr04b | ✅ |
| p.69 | 无编号公式（图 13、陈述 4.1） | 0 | tr04b | ✅ |
| p.70 | 4.44–4.49（6 条） | 4.44–4.49 | tr04b | ✅ |
| p.71 | 4.50–4.51（2 条） | 4.50–4.51 | tr04b | ✅ |
| p.72 | 4.52–4.59（8 条） | 4.52–4.59 | tr04c | ✅ |
| p.73 | 无编号公式（仅图 16） | 0 | tr04c | ✅ |
| p.74 | 4.60–4.66（7 条） | 4.60–4.66 | tr04c | ✅ |
| p.75 | 4.67–4.72（6 条） | 4.67–4.72 | tr04c | ✅ |
| p.76 | 4.73–4.78（6 条） | 4.73–4.78 | tr04c | ✅ |
| **合计** | **76** | **76** | — | **✅ 无缺/重/跳** |

> 已脚本化按 `% [原文 p.N]` 分段统计每页 `\tag` 数：16 页全部与 `tags_bypage.txt` 精确相等（0 处错位）。p.65/p.69/p.73 为纯图页/无编号页，与原文一致。

---

## 2. 逐符号核对表（26 条，600–800 dpi 裁图）

| tag | 页 | 原文关键内容（裁图读出） | tr04 转录 | 判定 |
|---|---|---|---|---|
| 4.3 | p.61 | $A\to A+d\Lambda$ | `A\to A+\dd\Lambda` | ✅ |
| 4.5 | p.61 | $G^{(p)}=U(1)^n,\ n>0$ | 同 | ✅ |
| 4.10 | p.62 | $2\pi\int B_{p+1}\wedge j^{d-p-1}$ | 同 | ✅ |
| 4.18 | p.63 | $2\pi\int\big(B^e_{p+1}\cup_\eta b_{d-p-1}+a_p\cup_\eta B^m_{d-p}\big)$ | 用 `\underset{\eta}{\cup}` | ✅ |
| 4.21 | p.63 | $w_2=B^e_2$ | 同 | ✅ |
| 4.28 | p.64 | $\eta:\widehat{\cZ}\times\cZ\to\R/\Z$ | 同 | ✅ |
| 4.30 | p.64 | $2\pi\int B^m_{d-2}\cup_\eta w_2=\pi\int B^m_{d-2}\cup w_2$ | 同 | ✅ |
| 4.32 | p.66 | $U_g=\int g(j_{d-p-1}),\ g\in G^{(p)}$ | 同 | ✅ |
| 4.34 | p.67 | $Z[B_{p+1}]\neq Z[B^g_{p+1}]$ | 同 | ✅ |
| 4.35 | p.67 | 两行：$B^g_{p+1}=B_{p+1}+d\Lambda_p$（连续）/ $B^g_{p+1}=B_{p+1}+\delta\Lambda_p$（离散） | `gathered` 两行 + 单 tag | ✅（原文即两行一号；tag 竖直居中一致） |
| 4.41 | p.68 | $Z[B^e_2{+}d\Lambda^e_1,B^m_{d-2}]=\exp\!\big({-}2\pi i\int\Lambda^e_1\wedge dB^m_{d-2}\big)\times Z[\cdot]$ | 同 | ✅ |
| 4.45 | p.70 | $\exp\!\big(2\pi i\,s(p)\int\Lambda^e_p\cup_\eta B^m_{d-p}\big)\times Z$ | 同 | ✅ |
| 4.46 | p.70 | $s(n):=(-1)^n,\ n\in\Z$ | 同 | ✅ |
| 4.47 | p.70 | $B^m_{d-p}\to B^m_{d-p}+\delta\Lambda^m_{d-p-1}$ | 同 | ✅ |
| 4.48 | p.70 | $\exp\!\big({-}2\pi i\int B^e_{p+1}\cup_\eta\Lambda^m_{d-p-1}\big)\times Z$ | 同 | ✅ |
| 4.51 | p.71 | $\cO_{g_1,g_2}$ | 同（`\cO`） | ✅ |
| 4.55 | p.72 | $\delta\omega(g_1,g_2,g_3,g_4)=\dfrac{\omega(g_2,g_3,g_4)\omega(g_1,g_2g_3,g_4)\omega(g_1,g_2,g_3)}{\omega(g_1g_2,g_3,g_4)\omega(g_1,g_2,g_3g_4)}=1$ | 逐项一致（分子 3 项、分母 2 项） | ✅ |
| 4.56 | p.72 | 两行：$\delta\alpha_p(\cdots)=\alpha_p(g_2,\cdots,g_{p+1})\alpha_p^{s(p+1)}(g_1,\cdots,g_p)\prod_{i=1}^{p}\alpha_p^{s(i)}(g_1,\cdots,g_{i-1},g_ig_{i+1},g_{i+2},g_{i+3}\cdots,g_{p+1})$ | 逐字一致（含 $s(p+1)$、$s(i)$、$g_{i+3}$ 的写法） | ✅ |
| 4.60 | p.74 | $[\omega]\in H^3(G^{(0)},\C^\times)$ | 同 | ✅ |
| 4.62 / 4.63 | p.74 | $\cS=\{G^{(p_1)},\cdots,G^{(p_n)}\}$；$Z[B_{p_1+1}=0,\cdots]=1$ | 同 | ✅ |
| 4.66 | p.74 | $U_g=D^{\mathrm{id}}_{d-p_i-1},\ \forall g\in G^{(p_i)},\forall i$ | 同 | ✅ |
| 4.70 | p.75 | $\cW_{j=\frac{1}{2}}$ | 同 | ✅ |
| 4.72 | p.75 | $Z[B_2]=\exp\!\big(\pi i s\int\frac{\cP(B_2)}{2}\big),\ s\in\{0,1\}$ | 同 | ✅ |
| 4.74 | p.76 | $\cO_{g_1,g_2}=\beta(g_1,g_2)\in\C^\times$ | 同 | ✅ |
| 4.76 | p.76 | $Z[A_1]=\int A_1^*\beta$ | 同 | ✅ |
| 4.78 | p.76 | $A_1^*\alpha_p(v_0,\cdots,v_p):=\alpha_p\big(A_1(v_0,v_1),A_1(v_1,v_2),\cdots,A_1(v_{p-1},v_p)\big)$ | 同（顶点对、下标 $p-1$ 均正确） | ✅ |

> 说明：4.35、4.56 原文为"两行一号"，tr04 分别用 `gathered` 并只在末行 `\tag`，符合 STYLE_GUIDE §3。

---

## 3. 结构核对

### 3.1 标题

| 页 | 原文标题 | tr04 写法 | 层级 | 判定 |
|---|---|---|---|---|
| p.67 | 4.2 't Hooft Anomalies and SPT Phases | `\subsection{'t Hooft 反常与 SPT 相}`（tr04b:3） | subsection | ✅ |
| p.67 | 4.2.1 Basics of 't Hooft Anomalies | `\subsubsection{'t Hooft 反常基础}`（tr04b:5） | subsubsection | ✅ |
| p.74 | 4.2.2 SPT Phases | `\subsubsection{SPT 相}`（tr04c:76） | subsubsection | ✅ |

（本块不负责 4.1、4.3 等标题，tr04 未越界写标题 ✅。）

### 3.2 图 12–16

| 图 | 页 | 原文图注要点 | tr04 写法 | 图文件 | 判定 |
|---|---|---|---|---|---|
| 12 | p.65 | 两个互为对偶的三角剖分（红/黑）；2-单形↔0-单形、边一一对应 | `figtitle{12}`，`width=0.35\textwidth` | fig12.png（845×960 PNG） | ✅ 图内文字与图注相符 |
| 13 | p.69 | 't Hooft 反常两例；上图 $U_{g'}$ 在 $U_g$ 下带电，下图联结带电 | `figtitle{13}`，`0.62\textwidth` | fig13.png（1865×1852） | ✅ |
| 14 | p.71 | 2d 0-形式对称性的拓扑局域与线算符构型 | `figtitle{14}`，`0.35\textwidth` | fig14.png（836×1072） | ✅ |
| 15 | p.71 | F-移动把关联函数改变 $\omega$ 倍 | `figtitle{15}`，`0.8\textwidth` | fig15.png（2221×899） | ✅ |
| 16 | p.73 | 连续 F-移动的两种路径 ⇒ (4.55) | `figtitle{16}`，`0.5\textwidth` | fig16.png（2155×2922，真实 PNG 文件头） | ✅ |

- 位置：图 12 在 p.65 页首（原文即浮动于 p.65 顶端）✅；图 13 在 p.69 页首 ✅；图 14、15 都在 p.71 ✅；图 16 独占 p.73 ✅；均在本页 `% [原文 p.N]` 之后。
- 5 个图文件均为真实 PNG（已核文件头 `89 50 4E 47`），不存在扩展名与内容不符的问题 ✅。

### 3.3 彩色方框（用 PDF 填充色逐页对账）

| 页 | 原文外观 / 标题 | 应有环境 | tr04 实际 | 判定 |
|---|---|---|---|---|
| p.61 | 绿 Definition 4.1: Background Field for Continuous p-Form Symmetry | definitionbox | ✅ tr04a:29 | ✅ |
| p.62 | 橙 Example 4.1: Maxwell Theory | examplebox | ✅ tr04a:54 | ✅ |
| p.62 | 绿 Definition 4.2: Background Field for Discrete p-Form Symmetry | definitionbox | ✅ tr04a:81 | ✅ |
| p.63 | 橙 Example 4.2: Discrete Gauge Theories | examplebox | ✅ tr04a:98 | ✅ |
| p.64 | 橙 Example 4.3: Pure SU(2) Yang-Mills Theory | examplebox | ✅ tr04a:120 | ✅ |
| p.64–65 | 橙 Example 4.4: Pure SO(3) Yang-Mills Theory（**跨页断开**） | examplebox（合并） | ✅ tr04a:152，末句并入方框 | ✅ |
| p.65 | 粉 "Operators vs. Defects" | notebox | ✅ tr04a:177 | ✅ |
| p.67–68 | 粉 "Other Types of Anomalies"（**跨页断开**） | notebox（合并） | ✅ tr04b:38 | ✅ |
| p.68 | 橙 Example 4.5: Maxwell Theory | examplebox | ✅ tr04b:50 | ✅ |
| p.69 | 蓝 Statement 4.1: 't Hooft Anomalies as Topological Defects Carrying Charges | statementbox | ✅ tr04b:90 | ✅ |
| p.70 | 橙 Example 4.6: Discrete Gauge Theories | examplebox | ✅ tr04b:99 | ✅ |
| p.72 | 绿 Definition 4.3: Group-Cochains | definitionbox | ✅ tr04c:12 | ✅ |
| p.72 | 绿 Definition 4.4: Differential on Group-Cochains and Group Cohomology | definitionbox | ✅ tr04c:25 | ✅ |
| p.74 | 绿 Definition 4.5: SPT Phase | definitionbox | ✅ tr04c:80 | ✅ |
| p.75–76 | 橙 Example 4.7: Faithful to Non-Faithful: 4d N=1 SU(2) Super-Yang-Mills（**跨页断开**） | examplebox（合并） | ✅ tr04c:113，末句并入方框 | ✅ |
| p.76 | 粉 "Pullback of Group-Cochains" | notebox | ✅ tr04c:166 | ✅ |

- 计数：statementbox ×1、definitionbox ×5、examplebox ×7、notebox ×3、noteboxplain ×0 = 16 个方框，与原文 pp.61–76 的方框清单**完全相等**（已用 `full.txt` 的 "Statement/Definition/Example N.M:" 清单核对：Def 4.1–4.5、Ex 4.1–4.7、Stmt 4.1，无遗漏、无多余）。
- 跨页合并符合 STYLE_GUIDE §7；且 tr04 用批注说明了合并（tr04a:164、tr04c:141）。

### 3.4 脚注与页码

- **pp.61–76 原文没有任何脚注**（已用 PyMuPDF 逐页扫描 y>700 区域确认）；tr04 也无 `\footnote` ✅（与我 tr-03 的 p.60 脚注 #6 无冲突）。
- 每页均有 `% [原文 p.N]`（61–76 全，顺序正确，无缺页）✅；三片开头分别为 `% ===== 原文 pp.61–66 / 67–71 / 72–76 =====` ✅。

---

## 4. 漏译检查（逐页对照 split 文字层）

**结论：无漏译。**

- p.61：(4.3)+"for 0-forms Λ"；"large gauge transformations … shift the holonomies ∮A by integers"；"correlation functions are functions of A"；"One denotes … as Z[A]"；(4.4)+Noether 流；`\para{连续的 p-形式对称性}`（含 "Since p≥1-form symmetries are abelian" 理由句）；(4.5)(4.6)；Definition 4.1（(4.7)）；(4.8)+"large gauge transformations … (p+1)-dimensional closed submanifolds"。齐。
- p.62："In a theory with (4.6) symmetry …"；(4.9)；(4.10)+"where j^{d−p−1} is the Noether current"；Example 4.1（"We return to the example of Maxwell theory introduced in example 2.2"、(4.11)–(4.15)、"respectively"、"From the knowledge of the Noether currents"）；`\para{离散 p-形式对称性}`（"We need a discrete version of differential forms. As discussed in section 2.3, this is provided by discrete cochains"）；Definition 4.2。齐。
- p.63：(4.16)+"If background fields for other symmetries are not turned on, then B is a cocycle"；"However, if … may not be a cocycle. This happens if G participates in a non-trivial group extension or a higher-group symmetry. We discuss such aspects later."；(4.17)；Example 4.2（含 (4.18)"where recall that a_p and b_{d−p−1} are dynamical gauge fields"）；`\para{非阿贝尔规范理论的电 1-形式对称性}`（(4.19)–(4.21)）。齐。
- p.64：Example 4.3（(4.22)–(4.24)）；`\para{非阿贝尔规范理论的磁 (d−3)-形式对称性}`（(4.25)–(4.28)，含 "Z is a subgroup of the center Z(G) of the simply connected group G"）；Example 4.4（(4.29)–(4.30)）。齐。
- p.65：Figure 12 图注全译；Example 4.4 末句（"where w2 is the second Stiefel-Whitney class, and on the RHS … standard cup product between two Z2-valued cochains"）；`\para{背景场作为拓扑缺陷网络}`；notebox "Operators vs. Defects"（两段全译）；"As discussed in section 2.3, the cochain B_{p+1} is defined in terms of a triangulation T … dual triangulation T̂, which is defined as follows:"。齐。
- p.66：三条 itemize（顶点/边/i-单形）全译（含原文 "The boundary of s_i" 的无 hat 写法，见 §6-b）；"See figure 12 for a depiction of the two triangulations in d = 2"；(4.31)+"Given this, insert the codimension-(p+1) topological defect U_g …"；"The partition function Z[B] … is then the same as the correlation function of the corresponding network …"；"This is easy to demonstrate in a situation when we have a discrete Noether current …"；(4.32)+"where j_{d−p−1} which is a dynamical Ĝ-valued cochain"；(4.33)；"By Poincaré duality, computing partition function in the presence of this term is precisely equivalent to …"；`\para{作为拓扑缺陷重排的规范变换}`。齐。
- p.67：`\subsection`+`\subsubsection`；`\para{纯 't Hooft 反常}`（两个 itemize 项 + (4.34)(4.35)）；`\para{混合 't Hooft 反常}`（(4.36)(4.37)+"in such a way that cannot be fixed by adding a counterterm"）；"There can also be mixed 't Hooft anomalies involving more than two symmetries, whose definition is a straightforward generalization of the above."；notebox "Other Types of Anomalies" 开头与 ABJ 项。齐。
- p.68：ABJ 项续（"In the context of 4d gauge theories … triangle diagrams having gauge currents on two vertices, and a global current on the third vertex"）；Gauge Anomalies 项；'t Hooft Anomalies 项；Example 4.5（(4.38)–(4.43) 及两段文字）。齐。
- p.69：Figure 13 图注全译；`\para{用拓扑算符描述}`；Statement 4.1 全文；"Addition of counterterms corresponds to redefining the topological operators and their junctions."（跨 p.69–70 的句子已在 tr04b 内合并写出）。齐。
- p.70：Example 4.6（(4.44)–(4.49) 及"has to do with the fact that the topological operators constituting the G^{(p)} electric p-form symmetry are charged under the Ĝ^{(p)} magnetic symmetry, and vice versa"一长段全译）；`\para{2d 中离散 0-形式对称性的 't Hooft 反常}`。齐。
- p.71：Figure 14、Figure 15 图注全译；(4.50)(4.51)+"at a junction where line operators L_{g1} and L_{g2} come together and transform into L_{g1g2}"；"Consider a movement of topological lines shown in figure 15, which is sometimes referred to as an associator or as an F-move"。齐。
- p.72：(4.52)(4.53)+"which characterizes the 't Hooft anomaly … once counterterms have been taken into account"；"Such a function is known as a C×-valued 3-group-cochain on G^{(0)}"；Definition 4.3（(4.54)）；"There is a consistency condition, known as the pentagon identity …"（(4.55)）；"which means that ω is a closed 3-group-cochain"；Definition 4.4（(4.56)(4.57) 及 "i.e. we take α_p for even i and α_p^{−1} for odd i"、"is referred to as the p-th group cohomology of G^{(0)} valued in M"）；(4.58)(4.59)。齐。
- p.73：Figure 16 图注全译。齐。
- p.74："as the reader can check. Thus, only the cohomology class [ω] of ω determines a 't Hooft anomaly."；(4.60)；"For later purposes let us note that"；(4.61)+"so [ω] can be regarded as an element of H^3(G,U(1))"；`\subsubsection{SPT 相}`；"intimately tied to … very important in various diverse areas of theoretical physics. Let us begin with the definition …"；Definition 4.5（(4.62)–(4.64)）；`\para{忠实与非忠实对称性}`（(4.65)(4.66)）。齐。
- p.75：(4.67) 及其引出句；"We say that a symmetry is non-faithful …"整段；"Let us emphasize that the faithfulness … is not an RG invariant notion …"；Example 4.7（(4.68)–(4.72)）。齐。
- p.76：Example 4.7 末句（"where P is the Pontryagin square operation discussed around equation (3.193). Thus the (4.69) 1-form symmetry is completely non-faithful in the IR."）；`\para{SPT 相的信息}`整段（含 "This information is stored entirely in the junctions of these topological operators."）；(4.73)；"As in (4.51), we have to choose … at a junction of L_{g1}, L_{g2} and L_{g1g2}"；"As the lines are all identity … which is C×"；(4.74)；(4.75)+"where ω was described in figure 15. In other words, β is a cocycle."；"It is straightforward to see that for a given β …"；(4.76)；notebox "Pullback of Group-Cochains"（(4.77)(4.78) 全文）。齐。

### 4.1 边界接缝

| 接缝 | 检查 | 结论 |
|---|---|---|
| tr-03（我的 p.60 末）→ tr04a 开头 | 我的 p.60 以 (4.2) $F=\dd A$ + 脚注 #6 结束；tr04a 从 "背景场的小规范变换为 (4.3)" 起 | **无重复、无缺口** ✅（原文 p.61 首句即 "The small gauge transformations for the background field are"）。 |
| tr04a → tr04b（p.66/p.67） | tr04a 末为 "…见图 13。"；tr04b 以 p.67 的 `\subsection` 起 | ✅ |
| tr04b → tr04c（p.71/p.72） | tr04b 末为 "这样的移动可能以如下复因子改变关联函数"；tr04c 以 (4.52) 起（原文 p.71 末 "correlation function by" / p.72 "a complex factor" 断句） | ✅ 跨页断句处理正确 |
| tr04c 末（p.76, (4.78)）→ tr-05（p.77, 4.79 之前） | tr04c 以 notebox（4.78）结束；p.77 首句为 "Note that replacing β→β+δλ (4.79)…"，tr05a 正是以该句开头 | **无重复、无缺口** ✅ |

---

## 5. 术语核对

### 5.1 块内一致性（tr04 三片）

- 上闭链（cocycle）×3（tr04a 两处、tr04c 一处）、上链（cochain）、群上链、群上同调、上同调类 —— **块内一致** ✅
- 障碍/障碍类 ×2；非阿贝尔 ×4；双基础/双重基础：本块未出现 bifundamental —— **块内一致** ✅
- 与 `glossary.tsv` 一致：背景场、规范变换、大规范变换、和乐、场强、Noether 流、规范丛、中心、单连通、Poincaré 对偶、余维、拓扑缺陷、联结（junction）、三角图、相位因子、简并真空、伴随表示、超 Yang–Mills、规范反常、SPT 相、离散 theta 角、Pontryagin 平方、拉回等 ✅

### 5.2 跨块不一致（**项目级，需 Lead 冻结 glossary**；tr04 与多数块一致，不建议单改 tr04）

| 英文 | tr04 用法 | 其它块用法 | 建议 |
|---|---|---|---|
| cocycle | **上闭链** | tr01c/tr05a 用"上闭链"；tr03/tr07b 用"上循环" | 建议定为**上闭链**（与"上链"同一词族），统一改 tr03/tr07b |
| obstruction (class) | **障碍（类）** | tr02c/tr03 用"阻碍（类）"；tr05/tr07/tr08 用"障碍" | 建议定为**障碍类**（多数块），统一改 tr02c/tr03 |
| non-Abelian | **非阿贝尔** | tr01/tr06/tr07/tr08 用"非阿贝尔"；tr02c/tr03/tr05 用"非 Abel" | 建议定为**非阿贝尔**（多数块），统一改 tr02c/tr03/tr05 |

### 5.3 本块新增术语（建议回写 `glossary.tsv`）

| 英文 | tr04 译法 |
|---|---|
| group-cochain | 群上链 |
| group cohomology | 群上同调 |
| cocycle | 上闭链 |
| pentagon identity | 五边形恒等式 |
| associator | 缔合子 |
| F-move | F-移动 |
| faithful / non-faithful symmetry | 忠实 / 非忠实对称性 |
| triangulation | 三角剖分 |
| simplex（0-/1-/i-simplex） | 单形（0-/1-/i-单形） |
| dual triangulation | 对偶三角剖分 |
| triangle diagram | 三角图 |
| pullback | 拉回 |
| counter-term / counterterm | 抵消项（块内统一） |
| bi-homomorphism | 双同态 |
| higher cup product / cup product | 高阶 cup 积 / cup 积（上积） |
| gauge bundle | 规范丛 |
| symmetry protected topological phase | 对称性保护拓扑相（SPT 相） |
| invertible TQFT | 可逆拓扑量子场论（TQFT） |

---

## 6. 必须改（附可替换文本）

| # | 位置 | 现状 | 改为 | 理由 |
|---|---|---|---|---|
| **1** | `tr04c.tex:43`（(4.56) 后的批注） | 批注断言原文"多出的 $g_{i+3}$ 破坏了指标连续性"，并称标准公式应为 $\alpha_p(\cdots,g_{i-1},g_ig_{i+1},g_{i+2},\cdots,g_{p+1})$ | **删除该错误论断**，改为：<br>`% [Tutor Note: p.72 式 (4.56) 是标准的非齐次群上链微分：乘积对 $i=1,\dots,p$ 求和，第 $i$ 项把 $g_i$ 与 $g_{i+1}$ 合并、其余下标依次为 $g_1,\dots,g_{i-1},g_ig_{i+1},g_{i+2},\dots,g_{p+1}$。原文的 $g_{i+2},g_{i+3}\cdots,g_{p+1}$ 正是 $g_{i+2},\dots,g_{p+1}$ 的展开写法，不是笔误。]` | **原文没有笔误。** "$g_{i+2},g_{i+3},\cdots,g_{p+1}$" 与 "$g_{i+2},\cdots,g_{p+1}$" 是同一数列；批注自相矛盾。**判据（可验证）**：把 (4.56) 取 $p=3$、$M=\C^\times$ 展开：领头项 $\omega(g_2,g_3,g_4)\omega(g_1,g_2,g_3)$，乘积项 $i=1,2,3$ 分别给 $\omega(g_1g_2,g_3,g_4)^{-1}$、$\omega(g_1,g_2g_3,g_4)^{+1}$、$\omega(g_1,g_2,g_3g_4)^{-1}$，正好重现原文自己的 (4.55)。 |
| **2** | `tr04c.tex:74`（(4.61) 后的批注末句） | "可用 $\Z_2$ 核对：$H^n(\Z_2,U(1))=\Z_2$ 对一切 $n\ge1$。" | 改为：<br>`可用 $\Z_2$ 核对：$H^1(\Z_2,U(1))=\Z_2$、$H^2(\Z_2,U(1))=0$、$H^3(\Z_2,U(1))=\Z_2$，即奇阶为 $\Z_2$、偶阶为 $0$（由泛系数定理 $H^n(G,U(1))\cong\operatorname{Hom}(H_n(G,\Z),U(1))$，因 $U(1)$ 可除故 $\operatorname{Ext}$ 项消失）。` | **原句数学上错误**：$H^n(\Z_2,U(1))$ 只在 $n$ 为奇数时为 $\Z_2$，偶数阶为 0。可交叉验证：论文 p.77 的 Statement 4.2 说 2d SPT 由 $H^2(G^{(0)},U(1))$ 刻画；若 $H^2(\Z_2,U(1))=\Z_2$，则 1+1 维会有 $\Z_2$ 玻色 SPT，而实际没有（$H_2(\Z_2,\Z)=0$）。 |
| **3** | `tr04c.tex:143`（(4.72) 后的批注末句） | "核对办法：$d=4$ 中 $\Z_2$ 1-形式对称性的 SPT 分类为 $H^4(B\Z_2,U(1))=\Z_2$，两个 SPT 相恰为 $s=0,1$。" | **删除该句**（其余保留）。若一定要保留，至少改为"分类空间应为 $B^2\Z_2=K(\Z_2,2)$（1-形式对称性的背景是 2-上链），其 $H^4$ 的取值需按所选系数的具体约定复核"。 | 两个问题：(i) 记号错——1-形式对称性的背景场是 **2-上链**，分类空间是 $B^2\Z_2$ 而非 $B\Z_2$；(ii) 数值存疑——$H^4(B^2\Z_2,U(1))$ 的常见值并非显然的 $\Z_2$（与 Pontryagin 平方的整提升/自旋结构有关），不能作为"核对办法"。该批注其余部分（$\cP$ 把 $\Z_2$ 2-上链映为 $\Z_4$ 4-上链、模 4 相位、$s=0,1$ 两个真空）正确，可保留。 |
| **4** | `tr04a.tex:17`（(4.4) 后的批注） | "…Noether 流取 $j^{d-1}=\star F$，即得 (4.14)…" | 改为：<br>`…把 (4.10) 中的背景 $B_{p+1}$ 换成电 1-形式背景 $B^e_2$、Noether 流取 $j^{d-p-1}=\star F$（$p=1$ 时即 $j^{d-2}=\star F$），即得 (4.14) 的 $2\pi\int B^e_2\wedge\star F$…` | **指标笔误**：$\star F$ 是 $(d-2)$-形式，对应 $p=1$ 的 $j^{d-p-1}=j^{d-2}$；而 $j^{d-1}$ 是 (4.4) 中 0-形式对称性的流，不能张冠李戴。原批注把 (4.4) 与 1-形式情形混用了。 |

> 除以上 4 条批注外，**未发现必须修改的公式、正文译文、结构或漏译问题**。

---

## 7. 可选改（附可替换文本，不影响验收）

| # | 位置 | 现状 | 建议 | 理由 |
|---|---|---|---|---|
| 1 | `tr04a.tex:106`、`tr04a.tex:135` | `\para{非阿贝尔规范理论的电 1-形式对称性}` / `\para{非阿贝尔规范理论的磁 $(d-3)$-形式对称性}`（**无句号**） | 末尾补"。" | 与全文另外 13 个 `\para` 体例统一（原文这两个标题本身不带句点，但中文体例宜统一）。 |
| 2 | `tr04c.tex:138`、`tr04c.tex:143` | "第 3.193 式附近" | "式 (3.193) 附近" | 项目公式引用体例是"式 (N.M)"（STYLE_GUIDE §3）。 |
| 3 | `tr04a.tex:164`（例 4.4 跨页批注） | "末句 … 位于 p.65 页顶" | "末句 … 位于 p.65（在图 12 之后）" | 实际在 p.65 中部、图 12 图注之下，不是"页顶"；描述更精确。（该方框合并本身正确。） |
| 4 | `tr04a.tex` 例 4.4 合并顺序 | 合并后的方框整体排在 `% [原文 p.65]` 与图 12 **之前**（图 12 在方框之后） | 可不动；若要严格复刻 p.65 版面，可把 `figure` 环境移到 examplebox 之前 | 原文 p.65 顶端是图 12、其下方才是方框末句；因 `figure` 是浮动体，编译结果通常会自动回到页顶，实际无影响。 |
| 5 | `tr04c.tex:58`（图 16 图注） | 图注末尾无句号（"…就得到式 (4.55)"） | 末尾加"。" | 与其余 4 条图注体例一致。 |
| 6 | `tr04c.tex:12–17`（Definition 4.3 标题与正文） | 标题"群上链"，正文"$p$-群上链 $\alpha_p$" | 首现处加英文：`$p$-群上链（p-group-cochain）` | 术语首现给原词（STYLE_GUIDE §5）。非强制。 |
| 7 | `tr04b.tex:129`（(4.49)/(4.45) 的批注） | "$s(p)=(-1)^p$ … 是为离散情形中 $\cup$ 积的分次交换符号服务的约定：$p$ 的奇偶决定 (4.45) 的相位相对 (4.48) 的符号。" | 可把"分次交换符号"写具体：`(4.45) 与 (4.48) 相差的符号来自把 $\Lambda^e_p$ 从 $\cup_\eta$ 左侧移到右侧时分次交换给出的 $(-1)^{p}$` | 现有表述含糊但不错；改为可核对的表述更好。 |

---

## 8. 自动检查（脚本结果，供 Lead 复核）

| 文件 | 行数 | tag 数 | 首–尾 | BOM | CRLF | U+FFFD | `**` | 花括号 | `$` 成对 | begin/end | 禁用命令 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| tr04a.tex | 214 | 31 | 4.3–4.33 | 无 | 无 | 0 | 0 | 253/253 | ✅（364） | 全配平 | 无 |
| tr04b.tex | 158 | 18 | 4.34–4.51 | 无 | 无 | 0 | 0 | 185/185 | ✅（132） | 全配平 | 无 |
| tr04c.tex | 177 | 27 | 4.52–4.78 | 无 | 无 | 0 | 0 | 193/193 | ✅（226） | 全配平 | 无 |

- 禁用命令检查项：`\documentclass`、`\usepackage`、`\begin{document}`、`\newcommand`、`\ref{}`、`\eqref`、`\cite{}`、`$$` —— 全部为 0 ✅。
- 宏检查：仅使用 preamble 已定义宏（`\cG \cO \cT \cZ \cN \cP \cS \cW \fsu \fg \dd \ii \R \Z \C` 等）+ 标准命令，未发现未定义宏 ✅。
- 批注数量：17 条 / 16 页（分布：4.1 的 tr04 部分 6 条、4.2.1 节 6 条、4.2.2 节 5 条），p.61–76 每 2–3 页 ≥1 条、每小节 ≥3 条 ✅；其中 4 条需按 §6 修正。

---

*报告完毕。仅写报告，未修改 tr-04 的任何文件；未被要求、也未对 tr-04 执行编译。*
