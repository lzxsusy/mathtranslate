# r-grass —— §3「B_dR-仿射 Grassmann 簇与 Hecke 叠」译校报告

- 译手：grass　｜　底本：Fargues, *Geometrization of the local Langlands correspondence: an overview*（2016-02-02），p.23–p.28
- 交付：`源码/sections/s05-grassmannian.tex`（新建，12.5 KB，303 行）
- 自检：`build.bat check sections/s05-grassmannian.tex d` → **[OK]，6 页，0 error**；log 中无 Overfull/Underfull，无 Missing character；`_check_d.pagemarks` = 23 24 25 26 27 28。

## 1. 编号对齐表（原文 ↔ 译文，逐条）

所有环境共享 `[section]` 计数器，依次连排即自动对齐（check 版节号为 1，故显示 1.x；整书为 §3 时即 3.x）。

| 原文 | 类型 | 源页 | 译文环境 | 备注 |
|---|---|---|---|---|
| 3 | 节标题 | p.23 | `\section` | 原文 “Grassmanian” 少一 n，译文用正确拼写 |
| 3.1 | Def | p.23 | `definition` `def:3.1` | 竖排小图（Gr↓Spa(E)⋄）已复原 |
| 3.2 | Rem | p.24 | `remark` `rem:3.2` | |
| 3.3 | Rem | p.24 | `remark` `rem:3.3` | 注体为斜体；“One checks that…” 属正文，已置于注外 |
| 3.4 | Prop | p.24 | `proposition` `prop:3.4` | 三条 bullet 保留 |
| 3.5 | Prop | p.24 | `proposition[{[6]}]` `prop:3.5` | 引用编号以可选参数照排 |
| 3.6 | Rem | p.24 | `remark` `rem:3.6` | Pic⁰(X_F)=0 |
| 3.7 | Prop | p.24 | `proposition` `prop:3.7` | |
| 3.8 | Conj | p.24 | `conjecture` `conj:3.8` | “光滑拓扑下局部满” |
| 3.9 | Conj | p.24 | `conjecture` `conj:3.9` | 见疑点 2 |
| 3.10 | Prop | p.25 | `proposition` `prop:3.10` | (1)(2)(3)，含两处显示公式 |
| 3.11 | Cor | p.25 | `corollary` `cor:3.11` | 原文上标 Gr^{B_dR} |
| 3.12 | Prop | p.25 | `proposition` `prop:3.12` | (1)(2) |
| 3.13 | Rem | p.26 | `remark` `rem:3.13` | 原文下标 Gr_{B_dR}，见疑点 5 |
| 3.14 | Thm | p.26 | `theorem[{[27]}]` `thm:3.14` | Scholze 的菱形定理 |
| 3.15 | **Hope** | p.26 | `hope` `hope:3.15` | preamble 已定名「期望」，语气弱于猜想 |
| 3.16 | Rem | p.26 | `remark` `rem:3.16` | |
| 3.17 | Def | p.26 | `definition` `def:3.17` | 四元组 + 4 bullet |
| 3.18 | Rem | p.27 | `remark` `rem:3.18` | |
| 3.19 | Def | p.27 | `definition` `def:3.19` | 交换图 ←h/→h 用 tikz-cd 复原 |
| 3.20 | Prop | p.27 | `proposition` `prop:3.20` | 𝒯×_{L⁺G}Gr^{≤μ} |
| 3.21 | Conj | p.27 | `conjecture` `conj:3.21` | (1)(2)(3)，含 IC_μ、r_μ |

小节：3.1 / 3.2 / 3.3（`\subsection`），3.3.1 / 3.3.2（`\subsubsection*` 保留原文号），3.4 / 3.5（`\subsection`）。
合计：21 个编号环境，与原文 3.1–3.21 一一对应；本块无编号公式（原文 (8) 属 §2）。

## 2. 页锚（\srcpage）

| 锚 | 语义位置 | 说明 |
|---|---|---|
| 23 | `\section` 之后、3.1 标题前 | p.23 起点即 §3 标题 |
| 24 | 定义 3.1 之后、注 3.2 前 | p.24 首件为注 3.2 |
| 25 | 3.3.1 之前 | p.25 首件为 3.3.1 标题 |
| 26 | 注 3.13 之前 | p.26 首件为注 3.13 |
| 27 | 注 3.18 之前 | p.27 首件为注 3.18 |
| 28 | 文件末尾（§3 末句后） | **p.28 整页是 §4，无 §3 内容**；此锚仅为满足「6 锚」体例，见遗留 1 |

## 3. 疑点表

