# BRIEF · SY02-18《shtuka 及其模空间导论》

## 原文

| 项 | 内容 |
| --- | --- |
| 原题 | Introduction to Shtukas and their moduli |
| 作者 | 恽之玮（Zhiwei Yun） |
| 场合 | IHES 2022 暑期学校（Langlands 纲领专题）讲稿 |
| 版本 | arXiv:2411.10248，2024 年，38 页，amsart 11pt |
| 结构 | 6 节 22 小节，含 5 张交换图（xy-pic）、44 条文献、40 个定理类对象、17 个编号公式 |
| 文件 | `工程文件/work/原文/main.tex`（2279 行）、`工程文件/work/pdf/src.pdf` |

**原文性质。** 这是给暑期学校学生的综述讲稿，不是专著：定义与主要定理陈述给全，证明多半只给论证思路（原文常写 "sketch"），大量结果直接引文献。全篇基本以「叠 + 层 + 上同调」的现代语言写成，预设有代数几何与 Langlands 纲领的基础。原文第 1 节是引言与路线图，第 2–5 节是主干，第 6 节讲三个进阶方向。

## 一句话主旨

shtuka 是函数域上「带 Frobenius 撕扯结构的 $G$-丛」，它的模叠把整体 Langlands 对应的自守侧几何化，于是可以用叠的几何工具（局部模型、因子化、部分 Frobenius、上同调）去攻 Langlands 猜想与 $L$-函数的高阶导数。

## 五步逻辑链

1. **定义链。** $G$-主丛 → Hecke 叠 $\Hk^I_{G,\bK}$ → $G$-shtuka（附加同构 $\tau\cE\cong\cE'$，撕扯 $r$ 处）→ 模叠 $\Sht^{(I_1,\cdots,I_r)}_{G,\bK}$。
2. **类比链。** shtuka 之于椭圆曲线（Drinfeld）、iso-shtuka 之于动机（Anderson $t$-动机）、Hecke 叠之于 Grassmann 簇、模叠之于 Shimura 簇。
3. **几何链。** 可表示性（DM 叠）→ 局部模型（与仿射 Grassmann 簇的截片对比）→ 沿 $I=I_1\sqcup\cdots\sqcup I_r$ 的分解结构 → 水平改变 → 中心作用 → Hecke 对应 → 部分 Frobenius。
4. **上同调链。** Satake 层 $\IC^I_{\Sht}(V)$ → 复形 $\cH^I(V)$ → Hecke 作用（与球 Hecke 代数 $\bH_x$ 的作用交换）→ 因子化同构 → 部分 Frobenius 给出的 Weil 结构。
5. **应用链。** 圈类与相交数（定理 6.3.2）→ 高阶 Gross–Zagier 与 Siegel–Weil 公式 → $L$-函数高阶导数的模性猜想（猜想 6.3.5）。

## 分块表

| 块 | 节 | 原文行 | 译本页 | 编号对象 | 目标文件 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| ch01 | §1 引言、§2 基本定义（2.1–2.3） | 585–962 | 4–10 | 8 例、3 注、1 引理、1 公式 | `chunks/ch01.tex` | 完成 |
| ch02 | §2.4、§3 亲戚与表亲、§4.1–4.2 | 963–1295 | 13–23 | 4 定理、4 命题、1 推论、1 问题、1 公式 | `chunks/ch02.tex` | 完成 |
| ch03 | §4.3–4.7、§5.1 | 1296–1647 | 23–31 | 1 引理、1 例、3 命题/推论、2 公式 | `chunks/ch03.tex` | 完成 |
| ch04 | §5.2–5.4、§6 | 1648–2027 | 31–41 | 3 定理、2 命题、1 猜想、2 注、2 公式 | `chunks/ch04.tex` | 完成 |
| ch05 | 参考文献 | 2029–2276 | 42–46 | 44 条 `\bibitem` | `chunks/ch05.tex` | 完成（脚本转换） |

合计：**57 个编号对象**（40 个定理类 + 17 个编号公式），与原 PDF 逐条一致（`工程文件/scripts/sim_numbering.py diff` → `mismatch 0`）。

## 施工流程（每块）

1. 从 `工程文件/work/原文/main.tex` 取本块行段，对照 `工程文件/work/pdf/src.pdf` 对应页核公式。
2. 环境名映射：theorem→`thm`、lemma→`lem`、prop→`prop`、cor→`cor`、conj→`conj`、definition→`dfn`、construction→`cons`、remark→`rmk`、example→`exam`、question→`ques`；`\sss{…}` → `\ssszh{…}`（保留原文的计数器步进）。
3. `\label`/`\ref`/`\eqref`/`\cite` 的 key 一字不改；不手写任何编号。
4. 数学模式里的中文一律 `\text{}`。
5. 单块编译（`xelatex` 两遍），查 `!`、Overfull、Missing character。
6. 写 `工程文件/reports/chNN.md` 记录原文行、编号对象、译注、坑。

## 纪律与已知坑

- **定理类与 `\sss` 共用 `subsubsection` 计数器**（原文 `\newcommand\sss{\subsubsection}`，amsart 下 `secnumdepth=2` 故小标题不显示编号但仍步进）。译文用 `\ssszh` 复现「显示标题 + 步进计数器」，否则定理号会比原文小。
- 题头格式照原文「2.3.3. 引理.」：数字→句点→环境名→句点，由 `源码/preamble.tex` 的自定义 `\newtheoremstyle{zhthm/zhdefn/zhrmk}` 实现。
- `xy-pic` 必须在 `tikz` 之后加载；`\xymatrix` 一律改写为 `tikz-cd`，空单元要填 `& {} &` 之类占位。
- 宏移植：原文大量 `\newcommand\cX{...}`（无花括号）与 `\renewcommand\a\alpha`（单 token 宏体），脚本要专门处理；与内核重名的宏改 `\renewcommand`。
- 与内核冲突的 `\c` 必须 `\renewcommand{\c}{\circ}`，否则被当成软音符，报 `Command \c invalid in math mode`。
