# tr-04 块（原文 pp.51–63）结构与图表交叉校对报告

- 校对者：**tr-03**（受 Lead 指派；侧重结构与图表；tr-07 另有侧重）
- 校对对象：`work/src/chunks/tr04a.tex`（pp.51–54）、`tr04b.tex`（pp.55–58）、`tr04c.tex`（pp.59–63）
- **审查版本**：tr04a/b/c 于 2026-11-03 10:32–10:33 的最后修改版（其中 fig3 宽度已从 0.75 改为 0.60\textwidth）。复审时若 tr-04 又有改动请以最新内容为准；下列问题已按最新版复核仍存在。
- 校对依据：`work/split/p051.txt … p063.txt`（定位）、`work/pages/pNNN.png`（200 dpi，公式与图形的唯一真值）、逐点裁图（`work/tmp/crop_tr03.py`）、以及**编译产物** `work/src/main.pdf`（131 页，2026-11-03 版），文中页码均为该 PDF 页码
- 结论概览：**tag 5.24–5.47 + 6.1–6.5 共 29 条全齐、无跳号/重号；脚注 42–49 全齐且编号对齐；Figure 3 图注照译；Table 3 十行全对；eq537/eq539 两张裁图完整；抽查的 4 条公式（(5.28)(5.43)(5.44)(6.4)）逐符号一致。** 发现 **2 处必须改**、**4 处可选改**。

---

## 一、必须改

### M1. `fig3.png` 底部残留原图英文图注（可见缺陷）
- **现象**：`work/figures/fig3.png`（1501×807 px）最后 31 行（y=776…806）是原书图注的残行，内容为
  “…construction of a U(4) × U(4) × U(3) gauge theory. Th…”。
  编译后在 **main.pdf p.48** 上，插图与中文图注「图 3：…」之间**肉眼可见一条英文残句**。
  实测（逐行暗像素统计）：y=767…775 全空，y=776 起出现文字像素 → 干净图形区止于 y=775。
- **修法（任选）**：
  1. 直接把现有 PNG 底部裁掉 32 px（改成 1501×775）；
  2. 重新裁图：`$py work\tools\crop.py 56 165 92 430 222 out\fig3.png`（PDF 点坐标；图区实测为 x 175–421、y 101–213，图注首行在 y≈235，故 y1=222 安全），裁完 **read_image 复核**：应含 NS5 / D6 / D4 / ⊗⊗ / ⊗ / Λ₁Λ₂Λ₃ 全部标签，且不含任何文字行。
- **说明**：中文图注本身翻译逐句正确（见 §三 B），只有图片像素有问题。

### M2. §6.1 标题与首段落的页码归属错位（p.61 → 应为 p.62）
- **原文**：p.61 以 “We summarize aspects of the correspondence in Table 3.”（+ Table 3 + 脚注 49）结束；**p.62 顶部**才是
  `6.1 2d CFT and Liouville CFT` 与紧随的 “We refer to reviews such as [128, 129] …”（已用 p.62 裁图确认，见 p062 顶部）。
- **tr04c 现状**：`% [原文 p.62]` 标记被放在 `\subsection{二维 CFT 与 Liouville 共形场论}` **和后一自然段之后**，
  导致 §6.1 标题与「关于 2d CFT…」段被归到 p.61 一侧。
- **修法**：把 `% [原文 p.62]` 一行**上移**到 `\subsection{二维 CFT 与 Liouville 共形场论}` 之前（只动注释行，正文与排版不变）。
- **影响**：不影响读者所见内容与编号，仅影响页码标注与"标题起始页"这条契约；但因 Lead 明确以此条为验收项，列为必须改。

---

## 二、可选改

### O1. (5.37)/(5.39) 的编号掉到图片下方（排版观感）
`tr04b.tex` 把 `\includegraphics` 直接写在 `equation` 里，图片基线在底部，故 amsmath 把 `\tag` 放在图片**下方**：
main.pdf p.49 的 (5.37)、p.50 的 (5.39) 均可见"图在上、编号在下一行右侧"。原文编号与图垂直居中。
建议改为 `\vcenter{\hbox{\includegraphics[width=…]{eq537.png}}}`（或 `\raisebox{-0.5\height}{…}`），编号即回到图右侧中部。

