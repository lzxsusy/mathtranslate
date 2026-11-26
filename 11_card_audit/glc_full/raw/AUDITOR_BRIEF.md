# GLC 全量审计 · 审计员须知（v1，2026-11-26）

> 本文件是本次「陈麟 GLC 讲义 154 张资料卡全量审计」的唯一审计协议补充件。
> 上位规范：`11_card_audit/WORKFLOW.md`、`datasets/_audit/third_party_2026-11-26/AUDIT_HANDBOOK.md`（**只读规范，不读其中任何一批卡的结论**）。
> 你是独立审计员，不是作者。你的产出只有一份 JSONL，**绝不修改任何卡片**。

---

## 0. 五条硬约束

1. **绝不修改卡片 JSON**，不跑 `git checkout/reset/clean/stash`，不 `git add/commit`。仓库里有大量与本任务无关的未提交改动。
2. **不伪造证据**：没翻到原文就不写页码、不写引文。查不到就 `unverifiable` 并写清查了什么。
3. **禁止使用**：Wikipedia、知乎/博客/内容农场、AI 摘要、模型记忆、未打开的 PDF。允许：本讲义 PDF、本讲义中译源码、arXiv、出版社、nLab / Stacks（仅作强佐证，具体公式回原文）。
4. **不读上一批审计结论**：`datasets/_audit/third_party_2026-11-26/passA|passB|confirmed|tiebreak/` **禁止打开**（那批含 10 张 glc 卡的旧判断，本次必须重新核）。同目录的 `AUDIT_HANDBOOK.md` 可读。
5. **不为凑数找问题**：解释性措辞、风格、自洽记号约定、底本自身的错（卡忠实记录了它）都不算卡错。`pass` 是合法且必要的结论。

---

## 1. 路径（全部相对仓库根 `C:\Users\admin\Desktop\数译发布\gitee_shuyi`）

| 用途 | 路径 |
|---|---|
| 待审卡（154 张，全 `concept`） | `datasets/glc/cards/concepts/*.json` |
| **证据包（先读这个）** | `datasets/_audit/glc_full_2026-11-26/tmp/packs/<slug>.md` |
| 英文原讲义 PDF | `datasets/_audit/glc_full_2026-11-26/tmp/glc.pdf`（85 页） |
| 逐页文本（推荐） | `datasets/_audit/glc_full_2026-11-26/tmp/pages/pNNN.txt`（`p011.txt` = PDF 第 11 页） |
| 全文文本 | `datasets/_audit/glc_full_2026-11-26/tmp/glc.txt` |
| 中译源码（锚点目标） | `08_source_code/SY02-33_几何Langlands理论导论（陈麟）_中文译注校订版/源码/chapters/chNN.tex` |
| 本组清单 | `datasets/_audit/glc_full_2026-11-26/groups/<A组>.txt`（每行一个卡的仓库相对路径，顺序即 JSONL 的 `n` 顺序） |

**证据包 `<slug>.md`** 已为每张卡拼好：①卡 JSON 原文 ②`anchor` 指向的中译 TeX 切片（带行号，含 ±3 行上下文）③`pages` 对应英文 PDF 页文本（±1 页上下文）④`related` 目标是否存在及其标题。
slug = 卡 id 去掉 `glc/concept/` 前缀（例：`quantum-local-gl.md`）。**先读 pack，再用 `ops_inspect_local_file` / `sed` 回原文核可疑处。**

## 2. 页码与来源口径（glc 专用）

