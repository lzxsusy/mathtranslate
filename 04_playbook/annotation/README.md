# 数译知识网络 · 方案包 v0.2

> 2026-11-14。目标：让「读论文」产出三样可积累的东西——**难点标注**、**思考链**、**以概念为节点的知识网络**——并且能安全地发布出去。
> v0.2 已落进发布仓：本目录 + `04_playbook/08_论证精读与知识网络.md`；新增 D0 结构索引与 G2.5 闸门。

---

## 快速开始（5 分钟）

```powershell
$py  = "C:\Users\admin\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe"
$ann = "C:\Users\admin\Desktop\数译发布\gitee_shuyi\04_playbook\annotation"

# 1) 跑通示例（应为 units=6 inferences=4 chains=1 concepts=3，RESULT PASS）
& $py "$ann\tools\validate_annotations.py"

# 2) 过 G2.5 闸门（units≥5 / 带证据 inference≥3 / chain≥1 / claims≥50）
& $py "$ann\tools\check_gate.py"

# 3) 看真实样例：WIT S3 的难点 + SY07-08 的定理依赖
notepad "$ann\examples\units.jsonl"
notepad "$ann\index\SY07-08\SUMMARY.md"

# 4) 读方案
notepad "$ann\00_方案总览.md"
```

---

## 先读哪几篇

| 顺序 | 文件 | 你会得到 |
|---|---|---|
| 1 | [00_方案总览.md](00_方案总览.md) | 全局判断、四层模型、两周试点、四个待拍板 |
| 2 | [01_数据体检与底座修复.md](01_数据体检与底座修复.md) | 语料/结构/文档/git 的真实状态与根因 |
| 3 | [02_精读标注规范.md](02_精读标注规范.md) | unit/inference/chain 字段、难度标尺、闸门 G2.5 |
| 4 | [03_知识节点网络方案.md](03_知识节点网络方案.md) | 概念图 DDL、6 步流水线、许可分层 |
| 5 | [04_工作流改造清单.md](04_工作流改造清单.md) | 具体改哪个文件、加什么三行、prompt |
| 6 | [05_两周试点计划.md](05_两周试点计划.md) | 逐日任务与验收线 |
| 7 | [06_发布与合规.md](06_发布与合规.md) | 发什么/不发什么、mt_daily 接法 |
| 8 | [08_论证精读与知识网络.md](../08_论证精读与知识网络.md) | **落地版纪律**：G2.5、三样交付物、工具链 |
| 附 | [index/README.md](index/README.md) | D0 三本书结构索引实测 |
| 附 | [research/三路调研摘要与来源.md](research/三路调研摘要与来源.md) | 三路调研结论、来源、可信度 |

---

## 目录

```
04_playbook/annotation/
├── 00_方案总览.md
├── 01_数据体检与底座修复.md
├── 02_精读标注规范.md
├── 03_知识节点网络方案.md
├── 04_工作流改造清单.md
├── 05_两周试点计划.md
├── 06_发布与合规.md
├── README.md
├── schemas/
│   ├── unit.schema.json
│   ├── inference.schema.json
│   ├── chain.schema.json
│   ├── concept.schema.json
│   └── claim.schema.json          # v2
├── examples/
│   ├── units.jsonl                # 6 条真实单元（WIT S3 + SY07-08）
│   ├── inferences.jsonl           # 4 条推理（含 AND 合取）
│   ├── chain.json                 # WIT 主链
│   └── concepts.jsonl             # 3 个概念节点
├── claims/
│   └── wit_claims_v2.jsonl        # 73 条 WIT claims（v1→v2，只加字段）
├── index/                         # D0 结构索引（零 LLM）
│   ├── README.md                  # 三本书对比与边界
│   ├── SY07-08/{nodes,edges}.jsonl + SUMMARY.md
│   ├── SY01-11/...
│   └── SY01-23/...
├── tools/
│   ├── build_structure_index.py   # LaTeX → 节点/边
│   ├── validate_annotations.py    # schema + 交叉引用 + 无环
│   ├── check_gate.py              # G2.5 闸门
│   └── migrate_claims_v2.py       # claims v1→v2
├── templates/
│   ├── 精读标注卡.md
│   ├── 论证地图模板.yaml
│   └── 试点验收表.tsv
└── research/
    └── 三路调研摘要与来源.md
```

---

## 三条核心结论

1. **结构层是空的，但根因不是「书里没有」**：`_append_pkg.py:120-130` 的 `doc_env()` 只认英文全名环境，`thm/lem/defn` 全落成 text——91 部书只剩 1,182 段定理/证明。**所以结构索引从 LaTeX 源码建，不修语料。**
2. **已有资产比想象中好**：73 条人工 claims（锚点 100%）是现成金矿；SY07-08 通读笔记里已经写出了显式依赖链。**升级 schema，不重写。**
3. **难度不能靠 LLM 自评**：用「局部 obligation 补全失败率」+ 人工金标准校准（κ≥0.6）；边没有原文 quote 就不入库。

---

## 当前状态

| 项 | 状态 |
|---|---|
| 四层 schema | 已写（含 claim v2） |
| 校验器 | **已跑通**（示例 PASS） |
| 真实样例 | 已写（WIT + SY07-08） |
| 三路调研 | 已回，已汇总 |
| 数据体检 | 已完成（44,138 段快照） |
| D0 结构索引 | **已完成三本书**（详见 index/README.md） |
| G2.5 闸门 | **已跑通**（PASS） |
| claims v2 | **73 条已迁移** |
| 模板改造 | **已加 argument_map 节 + 3 行任务书硬规矩** |
| 两周试点 | 计划已写，**未开始**（D1 从 SY07-08 开始） |
| 发布仓改动 | **已落库**：本目录 + `08_论证精读与知识网络.md` |

---

## 需要主人拍板（详见 00 第 10 节）

1. 发布载体：现有 `site/` 加页面，还是另开 Cloudflare Pages？
2. 许可：事实层 CC0 + 标注层 CC BY 4.0（提案），是否接受？
3. 训练口径：`00_README` 与 `DATASHEET` 矛盾，二选一。

> 仓库正被每晚 21:30 的 `mt_daily` 定时任务更新；落库前先 `git status`，避免和自动任务抢同一文件。
