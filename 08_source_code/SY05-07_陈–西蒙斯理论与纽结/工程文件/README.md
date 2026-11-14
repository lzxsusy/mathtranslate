# 陈–西蒙斯理论与纽结（中文译注本）

**David Grabovsky, _Chern–Simons Theory in a Knotshell_（2022-09-14，38 页，pdfTeX）之中译、结构化重排与学术审校批注**

| 项目 | 内容 |
|---|---|
| 原文 | David Grabovsky, *Chern–Simons Theory in a Knotshell*, 2022-09-14, 38 pp., pdfTeX + hyperref |
| 原文性质 | 以 Witten 1989 年 *Quantum Field Theory and the Jones Polynomial*（Commun. Math. Phys. **121**, 351）为主线的**教学性综述**；作者 Grabovsky 写作时为学生，**不是 Witten 本人**。正文中「Witten 表明/证明了……」指被综述的 Witten 工作，译文一律保留这一表述，不把作者与 Witten 混同 |
| 译本 | 全文汉译 + 84 条学术译注（另有 5 组「本节重点」）+ 5 张原图无损插入 + 32 条参考文献原样著录 |
| 源码 | `CS and Knots.tex`（单文件，1,803 行，约 199 KB，UTF-8）+ `figures/` 5 张 PNG |
| 成品 PDF | `CS and Knots_中文译注本.pdf`（**43 页**，XeLaTeX 两遍实测编译，0 error、0 缺字） |
| 编译 | **XeLaTeX**（必须），连跑两遍：`xelatex "CS and Knots.tex"` ×2 |
| 规模 | 正文 32,970 个汉字；编号公式 **74** 个（(2.1)–(2.31)、(3.1)–(3.32)、(4.1)–(4.7)、(5.1)–(5.4)）；图 **5**；表 0；脚注 **9**；文献 **32** |
| 页锚点 | 每个原文页起始处有 `% ==== 原文 p.N ====` 注释，可逐页对照 PDF |

---

## 1. 编译方法

```bash
xelatex "CS and Knots.tex"     # 第一遍
xelatex "CS and Knots.tex"     # 第二遍：生成目录、交叉引用、hyperref 书签
```

- 中文由 `ctex` 宏包处理，**必须用 XeLaTeX**；`pdfLaTeX` 不能直接编译（会缺 CJK 字体设置）。
- 默认字体集 `fontset=fandol`（TeX Live 自带，跨平台）。若缺 Fandol，把导言区第 15 行的
  `fontset=fandol` 改成 `fontset=windows`（用宋体/黑体，Windows 本机可用）。
- 依赖宏包：`ctex, amsmath, amssymb, mathtools, bm, geometry, graphicx, xcolor, tcolorbox, enumitem, booktabs, array, caption, cite, hyperref`。全部是 TeX Live 完整安装自带的常规包，无需额外安装。
- 插图路径为 `figures/...`，**编译时须保持 `CS and Knots.tex` 与 `figures/` 在同一目录**。

### 一键隐藏译注（交付纯净译文）

导言区有两个开关：

```latex
\showyizhutrue   % 改成 \showyizhufalse：橙色「译注」方框与连续编号全部消失
\showkeytrue     % 改成 \showkeyfalse ：蓝色「本节重点」方框全部消失
```

两开关全关时，正文即为纯译文，公式编号、图表与参考文献不受影响。

---

## 2. 目录结构

