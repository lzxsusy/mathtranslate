# SY02-08《圈群的 Langlands 对应》中文译注本 v2 —— 工程说明（BRIEF）

## 1. 项目身份

| 项 | 内容 |
|---|---|
| 编号 | SY02-08 |
| 原名 | Edward Frenkel, *Langlands Correspondence for Loop Groups* |
| 丛书 | Cambridge Studies in Advanced Mathematics 103 |
| 出版 | Cambridge University Press, 2007（406 个 PDF 页；正文 p.1–392） |
| 中译名 | 《圈群的 Langlands 对应》 |
| 版本 | v2 校订译注版（2026-11-23 起） |
| 上一版 | 327 页，10 章 41 节 164 小节，386 个编号公式，372 条源码批注，约 17 万字 |
| 许可 | 演绎作品；底本权利归原作者与 CUP；本库不代原作者授权，权利人通知即撤 |

## 2. 这本书讲什么

Frenkel 把经典局部 Langlands 对应中的局部域 \(\F_q((t))\) 换成 \(\C((t))\)，把离散群 \(G(F)\) 换成形式圈群 \(G(\C((t)))\)，把向量空间上的表示换成范畴上的表示（Hecke 特征层、D-模），从而把 Langlands 对应解释为仿射 Kac–Moody 代数在临界水平的中心与 opers 的关系。全书从经典局部对应出发（第 1 章），依次建立圈群表示、顶点代数、Wakimoto 模、临界水平中心、Miura 变换与 opers（第 2–9 章），最后在整体情形给出几何 Langlands 对应的 Hecke 特征层构造（第 10 章）。

## 3. 本版做了什么（v2）

1. **重校订**：18 份旧单元报告 + 372 条旧批注 + 96 条原书疑似笔误逐条复核；修误译、漏译、中文、术语、编号。
2. **正式译注**：源码里的 `% [Tutor Note: ...]` 升级为编译后可见的脚注（`\transnote`），每条带来源或“译者按”，全书落成 **243 条**（241 条有来源，2 条译者按）。
3. **新增前置知识导引**（`chapters/front-prereq.tex`）：李代数与泛包络、中心扩张与上循环、仿射 Kac–Moody、顶点代数与 Wakimoto 模、D-模与 Hecke 本征层、Hecke 算子。
4. **新增 2007 年后进展**（`chapters/back-progress.tex`）：几何 Langlands 的 2024 年五篇预印本（未分歧情形）、q-特征标与 q-Langlands、对「opuscule」的术语核查、W-代数与 class S、Kapustin–Witten 的后续。严格区分已证（预印本）/部分结果/猜测/未核实；书中已更正任务书里「q-特征层」「opuscule 表示」两处不存在的术语。
5. **资料卡**：`资料卡/` 五件套 + `对齐卡/index.jsonl`。

新增两章用 `\chapter*` + `\addcontentsline`，**不改变原书第 1–10 章编号**。

## 4. 目录结构

```
SY02-08_圈群的Langlands对应\
├─ 施工计划.md                 工程计划与批次
├─ 投稿信息.md                 投稿元数据（入仓时更新为 v2）
├─ 工程文件\
│  ├─ BRIEF.md                 本文件
│  ├─ STYLE_GUIDE.md           体例与写作规范
│  ├─ STATUS.md                进度台账
│  ├─ work\                    glossary.tsv、旧批注台账、诊断底稿、章节 briefs、notes、changes
│  └─ reports\                 原 28 份报告 + 诊断报告_v2.md + formula-fixes.tsv
├─ 源码\
│  ├─ main.tex  preamble.tex
│  └─ chapters\                23 个原书分片 + front-prereq.tex + back-progress.tex
├─ 成品\圈群的Langlands对应_中文译注本_v2.pdf
├─ 资料卡\                     00–04 五件
│  └─ 对齐卡\index.jsonl       6 张
```

## 5. 编译

```bash
cd 源码
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
```

- 引擎：XeLaTeX（ctexbook，11pt，A4）。
- MiKTeX 路径：`C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe`
- 要求：0 error、无 undefined reference、无 Missing character；overfull 逐条处理。
- 成品 PDF 与 `源码\main.tex` 必须同源。

## 6. 章节与页范围

| 文件 | 内容 | 原书 PDF 页 |
|---|---|---|
| ch01-1 | 第 1 章 局部 Langlands 对应，§1.1 经典理论 | 15–22 |
| ch01-2 | 第 1 章 §1.2–§1.6（复域上的 Langlands 参数、圈群表示） | 23–44 |
| ch02 | 第 2 章 顶点代数 | 45–74 |
| ch03-1 | 第 3 章 构造中心元，§3.1–§3.3 | 75–94 |
| ch03-2 | 第 3 章 §3.4–§3.6（射流概形、sl₂ 情形） | 95–114 |
| ch04 | 第 4 章 Opers 与一般李代数的中心 | 115–139 |
| ch05-1 | 第 5 章 自由场实现，§5.1–§5.3 | 140–153 |
| ch05-2 | 第 5 章 §5.4–§5.6（顶点代数解释、2-上循环） | 154–176 |
| ch06 | 第 6 章 Wakimoto 模 | 177–208 |
| ch07 | 第 7 章 交织算子 | 209–231 |
| ch08 | 第 8 章 中心与 opers 上函数代数的等同 | 232–260 |
| ch09-1 | 第 9 章 临界水平 $\hat{\mathfrak{g}}$-模的结构，§9.1–§9.3 | 261–283 |
| ch09-2 | 第 9 章 §9.4–§9.6（表示范畴、Verma/Weyl 模自同态） | 284–314 |
| ch10-1 | 第 10 章 构造 Langlands 对应，§10.1–§10.2 | 315–325 |
| ch10-2 | 第 10 章 §10.3 无分歧情形 | 326–347 |
| ch10-3 | 第 10 章 §10.4 温和分歧情形 | 347–374 |
| ch10-4 | 第 10 章 §10.5 从局部到整体 | 375–388 |
| appendix | 附录 A 李代数、泛包络代数、单李代数、中心扩张、仿射 Kac–Moody 代数（A.1–A.5） | 389–395 |
| glossary | 附录 B 术语表（译者增补） | — |
| front-prereq | 前置知识导引（v2 新增） | — |
| back-progress | 2007 年后的进展（v2 新增） | — |

## 7. 关键约定

- 公式原则上零改动；仅旧译转写错误且页图 + 第二独立出处齐备时改正，本版共 7 处，记 `reports/formula-fixes.tsv`。
- 原书笔误保留原文 + 译注说明，不擅改。
- 译注机制：`\transnote{...}`（preamble 定义，编译为【译注】脚注）。
- 术语裁决：`work/glossary.tsv`。
- 来源黑名单：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记。
- 不把出版社 PDF、页图、文字层放进仓库。

## 8. 验收（对应 17 号规范 §7）

- [x] 三遍 xelatex，0 error；成品 364 页。
- [x] 术语登记 `work/glossary.tsv`（206 条）。
- [x] 资料卡 01/03 带页码。
- [x] 对齐卡 6 张，rights=rewritten。
- [x] RELEASE_REGISTER、03_translations_meta、CHANGELOG 同步。
- [x] `make_stats.py --write` 后 README 统计与实物一致（125 部 / 1,232 卡）。
- [x] 投稿信息 tier C→A。
