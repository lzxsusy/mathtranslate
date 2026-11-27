# 资料卡校对工作规范 v1.0

> 适用对象：`datasets/<set>/cards/**/*.json` 的数学资料卡，以及后续从卡片改写 Lean / 讲义的工序。
> 目标不是“把卡改得好看”，而是：**事实正确、出处可核、修改最小、过程可追溯、同类错误不再犯**。
>
> 本规范来自 2026-11-26 对 100 张随机卡的第三方审计（32 张卡实际修复）。它不是建议，是下一次动卡前的门槛。
>
> 制卡模板、字段枚举与 lint 见 [`../04_playbook/23_资料卡制作规范_v1.md`](../04_playbook/23_资料卡制作规范_v1.md)；本文件只规定「审计与校对」流程。

---

## 0. 三条铁律

1. **不伪造证据。** 没有翻到原文，就不写页码、不写引文、不写“已核”。记忆、猜测、渲染预览都不算证据。
2. **不强行找问题，也不放过真问题。** 解释性差异、风格、自洽的记号约定不算错；可核实的事实/数学/出处错误必须登记。
3. **改卡必须可回滚。** 每处改动有 `before` / `after`；只改确认过的字段；不 batch 重排；不碰无关卡。

违反任意一条，整批结果作废重审。

---

## 1. 角色与职责

| 角色 | 职责 | 禁止 |
|---|---|---|
| **Lead** | 抽样、分组、裁决、最终修卡、汇总报告 | 不亲自替代两名审计员做“双独立”判断 |
| **Pass A 审计员**（5 人） | 逐卡深审，写 `verdict + issues + checks` | 不改卡；不引用未读过的文献 |
| **Pass B 盲审员**（5 人） | 对 A 的问题卡 + 抽样 pass 卡独立复核 | **禁读** `passA/`、`confirmed/`、别人的结论 |
| **Arbiter**（1 人） | 对单方 issue 做盲审，决定是否达到“两个独立判断” | 禁读两轮结论；只看卡与原文 |

角色必须实名记录在 JSONL 的 `reviewer` 字段。不同 pass 的同一人不能复用同一份结论。

---

## 2. 抽样与批次

### 2.1 抽样

```bash
# 池：所有非 work.json 卡
# 固定种子；记录 git head 与池哈希
python datasets/_audit/third_party_2026-11-26/tools/sample_cards.py --seed 20261126 --n 100
```

要求：

- 池子必须是**运行时的实际文件列表**，不是 README 里的旧数字。
- 记录 `git_head`、`pool_size`、`pool_sha256`、`generated_at`。
- 样本清单同时产出 `sample.json`（机器）与 `sample.md`（人读）；每行含 `# / group / set / type / status / id / path`。
- 分组前再 `shuffle` 一次，避免按目录聚集；每组 20 张。
- 抽中 `draft` 卡也要审；不能因为状态低就跳过。

### 2.2 批次

- 5 个 A 组 ×20 张；5 个 B 组轮转（B1→B、B2→C、B3→D、B4→E、B5→A）。
- B 轮不是“重审全部 20 张”，而是：**A 的全部 issue 卡 + 最多 6 张随机 pass 卡 + 必要时补 unverifiable**，打乱顺序。
- B 轮清单只给卡片路径与编号，**不给 A 的结论**。

---

## 3. 证据等级与来源规则

### 3.1 等级

| 等级 | 来源 | 用法 |
|---|---|---|
| **E1 一手** | 原书 PDF / arXiv / 出版社 / 作者讲义 | 可直接定错；引文必须逐字 |
| **E2 权威二手** | nLab、Stacks Project、标准教材、MathOverflow 高赞但需交叉 | 可作强佐证；与 E1 冲突时以 E1 为准 |
| **E3 卡内推导** | 卡自身公式/定义/前后文 | 可证内部不一致；不能单独证外部事实 |
| **E4 记忆/直觉** | 模型记忆、网络摘要、博客、Wikipedia | **不能作证据**，只能作“去查什么”的线索 |

### 3.2 页码

- 必须同时记 **PDF 页** 与 **印刷页**（或明确写“PDF 页 = 印刷页 + offset”）。
- 卡里的 `pages` 通常指印刷页；`pdf_pages` 指 PDF 页；`anchor` 要写清用的是哪一种。
- 不确定时不要写具体页码；写 `§x.y` + 定理/公式号，并在 `notes` 说明未核到页。

### 3.3 引文

- `quote` 必须逐字；允许省略用 `…`，但不得改写、不得把转述放进引号。
- 引文语言与原文一致；翻译放 `problem` / `should_be`，不要混进 `quote`。
- 每条 issue 至少一个可定位证据：`source` + `entry` + `page/§` + `quote`。

