# ch09a 施工报告

- 负责页段：PDF 128–149（原书 p.119–140）
- 文件：src\chunks\ch09a.tex（48.2 KB，1090 行）
- 节：第9章 二维规范理论（含本章引言）/ 9.1 二维的乐园 / 9.2 向量丛的联络 / 9.3 Yang–Mills 联络 / 9.4 二维流形上的拓扑向量丛 / 9.5 作为动量映射的曲率 / 9.6 全纯向量丛 / 9.7 标准联络 / 9.8 复规范变换群 / 9.9 梯度与稳定性 / 9.10 Narasimhan–Seshadri 定理 / 9.11 Sobolev 空间。按分工**本 chunk 只写 `\chapter`，不写 `\chapterreview`**（章末回顾归 ch09b）。
- 编译：file:line=0 fatal=0 undefined=0 missingchar=0 overfull=0 undefref=0（`build.ps1 -Chunk ch09a`，草稿 tmp_ch09a.pdf 共 22 页，与原书页数恰好一致）
- 环境与编号：定理* 9.3.1、9.6.1、9.10.1、9.11.1、9.11.2、9.11.3、9.11.4、9.11.5；命题* 9.4.1、9.7.1（9.7.1 原书给两个证明，分别用 `\begin{proof}[命题 9.7.1 的用局部酉标架的证明]` 与 `[…用局部全纯标架的证明]`）。陈述一律用**带 `*`** 的环境：原书这些陈述后紧接「証明」且陈述末尾无 □（已逐页看图确认，如 p.124 定理 9.3.1、p.125 命题 9.4.1 均如此），故用不带 □ 的版本。公式共 176 个 `\tag`，全部照抄原书号：9.1 节 5 式、9.2 节 21 式、9.3 节 7 式、9.4 节 1 式、9.5 节 35 式、9.6 节 21 式、9.7 节 19 式、9.8 节 14 式、9.9 节 3 式、9.10 节 2 式、9.11 节 48 式。11 个 `\takeaway`（每节一次，均 ≤40 字）。
- 批注：共 19 条（背景 8 / 难点 5 / 校勘 6），平均 0.86 条/页，最长一条 118 字。批注将被 `work\gen_appendix_notes.py` 转排进附录 A，故批注内**一律不写裸 Unicode 数学符号**：p.120 那条的「⟺」已改为 `$\Longleftrightarrow$`（Lead 提示后全文复查：`⟺ ⟹ ↔ ⇔ ・ π δ` 及 U+2190–U+2BFF、希腊字母区间均无残留；`–`（U+2013）仅出现在 Narasimhan–Seshadri 等人名中，属正文字符且主文档编译无 missingchar）。
- 插图：本页段原书无插图（図9.1 在本页段之外），故未使用 `\includegraphics`。
- 新增术语（原书→中译，首现括注西文或加批注）：
  - 位相的ベクトル束＝拓扑向量丛（topological vector bundle）/ 分類空間＝分类空间（classifying space）/ 胞体近似定理＝胞体近似定理（cellular approximation theorem）/ 骨格＝骨架（skeleton）
  - 位相同型類＝同型类（up to homeomorphism）/ 障害＝障碍（obstruction）
  - 勾配＝梯度（slope）/ 半安定・安定＝半稳定・稳定（semistable / stable）/ 可約・直既約（ベクトル束）＝可分解（decomposable）/ 直和不可分解（indecomposable）
  - フィルトレーション＝滤过（filtration）/ 部分束＝子丛（subbundle）/ 中間次数＝中间次数 / Harder–Narasimhan 滤过
  - 常中心曲率接続＝常中心曲率联络（constant central curvature connection）/ 標準接続＝标准联络（canonical connection）/ 複素ゲージ変換群＝复规范变换群（complexified gauge transformation group）
  - 全純ベクトル束＝全纯向量丛（holomorphic vector bundle）/ 両立する＝相容（compatible）/ 自己同型群＝自同构群
  - 弱微分可能＝弱可微（weakly differentiable）/ 弱導関数＝弱导数（weak derivative）/ ソボレフ空間＝Sobolev 空间 / ソボレフノルム＝Sobolev 范数
  - コンパクト埋め込み＝紧嵌入（compact embedding）/ 相対コンパクト＝相对紧 / 一様有界＝一致有界 / 同程度連続＝等度连续（equicontinuous）
  - 先験的評価＝先验估计（a priori estimate）/ 二乗平均＝均方 / 本質的上限＝本质上确界（essential supremum）/ 楕円型作用素＝椭圆型算子
  - 直既約（接続）＝不可约（irreducible）；同一词形在原书中有两义，见批注与「疑似笔误」第 4 条
