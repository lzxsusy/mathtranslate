# 勘误卡（correction）审计报告

日期：2026-11-19　范围：`datasets/seidel/cards/corrections/*.json`（30 张）

## 一、结论摘要

| 项目 | 结果 |
|---|---|
| 卡片数 | 30 |
| 修订总表数据行 | 40 |
| 覆盖 | **40/40**，无遗漏；合并卡 3 张（operad、a05-41、thimble） |
| 逐字一致（original/corrected 对表） | 29/29 可比对卡全部一致；a09-cd 一行为表损坏，按报告/译注复原 |
| 页码回页图核对 | **30/30 卡**（含合并卡分页共 33 个印刷页，均看页图，非仅文本层） |
| 修正卡片 | 24 张（另 4 张 ok，2 张 unresolved） |
| 页码修正 | 12 张 |
| lint | `python tools/lint_cards.py --strict` → 70 张卡，**0 error，0 warn** |

三句话：合并卡与行号注记全部对齐；12 张卡的页码、8 处被截断的 summary/why 已修正；**a04、a08-a 两条修订本身不成立**（英文原句与修订所据引文不符），卡内已标为待核并建议回退，未擅自改修订方向。

## 二、核对口径

1. **行号**：修订总表第 2–41 行为数据行 1–40，本报告及卡内 note 一律用数据行号。卡内原来自造的「第 N 条」已全部改成真实行号。
2. **逐字比对**：读 TSV 原始字段（不清洗内部反引号），仅在两端口径一致时去掉包裹反引号。合并卡取组内一条全文作卡面，其余在 note 列明。
3. **页码**：先看 `reason` 的 p.N 与 `page_map.csv`，再打开 `work/pages/pNNN.png`（缺页用 pdftoppm 按「印刷页+8」生成）确认该页确有对应英文句子；两者冲突时以页图为准。
4. **理由**：why 中引用的英文原句一律回页图核对；数学论证按原书上下文复核。
5. **errata**：`work/errata.md` 仅 5 条（p4/5 Theorem A、p4 combinational、p106 §8g、p24 Lemma 2.1、p52 Lemma 3.30），与 30 卡无一对应；因此卡片一律不冒充 errata 条目。

## 三、逐卡结果

`rows` 为修订总表数据行；`✓` = 页图已核。

