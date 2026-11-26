# 资料卡审计档案（独立分区）

这里存放 **2026-11-26 第三方资料卡审计** 的工作日志、正误对比案例库和后续校对规范。

> 这个分区**不是卡片目录**，也不参与 `datasets/` 的加载。
> 卡片本身已经在原位置完成修改；这里的文件用于追溯、复核、教学和防止回归。

## 这次审计做了什么

- 从 `datasets/*/cards/**/*.json` 的 **1,675** 张非 `work.json` 卡片中，用固定种子 `20261126` 随机抽取 **100** 张。
- 5 名 Pass A 审计员各审 20 张；5 名 Pass B 盲审员轮转复核，另设 1 名独立仲裁员。
- **两个独立审计员都判 issue** 才进入确认修复；单方 issue 由仲裁员盲审，仲裁也判 issue 才确认；仲裁判 pass 的只记录为单方发现。
- 最终：**31 张卡确认修复（103 处）+ 1 张 lead 机械补修（1 处）= 32 张卡 / 104 处**。
- 其余：22 张双人均 clear，4 张本地/外部证据不足判 `unverifiable`，37 张 B 轮未抽到，6 张单方发现经仲裁 pass、未修。

完整数字与逐卡表见 [`logs/2026-11-26/raw/report.md`](logs/2026-11-26/raw/report.md)；机器可读汇总见 `logs/2026-11-26/raw/summary.json`。

## 第二批：GLC 154 卡全量审计（2026-11-26 晚）

- 对象：`datasets/glc/cards/**/*.json` 全部 **154** 张 `concept` 卡，**全量**审计（不抽样）。
- 流程：8 名 Pass A（154 行）→ Pass B 52 张盲审（27 张 A-issue 全覆盖 + 25 张随机 20%）→ 12 张单方发现交第三名 arbiter 盲审 → 22 张确认修复（15 both_issue + 7 arbiter 同字段）。
- 结果：**22 张卡 / 51 处**（26 minor + 1 major），5 张单方未修，0 unverifiable；另做 51 处外部核验（原书页 + arXiv 一手，51/51 通过、0 推翻）。
- 归档：[`glc_full/`](glc_full/)——结构与上一批同构：`README.md`（范围/结论）、`TRACE.md`（时间线/决策/返工）、`raw/`（passA、passB、tiebreak、compare、issues、fix_log、report、EXTERNAL_VERIFICATION、三份 brief）、`tools/`（13 个脚本）、`casebook/`（22 例七节）+ `index.json`。
- 与上一批互不影响：本批不改 `casebook/` 的 32 例与其 `index.json`。

## 目录

```text
11_card_audit/
├── README.md                     # 本文件
├── WORKFLOW.md                   # 未来卡片校对的工作规范（核心）
├── casebook/
│   ├── README.md                 # 32 例索引 + 失效模式统计
│   ├── SHOWCASE.md               # 10 个代表性正误对比
│   ├── index.json                # 机器可读索引
│   └── <set>__<type>__<slug>.md  # 每例：错误版/正确版/为什么错/证据/形式化提示
├── logs/2026-11-26/
│   ├── README.md                 # 原始日志清单与复现命令
│   ├── TRACE.md                  # 审计时间线、角色、关键裁决
│   └── raw/                      # passA/passB/tiebreak/compare/issues/fix_log/report
├── templates/
│   ├── CASE_TEMPLATE.md          # 新案例模板
│   ├── CHECKLIST.md              # 校对检查清单
│   └── REVIEW_RECORD_TEMPLATE.jsonl
└── tools/
    ├── build_casebook.py         # 从冻结记录重建 casebook（只写本分区）
    └── check_casebook.py         # 校验案例完整性与索引一致性
```

## 怎么读

1. **先读** [`WORKFLOW.md`](WORKFLOW.md)：以后要改卡，按这个流程走。
2. **再读** [`casebook/README.md`](casebook/README.md)：按卡片 id 或失效模式找同类错误。
3. 想快速看“错在哪” → [`casebook/SHOWCASE.md`](casebook/SHOWCASE.md)。
4. 想复核判定 → [`logs/2026-11-26/TRACE.md`](logs/2026-11-26/TRACE.md)，再查 `raw/` 里的原始 JSONL。
5. 想重跑/复现 → 见 [`logs/2026-11-26/README.md`](logs/2026-11-26/README.md)。

## 重要声明

- 本库中的“为什么会错”是**从错误形态反推的失效模式**，不是原始模型的私有思维链，也不是对作者动机的猜测。每条都标了“推断”。
- 审计轨迹只记录**可复核的事实**：谁在哪个 pass 判了什么、引了哪一页/哪一句、lead 怎么裁决。原始证据在 `raw/`。
- 卡片的修改是**最小文本编辑**：不改结构、不改无关字段、不批量重排；每处都有 before/after（`raw/fix_log.json`）。
- 本分区没有再次改卡；`datasets/` 下 32 张卡的修改已在前一步完成。
- 上一批（100 卡）当时没有 commit / push；工作区里原本就有 68 个与本任务无关的修改，当时没有动它们。
- 本批（GLC 154 卡）按用户要求已 commit 并 push 到 AtomGit `main` 与 Gitee `master`（提交 `7d79721e`、`bfffe0cc`），详见 [`glc_full/TRACE.md`](glc_full/TRACE.md) §7。

## 两个命令

```bash
# 校验 32 个案例、索引、必需章节
python 11_card_audit/tools/check_casebook.py

# 从冻结的审计记录重建 casebook（不会碰卡片）
python 11_card_audit/tools/build_casebook.py
```
