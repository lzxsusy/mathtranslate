---
id: MS-10
zh: Hodge 结构与滤过
en: Hodge structure and filtration
aliases: [Hodge 结构, Hodge 滤过, 权 k Hodge 结构, 极化 Hodge 结构, Hodge 分解]
layer: L0
prereqs: []
sources:
  - "A 级：Cox–Katz 1999, p.96–99（PDF p.96–99，印刷 p.73–76）§5.1.1–5.1.4；§5.2 p.101–103"
  - "A 级：P. Griffiths, On the periods of certain rational integrals I, II, Ann. of Math. 90 (1969), 460–495, 496–541（书内 [Griffiths1]）"
  - "A 级：W. Schmid, Variation of Hodge structure: the singularities of the period mapping, Invent. Math. 22 (1973), 211–319（书内 [Schmid]）"
  - "B 级：本书 §5.1（节号）；Griffiths–Harris, Principles of Algebraic Geometry, Wiley 1978（书内 [GH]）"
  - "B 级：nLab 条目 Hodge structure（索引页）"
status: draft
review:
  drafter: agent-220
  reviewer: lead
  blindtest: pending
glossary_refs: ["SY01-24 术语表 #11 Hodge 菱形", "#17 Gauss–Manin 联络", "#20 Griffiths 横截性"]
symbols_refs: ["$H^{p,q}(X)$", "$F^p(X)$", "$\\mathcal F^\\bullet$", "$\\mathcal W_\\bullet$", "$H^k(X,\\mathbb Z)$"]
updated: 2026-11-20
---

# MS-10 Hodge 结构与滤过

## 1. 一句话

把复流形上同调按双次数分解连同整数格一起编码；Hodge 滤过是它的等价递减封装。

## 2. 为什么需要它

- **B 模型的全部计算建在它上面。** 前言 p.16 明言镜像 $V^\circ$ 的 B 模型「可以用 Hodge 理论来计算」；第 5 章开篇即回顾这套理论（p.96）。
- **镜像对称的第一层预言就是 Hodge 数的反射。** 先有 Hodge 分解、写出 $h^{p,q}$，才能谈 $h^{p,q}(V)=h^{3-p,q}(V^\circ)$ 与「Hodge 菱形关于 $45^\circ$ 线镜像」（p.28）。
- **它把「周期」变成可谈的对象。** 有了 $F^\bullet$ 与整数格，$F^n$ 的局部截面 $\Omega(t)$ 沿圈的积分 $y=\int_{\gamma_t}\Omega$ 才有定义，Picard–Fuchs 方程才写得出来（p.97–98；MS-06）。
- **退化处 Hodge 数不够用。** 单值性幺幂时须用极限滤过 $F_{\lim}$ 与单值性权滤过 $W_\bullet$ 拼成混合 Hodge 结构；最大幺幂单值性（p.101–102；MS-12）与 Hodge–Tate 分裂（p.103）都以它为前提。
- **镜像定理的最终形态是两个 Hodge 结构变分的同构**（p.36；MS-11、MS-18），没有本卡的对象就无法陈述。

## 3. 定义（全假设）

**3.1 设定。** $X$ 为 $n$ 维光滑复射影簇（p.96 的假设；$X$ 紧 Kähler 亦成立，但书中按射影陈述），$k\in\mathbb Z_{\ge0}$。

**3.2 Hodge 分解。** 若 $X$ 如上，则 $H^k(X,\mathbb C)\cong\bigoplus_{p+q=k}H^{p,q}(X)$，其中 $p,q\ge0$；相对于 $H^k(X,\mathbb R)$ 所确定的实结构（即 $H^k(X,\mathbb R)\otimes_{\mathbb R}\mathbb C\cong H^k(X,\mathbb C)$），有 $\overline{H^{p,q}(X)}=H^{q,p}(X)$（p.96）。

**3.3 权 $k$ 的 Hodge 结构。** 在 3.2 的数据上「再加入来自 $H^k(X,\mathbb Z)$ 的整数格」，所得对象称为权 $k$ 的 Hodge 结构（p.96 原话）。严格说法（书中未展开，见 §11）：整数格 $H_{\mathbb Z}=H^k(X,\mathbb Z)/\text{tors}$ 的像满足 $H_{\mathbb Z}\otimes\mathbb C\cong H^k(X,\mathbb C)$，且 $H^{p,q}$ 与格、实结构相容。

