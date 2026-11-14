# ch03c 报告（原书 p.555–p.563）

## 1. 内容与结构
- 本块覆盖的小节与页码：§3.4“主定理的证明”，p.555 中部（“3.4. Proof of the main theorem.”）至 p.563 末。p.555 上半页是命题 3.3.5 的陈述与证明末段，属 ch03b；p.564 整页为 §3.5，属 ch03d（该页无 §3.4 的残留文字，已核 p054.png）。
- 主要陈述清单（编号 + 一句话）：
  - 定义 3.4.1：阿贝尔范畴中指标为负的对象序列 $\{P_i\}$ 之“丰富性”（三条条件 a) b) c)）。
  - 例 3.4.2：射影簇上丰富线丛给出的序列 $\{\mathcal L^{i}\mid i\leqslant 0\}$ 是丰富的。
  - 引理 3.4.3：$\Hom^{\bullet}(P_i,X)=0$（$i\ll 0$）推出 $X=0$。
  - 引理 3.4.4：$\cA$ 有限同调维数时，$\Hom^{\bullet}(X,P_i)=0$（$i\ll 0$）推出 $X=0$。
  - 引理 3.4.5：丰富序列上所有 $k$、$j<i$ 的 $\Hom^{k}$ 同构，推出正合函子 $F$ 全忠实。
  - 命题 3.4.6：$\cC$ 上的同构 $f:j\iso F|_{\cC}$ 可唯一延拓为整个 $\Db(\cA)$ 上的同构 $\id\iso F$（证明分 7 步）。
  - 定理 3.2.1 的证明（原书无独立编号，接排于命题之后）：1) 存在性（用命题 3.3.5、引理 3.3.1、3.4.5、3.4.6 与映射锥 $C_Z$）；2) 唯一性（复形 (32) 的卷积 + 引理 3.1.2 + 命题 3.3.5）。

## 2. 公式与图
- 编号公式：(38)（a) b) c) 三条件，用 `aligned` 排、单号）、(41)、(42)。另有两个**带编号的交换图** (39) 与 (40)，按页图位置用 `equation` + `\tag` 把编号排在图右侧（正文仍以“交换图 (39)”“方块 (40)”指称）。
- 交换图共 11 张，已全部用 TikZ（`\diag{…}` 或自写 `tikzcd`）重绘，不再走 `\figdiag` 占位：
  - p.557 a：两个上下相叠的特异三角 $Y\to P_i^{\oplus k}\to X\to Y[1]$ 与 $F(Y)\to F(P_i^{\oplus k})\to F(X)\to F(Y)[1]$，中间一条竖箭头 $f_i$。
  - p.558 a：交叉方块，上排 $P_j^{\oplus l}\to P_{i_2}^{\oplus k_2}$、下排 $P_{i_1}^{\oplus k_1}\to X$，竖箭头 $w_1$（左）、$v_2$（右），上排横箭头 $w_2$。
  - p.558 b：三列两行，上排 $P_j^{\oplus l}\to P_{i_1}^{\oplus k_1}\to X$，下排 $F(\cdots)\to F(\cdots)\to F(X)$，竖箭头 $f_j$、$v_2$、$f_X$（页图原样，见下条出入）。
  - p.558 c：方块 $P_i^{\oplus k}\to X$、$P_j^{\oplus l}\to Y$，竖箭头 $\psi$、$\varphi$。
  - p.559 a：上排 $Z\to P_i^{\oplus k}\to X\to Z[1]$，下排 $F(W)\to F(P_j^{\oplus l})\to F(Y)\to F(W)[1]$，竖箭头 $F(\psi)f_i$ 与 $h_t$（$t=1,2$）。
  - p.559 b：$\Ext^{1}$ 方块：$Y\to Z\to X\to Y[1]$ 及其 $F$ 像，竖箭头 $f_Y$、$f_Z$、$f_Y[1]$。
  - p.560 a：图 (39)，四列 $P_i^{\oplus k}$、$X$、$Y$、$P_i^{\oplus k}[1]$ 与对应下行 $F$ 像，竖箭头 $f_i$、$f_X$、$f_Y$、$f_i[1]$；其中第 2 列那条 $f_X$ 按页图排作**虚线**（400 dpi 裁切 c560a2.png 已核：是竖直虚线箭头，不是斜向）。
  - p.560 b：方块 $P_j^{\oplus l}\to P_{i_2}^{\oplus k_2}$、$P_{i_1}^{\oplus k_1}\to H^{0}(X)$，竖箭头 $w_1$、$u_2$。
  - p.561 a：三角态射 $(w_1,\id,\varphi)$：$P_j^{\oplus l}\to X\to Y_j\to P_j^{\oplus l}[1]$ 与 $P_{i_1}^{\oplus k_1}\to X\to Y_{i_1}\to P_{i_1}^{\oplus k_1}[1]$，竖箭头 $w_1$、$\id$、$\varphi$、$w_1[1]$。
  - p.561 b：方块 $Y_j\to Y_{i_1}$、$F(Y_j)\to F(Y_{i_1})$，竖箭头 $f_{Y_j}$、$f_{Y_{i_1}}$。
  - p.561 c：方块 (40)：$X\to Y$、$F(X)\to F(Y)$，竖箭头 $f_X$、$f_Y$。
