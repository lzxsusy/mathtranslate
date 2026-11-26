# 审计轨迹 TRACE（glc 154 卡全量，2026-11-26）

本文件是 `datasets/_audit/glc_full_2026-11-26/` 的过程记录：时间线、命令、关键决策与返工。数字口径以该目录 `report.md` 与 `tmp/stats.json` 为准。

## 1. 时间线

| 时间（+08:00） | 事件 |
|---|---|
| 18:58 | 启动；读 `11_card_audit/WORKFLOW.md`、`AUDIT_HANDBOOK.md`、casebook `SHOWCASE.md`/`README.md`、`datasets/glc/README.md` 与 `datasets/README.md` glc 节 |
| 19:01 | 建基建：PDF 副本 + 逐页文本 `tmp/pages/pNNN.txt`；`make_inventory.py` 生成 154 卡清单与 A1–A8 分组；`build_packs.py` 生成 154 个审计包（卡 JSON + 源码切片 + 对应 PDF 页 + related 检查）；`check_audit.py`；`AUDITOR_BRIEF.md` |
| 19:02 | 启动 8 名 Pass A 审计员（A1–A8，17–20 张/人，cwd=仓库根） |
| 19:08–19:26 | A 各组陆续交卷，全部 checker 0 error；共 154 行、127 pass / 27 issue |
| 19:10–19:24 | lead 侧独立机械校验 `mech_checks.py`（PDF 目录页码 / 源码 `\label` 段区间 / 编号对象 / 正文页码），把 9 个 flag 逐一核到假阳性或真问题 |
| 19:20 | lead 把 27 张 A-issue 卡逐条亲核，写 `tmp/lead_verdicts.md`（27 行：卡 / 字段 / 亲核证据 / 判断），全部成立 |
| 19:26–19:28 | `make_passB_list.py --seed 20261126 --frac 0.2` → 52 张（27 A-issue + 25 随机 A-pass），分 B1/B2/B3；写 `PASSB_BRIEF.md` |
| 19:29 | 启动 3 名盲审 B（只给路径，禁读 A 的产物） |
| 19:34–19:42 | B3（17 行，2 卡 3 条）、B2（17 行，8 条）、B1（18 行，5 条）交卷，全部 0 error |
| 19:43 | `compare.py`（修正 `b_not_sampled` 分类）→ 15 both_issue / 12 a_issue_only / 25 both_pass / 102 未抽；`make_tiebreak.py` + `ARBITER_BRIEF.md` |
| 19:44 | 启动 arbiter-t1a / arbiter-t1b（各 6 张单方卡，盲审） |
| 19:52 | T1b：3 issue（fourier、restricted-categorical、local-whittaker 另一字段）/ 3 pass |
| 19:54 | T1a：5 issue（b-lambda-ic、perverse-quotient、shv-nilpotent、frobenius-twisted、local-laumon）/ 1 pass（hecke-laumon-stack） |
| 19:54–19:56 | 确认集 22 卡 51 处；`make_fix_plan.py` → `apply_fixes.py --apply`；`verify_final.py` ok |
| 19:56 | `finalize.py` → `issues.jsonl` 32 行；`tmp/stats.json`；`compare.md` 追加仲裁与最终确认节 |
| 19:57 | `make_casebook.py` → 22 例 + `index.json` + `casebook/README.md`；修 REPO 路径 bug |
| 20:00 | 本批文档：`report.md`、本 README、TRACE |
| 20:12 | 用户要求「外部核验 22 卡 51 处 + 推送工程与思考链」；`tools/reverify_pages.py` 独立重算 35 处定位编辑（21 处差异逐条归因到 `\srcpage` 漂移） |
| 20:16–20:24 | 外郭取 E1/E2 证据：Gaitsgory math/0204081（vanishing 条件）、CCF24 2409.07051 TeX（Casselman–Shalika）、AGKRRV 2010.01906 TeX（QLisse 左完备化）、原书逐页引文；写 `EXTERNAL_VERIFICATION.md`（51/51 通过，0 推翻） |
| 20:21–20:24 | 更新 `report.md` §8/§9/§10 与本文；审计工程复制为 `11_card_audit/glc_full/{raw,tools}/`；commit `7d79721e`；push AtomGit `master:main`、Gitee `master`（6a488d50..7d79721e） |
| 20:25–20:27 | 按 `09_thinking/README.md` 写 L2 链 `GLC-154-AUDIT-01`（6516 字符，九节）、登记 `index.csv`；写 `MEMORY.md`（Hindsight 401 无 token 的回退）；commit `c50e7c27`；再 push AtomGit/Gitee（bfffe0cc..c50e7c27） |
| 20:52–20:58 | 用户要求「对英文原本再核」：逐页重读 38 处定位、12 处内容、5 张单方卡；英文原本即 `glc.pdf`（85 页，sha256 f79cd79c…）；写 `EXTERNAL_VERIFICATION.md` §9（3 张单方被原书证实），更新 `report.md` §8/§9 |
| 21:00–21:12 | 用户 m01466 要求「先用 nLab/全网检索佐证，成立就修」：检索 nLab `l-adic cohomology`/`geometric class field theory`/`extension`、CAG 2001 的 Ext¹ 参数化、Casselman–Shalika 1980 与 BIRS/Chhaibi 讲义；三条判断均有 E1+E2 支持 |
| 21:12–21:20 | 写 `tmp/make_followup_plan.py` → `tmp/fix_plan_followup.json`（3 卡 5 处）；`apply_fixes.py --check` 通过；`--apply --log fix_log_followup.json` 写 3 卡 5 处，md 同步 |
| 21:30–21:38 | 写 §10 证据表、TRACE §7.5、案例 23–25；commit `83043f32`；push AtomGit `main`、Gitee `master`（a5a22926..83043f32） |
| 21:20–21:30 | 合并 `fix_log.json`（25 卡 56 处：`fixes` 22/51＋`followup` 3/5）；`issues.jsonl` 3 行改 `confirmed_fixed_followup`；更新 `report.md` §4.2/§5/§8/§9/§10、`EXTERNAL_VERIFICATION.md` §0/§10、README/MEMORY、案例 23–25 与 `index.json` |

