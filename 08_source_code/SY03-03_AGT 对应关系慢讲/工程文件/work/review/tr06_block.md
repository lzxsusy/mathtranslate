# tr-06 块交叉校对报告（原文 pp.77–89，tag 7.16–7.21 + 8.1–8.10）

校对者：tr-04　　日期：2026-11-03　　被校对文件：`work/src/chunks/tr06a.tex`(pp.77–80)、`tr06b.tex`(pp.81–84)、`tr06c.tex`(pp.85–89)

方法：tag 与 `work/tags_bypage.txt` 逐条对齐；公式逐符号对 200 dpi 整页图 + 300–900 dpi 局部放大
（裁剪脚本 `work/tmp/crop_tr04.py`，坐标为 PDF 点，整页 595×842）；正文用 `work/split/p077–p089.txt`
只作段落定位（数学不可信），凡涉及符号一律看图像。

---

## 一、必须改（4 项）

### M1. tr06a L11：质量参数个数的等式抄错（漏了一个 `-1` 的位置）

现文：
```
该穿刺点有 $n_1+\cdots+n_{\ell-1}=N_1-1$ 个质量参数。
```
原文（p.77 第 1 段，放大 700 dpi 复核）：
> The puncture has $n_1+\cdots+n_\ell-1 = N_1-1$ mass parameters.

即 **∑_{k=1}^{ℓ} n_k − 1 = N_1 − 1**，不是 $n_1+\cdots+n_{\ell-1}$。

判断依据（三重）：
1. 图像：p.77 该句裁图（`crop 77 60 168 545 190`，800 dpi）清楚显示 `n₁+⋯+n_ℓ −1 = N₁−1`；
   PDF 文字层把 `n_ℓ − 1` 误抽成 `nℓ−1`（当成了下标 ℓ−1），tr-06 跟着文字层错了。
2. 自洽性：(7.16) 的味对称群是 $[\prod_{k=1}^{\ell}U(n_k)]/U(1)_{\rm diag}$，其秩为 $\sum_k n_k-1$；
   而 tr05c 已推出 $N_1=\sum_{k=1}^{\ell} n_k$（p.76 的递推 $N_j-N_{j-1}=n_j+\cdots+n_\ell$，$N_0=0$），
   故质量参数个数 $=\sum_k n_k-1=N_1-1$，与原文完全一致。
3. 极端情形：满穿刺点 $Y=1^N$ 时 $\ell=1$、$n_1=N$，原文写法给 $N-1$ ✓（现文的写法给 $0$ ✗）。

建议改成（其余不动）：
```
该穿刺点有 $n_1+\cdots+n_\ell-1=N_1-1$ 个质量参数。
```

### M2. tr06a L9：同一条 Tutor Note 建立在 M1 的误读上，应删除或改写

该批注主张"原文疑为 $n_1+\cdots+n_\ell-1$ 之误"，并给出"两组极端情形可判"的论证。
实际上**原文本来就写对了**，是文字层抽取出错；批注的"满穿刺点给 0（错）"之说也就不成立
（按原文 $Y=1^N$：$\sum n_k-1=N-1$ ✓）。**这条批注必须删掉**，否则会把一个不存在的"原文笔误"写进译注汇总。

若要保留一条有价值的批注，建议替换为（已验证）：
```latex
% [Tutor Note: p.77 质量参数计数核对：由 p.76 的递推 $N_j-N_{j-1}=n_j+\cdots+n_\ell$（$N_0=0$）得 $N_1=\sum_{k=1}^\ell n_k$；而 (7.16) 的群 $[\prod_k U(n_k)]/U(1)_{\mathrm{diag}}$ 的秩为 $\sum_k n_k-1$。故质量参数个数为 $\sum_k n_k-1=N_1-1$，与原文 $n_1+\cdots+n_\ell-1=N_1-1$ 一致。用满穿刺点 $Y=1^N$（$\ell=1,n_1=N$）可作锚点：给 $N-1$ 个质量参数，正是 $SU(N)$ 味道对称性的秩。]
```

### M3. tr06a L53：`simply-laced` 误译为"单连通"（物理含义完全不同）

