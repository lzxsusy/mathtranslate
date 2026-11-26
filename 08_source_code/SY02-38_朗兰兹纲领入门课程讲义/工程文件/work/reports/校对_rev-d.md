# 校对报告 rev-d：译者说明、第 1 讲、第 11–12 讲

校对对象：`源码/chapters/preface.tex`、`lecture01.tex`、`lecture11.tex`、`lecture12.tex`（行号均指当前文件）。
底本：`工程文件/work/pages/p002.txt`、`p088–p101.txt`；另参 `glossary.tsv`（冻结）、`STYLE_GUIDE.md`、`疑点清单.tsv`。
共 25 条：严重 1、中等 10、轻微 14。标「须核 PDF」者指提取文本与上下文冲突，需回原页确认。

## 译者说明（preface.tex）

[中等] preface.tex:16 | 「【译注】均有可追溯来源」与正文不符：lecture11.tex:19、lecture12.tex:261、322 的 `\znote` 只有底本校勘、无 `[来源：…]`；且 `\znoteplain` 实际还用于转述原文脚注（lecture01.tex:4、lecture12.tex:317），与「本译本的补充说明」的定义不合 | 「标有「【译注】」者均有可追溯来源（见脚注内的\emph{来源}），标有「【译者按】」者为本译本的补充说明、无外部依据」 | 改为三分说明：【译注】=带 `[来源：…]` 的解释；【译者按】=本译本的补充说明，含原文脚注的转述与底本笔误的校勘
[轻微] preface.tex:17 | 节号顺序倒置（§5 在 §4 前），且 $\Gamma_0(m)$ 的条件在 §4（p.32）与 §5（p.43）各出现一次 | 「\S 5 中 $\Gamma_0(m)$ 的 $\Gamma_0$ 条件、\S 4 中 $Y$ 的矩阵分解、\S 11 中 Casimir 元」 | 「\S 4 中 $Y$ 的矩阵分解、\S 5 中 $\Gamma_0(m)$ 的 $\Gamma_0$ 条件、\S 11 中 Casimir 元」

## 第 1 讲（lecture01.tex）

[中等] lecture01.tex:6 | 同一句里「陈述…陈述」重复，且「不给出任何证明的迹象」是硬译 | 「陈述（大多不给出任何证明的迹象）朗兰兹纲领中出现的各种陈述、对象、猜想……」 | 「（大多不提示证明）介绍朗兰兹纲领中出现的各种陈述、对象、猜想……」
[轻微] lecture01.tex:12 | 「远不是…有严肃知识或理解的人」语序照搬英文 | 「我远不是对朗兰兹纲领有严肃知识或理解的人」 | 「我对朗兰兹纲领远谈不上有严肃的知识或理解」

## 第 11 讲（lecture11.tex）