### 3.4 禁止

- 禁止编造 URL、DOI、arXiv 编号、页码、引文。
- 禁止用 Wikipedia / 博客 / 内容农场 / 模型记忆作为最终依据。
- 禁止把“底本本身有错/中译有错”直接算成“卡错”；先判断卡是否忠实于底本，再判断底本问题。
- 禁止把“另一种合法约定”判成错；卡内部自洽即可，除非它与所引原文冲突。

---

## 4. 逐卡检查清单

按字段顺序过一遍；每张卡至少 3 条 `checks`，且必须覆盖 `definition/theorem`、`sources`、`internal` 三类。

### 4.1 `definition` / `notation`

- [ ] 量词与范围：`∃/∀`、`F`-分裂、proper/closed、非阿基米德/阿基米德。
- [ ] 假设是否被弱化或漏掉（最常见错误）。
- [ ] 记号是否与卡内公式、`sources.quote` 一致。
- [ ] 是否把“必要条件”写成“等价”，把“充分”写成“当且仅当”。

### 4.2 `theorems[]`

- [ ] 条件、结论、方向、逆命题、等号成立情形。
- [ ] 定理/命题/引理/定义的**层级**是否与原文一致（定理不能写成猜想）。
- [ ] `proof.status`（`sketch` / `gap` / `complete`）是否诚实。
- [ ] `gap_note` 是否把“构造未给出”与“同构性未验证”分开。

### 4.3 `formulas[]`

- [ ] 符号、系数、归一化（`Tr`、`κ`、`2π`、`1/2`）。
- [ ] 指标（上/下、bar、手征性、`GL_n` vs `GL_2`）。
- [ ] 乘积/求和、局部/整体、`∏_i` vs `∑_i`。
- [ ] 公式与 `summary` / `pitfalls` 是否自相矛盾。

### 4.4 `sources[]`

- [ ] `book` 的作者/版本/年份是否正确。
- [ ] `section` 是否精确到小节；`pages` 是否覆盖所引定理的**证明**。
- [ ] `anchor` 是否能在本地源码/PDF 中解析。
- [ ] `quote` 是否逐字、是否与 `card_says` 对得上。
- [ ] 页码偏移是否正确（PDF vs 印刷）。

### 4.5 内部一致性

- [ ] `summary` 与 `definition` 是否同一方向（单向/等价）。
- [ ] `key_points` 是否把“已证”与“猜想”混在一起。
- [ ] `pitfalls` 是否把正确写法标成错误（会把读者教反）。
- [ ] `aliases` / `related` / `verification` 是否残留旧结论。

### 4.6 JSON 层

- [ ] `json.load` 成功；无 U+0000–U+001F 控制字符（`\b`、`\v`、`\f` 是常见暗坑）。
- [ ] LaTeX 反斜杠在 JSON 中双写；不要手写单反斜杠。
- [ ] 缩进/键序保持仓库规范；不要整文件重排。

---

## 5. 判定与 schema

### 5.1 verdict

- `pass`：核过，未发现可核实错误。
- `issue`：至少一个可核实错误；必须带 `issues[]`。
- `unverifiable`：关键 source 缺失/无法访问，且不能靠卡内推导判定；必须写 `unverifiable_aspects[]`。

`confidence`：`high` / `medium` / `low`；低置信度不能单独作为 confirmed 依据。

### 5.2 severity

- `critical`：结论反了、定义恒真/恒假、核心公式符号错，会让下游数学整体失效。
- `major`：定理条件/方向/关键因子错，或重要出处错到无法定位。
- `minor`：页码、节号、笔误、术语、非核心 locator；不影响主结论。

### 5.3 issue 对象

```json
{
  "severity": "major",
  "aspect": "公式（符号）",
  "field": "formulas[1]",
  "card_says": "卡上原句（逐字）",
  "problem": "为什么错；与哪条原文冲突",
  "should_be": "建议改法；可给多个选项",
  "evidence": [
    {"kind": "pdf", "ref": "book.pdf PDF p.61 / 印刷 p.61, eq (6.15)",
     "quote": "逐字原文"}
  ],
  "suggested_fix": "可选：最小编辑文本"
}
```

### 5.4 每卡 JSONL

一行一卡，字段至少：

```json
{"n": 1, "group": "A", "reviewer": "A1", "pass": "A",
 "set": "gtgl15", "id": "gtgl15/concept/...", "path": "datasets/...json",
 "verdict": "issue", "confidence": "high",
 "checks": ["definition: ...", "sources: ...", "internal: ..."],
 "issues": [], "unverifiable_aspects": [], "notes": ""}
```