**3.4 Hodge 滤过。** 定义递降滤过 $F^\bullet(X)=\{F^p(X)\}_{p=0}^{n}$，$F^p(X)=\bigoplus_{a\ge p}H^{a,k-a}(X)$（$p>n$ 时 $F^p=0$；对 $k<n$，$p>k$ 时自动为 $0$）。等价性质（p.97）：
$$F^p(X)\oplus\overline{F^{k-p+1}(X)}=H^k(X,\mathbb C),\qquad H^{p,q}(X)=F^p(X)\cap\overline{F^q(X)};$$
并且 $H^{p,q}(X)\cong F^p(X)/F^{p+1}(X)$（$p+q=k$）。因此 $H^k$ 上的 Hodge 结构由整数结构与 Hodge 滤过唯一确定（p.97）——本书就用 $F^\bullet$ 代表 Hodge 结构。

**3.5 极化 Hodge 结构。** 设 $\omega$ 为 $X$ 上的 Kähler 类（$X$ 射影故存在），本原上同调 $H_0^k(X,\mathbb C)=PH^k(X)\subset H^k(X,\mathbb C)$（标准定义 $PH^k=\ker(\omega^{n-k+1}\cup\cdot)$，书中只给记号）。配对
$$Q(\alpha,\beta)=(-1)^{k(k-1)/2}\int_X\omega^{n-k}\wedge\alpha\wedge\beta ,\qquad \alpha,\beta\in H_0^k(X,\mathbb C)$$
称为极化，若满足式 (5.1)（p.97）：
$$Q(i^{p-q}\alpha,\overline\alpha)>0,\qquad 0\ne\alpha\in H_0^{p,q}(X),\ p+q=k .$$
带此数据的 $(H_{\mathbb Z},H^{p,q},Q)$ 称为极化 Hodge 结构。

**3.6 变分（衔接 MS-11）。** 设 $\pi:\mathcal X\to S$ 为相对维数 $n$ 的光滑态射，$S$ 光滑拟射影；则 $H^k(X_t,\mathbb C)$ 拼成局部自由层 $\mathcal F^0=R^k\pi_*\mathbb C\otimes\mathcal O_S$，它含局部常值层 $R^k\pi_*\mathbb C$ 并唯一确定 Gauss–Manin 联络 $\nabla(s\otimes f)=s\otimes df$；$F^p(X_t)$ 拼成局部自由子层 $\mathcal F^p$，且满足 Griffiths 横截性 $\nabla(\mathcal F^p)\subset\mathcal F^{p-1}\otimes\Omega_S^1$。数据 $(\mathcal H,\nabla,\mathcal H_{\mathbb Z},\mathcal F^\bullet)$ 称为 Hodge 结构变分（p.97）。

**3.7 混合 Hodge 结构（极限情形）。** 设 $S\subset\overline S$ 为光滑紧化、边界除子 $D$ 正规交叉、$\nabla$ 有正则奇点、单值性 $T_j$ 幺幂（必要时取覆盖）。递增滤过 $W_\bullet$（单值性权滤过，p.99 的显式公式）与 $F_{\lim}^\bullet$ 满足：$F_{\lim}^\bullet$ 在每个 $W_k/W_{k-1}$ 上诱导权 $k$ 的纯 Hodge 结构，则称 $(W_\bullet,F_{\lim}^\bullet)$ 为混合 Hodge 结构（p.99）。

## 4. 最小例子（能算出）

**椭圆曲线的 $H^1$（权 1）。** 取 $E=\mathbb C/\Lambda$，$\Lambda=\mathbb Z+\mathbb Z\tau$，$\operatorname{Im}\tau>0$。这里 $n=1$、$k=1$。

