# N=2 超对称规范理论中的 S-对偶导引（中文译注本）

**底本（唯一依据）**：L. Alvarez-Gaumé, S. F. Hassan,
*Introduction to S-Duality in N=2 Supersymmetric Gauge Theory (A Pedagogical Review of the Work of Seiberg and Witten)*,
arXiv:**hep-th/9701069v1**（CERN-TH/96-371，1996 年 12 月；82 页，7 幅插图；期刊版 Fortschr. Phys. **45** (1997) 159–236）。

**成品**：中文译注本，A4 单栏，XeLaTeX 编译，正文 94 页（含目录、译本说明、审校批注索引）。

---

## 一、交付物清单

| 文件/目录 | 内容 |
|---|---|
| `9701069v1(2)_中文译注.pdf` | **成品 PDF**（94 页，XeLaTeX 两遍编译，0 error） |
| `main.tex` | 主控文件（`\documentclass{ctexart}`，按原文章节顺序 `\input` 各分片） |
| `preamble.tex` | 导言区：宏包、版式、`keypoints` 环境、页眉页脚定义 |
| `front.tex` | 封面、摘要、译本说明（含**符号约定说明**、图表清单、编译说明） |
| `refs.tex` | 参考文献（保留原文英文条目，编号 [1]–[40] 与原文一致） |
| `notes_index.tex` | 附录：审校批注索引（209 条，自动汇总生成） |
| `translate/part_A.tex` … `part_G.tex` | 正文七个分片的译文源码（按原文章节切分） |
| `translate/part_H.tex` | 致谢译文 |
| `translate/src/src_A.tex` … `src_G.tex` | 各分片对应的**英文 LaTeX 底本切片**（已规范化），供逐行对照 |
| `figures/fig1.pdf` … `fig7.pdf` | 7 幅插图（由作者原始 EPS 矢量转换，可无损缩放） |
| `figures/fig1.png` … `fig7.png` | 插图位图预览（180 dpi） |
| `审校批注汇总.md` | 209 条批注的 Markdown 汇总（不必读源码即可检索） |
| `pages/p01.png` … `p82.png` | 原文 PDF 逐页渲染（150 dpi），批注核对的底图 |
| `pagemap.json` | 章节/插图 → 原文 PDF 页码对照表 |

## 二、编译方法

```bash
xelatex main.tex
xelatex main.tex     # 第二遍生成目录、交叉引用与书签
```

- 文档类：`ctexart`（`xelatex` 专用，中文字体走 `fandol`，无需系统安装中文字体）。
- 依赖宏包：`amsmath`、`amssymb`、`amsthm`、`mathtools`、`bm`、`graphicx`、`xcolor`、
  `tcolorbox`、`caption`、`enumitem`、`booktabs`、`array`、`multirow`、`fancyhdr`、
  `hyperref`、`bookmark`（均为 TeX Live 标准配置）。
- 已验证：XeLaTeX 两遍 **0 error、0 undefined reference、0 missing character**。

## 三、成品规模

| 指标 | 数值 |
|---|---|
| 成品页数 | 94 页（原底本 82 页） |
| 编号公式 | **116 个**，编号 (1)–(116) 与原文**逐一相同**（自动比对通过） |
| 章节 | 4 节 + 引言；34 个小节；编号与原文一致 |
| 插图 | 7 幅（矢量 PDF），位置、图注、原文页码标注齐全 |
| 审校批注 | **209 条**（平均 2.2 条/页原文），四类：易错预警 / 含糊点拨 / 原文笔误 / 术语说明 |
| 正文汉字 | 约 5.3 万字 |
| 参考文献 | 40 条，编号与原文一致 |

## 四、结构与页码对照

“译文页”指成品 PDF 的页码；“原文页”指 arXiv PDF 的页码（原文印刷页 = 原文 PDF 页 − 1）。

