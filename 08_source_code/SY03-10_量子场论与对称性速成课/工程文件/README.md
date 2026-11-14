# 《量子场论与对称性速成课》中文译注版 — 交付说明

**原著**：Si Li（李思），*A Crash Course on QFT and Symmetry*，version 2025.7
（2025 年四川大学几何与拓扑暑期学校"量子场论"迷你课程讲义，103 页）

**母本**：`QFT.pdf`（103 页，含文字层与矢量图；本工程另存有逐页文本与渲染图用于核校）

**成品**：结构化中文 LaTeX 源码 + 裁切图 + 译注 + 审校记录 + **已编译 PDF（108 页）**

---

## 一、目录结构

```
QFT_中文译注版/
├── main.tex                # 主文件（由 tools/build.py 生成，含 14 个 \input）
├── preamble.tex            # 导言区：宏包、版式、结构宏、记号宏、\fint 定义
├── tex/
│   ├── part01.tex          # 前言 + 第 1 章 引言（PDF p.2–6）
│   ├── part02.tex … part13.tex   # 第 2–10 章正文（按 PDF 页序切分，共 12 段）
│   └── part14.tex          # 参考文献 [1]–[41]（PDF p.101–103）
├── figures/                # 从原 PDF 裁切的全部图（87 张，PNG，400 dpi）
├── 审校记录/
│   ├── PROTOCOL.md             # 翻译规范（结构/公式/图表/批注/术语表）
│   ├── review_编译与检查.md      # 编译验证与静态检查报告
│   ├── review_原文疑误.md        # 原文笔误/记号不一致汇总（60 余处）
│   ├── review_术语与体例.md      # 术语一致性、记号约定、批注体例
│   └── review_逐节抽查.md        # 逐章公式抽查记录
├── 工具/                   # build.py / lint.py / coverage.py / recrop.py 等工程脚本
├── QFT_中文译注版.pdf       # 已编译成品（XeLaTeX，108 页）
└── README.md               # 本文件
```

## 二、编译

需要 **XeLaTeX**（因使用 `ctexart` 排中文；pdfLaTeX 不适用）：

```bash
xelatex main.tex     # 第一遍：生成 .aux / .toc
xelatex main.tex     # 第二遍：目录、页码、书签正确
```

本工程在无网络环境下用 **tectonic（XeTeX 引擎，TeX Live 2022 bundle）** 实际编译通过：
`main.log` 无错误、无 overfull/underfull 警告，输出 108 页（见 `审校记录/review_编译与检查.md`）。

依赖宏包：`ctex, amsmath, amssymb, amsthm, mathrsfs, bm, graphicx, geometry,
booktabs, array, multirow, enumitem, xcolor, caption, hyperref, fancyhdr`。
`\fint`（原文"积分号加横杠"的正则化积分记号）因发行版未带 `esint`，已在
`preamble.tex` 中用 `\rule` 叠加实现。

## 三、结构约定（便于后续修改）

| 原文 | 源码写法 | 排版效果 |
|---|---|---|
| `1 Introduction` | `\section{引言（Introduction）}` | 自动编号 1，进入目录 |
| `1.1 Action Principle` | `\subsection{作用量原理（Action Principle）}` | 自动编号 1.1 |
| `Definition 2.1` | `\begin{wdefn}{2.1} … \end{wdefn}` | 段首加粗"定义 2.1"，**编号与原文一致** |
| `Example 5.4` | `\begin{wexam}{5.4} … \end{wexam}` | "例 5.4" |
| `Theorem 10.12` | `\begin{wthm}{10.12} … \end{wthm}` | "定理 10.12" |
| `Proof.` | `\begin{proof} … \end{proof}` | "证明"，末尾 □ |
| 展示公式（原文不编号） | `\[ … \]` | 不编号；原文 `(*)` 用 `\tag*{$*$}` |
| 图 | `\begin{figure}…\includegraphics{fig_pNNN_k.png}…\caption*{…}` | 图题中文 + 原文页码 |
| 表 | `tabular` + `booktabs` 重排（共 5 处） | 表头译中文 |
| 每节提要 | `\begin{keypoints}…\end{keypoints}` | "本节重点（Key Takeaways）"框 |
| 译注 | `% [Tutor Note: …]` | LaTeX 注释，**不进入排版正文** |

约定：`fig_pNNN_k.png` 中 `NNN` 为 **PDF 页号**，`k` 为该页自上而下第 k 张图；
图题末尾同时标注原文页脚页码与 PDF 页号（例如"原文 PDF p.9 示意图，原文无编号"）。
原文两张编号图（Figure 1、Figure 2）在图题中明确标出。

## 四、译注（Tutor Note）系统

全书共 **187 条** `% [Tutor Note: …]`，全部为 LaTeX 注释，紧跟在所批注段落/公式之后，分四类：

