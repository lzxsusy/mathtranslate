# BRIEF —— SY02-31《朗兰兹纲领 II：朗兰兹对应的几何化》

## 一、项目身份

| 项 | 内容 |
|---|---|
| 编号 | SY02-31（主题域 SY02 几何朗兰兹） |
| 原名 | *The Langlands Program II. Geometrization of the Langlands Correspondence* |
| 丛书 | Proceedings of Symposia in Pure Mathematics, Vol. 112.2 |
| 出版 | American Mathematical Society, 2025 |
| 编者 | Pierre-Henri Chaudouard、Wee Teck Gan、Tasho Kaletha、Yiannis Sakellaridis |
| 中译名 | 《朗兰兹纲领 II：朗兰兹对应的几何化》 |
| 底本 | 2022 年 7 月 11–29 日 IHES 朗兰兹纲领暑期学校会议录（第二卷，第 3 部分）；583 个 PDF 页，印刷页 iii–xi、1–567 |
| 权利状态 | 在版图书；本库只发布源码、工程文件与资料卡，**不发布成品 PDF**（R3） |
| 语言 | 英文 → 简体中文 |

## 二、这本书讲什么

2022 年 IHES 暑期学校纪念 1977 年 Corvallis 会议 45 周年，会议录分三卷。本卷收六篇文章，主题是朗兰兹对应的**几何化与范畴化**：局部 Langlands 参数的模空间（Dat）、其上的凝聚层（Zhu）、曲线模叠与 Fargues–Scholze 纲领（Fargues–Scholze）、$p$-进 Langlands 的范畴化（Emerton–Gee–Hellmann，253 页，含六个附录）、凝聚型与可构造型局部 Langlands 对应的关系（Ben-Zvi–Chen–Helm–Nadler）、以及导出结构（Feng–Harris）。

## 三、本版做了什么

1. 六篇文章全文中文译注，保留底本全部编号与页锚。
2. 术语表 `工程文件/work/glossary.tsv`（约 190 条，含等级与依据）。
3. 通读笔记、疑点清单、逐篇状态报告（`工程文件/reports/`）。
4. 资料卡五件套（`资料卡/`）、对齐卡（`对齐卡/`）。
5. 编译脚本与审计记录（`工程文件/build.bat`、`工程文件/reports/编译审计.md`）。

## 四、目录结构

```
SY02-31_朗兰兹纲领II_朗兰兹对应的几何化/
├── 投稿信息.md
├── README.md
├── 工程文件/
│   ├── BRIEF.md
│   ├── STATUS.md
│   ├── build.bat
│   ├── work/        glossary.tsv, STYLE_GUIDE.md, WORKER_BRIEF.md, 通读笔记.md, 疑点清单.tsv
│   ├── reports/     编译审计.md, U01–U06 分篇报告
│   ├── deliverable/ 本库不放成品 PDF（R3）
│   └── data/        页面切分与校验脚本
├── 源码/
│   ├── main.tex  preamble.tex
│   ├── front/    preface.tex, translator.tex, guide.tex
│   └── chunks/   ch-a1-00 … ch-a6-08（47 片，按 PDF 页序）
├── 资料卡/       00-速览.md … 04-术语文献勘误.md
└── 对齐卡/       SY02-31-ALIGN-01.md …
```

## 五、编译

```
cd 源码
xelatex main.tex
xelatex main.tex
xelatex main.tex
```

要求：0 error、0 undefined references、0 missing characters。引擎 XeLaTeX（MiKTeX 4.18），`ctexbook` + `fontset=windows`。

## 六、章节与页范围

| 章 | 内容 | 作者 | 印刷页 | PDF 页 | chunk |
|---|---|---|---|---|---|
| 前言 | Preface | 编者 | ix–xi | 10–12 | front/preface.tex |
| 1 | 局部 Langlands 参数的模空间 | J.-F. Dat | 3–37 | 16–50 | ch-a1-00…03 |
| 2 | 参数叠上的凝聚层 | X. Zhu | 39–123 | 52–136 | ch-a2-01…07 |
| 3 | 朗兰兹纲领与曲线上的向量丛模叠 | L. Fargues, P. Scholze | 125–165 | 138–178 | ch-a3-01…04 |
| 4 | 范畴化 $p$-进 Langlands 纲领导论 | M. Emerton, T. Gee, E. Hellmann | 167–419 | 180–432 | ch-a4-01…21 |
| 5 | 凝聚型与可构造型局部 Langlands 对应之间 | D. Ben-Zvi, H. Chen, D. Helm, D. Nadler | 421–470 | 434–483 | ch-a5-01…04 |
| 6 | Langlands 对应中的导出结构 | T. Feng, M. Harris | 471–568 | 484–581 | ch-a6-01…08 |

## 七、勾选（交付前）

- [x] 通读笔记 + 疑点清单（G0）
- [x] 术语表定稿并用于全文
- [x] 六篇全文译完
- [x] 编译三遍 0 error / 0 Overfull / 0 undefined / 0 missing character（495 页；见 `reports/U04_编译与审计.md`）
- [x] 二校（结构层，他校）：页锚 562 个 0 缺失、编号陈述 802 条、术语 314 条全书统一、lint 0 命中
- [ ] 逐句抽读二校（TODO：第二轮，人工）
- [x] 资料卡五件套
- [x] 对齐卡 ≥1
- [x] RELEASE_REGISTER 登记（SY02-31，成品不公开，R3）
- [x] CHANGELOG（项目根 `CHANGELOG.md`）
