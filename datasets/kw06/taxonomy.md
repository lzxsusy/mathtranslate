# 分类与关系

## 两类卡

| 类型 | id 前缀 | 回答的问题 | 关键字段 |
|---|---|---|---|
| 概念卡 | `kw/concept/` | 这是什么、为什么需要、哪里会错 | `definition` `key_points` `formulas` `theorems`（含 proof 状态）`pitfalls` |
| 推导卡 | `kw/deriv/` | 这条论证怎么一步步走通、每步凭什么 | `setup` `steps`（每步 `why` `locator` `provenance`）`result` `gaps` |

## 五条轨道（track）

| track | 名称 | 在论证链上的位置 | 原文页 |
|---|---|---|---|
| A | 四维物理与对偶 | 出发点：$N=4$ SYM、$\tau$、S-对偶、GNO/Montonen–Olive、$^LG$、Table 1 | 2–16 |
| B | 扭化与拓扑 | 方法：GL 扭化、一族 4d TFT、$\mathbb{CP}^1$ 参数族、消失定理、$\Psi$ | 16–38 |
| C | 舞台：曲线与模空间 | 场地：Riemann 面、Higgs 丛、$\mathcal M_H$ 超凯勒商、Hitchin 纤维化、可积性 | 38–56 |
| D | 二维、膜与算子 | 接口：2d sigma 模型、A/B-模型、镜像、A/B-膜、Wilson/'t Hooft 算子、特征膜 | 56–123 |
| E | Langlands 与翻译器 | 结论：Hecke 修改与特征层、仿射 Grassmannian、Bogomolny、c.c. 膜、D-模、§12 检查表 | 123–222 |

## `related` 的语义

本数据集用**扁平关系表**（不引入边类型），语义按两张卡的类型决定：

- 概念卡 ↔ 概念卡：概念上的依赖或对照（「没有它就没有它」）。
- 概念卡 ↔ 推导卡：这张卡是那条推导的**要素**（推导卡 `related` 里出现的概念），或反过来。
- 推导卡 ↔ 推导卡：**前后接力**（前一条的 `result` 是后一条的 `setup`），或同一结论的两种走法（例如 `sdual-mirror` 与 `generalized-complex`）。

## 数值索引

- 概念卡 40 张：A 8 / B 6 / C 10 / D 8 / E 8。
- 推导卡 27 张：A 3 / B 5 / C 4 / D 6 / E 9；合计约 100 步。
- 体量：概念卡均 ~0.6 KB 级文本；推导卡均 4–8 步，每步带 locator 与 provenance。

## 与仓库里其他数据的关系

| 数据集 | 粒度 | 用途 |
|---|---|---|
| `datasets/math/` | 命题级（陈述 + 自足上下文 + 证明步骤） | 训练数学推理 |
| `datasets/traces/` | 事件级（一次工程里 AI 怎么决策） | 训练过程/奖励模型 |
| `datasets/kw06/`（本目录） | **卡级**（概念 + 推导，带出处与可信度） | SFT 讲义化问答、PRM 步骤监督、检索增强的 ground truth |

三者共享同一套出处规范（印刷页 + 式号），可以互相 join：`kw06` 的推导卡步 ↔ 讨论班 `GL2-*` 语料 ↔ 解经本锚点。
