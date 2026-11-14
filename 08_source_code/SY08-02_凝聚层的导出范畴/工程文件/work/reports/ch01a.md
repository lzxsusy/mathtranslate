# ch01a 报告（原书 p.517–p.523 前）

## 1. 内容与结构

- 覆盖范围：第 1 章「Preliminaries」标题（p.517）与 §1.1「Triangulated categories and exact functors」（p.517–p.523 前）。§1.2 标题及其后内容未译入，归 ch01b。
- 页码说明：任务书写「p.517–522，7 页」，但块的实际终点锚是 p.523 上的 §1.2 标题**之前**，因此 p.523 上位于该标题之前的 Lemma 1.1.12、「足够多的 F-分裂对象」一段与编号公式 (2) 收在本块（详见 §5 与 §6）。译本在整书中占 PDF p.12–17，共 6 页。
- 主要陈述清单：
  - 定义 1.1.1：三角范畴之间正合函子的定义（p.518，两条：与平移交换、保持特异三角）。
  - 引理 1.1.2（[6]、[8]）：正合函子的左（或右）伴随仍正合（p.519）。
  - 定义 1.1.3：Serre 函子——范畴等价 $S$ 加双函子同构 $\varphi_{A,B}:\Hom(A,B)\iso\Hom(B,SA)^*$（p.519）。
  - 引理 1.1.4（[8]）：任何范畴等价与 Serre 函子交换；随后一段给出 Serre 函子的唯一性（在同构意义下唯一确定）（p.519）。
  - 引理 1.1.5（[6]）：三角范畴的 Serre 函子正合（p.519）。
  - 引理 1.1.6（[17]、[25]）：$\Sigma\cap\cB$ 亦有左分式演算；$\cB$ 右共尾时典范函子全忠实（p.520）。
  - 定义 1.3：全忠实函子（p.521；原书编号异常，见 §2、§3）。
  - 命题 1.1.8：按 Deligne 的方式赋予结构后 $\cD/\cN$ 是三角范畴，$Q$ 正合（p.521）。
  - 命题 1.1.9（[12]）：Deligne 构造，$\Rf F$ 在特异三角的两端有定义即在整个三角上有定义，$\cW$ 为三角子范畴（p.522）。
  - 引理 1.1.10：$\Rf F$ 在 $V\in\cV$ 上有定义 $\iff$ $\Rf(Fj)$ 在 $V$ 上有定义，且有函子同构 $\Rf(Fj)V\iso\Rf F\Rf jV$（p.522）。
  - 定义 1.1.11：（右）F-分裂对象（p.522）。
  - 引理 1.1.12：F-分裂的判别——$\Sigma$ 中任一 $s:Y\to Y'$ 的像 $QFs$ 有收缩（p.523）。
- 非陈述内容：公理 T1–T4（p.517–518，其中 T3、T4 各配一图）；局部化与左分式演算 L1–L4（p.519）；$\cC[\Sigma^{-1}]$ 的显式描述（p.520）；右共尾定义（p.520）；$\cD/\cN$ 的构造（p.521）；Deligne 构造中的 $\mathbf{r}F_Y$、$\Rf FY$ 与左导出函子 $\mathbf{l}F_Y$、$\Lf FY$（p.521–522）；「足够多的 F-分裂对象」与公式 (2)（p.523）。

## 2. 公式与图

