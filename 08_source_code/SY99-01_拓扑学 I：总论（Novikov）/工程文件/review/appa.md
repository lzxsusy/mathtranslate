# 核验报告 · appa（原书 p.274–282，附录导言与 §2 纽结）

核验人：译者戊　　作者：译者辛　　日期：2026-11-09

## 结论
通过（小改）。逐页核对 9 页（`pages\p281.png`–`p289.png`）：章标题、§1/§2 标题、`\takeaway`、10 条 Tutor Note、7 张裁图（图 A.1–A.7）与全部公式（Alexander/HOMFLY/Kauffman/Jones 多项式、Burau 表示、群环微分算子 $\partial_{a_i}$ 与矩阵 $q_{ij}$）均与原书逐个对得上，无内容性错误。必须改只剩 1 条页标记位置；另有 2 条建议。

## 必须改（影响正确性）
1. **第 189 行**（`% [原文 p.281]`）：页标记插在句中——「……一个整值函数，它在几乎所有点处为常数（即在某些「跳跃」的代数`% [原文 p.281]`」后紧接「子簇 $W_j\subset\mathrm{Rep}_n(\pi_1)$……」。须把该句写完（「……之外）；$b_i(\rho)$ 的值在每个这样的子簇上跳跃，在它们的两两交集上又进一步跳跃，如此递推。」）后再放该标记。
   （第 21 行的 p.275 标记此前曾嵌在句中，现已由作者改为独占一行，复查通过。）

## 建议改（可读性/忠实度）
1. **第 14 行**：原书 p.274 本段把 Salamon 印作 "Salomon"（与同行 "Calaby--Yau" 一样都是原书拼写）。下一行 Tutor Note 只解释了 Calaby--Yau，未提 Salomon；建议照印 Salomon 并在同一条 Note 或新 Note 里补一句「原书 p.274 拼作 Salomon，通行拼法为 Salamon」，与 Calaby--Yau 的处理保持一致。
2. **第 248–251 行**：Yang–Baxter 一般式的右括号被塞进数学式里（`$R_{12}R_{13}R_{23}=R_{23}R_{13}R_{12}.\ \text{）}$`），建议把「）」移出数学模式，改为 `$R_{12}R_{13}R_{23}=R_{23}R_{13}R_{12}$.）` 一类写法，排版更稳。

