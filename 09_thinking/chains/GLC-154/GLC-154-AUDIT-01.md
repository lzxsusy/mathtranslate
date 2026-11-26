---
chain_id: GLC-154-AUDIT-01
project: GLC-154
session: 2026-11-26 lead + 8 Pass A 审计员 + 3 Pass B 审计员 + 2 arbiter（共 13 个并行子会话）
created: 2026-11-26
approved_by: lzxSUSUY（用户 m01030 明确要求「外部核验 + 推送工程文件与思考链 + 记住这个工程」）
approved_at: 2026-11-26
score: pending
reasoning_chars: n/a（13 个子会话，未统计）
decision: 154 张全量双盲 + 第三方仲裁；只修 22 卡 51 处；5 张单方发现保留不修；页码以 PDF 正文页眉为准而非源码 \srcpage
audit_note: 51/51 外部核验通过、0 推翻；1 处（fourier）仅有内部一致性依据，未主张新命题；5 张单方卡的外部依据仍成立，列残余风险
source_card: datasets/_audit/glc_full_2026-11-26/report.md
---

## 0. 审计结论

对陈麟 GLC 讲义 154 张资料卡做了一次全量、双独立、可回滚的审计：Pass A 8 名审计员共 154 条记录（127 pass / 27 issue），Pass B 盲审 52 张（37 pass / 15 issue），第三名 arbiter 盲审 12 张单方分歧（8 issue / 4 pass）。最终确认 22 卡 51 处（26 minor + 1 major），5 张单方发现按规则保留不修，0 张 unverifiable，51/51 处改动经原书 PDF 与 arXiv 一手材料复核、0 推翻。

三条改变交付物的判断：

1. **`sources.pages` 必须以 PDF 正文页眉为准，不能信源码 `\srcpage`**。该标记会漂移（插在段末、标题后、缺页），本批 21 处「机械映射页 ≠ 卡写页」全部可归因到它，而不是卡错。
2. **只有 both_issue 或 arbiter 同字段 issue 才允许改卡**。12 张单方分歧里 4 张 arbiter 判 pass、1 张 arbiter 只认另一个字段，全部保留原样并写进残余风险，避免把有争议的解释性判断写进数据。
3. **修卡的字符串编辑必须带足 TeX 边界**。一次 `old` 少了前导 `$`，产生 `"$等价加 $t$-正合…"` 的坏公式；回滚该卡、重做编辑、合并 fix_log 才恢复。此后所有 substring 编辑都断言「当前值中恰好出现 1 次」且带完整 `$...$` 或标点。

## 1. 任务

- 对象：`datasets/glc/cards/**/*.json` 共 154 张，全部 `type=concept`，16 章，正文 p.5–p.83。
- 来源：用户 m00001（全量审计，不抽样；每卡≥3 条 checks，覆盖定义/定理、sources、internal 三类）；用户 m01030（外部核验 51 处、按以往格式推送工程文件与思考链、记住这个工程）。
- 约束：外部只用一手/权威二手（原书 PDF、本地中译源码、arXiv、出版社、nLab/Stacks 强佐证）；禁 Wikipedia/博客/模型记忆；禁编造页码引文；卡自带 `verification` 只作线索；不 commit 冲突文件；不覆盖上一批冻结档案。
- 成功标准：154/154 有 A 记录；所有 A-issue 卡有 B 或 arbiter 第二判断；确认数与 fix_log 一致；改后 154 卡与全库 1676 卡 JSON 0 错；`git diff` 只含确认卡；不 commit 额外文件。

## 2. 为什么值得看

三类失效在这批卡里各自成片出现，且都不是「翻译腔」而是可判定的错：

- **出处定位漂移**（17 处）：卡写 p.N，实际陈述在 p.N−1、N+1 或跨页。系统性成因是 `\srcpage` 的插入位置，而不是审计员随手改数。
- **适用范围遗漏**（4 处）：summary/要点把「限制到 `C_k^{tor=0}` 的层」写成「茎」，把「几何不可约仍需」写成「不再要求」。
- **内部不一致**（4 处）：同卡 summary 与定理、key_points 与 proof、verification 与正文互相打架；其中 `vanishing-theorem` 的括注同时与原文和同卡定理冲突，是唯一 major。

## 3. 关键片段（压缩摘录）

### 片段 1 · 8 名审计员怎么并行而不互相污染

