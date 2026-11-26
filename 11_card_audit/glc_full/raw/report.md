# 陈麟 GLC 讲义 154 张资料卡全量审计报告

- 审计日期：2026-11-26
- 对象：`datasets/glc/cards/**/*.json`，154 张，全部 `type=concept`
- 底本：`datasets/_audit/third_party_2026-11-26/tmp/sources/glc.pdf`（85 页，正文 p.5–p.83，页码偏移 0）
- 中译源码：`08_source_code/SY02-33_几何Langlands理论导论（陈麟）_中文译注校订版/源码/chapters/ch01.tex…ch16.tex`（119 节）
- 仓库基线：HEAD `6a488d50dc9c47b9b8801d597c7a36d683046aea`，未 commit、未 push

**结论一句话**：154 张全部过审；Pass A 判 27 张有问题，Pass B 盲审 52 张（27 张 A-issue 全覆盖 + 25 张 A-pass 随机样本），对照后 15 张双方同判、12 张单方，第三名 arbiter 盲审后 **确认 22 张、51 处** 并已修复；**5 张保留为单方发现不修**；`unverifiable` 0 张；severity 26 minor + 1 major。修复后 154 张卡 JSON 0 错误、全库 1676 张 0 错误、`git diff --check` 干净、diff 范围仅限本次确认的 22 张卡与其 22 个 md 镜像。

---

## 1. 审计对象

| 项 | 值 |
|---|---|
| 卡片数 | 154（`datasets/glc/cards/concepts/*.json`，另 `cards/` 下无其它子目录） |
| 章节覆盖 | ch01–ch16，共 119 节；章页范围 ch01 p.5-11 … ch16 p.75-82 |
| 卡类型 | 全部 `concept` |
| status | reviewed 88 / published 66 / rejected 0 |
| track 分布 | F 30 / H 30 / G 20 / C 20 / D 19 / E 18 / B 9 / O 4 / A 4 |
| `sources[]` | 160 条，148 卡 1 条、6 卡 2 条；键固定为 `book/section/pages/pdf_pages/anchor`（无 `quote` 字段） |
| theorems | 123 张有定理条目，`proof.status` = sketch 111 / complete 13；31 张无定理 |
| 规模 | 总计 982,385 字节，单卡 3.1–10.5 KB |

清单位于 `sample_inventory.json`（154 行：id / chapter / section / anchor / pages / path / sha256 前 12 位 / bytes），分组清单位于 `groups/A1.txt…A8.txt`、`groups/manifest.json`。

## 2. 方法与协议

### 2.1 分组

按连续章块分组，保证同一章的记号与口径由同一人审：

| 组 | 章 | 卡数 | | 组 | 章 | 卡数 |
|---|---|---|---|---|---|---|
| A1 | ch01–02 | 17 | | A5 | ch09–10 | 20 |
| A2 | ch03–04 | 20 | | A6 | ch11–12 | 20 |
| A3 | ch05–06 | 19 | | A7 | ch13–14 | 20 |
| A4 | ch07–08 | 18 | | A8 | ch15–16 | 20 |

Pass B 与 arbiter 的名单由种子随机（`seed=20261126`）生成并打乱，与 A 的组结构正交。

### 2.2 双盲

- **Pass A**：8 名审计员，各 17–20 张，互不可见；每人只拿本组路径清单；禁读既有审计结论（`third_party_2026-11-26/passA|passB|confirmed`）。
- **Pass B**：52 张 = 全部 27 张 A-issue + 25 张 A-pass 随机样本（20%，seed 固定）。B 只拿卡路径，不读 A 的 JSONL、`compare.*`、`issues.jsonl`、`fix_plan.json` 与 A 的工作笔记。
- **Arbiter**：12 张单方判 issue 的卡交第三名盲审（同样只拿路径），arbiter 同字段判 issue 才确认；arbiter 判 pass、或 arbiter 发现的是另一个字段，均保留为单方发现。
- 每人每卡 ≥3 条 `checks`，覆盖 definition/theorem、sources、internal 三类；issue 必带逐字 `card_says`（须为卡 JSON 子串）、`problem`、`should_be`、`evidence[{kind,ref,quote}]`。全部 10 个 JSONL 用 `tools/check_audit.py` 校验到 **0 error / 0 warning**。

