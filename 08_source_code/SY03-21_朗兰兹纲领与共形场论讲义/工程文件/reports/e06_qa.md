# e06 QA（§6 C 上的几何朗兰兹猜想、双参数形变、D-膜）

- 规模：en 31,124 字符 → 译文 15,999 字符；equation 4/4、$$ 6/6、subsection 4/4、label 8/8、eqref 9/9、secref 19/19、thmref 2/2、conjref 1/1、cite 15/15、index 10/10、footnote 3/3。
- 数学：显示公式 10/10 逐字符一致；行内公式多重集之差 4 项，皆为有意——3 项出自 ZHU-CAND 注释、1 项为中文化「$\M'(\OO_x)$ 的截面」复述符号，数学内容未变。
- 结构：段落与原文一一对应（含 `{}From now on` 行首的 `{}`）；数学环境内 `\text{}`、`\begin{CD}` 标签、framebox 内的英文一律未译（依 Lead m00044），初稿误译的 3 处已改回。
- 术语：一律从 TERMS.md；与 STYLE.md 第 20 组表冲突时按 TERMS（几何 Langlands 对应 / Langlands 对偶群 / 局部系 / Langlands 纲领），此裁决记录在案。
- 译名处理：opers 全小写不译；D-模、D-膜、Hecke 本征层、反常层、摩天大楼层、扭余切丛、oper 条件、扭子（torsor，首现加英文）。
- ZHU-CAND 1 条：第 6 节「whereas for $\la \neq 0$ a $\la$-connection…」第二个条件应为 $\la=0$，否则与紧接下句 $\on{Loc}^0_G \simeq T^*\Bun_G^\circ$ 矛盾；译文照录原文，注记在 tex 第 136 行。
- 原文笔误：即上条（唯一发现）。
- 自检：无 `\section` / `\begin{document}`；UTF-8；正文 `& % #` 已转义；中文标点全角，中文与公式间无空格。
