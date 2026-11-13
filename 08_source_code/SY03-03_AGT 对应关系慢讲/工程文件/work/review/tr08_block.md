# tr-08 块交叉校对报告（原文 pp.103–106；tr08a/tr08b/tr08c）

校对者：tr-06　　日期：2026-11-03
方法：逐页对照 `work/pages/p103–p106.png`（局部 700 dpi 放大核公式）+ 文字层；并实看成品 `work/src/main.pdf`（131 页）p.87–89 排版。

## 0. 结论摘要

| 项目 | 结果 |
|---|---|
| 结构（接续/小节/附录编号） | ✅ 通过（详见 A） |
| 缩写表 33 条 | ✅ 33/33 一条不少、顺序与原文完全一致；仅 1 处术语译名待统一（见「必须改」） |
| 附录 A 四组特殊函数公式 | ✅ 逐符号核对全对（见 C） |
| 漏译 | ✅ pp.103–106 正文全覆盖；**本段原文没有脚注**（你记的 100–104 号不在本段） |
| longtable 溢出/断行 | ✅ 无溢出（实看成品 p.87–88），仅跨页无表头重复（见可选改 5） |
| 术语一致性 | ⚠ 2 处跨块不一致（irregular；protected subsector），1 处原文内部不一致（NS 极限） |

**tr-08 三份文件中没有发现「硬错误」**：没有公式抄错、没有漏译、没有编号错位。下面「必须改」第 1 条是**跨块术语裁决**，改哪一边由你定。

---

## 必须改

### 1. 「irregular」全篇译名不一致 —— 需你裁决改哪一边

| 文件 | 现有译法 | 出现处 |
|---|---|---|
| `c00.tex`（Lead） | 非正规（irregular） | 「……对应于非正规（irregular）CFT 算子」 |
| `c01.tex`（Lead） | 非正规 | 「……把主顶点算子换成了非正规算子」 |
| `tr08b.tex`（tr-08） | 非正规态 | BMT 条：「2d CFT 中的非正规态」 |
| `tr06b.tex`（**tr-06，我的块**） | **不规则**算子/态 | 「……的不规则算子（irregular operators）」「不规则态（irregular states）」 |

- tr-08 这边**与 c00/c01 一致**，按多数（3:1）口径 tr-08 **不需要改**；需要改的是我的 tr06b（2 处）。
- 若你偏好「不规则」（更贴近 irregular 字面，且能避开与 non-normalizable「非正规（可归一化）」的混淆），则要改 `tr08b.tex` 1 处 + `c00.tex`/`c01.tex` 各 1 处。
- **建议**：统一为「非正规」+ 在 c00 首现处保留英文括号（已有），我这边改 tr06b 两处；你可回复一句确认，我立刻改（不改别人文件）。

---

## 可选改（按性价比排序）

1. **标题层级**：`tr08b.tex:8` `\subsection*{缩写表}` → `\section*{缩写表}`。
   依据（用 PDF 内嵌字体度量，非目测）：原文 p.104「Acknowledgments」= LMRoman12-Bold **14.35pt**；p.105「Table of acronyms」= LMRoman12-Bold **14.35pt**；p.105「A Special functions」的「A」也是 **14.35pt**。三者同级。而译文成品里「致谢」= 14.35pt、「缩写表」= **11.96pt**（\subsection*），故「缩写表」比原文矮了一级。改成 `\section*` 后即为 14.35pt，与致谢、与「A 特殊函数」三者一致。

2. **p.104「chiral blocks」**（`tr08a.tex:44`）现译「共形块」，应为「**手征块**」。
   原文："likewise **the chiral blocks** of the $q$-deformed Virasoro algebra and $qW$-algebras give solutions of $q$-Painlevé equations"。同段前半句 "conformal blocks ... Fourier transformed" 才是「共形块」，两处不可混。全篇 `tr07a.tex` 已统一用「手征块」（3 处）。

3. **protected subsector**：`tr08a.tex:30`「受保护子部门」↔ `tr04c.tex`「受保护子扇区」（同一短语）。建议统一（「子扇区」更常见；但 `c01.tex` 也用「子部门」）。tr-08 这边只改一个词。

4. **parafermionic**：`tr08a.tex:42`「仲费米子 Liouville CFT」，而 `tr05b.tex` 全篇保留英文 `parafermion`（4 处）。建议二选一统一（推荐首现「parafermion（仲费米子）」、后文保留英文）。

5. **缩写表排版增强**（纯美观，不影响正确性）：longtable 跨 p.87→p.88 时无表头重复，也无 booktabs 三线。可加 `\endhead` 与 `\toprule/\midrule/\bottomrule`（STYLE_GUIDE §7 对表格的建议）。当前**无溢出**，13.1cm + 标签列 ≈ 15.2cm < 16cm 版心。