### 2.3 证据与裁定口径

- 只用 E1（`glc.pdf` 正文、本地中译源码）与 E2（nLab/Stacks/arXiv/出版社，仅作强佐证）；禁 Wikipedia/博客/模型记忆。
- **卡自带的 `verification` 字段只当线索**，不作证据；`sources[]` 无 `quote` 字段，因此「逐字引文」一律由审计员回 PDF/源码取。
- 改卡判据：卡对 E1 来源有**错误断言**（页码、编号、引文、归属、定义、定理条件/方向），或卡内字段互相矛盾。风格、记号选择、解释性补充不算错；底本自身的缺陷在卡未歪曲时不算卡错。
- **页码规则**：PDF 页 = 印刷页（偏移 0）。`\srcpage{N}` 是分页标记，其后文字属第 N 页；但标记会漂移，见 §6。判定以 PDF 正文页眉/正文为准，PDF 目录与源码 `\srcpage` 只作线索。

## 3. 结果

### 3.1 Pass A

| 组 | 行数 | pass | issue | issue 卡 |
|---|---|---|---|---|
| A1 | 17 | 14 | 3 | deligne-gl1-existence, gl1-trace-character, affine-grassmannian |
| A2 | 20 | 17 | 3 | local-whittaker-eigenfunction, b-lambda-ic, local-laumon-formula |
| A3 | 19 | 16 | 3 | fourier-deligne-transform, vanishing-theorem, base-whittaker-sheaf |
| A4 | 18 | 13 | 5 | torsion-stack-local-model, euler-characteristic-trace-test, hecke-laumon-eigensheaf, hecke-laumon-stack, perverse-quotient-lemma |
| A5 | 20 | 18 | 2 | restricted-local-systems, scheme-of-singularities |
| A6 | 20 | 17 | 3 | shv-nilpotent-support, frobenius-twisted-trace, restricted-categorical-langlands |
| A7 | 20 | 16 | 4 | whittaker-coefficient, aut-sigma-module, drinfeld-sokolov-gauge, hitchin-base |
| A8 | 20 | 16 | 4 | quantum-local-langlands, unramified-oper, eisenstein-compatibility, global-langlands-functor |
| **合计** | **154** | **127** | **27** | 29 条 issue 记录 |

### 3.2 Pass B

| 组 | 行数 | pass | issue | issue 卡 |
|---|---|---|---|---|
| B1 | 18 | 13 | 5 | torsion-stack-local-model, gl1-trace-character, unramified-oper, quantum-local-langlands, aut-sigma-module |
| B2 | 17 | 9 | 8 | drinfeld-sokolov-gauge, base-whittaker-sheaf, scheme-of-singularities, restricted-local-systems, hitchin-base, vanishing-theorem, whittaker-coefficient, hecke-laumon-eigensheaf |
| B3 | 17 | 15 | 2 | global-langlands-functor, eisenstein-compatibility |
| **合计** | **52** | **37** | **15** | 15 张卡 |

B2 独立给出一个系统性观察：它报的 8 条里有 5 条同源于「`\srcpage{N}` 被插在段落/公式中间」——与 A 侧页码问题同因，属于一致的失效模式。

### 3.3 对照

| 分类 | 卡数 | 说明 |
|---|---|---|
| both_issue | 15 | 双方都判 issue |
| a_issue_only | 12 | A 判 issue、B 判 pass → 交 arbiter |
| both_pass | 25 | 双方都判 pass |
| b_not_sampled | 102 | A 判 pass、未被 B 抽中（协议内 80% 未抽） |

