# 自然语言 ↔ 形式语言对齐规范（STYLE_FORMAL.md）

> 本文件管「把一条已经译成中文的数学陈述变成一条可机器校验的对齐卡」这件事。
> 它是仓库未来的重心：页数是库存，**对齐卡才是产能**。现有落地试点是 `datasets/leanstmt/`
> （39 卡：21 certified + 18 gap）；本文件把该试点的实践固化成规范，供后续所有工程套用。

## 0. 为什么这一层值得做

中文数学语料的现状是：译文能读，但机器读不懂。词典层面已有 1,820 条术语、76 条记号，
但它们只能回答「这个词怎么译」，不能回答「这句话在说什么」。形式化陈述层要回答的是后者：
给定一条中文陈述，写出它的 Lean 4 命题，并让编译器判定它是否成立（或有条件地成立）。
这带来三件此前做不到的事：

1. **陈述级检索**：可以按「结论形态」而不是按「关键词」检索中文数学文献。
2. **错误定位**：陈述翻译错，Lean 会报错；这是目前唯一能自动发现「译错了数学」的机制。
3. **术语收敛**：一条陈述只能用一个译名，对齐卡本身就是术语裁决的机器证据。

## 1. 四层对齐（L1–L4）

| 层 | 对齐什么 | 产物 | 验收 |
|---|---|---|---|
| **L1 术语** | 中文术语 ↔ Lean 定义名 | `TERMS.tsv` 的 `术语ID` + 对齐卡的 `lean.name` 前缀 | 每个进卡的术语都能在 `TERMS.tsv` 查到且唯一 |
| **L2 陈述** | 中文陈述 ↔ Lean `Prop` | `cards/statements/*.json` 的 `lean.statement` | `lean` 编译通过；`#check` 类型符合预期 |
| **L3 证明** | 中文论证 ↔ Lean 证明项 | 同名 `.lean` 文件的 `theorem ... := by ...` | 无 `sorry`；或 `sorry` 全部登记为 gap |
| **L4 反例** | 原文的反例/边界条件 ↔ Lean 反例 | `type: "counterexample"` 的卡 | 反例可编译且确实否定对应陈述 |

本仓库当前只做 L1 + L2（陈述层），L3 只在 21 条 certified 里出现，L4 尚未开始。
**不要跳过 L1 直接做 L2**：术语没对齐的陈述，形式化后无法与译文互查，等于白做。

## 2. 对齐卡 schema

一张卡 = 一个 JSON 文件，路径 `datasets/<数据集>/cards/statements/<track>-<s|g><NN>.json`。
`s` 表示 statement（已认证），`g` 表示 gap（陈述已写出但依赖缺失或证明未完成）。

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `id` | string | ✓ | `<数据集>/<文件名去扩展>`，如 `leanstmt/gno1977-s01` |
| `type` | string | ✓ | `statement` / `counterexample` / `definition` |
| `title` | string | ✓ | 一行中文标题，用于索引与人工浏览 |
| `track` | string | ✓ | 底本缩写，如 `GNO77` / `W15` / `W08` |
| `source.paper` | string | ✓ | 底本标题（与 `RELEASE_REGISTER.csv` 一致） |
| `source.arxiv` | string | | arXiv 号，无则省略 |
| `source.section` | string | ✓ | 章节号或节标题 |
| `source.pages` | [int,int] | ✓ | 原书页码区间（**必须是页面图像上印的页码**） |
| `source.anchor` | string | ✓ | 该陈述在底本里的编号（`Theorem 3.2`）或首句片段，用于人工复核定位 |
| `natural_language.zh` | string | ✓ | 中文陈述一句话，术语用 `TERMS.tsv` 的译名 |
| `natural_language.en` | string | ✓ | 英文陈述，优先照抄底本原句；改写须在 `notes` 说明 |
| `lean.file` | string | ✓ | 相对 `datasets/<集>/lean/` 的路径 |
| `lean.name` | string | ✓ | 完全限定名（含 namespace） |
| `lean.statement` | string | ✓ | 命题本体（可含 `∀`、`→`），不含证明 |
| `lean.imports` | [string] | ✓ | **只列直接依赖**的模块，不写 `Mathlib` 全量 |
| `dependencies` | [{name,module,kind}] | | 该陈述用到的上游定义/定理；`kind` ∈ `def/theorem/instance` |
| `hypotheses` | [string] | ✓ | 陈述的显式前提，每条一句话；与 `lean.statement` 的 `→` 前件一一对应 |
| `scope` | string | ✓ | 当前只有 `discrete-core`（离散核心：不依赖大量几何基础设施） |
| `backtranslation.zh` | string | ✓ | 由 Lean 陈述**盲翻**回中文的结果，用于核对语义 |
| `backtranslation.method` | string | ✓ | 固定 `blind-backtranslation` |
| `backtranslation.reviewer` | string | ✓ | 复核者（人或 agent 名） |
| `verification.status` | enum | ✓ | `certified` / `gap` |
| `verification.toolchain` | string | ✓ | 如 `leanprover/lean4:v4.36.0` |
| `verification.lean_version` | string | ✓ | `lean --version` 输出 |
| `verification.mathlib_rev` | string | ✓ | mathlib commit 全哈希 |
| `verification.checked_at` | string | ✓ | `YYYY-MM-DD` |
| `verification.checker` | string | ✓ | 谁跑的编译 |
| `verification.sorry_count` | int | ✓ | 该卡对应证明项里的 `sorry` 数；`certified` 必须为 0 |
| `gaps` | [string] | | 缺失依赖清单，见 §6 |
| `notes` | string | | 与底本的出入、术语选择理由 |
| `rights` | string | ✓ | 固定 `rewritten`（改写，不复制原文） |
| `status` | string | ✓ | 卡的生命周期：`dev` / `reviewed` / `published`；**与 `verification.status` 是两个轴** |