- 编号公式：仅 (2)（p.523），已按页图核对：$\Hom(\Lf GX,Y)\cong\Hom(X,\Rf FY)$，限定语「对 $X\in\cD/\cN$ 与 $Y\in\cC/\cM$」在公式同一行右侧，编号居右。本块无其它编号公式，其余公式均用 `equation*`。
- 图：6 张，全部按页图以 TikZ（preamble 的 `\diag{tikzcd}`）重排；原 `\figdiag` 占位框已全部删除，`src/figures/` 不再需要为本块裁图。逐图（页码 + 节点 + 箭头 + 标签方位，方位一律以页图为准）：
  1. p.518 a（T3）：8 节点，上排 $X\xrightarrow{u}Y\xrightarrow{v}Z\xrightarrow{w}X[1]$，下排 $X'\xrightarrow{u'}Y'\xrightarrow{v'}Z'\xrightarrow{w'}X'[1]$；竖箭头 $f$（标签在左）、$g$、$h$（虚线）、$f[1]$（后三者标签在右）；左侧方块内、$f$ 箭头右侧画 $\square$。
  2. p.518 b（T4）：4 行 4 列，第 3 行缺第 1 列、第 4 行只有 2 个节点。行 1：$X\xrightarrow{u}Y\xrightarrow{x}Z'\to X[1]$（末箭头无标签）；行 2：$X\to Z\xrightarrow{y}Y'\xrightarrow{w'}X[1]$（首箭头无标签）；行 3：$X'=\!=\!=X'\xrightarrow{r}Y[1]$；行 4：$Y[1]\xrightarrow{x[1]}Z'[1]$。竖箭头：第 1 列 $\|$；第 2 列 $v$、无标签、$r$；第 3 列 $w$、$t$、无标签；第 4 列 $\|$、$u[1]$。标签一律在箭头右侧，两处横箭头（$r$、$x[1]$）的标签在上。
  3. p.519 a（L3）：4 节点；上边 $u$ 实线，左边 $s$ 实线下指（标签在左），右边 $t$ 虚线下指（标签在右），下边 $u'$ 虚线右指（标签在下）。
  4. p.520 a（两个偶等价的「屋顶」图）：5 节点（$X$ 左、$Y$ 右、$Y''$ 上、$Y'''$ 中、$Y'$ 下）；$f:X\to Y''$、$s:Y\to Y''$、$h:X\to Y'''$、$r:Y\to Y'''$、$g:X\to Y'$、$t:Y'\to Y$，另有 $Y''\to Y'''$（下指）与 $Y'\to Y'''$（上指）两条竖箭头。页图上这两条竖箭头是单根粗线，**不是**双箭头（12 倍放大确认），故用普通箭头。
  5. p.520 b（复合 $(g'f,s't)$ 的图）：6 节点（$Z''$ 顶、$Y'$ 左上、$Z'$ 右上、$X$ 左下、$Y$ 下中、$Z$ 右下）；实线 $f:X\to Y'$、$s:Y\to Y'$、$g:Y\to Z'$、$t:Z\to Z'$，虚线 $g':Y'\to Z''$、$s':Z'\to Z''$——与正文复合式 $(g'f,s't)$ 相符（初版报告曾把两条虚线标签误读作 $s',t'$，已按页图放大更正）。
  6. p.521 a（$\mathbf{r}F_Y$ 的等价关系）：左右并列两个同构菱形。左：$Y$ 在左、$Y'$ 在上、$Y'''$ 在中、$Y''$ 在下，标 $s$（$Y\to Y'$）、$u$（$Y'\to Y'''$，竖下）、$r$（$Y\to Y'''$，横右）、$t$（$Y\to Y''$）、$v$（$Y''\to Y'''$，竖上）；右：同样形状，节点换成 $X,FY',FY''',FY''$，标 $f$、$h$、$g$、$Fu$、$Fv$。
- 页图与文字层的出入（逐条：页码 + 文字层抽出 + 页图实际 + 处理）：
  1. p.518（T2 箭头）：文字层把标签抽成两行、与箭头分离（形如 `-u[1]` 落在符号表外）；页图为 $-u[1]$ 置于箭头上方。处理：写 `\xrightarrow{-u[1]}`。
  2. p.521（$\mathbf{r}F_Y$）：文字层作 `rFY`；页图为粗体 r、正体 F、$Y$ 作下标。处理：写 `\mathbf{r}F_Y`（preamble 无小写粗体宏，用 `\mathbf{r}`，未新造宏）。
  3. p.522（同一函子）：页图此处 $Y$ **不**作下标（作 `rFY`），与 p.521 不一致。处理：统一作 `\mathbf{r}F_Y`，加 Tutor Note 说明。
  4. p.520：同段内先把等价类代表写作 $(s,f)$，随即写作 $(f,s)$。页图与文字层一致，属原书自身不统一。处理：两处均照录，加 Tutor Note。
  5. p.522（引理 1.1.10 末）：页图作「RFRjV」连续排列，$F$ 与 $Rj$ 之间无空隙。处理：照录为 `$\Rf F\Rf jV$`，未添加空格或点号。
  6. p.517 b)：原文「a class of distinguished (or exact) triangles」；术语表规定 exact triangle 一律作「特异三角」。处理：正文作「特异（或正合）三角」保留原文括注，并加 Tutor Note 说明与术语表的关系。
  7. p.519（定义 1.1.3）：$\varphi$ 公式右端「for any objects $A,B\in\cD$」与公式同处一行。处理：用 `\qquad\text{对任意对象 } A,B\in\cD.` 排在同一公式行。
  8. p.523（公式 (2)）：行内限定语同样与公式同行。处理：同上，用 `\qquad\text{对 } X\in\cD/\cN \text{ 与 } Y\in\cC/\cM.`。