- 15 张 both_issue 中 **13 张字段完全一致**；2 张（drinfeld-sokolov-gauge、gl1-trace-character）是同一缺陷的不同字段标注，按缺陷算一致。
- 无 `b_issue_only`：B 报的 15 张全部在 A 的 27 张内。

### 3.4 仲裁

12 张 a_issue_only 由两名 arbiter（T1a/T1b 各 6 张）盲审，结果 8 张判 issue、4 张判 pass：

| 卡 | arbiter | 处理 |
|---|---|---|
| b-lambda-ic | issue（同字段：key_points[3] 名称） | 确认并修复 |
| fourier-deligne-transform | issue（同字段：steps[2].why） | 确认并修复 |
| frobenius-twisted-trace | issue（同字段：sources.pages / theorems[0].source） | 确认并修复 |
| local-laumon-formula | issue（同字段：definition.text 等 4 处） | 确认并修复 |
| perverse-quotient-lemma | issue（同字段：summary） | 确认并修复 |
| restricted-categorical-langlands | issue（同字段：sources.pages） | 确认并修复 |
| shv-nilpotent-support | issue（同字段：sources.pages / gap_note） | 确认并修复 |
| local-whittaker-eigenfunction | issue，但只在 **verification.checks[2]** | 单方未修（A 指的是 key_points[4]） |
| affine-grassmannian | pass | 单方未修 |
| deligne-gl1-existence | pass | 单方未修 |
| euler-characteristic-trace-test | pass | 单方未修 |
| hecke-laumon-stack | pass | 单方未修 |

## 4. 修复

**22 张卡、51 处编辑**（`fix_log.json` 逐处记录 before/after、sha256 前后值、md 镜像改动；卡与 md 同步修改）。其中 39 处是出处/页码/定理编号定位，12 处是数学内容、术语或内部一致性。

| # | 卡 | 编辑数 | severity | 确认链 |
|---|---|---|---|---|
| 1 | aut-sigma-module | 2 | minor | A(A7)+B(B1) |
| 2 | b-lambda-ic | 2 | minor | A(A2)+arbiter-t1a |
| 3 | base-whittaker-sheaf | 1 | minor | A(A3)+B(B2) |
| 4 | drinfeld-sokolov-gauge | 3 | minor | A(A7)+B(B2) |
| 5 | eisenstein-compatibility | 2 | minor | A(A8)+B(B3) |
| 6 | fourier-deligne-transform | 1 | minor | A(A3)+arbiter-t1b |
| 7 | frobenius-twisted-trace | 3 | minor | A(A6)+arbiter-t1a |
| 8 | gl1-trace-character | 3 | minor | A(A1)+B(B1) |
| 9 | global-langlands-functor | 3 | minor | A(A8)+B(B3) |
| 10 | hecke-laumon-eigensheaf | 2 | minor | A(A4)+B(B2) |
| 11 | hitchin-base | 2 | minor | A(A7)+B(B2) |
| 12 | local-laumon-formula | 4 | minor | A(A2)+arbiter-t1a |
| 13 | perverse-quotient-lemma | 1 | minor | A(A4)+arbiter-t1a |
| 14 | quantum-local-langlands | 3 | minor | A(A8)+B(B1) |
| 15 | restricted-categorical-langlands | 4 | minor | A(A6)+arbiter-t1b |
| 16 | restricted-local-systems | 2 | minor | A(A5)+B(B2) |
| 17 | scheme-of-singularities | 2 | minor | A(A5)+B(B2) |
| 18 | shv-nilpotent-support | 4 | minor | A(A6)+arbiter-t1a |
| 19 | torsion-stack-local-model | 3 | minor | A(A4)+B(B1) |
| 20 | unramified-oper | 2 | minor | A(A8)+B(B1) |
| 21 | vanishing-theorem | 1 | **major** | A(A3)+B(B2) |
| 22 | whittaker-coefficient | 1 | minor | A(A7)+B(B2) |