1. **Hodge 分解**：$H^1(E,\mathbb C)=\mathbb C\,dz\oplus\mathbb C\,d\bar z$，即 $H^{1,0}=\mathbb C\,dz$、$H^{0,1}=\mathbb C\,d\bar z$，故 $h^{1,0}=h^{0,1}=1$、$b_1=2$；又 $h^{1,1}=1$、$b_2=1$。
2. **滤过与维数**：$F^0=H^1(E,\mathbb C)$（$\dim 2$）$\supset F^1=H^{1,0}=\mathbb C\,dz$（$\dim 1$）$\supset F^2=0$。校验 3.4：$F^1\oplus\overline{F^{1}}=H^{1,0}\oplus H^{0,1}=H^1$（此时 $k-p+1=1$），且 $H^{1,0}=F^1\cap\overline{F^0}=F^1$。
3. **整数格决定滤过的位置**：$H_1(E,\mathbb Z)=\mathbb Z A\oplus\mathbb Z B$，$\int_A dz=1$、$\int_B dz=\tau$。在 $H^1(E,\mathbb C)$ 的对偶基下 $F^1=\mathbb C\cdot(1,\tau)\subset\mathbb C^2$；同一格、不同 $\tau$ 给出不同的（非等同的）Hodge 结构。
4. **极化**：$k=n=1$，故 $Q(\alpha,\beta)=\int_E\alpha\wedge\beta$。取 $\alpha=dz\in H^{1,0}$：由 $dz\wedge d\bar z=-2i\,dx\wedge dy$ 得
   $$Q(i\,dz,d\bar z)=i\int_E dz\wedge d\bar z=i\cdot(-2i)\operatorname{Area}(E)=2\operatorname{Area}(E)=2\operatorname{Im}\tau>0 .$$
   检验 3.5 的条件（$p=1,q=0$ 时 $i^{p-q}=i$），正性成立；对 $d\bar z$ 同理 $Q(-i\,d\bar z,dz)=2\operatorname{Im}\tau>0$。
5. **数值自检**：$h^{1,0}+h^{0,1}=2=b_1$；$\sum h^{p,q}=1+2+1=4=b_0+b_1+b_2=1+2+1$。而 $h^{1,0}=h^{0,1}=1$ 对一切椭圆曲线成立，Hodge 结构却随 $\tau$ 变——正是 §7 反例 1 的来源。

**书中同类算例（升级版）**：五次镜像 $V^\circ$（p.110–111）有 $h^{3,0}=h^{2,1}=h^{1,2}=h^{0,3}=1$，故 $\dim F^3=1$、$\dim F^2=2$、$\dim F^1=3$、$\dim F^0=4=b_3$；书中取 $\omega_j=(-1)^{j-1}\psi^j(x_1x_2x_3x_4x_5)^{j-1}\Omega_0/f^j$（$j=1,\dots,4$），并用 $\operatorname{Res}(\omega_j)\in F^{4-j}H^3(V^\circ)$（p.110）与 $\delta\omega_j=-\frac j5(\omega_j+\omega_{j+1})$（p.111）说明这 4 个留数构成 $H^3$ 的基；§5.2（p.101）再用 $h^{2,1}=1\Rightarrow h^3=4$。

## 5. 关键性质（3–6 条，带出处）

| # | 性质 | 出处（书页/文献）| 备注 |
|---|---|---|---|
| 1 | Hodge 结构 $\Leftrightarrow$（整数结构 + Hodge 滤过）；$h^{p,q}=\dim F^p/F^{p+1}$ | Cox–Katz p.97 | 书中原话「由整数结构与 Hodge 滤过唯一确定」 |
| 2 | $F^p\oplus\overline{F^{k-p+1}}=H^k$，$H^{p,q}=F^p\cap\overline{F^q}$ | p.97 | 由定义直接展开即得 |
| 3 | Kähler 类 $\omega$ 使本原上同调 $PH^k$ 成为极化 Hodge 结构，式 (5.1) | p.97；证明引 [CaK, Griffiths2] | 极化只保证在 $PH^k$ 上，$\omega$ 出现在 $Q$ 的 $\omega^{n-k}$ 中 |
| 4 | $H^{p,q}$ 不全纯变化，但 $F^p$ 拼成局部自由子层，配 Gauss–Manin 联络且 $\nabla F^p\subset F^{p-1}\otimes\Omega_S^1$ | p.97 | 这是「为什么用滤过而不用分解」的理由 |
| 5 | 单值性拟幺幂：存在 $m>0$ 使 $(T_j^m-I)^{n+1}=0$，故 $T_j$ 特征值均为单位根 | p.98（单值性定理，引 [Landman]） | 书中原文 $m>0$；与 MS-13 记的 $m\ge0$ 有出入，见 §11 |
| 6 | 极限混合 Hodge 结构：$N(W_k)\subset W_{k-2}$，$N^k:W_{n+k}/W_{n+k-1}\cong W_{n-k}/W_{n-k-1}$，$F_{\lim}$ 在 $W_k/W_{k-1}$ 上给权 $k$ 纯 Hodge 结构 | p.98–99（[Schmid]、[Griffiths2]） | $N=\log T$；MUM 时退化为 Hodge–Tate 型，$F_{\lim}^p\oplus W_{2p-1}=H^3$（p.103） |

