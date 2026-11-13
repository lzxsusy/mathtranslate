# tr-08 交叉校对报告

- 校对人：tr-07　　校对时间：2026-11-04
- 对象：`work/src/chunks/tr08a.tex`（pp.125–129）、`tr08b.tex`（pp.130–134）、`tr08c.tex`（pp.135–138）
- 范围：tag 5.60–5.94、6.1–6.54（共 89 条）；fig28；pp.125–138 全部正文、方框、脚注
- 底本比对：`work/pages/p125…p138.png`（关键式用 `crop.py` 裁 700–2400 dpi）、`work/split/p125…p138.txt`、`work/tags_bypage.txt`
- 声明：**未修改 tr-08 任何文件**；本报告只提出建议，替换文本需 tr-08 或 Lead 决定。

---

## 0. 结论摘要

**总体质量高，可以合入（修掉 3 项"必须改"后）。**

- 编号公式 **89/89 完整**：5.60–5.94、6.1–6.54 齐全，顺序连续，无缺、无重、无跳、无自造；
  每页归属与 `tags_bypage.txt` 仅 (5.71) 一处因 `% [原文 p.126]` 标注位置偏晚而差一页（见 §8-O1，不影响公式本身）。
- 抽查 **17 条公式逐符号复核**（5.60、5.62、5.69、5.71、5.75、5.80、5.87/5.88、5.94、6.1、6.2、6.12、6.20、6.29、6.40、6.43、6.46、6.54），**符号全部与图像一致**；
  其中两处"原文字形细节"被正确复刻：(6.46) 后两行的 `w_2`（非 `ω_2`）、(6.43) 第一个积分用 `ℂP³`（P 斜体）而第二个用 `ℂP¹`（P 黑板体）。tr-08 为这两处写的批注经 1100–1600 dpi 复核**属正确**。
- 结构、方框、脚注、页标注**全部正确**；跨页方框（定义 5.2、例 6.1、例 6.3、例 6.4）均按 STYLE_GUIDE §7 合并为单框；脚注 5 条（原文 fn7–fn11）逐条比对无误。
- 未发现整句/整段漏译；边界接缝（tr07c→tr08a、tr08a→tr08b、tr08b→tr08c、tr08 结尾）**四处全部对齐**，无重复、无缺口；结尾止于 p.138 (6.54)，未侵入 p.139 致谢。
- 主要问题集中在 **3 条 Tutor Note 的数学表述**（1 处数值算错、1 处商的方向说反、1 处术语误译），公式正文本身无误。

---

## 1. 编号公式完整性

### 1.1 逐页归属表（对照 `tags_bypage.txt`）

| 页 | `tags_bypage.txt` 期望 | tr-08 实际（按 `% [原文 p.N]` 归属） | 判定 |
|---|---|---|---|
| 125 | 5.60–5.70（11） | 5.60–5.70（11）＋5.71 提前到此 | ⚠ 见 §8-O1 |
| 126 | 5.71–5.79（9） | 5.72–5.79（8） | ⚠ 同上（(5.71) 被计入 p.125） |
| 127 | 5.80–5.86（7） | 5.80–5.86（7） | ✓ |
| 128 | 5.87–5.93（7） | 5.87–5.93（7） | ✓ |
| 129 | 5.94, 6.1, 6.2（3） | 5.94, 6.1, 6.2（3） | ✓ |
| 130 | 6.3（1） | 6.3（1） | ✓ |
| 131 | 6.4–6.9（6） | 6.4–6.9（6） | ✓ |
| 132 | 6.10–6.15（6） | 6.10–6.15（6） | ✓ |
| 133 | 6.16–6.23（8） | 6.16–6.23（8） | ✓ |
| 134 | 6.24–6.29（6） | 6.24–6.29（6） | ✓ |
| 135 | 6.30–6.32（3） | 6.30–6.32（3） | ✓ |
| 136 | 6.33–6.40（8） | 6.33–6.40（8） | ✓ |
| 137 | 6.41–6.45（5） | 6.41–6.45（5） | ✓ |
| 138 | 6.46–6.54（9） | 6.46–6.54（9） | ✓ |
| **合计** | **89** | **89** | ✓ |

### 1.2 机器校验结果（脚本比对全序列）

```
TOTAL tags 89 / expected 89 / match True
first = 5.60, last = 6.54
missing = []  extra = []
每片分布：tr08a 37 条（5.60–6.2）、tr08b 27 条（6.3–6.29）、tr08c 25 条（6.30–6.54）
```

