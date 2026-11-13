# 工作流：这份讲义是怎么被生产出来的

本目录记录 WIT-1989-JONES 研讨班的生产流程、角色分工与可复现步骤。
它回答三个问题：谁做了什么、数据怎么流动、别人怎么重跑。

## 1. 三层产物

```
sessions/s1 … s6/        过程证据：议程、报告、质询、逐字记录、claims/questions、评分
materials/               底料：文献表、已译资料清单、语境史、教材核查、外部参照
deliverables/
  reading_note/          注疏版（97 页）：与原文逐句对照，查证用
  lecture/               讲义版（50+ 页）：连续叙事，可当课程主文本
  engineering/           构建脚本、校验器、manifest、HTML 导出
  workflow/              本目录：流程说明与交互数据索引
```

## 2. 角色

| 角色 | 职责 | 产出 |
|---|---|---|
| Lead（主席） | 定议程、派活、写收束、终审、对外交付 | transcript、lecture、README |
| historian | 语境与问题史（T0/T5/T6 主线） | materials/1988语境与问题史.md、s*/reports/A_* |
| bibliographer | 文献与书目（T1–T4 主线） | materials/文献表.md、s*/reports/B_* |
| archivist | 证据官：锚点抽检、教材对照、errata | s*/challenges/证据官_*、appD_errata |
| verifier | 独立评分：只读 claims/questions 与原文，不读报告 | s*/score.md |
| writer-1/2 | 讲义章节代笔（ch05/06、ch09/10） | deliverables/reading_note/chapters/ch05、ch06、ch09、ch10 |

## 3. 一场讨论会的数据流

```
agenda.md  ──►  两名报告人各写 reports/*.md（800–1500 字，带 [src p.N]）
            ──►  证据官写 challenges/*.md（300–600 字，点名句子/公式）
            ──►  Lead 写 transcript.md（保留分歧）+ claims.jsonl + questions.jsonl + one_pager.md
            ──►  verifier 独立评分 score.md（抽检 3–5 条，任一条 fabricated → T<75）
            ──►  不合格则 Lead 修数据（见 sessions/_schema_fix_log.md），再请 verifier 复审
```

数据格式：
- `claims.jsonl`：`id / session / claim / type(definition|conjecture|evidence|interpretation|open) / anchors / source(witten|reconstruction|post-1990) / confidence / status(active|contested|refuted) / counterpoints`
- `questions.jsonl`：`id / session / question / target / why_open / attempts / status`
- 锚点写法：`[src p.370]`（原文页码）、`[eq 3.4]`（原文公式号）、`[河野 p.60]`、`[Moore 中译 p.92]`、`[我们]`（本组推导）。

## 4. 六场议题

| 场 | 主题 | 报告 A | 报告 B |
|---|---|---|---|
| S1 | 问题从哪来；§1 作用量与 k 整性 | historian | bibliographer |
| S2 | 相空间、预量子化、极化 | historian | bibliographer |
| S3 | 穿刺点、BWB、G/T 量子化 | historian | bibliographer |
| S4 | 共形块与 WZW：对应是什么级别 | historian | bibliographer |
| S5 | Verlinde：从共形块到融合规则 | historian | bibliographer |
| S6 | 两种对偶；纽结范畴化 | historian | bibliographer |

## 5. 质量闸门

1. 每条实质断言必须有锚点；锚点错或把猜想写成定理 → contested，该场不进语料。
2. verifier 独立评分（T1 原子性 / T2 依据闭合 / T3 分支修复 / T4 边界置信 / T5 可机读 / T6 反事实迁移）。
3. 数字必须能被脚本复算（`deliverables/engineering/scripts/`），结果写进报告。

## 6. 复现

```powershell
# 讲义（50+ 页）
cd deliverables/lecture
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex

# 注疏版（97 页）
cd deliverables/reading_note
xelatex -interaction=nonstopmode -jobname=lecture main.tex

# 数据校验 + 锚点校验 + manifest + HTML
cd deliverables/engineering
powershell -NoProfile -ExecutionPolicy Bypass -File build.ps1
```

依赖：TeX Live / MiKTeX（xelatex + ctex + fandol + tcolorbox + longtable）、Python 3（仅标准库）。

## 7. 记录与版权

- 读者交互数据（报告、质询、评分）保留在 `sessions/`，是生产的原始记录。
- Witten 原文版权属 CMP；本仓库只提供中文译注与解读，不附原文 PDF。
- 引用原文页码一律用 CMP 印刷页（351–399）。
