# tr-07 块交叉校对报告（原文 pp.90–102）

- **校对者**：tr-05（Lead 指派交叉校对；只出报告，不改被校对文件）
- **日期**：2026-11-03
- **被校对文件**：`work/src/chunks/tr07a.tex`（pp.90–93）、`tr07b.tex`（pp.94–97）、`tr07c.tex`（pp.98–102）
- **负责 tag 区间**：8.11–8.12、9.1–9.7
- **校对素材**：`work/pages/p090.png … p102.png`（200 dpi，逐页看）+ 500–800 dpi 裁剪放大（`work/tmp/z90_811b.png`、`z91_812.png`、`z93_91b.png`、`z97_97.png`）+ `work/split/p090.txt … p102.txt`（已去控制字符，副本在 `work/tmp/clean/`）+ `work/tags_bypage.txt`

## 0. 结论摘要

**总体质量高，可以合并。** 9 条编号公式齐全、无重复、无跳号、无自造，与 `tags_bypage.txt` 逐页对齐；p.98–102 确实没有编号公式。Lead 指定的 8 条必查公式（(8.11)、(8.12)、(9.1)、(9.2)–(9.5)、(9.6)(9.7)）我全部对着图像逐符号核对过，**数学内容无误**。发现 **1 处必须改的图形错误**：(8.12) 的方括号横档画反了（画成了「][」而不是「[ ]」）；另有 **2 处一致性必须改**（「三穿孔球面」→「三穿刺球面」；理论符号 `T(…)` 用斜体，与全书正体 `\mathrm{T}` 不一致）。正文无整段漏译，8 条脚注（67–74）齐全且锚点正确，p.90 与 p.102 两个边界都无缝。

| 类别 | 数量 |
|---|---|
| 编号公式（应/实） | 9 / 9 |
| 逐符号抽查 | 9 条（全部） |
| 必须改 | **3** |
| 可选改 | 9 |
| 原文笔误（tr-07 已标 / 未标） | 5 已标 / 3 未标 |

---

## 1. 编号公式完整性（Lead 任务 1）

`tags_bypage.txt` 在 p.90–102 的清单与 tr-07 实际 `\tag{}` 逐页对照：

| 页 | tags_bypage | tr-07 实际 | 结论 |
|---|---|---|---|
| p90 | 8.11 | 8.11 | ✅ |
| p91 | 8.12 | 8.12 | ✅ |
| p93 | 9.1 | 9.1 | ✅ |
| p94 | 9.2 | 9.2 | ✅ |
| p95 | 9.3, 9.4, 9.5 | 9.3, 9.4, 9.5 | ✅ |
| p97 | 9.6, 9.7 | 9.6, 9.7 | ✅ |
| p98–p102 | ∅（无编号公式） | 无 `\tag` | ✅ |

- 合计 **9 条唯一编号**，脚本核验：`tags = 8.11,8.12,9.1,9.2,9.3,9.4,9.5,9.6,9.7`（顺序与原文一致），`\begin{equation}`/`\end{equation}` = 9/9。
- 结构平衡：花括号 tr07a 98/98、tr07b 127/127、tr07c 127/127；`tikzpicture` 2/2、`tcolorbox` 1/1、`itemize` 4/4、`keybox` 1/1、`gathered` 1/1；逐行 `$` 均为偶数；UTF-8 无 BOM、LF。
- 页标注：`% [原文 p.90]` … `% [原文 p.102]` 共 13 个，无缺页。
- 原文 pp.90–102 只有一处**无编号**展示公式（p.101 DIM 代数的二次关系），tr-07 用 `\[ … \]` 处理正确，未自造编号。

---

## 2. 公式逐符号抽查（Lead 任务 2）

判定依据：`work/pages/pNNN.png` 200 dpi 看位置，再按区域裁 500–800 dpi 逐符号读。

### 2.1 (8.11)（p.90，tr07a.tex:26–39）— ✅ 正确

原图：`Z_{S³_b}[ N □ —(N−1)⬭— ⋯ —(1)◯ ] = (W_N algebra S-move kernel).`

- 左侧 $Z_{S^3_b}$ ✅；方括号用 `\left[ … \right]` ✅（原图确为方头括号，非圆括号）。
- 四个节点形状逐一对：`N` = 方框（rectangle）✅；`N−1` = 圆角长条（stadium）✅；`⋯` = 无框 ✅；`1` = 圆圈 ✅。
- 连线：N—N−1 实线 ✅；N−1—⋯—1 的断开式连线（2.75 / 3.25 两段夹 `\cdots`）✅。
- 右侧 `(W_N algebra S-move kernel)` 逐词一致，$W_N$ 为斜体（非 `\mathcal W`）✅。

### 2.2 (8.12)（p.91，tr07a.tex:49–68）— ⚠️ **必须改：方括号方向反了**

原图（放大图 `work/tmp/z91_812.png`）：`Z [ ⟨N⟩4d / U(N−1) ← 2N / ⟨N⟩4d ] = (W_N algebra braiding kernel).`
即左括号是「[」（竖线在左、上下横档朝**右**），右括号是「]」（竖线在右、横档朝**左**）。

- 节点与箭头**全部正确**：U(N−1) 圆角框在中间；上方/下方各一个圆节点 N，箭头自 U(N−1) 指向 N（上箭头朝上、下箭头朝下）✅；右侧 `2N` 方框，箭头 2N → U(N−1)（朝左）✅；两个 N 旁标 `4d` ✅；2N 方框左上/左下角各有斜线连到上/下 N ✅。
- **错误**：tr07a.tex:63–64 两条 `\draw` 的竖线与横档关系反了，渲染出来是「]」在左、「[」在右（即 `][`），与原图相反。

当前代码（tr07a.tex:63–64）：
```latex
\draw (-0.35,2.6) -- (-0.15,2.6) -- (-0.15,-0.65) -- (-0.35,-0.65);
\draw (4.05,2.6) -- (3.85,2.6) -- (3.85,-0.65) -- (4.05,-0.65);
```
建议改为（竖线在外、横档朝内）：
```latex
\draw (-0.15,2.6) -- (-0.35,2.6) -- (-0.35,-0.65) -- (-0.15,-0.65);
\draw (3.85,2.6) -- (4.05,2.6) -- (4.05,-0.65) -- (3.85,-0.65);
```
> 判据：左括号「[」= 竖线在最左（x 最小）、上下横档向右延伸；右括号「]」= 竖线在最右、横档向左延伸。现码左括号竖线在 x=−0.15（较右）、横档伸到 −0.35（向左），形状是「]」。

