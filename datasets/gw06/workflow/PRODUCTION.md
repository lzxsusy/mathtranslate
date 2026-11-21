# gw06 资产生产流程（PRODUCTION）

本数据集与 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/`
（Gukov–Witten 2006, *Gauge Theory, Ramification, And The Geometric Langlands Program*,
hep-th/0612073v2 的中译校订本）同批生产。下面记录每一批是谁、用什么材料、怎么校验的，
便于复跑与追责。

## 1. 材料

| 材料 | 位置 | 说明 |
|---|---|---|
| 原文 PDF | `gw06.pdf`（160 页，arXiv:hep-th/0612073v2） | **PDF 页 = 印刷页 + 1** |
| 原文 harvmac 源码 | `src/ramified.tex`（7705 行） | 编号公式、页锚的终极依据 |
| 原文逐页文本 | `pages/p001–p161.txt` | `pdftotext -layout` 产物，供页锚核对 |
| 英文章节切片 | `en/s00-front.txt … sB-notation.txt` | 与中译分片一一对应 |
| 中译源码 | `08_source_code/SY02-06_…/源码/sections/*.tex` | 唯一锚点来源；行号随校订漂移 |

页锚格式（译者约定）：`%% ==== 原文 §2.1：PDF 第 5 页（印刷第 4 页）====`。

## 2. 校订（P1/P2）

- 14 个分片各派一个校对子代理，按 `workflow` 外的作业说明
  （`REVIEW-BRIEF.md`）逐段对照英文切片：P1 = 改变数学/物理含义，P2 = 体例与术语；
  「更通顺」不构成改动理由。
- 每个子代理只改自己那片，改动最小替换，并落一份日志 `logs/<slice>.md`：
  统计 / P1 逐条 / P2 逐条 / 页锚与公式号核验 / 存疑未改 / 新增译注 / SUMMARY(JSON)。
- 新译注（`yizhu` 环境）须含可核验断言（公式、约定、跨节引用或文献），80–260 汉字。
- 汇总：`REVIEW-NOTES.md` 逐条索引全部译注；P1 与「原文疑误」进 `cards/corrections/`。

## 3. 写卡

- 卡型两类：`concept`（每个核心概念一张）与 `correction`（每处实际改动或原文笔误判定一张）。
- 概念卡要求：自足定义（先数学后物理）、4 条以上可检验的 key_points、逐字抄录的公式、
  2 条以上「写错会怎样」的 pitfalls、三条批注（易错预警 / 含糊点拨 / 背景直觉各一）。
- 锚点：`08_source_code/SY02-06_…/源码/sections/<slice>.tex:<起>-<止>`。
  校订轮期间行号会漂移，**写卡前必须重新生成 `tools/section_index.json`**
  （由 `sync_repo.py` 抽取），不得沿用旧行号。
- 三批生产：exemplar 3 张（landing 卡，定风格）→ 分片代理按 `CARD-BRIEF.md` 各写各的 →
  总编统一补 related、跑严格校验、写 README/MAP。

## 4. 校验

```bash
cd datasets/gw06/tools
python make_cards.py --check --allow-missing-related   # 分批期间
python make_cards.py --strict                          # 收尾：0 error 0 warning
```

校验覆盖：id 唯一、track 形如 `§3.2`/`附录A`、summary ≤ 120 汉字、question 问号结尾、
annotations 三型且带 title/text、related ≥ 2 且可解析、sources 的 `pdf_pages = pages + 1`、
anchor 文件存在且行号在文件内、概念卡 key_points/formulas/pitfalls 数量、
勘误卡 corrected 片段确实出现在 anchor 区间、published 必须 external-confirmed。

## 5. 已知边界

- 未做 Curr. Dev. Math. 2006 印刷本的页面对照；页锚以 arXiv v2 为准。
- 概念卡的论证只到「与译文源码一致」这一级；未逐条对现代文献做外部确认，
  故全部 `verification.status = source-only`。
- 原文自身疑误（如 p083 的 `S: τ → −1/n_g τ` 排版、p016 的 Im τ 因子）
  按「照录 + 译注 + 勘误卡」处理，不改动数学内容。

## 6. 与仓库现行卡片范式的对齐

仓库里「卡片」有两层，gw06 两层都做了，内容互为镜像：

| 层 | 位置 | 读者 | 形态 |
|---|---|---|---|
| 阅读资料卡 | `08_source_code/SY02-06_…/资料卡/`（00-速览 / 01-结果清单 / 02-论证地图 / 03-条款索引 / 04-术语文献勘误） | 人，先读这个再进正文 | Markdown，五件套命名与 `10_gmn_series`、`SY01-27` 一致 |
| 数据集卡 | `datasets/gw06/cards/**/*.json` | 机器/检索，可逐卡复用 | JSON + `make_cards.py` 渲染出的 `md/` |

写作口径（两层通用）：

1. **锚点先于断言**：每句技术断言都要能落到 `源码/sections/sNN-*.tex:A-B`；写卡前先跑
   `sync_repo.py`，再用 `section_index.json` 取行号，不凭记忆。
2. **不复制原文**：英文短引 ≤ 120 字符，中文只写改写后的表述；勘误卡的 `original`/
   `corrected` 只保留差异片段。
3. **诚实标核验级别**：默认 `source-only`；只有逐页对过印刷本才能升 `external-confirmed`，
   升了才能把卡设成 `published`（本轮全部 `reviewed`）。
4. **批注三型各有分工**：`易错预警` 写「最容易写错/读错的那一步」，`含糊点拨` 写原文一句话
   带过但需要展开的地方，`背景直觉` 写「为什么这样定义是自然的」。三型各一条，不重复正文。
5. **与校订互锁**：cards/corrections 的每张卡对应 `校对报告.md` 里一条 P1/P2 或一处理论疑误；
   新增勘误卡时先补报告，再补卡，避免两处数字对不上。
