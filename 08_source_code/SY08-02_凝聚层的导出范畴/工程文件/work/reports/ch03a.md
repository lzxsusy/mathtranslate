# ch03a 报告（原书 p.544–p.549 前）

## 1. 内容与结构

覆盖：第 3 章标题（p.544）、§3.1（p.544–547）、§3.2（p.547–549，止于注 3.2.4 末句）。

- `\chapter{导出范畴之间的全忠实函子}`（p.544，CHAPTER 3 原在页中，其前七段属 §2.2，归 ch02b，本块不重复译）
- `\section{Postnikov 图及其卷积}` + `\takeaway`（p.544）
  - 段 1：本节任务（p.544）；段 2：有界复形 $X^{\cdot}$ 的记号（p.544）；段 3：左 Postnikov 系统定义 + 图 544a（p.544）
  - 段 4：$\star$/$\circlearrowleft$ 的含义、左卷积、$\Tot(X^{\cdot})$、正合函子下的保持（p.545）；段 5：$\Tot$ 可能是类或空、引理出处 [3]（p.545）
  - 引理 3.1.1（p.545，含图 545a）；过渡句（p.545）
  - 引理 3.1.2（p.545–546，式 (25)(26)）
  - 引理 3.1.3（p.545–546，式 (27)(28)，含图 545b）
  - 证明（p.546–547，两引理同时归纳）：式 (29)、$\overline{d^{c+1}}$、图 546a、546b、547a、547b
- `\section{凝聚层导出范畴之间的全忠实函子}` + `\takeaway`（p.547）
  - 段 1–2：$X$、$M$、$\Db$、投影 $p,\pi$（p.547）；式 (30)、$\Phi^{*}_{\cE}$ 与 $\Phi^{!}_{\cE}$ 的两式、"$\cE^{\vee}$ 的定义"（p.547）
  - 段 3：猜想与本章主定理的引出（p.548）；定理 3.2.1（p.548）；推论句（p.548）；定理 3.2.2（p.548）
  - 段 4–5：$F^{*}$/$F^{!}$ 与 $F^{!}=S_{M}\circ F^{*}\circ S_{X}^{-1}$、Serre 函子（p.548）
  - 段 6：有界函子的定义（p.548）
  - 引理 3.2.3 + 证明（p.548–549：$\cO(k)$ 的右消解、谱序列、$\Hom^{j}(\cL^{i},F(A))\cong\Hom^{j}(G(\cL^{i}),A)$、同调维数）
  - 注 3.2.4（p.549，本块末条）

陈述条数：7（引理 3.1.1、引理 3.1.2、引理 3.1.3、定理 3.2.1、定理 3.2.2、引理 3.2.3、注 3.2.4），编号一律手工照抄原书。

## 2. 公式与图

### 编号公式（6 条）
| 号 | 页 | 内容 |
| --- | --- | --- |
| (25) | p.545 | $\Hom^{i}(X^{a},X^{b})=0$，$i<0$，$a<b$ |
| (26) | p.545 | $\Hom^{i}(X^{a},Y^{0})=0$，$i<0$，一切 $a$ |
| (27) | p.546 | $\Hom^{i}(X_{1}^{a},X_{2}^{b})=0$，$i<0$，$a<b$ |
| (28) | p.546 | $\Hom^{i}(X_{1}^{a},Y_{2}^{0})=0$，$i<0$，一切 $a$ |
| (29) | p.546 | $X^{c}\xrightarrow{d^{c}}X^{c+1}\xrightarrow{\alpha}Y^{c+1}\to X^{c}[1]$ |
| (30) | p.547 | $\Phi_{\cE}(\,\cdot\,):=\Rf\pi_{*}(\cE\otL p^{*}(\,\cdot\,))$ |

### 未编号 display（9 处）
$d^{c+2}\circ\overline{d^{c+1}}:Y^{c+1}\to X^{c+3}$（p.546）；$\Hom^{i}(Y^{c+1},X^{b})=0$（p.546）；$M\xleftarrow{\ p\ }M\times X\xrightarrow{\ \pi\ }X$（p.547，单行箭头串手写）；$\Phi^{*}_{\cE}$ 式（p.547）；$\Phi^{!}_{\cE}$ 式（p.547）；$F^{!}=S_{M}\circ F^{*}\circ S_{X}^{-1}$（p.548）；$\cO(k)\iso\{V_{0}\otimes\cO\to\cdots\to V_{N}\otimes\cO(N)\to 0\}$（p.548）；谱序列 $E_{1}^{p,q}=V_{p}\otimes H^{q}(G(\cL^{p}))\Longrightarrow H^{p+q}(G(\cL^{i}))$（p.549）；$\Hom^{j}(\cL^{i},F(A))\cong\Hom^{j}(G(\cL^{i}),A)$（p.549）。