> 分组按连续章块（ch01+02、ch03+04、…、ch15+16），每组 17–20 张，保留同章记号一致性。每人只写自己的 JSONL，跑同一个 checker；checker 校验 n 连续、路径逐行对齐、checks 覆盖三类、`card_says` 必须是卡 JSON 子串。A 判完不收工，lead 逐条亲核后才进 B 名单。

### 片段 2 · B 的独有发现

> B3 在 `eisenstein-compatibility` 上报了 A 没报的字段：`key_points[3]` 写「Casselman–Schalika」，而同卡 proof 与底本 p.76 都是 Shalika。A 只报了 theorem.source 的页码。这说明双盲不是形式：同一张卡，两双眼睛看的是不同字段。

### 片段 3 · 页码为什么必须回到 PDF 页眉

> `gl1-trace-character` 的引理 1.1.4，源码把 `\srcpage{7}` 放在 `\end{lemma}` 之后，机械映射得 p.6；PDF `p007.txt` 页眉后第一行就是 `Lemma 1.1.4.`。同一类偏差在 ch11（缺 p.60 标记）、ch12（缺 p.64）、ch15（§15.4 标题在 :65，标记在 :77）、ch16（注释写「原PDF第75页」而 `\srcpage{76}` 才对）各出现一次。

### 片段 4 · 修卡事故

> 第一次 apply 后 `fourier-deligne-transform` 的公式变成 `"$等价加 $t$-正合…"`：`old` 少了前导 `$`。处理不是补丁，而是 `git checkout --` 该卡与 md、改 spec、重建 22 卡 plan、单卡重 apply、再把单卡记录合并回总 fix_log——保证 51 条都能从一次干净 apply 复现。

### 片段 5 · 外部核验到底核什么

> 只问三件事：外部原文有没有说反、有没有丢掉条件、页码是否真的错。`vanishing-theorem` 的「不再要求 k<n」被 arXiv:math/0204081 的 Conjecture 1.3 直接否掉（原文仍要求 E 不可约，且 `rank(E)>k` 本就是 `k<n` 的改写）；`restricted-local-systems` 的 IndLisse 左完备化被 AGKRRV 正文原文证实。核不出来的（fourier）不硬凑，标明「仅有内部一致性依据」。

## 4. 决策与替代方案

1. **分组按章而非按 track**：否决按 A/B/C… track 分——同章多张卡共享记号，同一人看能发现跨卡矛盾。代价是各组张数不均（17–20）。
2. **Pass B 抽 20% A-pass 卡**：否决只审 A-issue 卡——那样无法估计 A 的漏报率；25 张 pass 样本里 0 张被 B 翻案，给出漏报率的上界线索。
3. **both_issue 才修 + 单方必 arbiter**：否决「A 判 issue 即修」——解释性判断（如 affine-grassmannian 的 L^±G_X 是否属「备注」）需要第三方；5 张保留卡即是这套规则的代价，写进残余风险而不是悄悄修掉。
4. **pages 覆盖 anchor 自述范围**：`affine-grassmannian` 的 anchor 明写「定义与扭曲积见 76-98 行」，覆盖 p.14，卡只写 [13] → 补 [13,14]。但「pages 已覆盖主对象、只漏背景句/续证页」不算错（springer-sheaf、extension-stack-vanishing 都据此不改）。
5. **卡与 md 同步改**：`datasets/glc/md/` 是手工渲染副本，只改卡会制造新不一致；apply_fixes 对每处编辑生成 md 替身（pages 渲染成 `p.6（PDF p.6）`），歧义即拒写。
6. **发布件只留一份真实目录**：`11_card_audit/glc_full/` 放 README/TRACE/casebook/raw/tools；`tmp/`（含 2MB 原书 PDF、3.4MB packs）不入库，版权与体积两理由。
7. **不推 GitHub**：远端落后 58 提交/2373 文件、最大新 blob 34MB；日常流程只走 AtomGit + Gitee，避免把一次审计变成全仓镜像。

## 5. 自纠与回退

