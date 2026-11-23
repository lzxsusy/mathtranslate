# r-lead —— 摘要/译本说明（s00）、导引（s01）、§4 猜想的陈述（s06）、文献表（s99）

Lead 自译的四块。原文 p.1–p.3、p.28–p.29、p.46。

## 1. 交付

| 文件 | 内容 | 原文页 | 页锚 |
|---|---|---|---|
| `源码/sections/s00-front.tex` | 摘要（据底部题头小字）、译本说明（底本、体例、术语、分工） | 封面/摘要 | 无（前置件） |
| `源码/sections/s01-intro.tex` | Introduction 全译 | p.1–3 | `\srcpage{1}`、`\srcpage{2}`、`\srcpageinl{3}` |
| `源码/sections/s06-statement.tex` | §4 Statement of the conjecture | p.28–29 | `\srcpage{28}`、`\srcpage{29}` |
| `源码/sections/s99-bibliography.tex` | References（32 条，保留英文原貌） | p.46 | 无 |

编译：整书 `main.pdf` 62 页；本块 0 error、0 Overfull。编号实印 `定义 4.1 / 注 4.2 / 猜想 4.3 / 猜想 4.4 / 注 4.5 / 注 4.6`，与原文逐条一致。

## 2. 编号对齐

| 原文 | 译本 | 备注 |
|---|---|---|
| Definition 4.1 (1)(2) | `definition`（两项 enumerate） | 「离散」「尖点」两个定义同段，原文即如此 |
| Remark 4.2 | `remark` | tempered 参数不可 ℓ-进插值 |
| Conjecture 4.3 (rough version) | `conjecture[粗略版本]` | 三条性质 |
| Conjecture 4.4 | `conjecture` | 六条，跨 p.28/p.29 |
| Remark 4.5 | `remark` | 中心连通时内形式=扩充纯内形式 |
| Remark 4.6 | `remark` | 非基本 b 处需 Jacquet 函子 |

## 3. 页界处理

- p.28 的界落在「注 4.5 之前」：`\srcpage{29}` 排在猜想 4.4 (6) 之后、注 4.5 之前
  （该处正是原文翻页点）。
- p.3 的界落在导引末段句中，用 `\srcpageinl{3}`。

## 4. 译注

导引 8 条（Hecke 特征层、完满空间、菱形、untilt、Kottwitz 集、Frobenius 下降、稳定分布、
$B(G)\tilde\to|{\Bun}_{G,\bar{\FF}_q}|$），§4 无新增译注（术语已在导引与 §3 定死）。

来源分布：A 类（原文页、[10]、[27]、[18]、[6]）为主；B 类 2 条（nLab "perfectoid space"、
nLab "diamond (pro-étale)"）；I 类 3 条（SY02-26 与 SY02-19/21/22 的既有裁定）。

## 5. 疑点

- p.28「this should be defined intrinsically via the conjecture 3.21」：**已核**，§3.5 确有
  Conjecture 3.21（`conj:3.21`），非笔误，疑点清单该行改「已解」，相应译注已删。
- p.3 首段「[21]」指 Pappas–Rapoport 而非 Scholze 的 perfectoid 论文，原文页码引用与
  文末文献表一致，无讹误。

## 6. 遗留

- 摘要为原文封面下方的两行题头（"We give a survey of..."），译本按中文摘要体重新分句，
  内容未增减；日期与资助信息在译本说明中给出，未混入摘要正文。
- 文献表按原文顺序 1–32 保留英文，不做中译（学科惯例）；条目内 `&` 已转义。
