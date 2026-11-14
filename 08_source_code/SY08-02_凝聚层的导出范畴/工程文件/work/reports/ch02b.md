# ch02b 报告（原书 p.538–p.544 前）

## 1. 内容与结构

覆盖：§2.2 全节，起于 p.538 中部的节标题，止于 p.544 第 3 章标题之前的最后一段。本块无 `\chapter`（第 2 章标题在 ch02a），节首为 `\section{等价的例子：flop 双有理变换}` + `\takeaway`，块末为第 2 章的 `\chapterreview`。

- `\section{等价的例子：flop 双有理变换}`（第 6 行，p.538）+ `\takeaway`（第 8 行）
- p.538：段 1 本节主旨（Mukai [29] 的阿贝尔簇与其对偶是第一个例子；本节的区别在于簇对由 flop 相联系；定理 2.1.3 的（反）典范层条件不能减弱）；段 2 回忆定义（见 [5]、[6]）；定义 2.2.1（右正交 $\cB^{\perp}$、左正交 ${}^{\perp}\cB$，第 14 行）；注（三角子范畴的正交仍是三角子范畴，第 18 行）；定义 2.2.2（右/左可容许，第 20 行）
- p.539：段 1 可容许性的正交刻画（特异三角 $N\to X\to M$、$M\to X\to N$）；段 2 半正交分解的引出（$\langle\cN^{\perp},\cN\rangle$、$\langle\cN,{}^{\perp}\cN\rangle$）；定义 2.2.3（第 31 行，含 display）；段 3（完备例外族是最简单的例子）；定义 2.2.4（第 42 行）；例 2.2.5（第 48 行，[2]）；段 4（二次超曲面与旗簇 [20]–[22]）；段 5 爆破的事实 + 交换图（TikZ，第 56 行）
- p.540：段 1（$i,j$ 闭嵌入、$p$ 平坦、$\tilde Y\cong\PP(N_{X/Y})$、$\cO_{\tilde Y}(1)$、$\cO(-\tilde Y)$，第 59 行）；命题 2.2.6（第 63 行，[34]）+ 证明（第 67–78 行）；命题 2.2.7（第 80 行，([34], [7])）+ 证明（第 84–108 行）；段 2（$D(X)$、$D(Y)_k$ 的定义，第 109 行）
- p.541：定理 2.2.8（第 112 行，[34]）；段 1（该定理的用途）；段 2（$Y\cong\PP^k$、$N_{X/Y}\cong\cO_Y(-1)^{\oplus(l+1)}$、$l\leqslant k$，第 123 行）；段 3（例外除子 $\tilde Y\cong\PP^k\times\PP^l$、正规层公式，第 125–129 行）；段 4（沿 $\PP^l$ 的收缩、$X^+$ 解析存在但未必代数、假设代数、图 (20)，第 129–133 行）；段 5（$\mathrm{fl}:X\dashrightarrow X^+$ 是 flip/flop 的最简单例子，第 135 行）；段 6（典范层限制 + 伴随公式 + 式 (21)，第 141–157 行）
- p.542：定理 2.2.9（第 160 行）+ 证明（第 165–211 行：式 (22)(23)(24)、$D(X)^{\perp}=\langle D(Y)_{-l},\dots,D(Y)_{-1}\rangle$、完备例外族的大 display）
- p.543：续证明（$D(X)^{\perp}=\langle\cB,\cA\rangle$、Hom 消没、Serre 对偶，第 213–228 行）；定理 2.2.10（第 232 行）+ 证明（第 236–241 行）；段 1（多个不交子簇上同时作 flop，第 240 行）；段 2（Fano 三维簇的双投影构造，第 242 行）
- p.544：段 1（Fano 段续：正规丛 $\cO(-1)\oplus\cO(-1)$、定理 2.1.3 条件不能减弱、极小模型纲领中的一般型簇）；段 2（$Y\cong\PP(E)\to Z$ 的推广）；段 3（三维簇 + 有理曲线 $Y\cdot K_X=0$ 的三种正规丛，[7]、[10]）；Tutor Note 标明本块在此收尾（第 250 行）
- `\chapterreview`（第 252 行起，五段：全章地位／知识脉络／核心结论／辨析与提醒／评注；汉字 734 字，落在 700–1100 区间内）

陈述条数：10（定义 2.2.1、2.2.2、2.2.3、2.2.4，例 2.2.5，命题 2.2.6、2.2.7，定理 2.2.8、2.2.9、2.2.10），编号一律手工照抄原书，未用 `\label`/`\ref`。段序段数与原书一致，未合段、未拆段。

## 2. 公式与图