字段分布：`sources[].pages/pdf_pages` 24 处、`theorems[].source` 11 处、`theorems[].proof.gap_note` 4 处、`theorems[].proof.steps` 2 处、`key_points` 4 处、`summary` 2 处、`pitfalls` 1 处、`definition.text` 1 处、`verification.checks` 2 处，合计 51。

## 5. 单方未修（5 张，保留为发现）

| 卡 | A（或 arbiter）指出 | 为什么没修 |
|---|---|---|
| affine-grassmannian | `sources[0].pages=[13]`，而 `L^±G_X` 的记号句在 p.14 | arbiter 复核：§2.4 与 Theorem 2.4.1 都在 p.13，p.14 的 `L^±G_X` 只是备注性补充，不构成卡的断言错误 → 按「pages 已覆盖主对象」规则不修 |
| deligne-gl1-existence | `definition.notation` 把系数域写成底域 k（F_q），原文 p.7 明确「algebraically closed coefficient field e」 | arbiter 认为该句在 `Shv(Spec k)` 语境下可读作「k 上的分次向量空间」而判 pass → 单方发现，保留 |
| euler-characteristic-trace-test | `pages=[45]`，χ_K 的定义首句在 p.44 | arbiter：定义首句 p.44、判据主体 p.45，卡引的是判据 → 单方发现 |
| hecke-laumon-stack | `key_points[0]` 的「三者互相决定其中之二」不成立（(M′,T) 不给 M） | arbiter 判 pass → 单方发现；A 引的 `Ext^1(T,M′)` 结构其实与卡内 `pitfalls[1]` 自述矛盾，仍保留为待议 |
| local-whittaker-eigenfunction | `key_points[4]` 说有效优势权「指数为负」，而 λ=(c,0,…,0) 指数为 0 | arbiter 判 issue 但找的是 `verification.checks[2]` 的陈旧判词，不是同一字段 → 按字段不确认，保留 |

## 6. 关键修正（数学内容）

1. **`vanishing-theorem`（major）**：`key_points[1]` 的括注称一般形式「不再要求 $k<n$ 且 $E$ 几何不可约」。原文（`ch05.tex:117`、PDF p.36）只给「当 `rank(E)>k` 时界为 `d>(2g−2)k·rank(E)`」，而 `rank(E)>k` 就是 `k<n`，且未解除几何不可约。该括注是同卡定理陈述的反向弱化 → 删去括注，保留「界更精确」的正确表述。这是本次唯一 major。
2. **`perverse-quotient-lemma`**：`summary` 只说「π_*K 反常」就断言结论，漏掉引理要求的 `π_!K` 反常（PDF p.47：`Suppose K ∈ Perv(E) is Gm-equivariant and that π! K, π∗ K ∈ Perv(B).`），与卡内 definition/theorem/pitfalls 直接矛盾 → summary 补齐双前提。
3. **`base-whittaker-sheaf`**：`summary` 说「是 `Av_E^d(W_k)` 的茎」，而卡内定义、定理与 `ch06.tex:69` 都是「限制到 `C_k^{tor=0}` 上的层」。与 2026-11-18 对 `averaging-functor` 的同款修订一致 → 改为限制而非茎。
4. **`fourier-deligne-transform`**：`theorems[0].proof.steps[2].why` 写「t-正合函子把单对象送到单对象（至多差平移）」，与本步 text「单靠 t-正合不足」及 `key_points[2]`「等价 + t-正合才保持单对象，且不产生平移」矛盾 → 改为「等价加 t-正合才保持单对象，且不产生平移」。
5. **`restricted-local-systems`**：`verification.checks[1]` 仍保留「卡中 definition.notation 与此冲突 → P1, alignment=error」的陈旧判词，而 notation 已按 AGK20a §0.5.4 改成 IndLisse 左完备化 → 判词与 verdict 同步改为 confirmed，消除卡内自相矛盾。
6. **`eisenstein-compatibility`**：图表 (16.1) 在 PDF p.77（p.76 只有 §16.2 标题与 q,p 对应）→ 出处改 p.77；另 `key_points[3]` 人名误拼 `Casselman–Schalika` → `Casselman–Shalika`（同卡 proof step 2、`ch16.tex:38`、PDF p.76 均为 Shalika）。
7. 其余 39 处为**页码/出处定位**修正，两类根因：①`\srcpage{N}` 被放在段落或公式中间，导致卡把跨页陈述记成单页（13 处）；②章节起始页判断错（第 16 章实起 p.76，源码旧注释写 p.75；§12.6 整节在 p.63 而非跨 p.62–63；§15.4 在 p.74 而非 p.73）。