| 内容 | 原文 PDF 页 | 译文页 |
|---|---|---|
| 封面 / 摘要 / 译本说明 | 1–2 | 1–6 |
| 目录 | — | 5–6 |
| 引言 | 2 | 7 |
| §1 规范场论中的磁单极 | 3–21 | 8–21 |
| §2 超对称规范理论 | 22–42 | 22–38 |
| §3 N=2 超对称规范理论的 Seiberg–Witten 分析 | 43–64 | 39–55 |
| §4 含物质的 N=2 规范理论的 Seiberg–Witten 分析 | 65–79 | 56–67 |
| 致谢 / 参考文献 | 80–82 | 68–70 |
| 附录 审校批注索引 | — | 71–94 |

各小节起页见成品目录；逐节精确对照见 `pagemap.json` 与各分片文件头的注释。

## 五、翻译与公式保真的技术做法

1. **以作者原始 LaTeX 源码为工作底本**（arXiv e-print 为单文件 `sw.tex` + 7 幅 EPS），
   而非从 PDF 文字层反推。这样公式、上下标、指标位置、`\label/\ref/\cite` 全部原样保留，
   从机制上排除 OCR 类错误。
2. 只对底本做了**结构规范化**：`\beq…\eeq`→`equation`、`\bea…\eea`→`eqnarray`、
   `\bq…\eq`→`quote`、Plain TeX 的 `\matrix{…}`→`array`、图块→标准 `figure` 环境。
   **数学内容一字未改。**
3. 译者只翻译公式之外的英文散文；所有显示公式、行内公式、`\nonumber`、`\label`、
   `\ref`、`\cite` 逐字保留。
4. **自动校验结果**：
   - 成品 PDF 中的编号公式序列与原文 PDF **完全一致**（1,2,…,116，逐项相同）；
   - 逐分片比对源切片与译文的数学片段：**缺失 0**（个别行内式仅作“$\lambda,\psi$”→“$\lambda$ 与 $\psi$”一类标点适配）；
   - `\ref`/`\cite` 全部解析（0 undefined）；
   - 全文无整句英文残留（人名、模型名、文献条目、图内文字除外）。
5. **唯一的排版层修正**：原文式 (78) 在 `equation` 环境内误带 `\nonumber`（1996 年 LaTeX 忽略该指令，
   故原 PDF 该式有编号；现代 amsmath 会真正取消编号，使其后全篇编号比原文少 1）。
   为满足“公式编号与原文逐一对应”，译本删去该多余 `\nonumber`（数学内容未动），
   该式仍编为 (78)；相应批注已记录在案。

## 六、符号约定（教授特别关注项）

原文**通篇采用号差** $(+,-,-,-)$，$\eta_{\mu\nu}=\mathrm{diag}(1,-1,-1,-1)$，$\varepsilon^{0123}=+1$。
教授要求 $(-,+,+,+)$。本译本的处理与理由：

- **严格照录原文的** $(+,-,-,-)$ **约定，不对任何公式作局部号差改写。**
  号差与 $F_{0i}$ 和 $E^i$ 的符号关系、费米子动能/质量项的相对符号、
  $\{Q,\bar Q\}$ 右端、中心荷与 BPS 界、$\theta$ 项与瞬子作用量、
  Seiberg–Witten 曲线与椭圆积分分支全部绑定，逐式局部替换必然自相矛盾。
- 若需整体改为 $(-,+,+,+)$，须同时作 $\eta_{\mu\nu}\to-\eta_{\mu\nu}$、$\gamma^\mu\to i\gamma^\mu$
  （保持 $\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}$），并相应调整作用量整体符号与费米场相位；
  这是“整体重写”而非“逐式替换”。详见 `front.tex` 第四节。

## 七、插图处理

原文 7 幅图均为作者提供的 EPS 矢量图（`fig1.eps`–`fig7.eps`）。处理方式：

- EPS → PDF **矢量**转换（Ghostscript/epstopdf），保持可缩放性，随文插入对应段落；
- **原文对这 7 幅图只标注 “Figure $n$”，没有说明性图注**。译本图注明确区分
  “原文标签”与“译者据图补写的说明”（后者不加引号），并在每条图注中标出原文 PDF 页码；