## 2. 命令日志（关键步骤）

```bash
# 基建
python datasets/_audit/glc_full_2026-11-26/tools/make_inventory.py
python datasets/_audit/glc_full_2026-11-26/tools/build_packs.py
pdftotext -layout glc.pdf tmp/glc.txt   # 逐页 split 到 tmp/pages/
# 逐组自检（8 + 3 + 2 次）
python datasets/_audit/glc_full_2026-11-26/tools/check_audit.py \
  --file .../passA/A1.jsonl --group A1 --reviewer A1
python datasets/_audit/glc_full_2026-11-26/tools/check_audit.py \
  --file .../passB/B1.jsonl --list .../passB/groups/B1.txt --reviewer B1
# 机械交叉校验
python datasets/_audit/glc_full_2026-11-26/tools/mech_checks.py
# 对照与仲裁
python datasets/_audit/glc_full_2026-11-26/tools/compare.py
python datasets/_audit/glc_full_2026-11-26/tools/make_tiebreak.py
# 修复（幂等）
python datasets/_audit/glc_full_2026-11-26/tmp/make_fix_plan.py
python datasets/_audit/glc_full_2026-11-26/tools/apply_fixes.py --plan .../fix_plan.json --check
python datasets/_audit/glc_full_2026-11-26/tools/apply_fixes.py --plan .../fix_plan.json --apply
# 汇总与验收
python datasets/_audit/glc_full_2026-11-26/tools/finalize.py
python datasets/_audit/glc_full_2026-11-26/tools/make_casebook.py
python datasets/_audit/glc_full_2026-11-26/tools/verify_final.py
```

## 3. 决策日志