`checks` 至少 3 条；`verdict=issue` 时 `issues` 非空；`verdict=pass` 时 `issues` 必须为空。

---

## 6. 双盲、对照与仲裁

```text
Pass A (5×20)
   ↓ 只传 issue 卡 + 抽样 pass 卡，打乱
Pass B (5 组轮转，盲审)
   ↓
compare:
   both_issue      → 可确认（仍需 lead 复核证据）
   a_issue_only    → 进仲裁
   b_issue_only    → 进仲裁
   both_clear      → 通过
   clear_unverifiable → 记录，不修
```

规则：

- **两个独立审计员都判 issue**：满足确认门槛；lead 复核证据成立后修。
- **单方 issue**：必须由第三名 arbiter 盲审；arbiter 也判 issue 才确认；arbiter 判 pass 则**保留为单方发现，不修**。
- 仲裁员不得读 A/B 的结论；只看卡、原文、必要的外部文献。
- 分歧记录在 `compare.md` / `tiebreak/T1.jsonl`，不能只留一句“有争议”。

---

## 7. 修复规范

### 7.1 只修什么

- 只修 **confirmed** 的卡；单方未仲裁的卡不动。
- 对 confirmed 卡，可修“两轮中任一方指出、且 lead 复核成立”的子项；不要求每个子项都被两人分别指出。
- 不修：风格、解释性措辞、自洽约定、纯格式、未复现的怀疑。

### 7.2 怎么修

1. 先读 `casebook` 中同卡/同字段案例，确认不是“改回去”。
2. 用脚本做**字段级**替换，每条带 `old` 断言；不要手改整段。
3. 一次只改一个语义单元；改完立刻 `json.load`。
4. 保留原 JSON 的键序与缩进风格；用 `json.dumps(ensure_ascii=False, indent=2) + "\n"`。
5. 不重排数组、不改无关字段、不批量格式化。
6. 每处写进 `fix_log.json`：`field / before / after`。

### 7.3 改完必做

```bash
# 1) 目标卡 JSON 解析
python - <<'PY'
import json, pathlib
for p in [...]: json.load(open(p, encoding="utf-8"))
PY

# 2) 全量解析（1,676 张）+ 字段级 after 核验
python datasets/_audit/third_party_2026-11-26/tools/verify_final.py

# 3) 只应看到预期文件
git diff --stat -- datasets
git diff --check

# 4) 案例库完整
python 11_card_audit/tools/check_casebook.py
```

### 7.4 禁止

- 禁止 `git checkout/reset/clean/stash` 清理工作树；禁止顺手格式化无关卡。
- 禁止在没有 `old` 断言的情况下批量替换。
- 禁止把“修完”当“验完”；必须回读 after 值。
- 禁止把已修内容再改回旧写法；若确有新证据，先更新 casebook 并写裁决。

---

## 8. 工作日志与案例库

每次审计/修卡都必须留下：

```text
11_card_audit/
  logs/<date>/
    TRACE.md            # 时间线、角色、关键裁决
    raw/                # 原始 JSONL、compare、fix_log、report
  casebook/
    <id>.md             # 每张修过的卡一例
    index.json
```

`TRACE.md` 记录“谁在何时判了什么、依据哪一页”，不是私有思维链。案例必须含：

1. 错误版本（逐字）；
2. 正确版本（逐字）；
3. 证据锚点（PDF/印刷页、引文）；
4. 审计轨迹（A/B/arbiter）；
5. **失效模式推断**（明确标“推断”，不是模型自述）；
6. 对形式化/Lean 的提示；
7. 防再犯检查。

---

## 9. 防回归

- 改卡前先搜 `casebook/`：同 `id`、同字段、同失效模式。
- 同一张卡第二次修改时，必须在案例里追加“第二次修改”段落，说明为什么第一次没改对。
- 任何“页码/符号/归一化”改动，必须同时检查 `summary`、`formulas`、`pitfalls`、`sources` 四处。
- 任何“定义”改动，必须检查量词与 `notation`。
- 每次批次结束跑：
  - `check_casebook.py`
  - 全量 JSON 解析
  - `git diff --check`
  - 只改预期文件的白名单检查

---

## 10. 快速模板

- 新案例：[`templates/CASE_TEMPLATE.md`](templates/CASE_TEMPLATE.md)
- 校对清单：[`templates/CHECKLIST.md`](templates/CHECKLIST.md)
- 单卡记录：[`templates/REVIEW_RECORD_TEMPLATE.jsonl`](templates/REVIEW_RECORD_TEMPLATE.jsonl)

### 一句话版本

> **先抽样、再双盲；先证据、再判定；两人都判才修；最小改、逐条记；改完回读、建案例、防回归。**
