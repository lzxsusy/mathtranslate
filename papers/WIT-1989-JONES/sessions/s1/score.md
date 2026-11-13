# S1 独立评分（Verifier）

- 评分人：verifier ｜ 日期：2026-11-13
- 独立声明：未读 `sessions/s1/transcript.md`、`reports/`、`one_pager.md`；只评 `claims.jsonl`、`questions.jsonl` 与原文（页图 `witten1989/pages/page-NN.png`、OCR `witten1989/text/page-NN.txt`、译本 `witten1989/deliver/witten.tex`、`witten1989/sections/*.tex`、校勘汇总）。页图页号 = 印刷页 − 350。
- 抽检 5 条（任务要求 ≥4；含 c-s1-12、c-s1-13）。

## 1. 抽检表

| claim | 锚点 | 实测 | 判定 | 证据路径 |
|---|---|---|---|---|
| c-s1-02 | 原文 p.352；文献[4] p.398 | p.352 有 "It has turned out that Donaldson theory can indeed be given a physical interpretation [4]." ✓；但文献[4]（Witten, CMP 117, 353 (1988)）在 **p.397**，不在 p.398 | **pass**（页锚 −1 页） | `witten1989/text/page-02.txt` L7–8；`witten1989/text/page-47.txt` L39–40 |
| c-s1-05 | 原文 p.356 / p.353 / p.396 | "we will assert" **原文不存在**：p.355 是 "we will claim that the invariants (1.6) are exactly those that appear in the Jones theory and its generalizations."；p.356 顶部是 "We claim that these properties…"，无 assert；"argue" 在 **p.354**（"…and argue that it is exactly soluble"），p.353 无 argue；p.396 的 "can be interpreted as the spaces of conformal blocks" ✓ | **fail**（引文与原文不符） | `witten1989/pages/page-06.png`；`witten1989/text/page-05.txt` L33–36；`witten1989/text/page-04.txt` L18–19；`witten1989/text/page-46.txt` L22 |
| c-s1-10 | eq 1.2；原文 p.353；s01-cs-action.tex:188–193 | 页图 (1.2) 逐符号为 L₀=∫√g g^{ik}g^{jl} Tr(F_ij F_kl)，**无 1/4、无负号**；脚注 1 说明 Tr 为 Cartan–Killing 型的倍数、归一化随后指定；tex 复核记录（2026-10-27）同结论，并写明与 −¼∫√g Tr F² 的差别来自 Tr 归一化与反厄米约定 | **pass** | `witten1989/pages/page-03.png`；`witten1989/text/page-03.txt` L37–44；`witten1989/sections/s01-cs-action.tex:188–193` |
| c-s1-12 | eq 1.6；eq 4.41；原文 p.391 | (1.6) p.355 ✓；(4.41)（Z→Z·exp(2πi(n−m)c/24)）在 **p.390**（page-40.txt L30–31），不在 p.391；"定理化要等组合侧 RT 1991" 属未锚的二手判断（其 counterpoint 亦自认） | **pass**（页锚 −1 页） | `witten1989/text/page-05.txt` L22–23；`witten1989/text/page-40.txt` L30–31 |
| c-s1-13 | 原文 p.366–367；s04-canonical.tex:159–171 | p.366 有 "These will turn out to be finite dimensional spaces." ✓；但 "one quantum state per unit volume in classical phase space…will be finite dimensional" 在 **p.368**（page-18.txt L25–28），不在 p.366–367；tex 159–171 含正文译句＋半经典计数译注（Weyl 律、指标定理/Verlinde、[ω] 整性前提），内容吻合 | **pass**（页锚补 p.368） | `witten1989/text/page-16.txt` L20；`witten1989/text/page-18.txt` L25–28；`witten1989/sections/s04-canonical.tex:159–171` |

## 2. 六维评分（每条扣分带锚点）

| 维 | 分 | 扣分点与锚点 |
|---|---|---|
| T1 原子性 | **9 / 15** | −2 c-s1-05 一条 claim 捆 G1/G2/G5 三处措辞＋"无 prove" 四断言；−2 c-s1-09 捆措辞＋Wilson 插入＋同痕类＋(N,k,q) 四断言（`text/page-05.txt` L13–14, L22–23, L33–36；`text/page-32.txt` L40–41）；−1 c-s1-13 捆断言＋半经典计数＋后世计数（`text/page-16.txt` L20；`text/page-18.txt` L25–28）；−1 c-s1-06 捆度规无关＋变分系数（`text/page-04.txt` L18–20） |
| T2 依据闭合 | **8 / 20** | −7 c-s1-05：fabricated 引文（"we will assert" 全文不存在，实为 "we will claim"，且与 c-s1-09 自相矛盾；`pages/page-06.png`；`text/page-05.txt` L33–36；`text/page-04.txt` L18–19；译本作"我们将断言"，见 `deliver/witten.tex:421`）；−2 c-s1-04："全篇无 prove、demonstrate、establish" 若指摘要则成立，按字面指全文则不成立——p.367/370/373/379/380/391 均有 prove/proved（`text/page-17.txt` L45；`text/page-20.txt` L28；`text/page-23.txt` L44；`text/page-29.txt` L24；`text/page-30.txt` L3；`text/page-41.txt` L41）；−1 c-s1-12 p.391→p.390；−1 c-s1-13 p.366–367 漏 p.368；−1 c-s1-01/c-s1-02 文献[1][4] p.398→p.397 |
| T3 分支失败修复 | **13 / 20** | −7：c-s1-04、c-s1-05、c-s1-11 的 counterpoints 为空（脚本计数 3/13）；全 13 条无一条按 §2.4 的"如果我对/如果作者对→Y/Z"格式写分叉；修复路径只在 c-s1-08（测度不变性未证）、c-s1-10（改已译资料清单）、c-s1-12（RT 1991）出现 |
| T4 边界置信 | **11 / 15** | −3 c-s1-05 confidence=high 但核心引文不实（`pages/page-06.png`），且无边界条；−1 c-s1-04 confidence=high 但"全篇"表述与 p.367/370/373 等 6 处 prove 冲突、无边界条；−1 c-s1-11 无边界条 |
| T5 可机读 | **8 / 15** | −7：脚本按 CHARTER §5 校验 13 条得 29 项违规——status 13 条全非法（accepted/provisional/downgraded，应为 active/contested/refuted）、confidence 13 条全为字符串（应为 0–1 数值）、counterpoints 空 3 条；锚点写法混用 "原文 p.N" / "eq 1.3" / "s01-cs-action.tex:188–193"，缺可解析的 `p.N`/`eq x.y` 规范 |
| T6 反事实迁移 | **9 / 15** | −6：只有 c-s1-07/08/09/12 有跨群/跨 k/跨流形的迁移（c-s1-09 给 SU(N) 与 q（`text/page-32.txt` L40–41）；c-s1-12 给手术表示与 framing（`text/page-40.txt` L30–31））；没有一条显式回答"换一个群/换一个流形，哪一步会变"；c-s1-13 的"严格计数"与 c-s1-12 的 RT 1991 延伸均无本地锚 |