| 卡 | rows | page | 页图 | 判定 | 问题与处置 |
|---|---|---|---|---|---|
| a01-introduction-49 | 1 | 5 | ✓ | fixed | 页码 1→5（p5 Corollary C）；「笔误」改「排版笔误」，避免误读为原书笔误 |
| a02-section-3-51 | 4 | 33 | ✓ | ok | 四要素一致；p33 核 `Hom_{H(Q)}(X,Z⊗Y)` |
| a03-section-4-19 | 5 | 55 | ✓ | fixed | p55 核 tautological；summary 原被截断，已补全 |
| a04-section-6-7 | 6 | 87 | ✓ | **unresolved** | 原书实作 `In fact, this just consists of an involution…`，无 `Concretely,`；修订不成立，建议回退 |
| a05-section-10-cd-41 | 7-8 | 138 | ✓ | fixed | 两条同 slug 合并；p138 同段 `H²(Γ;HH⁰)` 与 `H²(π₀(G);π₁(G))` 均见图；卡面取第 8 条，note 列第 7 条 |
| a05-section-10-cd-10 | 9 | 137 | ✓ | fixed | 页码 138→137（p137 `the Floer data for the pairs`） |
| a06-section-11-a-46 | 10 | 151 | ✓ | fixed | 页码 150→151（p151 `removing the sign`） |
| a06-section-11-gh-32 | 11 | 163 | ✓ | fixed | 页码 162→163（p163 `the pair (μ,w₂)`） |
| a06-section-11-ef-123 | 12 | 161 | ✓ | fixed | 页码 158→161（p161 `nonempty null space`） |
| a06-section-11-jl-26 | 13 | 170 | ✓ | ok | 四要素一致（p170 `mostly but not entirely satisfactory`）；summary 补出改后表述 |
| a07-section-12-ef-106 | 14 | 183 | ✓ | fixed | 页码 180→183；TSV reason 被截断，why 据报告补全；p183 核 `→K` |
| a07-section-12-gh-24 | 15 | 184 | ✓ | fixed | p184 核 `+2−d`；summary 原被截断，已补全 |
| a07-section-12-gh-8 | 16 | 183 | ✓ | fixed | 页码 184→183；**原书实印 `⊂`**，报告误称 `∈`；按原书排印笔误处理，errata 缺条已注明 |
| a07-section-13-c-25 | 17 | 196 | ✓ | fixed | p196 核 `a square with the two vertical sides identified`；summary 重复的「改为「改为「」已修 |
| a08-section-14-a-44 | 18 | 199 | ✓ | **unresolved** | 原书实作 `hence explains (14.3)`，非 `gives a proof`；修订不成立，建议回退 |
| a08-section-14-c-15 | 19 | 203 | ✓ | ok | p203 核 `There is a Z worth of choices`；page_map 的 204 有误 |
| a09-section-16-ab-9 | 20 | 221 | ✓ | fixed | p221 核 `contractible for n<3`；why 原称 n=3 时该群不平凡，不确，改为原书只断言 n<3、译文不应扩大范围 |
| a09-section-16-ab-13 | 21 | 221 | ✓ | fixed | p221 核 `unique embedded Lagrangian (n+1)-ball`；「指套」统一为「顶针」 |
| a09-section-16-ab-44 | 22 | 223 | ✓ | fixed | 页码 221→223（p223 `τ'' is an embedded (n+1)-ball`） |
| a09-section-16-ab-51 | 23 | 223 | ✓ | fixed | 页码 221→223（p223 `immersed … Lagrangian balls`） |
| a09-section-16-cd-10 | 24 | 224 | ✓ | fixed | TSV 该行竖线误作 tab、字段错位；按 report-A09 与注 A09-04 重建；p224 核 `|ξ|²/2` 与对径映射 |
| a09-section-16-g-14 | 25 | 231 | ✓ | fixed | p231 核 `conformally symplectic embedding` 与后文 `ρ`；summary 截断已补 |
| a09-section-16-hi-65 | 26 | 234 | ✓ | fixed | p234 核 `√(1−s)S^n⊂C^{n+1}`；summary 补出 `S^{n+1}→S^n` |
| a09-section-17-a-45 | 27 | 237 | ✓ | fixed | 页码 236→237（p237 (17.5) 的 `R(∂s,∂t)`） |
| a10-section-17-j-2 | 28 | 261 | ✓ | fixed | p261 核 `Example 17.14 applies`；page_map 的 262 有误；summary 截断已补 |
| a10-section-17-k-41 | 29 | 265 | ✓ | fixed | p265 核方框第二式 `κ`；summary 原未说明 `k→κ`，已重写 |
| a12-section-19-c-33 | 39 | 300 | ✓ | ok | p300 核 `unique up to isotopy and orientation-reversal`；summary 补出改后表述 |
| a12-section-20-b-20 | 40 | 306 | ✓ | fixed | p306 核 `once one has made … strictly unital`；why 原称「缺谓语」不确，已改写 |
| operad-shuyunpei | 2-3 | 7 | ✓ | fixed | pages 改 `[7,19]`，p7/p19 均见图；卡面取第 2 条，note 列第 3 条 |
| lefschetz-thimble-dingzhen | 30-38 | 267 | ✓ | fixed | 9 条修订（12 处）合并；page 266→267、pages `[267,291]`；18-eb:2 实在 p278 |

## 四、页码修正（12 张）

| 卡 | 原 | 新 | 依据 |
|---|---|---|---|
| a01 | 1 | 5 | p5 Corollary C |
| a05-10 | 138 | 137 | p137 Floer data for the pairs |
| a06-11-a-46 | 150 | 151 | p151 removing the sign |
| a06-11-gh-32 | 162 | 163 | p163 the pair (μ,w₂) |
| a06-11-ef-123 | 158 | 161 | p161 nonempty null space |
| a07-12-ef-106 | 180 | 183 | p183 c_u → K |
| a07-12-gh-8 | 184 | 183 | p183 ⊂ (∂D)^{d−2} |
| a09-16-ab-44 | 221 | 223 | p223 embedded (n+1)-ball |
| a09-16-ab-51 | 221 | 223 | p223 Lagrangian balls |
| a09-17-a-45 | 236 | 237 | p237 (17.5) |
| thimble | 266 | 267 | p267 Type (B) 两处 thimble |
| operad | sources [7,7] | [7,19] | p7、p19 两处 operad |

## 五、合并卡明细

