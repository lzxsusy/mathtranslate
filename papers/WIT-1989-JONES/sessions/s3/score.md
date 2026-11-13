# S3 独立评分（Verifier）

- 评分人：verifier ｜ 日期：2026-11-13
- 独立声明：未读 `sessions/s3/transcript.md`、`reports/`、`one_pager.md`；只评 `claims.jsonl`、`questions.jsonl` 与原文（页图 `witten1989/pages/page-NN.png`、OCR `witten1989/text/page-NN.txt`、译本 `witten1989/deliver/witten.tex` 与 `sections/*.tex`）。页图页号 = 印刷页 − 350。
- 抽检 5 条（要求 ≥4）。外部教材（Moore/河野/上野/nLab）不在 Verifier 允许材料内，标"范围外未独立核"。

## 1. 抽检表

| claim | 锚点 | 实测 | 判定 | 证据路径 |
|---|---|---|---|---|
| c-s3-01 | [src p.371]、eq 3.4 | p.371 L38–45 印 (3.4)：$k\,\epsilon^{ij}F^a_{ij}(x)=\sum_s\delta^2(x-P_s)T^a_{(s)}$；p.372 L5–7 "the solution $A$ of (3.4) cannot be an ordinary c-number connection, since non-commuting operators appear on the right-hand side"；p.371 L49–51 称 naive 量子化 (3.4) 极困难。"$\hat G|\psi\rangle=0$"为重建。 | **pass**（补 p.372） | `text/page-21.txt` L38–51；`text/page-22.txt` L5–7 |
| c-s3-03 | [src p.372] | p.372 L7–11：q-number connection…"quantum group"…"it seems likely that the theory of quantum groups [35] can be considered to arise in this way"——presumably/seems likely，无定义无构造。 | **pass** | `text/page-22.txt` L7–11 |
| c-s3-04 | [src p.372]、[nLab] | p.372 L15–26 逐句：BWB "gives a canonical way to exhibit for every irreducible representation $R$ … quantization of this classical problem gives back $R$ … flag manifold $G/T$ … symplectic structure $\omega_R$"。"$H^0(G/T,L_\lambda)=R$"原文未写，属标准重建。 | **pass**（标 [重建]） | `text/page-22.txt` L15–26 |
| c-s3-07 | [src p.372]、[Moore B.34/B.36 p.165] | **fail**：全文 OCR 无 half-form/metaplectic/square root（零命中）；p.372 只有 BWB+相空间，无"Witten 明说略去半形式"之句；该说法来自译本 [Tutor Note] `deliver/witten.tex:1206–1208`（=`sections/s04-canonical.tex:200–202`）："Witten 在本节略去了半形式修正"——译注推断被写成原文"明说"，违反 §7.4；按 §6.1(1) 引文与原文不符。$K_{G/T}=L_{-2\rho}$、$K^{1/2}=L_{-\rho}$ 本身是标准重建。 | **fail** | 全文 grep；`deliver/witten.tex:1206–1208`；`sections/s04-canonical.tex:200–202` |
| c-s3-10 | [src p.371] | partial：p.371 L36 "deferring a fuller treatment for another occasion" ✓；但"替换成 $S^1\to G/T$ 泛函积分"的陈述在 **p.373 L3–5**："One should use the theorem to replace the Wilson lines (1.5) … with a functional integral over maps of the circle $S^1$ into $G/T$…"——"One should"=纲领确有陈述；"无陈述无证明"过头，应改"只有纲领性陈述、无证明"。 | **partial** | `text/page-21.txt` L36；`text/page-23.txt` L3–5 |

## 2. 六维评分（每条扣分带锚点）

| 维 | 分 | 扣分点与锚点 |
|---|---|---|
| T1 原子性 | **12 / 15** | −2 c-s3-07 一条捆"$\lambda$ 不加 $\rho$／$K_{G/T}=L_{-2\rho}$／$K^{1/2}=L_{-\rho}$／Witten 明说"四断言（`text/page-22.txt` L15–26；`deliver/witten.tex:1206–1208`）；−1 c-s3-11 捆"$2j\le k$ 不在原文／非 BWB 推论／仿射上限／教材出处"四项（`text/page-22.txt` L41–47；`text/page-23.txt` L29–31） |
| T2 依据闭合 | **13 / 20** | −4 c-s3-07："明说"无原文（全文无 half-form；p.372 无此句；`deliver/witten.tex:1206–1208` 是译注）；−1 c-s3-10 漏 p.373 L3–5；−1 c-s3-04/08/09 的 $H^0$ 与 $\omega_R$ 公式化属重建未标；−1 外部锚（Moore p.165、河野 p.11、上野 p.39、nLab）范围外未核 |
| T3 分支失败修复 | **14 / 20** | −6：counterpoints 空 8/12（c-s3-01/02/03/04/06/08/09/11）；c-s3-07 的分叉只写"报告人推断未逐字核"，无 §2.4 "如果我对/如果作者对→判定"的修复路径 |
| T4 边界置信 | **10 / 15** | −4：8/12 无边界条件；−1 c-s3-07 confidence=medium 但核心断言错（"明说"），边界未起作用 |
| T5 可机读 | **7 / 15** | −8：validator 44 项/12 条——status 12 全 confirmed/provisional（非法）、confidence 12 全字符串、session 12 小写 s3（与 §5 示例 "S2" 不一致）、counterpoints 空 8；anchors "[src p.N]" 非 §5 的 p.N/eq x.y |
| T6 反事实迁移 | **10 / 15** | −5：迁移只散见 c-s3-09（SU(2) 验算）、c-s3-11（$2j\le k$ 来源）、c-s3-12（Moore 定义）；无一条显式回答"换一个群/k/流形，哪一步会变" |

## 3. 总分与准入

**总分 66 / 100。** §6.1(1) 一票否决触发（c-s3-07 "Witten 明说不做半形式"无原文依据，实为译注）→ 按 §6.2 **本场不进语料；需重评**。

## 4. §6.1 否决

c-s3-07 的"Witten 明说不做半形式"在原文任何页找不到（全文无 half-form/metaplectic 字样；p.372 只讲 BWB），实为译本译注（`deliver/witten.tex:1206–1208`："Witten 在本节略去了半形式修正"）被写成原文立场，违反 §7.4；按 §6.1(1) 判 fabricated。**整改后可解除**：改为"原文全文未提半形式修正（[译注] 本节略去，见 `sections/s04-canonical.tex:200–202`）"。

## 5. 整改项（按优先级）

1. **c-s3-07**：删"明说"，改"原文全文未提 half-form（[译注]：本节略去，`sections/s04-canonical.tex:200–202`）；$\rho\leftrightarrow$ 半形式为报告人推断，非原文"；$K_{G/T}=L_{-2\rho}$、$K^{1/2}=L_{-\rho}$ 标 [重建]。
2. **c-s3-10**：补 `p.373 L3–5`；"无陈述无证明"→"只有纲领性陈述（should），无证明"。
3. **schema（T5）**：status→active/contested/refuted；confidence→数值（如 0.85）；session→大写 "S3"（或 Lead 统一口径并同步 CHARTER）；补 8 条 counterpoints；anchors 统一 p.N / eq x.y。
4. **c-s3-01** 补 `p.372` 锚；c-s3-04/08/09 的公式化标 [重建]；外部教材锚标"Verifier 范围外未独立核"。
5. **补 §2.4 分叉**：至少 2 条（建议 c-s3-07 的 $\lambda\leftrightarrow\rho$ 与 c-s3-10 的泛函积分严格化），写"如果我对，应看到 X；如果作者对，应看到 Y→判定"。