- **无跳号**：5.60→5.94 连续、6.1→6.54 连续，与 §5/§6 的编号规则（5.94 为 §5 最后一条，§6 从 6.1 起）一致。
- **无重复**：脚本按行扫描，无同一 tag 出现两次。
- **无自造**：全部 tag 均在 `tags.txt` 中。
- 唯一"瑕疵"是 `% [原文 p.126]` 标注位置，见 §8-O1（属页标注问题，不是公式问题）。

---

## 2. 逐符号核对表（17 条，全部裁图比对）

| # | 公式 | 页 | 核对要点（以原图为准） | tr-08 写法 | 判定 |
|---|---|---|---|---|---|
| 1 | (5.60) | 125 | `Ẑ(𝒢) = ℤ₄`；左端帽只加在 `Z` 上、`𝒢` 花体、右端黑板 `ℤ` | `\widehat{Z}(\mathcal{G}) = \Z_4` | ✓ |
| 2 | (5.62) | 125 | `𝔣 = 𝔰𝔭(M) = 𝔲𝔰𝔭(2M)`，三处均为 Fraktur | `\mathfrak{f}=\mathfrak{sp}(M)=\mathfrak{usp}(2M)` | ✓ |
| 3 | (5.69) | 125 | `G^{(0)}=F/𝒵=Sp(M)/ℤ₂=PSp(M)`（𝒵 花体、Sp/PSp 正体） | `F/\mathcal{Z}=\Sp(M)/\Z_2=\mathrm{PSp}(M)` | ✓ |
| 4 | (5.71) | 125–126 | `0→G^{(1)}→ℰ→𝒵→0`；ℰ、𝒵 均花体 | `\mathcal{E}`, `\mathcal{Z}` | ✓ |
| 5 | (5.75) | 126 | `q^{𝒵}=0∈𝒵̂`（上标花体 Z，右端帽在花体 Z 上） | `q^{\mathcal{Z}}=0\in\widehat{\mathcal{Z}}` | ✓ |
| 6 | (5.80) | 127 | `ℰ̂→Ĝ^{(1)}` | `\widehat{\mathcal{E}}\to\widehat{G}^{(1)}` | ✓ |
| 7 | (5.87)(5.88) | 128 | `(ℤ×ℤ₂)/⟨(2,1)⟩=ℤ₄`；`(0,1)~(2,1)` 平移给 `(0,1)~(−2,0)`、`(4,0)~0` | 与图一致 | ✓ |
| 8 | (5.94) | 129 | `𝒮=(𝒢×F)/ℰ`，三分量均花体（𝒮、𝒢、ℰ） | `\mathcal{S}=\frac{\mathcal{G}\times F}{\mathcal{E}}` | ✓ |
| 9 | (6.1) | 129 | `𝒟∈{10,11}`，**花体** D | `\mathcal{D}\in\{10,11\}` | ✓ |
| 10 | (6.2) | 129 | `M_{𝒟}=M_d×M_D`：**左边下标是花体 𝒟、右边是斜体 D** | `M_{\mathcal{D}}=M_d\times M_D` | ✓（易错处正确） |
| 11 | (6.12) | 132 | 长正合列：六段映射 `h_i, f_i, g_i, h_{i-1}` 的箭头位置；第二行末 `→⋯` | `\xrightarrow{h_i}` 等，两行 `aligned` | ✓ |
| 12 | (6.20) | 133 | `H_k(M_D,∂M_D)=H_{D-k}(M_D)`，此处 D 为**斜体**维数 | `H_{D-k}(M_D)` | ✓ |
| 13 | (6.29) | 134 | `AdS_{d+1}×X_{D-d-1}`（AdS 正体、维数斜体） | `\mathrm{AdS}_{d+1}\times X_{D-d-1}` | ✓ |
| 14 | (6.40) | 136 | `∫_{S⁵}dH₇=−∫_{S⁵}F₅∧F₅=−NF₃` | 与图逐符号一致 | ✓（原文如此，另见 §8-O3） |
| 15 | (6.43) | 137 | `∫_{ℂP³}F₆/2π~N`（**P 斜体**）；`∫_{ℂP¹⊂ℂP³}F₂/2π~k`（**ℂP¹ 的 P 为黑板体**、其后 `ℂP³` 的 P 为斜体） | `\mathbb{C}P^3`；`\mathbb{CP}^1 \subset \mathbb{C}P^3` | ✓（1600 dpi 复核，字形差异属实，批注正确） |
| 16 | (6.46) | 138 | `F₂=kω₂+g₂`；`F₆=Nω₂∧ω₄+f₂∧ω₄+f₄∧w₂`；`H₃=h₃+h₁∧w₂`（**后两处确为 `w₂` 而非 `ω₂`**） | 原样保留 `w_2` | ✓（批注正确） |
| 17 | (6.54) | 138 | `b₂↔B₂, c₁↔A_{D0}, a₁↔A_{D4}` | 与图一致 | ✓ |

