# e01a QA（§1.1–1.4 伽罗瓦群、阿贝尔类域论、Frobenius 自同构、ACFT 的刚化）

- 规模：en 24,243 字符 → 译文 11,845 字符；段落 43/43；`$$` 20/20、equation 7/7、subsection 4/4、label 9/9、eqref 13/13、cite 3/3、index 17/17、footnote 7/7。
- 数学：显示公式 17/17 逐字符一致；行内公式 456/456 归一化后完全一致（`check_math.py e01a` 通过）。
- 结构：四个 `\subsection` 译作「伽罗瓦群」「阿贝尔类域论」「Frobenius 自同构」「ACFT 的刚化」；`\label{acft}` 前的四个空格、`\begin{equation}` 与其后 `\label` 之间的四空格均原样照抄。
- 数学环境内英文未译：(1.5) 式中两处 `\boxed{\begin{matrix}\text{Galois group}...\text{components of }...}` 依 Lead m00057 逐字符保留。
- 术语：数域、分圆域、伽罗瓦群、极大阿贝尔扩张、逆极限、p-进数/p-进整数、阿代尔、伊代尔、剩余域、分解群、惯性群、非分歧、共轭类、互反律；`Frobenius automorphism` 按 TERMS 作「Frobenius 自同构」，`Frobenius element` 作「Frobenius 元」；`local system` 按 STYLE.md §3 作「局部系统」（e06 报告取「局部系」，与 STYLE 相反，已一并报 Lead）。
- 存疑（照录原文，未改）：① 三处 `$\on{Gal}(\OO_K/w,\OO_L/v)$` 中的 `\OO_L` 疑应为 `\OO_F`；② 原文第 293 行 `$\wh{Z}$` 用大写 Z，与其余 `\wh\Z` 不一致；③ `Can relate this group to...?` 原文脱主语 we，译作「能否把这个群与……联系起来？」。
- 自检：无 `\section`/`\begin{document}`；UTF-8；中文标点全角、中文与公式间无空格；正文无裸露 `& % # _`；无 `% ZHU-CAND`。
