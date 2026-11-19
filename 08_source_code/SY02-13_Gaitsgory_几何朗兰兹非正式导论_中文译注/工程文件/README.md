# SY02-13 几何朗兰兹的非正式导论（中文译注）

D. Gaitsgory 为《朗兰兹纲领导论》（Bernstein–Gelbart 编，Birkhäuser 2004）所撰第 12 章的中文译注本。底本 13 页，译文 15 页（含译者说明与文献）。

## 文件

| 路径 | 内容 |
|---|---|
| `deliverable/SY02-13_Gaitsgory_几何朗兰兹的非正式导论_中文译注.pdf` | 成品 PDF（15 页） |
| `deliverable/译注汇总.md` | 8 条译注的总表与全文 |
| `deliverable/术语表.tsv` | 109 条术语（英文 / 中文 / 依据 / 首现） |
| `deliverable/工程总结.md` | 底本、流程、工具链、质量数据、取舍与遗留 |
| `src/main.tex` | 主控文件（版式、宏、字体） |
| `src/chapters/titlepage.tex` | 题页 |
| `src/chapters/preface.tex` | 译者说明（含原书页与本书页对照表） |
| `src/chapters/ch12_sec1.tex` | §1 函数域上 $\mathrm{GL}_n$ 的自守形式 |
| `src/chapters/ch12_sec2.tex` | §2 用向量丛解释 |
| `src/chapters/ch12_sec3.tex` | §3 从函数到层；§4 附录：层-函数对应 |
| `src/chapters/bibliography.tex` | 文献 |
| `work/通读笔记.md` | 开译前的通读记录 |
| `work/疑点清单.tsv` | 17 条疑点及查证结论 |
| `work/glossary.tsv`、`work/符号表.tsv` | 术语与符号底稿 |
| `work/公式核对记录.md` | 逐条公式与页图的核对表 |
| `work/en/ch12_raw.txt` | 英文文本提取件（仅作行文参照） |
| `work/pages/p271.png`–`p283.png` | 150 dpi 原书页图（公式核对依据） |

## 编译

```
cd src
xelatex main.tex
xelatex main.tex
xelatex main.tex
```

需要 xelatex、ctex、Noto Serif SC / Noto Sans SC 字体。成品应为 15 页、0 error、0 undefined、0 overfull。

## 说明

- 版式沿用本译丛既有的 ctexbook 模板：A4、11 pt、左边距 2.8 cm、右边距 2.6 cm。
- 原书「小节编号」与「命题/引理编号」共用一套数字，译文保留这一做法。
- 底本为受版权保护的书籍章节，本工程仅作内部交付，成品不对外发布。
