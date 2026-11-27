# 12_sandbox · 数译数学沙盒

> **永久免费、开源、不商业化。** 把前沿数学做成大模型可以反复跑、编译器可以判对错的环境；就算没人拿它当沙盒，它也是一份可检索、可引用、可训练的中文数学语料。

## 一句话

中文数学语料不缺产量，缺的是「每个判断都能被机器裁定对错」的环境。这个目录就是那个环境的工地。

## 为什么做

- 国内的大模型公司不一定有人系统地做「研究级数学 + 形式化 + 中文」这件事。我们先做，做出来放在网上；他们哪天发现了，可以直接用。
- 研究级形式化远未饱和：FATE 最好模型在 FATE-H 上只有 3/100，FATE-X 没有任何有效 Lean 证明；TCSEXAM 研究级 Lean 最好 70%、第二 38%。瓶颈不是证明搜索，是**定义缺口**和**判断是否忠实**。
- 现有 benchmark 饱和太快：miniF2F 已被打到 100%，FrontierMath T4 在 2026-09 被刷到 97.6%。研究级、有出处、抗污染的数据是空位。
- 我们的本意是支持这件事，不是拿它收费。**我们不做收费产品，也不把知识锁起来。**

## 原则

1. **免费开放**：代码、陈述、Lean、判分脚本，能公开的都公开；不设付费墙、不做商业授权、不卖数据。
2. **编译器裁判**：`verification.status` 只认编译器；0 error + sorry=0 = certified；LLM 自评只作辅助。
3. **页码锚定**：每条陈述带 paper / page / display；可追溯、可核验、抗污染。
4. **可复现**：陌生人 clone 后一条命令跑通；Docker + 钉死 Lean/mathlib 版本；CI 绿灯才算数。
5. **不造影子**：certified 分 `full`（真陈述）与 `shadow`（特殊/离散情形）；headline 只用 full。
6. **陈述与证明分离**：statement 文件冻结，只允许改 proof 文件；防弱化、防空泛。

## 立项文档

- `docs/04_形式化立项_2026-11-27.md`：两条车道（地基 / 定义库）、节拍、验收、止损。**形式化从这里读起。**
- `docs/工作日志.md`：每次自动运行追加一条，含编译器实测数字。

## 四层

| 层 | 内容 | 现在 |
|---|---|---|
| L0 语料 | 142 部译注 / 51,009 段 / 417 万汉字 / 2,214 术语 | 已有 |
| L1 陈述 | 页码锚定中文陈述 + 依赖 + formalizable 状态 | 43 张 Lean 卡 + 1,764 张资料卡 |
| L2 形式化 | full / skeleton / gap 三轨 | 43 卡 = 21 certified（多为 shadow）+ 22 gap；8 个 `.lean`，全文件编译 exit=0 |
| L3 沙盒 | Docker + 编译/判分 API + 任务生成器 | **动工**：复现工程文件已进仓（`datasets/leanstmt/lean/`），Docker/CI 见 `docs/04_形式化立项_2026-11-27.md` |
| L4 对局 | 复谱 / 补步 / 对译 / 出题 + 段位榜 | 设计阶段 |

## 现在有什么

- `datasets/leanstmt/`：43 张卡（21 certified + 22 gap），8 个 Lean 文件，Lean 4.36.0 + mathlib d33c49ca（已钉死，`lakefile.lean` 在 `lean/` 下，一条命令可复现）。
- `datasets/`：1,676 张资料卡（42 集），含 GLC 154 卡、nLab DAG 67 卡等。
- `11_card_audit/`：100 张抽样审计（32 卡 / 104 处）、GLC 154 卡全量（25 卡 / 56 处）、每日 20 卡外部核验。
- `kb/`：SQLite 2,938 卡 + FTS；`kb/DESIGN_claim_graph.md` 检索设计草案。
- `shuyi/formal/`：Lean 工程（ShuyiFormal），含 lakefile / lean-toolchain / lake-manifest。

## 目录

```text
12_sandbox/
├── README.md                    # 本文件：愿景、原则、现状
├── docs/
│   ├── 00_顶层设计报告_v0.1.md    # 原始设计（存档，不删不改）
│   ├── 01_定位与采用.md           # 免费开放下，怎么被看见/用/引用/贡献
│   ├── 02_路线图.md               # 90 天 + 12 个月，带验收标准
│   └── 03_给大模型公司的一页说明.md
├── env/                         # Docker / lakefile / CI（待建）
├── api/                         # 编译/判分服务（待建）
├── harness/                     # pass@k / Elo / 防作弊（待建）
└── bench/                       # 基准任务与榜单（待建）
```

## 怎么用（现在）

```bash
git clone <repo>
cd shuyi/formal
lake build
```

对外预览（待上线）：HuggingFace 数据集 + 静态 Gap Atlas + GitHub Action。不自建 API，需要时用 Lean4Web / HF Spaces / OpenReward。

## 路线图

见 [`docs/02_路线图.md`](docs/02_路线图.md)。90 天只做三件：复现性、40 卡 preview、基线 + workshop 论文。

## 许可

- 自产层（陈述、Lean、判分脚本、文档）：CC BY 4.0。
- 译文层：演绎作品，不额外设限，但**不用于商业授权**；对外只做 clean-room 导出（事实 + 页码锚 + Lean + 自写注记），不打包译文原文。
- 原文 PDF 不发布。

## 贡献

- 提 issue：指出一条陈述的页码 / 形式化 / 判定问题。
- 提 PR：补一条 gap、修一个 proof、加一个 baseline。
- 不需要付费，也不需要许可；引用即可。
