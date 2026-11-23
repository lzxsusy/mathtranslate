# BRIEF —— SY02-29 局部 Langlands 对应的几何化（综述）

## 一、任务

把 Laurent Fargues 的综述

> Laurent Fargues, *Geometrization of the local Langlands correspondence: an overview*,
> 2016-02-02，46 页（作者自排 pdfLaTeX 文稿，无出版方版式）。

译成中文译注本，并配套资料卡。底本文件由用户提供（微信收件箱中的
`Fargues_Geometrization_overview(1).pdf`）；本工程只保留逐页文本与页面图，
不复制 PDF 原件。

## 二、底本判读

- 印刷页码与 PDF 页码一致（第 1 页即 PDF 第 1 页），共 46 页。
- 正文九节：导引（p.1–3）；§1 曲线（p.3–16）；§2 叠 $\Bun_G$（p.16–23）；
  §3 $B_{\mathrm{dR}}$-仿射 Grassmann 簇与 Hecke 叠（p.23–28）；§4 猜想的陈述（p.28–29）；
  §5 特征层性质（p.29–31）；§6 $F$-等晶体、$p$-可除群与向量丛的修正（p.31–34）；
  §7 局部/整体相容（p.34–36）；§8 Kottwitz 猜想（p.36–42）；§9 交换情形（p.42–46）；
  文献表（p.46）。
- 定理类编号按节连续（定义 1.5、命题 1.6、注 1.7…），译本沿用同一计数器，
  节号即原文节号，故编号可直接对照。

## 三、方法（九步流程的裁剪版）

1. **通读**（第 0 定律）：全文速读一遍，产出 `work/通读笔记.md`；
   逐节细读时同步登记 `work/疑点清单.tsv`（六类：概念/术语/记号/跳步/笔误/歧义）。
   未解 = 0 才开译。
2. **定术语**：`work/glossary.tsv` 冻结 76 条，优先沿用本库 SY02-16、SY02-19、SY02-21、SY02-26 的既定译法。
3. **分章翻译**：七名译手按章并行（§1 拆两段），各自只写自己的 `源码/sections/sNN-*.tex`；
   译手契约见 `work/TASK-translator.md`。
4. **核对**：公式逐符号对页面图（`work/pages/pNNN.png`，150 dpi）核；
   定理编号、交叉引用、文献编号逐一对照。
5. **编译**：`源码/build.bat`（xelatex 两遍）。
6. **报告**：每章一份 `reports/chNN.md`（改动、裁定、遗留）。
7. **资料卡**：36 张概念卡 + 8 张推导卡，见 `资料卡/SCHEMA.md`。
8. **入库**：`03_translations_meta/SY02-29/投稿信息.md`、`datasets/sy02-29/` 卡副本、
   仓库 `tools/make_stats.py --write` 与 `tools/build_manifest.py`。

## 四、交付物

| 位置 | 内容 |
| --- | --- |
| `源码/` | `main.tex`、`preamble.tex`、`sections/s00–s99`、`build.bat` |
| `成品/` | 编译出的 PDF（入库时按仓库规范命名） |
| `工程文件/` | 本 BRIEF、`SPEC.md`、`work/`（通读笔记、疑点清单、术语表、逐页文本、页面图）、`reports/`、`tools/` |
| `资料卡/` | `SCHEMA.md`、`cards/concepts/*.json`、`cards/derivations/*.json`、`tools/` |

## 五、硬约束（摘自 04_playbook/01）

- 数学正确性优先；不臆造，底本疑难只进批注与疑点清单，不改正文。
- 译注必须带来源等级 A/B/I；黑名单站点不看、不引、不缓存。
- 只改本工程文件；不改 label/ref/编号；术语改名须三同步。
- 中文数学文风；一句 ≤ 60–70 汉字；中英之间半角空格；全角标点。
- 交付前 `grep` 旧术语 = 0，单章编译须过。

## 六、进度

见 `work/进度.md`（由 lead 维护）。