- 页图与文字层的出入（逐条）：
  - p.556（及本块各处）：文字层抽出“Hom·”，页图印作 $\Hom$ 的上标小圆点；本译本统一作 $\Hom^{\bullet}$。处理：照页图语义，加 Tutor Note。
  - p.558 b：中间一条竖箭头页图印作 $v_2$，按上下文应为同构 $f_{i_1}$（与左右两条 $f_j$、$f_X$ 并列）。处理：照录 + Tutor Note。
  - p.561：页图印 $F(\varphi)F_{Y_j}y$，据上下文应为 $F(\varphi)f_{Y_j}y$。处理：照录 + Tutor Note。
  - p.562 式 (41)：末项页图印 $P_i^{\oplus k}$，按特异三角应为 $P_i^{\oplus k}[1]$。处理：照录 + Tutor Note。
  - p.562 式 (42)：中间项页图印 $f(\beta\varphi)f_X$（小写正体 $f$），据上下文应为 $F(\beta\varphi)f_X$。处理：照录 + Tutor Note。
  - p.563：页图印“Applying Lemma 3.6”，本章无 3.6 号引理，所指应为引理 3.4.3。处理：照录 + Tutor Note。
  - p.563：页图印 $F^{!}(Z)=0$，据上下文应为 $F^{!}(C_Z)=0$。处理：照录 + Tutor Note。
  - p.563：文字层把函子同构抽作 $f$，页图实印 $\overline{f}$（裁切 z_barf.png 已核）。处理：按页图写作 $\overline{f}$。
  - p.559：文字层与页图均为 $f_{X[n]}=f_X[n]$（即 $f_X$ 的平移），非笔误，初稿一度误标，已删去该条 Tutor Note。

## 3. 译注
- `\yizhu` 条数：4
  1. 丰富序列为何是本节技术核心：把“对象为零”化为“在一列对象上各阶 $\Hom$ 全为零”，并说明 a) b) c) 各自的作用（p.555）。
  2. 分次 $\Hom$ 记法 $\Hom^{\bullet}(E,F)=\bigoplus_k\Hom^{k}(E,F)$，及页图小圆点上标的处理（p.556）。
  3. 定理 3.2.1 证明中“三角分裂”的两步：分裂得 $F(Z)\cong C_Z[-1]\oplus\Phi_{\cE}(Z)$，再代入 $Y=Z[1]$ 使 $\Hom(C_Z,C_Z)=0$（p.563，以〔译者按〕收尾）。
  4. “复形 (32) 的卷积”与引理 3.1.2 的作用（p.563）。