6. **缩写表 NS 条**（`tr08b.tex:35`）：「（$b\to0$ 极限，即 $\epsilon_1\to0$）」照译原文 p.105 **无误**，但原文本身与 p.86 不一致：p.86 明写「NS 极限 $\epsilon_2\to0$」，而 p.8/p.52/p.86 统一用 $\epsilon_1=b/r,\ \epsilon_2=1/(rb)$，故 $\epsilon_2\to0 \Leftrightarrow b\to\infty$，不是 $b\to0$。两处只在把 $\epsilon_1\leftrightarrow\epsilon_2$ 重命名后才一致。建议：**不改译文**，在缩写表后补一句批注说明原文两处差一个 $\epsilon_1\leftrightarrow\epsilon_2$ 的重命名（或由你裁定按 p.86 校正为「$b\to\infty$，即 $\epsilon_2\to0$」）。

7. **批注位置**：`tr08a.tex:8` 的批注讲 $b^2=\epsilon_1/\epsilon_2\ne-1$，该式出现在**下一段**（`tr08a.tex:10`）。建议下移到该段之后，读者对照更顺。

8. **`tr08a.tex:8` 批注措辞**：其中「p.105 缩写表 'NS' 条……正是在 $b\to1/b$ 对称下对同一个 NS 极限的表述（等价地 $\epsilon_1\to0$）」略强：$b\to1/b$ 交换的是 $\epsilon_1,\epsilon_2$，严格说是「同名极限在两种 $b$ 规范化下的表述」，建议改成与第 6 条一致的措辞。

9. **resurgence**：`tr08a.tex:21` 用「复活（resurgence）」，而 `tr06b.tex`（我的块）在一处只写英文 `resurgence`。建议以 tr08a 为准（首现注英文），我改 tr06b 那一处。

10. `tr08c.tex:8` itemize 用 `itemsep=4pt`，`tr08a.tex` 两处用 3pt；纯美观，统一即可。

---

## A. 结构（逐条核对）

1. **p.102→p.103 跨页句**：`tr07c.tex` 末句「……而后者的可用性取决于每个三穿孔球面中 Liouville/Toda 动量之和**是否被适当量子化**。」= 原文 "…provided the sum of Liouville/Toda momenta in each three-punctured sphere **is suitably quantized**."；
   `tr08a.tex` 首句「保形块中的内动量则对应矩阵模型积分中围道的选取 [289, 1081, 1082]。」= 原文 p.103 **第二句** "Internal momenta in the conformal block translate to choices of contours in the matrix model integral"。
   → **无重复、无缺口**，接续正确 ✅（p.103 第一行的从句已由 tr-07 收尾，符合 §10「开始者写完」）。
2. **「最后的思考」**：`tr08a.tex:49` 用 `\para{最后的思考。}`；原图 p.104「**Final thoughts.**」是**段首粗体行内标题**（不是 subsection），处理正确 ✅。同理 `\para{其他相关主题。}`（原文 "Other connected topics."）✅。
3. **`\section*{致谢}`** ✅（`tr08b.tex:3`）；原图 p.104 的「Acknowledgments」确为节级无编号标题。
4. **两个 itemize**：p.103 起 5 项（tt*、手征代数、YBE、theory space、conformal bootstrap）+ p.104 起 4 项（共形块/全息/CS、Toda 变体、分数量子霍尔、isomonodromy）= 原文 5+4 ✅；p.103 末项跨页到 p.104 首项，译文仍在一个 itemize 内 ✅。
5. **致谢全文**：p.104 末 6 行 + p.105 前 6 行，逐句对照无漏：Gomis → 其他合作者（6 人）→ Bourget 等（7 人）→ Pomoni/Sfondrini（YRISW 2020）→ 妻子与孩子 ✅。
6. **`\appendix` + `\section{特殊函数}`** ✅（`tr08c.tex:3–4`）；成品 PDF p.88 实际显示为「**A 特殊函数**」，编号 A 正确。
7. 参考文献顺序（附录之后才是 References）与原文 p.106 一致 ✅（Lead 的 c-refs 接在 tr08c 后）。

## B. 缩写表（33 条逐条核对）

顺序与原文 p.105 **完全一致**（原文是两栏并排 ABJM–GW / IR–YRISW，译文改单栏 longtable 为 STYLE_GUIDE §7 允许的改编）：
ABJM, AD, ADHM, AGT, ALE, BMT, BPS, CFT, COHA, DAHA, DIM, DOZZ, DS, FI, GW, IR, JK, KK, LMNS, NS, OPE, QFT, RG, SCFT, SQCD, SW, SYM, TQFT, UV, VEV, YBE, YM, YRISW = **33 条，一条不少** ✅

