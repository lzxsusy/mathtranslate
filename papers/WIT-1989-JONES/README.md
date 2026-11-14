# WIT-1989-JONES：Witten《量子场论与 Jones 多项式》研讨班

第二轮「威腾文章解经」的试点论文。对象是 Witten 1988 年 9 月收稿、1989 年发表于 *Communications in Mathematical Physics* 121 卷的 CS/Jones 论文（原文 49 页）。

一句话：**用 3 维陈–西蒙斯理论的量子化，给 Jones 多项式一个内蕴三维定义；副产品是 2 维共形场论的共形块被解释为 3 维理论的 Hilbert 空间。**

---

## 五分钟上手

只读三个文件，不用碰其他：

1. `seminar/开题导读.md` —— 论文在做什么、四个起点问题的答案、七条主线地图、阅读路线。
2. `seminar/CHARTER.md` —— 这轮研讨班怎么开、要求是什么、每场交什么、怎么判分。
3. `materials/文献表.md` —— 读什么、先读什么、本地有没有 PDF。

如果你只想读一页：看 `seminar/开题导读.md` 的 §0。

---

## 目录

```
WIT-1989-JONES/
├── README.md                 本文件
├── seminar.yaml              机器可读元数据（论文、译本、角色、闸门）
├── deliverables/             ★ 最终交付（2026-11-13 用户定）
│   ├── reading_note/         正儿八经的读书笔记：LaTeX 源 + PDF（20–35 页）
│   └── engineering/          工程文件与源代码：构建脚本、manifest、锚点核验、数据
├── materials/                研读底料（不随场次变）
│   ├── _BRIEF.md             给 AI 成员的作业简报（七主线 + 硬规矩）
│   ├── 文献表.md             注释书目：阅读优先级、T0–T6 分组、核验、本地馆藏
│   ├── 已译资料清单.md       我们已有的中译/笔记，逐主线可用性映射
│   ├── 1988语境与问题史.md    时间线、四问深答、1988 vs 后世、T5/T6 边界
│   ├── 本地教材核查_河野拓扑场论.md  河野俊丈《场论与拓扑学》中译的目录与覆盖矩阵
│   ├── 教材核查_李思几何量子化.md    李思《量子力学与几何》第 5 章的页码、覆盖与桥接表
│   └── 外部参照_Moore与Schottenloher.md  Moore TASI / Schottenloher §11 / nLab / Wang 的按节查法
├── seminar/                  研讨班本体（制度层）
│   ├── 开题导读.md           S0 导读（Lead 写）
│   ├── CHARTER.md            本轮章程（要求、场次、闸门、评分）
│   ├── 团队与阅读计划.md      4 人编制、分角色阅读清单、S3–S6 问题集
│   ├── 问题清单.md           原问题诊断 + 改写后的可答子问题
│   └── 争议清单.md           每场后追加：内部没达成一致的条目（S1–S6）
├── sessions/                 每场执行层（s1–s6 均已跑完）
│   ├── s1/ … s6/             agenda、reports/、challenges/、transcript、claims、questions、one_pager
│   └── _schema_fix_log.md    verifier 复审后的数据整改日志（37 条 schema + 4 条内容）
└── deliverables/             ★ 最终交付
    ├── reading_note/         读书笔记：main.tex + chapters/ + main.pdf（21 页）
    └── engineering/          build.ps1、校验脚本、manifest.json、claims/questions 数据
```

---

## 现状（2026-11-13，v0.5：六场跑完；两版讲义定稿——49 页连续叙事 + 97 页逐句注疏）

| 项 | 状态 |
|---|---|
| 底本中译 | **已完成并编译**：`<本地路径>`（**40 页**重排版式 / 原文印刷 49 页；1,274,530 B，sha256 `9471496…b3f4966`）；`校勘与审校批注汇总.md` 86 KB |
| 文献表 | **完成**（273 行，73 条）；§1A 已按“原文核心 + 教材补前置”二次修订 |
| 已译资料清单 | **完成**（31 项资产 + 七主线可用性 + 10 条质量警告） |
| 1988 语境与问题史 | **完成**（266 行；11 条未核在 §10） |
| 教材核查 | **三份**：河野《场论与拓扑学》（126 页，T0–T4，T5/T6 无）；李思《量子力学与几何》第 5 章（PDF 309–325，补 T1 预量子化/极化）；外部参照（Moore TASI 2019 / Schottenloher §11 / Wang CS notes / nLab） |
| 阅读策略 | **已二次改定**：Witten 原文逐节读；前置用李思/河野/上野；1980 年代原文非必需 |
| S1 问题地图 | **完成**（T 自评 88；claims 13 / questions 6）；verifier 58/100 → 已整改（否决解除） |
| S2 几何量子化 | **完成**（T 自评 88；claims 12 / questions 6）；verifier 61/100 → 已整改（实质通过） |
| S3 Wilson 线/BWB | **完成**（T 自评 88；claims 12 / questions 6）；verifier 66/100（c-s3-07 已改） |
| S4 共形块与 WZW | **完成**（T 自评 90；claims 11 / questions 5）；verifier 73/100（页锚已改） |
| S5 Verlinde | **完成**（T 自评 89；claims 12 / questions 6） |
| S6 两种对偶 + 范畴化 | **完成**（T 自评 87；claims 13 / questions 6） |
| 数据整改 | **完成**（`sessions/_schema_fix_log.md`：37 条 schema 归一 + 4 条内容错误；check_claims 0 错误） |
| 团队与阅读计划 | **完成**（`seminar/团队与阅读计划.md`：4 人编制、分角色阅读、S3–S6 问题集） |
| **交付①讲义（主文本）** | **49 页 PDF 定稿**（`deliverables/lecture/main.pdf`）：前言 + 八讲（问题→作用量→相空间→量子化→Wilson 线→WZW→计算→边界）+ 附录（符号、练习提示、原文对照表、术语表、练习选解、复现指南） |
| **交付②注疏版（查证手册）** | **97 页 PDF 定稿**（`deliverables/reading_note/main.pdf`）：十二讲 + 附录 A–E，按原文节序逐句对照，含 G-x 缺口与 D-x 推导 |
| **交付③协作流程** | `deliverables/workflow/`：WORKFLOW.md（数据流与复现）、agents.json（角色与产物）、tasks_summary.md（31 个任务的台账与评分） |
| **交付④打包下载** | `WIT-1989-JONES-v1.0.zip`（2.55 MB，125 个文件：两版 PDF + LaTeX 源码 + 工程脚本 + sessions 交互数据） |
| **交付②工程+源码** | **已跑通**（`deliverables/engineering/`：build.ps1、check_claims.py、check_anchors.py、make_manifest.py、export_html.py、manifest.json） |
| **交付③开源仓库** | 推送 AtomGit：`lzxSUSUY/mathtranslate` 的 `papers/WIT-1989-JONES/`（本目录精简副本，不含第三方 PDF） |