## 6. 推导流程（D1…Dn）

- **D1（输入：Hodge 分解）**：$X$ 光滑复射影 $\Rightarrow$ 存在双次数分解 $H^k=\bigoplus_{p+q=k}H^{p,q}$ 与共轭对称 $\overline{H^{p,q}}=H^{q,p}$。依据：p.96。
- **D2（换成滤过）**：令 $F^p=\bigoplus_{a\ge p}H^{a,k-a}$（$p=0,\dots,n$），得递降 $F^0=H^k\supset F^1\supset\cdots\supset F^n\supset F^{n+1}=0$。依据：p.96–97。
- **D3（滤过还原分解）**：对 $p+q=k$，由 D2 直接展开得 $F^p\oplus\overline{F^{k-p+1}}=H^k$、$H^{p,q}=F^p\cap\overline{F^q}$、$H^{p,q}\cong F^p/F^{p+1}$；故 Hodge 结构 $\Leftrightarrow$ 整数格 $+F^\bullet$。依据：p.97。
- **D4（加极化）**：取 Kähler 类 $\omega$，令 $H_0^k=PH^k$，定义 $Q(\alpha,\beta)=(-1)^{k(k-1)/2}\int_X\omega^{n-k}\wedge\alpha\wedge\beta$，验证式 (5.1) 的正性（Hodge–Riemann 双线性关系）。依据：p.97 式 (5.1)；细节引 [CaK, Griffiths2]。
- **D5（相对化）**：光滑族 $\pi:\mathcal X\to S$ 下各 $F^p(X_t)$ 拼成局部自由子层 $\mathcal F^p\subset\mathcal F^0=R^k\pi_*\mathbb C\otimes\mathcal O_S$；局部常值层给出 $\nabla$，再验证 $\nabla(\mathcal F^p)\subset\mathcal F^{p-1}\otimes\Omega_S^1$。依据：p.97。
- **D6（退化与单值性）**：把 $S$ 补成正规交叉边界的紧化 $\overline S$，取 Deligne 典范延拓 $\overline{\mathcal F}^0$，$\nabla$ 有正则奇点；绕 $D_j$ 的解析延拓给出单值性 $T_j$；由单值性定理得 $(T_j^m-I)^{n+1}=0$，故 $T_j$ 拟幺幂、特征值为单位根。依据：p.98（[Deligne1]、[Landman]）。
- **D7（极限混合 Hodge 结构）**：令 $N_j=\log T_j$，多值平坦截面经 $\exp\!\big(-\frac1{2\pi i}\sum_j\log z_j\,N_j\big)$ 单值化后给出 $\overline{\mathcal F}^0$ 的截面；Schmid 幂零轨道定理保证 $\mathcal F^p$ 延拓为 $\overline{\mathcal F}^p$，在 $0$ 处得 $F_{\lim}^\bullet$；定义 $W_\bullet$（p.99 的 $W_0=\operatorname{im}N^n,\dots,W_{2n-1}=\ker N^n$ 等），验证 $N(W_k)\subset W_{k-2}$ 与 $N^k$ 同构，并注意 $F_{\lim}$ 在 $W_k/W_{k-1}$ 上给纯权 $k$ Hodge 结构，于是 $(W_\bullet,F_{\lim})$ 是混合 Hodge 结构；同页还得 $\overline\nabla_{\delta_j}=-\frac1{2\pi i}N_j$。依据：p.98–99（[Schmid]、[Griffiths2]）。
- **D8（接回本书主线）**：由 $h^{p,q}$ 与滤过得镜像关系 $h^{p,q}(V)=h^{3-p,q}(V^\circ)$（p.28）；在最大幺幂边界点用 $F_{\lim},W_\bullet$ 定义 MUM 与 Hodge–Tate 分裂（p.101–103，MS-12/13）。