### 编号公式（5 条，含 1 幅编号图）
| 号 | 页 | 内容 |
| --- | --- | --- |
| (20) | p.541 | flop 的六节点交换图（TikZ 重绘，套 `equation`+`\tag{20}`，见下） |
| (21) | p.541 | $\omega_{\tilde X}|_{\tilde Y}\cong(\pi^{*}\omega_{X}\otimes\cO_{\tilde X}(l\tilde Y))|_{\tilde Y}\cong p^{*}(\omega_{X}|_{Y})\otimes\cO_{\tilde X}(l\tilde Y)|_{\tilde Y}\cong\cO(-k;-l)$，按原书拆两行（`aligned`） |
| (22) | p.542 | $\Hom(A,B)\xrightarrow{\ \sim\ }\Hom(\Lf\pi^{+*}A,\Lf\pi^{+*}B)\longrightarrow\Hom(\Rf\pi_*(\Lf\pi^{+*}A\otL\cL),\Rf\pi_*(\Lf\pi^{+*}B\otL\cL))$，两行 `align`，首行 `\notag` |
| (23) | p.542 | $\Lf\pi^{*}\Rf\pi_*(\Lf\pi^{+*}A\otL\cL)\longrightarrow\Lf\pi^{+*}A\otL\cL\longrightarrow\overline A$ |
| (24) | p.542 | $\Hom(\overline A,\Lf\pi^{+*}B\otL\cL)=0$ |

### 未编号 display（按页）
- p.539：$\cD=\langle\cN_0,\dots,\cN_n\rangle$（定义 2.2.3）；$(\cO(i),\dots,\cO(i+N))$（例 2.2.5 中的族，行内给出）
- p.540：$\Rf\pi^{*}\colon\Db(X)\to\Db(\tilde X)$ 与 $p^{*}\colon\Db(Y)\to\Db(\tilde Y)$（命题 2.2.6，一行内用「与」连接，照原书 and 的位置）；$\Rf j_*(\cL\otimes p^{*}(\,\cdot\,))\colon\Db(Y)\to\Db(\tilde X)$（命题 2.2.7）；$\Hom(\Lf\pi^{*}F,\Lf\pi^{*}G)\cong\Hom(F,\Rf\pi_*\Lf\pi^{*}G)\cong\Hom(F,\Rf\pi_*\cO_{\tilde Y}\otL G)$；$\Hom^{i}(j_*\cO_F,j_*\cO_F)\cong\Hom^{i}(\Lf j^{*}j_*\cO_F,\cO_F)$；$\cO_F\otimes\cO_{\tilde Y}(1)[1]\to\Lf j^{*}j_*\cO_F\to\cO_F$；$\Hom^{i}(\cO_F\otimes\cO_{\tilde Y}(1),\cO_F)=0$；$\Hom^{i}(j_*\cO_F,j_*\cO_F)\cong\Hom^{i}(\cO_F,\cO_F)$
- p.541：$\langle D(Y)_{-r+1},\dots,D(Y)_{-1},D(X)\rangle$（定理 2.2.8）；$N_{\tilde X/\tilde Y}=\cO_{\tilde X}(\tilde Y)|_{\tilde Y}\cong\cO(-1;-1)$；$\cO(-1;-1):=p_1^{*}\cO_{\PP^k}(-1)\otimes p_2^{*}\cO_{\PP^l}(-1)$；$\omega_{\tilde X}\cong\pi^{*}\omega_X\otimes\cO_{\tilde X}(l\tilde Y)$；$\omega_X|_{Y}\cong\omega_Y\otimes\bigwedge^{l+1}N^{*}_{X/Y}\cong\cO_Y(l-k)$
- p.542：$\Rf\pi_*(\Lf\pi^{+*}(\,\cdot\,)\otimes\cL)\colon\Db(X^+)\to\Db(X)$（定理 2.2.9）；$\Hom(\Rf\pi_*(\Lf\pi^{+*}A\otL\cL),\Rf\pi_*(\Lf\pi^{+*}B\otL\cL))\cong\Hom(\Lf\pi^{*}\Rf\pi_*(\Lf\pi^{+*}A\otL\cL),\Lf\pi^{+*}B\otL\cL)$；$D(X)^{\perp}=\langle D(Y)_{-l},\dots,D(Y)_{-1}\rangle$；完备例外族的三行 + 两列 $\vdots$ 的大括号 display
- p.543：$D(X)^{\perp}=\langle\cB,\cA\rangle$；$\Hom(\overline A,\Rf j_*\cO(a-i;-s))=0$（$1\leqslant i\leqslant k$、$1\leqslant s\leqslant l$）；$\Hom(\Lf\pi^{+*}B\otL\cL,\overline A\otimes\omega_{\tilde X})=0$；$\cA\otimes\omega_{\tilde X}\subset D(X^+)^{\perp}\otimes\cL$（行内）；定理 2.2.10 的函子与 $\cL'=\cL^{-1}\otimes\omega_{\tilde X}\otimes\pi^{+*}\omega_{X^+}^{-1}$

