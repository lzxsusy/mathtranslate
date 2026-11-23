# 章节结构审计报告（structure-audit）

- 审计对象：`loopbook_toc.txt`（原书 PDF 目录，229 条）与 `tex/chapters/*.tex`（18 个片段 + `glossary.tex`）、`tex/main.tex` 的 `\input` 顺序。
- 审计方法：按 `main.tex` 顺序提取全部 `\chapter` / `\section` / `\subsection`，逐条与目录的章号、节号、英文标题对应关系及次序比对；小节逐条比对标题语义（允许中文措辞不同）。
- **审计快照时间：2026-10-28 16:21**（据文件 mtime；`ch06.tex` 16:21:31 定稿，结构为 4 节 / 11 小节；`ch09-2.tex` 16:21:09 更新后 §9.4–9.6 小节齐全）。本报告按 16:21 的结构状态给出结论。
- 结论速览：**10 个正文章齐全、各出现一次、顺序正确**；章节标题与原书目录一一对应，**无缺失、无多出的节/小节**（41/41 节、164/164 小节、附录 A.1–A.5 齐全）。剩余问题只有**接缝层面**：2 处**文本重复/断句必须修**（ch09-1↔ch09-2、ch05-1↔ch05-2），1 处接缝注释与事实不符（ch03-2，无需删改），以及术语表这一额外章待确认。

---

## 1. 章级核对（`\chapter` 唯一性与顺序）

| # | 原书目录 | 译本（文件:行） | 结论 |
|---|---|---|---|
| Ch.1 | Local Langlands correspondence | 局部 Langlands 对应（ch01-1:7） | ✅ 唯一、序正确 |
| Ch.2 | Vertex algebras | 顶点代数（ch02:18） | ✅ |
| Ch.3 | Constructing central elements | 构造中心元（ch03-1:8） | ✅ |
| Ch.4 | Opers and the center for a general Lie algebra | oper 与一般李代数的中心（ch04:7） | ✅ |
| Ch.5 | Free field realization | 自由场实现（ch05-1:7） | ✅ |
| Ch.6 | Wakimoto modules | Wakimoto 模（ch06:16） | ✅ |
| Ch.7 | Intertwining operators | 交织算子（ch07:7） | ✅ |
| Ch.8 | Identification of the center with functions on opers | 中心与 opers 上函数代数的等同（ch08:10） | ✅ |
| Ch.9 | Structure of ĝ-modules of critical level | 临界水平 ĝ-模的结构（ch09-1:7） | ✅ |
| Ch.10 | Constructing the Langlands correspondence | 构造 Langlands 对应（ch10-1:9） | ✅ |
| App. | Appendix | 李代数与泛包络代数（appendix:7，`\appendix` 后编号为 A） | ✅（标题为译本所拟，原书仅 “Appendix”） |
| — | （无） | 术语表（glossary:2） | ⚠️ **多出的章**：译校增补，不在原书目录；`main.tex` 已置于附录之后、参考文献之前。确认是否有意加入目录 |

- 共 12 个 `\chapter` 命令：10 个正文章 + 附录 + 术语表。**每个正文章恰好出现一次，顺序 1→10 正确**；无重复 `\chapter`。
- `main.tex` 的 `\input` 顺序：ch01-1 → ch01-2 → ch02 → ch03-1 → ch03-2 → ch04 → ch05-1 → ch05-2 → **ch06** → ch07 → ch08 → ch09-1 → ch09-2 → ch10-1 → ch10-2 → ch10-3 → ch10-4 → appendix → glossary → bibliography。✅

## 2. 节级核对（`\section`）

原书共 **10 章 41 个编号节 + 附录 5 节 = 46 节**；译本现有 **41 + 5 = 46 节（41/41，齐）**。下表中“小节（原/译）”列出该节在原书/译本中的小节数。

