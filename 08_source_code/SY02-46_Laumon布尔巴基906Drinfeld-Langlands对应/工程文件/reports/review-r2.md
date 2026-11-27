# SY02-46 中译本独立审校 r2

**审校范围**：`源码/sections/s04-perverse.tex`（§3，p8–9）、`s05-autprime.tex`（§4，p9–11）、`s06-fourier.tex`（§5，p11–13），合计 44 + 105 + 135 = **284 行**；逐句对读法文权威源 `Bourbaki2002.tex` L1407–1829，并以 `src/p08.txt`–`p13.txt` 及 `pages/p011.png`、`pages/p012.png`、`pages/p013.png` 图版复核（公式/字形以图版为准）。
**结论**：**有 5 处问题（critical 2、major 1、minor 2）**。§3、§4 未发现实质错误；问题全部集中在 §5，其中 2 处 critical 都是"对象/上下标写错"（图注第四个投影、漏 overline）；§5 的 tikz-cd 基本图本身（对象、箭头方向、上下标、勾箭朝向、斜投影落点）与原文 `\diagram`（L1734–1759）逐项相符，无错。

## 基本图核验（p12 / L1734–1759）

- 上段：`\bar\cV^\circ_n \xleftarrow{\sim} \bar\cV^{\vee\circ}_{n-1} \xhookrightarrow{} \bar\cV^\vee_{n-1}`（c2–c4）、`\bar\cV_{n-1} \xhookleftarrow{} \bar\cV^\circ_{n-1} \xleftarrow{\sim} \bar\cV^{\vee\circ}_{n-2} \hookrightarrow \cdots`（c6–c9）——顺序、箭头指向、`\sim`（左向同构）与两个勾箭（`hook` 在右、`hook'` 在左）均与原文一致。
- 下段：c2 `\bar\cV^\vee_2` 孤立、c4–c7 `\bar\cV_2 \hookleftarrow \bar\cV^\circ_2 \xleftarrow{\sim} \bar\cV^{\vee\circ}_1 \hookrightarrow \bar\cV^\vee_1`、c9–c11 `\bar\cV_1 \hookleftarrow \bar\cV^\circ_1 \xleftarrow{\sim} \bar\cV^{\vee\circ}_0`，与原文一致。
- 八个斜投影落点全部正确：`\bar\cV^\circ_n\to\cC_n`、`\bar\cV^\vee_{n-1}\to\cC_{n-1}`、`\bar\cV_{n-1}\to\cC_{n-1}`、`\bar\cV^\vee_2\to\cC_2`、`\bar\cV_2\to\cC_2`、`\bar\cV^\vee_1\to\cC_1`、`\bar\cV_1\to\cC_1`、`\bar\cV^{\vee\circ}_0\to\cC_0`；`\cC_n,\cC_{n-1}` 在第 2 行第 1/5 列，`\cC_2,\cC_1,\cC_0` 在第 4 行第 3/8/12 列，与 p012.png 版面吻合。
- 图注四个斜投影的**前三个**（L92–94）与原文 L1761–1767 一致；第四个见下条 critical。
- 另用 `latex_look` 编译 `源码/main.tex`，取含图的第 10 页（印刷页 906–13）核对成品：4 个 `\sim` 标记都落在**向左**的同构箭头上方（未压线），两个勾箭分别渲染为 ↪（右向、钩在尾部）与 ↩（左向、钩在尾部），8 个斜箭头落点与 `\cC_n,\cC_{n-1},\cC_2,\cC_1,\cC_0` 的位置都与 p012.png 一致；编译 0 error（仅 hyperref 书签 Unicode 警告 1 条）。

---

### [critical] s06-fourier.tex:L95
- 原文：`et $\overline{\pi}_{0}^{\vee\circ}: \overline{{\cal V}}_{0}^{\vee\circ}= [{\cal V}_{0}^{\vee\circ}/{\Bbb G}_{{\rm m}}]\rightarrow {\cal C}_{0}$`（`Bourbaki2002.tex` L1767–1769；`src/p12.txt` 图注末项作图「π^{∨◦}_0 : V^{∨◦}_0 = [V^{∨◦}_0/G_m] → C_0」；p012.png 同处）
- 译文：`$\bar\pi{}^\circ_0\colon\bar\cV{}^\circ_0=[\cV^\circ_0/\Gm]\to\cC_0$。`
- 问题：类别 2（上下标/对象错）。图注第四个投影被写成 $\bar\pi^\circ_0:\bar{\cal V}^\circ_0=[{\cal V}^\circ_0/\Gm]\to{\cal C}_0$，但图中射向 $\cC_0$ 的斜箭头来自第 3 行第 11 列的 $\bar{\cal V}^{\vee\circ}_0$，$\bar{\cal V}^\circ_0$ 在整张图中并不存在；且与本文件 L108 的 $K_{E,1}=(\iota_0)_*(\bar\pi^{\vee\circ}_0)^*\cL_E$ 直接冲突（同一页自相矛盾）。
- 建议：`$\bar\pi{}^{{\vee}\circ}_0\colon\bar\cV{}^{{\vee}\circ}_0=[\cV^{{\vee}\circ}_0/\Gm]\to\cC_0$。`

