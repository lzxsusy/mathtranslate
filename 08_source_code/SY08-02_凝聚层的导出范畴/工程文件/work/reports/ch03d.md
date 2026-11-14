# ch03d 报告（原书 p.564–p.567）

## 1. 内容与结构
- 本块覆盖的小节与页码：§3.5「附录：齐次坐标代数的 n-Koszul 性质」全文，原书 p.564–p.567 上半页（正文止于式 (46) 之后的 “That is, the complex (46) is exact.”；p.567 下半页的 CHAPTER 4 标题与 4.1 首段不属本块）。段序照原书：p.564 起 7 段 + 引理 3.5.1 及其证明 + 复形 $P^\bullet_n$ 引出段；p.565 续完 $P^\bullet_n$ 正合性、$P^\bullet_2$ 例、引理 3.5.2 + (43) 及其证明、$B_n$ 与 $R_{n-1}$ 的记号段、命题 3.5.3；p.566 命题 3.5.3 证明的 1)（含 (44)）与 2) 的开头（含 (45)）；p.567 续完 2) 与 3)（含 (46)）。
- 主要陈述清单：
  - 引理 3.5.1：$\cJ^{(m)}_1\cong\cO_{\Delta^{(m)}_{(m,\ldots,1)}}$，$k>1$ 时 $\cJ^{(m)}_k\cong s_*p^*(J_{\Sigma^{(k-1)}})$，并给出 a) b) c) 三条上同调/导出推进的同构。
  - 引理 3.5.2：丰富丛 $\cM$ 的充分大幂 $\cL=\cM^i$ 使条件 (43)（a) b) c) 三条消没）对一切 $1<m\leqslant k$ 成立。
  - 命题 3.5.3：条件 (43) 下 1) $A$ 是 n-Koszul 代数；2) $\cL^k$ 的层复形正合；3) 对角 $\Delta\subset X\times X$ 有 n-消解。（即 §3.3 命题 3.3.4 的证明版本。）
  - 无定理、推论、定义、例、注。

## 2. 公式与图
- 编号公式：(43)（引理 3.5.2 的三条消没条件，右花括号成组，标号在中间行）、(44)（证明 1) 的两条，标号在第二行）、(45)（证明 2) 的两条，标号在第二行）、(46)（$X\times X$ 上的 n-消解）。
- `\figdiag` 占位：无。本块只有线性箭头串（复形与长正合列），照原文分行打排，没有二维交换图，故未用 `\figdiag`。
- 页图与文字层的出入（逐条）：
  1. p.564–p.567 全篇：文字层把花体 $\mathcal{J}$ 抽成大写 $I$（如 “I(m) k”“In”）；页图印作 $\mathcal{J}^{(m)}_k$。处理：从页图作 `\cJ`，并加 Tutor Note。
  2. p.564：「$s$ 是子簇 $S^{(m)}_k\cong X^{k-1}\times X$ 到 $X^n$ 的嵌入」——文字层与页图一致，均作 $X^n$。处理：照录 + Tutor Note（据上下文应为 $X^m$）。
  3. p.565 命题 3.5.3 第 3) 条、p.567 式 (46)：均作 $\cO_M\boxtimes R_0$。核对 §3.3（ch03b.tex「令 $R_0=\cO_M$」）后确认是沿用的记号而非笔误（本节簇改称 $X$，$\cO_M$ 即 $\cO_X$）。处理：照录 + Tutor Note 说明。
  4. p.566：「the exactness for $i\leqslant 1$ has been proved above」，而上一句的序列是对 $i\geqslant 1$ 给出的。处理：照录 + Tutor Note（应为 $i=1$ 的情形）。
  5. p.566–p.567 的 (44)(45) 标号位置：页图把标号排在第二条等式的行末，已用 `align` + `\notag`/`\tag` 复现；(43) 用 `\left.\begin{aligned}…\end{aligned}\right\}` 复现右花括号。
  6. 上标/下标逐条核过：引理 3.5.1 a) b) 末为 $\otimes A_{m-k+i}$、c) 末为 $\boxtimes\cL^{m-k+i}$；(44) 1) 末为 $\otimes A_{m-k+i}$，(45) 1) 末为 $\otimes A_{m-k+1}$（$i$ 与 $1$ 之别是原文如此，未改）。