| 原书节 | 译本标题（文件:行） | 小节（原/译） | 结论 |
|---|---|---|---|
| 1.1 The classical theory | 经典理论（ch01-1:24） | 6/6 | ✅ |
| 1.2 Langlands parameters over the complex field | Langlands 参数（复域）（ch01-2:11） | 6/6 | ✅ |
| 1.3 Representations of loop groups | 圈群的表示（ch01-2:239） | 6/6 | ✅ |
| 2.1 The center | 中心（ch02:48） | 3/3 | ✅ |
| 2.2 Basics of vertex algebras | 顶点代数基础（ch02:390） | 6/6 | ✅ |
| 2.3 Associativity in vertex algebras | 顶点代数中的结合性（ch02:1085） | 4/4 | ✅ |
| 3.1 Segal–Sugawara operators | Segal–Sugawara 算子（ch03-1:28） | 5/5 | ✅ |
| 3.2 Lie algebras associated to vertex algebras | 与顶点代数相联系的李代数（ch03-1:379） | 3/3 | ✅ |
| 3.3 The center of a vertex algebra | 顶点代数的中心（ch03-1:606） | 4/4 | ✅ |
| 3.4 Jet schemes | 射流概形（ch03-2:42） | 3/3 | ✅ |
| 3.5 The center in the case of sl₂ | $\mathfrak{sl}_2$ 情形的中心（ch03-2:229） | 8/8 | ✅ |
| 4.1 Projective connections, revisited | 射影联络再探（ch04:22） | 3/3 | ✅ |
| 4.2 Opers for a general simple Lie algebra | 一般单李代数的 opers（ch04:186） | 5/5 | ✅ |
| 4.3 The center for an arbitrary affine Kac–Moody algebra | 任意仿射 Kac–Moody 代数的中心（ch04:477） | 3/3 | ✅ |
| 5.1 Overview | 概览（ch05-1:18） | 0/0 | ✅ |
| 5.2 Finite-dimensional case | 有限维情形（ch05-1:54） | 5/5 | ✅ |
| 5.3 The case of affine algebras | 仿射代数情形（ch05-1:310） | 3/3 | ✅ |
| 5.4 Vertex algebra interpretation | 顶点代数解释（ch05-2:32） | 3/3 | ✅ |
| 5.5 Computation of the two-cocycle | 二上循环的计算（ch05-2:212） | 5/5 | ✅ |
| 5.6 Comparison of cohomology classes | 上同调类的比较（ch05-2:419） | 5/5 | ✅ |
| 6.1 Wakimoto modules of critical level | 临界水平的 Wakimoto 模（ch06:74） | 2/2 | ✅ |
| 6.2 Deforming to other levels | 形变到其他水平（ch06:388） | 6/6 | ✅ |
| 6.3 Semi-infinite parabolic induction | 半无限抛物诱导（ch06:1063） | 3/3 | ✅ |
| 6.4 Appendix: Proof of the Kac–Kazhdan conjecture | 附录：Kac--Kazhdan 猜想的证明（ch06:1749） | 0/0 | ✅ |
| 7.1 Strategy of the proof | 证明的策略（ch07:22） | 2/2 | ✅ |
| 7.2 The case of sl₂ | $\mathfrak{sl}_2$ 的情形（ch07:186） | 3/3 | ✅ |
| 7.3 Screening operators for an arbitrary g | 任意 $\mathfrak{g}$ 的屏蔽算子（ch07:534） | 5/5 | ✅ |
| 8.1 Description of the center of the vertex algebra | 顶点代数中心的描述（ch08:26） | 5/5 | ✅ |
| 8.2 Identification with the algebra of functions on opers | 与 opers 上函数代数的等同（ch08:402） | 6/6 | ✅ |
| 8.3 The center of the completed universal enveloping algebra | 完备泛包络代数中心的描述（ch08:844） | 3/3 | ✅ |
| 9.1 Opers with regular singularity | 带正则奇点的 opers（ch09-1:24） | 3/3 | ✅ |
| 9.2 Nilpotent opers | 幂零 opers（ch09-1:149） | 5/5 | ✅ |
| 9.3 Miura opers with regular singularities | 带正则奇点的 Miura opers（ch09-1:499） | 3/3 | ✅ |
| 9.4 Categories of representations of ĝ at the critical level | 临界水平 $\gghat$-模的表示范畴（ch09-2:54） | 3/3 | ✅ |
| 9.5 Endomorphisms of the Verma modules | Verma 模的自同态（ch09-2:329） | 3/3 | ✅ |
| 9.6 Endomorphisms of the Weyl modules | Weyl 模的自同态（ch09-2:576） | 6/6 | ✅ |
| 10.1 Opers vs. local systems | Opers 与局部系（ch10-1:54） | 0/0 | ✅ |
| 10.2 Harish–Chandra categories | Harish–Chandra 范畴（ch10-1:173） | 3/3 | ✅ |
| 10.3 The unramified case | 无分歧情形（ch10-2:7） | 8/8 | ✅ |
| 10.4 The tamely ramified case | 温和分歧情形（ch10-3:10） | 6/6 | ✅ |
| 10.5 From local to global Langlands correspondence | 从局部到整体 Langlands 对应（ch10-4:31） | 3/3 | ✅ |
| A.1 Lie algebras | Lie 代数（appendix:9） | — | ✅ |
| A.2 Universal enveloping algebras | 泛包络代数（appendix:45） | — | ✅ |
| A.3 Simple Lie algebras | 单李代数（appendix:142） | — | ✅ |
| A.4 Central extensions | 中心扩张（appendix:222） | — | ✅ |
| A.5 Affine Kac–Moody algebras | 仿射 Kac–Moody 代数（appendix:267） | — | ✅ |

**多出的节**：无（46 个已有节均与目录逐一对应；唯一额外的是术语表这一“章”，不是节）。

