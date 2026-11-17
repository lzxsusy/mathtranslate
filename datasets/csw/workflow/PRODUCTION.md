# csw 资料卡生产流程（PRODUCTION v1）

本文件回答三件事：**队伍怎么构造**、**每张卡怎么过闸**、**怎么复现**。

## 1. 队伍怎么构造

资料卡是本仓库 `papers/WIT-1989-JONES` 研讨班的产物，沿用同一套五角色编制（Lead + 4）：

| 角色 | 负责什么 | 不做什么 | 产物 |
| --- | --- | --- | --- |
| **Lead**（主席） | 定 track 与卡清单、切分任务、裁决分歧、集成与入库 | 不替角色写卡；不自己给分 | `taxonomy.md`、`index.jsonl`、README、最终 push |
| **historian** | 语境与问题史：这张卡在原文哪一节、为什么需要它、1988 年知道什么 | 不做文献计量 | `sources`、`definition`、`pitfalls` 里的历史坑 |
| **bibliographer** | 文献与交叉核对：同一结论在河野/上野/Moore/Schottenloher 的页码与归一化 | 不写成“综述” | `key_points`、`formulas`、归一化换算 |
| **archivist**（证据官） | 锚点抽检：每张卡的 `sources` 是否可核对、页图/tex 行号是否对得上 | 不改卡的内容方向 | 抽检表（pass/fail + 证据） |
| **verifier** | 独立评分：只读 claims/卡，不读起草过程；按四维打分，一条 fabricated 即不及格 | 不参与写作 | 评分与整改清单 |

**任务板**：一次生产 = 一个批次（本批 40 张）。Lead 建 task，写清“只写哪些文件、验收标准、卡数”；每人只碰自己的文件（`tools/_dataN.py` 与 `md/` 由 build 脚本生成，不手改）。完成后在群里回三行：产物、卡数、lint 结果。

**为什么这样分**：卡的价值在“可核对”。写作、找证据、打分三种动机必须分开，否则“自己写自己夸”。上一轮研讨班的教训（S1 58/100、S2 61/100）就是引文与页锚没有独立复核。

## 2. 每张卡怎么过闸

```
起草（historian/bibliographer）
   ↓  tools/build_cards.py 生成 JSON
闸 1  结构：lint_csw.py 0 error、0 warning
   ↓
闸 2  证据：archivist 抽 3 条 sources 对页图/tex 行号（fail → 退回）
   ↓
闸 3  内容：verifier 抽 3 张卡，读 `definition`/`theorems`，任一条与 sources 不符 → 退回
   ↓
入库：status 从 draft → reviewed（Lead 改），index.jsonl 重建，commit
```

硬规矩（与研讨班 CHARTER 一致）：

1. **锚点优先**：任何实质断言必须有 `sources`；找不到锚点的句子只能进 `pitfalls` 或删掉。
2. **原文说 / 我们补 / 后世**三分：`proof.status=sketch` 必须写 `gap_note` 说明“本文没证、谁补的”。
3. **归一化必须声明**：$k$ 的归一化、$\operatorname{Tr}$ 的表示、$q$ 的定义，三处任一不明就不算过闸。
4. **不编造**：引文必须逐字可查；译本里的“断言”不能回译成原文的 “assert”。
5. **一票否决**：任一条 fabricated（引用不存在、页码错、把猜想写成定理），整批退回。

## 3. 批次卡清单（本批）

- 概念卡 31：O1 + A3 + B4 + C6 + D4 + E6 + F2 + G4 + H1（见 `taxonomy.md`）
- 例子卡 9：`abelian-torus-dimension`、`su2-torus-theta`、`su2-k2-s-matrix`、`s3-normalization`、`pillowcase-dimension`、`bwb-su2`、`kz-two-point`、`level-shift-check`、`trefoil-jones`

## 4. 复现

```bash
cd datasets/csw
python tools/build_cards.py    # tools/_data1..5.py → cards/*.json + index.jsonl
python tools/lint_csw.py       # 0 error / 0 warning
python tools/render_md.py      # cards → md/
python tools/gen_docs.py       # taxonomy.md + MAP.md
```

数据源是 `tools/_data1.py … _data5.py`（Python 字面量，`DATA=[...]`）。改卡 = 改数据 + 重跑四步；**不要直接改 `cards/` 或 `md/`**，下次 build 会覆盖。

## 5. 纠错

发现错误：记一条「卡 id + 错在哪 + 证据（页图/tex 行号）+ 正确说法」，交 Lead 派给证据官复核；确认后改 `_dataN.py`、重跑、commit，并在提交信息里写 `fix(csw): <id> ...`。历史批次的问题不删除，只追加 `pitfalls` 或修订字段，保留可追溯性。

## 6. 与讲义/研讨班的关系

- 讲义 `deliverables/lecture/main.pdf` 给**连续叙事**；资料卡给**原子断言**。
- 注疏本 `deliverables/reading_note/main.pdf` 给**逐节对照**（G-x/D-x 编号）。
- 研讨班 `sessions/s1..s6` 的 claims.jsonl 是卡的“前身”；卡是 claims 的“可复用版”（去掉场次上下文、补 related 与 sources）。
