# STYLE_GUIDE —— SY02-41 中译本体例

> 译手必读。与 `work/TASK-translator.md` 一致；冲突时以本文件为准（本文件是交付标准）。

## 1. 文体

- 现代汉语书面语，数学论文体；不用口语、不用「我们觉得」。
- **一句 ≤ 60–70 汉字**。英文长句按分号/从句切成两三句，宁可多断句。
- 连接词按词义分译，不一律译「因此」：

| 原文 | 译 |
|---|---|
| Thus / So | 因此 / 于是 |
| Hence | 从而 |
| Therefore | 所以 |
| It follows that | 由此可得 |
| In particular | 特别地 |
| Conversely | 反之 |
| Indeed | 事实上 |
| Namely | 即 |
| However | 然而 |
| Note that | 注意 |
| Recall that | 回忆 |
| Similarly | 类似地 |
| More precisely | 更确切地说 |
| On the other hand | 另一方面 |
| In other words | 换言之 |
| roughly speaking | 粗略地说 |
| by the way | 顺带一提 |
| strictly speaking | 严格说来 |

- 原文 `i.e.` → 即；`e.g.` → 例如；`cf.` → 参看；`resp.` → 分别；`vs.` → 与（对比）。
- 第一人称复数、`we want to` 等照译「我们」。
- 原文的破折号 `—` 用 `——`；引号用「」。

## 2. 术语

- 一律照 `work/glossary.tsv`（215 条）。**先查表，再动笔**。
- 首现写「中文（English）」，之后只用中文；**人名、定理名、软件名、记号不译**。
- 不译（保留英文原词）：`shtuka`、`leg`、`untilt`、`étale`、`pro-étale`、`adic`、`affinoid`、
  `anima`、`ULA`、`qcqs`、`GAGA`、`Bun_G`、`B^+_dR`、`Hecke`、`Satake`、`Levi`、`Borel`、`Cartan`、
  `Witt`、`Frobenius`、`Huber`、`Berkovich`、`Stein`、`Dieudonné`、`Kottwitz`、`Lubin–Tate`、
  `Banach–Colmez`、`Beilinson–Drinfeld`、`Grassmann`、`Harder–Narasimhan`、`Newton`、`Weil`、`Langlands`。
- 有争议的术语首现加译注标出别名（例：菱形（香蕉空间作「钻石」））。

## 3. 公式

- 行内 `$...$`；行间 `\[...\]`、`align*`、`gather*`、`cases`。
- **公式只信页面图**：文本层的 `⊕` 会变 `M`、`⊔` 变 `a`、`ﬁ` 是连字、上下标会拆行、`˘E` 是 `\breve E`。
- 交换图用 `tikz-cd`；不能确定结构时用文字叙述 + 记疑点，不硬画。
- 括号层级、正体/斜体：算子名用 `\operatorname` 或 `\mathrm`（`\Spec`、`\Bun`、`\Spa`、`\Perf` 已定义）。
- 分数、极限、上下标一律显式写清，不用 `\frac12` 这类易混写法以外的东西；不改原文的记号。

## 4. 编号与结构

- 讲次 = `\section`；小节 = `\subsection`；三级 = `\subsubsection`。
- **编号交给 LaTeX**：`\begin{definition}` … `\end{definition}`，**禁止手写「定义 1.1」**。
- 所有条目（definition/example/theorem/proposition/lemma/corollary/remark/warning/question/conjecture/notation）
  **共用同一个计数器**，故原文每一个编号条目都必须落成环境，**一个不漏、顺序不变**。
- 正文里的交叉引用照抄原文数字（原文「Theorem 2.14」→「定理 2.14」）。

## 5. 页锚

- 每个原文页第一段前写 `\srcpage{N}`（N 用印刷页码，与 PDF 页码相同）。
- 一讲内页锚必须递增、不缺页；交付前数一遍。

## 6. 译注

- `\yizhu{正文}{来源}`，来源带等级：`A（原文 §1.2 p.8）`、`B（nLab "condensed mathematics"）`、
  `I（本库 SY02-26 术语表）`。
- 只写三类：**术语背景**、**原文省略**、**原文笔误**；每条 1–4 句；每讲 ≤ 6 条。
- 不写读后感、不写「笔者认为」、不补证明。

## 7. 标点与空格

- 全角标点（，。；：？！「」（））；公式内半角。
- 中文与拉丁字母/数字之间一个半角空格：「étale 上同调」「$p$ 进」「148 页」。
- 人名复合词内部用 en dash：`Fargues–Fontaine`、`Lubin–Tate`、`Beilinson–Drinfeld`、`Harder–Narasimhan`。
- 不出现中文顿号在数学列表里混淆的情形：列表用「、」，公式间用「，」。

## 8. 交付前自检清单

1. `\srcpage` 数 = 原文页数，递增无缺。
2. 环境配对；`$`/`\[` 配对；无 `\usepackage`。
3. 本节最后编号 = 原文最后编号。
4. 术语与 glossary.tsv 一致；禁用译名 grep = 0（「块」指 shtuka、「钻石」、「完全胚」、「斜置」、「错致层」
   仅允许出现在译注里）。
5. 报告 `reports/chNN.md` 四小节齐全。