现文：
```
\para{非单连通的规范群。} 把 $\cX(\fg)$ 在圆周上约化给出规范代数 $\fg$ 的 5d $\cN=2$ SYM，
而 $\fg$ 是单连通的。非单连通的规范群通过扭（twisting）来实现，……
```
原文（p.78 末段）：
> **Non-simply-laced gauge groups.** Reducing X(g) on a circle yields 5d N=2 SYM with gauge
> algebra g, which is **simply-laced**. Non-simply-laced gauge groups are achieved by twisting, …

`simply-laced` = 单链（各根等长，ADE 型），与 `simply-connected`（单连通，$\pi_1=1$）是两回事；
且原文"……给出规范代数 $\fg$ 的 5d SYM，而 $\fg$ 是单链的（即规范代数总是 ADE 型）"这一因果，
正是下文"用外自同构（扭）把单链代数变成非单链（B_n/C_n/F_4/G_2）"的前提——译成"单连通"后逻辑断裂。

建议改成：
```
\para{非单链的规范群。} 把 $\cX(\fg)$ 在圆周上约化给出规范代数 $\fg$ 的 5d $\cN=2$ SYM，
而 $\fg$ 是单链的（simply-laced）。非单链的规范群通过扭（twisting）来实现，……
```

### M4. 术语不统一：`味道` → `味`（tr06 共 11 处；另发现 tr02c 也有 7 处）

全书的**主流约定是"味对称性 / 味对称群"**（"味对称" 共 43 处：c01 13、tr02a 11、tr02b 9、tr02c 5、
tr03a 8、tr03b 3、tr04a 1、tr04b 3、tr05c 8、tr07b 7）；用"味道"的是 tr-06（11 处）与 tr02c（7 处）。

| 文件 | 行 | 处数 |
|---|---|---|
| tr06a | L4, L11, L15(2), L36, L80, L86 | 7 |
| tr06b | L9, L85 | 2 |
| tr06c | L80, L113（批注内） | 2 |

建议 tr06 全局替换 `味道` → `味`（"味道对称群"→"味对称群"、"味道对称性"→"味对称性"）。
注意 tr06b L9 的"$N_f=4$ 个味道"应改成"$N_f=4$ 个味"（与 tr-02/tr-03/tr-04 的"味"一致）。
※ tr02c 的 7 处属于 tr-02 的块，请 Lead 一并转告（我未改任何他人文件）。

---

## 二、可选改（4 项）

### O1. tr06a L86、L89：`$\cT_2$` 应为 `$T_2$`（符号保真）

原文 p.80 的图注与正文都是**普通斜体** $T_2$（见 p.80 图注 "into $T_2$ and $X_p$ building blocks"、
正文 "the trifundamental half-hypermultiplet $T_2$"，以及 fig5.png 图内标签 "T₂"），
tr-06 用了花体 `\cT_2`。建议改回 `$T_2$`（两处：图注 + 正文）。

### O2. (8.8)/(8.10) 的 TikZ 与原文图的细节差异（结构忠实，仅外观）

- **(8.8)（p.88）**：原图是**一个**虚线圆角框，框内 4d/2d 之间用**一条水平虚线**分隔；
  tr-06 画成上下两个独立虚线框（中间有 ~0.04 cm 缝）。另外原图的 $K$ 结点接近圆（宽高比约 1.2:1），
  tr-06 画成 `ellipse (0.295 and 0.155)`（≈1.9:1）偏扁。
  核对无误的部分：方框 2 — 圆 2 — 方框 2 的水平链、两条斜线、**两条跨线小弧**（原图确实有两条）、
  4d/2d 标签位置、无箭头。→ 建议把"两个框"改成"一个框 + 中间水平虚线"，$K$ 改成圆形。
- **(8.10)（p.89）**：原图的 4d/2d 界面是**一条竖直虚线，上下两端各带一小段弧**；
  tr-06 用两条贯穿全高的对合曲线（更像 (8.8) 的交叉记号）。其余（单个虚线框、4d/2d 标签、
  结点 N / K_{n−1} / ⋯ / K_1、三支箭头一律指向左侧、$N$ 与 $K$ 均为胶囊形 rounded rectangle）全部忠实。
- 两图均只用 TikZ core 语法（`arc[start angle=…]`、`.. controls ..`、`++`、`ellipse`、`rounded corners`），
  不依赖 `positioning/calc` 等库，与当前 preamble 的 `\usepackage{tikz}` 兼容 ✓。

### O3. p.82 灰框（keybox）的位置

