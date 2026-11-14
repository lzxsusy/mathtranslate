# BRIEF —— Orlov 2003 综述中文译注本 · 工程纲要

**项目编号**：SY08-02 **主题域**：08 教材与参考书（文献翻译）
**底本**：D. O. Orlov, *Derived categories of coherent sheaves and equivalences between them*,
Russian Math. Surveys 58:3 (2003) 511–591 = Uspekhi Mat. Nauk 58:3 89–172，
DOI 10.1070/RM2003v058n03ABEH000629。英文，81 页（PDF 第 1 页 = 书页 511）。
**页映射**：**书页 = PDF 页 + 510**（已核验：PDF p1 = 511）。
**状态**：开工（2026-11-15）。

---

## 1. 工作目录（全 ASCII，可直接编译）

```
C:\Users\admin\Downloads\orlov_derived_work\
├── src\                     # 可编译工程（lualatex）
│   ├── main.tex             # Lead 独占
│   ├── preamble.tex         # Lead 独占
│   ├── chunks\              # 每位译者一个（或多个）chNNx.tex
│   └── figures\             # Lead 裁切的交换图 dg_<书页>_<字母>.pdf
├── work\
│   ├── src\<chunk>.txt      # 按块切好的底本文字层
│   ├── pages\pNNN.png       # 200dpi 灰度页图，NNN = 书页 − 510
│   ├── reports\<chunk>.md   # 译者报告
│   ├── glossary.tsv         # 冻结术语表（只读）
│   ├── proposals\           # 译者新术语提案
│   ├── 通读笔记.md
│   ├── 疑点清单.tsv
│   └── tools\               # crop.py / pdf2png.py / check.py / gen_*.py
├── 工程文件\                 # 本文件、STYLE_GUIDE.md、build.ps1
└── 成品\                     # 交付 PDF
```

## 2. 分块表（唯一权威边界）

| chunk | 书页 | 页数 | 内容 | 归属 |
|---|---|---|---|---|
| ch00a | 512–517 前 | 6 | 引言（到「第 1 章」标题前） | Lead（样板） |
| ch01a | 517–523 前 | 7 | 第 1 章标题 + 1.1 | 译者 |
| ch01b | 523–530 前 | 8 | 1.2 + 1.3 + **章末评注** | 译者 |
| ch02a | 530–538 前 | 8 | 第 2 章标题 + 2.1 | 译者 |
| ch02b | 538–544 前 | 7 | 2.2 + **章末评注** | 译者 |
| ch03a | 544–549 前 | 6 | 第 3 章标题 + 3.1 + 3.2 | 译者 |
| ch03b | 549–555 前 | 7 | 3.3 | 译者 |
| ch03c | 555–564 前 | 10 | 3.4（到 3.5 标题前） | 译者 |
| ch03d | 564–567 前 | 4 | 3.5 + **章末评注** | 译者 |
| ch04 | 567–573 前 | 7 | 第 4 章标题 + 4.1 + 4.2 + **章末评注** | 译者 |
| ch05a | 573–581 前 | 9 | 第 5 章标题 + 5.1 | 译者 |
| ch05b | 581–589 前 | 9 | 5.2 + 5.3 + **章末评注** | 译者 |
| refs | 589–591 | 3 | 参考文献（不译，照排） | Lead |

**边界锚**（照这些句子切，不要靠页码硬切）：

- ch00a 止于 `CHAPTER 1` 之前（原书末段：`…Auteq D^b(A) → U(A×Â) → 1.`）。
- ch01b 起于 `1.2. Derived categories and derived functors` 标题。
- ch02b 起于 `2.2. Examples of equivalences: flopping birational transformations` 标题。
- ch03c 止于 `3.5. Appendix: the n-Koszul property…` 标题之前。
- ch03d 起于 `3.5.` 标题。
- ch05b 起于 `5.2. Objects representing equivalences…` 标题。

## 3. 章末评注与节首重点

- 每个 `\section{…}` 之后紧跟 `\takeaway{…}`：≤120 字，说清「这一节要做什么、用什么工具、结论是什么」，不要抄摘要。
- 每章末块最后写 `\chapterreview{…}`：700–1100 字，五段（全章地位／知识脉络／核心结论／辨析与提醒／评注）。
  归属：ch01b、ch02b、ch03d、ch04、ch05b。

## 4. 陈述数量预警（供对账）

原书陈述（据正文实测）：Ch1 约 30 条（Def 1.1.1、Lem 1.1.2、Def 1.1.3、Lem 1.1.4–1.1.6、Def 1.3(!)、Prop 1.1.8–1.1.9、Lem 1.1.10–1.1.12、Lem 1.2.1、Def 1.2.3、Lem 1.2.4–1.2.5、Prop 1.3.1–1.3.8、Cor 1.3.4 …）；
Ch2 约 22 条；Ch3 约 12 条；Ch4 约 6 条；Ch5 约 16 条。**最终以逐块报告汇总为准。**

## 5. 质量闸门

1. 整书 `lualatex ×3` 通过，`file:line=0 fatal=0 undefined=0 missingchar=0`。
2. 页标记单调、覆盖 p.512–591 无缺页。
3. 陈述编号与原文一一对应（Lead 抽查 + 附录 D 自动生成后双向差集为空）。
4. 每个 `\figdiag` 都能在 `src/figures/` 找到对应裁图，且裁图与页图一致。
5. 术语终检：`work/tools/term_scan.py` 无违例。
6. 每块有报告，报告的「存疑」栏被 Lead 逐条处理。
