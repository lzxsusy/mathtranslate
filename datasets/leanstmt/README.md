# leanstmt —— 自然语言陈述 ↔ Lean 陈述对照语料

研究级论文里的**陈述**（定义/命题/定理）与其 Lean 4 转写之间的逐条对照语料。
不做证明层：目标是把「这句数学话在 Lean 里到底写成什么」固定下来，并让每一条都
可被机器重放检查。

## 30 秒入口

| 想看什么 | 看哪里 |
| --- | --- |
| 12 张卡的总览 | `MAP.md` |
| 字段规范 | `SCHEMA.md` |
| 一条卡长什么样 | `cards/statements/witten2015-s01.json`（及其 `md/` 渲染） |
| Lean 源码 | `lean/ShuyiFormal/Witten2015/{Statements,Gaps}.lean` |
| 验证怎么做 | `tools/check_lean.py`、`tools/lint_cards.py` |
| 这批是怎么做出来的 | `workflow/PRODUCTION.md` |
| 下一步找哪些文献、做哪些陈述 | `ROADMAP.md` |

## 试点范围

底本：Witten, *More On Gauge Theory And Geometric Langlands*, arXiv:1506.04293v3（79 页；
印刷页 = PDF 页 − 1）。本批只取其中**能落在现有 mathlib 上**的离散/代数陈述，
共 12 条：**10 条 certified + 2 条 gap**。

- 通轨 W（Witten 2015），scope 四值——
  `discrete-core`（有限群/单位根）、`algebraic-core`（对偶空间/维数）、
  `arithmetic-core`（维数账与 RH 推论）、`gap`（mathlib 缺口，`sorry` 占位）。
- certified 的判据：`lake env lean` 对该文件 **0 error**、`sorry` 计数为 0、
  声明的 mathlib 依赖用 `#check`/`lake env lean` 实证存在。
- gap 卡同样发布：缺口清单本身是交付物（`verification.jsonl` 与卡片 `gaps` 字段）。

## 验证环境（钉死）

| 项 | 值 |
| --- | --- |
| Lean | `leanprover/lean4:v4.36.0`（4.36.0, commit 611c117b） |
| mathlib | `d33c49ca43873d3746194325da62640cc893c9d9`（`master`） |
| 工作工程 | `C:\Users\admin\Desktop\数译发布\shuyi\formal`（`lakefile.lean` 里 `require mathlib ... @ "master"`） |
| 检查方式 | 逐文件 `lake env lean <file>`（**不在 LSP 里 import 全量 Mathlib**，见 `workflow/PRODUCTION.md` 事故记录） |

## 已知限制

1. 只覆盖 12 条，是试点，不是全量；原文 §2.4–§5 的主体（Hitchin 模空间、谱曲线、
   本征膜）几乎全部落在 2 条 gap 卡所代表的缺口里。
2. `arithmetic-core` 四卡（S08–S10、S09）只固化代数恒等式，几何前提没有形式化，
   引用时须连带 gap 卡一起看，不能当成「Hitchin 系统已形式化」。
3. 盲验回译目前是单一 reviewer（subagent），不是双盲；`verification.status` 只到
   `certified`，还没有 `reviewed`/`expert-checked` 档。
4. 本语料**不进 mathlib**，只发布原文已有陈述的重述（`rights: rewritten`）。

## 质检

```bash
python tools/lint_cards.py cards --strict      # 字段/枚举/lean 名存在性/sorry 一致性
python tools/build_index.py                     # 生成 index.jsonl
python tools/render_md.py                       # 生成 md/
python tools/check_lean.py --project <formal 工程路径> --run   # 真跑 Lean（需要 elan）
```

## 版本

- v0.1（2026-11-19）：试点 12 卡（10 certified + 2 gap）、Lean 快照入库、工具与规范落地。