逐条英文全称/释义核对（只列需要点到的）：
- ABJM：Aharony–Bergman–Jafferis–Maldacena（M2 膜世界体积理论）✅
- AD：strongly coupled 4d $\cN=2$ theories ✅；ADHM：(construction of instantons) ✅
- ALE：asymptotically locally Euclidean space（resolution of $\C^2/\Gamma$）✅
- BMT：Bonelli–Maruyoshi–Tanzini（**irregular** states in 2d CFT）→ 译文「非正规态」，见「必须改」1
- DOZZ：three-point function in Liouville CFT ✅；DS：reduction of W-algebras ✅
- FI：parameter in supersymmetric action ✅；GW：surface defect ✅
- IR：low energy/long distance ✅；JK：residue prescription ✅；KK：reduction on circle ✅
- LMNS：formula for the instanton partition function ✅
- NS：$b\to0$ limit, i.e., $\epsilon_1\to0$ ✅（照译；原文内部不一致见可选改 6）
- SQCD：SYM plus matter ✅；SW：curve $\Sigma$ and differential $\lambda$ giving IR description and prepotential $F$ of 4d $\cN=2$ theories ✅；SYM：4d $\cN=2$ vector multiplet ✅
- UV/VEV/YBE/YM(non-supersymmetric)/YRISW ✅

## C. 附录 A 公式（p.105–106 放大逐符号核对，全部一致）

1. $\Gamma(x)=\prod_{n\ge0}^{\mathrm{reg}}\frac{1}{x+n}$，极点在 $-\Z_{\ge0}$，平移 $\Gamma(x+1)=x\Gamma(x)$ ✅
2. $\Gamma_b(x)=\prod_{m,n\ge0}^{\mathrm{reg}}\frac{1}{x+mb+n/b}$，极点在 $-b\Z_{\ge0}-b^{-1}\Z_{\ge0}$，平移 $\Gamma_b(x+b)/\Gamma_b(x)=\sqrt{2\pi}\,b^{xb-1/2}/\Gamma(xb)$ ✅
   （放大确认指数是 $xb-\tfrac12$，不是 $\tfrac12-xb$；$b$ 的指数与 $\Gamma(xb)$ 分母位置均正确）
3. $S_b(x)=\frac{\Gamma_b(x)}{\Gamma_b(b+1/b-x)}$，极点 $-b\Z_{\ge0}-b^{-1}\Z_{\ge0}$，零点 $b\Z_{\ge1}+b^{-1}\Z_{\ge1}$，平移 $S_b(x+b)/S_b(x)=2\sin(\pi bx)$ ✅
4. $\Upsilon_b(x)=\frac{1}{\Gamma_b(x)\Gamma_b(b+1/b-x)}$，零点为上述两集之并，平移 $\Upsilon_b(x+b)/\Upsilon_b(x)=b^{1-2bx}\Gamma(bx)/\Gamma(1-bx)$ ✅
5. 「$\Gamma_b,S_b,\Upsilon_b$ 在 $b\to1/b$ 下不变」✅

译文批注的数学核对（我独立算过）：
- $\prod^{\mathrm{reg}}$ 的 ζ 正规化常数：$\prod_{n\ge0}^{\zeta}(x+n)=\sqrt{2\pi}/\Gamma(x)$（由 Weierstrass 乘积），故原式与 $\Gamma(x)$ 差 $\sqrt{2\pi}$ 常数——批注说法正确 ✅
- $S_b$ 零点：$Q-x=-mb-n/b\Rightarrow x=(m+1)b+(n+1)/b$，系数 $\ge1$ ✅
- $S_b$、$\Upsilon_b$ 平移公式用 $\Gamma_b$ 平移两次 + $\Gamma$ 反射公式推导，两处结果均与原文相符 ✅

## D. 漏译/脚注

- pp.103–106 **没有脚注**（p.103、p.104、p.105、p.106 页脚均为空白或参考文献），故不存在漏译脚注；你提到的「100–104」不在本段。
- 正文覆盖：p.103（6 段 + 2 bullet）、p.104（3 bullet + 2 段 + Final thoughts + Acknowledgments 起）、p.105（致谢续 + 缩写表 + A 节标题 + 第 1 条）、p.106（后 3 条 + Note + References 起）——逐段对应，无整句遗漏 ✅
- 未发现整句英文残留（唯一英文串是 "4d class S"，属允许保留术语）✅

## E. 成品排版实看（main.pdf）

- p.87：最后的思考 → 致谢 → 缩写表（ABJM…SQCD）
- p.88：缩写表后半（SW…YRISW）→ **A 特殊函数** → 四条公式
- 表格无溢出、无列宽错乱；长条目（SW/YRISW/SQCD）正常折行；仅「YRISW」行在「研讨会」中间折行，CJK 断行可接受。
- 两处可改进（非错误）：跨页无表头重复；缩写表字号用 `\small` 与原图接近 ✅

## F. 我未改任何文件

按你的要求只写本报告。若你确认「必须改 1」按「非正规」统一，我可立即改 `tr06b.tex` 的 2 处（以及可选改 9 的 1 处），其余涉及 c00/c01/tr08b 的改动请指派给对应负责人或你直接改。
