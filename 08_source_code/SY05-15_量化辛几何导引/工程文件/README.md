# 《量化辛几何导引》中文译注版

**原著**：张俊、祝安铜《量化辛几何导引》（*Introduction to Quantitative Symplectic Geometry*），中国科学技术大学出版社，2025 年 6 月第 1 版，ISBN 978-7-312-06282-7。

**底本**：出版社英文版扫描件（363 页，纯图像、无文字层）。正文印刷页 1–334 对应扫描 PDF 第 9–342 页。

**成品**：结构化中文 LaTeX 源码 + 从原扫描件裁剪的全部插图 + 学术批注 + 已编译 PDF（317 页）。

| 指标 | 数值 |
|---|---|
| 译注版页数 | 317 页（A4，ctexbook，XeLaTeX） |
| 正文章节 | 10 章、59 节 |
| 插图 | 131 张 300 dpi 裁剪图（131 处 figure 环境，124 幅原书编号图） |
| 定理/定义/例/注等环境 | 652 个（编号逐条照原文） |
| 编号公式 | 351 条（`\tag` 逐条照原文，无重号/跳号） |
| 学术批注 | 426 条 `% [Tutor Note: …]` |
| 参考文献 | 248 条（保留英文原文） |
| 索引 | 418 条（中文术语 + 英文 + 原书页码） |

---

## 一、目录结构

```
量化辛几何导引_中文译注版/
├── main.tex                  # 主文件（由 tools/make_main.py 生成，含全部 \input）
├── preamble.tex              # 导言区：宏包、版式、定理环境、记号
├── tex/
│   ├── 00-front.tex          # 扉页、内容简介/CIP、译注版说明、前言、目录
│   ├── ch01-s01.tex …        # 第 1 章
│   ├── …
│   ├── ch10b-s04.tex …       # 第 10 章
│   ├── 90-bib.tex            # 参考文献（248 条，保留英文）
│   └── 91-index.tex          # 索引（418 条）
├── figures/                  # 从原书扫描页 300 dpi 裁剪的插图（fig_pNNN_k.png）
├── tools/                    # make_main.py、build.py、check.py、pageimg.py、stats.py
├── 审校记录/
│   ├── review_原文疑误_汇总.md   # 全书原文疑误与记号问题（按章汇总）
│   ├── review_ch01.md … review_ch10b.md
│   ├── review_编译与检查.md      # 编译日志、覆盖统计、已知限制
│   └── QA_report.md             # 独立 QA 核查报告
├── 量化辛几何导引_中文译注版.pdf
└── README.md
```

## 二、编译

需要 **XeLaTeX**（中文用 `ctexbook` + Fandol 字体；pdfLaTeX 不适用）：

```bash
xelatex main.tex
xelatex main.tex
```

或：

```bash
python tools/build.py
```

本工程已在本地 TeX Live 2026 下实际编译通过：**317 页，0 error，0 Missing character，0 未定义引用**；overfull hbox 4 处、underfull 36 处（均为长 URL/中英混排所致的轻微警告，不影响阅读）。

## 三、体例约定（便于后续修改）

| 原文 | 源码写法 | 排版效果 |
|---|---|---|
| `Chapter 1 Symplectic Manifold` | `\chapter{辛流形（Symplectic Manifold）}` | 第 1 章 |
| `1.1 Symplectic Structure` | `\section{辛结构（Symplectic Structure）}` | 1.1 |
| `Definition 1.1.1` | `\begin{wdefn}{1.1.1} … \end{wdefn}` | 「定义 1.1.1」，编号与原书一致 |
| `Example 1.5.1` | `\begin{wexam}{1.5.1} … \hfill$//$ \end{wexam}` | 「例 1.5.1」，以原书记号 `//` 收尾 |
| `Exercise 1.1.13` | `\begin{wexer}{1.1.13} …` | 「练习 1.1.13」 |
| `Equation (1.11)` | `\begin{equation}\tag{1.11} …` | 式 (1.11) |
| `Proof.` | `\begin{wproof} … \end{wproof}` | 「证明」+ 证毕 □ |
| 图 | `\begin{figure}…\includegraphics{figures/fig_pNNN_k.png}…\caption*{图 2.1\quad …（原书 p.22, Figure 2.1）}` | 中文图注 + 原文页码 |
| 每节提要 | `\begin{keytakeaways}…\end{keytakeaways}` | 「本节重点（Key Takeaways）」框 |
| 批注 | `% [Tutor Note: …]` | LaTeX 注释，不进入排版 |

编号全部**手工传入**，与原文严格一致，因此原文中「由定理 5.4.1」「见式 (4.19)」这类交叉引用无需改动即可对上。
插图文件命名 `fig_pNNN_k.png`：`NNN` 为扫描 PDF 页码，`k` 为该页自上而下第 k 张图。

## 四、批注系统

`% [Tutor Note: …]` 注释分四类：

1. **易错预警**：张量缩并、指标升降、定向与符号约定、Fredholm 指标、分次交换号、Euler–Lagrange 变分的边界项、Koszul 符号、Conley–Zehnder 指标的端点约定等；
2. **含糊点拨**：作者写「显然/易验证/留作练习」处的实质证明与所依赖的定理（如强 Lefschetz 性质、du Bois-Reymond 引理、Cartan 公式、Gromov 紧性、SFT 紧性等）；
3. **原文疑误**：保留原文写法并注明疑点，汇总于 `审校记录/review_原文疑误_汇总.md`（共约 150 条）；
4. **术语/记号依据**：不常见译名或记号首次出现处的说明。

若希望在 PDF 中显示批注，可将 `% [Tutor Note: …]` 批量替换为 `\footnote{…}` 或 `\marginpar{\footnotesize …}`。

## 五、已知情况与限制

- 底本扫描件**缺失原书附录「Exams」**（四次考试，印刷页 335–344，约 10 页），经与目录页码及文献起始页核对确认；本译注版不含该附录，其余正文（第 1–10 章）、参考文献、索引完整。
- 底本 **PDF p353（印刷页 355）为损坏扫描页**（整页二次曝光/重影，页眉与编号不可辨）。该页 18 条文献（原书 [179]–[196]）已按字母序与前后编号夹逼恢复，人名按学界通行拼写排印；建议使用者对照原书复核这 18 条。
- 参考文献条目按学术惯例**保留英文原文**，未作汉译。
- 索引词条后的页码为**原书印刷页码**（便于与英文原书对照），不是本译注版页码；本译注版正文页码见目录。
- 插图由扫描页裁剪，受底本扫描分辨率限制，个别线条图边缘略有噪点；已按 300 dpi 重新渲染。
- 原文两次印出 (9.16)（p.239 末与 p.240）；译文忠实保留：前者 `\tag{9.16}`，后者 `\tag*{(9.16)}`，渲染均为 (9.16)。