### O2. (5.37)(5.39) 末尾句点缺失
原文两式末尾各有一个句点（`. `），裁图未包含，译文也未补。若追求与原书形似，可在 equation 内补 `\ .`；不补亦无实质影响。

### O3. 两处措辞精修
- p.51 “hypermultiplets in the representations $R$ and $\bar R$ are equivalent (with mass $m\to-m$)” 现译「（**伴随** $m\to-m$）」。本节"伴随"专指 adjoint 表示，易误读；建议改「（质量随之 $m\to-m$）」。
- p.51 “so adding a mass $m$ in (5.25) simply changes $\Upsilon_b(\cdots)\to\Upsilon_b(\cdots+rm)$” 现译「只不过是把左端换成右端」；建议改「只需把 $\Upsilon_b$ 的宗量作如下平移」。

### O4. 给 Lead 的清单勘误：Table 3 不是"左列 8 行"，而是 **10 行**
交办说明写"「参数/构建单元」两个行标、左列 8 行"。实测原文（p.61 裁图逐格数）= **1 个独立行 + Parameters 组 4 行 + Building blocks 组 5 行 = 10 行**；
tr04 的表 **10 行全部正确**（见 §三 C 的逐格对照），**不需要改**，只需更新核对清单里的"8 行"。

---

## 三、逐项核对结果

### A. 标题与小节位置（对照原文 p.52 / p.58 / p.61 / p.62）
| 标题 | 原文页 | tr04 位置 | 结论 |
|---|---|---|---|
| §5.3 Instanton partition functions | p.52 | `tr04a`：在 (5.29) 段之后、`% [原文 p.53]` 之前 | ✅ 对齐 |
| §5.4 Cutting by localization | p.58 | `tr04b`：在 (5.40) 段之后、`% [原文 p.59]` 之前 | ✅ 对齐 |
| §6 AGT for SU(2) quivers | p.61 | `tr04c`：在「…非拉格朗日 tinkertoy。」段之后、正文首段之前 | ✅ 对齐 |
| §6.1 2d CFT and Liouville CFT | **p.62** | `tr04c`：落在 `% [原文 p.62]` **之前**（即 p.61 侧） | ❌ 见 **M2** |

补充：三个 `\subsection`/`\section` 标题译名与原文一致（瞬子配分函数 / 用局域化切割 / SU(2) 箭图的 AGT 对应 / 二维 CFT 与 Liouville 共形场论），层级也正确（§5.3、§5.4 为 subsection，§6 为 section，§6.1 为 subsection）。

### B. Figure 3（原文 p.56）
- `\begin{figure}` + `\includegraphics[width=0.60\textwidth]{fig3.png}` + `\figtitle{3}{…}`，放在 `% [原文 p.56]` 之后、"U(1) 因子"段末与"规范化带来的主要麻烦效应"段之间；正文"如图 3 所示"在其前 ✅。
- **图注逐句对照**（原文 → 译文）：
  - “Brane construction of a U(4) × U(4) × U(3) gauge theory.” → 「U(4)×U(4)×U(3) 规范理论的膜构造。」✅
  - “The leftmost U(4) factor has two fundamental hypermultiplets (inserted by transverse D6 branes depicted as ⊗)” → 「最左侧的 U(4) 因子带两个基本超多重态（由横向 D6 膜插入，图中记作 ⊗）」✅
  - “and the rightmost U(3) factor has one fundamental hypermultiplet.” → 「最右侧的 U(3) 因子带一个基本超多重态。」✅
  - “In this example each gauge group is asymptotically free.” → 「在这个例子中，每个规范群都是渐近自由的。」✅
- **图片像素**：❌ 见 **M1**（图注残行）。图形本体完整（与 p.56 原图逐项一致：3 条 NS5 竖线、各区间 D4 段、D6 与 ⊗⊗/⊗、Λ₁Λ₂Λ₃ 箭头）。