## 7. 常见误解与反例（≥2）

1. **误解：Hodge 结构就是 Hodge 分解 $H^k=\bigoplus H^{p,q}$。** 错在漏掉实结构/共轭与整数格：若无共轭对称，$H^{p,q}$ 只是任意子空间；若无整数格，滤过可连续变形。反例：椭圆曲线族中 $h^{1,0}=h^{0,1}=1$ 始终不变，但 $F^1=\mathbb C(1,\tau)$ 随 $\tau\in\mathbb H$ 变化（§4），Hodge 数相同而 Hodge 结构（以及周期）不同。书中强调 $H^{p,q}$ 不随族全纯变化（p.97）。
2. **误解：$F^p$ 就是 $H^{p,k-p}$。** 错：$F^p=\bigoplus_{a\ge p}H^{a,k-a}$ 是多块之和，只有商 $F^p/F^{p+1}\cong H^{p,k-p}$ 等于单个双次数块。对五次镜像（§4），$\dim F^2=2$ 而 $\dim H^{2,1}=1$；把 $F^p$ 当单块会算错维数与横截性。
3. **误解：任一 Kähler 类都可让整个 $H^k$ 极化。** 错：$Q$ 含 $\omega^{n-k}$，正性只对非零 $\alpha\in H_0^{p,q}=PH^{p,q}$（本原部分）陈述（p.97）；$k<n$ 时本原条件是真实限制，$\omega^{n-k}$ 也随 $k$ 改变指数。
4. **反例：退化纤维处 $H^k$ 不再是纯 Hodge 结构。** 光滑纤维的 $H^k$ 是纯的；但在 $\overline S$ 的边界点极限对象只是混合 Hodge 结构。取 §5.1.4 的 $n=1$ 情形（椭圆曲线族 $y^2=x(x-1)(x-t)$ 在 $t\to0$ 的结点纤维处退化）：$N^2=0$、$\operatorname{rank}N=1$（Picard–Lefschetz），$b_1=2$，故 $\operatorname{im}N=\ker N$，p.99 的公式给出 $W_0=\operatorname{im}N$、$W_1=\ker N$、$W_2=H^1$，于是 $\operatorname{Gr}^W_0\cong\mathbb C$、$\operatorname{Gr}^W_1=0$、$\operatorname{Gr}^W_2\cong\mathbb C$——权重 0 与 2 各一块，不是权 1 的纯 Hodge 结构。这也说明 §3.7 的 $F_{\lim},W_\bullet$ 不是装饰。

## 8. 在文献中的坐标

| 文献 | 位置 | 它在那里干什么 |
|---|---|---|
| Cox–Katz 1999（中译本）| p.96–99 §5.1.1–5.1.4；p.101–103 §5.2；p.28（Hodge 菱形）；p.110–111 例 5.4.1；p.97 式 (5.1) | 权 $k$ Hodge 结构、$F^\bullet$、极化、VHS、退化与极限混合 Hodge 结构全套定义；后文 §5.2/§5.4 直接使用 |
| SY01-24（Siebert 讲义中译本）| ch01.tex 式 (1.95)–(1.97)（$F=F^0\supset F^1\supset F^2\supset F^3$ 与 Griffiths 横截性）；术语表 #11 Hodge 菱形、#17 Gauss–Manin 联络、#20 Griffiths 横截性 | 指标约定与本卡一致；但只对 CY 三维簇的 $H^3$ 写出 $F^k$，且用「Hodge 结构变动」。冲突：SY01-24 用「变动」、本书 p.97 用「变分」；SY01-24 只覆盖 $H^3$、本书覆盖任意 $n$ 与任意 $H^k$——术语与适用范围均不一致，待裁（见 §11） |
| SY01-25 资料卡 | 04-术语文献勘误.md §二文献表（[De] Hodge 结构在无穷远处的局部行为、[Mum]/[BL] 退化阿贝尔簇）；§三/§四不涉 Hodge | 无 Hodge 结构/滤过定义可对照（缺口，不算冲突）；其「消没圈」与本书「消失圈」用字差异属 _冲突表 T2（已裁），归 MS-14 |
| Griffiths 1969（书内 [Griffiths1]）| Ann. of Math. 90 (1969) 460–495、496–541（I、II 两部分）| 有理积分的极点阶滤过：$F^p$ 的解析来源，本书 §5.3 Griffiths–Dwork 方法（p.106–110）建立其上 |
| Schmid 1973（书内 [Schmid]）| Invent. Math. 22 (1973) 211–319（幂零轨道定理）| 本书 p.99 用它把 $\mathcal F^p$ 延拓为 $F_{\lim}^p$，从而定义极限混合 Hodge 结构 |

