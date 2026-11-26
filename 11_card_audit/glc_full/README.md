# GLC 154 张资料卡全量审计（2026-11-26）

本目录记录 2026-11-26 对 `datasets/glc/cards/**/*.json` 全部 **154 张** `concept` 卡的独立全量审计：Pass A（8 人）→ Pass B（52 张盲审）→ 单方发现交第三名 arbiter 盲审 → lead 逐条复核 → 22 张确认卡最小修复。

与 `11_card_audit/casebook/`（上一批 100 卡审计的 32 例冻结档案）**互不影响**：本批不改、不覆盖那 32 例与其 `index.json`；本批 22 例另存于本目录 `casebook/`。

## 结论

| 指标 | 数 |
|---|---|
| 审计卡数 | 154（全量，非抽样） |
| Pass A 判 issue | 27 张 / 29 条 |
| Pass B 盲审 | 52 张（27 张 A-issue 全覆盖 + 25 张 A-pass 随机 20%） |
| 双方同判（both_issue） | 15 张 |
| 单方判 issue（a_issue_only） | 12 张 |
| arbiter 确认 | 7 张（另 4 张 arbiter 判 pass、1 张只认另一字段） |
| **确认修复** | **22 张 / 51 处** |
| 单方未修 | 5 张 |
| unverifiable | 0 |
| severity | minor 26 / major 1（`vanishing-theorem`） |
| 外部核验 | 51/51 通过、0 推翻（38 定位＋12 内容/术语＋1 内部一致性） |

完整数字、逐条证据与残余风险见 `raw/report.md`；51 处修改的外部核验见 `raw/EXTERNAL_VERIFICATION.md`。

> 工作副本在 `datasets/_audit/glc_full_2026-11-26/`（含 PDF 与逐页文本，**不入库**，版权理由）；本目录的 `raw/`、`tools/` 是发布拷贝。

## 目录结构

```
11_card_audit/glc_full/
├── README.md            本文件：范围、方法、结论、用法
├── TRACE.md             审计轨迹：时间线、命令、关键决策与返工
├── index.json           22 个案例的索引（slug / mode / severity / fields / confirmed_by / file）
├── casebook/
│   ├── README.md        案例库说明与失效模式统计
│   └── NN-<slug>.md     22 个案例，每例七节
├── raw/                 原始审计数据（本目录自足，无需访问 datasets/_audit）
│   ├── passA/A1–A8.jsonl      Pass A 154 行
│   ├── passB/B1–B3.jsonl      Pass B 52 行（含 groups/）
│   ├── tiebreak/T1a–T1b.jsonl arbiter 12 行（含 groups/）
│   ├── groups/                A1–A8 分组清单与 manifest
│   ├── compare.json / compare.md   对照分类、字段重叠、仲裁与最终确认
│   ├── issues.jsonl           32 条 issue（27 confirmed_fixed + 5 single_sided）
│   ├── fix_log.json           22 卡 51 处 before/after、sha256、md 同步
│   ├── fix_plan.json          修复计划（含 evidence 与确认链）
│   ├── sample_inventory.json  154 卡清单（id/chapter/section/anchor/pages/sha256）
│   ├── verify_report.json     终验结果
│   ├── stats.json             各组行数与 verdict 分布
│   ├── report.md              审计全过程报告
│   ├── EXTERNAL_VERIFICATION.md  51 处外部核验（原书页＋arXiv 一手）
│   └── AUDITOR_BRIEF / PASSB_BRIEF / ARBITER_BRIEF.md  三份盲审协议
└── tools/               13 个可复现脚本（清单/审计包/校验/对照/仲裁/修复/终验/外部核验）
```

每个案例七节：错误版（改前逐字）→ 正确版（改后逐字）→ 为什么错 → 证据（E1 页码/源码行号/逐字引文）→ 审计轨迹（哪些人、哪一轮、怎么确认的）→ 形式化提示 → 防再犯。

## 本批的 5 类失效模式

| 失效模式 | 例数 | 典型 |
|---|---|---|
| 页码/出处定位漂移 | 9 | `\srcpage{N}` 插在段落中间，卡把跨页陈述记成单页 |
| 页码范围遗漏 | 5 | 底本缺 `\srcpage{60}`、`\srcpage{64}`，卡照抄导致漏页 |
| 术语/人名拼写 | 2 | `Casselman–Shalala`、`Casselman–Shalika` 混用 |
| 适用范围（限制 vs 茎） | 1 | `base-whittaker-sheaf` 把限制写成茎 |
| 逻辑条件反转 / 内部矛盾 / summary 漏前提 / 残留字段 | 5 | `vanishing-theorem` 把 `rank(E)>k` 说成「不再要求 k<n」 |

## 用法

- 想知道**某张卡改了什么、为什么**：先看 `index.json` 找 `NN-<slug>.md`。
- 想复核某处修改是否站得住：读 `raw/EXTERNAL_VERIFICATION.md`，里面有每处的改前/改后、原书页码与逐字引文、arXiv 佐证，以及 21 处「源码分页标记漂移」的逐条归因。
- 想复核证据：案例里的页码对应 `datasets/_audit/glc_full_2026-11-26/tmp/pages/pNNN.txt`（PDF 逐页文本，页码＝印刷页）；源码行号指向 `08_source_code/SY02-33_…/源码/chapters/chNN.tex`。
- 想重跑/复现：见 `raw/report.md` §11 与 `tools/`；`reverify_pages.py` 可独立重算定位编辑的页码。
- 想给下一批审计立规矩：读 `TRACE.md` 的「决策日志」「返工记录」与「外部核验与发布」。

## 维护约定

1. **卡与 md 必须同步改**：`datasets/glc/md/concepts/<slug>.md` 是卡的渲染副本，只改 JSON 会造成卡/md 不一致。修复脚本 `apply_fixes.py` 强制 md 同步，歧义时拒写。
2. **最小编辑**：只改确认的字段，old 必须逐字匹配当前值（`substring` 模式要求恰好出现一次），不做整体重排。改后统一 `json.dumps(ensure_ascii=False, indent=2) + "\n"`。
3. **页码以 PDF 正文页眉为准**，`\srcpage` 与 PDF 目录只作线索（底本有漂移，见 `report.md` §7）。
4. 本目录的 22 例是**已确认并修复**的案例；单方未修的 5 张只记在 `report.md` §5，不进 casebook。
