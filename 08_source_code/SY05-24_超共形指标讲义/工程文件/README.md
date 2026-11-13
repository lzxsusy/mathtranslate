# README.md — SY05-24《超共形指标讲义》中文译注本

**原书**：Abhijit Gadde, *Lectures on the Superconformal Index*
**底本**：arXiv:2006.13630v1 [hep-th]，2020-06-24，32 页（TIFR/TH/20-20；YRISW 2020 冬季学校讲义，拟刊 JPhysA 专辑）
**本译本**：中文译注本，全文翻译 + 术语批注；保留全部编号公式与编号习题，复刻 2 张表格。

## 统计

| 项 | 数 |
|---|---|
| 页数（底本） | 32 |
| 编号公式 | 110 |
| 编号习题 | 8 |
| 表格 | 2 |
| 插图 | 0 |
| 参考文献 | 47 条 |
| Tutor Note | 124 条 |
| 成品页数 | 24（含封面、目录、译者说明） |

## 目录

- 译者说明
- 摘要
- §0 讲义提纲
- §1 Witten 指标（§1.1 超对称谐振子；§1.2 整体对称性）
- §2 超共形指标（§2.1 手征多重态；§2.2 规范理论的指标；§2.3 重组下的不变性；§2.4 插叙：超对称拉氏量）
- §3 $\sN=2$ 理论（§3.1 超对称极限；§3.2 $\sN=2$ 超 QCD 的 S 对偶；§3.3 Class S 对偶与 TQFT）
- §4 大 $N$ 极限下的指标（§4.1 黑洞呢？）
- 致谢、参考文献

## 工程结构

```
SY05-24\
├─ 投稿信息.md
├─ 工程文件\   （BRIEF / STYLE_GUIDE / TIMELINE / probe / glossary / prep.py / crop.py / check_block.py / build.ps1 / pages / split / full.txt）
├─ 源码\       （main.tex / preamble.tex / abstract.tex / sec0.tex / sec1a.tex / sec1b.tex / sec2a.tex / sec2b.tex / sec3a.tex / sec3b.tex / sec4.tex / refs.tex / translator_note.tex）
└─ 成品\       （编译后的 PDF）
```

## 编译

```powershell
powershell -ExecutionPolicy Bypass -File 工程文件\build.ps1
```

输出：`成品\SY05-24_超共形指标讲义_中文译注本.pdf`（xelatex 两遍；引擎为 MiKTeX）。

## 分工与验收

| 块 | 文件 | 内容 | 公式 | 环境 |
|---|---|---|---|---|
| c01 | abstract.tex + sec0.tex | 摘要、§0 | — | — |
| c02 | sec1a.tex | §1+§1.1 | (1.1)–(1.17) | — |
| c03 | sec1b.tex | §1.2 | (1.18)–(1.30) | 习题 1.1 |
| c04 | sec2a.tex | §2+§2.1 | (2.1)–(2.16) | 习题 1.2、2.1；Table 1 |
| c05 | sec2b.tex | §2.2–2.4 | (2.17)–(2.29) | 习题 2.2、2.3；Table 2 |
| c06 | sec3a.tex | §3+§3.1+§3.2 开头 | (3.1)–(3.19) | 习题 3.1、3.2 |
| c07 | sec3b.tex | §3.2 余+§3.3 | (3.20)–(3.35) | — |
| c08 | sec4.tex | §4+§4.1+致谢 | (4.1)–(4.16) | 习题 4.1 |
| c09 | refs.tex | 参考文献 | — | — |

验收：每块 `check_block.py` 输出 `OK`；公式号/环境号齐全；表格逐格复核；全本 xelatex 两遍无 `!` 错误。

## 体例

- 公式号照原文（(节.序)），手工 `\tag`；正文引用写「式 (2.14)」。
- 原文 2 张表格复刻（Table 1/2），无插图。
- 术语见 `工程文件\glossary.tsv`（215 条冻结表）。
- 批注以 `% [Tutor Note: …]` 或 `remark` 环境给出，四类：术语/动机/易错/文献。
- 参考文献条目不译，照抄原文。
