# tr07 交叉校对报告（原文 pp.109–124，tag 4.256–5.59，图 21–27）

- 校对者：tr-06（本人块为 pp.93–108、tag 4.185–4.255）
- 对象：`work/src/chunks/tr07a.tex`（pp.109–112）、`tr07b.tex`（pp.113–118）、`tr07c.tex`（pp.119–124）
- 方法：逐页对照 `work/split/pNNN.txt`（定位段落/句子）+ `work/pages/pNNN.png`（1700×2200，200 dpi）；指定的重点公式另用 `work/tools/crop.py` 以 700 dpi 裁图逐符号比对；编号用脚本对 `work/tags_bypage.txt` 逐页比对；结构用脚本统计环境/页标注/图题。
- 约束遵守：**未修改任何他人文件、未编译**（只读比对 + 批注文本建议）。

---

## 一、结论摘要

1. **编号完整性：71/71 完全匹配。** 逐页与 `tags_bypage.txt`（p109–p124）一致，无缺、无重、无跳号，文件内顺序递增；分片边界 a: 4.256–4.260、b: 4.261–5.20、c: 5.21–5.59 与 tr-06（止于 4.255）、tr-08（起于 5.60）严格衔接。
2. **公式正确性：抽查 36 条（含全部指定优先项）逐符号核对，未发现公式错误。** 上下标、撇号/帽子/波浪号、`\mathcal` vs 普通体、≇ 与 ≠、`\cup_\eta`、`\longmapsto`、多行公式的单 tag 归属均正确。
3. **结构正确。** 8 个标题（§5、5.1、5.2、5.2.1、5.2.2、5.2.3、5.3、5.3.1）层级与页位全部符合 BRIEF/TIMELINE；图 21–27 共 7 张齐全且都落在原书对应页首；8 个方框颜色/类型正确（橙=examplebox、粉=notebox、绿=definitionbox）；**例 5.3 跨文件开框/闭合配对正确，内容边界无重复、无丢失**。
4. **漏译：未发现。** 17 个行内粗体小标题全部转成 `\para{}`；7 处图引用、全部 `[nnn]` 文献引用、"See figure 23/24（各两处）/25/26/27/21/22" 全部在位；逐页比对未发现段落或句子缺失。
5. **主要问题集中在批注（Tutor Note）：4 条存在事实性错误**（不影响 PDF 排版，但会进入《译注汇总.md》，读者可见），已给可替换文本（见 §七 A）；另有若干术语/格式与强调范围的可选修正（§七 B）。
6. 备注：tr07a 只覆盖 4 页（109–112），tr07b/tr07c 各 6 页；不影响正确性，仅与"每片 5–6 页"的约定略有出入，供 Lead 拼装时参考。

---

## 二、编号完整性表（逐页）

| 页 | `tags_bypage.txt` 应收 | tr07 实际（所在文件） | 结论 |
|---|---|---|---|
| 109 | 4.256 | 4.256（a） | 一致 |
| 110 | 4.257, 4.258 | 4.257, 4.258（a） | 一致 |
| 111 | 4.259, 4.260 | 4.259, 4.260（a） | 一致 |
| 112 | （无） | （无） | 一致（该页为图 24 与正文，无编号公式） |
| 113 | 4.261, 4.262, 4.263 | 4.261, 4.262, 4.263（b） | 一致 |
| 114 | 4.264, 4.265, 4.266, 4.267 | 4.264–4.267（b） | 一致 |
| 115 | 5.1, 5.2, 5.3 | 5.1, 5.2, 5.3（b） | 一致（含 TIMELINE 特批的手工补录 5.1） |
| 116 | 5.4–5.9 | 5.4–5.9（b） | 一致 |
| 117 | 5.10–5.17 | 5.10–5.17（b） | 一致 |
| 118 | 5.18, 5.19, 5.20 | 5.18, 5.19, 5.20（b） | 一致 |
| 119 | 5.21–5.24 | 5.21–5.24（c） | 一致 |
| 120 | 5.25–5.32 | 5.25–5.32（c） | 一致 |
| 121 | 5.33–5.36 | 5.33–5.36（c） | 一致 |
| 122 | 5.37–5.43 | 5.37–5.43（c） | 一致 |
| 123 | 5.44–5.47 | 5.44–5.47（c） | 一致 |
| 124 | 5.48–5.59 | 5.48–5.59（c） | 一致 |
| **合计** | **71** | **71**（a=5, b=27, c=39） | **一致** |

- 顺序：`4.256 … 4.267 → 5.1 … 5.59`，逐文件单调递增；无重复 tag；无自造编号。
- 环境：`equation` 70 个 + `align` 1 个（(5.26)，首行 `\nonumber`、末行 `\tag`），共 71 个 tag，与 71 条编号公式一一对应。
- 本段（pp.109–124）原文没有无编号的展示公式，因此不存在"该排 `\[…\]` 却加了编号"或反过来的情况。

---