### 2.3 (9.1)（p.93，tr07a.tex:122–125）— ✅ 正确

原图：`Z_{S⁵} = ∫ da Z_pert Z_inst,1 Z_inst,2 Z_inst,3.`
- 下标 $S^5$（不是 $S^5_b$）✅；积分测度 upright `d` ✅；三个 `Z_{\text{inst},i}` 下标 upright ✅；$Z_{\text{pert}}$ ✅。

### 2.4 (9.2)（p.94，tr07b.tex:18–21）— ✅ 正确

原图：`𝓘(u) = Tr[ (−1)^F e^{−βH̃} ∏_i u_i^{K_i} ]`
- `(-1)^F` ✅；`\tilde H`（H 上波浪号）✅；`\prod_i u_i^{K_i}`（K 大写、下标 i）✅；`\Tr` 正体 ✅。

### 2.5 (9.3)（p.95，tr07b.tex:32–35）— ✅ 正确

原图：`𝓘[T](a₁,a₂) = ∫[dz]_G 𝓘_vec(z) 𝓘[T₁](a₁,z) 𝓘[T₂](a₂,z)`
- 测度记号 `[\dd z]_G` ✅；三个 $\mathcal I$ 因子与自变量 ✅；`\mathcal I_{\text{vec}}` ✅。