`index.jsonl` 每行是一张卡的摘要：`id,title,track,scope,section,pages,lean_name,lean_file,verification,sorry_count,mathlib_rev`。
改卡必须同步改 `index.jsonl`（`tools/build_align_index.py` 将负责重建，现阶段手工）。

### 示例（截断自真实卡）

```json
{
  "id": "leanstmt/gno1977-s01",
  "type": "statement",
  "title": "单值化：紧黎曼面的万有覆叠是单连通的",
  "track": "GNO77",
  "source": {"paper": "Grauert–Remmert 等", "section": "§2", "pages": [12, 12],
             "anchor": "Theorem 2.1"},
  "natural_language": {"zh": "紧黎曼面的万有覆叠空间是单连通的。",
                       "en": "The universal covering of a compact Riemann surface is simply connected."},
  "lean": {"file": "GNO77/S01.lean", "name": "GNO77.universalCover_simplyConnected",
           "statement": "∀ (X : Type*) [TopologicalSpace X] [CompactSpace X] ..., SimplyConnectedSpace ...",
           "imports": ["Mathlib.Topology.AlgebraicTopology.FundamentalGroup"]},
  "hypotheses": ["X 是紧黎曼面", "覆叠取万有覆叠"],
  "scope": "discrete-core",
  "verification": {"status": "certified", "toolchain": "leanprover/lean4:v4.36.0",
                   "mathlib_rev": "d33c49ca43873d3746194325da62640cc893c9d9",
                   "checked_at": "2026-11-19", "sorry_count": 0},
  "rights": "rewritten", "status": "dev"
}
```

## 3. 陈述从哪里来

**不要从译文正文里随机摘句。** 陈述的第一来源是资料卡的 `01-结果清单.md` 与 `03-条款索引.md`：

- `01-结果清单.md` 已经按「定理 / 命题」分表，每行带编号、陈述要点、前提/位置、作用、原文页码；
  一行 = 一张卡的候选。
- `03-条款索引.md` 的定义条目对应 `type: "definition"` 的卡（L1 术语层）。
- 只有资料卡缺失的工程，才从译文的 `\begin{theorem}` 环境抽，且必须回页面图像核对页码。

抽取时做四件事：

1. **显式化量词与前提**：底本写「设 $X$ 是紧的」，Lean 里必须出现 `[CompactSpace X]`；
   底本省略的「$X$ 非空」也要补，并记进 `hypotheses`。
2. **拆开复合陈述**：一句话里有「且」「等价于」的，拆成多张卡，`id` 递增。
3. **保留编号**：`source.anchor` 写底本编号；中文标题不写编号（编号会随版本变）。
4. **不改数学**：翻译成 Lean 时允许换等价写法，不允许加强或减弱条件；
   若必须减弱（mathlib 缺定义），把卡标 `gap` 并在 `gaps` 写清减弱了什么。

## 4. Lean 侧约定

- **namespace = track**：`GNO77`、`W15`、`W08`；文件名与之对应（`GNO77/S01.lean`）。
- **statement 与 proof 分离**：卡的 `lean.statement` 只放命题；证明在同名 `.lean` 里，
  形如 `theorem universalCover_simplyConnected : <statement> := by ...`。
- **命名**：`<小写驼峰的主体>_<性质>`，与 `lean.name` 末段一致；不译人名，用拉丁转写
  （`fukaya_category`、`atiyah_singer`）。
- **`sorry` 允许但必须记账**：`by sorry` 可以提交，但 `verification.sorry_count` 必须同步，
  且 `verification.status` 只能是 `gap`。`certified` 的卡 `sorry_count == 0`，这是机器可查的。