## 3. 译注
- `\yizhu` 条数：4。
  1. 齐次坐标代数（含射影正规时与 $\PP^N$ 中齐次坐标环一致、分次结构与附加条件的作用）。
  2. Koszul 复形（经典定义、本块 $P^\bullet_n$ 的同型性、$n=2$ 时退化为 $0\to J_\Delta\to\cO_{X\times X}\to\cO_\Delta\to 0$）。
  3. n-Koszul 性质（复述定义 3.3.3 与式 (33) 的 $B_m$ 递归、Ext 代数 $\Ext^\bullet_A(k,k)$ 与「由 $\Ext^1$ 生成」的 Koszul 判据）。
  4. 对角的消解（$\cO_\Delta$ 作末项、外张量积化归、与 n-Koszul 消解互为表里、§3.3 的 Beilinson 型消解）。
- `% [Tutor Note:]` 条数：5。分别注：花体 $\mathcal{J}$ 被文字层抽成 $I$；$s$ 的嵌入目标 $X^n$ 应为 $X^m$；命题 3.5.3 是 §3.3 命题 3.3.4 的改写版本且 $\cO_M$ 为沿用记号；$i\leqslant 1$ 实指 $i=1$；式 (46) 的 $\cO_M$ 同前注。

## 4. 术语
- 用了冻结表但觉得不妥的：`ideal sheaf` 表中无条目，按表中 `sheaf`=层 处理为「理想层」；`resolution of the diagonal` 表中作「对角的消解」，本块照用。`ample sequence` 依 ch03c 作「丰富序列」，章末评注中首次出现时括注英文。
- 新定术语（已写入 proposals/<名>.tsv）：无。本块未出现冻结表之外的新术语，故未建 `work/proposals/ch03d.tsv`。

## 5. 存疑（必须老实写）
- 未解决的疑点：
  1. p.564「$s$ 是 … 到 $X^n$ 的嵌入」：页图与文字层一致，但 $s$ 的像落在 $X^m$ 中（引理 3.5.1 全部在 $X^m$ 上取上同调），猜测原文欲写 $X^m$。已照录并批注，未改原文。
  2. p.566「the exactness for $i\leqslant 1$」：与上句「对 $i\geqslant 1$」并存，猜测指 $i=1$（正合性对 $i\geqslant1$ 成立，而 $i=1$ 已在 1) 中证过）。已照录并批注。
  3. 命题 3.5.3 陈述中的 $k$（第 2 条）与 (43) 中的 $k$ 不是同一个量，原文未加区分；照译，未补写说明（避免越界补内容）。
- 编译状态：`file:line=0 fatal=0 undefined=0 missingchar=0 overfull=0`
  - 隔离编译（`src/_check_ch03d.tex`：preamble + 本块）：0 个 `!` 错、0 处 `Missing character`、0 处 `Overfull/Underfull \hbox`。
  - 整书编译（`main.tex`，lualatex）：0 个 `!` 错；日志中 3 处 `Missing character: There is no α (U+03B1)` 出现在 `chunks/appendix_b.tex`（他人分块），与本块无关；本块无 `Overfull \hbox`。注意：多人同时在同一 `src/` 目录编译，`main.pdf` 偶有被并发写入而损坏的情况，本块的版面核验以隔离编译为准。

## 6. 与邻块的边界
- 本块从哪句开始：原书 p.564 小节标题 “3.5. Appendix: the n-Koszul property of a homogeneous coordinate algebra” 及其后首句 “The facts collected in this appendix are not original, and are well known in one form or another.”
- 到哪句为止：p.567 “That is, the complex (46) is exact.”（紧接 “CHAPTER 4 / Derived categories of coherent sheaves on K3 surfaces / 4.1. K3 surfaces and the Mukai lattice.” 之前）。
- 有没有把邻块的内容多译/漏译：无。BRIEF 记本块为 p.564–566，实际正文延伸至 p.567 上半页（命题 3.5.3 的证明跨页），已按任务书的「CHAPTER 4 之前」执行；p.567 下半页的第 4 章标题与 4.1 首段留给 ch04，未译一字。块末 `\chapterreview` 为第 3 章章末评注（五段，929 字），不属任何邻块内容。
