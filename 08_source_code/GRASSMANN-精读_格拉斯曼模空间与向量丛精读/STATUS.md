# 进度台账（STATUS）

> 唯一真相来源。Lead 每完成一个 phase / 收到一章就更新一次，**不要重复做已完成的事**。
> 状态枚举：`todo` / `running` / `done` / `partial`（读不懂的部分已注明）/ `failed`

最后更新：2026-11-25 19:42 · **全部 Phase 完成**（九章 PASS；90 张卡，`--strict` 0 error；汇总文件齐）

## 总状态

| Phase | 状态 | 备注 |
|---|---|---|
| 0 · 预热 | done | preflight 0 FAIL；81 条译注在位；ch1 首页渲染正常 |
| 1 · 全书导读 + 台账骨架 | done | `产出\导读\00-全书导读.md` 六节；审校方法/交叉引用/术语增补/修订补丁骨架齐 |
| 2 · 九章精读 + 审校 | done | 9×6 文件全齐；`tools\check_chapter.py --all` 九章全 PASS（ALL PASS，19:40 复跑） |
| 3 · 资料卡（`..\_cards_grassmann`） | done | 90 张（概念 73 / 例子 17）；`validate_cards.py --strict` **0 error / 0 warn**；`build_index.py` → `index.jsonl` 90 行 + `md\INDEX.md` |
| 4 · 汇总 | done | `00-审校总表.tsv` 58 条；`00-修订补丁.md`（六节）；`README.md`、`stats.tsv`、`交叉引用.md`（15 条跨章点 + 术语抽查）、`术语增补.tsv`（19 行）、`审校方法.md` |

## 章进度（全部 PASS）

| 章 | 中译页 | 已有译注 | 导读(字) | 批注 | errata | 笔记(字) | 卡片候选 | 状态 |
|---|---|---|---|---|---|---|---|---|
| ch1 | 7–29 | 8 | 1492 | 16 | 10 | 1773 | 10 | PASS(partial) |
| ch2 | 30–54 | 14 | 1676 | 16 | 5 | 2100 | 15 | PASS(partial) |
| ch3 | 55–71 | 5 | 1412 | 18 | 6 | 1735 | 9 | PASS(partial) |
| ch4 | 72–81 | 3 | 1957 | 19 | 7 | 2662 | 7 | PASS(partial) |
| ch5 | 82–93 | 7 | 2124 | 18 | 10 | 2934 | 10 | PASS(partial) |
| ch6 | 94–115 | 13 | 1691 | 18 | 8 | 1817 | 10 | PASS(partial) |
| ch7 | 116–134 | 6 | 1996 | 18 | 3 | 2029 | 10 | PASS(partial) |
| ch8 | 135–159 | 18 | 1609 | 19 | 5 | 2066 | 11 | PASS(partial) |
| ch9 | 160–170 | 7 | 1712 | 17 | 4 | 2305 | 7 | PASS(partial) |
| 合计 | 7–170 | 81 | 15669 | 159 | 58 | 19421 | 89→90 卡 | — |

## 卡片进度（Phase 3，全部 done）

| 组 | 范围 | 张数 | 任务书 | 报告 | 状态 |
|---|---|---|---|---|---|
| 甲 | A + ch1 + ch3 | 22 | `tmp\cardtask-甲.md` | `产出\汇总\card甲-report.md` | done（18 概念 + 4 例子；6 张 sketch） |
| 乙 | ch2 + ch7 | 22 | `tmp\cardtask-乙.md` | `card乙-report.md` | done（14 + 8；12 张 sketch） |
| 丙 | ch5 + ch8 | 19 | `tmp\cardtask-丙.md` | `card丙-report.md` | done（15 + 4；4 张 sketch） |
| 丁 | ch4 + ch6 + ch9 | 24 | `tmp\cardtask-丁.md` | `card丁-report.md` | done（20 + 4；12 张 sketch） |
| 合计 | — | 90 | — | 四份组报告 | 概念 73 / 例子 17；track 分布 A=3, 1=10, 2=14, 3=9, 4=7, 5=9, 6=10, 7=11, 8=10, 9=7 |

- 全量 id 表：`tmp\cards-ids.md`；施工计划：`tmp\cards-plan.tsv`；清单：`..\_cards_grassmann\taxonomy.md`；索引：`..\_cards_grassmann\md\INDEX.md`。
- 校验器坑已修：绝对路径正则原会把 `$d:\text{…}$` 误判，现只在「盘符:\段\」真路径上报错（`tmp\patch_validator.py`）。
- 合并记录：ch7 的 `alpha-stability` 并入种子 `alpha-stable-coherent-system`（其 aliases 已收），taxonomy 去重记录不再用反引号列该 id——这是 `--strict` 通过的关键一步。

## 已知缺口（partial 原因一句话版）

- ch1：§4 式(22) `V[c^(1)]` 的变分来源、§3 式(17) 疑恒等式。
- ch2：Hilbert 概形描述（定理 2.10）、`dim W¹_{n+δ}≥2δ`（定理 4.12/4.13）、猜想 5.8 量词。
- ch3：推论 3.9(ii) 的 `C²≥1` 整性一步、命题 3.8(b) 的 D 来源。
- ch4：式(2)(10) 右端多一个 D；定义 5.1 与定理 5.6 的类型不平衡。（本章实测「中译 = 原书 + 2」）
- ch5：Lemma 3.2 的开邻域、两版本对角纤维维数不齐、Remark 2.10「too large」。
- ch6：§5.2 粘合下降数据（需 [19]）、A.2.3(2) Lang–Weil 计数。
- ch7：例 7.5 中「dim Ker ψ≥4 ⇒ 式(8) 不单射」一步。
- ch8：已 complete（只有 6 条存疑待商）。
- ch9：§4 扭转符号与度数记账、§6 算例维数 6 vs ρ=5（需 [T1]）。

## 口径备忘

- errata 表头 **10 列**：chapter loc_book loc_zh loc_tex type severity original problem suggestion evidence。
- 「中译 p.N」= 中文 PDF 的 PDF 页；ch9 页脚印刷号 = PDF 页 − 6。
- 页表：前言 1–6 / ch1 7–29 / ch2 30–54 / ch3 55–71 / ch4 72–81 / ch5 82–93 / ch6 94–115 / ch7 116–134 / ch8 135–159 / ch9 160–170。
- ch5 已有译注 7 条内容全部正确，但其中 5 条（第 2、4、5、6、7 条）的中译页比实际大 1（注 2 标中译 p.86，实文在 PDF p.85，已用文字层验过）——只影响元数据，不影响判断。
- 恢复/复跑：`python tools\preflight.py` → `check_chapter.py --all` → `merge_errata.py` → `_cards_grassmann\tools\validate_cards.py --strict` → `build_index.py` → `tools\build_summary.py`。
