# S1–S4 数据整改日志（schema 归一 + 4 条内容修正）

> archivist｜2026-11-13｜task-24｜依据：`seminar/CHARTER.md` §5（行 138–153）与 verifier 复审意见。
> 范围：`sessions/s{1,2,3,4}/claims.jsonl`、`sessions/s{1,2,3,4}/questions.jsonl`。未动 transcript/score/reports/教材核查。

## 0. 枚举依据（CHARTER 原文）

- **type** ∈ `definition | conjecture | evidence | interpretation | open`（§5 行 144）。
- **source** ∈ `witten | reconstruction | post-1990`（§5 行 145）。
- **status** ∈ **`active | contested | refuted`**（§5 行 146：「status ∈ active | contested | refuted」）。此前 checker 里额外放的 `accepted/confirmed/provisional/downgraded/retired` 不是章程枚举，本轮全部归一。
- **confidence**：CHARTER §5 只给示例 `0.85`、未列枚举；按 Lead 本轮指令统一为 `high | medium | low`（与 `check_claims.py:27` 的 `CONFIDENCE` 一致）。
- **session** 小写 `s1..s4`（原本已合规，0 改动）。
- **questions.status** 原为 `open`（合法），0 改动。

## 1. 机械归一（status）

| 文件 | 旧值 | 新值 | 条数 | 依据 |
|---|---|---|---|---|
| s1/claims.jsonl | accepted | active | 11 | CHARTER §5 行 146 |
| s1/claims.jsonl | provisional | active | 1 | 同上（章程无 provisional；见 §4 待判 ①） |
| s1/claims.jsonl | downgraded | contested | 1 | 同上（见 §4 待判 ②） |
| s2/claims.jsonl | confirmed | active | 10 | 同上 |
| s2/claims.jsonl | provisional | active | 2 | 同上 |
| s3/claims.jsonl | confirmed | active | 11 | 同上 |
| s3/claims.jsonl | provisional | active | 1 | 同上 |
| s4/claims.jsonl | active | active | 11 | 已合规，0 改动 |

合计：status 改动 **37 条**（s1 13、s2 12、s3 12、s4 0）。type/source/confidence/session 均为 0 改动（原本已合法）。

## 2. 内容修正（4 条）

### 2.1 c-s1-04（s1/claims.jsonl）——「全篇」不成立
- 旧：`…摘要（p.351）四句的动词是 is shown / … / shed，全篇无 prove、demonstrate、establish。`
- 新：`…摘要内无 prove、demonstrate、establish（grep text/page-01..03.txt：0 命中；全文则有 proved/proof 共 10 处，如 p.373、p.391，故不能说「全篇无」）。`
- 新 anchors：`原文 p.351`、`witten1989/text/page-01.txt L10–16`、`grep text/page-01..03.txt: prove|demonstrate|establish = 0；p.373/p.391 有 proved/proof`。
- 依据（grep 实测）：`text/page-01..03.txt` 中 prove/demonstrate/establish = **0**；但全文 text 层 `prove` 1、`proved` 5、`proof` 4（p.373「Moore and Seiberg have proved」、p.379「to prove」、p.380「has been proved」、p.386「new proof」、p.391「proved by Moore and Seiberg」「new proof」）。故「摘要内 0」成立、「全篇 0」不成立。

### 2.2 c-s3-07（s3/claims.jsonl）——删「Witten 明说」
- 旧：`…做 metaplectic 修正才等价于 L_λ→L_{λ+ρ}。Witten 明说不做半形式，故 λ 不位移。`
- 新：`…做 metaplectic 修正才等价于 L_λ→L_{λ+ρ}。本文未引入半形式修正；此判断来自译本批注 witten.tex:1206–1208 [译注]。`
- 字段：`source=reconstruction`（原已如此）、`status=active`（原 provisional，按 §1 归一）、`confidence=medium`。
- 新 anchor：`witten.tex:1206–1208（% [Tutor Note]，[译注]）`。
- 依据：`deliver/witten.tex` 全文 `half-form` 仅 **1** 处，在 `witten.tex:1206` 的 `% [Tutor Note]` 里（「严格量子化还需半形式（half-form，$K^{1/2}$）修正……Witten 在本节略去了半形式修正」），是译本批注不是原文；正文 p.369 只用 `L^{⊗k}`，无半形式构造。

### 2.3 c-s4-08（s4/claims.jsonl）——三处页锚全改
- 旧 anchors：`[src p.394]`、`[src p.396]`、`[src p.397]`；旧文：「p.394 词典级、p.396 定理级（借 Segal [39]）、p.397 纲领级」。
- 新 anchors：`[src p.396]`、`[src p.397]`；新文：`§5 的措辞分三层…p.396 用 "can be interpreted as"（解释级，且该页无 [39]）；p.397 引 Segal [39]，说 LG/G 的辛量化给出圈群的基本不可约最高权表示（引定理级，限 genus 0 与基本表示）；p.397 末 "It is obvious at this point…" 是纲领级。`
- 依据（页图）：`pages/page-46.png` = 印刷 396，§5 标题起于本页，原句是 *"the physical Hilbert spaces obtained by quantization in 2+1 dimensions **can be interpreted as** the spaces of conformal blocks in 1+1 dimensions"*；本页引的是 Segal [16]，**无 [39]**。`pages/page-47.png` = 印刷 397，原文 *"according to Segal [39], the quantization of LG/G, with this symplectic structure, gives rise to the basic irreducible highest weight representation of the loop group"*；同页末 *"It is obvious at this point that…we can generate the whole 1+1 dimensional conformal field theory"*。
- 附：p.394 不是 §5（§5 标题在 p.396 页图），原锚点 `p.394` 作废。

### 2.4 c-s4-09（s4/claims.jsonl）——p.396→p.397
- 旧：`原文最强的数学断言在 p.396：按 Segal，把辛结构量子化 LG/G 得圈群基本不可约最高权表示；归功于 [39]。` anchors `[src p.396]`。
- 新：`原文最强的数学断言在 p.397（不在 p.396）：按 Segal [39]，把 LG/G 的辛结构量子化给出圈群的基本不可约最高权表示；该断言归功于 [39]，本文只引用未证明。` anchors `[src p.397]`。
- 依据：同 2.3 的 `pages/page-47.png`（印刷 397）原句；p.396 页图上无 [39]。

## 3. 校验结果

- 8 个 JSONL：`json.loads` 全部通过（逐行）。
- 枚举自检：type/source/confidence/status/session 违例 **0**。
- `check_claims.py <project_root>`：claims 60 条、questions 29 条，**「通过：0 个错误」**（exit 0；0 WARN，因为 status 已全在章程集合内）。

## 4. 需人判的两处（映射丢了语义）

① `provisional → active`（4 条：c-s1-12、c-s2-03、c-s2-10、c-s3-07）：章程无「暂定」档，`active` 只表示「未被驳倒」。若 verifier 要求保留「未终审」信息，只能进 `counterpoints` 或另立字段——本轮未擅自加字段。
② `downgraded → contested`（1 条：c-s1-13，G3 的「H_Σ 有限维」降为论证）：`contested` 表示「有争议」，与该条「本场降级」的语义最接近；若评审认为应记 `refuted` 或 `active`，改 1 行即可。