- **D1 分组按连续章块**（而非随机分卡）：同一章内 `nLab 相关记号、页码起点、编号风格一致，避免 8 名审计员对同一章的同类问题重复劳动或口径不一。
- **D2 页码偏移 = 0**：实测 `glc.pdf` p.11 页眉印 `11`，且该页正是 Conjecture 1.5.1；`sources.pages` 与 `pdf_pages` 160 条全部相等。故卡内页码可直接对 PDF 页文本。
- **D3 `\srcpage` 只作线索**：它会在段落中间、`\end{}` 之后、注中漂移（ch01:109、ch15:65↔:77、ch12:110↔:117），ch11/ch12 还缺 `\srcpage{60}`、`\srcpage{64}`；PDF 自带目录对 §15.4 之后与 ch16 也不可靠。**一律以 PDF 正文页眉/正文为准**。
- **D4 mech flag 不是错误检测器**：8 个 anchor_pages flag 中 7 个是「背景句/证明续页落在邻页」，按「pages 已覆盖主对象即不算错」处理；只有卡自己的定义/陈述越界才算错。
- **D5 卡自带 `verification` 不作证据**：只当线索，且本轮实际证出两处陈旧判词（`restricted-local-systems`、`local-whittaker-eigenfunction`）。
- **D6 B 只给路径、只抽 20%**：B 的样本 = 全部 A-issue（27）+ A-pass 随机 25（seed 20261126）。B 不读 A 的 JSONL、compare、issues、fix_plan 与 A 的笔记，三份 brief 各自声明禁读清单。
- **D7 arbiter 按字段比对**：arbiter 判 pass，或判 issue 但字段与 A 不同，都**不确认** A 的断言（`local-whittaker-eigenfunction` 即此例：arbiter 认的是 `verification.checks[2]`，A 指的是 `key_points[4]`）。
- **D8 卡与 md 同步**：`datasets/glc/md/concepts/<slug>.md` 是手工维护的渲染副本，只改 JSON 会制造新的不一致；`apply_fixes.py` 强制 md 同步，歧义时整体拒写。
- **D9 substring 编辑必须带足前后文**：`fourier-deligne-transform` 第一次替换只写了 `t$-正合…`，留下孤立的 `$`，产生坏公式；此后规定 old 必须包含完整 TeX 记号边界（前导 `$`、左括号等），并用 `--check` 先行验证。
- **D10 单方发现不入 casebook**：casebook 只收已确认并修复的 22 例；5 张单方未修只写进 `report.md` §5，避免把未确认的判断固化成「案例」。

## 4. 返工与事故记录

1. **`compare.py` 把 B 未抽到的卡误标 `unverifiable`**：加 `b_not_sampled` 分支后重跑，102 张归位。教训：盲审抽样下「未审 ≠ 无法核验」。
2. **`fourier-deligne-transform` 的 `$` 残留**（见 D9）：备份 → `git checkout --` 该卡与 md → 改 spec old/new → 重建 plan → 单卡 `--apply` → 合并回 22 卡 fix_log。
3. **`verify_final.py` 两个误判**：`after` 可能是列表（多页 pages）导致比较报错；md 检查误用「after 文本应出现在 md」而 md 只渲染 `p.N（PDF p.N）`。改为读 `md_sync.edits[].md_new`，并放行 `.verdict` 的 not_found（md 的「## 核验」不渲染 verdict）。
4. **`apply_fixes.py` md 歧义判据过严**：旧判法是「before 仍出现在最终 JSON 任何位置」，把 `p.63`→`p.63–64` 这类前缀重叠误判为歧义；改为「同文本出现在另一个字段」+「md 中出现 >1 次」。
5. **`make_casebook.py` 的 REPO 路径少一层**（`AUDIT/../..` 指到 `datasets/`）：已改 `../../..`，并删除误建的 `datasets/11_card_audit/`。
6. **checker 的 `pass` 只接受 A / B / arbiter**：arbiter brief 里示例写 `tiebreak` 会报 `bad pass`；实际输出每行 `pass="arbiter"`（文件仍是 `tiebreak/T1a.jsonl`）。
7. **`make_fix_plan.py` 需要 `SINGLE_SIDED` 集合**：最初按 A+B 生成会把 5 张单方卡也纳入修复；加排除集后为 22 卡 51 编辑。
8. **`show_card.py <slug>` 前缀歧义**：`vanishing-theorem` 会命中 `averaging-vanishing-theorem`；歧义时改用精确路径读 JSON。

## 5. 验证记录（终验）

- `verify_report.json`：`ok: true`、`fails: []`、`fix_edits_checked: 51`、`fix_cards: 22`、`md_not_synced: []`、`diff_check: "clean"`、HEAD `6a488d50dc9c47b9b8801d597c7a36d683046aea` 未动。
- 154 张目标卡 JSON 0 错误；全库 `datasets/*/cards/**/*.json` 1676 张 0 错误。
- `git diff --numstat -- datasets/glc` 恰为 22 卡 + 22 md（其中 `frobenius-twisted-trace` 卡/md 另含进入本任务前就存在的 1 行无关改动「游走→巡游」）。
- 13 个 JSONL（A1–A8、B1–B3、T1a–T1b）checker 全部 0 error / 0 warning。
- 外部核验：51/51 通过、0 推翻（`EXTERNAL_VERIFICATION.md`）。
- 发布：`11_card_audit/glc_full/`（README/TRACE/casebook/index + `raw/` 数据件 + `tools/` 脚本）与 22 卡＋22 md 的改动一起 commit（`7d79721e`），push 到 AtomGit `master:main` 与 Gitee `master`（均为 `6a488d50..7d79721e`，快进，无强推）。
- 复跑口径：`verify_final.py` 的「`git diff --numstat` 只含确认卡」与「HEAD 未动」只在 commit 前成立；修复已随 `7d79721e` 入库后，原地复跑会在这两条报红（预期）。发布后核对改用 `fix_log.json` 的 51 处 sha256 与 `git show --stat 7d79721e`；其余检查（154/1676 解析、md 同步、sha256 在位）随时可复跑。

## 6. 边界（本批没做）

- 不动底本源码：`ch16.tex:2` 的错误注释、`\srcpage` 漂移、ch11/ch12 缺页标记均保留原样；只在卡照抄了错误时改卡。
- 不重审卡内 `verification` 的每一条 nLab/Stacks 判词（只核了被引用的条目）。
- 不对 102 张未抽到 B 的卡补第二判断；`report.md` §9 已列为残余风险。
- 不改 `11_card_audit/casebook/`（32 例冻结档案）与其 `index.json`。

## 7. 外部核验与发布（2026-11-26 晚）

### 7.1 外部核验

用户要求「修的这些是不是对的，要回到卡以外」。做法：

1. **定位类 38 处**：只取 `sources[].anchor` 里未改动的源码行号，按 `\srcpage{N}` 重建「行 → 印刷页」，再逐页对 PDF 首句/节标题。`tools/reverify_pages.py` 覆盖 35 处可机械重算者：0 处与 PDF 实文冲突；21 处「naive ≠ 改后」全部归因到四类已知漂移（标记迟一页 15、标记早一页 2、缺标记 3、anchor 含上页标题 1）。
2. **内容／术语类 12 处**：逐条回到原书原文句；其中 5 张卡另有 arXiv 一手佐证——Gaitsgory `math/0204081`（vanishing 的一般形式仍要求几何不可约）、CCF24 `2409.07051` TeX（Casselman–Shalika 拼写）、AGKRRV `2010.01906` TeX（QLisse = IndLisse 的左完备化）。原书 p.37 的 `Av|C^{tor=0}` 公式与 p.47 的双前提句，直接支撑 base-whittaker 与 perverse-quotient 两处 summary 修复。
3. **唯一内部一致性类 1 处**：`fourier-deligne-transform` 的 `why` 行只删掉与本步 `text` 矛盾的从句，不主张新命题；Juteau 的 TeX 未找到显式「Fourier t-正合」陈述、KL85 PDF 两次超时，故明确标为 E3、不冒充外部证据。
4. **5 张单方未修**：外部复核后 2 张维持不改、3 张（deligne-gl1、hecke-laumon-stack、local-whittaker）A 方观察仍有依据，按协议保留为残余风险，写进 `EXTERNAL_VERIFICATION.md` §5 与 `report.md` §9。

完整逐条对照见 `datasets/_audit/glc_full_2026-11-26/EXTERNAL_VERIFICATION.md`。

### 7.2 发布布局

上一轮把过程档案放在 `11_card_audit/logs/2026-11-26/{README.md,TRACE.md,raw/}`，但那批文件当时并未 commit（任务禁止 push）。本轮的发布件按同一读者路径组织，但不复制第二份真实工作目录：

```
11_card_audit/glc_full/
  README.md          # 做了什么、怎么读、产物索引
  TRACE.md           # 本文：时间线、命令、裁决、返工
  index.json         # 22 个案例的机器索引
  casebook/          # 22 例（错误版/正确版/为什么错/证据/轨迹/形式化提示/防再犯）
  raw/               # passA 8、passB 3、tiebreak 2 的 JSONL；compare.json/md、
                     # issues.jsonl、fix_log.json、fix_plan.json、sample_inventory.json、
                     # verify_report.json、report.md、EXTERNAL_VERIFICATION.md、三份 brief
  tools/             # 从审计目录复制的 13 个脚本（可复现，不含 PDF/审计包）