## 7. 页码体系（可复用的底本知识）

1. `\srcpage{N}` 其后文字属第 N 页，标记行本身算 N；但标记位置会漂移：`ch01.tex:109` 把 `\srcpage{7}` 放在 `\end{lemma}` 之后（引理 1.1.4 实为 p.7）；`ch15.tex:65` 是 §15.4 标题、`\srcpage{74}` 在 `:77`；`ch12.tex:110` 是 §12.6 标题、`\srcpage{63}` 在 `:117` 的注中。
2. **缺页标记**：`ch11.tex` 无 `\srcpage{60}`，`ch12.tex` 无 `\srcpage{64}`——照抄 `sources.pages` 就会漏掉这些页（本次 shv-nilpotent-support、frobenius-twisted-trace 即此因）。
3. **源码注释可能错**：`ch16.tex:2`「原PDF第75页，第16章开始」是错的，`:12 \srcpage{76}` 才对；第 16 章起于 PDF p.76（页眉 76）。
4. **PDF 自带目录对后几章不可靠**：目录写 §15.4→p.73、§15.5→p.74、ch16→p.75，正文实测 §15.4 在 p.74、§15.6 在 p.75、ch16 在 p.76。以正文页眉为准。
5. 机械筛子（`tools/mech_checks.py`）只能定位嫌疑，不能定罪：8 个 anchor_pages flag 中 7 个经复核为假阳性（背景句/证明续页落在邻页），只有 1 个与审计结论吻合。规则是：只有卡**自己的定义/陈述**落在 `pages` 之外才算错。

## 8. 验收

| 检查 | 结果 | 证据 |
|---|---|---|
| 154 张目标卡 JSON 解析 | 0 错误，id 与清单一一对应 | `verify_report.json` |
| 全库 `datasets/*/cards/**/*.json` 1676 张 | 0 解析错误 | 同上 |
| `git diff --numstat -- datasets/glc` | 仅 22 卡 + 22 md（另含基线既有 frobenius-twisted-trace 卡/md 的无关改动） | 同上 |
| `git diff --check` | clean（无空白错误） | 同上 |
| HEAD 未动 | `6a488d50dc9c…` | 同上 |
| fix_log 51 处 sha256/after 文本在位 | 51/51 | `fix_edits_checked: 51` |
| 卡与 md 镜像同步 | `md_not_synced: []` | 同上 |
| 13 个 JSONL（A1–A8、B1–B3、T1a–T1b）checker | 全部 0 error / 0 warning | 各 pass/tiebreak 目录 |
| 外部核验 22 卡 51 处 | 51/51 通过，0 推翻（38 定位＋12 内容/术语＋1 内部一致性） | `EXTERNAL_VERIFICATION.md` |

## 9. 残余风险与未解决