- 图注中保留了图内原始英文标注（如 “The $x$-space”、“$a$-cycle”），因为它们是矢量图内容本身。

| 图号 | 原文 PDF 页 | 内容 | 译文页 |
|---|---|---|---|
| 图 1 | 7 | 狄拉克弦与磁单极的磁场位形 | 11 |
| 图 2 | 15 | $S^2$ 上闭曲线的同伦类 | 17 |
| 图 3 | 60 | $u$ 平面上的奇点与单值变换 | 52 |
| 图 4 | 61 | $x$ 空间：双叶黎曼面 | 53 |
| 图 5 | 61 | 由环面理解 $x$ 空间 | 53 |
| 图 6 | 77 | $\lambda$ 平面上的分支点与积分路径 | 65 |
| 图 7 | 77 | 路径 $\Gamma_2$ 的变形 | 65 |

## 八、审校批注体系

- 格式：`% [Tutor Note: ...]`（LaTeX 注释，编译后不显示，供教授在源码中检索/删除）。
- 四类：**易错预警**（指标、$\gamma$ 矩阵迹、$\epsilon$ 约定、全导数/边界项、$1/2$ 与 $2\pi$ 因子、
  符号约定）、**含糊点拨**（“it is easy to see / one can show”处补出定理与文献）、
  **原文笔误**、**术语说明**。
- 全部批注按章节汇总为两个检索入口：成品**附录（第 71–94 页）**与 `审校批注汇总.md`。

## 九、原文笔误与可疑处清单

> 处理原则：**正文公式一律保留原文形式**，由批注指出问题并给出正确形式；
> 仅 §5 第 5 条所列的 (78) `\nonumber` 属编译层指令，已删除以恢复原文编号。
> “判定”列中，“确定”指可由原文内部逻辑/矩阵计算直接核验；“疑”指需教授裁定的可疑处。

