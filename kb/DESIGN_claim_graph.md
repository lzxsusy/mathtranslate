# 数译断言图谱（SCG）设计书 v1.0

> 状态：草案，待主人审阅后冻结为 v1.0
> 日期：2026-11-24
> 读者：明天要在本仓库里干活的 Agent（A/B/C）、以及维护 `dsh-kb` 插件的人
> 关联文件：`kb/README.md`（现有知识库）、`04_playbook/01_数学文献翻译纪律.md`（来源分级）、`04_playbook/17_仓库理念与上传规范.md`（目录与权利）、`08_source_code/SY02-31_*/资料卡/`（首个试点语料）

---

## 0. 这份文档是什么

这是一份**要照着施工**的设计书，不是愿景稿。它回答四件事：

1. 我们要做一个什么东西，解决谁的什么问题（第 1–3 节）；
2. 它内部由哪些实体构成，接口长什么样（第 5–6 节）；
3. 怎么从**现在已经有的**卡片、FTS、译文、源码里把它编译出来（第 7–8 节）；
4. 怎么判断它到底有没有用，以及明天谁先做哪一块（第 9–12 节）。

它不包含：具体代码实现（由 ticket 落地）、界面上怎么摆按钮（插件侧自理）、任何出版社 PDF 的分发（R3 禁止，见 §8.7）。

---

## 1. 问题

### 1.1 现象（来自真实使用，不是假想）

让别的 Agent 用现在的 `dsh-kb` 插件翻译数学文献，反馈集中为三条：

1. **「占用了搜索资源」**：查一次返回一大段原文，agent 还得自己再读一遍，综合成本高于直接上网搜。
2. **「想找某定理怎么证，关键词搜不出来」**：搜「几何 Stark 等价」，回来一堆同名提及（引言里提一句、文献综述里提一句），没有一条是陈述或证明。
3. **「没有分级」**：定义、定理、猜想、举例、文献提及，返回时混在一起，agent 无法判断哪条能当依据。

这三条都不是「搜索算法不够好」，而是**索引单位选错了**。

### 1.2 诊断：索引单位错，不是排序错

