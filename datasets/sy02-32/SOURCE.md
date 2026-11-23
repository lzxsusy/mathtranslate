# 投稿信息 · SY02-32

TRANSLATION-STANDARD:v2.1 施工标准

## 一、书目

| 项 | 内容 |
| --- | --- |
| 编号 | SY02-32 |
| 原作 | Formule des traces et fonctorialité : le début d'un programme |
| 作者 | Edward Frenkel（UC Berkeley）、Robert Langlands（IAS）、Ngô Bao Châu（University of Chicago / VIASM） |
| 出处 | arXiv:1003.4578v2 [math.RT]，2010-09-29；法文，54 页 |
| 中译名 | 迹公式与函子性——一个纲领的开端 |
| 主题 | 用稳定迹公式研究自守 $L$ 函数在临界线上的极点，从而「自下而上」地建立函子性；含函数域上的几何化验证、迹公式的阿代尔化与主项计算 |
| 体例 | 单篇研究论文：导引 + 5 节 + 文献 42 条；印刷页 = PDF 页（偏移 0），范围 1–54 |
| 学科 | 数论 / 自守表示 / 迹公式 / 几何 Langlands |
| 难度 | 极高（稳定迹公式、内窥、Arthur 分类、Hecke 叠与几何 Satake、Grothendieck–Springer 同时消解同时在场） |
| 篇幅 | 原文 54 页；译本 **39 页**（含译者说明与 14 条译注） |

## 二、交付物

```
SY02-32_迹公式与函子性_一个纲领的开端/
├── README.md
├── 源码/
│   ├── main.tex
│   ├── preamble.tex
│   ├── build.bat
│   └── sections/
│       ├── s00-front.tex        译者说明
│       ├── s01-intro.tex        导引            p.1–3
│       ├── s02-sec1.tex         §1 L 函数的极点与函子性   p.3–12
│       ├── s03-sec2.tex         §2 函数域情形    p.12–17
│       ├── s04-sec3a.tex        §3.1–3.2 假设、测度   p.17–25
│       ├── s05-sec3b.tex        §3.3–3.4 Steinberg–Hitchin 基、椭圆正则元  p.25–33
│       ├── s06-sec3c.tex        §3.5 沿稳定共轭类的积分   p.34–38
│       ├── s07-sec4.tex         §4 迹公式的阿代尔化     p.38–46
│       ├── s08-sec5.tex         §5 主项                p.46–52
│       └── s99-bibliography.tex 文献（原样保留法/英条目） p.53–54
├── 工程文件/
│   ├── BRIEF.md / SPEC.md
│   ├── work/（通读笔记、疑点清单、术语表、逐页原文、页面图、脚本）
│   └── reports/（分章报告、审校报告）
├── 资料卡/
│   ├── 00-速览.md … 04-术语文献勘误.md
│   └── cards/{concepts,derivations}/*.json   31 张（24 概念 + 7 推导）
├── datasets/sy02-32/（副本：SCHEMA.md、SOURCE.md、cards/、tools/）
└── 成品/（main.pdf）
```

## 三、统计

| 项 | 数 |
| --- | --- |
| 原文页 | 54 |
| 译本页 | 39 |
| 页锚 `\srcpage` | 54（p.1–54 全覆盖） |
| 编号公式 | 72 |
| 编号断言 | 10 |
| 译注 `\yizhu` | 12 |
| 脚注 | 12 |
| 参考文献 | 42 |
| 术语表 | 约 120 条 |
| 疑点清单 | 15 行（全部已解） |
| 资料卡 | 31（24 概念 + 7 推导） |
| 编译 | 0 error / 0 Overfull / 0 undefined |

## 四、权利与风险

- 底本为 arXiv 预印本，作者保留权利；本译本为**演绎作品**（rewritten），非逐字复制。
- 依 `04_playbook/01_数学文献翻译纪律.md` §9：arXiv 底本**可随仓公开成品 PDF**。
- 引用原文仅为术语核对与卡片 `sources[].quote`（每条 ≤120 字符），属合理引用范围。
- 风险等级：**低**（无第三方版权图片、无在版图书正文）。