原文的 "Main examples of gauge theory and CFT operators" 灰框是**嵌在段中间、文字环绕**的侧栏
（句子被它切成 "…an orbifold group that must ／框／ respect orientation…"）。tr06b 把整句合并、
把 keybox 作为独立块放在该段之后——内容完整、阅读顺，是合理的 LaTeX 化处理，**无需一定改**；
若想还原环绕效果需 `wrapfig` 之类（不建议为此改 preamble）。同样，(8.8) 的 `K` 结点与 (8.6) 的
tag 位置等都属可接受的版式近似。

### O4. "扭线 / 扭算子" 与全书 "扭曲" 的用词

tr06a 用"扭线（twist lines）"（2 处 + 1 处英文括注）、tr06b 用"扭算子"（1 处，p.82 "punctures and
twist operators"），而 tr05b 用"外自同构扭曲算子"、§3 全篇用"部分拓扑扭曲"。建议统一为
**"扭曲线 / 扭曲算子"**（保留"扭（twisting）"作为动词），或由 Lead 决定后写进 glossary，二者择一。

### O5. 段落切分（跨页句，非错误，供决策）

- p.79→p.80：原文一句 "…can be constructed by gauging SU(2) flavour symmetries **of the
  trifundamental half-hypermultiplet** $T_2$ … and of theories $X_p$ …" 被图 5 隔开。tr-06 在
  "…就可以通过规范化 $SU(2)$ 味道对称性来构造" 处断段，下一段以"三基本半超多重态…"开头，
  中文读来略突兀。可照我块里 Figure 3 的做法：把整句并在同一段，图放到该段之后。
- p.76→p.77 边界：tr05c 末句"特别地 $N_\ell=N$。"与 tr06a 的"味道对称群为 (7.16)"在原文是**同一段**，
  现在因 tr05c 末尾的空行被切成两段（跨文件段落切分）。属 tr05c 侧的行尾空行，内容无缝、无重复，
  只影响版式；若 Lead 在意，让 tr-05 把最后的 Tutor Note 前的空行去掉即可。

---

## 三、已核对无误（逐项）

### 3.1 tag 完整性（与 `tags_bypage.txt` p.77–p.89 完全一致）

| 页 | tags_bypage | tr06 位置 | 状态 |
|---|---|---|---|
| p.77 | 7.16, 7.17 | tr06a L5–8 / L22–25 | ✓ |
| p.78 | 7.18 | tr06a L32–35 | ✓ |
| p.79 | 4.2（引用）, 7.19 | tr06a L68 引用 / L69–74 | ✓（4.2 是行文引用，未误当新公式） |
| p.80 | （无） | — | ✓ |
| p.81 | 7.20, 7.21 | tr06b L5–8 / L20–25 | ✓ |
| p.82 | （无） | — | ✓ |
| p.83 | 8.1 | tr06b L57–61 | ✓ |
| p.84 | 8.2 | tr06b L73–77 | ✓ |
| p.85 | 8.3, 8.4, 8.5 | tr06c L5–8 / L15–23 / L27–31 | ✓ |
| p.86 | 8.5（引用） | tr06c L39 引用 | ✓ |
| p.87 | 8.6, 8.7 | tr06c L54–62 / L70–74 | ✓ |
| p.88 | 8.8, 8.9 | tr06c L81–112 / L116–119 | ✓ |
| p.89 | 8.10 | tr06c L131–158 | ✓ |

合计 **16 条**（7.16–7.21 六条 + 8.1–8.10 十条），无缺、无重、无跳、无自造编号。

### 3.2 公式逐符号抽查（16 条，全部与图像一致）

