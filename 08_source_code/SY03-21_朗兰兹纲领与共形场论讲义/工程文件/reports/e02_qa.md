# e02 QA（§2 从数域到函数域）

- 规模：en 32,430 字符 → 译文 14,975 字符；段落 76/76；`$$` 16/16、equation 8/8、subsection 4/4、label 11/11、eqref 4/4、secref 5/5、thmref 2/2、cite 6/6、index 11/11、footnote 7/7。
- 数学：显示公式 16/16、行内公式 516/516 归一化后逐字符一致（`check_math.py e02` 全 [OK]）。
- 结构：本节由 `main.tex` 提供 `\section{从数域到函数域}`，故 e02 以散文开头、无 section 命令；四个 `\subsection` 译作「函数域」、「Galois 表示」（`\label{galois}`）、「自守表示」（`\label{autrepr}`）、「朗兰兹对应」；`\index{function field}`、`\index{Langlands correspondence}` 单列一行，位置照抄；结尾保留 `\newpage` 与 `\vspace*{10mm}`。
- 数学环境内英文未译：定理 `\label{langl}` 前后两个 `center`+`\framebox{$\begin{matrix}...\text{...}$}` 示意图的 `\text{}` 英文依 Lead m00057 逐字符保留；`$\sigma \longleftrightarrow \pi$` 照抄。
- 术语：函数域、有理函数域、函数环、极大理想、剩余域、仿射直线、形式 Laurent 幂级数、形式 Taylor 级数、一致化元（uniformizer，首现括注）、局部坐标、覆叠/覆叠变换、射有限完备化、分解群、惯性子群、非分歧、幂幺根、标准抛物子群、诱导表示、连续谱、球 Hecke 代数、双陪集、初等对称多项式、基本表示、半单共轭类、强重数一定理、几何 Frobenius 元、Ramanujan–Petersson 猜想、Deligne 纯性猜想、Maass 形式；人名与 `\emph{}` 书文名保留原文。
- 存疑（照录原文，未改）：① 函数环 `${\mc R} = \R[x,y]/(x^2+y^2+1)$` 与方程 `$x^2+y^2 = -1$` 符号不一致（疑应为 `-1`）；② 方程 \eqref{ellcurve} 的 `$a,b,c \in \Fq$` 中 `c` 在方程里未出现；③ `$\mu^{p^n} - 1 \in \ell^{p^n} \Z_\ell$` 与 `$|\mu^{p^n} - 1|_\ell \leq p^{-n}$` 的指数疑应为 `n`（`p^n` 处）；④ `$(z_1,\ldots,z_N)$` 大写 `N` 疑应为小写 `n`；⑤ `\secref{Frob}` 首字母大写，与 label `frob` 不一致；⑥ 行文 `it can shown`（脱 be）见 e01b。
- 自检：无 `\section`/`\begin{document}`；UTF-8；中文全角标点、中文与公式间无空格、中文与英文缩写间一个半角空格；正文无裸露 `& % # _`；无 `% ZHU-CAND`（原文概念无缺注之处，疑问已列入上书）。