- **PDF 页 = 印刷页**（偏移 0）。已验证：PDF 第 11 页页眉印 `11`，该页正是 Conjecture 1.5.1。卡内 `pages` 与 `pdf_pages` 都按此写。
- 判定页码错之前，**先打开那一页看页眉数字**，不要按"大概位置"推断。
- `sources[].anchor` 形如 `源码/chapters/ch05.tex:114-123`，指向**中译校订本**的 TeX 行号；已机械校验全部 160 条锚点行号在文件范围内。锚点解析成功 ≠ 内容对齐，仍要读那几行。
- 本批 154 张卡的 `sources` **没有 `quote` 字段**（`book/section/pages/pdf_pages/anchor` 五个键）。所以"逐字引文"检查落在：卡内中文叙述 vs 中译 TeX 原句、卡内公式 vs 英文 PDF 原式。
- `datasets/glc/README.md` 的「本批修订记录」列了 2026-11-18 已修的 9 处对齐错误（quantum-local-gl、local-whittaker-eigenfunction、restricted-local-systems、categorical-trace、fourier-deligne-transform、averaging-functor、vanishing-theorem、whittaker-equivalence、global-langlands-functor）。**这 9 处若已改对，不要再报**；只有仍然错才报。
- 卡内 `verification` 块与 `datasets/glc/verification.jsonl` 只是**线索**，不是证据；不得作为判 pass 的依据。

## 3. 证据等级

| 等级 | 来源 | 用法 |
|---|---|---|
| E1 一手 | 本讲义 PDF、中译 TeX 源码、arXiv/出版社原文 | 可直接定错 |
| E2 权威二手 | nLab、Stacks Project、标准教材 | 仅作强佐证；冲突时以 E1 为准 |
| E3 卡内推导 | 卡自身定义/公式/前后文 | 可证内部不一致，不能单独证外部事实 |
| E4 不可用 | 记忆、博客、Wikipedia、AI 摘要 | 只能当"去查什么"的线索 |

## 4. 逐卡检查清单（按字段顺序，至少 3 条 `checks`）

**必须覆盖三类**（校验器会查）：
- `definition` / `theorem`（数学：量词、范围、条件、方向、层级、公式符号）
- `sources`（页码、锚点、节号、归因、与原文对齐）
- `internal`（summary / key_points / formulas / pitfalls / related 的自洽）

细项：
1. `definition.text` / `notation`：`∃/∀`、`F`-分裂、proper/closed、有限维/紧、阿基米德/非阿基米德；**假设是否被弱化或漏掉**（最常见错误）；记号是否与 `formulas` 一致；有没有把"必要"写成"等价"。
2. `theorems[]`：条件、结论、方向、逆命题；**层级**（定理/命题/引理/猜想/构造 是否与原文一致）；`proof.status`（`sketch`/`gap`/`complete`）是否诚实、`gap_note` 是否把"构造未给出"和"同构未验证"分开；`source` 的编号/页码。
3. `formulas[]`：符号、系数、归一化（`Tr`、`κ`、`2π`、`1/2`、`q` 的幂）、上下标与 bar/check、`GL_n` vs `GL_2`、`∏` vs `∑`、局部 vs 整体；公式与 `summary`/`pitfalls` 是否自相矛盾。
4. `sources[]`：`book`（作者/版本/年份）、`section`（是否精确到小节）、`pages`（是否覆盖所引定理）、`anchor`（能否解析、行号是否真的落在该内容上）。
5. 内部一致性：`summary` 与 `definition` 同方向；`key_points` 不把"已证"与"猜想"混在一起；`pitfalls` 不把正确写法标成错（会把读者教反）；`aliases`/`related`/`verification` 无残留旧结论、`related` 无断链。

## 5. 判定

- `pass`：核过，未发现可核实错误。
- `issue`：至少一个可核实错误，**必须带 `issues[]` 与证据**。
- `unverifiable`：没发现错，但关键点无法核（如锚点对不上、页码页无内容），且可能藏错；必须写 `unverifiable_aspects[]` 与 `notes`。

`confidence`：`high`（一手源逐字核）/ `medium`（部分核对或权威二手）/ `low`（仅间接证据）。

`severity`：
- `critical`：结论反了、定义恒真/恒假、核心公式符号错，下游数学整体失效。
- `major`：定理条件/方向/关键因子错；定理编号或出处错到无法定位；例子算错。
- `minor`：页码/节号/笔误/术语不精确/related 断链，不影响主结论。

## 6. 输出：一份 JSONL，一行一卡