- **禁止 `axiom` / `admit`**；需要额外假设时写进 `hypotheses` 并作为 `lean.statement` 的前件。
- **imports 只列直接依赖**：`Mathlib` 全量导入会让编译时间失控；只列该陈述真正用到的模块。
- **toolchain 与 mathlib 固定**：卡里写死版本与 commit；升级时批量改并重跑，不允许「未记录版本」的卡。
- **类型类实例显式**：`[TopologicalSpace X]`、`[CompactSpace X]` 写在 `∀` 之后，
  不要依赖 `variable` 的隐式推断——隐式推断会让陈述在不同 mathlib 版本下含义漂移。

## 5. 反向翻译（blind back-translation）

每张 L2 卡都要做一次盲翻：只看 `lean.statement`，不看 `natural_language`，把命题写回中文，
填进 `backtranslation.zh`。然后三向核对：

1. 盲翻结果与底本原句是否同义（不是同词）；
2. 盲翻结果与 `natural_language.zh` 是否同义；
3. 若不同义，是翻译错（改 `zh`）还是形式化错（改 `statement`）。

盲翻的价值在于：**它只依赖 Lean 命题**，所以能抓出「中文写得对、Lean 写错」这类最难发现的错。
`backtranslation.reviewer` 必须填真实复核者，不得留空或填 `TODO`。

## 6. gap 类型（G1–G5）

`verification.status = gap` 时，`gaps` 里每条必须是下列之一 + 一句说明：

| 类型 | 含义 | 处理 |
|---|---|---|
| **G1 缺定义** | mathlib 没有该概念（如某些导出范畴构造） | 先补 `type: definition` 的卡，或改用等价刻画 |
| **G2 缺定理** | 定义有、关键引理没有 | 记录依赖名；该引理本身可以做卡 |
| **G3 版本漂移** | 陈述依赖 mathlib 某版本的行为 | 锁 commit；升级时重跑 |
| **G4 陈述歧义** | 底本本身含糊（「适当条件下」） | 拆成多张卡或写明所取解释 |
| **G5 证明未完成** | 陈述已写出，证明有 `sorry` | `sorry_count` 记账，后续补 |

`certified` 的判定标准只有一条：**编译通过且 `sorry_count == 0`**。人工觉得「应该对」不算。

## 7. 验收闸门

新卡入库前逐项过（`tools/check_align.py` 将把这套规则机械化，现阶段人工 + `ds_lint.py`）：

| 闸门 | 通过标准 |
|---|---|
| schema | 必填字段齐全；`id` 与文件名一致；`type`/`scope`/`rights`/`status` 在枚举内 |
| 唯一性 | `id` 全局唯一；`lean.name` 全局唯一 |
| 来源 | `source.pages` 的两个页码在底本页数范围内；`source.anchor` 能在页面图像找到 |
| 编译 | `lean.file` 存在；`lake build` 该文件通过（或 `sorry` 数与 `sorry_count` 一致） |
| 版本 | `toolchain`/`mathlib_rev` 与仓库 `lean-toolchain`、`lake-manifest.json` 一致 |
| 盲翻 | `backtranslation.zh` 非空且 `method` 为 `blind-backtranslation` |
| 术语 | `natural_language.zh` 里的术语能在 `TERMS.tsv` 查到（D 级不算） |
| 索引 | `index.jsonl` 有对应行且字段一致 |

## 8. 优先级

1. **先扩 certified，不铺面**：现有 21 条 certified 来自 GNO77 / W15 / W08 三批离散核心陈述。
   2026-Q1 目标 100 条 certified（不是 1,000 条草稿），集中在 `discrete-core`。
2. **资料卡齐备的工程先做**：SY01-25（Kontsevich–Soibelman，83 卡含 73 条款卡）与
   SY02-09、FUNCTORIALITY 三部既有术语表又有条款索引，是下一批 L2 的自然来源。
3. **做「陈述密集」的底本**：综述、讲义、会议录里的定理陈述密度高、依赖少，比专著更适合起步。
4. **不做的**：需要大量几何/层论基础设施才能陈述的（导出范畴、指标定理的解析部分），
   在 mathlib 补齐前只做 L1 术语卡，不做 L2。

## 9. 与数据集的关系

```
资料卡（人类可读）          01-结果清单.md / 03-条款索引.md
        │ 抽陈述
        ▼
对齐卡（机器可校验）        datasets/leanstmt/cards/statements/*.json  ← 本规范管这一层
        │ 索引
        ▼
statements.tsv（机器索引）  id / title / track / statement / status  （将随 check_align.py 生成）
        │ 编译
        ▼
Lean 4 文件                datasets/leanstmt/lean/<track>/<NN>.lean
```

对齐卡不是「另一种资料卡」，而是资料卡的**可执行子集**：资料卡可以写背景、动机、历史，
对齐卡只写能被 Lean 判定的那一句。两者共用同一个术语 ID 与同一组页码。