### 七张图（2026-11-15 改为 TikZ 重绘，不再贴页图位图）
六张用 preamble 的 `\diag{...}`（内部 tikzcd，row sep 2.2em / column sep 2.6em）；544 那张最宽，`\diag` 的 2.6em 列距会溢出正文宽 81.8pt，故该图改用内联 `tikzcd` 并把 `column sep` 收到 1.45em、`row sep` 收到 1.9em（正文其余内容未动）。箭头标签一律写成 `"{...}"` 形式，避免 `,` 与未配对 `[]` 被 tikz-cd 的引号解析器截断。
1. `\diag` 首图（p.544 a）—— 左 Postnikov 系统全图。顶行 $X^{c}\xrightarrow{d^{c}}X^{c+1}\xrightarrow{d^{c+1}}X^{c+2}\cdots X^{0}$；底行 $Y^{c}=X^{c}$、$Y^{c+1}$、$Y^{c+2}$、$\cdots$、$Y^{-1}$、$Y^{0}$，相邻项箭头向左并标 $[1]$；斜箭头下行 $i_{k}$（最左标 $i_{c}=\id$）、上行 $j_{k}$（最左标 $j_{c}$），右端 $X^{0}$ 处上行标 $j_{-1}$、下行标 $i_{0}$；每个三角块内标 $\star$（特异）与小圆圈（交换）。引出语：第 17 行“是如下形式的图：”。
2. 图 545a（`\diag`）—— 三角态射。上行 $X\xrightarrow{u}Y\xrightarrow{v}Z\xrightarrow{w}X[1]$，下行 $X'\xrightarrow{u'}Y'\xrightarrow{v'}Z'\xrightarrow{w'}X'[1]$，竖直 $f,g,h,\{f[1]\}$。引出语：第 42 行“落在特异三角中：”。
3. 图 545b（`\diag`）—— 复形梯子。$X_{1}^{c}\xrightarrow{d_{1}^{c}}X_{1}^{c+1}\to\cdots\to X_{1}^{0}$ 对 $X_{2}^{c}\xrightarrow{d_{2}^{c}}\cdots\to X_{2}^{0}$，竖直 $f_{c},f_{c+1},f_{0}$。引出语：第 71 行“这两个复形之间的态射：”。
4. 图 546a（`\diag`）—— 锥的三角态射。$X_{1}^{c}\xrightarrow{d_{1}^{c}}X_{1}^{c+1}\xrightarrow{\alpha}Y_{1}^{c+1}\to X_{1}^{c}[1]$ 对 $X_{2}^{c}\xrightarrow{d_{2}^{c}}X_{2}^{c+1}\xrightarrow{\beta}Y_{2}^{c+1}\to X_{2}^{c}[1]$，竖直 $f_{c},f_{c+1},g_{c+1},\{f_{c}[1]\}$。引出语：第 110 行“补成三角态射，”。
5. 图 546b（`\diag`）—— 方块。$Y_{1}^{c+1}\xrightarrow{\overline{d_{1}^{c+1}}}X_{1}^{c+2}$ 对 $Y_{2}^{c+1}\xrightarrow{\overline{d_{2}^{c+1}}}X_{2}^{c+2}$，竖直 $g_{c+1},f_{c+2}$。引出语：第 115 行“考虑下图：”。
6. 图 547a（`\diag`）—— 复形梯子。$Y_{1}^{c+1}\xrightarrow{\overline{d_{1}^{c+1}}}X_{1}^{c+2}\to\cdots\to X_{1}^{0}$ 对 $Y_{2}^{c+1}\xrightarrow{\overline{d_{2}^{c+1}}}\cdots\to X_{2}^{0}$，竖直 $g_{c+1},f_{c+2},f_{0}$。引出语：第 123 行“于是我们得到复形态射”。
7. 图 547b（`\diag`）—— 三角态射。$Y_{1}^{-1}\xrightarrow{j_{-1}}X_{1}^{0}\xrightarrow{i_{0}}Y_{1}^{0}\to Y_{1}^{-1}[1]$ 对 $Y_{2}^{-1}\xrightarrow{j_{-1}}X_{2}^{0}\xrightarrow{i_{0}}Y_{2}^{0}\to Y_{2}^{-1}[1]$，竖直 $g_{-1},f_{0},g_{0},\{g_{-1}[1]\}$。引出语：第 132 行“特异三角之间的态射，”。