注：书内页码一律为 PDF 物理页（$=\backslash$SourcePage$\{N\}$，印刷页 $+23$）；外部文献用原书页码。

## 9. 前置与后继

- 前置：无（L0 起点）。可选背景：MS-07 环面簇 / MS-03 五次三维簇（§4 例子用到的几何）。
- 后继：MS-11（Hodge 结构变分：$\mathcal F^p$ 相对化、Gauss–Manin 联络、Griffiths 横截性，见 §3.6/§5 第 4 条）；MS-06（Picard–Fuchs：周期是 $F^n$ 截面沿圈的积分，p.97–98）。
- 后继：MS-12（最大幺幂单值性）、MS-13（单值性定理与极限混合 Hodge 结构）、MS-14（消失圈）——都用本卡 §5 第 5–6 条与 §3.7。
- 后继：MS-18（Frobenius 流形与 Dubrovin 联络需要极化 Hodge 结构 + Griffiths 横截性）；MS-01/MS-03（镜像对称的 Hodge 数反射，p.28）。

## 10. 形式化接口（Lean 可 sorry）

```lean
import Mathlib.LinearAlgebra.FiniteDimensional
import Mathlib.Analysis.Complex.Basic

universe u

/-- 权 k 的 Hodge 滤过（Cox–Katz p.96–97）：递减 F^0 = V ⊇ F^1 ⊇ ⋯ ⊇ F^{k+1} = ⊥。 -/
structure HodgeFiltration (V : Type u) [AddCommGroup V] [Module ℂ V] (k : ℕ) where
  F : ℕ → Submodule ℂ V
  antitone : ∀ p, F (p + 1) ≤ F p
  top : F 0 = ⊤
  bot : F (k + 1) = ⊥

/-- 权 k 的 Hodge 结构：复向量空间、实结构、整数格与 Hodge 滤过（p.96–97）。 -/
structure HodgeStructure (k : ℕ) where
  V : Type u
  [addCommGroup : AddCommGroup V]
  [module : Module ℂ V]
  [finiteDimensional : FiniteDimensional ℂ V]
  filt : HodgeFiltration V k
  realForm : Submodule ℝ V
  integralLattice : AddSubgroup V

namespace HodgeStructure

variable {k : ℕ} (H : HodgeStructure k)

/-- H^{p,q} := F^p ∩ \overline{F^q}（p + q = k，书 p.97）。共轭像需实结构，细节留 sorry。 -/
def hodgePiece (p q : ℕ) (hpq : p + q = k) : Submodule ℂ H.V := by sorry

/-- 书 p.97：H^{p,q} ≅ F^p/F^{p+1}，故 Hodge 数是滤过的跳跃。 -/
theorem hodgePiece_finrank (p q : ℕ) (hpq : p + q = k) :
    Module.finrank ℂ ↥(H.hodgePiece p q hpq) =
      Module.finrank ℂ ↥(H.filt.F p) - Module.finrank ℂ ↥(H.filt.F (p + 1)) := by
  sorry

/-- 书 p.97：整数结构 + Hodge 滤过唯一确定 Hodge 结构。 -/
theorem determined_by_lattice_and_filtration (H₁ H₂ : HodgeStructure k)
    (hF : H₁.filt = H₂.filt) (hZ : H₁.integralLattice = H₂.integralLattice)
    (hR : H₁.realForm = H₂.realForm) : H₁ = H₂ := by sorry

end HodgeStructure

/-- 极化（p.97 式 (5.1)）：Q(i^{p-q} α, \bar α) > 0，0 ≠ α ∈ H_0^{p,q}。 -/
def IsPolarized {k : ℕ} (H : HodgeStructure k) (Q : H.V → H.V → ℝ) : Prop :=
  ∀ (p q : ℕ) (hpq : p + q = k) (x : ↥(H.hodgePiece p q hpq)), x ≠ 0 →
    Q (Complex.I ^ ((p : ℤ) - q) • (x : H.V)) (x : H.V) > 0

/-- 极限混合 Hodge 结构（p.99）：W_• 递增、F_lim^• 递减，F_lim 在 Gr^W_k 上给纯权 k。 -/
structure MixedHodgeStructure where
  V : Type u
  [addCommGroup : AddCommGroup V]
  [module : Module ℂ V]
  W : ℕ → Submodule ℂ V
  F : ℕ → Submodule ℂ V
  W_monotone : Monotone W
  F_antitone : ∀ p, F (p + 1) ≤ F p
  graded_pure : ∀ k, True  -- 占位：F 在 W_k/W_{k-1} 上诱导权 k 的纯 Hodge 结构

/-- 定理（p.98–99，[Schmid]）：T 幺幂、N = log T 幂零时，(W_•, F_lim) 是混合 Hodge 结构。 -/
theorem limit_mixed_hodge (V : Type u) [AddCommGroup V] [Module ℂ V] (n : ℕ)
    (N : V →ₗ[ℂ] V) (hN : N ^ (n + 1) = 0) :
    ∃ (W F : ℕ → Submodule ℂ V), True := by sorry
```

