# 几何朗兰兹对偶是什么？——中文译注本 v1.0

David Ben-Zvi 综述 *What is the Geometric Langlands Correspondence About?*（arXiv:2605.23167v1）的完整中译，附 nLab 批注。

## 直接看这个

- **成品 PDF**：[`成品/几何朗兰兹对偶是什么_中译注本_v1.0.pdf`](成品/几何朗兰兹对偶是什么_中译注本_v1.0.pdf) — 48 页，可直接阅读/打印
- **可重编源码**：[`成品/源码_v1.0.zip`](成品/源码_v1.0.zip) — 解压后 `cd 源码 && xelatex main.tex`（跑两趟）即可复现

## 这本译稿做了什么

1. **全文逐段移译**（不压缩、不改写），节号与原文一一对应，公式编号 (1)–(6) 沿用原编号。
2. **三幅插图从原 PDF 抽出**（Elliot Kienzle 绘），重新置入译文对应位置，图注标明原作者。
3. **nLab 批注 12 条**：以脚注「译注｜」嵌在概念首现处，均标 B 级来源（nLab 属权威综述/百科级）。
   只做两件事——把原文一句带过的定义讲清、给出可查链接；不替作者立论、不引非权威网络来源。
   每条链接都标了词条的 **last revised** 日期（取自发布仓 `07_refs_nlab/pages/` 的缓存快照）。
4. **两个附录**：「译注汇总」（12 条按节重列 + 32 行 nLab 词条对照表，含修订日期列）、「术语表」（115 行，中／英／首现节）。
5. **参考文献 122 条**原样照排（不译），只修 PDF 抽取造成的连字断行与 `.ezproxy` 代理前缀。

## 体例要点

| 项 | 做法 |
|---|---|
| 原文脚注 / 译者脚注 | 「原注｜」14 条 / 「译注｜」12 条，起首即区分 |
| 来源等级 | A 原始文献 / B 权威综述与百科（本次批注全为 B）/ I 译者推断 |
| 术语 | 首现「中文（English）」；人名、群名、定理名、拉丁词不译（Hecke、Hitchin、étale、de Rham…） |
| 比喻 | 「白光」（White Field）、「跳动的心脏」、「罗塞塔石碑」等保留并加注，不意译 |
| 排版 | ctexart 11pt A4，宋体正文，页眉左标题右作者，三线表 |

## 目录结构

```
GL_work/
├── 成品/
│   ├── 几何朗兰兹对偶是什么_中译注本_v1.0.pdf
│   └── 源码_v1.0.zip
├── 源码/
│   ├── main.tex              封面 / 译者说明 / 摘要 / 目录 / 各章装配
│   ├── preamble.tex          宏包与数学记号宏（\Bun \Loc \IndCoh \Sph …）
│   ├── chunks/ch1–ch6.tex    §1–§6 译文
│   ├── chunks/refs.tex       122 条参考文献
│   ├── chunks/notes.tex      译注汇总 + nLab 对照表
│   ├── chunks/terms.tex      术语表
│   └── figures/fig1–3.jpg    三幅插图（1400px 长边）
├── 工程文件/
│   ├── BRIEF.md              任务书：底本、读者、硬约束、批注方案、验收
│   ├── STYLE_GUIDE.md        排版与术语规范（冻结的译名表）
│   ├── reports/01_通读笔记.md
│   ├── reports/02_疑点清单.md     28 条疑点及处理依据
│   ├── reports/03_nLab批注清单.md 12 条批注 + 两处词条纠错的记录
│   └── *.py                  抽取全文、生成参考文献、裁图、核 slug、补修订日期、查破洞页
├── 精选片段.md               入库用判定链（8 条）
├── 投稿信息.md
└── full.txt                  原文纯文本（pymupdf 抽取，含页码标记）
```

## 编译

```powershell
cd 源码
& "<HOME>\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe" -interaction=nonstopmode main.tex
& "<HOME>\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe" -interaction=nonstopmode main.tex
```

需要 MiKTeX（含 ctex、xurl、booktabs、longtable、fancyhdr）。两趟即可定稿目录与交叉引用。
`main.log` 里会有 5 条无害警告：两条 <8pt 的 Overfull \hbox（长公式），`TU/SimSun(0)/b/it` 字体形状
缺省替代（宋体无粗斜体），以及 hyperref 的 PDF 书签字符串提示。

## 已知边界

- nLab 链接核对于 2026-11-15，并顺手把用到的 16 个词条原文抓进了发布仓 `07_refs_nlab/pages/`；
  nLab 为维基式站点，日后 slug 若改动链接会失效，但批注文字与其修订日期快照不受影响。
- nLab 上 `oper/opers`、`IndCoh`、`nilpotent cone`、`character variety` 无独立词条（404），
  这些概念只作文字说明，未给链接（改引 `ind-coherent sheaves`）。
- `singular+support` 实为重定向到「分布的支集」，与层论的奇异支撑不同义；本次已改为引
  `characteristic variety` 并在正文脚注里如实说明（详见 `reports/03_nLab批注清单.md`）。
- 原文 §5 的五篇论文（[GR24a]、[ABC+24b]、[CCF+24]、[ABC+24a]、[GR24b]）分工按原文顺序保留，
  未合并改写，以便与原文逐段对照。
- 插图版权属 Elliot Kienzle，取自 arXiv 预印本内嵌位图，仅作学术阅读的说明性使用。