---

## 六场安排（详见 `seminar/CHARTER.md` §3）

| 场 | 主题 | 论文位置 |
|---|---|---|
| S1 | 起点 + §1 作用量 | p.351–356 |
| S2 | 几何量子化（机器） | §3.1–3.2，p.366–371 |
| S3 | Wilson 线/穿刺/BWB（载荷） | §3.3–3.4，p.371–374 |
| S4 | 共形块与 WZW（字典） | §3.2、§5，p.369–371, 394–397 |
| S5 | Verlinde（推论） | §4.3–4.5，p.384–393 |
| S6 | 对偶与范畴化（边界） | §5 + [38] + 后世 |

---

## 三条硬规矩（违反即锚点作废）

1. **页码**：`p.N` 一律指 CMP 印刷页码。「PDF 页 = N − 350」只对**原文页图/OCR**（49 张）成立；译本 PDF 是 40 页重排，定位用页边注「原文 p. N」。
2. **出处四级**：`[原文]` / `[译注]`（译本的 `% [Tutor Note]`）/ `[补]`（我们补的）/ `[后世]`（1989 年以后）。四者不许混。
3. **无锚点断言不进 `claims.jsonl`**，只能进 `questions.jsonl`。

---

## 与父项目的关系

- 制度母体：`<本地路径>`（宪章 v0.2、计划书 v0.2）。本目录只写增量。
- 规格与发布：`<本地路径>`（README、docs/00–05、schema/、papers/）。最终 `reading_note.md` 走该仓库的 100 页规格里的 H 线（本论文目标 20–35 页）。
- 上一轮试点：`papers/WIT-1990-2DGRAV`（格式锚点，闸门未真跑，**不可当质量范本**）。

---

## 成本与时间（预估）

- 讨论：6 场 × 90 分钟模拟 ≈ 9 小时；准备 ≈ 20–25 小时。
- 目标：两周出 `reading_note.md` v1。
- 预算：¥60–120（不含重译），上限 ¥150。

---

## 交付物（2026-11-13 用户定，优先级最高）

| # | 交付 | 位置 | 验收 |
|---|---|---|---|
| ① | 正儿八经的读书笔记 | `deliverables/reading_note/`（LaTeX 源 + PDF） | 20–35 页；逻辑完整回答四起点 + 七主线；把本文完整讲一遍；每章有 derivation 框与边界；编造零容忍 |
| ② | 工程文件 + 源代码 | `deliverables/engineering/` | 一条命令可重建笔记；manifest 记录每个锚点来源；claims/questions 可机读校验 |
| ③ | 开源仓库可读可用 | 本地 git → 公开仓库 | README 5 分钟上手；许可证清楚；不含 L1/L2 版权内容 |

## 待办

- [x] 三名成员交稿：文献表、已译资料清单、1988 语境与问题史。
- [x] 教材核查：河野（126 页）、李思第 5 章（PDF 309–325）。
- [x] 阅读策略二次改定（原文核心 + 教材补前置）。
- [x] S1 跑完（T 88），争议 3 条入 `seminar/争议清单.md`。
- [ ] S2 起跑（李思 5.4.3–5.4.4 前置；task-8/9/10 待发消息）。
- [ ] S3–S6 视 S2 质量决定是否合并（用户已表态最终要的是笔记，不是六场本身）。
- [ ] `deliverables/reading_note/` 章节骨架：S3 后定稿（现在定会被几何量子化细节带偏）。
- [ ] 开源仓库：本地提交 → 推送渠道（AtomGit 已有账号；GitHub 需先建号）→ 用户确认。
