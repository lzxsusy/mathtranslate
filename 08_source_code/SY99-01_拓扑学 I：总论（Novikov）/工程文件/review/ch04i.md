# 核验报告 · ch04i（原书 p.239–243）

核验人：译者庚　　作者：译者己　　日期：2026-11-09

## 结论
需修改（3 条必须改，其中第 1 条会让 lualatex 直接编译失败；第 3 条是漏译 p.243 末的引导句）

> **复核（2026-11-09，闭环）**：作者已按清单全部改正——6 处 `\mathcal{N}` 定界符修好（逐字符复查无 `$X$\mathcal` 残片）、(4.17)(4.18) 分母改为花体 `\mathcal{G}`/`\mathcal{J}`、p.243 末引导句「由此可推出如下推论：」已补在文件末尾（lead 已确认此句归 ch04i）；另采纳 :41 语序、:120「由此可得」、$J$-同态长句拆分三条建议。复核 `check_chunk.py` → OK，页标记 239–243 共 5 条，全稿 p.239 无重复。

## 必须改（影响正确性）
1. **6 处 `\mathcal{N}` 定界符损坏，会直接编译失败**（check_chunk.py 只查 `$` 成对，查不出这类错误）：
   - 第 10 行 `$\bar{\mathcal{N}}$\mathcal{N}(X^n,\xi)$` → `$\bar{\mathcal{N}}(X^n,\xi)$`
   - 第 37 行 `$\alpha\in N$\mathcal{N}(M^n,\xi)$` → `$\alpha\in\mathcal{N}(M^n,\xi)$`
   - 第 51 行 `$N$\mathcal{N}(M^n,\nu_n)$` → `$\mathcal{N}(M^n,\nu_n)$`；同段 `$G$\mathcal{N}(M^n,\nu_n)$` → `$\mathcal{G}(M^n,\nu_n)$`
   - 第 57 行 `$J$\mathcal{N}(M^n,\nu_n)$` → `$\mathcal{J}(M^n,\nu_n)$`；同段 `$G$\mathcal{N}(M^n,\nu_n)$` → `$\mathcal{G}(M^n,\nu_n)$`
   - 第 68 行 `$\bar{\mathcal{N}}$\mathcal{N}(M^n,\nu_n)$` → `$\bar{\mathcal{N}}(M^n,\nu_n)$`
   - 第 90 行 `$\alpha\in N$\mathcal{N}(M^n,\xi)$` → `$\alpha\in\mathcal{N}(M^n,\xi)$`
   共性：符号前的正体字母（N、G、J）后多出一个 `$`，把公式截断成两段数学模式夹一段文字。修完请重跑 check_chunk 并**用 lualatex 前的 grep 自查**：`Select-String -Pattern '\$[^$]*\$\\mathcal' src\chunks\ch04i.tex` 应无输出。
2. **(4.17)、(4.18) 的分母应为花体 `\mathcal{G}`、`\mathcal{J}`**（第 53、59 行）。原书 p.240 分母印刷为花体 $\mathcal{N}/\mathcal{G}$、$\mathcal{N}/\mathcal{J}$，现写作正体 `N/G`、`N/J`。请改为 `\mathcal{N}/\mathcal{G}`、`\mathcal{N}/\mathcal{J}`，与同段正文里的 $\mathcal{N}$、$\mathcal{G}$、$\mathcal{J}$ 记号统一。
3. **漏译 p.243 末句（引导句）**：「由此可推出如下推论：」（原书 From this divisibility result one may infer the following corollary:）。ch04i 现在停在「……分母为 $7$ 的分数（见 §3）。」即止。这句是 p.243 的最后一行、也是第 4 章 §4 与 §5 的交界句，按 BRIEF 分工应由 ch04i 收尾，ch04j 从 p.244 的无编号推论开始（已完成）。请补在文件末尾。

## 建议改（可读性/文风）
1. 第 41 行「这对 $n=4k$ 的情形同样成立，是充分必要条件」——中文语序不顺，建议「这一条件对 $n=4k$ 的情形也是充分必要的」（原书：this condition is also sufficient and necessary for n = 4k）。
2. 第 68 行是一个很长的句子（「由同伦等价 $f:M''\to M'$ 的代数构造，我们得到一个流形 $M_1$，以及一个 $PL$ 同构 $M_1\to M$；如果……则存在一个同伦等价 $f_2:M''\to M$，它可形变为一个微分同胚」），建议在分号处断句。
3. 第 120 行「由这个同构可知：」——原书是「From this isomorphism one obtains the obstructions …」，此处「这个同构」指 (4.19)，建议改「由这个同构可以得出」或直接「由此可得」。
4. 第 128 行脚注 10 的人名「Madsen, Milgram」按原书保留，正文提到「Sullivan 的结果至今（1994 年）尚未有完整证明发表」——原书如此（up to the present (1994)），译文照抄正确，可在 Tutor Note 点一句「这是 1990 年代初的写作时态」。
5. $SG_q$/$\overline D f$ 段落里「$q\to\infty$ 的极限下的半群 $SG$」建议写作「$q\to\infty$ 时的稳定半群 $SG$」，与后文「谱 $SG_q\subset SG_{q+1}\subset\cdots$」呼应。