1. `compare.py` 原把「B 未抽到」标成 `unverifiable`，改成 `b_not_sampled` 后计数才正确（both_issue 15 / a_issue_only 12 / both_pass 25 / b_not_sampled 102）。
2. `apply_fixes.py` 的 md 歧义判法从「before 是否还在最终 JSON」改为「同文本是否出现在另一个字段」+「md 中出现 >1 次」；旧判法把「p.63」→「p.63–64」误判歧义。
3. `verify_final.py` 两处脚本 bug：`after` 可能是列表；md 校验改用 `md_sync.edits[].md_new` 并放行 `.verdict` 的 not_found（md 不渲染 verdict）。
4. `make_casebook.py` 的 REPO 少一层，曾误建 `datasets/11_card_audit/`；删掉后改 `../../..`。
5. `show_card.py` 用前缀匹配，`vanishing-theorem` 会撞 `averaging-vanishing-theorem`；歧义时直接按精确路径 `json.load`。
6. Hindsight 写入 401（无 API key，config 不存在）→ 回退为仓库内 `11_card_audit/glc_full/MEMORY.md`，并在最终答复里披露。
7. 外部核验时 KL85 PDF 下载超时（curl 28），未取到直接证据；`fourier-deligne-transform` 那处因此只按底本陈述 + 卡内一致性定性。

## 6. 验证证据

- `check_audit.py`：passA 8 份共 154 行、passB 3 份 52 行、tiebreak 2 份 12 行，全部 0 error 0 warning，行序与组清单逐行一致。
- 对照：`compare.json` 37 个抽样/命中卡的分类如上；15 张 both_issue 中 13 张字段完全重叠，2 张是同一缺陷不同字段。
- 修改：`APPLIED: 22 cards, 51 edits`；`fix_log.json` 记录每处 before/after 与 sha256。
- 回读：`verify_final.py` → `ok:true`、`fails:[]`、`fix_edits_checked:51`、`md_not_synced:[]`、`diff_check:"clean"`；154 卡 0 错、全库 1676 卡 0 错；`git diff --numstat -- datasets/glc` 恰为 22 卡 + 22 md。
- 外部核验：`EXTERNAL_VERIFICATION.md` 51/51 通过、0 推翻；35 处可机械重算的定位编辑由 `reverify_pages.py` 独立重算，21 处差异全部落在已知 `\srcpage` 漂移类型内。
- 发布：commit `7d79721e`（工程归档）、`bfffe0cc`（TRACE 补记）；AtomGit `main` 与 Gitee `master` 均已推送，HEAD 与记录一致。
- 已知遗留：4 条旧链（SY02-31、GRASSMANN、SY02-38×2）索引指向不存在的按项目目录路径，`thinking_audit.py check` 在本次之前即失败；本次 GLC 条目按 checker 约定放 `chains/GLC-154/GLC-154-AUDIT-01.md`，不再增加新失败。

## 7. 逆转条件

- 若发现 PDF 页眉与 `\srcpage` 冲突的更多实例 → 重跑 `reverify_pages.py` 全量重算，并把「以页眉为准」写成数据集级约定。
- 若 Pass B 抽样率提高到 100%（下一轮）→ 5 张单方卡可能被翻案；届时按同一 arbiter 规则重判，而不是直接采信本轮 lead 结论。
- 若 CCF24/AGKRRV 出现新版本改掉「Casselman–Shalika」拼写或 IndLisse 定义 → 回退相应两处改动（均有 before/after 可查）。
- 若仓库启用云端 Hindsight token → 把 `MEMORY.md` 迁进去，并删本地副本。
- 若 reviewer 指出 `vanishing-theorem` 的「删括注」改变了作者原意 → 以原书 p.36 逐字句为准复核，不改回「不再要求」。

## 8. 交付物

- `datasets/_audit/glc_full_2026-11-26/`：`passA/A1–A8.jsonl`、`passB/B1–B3.jsonl`、`tiebreak/T1a–T1b.jsonl`、`compare.json/md`、`issues.jsonl`、`fix_log.json`、`fix_plan.json`、`sample_inventory.json`、`verify_report.json`、`report.md`、`EXTERNAL_VERIFICATION.md`、`tools/`。
- `11_card_audit/glc_full/`：`README.md`、`TRACE.md`、`MEMORY.md`、`index.json`、`casebook/`（22 例 + README）、`raw/`（全部 JSONL 与报告拷贝）、`tools/`（13 个脚本拷贝）。
- 数据：22 张 `datasets/glc/cards/concepts/*.json` 与对应 `datasets/glc/md/concepts/*.md` 的字段级修改（51 处）。
- 登记：`09_thinking/index.csv` 新增 GLC-154 一行；本链。