**小结**：17 条全部通过；`\dd` 用于外微分（`dF₇`、`dH₇`、`da₁`、`db₂` 等）符合 STYLE_GUIDE §3，维数下标保持斜体 `d`/`D`，二者未混用。

---

## 3. 结构检查

| 项目 | 原文位置 | tr-08 实现 | 判定 |
|---|---|---|---|
| §5.3.2 标题「Bockstein 2-Group Symmetries」 | p.125（例 5.3 方框闭合后） | `tr08a:57 \subsubsection{Bockstein 2-群对称性}`，位于 `\end{examplebox}` 之后 | ✓ |
| §6 标题「Higher-Form Symmetries and String Theory」 | p.129 | `tr08a:214 \section{高阶形式对称性与弦论}` | ✓ |
| 6.1「Higher-Form Symmetries from Geometric Engineering」 | p.129 | `tr08a:217 \subsection{来自几何工程的高阶形式对称性}` | ✓ |
| 6.2「Generalised Symmetries in Holography」 | p.134 | `tr08b:191 \subsection{全息中的广义对称性}` | ✓ |
| fig28 | p.130 页首 | `tr08b:8–12`，`width=0.62\textwidth`，`\figtitle{28}{…}` 图注照译（非紧/蓝→缺陷，紧/青→动力学激发） | ✓ |
| 定义 5.2（绿色 box） | p.125 起、p.126 收尾（跨页） | 合并为**一个** `definitionbox`（`tr08a:59–69`），(5.70)(5.71) 各只出现一次 | ✓ |
| 例 5.3 闭合处（橙色 box） | p.125，紧跟 (5.69) | `tr08a:48 \end{examplebox}` 紧接 (5.69)，与原文位置一致；未重写框题、未重出 (5.59) | ✓ |
| 例 5.4 / 例 5.5（橙色） | p.128 | `examplebox` ×2，完整落在 p.128 | ✓ |
| 「相对同调」框（粉色） | p.131 | `notebox`，完整 | ✓ |
| 「与 swampland 猜想的一致性」框（粉色） | p.132 | `notebox`，完整 | ✓ |
| 例 6.1（橙色） | p.132–133 跨页 | 合并为一个 `examplebox` | ✓ |
| 例 6.2（橙色） | p.134 | `examplebox`，完整 | ✓ |
| 例 6.3（橙色） | p.135–137 跨页，含 (a)(b)(c) 三段 | 合并为一个 `examplebox`，`\para{(a) 边界条件 1。}`/`\para{(b)…}`/`\para{(c)…}` 均在框内 | ✓ |
| 例 6.4（橙色） | p.137–138 跨页 | 合并为一个 `examplebox`，(6.41)–(6.54) 在框内 | ✓ |
| 脚注 | fn7 (p.130)、fn8 (p.133)、fn9/10/11 (p.134) | 5 条 `\footnote`，逐条与原文比对无误（见下表） | ✓ |
| 页标注 | pp.125–138 | 14 个 `% [原文 p.N]`，无缺、无重 | ✓（仅 p.126 位置见 §8-O1） |
| 环境/括号 | — | `{}` 724/724；`$` 成对；`\begin/\end` 配对（唯一"未闭合"是 tr08a 的 `\end{examplebox}`，其 `\begin` 在 tr07c，属设计内） | ✓ |

### 脚注逐条核对

| 编号 | 内容要点 | 判定 |
|---|---|---|
| fn7 (p.130) | 早期研究聚焦带电缺陷的弦论起源；拓扑对称性产生子早期讨论 [62,103]、较新工作 [136,138,139,154] 说明拓扑极限下包裹膜描述拓扑产生子 | ✓ 完整 |
| fn8 (p.133) | 假设 `M_D` 同调无挠 | ✓ |
| fn9 (p.134) | 早期 [95,101]；较近 [99,106,133,136,138,142,161,175,177,194,215] | ✓（含原文 161,175,177 的异常逗号，照抄） |
| fn10 (p.134) | SymTFT 与全息拓扑体项精确对应见 [175] | ✓ |
| fn11 (p.134) | 限制到 AdS 解只为示意；Klebanov–Strassler 解 [216] 不属此类，已在 [136,177,215] 研究 | ✓ |

---

## 4. 漏译检查（逐页对照 split）

逐页核对 `split/p125.txt … p138.txt` 的段落与句子，**未发现整句/整段漏译**。各页代表句对应如下（左：split 原句起始，右：tr-08 位置）：