## 抽查记录（逐页）
- **p.239**（`pages\p246.png`）：段首「Cartan–Serre 理论表明，稳定群 $\pi_{n+N}(T\xi)$ 具有形式」(4.14) $\pi_{n+N}(T\xi)=\Z\oplus\bar{\mathcal N}(X^n,\xi)$；「至少存在一个元素 $\alpha$，其分离维数等于 $X^n$ 的维数」；对应 (4.15) $\alpha=1+a$；恒等映射诱导的交换图（tikz）；断言「对 $n\ge5$，任意两个实现同一元素 $\alpha$ 的流形 $M_1^n$、$M_2^n$ 都同胚，且挖去一点后微分同胚；$n>5$ 且 $n$ 为偶数时它们甚至微分同胚」(4.16) $M_1^n\cong\Sigma^n\#M_2^n$（$\Sigma^n\in bP^{n+1}$）；0 元素对应平凡配边；**Result 2**（奇 $n\ge5$：每个 $\alpha\in\mathcal N(M^n,\xi)$ 由同伦等价 $f:M'\to M^n$ 实现，且 $L(p_1(\xi),\dots,p_k(\xi))=\tau(M^n)$）——逐句一致（除必须改 1 的定界符）。
- **p.240**（`p247.png`）：Browder 与 Novikov 关于「$n=4k$ 时条件同样充分必要」；有限性推论（给定同伦型与 Pontryagin 类 ⇒ 只有有限多个光滑结构与 PL 结构）；Remark 及 □；可形变为微分同胚的判据：陪集 $f_1[f]^{-1}$、$f_2[f]^{-1}$ 在 $\mathcal N(\cdot,\xi)$ 中相等，且 $f_1f_2^{-1}$ 同伦于微分同胚模 $bP^{n+1}$；(4.17) $\mathcal N/\mathcal G$、(4.18) $\mathcal N/\mathcal J$——内容正确，仅符号字体与定界符须改（必须改 1、2）。
- **p.241**（`p248.png`）：$T\nu_M=S^{N+n}/(S^{N+n}\setminus U_\eps)$、$N\gg n$；$n=4k+2$ 时 $1+a$ 中 $a$ 属于指数 1 或 2 的子群 $B$；Golo 与 Wall 的带边推广；脚注 9（A. Schwarz，Novikov，Sullivan）；Spanier–G. W. Whitehead $S$-对偶 $DK=S^m\setminus K$、$D:K\mapsto S^m\setminus K$、$Df:DL\to DK$、$[K,L]_s=[DL,DK]_s$；Atiyah 的 $D(T\nu_M)=\Sigma(M^n_+)=T\eps^q$、$M^n_+=M^n\cup\{*\}$、$Df:T\eps^q\to S^q$——一致。
- **p.242**（`p249.png`）：$SG_q$ 半群、$\overline Df:M^n\to SG_q$（$q\to\infty$）、$SG_q/SO$ 中的障碍；谱 $SG_q\subset SG_{q+1}\subset\cdots$、$SG\supset SPL\supset SO$；$\pi_j(SG)=\pi_{N+j}(S^N)$（$N>j+1$）；$BSG$；$SG_q\sim\Omega^q(S^q)$、$\pi_j(\Omega^q(S^q))\cong\pi_{q+j}(S^q)\cong\pi_j(SG)$；$BSG$ 不是 $(q-1)$-重环路空间；微丛与 $PL$ 流形切微丛；(4.19) $\pi_j(SPL,SO)=\pi_j(SPL/SO)=\Gamma^{j-1}$——一致。
- **p.243**（`p250.png`）：$PL$ 流形 $M$ 的 $j$ 维骨架邻域上光滑结构的存在障碍为上同调类 $H^j(M;\Gamma^j)$；$PL$ 流形理论史（Newman、Whitehead、Zeeman、Munkres、Mazur、Hirsch 等）；小开区域上的「局部」光滑结构、Morse 手术在小可平行化区域中进行；$PL$ 丛的自同构多于光滑丛 ⇒ 用 $S$-对偶时 $PL$ 同构的障碍是映射 $M^n\to SG/SPL$ 的同伦类；1966 年 Sullivan 与 Wagoner 证明 $\pi_j(SG/SPL)=\pi_j(G/PL)$ 的四周期性（$\Z$、$0$、$\Z/2$、$0$）；脚注 10（Madsen–Milgram，1979）；$\pi_j(SPL/SO)\cong\Gamma^{j-1}$、$\pi_j(SO)\to\pi_j(SPL)$ 在 $j\le6$ 同构、$j=7$ 时像的阶被 7 整除、$BSO\to BSPL$、$PL$ 流形的 Pontryagin 类分母可为 7；**末句引导句须补（必须改 3）**。

## 体例抽查
- 页标记：`% [原文 p.239]`–`p.243]` 共 5 个，递增无重复 ✓。注意 p.239 在 ch04h 第 372 行还出现一次（越界重复），处理见 `review/ch04h.md` 必须改 2：删 ch04h 的那条，保留本块首行这条。
- 编号：ch04h 的 (4.13) 之后接 (4.14)–(4.19)，共 6 个，连续无缺号 ✓。
- 陈述：Result 1/Result 2 用 enumerate 排出（原书用斜体编号 1./2.），Remark 带手写 `\hfill$\square$`（原书有 □）✓；无编号定理陈述用带星环境，符合「□ 判断规则」✓。
- 脚注 9、10 就地译出 ✓；Tutor Note 2 条（5 页，要求 ≥1）✓；`% CHUNK ch04i DONE` 末行 ✓；check_chunk 0 error（但查不出必须改 1 的定界符问题，见上）。
- 图表：本块无图（图 4.21–4.27 均在 ch04g/ch04h），符合原书 ✓。