### [critical] s06-fourier.tex:L119、L125、L132
- 原文：`Les champs $\overline{{\cal V}}_{i}^{\circ}$ et $\mathop{\rm Fib}\nolimits_{i}^{\prime}(X)$ sont des ouverts de $\mathop{\rm Coh}\nolimits_{i}^{\prime}(X)$ et on peut donc considérer leur intersection.`（L1805–1808）；`la restriction de $K_{E,i}$ à l'ouvert $\overline{{\cal V}}_{i}^{\circ}\cap \mathop{\rm Fib}\nolimits_{i}^{\prime\,i(i-1)(g-1)+d}(X)$ de $\mathop{\rm Coh}\nolimits_{i}^{\prime\,i(i-1)(g-1)+d}(X)$`（L1814–1816）；`à l'ouvert $\overline{{\cal V}}_{n}^{\circ}\cap\mathop{\rm Fib}\nolimits_{i}^{\prime\,n(n-1)(g-1)+d}(X)$ de $\mathop{\rm Coh}\nolimits_{i}^{\prime\,n(n-1)(g-1)+d}(X)$`（L1825–1827）
- 译文：L119「叠 $\cV{}^\circ_i$ 与 ${\Fib'}_i(X)$ 都是 ${\Coh'}_i(X)$ 的开集，因此可以考虑它们的交。」；L125「${\Coh'}^{i(i-1)(g-1)+d}_i(X)$ 的开集 $\cV{}^\circ_i\cap{\Fib'}^{i(i-1)(g-1)+d}_i(X)$」；L132「${\Coh'}^{n(n-1)(g-1)+d}_i(X)$ 的开集 $\cV{}^\circ_n\cap{\Fib'}^{n(n-1)(g-1)+d}_i(X)$」
- 问题：类别 2（对象错，漏 overline）。按本文件 L92–95、L106 自身的约定，$\bar{\cal V}^\circ_i=[{\cal V}^\circ_i/\Gm]$ 才是 $\Coh'_i(X)$ 的开子叠；$\cV^\circ_i$ 是取商之前、带 $\Gm$-作用的叠（$\Gm$-主丛的总空间），不是 $\Coh'_i$ 的子叠。漏掉 overline 后，"是开集"与"取交"两处断言都不成立，引理 5.2 的前提也不再良定义。
- 建议：三处统一改为 `\bar\cV{}^\circ_i` / `\bar\cV{}^\circ_n`，例如 L119「叠 $\bar\cV{}^\circ_i$ 与 ${\Fib'}_i(X)$ 都是 ${\Coh'}_i(X)$ 的开集」。

### [major] s06-fourier.tex:L113、L116
- 原文：`$$K_{E,i+1}=(\iota_{i})_{\ast}(j_{i}^{\vee})^{\ast}\mathop{\rm Four}\nolimits_{\overline{{\cal V}}_{i}/{\cal C}_{i}}((j_{i})_{!}K_{E,i}),\quad i=1,\ldots,n-1$$`（L1794–1796）；`où $\mathop{\rm Four}\nolimits_{\overline{{\cal V}}_{i}/{\cal C}_{i}}:\mathop{\rm D}_{{\rm c}}^{{\rm b}}(\overline{{\cal V}}_{i})\rightarrow \mathop{\rm D}_{{\rm c}}^{{\rm b}}(\overline{{\cal V}}_{i}^{\vee})$ est la transformation de Fourier homogène pour le fibré vectoriel ${\cal V}_{i}\rightarrow {\cal C}_{i}$ d\'efinie dans la section $0$.`（L1798–1803）
- 译文：L113「$K_{E,i+1}=(\iota_i)_*\,(j^\vee_i)^*\,\Four_{\cV_i/\cC_i}\big((j_i)_!K_{E,i}\big)$」；L116「其中 $\Four_{\cV_i/\cC_i}\colon\Dbc(\cV_i)\to\Dbc(\cV^\vee_i)$ 是向量丛 $\cV_i\to\cC_i$ 的齐次 Fourier 变换，其定义见第~0~节。」
- 问题：类别 2（函子下标及其定义域/值域的对象错）。原文 $\Four$ 的下标与两端范畴都带 overline（$\overline{{\cal V}}_i$、$\overline{{\cal V}}_i^\vee$），因为 $K_{E,i}$ 活在 $\bar\cV^\circ_i\subset\bar\cV_i$ 上、$(j_i)_!K_{E,i}$ 活在商叠 $\bar\cV_i$ 上；译文把它写在未取商的 $\cV_i$ 上，函子类型不成立。注意同句末尾"向量丛 ${\cal V}_i\to{\cal C}_i$"原文确实不带 overline（L1802–1803），此处保留是对的，只需改下标与两端范畴。
- 建议：`$K_{E,i+1}=(\iota_i)_*\,(j^\vee_i)^*\,\Four_{\bar\cV_i/\cC_i}\big((j_i)_!K_{E,i}\big)$`，且 L116 改为 `$\Four_{\bar\cV_i/\cC_i}\colon\Dbc(\bar\cV_i)\to\Dbc(\bar\cV{}^\vee_i)$`（"向量丛 $\cV_i\to\cC_i$"不动）。

