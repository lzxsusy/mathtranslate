# SY02-38《朗兰兹纲领入门课程讲义》中文译注本 · 施工规范（STYLE GUIDE）

<!-- TRANSLATION-STANDARD:v2.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.1** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（SY02-09 / SY02-24 术语表），再查 nLab / Stacks Project 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制，权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：`04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md

> 本文件是全体译者的**唯一体例依据**。开工前必须通读；有疑问先读 BRIEF.md，再问 Lead。

---

## 0. 底本是什么

- 底本：Johannes Anschütz, *Lecture notes for an introductory course on the Langlands program*（2020-07-22 修订稿，103 页，含 Ben Heuer 的三讲：第 7、8、10 讲）。
- **这是讲义，不是教材**：条目式正文，大量「Last time / Fact / Upshot / Note」标签，定义与定理多数只给陈述，证明常写「sketch」或直接引 [GH19]。
- 两种文风并存：Anschütz 本人的条目体（第 1–6、9、11、12 讲）与 Heuer 的三讲（第 7、8、10 讲，编号、定理、脚注更密）。**两种都要保留各自的结构，不做跨讲统一改写。**
- 原文页 = PDF 页（无偏移）：`work/pages/pNNN.txt`，NNN 为 PDF 页号三位（如 `p011.txt`），首行有 `===== BOOK PAGE 11 (PDF 11) =====` 标记。

## 1. 坐标与分工

| 讲 | 内容 | PDF 页 | 作者 |
|---|---|---|---|
| 1 | 关于本讲稿的说明 | 2 | Anschütz |
| 2 | 一般性介绍 | 3–10 | Anschütz |
| 3 | 从模形式到自守表示 I | 11–23 | Anschütz |
| 4 | 从模形式到自守表示 II | 24–32 | Anschütz |
| 5 | 从模形式到自守表示 III | 33–45 | Anschütz |
| 6 | 新形式的 Langlands 互反 | 46–54 | Anschütz |
| 7 | 模曲线作为椭圆曲线的模空间 | 55–61 | Heuer |
| 8 | Eichler–Shimura 关系 | 62–69 | Heuer |
| 9 | 附着于新形式的 Galois 表示 | 70–78 | Anschütz |
| 10 | 权 1 形式的 Galois 表示 | 79–87 | Heuer |
| 11 | 一般群的 Langlands 纲领 I | 88–93 | Anschütz |
| 12 | 一般群的 Langlands 纲领 II | 94–101 | Anschütz |
| — | 参考文献 | 102–103 | — |

每个译手**只写自己那一讲的 `源码/chapters/lectureNN.tex`**，不改 main.tex、不改别人的文件、不改 `work/` 下的术语表（发现要改，写进 `work/reports/lectureNN.md` 交 Lead 处理）。

## 2. 原样保留的东西（红线）

1. **条目层级**：原文的 `•`、`–`、`1.`、`2.` 是结构，不是排版噪声。译文用 `itemize`/`enumerate` 一一对应，层级不能合并、不能升格。
2. **标签**：`Last time` → **上次**；`Upshot` → **要点**；`Fact` → **事实**；`Note` → **注**；`Sketch` → **略述**；`cf.` → **参见**；`Recall` → **回忆**；`Hence` → **因此**。标签统一加粗。
3. **编号**：原文的定义/定理/命题/引理/推论/猜想/例/注的编号（如「定义 2.1」「定理 9.1」「引理 8.2」）**原样保留**，不得重编。公式编号 (1)(2)(3) 原样保留。
4. **引用**：`[GH19, Lemma 3.7.1]` 这类文献引用原样保留，不翻译文献名、不改编号。
5. **公式**：一律逐符号核对 `work/pages/pNNN.txt`；提取文本的连字（ﬁ、ﬂ）、上下标错位、`\u0012` 之类矩阵括号乱码**必须**按页面重建，不能照抄。矩阵用 `\begin{pmatrix}…\end{pmatrix}`。
6. **不补证、不改写、不加小节、不删条目**。原文说「不证明」就不证明；原文只说「cf.」就只说参见。

## 3. 文风

- 中文**讲解体**：句子短，逻辑连接显式（「于是」「从而」「注意」「这里」），允许「我们」。
- 术语按 `work/glossary.tsv` 冻结；一个概念只用一种译法，首次出现可在括号里附英文原词。
- 数学陈述里的 `we`、`one`、`the reader` 不硬译成「我们」时可用无主句；但**不要**写成文言或口语化过度（不用「搞」「弄」「说白了」）。
- 每个 `itemize` 条目译文尽量不超过 3 行；长条目按原意断成子条目（保持原层级语义）。

## 4. 术语（冻结，摘录；全表见 `work/glossary.tsv`）

adelic 阿代尔的；adèle 阿代尔；idele 伊代尔；reductive group 约化群；parabolic subgroup 抛物子群；Levi subgroup Levi 子群；unipotent radical 幺幂根基；automorphic form 自守形式；automorphic representation 自守表示；cuspidal 尖点的；cusp form 尖点形式；Eisenstein series Eisenstein 级数；moderate growth 适度增长；rapid decrease 速降；admissible 容许的；smooth representation 光滑表示；Hecke algebra Hecke 代数；Hecke operator Hecke 算子；Hecke eigensystem Hecke 特征系统；spherical Hecke algebra 球面 Hecke 代数；modular form 模形式；weight 权；level 级；nebentypus 旁特征；newform 新形式；oldform 旧形式；eigenform 本征形式；q-expansion q-展开；cusp 尖点；modular curve 模曲线；elliptic curve 椭圆曲线；isogeny 同源；quasi-isogeny 准同源；Tate module Tate 模；Tate curve Tate 曲线；moduli problem 模问题；representable 可表的；stack 叠；generalized elliptic curve 广义椭圆曲线；compactification 紧化；line bundle 线丛；ample 丰沛；Hasse invariant Hasse 不变量；ordinary 普通的；supersingular 超奇异的；q-expansion principle q-展开原理；Galois representation Galois 表示；unramified 非分歧；ramified 分歧；inertia group 惯性群；Frobenius element Frobenius 元；arithmetic Frobenius 算术 Frobenius；geometric Frobenius 几何 Frobenius；residual representation 剩余表示；de Rham representation de Rham 表示；Hodge–Tate weight Hodge–Tate 权；étale cohomology 平展上同调；cohomology with compact support 紧支上同调；interior cohomology 内上同调；Kummer sequence Kummer 序列；Weil pairing Weil 配对；Picard group Picard 群；Satake parameter Satake 参数；Satake isomorphism Satake 同构；L-group L-群；dual group 对偶群；L-parameter L-参数；L-packet L-包；Arthur parameter Arthur 参数；functoriality 函子性；trace formula 迹公式；multiplicity one 重数一；strong multiplicity one 强重数一；L-algebraic L-代数的；Shimura variety Shimura 簇；Shimura datum Shimura 数据；canonical model 典范模型；reflex field 反射域；automorphic vector bundle 自守向量丛；Hermitian symmetric domain Hermite 对称域。

**易错**：`[G]` 保留记号不译；`K_∞`、`K(m)`、`K_1(m)`、`Γ_0(m)`、`Γ_1(m)`、`Γ(N)` 保留记号；`A_G` 保留；`|·|_adélic` 译作「adélic 绝对值」并保留记号 `|\cdot|_{\mathrm{ad\acute elique}}`；`χ_no` 保留记号。

## 5. 译注

- 只在三种情况下写译注：**易错预警**（读者会读错的地方）、**含糊点拨**（原文一笔带过、需补一步）、**背景直觉**（概念的第一直觉）。
- 每讲译注 **3–8 条**，不宜更多；每条只讲一件事，不超过 5 行。
- 格式：`\zhnote{……[来源：nLab "Eichler-Shimura relation"，\url{https://ncatlab.org/…}（2026-11-26 访问）。]}`；无外部依据时只准 `\zhnoteplain{……}`。
- 原文已知笔误（见 `work/疑点清单.tsv`）在译注里说明「原文作 X，此处按 Y 译」，**不要**在正文里偷偷改掉而不作声。

## 6. LaTeX 体例

- 不使用 `\chapter` 自动编号的定理环境；**编号手写**：
  ```latex
  \noindent\textbf{定义 2.1}\phantomsection\label{def:2.1}\quad 设 $G$ 为……
  ```
  交叉引用写 `\hyperref[def:2.1]{定义 2.1}`（保证链接与显示编号一致）。
- 公式编号：`\begin{equation}\tag{1}\label{eq:1} … \end{equation}`；无编号用 `\[ … \]` 或 `equation*`。
- 每页开头写页标记注释（**单独一行，前后不留空行**）：
  ```latex
  % ===== PDF p.011 =====
  ```
- 每个 `\item` 内不要空行；条目之间不空行。段落之间最多一个空行。
- 矩阵、长公式允许 `align*`；不要用 `\begin{cases}` 的 `\\` 后加空行。
- 中文标点用全角，数学内用半角；`，` 与 `；` 不要出现在数学模式里。
- 强调：`\textbf{…}` 用于标签与术语首次出现；`\emph{…}` 少用。

## 7. 交稿（每个译手）

1. `源码/chapters/lectureNN.tex`（唯一你该写的文件）。
2. `work/reports/lectureNN.md`：5 行——译了哪些页、遇到的疑点、新增/修改的术语、译注条数、未决问题。
3. 若发现术语表要改或原文有错，写进上面那份 report，不要直接改 `work/*.tsv`。
4. 自检：文件里页标记数 = 你负责的页数；`\begin{itemize}` 与 `\end{itemize}` 配对；没有 `\chapter`、没有 `\documentclass`、没有 preamble。
