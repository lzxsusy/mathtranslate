# ERRATA 补登（errata-extra.md）

本文件汇总 `xref.py` 交叉引用审计中查实的**原书笔误**，供 lead 并入 ERRATA.md。三条都已用原书 OCR（`split\pNNN.txt`）与页面裁图核对；按项目惯例**正文照排不改**，此处只作登记。

| 文件 | 原文页 | 原文印 | 应为 | 依据 |
| --- | --- | --- | --- | --- |
| src/b10.tex:321 | p.86 | “By **Corollary 4.8** the theorem is true if our family $\mathfrak F^{(0)}$ contains no singular curves (i.e. $D=\emptyset$).”（译作「由推论 4.8……」） | **Theorem 4.8**（定理 4.8） | (1) p.80 陈述处印 “Theorem 4. 8”，本译本作「定理 4.8」（光滑族上 $\cV_{\vec\lambda}$ 在 $\cB\setminus D$ 局部自由）；(2) 本书每章陈述编号**共用一套计数器**（4.7 命题、4.8 定理、4.9 推论、4.10 推论），全章不存在「推论 4.8」；(3) 上下文「$D=\emptyset$（族不含奇异曲线）」正是定理 4.8 的条件。OCR 证据：`split/p095.txt:49`（原文 p.86），裁图 `tmp/x95b.png`。 |
| src/b10.tex:473 | p.89 | “the theorem is true by **Corollary 4.8**”（译作「由推论 4.8 定理成立」） | **Theorem 4.8**（定理 4.8） | 同上；同一处引用在 p.89 重复出现。OCR 证据：`split/p098.txt:41`。 |
| src/b02.tex:46 | p.18 | “The meaning of the condition (Q) will be clarified in the following **Lemma 1.21 and Lemma 1.22**.”（译作「引理 1.21 与引理 1.22」） | **Theorem 1.22**（定理 1.22）；若作者本意指相继两条，则可能作 Lemma 1.20 与 Lemma 1.21 —— 目标有歧义 | p.20 相继两条印 “Lemma 1. 20”、“Lemma 1. 21”（`split/p029.txt:21,23`），p.21 印 “Theorem 1. 22”（残差配对，`split/p030.txt:10`）；故 1.22 是定理而非引理。原句出处 `split/p027.txt:25`。 |

## 说明

1. 三条的译文都忠实照译了原书，**不属于译手错误**；正文保持原样，由译注/ERRATA 说明。
2. 第 1、2 条是同一处笔误的两个出现点（p.86 证明开头、p.89 归纳回代），建议在 b10 的译注里合并说明一次即可。
3. 第 3 条因「作者原意」不确定（1.22 是残差配对定理，未必就是说明条件 (Q) 的那一条），只登记、不建议改字；若 lead 决定统一处理，建议改为「定理 1.22」并在译注注明原文作 Lemma。
4. 审计脚本 `xref.py` 的未解析清单即由这三条构成（见 `block-reports/xref.md` 第三、八节）。