[中等] lecture11.tex:162 | p.091 页标记晚约 10 行：底本 p090 止于 "namely: isomorphism"，p091 自 "classes of irreducible unitary representations…" 起；故 152–161 行（容许性、Schur 引理变体、Harish-Chandra 同构、$X^*(T_\C)$、无穷小特征的典范 $W$-轨道）本属 p.091，却记在 p.090 名下 | 第 162 行 `% ===== PDF p.091 =====` 置于第 161 行之后 | 移到第 151 行 `\item` 之前（或在「即：$G(\R)$ 的不可约酉表示的等类」处断句，标记插在该句中间）
[中等] lecture11.tex:151、183 | 底本 isomorphism classes 译作「等类」，非标准，且与同文件 17、143 行的「同构类」不一致（lecture02.tex:68/86/311 同病） | 「不可约酉表示的\textbf{等类}单射到不可约 $(\g_\C,K_\infty)$-模的\textbf{等类}中」「…等类之集 $\mathrm{Irr}$」 | 一律作「同构类」，全书统一
[中等] lecture11.tex:245–246 | adèlic 绝对值：术语与记号都与 glossary/前文不一致（作「阿代尔范数」`\text{adèlic}`，且 è/é 混用）；lecture03.tex:541 已用 `|\cdot|_{\mathrm{ad\acute{e}lique}}`、lecture09.tex:107 用 `|\cdot|_{\mathrm{ad\acute{e}lic}}`，术语均作「adélic 绝对值」 | 「$|\cdot|^k_{\text{adèlic}}$，其中 $|\cdot|_{\text{adèlic}}$ 是阿代尔范数」 | 「$|\cdot|^k_{\mathrm{ad\acute{e}lique}}$，其中 $|\cdot|_{\mathrm{ad\acute{e}lique}}$ 是 adélic 绝对值」（三处同步改）
[轻微] lecture11.tex:19 | `\znote` 只校勘原文、无 `[来源：…]`，与 §5 及 preface.tex:16 的承诺不合 | `\znote{原文此处作 “Langland(…)”…}` | 改 `\znoteplain{…}`，或补「[来源：底本 p.~88]」
[轻微] lecture11.tex:116 | 定语 containing 被译成条件「只要它包含」 | 「并取 $V$ 为 $G$ 上函数空间中的任一表示，只要它包含 $C_c^\infty(G)$」 | 「并取 $V$ 为 $G$ 上函数空间上的一个表示，其空间包含 $C_c^\infty(G)$」
[轻微] lecture11.tex:171 | 「唯一的（在同构意义下）由…生成」插入语位置使限定悬空 | 「存在唯一的（在同构意义下）由这样的元素 $\phi$ 生成的…模」 | 「存在一个在同构意义下唯一的、由这样的元素 $\phi$ 生成的…模」
[轻微] lecture11.tex:177 | 「只在…取逆的意义下一致」硬译，读不出口语感 | 「与我们的 $\cA(\GL_2)$ 只在 $\GL_2(\A)$ 上取逆的意义下一致」 | 「仅在把 $\GL_2(\A)$ 中的元素取逆之后才与我们的 $\cA(\GL_2)$ 一致」
[轻微] lecture11.tex:187 | 括号切断「模—无穷小特征」的所属关系，成病句 | 「因为（与 $|\det|^{1/2}$ 相伴的 $(\mathfrak{gl}_{2,\C},\mathrm{O}_2(\R))$-模）的无穷小特征对应于 $Z\mapsto1$、$H\mapsto0$」 | 「因为与 $|\det|^{1/2}$ 相伴的 $(\mathfrak{gl}_{2,\C},\mathrm{O}_2(\R))$-模，其无穷小特征对应 $Z\mapsto1$、$H\mapsto0$」
[轻微] lecture11.tex:210 | 底本 "quasi-split and split over an unramified extension"，状语应同管两个形容词，译文只挂在第一项上 | 「在一个非分歧扩张上是准分裂的（…）并且是分裂的（…）」 | 「在一个非分歧扩张上既准分裂（即含定义在 $\Q_p$ 上的 Borel 子群）又分裂（即含极大分裂环面）」

## 第 12 讲（lecture12.tex）