### 2.6 (9.4)（p.95，tr07b.tex:46–49）— ✅ 正确

原图：`𝓘[T(g,C,D)](a_i) = ⟨O_{D₁}(a₁) … O_{D_n}(a_n)⟩_{some TQFT}`
- `\mathcal{O}_{D_1}` 花体 O + 下标 D₁ ✅；右侧下标 upright `\text{some TQFT}` ✅（原文即正体）。

### 2.7 (9.5)（p.95，tr07b.tex:53–56）— ✅ 正确

原图：`𝓘[T(g,C,D)](a_i) = Σ_λ (C_λ)^{2g−2} φ^{D₁}_λ(a₁) … φ^{D_n}_λ(a_n)`
- 指数 $(C_\lambda)^{2g-2}$ ✅（是 $2g-2$ 而非 $2g-2+n-3$，照原文）；$\phi^{D_i}_\lambda$ 的上下标顺序 ✅；求和指标 $\lambda$ 对所有穿刺点共用 ✅。

### 2.8 (9.6)（p.97，tr07b.tex:84–88）— ✅ 正确

原图：`S = (k+iσ)/8π ∫_{C₃} Tr(𝒜∧d𝒜 + ⅔𝒜∧𝒜∧𝒜) + (k−iσ)/8π ∫_{C₃} Tr(Ā∧dĀ + ⅔Ā∧Ā∧Ā)`
- **花体** $\mathcal A$ 与 $\bar{\mathcal A}$（不是普通 $A/\bar A$）✅——这正是 Lead 特别提醒的一点，tr-07 处理正确。
- 两项系数 $k+i\sigma$ 与 $k-i\sigma$ ✅（tr07b 用 `\ii`）；$(2/3)$ ✅；$\dd\mathcal A$ 的 d 为 upright ✅。
- 紧接正文 `𝒜 = A + iΦ` 为 $\mathcal A=A+\ii\Phi$ ✅（大写 $\Phi$，不是 $\phi$）。

### 2.9 (9.7)（p.97，tr07b.tex:99–106）— ✅ 正确

原图（放大图 `work/tmp/z97_97.png`）：
1. `Z_{S²×_q S¹}[T(g,C₃,K₁)] = Z_{C₃}[G_ℂ at levels (0,σ)],  q = e^{2π/σ}`
2. `Z_{S³_b}[…] = Z_{C₃}[G_ℂ at levels (1, (1−b²)/(1+b²))]`
3. `Z_{L(k,1)_b}[…] = Z_{C₃}[G_ℂ at levels (k, k(1−b²)/(1+b²))]`

- 三行与 `gathered` + 单 `\tag{9.7}` ✅（原文三行共一个编号 ✅）。
- 关键细节 `q = e^{2π/σ}` **无虚数单位 i** ✅（易错点，tr-07 抄对）。
- 第一行下标 `S^2\times_q S^1`（q 作下标）✅；第三行 `L(k,1)_b` ✅；$G_\C$ ✅。

---

## 3. 结构、标题、要点框、脚注（Lead 任务 3）