1. **5 张单方发现未修**（§5）。外部复核（`EXTERNAL_VERIFICATION.md` §5）判定：`affine-grassmannian`、`euler-characteristic-trace-test` 维持不改；`deligne-gl1-existence`（系数域写成 k）、`hecke-laumon-stack`（三者互相决定其二）、`local-whittaker-eigenfunction`（有效优势权「指数为负」，λ_n=0 时实为 0）三处 A 方观察仍有依据，但按「arbiter pass 不修」的协议保留，列为残余风险，建议下一轮用单方发现二审通道处理。
2. **Pass B 只覆盖协议规定的 52 张**：其余 102 张只有 Pass A 一个判断。为弥补，lead 对 8 个机械 flag、27 张 A-issue 卡全部亲核；但「A 与 B 都没抽到」的卡不排除仍有同类页码漂移。
3. **底本自身缺陷未改源码**：`ch16.tex:2` 的错误注释、`\srcpage` 漂移、ch11/ch12 缺页标记都还在；本次只在卡照抄了错误时改卡。若要根治，应另开一轮修源码任务。
4. **卡内 `verification` 字段**（nLab/Stacks 判词）未逐条重审，只核了被审计员引用到的条目；其中 `restricted-local-systems`、`local-whittaker-eigenfunction` 两处已证陈旧。
5. **`extension-stack-vanishing`**：`sources.pages=[40]` 而 anchor 含 §7.5 收尾（p.43），但卡的定义/陈述都在 p.40、`theorem.source` 已写「p.40–43」→ 按规则不算错，记入残余风险。
6. 未评估「表达质量/可读性」，本审计只对**事实断言**负责。

## 10. 产物

审计目录 `datasets/_audit/glc_full_2026-11-26/`：

| 文件 | 内容 |
|---|---|
| `sample_inventory.json` | 154 卡清单（id/chapter/section/anchor/pages/path/sha256/bytes） |
| `passA/A1–A8.jsonl` | Pass A 154 行 |
| `passB/B1–B3.jsonl` | Pass B 52 行 |
| `tiebreak/T1a–T1b.jsonl` | arbiter 12 行 |
| `compare.json` / `compare.md` | 对照分类、字段重叠、仲裁与最终确认 |
| `issues.jsonl` | 27 张卡 32 条 issue（22 张确认卡 27 条 confirmed_fixed + 5 张 single_sided） |
| `fix_log.json` | 22 卡 51 处 before/after、sha256、md 同步 |
| `fix_plan.json` | 修复计划（含 evidence 与确认链） |
| `verify_report.json` | 终验结果 |
| `EXTERNAL_VERIFICATION.md` | 22 卡 51 处的逐条外部核验（原书页＋arXiv 一手，0 推翻） |
| `AUDITOR_BRIEF.md` / `PASSB_BRIEF.md` / `ARBITER_BRIEF.md` | 三份盲审协议 |
| `groups/` `tmp/` `tools/` | 分组清单、页码/PDF 文本缓存、工具脚本 |

案例与日志 `11_card_audit/glc_full/`：`README.md`、`TRACE.md`、`casebook/`（22 例，七节）、`index.json`。

## 11. 复现

```bash
cd C:/Users/admin/Desktop/数译发布/gitee_shuyi
python datasets/_audit/glc_full_2026-11-26/tools/make_inventory.py
python datasets/_audit/glc_full_2026-11-26/tools/build_packs.py
python datasets/_audit/glc_full_2026-11-26/tools/mech_checks.py
python datasets/_audit/glc_full_2026-11-26/tools/make_passB_list.py --seed 20261126 --frac 0.2
python datasets/_audit/glc_full_2026-11-26/tools/compare.py
python datasets/_audit/glc_full_2026-11-26/tools/make_tiebreak.py
# 修复（幂等；old 必须逐字匹配）：
python datasets/_audit/glc_full_2026-11-26/tmp/make_fix_plan.py
python datasets/_audit/glc_full_2026-11-26/tools/apply_fixes.py --plan datasets/_audit/glc_full_2026-11-26/fix_plan.json --check
python datasets/_audit/glc_full_2026-11-26/tools/apply_fixes.py --plan datasets/_audit/glc_full_2026-11-26/fix_plan.json --apply
python datasets/_audit/glc_full_2026-11-26/tools/finalize.py
python datasets/_audit/glc_full_2026-11-26/tools/make_casebook.py
python datasets/_audit/glc_full_2026-11-26/tools/verify_final.py
```
