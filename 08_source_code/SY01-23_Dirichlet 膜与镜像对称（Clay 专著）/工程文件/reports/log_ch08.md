# ch08 校订日志（rv-ch04 接手，原任务 rv-ch08 / task-10）

负责文件：`chapters/ch08.tex`、`ch08-sec82.tex`、`ch08-sec83.tex`、`ch08-sec84head.tex`、`ch08-sec84tail.tex`、`ch08-sec85.tex`
负责页范围：PDF 585–663（第 8 章），共 12 块。
规则：`review/GUIDE.md`。只改上述 6 个 tex 文件与本日志；不运行 LaTeX 编译；不新建其他文件。

## 已核对范围
- 块1：`chunks/ch08/p585-594.txt`（p585–594）✅
- 块2：`chunks/ch08/p595-596.txt`（p595–596）✅

## 块1：p585–594 ✅（无改动）
已核对段落 id：ch08-intro-001…004、ch08-8.1.1-001…016（含 sec:8.1 标题、8.1.1 引言、图1–图9、def:8.1 带状树、def:8.2 $\overline S_d$、def:8.ainfty-space、note:8.3）、ch08-8.1.2-001…010（def:8.4 $A_\infty$ 代数与 (8.2)、$d=1,2,3$ 的展开与 (8.3)(8.4)(8.5)、def:8.5 态射与 (8.6)）

