# SY05-27 交付说明 · 三价图的拉格朗日 Floer 理论与曲线的同调镜像对称

**原文**：Denis Auroux, Alexander I. Efimov, Ludmil Katzarkov,
*Lagrangian Floer theory for trivalent graphs and homological mirror symmetry for curves*,
arXiv:2107.01981v3 [math.SG], 2021-07-05 提交, 2024-07-05 修订, 59 页, 6 图；
*Selecta Mathematica, New Series* **30** (2024), Paper 95.

**译文**：三价图的拉格朗日 Floer 理论与曲线的同调镜像对称（中文译注本，50 页）。

---

## 一、交付清单

| 文件 | 说明 |
|---|---|
| `源码/main.tex` | 主文件。`ctexart` + XeLaTeX，`\input` 各章。 |
| `源码/preamble.tex` | 宏包、定理环境（与原文共享计数）、全部自定义宏。 |
| `源码/ch0_front.tex` … `ch8_epilogue.tex` | 封面/译者说明/目录、§1–§8 译文，共 11 个分章文件。 |
| `源码/refs.tex` | 参考文献 32 条，与原书逐条对应，全部 `\cite` key 命中。 |
| `源码/app_terms.tex` | 附录 A《术语对照表》135 条（由 `工程文件/reports/03_术语表.md` 生成）。 |
| `源码/original/2107.01981v3.tex` | 底本 LaTeX 源（arxiv.org/src 原样，未改动），供逐符号核对。 |
| `成品/SY05-27_三价图的拉格朗日Floer理论_中译注本.pdf` | **成品**，50 页，A4。按仓库 §4 规则成品 PDF 不入库、走 Release 外链；本地由 `源码/main.tex` 三遍 XeLaTeX 生成（`源码/main.pdf` 为同名构建产物）。 |
| `工程文件/reports/01_通读笔记.md` | 译前通读笔记（结构图、各节要点、术语线索）。 |
| `工程文件/reports/02_疑点清单.tsv` | 9 条疑点，全部「已解」，未解 = 0（其中 3 条为原文笔误/跳步，正文保留原文并加批注）。 |
| `工程文件/reports/03_术语表.md` | 冻结版术语表 135 条（英文／中文／依据）。 |
| `工程文件/reports/04_交付核对.md` | 对照《数学文献翻译纪律》v2.1 的自检清单。 |
| `工程文件/tools/` | 辅助脚本目录。 |

---

## 二、编译方法

必须用 **XeLaTeX**（`ctexart` + `fontset=windows`），三遍（第二遍处理交叉引用，第三遍稳定目录页码）：

```
cd 源码
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
```

**编译实测记录**（MiKTeX 26.5 / XeTeX 4.18 / Windows 11）：

| 指标 | 结果 |
|---|---|
| 错误 | 0 |
| Overfull \hbox | 0 |
| Underfull \hbox | 6（均为短标题行，badness ≤ 10000，不影响版面） |
| 未定义引用 / 文献 | 0 |
| 缺字（Missing character） | 0 |
| 页数 | 50 |

中文粗体/斜体走 SimSun/SimHei 的伪粗体，编译日志有 `Font shape ... undefined` 提示（ctex 正常现象，不产生缺字）。

---

## 三、翻译与校订

- **流程**：按《数学文献翻译纪律》v2.1，先通读全篇（§1–§8 与文献表），产出《通读笔记》《疑点清单》，未解清零后开译；先做样板章（§1），再逐章推进。
- **图**：原文 6 幅图全部为 Ti*k*Z/pstricks 代码，无位图。译文按原图几何重绘为 6 幅简化 Ti*k*Z 示意图，图注标明对应原书图号；不追求与原图逐笔一致，只求表达原图所画的构形。
- **编号**：定义、定理、引理、命题、注、例共享计数、按节编号，与原书一致；`\label`/`\ref` 一律不改名。
- **批注**：11 条 `% [Tutor Note: 易错/点拨/直觉]`，只写在源码注释里、不进 PDF；每条都带「依据」（原文节次或本工程笔记/术语表）。
- **术语**：135 条冻结术语，正文与附录一致；有通行中文译名者用中文（如「缠绕 Floer 上同调」「传播圆盘」「分叉」），无通行译名者保留英文（如 thimble、perverse curve 首次括注）。
- **公式**：所有公式对照 `源码/original/2107.01981v3.tex` 逐符号录入；原文 3 处笔误/跳步（§4.2 的 $g$、§5.3 的两个不等式、§3.3 的 $K$ 记号）保留原文表述，另加批注说明，不改原文结论。

---

## 四、已知取舍

1. 原文 §3.3.2–§3.3.3 的组合引理证明很长，译文完整保留，未压缩步骤；§5.4 的 HPL 论证亦逐段译出。
2. 原文 6 幅图为代码生成的矢量图，译文以简化 Ti*k*Z 重绘，属「示意图」而非复刻；若需逐笔复刻，应以原 PDF 页面为底稿另行重制。
3. 原文文献表 32 条，译文 32 条逐条对应（保留英文原条目，仅把作者名、刊名按原样排版），不增删。