| 式 | 页 | 核对要点 | 结果 |
|---|---|---|---|
| (7.16) | 77 | $[\prod_{k=1}^{\ell}U(n_k)]/U(1)_{\rm diag}$，U 不是 SU | ✓ |
| **(7.17)** | 77 | 双 underbrace：左 brace 覆盖 $\alpha_{(1)},\cdots,\alpha_{(1)}$ 标 $l_1$，右 brace 覆盖 $\alpha_{(r)},\cdots,\alpha_{(r)}$ 标 $l_r$；块内与块间都用居中 $\cdots$；括号内下标是**圆括号** $\alpha_{(k)}$（不是 $\alpha_k$）；外层圆括号 | ✓ 完全一致 |
| (7.18) | 78 | $\alpha=(b+1/b)\rho_Y+m_Y$ | ✓ |
| **(7.19)** | 79 | $\varphi(z)$（**卷曲 varphi**）$\sim(\frac{\diag(m,-m)}{z-z_i}+O(1))\dd z$；$\Longrightarrow$ 双线箭头；右端 $\phi_2(z)$（**直杆 phi**）$=(\frac{m^2}{(z-z_i)^2}+O(\frac{1}{z-z_i}))\dd z^2$ — 900 dpi 放大确认两端用**不同的 phi 字形**，tr06 的 `\varphi` / `\phi_2` 选择正确 | ✓ |
| (7.20) | 81 | 分子三项 $\frac{q}{z}m_1^2,\frac{q(q-1)}{z-q}m_2^2,\frac{z-q}{z-1}m_3^2$ + $zm_4^2-u$；分母 $z(z-q)(z-1)$ | ✓ |
| (7.21) | 81 | $\sum_{k=n-1}^{2n-2}\frac{\Lambda_k}{z^{k+2}}$；$\stackrel{r\to\infty}{\simeq}$；结尾 $+\cdots$ 与 $+\ldots.$ 用法与原文一致 | ✓ |
| (8.1) | 83 | $\propto\frac{\langle W_k\hat V_{\mu_1}\ldots\hat V_{\mu_n}\rangle}{\langle\hat V_{\mu_1}\ldots\hat V_{\mu_n}\rangle}$，$\text{as }\epsilon_1,\epsilon_2\to0$ | ✓ |
| (8.2) | 84 | $\frac{\widehat{\fsu}(N)_k\times\widehat{\fsu}(N)_M}{\widehat{\fsu}(N)_{k+M}}\times\frac{\widehat{\fsu}(M)_N}{\widehat{\fu}(1)_{M-1}}$，$k=-N-\frac{Mb^2}{1+b^2}$ | ✓ |
| (8.3) | 85 | $W_{\gamma,R}=\Tr_R(\mathrm{Pexp}\int_L(A_\gamma+\mathrm{scalars}_\gamma))$ | ✓ |
| **(8.4)** | 85 | 三行 $\mathsf{aligned}$：① $\int\dd a\,\Tr_R(e^{a_\gamma})Z_{\rm cl}(a,q,\bar q)Z_{\rm one-loop}(a)Z_{\rm inst}(a,q)Z_{\rm inst}(a,\bar q)$ ② $\int\dd\alpha\,f(\alpha)C(\alpha)\cF(\alpha,q)\cF(\alpha,\bar q)$ ③ $\langle\hat V_{\mu_1}\ldots\hat V_{\mu_n}\cL_\gamma\rangle^{\rm Toda(\fg)}_C$；上标 $\mathsf{T}(\fg,C,D)$、下标 $S^4_b$ | ✓ |
| (8.5) | 85 | $\int\dd\alpha\,C(\alpha)\cF(\alpha,q)\sum_h\cL_\gamma(\alpha,\alpha+h)\cF(\alpha+h,\bar q)$ | ✓ |
| **(8.6)** | 87 | 四行：$b^2(y_1^2+y_2^2)+b^{-2}(y_3^2+y_4^2)$ 的指数字号；$S^2_b$ 用 $b^{-2}$、$S^2_{1/b}$ 用 $b^{2}$（**不可对调**）；$T^2_{\theta,\varphi}$ 中 $(rb^{-1}\sin\theta\cos\varphi)^2$ 与 $(rb\sin\theta\sin\varphi)^2$ | ✓ 全部一致 |
| (8.7) | 87 | LHS $\langle\text{surface operator}\rangle$；RHS $V_{-b^{\pm1}\Omega_R}$ | ✓ |
| **(8.8)** | 88 | LHS $Z_{S^2_b\subset S^4_b}[\,\text{图}\,]$；RHS $\langle\hat V_{\mu_1}\hat V_{\mu_2}\hat V_{\mu_3}\hat V_{\mu_4}V_{-Kb/2}\rangle^{\rm Liouville}_{S^2}$；图示见 O2 | ✓（图见 O2 的细节偏差） |
| (8.9) | 88 | $\log Z_{\rm inst,vort}=\frac{F}{\epsilon_1\epsilon_2}+\frac{\cW}{\epsilon_1}+O(1)$ | ✓ |
| **(8.10)** | 89 | LHS $Z_{S^2_b\subset S^4_b}[\,N\ K_{n-1}\ \cdots\ K_1\ 4d\,2d\,]$；RHS $\langle\hat V_{\mu_1}\ldots\hat V_{\mu_4}\rangle^{\rm generalization\ of\ Toda\ CFT}_{S^2}$；$K_i=N_1+\cdots+N_i$ | ✓（界面记号见 O2） |

