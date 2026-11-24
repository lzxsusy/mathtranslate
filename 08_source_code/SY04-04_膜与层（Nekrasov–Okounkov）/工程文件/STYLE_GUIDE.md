# STYLE GUIDE — SY04-04《膜与层》

本书的文体、术语、公式与排版约定。**只写本工程的差异**，通用条款见
`04_playbook/01_数学文献翻译纪律.md` 与 `01_corpus_zh/数语规范/`（数语规范三份：术语与记号、中文语体、对齐卡）。

## 1. 文体

| 项 | 约定 |
| --- | --- |
| 语体 | 学术书面语，直述式；「我们」跟原文 *we*，不改成无人称 |
| 句长 | 长句可拆，但不删原文的逻辑连接词（hence／therefore／in particular 必须译出） |
| 人名 | 一律保留拉丁字母，不音译：Nekrasov、Okounkov、Kontsevich、Maulik、Taubes、Witten、Joyce |
| 数学对象名 | 保留拉丁字母：Calabi–Yau、Gromov–Witten、Donaldson–Thomas、K-theory、M-theory、Taub–NUT、Kaluza–Klein、Serre、Künneth、Morse |
| 中拉之间 | 本稿沿用译者既有排版：汉字与拉丁字母/公式之间留一个半角空格（如「第 7 节」「Calabi–Yau 三重流形」）。**不为此做全局调整** |
| 语料一致性 | 术语取 `work/glossary.tsv` 冻结表；不与旧译逐字对齐，但不得出现一译多名 |

## 2. 术语（冻结表见 `work/glossary.tsv`）

本工程的五个**易错点**，改稿时优先核对：

1. **resolution = 解消**，decomposition = 分解。别把 minimal resolution 写成「最小分解」。
2. **proper = 固有**（首现括注 `proper`）；主流译法「紧合」只在术语卡记录，正文不动。
3. **toric chart = 环面坐标卡**，toric diagram = 环面图。二者不可混。
4. **fixed locus = 不动点轨迹**（不是「不动点」——后者指单个点）。
5. **n-fold = 「n 重流形」**（Calabi–Yau 五重流形、三重流形），不是「n 维流形」。

## 3. 公式

- 显示公式一律 `equation` 环境并带 `\label`；引用用 `\eqref`（95 处，与底本相等）。
- 编号与原书**逐一对齐**：`\begin{equation}` 67 个，与底本一致；不要新增/删除编号公式。
- 交换图用 `tikz-cd`（译者已把底本的 xymatrix 全部改写），箭头标签内的宏必须**加花括号**：
  `"\displaystyle{\pi_{\MM}}"`，不要写 `"\displaystyle{\pi_\MM}"`。
- 数学上下标后紧跟文本字体宏时必须加花括号：`ds_{\textup{TN}}^2`、`\tO_{\MM}`（本项目 158 处已统一）。
- 希腊大写粗体只能用 `\boldsymbol{\Phi}`；`\mathbf{\Phi}` 在 TU 编码下没有字形，会 6 处缺字。
- 图：`figures/fig1…fig5`，正文 6 处 `\includegraphics`（fig1 复用一次），宽度按版面 `0.6–0.9\linewidth`。

## 4. 引用与文献

- 参考文献 39 条，`thebibliography` + `\bibitem`，正文用 `\cite`；键集必须与底本一致（校对时逐键比过）。
- 底本中被 `%` 注释掉的两条引理（`MDT_original.tex` L1528–1531、L1560–1563）**不译、不补**。
- 致谢里保留英文标题 *The index of M-theory*（引号内是报告原标题，不译）。

## 5. 译注

- 底本脚注 9 条照译，不加译者注；本轮校订**没有新增任何译注**（改动理由进 `工程文件/校对报告.md`，不进正文）。
- 若以后加译注：格式 `\footnote{……[来源：A/B/I]}` 或 `[译者按（无外部依据）]`，
  来源等级按《纪律》§2.5；知乎/百科/博客一类黑名单来源一律不用。

## 6. 排版

- `ctex` + `article` 12pt，页边距 2.3/2.5 cm；单栏。
- 节号沿用底本：`\section` → 1 … `\subsection` → 1.1 …；`\subsubsection{\ }` 的空标题会产生
  2.3.4、5.5.7 这类孤立编号，**这是底本自身的样子，不要清理**。
- 未定义引用 / 缺字必须为 0；Overfull 容忍 ≤3pt（当前 2 处：2.28pt、0.50pt，肉眼不可见）。
