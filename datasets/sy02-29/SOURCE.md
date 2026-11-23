# 投稿信息 · SY02-29

TRANSLATION-STANDARD:v2.1 施工标准

## 一、书目

| 项 | 内容 |
| --- | --- |
| 编号 | SY02-29 |
| 原作 | Geometrization of the local Langlands correspondence: an overview |
| 作者 | Laurent Fargues（CNRS, IMJ, 4 place Jussieu, 75252 Paris） |
| 主题 | 局部 Langlands 对应的几何化纲领综述：Fargues–Fontaine 曲线、Bun_G 叠、B_dR-仿射 Grassmann 簇与 Hecke 叠、几何 Satake、F-等晶体与 p-可除群的两周期态射、Kottwitz 猜想 |
| 出处 | 作者 2016-02-02 预印本（page 46；ANR-14-CE25 PerCoLaTor 资助） |
| 中译名 | 局部 Langlands 对应的几何化：综述 |
| 体例 | 单篇综述，9 节 + 文献 32 条；页码与 PDF 页一致（偏移 0） |
| 学科 | 数论 / 算术几何 / p-进几何 / 几何 Langlands |
| 难度 | 极高（完满空间、菱形、v-层、六函子直觉同时在线），但**可读性远高于 SY02-26 的 356 页正文** |
| 篇幅 | 原文 46 页；译本 **62 页**（含前置件与 96 条译注） |

## 二、交付物

```
SY02-29_局部Langlands几何化综述/
├── README.md
├── 源码/
│   ├── main.tex / preamble.tex / build.bat
│   └── sections/
│       ├── s00-front.tex        ← 摘要 + 译本说明
│       ├── s01-intro.tex        ← 导引（p.1–3）
│       ├── s02-curve-a.tex      ← §1.1–1.4（p.3–10）
│       ├── s03-curve-b.tex      ← §1.5–1.6（p.10–16）
│       ├── s04-bung.tex         ← §2（p.16–23）
│       ├── s05-grassmannian.tex ← §3（p.23–28）
│       ├── s06-statement.tex    ← §4（p.28–29）
│       ├── s07-character.tex    ← §5（p.29–30）
│       ├── s08-fisoc.tex        ← §6（p.31–34）
│       ├── s09-compat.tex       ← §7（p.34–36）
│       ├── s10-kottwitz.tex     ← §8（p.36–42）
│       ├── s11-abelian.tex      ← §9（p.42–46）
│       └── s99-bibliography.tex ← 文献表（p.46）
├── 工程文件/
│   ├── BRIEF.md / SPEC.md
│   ├── reports/  ← r-lead、r-curve-a、r-curve-b、r-bung、r-grass、r-charfisoc、r-kottwitz、r-abelian、lead-log
│   ├── work/     ← 通读笔记、疑点清单、glossary、trace-*、TASK-translator、src/（逐页文本）、pages/（页面图）
│   └── tools/    ← render_pages.py
├── 资料卡/
│   ├── SCHEMA.md
│   ├── cards/concepts/  ← 概念卡（轨道 A–E + 符号索引）
│   ├── cards/derivations/ ← 推导卡
│   └── tools/  ← lint_cards.py、verify_quotes.py
└── 成品/
    └── SY02-29_局部Langlands对应的几何化_全本.pdf
```

## 三、质量记录

| 门 | 结果 |
| --- | --- |
| 整书编译 | `main.pdf` **62 页**，0 error，0 Overfull，0 undefined ref，0 Missing character |
| 页锚 | `.pagemarks` 覆盖 p.1–p.46，46/46 无缺页 |
| 编号 | 定义 20、命题 34、定理 12、引理 1、推论 9、例 5、猜想 7、期望 3、注 30，与原文逐条一致（PDF 抽取比对） |
| 译注 | 96 条（`\yizhu` 50 + `\yizhuw` 46），全部带来源或标「（无外部依据）」 |
| 语言 | 「被……所」「进行……的」「对于……而言」全书 0 处 |
| 术语 | 87 条冻结表，交付前 grep 旧译法 = 0 |
| 疑点 | 54 行（49 已解 / 5 待核），「未解」= 0 才开译 |
| 资料卡 | `lint_cards.py --prefix sy29 --max-pages 46`、`verify_quotes.py --strict` 均 0 错误 |

## 四、勘误（原文，节选；全表见 `工程文件/work/疑点清单.tsv`）

| 序 | 位置 | 原文 | 判定 | 处置 | 置信度 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| E1 | p.10 例 1.19 | `Z_p^cyc = W(F_p[[T^{1/p^∞}]])/(1+[1+T^{1/p}]+⋯+[1+T^{(p-1)/p}])` | 该元素经 θ 的像非零，疑非本原元 | 照排 + 待核 | low | open |
| E2 | p.13 §1.5.3 / p.26 §3.3.2 | 标题作「equal characteristic」，正文假设 `[E:Q_p]<+∞` | 标题笔误 | 按内容改题 + 译注 | high | fixed |
| E3 | p.30 | `Kottitz` | 应为 Kottwitz | 照排 + 译注 | high | fixed |
| E4 | p.39 | `Gr^{≤μ,b} ⊂ Gr^{≤−μ}` | 应为 `⊂ Gr^{≤μ}` | 照排 + 译注 | high | fixed |
| E5 | p.32 | `𝔻_S = 𝒴_{S,[0,1[} ⊂ 𝒴_{S,]0,1[} = 𝔻_S^*` | 包含关系按集合论不成立 | 照排 + 待核 | low | open |
| E6 | p.37 vs §8.1 末 | Tate 扭转 `((n−1)/2)` 与 `((1−n)/2)` 并存 | 二者差整体平移 | 照排 + 待核 | medium | open |
| E7 | p.42 命题 9.1(2) | `←h^*T_{d+k} ≅ →h^*T_d ∧ LT^{−k}` | 指标 `d+k` 存疑 | 照排 + 待核 | low | open |
| E8 | p.36 §8.1 | `b` 的矩阵式（`−1` 次幂、缺项位） | 排版歧义 | 照排 + 待核 | low | open |
| E9 | 全篇 | `interpreated`、`affinoid perfctoid`、`faithfull`、`crsytalline`、`Weirstrass`、`coindices`、`rationnal`、`on should`、`wether`、`We thus deduces`、`has has`、`a a`、`the the`、`this this`、`we 𝔻(H̃_Q) is`… | 拼写/衍字 20 余处 | 照排 + 译注 | high | fixed |

## 五、说明

- 本包为**全本**（46/46 页），不是节译。§1–§9 与文献表齐备。
- 底本 PDF 与逐页文本 `工程文件/work/src/` **不入仓**，只随本地工程保留；仓内不含底本 PDF。
- 术语以 `工程文件/work/glossary.tsv` 与 `reports/lead-log.md` §2 为唯一裁决源。
- 页锚 `\srcpage{N}` 排页边，供读者跳回原文页；文件边界处重复一页属设计（保证单章可独立编译）。
- 本册宜与 SY02-26（同主题 356 页正文）对读：本篇给动机与构造，SY02-26 给证明与细节。
