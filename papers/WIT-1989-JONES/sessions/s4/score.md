# S4 独立评分（Verifier）

- 评分人：verifier ｜ 日期：2026-11-13
- 独立声明：未读 `sessions/s4/transcript.md`、`reports/`、`one_pager.md`；只评 `claims.jsonl`、`questions.jsonl` 与原文（页图 `witten1989/pages/page-NN.png`、OCR `witten1989/text/page-NN.txt`、译本 `witten1989/deliver/witten.tex` 与 `sections/*.tex`）。页图页号 = 印刷页 − 350。
- 抽检 5 条（要求 ≥4）。外部教材（河野）不在 Verifier 允许材料内，标"范围外未独立核"。

## 1. 抽检表

| claim | 锚点 | 实测 | 判定 | 证据路径 |
|---|---|---|---|---|
| c-s4-01 | [src p.370]、[src p.366] | p.370 L44–45："the space of conformal blocks in 1+1 dimensions **are** the quantum Hilbert spaces obtained by quantizing a 2+1 dimensional theory"——"are" 确认；p.366 L23–29 "precisely those functors can be obtained by quantization of a three dimensional quantum field theory" ✓ | **pass** | `text/page-20.txt` L44–45；`text/page-16.txt` L23–29 |
| c-s4-03 | [src p.397] | p.397 L25–28："It is obvious at this point that by considering more complicated Riemann surfaces with various boundary components, we can generate the whole 1+1 dimensional conformal field theory"——"obvious"=纲领，无缝合/函子性证明 ✓ | **pass** | `text/page-47.txt` L25–28 |
| c-s4-04 | [src p.359]、(2.16)(2.17) | p.370 L33–34 current algebra "level" $k$；p.390 L5–6 "integrable representations of level $k$ … $n=0\ldots k$"；(2.16)(2.17) p.359 的 $k\to k+c_2/2=k+h^\vee$ → "k+h∨ 不是 level 差而是同一 $k$ 在 WZW 侧的组合形式"是解释非原文；内容为正确处理 ✓ | **pass**（术语标 [解释]） | `text/page-20.txt` L33–34；`text/page-40.txt` L5–6；`text/page-09.txt` L35–45 |
| c-s4-08 | [src p.394]、[src p.396]、[src p.397] | **fail（锚）**：p.394 属 §4.6 "The Knot Polynomials and the Braid Group"（`text/page-44.txt` L17 起），非 §5，且全文 OCR 无 "dictionary" 字样；p.396 L19–22 原文是 "**can be interpreted as** the spaces of conformal blocks"=词典级，不是定理级；Segal [39] 定理在 **p.397 L18–24**；p.397 L25–28 的 "It is obvious…" 才是纲领级。即：词典级→p.396，定理级→p.397，纲领级→p.397；claim 三处页锚两处错、一处级别错。 | **fail** | `text/page-44.txt` L17；`text/page-46.txt` L19–22；`text/page-47.txt` L18–28 |
| c-s4-09 | [src p.396] | partial：内容 ✓（p.397 L18–24 "according to Segal [39], the quantization of $LG/G$, with this symplectic structure, gives rise to the basic irreducible highest weight representation of the loop group"），但页锚 p.396→**p.397**。 | **partial**（页锚 −1） | `text/page-47.txt` L18–24 |

## 2. 六维评分（每条扣分带锚点）

| 维 | 分 | 扣分点与锚点 |
|---|---|---|
| T1 原子性 | **13 / 15** | −1 c-s4-08 一条含"三处措辞强度"三断言（同主题，轻度）；−1 c-s4-10 一条综合对象级/函子级/范畴级三层判断 |
| T2 依据闭合 | **14 / 20** | −2 c-s4-08 两处页锚错+一处级别错（`text/page-44.txt` L17；`text/page-46.txt` L19–22；`text/page-47.txt` L18–24）；−1 c-s4-09 p.396→p.397；−1 c-s4-04 "WZW 侧组合形式"属解释未标；−1 c-s4-02 "两边都是 $H^0(M_J,L^{\otimes k})$"是推断（p.369 只给 CS 侧，p.370 原话是 "exactly reproduced this description"）；−1 外部河野（c-s4-07 p.25–28）范围外未核 |
| T3 分支失败修复 | **15 / 20** | −5：counterpoints 空 6/11（c-s4-02/06/07/08/09/11）；但 q-s4-01（函子性缺哪条公理）、q-s4-02（半形式符号 $k-h^\vee$ 还是 $k+h^\vee$ 的 A/B 分歧）记录了分叉与修复方向 |
| T4 边界置信 | **11 / 15** | −4：6/11 无边界条件；c-s4-09 confidence=high 但页锚错；c-s4-02 high 但结论为推断 |
| T5 可机读 | **9 / 15** | −6：validator 28 项/11 条——status 已用 active 合法（0 项）、confidence 11 条字符串、session 11 条小写 s4、counterpoints 空 6 |
| T6 反事实迁移 | **11 / 15** | −4：c-s4-04/05/06/07/08 有跨群/跨 $k$/半形式/KZ/词典的迁移，但无一条显式回答"换一步（加半形式、换群、换流形）会变什么" |

## 3. 总分与准入

**总分 73 / 100。** 未触发 §6.1 一票否决（c-s4-08/c-s4-09 是页锚错位，内容本身可在相邻页找到，按页差 1 页不判 fabricated，与 S1/S2 复审口径一致）；按 §6.2 单场 T≥75 才计入 → **本场不进语料；需重评**。

## 4. 整改项（按优先级）

1. **c-s4-08 页锚重排**：词典级→p.396 L19–22（"can be interpreted as"）；定理级→p.397 L18–24（Segal [39]）；纲领级→p.397 L25–28（"It is obvious…"）；"§5 三处"改为"§5 一处（p.396 词典）+ p.397 两处"。
2. **c-s4-09**：页锚 p.396→p.397；q-s4-03 的"p.396 的 Segal 定理"同步改 p.397。
3. **schema**：confidence→数值；session→"S4"（口径）；补 6 条 counterpoints。
4. **c-s4-02**：把"两边都是 $H^0(M_J,L^{\otimes k})$"标 [重建]（p.369 只给 CS 侧；p.370 是 "exactly reproduced this description"）。
5. **c-s4-07** 外部河野锚标"范围外未核"；c-s4-04 的"组合形式"标 [解释]。
6. **补 §2.4 分叉**：建议把 c-s4-05 的半形式符号写成两分支——"若加 $K^{1/2}$ 后符号为负（$k-h^\vee$），应看到…；若为正（$k+h^\vee$），应看到…→判定"。
