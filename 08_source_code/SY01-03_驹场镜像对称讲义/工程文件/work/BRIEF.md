# BRIEF —— 分工与接续点（Lead 维护；开工前必读）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，保留权利，仅限非商业学术研读，权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

## 项目
把 **Kentaro Hori（堀健太郎）《Komaba Lectures on Mirror Symmetry》**（2016 年 8 月东京大学驹场校区讲义；
PDF 49 页：p.1 标题页、pp.2–49 正文+参考文献）的**正文**译成中文 LaTeX（公式无损、结构化、带学术批注），
由 Lead 合成单文件 PDF。p.49（印刷 p.48）的 12 条参考文献由 Lead 处理，不译。

**页码约定（务必记牢）**：`PDF 页号 = 印刷页码 + 1`。本文件里的页段一律写成
「印刷 pp.A–B（PDF pp.A+1–B+1）」。写 `% [原文 p.N]` 时用**印刷页号**。

## 硬性流程（每位译者）
1. 读 `work/STYLE_GUIDE.md`（全文，必须）→ `work/glossary.tsv` → 本 BRIEF 中你的一段 → `work/TIMELINE.md`。
2. 读你的 `work/split/pNNN.txt`（NNN = **PDF** 页号）把握论证结构与段落（**文字层只用来定位**）。
3. **逐页看 `work/pages/pNNN.png`**（`read_image`），公式逐符号抄成 LaTeX；
   图像看不清就用 `work/tools/crop.py` 裁局部放大（用法见 STYLE_GUIDE §1）。
4. 写你的 `work/src/chunks/<trNN{a,b,c}>.tex`（UTF-8 无 BOM、LF；a→b→c 顺序拼接）。
   建议每 2–3 页写一个文件，不要等全部读完再写。
5. 逐项过 STYLE_GUIDE §10 自检 → `send_message` 给 lead 回执（格式见 STYLE_GUIDE §11）。