文件写到 `datasets/_audit/glc_full_2026-11-26/passA/<组>_<reviewer>.jsonl`（或 Pass B 指定路径）。UTF-8，无 Markdown 围栏，无外层数组。

```json
{"n":1,"group":"A1","reviewer":"A1","pass":"A","set":"glc",
 "id":"glc/concept/quantum-local-gl",
 "path":"datasets/glc/cards/concepts/quantum-local-gl.json",
 "verdict":"issue","confidence":"high",
 "checks":[
   {"aspect":"definition","verdict":"ok","note":"对照 PDF p.11 Conjecture 1.5.1 与 ch01.tex:295-308，五组对应与 κ/κ̌ 配对一致。","evidence":[{"kind":"pdf","ref":"glc.pdf PDF p.11","quote":"..."}]},
   {"aspect":"sources","verdict":"ok","note":"anchor 行号 295-308 正落在 conjecture 环境内。"},
   {"aspect":"internal","verdict":"ok","note":"summary/formulas/pitfalls 的 Whit↔KM 互换一致。"}],
 "issues":[],
 "unverifiable_aspects":[],
 "notes":""}
```

issue 对象（`field` 用真实 JSON 路径：`summary`、`definition.text`、`key_points[2]`、`formulas[0]`、`theorems[1].statement`、`sources[0].pages`、`sources[0].anchor`、`sources[0].section`、`pitfalls[1]`、`related[0]`）：

```json
{"severity":"major","aspect":"theorem","field":"theorems[0].statement",
 "card_says":"卡上原句（逐字，可用 … 省略）",
 "problem":"为什么错；与哪条原文冲突",
 "should_be":"应改成什么（给最小改法）",
 "evidence":[{"kind":"pdf","ref":"glc.pdf PDF p.37, Theorem 6.2","quote":"逐字英文原文"}],
 "suggested_fix":"可选：最小编辑文本"}
```

要求：
- `n` 从 1 连续到本组张数，**顺序必须与 `groups/<组>.txt` 的行顺序一致**，`path` 必须逐字相同（校验器逐行比对）。
- `checks` ≥ 3 且覆盖三类；每条 `note` 必须写"对照了什么、结论是什么"，不能只写 "OK"。
- `card_says` 会被校验器在卡 JSON 里做子串比对（去掉空白后），**必须是卡上真实存在的文字**；引用多处用 `…` 连接。
- `verdict=issue` ⇔ `issues` 非空；`verdict≠issue` ⇒ `issues` 必须为空。

写完后**立即自检**（必须 0 error；WARN 可解释即可）：

```bash
cd /c/Users/admin/Desktop/数译发布/gitee_shuyi
python datasets/_audit/glc_full_2026-11-26/tools/check_audit.py \
  --file datasets/_audit/glc_full_2026-11-26/passA/A1_A1.jsonl --group A1 --reviewer A1
```

## 7. 常见误判（务必避开）

- **改写不是错**：卡用自己的话重述定义，只要量词/条件/结论等价，就不算错。
- **省略不是错**：`sketch` 有 `gap_note`、`reference` 说明不重证，不算证明缺失。
- **猜想不是错**：标了"猜想"的陈述与原文一致即可，不要求证明；但把定理降级成猜想、或把猜想写成定理，是 `major`。
- **底本的错不是卡的错**：卡若忠实记录"底本此处写 X，应作 Y"，核的是它记的错是否真实、改法是否对。
- **版本/编号差异**：先看卡写的书/版本，再判编号。
- **中文译名差异**：不同译法不算错，除非指错了对象（如把"球面 Hecke 范畴"说成"Hecke 特征层"）。
- **不要用卡自己的 `verification` 当证据**。
- **公式 OCR 风险**：PDF 文本层会把 `∞` 抬成上标、把 `−→` 拆成 `−→`、把 Ě 写成 `Ǧ`。核公式时对照上下文与 TeX 源码，别把 OCR 噪声当原文错误。

## 8. 最后一条消息只需给

`完成 N/M；pass X；issue Y；unverifiable Z；校验器 0 error；最严重问题一句话（卡 id + 一句）`。