```
CS and Knots_中文译注本/
├── CS and Knots.tex          单文件完整源码（可直接编译）
├── README.md                 本文件
├── REVIEW-NOTES.md           84 条译注的汇总索引（编号 = PDF 中「译注 N」，含原文页码与文件:行号）
├── 审校报告.md                学术级审校：原文笔误 13 处、已核无误 4 处、含糊点与易错点分类
├── 术语表.md                  符号表 + 术语表（约 150 条）+ 人名表 + 译名裁定记录
├── figures/
│   ├── fig1_cs_universe_anyon.png   （原 p.5，1524×506）
│   ├── fig2_anyon_torus.png         （原 p.10，886×644）
│   ├── fig3_trefoil_framing.png     （原 p.23，956×442）
│   ├── fig4_wilson_loop.png         （原 p.24，572×440）
│   └── fig5_surgery.png             （原 p.31，1212×610）
├── sections/                 分片源码（按原文节次，一人一片，便于维护）
│   ├── s00-front.tex         题名页、摘要、译者说明、目录
│   ├── s01-intro.tex         §1 引言与动机
│   ├── s02a-abelian.tex      §2 引言 + 2.1 + 2.2
│   ├── s02b-abelian2.tex     2.3 + 2.4
│   ├── s03a-framing.tex      §3 引言 + 3.1 + 3.2
│   ├── s03b-framing2.tex     3.3 + 3.4
│   ├── s04a-hilbert.tex      §4 引言 + 4.1
│   ├── s04b-hilbert2.tex     4.2 + 4.3 + 4.4
│   └── s05-wrapup.tex        §5 + 参考文献
├── main.tex                  装配入口（\input{sections/*}）
└── tools/                    维护脚本（见 §8）
```

> 修改建议：直接改 `CS and Knots.tex` 最快；若想保持"分片可维护"，改 `sections/` 后运行
> `python tools/assemble.py` 重新生成单文件（会覆盖 `CS and Knots.tex`）。

---

## 3. 排版约定

1. **公式编号锁定原文**：每个编号公式写作 `\begin{equation}\tag{2.7}\label{eq:2.7} … \end{equation}`。
   `\tag` 直接把编号钉死为原文编号，故**删改公式也不会错位**；正文引用一律 `\eqref{eq:2.7}`，渲染为 (2.7)，与原文逐号对应。原文无编号的展示公式用 `\[ … \]`，不占编号。
2. **章节编号自动生成**，与原文一致（`\section` 1–5，`\subsection` 2.1–2.4、3.1–3.4、4.1–4.4、5.1–5.2）。
3. **图号与原文一致**（图 1–5），图注末尾标注「（原文 Figure N，原文 p.N）」。
4. **原文的口语化小标题**（Euclidean acrobatics、How not to quantize、Tying Up Loose Ends 等）译出语气，并在源码中用 `% 原文标题：…` 保留原文，供对照。
5. **页锚点** `% ==== 原文 p.N ====` 只在源码中，不影响排版。
6. **译注**：橙色方框为译者所加，按出现顺序连续编号（译注 1–84）；每条在源码中另有一行 `% [Tutor Note: 类型] 摘要`，便于检索。类型限四类：易错点 / 含糊点 / 物理图像 / 原文疑误。

---

## 4. 图表审计

原 PDF 共 38 页，逐页用 PyMuPDF `get_images` + `get_drawings` + 文本块扫描审计：

- **位图插图 5 张**，全部为**原始嵌入位图的无损导出**（不是屏幕截图、不是重采样），像素尺寸与原始一致；其余 `drawing` 对象均为公式的分数线、上下标、表格框线，不构成图。
- **表格 0 张**；原文无 Table 环境，也无对置表（A/B 对照表）。
- 5 张图按原位置插入，图注全译并标注原文图号与页码：

| 译本图号 | 原图号 | 原文页 | 内容 | 文件 |
|---|---|---|---|---|
| 图 1 | Figure 1 | p.5 | 左：陈–西蒙斯宇宙（电荷与磁通线）；右：一个任意子绕行 | `fig1_cs_universe_anyon.png` |
| 图 2 | Figure 2 | p.10 | 环面上运动的任意子（两生成圈） | `fig2_anyon_torus.png` |
| 图 3 | Figure 3 | p.23 | 左：三叶结的标架（正交向量场）；右：标架变换 = 相对扭转 | `fig3_trefoil_framing.png` |
| 图 4 | Figure 4 | p.24 | 左：含威尔逊圈的 3-流形沿 $\Sigma$ 切开；右：领状邻域与标记点 | `fig4_wilson_loop.png` |
| 图 5 | Figure 5 | p.31 | 沿 $S^2$ 拆解 $M=M_1\#M_2$，用 $S^3$ 的帽子补圆 | `fig5_surgery.png` |