## 绝对路径速查
- 项目根：`<本地路径>`
- 工作区：`...\work`（pages/ split/ figures/ tags.txt tags_bypage.txt glossary.tsv STYLE_GUIDE.md BRIEF.md TIMELINE.md tools/）
- 输出：`...\work\src\chunks\`
- 原 PDF：`<本地路径>).pdf`
- Python（裁剪脚本用）：`<本地路径>`
- **不要编译**（Lead 统一编译）；不要改 preamble.tex / main.tex / STYLE_GUIDE / 别人的 chunks。

## 七块分工（tag 区间必须首尾接上邻居；每块 tag 数已核对，合计 139）

| 块 | 负责人 | 印刷页 (PDF 页) | 内容 | tag 区间 | 输出文件 |
|---|---|---|---|---|---|
| L | **lead** | 0–8（1–9）+ p9 上半（p10 上半） | 标题页/摘要/译者说明 + §1 引言 + §2 二维 (2,2) 超对称量子场论（2.1–2.7 全部，含 2 张图的正文叙述） | 2.1–2.19 | c00.tex, c01a/b/c |
| 1 | **tr-01** | 9–16（10–17） | §3 T-对偶 全部：3.1 T-对偶（含 D-膜上的 T-对偶、阿贝尔对偶、推广）、3.2 T-对偶即镜像对称、3.3 一个谜题与解答；**Figure 1、Figure 2** | 3.1–3.23 | tr01a/b/c |
| 2 | **tr-02** | 17–22（18–23） | §4 规范线性 sigma 模型 标题 + 4.1 数据、4.2 拉氏量、4.3 相（含 Calabi–Yau 情形 / 非 Calabi–Yau 情形） | 4.1–4.20 | tr02a/b/c |
| 3 | **tr-03** | 23–29（24–30） | 4.4 例子（前半）：CP^{N−1} 模型、T^{(1)}_{N,d} 模型、T^{(1)}_{N,d}(0) 模型、H_n 模型开头（到 (4.34)）；**Figure 3** | 4.21–4.34 | tr03a/b/c |
| 4 | **tr-04** | 30–36（31–37） | 4.4 例子（后半）：H_n 的 n=0,1 / n=2 / n≥3 各情形 + 4.5 矩多面体与环面簇（到 (4.54)）；**Figure 4、Figure 5、Figure 6、Figure 7、Figure 8** | 4.35–4.54 | tr04a/b/c |
| 5 | **tr-05** | 37–43（38–44） | §4 结尾（4.55–4.56）+ §5 镜像对称 标题 + 5.1 荷电场的 T-对偶、5.2 超势的产生（Step 1–4，含 (5.27)）、5.3 标题 | 4.55–4.56, 5.1–5.27 | tr05a/b/c |
| 6 | **tr-06** | 44–47（45–48） | 5.3 推导一（无超势理论）续完 + 5.4 推导二（有超势理论）+ 5.5 例子（CP^{N−1} 模型 / H_n 模型 / T^{(1)}_{N,d} 模型） | 5.28–5.41 | tr06a/b |

## 标题归属表（**只写自己名下的标题**；写错会令全书编号错位）
| 标题 | 由谁写 |
|---|---|
| `\section{引言}` | lead |
| `\section{二维 $(2,2)$ 超对称量子场论}` | lead |
| `\subsection{二维 $(2,2)$ 超对称}`（2.1） | lead |
| `\subsection{A 与 B}`（2.2） | lead |
| `\subsection{重整化群流}`（2.3） | lead |
| `\subsection{形变}`（2.4） | lead |
| `\subsection{拓扑扭转}`（2.5） | lead |
| `\subsection{例子}`（2.6） | lead |
| `\subsection{镜像对称}`（2.7） | lead |
| `\section{T-对偶}` | tr-01 |
| `\subsection{T-对偶}`（3.1） | tr-01 |
| `\subsection{T-对偶即镜像对称}`（3.2） | tr-01 |
| `\subsection{一个谜题与一个解答}`（3.3） | tr-01 |
| `\section{规范线性 sigma 模型}` | tr-02 |
| `\subsection{数据}`（4.1） | tr-02 |
| `\subsection{拉氏量}`（4.2） | tr-02 |
| `\subsection{相}`（4.3） | tr-02 |
| `\subsection{例子}`（4.4） | tr-03 |
| `\subsection{矩多面体与环面簇}`（4.5） | tr-04 |
| `\section{镜像对称}` | tr-05 |
| `\subsection{荷电场的 T-对偶}`（5.1） | tr-05 |
| `\subsection{超势的产生}`（5.2） | tr-05 |
| `\subsection{镜像对称的推导一——无超势的理论}`（5.3） | tr-05 |
| `\subsection{镜像对称的推导二——有超势的理论}`（5.4） | tr-06 |
| `\subsection{例子}`（5.5） | tr-06 |

> 原文的**行内小标题**（不是编号小节）一律用 `\para{…}`，**不是** `\subsection`。清单如下：
> lead：`2.6` 内的 "Non-linear sigma model"（非线性 sigma 模型）、"Landau-Ginzburg model"（Landau–Ginzburg 模型）；
> tr-01：3.1 内的 "T-duality on D-branes"、"Abelian Duality"、"Generalizations"；
> tr-02：4.3 内的 "Calabi-Yau case"、"Non Calabi-Yau case"；
> tr-03：4.4 内的 "The CP^{N−1} Model"、"The Model T^{(1)}_{N,d}"、"The Model T^{(1)}_{N,d}(0)"、"The Model H_n"；
> tr-04：4.4 内的 "n = 0,1"、"n = 2"、"n ≥ 3"（原文即写作 "n = 2" 等，作成 \para）；
> tr-05：5.2 内的 "Step 1 — Reduction to the CP^0 model"、"Step 2 — Exclusion of other corrections"、
> "Step 3 — Instanton calculus"、"Step 4 — Coefficient"；
> tr-06：5.5 内的 "The CP^{N−1} Model"、"The Model H_n"、"The Model T^{(1)}_{N,d}"。

## 图归属（**只写自己名下的图**；图已在 `work/figures/`）
| 图 | 位置（印刷页） | 归属 | 图注（要译） |
|---|---|---|---|
| fig1 | p.15（PDF 16） | tr-01 | CP$^1$ 作为线段上的圆纤维化。 |
| fig2 | p.16（PDF 17） | tr-01 | 纤维化的朴素 T-对偶。 |
| fig3 | p.29（PDF 30） | tr-03 | $\mathrm{H}_n$ 的各相（$n=3$）。 |
| fig4 | p.31（PDF 32） | tr-04 | $\mathrm{H}_0$（左）与 $\mathrm{H}_1$（右）的 RG 流。 |
| fig5 | p.32（PDF 33） | tr-04 | $\mathrm{H}_2$（左）与 $\mathrm{H}_3$（右）的 RG 流。 |
| fig6 | p.34（PDF 35） | tr-04 | $\CP^1$（左）与 $\CP^2$（右）的矩多面体。 |
| fig7 | p.35（PDF 36） | tr-04 | $\C^2/\Z_d$（左）与 $\mathrm{tot}[\cO(-d)\to\CP^1]$（右）的矩多面体。 |
| fig8 | p.35（PDF 36） | tr-04 | $\WP^2_{1,1,n}$（左）与 $\mathrm{F}_n$（右）的矩多面体。 |

## 边界接续（Lead 已裁决，详见 TIMELINE.md）
1. **lead → tr-01**：§2.7 的最后两句在 PDF p.10 顶部（印刷 p.9 顶），由 **lead** 读完
   （"...other well known examples are mirror symmetry between the sigma model with a non-Calabi-Yau target
   and the Landau-Ginzburg model, and the one between Landau-Ginzburg orbifolds. Some of the consequences
   in these examples are mathematically proven."）。**tr-01 从 `\section{T-对偶}` 开始**（同页稍后）。
2. **tr-01 → tr-02**：tr-01 结束于 PDF p.17 末句 "...gauged linear sigma models to which we turn next."
   tr-02 从 PDF p.18 顶 `\section{规范线性 sigma 模型}` 开始。
3. **tr-02 → tr-03**：tr-02 结束于 PDF p.23 末段（"...the moduli space of complex structures of the Higgs
   branch, respectively." + (4.20)）。tr-03 从 PDF p.24 顶的 `\para{非 Calabi–Yau 情形}` 开始。
4. **tr-03 → tr-04**：tr-03 结束于 PDF p.30 的 (4.34)。tr-04 从 PDF p.31 顶
   "The space of FI parameter $\R^2=\{(\zeta_1,\zeta_2)\}$ is separated into three phases..." 开始。
5. **tr-04 → tr-05**：tr-04 结束于 PDF p.37 末的 (4.54) 公式。tr-05 从 PDF p.38 顶
   "This means that $v_i$ is an inward normal to the polytope..." 开始（新段落，干净接缝）。
6. **tr-05 → tr-06**：tr-05 结束于 PDF p.44 的公式 (5.27)（含 §5.3 标题）。tr-06 从 PDF p.45 顶
   "which defines an algebraic torus $T^{N-k}_{Q,t}\subset(\C^\times)^N$ isomorphically..." 开始
   （这是 (5.27) 后的续写分句，直接接着译）。
7. **公式编号连续性**：每块 tag 区间首尾相接（见上表）；块内无编号公式照原文排成 `\[…\]`，不得加编号。
8. 块起始页可能从一句/一个公式中段开始：**直接续写**，不重写、不删除上文。
9. **图的位置**：放在原文对应段落的自然位置（`\begin{figure}[htbp]`），并在正文里写"如图 N 所示"。

## 常见误判提醒
1. 文字层里 `\int`、`\prod`、`\sum`、希腊字母、上下标几乎必然错；`\widetilde{X}`→`eX`、`\tilde\phi`→`eφ`、
   `\widetilde W`→`fW`、`\bar\psi`→空白。**只信图像**。
2. 原文大量公式**没有编号**；`tags_bypage.txt` 里同一 tag 在一页出现两次的多是行文引用，不是新公式
   （已知：2.15@p13、4.35@p32、5.22@p44、5.31@p46）。
3. 原文的 "Figure x"、"Step 1–4"、"n = 2" 编号/标记是手工的，照抄。
4. 本讲义是**不完整版**：5.5 开头 "The CP^{N−1} Model" 小标题后没有内容（原文如此），照排 + 批注说明。
5. 原文笔误不少（如 "empolyed"、"negtative"、"ture"、"defomation"、"choise"、"Furtheremore"、
   "constanits"、"exn2"/"ex2" 混用、"one pont blow up"），**正文照译不修改**，可在批注指出；
   数学式里的笔误必须先 300+ dpi 裁图复核。
6. 术语统一：先查 `glossary.tsv`；新词自己定译法后回报 Lead，由 Lead 汇总回写。
7. 数学环境里 LaTeX 写法：`\CP^{N-1}`、`\WP^2_{1,1,n}`、`\mathrm{H}_n`、`\cO_{\CP^{N-1}}(-d)`、
   `T^{(1)}_{N,d}`、`\mu_F`、`\mathfrak{t}_F`、`\Lambda_G`、`P_W`、`\mathfrak{g}_{\C}`。

## 回执要报告的东西（缺一不可）
①完成文件与印刷页段 ②tag 区间（起–止）及跳号/存疑 ③原文可疑/笔误（页+式号+判据）
④新增术语（英→中）⑤自检结果（逐项 pass）。发送给 **lead**。
