# 全书锚点复核报告（task-29）

日期：2026-11-13　复核人：archivist（证据官）
复核对象：`papers/WIT-1989-JONES/sessions/s1..s6` 的 `claims.jsonl` / `questions.jsonl`
工具：`deliverables/engineering/scripts/check_anchors.py`、`check_claims.py`，另加独立脚本 `_arch/anchor_audit.py`
**未改动任何 session 数据与别人正文**；问题只在本报告点名。

## 1. 官方检查器结果

```
python deliverables/engineering/scripts/check_anchors.py <项目根> \
  --tex "C:\Users\admin\Documents\deepseek-harness\default-workspace\witten1989\deliver\witten.tex"
python deliverables/engineering/scripts/check_claims.py <项目根>
```

| 检查 | 统计 | 结果 |
|---|---|---|
| check_anchors | `\tag` 108 个（1.1–1.6, 2.1–2.33, 3.1–3.6, 4.1–4.60, 5.1–5.3），实际核对 20 处 | **0 错误**，exit 0 |
| check_claims | claims 73（s1 13 / s2 12 / s3 12 / s4 11 / s5 12 / s6 13），questions 35（6/6/6/5/6/6） | **0 错误**，exit 0 |

“0 错误”只覆盖检查器认得的写法（见 §4 盲区），不等于全部锚点已核。

## 2. 独立复核（`_arch/anchor_audit.py`）

| 项目 | 数量 | 结果 |
|---|---|---|
| claims+questions 中的锚点条目 | 148（Witten 型 96，教材/后世 52） | 全部可解析 |
| 页引用（`p.N` / `p.N–M`） | 103 | **全部落在 351–399** |
| 公式引用（`eq x.y` / `(x.y)`） | 34 | **全部在 108 个 `\tag` 之内** |
| claim status | s1 12 active + 1 contested；s2/s3/s4/s6 全 active；**s5 11 accepted + 1 provisional** | s5 不合 CHARTER |
| question status | 35 条全 open | 合规 |

## 3. 不一致清单（点名，未改）

| # | 位置 | 现状 | 应为 | 依据 |
|---|---|---|---|---|
| 1 | `sessions/s5/claims.jsonl` 全 12 条 | `status` = accepted（11）/ provisional（1） | active / active（或按语义 contested） | `seminar/CHARTER.md:146`：`status ∈ active \| contested \| refuted`；s1–s4 已于 task-24 归一 |
| 2 | `sessions/s5/claims.jsonl:8`（c-s5-08） | 锚 `[上野 p.103 (5.29)(5.30)]` | `[上野 p.111 (5.29)(5.30)]` | `cft_gauge/src/b12.tex:570`「矩阵 $(S_{\lambda,\mu})$ 称为 S-矩阵」@书 p.111；(5.29)(5.30) 同页区；p.103 属 §5.3 |
| 3 | `sessions/s2/claims.jsonl:10`（c-s2-10） | 锚 `[src p.385–388 §4.3]` | `[src p.384–387 §4.3]` | `s04-canonical.tex` §4.3 起于 p.384；p.388 页首已是 §4.5（`page-34`=384，`page-38`=388） |
| 4 | `sessions/s6/claims.jsonl:7`（c-s6-07） | 锚 `[原文 p.351--399 全体]` | 具体页，或降级为 `open` | 全区间锚点不可核对；check_claims 只查区间端点 |

## 4. 检查器盲区（这次没被“0 错误”覆盖的部分）

1. `check_anchors.py` 只认方括号 `[eq x.y]`；s1 中裸露的 `eq 1.2/1.3/1.6/4.21/4.41` 与 s6 的 `[eq 3.5 p.373]`（带页后缀）都未被检查。
2. `check_claims.py` 只核对以 `[src` / `[原文` 开头的页锚；s1 中裸露的 `原文 p.N`（12 条）未核。
3. **全部教材页锚未核**：`[河野 p.N]`、`[上野 §x.y]`、`[Moore p.N]`、`[Schottenloher p.N]`、`[李思 p.N]` 一条都没进检查器；只能靠证据官人工抽检（S1–S6 已抽 5+3+3+3+3+3 条，均 pass，除本报告第 3 节第 2 条）。
4. `check_claims.py` 对未知 `status` 只 WARN 不报错，所以 s5 的旧枚举可以藏过校验。

## 5. 建议（交给 Lead 决定，我没有改）

1. 把 s5 的 12 条 status 归一（与 task-24 相同规则：accepted/confirmed/provisional→active，downgraded→contested）。
2. 修正第 3 节 #2、#3、#4 三处锚点；#4 建议同时补一条具体页。
3. 把 s1 的裸 `eq …` 与裸 `原文 p.N` 改成 `[eq x.y]` / `[src p.N]` 形式，让检查器真正覆盖。
4. 教材页锚建议另加一张“教材锚点抽检表”（S1–S6 已抽到的 pass 记录可复用），否则“0 错误”对外说服力不足。

## 6. 附：本次复核顺带确认的页锚

- Witten 正文：`\tag{3.1}` p.367、`\tag{3.4}` p.371、`\tag{3.5}` p.373、`\tag{3.6}` p.374、`\tag{4.28}` p.386、`\tag{4.36}` p.388、`\tag{4.51}` p.393；《证明 Verlinde 猜想》小标题 p.391。
- §5 起于 p.396（“can be interpreted as”），Segal [39] 引文在 p.397。
- 河野：Verlinde 命题 1.22 p.37；定理 2.16 是 Dehn 手术/Witten 不变量 p.60–61。
- 上野：$S$ 矩阵 p.111；Verlinde 定理 5.21–5.22、例 5.23 p.111–115；反常移位 p.125。