## 抽查记录（逐页）
- **p.274**（`pages\p281.png`）：章标题 "Recent Developments in the Topology of 3-manifolds and Knots"、§1 标题与导读段（1983–84 写成、1986 俄文出版；Floer 同调与辛拓扑；$SO_2$ 作用与椭圆亏格；TQFT/Reidemeister–Ray–Singer 挠；矩阵模型与模空间；瞬子）；Calaby--Yau 拼写、Oshanine、Kontzevich 均照原；`\takeaway` 有且仅有一条——一致（建议改 1）。
- **p.275**（`p282.png`）：量子场论物理学家转入抽象数学；对 QFT 严格化现状的评论；§2 标题 "Knots: the classical and modern approaches to the Alexander polynomial. Jones-type polynomials"；纽结/链环定义 $K=\bigcup K_i$、$K_i\cap K_j=\varnothing$；投影与图（generic、交叉、定向）；补空间 $M=S^3\setminus K$ 与小管状邻域的 2 维环面边界——一致。
- **p.276**（`p283.png`）：$\pi_1(M)$ 与 $T^2\subset M^2$（原书确印 $M^2$，Note 已说明）；Papakyriakopoulos 定理、Haken 算法、Waldhausen 的拓扑等价判据与算法未决问题；Alexander 多项式与 Conway 重发现；图 A.1 的定义性关系 $y(D_{n,+})-y^{-1}(D_{n,-})=z(D_{n-1})$（figA1.png 已打开核对：三图与 $y,y^{-1},z$ 标注完整、无原书图题）；$zP_{D_{n-1}}=P_{D_{n,+}}-P_{D_{n,-}}$；零图条件与平凡图取值 1——一致。
- **p.277**（`p284.png`）：$A(t,t^{-1})=P(z)$、$z=t^{1/2}-t^{-1/2}$；HOMFLY 的 $xH_{D_{n-1}}=yH_{D_{n,+}}-y^{-1}H_{D_{n,-}}$ 与 $H=1$（平凡纽结）；$y=1,x=z$ 得 Alexander、$x=y^{1/2}-y^{-1/2}$ 得 Jones；Kauffman 状态多项式（图 A.2）、$Q_{D_0}=\mu=(a-a^{-1})/z+1$、Reidemeister 变换下乘 $a^{\pm1}$（原书确印大写 $A^{\pm1}$，Note 正确）；$K_{D_n}=a^{-w(D_n)}Q_{D_n}(a,z)$ 与 writhe 数——一致。
- **p.278**（`p285.png`）：图 A.3（第一 Reidemeister 变换与状态多项式）、图 A.4（由交叉定向决定的 writhe 数 ±1）；$J_D(t)=K_D(z=t^{-1/4}-t^{1/4},a=t^{3/4})/(t^{1/2}-t^{-1/2})$；Jaeger 定理；Kauffman bracket $S_{D_n}(A,B;d)=AS_{D_{n-1,a}}+BS_{D_{n-1,b}}$、$S_{D_0}=d$、$B=A^{-1}$、$-d=A^2+A^{-2}$（图 A.5）——一致。
- **p.279**（`p286.png`）：$J(A^4,A^{-4})=(-A)^{-3w(D)}S(A,B;d)$、$t=A^{-4}$；$S$ 与 Turaev–Reshetikhin 不变量的关系；图 A.6 三种 Reidemeister 变换；Whitney–Pontryagin–Thom 的「通有性质」对问题简化的作用；群环中「微分」的拓扑来源（L. Alania；图 A.7 基本群计算）——一致。
- **p.280**（`p287.png`）：复形 $L$ 的 0/1/2-胞腔与形变收缩；万有覆叠上的自由 $\Z[\pi_1]$-模复形与方阵；$\partial_{a_i}(a_j)=\delta_{ij}$、$\partial_{a_i}(bc)=\partial_{a_i}(b)+b\partial_{a_i}(c)$、$q_{ij}=\partial_{a_i}(r_j)$；$a_i\mapsto t$ 与 Laurent 多项式、余子式最大公因式给出 $A(t)$；Milnor 的挠率处理与 $\mathrm{Rep}_n(\pi_1)$、跳跃子簇——一致（页标记见必须改 1）。
- **p.281**（`p288.png`）：跳跃子簇上 $b_i(\rho)$ 的跳变；$M=S^3\setminus K$、$n=1$ 时 $\mathrm{Rep}_1(\pi_1)=\C\setminus\{0\}=\C^*$；引文（$i=1$ 时跳跃子簇是有限点集，恰为 Alexander 多项式的根）；$k$ 分支链环的 $H_1(M)=\Z^k$、$(\C^*)^k$ 与多变量 Alexander 多项式（H. Murakami）；Le Tu 对二桥纽结的考察；辫群 $B_n$ 与 Markov 定理、两个 Markov 变换——一致。
- **p.282**（`p289.png`）：辫对应的几何解释（$S^1\subset\R^3$ 的管状邻域、横截纽结、Alexander 与 Markov）；线性表示 $\rho$ 与特征 $\chi_\rho(a)=\Tr[\rho(a)]$；Jones 用 Yang–Baxter 方程构造表示；$S:V\otimes V\to V\otimes V$、$S_{12}S_{23}S_{12}=S_{23}S_{12}S_{23}$、$R=\tau S$ 的一般形式；$\rho(\sigma_i)=S_{i,i+1}$ 与 $\rho_n$——一致（建议改 2）。

## 体例抽查
- 页标记：`% [原文 p.274]`…`% [原文 p.282]` 共 9 个，递增、无重复 ✓；1 处落在句中（必须改 1）。
- 公式：本块原书无编号公式，全部用无编号 `\[ \]` ✓；无自造编号 ✓。
- 图：A.1–A.7 七张裁图齐全（`src\figures\figA1.png`–`figA7.png`），裁图不含原书图题，`\figtitle` 中文另写 ✓。
- 陈述：无编号引文用 `quote`+`\itshape` ✓；Hecke 等无编号陈述处理正确。
- Tutor Note：10 条（要求 ≥ 9/3 = 3）✓，单行、无 `%` 字符 ✓。
- `% CHUNK appa DONE` 在末行 ✓。
- check_chunk 复跑：页 274..282、tag 0、陈述 0、Note 10、本节重点 2、OK（0 error）。
