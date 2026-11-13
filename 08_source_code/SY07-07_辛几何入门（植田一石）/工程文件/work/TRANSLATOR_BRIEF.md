# 译者须知（本书统一施工规范）

工程：植田一石《数物系のためのシンプレクティック幾何学入門》（SGC ライブラリ 118，2015）中文译注本。
你只负责 Lead 指定的 chunk 文件；其余一切文件属 Lead，不得改动。

## 1. 底本与页映射

- 原书 PDF：`<本地路径> (SGCライブラリ 118) (植田一石) (z-library.sk  1lib.sk  z-lib.sk).pdf`（217 页）
- **原书页 = PDF 页 − 9**。例：原书 p.113 = PDF 第 122 页。
- 每页扫描图：`work\pages\pNNN.png`（NNN = PDF 页号，三位补零；150 dpi，清晰可读）。
- 每页 OCR 文本：`work\split\pNNN.txt`（首行 `===== BOOK PAGE n (PDF m) =====`）。
  **OCR 只能用来查词、定位段落；公式、上下标、希腊字母、符号一律不可信**（例：`M ：＝包x x`、`e ＝ 土＋E`）。任何公式都必须打开页面图核对。
- 术语冻结表：`work\TERMS.md`（含本册全部译名，**开工先读**；未收录的新术语按同一风格自定，并在报告里登记）。

## 2. 产出文件

1. 译文：`src\chunks\<chunk>.tex`（UTF-8 无 BOM；只写这一个 LaTeX 文件）
2. 施工报告：`work\reports\<chunk>.md`

## 3. LaTeX 体例（严格遵守，便于全册合并编译）

- chunk 文件是 `main.tex` 的一段，**不写 `\documentclass` / `\begin{document}` / `\input{preamble}`**。
- 章标题只在该章第一个 chunk 写一次：`\chapter{中文章名}`；节 `\section{名称}`；小节 `\subsection{名称}`。
  编号由 LaTeX 自动生成，**不要手写章/节号**，但节序必须与原书一致。
- **陈述（定义/定理/命题/引理/推论/例/注意/问题/猜想/反例/记法/假设）全部用环境 + 手工编号**，编号照抄原书：

  ```latex
  \begin{definition}{2.1.3}
  设 $M$ 为……
  \end{definition}
  ```

  可用环境：`definition, theorem, theorem*, lemma, lemma*, proposition, proposition*, corollary,
  corollary*, example, remark, question, problem, conjecture, counterexample, notation,
  assumption, formulaenv, proof`。原文「証明」用 `\begin{proof} … \end{proof}`（无编号）；
  **紧跟陈述之后**的证明版本用带 `*` 的环境（如 `theorem*` / `lemma*` / `proposition*` / `corollary*`）。
  原书编号形如「定義 2.1.1」「命題 3.1.4」「注意 2.2.1」，照抄数字层级。
- 公式：
  - 行内 `$...$`；
  - 不编号的独立公式 `\[ ... \]`；
  - **有编号的独立公式**用
    ```latex
    \begin{equation}
      ...
      \tag{2.1.19}
    \end{equation}
    ```
    原书公式号形如 (2.1.19)/(2.4.1)/(8.4.33)，**照抄**，不要自己编号。
  - 多行对齐用 `align`（逐行 `\tag{...}` 或 `\notag`），必要时 `aligned` 嵌在 `equation` 里。
  - 原书一个公式号对应一组对齐等式时，用 `\begin{equation}\begin{aligned}...\end{aligned}\tag{...}\end{equation}`。