| # | 原文位置 | 原文 | 判断与建议 |
|---|---|---|---|
| 1 | PDF 7 页，§1.3 首句 | $\vec B_{mon}=\vec\nabla\vec A_{mon}$ | **确定**：漏叉乘，应为 $\vec\nabla\times\vec A_{mon}$ |
| 2 | PDF 7 页，式 (14) | $g/4\pi r^2$ | **确定**：漏单位矢量，应为 $g\hat r/4\pi r^2=g\vec r/4\pi r^3$ |
| 3 | PDF 10 页，式 (26) 后 | “Since $\phi^2=a$;” | **确定**：应为 $\phi^2=a^2$，且分号应为逗号 |
| 4 | PDF 28 页，式 (57) | $D_\alpha=\partial_\alpha+i\sigma^\mu_{\alpha\dot\alpha}\partial_\mu$ | **确定**：漏 $\bar\theta^{\dot\alpha}$，应为 $\partial_\alpha+i\sigma^\mu_{\alpha\dot\alpha}\bar\theta^{\dot\alpha}\partial_\mu$，否则与原文 $\{D,\bar D\}=-2i\sigma^\mu\partial_\mu$ 矛盾 |
| 5 | PDF 28 页，式 (59) 下方 | “A and $\psi$ are the fermionic and scalar components” | **确定**：词序颠倒（$A$ 为标量、$\psi$ 为费米子） |
| 6 | PDF 32 页，式 (68) | $\int d^\theta$ | **确定**：应为 $\int d^2\theta$ |
| 7 | PDF 32 页，式 (70) | $V=\sum_i\lvert\partial W/\partial A_i\rvert^2-\frac{1}{2g^2}(A^\dagger T^aA)^2$ | **疑**：按同页式 (69) 消去 $D^a$ 应得 $+\frac{g^2}{2}(A^\dagger T^aA)^2$；符号与 $g$ 的幂次均与该式不自洽（对照式 (71) 的 $-\frac{1}{2g^2}{\rm Tr}([A^\dagger,A]^2)$ 更清楚）。请教授裁定 |
| 8 | PDF 34 页，式 (74) | $\Phi^\dagger e^{2gV}{\cal F}_a(\Phi)$ | **疑**：与式 (72) 的 $\Phi^\dagger e^{-2V}\Phi$ 不自洽（规范不变性要求同号指数；$g$ 的归属亦需统一） |
| 9 | PDF 36 页 | “$N-N_f$ zero eigenvalues”；“except for $N_c=N_f-1$” | **疑**：应为 $N_c-N_f$ 与 $N_c=N_f+1$（否则 $SU(N_c-N_f)$ 无意义） |
| 10 | PDF 36 页 | 情形 2 标题 “$N_f\le N$”；末句 “For $N_f>N$” | **疑**：按该段分类应为 $N_f\ge N_c$ 与 $N_f\ge N_c$ |
| 11 | PDF 44 页 | $v=-\frac13{\rm Tr}(\phi^3)=a_1a_2a_3$ | **确定**：符号误，应为 $v=+\frac13{\rm Tr}(\phi^3)$（由 $a_1+a_2+a_3=0$ 直接验证） |
| 12 | PDF 54 页 | $(A\tau+B)(c\tau+D)^{-1}$ | **确定**：矩阵块小写 $c$ 应为 $C$ |
| 13 | PDF 54 页 | $\partial a_Di/\partial a_j$ | **确定**：下标应为 $\partial a_{Di}/\partial a_j$ |
| 14 | PDF 56 页，式 (102) 后 | “$q_m=m,\ q_n=n$ is a solution” | **确定**：$q_n$ 应为 $q_e$（本征向量为 $(q_m,q_e)$） |
| 15 | PDF 61 页 | “first homology group $V_u=H^1(E_u,\mathbb C)$” | **记号**：标为同调却用上同调记号 $H^1$（同调为 $H_1$）；二者经 Poincaré 对偶同构，按同调使用无碍 |
| 16 | PDF 69 页，式 (112) | 第二组第二行 $\widetilde Q_1$ | **确定**：按上下文应为 $\widetilde Q_i$ |
| 17 | PDF 72 页 | ${\cal M}^{-1}$ 第三行为 $(0,1,1)$ | **确定**：由 ${\cal M}$ 求逆应为 $(0,0,1)$（用紧接的电荷变换律反验即知） |
| 18 | PDF 78 页 | “massless magnetic monopoles with one unit of magnetic charge and $n_e$ units of **magnetic** charge” | **确定**：第二个 “magnetic charge” 应为 “electric charge” |
| 19 | PDF 41 页 | “the Witten effect described in section (1.10)” | 原文**无误**：§1.10 即“$\theta$ 参数与磁单极电荷”一节（§1 共 10 个小节） |
| 20 | PDF 42 页 | $M=\sqrt2 Z$ | **确定**：应为 $M=\sqrt2\lvert Z\rvert$ |
| 21 | PDF 26 页 | 式 (53) 前 “the algebra (51) reduces to” | **疑**：按上下文应指式 (52) |
| 22 | PDF 9 页微扰谱表 | “Spin” 列对光子/$W^\pm$ 填 $\hbar$、对 $H$ 填 0 | **疑**：应为自旋量子数 $1,1,0$（即表中数值取 $s$ 而非 $s\hbar$） |
| 23 | PDF 18 页 | $\lvert s>$、$\lvert c>$ | **确定**：应为 $\lvert s\rangle$、$\lvert c\rangle$ |
| 24 | PDF 16 页 | “we will prove later $g=4\pi N/e$”；“$\pi_2(G)$ can be embedded in $\pi_2(G/H)$ as its identity element” | **表述不严**：式 (37)–(42) 只给出拓扑荷的等价表述，未再单独“证明”该式；$\pi_2(G)$ 是 $\pi_2(G/H)$ 的像（正合序列意义），非“作为单位元嵌入” |
| 25 | PDF 47 页 | “Invariance of $\phi^3$ picks $n=2N_c,4N_c$”；“For SU(4) and higher … no subgroup survives” | **表述不严**：单看 $\phi^3$ 只给 $n$ 偶（${\bf Z}_6$），须与 $\phi^2$ 条件取交才得 ${\bf Z}_2$；后半句应理解为商掉 $SU(2)_R$ 中心后不再给出新对称性 |
| 26 | PDF 39 页 | “the supercurrent is not just the sum of the above, plus…” | **含混**：原意为超流除上列各项外还包含其它项；译文按正确语义译出并批注 |
| 27 | PDF 65 页 | “to insure asymptotic freedom we require $N_f\le4$” | **表述不严**：由式 (beta) 知 $N_f=4$ 时 $\beta=0$（有限/共形），严格渐近自由条件为 $N_f<4$ |

