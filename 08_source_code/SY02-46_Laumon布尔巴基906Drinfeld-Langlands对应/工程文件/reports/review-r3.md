# SY02-46 中译本独立审校 r3

**审校范围**：`源码/sections/s07-vanishing.tex`（§6，p13–15）、`s08-descente.tex`（§7，p15–17）、`s09-refs.tex`（参考文献，p18–19），合计 55 + 158 + 81 = **294 行**；逐句对读法文权威源 `texsrc/Bourbaki2002.tex` L1832–2374（§6、§7、BIBLIOGRAPHIE 及作者块），并以 `work/src/p13.txt`–`p19.txt`、`work/pages/p013.png`–`p019.png` 对页复核（上下标、花体/正体以图版为准），另以 `main.pdf`（14:34 编译版）核对成品。
**版本快照**：以 2026-11-27 14:47 的源码为准，sha1 前 8 位——s07 `2d933e66`、s08 `b8152ab5`、s09 `0e5fc01f`。注意 s08 在 14:32:57 被改过一次（只动了 L121 译注的第二参数），行号不受影响。
**结论**：**有 2 处问题（critical 1、major 0、minor 1）**。§6 与参考文献未发现实质错误（s09 的 21 条与原文逐字一致，含原文笔误照录）；唯一 critical 在 §7 的 $\widetilde{\mathcal Z}^d_n$ 显示式：原文显示式作 $\mathrm{Mod}^{\,d}_{n}(X)$，译文改成 $i$，改后纤维积两侧落在不同叠上、公式不成立——原文紧接着的正文确实印作 $i$，那是原文自己的笔误，**显示式的 $n$ 才是对的**。

---