| # | 位置 | 原文 | 类型 | 判断与处理 | 依据 | 状态 |
|---|---|---|---|---|---|---|
| 1 | p.26 §3.3.2 标题 | The equal characteristic case | 笔误 | 正文 “Suppose now that E|Q_p” 即不等特征；译文题作「不等特征情形」并加 `\yizhuw` | 页面图像 p.26；工程《疑点清单.tsv》同条 | 已解 |
| 2 | p.24 猜想 3.9 | the moduli space **or** reductions | 笔误 | 应为 of；译文按「E 到 B 的约化的模空间」照意译，未加注（不影响读解） | 语义；页面图像 p.24 | 待录 |
| 3 | p.24 猜想 3.8 | comes from **en** element | 笔误 | an 之误；译文「来自 … 的一个元素」 | 页面图像 p.24 | 待录 |
| 4 | p.26 定义 3.17 后 | **en** element（两处） | 笔误 | an 之误，同上 | 页面图像 p.26 | 待录 |
| 5 | p.25 推论 3.11 vs p.26 注 3.13 | Gr^{B_dR}（上标）/ Gr_{B_dR}（下标） | 记号不一致 | 两处均按各自原样排，未统一；建议 Lead 裁定全书写法 | 页面图像 p.25、p.26 | 待裁 |
| 6 | p.25 命题 3.10(2) | Gr^{PR} 后紧跟 hat-⊗_{F_q}O_E（hat-⊗ 的下标被排到上标位） | 排版讹误 | 按语义排 `\Gr^{\mathrm{PR}}\widehat{\otimes}_{\FF_q}\oo_E` | 页面图像 p.25 | 已归一 |
| 7 | p.26 | faithfull topology | 拼写 | 译文「忠实拓扑」 | 页面图像 p.26 | 已解 |
| 8 | p.26 定义 3.17 | perfectoif affinoid | 拼写 | 译文「完满 affinoid」 | 页面图像 p.26 | 已解 |
| 9 | p.27 猜想 3.21 后 | satiﬁes descent | 拼写 | 译文「满足下降」 | 页面图像 p.27 | 已解 |
| 10 | p.23 §3 标题 | Grassmanian | 拼写 | 少一 n；译文用正确拼写，不另注 | 原文目录 | 已解 |
| 11 | p.28 | 无 §3 内容 | 体例冲突 | 见遗留 1 | 逐页文本 p028.txt | 待裁 |
| 12 | s06-statement.tex 第 6 行译注 | 称「全文并无编号 3.21 的猜想」 | **误判** | §3.5 确实有猜想 3.21（Conjecture 3.21，本文件 `conj:3.21`），s06 的交叉引用是对的；建议 Lead 删除 s06 该条译注 | 本文件 §3.5；原文 p.27 | 待改（他文件） |

## 4. 术语与新增术语建议

按 `glossary.tsv` 用工：B_dR-仿射 Grassmann 簇、Hecke 叠、Hecke 对应、Hecke 特征层（本块未出现，留待 §6）、Schubert 胞腔、几何 Satake 等价、六函子形式化、球 Hecke 代数、反常层、特征层、Beauville–Laszlo 单值化、等特征、不等特征、Cartier 除子、形式完备化、余特征、支配的、环面、约化群、完满、菱形、adic 空间、Witt 向量、刚性解析空间。

建议补入 glossary 的新译（本块首次出现）：
`torsor` 扭子｜`pro-étale torsor` pro-étale 扭子｜`partially proper` 部分 proper｜`twisted affine Grassmannian` 扭仿射 Grassmann 簇｜`hyperspecial` 超特殊｜`perfection` 完满化｜`ind-perfectoid` ind-完满｜`analytification` 解析化｜`descent theory` 下降理论｜`relative position` 相对位置｜`semi-continuous` 半连续｜`minuscule` 极小｜`intersection cohomology complex` 相交上同调复形｜`cohomological correspondences` 上同调对应｜`faithful topology` 忠实拓扑｜`modification` 修正｜`gluing` 黏合｜`overconvergent` 超收敛｜`without boundary` 无边界。

## 5. 译注（8 条）

1. §3.1 约定 Spa(E)⋄=Spa(E)（A/I）
2. §3.1 竖箭头小图体例（`\yizhuw`）
3. 定义 3.1 后：B_dR⁺(R) 的来历（A：原文 §1.6.2；Fontaine 1979）
4. §3.3.2 标题 equal/unequal 笔误（`\yizhuw`）
5. 期望 3.15：“Hope” 弱于 “Conjecture”，译文作「期望」（`\yizhuw`）
6. 期望 3.15：Witt 向量仿射 Grassmann 簇（A：原文 p.26，引 [32]、[29]）
7. §3.5 开头：^LG=Ĝ⋊Γ 的含义（A：原文 p.27、p.28）
8. 猜想 3.21(3)：minuscule 余权（A：Bourbaki, Lie Groups and Lie Algebras, Ch. VI）

## 6. 遗留与建议

1. **p.28 页锚重复**：本节末尾的 `\srcpage{28}` 与 `s06-statement.tex` 首行的 `\srcpage{28}` 重复。建议 Lead 删除本节末尾那一行（p.28 起点由 §4 承担）。
2. **\marginnote 可见性不稳**：`_check_d.pagemarks` 六条齐全，但 check 版 PDF 中只有部分锚可见（project 内 s02 亦然：8 个锚仅 4 个可见）。preamble 已注明「任何不可见的情况都能事后核查（tools/check_pagemarks.py）」，故本文件只保证源码位置正确、pagemarks 齐全，不再为可见性调排版。
3. **\Hck 未采用**：preamble 的 `\Hck` 印作正体 “Hck”，原文实为斜体 *Hecke*；本文件统一用 `\mathit{Hecke}^{\le\mu}`。若 Lead 要全书统一，建议改 preamble 或统一改用 \Hck（二者择一，勿混用）。
4. **宏兜底**：`\llbracket/\rrbracket` 仍无 stmaryrd，本文件与 s02 各自 `\providecommand`；若 Lead 在 preamble 加 stmaryrd，两处 `\providecommand` 会自动让位，无需改动。
5. **引文编号**：[1][5][6][21][27][29][32] 均以字面 [] 排入正文（与本工程 s02、s06 的做法一致），未用 `\cite`；s99-bibliography 编号须与之对应。
