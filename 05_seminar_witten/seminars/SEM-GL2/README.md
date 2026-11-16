# SEM-GL2 威腾讨论班第二期：电磁对偶与几何朗兰兹（三文本轮读）

> 一句话：八个人先通读两篇短导读，再把 Kapustin–Witten 2006 切成八节，一节一人轮值报告；
> 每节走「报告 → 三席质询 → 修订（带 before/after diff）→ 证据核验 → 独立复算 → 语料入库」。
> 本仓库只放我们自己写的东西：原文 PDF、页图、逐页文本、整节译文一律不进。

## 读什么

| 代号 | 文本 | 页数 | 角色 |
|---|---|---|---|
| B | Kapustin–Witten, *Electric–Magnetic Duality and the Geometric Langlands Program*, hep-th/0604151 | 231 | **主文**，切成 U01–U08 |
| D | Frenkel, *Gauge Theory and Langlands Duality*, arXiv:0906.2747（Bourbaki 1010） | 32 | 全员通读的前置导读 |
| C | Witten, *Mirror Symmetry, Hitchin's Equations, and Langlands Duality*, arXiv:0802.0999 | 15 | 全员通读的前置导读 |
| A | Ben-Zvi 等 / Gukov–Witten 等中译综述 | — | 按节取用的参考扩展 |

## 八节怎么切

见 `map.yaml`。规则：区间 = `[本节标题所在行, 下一节标题所在行)`，按逐页文本行号判定，
所以 §2 的尾巴落在 p.16、§3 的尾巴落在 p.38 是正常的（不是切错）。

## 每轮五拍

1. **R-a 报告**（P1）：五栏（要解决什么 / 关键构造与推导 / 结论与重要性 / 与前后节接口 / 仍不懂 ≥3 条），每条断言带 locator。
2. **R-b 质询**（P2 ×3）：三席分工 = 推导与逻辑 / 跨文本对照（B vs C vs D）/ 页锚审计；JSONL 记录，每条带 severity 与 suggested_fix。
3. **R-c 修订**（P1）：逐条判定 接受/部分接受/拒绝，出 v2 + `report_v2.diff.md`（before/after）。
4. **R-d 核验与复算**（P4 证据官 / P5 复算员）：证据官抽核 ≥26 条 locator；复算员**自己算**关键公式并给可重跑代码。
5. **R-e 入库**（P6）：每轮 14 条语料（7 类）+ 一份讲义；过门禁后进本仓库。

## 产出

- `manuscript/U0X.md`：该节定稿讲义
- `corpus/U0X.jsonl`：该节语料（7 类，reasoning 必带 dead_end，challenge 必带 before/after diff）
- `reports/verify_U0X.md`、`reports/recalc_U0X.md`：证据审计与复算
- `reports/roundtable_U0X.md`：该轮讨论纪要

## 门禁

`tools/check_package.py --corpus/-lectures/--compliance` 三项退出码 0 才准入库；
每轮结果写在 `reports/gate_U0X.txt`（由 `check_round.py` 生成）。

## 合册与三文对读（M9）

- `volume/第二期_正稿.pdf`（198 页）与 `volume/第二期_正稿.md`：八轮定稿报告合册，含八单元一览、术语对照 27 行、质检数据表、方法与坑。
- `reports/crosswalk.md`：B/D/C 三文对读表（20 主题、抽核 53 处全中），附「三文互证最硬 / 只有 B 说」的条目。
- `reports/gaps.md`：盲区清单（物理 6 / 数学 7 / 三文冲突 5 / 方法论 6 / 下一步 10 / 留档 6）。
- `reports/training_value.md`：训练价值终评（现算 112 条语料、7 类分布、SFT/PRM/DPO 配方与风险）。

## 这一期抓到的东西（写进书里了吗）

八轮质询与复算抓出我们已发布解经本的**六处实质错误**，全部回原页图核对后重编：
U02 发现 (3.52) 共轭位置写反（v1.2 勘误，5 处）；U07 发现 §10.5 扩展 Bogomolny 方程丢横线，
顺藤摸出 §4.2 (4.11)(4.20)、§12.3 复 Hitchin 同族错误共 5 处（v1.3 勘误，5 文件 8 式）。
教训：**locator 对得上不等于公式对**。