- **§9 标题**：`\section{其他几何}` ← "Other geometries" ✅（p.91 原书为 "9 Other geometries"）。
- **§10 标题**：`\section{结论}` ← "Conclusions" ✅（p.99）。
- **9.1–9.4 小节**：`升到 5d 与 q-Toda` / `超共形指标与 2d q-YM` / `3d/3d 对应` / `更多的几何设置`，与 p.92 "Lift to 5d and q-Toda"、p.94 "Superconformal index and 2d q-YM"、p.96 "3d/3d correspondence"、p.98 "Some more geometric setups" 逐字对应 ✅。
- **§9 要点框（p.91）**：原文带深色标题条 "AGT correspondence in some other geometries"，tr-07 用 `\begin{keybox}{在其他一些几何中的 AGT 对应}` ✅ 正确（该框**有**标题，与 §10 的框不同）。四条要点顺序、粗体引导语均照原文 ✅。
- **§10 要点框（p.99）**：原文**无**标题条，tr-07 用裸 `tcolorbox`（tr07c.tex:46–53）复刻浅灰底/黑框，三条要点顺序与 `\textbf` 标签照抄 ✅。**提示**：Lead 已在 preamble 加 `keyboxplain`，可改用它统一风格（见 O4）。
- **脚注**：共 **8 条**，与原文 67–74 一一对应，内容与锚点全对：
  | 脚注 | 页 | tr-07 位置 | 内容核对 |
  |---|---|---|---|
  | 67 | p.91 | tr07a:93（"q-形变"后）| q 与规范耦合无关 ✅ |
  | 68 | p.92 | tr07a:98（"[151]."后）| 感谢 Nieri ✅ |
  | 69 | p.92 | tr07a:103（"[625]）"后）| Ding–Iohara ✅ |
  | 70 | p.93 | tr07a:133（"q-Toda 理论"后）| 只谈手征块时也叫 q-Liouville ✅ |
  | 71 | p.94 | tr07b:28（"这些参数之外"后）| 指标形式不变性失效/wall-crossing ✅ |
  | 72 | p.95 | tr07b:57（"波函数"后）| 额外 R 对称性逸度 t ✅ |
  | 73 | p.96 | tr07b:74（"规范理论"后）| 非标准记号 T_N[C₃∖K₁] ✅ |
  | 74 | p.97 | tr07b:98（"能级 k=0…"后）| [311,312] 差异是否解决 ✅ |

---

## 4. 漏译 / 语义偏差（Lead 任务 4，逐页对照 split 文本）

我把 p.90–p.102 的每一段与 tr-07 正文逐段对齐（13 页、约 90 段），**没有发现整段或整句漏译**。逐段覆盖情况：

- p.90：Verlinde 圈续句、α 的连续参数段、Janus wall、S-duality wall、两段 "For instance/Bootstrapping"、(8.11) 前后 ✅
- p.91：(8.12)、"Just like the T[G] theories…"、Boundary CFT 两段、§9 要点框、§9 引言两段 ✅
- p.92：(9.1 前) 9.1 引言、Instanton partition functions 四段、五膜网/谱对偶段、4d 极限与其它极限段 ✅
- p.93：q-Painlevé 句、Compact partition functions (9.1)、三轴长段、q-Toda 图景段、半 BPS 算子段、余维 4 算子句、Geometric setup 段 ✅
- p.94：q-Toda 本性段、Elliptic lift、9.2 引言、超对称指标三段、(9.2)、指标性质两段 ✅
- p.95：(9.3)+说明段、Class S 三段、(9.4)、自举段、(9.5)+波函数段 ✅
- p.96：波函数各级极限段、检验与推广段、9.3 引言两段、四面体/三角剖分段 ✅
- p.97：Statement 段、(9.6)、非紧群段、能级对应段、(9.7)、全纯块段、Boundaries 段 ✅
- p.98：Janus 续句、纽结不变量两段、9.4 标题、2d/4d 两段、Less supersymmetry 两段 ✅
- p.99：Calabi–Yau 续句、class S_k 段、F 理论段、两族 N=1 SCFT、Miscellaneous 四段、§10 标题+要点框+引言、Integrable systems 首段 ✅
- p.100：谱曲线续句、NS 极限/面算子、BPS/CFT 段、Bethe/gauge 段、可积模型文献句、Topological strings 五段 ✅
- p.101："include […]"续句、Symmetries and special polynomials 两段、椭圆 Hall 代数三段、DIM、量子环面、仿射 Yangian ✅
- p.102：SH^c 两段、代数应用段、Further algebras 五个 bullet、椭圆顶点段、Matrix models 两段（末句跨页） ✅