### 两张交换图（TikZ 重绘，2 处；`src\figures\` 已清空，不再用 `\figdiag`）
1. `\diag{…}`（第 56 行）—— 爆破的方块图，2×2：上行 $\tilde Y\xrightarrow{\ j\ }\tilde X$，左列 $p\downarrow$，右列 $\pi\downarrow$，下行 $Y\xrightarrow{\ i\ }X$。引出语：第 55 行末“并且有交换图：”。
2. `equation` 内 `\parbox` 包 `\diag{…}`（第 130–139 行）—— 原书图 (20)，6 个节点、7 条箭头：顶为 $\tilde Y$；中排左 $Y$、中 $\tilde X$、右 $Y^+$；底排左 $X$、右 $X^+$。箭头为 $p:\tilde Y\to Y$、$j:\tilde Y\to\tilde X$、$p^{+}:\tilde Y\to Y^{+}$、$i:Y\to X$、$\pi:\tilde X\to X$、$\pi^{+}:\tilde X\to X^{+}$、$i^{+}:Y^{+}\to X^{+}$。引出语：第 129 行末“上面描述的几何都包含在下图中：”。编号用 `\tag{20}` 挂在同一个 `equation` 上，实测（`work\ch02b_fig39.png`）编号落在图的中部右侧，与原书一致。

### 页图与文字层的出入（均已在正文照录并加 `% [Tutor Note]`）
1. p.540 命题 2.2.6 证明：投影公式末项页图印 $\Rf\pi_*\cO_{\tilde Y}\otL G$，而同一证明的下一行印 $\Rf\pi_*\cO_{\tilde X}\cong\cO_X$；按投影公式应为 $\cO_{\tilde X}$，原书此处当是笔误，照录页图。
2. p.542–543：文字层把 (23)、(24) 及以下各处的 $\overline A$ 一律抽成 $A$（上横线丢失），页图三处均印 $\overline A$；已按页图作 $\overline A$，以免与证明开头的 $A\in\Db(X^+)$ 混淆。
3. p.542：定理 2.2.9 及其证明中，页图印 $\Lf\pi^{+*}$（$+$ 与 $*$ 都在上标位），而同一证明的末句左伴随印 $\Rf\pi^{+}_{*}$（$+$ 上标、$*$ 下标）；两种写法都是 $(\pi^{+})^{*}$ 与 $(\pi^{+})_{*}$，照录页图，不作统一。
4. p.541：图 (20) 的扫描件多处箭头与节点糊死，底排两个节点标签与右下角若干残段不可辨，右端残留短虚线无法判定归属；重绘依据与取舍已写进第 137 行的 Tutor Note，未画任何页图不能证实的虚线箭头。
5. p.540 首句“the projective bundle of the exceptional divisor of $\tilde Y$ over the centre $Y$”文句本身歧义（$\tilde Y$ 与 $X$ 都在句中出现），已按上下文（$\tilde Y$ 即爆破的例外除子）译出，并在第 61 行留批注。

## 3. 译注

`\yizhu` 5 条（均以 `【来源：…】` 收尾，来源为原书 / 所引原始论文，属 A 级）：
1. 第 24 行（p.538–539）：可容许性 = 伴随存在 = 每个对象能“投影”到子范畴上，从而把三角范畴劈成两块；呼应定理 2.2.8 的 $D(X)$ 与诸 $D(Y)_k$。
2. 第 38 行（p.539）：半正交分解是“带方向的直和”，$j<i$ 时单向消没、反方向允许非零，是“半”字由来；以 $\langle D(Y)_{-r+1},\dots,D(Y)_{-1},D(X)\rangle$ 为例。
3. 第 51 行（p.539）：例外对象像点一样刚性、完备例外族给出与 $\End(\bigoplus_i E_i)$ 上模范畴的等价；$\PP^N$ 上的 $(\cO(i),\dots,\cO(i+N))$ 是最早的例子。
4. 第 119 行（p.541）：定理 2.2.8 即 Orlov 爆破定理，$\Db(\tilde X)$ 由 $\Db(X)$ 与 $r-1$ 份“扭过的” $\Db(Y)$ 拼成，并说明本节为何需要它。
5. 第 139 行（p.541）：flip 与 flop 的定义性区别（典范类是否改变），并指出 $l<k$ / $l=k$ 正对应 flip / flop，来源为原书 §2.2 与式 (21) 以及 Kollár–Mori 的专著（A 级）。