- 疑似原书笔误/排版问题（均**照录**并加校勘批注或在此登记）：
  1. p.127 引出 (9.5.21)–(9.5.23) 的句子同时引入 $\eta\in\Omega^1(P\times_G\mathfrak g)$ 与 $\alpha$，但三式中只出现 $\alpha$；$\eta$ 疑为笔误。
  2. p.133 (9.8.4) 右端两个曲率分量印作 $-F^{0,2},-F^{1,1}$，未写下标 $A$（实即 $F_A^{0,2},F_A^{1,1}$）。
  3. p.136 「$v\in B$」按上下文应为 $v\in V$（$B$ 疑为 $V$ 之误）。
  4. p.135 同一个「直既約」在原书被 gloss 成两种意思：向量丛处作 indecomposable（译「直和不可分解」），联络处作 irreducible（译「不可约」）。
  5. p.137 原书叙述 Sobolev 不等式时称「$f$ 的 $L^p_k$ 范数被 $L^q_l$ 范数从上控制」，方向与嵌入 $L^p_k\subset L^q_l$ 相反（通常为 $\|f\|_{L^q_l}\le C\|f\|_{L^p_k}$）。
  6. p.140 (9.11.33) 右端印作 $C^0(C)$，按上下文应为 $C^0(X)$；另 (9.11.18) 第三行只写 $L^{q'}$ 而漏 $(X)$，均照录。
- 记号统一决定（供合并/交叉校对）：
  - 原书 script 体 $\mathscr E$ 与普通 $E$ 混用（如 $\bar\partial_{\mathscr E}$），译文统一作 $E$、$\bar\partial_E$。
  - 9.5 节辛商的模空间记号原作 $\mathcal M$（$\cM$），稳定丛模空间 $\cM(r,d)$ 亦用 `\cM`；规范群 $\cG$、联络空间 $\cA$、$\cA^{1,1}$、复化 $\cG_\C$ 分别用 `\cG`、`\cA`、`\cA^{1,1}`、`\cG_\C`；李代数 $\mathfrak g$ 用 `\mathfrak{g}`。
  - 紧嵌入符号本译本统一用 `\Subset`（原书 p.147 处为 ⋐，即 `\Subset` 的直立写法）。
  - 文献引用照 Lead 指示保留纯文本方括号数字（如 [122]、[108]、[37, Theorem 2.1.53]），未用 `\cite`。
- 待核/未解：无卡住的项；下列两点留待合并时统一（不影响本 chunk 编译）：(a) 上述第 5 条 Sobolev 不等式方向是否确为原书笔误，需与 ch09b 同一节后续（p.141 起）对照；(b) `\takeaway` 措辞待全章统稿时与 ch09b 的风格对齐。
- 需要的宏：无新增。用到的 `\Subset`、`\hookrightarrow`、`\operatorname*{ess\,sup}`、`\begin{cases}`、`enumerate[label=…]`、`\xrightarrow{\sim}`、`\varinjlim`、`\mathrm{Gr}` 均在既有 preamble（amsmath/amssymb/enumitem）内可用，未改 preamble。
- 边界说明：起始页 p.119 即章首，故写 `\chapter{二维规范理论}` 与本章引言；截止 p.140 末行为定理 9.11.5 证明的结尾（以 □ 收束），9.11 节在 p.141 尚有后续，故本 chunk 不写 `\chapterreview`，把该节余下部分留给 ch09b。

## 批注清单

| 原书页 | 类型 | 内容 |
|---|---|---|
| p.119 | 背景 | Narasimhan–Seshadri 定理（1965）断言紧 Riemann 面上次数与秩互素的稳定全纯向量丛与基本群的中心扩张的不可约酉表示一一对应；Atiyah–Bott 将其重述为无限维辛商，见本章 9.5 节。 |
| p.119 | 背景 | KdV 方程（Korteweg–de Vries）与 KP 方程（Kadomtsev–Petviashvili）都是可积的孤子方程；「可积层级」指由无穷多个彼此相容的方程构成的族。 |
| p.120 | 难点 | 2 维时曲率张量只剩一个独立分量，故 (9.1.4) 右端只有单一项 $R$；这是「Einstein ⟺ 常曲率」在 2 维成立的原因。 |
| p.120 | 背景 | Killing–Hopf 定理（1898）分类单连通完备常曲率空间：$S^n$、$\R^n$、$\HH^n$ 三种模型空间。 |
| p.120 | 难点 | 「近复结构可积」指存在相容的复坐标图册，即 Newlander–Nirenberg 条件 $\bar\partial^2=0$ 成立；2 维时该条件自动满足。 |
| p.121 | 背景 | 常中心曲率联络在文献中多称 Hermite–Einstein 联络；「中心」指曲率取值为李代数中心里的标量矩阵。 |
| p.121 | 背景 | GAGA 是 Serre 论文标题「Géométrie Algébrique et Géométrie Analytique」的缩写，1956 年发表于 Ann. Inst. Fourier。 |
| p.122 | 背景 | Atiyah–Bott（1982, Phil. Trans. Roy. Soc. A 308, 523–615）给出 9.5 节无限维辛商观点，是本章的理论源头。 |
| p.123 | 难点 | (9.2.14) 的减号来自分次 Leibniz 律 $d(A\wedge s)=dA\wedge s+(-1)^{|A|}A\wedge \rd s$，此处 $|A|=1$。 |
| p.124 | 难点 | (9.3.6) 用了 $X$ 上的内积 $\langle\alpha,\beta\rangle=\int\tr(\alpha\wedge*\beta)$ 的对称性与 $\tr$ 的循环性；(9.3.7) 用了一次分部积分并丢弃边界项。 |
| p.125 | 背景 | $\mathrm{Gr}(r,N)$ 为 $\C^N$ 的 $r$ 维复子空间构成的 Grassmann 流形；$\PP^1=\mathrm{Gr}(1,2)$ 给出 $BU(r)$ 的 2 骨架，故 2 维底流形上只需一个整值不变量。 |
| p.127 | 校勘 | 原书此句引入 $\eta\in\Omega^1(P\times_G\mathfrak g)$，但下面 (9.5.21)–(9.5.23) 中只出现 $\alpha$；疑为笔误，照录。 |
| p.130 | 难点 | 「与全纯结构相容」按定义即 $(0,1)$ 分量等于该全纯结构自带的 $\bar\partial_E$；这是后面标准联络存在唯一性的前提。 |
| p.131 | 背景 | (9.7.7) 表明标准联络的 1 形式完全由 $\alpha=\bar\partial$ 的标架矩阵决定，故又称 Chern 联络。 |
| p.133 | 校勘 | (9.8.4) 右端的 $F^{0,2},F^{1,1}$ 原书未写下标 $A$，照录；实即 $F_A^{0,2},F_A^{1,1}$。 |
| p.135 | 校勘 | 原书把向量丛的「直既約」gloss 作 indecomposable，把联络的「直既約」gloss 作 irreducible，同一词形两种含义；译文分别作「直和不可分解」与「不可约」。 |
| p.136 | 校勘 | 上段「$v\in B$」原书如此，按上下文应为 $v\in V$（$B$ 疑为 $V$ 之误），照录。 |
| p.137 | 校勘 | 原书称 $L^p_k$ 范数被 $L^q_l$ 范数从上控制，方向似与嵌入 $L^p_k\subset L^q_l$ 相反（通常为 $\|f\|_{L^q_l}\le C\|f\|_{L^p_k}$）；照录原书。 |
| p.140 | 校勘 | (9.11.33) 右端原书作 $C^0(C)$，按上下文应为 $C^0(X)$（$C$ 疑为 $X$ 之误），照录。 |