## 3. 总分与准入

**总分 58 / 100。** §6.1(1) 一票否决触发：抽检 c-s1-05 的引文与原文不符（"we will assert" 在 p.356 页图上不存在；原文为 "we will claim"／"We claim"，"argue" 在 p.354）。按 §6.2 单场 T≥75 才计入 → **本场不进语料；需重评。**

## 4. 整改项（按优先级）

1. **重写 c-s1-05**：把 "we will assert（p.356）" 改为 "we will claim（p.355；p.356 顶部为 We claim）"，G2 页锚 p.353→p.354；凡引译本"断言"必须标 `[译注]`（`deliver/witten.tex:421`），不得回译成原文。重写后必须与 c-s1-09 的引文一致。
2. **页锚批改**：c-s1-12 p.391→p.390（`text/page-40.txt` L30–31）；c-s1-13 补 p.368（`text/page-18.txt` L25–28）；c-s1-01/c-s1-02 文献[1][4] p.398→p.397（`text/page-47.txt` L39–44）。
3. **收紧 c-s1-04**："全篇"改为"摘要四句"，否则与 p.367/370/373/379/380/391 的 prove/proved 冲突（`text/page-17.txt` L45 等）。
4. **补边界**：c-s1-04/05/11 各补一条"该结论在什么情况下不成立"，并把 c-s1-05 的 confidence 降为数值低值。
5. **schema 对齐 CHARTER §5**：status→active/contested/refuted；confidence→数值（如 0.85）；anchors 统一为 `p.N` / `eq x.y`；补 3 条空 counterpoints。
6. **补 §2.4 分叉**：至少 2 条"如果我对，应看到 Y；如果作者对，应看到 Z"的显式检验（建议用在 k∈Z 是否在测度层成立、第二问是否已定理化）。
7. **标注二手**：c-s1-12 的 RT 1991 判断标 `[后世]` 并给可核出处；c-s1-13 的"指标定理/Verlinde 严格计数"标 `[后世]`。
8. questions：q-s1-06 的 target "p.391" 应改 p.390（`text/page-40.txt` L30–31）。

## 5. 复审（2026-11-13 第二轮；历史分不改）

- 抽检（Lead 指定 + 随机）：c-s1-05、c-s1-12、c-s1-13、c-s1-01/c-s1-02、q-s1-06。

| 项 | 原问题 | 现文核对 | 判定 |
|---|---|---|---|
| c-s1-05 | "we will assert"(p.356) 原文不存在 | 现文："we will claim"(p.355)、p.356 顶部 "We claim"、argue p.354、G5 "can be interpreted as"(p.396)、第二问无 prove——与 `text/page-05.txt` L33–36、`pages/page-06.png`、`text/page-04.txt` L18–19、`text/page-46.txt` L22 逐句相符 | **修复** |
| c-s1-12 | (4.41) 页锚 p.391 | 已改 p.390（`text/page-40.txt` L30–31） | **修复** |
| c-s1-13 | 缺 p.368 | 已补 p.368（`text/page-18.txt` L25–28） | **修复** |
| c-s1-01/c-s1-02 | [1][4] 页锚 p.398 | 已改 p.397（`text/page-47.txt` L39–45） | **修复** |
| q-s1-06 | target p.391 | 已改 p.390 | **修复** |

- §6.1(1) 否决：**解除**（c-s1-05 引文已与原文一致，不再构成 fabricated）。
- 仍未改（validator 42 项 / 13 条）：status 13 条仍为 accepted/provisional/downgraded（非法）；confidence 13 条仍为字符串；session 13 条小写 s1（与 §5 示例 "S2" 不一致，属口径问题）；counterpoints 空 3 条（c-s1-04/05/11）。
- 另：c-s1-04 的 "全篇无 prove、demonstrate、establish" **未改**；若"全篇"指全文，与 p.367/370/373/379/380/391 的 prove/proved 冲突（`text/page-17.txt` L45 等），应改"摘要四句内"。
- 复审结论：**否决解除；形式项仍未达标 → 复审不通过（仍有 42 项 schema + c-s1-04 一处表述）**。历史总分 58 不追溯修改。