### [minor] s06-fourier.tex:L127
- 原文：`$$M_{i,E}^{\prime d}(L_{i})$$`（L1819；p013.png 同处印作**斜体** $L_i$）
- 译文：`$M'^{d}_{i,E}(\cL_i)$`
- 问题：类别 5（字形错致记号冲突）。该对象即 §4 定义 4.1 的复形 $L_n$（`s05-autprime.tex` L63 `$L_n=(\overline f_n)_!(\overline g_n)^*\Psi[\dim\overline{\cU}_n]$`、L99 `$M'^d_{n,E}(L_n)$`，印刷体为斜体 $L$）；本译本 `\cL` 已固定给 §3 的反常层 $\cL^d_E$（s06 L110 的 $\cL_E$ 同此），写作 `\cL_i` 会让读者误认成反常层。
- 建议：`$M'^{d}_{i,E}(L_i)$`。

### [minor] s06-fourier.tex:L133
- 原文：`En particulier, pour chaque entier $d\geq 0$, les restrictions de $K_{E,n}$ et de $\mathop{\rm Aut}\nolimits_{E}^{\prime}$ à l'ouvert $\overline{{\cal V}}_{n}^{\circ}\cap\mathop{\rm Fib}\nolimits_{i}^{\prime\,n(n-1)(g-1)+d}(X)$ de $\mathop{\rm Coh}\nolimits_{i}^{\prime\,n(n-1)(g-1)+d}(X)$ co\"{\i}ncident.`（L1823–1827）
- 译文：「`\yizhu{末句两个上标写的都是 $i$，与句首的 $K_{E,n}$、$\Aut'{}_E$ 以及本引理首段不合，似应为 $n$；此处照原文翻译。}`」
- 问题：类别 4（译注内容与事实不符）。原文那两处的 $i$ 都是**下标**（$\mathop{\rm Fib}'_i$、$\mathop{\rm Coh}'_i$），不是上标；译注"应为 $n$"的判断正确（L1826–1827 处确为原文笔误），仅"上标"一词用错。
- 建议：「末句两处下标写的都是 $i$，……」。

## 无法判定

1. **`s06-fourier.tex:L110–111`**："它在 $\cC_0$ 的每个连通分支 $\cC^d_0$ 上的限制"——原文 L1790–1791 作 `à chaque composante connexe ${\cal C}_{0}^{d}$ de ${\cal C}^{0}$`，p013.png 印刷体也确作 ${\cal C}^0$（少了下标 0）。译文按 $\cC_0$ 顺译，我判为原文笔误、译文处理合理，未列为错误；若主控要求"照译 + 译注"的口径，此处需补一条注。
2. **`s06-fourier.tex:L113/L116` 的判级**：与 L119/125/132 同属"漏 overline"。此处给 major 的理由：$\Four$ 仍是同一个齐次 Fourier 变换，正确对象可由同页 L106 的 $\bar\cV^\circ_i$ 与 L1789 的 $\bar\cV_i$ 唯一复原，错误不改变引理 5.2 的结论；L119/125/132 给 critical 的理由："是开集/取交"的断言本身变假、引理 5.2 的前提不再良定义。若主控统一口径为"漏 bar 一概 major"，则 critical 1、major 2；反之若一概 critical，则 critical 3、major 0。报告中其余判级不受影响。
3. **`s06-fourier.tex:L47`「基本图」**（原文 `le diagramme fondamental`，L1732）：`glossary.tsv` 未收该词组（只有 `diagramme`→图表），译者为"基本图"并在交付报告 s06.md 第 10 条提请主控确认。按现表不算冲突，我不列为错误；是否补入 glossary 请主控裁决。
4. **`s05-autprime.tex:L85–86` 与 `L88`**：原文 L1629 的 `\mathop{\rm Fib}\nolimits_{i}^{\prime\,n(n-1)(g-1)+d}(X)` 下标 $i$ 与上下文不合，译文"照译 $i$ + 译注"（说法与 p11 版面相符，我已核对 p011.png）。这是原文笔误、译文处理正确，不列为错误，仅在此备案。