[严重] lecture12.tex:112 | (5) 式通项作 $X^i$：与首项 $X^{n-1}$ 矛盾，$i=n$ 时还给 $X^n$ 与首项重复、全式无常数项；按 $\prod_i(X-\alpha_i)=\sum_i(-1)^ie_i(\alpha)X^{n-i}$ 应为 $X^{n-i}$。p096 提取在别处保留了上标（$X^{n-1}$、$p^{\frac{1-n}{2}}$ 均未丢），故此式原文很可能即误作 $X^i$ | `+\cdots+(-1)^ip^{\frac{i(i-n)}{2}}e_{a_{p,i}}X^i+\cdots+(-1)^ne_{a_{p,n}}` | 改 $X^{n-i}$，并加【译者按】：「原文此处作 $X^i$，按特征多项式应为 $X^{n-i}$」；仍请对 p.096 原页一眼确认
[中等] lecture12.tex:125 | 译注为 (6) 辩护，却未与 (5) 衔接：(5) 取 $n=2$ 给一次项系数 $p^{(1-2)/2}a_{p,1}=p^{-1/2}a_{p,1}$，(6) 印的是 $p^{1/2}a_p$，二者只在 $a_{p,1}=p\,a_p$ 时一致，而译文未交代这个归一化差别，读者会以为 (6) 多乘了一个 $p$ | 「两式自洽，故此处并非笔误」 | 补一句：(5) 的 $e_{a_{p,1}}$ 与经典 $a_p$ 相差一个 $p$（即 $a_{p,1}=p\,a_p$，故 $p^{-1/2}a_{p,1}=p^{1/2}a_p$，两式确实相合）；若不愿断此关系，则须明言 (5)(6) 归一化不同、此处以 (6) 为准，否则按 $a_{p,1}=a_p$ 直读 (5) 会得到 $p^{-1/2}a_p$
[中等] lecture12.tex:48 | p.095 页标记过早：底本 p094 含 Gelfand–Piatetski-Shapiro 整条（含 (2) 式 $L^2_{\mathrm{cusp}}\cong\bigoplus m_\pi\pi$ 与「其中每个 $m_\pi$ 有限…」，cf. [GH19, Corollary 9.1.2]），p095 自「• In particular, $L^2_{\mathrm{cusp}}\subset L^2_{\mathrm{disc}}$」起 | 第 48 行标记位于 (2) 式之前 | 移到第 52 行后、第 53 行「特别地」前
[中等] lecture12.tex:70 | 漏译数量限定：原文 "we can give (at least two) formal definition"，译文把「至少」挪去修饰「可以给出」，变成「至少可以给出（两种）」 | 「但用现在陈述的材料，我们至少可以给出（两种）形式定义」 | 「但用现在陈述的材料，我们可以给出（至少两种）形式定义」
[中等] lecture12.tex:320 | 紧化缺星号：本条 (4)(5) 小条与 p.099 均作 $X_K^*$，而 p101 底本此处作 $X_K$（提取在 p099 保留了 $X^*_K$，故这里大概率是底本笔误，而非漏字）；按 §2.5，底本笔误须加译注 | 「则确实存在紧化 $X_K$，但它们不再是典范的」 | 改「则确实存在紧化 $X_K^*$」，并加【译者按】：「原文此处作 $X_K$，按第 (5) 条应为 $X_K^*$」
[中等] lecture12.tex:121 | 同 lecture11.tex:245–246：`\text{adèlic}`＋「阿代尔范数」，与 glossary「adélic 绝对值」`|\cdot|_{\mathrm{ad\acute{e}lique}}` 不合（本行两处） | 「$\pi\otimes_\C|\det|^{1/2}_{\text{adèlic}}$」 | 「$\pi\otimes_\C|\det|^{1/2}_{\mathrm{ad\acute{e}lique}}$」，术语作「adélic 绝对值」
[轻微] lecture12.tex:115 | 底本 p096 作 $f=\sum_{i=1}^{\infty}a_nq^n$（下标不一致），译文径改为 $\sum_{n\ge1}a_nq^n$ 而未加注，属未说明的静默校正（§2.5） | 「$f=\sum_{n\ge1}a_nq^n\in S_k(\Gamma_0(N),\chi)$」 | 正文保留，另加【译者按】：原文下标作 $\sum_{i=1}^{\infty}a_nq^n$，按含义应为 $\sum_{n\ge1}$
[轻微] lecture12.tex:183 | 「存在单射，从…之集，映入…」结构断裂，读不成句 | 「则存在单射，从…的同构类之集 $\mathcal{G}_{\mathrm{geom}}$，映入 $\cL$ 的不可约表示的等类之集 $\mathrm{Irr}$」 | 「则存在从…的同构类之集 $\mathcal{G}_{\mathrm{geom}}$ 到 $\cL$ 的不可约表示的同构类之集 $\mathrm{Irr}$ 的单射」
[轻微] lecture12.tex:271 | 夹注「（猜想）」生硬，且缺被动 | 「其像（猜想）可以描述」 | 「其像（猜想上）可被描述」
[轻微] lecture12.tex:151–152 | 「$L$-代数」用数学模式，紧邻的「L-参数」用正体；glossary 为「L-代数的」（正体），lecture11.tex:16 等亦作 `$L$-` | 「…$L$-代数自守表示…」＋「…L-参数…」 | 统一正体：L-代数、L-参数、L-群、L-包（lecture11 同改）
[轻微] lecture12.tex:261、322 | `\znote` 无 `[来源：…]`（同 lecture11.tex:19），且 322 行一条注里混了两件事（编号笔误与衍字） | `\znote{原文在第 (4)、(6) 条用 $\widehat X$…}`；`\znote{原文此处作 “obtain analogs of points (18),(19),(20)”…}` | 均改 `\znoteplain`（或补「[来源：底本 p.~100/101]」）；322 行可拆成两条
[轻微] lecture12.tex:301/304 | 底本 p100→p101 是同一 itemize 的延续（"• For $K\subseteq G(\Af)$ recall…"），译文在页标记处收、重开环境，多出段距 | 301 `\end{itemize}`、304 `\begin{itemize}` | 合并为一个 itemize（页标记仍留在 p.101 处）