## 11. 待核清单

- [ ] 冲突（§8 第 2 行）：SY01-24 用「Hodge 结构变动」且 $F^k$ 只对 CY3 的 $H^3$ 定义（式 1.95–1.97）；本书 p.97 用「Hodge 结构变分」且对任意 $n$、任意 $H^k$ 定义 $F^p$。术语与适用范围不一致，待裁并同步 _冲突表.md（本卡不改既有文件，建议编号 T7；涉及 MS-11）。
- [ ] **缺口**：SY01-24 术语表 70 条无「Hodge 结构」「Hodge 滤过」条目，MS-10 无可直接对照的词条；是否补词条待定（不算冲突）。
- [ ] **整数格严格化**：书 p.96 只说「加入来自 $H^k(X,\mathbb Z)$ 的整数格」，未写 $H^k(X,\mathbb Z)\otimes\mathbb C\cong H^k(X,\mathbb C)$ 与格的饱和性（§3.3 的补全依据待核，B 级 [GH]）。
- [ ] **极化定义域**：书 p.97 只对本原上同调 $H_0^k=PH^k$ 陈述式 (5.1)，非本原部分（Lefschetz 分解）未展开；所引 [CaK, Griffiths2] 的定理号待查。
- [ ] **$m$ 的正负**：书 p.98 单值性定理原文为「对某个整数 $m>0$，$(T_j^m-I)^{n+1}=0$」；MS-13 队列记「应为 $m\ge0$（原译笔误）」——本卡按书中原文陈述，待裁（不属 SY01-24/25 冲突）。
- [ ] **§4 椭圆曲线例**：书中无此例，$h^{1,0}=1$、$h^{1,1}=1$、周期 $(1,\tau)$ 为标准事实，本卡自算并逐项校验；[GH] 具体页码待补（B 级 → 待升 A）。
- [ ] **交叉引用**：_冲突表 T1（单值变换→单值性）与 T2（消失循环→消失圈）已裁，分别属 MS-12/MS-14；本卡只用「单值性」，不重复计数。
- **核验（2026-11-20）**：本卡经 `_核验记录.md` 核验，修正 1 处（详见该文件 ✗ 清单与证据链接）；其余待核条目保留。