```

`datasets/_audit/glc_full_2026-11-26/` 仍是真实工作目录（含 `tmp/` 的 PDF 副本、逐页文本、审计包），**不入库**：其中含有讲义正文，版权理由与体积理由都不适合推公开仓库。

### 7.3 新增决策

- **D11 外部核验与审计分离**：审计阶段的「卡 vs 来源」判断不再复用，独立用 anchor＋`\srcpage`＋PDF 正文页重算；目的不是再判一遍对错，而是证明「修复没有把错的改得更错」。
- **D12 发布件只保留一份真实目录**：`11_card_audit/glc_full/raw|tools` 是拷贝件，修改仍回 `datasets/_audit/...` 源头；`tmp/` 永不入库。
- **D13 残余风险显式化**：arbiter pass 但 lead 外部复核仍认为成立的三条不硬改（守协议），但必须写进两处报告，避免「审计通过」被误读成「这些卡没问题」。

### 7.4 英文原本逐句再核（2026-11-26 20:55）

- 底本确认：`datasets/_audit/third_party_2026-11-26/tmp/sources/glc.pdf` 就是 `LinChenGLC2023.pdf`（85 页，2025-08-08 修订），sha256 `f79cd79c…`；§2–§3 的 E1 引文本来就出自它。
- 复核方式：逐页打开 `tmp/pages/pNNN.txt`，抄回页眉、节标题与逐字句；不再引用上一轮笔记。
- 结果：已修 51 处 **51/51 维持**；5 张单方卡中 `deligne-gl1-existence`（p.7 coefficient field e）、`hecke-laumon-stack`（(M′,T) 不决定 M）、`local-whittaker-eigenfunction`（λ=(c,0,…) 指数为 0）**被原书/公式证实**，但按 arbiter-pass 不修协议保留，列为「证据充分、仅因协议未修」。
- 产物：`raw/EXTERNAL_VERIFICATION.md` §9（含 3 张单方的原句对照表）。

### 7.5 Follow-up：单方卡的外部补核与修复（21:00–21:30）

- **触发**：用户 m01466 要求先检索 nLab/全网佐证，再决定是否修 3 张单方卡。
- **证据**：E1 原书 p.7（系数域 e）、p.45–46（HL 定义）、p.21（指数公式）；E2 nLab `l-adic cohomology`（Q_ℓ 系数、k 底域）、nLab `geometric class field theory`（任意完全域）、nLab `extension`、CAG 2001（`dim Ext^1(O_x,L) = s > 1`，扩展由 P^{s−1} 参数化）、Casselman–Shalika 1980（numdam）、BIRS 13w5154 / Chhaibi ART 讲义。
- **修复**：3 卡 5 处——`deligne-gl1-existence`/`definition.notation`；`hecke-laumon-stack`/`key_points[0]`；`local-whittaker-eigenfunction`/`key_points[4]`、`verification.checks[2].asserts`、`verification.checks[2].verdict`。md 镜像同步 4 处（verdict 不渲染，属预期）。
- **协议处理**：不改 `passA/`、`passB/`、`tiebreak/`；`fix_log.json` 增加 `followup` 段（n_cards_primary 22 / n_edits_primary 51，总 25/56）；`issues.jsonl` 3 行状态 `single_sided → confirmed_fixed_followup`；案例库新增 23–25（确认链写 `lead+E1/E2`）。
- **决策 D14**：单方发现若被用户授权的 E1/E2 补核证实，可作为 follow-up 修复，但必须与原双盲记录分离存档（`fix_log.followup`、issues 状态区分、案例标 `lead+E1/E2`），不得回写成 A/B/arbiter 的确认。
- **数字**：确认 25 卡 56 处（29 minor＋1 major 的 30 条确认 issue），单方未修 2 张，外部核验 56/56、0 推翻。

### 7.6 思考链与工程记忆

- 按 `09_thinking/README.md`（L2 纪律）写 `09_thinking/chains/GLC-154/GLC-154-AUDIT-01.md`：6516 字符，九节（审计结论/任务/为什么值得看/关键片段/决策与替代方案/自纠与回退/验证证据/逆转条件/交付物），`score: pending` 等人工复核；登记在 `09_thinking/index.csv` 第 5 行。
- 该链只放「判断 + 否决 + 证据 + 逆转条件」，不放 raw CoT；会话原文留在 L0，不进仓库。
- 云端 Hindsight 在本机不可用：`hindsight_ingest_document` 返回 `401 Authentication failed: API key required`，`hindsight_diagnose` 显示 `C:\Users\admin\.hindsight\coding-agent.json` 不存在、`api_token_configured=false`。回退为仓库内 `MEMORY.md`（工程备忘录：定稿数字、关键修正、未解项、可复用约定、发布信息）。
- `thinking_audit.py check` 现存 4 条失败均来自上一批旧链（索引指向 `chains/SY02-31/…` 等不存在的按项目目录），本批之前即失败；本批条目按 checker 约定放 `chains/GLC-154/`，未新增失败。