### [critical] s08-descente.tex:L139
- 原文：`\widetilde{{\cal Z}}_{n}^{d}=\widetilde{{\cal Y}}_{n}^{0} \times_{\mathop{\rm Fib}\nolimits_{n}(X),p'}{\mathop{\rm Mod} \nolimits_{n}^{d}(X)}`（`Bourbaki2002.tex` L2148–2150；`work/src/p17.txt` L45 文本层作 `e0 ×Fib (X),p′ Modd (X)`；`work/pages/p017.png` 印刷页同处放大（2×）可见下标确为 $n$）
- 译文：L138–140 `\widetilde{\cZ}^d_n = \widetilde{\cY}^0_n \times_{\Fib_n(X),p'} \Mod^d_i(X)`
- 问题：类别 2（公式·下标错，数学内容错）。此处纤维积取在 $\Fib_n(X)$ 上：$\widetilde{\cY}^0_n$ 经遗忘截面打到 $\Fib_n(X)$，另一侧 $p'\colon\Mod^{\,d}_{n}(X)\to\Fib_n(X)$ 把 $(\cL'\subset\cL)$ 送到 $\cL'$（秩 $n$）。改成 $\Mod^{\,d}_{i}$ 后 $p'$ 落到 $\Fib_i(X)$，两侧不在同一叠上，公式不成立；紧随其后的三元组描述（$(\cL',s'^\bullet)\in\cY^0_n$ 而 $(\cL'\subset\cL)\in\Mod^{\,d}_{i}$）也随之自相矛盾（$\cL'$ 不可能同时秩 $n$ 与秩 $i$）。原文正文 L2155 确实印作 `\mathop{\rm Mod}\nolimits_{i}^{d}(X)`，属原文自身笔误（秩必须为 $n$）；原稿显示式与正文不一致，译文把**本来正确的显示式**改成了**错的 $i$**，且交付报告 `工程文件/reports/s08.md`「疑点」未记录此改动。14:34 编译的 `main.pdf` 第 14 页已按 $i$ 排出，缺陷已进入成品。
- 建议：L139 恢复 `\Mod^d_n(X)`（即 `\times_{\Fib_n(X),p'} \Mod^d_n(X)`）。L143 正文的 `\Mod^d_i(X)` 系照原文笔误，保留即可；如愿彻底消歧，可在 L143 加一条「原文笔误」译注（说明 p17 显示式作 $n$、正文作 $i$，按纤维积应取 $n$），本节现仅 1 条译注，未超每节 6 条上限。

### [minor] s08-descente.tex:L120、L121
- 原文：`\widetilde{f}:\widetilde{{\cal Y}}_{n}^{d}:=[{\cal Y}_{n}^{d}/{\Bbb G}_{{\rm m}}^{n}]\rightarrow \mathop{\rm Fib}\nolimits_{n}^{\prime\,n(n-1)(g-1)+d}(X)`（`Bourbaki2002.tex` L2106–2108，即命题 7.3，印刷页 p17）
- 译文：译注内「按上式末端的等号，$[\cY^0_n/\GG_m^n]$ 应等于 $\widetilde{\cY}^0_n$（见 p15 处的定义）」；第二参数 `{原文笔误，I（原文 p15 定义互证）}`
- 问题：类别 4（指代/编号错；译注内容与事实不符）。$\widetilde{\cY}^{\,d}_{n}:=[\cY^{d}_{n}/\GG_m^{n}]$ 的定义在**命题 7.3**（p17，L2106–2108）；p15 只到「considérons le champ ${\cal Y}_{n}^{d}$ introduit par Drinfeld」（L2021，p15 正文末句止于 `qui classifie les couples (L, s•)`），连 $\cY^{d}_{n}$ 的完整定义都在 p16。译注正文与第二参数两处的「p15」都指错了页。译注的其余内容（原文此处印 $d$、按等号应为 $0$、$\Phi\in\Dbc(\widetilde{\cY}^0_n)$）核对无误。
- 建议：正文改「（见 p17 命题 7.3）」，第二参数改为 `{原文笔误，I（原文 p17 命题 7.3 定义互证）}`。

---

## 已核项（逐句对读通过，未列问题）

- **s07（§6）**：p13 图表（$\Mod^d_i$ 在上中、$q$ 向右到 $\Coh^d_0(X)$、$p'$/$p$ 斜向下到两个 $\Fib_i(X)$）与原文 `\diagram`（L1837–1848）逐项相符；$M^d_{i,E}(K)=p_*p'^*(K\otimes q^*\cL^d_E)[id]$ 的 `[id]` 平移原文如此（非笔误）；定理 6.1 的 $d>in(2g-2)$、注 6.2 的 $d>n(2g-2)$ 均照录；命题 6.3 方向 $(j_i)_!K_{E,i}\to(j_i)_*K_{E,i}$ 正确；证明思路中 $(\overline{\pi}^\circ_i)_!K_{E,i}=(0)$、$\overline{\pi}^\circ_i\colon\overline{\cV}^\circ_i\to\cC_i$、引理 (0.3)、引理 5.2、$M^d_{i,E}(\pi'_*L_i)$、$\pi'\colon\Fib'_i(X)\to\Fib_i(X)$「遗忘截面 $s\colon(\Omega^1_X)^{\otimes n-1}\to\cL$」均与原文一致；推论 6.4 的 $\overline{\cV}^\circ_n$ 经原文 L1948 确认确有上横线。**L22 译注内容核对准确**：原文作 $in(2g-2)$（$i$ 与 $n$ 之积）、注 6.2 中 $i=1$ 写作 $n(2g-2)$，三处事实无误（类别归属见「无法判定」1）。
- **s08（§7）**：$\chi_K$ 定义、引理 7.1（Deligne，`[Il] Corollaire 2.10`，propre→紧合 ✓）、引理 7.2 及其证明（$K\cong i_*j_{!*}E[\dim Q]$、$\pi^*(L)[r-1]$、当且仅当 ✓）、$\cY^d_n$ 定义（次数 $n(n-1)(g-1)+d$、$s^\bullet$ 各次张量与 $\bigwedge^i\cL$、Plücker 关系与一般点处完全旗）、三元组叠与 $\cY^{d\circ}_n$ 等同（$s^i=s_n\otimes\cdots\otimes s_{n-i+1}$、$\cong\bigwedge^i\cL_i$、$i=1,\dots,n-1$ 余核无挠）、$\GG_m^n$ 作用及三元组上的 $(t_nt_{n-1}^{-1}s_1,\dots,t_2t_1^{-1}s_{n-1},t_1s_n)$、$\cU_n$ 与 $\overline{\cU}_n=[\cU_n/\GG_m]$（上划线，与 s05 一致）、两个嵌入 $t\mapsto(t,t^2,\dots,t^n)$ 与 $(t,t')\mapsto(t,t^2t',t^3t'^3,\dots,t^nt'^{\frac{n(n-1)}{2}})$、命题 7.3（$\tilde f$ 可表且紧合）、$\Phi$ 的两步复合态射（商映射 + 包含，未合并）、$N^d_{n,E}$ 与 $[nd]$、图表 $p'$/$p$/$q$、引理 7.4 的 $\Aut'_E\,|\,\Fib'^{\,n(n-1)(g-1)+d}_n=\tilde f_*N^d_{n,E}(\Phi)$、末段 7.4→7.3→7.1 与 7.2 的使用链，均逐句对上，无漏译/增译。
- **s09（参考文献）**：21 条（B-B-D、B-D、B-L、Br、B-G、Dr 1–3、F-G-K-V、F-G-V 1–2、Ga、Il、La、Lau 1–3、L-M、Ly 1–2、Se）按 `\auteur`/`\titre`/`\reste`/`\revue`/`\tome`/`\annee`/`\pages` 归一化后与原文**逐条字符串相等**（作者、题名、期刊、卷、年、页），顺序一致；[B-L] 的 `Springer-verlag (1974)`（LNM 1578 实为 1994）照录原文，[Ly 2] 的小写 `arxiv.org` 照录，作者块 6 行（Gérard Laumon / Université Paris-Sud / et CNRS, UMR 8628 / Mathématique, Bât. 425 / F-91405 Orsay Cedex (France) / Gerard.Laumon@math.u-psud.fr）与原文一致；`\srcpage{18}` 在篇首、`\srcpage{19}` 在 `[La]` 之前，与 p18/p19 换页吻合。

## 无法判定

1. **s07-vanishing.tex:L22 译注的类别**：内容已核准确（见上），但第二参数写「术语背景，A（原文注 6.2 互证）」。该条解释的是记号 $in=i\cdot n$ 的读法并与注 6.2 互证，既可以算「术语背景」（记号说明），也符合「原文笔误」类的「给页码 + 判断依据」要求（原文 p13/p14 与此互证）。按 `s07.md` 疑点 5，这条注是按主控要求加的、等级与出处也由主控定；工程正在统一译注体例（14:32 后 s05/s06/s08 的第二参数已改为「类别，依据等级（出处）」式），故不列为错误，请主控定夺是否把「术语背景」改为「原文笔误」。
2. **s07-vanishing.tex:L52 与 s08-descente.tex:L1 的 `\srcpage{15}` 重复**：两处各写一次，编译后同一页（`main.pdf` 第 12 页）出现两个「906--15」边缘注——紧接「推论 6.4」之前一个、§7 标题之右一个。属排版/呈现（契约第 20 行不计错），是否删 s08 L1 的页锚（或改到「7 下降」标题所在位置）请主控按体例定；删前请注意 `check_sections.py` 是否要求每节首行带页锚。
3. **s09-refs.tex 的 `http ://`（L9、L19、L36、L44、L69）**：译文冒号前有空格，系照录印刷页 p18/p19（印刷页本身表现为 `http ://`，见 `p18.txt` L10、`p19.txt` L16），而 TeX 源 `Bourbaki2002.tex` L2216 等处写的是 `http://`、无空格。这是 PDF 排版层的断行/字距现象，照录不算错；若主控要求以 TeX 源为准，可统一去掉空格（属排版层，非内容）。
4. **s08-descente.tex:L121 与 s07-vanishing.tex:L22 的译注第二参数体例**：14:32:57 的改动把 s08 的 `{原文笔误（A）}` 改成 `{原文笔误，I（原文 p15 定义互证）}`，但仍未给「判断依据」（STYLE_GUIDE §6 要求原文笔误类给页码 + 判断依据；此处页码也有误，见 minor 条）。内容本身（原文印 $d$、应为 $0$）已核无误，体例问题不计为内容错误。
