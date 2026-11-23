# BRIEF —— SY02-32 迹公式与函子性：一个纲领的开端

## 一、任务

把 Edward Frenkel、Robert Langlands、Ngô Bao Châu 合著的法文论文

> E. Frenkel, R. Langlands, Ngô B. C., *Formule des traces et fonctorialité : le début d'un programme*,
> arXiv:1003.4578v2 [math.RT]，2010-09-29，54 页（arXiv 作者自排版式）。

译成中文译注本，并配套资料卡。底本文件由用户提供（微信收件箱中的
`44_Frenkel-Ngo-Langlands_1003.4578.pdf`）；本工程只保留逐页文本与页面图，
不复制 PDF 原件。

## 二、底本判读

- **原文语种为法语**，不是英语；术语按法语原文核对，文献表中英文条目保持原文。
- 印刷页码与 PDF 页码一致（偏移 0），共 54 页：正文 p.1–52，文献 p.53–54（40 条）。
- 正文结构：
  - 导引（Introduction）p.1–3；
  - §1 $L$ 函数的极点与函子性 p.3–12；
  - §2 函数域情形 p.12–17；
  - §3 假设、测度与稳定迹公式 p.17–38（3.1 p.17–19；3.2 p.19–25；3.3 p.25–30；3.4 p.30–33；3.5 p.34–38）；
  - §4 迹公式的阿代尔化 p.38–46；
  - §5 主项 p.46–52。
- 编号制度：公式按节编号 (1.1)–(1.14)、(2.1)–(2.7)、(3.1)–(3.34)、(4.1)–(4.13)、(5.1)–(5.13)；
  断言编号跨节连续（Lemme 2.6、Lemme 3.26、Proposition 3.29、Lemme 4.1、4.2、Lemme 5.4、
  Proposition 5.6、Lemme 5.8、5.10、5.13），译本用同一计数器逐条对齐（见 `SPEC.md` §3）。
- 脚注 10 条，全部译出；脚注编号沿用原文顺序。

## 三、方法（九步流程的裁剪版）

1. **通读**（第 0 定律）：全文速读一遍，产出 `work/通读笔记.md`；逐节细读时登记
   `work/疑点清单.tsv`（六类：概念/术语/记号/跳步/笔误/歧义），15 条全部结案。
2. **定术语**：`work/glossary.tsv` 冻结 137 条，优先沿用本库 `lbook04`（Arthur–Selberg 迹公式）、
   `SY02-29`（几何 Langlands）与 `04_playbook` 的既定译法；无通行译名者保留原文。
3. **分章翻译**：按节切文件（`s01-intro` … `s08-sec5`），每个文件对应一段连续原文页，
   页首 `\srcpage{N}`，页界在句中用 `\srcpageinl{N}`。
4. **核对**：公式逐符号回页面图（`work/pages/pNNN.png`，170 dpi）；定理编号、交叉引用、
   文献编号逐一对照。
5. **编译**：`源码/build.bat`（xelatex 两遍）。
6. **报告**：`reports/分章报告.md`（逐节：页数、译注、裁定、遗留）。
7. **资料卡**：概念卡 + 推导卡，见 `资料卡/SCHEMA.md`。
8. **入库**：`datasets/sy02-32/`、`RELEASE_REGISTER.csv`、`README.md` 统计块、
   `tools/make_stats.py --write` 与 `tools/build_manifest.py`。
9. **发布**：AtomGit `main` / Gitee `master`。

## 四、交付物

| 位置 | 内容 |
| --- | --- |
| `源码/` | `main.tex`、`preamble.tex`、`sections/s00–s99`、`build.bat` |
| `成品/` | 编译出的 PDF（arXiv 底本，按仓库规范可发成品） |
| `工程文件/` | 本 BRIEF、`SPEC.md`、`work/`（通读笔记、疑点清单、术语表、逐页文本、页面图）、`reports/` |
| `资料卡/` | `SCHEMA.md`、`cards/concepts/*.json`、`cards/derivations/*.json`、`tools/` |
| 根目录 | `README.md`、`精选片段.md`、`投稿信息.md` |

## 五、硬约束（摘自 04_playbook/01）

- 数学正确性优先；原文有误只加译注，不改正文，也不擅自"修正"公式。
- 术语按冻结表；改名须正文、索引键、术语表三处同步。
- 译注只写三类（易错预警 / 含糊点拨 / 背景直觉），每条给来源（A 原书页码、
  B nLab/Stacks、I 本库既有卡片）；无来源时写"上下文推断，无外部依据"。
- 不补写原文没有的内容；不把纲领性猜测写成定理。
- 编译判据：0 error、0 Overfull、0 undefined reference、0 缺字。
- 黑名单来源（知乎、百度百科、CSDN、公众号、个人博客、AI 摘要）不看、不引、不缓存。