`% [Tutor Note: …]` 5 条：
1. 第 61 行：p.540 首句“exceptional divisor of $\tilde Y$”的文句歧义与译法。
2. 第 78 行：命题 2.2.6 证明中 $\cO_{\tilde Y}$ / $\cO_{\tilde X}$ 的原书笔误。
3. 第 137 行：图 (20) 的辨读清单（6 节点、7 箭头），供裁图核对。
4. 第 214 行：$\overline A$ 的上横线在文字层丢失，本译本从页图。
5. 第 250 行：本块止于第 3 章标题之前，其下归 ch03a。

## 4. 术语

- 冻结表（`work/glossary.tsv`）中本块用到且照用：半正交分解、可容许子范畴、正交／左正交／右正交、例外对象、例外族、完备例外族、flop（保留英文）、flop 收缩、收缩、例外除子、爆破、作爆破、正规丛、线丛、丰富、极丰富、典范层、反典范、投影公式、双有理变换、三维簇、射影、光滑、簇、生成、全加性、三角范畴。
- 冻结表未收、本块必须译出的词，已按 STYLE_GUIDE 记入 `work/proposals/ch02b.tsv`（14 条，均为 A 级）：flip（保留英文）、flip 变换、相对丰富、正规层（区别于正规丛：原书用 normal sheaf）、射影丛、爆破中心、射影化、真变换、双投影、一般型、极小模型纲领、自同态代数、指标、反典范系统。
- 取舍说明：flip 与 flop 一律保留英文（glossary 只冻结了 flop），全块未出现「翻转」这个译法；「general type」取「一般型」而非「通用型」；「proper transform」取「真变换」而非「真原像」。

## 5. 存疑

1. **命题 2.2.6 证明中的 $\cO_{\tilde Y}$**：页图确实印 $\tilde Y$（已放大到 900 dpi 逐字核对，与下一行的 $\cO_{\tilde X}$ 字形不同）。按投影公式应为 $\cO_{\tilde X}$，判断为原书笔误；照录页图并加批注，未擅改。
2. **图 (20) 的箭头方向**：扫描件（缩微胶片）已多处糊死，底排两个节点的标签完全不可辨；$p$、$j$、$p^{+}$、$i$、$\pi$、$\pi^{+}$、$i^{+}$ 七条箭头的起讫按“$\tilde Y$ 在顶、$X$ 与 $X^{+}$ 在底”的几何辨读并重绘为 TikZ，页图右端残留的短虚线无法判定归属，未画。
3. **定理 2.2.8 与后文下标范围的差异**：定理写 $D(Y)_{-r+1},\dots,D(Y)_{-1}$（$r$ 为余维），而 p.542、p.543 一律写 $D(Y)_{-l},\dots,D(Y)_{-1}$。原书在特例（$Y\cong\PP^k$，余维 $r=l+1$）中把 $r$ 换成 $l$，两处并不矛盾，故照录，未统一记号。
4. **式 (20) 的编号位置**：已解决。图改为 TikZ 重绘后，编号由同一个 `equation` 的 `\tag{20}` 给出，实测落在图的中部右侧，与原书一致（见 `work\ch02b_fig39.png`）。
5. **“the proper transforms of the lines”**：取「真变换」；若全书他处已定「严格变换」（strict transform），需与 Lead 统一。
6. **编译状态**（Lead 指定的整书构建）：`cd src; lualatex -interaction=nonstopmode -output-directory=…\build_ch02b main.tex` → `main.pdf` 137 页；`file:line=无「!」行 fatal=0 undefined=0 missingchar=0 overfull=0`（另查 `Undefined control sequence`=0）。本题两图所在页为 PDF p.37（爆破方块图）与 p.39（图 (20)），已渲染核对：`work\ch02b_fig36.png`–`work\ch02b_fig39.png`。早先的隔离构建 `work/build02b/chk.tex` 亦为 0/0/0（当时 `src/` 被多个块的并行编译共用，`src/main.pdf` 一度被并发写入损坏，故曾改用隔离构建）。

## 6. 与邻块的边界

- 原书首句（本块从这里开始）：p.538 “**2.2. Examples of equivalences: flopping birational transformations.** In this section we present an entire class of examples of pairs of smooth varieties for which the derived categories of coherent sheaves are equivalent.”
- 原书末句（本块在这里收尾）：p.544 “More recently, the equivalence of categories was proved in all these cases together in [10].”
- 起点之前：p.538 上半页仍是 §2.1 的收尾（推论 2.1.12 及其证明、$K(X)\to K(Y)$ 与 $\mathrm{ch}\cdot\sqrt{\mathrm{td}}$ 的交换图、“is commutative.”一句），归 ch02a，本块从节标题起译，未重复。
- 终点之后：p.544 的 `CHAPTER 3 — Fully faithful functors between derived categories` 及其下的 §3.1 归 ch03a（其报告已注明 p.544 上半页七段属本块）。本块未译第 3 章一字。
