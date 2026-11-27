# STYLE_GUIDE —— SY02-48 中译本体例

> 译手必读。与 `work/TASK-translator.md` 一致；冲突时以本文件为准（本文件是交付标准）。

## 1. 文体

- 现代汉语书面语，数学论文体；不用口语、不用「我们觉得」。
- **一句 ≤ 60–70 汉字**。英文长句按分号/从句切成两三句，宁可多断句。
- 本底本是**课堂现场记录**，作者口气随意（「you can yeet $K$ out」「be careful!」）。
  这类口语**照译其义、译成书面语**，但不删、不改写其态度；保留讲稿的现场感。
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
- 原文 `(TODO: …)` 一律照译作「（TODO：……）」，保留在正文，并可在报告 §三 登记。

## 2. 术语

- 一律照 `work/glossary.tsv`（306 条）。**先查表，再动笔**。
- 首现写「中文（English）」，之后只用中文；**人名、定理名、软件名、记号不译**。
- 不译（保留英文原词）：`shtuka`、`Hecke`、`Satake`、`Tannakian`、`Cartier`、`Pontrjagin`、
  `Betti`、`de Rham`、`Langlands`、`Galois`、`Weil`、`Frobenius`、`Koszul`、`TFT`（首现给全称）、
  `Bun_G`、`Gr`、`G^∨`（对偶群）、`étale`、`Levi`、`Borel`、`Cartan`、`Weyl`。
- 物理词按 glossary：topological field theory = 拓扑场论；extended TFT = 扩张拓扑场论；
  electric-magnetic duality = 电磁对偶；defect = 缺陷；defect operator = 缺陷算子；
  local operator = 局部算子；interface = 界面；boundary condition = 边界条件。
- 层论词按本库冻结译名：perverse sheaf = 反常层；Hecke eigensheaf = Hecke 特征层。
- 表外词先查 `01_corpus_zh/数语规范/TERMS.tsv` 与 SY02-41/SY02-26 的 glossary；
  都没有就保留英文，并在报告 §二 登记，**不许自造**。

## 3. 公式

- 行内 `$...$`；行间 `\[...\]`、`align*`、`gather*`、`cases`。
- **公式只信页面图**（`work/pages/pNNN.png`）：文本层里 `⊕` 会变 `M`、`⊔` 变 `a`、
  `ﬁ` 是连字、上下标会拆行、`˘E` 是 `\breve E`、`∨` 常丢失。
- 交换图用 `tikz-cd`；不能确定结构时用文字叙述 + 记疑点，不硬画。
- 算子名用 `\operatorname` 或 `\mathrm`（`\Spec`、`\Bun`、`\Gr`、`\Hck`、`\cO` 已定义）。
- **公式不编号**：`equation` 环境禁用；原文 (9.8) 之类的编号不重现，
  正文回指改写成「前式」「上述同构」。

## 4. 编号与结构

- 讲次 = `\section`（首行已有 `\section[短名]{标题（M 月 D 日）}`，**保留不改**）。
- **编号交给 LaTeX**：`\begin{definition}` … `\end{definition}`，**禁止手写「定义 1.1」**。
- 所有条目（definition/example/theorem/proposition/lemma/corollary/remark/warning/question/
  conjecture/notation/fact/exercise/construction）**共用同一个计数器**，
  故原文每一个编号条目都必须落成环境，**一个不漏、顺序不变**。
- 正文交叉引用：原文「Theorem 2.14」→「定理 2.14」（纯文本数字，**禁 `\ref`**）。
- 环境名与原文类型的对应：Definition→`definition`、Theorem→`theorem`、Proposition→`proposition`、
  Lemma→`lemma`、Corollary→`corollary`、Example→`example`、Remark→`remark`、
  Warning→`warning`、Question→`question`、Conjecture→`conjecture`、Notation→`notation`、
  Fact→`fact`、Exercise→`exercise`、Construction→`construction`、Hope→`hope`。

## 5. 页锚

- 每个原文页第一段前写 `\srcpage{N}`（N 用印刷页码，与 PDF 页码相同）。
- 页界落在句中（上一页的最后一句跨到下一页）时，在该句前用 `\srcpageinl{N}`。
- 一讲内页锚必须递增、不缺页；交付前数一遍（`check_sections.py` 会核）。

## 6. 译注

- `\yizhu{正文}{来源}`，来源带等级：`A（原文 p.12）`、`B（nLab "topological field theory"）`、
  `I（本库 SY02-26 术语表）`。
- 只写三类：**术语背景**、**原文省略**、**原文笔误**；每条 1–4 句；每讲 ≤ 6 条。
- 不写读后感、不写「笔者认为」、不补证明。
- 原文脚注（底本用 `\footnote` 处）照译成 `\footnote`，带编号语义即可。

## 7. 标点与空格

- 全角标点（，。；：？！「」（））；公式内半角。
- 中文与拉丁字母/数字之间一个半角空格：「étale 上同调」「$p$ 进」「89 页」。
- 人名复合词内部用 en dash：`Beilinson–Drinfeld`、`Harder–Narasimhan`、`Lubin–Tate`。
- 列表用「、」，公式之间用「，」。

## 8. 交付前自检清单

1. `\srcpage` 数 = 原文页数，递增无缺。
2. 环境配对；`$`/`\[` 配对；无 `\usepackage`。
3. 本节最后编号 = 原文最后编号；条目数 = `work/条目总表.tsv` 对应行数。
4. 术语与 glossary.tsv 一致；禁用命令 grep = 0。
5. 报告 `reports/chNN.md` 四小节齐全。