### 页图与文字层的出入
1. p.546：文字层把 $\overline{d^{c+1}}$ 的上划线全部丢掉（“there is a unique morphism dc+1 : Y c+1 → Xc+2 such that dc+1 ◦ α = dc+1”），页图印作 $\overline{d^{c+1}}$；已按页图处理并加 Tutor Note。
2. p.544、p.545、p.546、p.547 全部五幅图在文字层中只剩零散字母（$X$、$d$、$[1]$ 等），无任何箭头与结构；图的内容一律取自页图。
3. p.547：$\cE^{\vee}:=\mathbf{R}^{\cdot}\mathcal{H}om(\cE,\cO_{M\times X})$——文字层抽成“R·Hom”，页图为 $\mathbf{R}$ 带点 + 花体 $\mathcal{H}om$；按页图作 `\Rb\mathcal{H}om`。
4. p.547：式 (30) 页图印作 $\mathbf{R}\pi_{*}$（$\mathbf{R}$ 无点），与引言式 (1) 的 $\mathbf{R}^{\bullet}$ 不同；照录式 (30) 写法并加 Tutor Note。
5. p.549：谱序列右端页图与文字层**一致**印作 $H^{p+q}(G(\cL^{i}))$，而同一句结论写 $G(\cL^{k})$；原书如此，照录并加 Tutor Note。
6. p.548：定理 3.2.2 末句页图无句号（“…isomorphic to the functor $\Phi_{\cE}$”）；译本按中文习惯补句号。
7. p.545：括号内页图确为 $j_{k}\circ i_{k}=d^{k}$（上标，非下标 $d_{k}$），文字层同；未改。

## 3. 译注

`\yizhu` 4 条：
1. 第 37 行（p.544–545）：Postnikov 系统作为三角范畴中“全复形”的替代、逐级取映射锥、$\Tot$ 只是类；〔译者按〕说明图中圆圈标的是 $j_{k}\circ i_{k}=d^{k}$。【来源：原书 §3.1，p.544–545】
2. 第 166 行（p.547）：积分变换 / 核对象 $\cE$、$\cE^{\vee}$ 为对偶复形、定理 3.2.1 的含义。【来源：原书引言式 (1) 与 §3.2 式 (30)、p.547–548】
3. 第 191 行（p.548）：Serre 函子把 Serre 对偶范畴化，$S_{X}=(\,\cdot\,)\otimes\omega_{X}[\dim X]$，以及“有左伴随⇒有右伴随”的依据。【来源：原书 p.548 及所引式 (6)】
4. 第 195 行（p.548–549）：有界性的含义与引理 3.2.3 的证明思路（极丰富线丛 + $\cO(k)$ 右消解 + 谱序列）。【来源：原书 §3.2，p.548–549】

`% [Tutor Note: …]` 6 条：
1. 第 11 行：原书节标题与正文接排，本译本改为独立节标题并加节首重点框。
2. 第 33 行：p.544 图斜箭头落点在 200 dpi 页图上无法直读，按 $j_{k}\circ i_{k}=d^{k}$ 与 $i_{c}=\id$ 的相容性判定为 $i_{k}:X^{k}\to Y^{k}$、$j_{k}:Y^{k}\to X^{k+1}$。
3. 第 102 行：文字层丢失 $\overline{d^{c+1}}$ 的上划线，按页图补。
4. 第 168 行：式 (30) 的 $\mathbf{R}$ 无点，与引言式 (1) 的 $\mathbf{R}^{\bullet}$ 不一致，照录。
5. 第 213 行：谱序列右端 $G(\cL^{i})$ 与同句结论 $G(\cL^{k})$ 不一致，照录不改。
6. 第 227 行：本块止于注 3.2.4，3.3 标题及其后归 ch03b。

## 4. 术语