唯一**语义偏差**（不是漏译）：

- **O1（可选改）p.102 末句 → p.103 首行**：原文 "which are available **provided** the sum of Liouville/Toda momenta … **is** suitably quantized." 是「**只要**…被适当量子化即可（就可用）」。tr-07（tr07c.tex:145）译作「而后者的可用性**取决于**每个三穿孔球面中 Liouville/Toda 动量之和**是否**被适当量子化」——把"前提条件"漂移成"是否（的条件句）"。建议改为：「…而后者的可用性以每个三穿刺球面中 Liouville/Toda 动量之和被适当量子化为前提」。

---

## 5. 边界（Lead 任务 4 后半）

### 5.1 p.90 起点（tr-06 → tr-07）— ✅ 无缝

- tr-06 末尾（tr06c.tex 末行）：「在 CFT 一侧，情形与圈算子类似，并且」
- tr-07 开头（tr07a.tex:5–6）：`% [原文 p.90]` + 「就得到 $\gamma$ 上的 Verlinde 圈，它由插入与该缺陷相关联的顶点算子 $V_\alpha$ 并使其绕 $\gamma$ 移动而构造出来。」
- 原文 p.90 首句 "gets the Verlinde loop on γ constructed by inserting the vertex operator Vα associated to the defect and moving it around γ." → 合起来是「…并且就得到 γ 上的 Verlinde 圈…」，**无重复、无缺口、无改写**。Lead 给出的期望串与实际情况一致。

### 5.2 p.102 末句（tr-07 → tr-08）— ✅ 无缝

- 原文 p.102 末："…Dotsenko–Fateev free-field representations of conformal blocks, which are available provided the sum of"；p.103 首："Liouville/Toda momenta in each three-punctured sphere is suitably quantized."
- tr-07（tr07c.tex:145）已把该句补完到 "…是否被适当量子化。"，并在 tr07c.tex:146–147 用普通注释说明"由本片段收尾、tr-08 自 p.103 第三行起续写"。
- tr-08 开头（tr08a.tex:7）：「保形块中的内动量则对应矩阵模型积分中围道的选取 [289, 1081, 1082]。…」= p.103 第 2 句 "Internal momenta in the conformal block translate to choices of contours in the matrix model integral [289, 1081, 1082]." ✅ **既不重复也不缺口**。
- 附带提示（属 tr-08，不属 tr-07，仅因接缝一并报告）：tr-08 用「**保形块**」「**内动量**」，全书其余块用「共形块」「内部动量」，建议 Lead 统一（见 O9）。

---

## 6. 批注质量

- 数量 22 条（13 页），远超 STYLE_GUIDE §5 下限，无空话、多数带核对锚点，质量好。**唯一内容错误**见 O2。
- 抽查若干条：p.100 Nekrasov–Shatashvili 极限的 $\epsilon_2=0$ 与 $\hbar=\epsilon_1$ 锚点 ✅；p.96 各极限层次（Schur ⊂ Macdonald ⊂ 一般 $(p,q,t)$，Hall–Littlewood 为 $p=q=0$）✅；p.102 的 $q$/$h$ 两种参数化不统一 ✅（原文确实如此）；p.101 双点记号（$\ddot{\mathcal U}$、$\ddot Y$、$\ddot{\mathrm{SH}}$）提示 ✅ 有用。
- 提示：密度偏高，若 Lead 想压缩，可优先精简 p.90、p.93 两条较短的（不影响正确性）。

---

## 7. 术语一致性