## 三、逐符号核对表（抽查 36 条 / 41 个公式）

说明：表格"原文（图像）"列为按 200 dpi 页面图或 700 dpi 裁图逐符号读出的原式；"tr07 源码"为节录。判定均为"无误"者不再单列理由。

| # | 式号 | 页 | 原文（图像逐符号） | tr07 源码（节录） | 判定 |
|---|---|---|---|---|---|
| 1 | 4.256 | 109 | 𝒮 = ∏_{i=1}^{n} G^{(p_i)} | `\cS=\prod_{i=1}^{n}G^{(p_i)}` | 无误 |
| 2 | 4.257 | 110 | 𝓘_{d+1}[A_{p₁+1},A_{p₂+1},⋯,A_{p_n+1}] = exp(i∫ℒ^{eff}_{d+1}[…]) | `\cI_{d+1}[A_{p_1+1},…]=\exp\left(\ii\int\cL^{\mathrm{eff}}_{d+1}[…]\right)` | 无误（700 dpi 复核） |
| 3 | 4.258 | 110 | ∑_{i=1}^{n} 2π∫ a_{p_i+1} ∪_η δb_{d−p_i−1} + ∫ℒ^{eff}_{d+1}[…] | `\sum_{i=1}^{n}2\pi\int a_{p_i+1}\cup_\eta\delta b_{d-p_i-1}+\int\cL^{\mathrm{eff}}_{d+1}[…]` | 无误（700 dpi 复核） |
| 4 | 4.259 | 111 | a_{p_i+1} → A_{p_i+1} | `a_{p_i+1}\to A_{p_i+1}` | 无误 |
| 5 | 4.260 | 111 | U_{ĝ_i}=∫ĝ_i(a_{p_i+1}), ĝ_i∈Ĝ^{(p_i)}；U_{g_i}=∫b_{d−p_i−1}(g_i), g_i∈G^{(p_i)} | `U_{\hat g_i}=\int\hat g_i(a_{p_i+1})`, `\hat g_i\in\widehat{G}^{(p_i)}`；`U_{g_i}=\int b_{d-p_i-1}(g_i)`, `g_i\in G^{(p_i)}` | 无误（双行单 tag） |
| 6 | 4.261 | 113 | 2π∫ a_{p+1} ∪_η δb_{d−p−1} | `2\pi\int a_{p+1}\cup_\eta\delta b_{d-p-1}` | 无误 |
| 7 | 4.262 | 113 | 𝒯′ = 𝒯/G^{(p)} | `\cT'=\cT/G^{(p)}` | 无误 |
| 8 | 4.263 | 113 | G^{(d−p−2)} = Ĝ^{(p)} | `G^{(d-p-2)}=\widehat{G}^{(p)}` | 无误 |
| 9 | 4.264 | 114 | δb_{d−p_i−1} = f_i[a_{p₁+1},a_{p₂+1},⋯,a_{p_n+1}] | `\delta b_{d-p_i-1}=f_i[a_{p_1+1},…,a_{p_n+1}]` | 无误 |
| 10 | 4.265 | 114 | 𝓘_{d+1}[A₂^e,A_{d−2}^m] = exp(πi∫A_{d−2}^m ∪ Bock(A₂^e)) | `\cI_{d+1}[A_2^e,A_{d-2}^m]=\exp\left(\pi\ii\int A_{d-2}^m\cup\operatorname{Bock}(A_2^e)\right)` | 无误（πi，非 2πi） |
| 11 | 4.266 | 114 | π∫(a₂^e∪δb_{d−2}^e + a_{d−2}^m∪δb₂^m + a_{d−2}^m∪Bock(a₂^e)) | 同左，`\pi\int\left(…\right)` | 无误 |
| 12 | 4.267 | 114 | δb₂^m = Bock(a₂^e) | `\delta b_2^m=\operatorname{Bock}(a_2^e)` | 无误 |
| 13 | 5.1 | 115 | W[B_{p+1}+dΛ_p, B_{d−2p−3}+dΛ_{d−2p−4}] = W[…] + 2πκ∫Λ_p∧H_{p+2}∧H_{d−2p−2} | 同左（`\dd\Lambda`、`\wedge`） | 无误 |
| 14 | 5.2 | 115 | j^{d−2p−2} = H_{d−2p−2} | `j^{d-2p-2}=H_{d-2p-2}` | 无误 |
| 15 | 5.3 | 115 | 2π∫ B_{2p+2} ∧ H_{d−2p−2} | `2\pi\int B_{2p+2}\wedge H_{d-2p-2}` | 无误 |
| 16 | 5.4 | 116 | B_{2p+2} → B_{2p+2}+dΛ_{2p+1}−κΛ_p∧H_{p+2} | 同左 | 无误 |
| 17 | 5.6 | 116 | H_{2p+3} = dB_{2p+2} + κB_{p+1}∧H_{p+2} | 同左 | 无误 |
| 18 | 5.7 | 116 | dH_{2p+3} = κH_{p+2}∧H_{p+2} | `\dd H_{2p+3}=\kappa H_{p+2}\wedge H_{p+2}` | 无误 |
| 19 | 5.10 | 117 | G^{(0)} ≇ H^{(0)}×K^{(0)} | `G^{(0)}\ncong H^{(0)}\times K^{(0)}` | 无误（≇ 用 `\ncong`） |
| 20 | 5.12 | 117 | g₁+g₂ = (h₁+h₂+e(k₁,k₂), k₁+k₂) | 同左 | 无误 |
| 21 | 5.16 | 117 | [e] ∈ H²(K^{(0)},H^{(0)}) | `[e]\in H^2(K^{(0)},H^{(0)})` | 无误 |
| 22 | 5.18 | 118 | δB₁^H = (B₁^K)^* e | `\delta B_1^H=\left(B_1^K\right)^*e` | 无误 |
| 23 | 5.19 | 118 | δB_{p+1} + Θ(B_{p₁+1},B_{p₂+1},⋯B_{p_n+1}) = 0 | 同左（原文省略末项前逗号，译文照抄） | 无误 |
| 24 | 5.20 | 118 | [Θ] ∈ H³(G^{(0)},G^{(1)}) | `[\Theta]\in H^3\left(G^{(0)},G^{(1)}\right)` | 无误 |
| 25 | 5.22 | 119 | 𝔊^{(2)} = {G^{(0)},G^{(1)},ρ,[Θ]} | `\mathfrak{G}^{(2)}=\big\{G^{(0)},G^{(1)},\rho,[\Theta]\big\}` | 无误（花括号 + Fraktur） |
| 26 | 5.24 | 119 | [Θ] ∈ H³_ρ(G^{(0)},G^{(1)}) | `[\Theta]\in H^3_\rho\left(…\right)` | 无误 |
| 27 | 5.26 | 120 | δ_ρ α_p(g₁,…,g_{p+1}) = ρ(g₁)·α_p(g₂,…,g_{p+1})·α_p^{s(p+1)}(g₁,…,g_p)·∏_{i=1}^{p}α_p^{s(i)}(…, g_i g_{i+1}, …) | `align`：首行 `\nonumber`，第二行 `\prod_{i=1}^{p}\alpha_p^{s(i)}(…,g_ig_{i+1},…)`，末行 `\tag{5.26}` | 无误（700 dpi 复核；单 tag 在末行，符合 STYLE §3） |
| 28 | 5.30–5.32 | 120 | G^{(1)}=ℤ_N；G^{(0)}=ℤ₂；p ⟼ −p, p∈{0,1,…,N−1} | `G^{(1)}=\Z_N`；`G^{(0)}=\Z_2`；`p\longmapsto-p,\quad p\in\{0,1,2,\cdots,N-1\}` | 无误（用 `\longmapsto` 与原图一致） |
| 29 | 5.34 | 121 | 𝓘_{d+1} = exp(−2πi s(d−p)∫B_{d−p−1}∪_ηΘ(B_{p₁+1},…,B_{p_n+1})), s(d−p)=(−1)^{d−p} | 同左 | 无误 |
| 30 | 5.37 | 122 | BG := EG/G | `BG:=EG/G` | 无误 |
| 31 | 5.44 | 123 | G^{(0)} = F/𝒵 | `G^{(0)}=F/\mathcal{Z}` | 无误（花体 𝒵，非 ℤ） |
| 32 | 5.45 | 123 | 𝒵 = Subgroup of Z(F) leaving all local operator representations R_i invariant. | `\mathcal{Z}=\text{保持所有局域算符表示 }R_i\text{ 不变的 }Z(F)\text{ 的子群}\,` | 无误（700 dpi 复核；Z(F) 普通体 vs 𝒵 花体区分正确） |
| 33 | 5.46 | 123 | (q_i^g,q_i^f) ∈ Ẑ(𝒢)×Ẑ(F) | `\left(q_i^g,q_i^f\right)\in\widehat{Z}(\mathcal{G})\times\widehat{Z}(F)` | 无误（帽号全对） |
| 34 | 5.48 / 5.49 | 124 | Q_genuine = Q∩Ẑ(F) ⊆ Ẑ(F)；𝒵̂ = Ẑ(F)/Q_genuine | `Q_{\mathrm{genuine}}=Q\cap\widehat{Z}(F)\subseteq\widehat{Z}(F)`；`\widehat{\mathcal{Z}}=\frac{\widehat{Z}(F)}{Q_{\mathrm{genuine}}}` | 无误（700 dpi 复核） |
| 35 | 5.54 / 5.55 | 124 | Ẑ(𝒢)×Ẑ(F)=ℤ×ℤ₂；Q=⟨(2,1)⟩∈ℤ×ℤ₂ | `\widehat{Z}(\mathcal{G})\times\widehat{Z}(F)=\Z\times\Z_2`；`Q=\langle(2,1)\rangle\in\Z\times\Z_2` | 无误 |
| 36 | 5.59 | 124 | 𝒢 = Spin(4N+2) | `\mathcal{G}=\Spin(4N+2)` | 无误 |