图 4 图注中原文的共轭表示经回图核实为 $\bar R$（R 上加横线），不是 $R^*$。

---

## 5. 译注统计

| 类型 | 条数 | 作用 |
|---|---|---|
| 易错点 | 37 | 指标升降、ε 约定、号差、因子 2、$i$ 因子、归一化、复坐标约定；每条点名"哪一步的哪个符号靠什么约定" |
| 含糊点 | 26 | 作者写 "it can be shown" / "a miracle" / 只引不证之处；每条补出定理名 + 一句话逻辑 + 文献编号 |
| 原文疑误 | 14 | 逐条给出与同段另一式/文献/量纲的矛盾，正文照录，不静默修正（清单见 `审校报告.md`） |
| 物理图像 | 7 | 一句话直觉（电荷自带磁通 → 绕行即 AB 相位；作用量不含度规 → $T^{\mu\nu}=0$ 等） |
| **合计** | **84** | 另有 5 组「本节重点」（每章开头）不计入译注编号 |

---

## 6. 原文疑误清单（正文照录，另加批注）

| # | 位置 | 问题 | 性质 |
|---|---|---|---|
| 1 | p.2 | 把 Khovanov 同调归入 Witten 1989 工作的"直接"实现 | 史实不准确（物理实现晚于 1989） |
| 2 | p.3 | "Starting with §3, however, however, …" 连写两个 however | 排印重复 |
| 3 | p.5 | 式 (2.8) 首行 $A'(x)$ 漏下标 $i$（同式左端为 $A_i$） | 笔误 |
| 4 | p.5 | "Aharanov–Bohm" 拼写 | 笔误（应为 Aharonov） |
| 5 | p.8 | "anyonic phass" | 笔误（phase） |
| 6 | p.12 | 式 (2.30) 末项系数 $k/2\pi$：按 $F\wedge F=\frac14\varepsilon F F$ 与 $\widetilde F=\frac12\varepsilon F$ 应为 $k/8\pi$，**大 4 倍** | 实质错误 |
| 7 | p.14 | 式 (3.3) 第二行恰为第一行的 2 倍（$\int A\wedge\dd A=\frac12\int\varepsilon A(\partial A-\partial A)$，$\int A^3=\frac12\int\varepsilon A[A,A]$），且与 (3.4) 的 $\frac13$ 矛盾 | 实质错误 |
| 8 | p.15 | "This forces $2\pi k w(g)$ to be an integer"：单值性只要求 $e^{2\pi ikw}=1$，即 $kw\in\Z$ | 表述错误 |
| 9 | p.19 | (3.19)(3.20) 指数上漏 $\frac12$：由 $\frac12\langle H,L_-H\rangle$ 应为 $e^{i\lambda h^2/2}$；补 $\frac12$ 后 (3.20) 右端的 $|\lambda|^{-1/2}$ 才精确 | 实质错误 |
| 10 | p.20 | "$\eta_g=\eta_g$" 同一符号自等，疑漏"平凡联络处"标记 | 笔误 |
| 11 | p.25 | "follow the the 'quantize, then constrain' procedure" 连写两个 the | 排印重复 |
| 12 | p.30 | 由毛球定理推出"$P^1$ 上没有平坦联络、模空间为空"：毛球定理只关乎切丛截面；$S^2$ 单连通，平凡丛的平坦联络模空间是**单点**（$A=0$ 的规范类）而非空集。结论（亏格零 1 维）不变 | 论证错误 |
| 13 | p.30 | 末句 "$R_2\neq R_1$" 与同段 "$R_2=\bar R_1$ 时一维" 矛盾 | 笔误 |
| 14 | p.4 | 式 (2.5) 的 $E_i=-\partial_iA_0-\partial_0A_i$ 与 (2.6) 的 $J^i=\frac{k}{2\pi}\varepsilon^{ij}E_j$ 仅在 $A_0=0$（原文随后一直采用的规范）时自洽；由 (2.4) 直接算得 $J^i=\frac{k}{2\pi}\varepsilon^{ij}(E_j+2\partial_jA_0)$ | 定义/规范不自洽（在所用规范下无碍） |