- `% [Tutor Note:]` 条数：8
  1. 块起点边界：p.555 上半页归 ch03b，本块仍标 p.555 页标。
  2. 分次 Hom 上标圆点（Hom$^{\cdot}$ → $\Hom^{\bullet}$）。
  3. p.558 第二条竖箭头印作 $v_2$，应为 $f_{i_1}$。
  4. p.561 $F(\varphi)F_{Y_j}y$ 应为 $F(\varphi)f_{Y_j}y$。
  5. p.562 (41) 末项缺 $[1]$。
  6. p.562 (42) 中间项 $f(\beta\varphi)$ 应为 $F(\beta\varphi)$。
  7. p.563 “Lemma 3.6”应为引理 3.4.3。
  8. p.563 $F^{!}(Z)$ 应为 $F^{!}(C_Z)$。

## 4. 术语
- 用了冻结表但觉得不妥的：无。要点：ample→丰富、amply/very ample→极丰富、distinguished triangle→特异三角、mapping cone→映射锥、convolution→卷积、Postnikov system→Postnikov 系统、fully faithful→全忠实、exact functor→正合函子，均按表。原书 “auto-equivalence” 对应表中 autoequivalence→自等价，按表译，不另立条目。
- 新定术语（已写入 `work/proposals/ch03c.tsv`）：ample sequence→丰富序列（p.555）；homological dimension→同调维数（p.556）；full subcategory→全子范畴（p.557）；direct summand→直和项（p.563）。

## 5. 存疑（必须老实写）
- 未解决的疑点：
  1. p.560 图 (39) 的虚线：400 dpi 裁切复核后确认是第 2 列竖直箭头 $f_X$ 排作虚线（不是斜向箭头），已按此排出，该疑点消解；页图为何把这一条画成虚线，原书未作说明。
  2. p.562 式 (41) 第三支缺 $[1]$：照录，但 (42) 之后的推理（$\Hom(X,F(-))$ 作用于三角）实际上依赖第三支为 $P_i^{\oplus k}[1]$ 或至少依赖该三角的形状，本块未在正文改动，保持原样。
  3. p.563 “Applying Lemma 3.6”：按论证只可能是引理 3.4.3（丰富序列上 $\Hom^{\bullet}$ 全为零则对象为零），但也不排除原书另有编号体系；照录，待 Lead 决断是否统一。
  4. p.558 第 1 步“由于 $\Hom(Y[1],F(X))=0$，由引理 3.1.1 存在唯一的态射 $f_X$”：原文只写 $\Hom(Y[1],F(X))=0$，而引理 3.1.1 的用法需要该消没对足够负的指标成立；本块照原文直译，未补条件。
- 编译状态：`file:line=无 fatal=0 undefined=0 missingchar=0 overfull=0`（`-output-directory=build_ch03c` 整书编译一轮：`main.log` 中 `^!` 计数 0、`Undefined control sequence` 0、Missing character 0、Overfull \hbox 0；11 张图的 `tikzcd` 引号标签一律外层加花括号、标签内不出现逗号，未触发 `\tikz@quote@@parser` 报错）。

## 6. 与邻块的边界
- 本块从哪句开始：原书 p.555 的 “**3.4. Proof of the main theorem.** In the previous section, starting from a fully faithful functor $F$ between the derived categories of coherent sheaves on varieties $M$ and $X$, we constructed an object $\mathcal E$ on the product $M\times X$ …”。
- 到哪句为止：原书 p.563 末 “Applying Proposition 3.3.5, we now see that the objects $\mathcal E_1$ and $\mathcal E_2$ are themselves also isomorphic.”（定理 3.2.1 证明结束）。
- 有没有把邻块的内容多译/漏译：没有。p.555 上半页命题 3.3.5 的陈述与证明末段（含两个交换图）未译，归 ch03b；p.564 的 §3.5 全节（含引理 3.5.1）未译，归 ch03d。§3.4 在 p.563 末已自然结束，p.564 无 §3.4 残留句，故边界无缝隙、无重叠。