补充核查（未单列行）：4.256 前的 (4.256) 符号 𝒮；5.8（`H_{p+2}=dB_{p+1}+Θ(…)`）、5.9、5.11、5.13–5.15、5.17、5.21、5.23、5.25、5.27–5.29、5.33、5.35、5.36、5.38–5.43、5.47、5.50–5.53、5.56–5.58 亦逐条对照页面图，未见符号级差异。

**结论：本块 71 条编号公式无一处需要改动。**

---

## 四、结构

### 4.1 标题（全部由 tr-07 写，层级/位置正确）

| 原文页 | 原文标题 | tr07 写法（文件:行） | 结论 |
|---|---|---|---|
| p.114 | 5 Higher-Group Symmetries | `\section{高阶群对称性}`（b:63） | 正确；位于例 4.19 方框之后、p.115 页标注之前，与原书一致 |
| p.115 | 5.1 Continuous Higher-Group Symmetries | `\subsection{连续高阶群对称性}`（b:73） | 正确 |
| p.116 | 5.2 Discrete Higher-Group Symmetries | `\subsection{离散高阶群对称性}`（b:125） | 正确 |
| p.116 | 5.2.1 Motivation: Group Extension | `\subsubsection{动机：群扩张}`（b:127） | 正确 |
| p.118 | 5.2.2 General Structure | `\subsubsection{一般结构}`（b:192） | 正确 |
| p.121 | 5.2.3 Relationship to Mixed 't Hooft Anomalies | `\subsubsection{与混合 't Hooft 反常的关系}`（c:84） | 正确 |
| p.121 | 5.3 Mixed Continuous-Discrete 2-Group Symmetries | `\subsection{混合连续-离散 2-群对称性}`（c:99） | 正确 |
| p.122 | 5.3.1 Global Form of 0-Form Symmetries | `\subsubsection{0-形式对称性的全局形式}`（c:146） | 正确 |

- 没有越权写 5.3.2（Bockstein 2-群，p.125，属 tr-08）或其它块标题；全库标题扫描确认 tr07 的 8 个标题不与任何其它 chunk 重复。
- 行内粗体小标题 17 个全部用 `\para{}`：夹心构造、高阶形式对称性的 SymTFT、规范化作为边界条件的改变、规范化的障碍、例：规范化混合 't Hooft 反常、一般结构、群扩张的扩张类、用拓扑算符解释、对背景场的含义、高阶群、2-群、更一般的 2-群、分裂 2-群、0-形式对称代数、0-形式对称群、0-形式对称丛、规范理论中的味对称群（其中若干为同名小节内的多个 `\para`）。

### 4.2 图（7/7 齐全，页位与原书一致）

| 图 | 原书页 | tr07 位置 | `\includegraphics` 宽度 | 图注核对 | 结论 |
|---|---|---|---|---|---|
| 21 | p.109 | a:3–7（页首） | 0.86 | "夹心构造……Y 形联结……局域在 𝔅^sym_𝒮 上" | 无误 |
| 22 | p.110 | a:31–35（页首） | 0.92 | "通过在 (d+1) 维中规范化（gauging）𝒮 构造" | 无误 |
| 23 | p.111 | a:62–66（页首） | 0.90 | "体拓扑算符被推向对称性边界时的命运" | 无误 |
| 24 | p.112 | a:86–90（页首） | 0.72 | "沿区间紧致化 $U_{\hat g_i}$ 产生带电算符 $\cO_{\hat g_i}$" | 无误 |
| 25 | p.113 | b:3–7（页首） | 0.86 | "另一个拓扑边界条件 𝔅^sym_{𝒮′} 的夹心构造" | 无误 |
| 26 | p.118 | b:178–182（页首） | 0.60 | "用 $K^{(0)}$（蓝）与 $H^{(0)}$（红）的拓扑余维-1 算符表示群扩张 (5.9)" | 无误 |
| 27 | p.119 | c:3–7（页首） | 0.96 | "余维-1 算符作用于余维-2 算符，把 $\gamma$ 变为 $\rho(g)\cdot\gamma$" | 无误 |

- 文件名 `fig21.png`–`fig27.png` 与 `work/figures/` 中实物一一对应，无路径前缀、无图注编号错位。
- 正文 9 处图引用全部保留（原书分布：p.109 "See figure 21"；p.110 "See figure 22"；p.112 "See figure 23" 与两处 "See figure 24"；p.113 "See figure 25"；p.117 "See figure 26"；p.119 "See figure 27"）。

### 4.3 方框（8/8，类型与颜色全部正确）

| 原书页 | 方框 | tr07 环境（文件:行） | 结论 |
|---|---|---|---|
| p.113–114 | Example 4.18: Gauging a Higher-Form Symmetry（橙色，跨页） | `examplebox`（b:11–35，已合并为一个框） | 正确；合并后 (4.261)–(4.263) 只出现一次 |
| p.114 | Example 4.19: Pure SO(6) Yang-Mills theory（橙） | `examplebox`（b:45–59） | 正确 |
| p.120 | Twisted Group Cohomology（粉，带标题条） | `notebox`（c:32–54） | 正确 |
| p.120 | Example 5.1: Charge Conjugation in Pure SU(N) Yang-Mills（橙） | `examplebox`（c:64–79） | 正确 |
| p.121–122 | Classifying Spaces（粉，跨页） | `notebox`（c:115–140，已合并） | 正确 |
| p.123 | Definition 5.1: 0-Form Symmetry Group（绿） | `definitionbox`（c:171–177） | 正确 |
| p.124 | Example 5.2: Abelian Gauge Theory（橙） | `examplebox`（c:214–251） | 正确 |
| p.124–125 | Example 5.3: Non-Abelian Gauge Theory（橙，**跨文件**） | `examplebox` 开（c:255），闭（tr08a:48） | 正确 |

### 4.4 「例 5.3」跨文件开框专项核查（Lead 点名项）

- **开框处**：`tr07c.tex:255` `\begin{examplebox}{例 5.3：非阿贝尔规范理论}`；框内正文到 `\mathcal{G}=\Spin(4N+2)\,, \tag{5.59}` 为止，文件以两行注释（说明由 tr-08 续写）结束，**没有** `\end{examplebox}`。
- **闭合处**：`tr08a.tex` 开头 `% [跨页方框续：…]` 注释后，正文从"它有"（原文 p.125 "which has"）接 (5.60)，经 (5.61)–(5.69)，于 `tr08a.tex:48` `\end{examplebox}` 闭合。
- **内容边界核对（对 p.124/p.125 页面图与 split）**：
  - 原书 p.124 框内最后一句 = "Consider a d-dimensional non-abelian gauge theory with gauge group [𝒢=Spin(4N+2)]"；p.125 接 "which has [Ẑ(𝒢)=ℤ₄]"。译文把"其规范群为"留在 tr07c、把"它有 Ẑ(𝒢)=ℤ₄"作为 tr08a 首句——**句子被正确切成两半，无重复、无丢失**。
  - 方框标题只在 tr07c 出现一次，tr08a 未重复标题；(5.59) 在 c、(5.60)–(5.69) 在 tr08a，编号连续无重叠。
  - 唯一的风格提示：该框的 `\end{examplebox}` 跨文件，单看 tr07c 不是自洽 LaTeX 片段；既然 Lead 已确认拼接后编译通过，且注释里写明原委，**无需改动**。
- **结论：配对正确，边界内容无重复/丢失。**

### 4.5 页标注与分片

- 页标注 `% [原文 p.N]`：**16/16 齐全**（109,110,…,124），单调递增，每页一条；p.112（无公式）也有标注。
- 分片头：`% ===== 原文 pp.109–112 =====`、`pp.113–118`、`pp.119–124`，格式与 STYLE_GUIDE §9 一致；三片覆盖 109–124 无缝隙、无重叠。
- 两处页标注位于跨页方框内部（b:33 在例 4.18 框内、c:119 在"分类空间"框内）。这是跨页方框的必然结果，可接受；若追求整洁可移到方框外（可选，见 §七 B-O9）。
- 编码：三片均 UTF-8 无 BOM、LF 换行、无 U+FFFD；花括号 826/826 平衡；三片内除了 c 片按设计留下的 `examplebox` 之外，所有 `\begin/\end` 均平衡（`figure` 4+2+1=7、`itemize` 2+1+1、`equation` 5+27+38、`align` 1、`notebox` 2、`definitionbox` 1、`examplebox` 3 开 / 2 闭）。

---

## 五、漏译

**未发现漏译。** 依据：

1. 以 `split/pNNN.txt` 为对照逐页通读，pp.109–124 的每个自然段、每个句子在译文中都有对应；连词/插入语（"Naively"、"Note that"、"Indeed"、"Said differently"）均有译出。
2. 17 个原文行内粗体小标题全部落地为 `\para{}`（清单见 §4.1）。
3. 全部图引用与 "See figure 23."（p.112 页首那句被浮动图隔开的话）都保留；后者 tr07a:96 还专门加了批注解释，处理得很好。
4. 全部文献引用在位：`[60]`(p.110)、`[183]`(p.115)、`[181–184]`、`[185–187]`、`[188–206]`(p.115)、`[186,188]`(p.122)、`[198]`(p.123)、`[207]`(p.122)。
5. 原文的强调（粗体/斜体）基本都还原：`\textbf{Dirichlet}`、`\textbf{Neumann}`、`\textbf{Postnikov 类}`、`\textbf{Bockstein 2-群}`、`\textbf{0-形式对称群}`、`\textbf{扭化群上同调}`、`\textbf{分裂 2-群}` 等。
6. 唯一强调范围的小差异：p.116 原文粗体覆盖 "**2-group symmetry**" 整个短语，译文只粗体化了 "2-群"，见 §七 B-O6（不影响语义）。

---

## 六、术语

### 6.1 与 glossary 一致（核对通过）

高阶群对称性（higher-group symmetry）、2-群（2-group）、Bockstein 2-群、夹心构造（sandwich construction）、对称性拓扑场论/SymTFT、分类空间（classifying space）、主丛（principal bundle）、群上同调（group cohomology）、上链（cochain）、离散挠率（discrete torsion）、联结（junction）、全局形式（global form of the gauge group）、单连通（simply connected）、忠实（faithful）、味对称（flavor symmetry，与 tr08 一致）、中心荷、障碍类（与 tr04/tr05/tr08 一致）、规范化（gauging）、SPT 相、't Hooft 反常、Green–Schwarz 机制、ABJ 反常、Pontryagin 对偶。

### 6.2 需要统一的差异（详见 §七 B）

| 英文 | tr07 用法 | 其它块用法 | 建议 |
|---|---|---|---|
| cocycle | **上循环**（tr07b 4 处；tr03a 1 处） | **上闭链**（tr01c 3 处、tr04a 2 处、tr04c、tr05a；tr04a 明确写成"上闭链（cocycle）"） | 全书统一为**上闭链**（多数派且已有英文对照） |
| twisted (cohomology) | **扭化**群上同调（tr07c 5 处） | 其它地方 twisted→**扭曲**（扭曲扇区/扭曲边界条件） | 建议保留"扭化群上同调"（数学惯例），但写入 glossary 说明与"扭曲"的分工 |
| Bockstein homomorphism | 只写 `\operatorname{Bock}`（未给中文名） | tr08a 用"Bockstein **映射**"；glossary 定为"Bockstein **同态**" | 统一；建议 glossary 增补 "Bockstein map → Bockstein 映射" 或把 tr08a 改为"同态" |

### 6.3 建议新增进 glossary 的术语（tr07 引入）

对称性边界条件（symmetry boundary condition）、物理边界条件（physical boundary condition）、扭转群上同调/扭化群上同调（twisted group cohomology）、Postnikov 类（Postnikov class）、分裂 2-群（split 2-group）、上闭链（cocycle）、万有 G-丛（universal G-bundle）、区间紧致化（interval compactification）、味对称代数/味对称群（flavor symmetry algebra/group）、中心荷（center charge）、离散高阶形式规范理论（discrete higher-form gauge theory）、0-形式对称代数（0-form symmetry algebra）。

---

## 七、问题清单

### A. 必须改（4 项，均为 Tutor Note 事实性错误；不影响 PDF，但会进《译注汇总.md》）

> 说明：以下只提供"可替换文本"，请 tr-07 或 Lead 自行落地；我未改动他人文件。

**M1. `tr07b.tex:94`（(5.1) 的次数批注写反了）**
- 问题：批注说"该项只在 $d+1$ 维中可积（$p+(p+2)+(d-2p-2)=d$）"——自己算出的次数是 $d$，与"$d+1$ 维"矛盾。Λ_p∧H_{p+2}∧H_{d−2p−2} 是 d-形式，正是 d 维规范变换的相位。
- 可替换文本：
```latex
% [Tutor Note: 式 (5.1) 右端第一项是 $W[B_{p+1},B_{d-2p-3}]$ 的规范变换「原样」，反常是第二项 $2\pi\kappa\int\Lambda_p\wedge H_{p+2}\wedge H_{d-2p-2}$。次数核对：$p+(p+2)+(d-2p-2)=d$，故该项是 $d$-形式，恰是 $d$ 维有效作用量 $W$ 在一次规范变换下产生的相位（不是 $(d+1)$-形式）。把同一反常写成 $(d+1)$ 维反常理论/SymTFT 作用量的形式见 §4.2.3 与 (4.197)。]
```

**M2. `tr07c.tex:56`（(5.26) 的 $s(i)$ 并非"未定义"）**
- 问题：批注称"原文始终未定义符号 $s(i)$"，但原文在 **(4.46)（p.70）** 明确定义 $s(n):=(-1)^n$，并在 **Definition 4.4 的 (4.56)（p.72）** 中用它写出普通（未扭化）群上链微分，其后还有"where $s(n)=(-1)^n$, i.e. we take $\alpha_p$ for even $i$ and $\alpha_p^{-1}$ for odd $i$"。因此 (5.26) 只是 (4.56) 的 $\rho$-扭化版本，不能称"未定义"。
- 可替换文本：
```latex
% [Tutor Note: 符号 $s(i)$ 在 (4.46)（p.70）已定义为 $s(n):=(-1)^n$；(5.26) 正是把 Definition 4.4 的普通群上链微分 (4.56)（p.72）换成 $\rho$-扭化版本，原文 (4.56) 后还注明「where $s(n)=(-1)^n$, i.e. we take $\alpha_p$ for even $i$ and $\alpha_p^{-1}$ for odd $i$」。核对：取 $\rho=1$ 时 (5.26) 退化为 (4.56)。]
```

**M3. `tr07c.tex:113`（(5.35)/(5.21) 中 $B_1$ 说成了 $K^{(0)}$ 的背景场）**
- 问题：(5.21) 的 $B_1$ 是 **$G^{(0)}$ 0-形式对称性**的背景场（原文："where $B_1$ is the background field for 0-form symmetry"）。$K^{(0)}$ 的背景场只出现在 §5.2.1 的 (5.18)（记作 $B_1^K$）。批注把两者混淆。
- 可替换文本：
```latex
% [Tutor Note: (5.35) 与离散情形的 (5.21) 形式相同，区别在 $B_1$ 的取值与 $\Theta$ 的系数域：(5.21) 中 $B_1$ 是 0-形式对称群 $G^{(0)}$ 的背景场（$G^{(0)}$ 取值的 1-上链，或等价地 $M\to BG^{(0)}$ 的映射）；$K^{(0)}$ 的背景场 $B_1^K$ 只出现在 §5.2.1 的 (5.18)。连续情形下 $B_1$ 是主丛的分类映射，于是 $\Theta$ 的系数域从群上同调 $H^3(G^{(0)},G^{(1)})$ 变为分类空间上同调 $H^3(BG^{(0)},G^{(1)})$（对照 (5.20) 与 (5.36)）。]
```

**M4. `tr07b.tex:190`（(5.18) 的次数写错）**
- 问题：批注说"$\delta B_1^H$（3-形式上链）与 $e$ 的次数（2）相差 1，需用 $\delta$ 而非 $\dd$"。实际 $B_1^H$ 是 1-上链，$\delta B_1^H$ 是 **2-上链**；$(B_1^K)^*e$ 也是 2-上链（$e$ 是 $H^{(0)}$-值 2-上链）。两边次数相同，不存在"相差 1"；用 $\delta$ 是因为离散群背景场用群上链微分。
- 可替换文本：
```latex
% [Tutor Note: (5.18) 的次数：$B_1^H$ 是取值于 $H^{(0)}$ 的 1-上链，故 $\delta B_1^H$ 是 2-上链；$B_1^K$ 是取值于 $K^{(0)}$ 的 1-上链（等价于映射 $M\to BK^{(0)}$），$e$ 是 $K^{(0)}$ 上的 $H^{(0)}$-值 2-上链，拉回 $(B_1^K)^*e$ 也是 2-上链，两边次数相同。这里用群上链微分 $\delta$ 而非 $\dd$，是因为背景场是离散群取值的上链。核对：图 26 中红线的端点（源）由蓝线交点的余维-2 联结给出。]
```

### B. 可选改（8 项；给出可替换文本或建议）

**O1. `tr07b.tex:69`（"$n$-群 / Postnikov 塔"截断层数疑似差一）**
- 现文："这与「$n$-群」的一般定义（Postnikov 塔在 $n+1$ 层截断）一致"。
- 建议：$n$-群对应 Postnikov 塔在**第 $n$ 层**截断（$\pi_k=0\ (k>n)$）；最高参与形式为 $r$ 时群为 $(r+1)$-群（$\pi_{r+1}\neq0$）。可替换为：
```latex
% [Tutor Note: §5 的「(r+1)-群」命名规则：参与混合的对称性最高形式次数为 $r$，则群称为 $(r+1)$-群；这与「$n$-群」的一般定义（Postnikov 塔在第 $n$ 层截断，即 $\pi_k=0\ (k>n)$）一致。核对：只含 0-形式与 1-形式时 $r=1$，故为 2-群（$\pi_1=G^{(0)},\pi_2=G^{(1)}$），与 5.2.2 的 2-群定义相符。]
```

**O2. `tr07c.tex:97`（(5.34) 中 $s(d-p)$ 的"来历"解释不严谨）**
- 现文："$(d-p)$ 维中交换两个算符需要 $(-1)^{d-p}$ 的交换因子，故反常的符号随维数奇偶而变。"该机制未经原文支持（原文只是符号约定）。
- 建议改为安全的说法：
```latex
% [Tutor Note: (5.34) 是群扩张结论 (4.194)→(4.197) 的高阶形式版本：规范化 $G^{(p)}$ 后，原高阶群的「不闭合」信息 (5.19) 变成对偶 $(d-p-2)$-形式对称性的混合 't Hooft 反常。符号 $s(d-p)$ 即 (4.46)（p.70）定义的 $s(n):=(-1)^n$，只依赖 $d-p$ 的奇偶性；其出现位置与 (4.197) 完全一致。]
```

**O3. `tr07b.tex:208`（"3-类"非原文术语）**
- 现文结尾："……这是「2-群 ↔ $H^3$」的来历，也是把 Postnikov 类称为「3-类」的原因。"——原文未用"3-类"这一说法。
- 建议删去"也是把 Postnikov 类称为「3-类」的原因"，或改为"（即 Postnikov 类落在 3 次上同调）"。

**O4. 术语统一：上循环 → 上闭链（tr07b 共 4 处：151、171、198、208 行）**
- 依据：全库扫描显示 tr01c/tr04a/tr04c/tr05a 用"上闭链"，tr04a 还直接写"上闭链（cocycle）"；tr03a 有 1 处"上循环"。
- 可替换：`2-上循环`→`2-上闭链`、`$(p+2)$-上循环`→`$(p+2)$-上闭链`、`3-上循环`→`3-上闭链`，以及 `\para{用拓扑算符解释。}上循环 $e$`→`上闭链 $e$`。

**O5. glossary 增补"扭化"条目**
- tr07c 用"扭化群上同调"（twisted group cohomology）与"被 $\rho$ 扭化"，与全书的"扭曲扇区/扭曲边界条件"（twisted sector/b.c.）分工不同。建议保留（数学惯例），但让 Lead 在 glossary 中加一行：`twisted group cohomology 扭化群上同调`。

**O6. `tr07b.tex:106`（粗体范围与原书不一致）**
- 原文（p.116，700 dpi 核实）："…in which case we have a **2-group symmetry**."，粗体覆盖整个短语。
- 现文："\textbf{2-群}对称性"。建议改为 `\textbf{2-群对称性}`。

**O7. 原文三处笔误未加批注（照译正确，但按 STYLE_GUIDE §5 宜补注）**
- (a) p.117："…is described a cohomology class"（缺 by；应为 "is described **by** a cohomology class"）。
- (b) p.121："The argument is the same the one taking (4.194) to (4.197)"（应为 "the same **as** the one"）。
- (c) p.123："…irreducible representations $R_i^g$ of $\mathcal{G}$ and irreducible representations of $R_i^f$ of $F$"（语序错乱；应为 "irreducible representations $R_i^f$ of $F$"）。
- 建议各加一条批注，例如：
```latex
% [Tutor Note: p.117 原文 "is described a cohomology class" 缺介词，应为 "is described by a cohomology class"；译文按正确含义翻译。]
% [Tutor Note: p.121 原文 "The argument is the same the one taking (4.194) to (4.197)" 应为 "the same as the one"；译文按正确含义翻译。]
% [Tutor Note: p.123 原文 "irreducible representations of $R_i^f$ of $F$" 语序错乱，应为 "irreducible representations $R_i^f$ of $F$"；译文按正确含义翻译。]
```

**O8. `tr07b.tex:61`（(4.265) 的 $\mathbb{Z}_2$ 取值表述可更精确）**
- 现文："因为 $\Z_2$ 上链取值为 $0,\frac12$，$\pi\ii\int A^m\cup\operatorname{Bock}(A^e)$ 给出 $\pm1$ 的相因子"——若按 $R/\Z$ 取 $\{0,\frac12\}$，则需 $2\pi\ii$；与 (4.265) 的 $\pi\ii$ 配套的应是 $\{0,1\}$ 的整数代表元。
- 建议：`因为 $\Z_2$ 上链取 $\{0,1\}$（等价地，在 $\R/\Z$ 中取 $\{0,\frac12\}$ 时指数为 $2\pi\ii$），故 $\exp(\pi\ii\int A^m\cup\operatorname{Bock}(A^e))$ 只取 $\pm1$，正是 $\Z_2$ 反常的标准归一化。`

**O9.（可选）页标注移出方框**
- `tr07b.tex:33`（p.114）与 `tr07c.tex:119`（p.122）的页标注在方框内部。跨页方框这样处理可以接受；若 Lead 希望页标注一律在方框外，可把这两行上移到 `\begin{examplebox}`/`\begin{notebox}` 之前（内容不变）。

**O10.（信息）分片页数**
- a=4 页、b=6 页、c=6 页；与"每片 5–6 页"略有出入，但不影响编号/边界契约；无需改动，仅提醒 Lead 拼装时注意 a 片较短。

---

## 八、附：本次校对覆盖范围

- 页面图：p109、p110、p111、p112、p113、p114、p115、p116、p117、p118、p119、p120、p121、p122、p123、p124（16/16 全看）；另用 700 dpi 裁图复核 (4.257)(4.258)(5.26)(5.45)(5.48)(5.49) 及 p.116 粗体范围。
- 文字层：`split/p109.txt`–`p124.txt`（逐一通读）；`p114.txt` 含一个 NUL 字节导致部分工具读不了，已用 Python 容错读取，内容完整。
- 脚本核对：`tags_bypage.txt` 逐页比对、tag 顺序/重复、环境配对、页标计数、花括号/`$` 配对、禁写命令、未译英文段、方框/图题计数。
- 未做的事：未编译（按要求）、未修改任何文件、未评价 tr-08 的内容（仅核对跨文件方框闭合处的配对与边界）。