## 已核对无误（不报为错）

- 数学：定义 11.1 四条件（适度增长／右 $K_\infty$-有限／被 $\cZ(\g_\C)$ 的有限余维理想杀死／左 $G(\Q)$-不变）；定义 11.2 三公理（译文静默补了底本缺的右括号）；lecture11.tex:101 Casimir 译注（$[X,Y]=H$、$2XY+2YX=4YX+2H$、$Y*\phi_f=0\Rightarrow\Delta*\phi_f=\frac14(k^2-2k)\phi_f$）与 lecture11.tex:186 奇偶性译注均验算正确；$X^*(T)$ 的 $a\equiv b\pmod2$ 正确；Harish-Chandra 同构、Schur 变体、Flath、$^LG=\widehat G(\Ql)\rtimes\Gal(\overline\Q/\Q)$、Buzzard–Gee 两条、Langlands 群五性质、Shimura 三条件（$z/\bar z,1,\bar z/z$）、反射域与典范模型、重数一/强重数一，均与 p088–p101 逐句相符。
- 待核：提取文本未保留公式的右缘编号，故 lecture11 的 (1)–(4)、lecture12 的 (1)–(7) 与底本编号是否一致无法逐条核实（preface 承诺「不重编」）；建议对照原 PDF 抽查一遍。
- 结构：环境配对 lecture11 30/30、lecture12 31/31；页标记 6/8/1 条与底本页数相符（仅位置问题见上两条）；Heuer 三讲标题已标（lecture07.tex:5、lecture08.tex:5、lecture10.tex:3），preface 的「103 页」「12 讲」属实。

## 总体评价

1. 两讲的数学骨架扎实：四个条件、三条公理、Casimir 计算、$L$-代数奇偶判据、Buzzard–Gee 两条与 Shimura 数据三条件都与底本逐句对得上，底本自身出错处（p.89 的 Casimir 中间式、p.100 的特征渲染、p.101 的编号与衍字）处理正确且克制。
2. 真正的数学风险只有一处——(5) 式通项 $X^i$ 应为 $X^{n-i}$（严重）；其次是 (6) 与 (5) 相差一个 $p$ 的归一化没有交代，以及「至少两种」被挪位、$X_K^*$ 漏星号这两处小范围曲译。
3. 其余为术语与体例：等类/同构类、adélic 绝对值、$L$-系列正体、两条 \znote 的来源、两处页标记位置；均可在不动数学内容的前提下一次性修好。

**是否建议定稿**：不建议按现状定稿；改完上列 1 条严重与涉及 (6) 译注、两处页标记、术语三项（adélic、同构类、$L$-正体）即可定稿，其余轻微项可在统稿时一并处理。