| 页 | split 代表句 | tr-08 对应 | 判定 |
|---|---|---|---|
| 125 | "which has / Additionally we have 2M complex scalars… / for all i. We tune…" | `tr08a:8–47` | ✓ |
| 126 | "an F bundle and Bock is the Bockstein map… / Screening Interpretation. / From the discussion in section 3.1…" | `tr08a:64–110` | ✓ |
| 127 | "or equivalently / Pontryagin dual to (5.71)… / A 2-Group Background Field. / Bockstein 2-Groups in Gauge Theories." | `tr08a:113–149` | ✓ |
| 128 | "Example 5.4 / Example 5.5 / Mixed Gauge-Flavor Bundles." | `tr08a:157–207` | ✓ |
| 129 | "that the gauge theory sums over… / 6 Higher-Form… / 6.1… / Setup." | `tr08a:203–229` | ✓ |
| 130 | "quantum field theory without dynamical gravity… / Defects and Dynamical Excitations." | `tr08b:3–24` | ✓ |
| 131 | "Relative Homology / Screening and p-Form Symmetries. / Combining all of these…" | `tr08b:27–62` | ✓ |
| 132 | "It should be noted though… / Consistency with Swampland Conjecture / Description in Terms of the Boundary." | `tr08b:65–105` | ✓ |
| 133 | "McKay correspondence… / Description in Terms of Intersection Numbers. / The map i maps…" | `tr08b:115–158` | ✓ |
| 134 | "Example 6.2 / 6.2 Generalised… / SymTFT from Holography. / fn9–11" | `tr08b:161–199` | ✓ |
| 135 | "is typically left with a bulk action… / Symmetry Boundary Condition from Holography. / Example 6.3 / (a) Boundary conditions 1." | `tr08c:3–34` | ✓ |
| 136 | "The bulk equations of motion… / (b) Boundary conditions 2. / which implies that N D1 strings…" | `tr08c:37–72` | ✓ |
| 137 | "(c) More general boundary conditions. / Example 6.4 / … / We choose to represent H², H⁴…" | `tr08c:80–114` | ✓ |
| 138 | "Furthermore, we choose to expand in F₂ and F₆… / … / which are exactly the equations of motion of (6.42)…" | `tr08c:121–176` | ✓ |

**特别核对**（易漏处）：

- p.130 "This is illustrated in figure 28." → `tr08b:20` 末句 ✓
- p.131 "as the defects pass these topological operators and acquire phases according to their charges" → `tr08b:44` ✓
- p.132 "One can cycle between different global forms by performing discrete gaugings (possibly with discrete torsions)…" → `tr08b:65` ✓
- p.133 "All of these 1-cycles are contractible when pushed into the bulk." → `tr08b:133` ✓
- p.135 "See [215] for more details on the procedure." → `tr08c:26` ✓
- p.136 "thus justifying (6.35)" / "thus justifying (6.39)" → `tr08c:53` / `tr08c:72` ✓
- p.137 "where m′ is a divisor of k and n′ a divisor of N." → `tr08c:92` ✓
- p.138 "where we have used the identity ∗₆ω₂=ω₄ and ∗₁₀vol_{AdS₄}=ω₂∧ω₄." → `tr08c:136` ✓

---

## 5. 术语一致性

| 英文 | tr-08 用法 | 全书/glossary 情况 | 判定 |
|---|---|---|---|
| geometric engineering | 几何工程 | glossary ✓ | ✓ |
| holography / holographic | 全息 | glossary ✓ | ✓ |
| brane / D-brane / M2 / M5 / NS5 / D5 / D1 | 膜 / D-膜 / … | glossary ✓ | ✓ |
| compactification / internal manifold | 紧致化 / **内禀**紧致化流形、内禀流形、内禀几何、内禀空间（11 处） | glossary 有 compactification；"internal" 未收 | ⚠ 见 §8-O6 |
| defect group | 缺陷群 | 未收 | 建议入 glossary |
| unscreened operator | 未屏蔽算符 | glossary 有 screening 屏蔽 | ✓（构词自然） |
| relative homology | 相对同调 | 未收 | 建议入 glossary |
| polarization | 极化（polarization） | glossary ✓ | ✓ |
| Lagrangian（此处的数学义） | **拉格朗日量** | — | ✗ 见 §7-M2 |
| structure group | 结构群（structure group） | 未收 | ✓ |
| Stiefel–Whitney class | Stiefel–Whitney 类 | glossary ✓ | ✓ |
| Bockstein map | Bockstein 映射 | glossary 收的是 "Bockstein homomorphism→Bockstein 同态" | ✓ 原文均作 "map"，"映射"忠实；遇 "homomorphism" 时应作"同态" |
| flux / flux quantisation | 通量 / 通量量子化 | glossary 有 flux 通量 | ✓ |
| swampland | swampland（保留英文） | 未收 | 建议入 glossary（正文首现处保留英文是通行做法） |
| baryon vertex | 重子顶点 | 未收 | 建议入 glossary |
| discrete theta angle | 离散 theta 角 | glossary ✓ | ✓ |
| non-dynamical defect / dynamical excitation | 非动力学缺陷 / 动力学激发 | 未收 | 建议入 glossary |
| Pontryagin dual | Pontryagin 对偶 | 未收 | 建议入 glossary |
| set up（小标题 Setup.） | 构造 | — | 可接受（"构造"与正文"几何工程构造"呼应） |