- 冻结表（`work/glossary.tsv`）中本块用到且照用：三角范畴、特异三角、正合函子、三角态射、映射锥、有界复形、卷积、Postnikov 系统、全复形、全忠实、伴随、等价、自等价、核对象、凝聚层、典范层、Serre 对偶、极丰富、丰富、线丛、对角的消解、拟同构、积分变换、Fourier–Mukai 函子、射影簇、光滑、完备。
- 冻结表不妥处：「right resolution」条为空（备注写“无”），而 p.548 必须译出，本块按“右消解”处理并列入提案；「Postnikov system」只有通用条目，p.544 的 left Postnikov system 需另立。
- 新定术语 10 条已写入 `work/proposals/ch03a.tsv`：left Postnikov system 左 Postnikov 系统（A）、left convolution 左卷积（A）、non-canonically isomorphic 非典范同构（A）、canonically isomorphic 典范同构（A）、morphism of complexes 复形态射（A）、Serre functor Serre 函子（A）、quasi-inverse functor 拟逆函子（A）、bounded functor 有界函子（A）、homological dimension 同调维数（A）、right resolution 右消解（A）。

## 5. 存疑

1. **p.544 图斜箭头的落点**。200 dpi 页图上，下行箭头的箭头端压在底行 $Y$ 的上缘、上行箭头压在与 $X$ 相邻处，无法百分百确认 $i_{k}$ 的终点是 $Y^{k}$ 还是 $Y^{k+1}$；本块报告采用“$i_{k}:X^{k}\to Y^{k}$、$j_{k}:Y^{k}\to X^{k+1}$”，与 $j_{k}\circ i_{k}=d^{k}$ 自洽，也与底行标注 $Y^{c}=X^{c}$ 自洽。若裁图后核对不符，只需改报告登记，正文文字不受影响（正文只说“如下形式的图”）。
2. **p.545 “that are in turn included into distinguished triangles”**：in turn 疑为 respectively 之误（英文措辞），照“分别”译出。
3. **p.549 “the non-zero cohomology of the objects $G(\cL^{j})$ belong to some interval”**：主谓不一致（belong/belongs），照译，未擅改。
4. **p.549 谱序列右端 $G(\cL^{i})$**：据上下文应作 $G(\cL^{k})$（消解对象是 $\cL^{k}$），页图与文字层一致印作 $i$，故照录并加批注。
5. **p.546 $\overline{d^{c+1}}$ 与 $d^{c+1}$ 并存**：原书以上划线区分“锥上的诱导态射”与“原微分”，文字层丢线后语义会冲突，已按页图恢复，可能与个别版本的排版不一致。
6. **编译状态**（最终，`build_ch03a`，主文件 `src/main.tex`，lualatex ×2）：`file:line=无「!」行 fatal=0 undefined=0 missingchar=0 overfull=0`，输出 `main.pdf (139 pages, 1347586 bytes)`，本块占 PDF p.44–48（印刷页 38–42），章/节编号“第 3 章 / 3.1 / 3.2”与页眉正确。中途一次构建曾出现 `! Package pgf Error: No shape named 'tikz@f@5-2-2' is known.`（定位在 `chunks/ch01a.tex:158`，他块），该块修好后已消失，与本块无关。更早的隔离构建（`work/build_ch03a`，仅 preamble + frontmatter + ch00a + ch03a）14 页同样 0 错；整书快照里曾有 3 处 `Missing character: There is no α (U+03B1)`（PDF p.80–81，他块正文裸写 Unicode α），现亦已消失。

## 6. 与邻块的边界

- 原书首句（本块从这里开始）：p.544 章标题下 “In this section we consider Postnikov diagrams in triangulated categories and find conditions under which a Postnikov diagram admits a convolution and this convolution is uniquely determined.”
- 原书末句（本块在这里收尾）：p.549 注 3.2.4 “…is non-zero only for $i\in[-a,0]$, where $a$ is a fixed positive integer.”
- 起点之前：p.544 上半页七段仍属 §2.2（flop 例子、定理 2.2.9/2.2.10、参考文献 [7][10]），归 ch02b，本块未重复译，也未漏译本章任何一句。
- 终点之后：“3.3. Construction of the object representing a fully faithful functor”标题及其正文归 ch03b，本块未译一字（第 194 行有 Tutor Note 标记）。