**拼写/排印笔误**（均不改动公式，译文按正确词义处理，批注已汇总）：
`intented`（2 页）、`proporties`（3）、`Minkowsky`（3）、`quations`（4）、`elecromagnetic`（5）、
`fermios`（6）、`intrduuced`（7）、`satifying`/`representaion`/`cavariant`（8）、`easiy`/`guage`/`treate`/`depends of`（11）、
`in term of`（12）、`sphare`（14）、`the the`（14、25、56）、`componenets`（18）、`weekly`/`monoples`/`superysymmetry`/`in the in the`（19）、
`inegral`（20）、`respectivly`（21）、`descrbing`（22）、`suplement`/`assiged`（24）、`metrices`/`Lapuszanski`（26）、
`assumtion`/`algera`/`representatin`/`supressed`/`superfieled`/`fundamantal`/`fileds`/`satify`（§2 各页）、
`containts`（43）、`non-tivially`/`non of`（47）、`sompnent`（50）、`equivanlently`（52）、`close loop`（53、54、61）、
`geting`（54）、`associalted`/`elementary stat`/`gauge theroy`/`in terms our`/`singuralites`/`Sine`/`anyone`/`regrad`/`Upto`/`hypergeometirc`（54–64）、
`martices`（72）、`varialbles`/`analoguous`/`representaion`（73–75）、`sigularities`（74–75）等。

## 十、需要教授裁定的开放问题

1. **式 (70) 的 D 项势**（第 32 页）：符号与 $g$ 幂次似与该页式 (69) 不自洽（见清单 #7）。
   本译本正文保留原文，批注给出推导；若教授确认，可一键改为 $+\frac{g^2}{2}(A^\dagger T^aA)^2$。
2. **式 (74) 的指数符号**（第 34 页）：$e^{2gV}$ 与 $e^{-2V}$ 的规范不变性要求需统一（清单 #8）。
3. **微扰谱表的“Spin”列**（第 9 页）：是否按 $s\hbar$ 或 $s$ 理解（清单 #22）。
4. 其余“表述不严”处（清单 #24–#27）是否改写，取决于教授对“逐字忠实”与“物理清楚”的取舍；
   本译本一律保留原意，仅在批注中说明。

## 十一、已知限制

- 原文 7 幅插图**没有说明性图注**，中文图注中已明确区分“原文标签”与“译者补写说明”；
- 参考文献保留英文原条目（学术惯例），仅统一了排版；
- 未做主题索引与人名索引（原文亦无）；
- 批注 209 条为译者与 Lead 的审校意见，不排除仍有可商榷处；批注不参与编译，可整体删除后得到“纯净译本”。

## 十二、生成方式

本译本由 Lead 与 7 个译者分片协同完成：Lead 负责底本获取与规范化、导言区/主文件、插图矢量处理、
页码映射、分片派发、合成编译、公式编号与数学内容自动校验、批注索引生成与终审；
各译者负责一个分片（A：引言 + §1.1–1.4；B：§1.5–1.10；C：§2.1–2.5；D：§2.6–2.9；
E：§3.1–3.5；F：§3.6–3.9；G：§4.1–4.6）。全部数学内容以源码逐字搬运，不经二次转录。