## 3. 小节级核对（`\subsection`）

原书共 **164 个小节**；译本现有 **164 个（164/164，齐）**。逐章逐一比对标题语义与次序，结论如下（“✔”表示全部与目录顺序一致、无缺无多）：

| 章 | 原书小节数 | 译本小节数 | 对应情况 |
|---|---|---|---|
| 1 | 18（1.1.1–1.1.6 / 1.2.1–1.2.6 / 1.3.1–1.3.6） | 18 | ✔ 完全对应 |
| 2 | 13（2.1.1–2.1.3 / 2.2.1–2.2.6 / 2.3.1–2.3.4） | 13 | ✔ |
| 3 | 23（3.1.1–3.1.5 / 3.2.1–3.2.3 / 3.3.1–3.3.4 / 3.4.1–3.4.3 / 3.5.1–3.5.8） | 23 | ✔ |
| 4 | 11（4.1.1–4.1.3 / 4.2.1–4.2.5 / 4.3.1–4.3.3） | 11 | ✔ |
| 5 | 21（5.2.1–5.2.5 / 5.3.1–5.3.3 / 5.4.1–5.4.3 / 5.5.1–5.5.5 / 5.6.1–5.6.5） | 21 | ✔ |
| 6 | 11（6.1.1–6.1.2 / 6.2.1–6.2.6 / 6.3.1–6.3.3） | 11 | ✔（6.3.1 Wakimoto 模作为诱导表示、6.3.2 主要结果、6.3.3 一般抛物子代数，顺序一致） |
| 7 | 10（7.1.1–7.1.2 / 7.2.1–7.2.3 / 7.3.1–7.3.5） | 10 | ✔ |
| 8 | 14（8.1.1–8.1.5 / 8.2.1–8.2.6 / 8.3.1–8.3.3） | 14 | ✔ |
| 9 | 23（9.1.1–9.1.3 / 9.2.1–9.2.5 / 9.3.1–9.3.3 / 9.4.1–9.4.3 / 9.5.1–9.5.3 / 9.6.1–9.6.6） | 23 | ✔ |
| 10 | 20（10.2.1–10.2.3 / 10.3.1–10.3.8 / 10.4.1–10.4.6 / 10.5.1–10.5.3） | 20 | ✔ |
| A | 0 | 0 | ✔（附录各节无小节） |