- 另：p.518 T1 的三角 $X\xrightarrow{\id}X\to 0\to X[1]$ 在页图上是单行箭头串，故按行间数学处理，未作图。

## 3. 译注

- `\yizhu` 条数：5。分别注了：
  1. （p.517–518 之后）T1–T4 各条的作用：T1 管恒等与同构、T2 是旋转规则、T3 管三角态射的补全、T4 即八面体公理；并声明本稿沿用原书编号，不把 T4 改称八面体公理。
  2. （p.519 定义 1.1.3 之后）Serre 函子之名源于 Serre 对偶：光滑射影簇上 $S(-)=(-)\otL\omega_X[\dim X]$；引理 1.1.5 说明三角范畴的 Serre 函子自动正合。
  3. （p.521 命题 1.1.8 之后）$\cD/\cN$ 即 Verdier 商：对象不变，态射为「屋顶」的等价类；$\cN$ 中对象在商中同构于零，反之亦然，故 $\cN$ 是 $Q$ 的核。
  4. （p.522 命题 1.1.9 之后）Deligne 构造把导出函子定义为可表性，等价于 $\Rf F$ 是 $QF$ 沿 $Q$ 的右 Kan 扩张；不要求阿贝尔范畴或内射消解。
  5. （p.522 定义 1.1.11 之后）F-分裂的直观（$F$ 在该对象上「已经算对」）、与「足够多的 F-分裂对象」的关系、引理 1.1.12 的可裂判别。
- `% [Tutor Note:]` 条数：4。分别注了：
  1. p.517 b) 的 exact triangle 括注与术语表「一律特异三角」的关系（照录括注）。
  2. p.521 陈述编号印作 Definition 1.3（跳过 1.1.7，其后命题为 1.1.8）；页图与文字层一致，照录 1.3，不改作 1.1.7。
  3. p.520 $(s,f)$ 与 $(f,s)$ 次序不一致，两处照录。
  4. p.522 $\mathbf{r}FY$ 与 p.521 $\mathbf{r}F_Y$ 写法不同，本译本统一作 $\mathbf{r}F_Y$。
- 另有一处技术性注释说明不够：preamble 的 `\usepackage` 未提供小写粗体宏，故用 `\mathbf{r}`（未新造宏）。

## 4. 术语

- 用了冻结表但觉得不妥的：无。「distinguished triangle＝特异三角」与「calculus of fractions＝分式演算」「cofinal＝共尾」均按表执行；唯一有张力的是 p.517 的同义名 exact triangle，已在原处加 Tutor Note 说明保留括注的理由。
- 与邻块对齐（两处，避免全库不一致）：
  - multiplicative system：本块初稿作「乘性系」，因 ch01b 已提案「乘法系」，已全块改为「乘法系」，本文件不再重复提案。
  - Serre functor＝Serre 函子：ch02a、ch03a 已提案，本块照用，不重复提案。
- 新定术语（已写入 `work/proposals/ch01a.tsv`，7 条）：F-split＝F-分裂；enough F-split objects＝足够多的 F-分裂对象；full additive subcategory＝全加性子范畴；full subcategory＝全子范畴；bifunctorial isomorphism＝双函子同构；retraction＝收缩；roof＝屋顶（仅译注用）。凡首现处均写成「中文（English）」。

## 5. 存疑（必须老实写）

