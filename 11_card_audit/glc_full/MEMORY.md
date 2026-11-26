# 工程备忘录（MEMORY）：GLC 154 卡全量审计

> 这份文件是给**下一轮审计/下一个 agent** 看的工程记忆，不是审计报告本身。
> 云端 Hindsight 记忆库在本机未配置 API token（`~/.hindsight/coding-agent.json` 不存在，POST 返回 401），
> 因此把「应该被记住的东西」落在仓库里，保证换会话也能直接接上。

## 1. 这是什么

2026-11-26 对 `datasets/glc/cards/**/*.json` 全部 **154 张** `concept` 卡做**全量**（非抽样）独立审计：
Pass A（8 人 × 17–20 张）→ Pass B（52 张盲审）→ 单方发现交第三名 arbiter 盲审 → lead 逐条复核 → 22 张卡最小修复 → 51 处外部核验；用户 m01466 追加 nLab/文献补核后 3 张单方卡再修 → 25 卡 56 处发布。

- 主报告：`raw/report.md`（审计全过程、逐卡修复表、验收、残余风险）
- 外部核验：`raw/EXTERNAL_VERIFICATION.md`（56 处逐条 before/after、原书页、arXiv 一手、nLab/CAG 2001 follow-up）
- 过程：`TRACE.md`（时间线、命令、决策 D1–D13、8 条返工）
- 逐卡对比：`casebook/`（25 例，七节）＋`index.json`

## 2. 定稿数字

| 项 | 数 |
|---|---|
| A | 154 行，127 pass / 27 issue（29 条） |
| B | 52 行（27 张 A-issue + 25 张随机 A-pass，seed 20261126），15 issue |
| 对照 | both_issue 15 / a_issue_only 12 / both_pass 25 / b_not_sampled 102 |
| arbiter | 12 行，8 issue（7 张与 A 同字段确认）/ 4 pass |
| 确认修复 | **25 卡 / 56 处**（15 both + 7 arbiter 同字段 + 3 单方经 E1/E2 补核） |
| severity | 26 minor + 1 major（`vanishing-theorem`） |
| 单方未修 | 5 张 |
| unverifiable | 0 |
| 外部核验 | 56/56 通过，0 推翻 |

## 3. 关键修正（数学/术语）

- **major `vanishing-theorem`**：`key_points[1]` 原称一般形式「不再要求 k<n 且 E 几何不可约」。`rank(E)>k` 就是 `k<n`（同条件改写）；原书 p.36 Thm 5.7.2 与 Gaitsgory arXiv:math/0204081 Conj 1.3 都仍要求几何不可约 → 删括注。
- `perverse-quotient-lemma` summary 漏 `π_!K` 反常前提（原书 p.47：`π! K, π∗ K ∈ Perv(B)`）。
- `base-whittaker-sheaf` summary 把「限制到 `C_k^{tor=0}`」写成「茎」（原书 p.37：`Av_E^d(W_k)|_{C_k^{tor=0}}`）。
- `eisenstein-compatibility`：图 (16.1) 实为 p.77；`Casselman–Schalika`→`Shalika`。
- `b-lambda-ic`、`local-laumon-formula`：`Casselman–Shalala`→`Casselman–Shalika`（CCF24 arXiv:2409.07051 TeX + 原书 p.76）。
- `restricted-local-systems`：verification 旧判词残留（AGKRRV arXiv:2010.01906：QLisse = IndLisse 左完备化），verdict `contradicted`→`confirmed`。
- 其余 38 处为页码/定理出处定位修正。

## 4. 未解决（下一轮直接从这里接手）

1. **102 张 A-pass 卡没有 B 第二判断**（方案取舍，不是遗漏）。
2. **`extension-stack-vanishing`**：pages [40]，anchor 含 §7.5 收尾（p.43）；按「pages 覆盖主对象」口径未改，收紧口径时应改 [40,43]。
3. **三条外部复核仍认为成立、但 arbiter 判 pass 的单方发现**（按协议未修，建议单方发现二审）：
   - `deligne-gl1-existence`：`Shv(Spec k)` 的系数域应为 e（原书 p.7「algebraically closed coefficient field e」），卡写 k。
   - `hecke-laumon-stack`：`key_points[0]`「三者互相决定其中之二」不成立；(M′,T) 只定扩充类 `Ext¹(T,M′) ≅ ⊕_x((T_x)^∨⊗M′_x)`。
   - `local-whittaker-eigenfunction`：`key_points[4]` 在 λ_n=0（如 λ=(1,0,0)）时 n(λ)=0，指数为 0 而非负；`verification.checks[2]` 还引错了 FGKV98 的 P_n^+ 定义。
4. **底本源码缺陷未修**（任务禁止改译注工程）：`ch11.tex` 缺 `\srcpage{60}`、`ch12.tex` 缺 `\srcpage{64}`、`ch15.tex:65` §15.4 标题但 `\srcpage{74}` 在 :77、`ch16.tex:2` 注释「原PDF第75页」错（`:12 \srcpage{76}` 对）、PDF 目录对 §15.4 后与 ch16 不可靠。
5. **KL85 原文未取到**（PDF 下载两次超时），故 `fourier-deligne-transform` 的 why 行按 E3（卡内一致性）处理，不声称外部命题支撑。

## 5. 可复用约定（血泪版）

- `apply_fixes.py`：`old` 必须逐字匹配当前值；`substring` 模式要求恰好出现一次；必须带足 TeX 边界（前导 `$`、括号）。曾把 `"$t$-正合…"` 换成 `"$…"` 留下坏公式，靠 `git checkout --` 卡+md 复原。
- 卡与 `datasets/glc/md/concepts/<slug>.md` **必须同步改**；md 是手工渲染副本，pages 在 md 里是 `p.6（PDF p.6）`（不是 `[6]`），多页用 ASCII `-` 连接。
- `compare.py` 必须把「B 未抽到」单列为 `b_not_sampled`，不能算 unverifiable。
- `show_card.py <slug>` 前缀匹配会歧义（`vanishing-theorem` 命中 `averaging-vanishing-theorem`），歧义时直接读 JSON。
- casebook 只收**已确认并修复**的案例；单方未修只进报告，别把未确认判断固化成案例。
- 页码以 PDF 正文页首句/页眉为准，`\srcpage` 与 PDF 目录只作线索。
- 外部来源只用 E1 原书 PDF / E2 arXiv 一手；Wikipedia、博客、内容农场、模型记忆不可作证据。
- `verify_final.py` 是最终闸门：154 卡 / 1676 库 / `git diff --numstat -- datasets/glc` 范围 / `diff --check` / HEAD / fix_log sha256 / md 同步。

## 6. 发布

- 提交：`7d79721e`（22 卡 51 处 + 归档）、`bfffe0cc`（TRACE 补记）。
- 已 push：AtomGit `master:main`、Gitee `master`（均快进 6a488d50→bfffe0cc）。
- GitHub 远端存在但落后 58 个提交，本批未推（日常流程只走 AtomGit + Gitee）。
- 工作副本 `datasets/_audit/glc_full_2026-11-26/`（含讲义 PDF、逐页文本、审计包）**不入库**，版权与体积理由。