需要 Lead 知晓的“标题对应但原书目录乱码”之处（译本按正文页图像核对后译出，属正常，不是偏差）：
- 2.2.4 “Vertex algebra associated to g0;090d"0362 g_” → 与 $\gghat_\kappa$ 相伴的顶点代数；
- 6.1.2 “Other g0;090d"0362 g-module structures on M_g” → $M_{\mathfrak g}$ 上的其他 $\gghat$-模结构；
- 8.3.1/8.3.2/8.3.3 中的 “Op_L G / Op_G(D)__0” 乱码 → $\operatorname{Fun}\operatorname{Op}_{{}^LG}(D^\times)$、$\operatorname{Fun}\operatorname{Op}_G(D^\times)_{\upsilon_0}$；
- 10.3.2 “unramified categories of g0;090d"0362 g__c-modules” → $\hat{\mathfrak{g}}_{\kappa_c}$-模的无分歧范畴；
- 10.4.2/10.4.3 的 “(g0;090d"0362 g__c,I)” → $(\hat\fg_{\kappa_c},I)$。

## 4. 缺口清单（必须修 / 需确认）

**必须修**
1. **ch09-1 → ch09-2 接缝断句重复**：ch09-1 末句作“这意味着，纤维 $\mu^{-1}(\chi)$ 中”（对应原文 “This implies that the set of points in the fiber μ⁻¹(χ) of the”，止于 p.283 页末），ch09-2 首句作“**由此推出**，Miura 变换 $\mu$ 在 … 的纤维 $\mu^{-1}(\chi)$ 的点集，与 Springer 纤维 … 一一对应”。两段拼合后成为“这意味着，纤维 μ⁻¹(χ) 中由此推出，……”，语法断裂且语义重复。修法（二选一）：
   - 删 ch09-1 末尾半句“这意味着，纤维 $\mu^{-1}(\chi)$ 中”；或
   - 把 ch09-2 首句改为“的点集与 Springer 纤维 $\operatorname{Sp}_{\operatorname{Res}_{\check\lambda}(\chi)}$ 的点集一一对应（见 (9.3-10)）”，去掉“由此推出，Miura 变换 … 的纤维 $\mu^{-1}(\chi)$ 的”这半句。
   注意：ch09-2 开头另有 §9.3 的正当续文（定理 9.3.7、式 (9.3-18)），不在 ch09-1 中，**无重复，保留**。
2. **ch05-1 → ch05-2 的 proof 环境接缝**：按 ch05-2 顶部 `[合并接缝]` 注释执行——删去 ch05-1 末尾的 `\end{proof}` 与 ch05-2 中紧跟注释的 `\begin{proof}[证明（续）]`，保留 ch05-2 段末的 `\end{proof}`。否则出现一个居中 QED 与“证明（续）”标题（能编译，但不合版式）。

**需确认 / 建议（非缺口）**
3. **ch03-2 顶部“接缝说明”与事实不符**：注释称“若 ch03-1.tex 末尾已含同样内容，合成时删去本文件开头一段”。经核对，ch03-1 **不含**式 (3.3-4)、引理 3.3.4 及该段文字（ch03-1 止于 p.94 句末逗号），故该段是全书唯一一份，**不能删**。建议 Lead 把该注释改为“此处为 §3.3.4 唯一结尾，保留”。
4. **术语表（glossary.tex）为额外章**：不在原书目录。若收入目录需确认其名称与位置（现位于附录之后、参考文献之前）。
5. **原书 Index（p.402）无对应译本文件**：现以术语表代替；若计划补索引，应另立 `index.tex`（不属于本次结构缺口）。
6. 附录章标题“李代数与泛包络代数”为译本所拟（原书目录只写 “Appendix”），可接受；A.1–A.5 齐全、顺序一致。

## 5. 跨文件重复与接缝核对（第 3 项要求）

**`\section` / `\subsection` 跨文件重复：无。** 每个节号（1.1–10.5、A.1–A.5）在整个项目中只生成一次；同一中文标题在**不同章**重复属正常（如“定义”“残数”“屏蔽算子”“分次伴随代数”“坐标变换的作用”），因为原书本身在不同章有同名小节（例如 9.1.2 与 9.2.3 都叫 Residue，6.1.1 与 6.2.1 都叫 Homomorphism of vertex algebras）。

各文件边界逐一核对（“接缝”指前一片段止于句中、后一片段先接续文字再出 `\section`）：

| 接缝 | 后一片段开头 | 结论 |
|---|---|---|
| ch01-1 → ch01-2 | 注释说明 p.23 第一句由 U01 补译，ch01-2 从第二句起 | ✅ 无重复（注释明确） |
| ch02 | 单文件 | ✅ |
| ch03-1 → ch03-2 | §3.3.4 续文（式 (3.3-4)、引理 3.3.4）→ §3.4 | ✅ 无重复（ch03-1 无此内容）；⚠️ 但 ch03-2 顶部注释误称“若重复可删”，见缺口 3 |
| ch04 | 单文件 | ✅ |
| ch05-1 → ch05-2 | 5.3.3 证明续文 → §5.4 | ⚠️ proof 环境需按注释删两处，见缺口 2；文本本身无重复 |
| ch06 | 单文件（§6.1–§6.4 完整） | ✅ |
| ch07、ch08 | 单文件 | ✅ |
| ch09-1 → ch09-2 | §9.3 续文（定理 9.3.7、(9.3-18)）→ §9.4 | ⚠️ 首句与 ch09-1 末句重复/断裂，见缺口 1；§9.3 续文本身无重复 |
| ch10-1 → ch10-2 | §10.3 | ✅ 顺序正确，无重复 |
| ch10-2 → ch10-3 | §10.4 | ✅ ch10-2 已含 10.3 末尾（Conjecture 10.3.12–10.3.13、(10.3-29)），ch10-3 从 §10.4 起，无缺无重 |
| ch10-3 → ch10-4 | §10.4 末段续文（“获得了有用的解释…”）→ §10.5 | ✅ 断句连续，无重复 |
| appendix | 单文件，A.1–A.5 | ✅ |

## 6. 附录核对（第 4 项要求）

原书附录 A.1 Lie algebras / A.2 Universal enveloping algebras / A.3 Simple Lie algebras / A.4 Central extensions / A.5 Affine Kac–Moody algebras。
`appendix.tex` 恰好 5 个 `\section`，顺序为 Lie 代数 → 泛包络代数 → 单李代数 → 中心扩张 → 仿射 Kac–Moody 代数，与 A.1–A.5 完全一致。✅ **齐全**。

---

### 附：核对数字汇总

| 项目 | 原书目录 | 译本（快照 16:21） | 差 |
|---|---|---|---|
| 正文章 | 10 | 10（各一次，顺序正确） | 0 |
| 编号节 | 41 | 41 | 0 |
| 附录节 | 5 | 5 | 0 |
| 小节 | 164 | 164 | 0 |
| 多出的节/小节 | — | 0 | — |
| 多出的章 | — | 1（术语表，译者增补） | 待确认 |
| 跨文件重复 `\section` | — | 0 | — |
| 缺口的节/小节 | — | 0 | — |
| 必须修的接缝 | — | 2（ch09 断句、ch05 proof 环境） | — |