- **块边界**（页码 + 问题 + 猜测）：任务书说本块是 p.517–522，但终点锚是 p.523 上 §1.2 标题之前。p.523 的 Lemma 1.1.12、「足够多的 F-分裂对象」段与公式 (2) 都在该标题之前，按锚点应属本块，我收进来了；若 Lead 要求严格按「到 p.522 末」，则这三段须移交 ch01b，公式 (2) 的编号归属也要相应改写。
- **p.522 引理 1.1.10 末的「RFRjV」**：字面连排，按数学含义应为 $(\Rf F)(\Rf j)$ 作用于 $V$。我照录未改；若 Lead 认为应断作 $\Rf F\circ\Rf j$，只需改这一处。
- **`\yizhu` 跨页**：p.12→13 的 T1–T4 译注被分页切开（框体在第 12 页底，`【来源：…】` 落到第 13 页顶）。preamble 的 `\yizhu` 未设不可分页；本块不能改 preamble，若要求整框不跨页需 Lead 统一处理（例如给框体加 `\needspace` 或 `breakable=false`）。
- **陈述环境 `[附加名]` 的坑（建议全库知会）**：`\begin{lemma}[{[6]、[8]}]{1.1.2}` 会被 TeX 的定界参数扫描在第一个 `]` 处截断，排成「、 [ ([6]) 8] 引理」这类乱码（本块初稿即如此，页上可见）。可行写法是把方括号字符包进组：`[{{[}6{]}、{[}8{]}}]`（ch02a 亦用 `{[}8{]}`），本块 5 处（引理 1.1.2、1.1.4、1.1.5、1.1.6、命题 1.1.9）已全改为该写法并逐页核对通过。根治办法是在 preamble 用 xparse 的 `O{}` 参数。
- **TikZ 图的一个坑（建议全库知会）**：`\arrow[r,"u[1]"]` 里标签中的 `]` 会提前结束 `\arrow[...]` 的可选参数，报 `! Argument of \tikz@quote@@parser has an extra }`。可行写法同 §5 上一条：把方括号包进组，即 `"u{[}1{]"`。本块的 $u[1]$、$x[1]$、$f[1]$ 三处标签均用此写法。另：`\arrow[...,equal]` 画出的 $\|$、$==$ 在 150 dpi 下会糊成单线，300 dpi 下正常，校对时需放大看。
- **附录 B 的「待裁切」注记**：已按 Lead 指示检索 `src/chunks/*.tex`，`appendix_b.tex` 只有两条与「裁切」有关的校勘注（第 96 行的 p.541 图 (20)、第 141 行的编号 (39)），均属其他块，与本块 6 张图无关；本块范围内不存在需要改写的「待裁切」注记（原 `\figdiag` 占位框已全部换成 TikZ）。
- **编译状态**：单块自检（`work/tools/ch01a_solo.tex`，只 `\input` 本块，xelatex 两遍）`fatal=0 undefined=0 missingchar=0 overfull=0`，7 页（图重排后比占位框多 1 页）。整书编译（`xelatex -output-directory "$env:TEMP\build_ch01a" main.tex`，两遍）138 页，全库 `!`=0、`Overfull \hbox`=0、`Undefined control sequence`=0、`Missing character`=0；本块位于印刷页 6–11（PDF 12–17），其中 p.518 b（印刷 p.7）与 p.521 a（印刷 p.10）已单独渲染核对。整书是并行编辑的，最终仍以 Lead 的收口编译为准。

## 6. 与邻块的边界

- 本块起点（原书首句）：「A detailed treatment of the facts collected in this chapter may be found in [14], [24], [25], and [44].」——紧接 `CHAPTER 1` / `Preliminaries` / `1.1. Triangulated categories and exact functors.` 之后的第一段。p.517 上半页（引言末段与 $0\to\Z\oplus(A\times\hat A)_k\to\Auteq\Db(A)\to U(A\times\hat A)\to 1$ 一行）属 ch00a，未重复译入。
- 本块终点（原书末句）：「…and hence there are functorial isomorphisms $\Hom(\Lf GX,Y)\cong\Hom(X,\Rf FY)$ for $X\in\cD/\cN$ and $Y\in\cC/\cM$. (2)」——即 p.523 上 §1.2 标题之前的最后一行。
- 多译/漏译检查：未译入 p.523 的「1.2. Derived categories and derived functors」标题及其后的 $\mathbf{C}(\cA)$、$\mathbf{H}(\cA)$、标准三角、映射锥等内容（归 ch01b）；也未回译 p.517 上半页的 ch00a 内容。段序与段数与原文逐段对应，未并段、未拆段（`\yizhu` 为新增注记，不计入原书段数）；原书陈述均无证明，本块亦未补写证明。
