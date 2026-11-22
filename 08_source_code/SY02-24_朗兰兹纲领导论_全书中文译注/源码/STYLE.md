# 全书译注工程 · 施工说明（STYLE.md）

底本：J. Bernstein, S. Gelbart 编，*An Introduction to the Langlands Program*，Birkhäuser 2004。
本工程把全书 12 章译成中文译注本，按本库《数学文献翻译纪律》v2.1 执行。

## 目录约定

- 原文抽取件：`work/en/chNN_raw.txt`（`===== BOOK PAGE n (PDF m) =====` 分页，BOOK PAGE 即原书页码）。
- 页面图像：`work/pages/cNN_pNNN.png`（150 dpi，文件名里的数字是 **PDF 页**；原书页 = PDF 页 − 2）。
- 译文源文件：`src/chapters/chNN.tex`，每章一个文件，以 `\chapter{中文章名}\label{ch:NN}` 开头。
- 编译：`src/main.tex`（xelatex 三遍）；`\InputIfFileExists` 只读已存在的章文件。

## 硬规则（按优先级）

1. **先通读后落笔**：先读完整章 `chNN_raw.txt`，写 `work/notes_chNN.md`（三句话主旨、逐节内容地图、体裁、风险点），再动笔。
2. **公式回页图核对**：抽取件的公式一律不可信，逐符号对照 `work/pages/cNN_pNNN.png`。
3. **编号照原书**：节号、公式号、定理号一律沿用原书（`\section` 自动给原书节号；带编号的条不用重编）。
4. **译注**：每章 8–15 条，三类（易错预警／含糊点拨／背景直觉），每条必须给出具体信息，并以
   `\par\vspace{0.15em}{\raggedleft 【来源：…（A|B|I）】\par}` 结尾。
   来源分级：A＝原书/作者论文/经典教材；B＝nLab、Stacks Project、ProofWiki（须与 A 交叉）；
   I＝本库既有译法。**禁引**：知乎、百度百科、CSDN、简书、公众号、个人博客、视频课笔记。
   允许并鼓励查外部文献补注（Serre《A Course in Arithmetic》、Iwaniec–Kowalski、Bump、
   Gelbart、Tate 论文、Milne 讲义、nLab、Stacks Project），但每条都要落到 A/B 级并写清依据。
5. **语言**：中文数学工作者文风；一句 60–70 汉字内；中文全角标点；英文术语与汉字间半角空格；
   禁「被……所……」「进行……的」「对于……而言」。
6. **LaTeX**：只用下节列出的宏；中文标点在数学模式外；`\label`/`\ref` 不硬编码。
   编译须 0 error、0 undefined、0 overfull。

## 可用宏（已定义，勿重复定义）

`\Fq \A \cK \cO \sO \GL \Funct \Bun \sBun \sH \Fc \Gr \Hom \Spec \Pic \Fr \Fl \diag \cusp \Ql \Flq`
（含义见 `src/main.tex` 注释；不敷使用时直接写标准 LaTeX。）

环境：`\begin{annote} … \end{annote}`（译注，左侧灰竖线）；`\ob{编号}{label}`（原书编号段）。

## 术语（沿用全书统一译法，勿自创）

automorphic form 自守形式；automorphic representation 自守表示；cuspidal 尖点的；
unramified 无分歧；ramified 分歧；Hecke operator Hecke 算子；Hecke algebra Hecke 代数；
spherical representation 球表示；adele 阿代尔；admissible 容许的；Whittaker model Whittaker 模型；
L-function L 函数；local field 局部域；residue field 剩余域；uniformizer 一致化子；
modular form 模形式；elliptic curve 椭圆曲线；Galois representation Galois 表示；
Frobenius element Frobenius 元；class field theory 类域论；functoriality 函子性；
Langlands dual group 朗兰兹对偶群；root datum 根数据；reductive group 约化群；
trace formula 迹公式；Eisenstein series Eisenstein 级数；Hecke character Hecke 特征；
Dirichlet character Dirichlet 特征；zeta function zeta 函数；gamma factor 伽马因子。

## 交付

每章交：`src/chapters/chNN.tex`（含译注）、`work/notes_chNN.md`（通读笔记）。
回复只需三行：章名／文件行数／译注条数／未解决的疑点。