### C. Table 3（原文 p.61）逐格对照
| # | 原文左列 | 原文右列 | tr04c | 结论 |
|---|---|---|---|---|
| 行标 | （空） | （空） | （空） | ✅ |
| 表头 | Gauge theory | Toda/Liouville CFT | 规范理论 / Toda/Liouville 共形场论 | ✅ |
| 1（无行标） | Partition function on $S^4_b$ | Toda correlator on $C$ | $S^4_b$ 上的配分函数 / $C$ 上的 Toda 关联函数 | ✅ |
| 组标 | **Parameters**（旋转） | — | **参数**（`\multirow{4}{*}{\rotatebox{90}{…}}`） | ✅ |
| 2 | Squashing parameter $b=\sqrt{\epsilon_1/\epsilon_2}$ | Toda coupling constant $b$ | 压扁参数 / Toda 耦合常数 $b$ | ✅ |
| 3 | Gauge couplings in 4d | Complex structure of $C$ | 4d 规范耦合 / $C$ 的复结构 | ✅ |
| 4 | Dual gauge theory descriptions | Pants decompositions of $C$ | 对偶规范理论描述 / $C$ 的裤子分解 | ✅ |
| 5 | Full tame puncture of mass $m$ | Vertex operator $\hat V_{Q+rm}$ | 质量为 $m$ 的满驯服穿刺 / 顶点算子 $\hat V_{Q+rm}$ | ✅ |
| 组标 | **Building blocks**（旋转） | — | **构建单元**（`\multirow{5}{*}{…}`） | ✅ |
| 6 | Coulomb branch parameter $a$ | Internal momentum $\alpha=Q+ra$ | Coulomb 分支参数 $a$ / 内部动量 $\alpha=Q+ra$ | ✅ |
| 7 | Gauge one-loop determinant | Inverse two-point function | 规范单圈行列式 / 两点函数之逆 | ✅ |
| 8 | Matter one-loop determinant | Three-point structure constant | 物质单圈行列式 / 三点结构常数 | ✅ |
| 9 | Classical action contribution | Conformal block leading term | 经典作用量贡献 / 共形块领头项 | ✅ |
| 10 | Instanton partition function | Conformal block power series | 瞬子配分函数 / 共形块幂级数 | ✅ |
| 表题 | “Table 3: Basics of AGT. In Liouville CFT conventions, change $Q$ to $Q/2$.” | | 「表 3：AGT 的要点。在 Liouville 共形场论的约定下，把 $Q$ 换成 $Q/2$。」 | ✅ |

- **行数与分隔线**：10 行数据 + 表头；`\toprule` / 表头下 `\midrule` / 独立行下 `\midrule` / 两组之间 `\midrule` / `\bottomrule`，与原文 5 条横线的位置一致 ✅
- **编号**：`\tabtitle{3}` ✅（main.pdf p.53 显示「表 3：…」）
- 说明：原文该表是 JPhysA 的带色标题条＋圆角外框样式；译文按 STYLE_GUIDE §7 用 booktabs 复刻（框线风格不同属既定约定，不算缺陷）。
- **另请 Lead 注意**：这是原文真实存在的**第三个表**（前有 p.10 Table 1、p.13 Table 2）。STYLE_GUIDE §0/§7 与 BRIEF 的表清单只列了表 1、表 2 与缩写表，建议补充"Table 3 p.61"。tr04 已在其自注中提示此事。