逐段与原文比对，未发现漏译/误译/数学错误，未作 edit。要点核对：
- 环路空间复合公式、$m_3$ 的同伦、$\overline S_4/\overline S_5$ 的各面公式、结合多面体与带状树（def 8.1、def 8.2）、$A_\infty$ 空间定义中的 (8.1) 括号与 $m_{d-p+1}(T,\ldots,m_p(T',\ldots),\ldots)$ 公式、def 8.4 的 (8.2) 符号 $(-1)^{\deg a_1+\cdots+\deg a_q-q}$、(8.3)(8.4)(8.5) 各项系数与符号、def 8.5 的 (8.6) 左右两侧，均与原文一致。
- 原文 p586 的 "$(x_1x_2)x_3$"（pdftotext 输出）在数学上应为 $(x_3x_2)x_1$，译文作 $(x_3x_2)x_1$，是正确写法，不需改。

块1 待确认（未改）：
- ch08-intro-002（L6–8）：原文 "the category of A-branes on X is isomorphic to the category of B-branes on $\check X$"，译文作"等价于"。范畴的"同构"与"等价"技术上不同，但下句原文自身也转到 "equivalence of categories"，译法可接受。
- ch08-8.1.1-012（def:8.2，L141–146）：译文末尾加"树按保持出顶点、循环次序及边长的同构识别；零长内部边通过收缩识别。"，原文该处无此句（属译者补足模空间的识别规则）。

## 块2：p595–596 ✅（无改动）
已核对段落 id：ch08-8.1.2-011…017（严格态射与 (8.7)、$d=1,2$ 的展开与 (8.8)、态射复合、def:8.6 $A_\infty$ 范畴、$A_\infty$ 函子、拟同构/严格函子、$H^*(\mathcal A)$ 与 $H^0(\mathcal A)$）

逐段与原文比对，未发现漏译/误译/数学错误，未作 edit。要点核对：(8.7)(8.8) 的符号与项数、复合公式的求和范围、def:8.6 的复合映射与 $2-d$ 次数、$A_\infty$ 函子的 $F_d$ 映射与关系式、H^*(A) 与 H^0(A) 的定义均一致。

块2 待确认（未改）：
- ch08-8.1.2-016（L397–405）：原文只定义 "$F$ is a quasi-isomorphism if $F_1$ ... is a quasi-isomorphism for each $X_0,X_1$"，译文加"即拟全忠实"（属术语性补注，通常称为 quasi-fully-faithful）。
- ch08-8.1.2-017（L406–423）：译文在 $H^0(\mathcal A)$ 后加"同样，在未施加幺性条件时，它可以不具有恒等态射。"，原文只对 $H^*(\mathcal A)$ 说过一次。
- ch08-8.1.2-013（L341–352）：原文 "where $r\ge1$ and $s_1+\cdots+s_r=d$"，译文加"$s_i\ge1$"（正分拆的隐含条件，补出无害）。
- ch08-8.1.2-014/015（L353–396）：译文补"其中求和范围与\BookRef{def:8.4}{定义 8.4}相同"及"各指标的范围与\BookRef{def:8.5}{定义 8.5}相同"，原文 def 8.6 处未明写（函子处原文有 "with the indices as in Definition 8.5"）。

## 块3：p596–605（8.2 例与构造）✅（无改动）
已核对：ch08-8.2.1-001…026（8.2 节标题、$D^b_\infty(X)$ 与 Čech 全复形、$\partial=d+(-1)^p\delta$、$m_1,m_2$ 与 (8.3)(8.4)、thm:8.7、投影算子 $\Pi$ 与链同伦 $H$、$\Pi\mathcal A$ 的 $m_d$ 与 $A_\infty$ 函子 $i$、图10–图15、$\widehat m_d$ 的两段论证、ex:8.8 与两张表）。
结论：未作 edit。
核对要点（与原文一致）：$\delta$ 公式 $d_{\mathcal F}\circ f_m-(-1)^q f_{m+1}\circ d_{\mathcal E}$；Čech 微分求和 $j=0$ 到 $p+1$（原文 pdftotext 显示到 $p$，系上标丢失，译文正确）；$\widehat m_d^{\Pi\mathcal A}$ 目标次数 $[3-d]$（原文显示 $[3-n]$，译文正确）；$\Pi\mathcal A$ 的 $m_d$、$i_d$ 定义，$\widehat m/\widehat i$ 的 $\Pi-1$ 与 $m_1H+Hm_1$ 展开、$p=1,d$ 的排除；五个层 $\mathcal O(1),\mathcal O(2),\mathcal O(-2),\mathcal O(-1),\mathcal O$ 的 Čech 复形与 $\Pi,H$ 表逐项一致。
块3 待确认（未改）：
- 8.2.1-025 后面的 $m_3$ 计算表：原文 p605 最后一行为 $z^{-1},(z,z),(z,z),1,(1,0),(1,1)$，译文该行末格作 $(0,0)$（其余各格一致）。两种取值都不影响其后"最后一列非零"的结论；无法断定原书误植还是译者改算，未改。
- ch08-8.2.1-021（L317–319）：译文"这个分次范畴的零次上同调范畴就是通常的 $D^b(X)$，其各次态射则为导出范畴中的相应 $\operatorname{Ext}$ 群"，原文只作 "The latter category is equal to $D^b(X)$ as an ordinary category"；译文加了"零次上同调范畴/各次态射为 Ext 群"的解释（意思无误，属补足）。

## 块4：p605–614（8.3 引言、Morse 范畴、8.3.2 预范畴、8.3.3 Fukaya 范畴开头）✅ 2 处改动
已核对：ch08-8.3-intro-001、8.3.1-001…020（Morse 理论回顾、def:8.9、$o_p$ 与 Morse 复形、$m_1$ 与 $n(q,p)$、Morse 范畴与 $A_\infty$ 预范畴、def:8.10 梯度树模空间、$\mathcal E(q;p_1,\ldots,p_d)$、映射 $\Phi$ 与预期维数、$n(q;p_1,\ldots,p_d)$ 与 $m_d$、$A_\infty$ 关系的边界论证、图16）、8.3.2-001…007（def:8.11 预范畴、Morse(M) 为例、def:8.12 函子、def:8.13 拟等价）、8.3.3-001…014（Fukaya 范畴对象四元组、Maslov 类、自旋结构、无障碍、交点指标与穿越形式、绝对 Maslov 指标、Novikov 环、Floer 复形、伪全纯带状域与 $m_1$、$\mathbb R$ 作用与商、图17–图19）

| # | 段落 id·位置 | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|
| 1 | ch08-8.3.1-005（ch08-sec83.tex L46） | 这些线段就是从 $p$ 到 $q$ 的 $-f$ 的\emph{负}梯度流轨道。 | 这些线段就是从 $p$ 到 $q$ 的 $-f$ 的梯度流轨道。 | 误译（多字） | 原文 "the gradient flow trajectories of −f from p to q"，无"负"字；且 $-f$ 的负梯度流即 $f$ 的正梯度流，方向与 $p\to q$ 相反，与本条定义的 def:8.10(2)"$-f_e$ 的梯度流"自相矛盾。 |
| 2 | ch08-8.3.2-006（ch08-sec83.tex L240） | 在 $H^*(\mathcal A)$、$H^*(\mathcal B)$ 层次诱导等价 | 在 $H^*(\mathcal A)$、$H^*(\mathcal B)$ 层次诱导同构 | 术语/误译 | 原文 "induces an isomorphism at the level of $H^*(\mathcal A),H^*(\mathcal B)$"；"isomorphism" 应作同构（此定义的是拟等价之所以为"等价"，正是因为它在 $H^*$ 上诱导同构）。 |

块4 待确认（未改）：
- ch08-8.3.1-001（L8–17）：译文作 $f=f(p)+x_1^2+\cdots+x_k^2-x_{k+1}^2-\cdots-x_n^2$，原文只写 $f=x_1^2+\cdots$（漏常数项，Morse 引理标准写法含 $f(p)$）；译文更正确，未改。
- ch08-8.3.2-005（L218–238，def:8.12(2)）：译文加"次数为 $1-d$ 的映射"，原文只写 "maps $F_d$"（$F_d$ 次数 $1-d$ 是标准事实）；属补足。
- ch08-8.3.3-005（L279–281）：译文加"在我们考虑的情形中"（原文 "Suffice it to say that it only becomes an issue when $\dim X\ge3$"）。
- ch08-8.3.3-010（L337）：原文 "the local systems $L_1,L_2$ are trivial"（原书笔误，应为 $L_0,L_1$），译文作 $\mathcal L_0,\mathcal L_1$，正确。
- ch08-8.3.3-008（L297–325）：原文 $c_k\in(-1,0]$（pdftotext 输出），译文作 $c_k\in(-1,0)$；若容许 $c_k=0$ 则 $\Lambda_0\cap\Lambda_1\neq0$ 与横截矛盾，译文取值正确。
- ch08-8.3.3-012（L361–367）：原文 "each point $u$ coming with a sign $s(u)$"，译文作"每个点 $u$ 都带有符号 $(-1)^{s(u)}$"（与紧随其后的 $m_1$ 公式一致）。
核对要点（一致，无需改）：def:8.10 的三条标注规则、$\mathcal E$ 的乘积与 def:8.10 中 $p_i:=p_{i-1,i}$、预期维数两行推导、$\overline{\mathcal S}$ 边界分解中 $\deg r=2-i+\sum_{k=j+1}^{i+j}\deg p_k$（原文 pdftotext 作 "$p-2+\cdots$"，译文正确）、8.3.1-019 的两步谱公式、def:8.11/8.12 各条、八类对象条件与图17/18/19 图题。

## 块5：p615–624（8.3.3 后半 + 8.3.4 恒等态射与三角 $A_\infty$ 范畴）✅ 无改动
已核对：ch08-8.3.3-015…031（圆盘冒泡与有障碍 Lagrange、开 Gromov--Witten 不变量、圆盘的 Maslov 类 $\mu(u)$ 及其积分式、$\dim\mathcal M(L,J)=\tfrac12\dim_{\mathbb R}X+\mu(u)$、$\dim/\mathrm{PSL}_2$、全纯多边形模空间 $m_d$ 及其预期维数 $I(p_{0,d})+d-2-\sum_iI(p_{i-1,i})$、图20 的标记圆盘、$m_d$ 的系数式、平坦 $U(1)$ 丛 $\mathcal L_i$ 的修正（$H^u_i$、系数中 $H_d^u\circ t\circ\cdots\circ H_0^u$ 的复合次序）、预范畴与 Hamilton 形变两种处理横截性的方式、$\dim_{\mathbb R}X=2$ 时椭圆曲线情形与符号规则、图21 的符号计数 $(-1)(+1)=-1$、图22 凸角论证、$L=\mathbb R/\mathbb Z$ 的例子（$m_1([p_0])=(-q^{\int u_1^*\omega}+q^{\int u_2^*\omega})[p_1]=0$））、8.3.4-001…022（两个代数问题、$c$ 幺与严格幺、def:8.14 $A_\infty$ 模及 (8.9) 的 $d=1,2,3$ 展开、pre-homomorphism 及 (8.10)、$m_1^{\mathrm{Mod}(\mathcal A)}$ 与复合公式、$\mathrm{Mod}(\mathcal A)$ 为微分分次范畴、Yoneda 嵌入、拟表示、平移函子、映射锥、$\iota,\pi$ 与 (8.11)、正合三角形、def:8.15 三角 $A_\infty$ 范畴、def:8.16 扭曲复形）。
结论：**未作 edit**，公式与符号逐项一致（$d=2,3$ 的模关系展开、$*$ 的表达式、$\iota_1,\pi_1$ 的符号、$D^b_\infty(X)$ 为三角范畴的例子均无误）。

块5 待确认（未改）：
- ch08-8.3.3-019（L409）：译文加"不会出现边界位于某个 Lagrange 子流形上的\emph{非恒定}全纯圆盘"，原文只写 "holomorphic disks ... do not appear"；加"非恒定"更准确（常值圆盘总存在），属补足，保留。
- ch08-8.3.3-023（L459–470）：译文在句首加"此时使用复数系数的 Novikov 环。"，原文无此句，且 Novikov 环的系数仍取整数（$\mathrm{Hom}(\mathcal L_{0,p},\mathcal L_{1,p})\cong\mathbb C$ 才是复线），表述略含混；属译者补充说明，不影响公式，暂留待定。
- ch08-8.3.3-027（L506–508）：译文作"以圆周 $L$ 为边界的\emph{抽象}圆盘 $D$"，原文 "a disk $D$ bounding the circle $L$"，"抽象"为译者所加。
- ch08-8.3.3-028（L509–521）：原文写 $u\in\mathcal M(p_{0,4};p_{0,1},\ldots,p_{3,4};L_0,\ldots,L_d)$（$L_d$ 与原书此处 $d=4$ 不一致），译文作 $L_0,\ldots,L_4$，正确。
- ch08-8.3.3-030（L532–553）：原文 $L_1=\{(x,\sin(2\pi x))\}$ 未说明扰动大小即断言 $L_0\cap L_1=\{p_0,p_1\}$；译文改为 $\varepsilon\sin(2\pi x)$、$\varepsilon>0$ 充分小，并补"把 $L$ 的一个小邻域视为余切丛的零截面邻域"，数学上更严谨，保留。
- ch08-8.3.4-004（L579–581）：译文加"及本节排除圆盘冒泡的假设下"，属补足；同段末句"这里不给出细节……均假设为严格幺"系把原文 p621 开头两句并入本段，跨页合并无误。
- ch08-8.3.4-021/022（L802–806、L807–817）：译文加"必要时先加入对象的形式平移"（def:8.16 中亦加"（在需要时包括它们的形式平移）"）；原文未提，但扭曲复形构造确实需先补形式平移，属补足。

## 块6：p625–626（8.3.4 扭曲范畴结尾 + 猜想 8.17）✅ 无改动
已核对：ch08-8.3.4-023…030（扭曲对象与 $\Delta^X$ 记号、$\mathrm{Tw}(\mathcal A)$ 的态射空间、$m_d^{\mathrm{Tw}(\mathcal A)}$ 的公式（$\Delta^{X^i}$ 出现 $j_i$ 次，与原文一致）、直和与映射锥例、$S(c)\in\operatorname{Hom}^1(SY_0,Y_1)$、典范态射 $(0,\mathrm{id}_{Y_1})$ 与 $(\mathrm{id}_{Y_0},0)$ 及正合三角形、$\mathrm{Cone}(c)$ 的 $\Delta^{SX^0}$ 块、$\mathrm{Tw}(\mathcal A)=D^b(\mathcal A)$、幂等态射与分裂闭、Karoubi 完备化与 $D^\pi$、conj:8.17）。
结论：**未作 edit**（ch08-sec83.tex 至 L894 结束）。

块6 待确认（未改）：
- ch08-8.3.4-025（L849）：译文作"给定满足 $m_1^{\mathcal A}(c)=0$ 的 $c\in\operatorname{Hom}_{\mathcal A}^0(Y_0,Y_1)$"，原文只写 "given $c\in\operatorname{Hom}^0_{\mathcal A}(Y_0,Y_1)$"；加这个条件后 $\Delta=(0,0;-S(c),0)$ 才真的是扭曲复形（Maurer--Cartan 方程），属必要补足，保留。
- ch08-8.3.4-026（L869）：译文作"给定\emph{闭}态射 $c\in\operatorname{Hom}^0_{\mathrm{Tw}(\mathcal A)}((X^0,\Delta^{X^0}),(X^1,\Delta^{X^1}))$"，原文无"闭"字，同上属补足。
- ch08-8.3.4-026（L879）：译文加"其中左上块为将 $X^0$ 连同其扭曲数据一并平移所得的矩阵。"，原文无此句，为解释 $\Delta^{SX^0}$ 的注，保留。

## 块7：p626–635（8.4 引言 + 8.4.1 Tate 曲线 + 8.4.2 theta 函数乘法）— 1 处改动
已核对：ch08-8.4-intro-001…003、8.4.1-001…024（$\varphi$ 的分段线性式与 (8.12) 周期性、$\Delta$ 与图24、法扇与图25、$X_\Sigma$ 的仿射覆盖 $U_w$、$\mathbb Z$ 作用的矩阵 $\left(\begin{smallmatrix}1&d\\0&1\end{smallmatrix}\right)$ 与 $z\mapsto zq^d$、$q=0$ 纤维与 $I_d$ 型 Kodaira 纤维、形式概形 $\widehat X_\Sigma=\varprojlim X_\Sigma^k$、$\Gamma(\widehat U_w,\mathcal O)$ 的完备张量积、$\widehat{\mathcal L}$ 的构造与 $C(\Delta)$、生成元矩阵 $T$ 与 $T_n$、$\vartheta_{n,p}$ 的定义与 (8.13)(8.14) 的 $\operatorname{ord}_n$、$\widehat R=\operatorname{Proj}$ 与 Grothendieck 存在性定理）、8.4.2-001…011（$\check X(B)$ 的辛形式与 $c_1(\mathcal L)$、§6.3 的对偶哲学、$K=y^2/2$ 与 $\omega=\mathrm dy\wedge\mathrm dx$、$L_n$ 的定义与 $f(L_{n_1}\cap L_{n_2})=B(\frac1{n_2-n_1}\mathbb Z)$、$\operatorname{Ext}^i$ 的两组计算与 (8.15)(8.16)、分次的选取与指标、theta 函数乘法的逐步推导、$\deg(p_1,p_2)$ 的定义）。
结论：数学与公式逐项一致；(8.15) 非零项在次数 0、(8.16) 在次数 1，与原文一致。

改动：
1. ch08-8.4.1-015（`ch08-sec84head.tex` L125，page=630）
   原文："To do so, we choose a relatively ample line bundle $L$ on $\hat X$."
   原译："选择相对丰沛线丛。"
   改为："选择 $\widehat{\mathcal X}$ 上的相对丰沛线丛。"
   类别：漏译（丢"在 $\widehat{\mathcal X}$ 上"这一限定语；"相对丰沛"正是相对于 $\widehat{\mathcal X}\to\widehat{\mathbb A}^1$ 而言，缺了会读不懂"相对"指什么）
   理由：补回原文的所在空间限定，最小改动。

块7 待确认（未改）：
- ch08-8.4-intro-001（L6）：原文 "inspired by Abouzaid in [2] and developed in [1] which uses the Čech approach…"，译文把 "which uses the Čech approach" 直接并到"利用 Čech 方法定义导出范畴的 $A_\infty$ 结构"，未指明是 [1] 的做法；语义可通，保留。
- ch08-8.4.1-001（L17）：原文 "Pick a degree $d$ for the choice of line bundle"，译文作"选择线丛的\emph{正整数}次数 $d$"；补"正整数"符合几何情形，保留。
- ch08-8.4.1-007（L79）：原文把商写作 $\mathbb C^*/q^{\mathbb Z}$、格写作 $\langle1,\frac1{2\pi\sqrt{-1}}\log q\rangle$（都少了 $d$），译文作 $\mathbb C^*/q^{d\mathbb Z}$ 与 $\langle1,\frac d{2\pi\mathrm i}\log q\rangle$；由 $z\mapsto zq^d$ 可验证译文正确，属修正原文笔误，保留。
- ch08-8.4.1-012（L111）：译文加"即沿 $g^{-1}(0)$ 的形式完备化"，原文无，属解释，保留。
- ch08-8.4.1-021（L188–197）：译文把 "there to exist $\mathbb Z$-invariant sections" 具体化为"才能存在这种\emph{非零}不变截面；对于 $n>0$，…没有这样的非零截面"，原文未点明非零与 $n>0$，属补足，保留。
- ch08-8.4.1-022（L199–205）：原文 "for any $n\in\mathbb Z$"（$n=0$ 时 $x/n$ 无定义），译文补"$n\in\mathbb Z\setminus\{0\}$；若 $n=0$、$x=0$，则自然取 $\operatorname{ord}_0(0,y)=y$"，属必要补足，保留。
- ch08-8.4.2-006（L249–270）：译文加"其中非零项位于次数零"，原文无，属说明，且正确，保留。
- ch08-8.4.2-008（L291–293）：原文 "The $L_n$'s are straight lines in the universal cover $\mathbb R^2$ of $\check X(B)$"，而 $L_n\subset X(B)$（同段上下文），译文作"$X(B)$ 的万有覆盖"，与 $L_n$ 所在空间一致，属修正原文笔误，保留。
- ch08-8.4.2-010（L309–339）：译文新增记号 $N=n_1+n_2$、$P_\alpha=\frac{n_1p_1+n_2(p_2+\alpha d)}N$、$\alpha=s_2-s_1$ 并重排推导，原文只写展开式；逐行验算与原文各式等价（$z$ 的第一坐标即 $N(P_\alpha+s_1d)$，$q$ 的指数即 $n_1\varphi(p_1+s_1d)+n_2\varphi(p_2+s_2d)-N\varphi(P_\alpha+s_1d)$），保留。
- 图28（fig:8.28）原文在 p634 顶部、正文引用在 p633，译文把 figure 环境放在 8.4.2-005 段末，浮动位置不同，无碍。

## 块8：p636–638（8.4.2 theta 函数乘法收尾）— 1 处改动
已核对：ch08-8.4.2-012…018（$\vartheta$ 乘法的 $\alpha$ 重排与 $q^{\deg(p_1,p_2+\alpha d)}$、仿射线段解释、note:8.18 与多面体的加权平均、Fukaya 一侧的乘法 $\operatorname{Hom}_{\mathrm{Fuk}(\check X)}(L_{n_1},L_{n_1+n_2})\otimes\operatorname{Hom}_{\mathrm{Fuk}(\check X)}(L_0,L_{n_1})\to\operatorname{Hom}_{\mathrm{Fuk}(\check X)}(L_0,L_{n_1+n_2})$、三角形面积的三步计算与 (8.17) $\psi(x)=x(x-1)/2$、图29、$A(x)=\psi(x)-\varphi(x)$ 与 (8.18)、映射 (8.19) $[p]\mapsto[p]q^{-(n_2-n_1)A(p)}$、$q^{\mathrm{Area}(T)}$ 的合流与"theta 乘法与 Floer 乘法一致"、转向 Čech 描述）。
结论：公式与符号逐项一致（面积式、$A$ 的周期性、指数 $n_1A(p_1)+n_2A(p_2)+\deg-(n_1+n_2)A(P_\alpha)=\mathrm{Area}(T)$ 的抵消均无误）。

改动：
1. ch08-8.4.2-014（`ch08-sec84head.tex` L375，page=636，注 8.18）
   原文："the points of $\Delta(\frac1n\mathbb Z)$ form a basis for $H^0(\mathbb P_\Delta,\mathcal O_{\mathbb P_\Delta}(n))$."
   原译："则 $\Delta(\tfrac1n\mathbb Z)$ 的点，\emph{对应于} $H^0(\ldots)$ 的一组基。"
   改为："则 $\Delta(\tfrac1n\mathbb Z)$ 的点，\emph{构成} $H^0(\ldots)$ 的一组基。"
   类别：误译（"form a basis" 是"构成/是一组基"，不是"对应于一组基"；"对应于"把等同弱化成某种对应，读起来像另有映射）
   理由：最小替换一个动词，恢复原意。

块8 待确认（未改）：
- ch08-8.4.2-013（L369–371）：译文作"连接它们的有向区间"，原文只说 "the interval $[p_1,p_2+\alpha d]$"，"有向"为译者所加；不影响理解，保留。
- ch08-8.4.2-015（L382–412）：原文此处写 $\operatorname{Hom}_{\mathrm{Fuk}(\check X)}$，但同段又说 $L_n\subset X(B)$、下页写作 $\mathrm{Fuk}(X(B))$；译文照原文分别作 $\mathrm{Fuk}(\check X)$ 与 $\mathrm{Fuk}(X(B))$，属原文自身不一致，未改。
- ch08-8.4.2-016（L413–436）：译文加"可以在态射的\emph{上同调层面}定义映射"并把源写成 $\operatorname{Ext}^*(\ldots)$，原文写作 $\operatorname{Hom}_{D^b(\hat X)}(\ldots)$；二者在此语境等价（$\operatorname{Ext}^*=H^*\operatorname{Hom}$），属澄清，保留。
- ch08-8.4.2-017（L437–452）：原文写 "the product of $[p_1]\otimes1$ and $[p_2+\alpha d]\otimes1$"，译文作"$[p_2+\alpha d]\otimes1$ 与 $[p_1]\otimes1$ 复合"；按张量因子的顺序（$\operatorname{Hom}(L_{n_1},L_{n_1+n_2})$ 在前、对应 $[p_2+\alpha d]$）译文次序更贴合复合方向，保留。

## 块9：p638–648（8.4.3 热带 Morse 树、8.4.4 分段线性圆盘、8.4.5 Čech 计算开头）— 无改动
已核对（`ch08-sec84tail.tex` L1–L433 左右）：8.4.3-001…006 与 def:8.19（标号 $n_e$、$p_{i,i+1}\in B(\tfrac1{n_{i+1}-n_i}\mathbb Z)$、条件 (1)–(6) 含 $v_e(s)$ 的切向与 $d/ds\,v_e(s)=n_e\phi_*(\partial/\partial s)$、边长 $=(1/n_e)\log(v_e(1)/v_e(0))$）、note:8.20（$B=\mathbb R^n$ 时 $v_e(s)=v_e(0)+n_e(\phi(s)-\phi(0))$；(6) 的作用）、ex:8.21、ex:8.22 与图30/31、8.4.4-001…010（$R_e(s,t)=\sigma_{n_i}(\phi(s))-t\,v_e(s)$ 的构造与逐边/逐顶点的 $L_{n_i}$ 归属论证、$P_v$ 的边向量 $-v_{e_1},\ldots,-v_{e_p},v_{e_{\mathrm{out}}}$、加厚圆盘 $\operatorname{Fat}(S)$ 与 $R\colon\operatorname{Fat}(S)\to X(B)$、图32/33/34/35、ex:8.23 椭圆曲线情形）、8.4.5-001…003 与 thm:8.24、8.4.5-004…009（开覆盖 $\widehat U_w$、$\Gamma_w^n$、图36、(8.20)(8.21)(8.22)、限制映射的 $T_n$ 复合、Čech 复形 $C^0\to C^1$）、8.4.5-010 的 (8.23)(8.24)（五个 $m_2$ 分支逐条目核对一致）。
结论：**未发现必修错误，未作 edit**；公式与符号逐项一致。

块9 待确认（未改）：
- ch08-8.4.5-012 / def:8.25（L337–408）：原文高阶乘法的公式作 $\sum_\phi(-1)^{s(\phi)}(-1)^{\deg(\phi)}[p_{0,d}]$，译文作 $\sum_\phi(-1)^{s(\phi)}q^{\deg(\phi)}[p_{0,d}]$。按本节的 Novikov 环约定（态射为 $\Lambda_{\mathrm{nov}}$ 上的自由模、$F_1([x])=[x]q^{(n_1-n_0)A(x)}$、以及证明里"次数转化为面积"的说法），系数必须是 $q^{\deg}$ 而非 $(-1)^{\deg}$；**原文此处 "(−1)" 应为 "q" 之误**，译文正确，保留。
- ch08-ex:8.21（L323–335）：原文 "We think of $\check K$ as a function on the universal cover $\tilde B$ of $B$"，译文作"将 $\check K$ 看作 $\check B$ 的万有覆盖上的函数"。$\check K$ 定义在 $\check B$ 上、同句后半也说 $l_i$ 定义在 $\check B$ 的万有覆盖上，故译文按 $\check B$ 处理正确（原文 "B̃ of B" 疑为笔误）；保留。
- ch08-8.4.5-013（L391–393）：译文加"中需要计数的\emph{孤立}元素"（原文只写 "where $\phi$ runs over elements of $S_d^{\mathrm{trop}}(\ldots)$"）；$\mathrm{TMC}$ 的计数要求模空间零维，属澄清，保留。
- ch08-8.4.5-009（L319–336）：原文写 $\tau_i\in\{w_i,\sigma_i\mid0\le i\le d-1\}$，译文改作 $\{w_j,\sigma_j\mid0\le j\le d-1\}$（避免与左侧下标 $i$ 同名，含义不变），保留。
- ch08-8.4.4-001（L88–95）：译文用"这个并"指并集（对应原文 "this union need not be an actual holomorphic submanifold"），中文此处"这个并"读来略生硬，但意思清楚，未改。
- ch08-8.4.3-002（L15–48）：def:8.19 前的引导句译文加"注意，外部边必须收缩为一点"，由条件 (3) 立刻可得，属补足，保留。
- ch08-def:8.25 的排版：原文把 $\operatorname{Hom}$ 写成 $\oplus\to0$ / $0\to\oplus$ 的单向箭头，译文照录，"$n_2<n_1$" 时的 $\frac1{n_2-n_1}\mathbb Z$ 为负格，原文即如此，未改。

## 块10：p649–658（lem 8.27 面积公式、灌木树 T_d、def 8.29/8.31、prop 8.32、F_d 的构造与 d=1 的检验）— 无改动
已核对（`ch08-sec84tail.tex` L434–L858 左右）：lem:8.27 的 $\int_{\operatorname{Fat}(S)}R^*\omega$ 公式与其证明（凸性→标准多边形面积公式、$\widetilde L_i$ 方程 $x=-n_iy+a_i$、$a_i=\sum_{j\le i}(n_j-n_{j-1})p_{j-1,j}$、六步面积化简到 $\sum(n_j-n_{j-1})\psi(p_{j-1,j})-(n_d-n_0)\psi(p_{0,d})$）、"直接比较 $A_\infty$ 结构"的说明段、$\mathcal P$ 与 $\check{\mathcal P}$（含 $[d-1,d]$ 记作 $[0,d-1]$ 的滥用）、$\check{\mathcal P}_\epsilon$ 的胞腔与图37、四条"相交当且仅当"关系、def:8.28（灌木树与长度条件）、def:8.29（数据、条件 (1)–(6)）、note:8.30 (1)–(3)、def:8.31（$\deg\phi=\operatorname{ord}_{n_r-n_0}(\sum m_{i-1,i})$）、prop:8.32 及其归纳证明（$v_e$ 的方向、图38/39、$\operatorname{ord}$ 即竖直距离）、$\dim T_r^{\mathrm{trop}}=\deg p_{0,r}-1+\sum_i\dim\tau_{i-1,i}$、$T_d^{\mathrm{trop}}$ 与 $\operatorname{ev}\colon T_d'\to B^{\#I}$ 的构造、$F_d$ 的定义与其 $[p_{0,d}]$ 系数公式（含 $\deg p_{0,d}-1+\sum_i\dim\sigma_{i-1,i}^\vee=0$ 的条件）、$d=1$ 时 $n_1>n_0$ / $n_1<n_0$ 两种情形与 $q^{\operatorname{ord}_{n_1-n_0}(m)}[p_{0,1}]$、$s'(\phi)$ 的规定、次数一关系 $m_1^{\operatorname{TMC}(B)}\circ F_1=F_1\circ m_1^{D(\widehat X)}$ 与三情形计算、$A_\infty$ 函子关系与 $T_d^{\mathrm{trop}}$ 边界退化 (1) 的开头。
结论：**未发现必修错误，未作 edit**；公式、指标与符号逐项一致。

块10 待确认（未改）：
- ch08-8.4.5-043（L718–729）：原文列举 $(\sigma_{i-1,i})_{ε_i}^\vee$ 可能的提升时第一行写作 "$(\alpha_j-\epsilon_i,\alpha_{j+1}-\epsilon_i),\ 0\le j\le d-2$"，译文作 $0\le j<d-2$。$\check{\mathcal P}_\epsilon$ 的定义（8.4.5-025）里同族胞腔正是 $0\le i<d-2$，且 $j=d-2$ 时 $(α_{d-2}-ε,α_{d-1}-ε)$ 与紧随其后的 $(α_{d-2}-ε,α_{d-1}+ε)$ 重复，故**原文 "≤" 应为 "<"，译文修正正确**，保留。
- ch08-8.4.5-030 / def:8.29（L550–583）：原文 "$\tau_{i-1,i}\subset B$"（pdftotext 作 "("），译文作"$\tau_{i-1,i}\subsetneq B$"；开胞腔确为真子集，无碍。
- ch08-8.4.5-030 / def:8.29（L560–562）：原文 "the moduli space of continuous maps $\phi:S\to B$ from a shrub $S\in T_d$"，但该处数据用的是 $r$ 个入顶点、模空间记 $T_r^{\mathrm{trop}}$，译文作"$S\in T_r$"（按 $r$ 处理，正确；原文 $T_d$ 疑为笔误），保留。
- ch08-lem:8.27 证明（L446–453）：译文面积公式作 $\frac12\sum_{i=0}^{d}(y_ix_{i+1}-y_{i+1}x_i)$ 并补注 $(y_{d+1},x_{d+1})=(y_0,x_0)$，原文作 $\sum_{i=0}^{d-1}$（顶点只有 $0..d$）；两者等价，属澄清，保留。
- ch08-8.4.5-051（L810–829）：原文此段直接是定理 8.24 证明的一部分（无独立标题），译文加 `\begin{proof}[定理8.24的证明梗概]`；结构上更清楚，保留。
- ch08-8.4.5-045（L742–744）：原文 "For a less ad hoc solution to this problem, see [2]"，译文"关于更自然的解决办法，见\BookCite{ref002}"；"less ad hoc"→"更自然的"属合理意译，保留。

## 块11：p659–661（$A_\infty$ 函子关系的边界分析收尾、$F_2$ 关系的图解、§8.4 结束）— 无改动
已核对（`ch08-sec84tail.tex` L859–L933）：8.4.5-055…058（退化 (2) 入顶点移到胞腔边界对应第二项；(3) 入边长度趋零、相邻两条同时趋零、$m_{i-1,i}+m_{i,i+1}$ 的出现、交集为空/零维/一维三种情形分别对应 (8.24) 的后四式与第一式、$\epsilon_i<\epsilon_{i+1}$ 强制 Čech 指标次序；符号处理后 $F$ 为 $A_\infty$ 函子，定理 8.24 证毕）、8.4.5-059…062（$F_2$ 关系 (8.26) 逐项核对一致、图40 的 (1)–(6) 六种退化、$F_1(\sigma_{i-1,i},z^{m_{i-1,i}})=q^{\operatorname{ord}_{n_i-n_{i-1}}(m_{i-1,i})}[p_{i-1,i}]$ 与"左侧/右侧第一、二项/最后一项"的对应、重叠集小/大两种情形）。
结论：**未发现必修错误，未作 edit**。公式、符号 $(-1)^{\dim\sigma_{0,1}-1}$ 与图解编号逐项一致。

块11 待确认（未改）：
- ch08-8.4.5-060（L915–928）：原文 "and $[p_{i-1,i}]=F_1(\sigma_{i-1,i},m_{i-1,i})$ for $i=1,2$"，译文展开成 $F_1(\sigma_{i-1,i},z^{m_{i-1,i}})=q^{\operatorname{ord}_{n_i-n_{i-1}}(m_{i-1,i})}[p_{i-1,i}]$；这与本节 $d=1$ 情形算出的系数公式一致，属等价展开，保留。
- ch08-8.4.5-062（L932–933）：原文 "some work has to be done to ensure that the signs work, but we omit this argument"，译文"也需要一定工作来保证符号正确；这里略去这一论证"，略去了"我们略去"，意思不变，保留。

## 块12：p661–663（§8.5 Seidel 对四次 K3 曲面的结果）— 无改动
已核对（`ch08-sec85.tex` 全部，L5–L50）：8.5-001（四次曲面 $X\subset\mathbb P^3$ 与 Fubini--Study 的 Kähler 形式、镜像族 (8.27) $q(x_0^4+\cdots+x_3^4)+x_0x_1x_2x_3=0$ 与 $\Gamma_{16}$ 的商、$\Gamma_{16}$ 的显式定义与对角作用、$D^b(\widehat X_q)$ 与 $\Lambda_{\mathrm{nov}}$ 作张量积、技术差异的免责声明）、thm:8.33（$\psi\in\operatorname{Aut}(\mathbb C[[q]])$ 与 $D^\pi\operatorname{Fuk}(X)\cong\psi^*D^b(\widehat X_q)\otimes\Lambda_{\mathrm{nov}}$）、8.5-003（镜像映射与典范坐标）、8.5-004、8.5-005（分裂生成的定义）、8.5-006（Beilinson 定理 $\Omega^i(i)[i]$、$4\times16=64$ 个分裂生成元）、8.5-007（Fermat 族 4 个奇异纤维 $\times$ 16 个奇异点、消灭闭链给的 Lagrange 球面、64 个生成元、最精细的一步是算子范畴）、8.5-008（Hochschild 上同调证明单参数变形族）。
结论：**未发现必修错误，未作 edit**；公式 (8.27)、$\Gamma_{16}$ 的定义、定理编号与引用编号（thm:4.72、sec:2.2.3）均无误。

块12 待确认（未改）：
- ch08-8.5-001（L5–23）：原文只说 "The generic fiber $\widehat X_q$ is a K3 surface over the field $\mathbb C((q))$"，译文加"其一般纤维的\emph{有理双点经过保典消解}，得到……K3 曲面"。$\Gamma_{16}$ 是辛作用、商族确有有理双点，要称其一般纤维为 K3 必须先消解，故该补充在数学上是必要的澄清（与 §4.7.2 的保典消解呼应）；保留。
- ch08-8.5-006（L43–45）：原文 "instead of considering the derived category of the quotient, one can consider the $\Gamma_{16}$-equivariant derived category upstairs"，译文加"利用\emph{导出 McKay 对应}，可以用商空间保典消解的导出范畴所对应的……等变导出范畴来研究问题"；属说明该替代为何成立的补充，保留。
- ch08-8.5-007（L46–48）：原文 "the Fermat family we considered (8.27), has, over $\operatorname{Spec}\mathbb C[q]$, 4 singular fibers each with 16 singular points"，译文加"除了 $q=0$ 处的退化纤维外"；澄清必要（$q=0$ 纤维是 (8.27) 的退化纤维，不属"4 个奇异纤维"），保留。
- ch08-8.5-008（L49–50）：原文 "one can prove that there is only a one-parameter family of deformations"，译文作"在\emph{所考虑的对称性约束下}，只有一个单参数变形族"；K3 的一般变形空间是 20 维，原文此句若不加上下文约束并不成立（作者指的是这些范畴/等变设定下的变形），译文补出"在所考虑的对称性约束下"是在替原文补前提，属译者修正，保留。
- ch08-8.5-003（L34–36）：原文 "as $q$ is not a canonical coordinate for the family $\widehat X\to\operatorname{Spec}\mathbb C[[q]]$"，此处原书混用 $\widehat X$ 与 $\check X$（§8.5 的族是 $\check X$），译文统一作 $\check X$，正确，保留。
- ch08-8.5-001 的 (8.27) 与 $\Gamma_{16}$：原文 $\prod a_i=1$ 只写 $\prod a_i$，译文作 $\prod_{i=0}^3a_i=1$，明确化，无碍。

## 第8章总统计（12 块全部完成）
- 页范围：PDF 585–663（8.1–8.5）。
- 12/12 块核对完毕；块1、2、3、5、6、9、10、11、12 零改动；块4 两处、块7 一处、块8 一处。
- 改动共 4 处，分类：误译 2（`ch08-sec83.tex` L46 "负梯度流"、`ch08-sec84head.tex` L375 "对应于一组基"）、术语错 1（`ch08-sec83.tex` L240 "等价"→"同构"）、漏译 1（`ch08-sec84head.tex` L125 "相对丰沛线丛"漏"$\widehat{\mathcal X}$ 上的"）。
- 待确认项共约 40 条（各块节内分列），主要类型：译者补充必要前提/澄清（如 8.4.5-012 把原文 $(-1)^{\deg\phi}$ 改成 $q^{\deg\phi}$、ex:8.21 把 $B$ 改成 $\check B$、8.5-008 补"在所考虑的对称性约束下"）、原文自身笔误（pdftotext 掉上标、"$0\le j\le d-2$" 应为 "$<d-2$"、同段混用 $\mathrm{Fuk}(\check X)$ 与 $\mathrm{Fuk}(X(B))$）、译文把长段拆成多个 \SourceParagraph 或补 \begin{proof} 标头等结构性改动。
- 未完成项：无。