- 图：本项目已裁好 5 张图，位于 `src\figures\`：`fig2.1.png`、`fig2.2.png`、`fig2.3.png`、`fig2.4.png`、`fig9.1.png`。
  原书该处有图时写：
  ```latex
  \begin{figure}[htbp]
    \centering
    \includegraphics[width=0.5\textwidth]{figures/fig2.1.png}
    \figtitle{2.1}{单振动（原书 p.8）}
  \end{figure}
  ```
  （`\figtitle{号}{说明}` 会排出「図 2.1 说明」的样式；说明里带原书页码。宽度按图的形状在 0.4–0.6 之间微调。
  `fig9.1` 为原书 図9.1「跷跷板原理」。）若某页确有插图但没有对应文件，用一行文字描述该图并加注释
  `% [Tutor Note: 原书此处有插图，本译本未裁入]`。
- 表格用 `booktabs` 的 `\toprule/\midrule/\bottomrule`，标题用 `\tabtitle{号}{说明}`。
- **页码标记**：每翻到新的一页，在该页第一段之前写一行
  `% [原文 p.N]`（N = 原书页号）。同一页内多段不重复标。
- **`\takeaway{...}`**：每节正文先译 1–2 段，然后给一句话要点（≤40 字）。每节一次。
- **`\chapterreview{...}`**：每章最后（该章最后一个 chunk 的末尾）给 3–6 句本章回顾。
- 术语首现括注西文：`辛流形（symplectic manifold）`；之后只用中文。
- 禁用：`\label`、`\ref`、`\cite`、`\newcommand`、`\def`、`\input`、`\include`。交叉引用一律写文字：
  「由 (2.1.19)」「见 3.2 节」「第 6 章」。
- 原书若出现「演習問題」「問」「章末問題」，照原样译出（用 `question` 环境或普通有序列表）。

## 4. 语言规范

- 学术中文，忠实、完整、**不删节不概述**；不添加原书没有的数学内容（补充只能进 `% [Tutor Note: ...]`）。
- 日文「である」体 → 中文陈述体；不用「我们」「让我们」。
- **禁用病灶句式**：「被……所……」「进行……的……」「对于……而言」「作为……的存在」。
- 长句按中文语序重组，但逻辑关系（因为/于是/反之/注意）必须与原书一致。
- 人名、定理名保留原文（Hamilton、Darboux、Noether…）；术语按 `work\TERMS.md`。
- 数字、单位、符号不译；`\R \C \Z \Q \N \HH \RP \CP \PP \GL \SL \Sp \SU \SO \U \OO \Lie \ad \Ric \grad \divergence \curl \rot` 等宏已在 preamble 定义，优先使用（`\R^n`、`\C^2/\!/K` 之类照原书记法）。

## 5. 数学核对纪律（最重要）

1. 逐页看 `pNNN.png` 原文，逐段翻译；先读整页再动笔，不要按 OCR 拼句子。
2. **每个公式回页面图核对**：系数、上下标、正负号、括号、`\,\mathrm{d}` 与 `d`、希腊字母、`\partial` 与 `d`、
   `\wedge` 与 `\cdot`、`:=` 与 `=`。原书用 `\mathbb{R}`、`\mathbb{C}` 等。
3. 原书疑似笔误（符号错、编号重复、缺字）：**照原样译，不改**，用注释说明：
   `% [Tutor Note: 原书 (3.2.5) 右端疑脱因子 2，此处照录。]`
4. 遇到看不清的字/符号：放大页面图再认，仍不确定就在报告里列出「待核」条目，不要猜。

## 6. 批注（`% [Tutor Note: ...]`）

只允许三类：
- **背景**：人名、历史、术语来源、与物理的对应（如「Hamilton 作用」为何叫作用）。
- **难点**：推导跳步处一句话说明为何成立（如「此处用了闭形式的 Poincaré 引理」）。
- **校勘**：原书疑似笔误/排版问题及依据。

要求：每条 ≤120 字；每 chunk 至少 6 条、平均每页不超过 2 条；正文中不出现批注标记（只在源码注释里）。
同时把批注清单抄进报告（表格：原书页 / 类型 / 内容）。

## 7. 编译自检

在本工程根目录运行（PowerShell）：

```
powershell -ExecutionPolicy Bypass -File build.ps1 -Chunk <chunk>
```

判据：`file:line=0  fatal=0  undefined=0  missingchar=0`，`overfull` 尽量 0。
草稿 PDF 输出为根目录 `tmp_<chunk>.pdf`（可自行查看排版）。
若 preamble 缺宏：**不要改 preamble**，改用已有宏或标准 LaTeX 写法，并在报告「需要的宏」里列出，由 Lead 统一补。
若某 chunk 里 `\chapter` 的编号因缺前章而显示为 1，属正常（草稿模式），不必处理。

## 8. 进度与汇报

- 建议每译完 1–2 节就编译一次，早发现 LaTeX 错误。
- 全部完成、编译干净后：写 `work\reports\<chunk>.md`，并向 Lead 发一条简短消息：
  chunk 名、页范围、文件大小、编译判据、批注条数、遗留问题。
- 报告模板：

```markdown
# <chunk> 施工报告
- 负责页段：PDF 15–30（原书 p.6–21）
- 文件：src\chunks\ch02a.tex（xx KB，xxx 行）
- 节：2.1 Newton 运动定律 / 2.2 Lagrange 形式 …
- 编译：file:line=0 fatal=0 undefined=0 missingchar=0 overfull=0
- 批注：共 N 条（背景 a / 难点 b / 校勘 c）
- 新增术语：日文=中文（…）
- 疑似原书笔误：…
- 待核/未解：…
- 需要的宏：…
```

## 9. 章名与节名统一译法（必须照用）

| 原书 | 中译 |
|---|---|
| 第1章 序章 | 第1章 序章：1.1 几何学与物理学 / 1.2 群作用 / 1.3 可积系统 / 1.4 动力系统 / 1.5 量子化 |
| 第2章 解析力学 | 第2章 分析力学：2.1 Newton 运动定律 / 2.2 Lagrange 形式 / 2.3 Legendre 变换 / 2.4 Legendre–Fenchel 变换 / 2.5 Hamilton 形式 / 2.6 相对论性点粒子 / 2.7 Poisson 定理 / 2.8 Poisson 流形 / 2.9 Noether 定理 / 2.10 叶状结构 / 2.11 辛流形 / 2.12 探测器的轨道 |
| 第3章 G 構造の幾何学 | 第3章 G 结构的几何学：3.1 辛向量空间 / 3.2 Darboux 定理 / 3.3 复流形 / 3.4 驯顺性与相容性 / 3.5 Kähler 流形 / 3.6 辛映射与 Poisson 映射 / 3.7 Lagrange 子流形 |
| 第4章 いろいろなシンプレクティック多様体 | 第4章 各种辛流形：4.1 余切丛 / 4.2 Stein 流形 / 4.3 射影簇 / 4.4 余伴随轨道 / 4.5 Liouville 区域 / 4.6 接触流形 |
| 第5章 運動量写像とシンプレクティック商 | 第5章 动量映射与辛商：5.1 Hamilton 作用 / 5.2 辛商 |
| 第6章 完全可積分系 | 第6章 完全可积系统：6.1 Liouville–Arnold 定理 / 6.2 Lie 群的分解（6.2.1 Cartan 分解 / 6.2.2 Iwasawa 分解 / 6.2.3 Bruhat 分解）/ 6.3 Toda 格子 / 6.4 R 矩阵与经典 Yang–Baxter 方程 / 6.5 AKS 定理 / 6.6 因子化定理 / 6.7 Toda 格子再论 |
| 第7章 Hamilton 力学系 | 第7章 Hamilton 动力系统：7.1 动力系统 / 7.2 近可积系统与摄动理论 / 7.3 KAM 定理 / 7.4 Liouville 定理 / 7.5 Poincaré 回复定理 / 7.6 遍历定理 |
| 第8章 トーリック多様体 | 第8章 环面流形：8.1 辛环面流形 / 8.2 作为代数簇的环面簇 / 8.3 反射多面体与 Fano 多面体 / 8.4 具体例（8.4.1 射影直线 / 8.4.2 射影平面 / 8.4.3 Atiyah flop） |
| 第9章 2次元のゲージ理論 | 第9章 二维规范理论：9.1 二维的乐园 / 9.2 向量丛的联络 / 9.3 Yang–Mills 联络 / 9.4 二维流形上的拓扑向量丛 / 9.5 作为动量映射的曲率 / 9.6 全纯向量丛 / 9.7 标准联络 / 9.8 复规范变换群 / 9.9 梯度与稳定性 / 9.10 Narasimhan–Seshadri 定理 / 9.11 Sobolev 空间 / 9.12 Harder–Narasimhan 滤过 / 9.13 常中心曲率 Hermite 度量的唯一性 / 9.14 Hermite 矩阵的范数 / 9.15 从稳定性到常中心曲率联络 / 9.16 从直和不可分解的常中心曲率联络到稳定性 |
| 第10章 正則シンプレクティック多様体 | 第10章 全纯辛流形：10.1 不可约全纯辛流形 / 10.2 四元数 / 10.3 超 Kähler 流形 / 10.4 超 Kähler 商 / 10.5 全纯辛向量空间 / 10.6 超环面流形 / 10.7 临界流形 |
| あとがき | 后记 |
| 参考文献 / 索引 | 参考文献 / 索引 |

> 注：preamble 的 `\ctexset` 已把章标题排成「第 N 章」。`\chapter{...}` 里只写章名本身（如 `\chapter{分析力学}`）。

## 10. 边界规则

- 你的页范围起点若在一节中间：直接从该页第一行接着译，**不要**重写该节标题，也不要重复上一 chunk 已译的内容。
- 你的页范围终点若在一节中间：译到该页最后一行即可（下一 chunk 接着译）；此时**不写** `\chapterreview`。
- 只有 Lead 明确说「你是该章最后一 chunk」时才写 `\chapterreview`。若不确定，在报告里注明，由 Lead 决定。