- **operad（第 2–3 条）**：`chapter-i.tex:4`（p7）、`section-1.tex:407`（p19）。卡面 original/corrected 取第 2 条全文；note 给出第 3 条原文与改文。
- **a05-41（第 7–8 条）**：同为 `section-10-cd.tex:41`。第 7 条 `H³(Γ;HH⁰(A,A)^×)→H²`，第 8 条 `H³(π₀(G);π₁(G))→H²`；卡面取第 8 条，why/note 两条均写明。p138 同段可见两处 `H²`。
- **thimble（第 30–38 条）**：9 条修订、**12 处**「指套」。页码：18-a:53/:57→267；18-c:10/:15→272；18-d:28→275；18-eb:2→**278**；18-l:15/:21→290、:34→291。卡面取第 30 条 `Lefschetz 指套`→`Lefschetz 顶针`。

## 六、未解决项

1. **a04-section-6-7（建议回退）**：页图 p87 明作 `In fact, this just consists of an involution on objects…`。原修订声称英文为 `Concretely,`，据此把「事实上」改「具体地说」；引文不存在，修订不成立。卡内已标「待核…建议回退」，但 original/corrected 仍保留表内字样（为满足逐字回溯），**需负责人决定是否从修订总表撤条**。
2. **a08-section-14-a-44（建议回退）**：页图 p199 明作 `hence explains (14.3)`，初版「说明」正确；修订所据 `hence gives a proof of (14.3)` 不存在。同上，待撤条决定。
3. **a07-12-gh-8 的 errata 缺口**：原书 p183 确印 `⊂`，数学上应为 `∈`；这是原书排印错，但 `errata.md` 未收。卡内已注明「建议补录」，**建议在 errata.md 增补 p183 一条**。
4. **源数据待修（不影响卡，但影响下次审计）**：
   - 修订总表数据行 24（`section-16-cd.tex:10`）的 `|` 被写成 tab，old/new/reason 三字段错位；
   - 数据行 14（`section-12-ef.tex:106`）的 reason 在「用来把 $」处截断，完整理由只在 `report-A07.md` 第 32 行；
   - `page_map.csv` 三处 off-by-one：`section-18-eb.tex` printed_first 279（实 278）、`section-14-c.tex` 204（实 203）、`section-17-j.tex` 262（实 261）；
   - `report-A07.md` 第 34 行称原书 g8 作 `∈`（实印 `⊂`）；`report-A09.md` 第 21 行 corrected 用「……」截断。
5. **a05-41 的表示方式**：卡面只能显示一条，另一条靠 note。若下游要求「一行一卡」，后续可拆成两张（当前满足「合并卡 note 列明」的要求）。

## 七、翻译修订 vs 原书笔误

30 张中 29 张是**译文修订/术语统一**（把误译、误抄、术语不统一改回原书或标准译名），只有 **a07-12-gh-8 触碰原书排印**：原书 `⊂` 应为 `∈`。该条在分章报告 A07 中已按「记号笔误」记录，但报告把原书说成 `∈`，与页图不符；本卡按页图事实改写，并明确 errata 尚未收录。其余卡片一律未冒充 errata 条目。

## 八、40 行覆盖索引

| 行 | 卡 | 行 | 卡 |
|---|---|---|---|
| 1 | a01 | 21 | a09-ab13 |
| 2-3 | operad | 22 | a09-ab44 |
| 4 | a02 | 23 | a09-ab51 |
| 5 | a03 | 24 | a09-cd |
| 6 | a04 | 25 | a09-g |
| 7-8 | a05-41 | 26 | a09-hi |
| 9 | a05-10 | 27 | a09-17a |
| 10 | a06-a | 28 | a10-j |
| 11 | a06-gh | 29 | a10-k |
| 12 | a06-ef | 30-38 | thimble |
| 13 | a06-jl | 39 | a12-19 |
| 14 | a07-ef | 40 | a12-20 |
| 15 | a07-gh24 | | |
| 16 | a07-gh8 | | |
| 17 | a07-13c | | |
| 18 | a08-a | | |
| 19 | a08-c | | |
| 20 | a09-ab9 | | |

## 九、复现命令

```
cd C:\Users\admin\Desktop\数译发布\gitee_shuyi\datasets\seidel
C:\Users\admin\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe tools/lint_cards.py --strict
```

输出：`卡片 70 张（概念 32，推导 8，勘误 30）` / `OK，0 error，0 warn`。