| 词 | tr-07 用法 | 全书/glossary | 判定 |
|---|---|---|---|
| three-punctured sphere | **三穿孔球面**（2 处） | 三穿刺球面（其余块 17 处）| ❌ 必须改（M2）|
| 理论符号 T(g,C,D) | 斜体 `$T(…)$`（15 处正文）| 正体 `\mathrm{T}`（其余块 42 处）；原书 p.91/p.97 也印正体 | ❌ 必须改（M3）|
| tinkertoy | 保留英文 | 同 glossary | ✅ |
| semidegenerate / degenerate | 退化 / 半退化 | 同 §7 | ✅ |
| fugacity | 逸度 | 与 §8 各块一致 | ✅ |
| 自举 (bootstrap) | 自举 | 我的块用「共形自举」 | ⚠️ 二者皆可，建议 Lead 定一个（小） |
| 五膜网 (fivebrane web) | 五膜网 | glossary 仅 brane web→膜网 | ⚠️ 可接受，提示 O6 |
| 面算子 / 畴壁 / 箭图 / 逸度 / 精细拓扑顶点 / 全纯块 | 与 glossary 一致 | — | ✅ |
| U(N−1) / SU(N) / SO | `\mathrm{U}`/`\mathrm{SU}` | 同 | ✅ |

---

## 8. 必须改（3 条）

### M1. (8.12) 方括号横档方向反了（tr07a.tex:63–64）

