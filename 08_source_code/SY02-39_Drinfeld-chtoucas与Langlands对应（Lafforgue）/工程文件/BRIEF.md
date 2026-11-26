# BRIEF · SY02-39 Drinfeld chtoucas 与 Langlands 对应

## 一、任务

把 Laurent Lafforgue 的 Tata 讲义 *Cours à l'Institut Tata sur les chtoucas de Drinfeld et la correspondance de Langlands*（IHES 预印本 IHES/M/02/45，Juin 2002，56 页）从法文译成中文，按《数学文献翻译纪律》v2.1 出 PDF，并配套一套可检索、可自测的资料卡。

## 二、为什么做这一篇

- **它是 Lafforgue 自己写的路线图**。正文两页的引言把函数域上 Langlands 对应证明的六章骨架一次讲完：截断 → 紧化 → 边界上同调可忽略 → 本质上同调里的迹公式。英文的长文（[Lafforgue 2002]）形式完备但极难入门，这篇法语讲义正是作者为"进入那篇长文"写的入口。
- **它把技术核心讲成了一条链**：Harder–Narasimhan 截断多边形 $p$ 怎么选、紧化怎么造（fourre-tout 与完整同态）、边界上同调为什么 $r$-可忽略、本质部分为何集中在中间次数 $2r-2$、Hecke 代数为何在紧化上"不安定"而在赋值判据下稳定。这条链每一环都对应一张可独立成卡的推导。
- **它记录了作者的一处自我修正**：第六章按 Yakov Varshavsky 的提示改正了 [Lafforgue 1998] 最后一页的一个小错误。这是理解"迭代 $\varphi$-格"构造的难得入口。

## 三、交付物

| 交付物 | 位置 |
| --- | --- |
| 中译注本 PDF（42 页） | `成品/SY02-39_Drinfeld-chtoucas与Langlands对应_中译注本.pdf` |
| 源码（14 个文件，约 3,300 行） | `源码/`（`main.tex`、`preamble.tex`、`ch0_front.tex`、`ch1_intro.tex`、`ch2_I_a.tex`、`ch2_I_b.tex`、`ch3_II.tex`、`ch4_III.tex`、`ch5_IV.tex`、`ch6_V_a.tex`、`ch6_V_b2.tex`、`ch7_VI_a.tex`、`ch7_VI_b.tex`、`biblio.tex`） |
| 通读笔记 | `工程文件/reports/01_通读笔记.md` |
| 疑点清单（16 行，未解 0） | `工程文件/reports/02_疑点清单.tsv` |
| 术语表（约 80 条冻结术语） | `工程文件/reports/03_术语表.md` |
| 交付核对 | `工程文件/reports/04_交付核对.md` |
| 精选片段（8 条判定链） | `工程文件/精选片段.md` |
| 资料卡（18 张） | `datasets/lafforgue02/` |

## 四、验收标准

1. 编译 0 error、0 Overfull、0 未定义引用、0 缺字。
2. 原书印刷页 1–56 与译本逐页锚 `\origpage{}` 一一对应，`ch0_front.tex` 的 longtable 可查。
3. 每条译注有来源或明确标"无外部依据"。
4. 原文笔误不擅改，照录原文并加译注、登记进《疑点清单》（`未解` 须为 0）。
5. 术语全篇唯一写法：`chtouca`、`fourre-tout` 保留原文不译；`cohomologie essentielle` 一律译"本质上同调"。
6. 资料卡 `lint_cards.py --strict` 0 error，`related` 全部可解析。

## 五、已知边界

- **原文无编号**：全篇定理、命题、引理、推论、定义一律以 `Théorème. –` 起头，不带编号；公式也不编号。译本保留这一体例，因此本译本与资料卡都**不出现"定理 3.2"式的引用**，指称一律用"第 III 章的那个命题"。
- **底本无 LaTeX 源码，也无法抽取文本**：PDF 文本层是 2002 年 Ghostscript 用 Type3 位图字体写的，抽取即乱码。全部正文由页面图像（150 dpi）逐页录入、逐符号核对，公式一律回页面图像复核。
- **法文原稿的笔误已登记 9 处**（见《疑点清单》），例如 p.20 的 `comment $u$ dégénère`（同页变量名为 $v$）、p.27 的 $\mathcal F_s$（按上下文应为 $\mathcal E'_s$）、p.37 的 `ne présente par`（应为 *pas*）。全部照录原文并加译注，未擅自改动。
- **部分论证原文只给思路**（作者自述"不想把笔记整理成文"）。译本不补写数学内容，凡原文一笔带过而读者易卡住处，只在译注里点到"此步依据的是哪个命题"，不代作者补证明。