### D. 脚注 42–49 齐全性
| 编号 | 原文页/位置 | tr04 位置 | 内容核对 |
|---|---|---|---|
| 42 | p.51，(5.24) 前句 "non-zero weights of the adjoint representation)," 后 | `tr04a` 首段句末 | ✅ Vandermonde 行列式说明 |
| 43 | p.52，(5.30) 前 "…prepotential of the gauge theory:" | `tr04a` 「低能预势…」句 | ✅ 预势定义说明 |
| 44 | p.53，"…instantons the partition function [127].44" | `tr04a` 「有若干种方法 [127]」句 | ✅ 感谢 Jaewon Song |
| 45 | p.55，$z_j$ 编码动力学能标句末 | `tr04a` (5.32) 之后 | ✅ $b_j>0$/$b_j=0$ 与重整化方案说明 |
| 46 | p.56，"schematically46" | `tr04b` (5.35) 之前 | ✅ 征求文献 |
| 47 | p.57，"…infinite tower of instanton corrections.47" | `tr04b` 该句末 | ✅ [247][248] |
| 48 | p.58，"In the following,48" | `tr04b` 该处 | ✅ 出处说明 |
| 49 | p.61，"su(2) Sicilian49" | `tr04c` §6 首段 | ✅ trinion/triskelion 命名由来 |
- **8 条全在，位置一致**；编译后编号实测为 **42–49**（main.pdf p.44 页脚可见「42 准确地说，我们在此已把…」），与原文编号完全对齐 ✅

### E. 漏译检查（对照 p051–p063 全部文字层）
逐段核对（含要点框、习题、无编号公式、括注、文献引用）结论：
- §5.2 余下（p.51–52）：(5.24)–(5.30)、单圈行列式两半球解释、(5.27)、U(1) 因子预告 ✅
- §5.3（p.52–56）：Omega 背景三段、(5.30)、5d 提升段、Computation methods 三个 bullet（ADHM/纯 SYM/质量形变 $\cN=4$）、recursion relations bullet、"Some matter representations escape…"、"Nekrasov 配分函数的推广"、(5.31)+(5.32)+脚注 45 ✅
- p.55–56：(5.33)+$S(\phi)$+指标范围、(5.34)+JK 留数、习题 5.4、U(1) 因子、(5.35)(5.36)、Figure 3 ✅
- p.56–58：重整化方案、(5.37)–(5.40) ✅
- §5.4（p.58–61）：无拉格朗日量局域化、切割 $C$、(5.41)(5.42)(5.43)、全纯因子化、(5.44)–(5.47) ✅
- §6（p.61–63）：Table 3、§6.1、Virasoro、(6.1)、习题 6.1、共形维数、(6.2)、主算子、(6.3)(6.4)、习题 6.2、两点/三点函数 (6.5) ✅
- **未发现整句或整段漏译**（唯一"缺失"是 O2 的两个句点，属标点级）。

### F. eq537.png / eq539.png 完整性与一致性
- `eq537.png`（1942×359）：完整呈现 (5.37) 六节点广义箭图——左 `Spin(4)—USp(2)—Spin(4)`、右 4 个 `SU(2)` 方框 + 中央圆角 `SU(2)` 的 Y 形接法；**未裁到编号 (5.37)**、无截断、无多余文字；与 p.57 原图逐项一致 ✅
- `eq539.png`（2376×375）：完整呈现 (5.39) 的 `T[so(4), 带分支切割的圆柱] = T[su(2), 四点球面]`（含圆柱上的割线圆点、右侧双覆盖曲面）；未含编号、无截断 ✅
- 宽度：原文 (5.37) 约占版心 0.55、(5.39) 约 0.70；译文取 0.51 / 0.62，略小但可读，可保持。

---