现码渲染为「][」，原图为「[ ]」。修法见 §2.2 给出的两行替换代码。
- 判据：原图放大 `work/tmp/z91_812.png` 中左括号竖线在最左、上下横档朝右；右括号竖线在最右、横档朝左。

### M2. 「三穿孔球面」→「三穿刺球面」（tr07b.tex:45、tr07c.tex:145）

- 全书其余块统一用「三穿刺球面」（17 处），glossary 亦以「穿刺点」为 puncture 的译名；只有这 2 处作「穿孔」。机械替换即可。

### M3. 理论符号用斜体 `$T(…)$`，与全书正体 `\mathrm{T}(…)` 不一致

涉及 15 处正文（tr07a:20、70、85、91；tr07b:45、47、54、74、76、83、101、102、103；tr07c:5、9），另有 1 处注释（tr07a:79）也写斜体。
- 依据：① 其余各块合计 42 处 `\mathrm{T}`、仅 4 处斜体；② 原书 p.91 "T(g, C, D)"、p.97 "T(g, C₃, K₁)" 均印**正体** T。
- 机械替换：`$T(\fg` → `$\mathrm{T}(\fg`；`$T[G]` → `$\mathrm{T}[G]`；行内的 `T(\fg,C_3,K_1)` → `\mathrm{T}(\fg,C_3,K_1)`（含 `\big[…]` 里的三处）。注意 (9.7) 三行里的 `T(\fg,C_3,K_1)` 也要改。

---

## 9. 可选改（9 条）

- **O1** p.102 末句 "provided … is quantized" 译成「取决于…是否」→ 建议改「以…被适当量子化为前提」（详见 §4）。
- **O2** tr07a.tex:23–24 批注把 (8.11) 的 "S-move kernel" 说成「S-移动（braiding）核」——**S-move 与 braiding 是两种不同的模变换**（原文 §8 与 (8.12) 右侧才是 braiding kernel）。建议删去括注 braiding，或改写为「（modular S-move）」；第 24 行「其 S-移动核应与 [611, 612] 的四点 Virasoro 编织核相符」同理建议改为「S-移动核由…编织核的模变换得到」。
- **O3** §9 要点框第 3 条漏译 "on C₃"：原文 "match complex g_ℂ Chern–Simons theory **on C₃** at level 0, 1 or k"；tr07a.tex:86 只写「与 $\fg_\C$ 上的复 Chern–Simons 理论在能级 0、1 或 $k$ 处相符」。建议补「在 $C_3$ 上」。
- **O4** §10 要点框用裸 `tcolorbox`（tr07c.tex:46–53）；Lead 现已加 `keyboxplain`，建议改为 `\begin{keyboxplain}…\end{keyboxplain}` 统一（现参数与 keyboxplain 等价，改后视觉不变）。
- **O5** (8.12) 两条斜线的接点：原图从 2N 方框左上/左下角连到上/下 N 圆的**右下/右上**（约 4/8 点钟方向）；tr-07 接到 `Nt.east`/`Nb.east`（水平点），视觉偏水平。可改 `(Nt.south east)`/`(Nb.north east)`。
- **O6** 「五膜网」：原文 "(p,q) fivebrane webs"，可保留，也可统一为「5-膜网」；glossary 未收，建议 Lead 决定。
- **O7** 页界注释位置：tr07a.tex:44 把 `% [原文 p.91]` 放在 (8.12) 之前，但该页首句 "on both sides of the wall," 已在上一行（p.90 行）译完；tr07c.tex:25 把 p.99 标记放在句子中间。二者都无碍编译，建议统一规则：「页界注释置于该页**第一段完整内容**之前」。
- **O8** tr07a.tex:79 注释里自称「全书他处（如 p.12、p.97）均写 $T(\fg,C,D)$」，但笔误写成斜体；改 M3 时顺手改成 `$\mathrm{T}$` 更自洽。
- **O9**（跨块，不属 tr-07）tr08a 用「保形块」「内动量」，其余块用「共形块」「内部动量」；建议 Lead 统一，以免 2d CFT 术语在 §10 之后突变。

---

## 10. 原文笔误一览

**tr-07 已正确标出的（5 处）**：
1. p.91 "punctures **which** extra data D" → 疑为 **with**（tr07a.tex:77–79 批注）✅ 判断合理。
2. p.94 "it is **an** renormalization group flow invariant" → 应为 **a**（tr07b.tex:25 批注）✅ 已用 split 文本核实原文确为 "an"。
3. p.102 "I do not know if there **is are** analogues" → 应为 **are**（tr07c.tex:128）✅。
4. p.102 "**Skylanin** algebra" → **Sklyanin**（tr07c.tex:136）✅。
5. p.101 末 "¨Y_{q₁,q₂,q₃}(gl₁)" 与同条开头 "¨Y_{h₁,h₂,h₃}" 的 $q$/$h$ 参数化不统一（tr07c.tex:109–112）✅ 原文确实如此。

**tr-07 未标、但可补的（3 处，非必须）**：
6. p.93 "the two fixed **point** of the supercharge squared" → **points**（tr-07 译「两个不动点」正确，只是没标注）。
7. p.98 "They also lead to new 4d N = 2 **［缺 theories］** that may be 'minimal'" → 原文漏名词（tr-07 译「新的 4d N=2 理论」，语义已补对）。
8. p.100 "developped" → **developed**（拼写；tr-07 未处理该词，只译其义）。

---

## 11. 复核建议（给 Lead 的最小动作）

1. 只改 M1 的三行（两行 `\draw` + 如需一并微调 O5 的两条 `\draw`），其余不动也不会错。
2. M2/M3 都是机械替换，建议用脚本一次改完再编译一遍（改完 `\tag` 数量应仍为 174）。
3. O1、O2、O3 各一句话，改与不改都不影响数学正确性；若时间紧可只改 O2（批注写错术语，读者可见度最低，但仍属"自我矛盾"）。
4. 我的 tr-05 块已按你的要求补了 p.69 关于 $b=\sqrt{\tilde q/q}$ 与 (6.20) 的 Tutor Note（约定差异 + 两种反解 + $b=1$ 锚点），并已确认 `keyboxplain`、`crop.py` 的改动在我的文件里生效；tr05b.tex 现有 6 条批注、花括号 151/151 平衡。

---

### 附：本报告用到的临时文件（都在 `work/tmp/`，可删）

`crop2.py`（crop.py 修好前的本地替代，现已被 Lead 修好的版本取代）、`z90_811b.png`、`z91_812.png`、`z93_91.png`、`z93_91b.png`、`z96_disp.png`、`z97_97.png`、`clean/p090.txt…p103.txt`。