另有 4 处**经回图复核确认"不是笔误"**、故未加"原文疑误"批注者：

- (3.26) 中段是**波浪箭头** $\leadsto$（"replace … with …"），不是除号；文本提取的 "/" 是提取伪影。相位取 $+$，与 (3.27) 自洽。
- (3.32) $Z=\sqrt{2/(k+2)}\sin\frac{\pi}{k+2}$ 与标准结果一致；$c_2(\mathrm{SU}(2))=4$ 即 $2h^\vee$，给出 $k+2$，无误。
- (3.28) $d=24$（$\mathrm{SU}(5)$）时 $e^{2\pi is}=1$，标架依赖消失，无误。
- p.11 文本提取的 "correponding" 经回图确认为 "corresponding"，非笔误。

这 4 条连同具体证据写在 `审校报告.md` 第三节——**审校不是只挑错，也确实为作者澄清了三处"看似有错"**。

---

## 7. 读者须知：本文的 5 个记号陷阱

1. **号差切换**：§2 用 Lorentz 号差（mostly minus），§3 起改欧氏号差。CS 作用量在欧氏号差下变纯虚，`e^{-S^E}=e^{iS}` 才是纯相位，能级量子化论证依赖这一点。
2. **$\varepsilon$ 的约定链**：$\varepsilon^{012}=+1$ 由 (2.6) 的 $\rho=\frac{k}{2\pi}B$ 固定；换成 $\varepsilon_{012}=+1$ 会让 (2.6) 整体变号。凡遇 $\varepsilon$，先固定三维与二维各一个分量。
3. **$g$ 的三重身份**：度规 / 群元 / 亏格。
4. **$\eta$ 的定义含 $\frac12$**：本文 $\eta\equiv\frac12\eta_{\mathrm{APS}}$，故相位写成 $e^{i\pi\eta/2}$；与 APS 文献的 $\eta(s)=\sum\sgn\lambda\,|\lambda|^{-s}$ 差一个因子 2。照抄文献公式会差一个 $\pi/4$。
5. **$q$ 的两个定义**：$q=e^{2\pi i/k}$（树图/阿贝尔类比）与 $q=e^{2\pi i/(k+N)}$（$\mathrm{SU}(N)$ 精确）。原文先给前者、随即自己更正，译文保留了这个层次。

---

## 8. 校验记录（已实测编译）

**已实测编译**：本机原先没有 TeX 发行版，为出 PDF，我下载并解压了一份便携 **TinyTeX**（TeX Live 2026 内核，XeTeX 3.141592653-2.6-0.999998），从 CTAN 镜像补齐了 ctex / xecjk / zhnumber / fandol / tcolorbox / pgf / caption / cite / enumitem / mathtools 等宏包，然后在 TinyTeX 下用 `xelatex` **连跑两遍**编译本交付源码：

- 编译结果：**43 页**，**0 error**，**0 missing character**，无 undefined reference、无 overfull box；
  仅 9 处 underfull hbox（badness 1442–10000），全部出现在参考文献的英文长行断行处，不影响可读性。