## 四、抽查公式逐符号结果（要求 4 条，实核 5 条）
| 公式 | 原文页 | 核对结果 |
|---|---|---|
| **(5.28)** | p.51 | ✅ $Z_{S^4_b}=\int\dd a\,Z_{\mathrm{cl}}(a,q\bar q)Z_{\text{one-loop}}(a)Z_{\text{inst}}(a,q)Z_{\text{inst}}(a,\bar q)$，与 main.pdf 排版一致；紧随文本 $Z_{\mathrm{cl}}=\exp(-S_{\mathrm{cl}})=|q|^{r^2|a|^2}$ 的**三级上标 $r^2|a|^2$** 与原文逐字一致（p.51 末行裁图核对），同页 $|a|^2=-\Tr(a^2)$ 亦对 |
| **(5.43)** | p.59 | ✅ $\prod_I[\sum_{k_I,\bar k_I\ge0}\int_{\fh_I\times\cM_{G_I,k_I}\times\cM_{G_I,\bar k_I}}\dd a_I\dd\xi_I\dd\bar\xi_I]\{\prod_I[|q_I|^{r^2|a_I|^2}q_I^{k_I}\bar q_I^{\bar k_I}Z^{\text{vector}}_{\text{one-loop}}[G_I;a_I,k_I,\xi_I,\bar k_I,\bar\xi_I]]\prod_L Z_{\mathrm{T}_L}[a,k,\xi,\bar k,\bar\xi]\}$ —— 逐因子、逐指标顺序与 p.59 裁图一致（含 $|q_I|^{r^2|a_I|^2}$ 的上标层级） |
| **(5.44)** | p.60 | ✅ $Z_{S^4_b}=\int[\mathrm{D}\Phi_{3d}]\,\ee^{-S_{3d}[\Phi_{3d}]}Z_{H S^4_b,\text{North}}[\Phi_{3d},q,\bar q]Z_{H S^4_b,\text{South}}[\Phi_{3d},q,\bar q]$，与 p.60 裁图一致 |
| **(6.4)** | p.63 | ✅ $\mathbb{L}_{-Y}\bar{\mathbb{L}}_{-\bar Y}|V\rangle:=L_{-m_1}\dots L_{-m_k}\bar L_{-n_1}\dots\bar L_{-n_l}|V\rangle$；黑板体 $\mathbb{L}$、双下标 $-Y$/$-\bar Y$、右侧 $L_{-m_k}$ 后接 $\bar L_{-n_1}$ 的顺序均与 p.63 裁图一致 |
| 附核 (5.42)/(5.45) | p.59/p.60 | ✅ (5.42) 两行结构、(5.45) 的 $Z_{\mathrm{cl},3d}Z_{\text{one-loop},3d}Z_{\text{North}}[a,q]Z_{\text{South}}[a,\bar q]$ 与裁图一致 |

---

## 五、其他观察（非缺陷，供 Lead 参考）
1. **tag 与边界**：tr04 的 tag 5.24–5.47、6.1–6.5 共 29 条，首尾与 tr-03 的 (5.23)、tr-05 的 (6.6) 衔接良好；分文件页段 51–54 / 55–58 / 59–63 与页面标记一一对应，无缺页、无重复页。
2. **块首**：`tr04a` 从 p.51 的 “Here, the vector multiplet one-loop determinant…” 起，正好接 tr-03 的 (5.23) 之后，不切句 ✅。
3. **块尾**：`tr04c` 结束于 p.63 “...by three-point functions $C_{123}$ as explained next.”，是完整句，p.64 由 tr-05 续 ✅。
4. **浮动体位置**：Figure 3 落在 main.pdf p.48 下半页、Table 3 落在 p.53 顶部，均在其引用文字之后，浮动合理；若希望图表更贴近原文位置（图在 p.56 顶部、表在 p.61 底部），可加 `[htbp]`→`[t]` 微调，非必要。
5. **公式 (5.33)** 体量极大但 `split` 未使用、单行式排版在 main.pdf 中未溢出（无 overfull），可保持。

---

### 附：本次校对使用的证据文件（均在 `work/tmp/`，可复核）
`rv51b.png`/`rv51c.png`（(5.28) 与 $|q|^{r^2|a|^2}$）、`rv52a.png`（(5.29)）、`rv537b.png`（(5.37)）、`rv59b.png`/`rv59c.png`（(5.42)(5.43)）、`rv60c.png`（(5.44)）、`rv60a.png`（(5.45)）、`rv62a.png`（p.62 顶部 §6.1）、`rv63b.png`（(6.4)）；
编译产物页图：`book_48.png`（Figure 3 缺陷实证）、`book_49.png`（(5.37) 编号位置）、`book_50.png`（(5.39)）、`book_53.png`（Table 3）、`fnn_44.png`（脚注 42 编号）。
