# 译手任务书（TASK-translator）—— SY02-29《局部 Langlands 对应的几何化：综述》

你负责**一块**原文的汉译。本文件是硬约束；与它冲突的临时想法一律以它为准。

---

## 0. 底本与位置

- 底本：Laurent Fargues, *Geometrization of the local Langlands correspondence: an overview*, 2016-02-02，46 页。
- 印刷页 = PDF 页（偏移 0）。
- 工程根：`C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-29_局部Langlands几何化综述`
- 逐页文本：`工程文件/work/src/pNNN.txt`（NNN 三位，p001–p046）。
- 页面图像：`工程文件/work/pages/pNNN.png`。**没有就先渲染**：
  ```
  cd "工程根"
  python 工程文件/tools/render_pages.py 16-23 --dpi 150
  ```
  （Windows 下终端若报编码错，前缀 `PYTHONIOENCODING=utf-8`。）
  然后用 read_image 读图像。**凡公式、上下标、交换图、花体、符号，一律以页面图像为准**；文本提取只用来定位段落。

## 1. 产出（三件，缺一不可）

1. `源码/sections/<你被指定的文件>.tex` —— 译文正文（只写正文，不写 documentclass）。
2. `工程文件/reports/r-<tag>.md` —— 施工报告：页范围、原文编号 → 译文编号对齐表、译注清单、疑点处理、遗留。
3. `工程文件/work/trace-<tag>.md` —— 决策流水：每个拿不准的地方记「原文 → 我的处理 → 依据」。

**只**能写这三类文件。不许改 `preamble.tex`、`main.tex`、别人的 sections、`glossary.tsv`、`BRIEF.md`、`SPEC.md`。

## 2. 必读（动笔前）

1. `工程文件/SPEC.md` —— 排版体例（环境、`\srcpage`、公式编号、tikz-cd）。
2. `工程文件/work/glossary.tsv` —— **冻结术语表**，按它译；表里没有的，先按学界惯例译并在报告里列为「新增术语建议」。
3. `工程文件/work/通读笔记.md` —— 全文主旨与论证地图（若已生成）。

## 3. 翻译纪律（违者返工）

- **不臆造**。原文省略、含糊、疑误，照字面译出，把判断写进 trace 与报告；**绝不**替作者补论证、改条件、加限定。
- **不略译**。一段不许并、不许拆；一句话不许丢。作者的行文是综述体（informal），保留其口语与插入语（"we try to convince the reader (and ourselves)"）。
- **数学正确性第一**。公式逐符号对页面图像核；上下标、花体、$B_{\mathrm{dR}}^+$、$\varphi$、$\pi$、$\varpi$ 这些提取易错处尤其要看图像。
- **疑似原文笔误**：译文照原样（可加 `\yizhuw` 说明），并在 trace 与报告里单列，交 Lead 定夺。**不许**悄悄改。
- **术语**：按 glossary；生造中文禁止；拿不准保留英文原词（斜体或正体照原文）。

## 4. 语言

- 中文数学文风，短句，一句 ≤60–70 汉字；一句话说完一层意思。
- 消灭「被……所」「进行……的」「对于……而言」「起到……的作用」这类翻译腔。
- 中英文之间半角空格（ctex 会处理，源码里也要留：`设 $S$ 是完满空间`）。
- 全角中文标点；数学模式内用英文标点。
- 第一人称复数「我们」照译；「作者」用第三人称。
- 专名：Fargues、Scholze、Fontaine、Kottwitz、Rapoport、Zink、Lubin、Tate、Drinfeld、Beauville、Laszlo、Caraiani、Kaletha、Vogan、Scholze 的 diamond 等一律保留拉丁字母。

## 5. 体例要点（SPEC 的浓缩）

```latex
\section{曲线}% 原文 1. The curve
\srcpage{3}

\subsection{adic 曲线}% 原文 1.1. The adic curve

设 $E$ 是局部域，剩余域为 $\FF_q=\oo_E/\pi$。……\srcpage{4}

\begin{definition}\label{def:1.1}
若 $E=\FF_q((\pi))$，令 $Y_S=D_S^*\subset\AA^1_S$。
\end{definition}

\begin{equation}\label{eq:1.1}
\delta(\varphi(y))=\delta(y)^{1/q}.
\end{equation}
```

- 每页正文起点放 `\srcpage{N}`；页界在句中用 `\srcpageinl{N}`。
- 定理环境：`definition` / `proposition` / `lemma` / `corollary` / `theorem` / `remark` / `example` / `conjecture` / `question`；证明用 `\begin{proof}`。
- 定理/公式编号与原文**逐条一致**（原文 Definition 1.1 → 译文 Definition 1.1）。原文编号若与上下文冲突（如 §4 里出现 3.21），照原文排、在报告里记一笔。
- 原文中**加粗的断言**（如导引里斜体的 Hecke 特征层条件）照排：`\emph{…}`。
- 交换图用 `tikz-cd`，对象与箭头照原文；原文图若有文字标签，一并译。
- 译注：`\yizhu{注文}{来源}`，注文 ≤120 字；`\yizhuw{注文}` 用于无外部依据。每块 5–12 条为宜，宁少勿滥；**注要解释为什么**，不要复述译文。

## 6. 自检（交稿前必须做）

```
cd "工程根\源码"
build.bat check sections\<你的文件>.tex <tag>
```
要求 **0 error**。若报缺宏/缺环境，**不要**改 preamble：在报告里说明，Lead 统一加。

另外自查：
- 页锚数 = 你负责的页数（`grep -c srcpage`）。
- 没有 `??`、没有空段落、没有 `\srcpage` 出现在脚注或环境内部。
- 术语抽查：与你 glossary 里的译法一致。

## 7. 报告格式（reports/r-<tag>.md）

```markdown
# r-<tag> —— <块名>（原文 p.X–p.Y）

## 1. 交付
- 文件：sections/xxx.tex（N 行）
- 页锚：p.X–p.Y 共 N 个
- 编译：build.bat check → 0 error

## 2. 编号对齐表
| 原文 | 译文 | 类型 |
|---|---|---|
| Definition 1.1 | definition def:1.1 | 定义 |

## 3. 译注
| # | 位置 | 术语 | 来源 |
|---|---|---|---|

## 4. 疑点
| 位置 | 原文 | 类型 | 处理 | 状态 |

## 5. 新增术语建议
| 原文 | 建议译名 | 依据 |
|---|---|---|
```

## 8. 风格样板（导引首段，Lead 译，照此定调）

原文：*In this article we give an informal exposition of a conjecture linking p-adic Hodge theory, the geometric Langlands program and the local Langlands correspondence.*

译文：本文非形式地阐述一个猜想，它把 p-进 Hodge 理论、几何 Langlands 纲领与局部 Langlands 对应联系起来。

原文：*A more precise but technical article will appear later ([7]).*

译文：更精确、也更技术性的文章将在稍后发表（[7]）。

——短句、直陈、不用「进行了……的讨论」这类空转结构；引用编号保留方括号。