**跨块一致性**：与 tr-07 相邻处用词一致（混合规范-味丛 / 结构群 / 全局形式 / 规范框架 / Pontryagin 对偶 / Bockstein 映射），接缝读起来无割裂感。

---

## 6. 边界接缝（重点）

| 接缝 | 前块结尾 | 后块开头 | 原文断点 | 判定 |
|---|---|---|---|---|
| **tr07c → tr08a**（p.124/125） | tr07c 末：(5.59)「$\mathcal{G}=\Spin(4N+2)$」+ 未闭合的 `\begin{examplebox}{例 5.3：非阿贝尔规范理论}` | tr08a:8「它有」＋(5.60)「$\widehat{Z}(\mathcal{G})=\Z_4$」 | p.124 末 "…with gauge group G = Spin(4N+2), (5.59)"；p.125 首 "which has Ẑ(G)=Z₄. (5.60)" | **✓ 完美对齐**：无重复 (5.59)、无缺口、不重写框题；`\begin`/`\end{examplebox}` 恰好跨文件闭合，tr08a:3–7 有注释说明 |
| tr08a → tr08b（p.129/130） | tr08a 末「…而为了构造」 | tr08b:3「一个没有动力学引力的量子场论，我们必须取极限」 | p.129 末 "…and in order to construct a"；p.130 首 "quantum field theory without dynamical gravity we have to take the limit" | ✓ 句子跨片拼合通顺 |
| tr08b → tr08c（p.134/135） | tr08b 末「…并只关注边界处的主导贡献之后，」 | tr08c:3「通常只剩下如下形式的体作用量」 | p.134 末 "…focusing on solely the dominant contributions at the boundary, one"；p.135 首 "is typically left with a bulk action of the form" | ✓ |
| tr08 结尾（p.138/p.139） | tr08c 末：(6.54)＋例 6.4 方框闭合＋批注 | — | p.138 正文结束（(6.54) 为该页最后一行） | **✓ 未侵入 p.139 致谢**；无致谢内容 |

**拼接依赖提醒**：`tr08a` 的第一个 `\end{examplebox}`（L48）依赖 `tr07c` 的 `\begin{examplebox}`。`\input` 顺序必须是 `…tr07c → tr08a → tr08b → tr08c`，否则编译报 `\end{examplebox} ended by …`。"tr-07 已在 tr07c 末尾、tr-08 已在 tr08a 头部各加注释"，建议 Lead 在 `main.tex` 顺序上最后确认一次。

---

## 7. 必须改（3 项，含可直接替换的文本）

### M1. `tr08a.tex:151–154` Tutor Note 的数值算错（分子是无限群 ℤ，不能按 8/2 算阶）

**现状**

```latex
% [Tutor Note: (5.84) 与 (5.85) 互为 Pontryagin 对偶，可拿例 5.2 验算：
%  $\widehat{Z}(\mathcal{G})=\Z$、$\widehat{Z}(F)=\Z_2$、$Q=\langle(2,1)\rangle$，商
%  $(\Z\times\Z_2)/\langle(2,1)\rangle$ 的阶为 $8/2=4$，正是 (5.87) 的 $\Z_4$。
%  注意分子上带帽、分母 $Q$ 不带帽，这是对偶侧的写法，不要写成 $Z(\mathcal{G})\times Z(F)/Q$。]
```

**问题**：`ℤ×ℤ₂` 是无限群，无"阶 8"可言；"8/2=4"只对 `ℤ₄×ℤ₂`（即 (5.92) 的例 5.5）成立。此处例 5.4 的 (5.87) 分子是 `ℤ×ℤ₂`，商为 `ℤ₄` 要靠 (5.88) 的等价关系直接算，不能靠数元素。

**替换为**

