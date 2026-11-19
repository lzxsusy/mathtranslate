# leanstmt —— 自然语言陈述 ↔ Lean 陈述对照语料

研究级论文里的**陈述**（定义/命题/定理）与其 Lean 4 转写之间的逐条对照语料。
不做证明层：目标是把「这句数学话在 Lean 里到底写成什么」固定下来，并让每一条都
可被机器重放检查。

## 30 秒入口

| 想看什么 | 看哪里 |
| --- | --- |
| 26 张卡的总览 | `MAP.md` |
| 字段规范 | `SCHEMA.md` |
| 一条卡长什么样 | `cards/statements/witten2008-s01.json`（及其 `md/` 渲染） |
| Lean 源码 | `lean/ShuyiFormal/Witten2015/{Statements,Gaps}.lean`、`lean/ShuyiFormal/Witten2008/{Statements,Gaps}.lean` |
| 验证怎么做 | `tools/check_lean.py`、`tools/lint_cards.py` |
| 这批是怎么做出来的 | `workflow/PRODUCTION.md` |
| 下一步找哪些文献、做哪些陈述 | `ROADMAP.md` |

## 两批范围（26 卡 = 15 certified + 11 gap）

**A 批：Witten 2015**（12 卡，10 certified + 2 gap）
底本 *More On Gauge Theory And Geometric Langlands*，arXiv:1506.04293v3（79 页；印刷页 = PDF 页 − 1）。
只取能落在现有 mathlib 上的离散/代数陈述。

**B 批：Witten 2008**（14 卡，5 certified + 9 gap）
底本 *Mirror Symmetry, Hitchin's Equations, and Langlands Duality*，arXiv:0802.0999v1（15 页；印刷页 = PDF 页）。
本文的主定理（Hitchin 纤维化上的镜像对称）恰好落在 mathlib 缺口最深的一层，
因此 B 批的 certified 卡只是若干离散/代数影子（中心 μ_N、有限 Pontryagin 对偶、
非正则奇点系数的伸缩律、函数空间 currying）。

- 轨道：`W15`（Witten 2015）、`W08`（Witten 2008）。
- scope 四值：`discrete-core`（有限群/单位根）、`algebraic-core`（对偶空间/维数/群中心）、
  `arithmetic-core`（维数账与 RH 推论）、`gap`（mathlib 缺口，`sorry` 占位）。
- certified 判据：`lake env lean` 对该文件 **0 error**、`sorry` 计数为 0、声明的 mathlib
  依赖用 `#check`/`lake env lean` 实证存在。
- gap 卡同样发布：缺口清单本身是交付物（`verification.jsonl` 与卡片 `gaps` 字段）。

## 验证环境（钉死）

| 项 | 值 |
| --- | --- |
| Lean | `leanprover/lean4:v4.36.0`（4.36.0, commit 611c117b） |
| mathlib | `d33c49ca43873d3746194325da62640cc893c9d9`（`master`） |
| 工作工程 | `C:\\Users\\admin\\Desktop\\数译发布\\shuyi\\formal`（`lakefile.lean` 里 `require mathlib ... @ "master"`） |
| 检查方式 | 逐文件 `lake env lean <file>`（**不在 LSP 里 import 全量 Mathlib**，见 `workflow/PRODUCTION.md` 事故记录） |

## 已知限制

1. 26 条仍是试点，不是全量。A 批原文 §2.4–§5 的主体（Hitchin 模空间、谱曲线、本征膜）
   几乎全部落在 gap 卡里；B 批的主定理见 G06。
2. `arithmetic-core`/`algebraic-core` 的卡只固化代数恒等式或群论骨架，几何前提没有形式化，
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
- v0.2（2026-11-19）：加入 Witten 2008 批 14 卡（5 certified + 9 gap）；轨道改为 `W15`/`W08`；
  两批合计 26 卡（15 certified + 11 gap）。
