# e00 QA（引言 + 致谢）

- 规模：en 19,730 字符 → 译文 7,227 字符；`$$` 2/2、subsection 0/0、cite 24/24、index 9/9、footnote 0/0、label 0/0、eqref 0/0。
- 数学：显示公式 2/2 逐字符一致；行内公式 111/111，归一化后完全一致（`check_math.py e00` 通过）。
- 结构：原文首行 `\section*{Introduction}` 已删（"引言"小节标题由 `main.tex` 提供），故 33 段 = 原文 34 段减该标题；结尾 `\bigskip`、`\newpage`、`\vspace*{10mm}` 原样保留。
- 数学环境内英文未译：两个 `\boxed{\begin{matrix}...\text{holomorphic rank $n$ bundles}...}` 及 `\text{Hecke eigensheaves on }` 逐字符照抄（依 Lead m00044/00057）。
- 术语抽查：几何朗兰兹对应、朗兰兹对偶群、Hecke 本征层、D-模、共形块、临界水平 $k=-h^\vee$、仿射 Grassmannian（不译）、oper（小写不译）、局部系统（按 STYLE.md §3，不用「局部系」）。
- 译名：R. Langlands、E. Witten、P. Goddard、J. Nuyts、D. Olive、V. Drinfeld、V. Sokolov、A. Beilinson、A. Kapustin、G. Laumon 等一律保留；「D-膜」「D-模」带引号处照原文。
- 存疑（未改，仅记录）：原文两处写作 "t'Hooft"（缺前引号），STYLE §3 作 't Hooft；译文照录原文。
- 自检：无 `\section`/`\begin{document}`；UTF-8；中文标点全角、中文与公式间无空格；无 `% ZHU-CAND`（原文此处叙述完整，未觉需注）。