```latex
% [Tutor Note: (5.84) 与 (5.85) 互为 Pontryagin 对偶，可拿例 5.4 验算：
%  $\widehat{Z}(\mathcal{G})=\Z$、$\widehat{Z}(F)=\Z_2$、$Q=\langle(2,1)\rangle$。
%  注意分子含无限群 $\Z$，**不能**按「元素个数相除」算阶（那是对例 5.5 的
%  $\Z_4\times\Z_2$ 才成立的算法）；应直接按 (5.88) 读商：$(0,1)\sim(-2,0)$
%  使 $(1,0)$ 的像阶为 4，而 $(4,0)\sim(0,0)$ 给出 $4\cdot(1,0)=0$，故商 $\cong\Z_4$。
%  另注意分子带帽、分母 $Q$ 不带帽，这是对偶侧的写法，不要写成 $Z(\mathcal{G})\times Z(F)/Q$。]
```

### M2. `tr08b.tex:46` 「拉格朗日量」是术语误译（此处 Lagrangian = 拉格朗日子群）

**现状**

```latex
每种这样的选择对应于所谓的\textbf{极化}（polarization）或\textbf{拉格朗日量}（Lagrangian），即
```

**问题**：原文紧接着就给出 `Λ = ⊕ᵢ Λᵢ`、`Λᵢ ⊆ Dᵢ`、`⟨·,·⟩|_Λ = 1`——这是**极大各向同性子群**（Lagrangian subgroup），与"拉格朗日量/Lagrangian density"无关。照现译读者会误解为作用量。

**替换为**

```latex
每种这样的选择对应于所谓的\textbf{极化}（polarization）或\textbf{拉格朗日（Lagrangian）子群}，即
```

### M3. `tr08b.tex:186–189` Tutor Note 把商的方向说反了

**现状**

```latex
% [Tutor Note: (6.25) 的 $-2$ 是非紧 CY 三流形里紧 4-闭链 $C_4=\mathbb{P}^1\times\mathbb{P}^1$
%  上 $\mathbb{P}^1$ 的自相交数，与 $E_1$ 理论流向纯 $SU(2)$ Yang--Mills 后
%  瞬子数/规范耦合的几何解释相容；可用 (6.26) 反推：两个紧 2-闭链贡献 $\Z\oplus\Z$，
%  模掉非紧闭链后只剩 $\Z_2$，说明这唯一的紧 4-闭链给出的正是 $\Z_2$ 的线算符群。]
```

**问题**：(6.26) 是 `H₂(M₆,∂M₆)/H₂(M₆)`，**分母 H₂(M₆) 是紧 2-闭链**（C₄ 内的两个 ℙ¹），分子才是相对（非紧）闭链。所以是"模掉**紧**闭链"，不是"模掉非紧闭链"。此外"瞬子数/规范耦合"一句与 E₁ 的几何对应关系表述含混，建议删掉。

**替换为**

```latex
% [Tutor Note: (6.25) 的 $-2$ 是紧 4-闭链 $C_4=\mathbb{P}^1\times\mathbb{P}^1$ 内两个
%  $\mathbb{P}^1$ 的（自）交数，它决定了 $E_1$ 理论中这条紧 4-闭链的刚性与
%  $SU(2)$ 规范理论的一圈结构。(6.26) 的商是「相对闭链模**紧**闭链」：
%  分子 $H_2(M_6,\partial M_6)\cong\mathbb{Z}$（Lefschetz 对偶于 $H^4(M_6)$，
%  由与 $C_4$ 配对给出），分母 $H_2(M_6)=\mathbb{Z}\oplus\mathbb{Z}$ 由 $C_4$ 内
%  两个 $\mathbb{P}^1$ 生成；它们在相对同调中的像由交数 $\mathbb{P}^1\cdot C_4=-2$
%  给出，即 $2\mathbb{Z}\subset\mathbb{Z}$，故商为 $\mathbb{Z}/2\mathbb{Z}=\mathbb{Z}_2$
%  ——这正是未屏蔽线算符的 $\mathsf{D}_1=\mathbb{Z}_2$。注意不要把它说成
%  「模掉非紧闭链」。]
```

---

## 8. 可选改（8 项，含替换文本）

### O1. `tr08a.tex:71` 页标注 `% [原文 p.126]` 放晚了约 6 行（影响 (5.71) 的页归属）

**现状**：(5.71) 与"这里 $\mathcal{E}$ 是 $\mathcal{Z}$ 被 $G^{(1)}$ 的某个扩张。"都排在 `% [原文 p.126]` **之前**，而原文 p.125 只到 "…lifting the background $G^{(0)}$ bundle to"，p.126 才从 "an $F$ bundle…" 起、（5.71）在 p.126 页首。故按页归属 (5.71) 被算进 p.125。