### 3.3 图、框、习题、脚注

- **Figure 4（p.79）**：`\includegraphics[width=0.95\textwidth]{fig4.png}` + `\figtitle{4}{…}`，位置在 p.79 页首 ✓；
  图注逐句对译（"带分支割线"/"双重覆盖"/"对 $N=2$"）✓。资产核验：fig4.png 2323×684，内容边界
  rows 106–614、cols 108–2199，四边均未触边 → 无截断、无图注残影 ✓。
- **Figure 5（p.80）**：`width=0.7\textwidth` ✓，位置 p.80 页首 ✓，图注与原文三句一一对应 ✓。
  资产核验：fig5.png 1106×418，内容 rows 94–413、cols 87–1074，未触边 ✓。
- **§8 要点框**：`keybox` 标题"规范理论与 CFT 算子的主要例子"，两条要点逐句对译（余维 2 / 余维 4）✓；
  位置见 O3。
- **Exercise 7.1**：`\begin{exercise}{7.1}` ✓，三步与原文逐句对应（含 $\Lambda=q(m_1+m_2)$、$\Lambda'^2=\Lambda(m_1-m_2)$、
  $\tilde z=z(m_3+m_4)$、$\tilde x=x/(m_3+m_4)$、$z\to z\Lambda^2$、$z^2x^2=u+\Lambda^2(z+1/z)$、$\lambda=x\dd z$）✓。
- **脚注 59–66（8 条，全部到位、内容对得上）**：
  59 "欢迎帮助补全参考文献"（tr06a L41）／60 "扭 vs 部分拓扑扭曲"（L53）／61 "数值系数依赖约定"（tr06b L56）／
  62 "自旋 $l$ 的流 $\tilde W_l$ 是 $W_k$ 的多项式"（L64）／63 "权在 $\fh^*$ 中，用 Killing 形式等同"（tr06c L12）／
  64 "退化算子融合只有有限多项"（L32）／65 "动量 $p\sim\ii\partial_x$ 类比"（L44）／66 "最一般 class S 情形有待澄清"（L78）。
  另：tr06b L29 指出原文把 correspondence 误拼为 "corespondence"，核对文字层属实 ✓（这是**原文**笔误，批注记录得当）。

### 3.4 漏译与边界

- 逐段对照 p077–p089 文字层：**未发现漏段、漏句、漏脚注**。§7.3、§8、8.1–8.4 的标题与全部
  `\para` 行内小标题（Quiver tails and punctures / Partially degenerate vertex operators /
  Punctures: nilpotent orbits, Nahm, Hitchin, and Toda / Non-simply-laced gauge groups /
  Wild punctures from collisions / Examples of theories with wild punctures / CFT side /
  Wild punctures and AD theories / Further directions / Coulomb branch operators / Orbifold C²/Z_M /
  Wilson loop operators / Dyonic loop operators / Algebra of line operators / Vortex string operators /
  Description as a 4d-2d coupled system / Gukov–Witten operators / Symmetry-breaking wall）
  全部有对应译文 ✓。
- **p.77 起点**：tr05c 末尾"特别地 $N_\ell=N$。" + tr06a 的"味道对称群为"(7.16) —— 无缝、无重复、无缺口 ✓
  （唯一的瑕疵是段落被跨文件切开，见 O5）。
- **p.89 终点**：tr06c 末句"……在 CFT 一侧，情形与圈算子类似，并且"与原文 p.89 末行
  "On the CFT side the situation is similar to loop operators, and one" 完全对应，**保持未完**，
  未越界写到 p.90 ✓（tr-07 从 "one ..." 收尾）。
- 跨页断句 4 处（p.78→79、p.79→80、p.84→85、p.88→89）均按"开始者写完"处理，接续正确
  （p.84→85 的 "codimension 4 operators / of X(g) should depend…" 横跨 tr06b→tr06c，两文件首尾对齐 ✓）。