- 用的是交付文件 `CS and Knots.tex` 本身（未改内容、未替换宏包选项），字体为 `fontset=fandol`；故这份 PDF 即该源码的真实排版产物。
- 排版微调：译注方框改为 `breakable` + `fontupper=\small`（避免整框跳页留下大片空白），目录另起一页。这些只影响 preamble，正文、公式编号、图表均未动。

**若教授在本机编译**：装 TeX Live 2022 及以上完整版，`xelatex` 两遍即可；若用精简发行版，缺哪个宏包就 `tlmgr install` 补哪个（清单见上）。附：本机为编译临时安装的 TinyTeX 不在交付目录内，可删。

已完成的静态审计（`tools/qa_all.py`，结果 `RESULT: OK`）：

| 检查项 | 结果 |
|---|---|
| 74 个原文编号公式的 `\tag` 齐全、无重复、无多余 | ✅ 74/74 |
| `\label{eq:X}` 与 `\tag{X}` 一一对应；`\eqref`/`\ref` 全部有目标 | ✅ |
| 32 条 `\bibitem` 与原文 [1]–[32] 顺序、键名完全一致；62 处 `\cite` 全部有对应条目 | ✅ |
| 5 个 `\includegraphics` 文件存在；图号 1–5 与原文一致 | ✅ |
| `\begin`/`\end` 环境配对、花括号平衡、`$` 成对、`\left`/`\right` 配对 | ✅ |
| 5 个 `\section`、14 个 `\subsection`、每节均有「本节重点」 | ✅ |
| 禁用命令（`\newcommand`/`\usepackage`/`\setcounter` 等出现在正文片段） | ✅ 0 处 |
| 非 ASCII 数学字符（⟹、δ、ζ 等文本态符号）残留 | ✅ 已全部改为数学命令 |
| 中文文风病灶（「被……所」「进行……的」「对于……而言」） | ✅ 0 处 |

`tools/` 下脚本说明：

| 脚本 | 用途 |
|---|---|
| `lint.py` | 单片段检查：环境配对、括号、`$`、`\tag` 集合、`\label`、禁用命令、译注计数、文风扫描 |
| `assemble.py` | 从 `main.tex` + `sections/*.tex` 装配单文件 `CS and Knots.tex` |
| `qa_all.py` | 全文审计：74 个 tag、标签/引用、文献、图文件、结构、开关 |
| `make_review_notes.py` | 从源码抽取 `% [Tutor Note: …]` 与 `yizhu` 方框，生成 `REVIEW-NOTES.md` |
| `restore_from_assembled.py` | 从单文件反向拆回 `sections/`（应急） |
| `normalize_groups.py` | 统一群名正体（$\mathrm{SU}(2)$ 等） |

---

## 9. 工作量与协作

原文 38 页由 7 个译校单元并行完成（每人 4–8 页），由 Lead 统一术语（开工前冻结）、统一宏与环境、逐片 `lint` 验收、全文 `qa_all` 审计、统一小标题层级与群名排版、补写跨片引用与译名规范化，并撰写本文件与审校报告。所有片段都在同一份 `SPEC.md`（术语冻结表 + 批注规范 + 已知疑点清单）下工作，故术语、记号、批注体例保持一致。

---

## 10. 阅读建议（给教授）

1. 想快速抓物理：读每节开头的蓝色「本节重点」，以及 7 条「物理图像」译注。
2. 想核对推导：易错点译注覆盖了号差、$\varepsilon$ 符号链、因子 2、$i$ 因子与归一化；`审校报告.md` 第四节把它们按主题排好了。
3. 想追文献：含糊点译注把作者"只引不证"的地方逐条补上定理名与文献（Bott、APS、Atiyah–Bott、Quillen、Borel–Weil–Bott、Verlinde、Segal、Lickorish–Wallace）。
4. 若怀疑某式有误：先看 `审校报告.md` 第二节（13 处已确证笔误）与第三节（4 处澄清），再看该式附近的橙色译注。