**建议**：把标注插到定义框内、句子中间（注释可出现在 tcolorbox 内，无需移出方框）：

```latex
其中 $\left[w_2^f\right]$ 是把背景 $G^{(0)}$ 丛提升为
% [原文 p.126]
$F$ 丛的 $\mathcal{Z}$-值障碍类，而 $\mathrm{Bock}$ 是与短正合列
```

并把原第 71 行的 `% [原文 p.126]` 删除。（若接受"页标注允许落在句末"，也可不改，只在本报告备案。）

### O2. `tr08b.tex:83` 原文 `D_{p−k+1}` 疑为 `D_{p,k}` 之笔误 —— 建议加批注（译文保留原文写法，正确）

**现状**：`\para{用边界来描述。}我们可以用内禀流形的边界 $\partial M_D$，借助相对同调的长正合列来描述 $\mathsf{D}_{p-k+1}$`

**原文**：p.132 "We can describe $\mathsf{D}_{p−k+1}$ in terms of the boundary $\partial M_D$…"（图像确认原文如此）。但本段其余各句、以及紧接的 (6.14) 都在讲 `D_{p,k}`，且 `p−k+1` 在本文记法里没有定义。

**建议**：在该句后追加一条批注（不必改译文）：

```latex
% [Tutor Note: p.132 正文此处作 $\mathsf{D}_{p-k+1}$，疑为 $\mathsf{D}_{p,k}$ 之笔误：
%  紧接着的 (6.14) 直接给出 $\mathsf{D}_{p,k}=\ker(h_{k-1})$，且本小节其余各处均用
%  $\mathsf{D}_{p,k}$（$p$ 为膜的世界体积维数、$k$ 为闭链维数，两者独立）。译文照原文保留。]
```

### O3. `tr08c.tex:74–77` 批注称 (6.36)/(6.40)「可用通量量子化直接核对」——对 (6.40) 不成立

**现状**：批注说 "(6.40) 中 $\int_{S^5}F_5\wedge F_5$ 只留一个 $F_5$ 的 AdS 分量，给出 $-NF_3$"。

**问题**：`dH₇` 为 8-形式，`∫_{S⁵}` 后是 3-形式，与右侧 `−NF₃` 相容；但 `F₅∧F₅` 是 10-形式，`∫_{S⁵}` 后是 **5-形式**，与 `−NF₃` 次数不符。原式疑为 `−F₃∧F₅`（其 `∫_{S⁵}` 正好给出 `−NF₃`）之类的笔误。tr-08 正文照抄原文是正确的，只是这条批注的"核对"论证站不住。

**替换为**

```latex
% [Tutor Note: (6.36) 可用通量量子化核对：$\int_{S^5}F_5=N$（D3-膜荷），故
%  $\int_{S^5}F_5\wedge H_3=N H_3$，两端同为 3-形式，自洽。(6.40) 则需注意次数：
%  原式右端 $-N F_3$ 是 3-形式，而 $F_5\wedge F_5$ 为 10-形式、经 $\int_{S^5}$ 后应得
%  5-形式，故原文此处疑为 $F_3\wedge F_5$（或同类记号）之笔误；译文照原文保留，
%  读者只需记住两式都是「7-形式 Bianchi 恒等式 + $\int_{S^5}F_5=N$」的推论。]
```

### O4. `tr08a.tex:50–52` 批注「若换成 $4N$，(5.61) 里的 $q^g=2$ 就不再是 $\Z_4$ 的元素」表述不严

**问题**：`Spin(4N)` 的中心是 `ℤ₂×ℤ₂`，根本不存在 `ℤ₄` 靶空间，所以不是"2 不是 ℤ₄ 的元素"这么表述，而是"电荷格整体从 ℤ₄ 变成 ℤ₂×ℤ₂"。建议改写：

```latex
% [Tutor Note: 式 (5.60) 可独立核对：$\mathrm{Spin}(4N+2)$ 的中心是 $\Z_4$，而
%  $\mathrm{Spin}(4N)$ 的中心是 $\Z_2\times\Z_2$；原文取 $4N+2$ 正是为了让
%  $\widehat{Z}(\mathcal{G})=\Z_4$，从而与 (5.66) 里 $\Z_4\times\Z_2$ 的荷矩阵配套。
%  若换成 $4N$，电荷格整体会变成 $\Z_2\times\Z_2$，(5.66)–(5.69) 都要重算。]
```

### O5. `tr08a.tex:193–197` 批注中间步骤有一个符号小误

**现状**："$(4,0)=2(2,0)=2[(2,1)-(0,1)]=2(0,1)=(0,0)$"