- 每页 `% [原文 p.N]` 齐备（p.77–p.89 共 13 页）✓。

### 3.5 结构与术语

- 三文件 brace 平衡、`$` 成对、`\begin/\end` 配对、`\left/\right` 配对（脚本逐行检查，全部 OK）；
  UTF-8 无 BOM、LF、无 U+FFFD ✓。
- "非正规（irregular）算子/态"与 c00、c01、tr08b（BMT 条）一致 ✓（全书统一用"非正规"，不必改）。
- 与 glossary 一致：穿刺点 / 箭图 / 驯服、野生穿刺 / 面算子 / 圈算子 / 畴壁 / 预势 / 共形块 /
  退化主算子 / tinkertoy / 类时 Liouville / 小弦理论 / 反常 8-形式 ✓。
- 数学记号与原文一致：$\mathfrak{A}_{\epsilon_1,\epsilon_2}$（哥特 A）、$\mathsf{T}(\fg,C,D)$（无衬线 T）、
  $\cX(\fg)$、$\fsu/\fso/\fu$、$\widehat{\fsu}(N)_k$、$(\exp(2\pi\ii/M),\exp(-2\pi\ii/M))$、
  $y^5$（p.86 原文就是**上标** 5，tr-06 未"顺手改成" $y_5$，正确）✓。

---

## 四、复现用的裁剪命令（如需复核）

```powershell
$py="<本地路径>"
$w="<本地路径>"
& $py "$w\tmp\crop_tr04.py" 77 60 168 545 190 "$w\tmp\rv_p77_n1.png" 800     # 「n_1+…+n_ℓ−1=N_1−1」原句
& $py "$w\tmp\crop_tr04.py" 77 100 555 545 600 "$w\tmp\rv_p77_717.png" 700    # (7.17) 双 underbrace
& $py "$w\tmp\crop_tr04.py" 79 90 468 500 500 "$w\tmp\rv_p79_719.png" 900      # (7.19) varphi / phi_2 字形
& $py "$w\tmp\crop_tr04.py" 88 170 320 460 375 "$w\tmp\rv_p88_88.png" 600      # (8.8) 图
& $py "$w\tmp\crop_tr04.py" 89 145 296 470 326 "$w\tmp\rv_p89_810.png" 800     # (8.10) 图
& $py "$w\tmp\crop_tr04.py" 86 100 235 545 272 "$w\tmp\rv_p86_y5.png" 700      # latitudes $y^5$
```

## 五、结论

tr-06 块的**大局是可靠的**：16 条编号公式一条不缺、所属页与 tags_bypage 完全吻合，全部公式
（含两条 TikZ 示意图）逐符号抽查无一处抄写错误，图/框/习题/脚注/边界/漏译都过关。

需要动手的只有 4 件事，其中 **M1（漏 `-1` 的位置）与 M3（simply-laced ≠ 单连通）是真正的内容错误**，
M2 是随之而来的错误批注（务必删），M4 是全书术语统一（机械替换即可）。
可选改的 4 项都是版式/记号层面的打磨，不做也不影响正确性。

---

## 附（不属于 tr-06 范围，但顺手发现，请 Lead 留意）

`work/figures/fig3.png` 在 10:16:27 被再次替换（38585 B，1501×807，不是我 10:14 交的 1356×673 版本）。
当前版本有两个问题（像素级核验）：
1. **底部仍含图注文字残影**：内容行 54–806（高 807），最后 ~15 行是原图注
   "…construction of a U(4)×U(4)×U(3) gauge theory. Th…" 的半截字，会印在图下方；
2. **左右被切**：内容列 0–1500（宽 1501），最左/最右的两条 NS5 竖线正好压在裁剪边界上（各被切掉一半）。

我在 10:14 交的干净版仍在 `work/tmp/fig3_new.png`（1356×673，四边留白 23–26 px，无图注残影，
只含 NS5/D4/D6/⊗/Λ₁–Λ₃ 与膜线），可直接覆盖使用；重裁命令：
```powershell
& $py "$w\tmp\crop_tr04.py" 56 177 100 421 221 "$w\figures\fig3.png" 400
```
（p.56，PDF 点坐标；内容 bbox 由绘图+字形联合求得以避开展示文字。）
