# e09d 自检报告（译者 tr4）

- 块：§9.7 分歧与抛物结构 + §9.8 分歧局部系统的 Hecke 本征层（en 正文 22,363 字符 → tex 10,400 字符，29 段一一对应，2 个 \subsection）
- 范围说明：en:389–550 的 `\newpage`、`%\printindex` 与 `\begin{theindex}…\end{theindex}`（约 155 条英文索引项）未收入 tex 块——`latex/main.tex:95` 已有 `\printindex`、`:92` 已有 `\input{tex/biblio}`，收入会重复排版；索引项本身为英文，与 `\index` 键一一对应，不译
- 数学：脚本逐条比对 display 块 3/3（2 个 equation + 1 个 `$$`）与 align* 图，逐字符一致；行内公式 en 311 / tex 310，唯一差异是 en:165 笔误重复了一个 `$\F$`（见下），非漏译
- 计数：label 4/4、eqref 10/10、cite 11/11、index 7/7（键与顺序均同）、footnote 5/5、subsection 2/2，段落 29/29
- 术语：球 Hecke 代数、尖点球函数、阿代尔群、半单共轭类、驯分歧、容许表示、Iwahori 子群、仿射旗簇、卷积张量积、范畴化、抛物结构、模叠/模空间、幂零 $^L \g$-oper、临界线丛、Verma 模、局部化函子、非正则奇点、水平结构
- 修正记录：补回漏掉的 `\index{geometric Langlands correspondence}`；补回 Iwahori 子群定义中 en 的第二个 `$G(\OO_y)$`；补回「在 $y$ 处」「$X$ 上」两处漏掉的 `$y$`/`$X$`；删去译文中多出的 2 个 `$\chi$` 与 2 个 `$X$`
- 原文疑似笔误（未改，仅记录）：(1) en:99 `no no-zero` 应为 `no non-zero`；(2) en:128 脚注 `\dim \pi_i^K = 1` 应为 `\pi_y^K`；(3) en:165 `where $\F$ a $^L G$-bundle $\F$ on $X$` 重复 `$\F$` 且缺系词 is；(4) en:234 `of $\ghat_y$ a the critical level` 应为 `at the critical level`
- 指令保留：无 `% ZHU-CAND`；无译注