**问题**：`2[(2,1)−(0,1)] = 2(2,1) − 2(0,1) = −2(0,1) ≡ (0,0)`，中间写成 `=2(0,1)` 少了一个负号（结论 `(0,0)` 不受影响）。

**替换**：把 `=2[(2,1)-(0,1)]=2(0,1)=(0,0)$` 改为 `=2(2,1)-2(0,1)=-2(0,1)=(0,0)（模去 $\langle(2,1)\rangle$）$`

### O6. 术语「内禀」11 处 vs「内部」1 处，建议统一

出现处：`tr08a:218, 229`、`tr08b:17, 20, 77, 83, 125, 146, 164, 199`、`tr08c:104`（内禀）；`tr08a:231` 批注（内部流形）。

**建议**：全书统一为「内部」（更常见），或由 Lead 在 glossary 增补 `internal manifold → 内部流形 / internal geometry → 内部几何` 后统一回写；**不要两词混用**。替换只需一次 `sed` 式批量：内禀→内部（"内禀紧致化流形"→"内部紧致化流形" 等）。

### O7. `tr08b.tex:194` 「来自全息的对偶 SymTFT」多出"对偶"

原文标题为 "SymTFT from Holography."（p.134），无 "dual"。

```latex
\para{来自全息的 SymTFT。}
```

### O8. `tr08a.tex:199–204` 代词「它」指代歧义（p.128→129 跨页句）

**现状**："…而规范理论要对这些丛求和。它现在不再闭合，意味着…"

原文 "…bundles that the gauge theory sums over. **Its** non-closure now means…"，`Its` 指背景场 `B₂`；但译文上一句主语是"规范理论"，"它"易被读成"规范理论不再闭合"。

```latex
而规范理论正是要对这些丛求和。该背景场现在不再闭合，意味着该规范理论不再严格地对 $\mathcal{G}/G^{(1)}$ 丛求和。
```

---

## 9. 其他观察（无需改动，供 Lead 参考）

1. **页标注的取舍**：全块只有 p.126 一处标注晚放（O1）；其余 13 个标注位置与原文页断点一致，`tags_bypage` 逐页比对仅此一处差异。
2. **图位置**：原文 fig28 浮在 p.130 页首（在 "quantum field theory without dynamical gravity…" 之前），译文把 `figure` 环境放在 (6.3) 之后。因 `[htbp]` 浮动，排版后通常仍回页顶，**不算错**；若 Lead 希望严格对应原文，可把 `figure` 移到 `% [原文 p.130]` 标注之后、该句之前。
3. **方框内公式编号**：`examplebox`/`definitionbox` 内的 `\tag` 会排在框内右侧（与原文一致）；框跨页时 `breakable` 生效，编号不会丢。
4. **批注密度**：18 条 / 14 页（§5 部分 5 条、§6 部分 13 条），满足 STYLE_GUIDE §5「每 2–3 页 ≥1、每节 ≥3」。
5. **版权/术语新词**：`缺陷群`、`相对同调`、`未屏蔽算符`、`极化`、`结构群`、`重子顶点`、`非动力学缺陷`、`swampland`、`Pontryagin 对偶` 建议一并回写 `glossary.tsv`。
6. **tr-08 的两处"细节正确"值得表扬**：(6.46) 的 `w₂/ω₂` 字形差异、(6.43) 的 `ℂP³ / ℂP¹` 字体差异都被逐字复刻并写了正确批注——这两处最容易"顺手统一"而失真。

---

## 10. 校对方法与可复现命令

```powershell
# 1) tag 完整性（按行扫描 + 与 tags_bypage 逐页比对）
#    结果：89/89，序列 match=True，唯 (5.71) 页归属差一页（见 O1）
python chk_tr08.py       # 脚本：正则抓 \tag{}、% [原文 p.N]、footnote、环境配对

# 2) 逐符号裁图（work\tmp\rev08\，700–2400 dpi）
& $py "...\work\tools\crop.py" <page> <x0> <y0> <x1> <y1> out.png <dpi>
# 已裁：p125(5.60,5.62,5.69) p126(5.71,5.75/5.76) p127(5.80) p129(5.94,6.1,6.2)
#       p132(6.12) p133(6.20) p134(6.29) p136(6.40) p137(6.43 左/右/全) p138(6.46,6.54)

# 3) 结构/宏检查：未定义宏 = 无；BOM=False、CRLF=0、U+FFFD=False
# 4) 接缝：cat tr07c.tex tr08a.tex | grep -n "examplebox"（begin/end 恰好跨文件）
```

**校对结论**：tr-08 通过交叉校对；修 M1–M3 后即可合入。O1–O8 可择机处理。