1. **易错预警**：指标缩并、分次符号规则（Koszul 符号）、$\eta_{\mu\nu}$ 号差、$\epsilon$ 张量、
   Wick 转动与 $i$ 因子、BV 算子 $\Delta$ 的符号与归一化、OPE 的 $(z-w)^{n+1}$ 约定、
   star product 的 $\hbar\to i\hbar$ 约定等；
2. **含糊点拨**：作者写 "It is obvious that… / left as exercise / One can show…" 处，
   指出被省略的实质论证及其依赖的定理或文献（如 Jacobi 恒等式与 $d_{\mathrm{CE}}^2=0$、
   椭圆正则性、轨道–稳定子定理给出 $1/|\Aut(\Gamma)|$、Poincaré 引理的 Cartan 公式证明等），
   不确定处明确写"建议参阅 XXX"，**不编造**；
3. **原文疑误**：照录原文、不改公式，在批注中说明疑点与可替换写法（汇总见
   `审校记录/review_原文疑误.md`）；
4. **术语/记号依据**：非常见译名首次出现处注明依据，并统一全书记号。

若希望在 PDF 中显示批注：可把 `% [Tutor Note: …]` 批量改为 `\marginpar{\footnotesize …}`
或 `\footnote{}`；当前按"源码注释"交付，以免污染正文版面。

## 五、图表

- 原文全部图（含两张编号图与正文内嵌示意图）共 **87 张**，均由原 PDF 以 400 dpi 裁切，
  非重绘；裁切坐标记录在 `工具/fig_overrides.json` 与 `build/figures_report.json`。
- 图题全部译为中文，并标注原文页码；原文无编号的示意图标注"原文无编号"。
- 原文 5 处表格（含第 6 章变量对照表、第 4 章对照表、第 9 章 TQM vs 手征 QFT 对照表等）
  用 `booktabs` 重排，表头译中文，未作截图。

## 六、质量保证与已知局限

**已完成**

| 项目 | 结果 |
|---|---|
| 逐页覆盖 | PDF p.2–p.103 共 102 页正文全部有对应译文（每页带 `% >>> pNNN` 标记，机器核验 102/102，无缺页） |
| 结构完整性 | 10 个 section、38 个 subsection，与原文目录逐条对应；126 个定理/定义/例环境，编号与原文一致、无重号 |
| 公式体例 | 全部展示公式为 `\[ … \]`（无 `equation`/`\tag`；仅原文唯一 `(*)` 用 `\tag*{$*$}` 保留） |
| 图 | 87 张全部裁切自原 PDF，`\includegraphics` 路径全部有效，编译后浮动体位置经逐页目检 |
| 编译 | tectonic/XeLaTeX 实际编译通过：108 页，0 错误，0 overfull/underfull（见编译报告） |
| 静态检查 | 花括号/环境/`$`/`\left\right` 配平、无 BOM/乱码、无 `???`/`TODO`、图文件存在性：14/14 通过 |
| 审校 | 5 份审校记录：编译、原文疑误、术语体例、逐节抽查；逐式核对 200+ 条展示式 |

**必须说明的局限（学术诚实）**

1. 原文为作者"边讲边写"的速成讲义，本身有大量笔误、记号不一致与省略的证明；
   本译本一律**照录原文 + 批注**，未擅自"修正"（疑误清单见 `review_原文疑误.md`）。
2. 文字由原 PDF 文字层 + 逐页读图核对转写；个别形近符号（如 $v/u$、$\nu$、花体与粗体）
   存在判定风险，均已在该处 `Tutor Note` 中标"请核对原书 p.NN"。
3. 原文的示意图嵌在公式行内（如例 5.2、5.3 的配对图），裁切时只能取图形部分，
   个别图的上下文公式以正文排印为准；不影响数学内容。
4. 编译环境为 tectonic bundle（TeX Live 2022 组件 + Fandol 中文字体）；
   若用本机 TeX Live 2023+ 编译，个别字体/宏包版本差异可能产生轻微排版警告，不影响内容。

## 七、修改指引

- 改译文：直接编辑 `tex/partNN.tex`；不要动 `% >>> pNNN` 标记（覆盖检查用）。
- 改公式：原文公式不编号，直接改 `\[ … \]` 内容；`(*)` 公式请保留 `\tag*{$*$}`。
- 加/换图：图片放 `figures/`，命名 `fig_pNNN_k.png`；改 `工具/fig_overrides.json` 后运行
  `python 工具/recrop.py` 可重新裁切。
- 重排后运行 `python 工具/build.py && xelatex main.tex` 两遍。
- 增删片段后重跑 `工具/build.py`（自动更新 `main.tex` 的 `\input` 列表）。