LeanSearch 论文在 50 条「非形式地问定理」的查询上给出了一组硬数字（[arXiv 2403.13310](https://ar5iv.labs.arxiv.org/html/2403.13310)）：

| 检索方式 | nDCG@20 | R@10 |
|---|---|---|
| BM25（关键词） | **0.024** | **0.030** |
| 纯向量（形式化语料） | 0.593 | 0.687 |
| 向量 + 非形式陈述库 + 查询增强 | **0.733** | **0.913** |

关键词检索在「用一个概念去问一条定理」时召回率 3%。这意味着：**我们现在这一层（卡片 + FTS）在最常见的数学查询上，结构性地不可能好用。** 不是调参能救的。

再叠加两条工程事实：

- 上下文越长召回越差（[context rot](https://research.trychroma.com/context-rot)），而 agent 的上下文预算有限，噪音是有价格的；
- 检索器太弱会让 agent 学会**不用它**（[Search-R1 类实证](https://ar5iv.labs.arxiv.org/html/2505.15117)）——这正是「它宁愿上网搜」的机制。

反过来，Cursor 的语义检索 A/B 提升 12.5%（[Cursor 博客](https://cursor.com/zh-Hant/blog/semsearch)），但它的索引单位是**代码块**——一个自足的语义单元。启示不是「上向量」，而是**先选对单元**。

### 1.3 需求清单

| 编号 | 需求 | 优先级 | 验收信号 |
|---|---|---|---|
| R1 | agent 能用**自然语言描述**找到一条**具体断言**（不是一段原文） | 必须有 | 30 题金标 P@1 ≥ 0.8 |
| R2 | 能回答「这条定理怎么证」，给出**证明骨架与前件** | 必须有 | 证明找到率 ≥ 0.7 |
| R3 | 能回答「这个概念我们译成什么、为什么」 | 必须有 | 决策命中率 ≥ 0.9 |
| R4 | 能比较**同一结果在不同书里的版本**（强弱、条件、记号） | 应该有 | 变体题 P@1 ≥ 0.7 |
| R5 | **覆盖不到就明说**，不倾倒原文 | 必须有 | drowning rate ≤ 0.15 |
| R6 | 每条返回都**可回溯**：作品、印刷页、源文件行、原文、译文 | 必须有 | 引用有效率 = 1.0 |
| R7 | 能从**现有资产自动编译**，人只裁冲突 | 必须有 | 单作品编译 ≤ 10 分钟，人工裁决 ≤ 20 条/书 |
| R8 | 与现有插件**兼容灰度**：老工具不坏，新工具可控 | 应该有 | 双写期两套工具并存 |

### 1.4 成功的定义（三句话）

1. 一个正在翻译的 agent，遇到「这条定理的前提到底是什么」时，**一次调用、≤800 token** 就能拿到带页码的答案；
2. 一个读者问「这本书里几何 Stark 等价是怎么证的」，拿到的是一条**证明链**，而不是二十条提及；
3. 覆盖不到时，它收到的是**一句「未覆盖」加三条最近线索**，而不是五千字原文。

---

## 2. 目标与非目标

**目标（v1）**

- 把「断言」而非「文档/段落」变成一等检索单元；
- 把「证明依赖」变成可查询的边；
- 把「翻译与校对时的判断」变成可复用的决策条目；
- 用**意图路由 + 硬预算 + 拒答**替代「一个大搜索框」。

**非目标（明确不做，防止摊大饼）**

- 不做全文语义搜索的替代品（原文层保留现状，只作为 L4 兜底）；
- 不做自动形式化（Lean 对齐卡保持 `status: g`，不假装 certified）；
- 不做社区/多人协作/上传入口；
- 不做出版社 PDF 的托管与分发（R3）；
- 不做手工本体（Cyc 的教训，见 §13）。

---

## 3. 使用者与最短路径

| 使用者 | 典型问题 | 最短路径 | 期望 token |
|---|---|---|---|
| 翻译中的 Agent | 「这个术语我们怎么译」「这句话里的 X 是不是漏了条件」 | `kb_resolve` / `kb_statement` | ≤300 |
| 校对中的 Agent | 「命题 5.3.37 的假设有几条，原文页码」 | `kb_statement` + `kb_proof` | ≤600 |
| 写导读/心得的 Agent | 「这一篇的主结果有哪几条，依赖什么」 | `kb_packet`（篇章级） | ≤1500 |
| 读者/问答 | 「几何 Stark 等价是什么，怎么证」 | `kb_resolve` → `kb_proof` | ≤800 |

关键点：**同一份数据，四种预算。** 接口按意图给不同粒度，而不是让调用者自己截断。

---

## 4. 设计原则

- **P1 断言是一等公民。** 段落、页、文件都是断言的出处，不是检索单位。
- **P2 载荷而非指针。** 返回的就是可读的陈述/骨架，不是「请去第 204 页看」（[ISC 的核心主张](https://arxiv.org/abs/2608.20845)）。
- **P3 变体不合并。** 同一结果在不同书里强弱不同，合并即造假；做法是「变体簇 + 一条 canonical」。
- **P4 宁缺毋滥。** 覆盖不到就拒答并给最近线索；drowning 是比 miss 更重的错误。
- **P5 出处即契约。** 无页码/无原文/无 confidence 的条目不许入库。
- **P6 策展寄生在翻译流水线上。** 人工只做裁决，不做录入（Cyc 教训）。
- **P7 可评测才算完成。** 没有基线数字的功能不上线（§9）。

---

## 5. 领域模型

### 5.1 五类实体

| 实体 | 一句话 | 主要来源 |
|---|---|---|
| **Claim（断言）** | 一条可独立陈述的数学命题/定义/猜想/例子 | LaTeX 定理环境 + `statements.tsv` |
| **Proof（证明）** | 一条证明的骨架与步骤，指向 Claim | chunk 内 `proof` 环境、`\ref` |
| **Variant（变体边）** | 两书/两处讲同一件事的关系（等价/更强/更弱/特例/记号不同） | 人工裁决 + 卡片 + 摘要比对 |
| **Decision（决策）** | 一次翻译/体例判断：触发条件、选择、理由、证据、适用范围 | glossary、`\tn`、疑点清单、资料卡 04 |
| **Work（作品）** | 一本书/一篇讲义的元数据与页映射 | `投稿信息.md`、`BRIEF.md` |

### 5.2 Claim 记录

| 字段 | 类型 | 说明 |
|---|---|---|
| `claim_id` | string | `SC:<work>:<编号>`，编号用**印刷页编号**（如 `SC:SY02-31:5.1.5`）；无编号用 `p<页>-<序>` |
| `work` / `chapter` | string | 作品号、篇号 |
| `type` | enum | `def/thm/prop/lem/cor/conj/ex/rem/notn/hyp/fact/ques/claim` |
| `label_orig` | string | 原文编号（`5.1.5`），必须逐字 |
| `stmt_zh` | string | 中文规范陈述：一句，可脱离上下文读懂 |
| `stmt_en` | string | 原文陈述逐字（可截断到 600 字，截断处标记） |
| `hypotheses` | string[] | 假设逐条（可空） |
| `conclusion` | string | 结论（尽量短，可公式） |
| `proof_state` | enum | `none/sketch/full/page`（L1–L4 的粗分） |
| `proof_ref` | string? | 指向 `proof_id` |
| `anchors` | object | `{pdf_page, print_page, chunk, line}` 四元组，全部必填（PDF 页可由 print+13 推，但仍显式写出） |
| `sources` | string[] | `\tn` 中引用的 A/B 级来源（可空） |
| `status` | enum | `canonical/variant/conjecture/unverified/disputed` |
| `confidence` | number | 0–1，抽取器给初值，人可改 |
| `aliases` | string[] | 别名/英文名/旧译名，供召回 |
| `variant_of` | string? | 若有更强/更一般版本，指向那条 |
| `created_by` | string | `extractor@v0.1` 或裁决人名 |

> `stmt_zh` 的生成规则：**只允许改写，不允许补全**。原文没说的条件不许加；改写后必须能逐句对回 `stmt_en` 的片段。对不上就标 `unverified`。

### 5.3 Proof 记录

| 字段 | 说明 |
|---|---|
| `proof_id` | `PF:<work>:<claim 编号>` |
| `claim_id` | 它证的是哪条 |
| `skeleton` | 3–7 步的骨架（每步一句：用了什么 → 得到什么） |
| `premises` | 用到的 Claim ID 列表（来自 `\ref` 与正文点名） |
| `external` | 用到但库外/未入库的结果（写成「[EGA III] 7.8.6 这类」） |
| `anchors` | 证明起止的 chunk:line 与印刷页 |
| `depth` | `sketch / full` |

### 5.4 Variant 边

`{from, to, relation, note}`，`relation ∈ {equivalent, stronger, weaker, special_case, generalization, notation_differs, reproves}`。
**单向存两次**：每条边写正反两条记录，避免查询时漏。

### 5.5 Decision 记录

| 字段 | 说明 |
|---|---|
| `decision_id` | `DC:<scope>:<序号>` |
| `trigger` | 什么情况下会用到（术语/句式/体例/文献处理） |
| `choice` | 我们选了什么（一句话） |
| `alternatives` | 被否掉的选项，以及为什么 |
| `reason` | 理由（可引用纪律条款） |
| `evidence` | 来源与级别（A/B/I/上下文推断） |
| `scope` | 适用范围（全书 / 某篇 / 某类对象） |
| `counters` | `{adopted, overridden}` 使用计数（ACE 的条目化做法） |

### 5.6 ID 规则与稳定性

- ID 一经发布**永不改变**；原文改版导致编号变化时，旧 ID 保留并标 `superseded_by`。
- 不以文件路径、行号、hash 作 ID（会漂移）。
- 与 Stacks Project 的 tag 思路一致：**位置可动，ID 不动**。

---

## 6. 检索协议

### 6.1 意图路由

| 意图 | 工具 | 输入 | 返回 | 预算 |
|---|---|---|---|---|
| 这个词/概念是什么 | `kb_resolve` | 术语/别名/一句描述 | 1 条 canonical + ≤3 变体 + 指路表 | 400 |
| 这条定理怎么陈述 | `kb_statement` | 编号/名称/一句描述 | 1 条 canonical（含假设） | 500 |
| 怎么证 | `kb_proof` | claim_id 或编号 | L2 骨架 + premises + 可展开 L3 | 800 |
| 为什么这么译 | `kb_why` | 术语/句式/疑问 | 1 条 Decision + 证据 | 300 |
| 两处结果比较 | `kb_compare` | 两个 claim_id 或两书 | 差异表（记号/条件/强弱） | 600 |
| 这一块缺什么 | `kb_gaps` | 主题/篇 | 未解项列表（≤10） | 400 |
| 篇章级总览 | `kb_packet` | work + chapter | 主结果表 + 依赖摘要 | 1500 |

路由规则：**先解析实体（编号/术语/别名），再决定动词**；解析不到实体时退回「描述检索」，并把 `answer_state` 标为 `fuzzy`。

### 6.2 返回信封（所有工具统一）

```json
{
  "answer_state": "exact | variant | fuzzy | gap | stale | ambiguous",
  "intent": "proof",
  "claim_id": "SC:SY02-31:5.1.5",
  "type": "thm",
  "stmt_zh": "……",
  "hypotheses": ["……"],
  "proof_skeleton": ["……"],
  "premises": ["SC:SY02-31:4.2.7"],
  "anchors": {"print_page": 204, "pdf_page": 217, "chunk": "ch-a4-15.tex", "line": 312},
  "variants": [{"claim_id": "SC:SY02-25:2.11", "relation": "weaker", "note": "…"}],
  "sources": ["[来源：nLab \"…\"，2015-10-05；访问 2026-11-24]"],
  "confidence": 0.92,
  "tokens_estimate": 380,
  "next": ["kb_proof SC:SY02-31:4.2.7"]
}
```

`answer_state` 是**契约的一部分**：`gap` 表示「库里确实没有」，`fuzzy` 表示「有相近但不保证」，两者都不许返回长原文。

### 6.3 预算与拒答

- 每个工具声明 `max_tokens` 并**自我截断**；超预算时先砍变体，再砍来源，最后只留 `claim_id + 一句话 + 锚点`。
- 拒答模板（固定 3 行，≤120 token）：
  ```
  未覆盖：<查询>。最近的三条线索：
  1) SC:…（一句话，为什么近）
  2) …
  3) …
  建议：换成编号或术语再问一次，或让我查原文层。
  ```
- **不许多说一句**。多说是 drowning 的来源。

### 6.4 错误语义

| 状态 | 含义 | 调用者应做 |
|---|---|---|
| `exact` | 编号/术语唯一命中 | 直接用 |
| `variant` | 命中的是变体，canonical 在别处 | 看 `variants[0]` |
| `fuzzy` | 按描述匹配，未验证 | 用前核对锚点 |
| `gap` | 库内无覆盖 | 换查询或走原文层 |
| `stale` | 条目版本已过期 | 先看 `superseded_by` |
| `ambiguous` | 同名多条 | 用全文编号再查 |

---

## 7. 编译流水线（从现有资产出发）

### 7.1 我们现在已经有什么

| 资产 | 数量（SY02-31 实测） | 现状用途 |
|---|---|---|
| 编号陈述 | 802 条 | 只在 `资料卡/02-命题.tsv` 里，未进库 |
| 底表 | 679 条 | 只用于审计 |
| `\ysrc` 页锚 | 562 个 | 排版用 |
| `\label` | 840 个 | 交叉引用 |
| 术语 | 314 条 | `glossary.tsv`，只被人读 |
| 译注 `\tn` | 149 条 | 脚注，未被检索 |
| 疑点 | 55 条 | 清单文件，未被检索 |
| 资料卡 | 五件套 + 6 对齐卡 | 卡片层，粒度粗 |
| 原文/译文段落 | 7,644 / 48,595 | 兜底层 |

**结论：原料齐全，缺的是「编译」这一步。**

### 7.2 LaTeX → Claim 的映射规则

| 源记法 | 抽取为 |
|---|---|
| `\begin{thm}{5.1.5}…\end{thm}` | `type=thm`, `label_orig=5.1.5` |
| 环境内首个 `\label{thm:a4-…}` | 内部标签，用于连边 |
| 环境前最近的 `\ysrc{204}` | `anchors.print_page=204` |
| 环境内 `\tn{…}` | `sources` + 译注锚 |
| `\begin{proof}`…`\end{proof}` 且紧随某 claim | `Proof` 记录 |
| 证明内 `\ref{thm:…}` / 「由定理 4.2.7」 | `premises` |
| 跨片证明（a4-19/a4-20 式） | 用「前一片无 `\end{proof}`」规则合并，需人工确认 |

### 7.3 依赖边

- 一级：`\ref{}` 与 `\eqref{}`（确定）；
- 二级：正文点名（「由引理 5.3.10」），用正则 + 编号表匹配（较确定）；
- 三级：无显式引用但同段反复出现的名词（**不自动建边**，进人工队列）。

### 7.4 决策抽取

| 来源 | 抽成 | 例 |
|---|---|---|
| `glossary.tsv` 一行 | 1 条 Decision（trigger=术语） | `perfectoid → 完美胚`，理由「中文数论文献通行」 |
| `\tn{…}` | 1 条 Decision（trigger=疑点）或 1 条 Claim（若含数学内容） | 「底本此处印作 X，按上下文应为 Y」 |
| `疑点清单.tsv` | 1 条 Decision（带状态） | 未解项同时进 `kb_gaps` |
| `资料卡/04` | 1 条 Decision（体例类） | 「文献题名保留英文」 |
| `09_thinking` 精选片段 | 1 条 Decision（流程类） | 「并发上限 8」 |

### 7.5 什么必须人裁

1. `stmt_zh` 与 `stmt_en` 对不上（补全/漏条件嫌疑）；
2. 同一编号在两处内容不同（底本笔误 vs 我们抄错）；
3. 变体关系（等价/更强）——机器只能提候选；
4. `confidence < 0.6` 的任何条目；
5. 跨书 canonical 的指定。

裁决队列落 `kb/review/queue.jsonl`，每条带「机器建议 + 依据 + 两个选项」，人只点一下。

### 7.6 五道闸（编译期校验，不过闸不入库）

1. **Schema 闸**：字段齐全、类型正确（JSON Schema）。
2. **锚点闸**：`chunk` 文件存在、`line` 处确有该环境、`print_page` 与 `\ysrc` 一致。
3. **回链闸**：`stmt_zh` 能在 `stmt_en` 中找到对应片段（字符级重合 ≥ 0.4，或人工签字）。
4. **编号闸**：`label_orig` 与 `statements.tsv` 对得上；对不上进裁决。
5. **重复闸**：同 `work+label_orig` 不得两条 canonical。

---

## 8. 工程实现

### 8.1 目录

```
kb/
  DESIGN_claim_graph.md      # 本文档
  schema/
    claim.schema.json        # 新增
    proof.schema.json
    decision.schema.json
  build/
    extract_claims.py        # LaTeX → claims.jsonl
    extract_proofs.py
    extract_decisions.py
    link_refs.py
    validate.py              # 五道闸
    build_db.py              # → claimgraph.db
  claims/
    SY02-31.claims.jsonl     # 派生，可重建
  proofs/
  decisions/
  review/
    queue.jsonl
  eval/
    gold30.jsonl             # 30 题金标
    run_eval.py
    report.md
  claimgraph.db              # 生成物，.gitignore
```

原则：**源在 `08_source_code/`，派生物在 `kb/`，`claimgraph.db` 永远可重建。**

### 8.2 存储

- 主格式 JSONL（人可读、可 diff、可 code review）；
- SQLite 索引 `claimgraph.db`：
  - `claims(claim_id PK, work, chapter, type, label_orig, stmt_zh, stmt_en, status, confidence, anchors_json, …)`
  - `claims_fts`（unicode61，中英混排；CJK 另建 trigram 表）
  - `edges(src, dst, kind)`，`kind ∈ {premise, variant, supersedes}`
  - `decisions(decision_id PK, trigger, choice, scope, …)`
  - `query_log(ts, tool, q, answer_state, tokens, latency_ms)` —— **必留**，评测靠它
- 向量可选：`sqlite-vec` 可用则加一列 `embedding`，不可用则退化到 FTS + 别名。**v1 不强制依赖向量库。**

### 8.3 CLI

```bash
PY=.../python.exe
"$PY" kb/build/extract_claims.py --work SY02-31
"$PY" kb/build/link_refs.py --work SY02-31
"$PY" kb/build/validate.py --work SY02-31        # 不过闸则非零退出
"$PY" kb/build/build_db.py
"$PY" kb/q2.py resolve "几何 Stark 等价" --json
"$PY" kb/q2.py proof SC:SY02-31:5.1.5 --json
"$PY" kb/eval/run_eval.py --suite gold30
```

### 8.4 检索算法（三路召回 + 预算重排）

1. **精确路**：ID/编号/术语/别名精确匹配（优先级最高）；
2. **词汇路**：FTS5（中英混排 + trigram）；
3. **语义路**（可选）：对 `stmt_zh + stmt_en` 建向量，仅用于描述式查询；
4. **重排**：`score = 3.0*exact + 1.0*fts + 0.6*vec + 0.4*type_prior - 0.8*status_penalty`；
5. **预算裁剪**：按 `canonical → 变体 → 来源 → 原文摘句` 顺序填充，超预算即停。

`type_prior`：查询里出现「怎么证」时 `thm/prop/lem` 加分；出现「例子」时 `ex` 加分。

### 8.5 规模与性能

- 单作品 800 条 claim、~1,500 条边：SQLite 毫秒级；
- 全库按 50 部作品估：4 万 claim、8 万边，FTS 仍 <50 ms；
- 编译：单作品 <2 分钟（纯解析），全库 <30 分钟；
- 内存：不用向量时 <200 MB。

### 8.6 与现有插件的关系

- **不删旧层**：`kb_search / kb_card / kb_brief / kb_source / kb_zh` 原样保留（原文/译文兜底仍有用）。
- **新增动词层**：`kb_resolve / kb_statement / kb_proof / kb_why / kb_compare / kb_gaps / kb_packet`。
- **灰度**：先只对 `SY02-31` 打开新动词，其余作品返回 `gap` 并提示「该作品尚未编译」。
- **双写期**：`query_log` 同时记录新旧工具调用，用两周数据决定旧层去留。

### 8.7 权利与安全

- R3：书籍底本不发布成品 PDF；图谱只存**我们自己的译文**与**短引原文**（≤600 字），且 `stmt_en` 永不导出为整页文本。
- L4（禁入）作品的原文不得进 `src` 层。
- 全部只读工具，不提供写入/上传 verb。
- 输出必须带 `work + print_page`，便于人工回查。

---

## 9. 评测

### 9.1 借鉴的指标族

MathIngestBench（[Zenodo 21329350](https://zenodo.org/records/21329350)）把「摄入是否忠实」定义为：**可靠检索 + 改版时正确失效 + 下游推理提升且无虚假提升**，并给出 invalidation completeness、stale-serving、false-change rate 等指标。我们取其前两组，另加「预算」维度：

| 指标 | 定义 | 目标 |
|---|---|---|
| `P@1` | 第一条即正确答案的比例 | ≥ 0.80 |
| `proof_found` | 问「怎么证」时给出可用骨架的比例 | ≥ 0.70 |
| `drowning` | 返回中与问题无关内容占比 | ≤ 0.15 |
| `citation_valid` | 返回的锚点能回查到原文的比例 | = 1.00 |
| `tokens/answer` | 单次答案 token 中位数 | ≤ 800 |
| `false_promotion` | 把猜想/未验证当定理返回的比例 | ≤ 0.02 |
| `stale_served` | 改版后仍返回旧条目的比例 | = 0 |

### 9.2 30 题金标（构造规则）

四类各 7–8 题，全部来自真实使用场景，答案由人写死：

1. **术语/概念**（8）：如「完美胚」「参数叠」「钻石」；
2. **陈述/假设**（8）：给编号或一句描述，要回假设清单；
3. **证明/依赖**（7）：问某定理怎么证、用了什么；
4. **比较/缺口**（7）：两书同一结果、库里没有的主题。

每题记录：`query / intent / expected_claim_id / expected_proof_steps(可空) / must_not_include / max_tokens`。

### 9.3 消融（证明组件各自有用）

| 组 | 配置 | 预期 |
|---|---|---|
| A | 现状（卡片 + FTS） | 基线，P@1 应显著低 |
| B | + claim 层 | P@1 大涨 |
| C | + 证明边 | proof_found 从 0 到可用 |
| D | + 决策层 | 术语类题命中 |

**没有这四组数，不许对外说「变好了」。**

### 9.4 上线门槛

同时满足才发版：`P@1 ≥ 0.8`、`drowning ≤ 0.15`、`citation_valid = 1`、`false_promotion ≤ 0.02`，且 30 题里**不得有一题**返回「大段原文」。

---

## 10. 案例（用 SY02-31 的真实内容）

### C1 术语：几何 Stark 等价

- 现状：`kb_search` 返回 20 条提及（引言、综述、脚注），agent 读 3 分钟仍不知道定义在哪。
- 目标：`kb_resolve("几何 Stark 等价")` →
  ```
  exact  SC:SY02-31:1.2.3  def  「……（一句定义）」
  锚点：印 p.12 / PDF 25 / ch-a1-01.tex:118
  变体：SC:SY02-25:… （relation=special_case）
  指路：Dat §1.2（入门）→ FS §3（构造）→ Feng–Harris §8（母题版）
  tokens≈260
  ```
- 判据：≤400 token，第一条即定义，锚点可回查。

### C2 证明：定理 5.1.5 怎么证

- 现状：搜「5.1.5」得零条（编号不在卡片里）；搜主题得一堆同名。
- 目标：`kb_proof("SC:SY02-31:5.1.5")` → 5 步骨架 + 3 条 premises（含 ID）+ 「展开 L3」入口。
- 判据：骨架每步都能在 chunk 里定位；premises 至少 2 条正确。

### C3 决策：perfectoid 为什么译「完美胚」

- 现状：glossary 里只有一行，理由在 U02 报告里，agent 找不到。
- 目标：`kb_why("perfectoid")` → 选择 + 备选（保留英文）+ 理由（中文数论文献通行）+ 证据（nLab 条目、本库 I 级译法）+ 适用范围（正文；书名不译）。
- 判据：≤300 token，含「反例场景」（人名/书名保留原文）。

### C4 比较：Zhu 篇猜想 4.11 与 FS 定理 2.11

- 目标：`kb_compare` 返回差异表：条件（$\ell\neq p$ vs 任意）、结论强弱、记号差异、各自页码。
- 判据：不合并、不裁判谁对，只列差异。

### C5 校对：命题 5.3.37 的假设有几条

- 目标：`kb_statement` 逐条列假设（含「$P\subseteq \mathrm{GL}_d$ 抛物」「$\lambda$ 整」等），每条带页码。
- 判据：假设条数与原文一致；漏一条即失败——这是 A 级错误。

### C6 拒答：未覆盖的主题

- 查询：「Fargues–Fontaine 曲线上 shtuka 的稳定化」
- 目标：`gap` + 3 条最近线索（shtuka 定义、稳定化相关命题、相关篇目），≤120 token，**不返回任何原文段落**。
- 判据：token 上限与「零原文」是硬指标。

---

## 11. 路线图

| 阶段 | 产出 | 退出条件 | 估时 |
|---|---|---|---|
| **M0 盘点** | `kb/review/inventory.md`：现有卡/FTS/译文各能答什么 | 30 题基线跑完（组 A） | 0.5 天 |
| **M1 断言层** | `claims/SY02-31.claims.jsonl`（≈800 条）+ 校验通过 | 五道闸全绿；人裁 ≤20 条 | 1 天 |
| **M2 证明层** | `proofs/*.jsonl` + `edges`（premise） | 抽 20 条证明人工核对，骨架准确率 ≥0.8 | 1 天 |
| **M3 动词层** | 7 个工具 + 路由 + 预算 + 拒答 | 30 题 P@1 ≥0.6（先达标再优化） | 1 天 |
| **M4 决策层** | `decisions/*.jsonl`（≥300 条） | 术语类题命中 ≥0.9 | 0.5 天 |
| **M5 评测与灰度** | `eval/report.md` + 插件灰度 | §9.4 四组消融齐、门槛达标 | 1 天 |

M1–M3 可并行（M3 用 M1 的样例数据先跑通）。

---

## 12. 任务拆分（可直接派给 Agent）

> 通用约束：只写 `kb/` 下的派生物；不改 `08_source_code/` 的源文件；每个 ticket 一个 PR；PR 必须附 `validate.py` 输出。

| Ticket | 任务 | 输入 | 产出 | DoD |
|---|---|---|---|---|
| **T1** | 环境抽 claim | `08_source_code/SY02-31_*/源码/chunks/*.tex` | `claims/SY02-31.claims.jsonl` | 条数与 `statements.tsv` 差 ≤2%；字段齐全 |
| **T2** | 锚点回填 | T1 输出 + `\ysrc` 表 | 同上（补 `anchors`） | 抽 30 条核对页码，全对 |
| **T3** | 证明骨架 | `proof` 环境 + `\ref` | `proofs/*.jsonl`、`edges` | 20 条人工核对 ≥16 条可用 |
| **T4** | 决策抽取 | glossary / `\tn` / 疑点 / 资料卡 04 | `decisions/*.jsonl` | ≥300 条，每条有 evidence |
| **T5** | Schema 与校验 | 三份 schema | `validate.py` 五闸 | 故意造 5 条坏数据，全部拦下 |
| **T6** | 建库与 FTS | T1–T4 产物 | `claimgraph.db` | 冷建 <2 min；查询 <50 ms |
| **T7** | 路由器 | 7 动词协议 | `q2.py` + 路由表 | 30 题各归对意图 |
| **T8** | 预算与拒答 | §6.3 | 截断器 + 拒答模板 | 超预算时只留 3 行；gap 零原文 |
| **T9** | MCP 包装 | `q2.py` | `dsh-kb` 新工具 | 工具名/参数与 §6.1 一致 |
| **T10** | 金标 30 题 | 真实使用日志 | `eval/gold30.jsonl` | 四类齐、答案人写、含 `must_not_include` |
| **T11** | 评测脚本 | 金标 + 工具 | `run_eval.py` + `report.md` | 输出 §9.1 全部指标 |
| **T12** | 消融报告 | A/B/C/D 四组 | `report.md` §消融 | 四组数齐，结论可复核 |

依赖：T1→T2→T3；T4 独立；T5 依赖 T1/T3/T4 的 schema 定稿；T6 依赖 T1–T4；T7/T8 依赖 T6 的样例数据；T10 可与 T1 并行；T11 依赖 T7/T8/T10；T12 最后。

---

## 13. 风险与反面模式

| 风险 | 后果 | 对策 |
|---|---|---|
| 抽取错误被当权威 | 比没有更糟 | confidence + 锚点 + 五道闸 + `unverified` 状态 |
| 过度合并变体 | 强弱不分，误导证明复用 | P3：变体不合并，只连边 |
| 手工建本体 | Cyc 式崩塌 | P6：只裁决，不录入 |
| 大而全重写上下文 | context collapse（ACE 实测 18,282→122 token） | 条目化 + 增量 delta，不整体重写 |
| 优化塌成通用话 | brevity bias | 保留具体条目与数字，禁止「概括成一句」 |
| 又一个搜索框 | BM25 0.024 的命运 | 意图路由 + 硬预算 + 拒答 |
| 索引漂移 | 页码/行号变化导致引用失效 | ID 稳定 + `superseded_by` + 改版重编译 |
| 评测自嗨 | 指标好看但 agent 不用 | 以 `query_log` 真实调用为准，金标来自真实问题 |
| 权利越界 | 下架风险 | R3/L4 + 只存短引 + 不导出整页 |
| 工具膨胀 | agent 不知道调哪个 | 7 个动词封顶；其余走 `kb_packet` |

---

## 14. 开放问题（等主人定）

1. `stmt_zh` 允许 LLM 生成吗？（我倾向：允许改写，禁止补全；对不上就 `unverified`）
2. 是否引入向量依赖（`sqlite-vec`）？v1 我建议**不引入**，先证明 claim 层本身有效。
3. 决策层是否随插件开源？涉及我们的译法偏好，可只开源 schema、闭源内容。
4. 多书冲突时谁能定 canonical？建议：主人一票，其余按「最完整/最新」规则。
5. 金标 30 题由谁出？建议：从 `query_log` 与真实翻译卡点里选，主人签字。

---

## 附录 A · Claim JSON Schema（节选）

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Claim",
  "type": "object",
  "required": ["claim_id","work","type","label_orig","stmt_zh","stmt_en","anchors","status","confidence"],
  "properties": {
    "claim_id": {"type": "string", "pattern": "^SC:[A-Z0-9-]+:.+$"},
    "work": {"type": "string"},
    "chapter": {"type": "integer"},
    "type": {"enum": ["def","thm","prop","lem","cor","conj","ex","rem","notn","hyp","fact","ques","claim"]},
    "label_orig": {"type": "string"},
    "stmt_zh": {"type": "string", "minLength": 8},
    "stmt_en": {"type": "string", "maxLength": 600},
    "hypotheses": {"type": "array", "items": {"type": "string"}},
    "conclusion": {"type": "string"},
    "proof_state": {"enum": ["none","sketch","full","page"]},
    "anchors": {
      "type": "object",
      "required": ["print_page","pdf_page","chunk","line"],
      "properties": {
        "print_page": {"type": "integer"},
        "pdf_page": {"type": "integer"},
        "chunk": {"type": "string"},
        "line": {"type": "integer"}
      }
    },
    "status": {"enum": ["canonical","variant","conjecture","unverified","disputed"]},
    "confidence": {"type": "number", "minimum": 0, "maximum": 1},
    "aliases": {"type": "array", "items": {"type": "string"}},
    "variant_of": {"type": ["string","null"]}
  }
}
```

## 附录 B · 返回示例（`kb_resolve`）

```json
{
  "answer_state": "exact",
  "intent": "resolve",
  "claim_id": "SC:SY02-31:1.2.3",
  "type": "def",
  "stmt_zh": "设 $F$ 为 $p$-进局部域……称满足（i）（ii）的配对为几何 Stark 配对。",
  "anchors": {"print_page": 12, "pdf_page": 25, "chunk": "ch-a1-01.tex", "line": 118},
  "variants": [{"claim_id": "SC:SY02-25:2.11", "relation": "special_case"}],
  "guide": [{"work": "SY02-31", "chapter": 1, "depth": "L1", "note": "定义在此"}],
  "confidence": 0.9,
  "tokens_estimate": 260,
  "next": ["kb_proof SC:SY02-31:1.2.3"]
}
```

## 附录 C · 用词

- **断言（claim）**：一条能独立陈述的数学内容，含定义、定理、猜想、例子等。
- **canonical**：同一结果在本库中被指定为主版本的那一条。
- **变体（variant）**：与 canonical 讲同一件事但在条件/强弱/记号上不同的条目。
- **决策（decision）**：翻译或体例上的一次判断，含理由与证据。
- **拒答（gap）**：库内无覆盖时返回的固定短回复。
