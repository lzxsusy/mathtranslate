# Faddeev 指标

> `grassmann/concept/faddeev-index` · 轨道 6 · 曲线上层的算术 · 状态 draft

> **先自测**：为什么「Faddeev 指标等于 2」可以翻译成扭曲模空间上的一个有理点？

## 一句话

把 Brauer 类沿 Br(K)-平移后取最小指标；Faddeev 指标 2 恰好等价于某个秩 2 扭曲模空间有有理点。

## 定义

给定域扩张 $L/K$ 与 Brauer 类 $\alpha\in\operatorname{Br}(L)$，$\alpha$ 的 **Faddeev 指标**（Faddeev index）为
$$\operatorname{ind}_K(\alpha)=\min_{\beta\in\operatorname{Br}(K)}\operatorname{ind}(\alpha+\beta_L),$$
其中 $\beta_L$ 是 $\beta$ 沿 $\operatorname{Spec}L\to\operatorname{Spec}K$ 的拉回，$\operatorname{ind}$ 是 Brauer 类的指标（$\alpha$ 所对应中心除环的次数）。等价地，它是对所有 $\beta\in\operatorname{Br}(K)$ 取 $\operatorname{ind}(\alpha+\beta_L)$ 的最小值，因此只依赖 $\alpha$ 在 $\operatorname{Br}(L)/\operatorname{Br}(K)$ 中的像，而不依赖 $\operatorname{ind}(\alpha)$ 本身。

**可直接使用的判据**（命题 5.2.2）：取 $L=\mathbf{Q}(t)$、$C=\mathbf{P}^1_{\mathbf{Q}}$、$\alpha\in\operatorname{Br}(\mathbf{Q}(t))[2]$ 的分歧除子 $D\subset\mathbf{P}^1_{\mathbf{Z}}$ 非空且 snc，$\mathscr{C}\to\mathscr{P}\to C$ 是 Brauer 类为 $\alpha$ 的 $\boldsymbol{\mu}_2$-gerbe。则
$$\operatorname{ind}_{\mathbf{Q}}(\alpha)=2\iff\exists\ \text{可逆层}L: \ M^{*}_{\mathscr{C}/\mathbf{Q}}(2,L)^{ss}(\mathbf{Q})\neq\varnothing .$$
若次数 $[D\otimes\mathbf{Q}:\mathbf{Q}]$ 为奇数，只需对半整数次数的 $L$ 取量词，并在稳定轨迹 $M^{*}_{\mathscr{C}/\mathbf{Q}}(2,L)$ 中找点。

**记号约定**：$L/K$ 是域扩张；$\alpha\in\operatorname{Br}(L)$；$\beta_L$ 是 $\beta\in\operatorname{Br}(K)$ 的拉回；$\operatorname{ind}$ 是 Brauer 类的指标（中心除环的次数）；$\mathscr{C}\to\mathscr{P}\to\mathbf{P}^1_{\mathbf{Q}}$ 是 $\alpha$ 的 $\boldsymbol{\mu}_2$-gerbe 模型；$M^{*}_{\mathscr{C}/\mathbf{Q}}(2,L)$ 是秩 $2$、行列式 $L$ 的稳定正则 $\mathscr{C}$-扭曲层模叠，上标 $ss$ 表示半稳定轨迹；$D$ 是分歧除子，$[D\otimes\mathbf{Q}:\mathbf{Q}]$ 是分歧点的次数和。

## 要点（为什么需要它）

- 与普通指标的关系：$\operatorname{ind}(\alpha)\ge\operatorname{ind}_K(\alpha)$，且 $\operatorname{ind}_K(\alpha)=1$ 当且仅当 $\alpha$ 来自基域（$\alpha\in\operatorname{Br}(K)$）。所以 Faddeev 指标度量的是 $\alpha$ 离 $K$ 有多远，而不是它本身有多大。
- 命题 5.2.2 的两半是一对「拉回—下降」：给定有理点 $P$，沿 $P$ 拉回 $\mathscr{M}\to M$ 得到 $\beta=-[\mathscr{S}]\in\operatorname{Br}(\mathbf{Q})[2]$，在 $P$ 上方 gerbe 分裂给出秩 $2$ 的 $\mathscr{C}\wedge\mathscr{S}$-扭曲层，于是 $\operatorname{ind}(\alpha-\beta)=2$，故 Faddeev 指标整除 $2$；$\alpha$ 分歧保证它不为 $1$。
- 关键归约：因为存在典范同构 $M_{\mathscr{C}\wedge\mathscr{S}/\mathbf{Q}}(2,L)=M_{\mathscr{C}/\mathbf{Q}}(2,L)$，可以把 $\mathscr{C}$ 换成 $\mathscr{C}\wedge\mathscr{S}$，从而假定 $\alpha$ 周期为 $2$，由四元数代数 $(a,b)$ 表示；再用命题 A.2.3(1) 归约到完备离散赋值环上的局部模型。
- 局部模型的算术：写 $b$ 为 $R$ 的一致化子、$a=ub^{\varepsilon}$（$u\in R^{\times}$，$\varepsilon\in\{0,1\}$），在 $R'=R[\sqrt{b}]$ 上令 $\tilde{x}=x/\sqrt{b}^{\varepsilon}$、$\tilde{y}=y/\sqrt{b}$，则 $\tilde{x}^{2}=u$、$\tilde{y}^{2}=1$，基 $1,\tilde{x},\tilde{y},\tilde{x}\tilde{y}$ 恰是一组 $\boldsymbol{\mu}_2$-特征基，$A$ 的特征层分解为 $\chi^{0}\oplus\chi^{1}\oplus\chi^{\varepsilon}\oplus\chi^{1+\varepsilon}\cong\rho^{\oplus2}$（$\rho=\chi^{0}\oplus\chi^{1}$ 是 $\boldsymbol{\mu}_2$ 的正则表示）。这正是「正则性」的定量内容。
- 奇数次假设的作用：秩 $2$ 且次数为奇数时秩与次数互素，半稳定即几何稳定，于是半稳定轨迹与稳定轨迹一致，命题 5.2.2 才能在稳定轨迹上要求有理点；否则只能在半稳定轨迹中找点。

## 关键公式

$$
\operatorname{ind}_K(\alpha)=\min_{\beta\in\operatorname{Br}(K)}\operatorname{ind}(\alpha+\beta_L)
$$

$$
\operatorname{ind}_{\mathbf{Q}}(\alpha)=2\iff\exists L: \ M^{*}_{\mathscr{C}/\mathbf{Q}}(2,L)^{ss}(\mathbf{Q})\neq\varnothing
$$

$$
\chi^{0}\oplus\chi^{1}\oplus\chi^{\varepsilon}\oplus\chi^{1+\varepsilon}\cong\rho^{\oplus2}\qquad(\varepsilon\in\{0,1\})
$$

$$
\tilde{x}=\frac{x}{\sqrt{b}^{\,\varepsilon}},\quad \tilde{y}=\frac{y}{\sqrt{b}},\quad \tilde{x}^{2}=u,\quad \tilde{y}^{2}=1
$$

## 定理与证明（或缺口）

### 命题 5.2.2（Faddeev 指标 2 等价于有有理点）

类 $\alpha$ 具有 Faddeev 指标 $2$，当且仅当对某个可逆层 $L$，空间 $M^{*}_{\mathscr{C}/\mathbf{Q}}(2,L)^{ss}$ 有一个 $\mathbf{Q}$-有理点；若 $[D\otimes\mathbf{Q}:\mathbf{Q}]$ 为奇数，则只需对半整数次数的 $L$ 取量词，并在稳定轨迹 $M^{*}_{\mathscr{C}/\mathbf{Q}}(2,L)$ 中寻找点。

**证明状态：提纲（有缺口）**

1. （$\Rightarrow$ 的反向）设 $\alpha$ 有 Faddeev 指标 $2$，则存在 $\mathscr{S}\to\operatorname{Spec}\mathbf{Q}$ 与秩 $2$ 局部自由 $\mathscr{C}\wedge\mathscr{S}$-扭曲层；由 $M_{\mathscr{C}\wedge\mathscr{S}}=M_{\mathscr{C}}$ 可设 $\alpha$ 周期 $2$，即由四元数代数 $(a,b)$ 表示。
   - *为什么*：Faddeev 指标的定义只允许平移 $\operatorname{Br}(\mathbf{Q})$ 中的类，而平移恰是把 $\mathscr{C}$ 换成 $\mathscr{C}\wedge\mathscr{S}$，模空间不变，故可把平移吸收进 $\alpha$。
2. 由命题 A.2.3(1) 只需对 $\mathscr{C}\otimes\widehat{\mathscr{O}}_{\mathbf{P}^{1},D}$ 证明，于是归约到完备 DVR $R$ 上的分歧四元数代数 $(a,b)$：在 $(a,b)$ 对 $R'=R[\sqrt{b}]$ 的限制中造一个 $\boldsymbol{\mu}_2$-等变 Azumaya 代数 $A$，使 $\boldsymbol{\mu}_2$ 在闭点上方纤维上的诱导表示为 $\rho^{\oplus2}$。
   - *为什么*：整体结论由局部资料粘合（命题 A.2.3）得到；等变 Azumaya 代数就是 $\mathscr{R}_2$ 上的扭曲层，而「$\overline{A}$ 的表示是 $\rho^{\oplus2}$」正是正则性的判据。
3. 由 $\chi^{0}\oplus\chi^{1}\oplus\chi^{\varepsilon}\oplus\chi^{1+\varepsilon}\cong\rho^{\oplus2}$ 得 $\mathscr{R}_2$ 上任意满足 $\mathscr{E}nd(V)=A$ 的扭曲层 $V$ 正则；粘合得整体秩 $2$ 正则 $\mathscr{C}$-扭曲层，其稳定（$\alpha\neq0$）故几何半稳定，奇数次时几何稳定。
   - *为什么*：正则性在叠点处按 $\rho^{\oplus m}$ 判定，分解式保证 $m=1$；稳定 + 秩次数互素推出几何稳定，于是稳定轨迹上的点即所求。

> **缺口**：原文在局部模型处只写「通过剩余域上的一个简单几何计算即推出 $\mathscr{R}_2$ 上任意满足 $\mathscr{E}nd(V)=A$ 的扭曲层都是正则的」，未写出该计算：缺口是验证 $\rho^{\oplus2}$ 在 $\boldsymbol{\mu}_2$-特征分解下没有秩 $1$ 的直和项（否则 $V$ 在叠点处不正则）。此外反向的整体粘合只引用命题 A.2.3(1) 与文献 [19]。


出处：ch6 §5.2 命题 5.2.2（原文 pp. 108–110 / en 118–120）

### 引理 5.2.3（半稳定轨迹有对象推出稳定轨迹有对象）

固定 $\mathbf{Q}$ 的一个位 $\nu$。若 $\mathscr{M}^{*}_{\mathscr{C}/\mathbf{Q}}(2,L)^{ss}_{\mathbf{Q}_{\nu}}$ 有一个对象，则 $\mathscr{M}^{*}_{\mathscr{C}/\mathbf{Q}}(2,L)_{\mathbf{Q}_{\nu}}$ 有一个对象。

**证明状态：完整**

1. 取 $V$ 为秩 $2$、行列式 $L$ 的正则半稳定 $\mathscr{C}\otimes\mathbf{Q}_{\nu}$-扭曲层，令 $Y$ 是其通有形变空间的代数化；曲线上向量丛的形变无障碍，故 $Y$ 在 $\mathbf{Q}_{\nu}$ 上光滑。
   - *为什么*：$\operatorname{Ext}^{2}=0$（相对维数 $1$，推论 A.2.2），故形变空间光滑；$V$ 是其上的 $\mathbf{Q}_{\nu}$-点。
2. $\mathbf{Q}_{\nu}$ 具有性质：任意带有理点的光滑簇具有 Zariski 稠密的有理点集。
   - *为什么*：这是局部域上的隐函数定理／紧化后取有理点的标准事实（$\mathbf{Q}_{\nu}$ 不是 $\mathbf{R}$，光滑点附近可解）。
3. 几何稳定 $\mathscr{C}\otimes\mathbf{Q}_{\nu}$-扭曲层的轨迹在 $Y$ 中开且稠密，故与有理点集相交非空，得到 $\mathbf{Q}_{\nu}$-有理的几何稳定层。
   - *为什么*：稳定性是开条件、几何稳定性在几何纤维上稠密（$Y$ 连通且几何稳定点非空），再用上一段的有理点稠密性。


出处：ch6 §5.2 引理 5.2.3（中译 p. 111 / en PDF p. 121）

### 命题 5.2.6（猜想 2.3 蕴含曲线上的周期-指标）

设 $\alpha\in\operatorname{Br}(\mathbf{Q}(t))$ 满足：(1) 其分歧是 $\mathbf{P}^{1}_{\mathbf{Z}}$ 中的 snc 除子，且是若干纤维与奇数个截面的并；(2) 每个交点处两个分歧扩张或都分裂、或都不分裂、或都分歧；(3) 在非分歧点 $d$ 处，所有给出相同 $(\alpha_{R(t)})_{d}\in\operatorname{Br}(R)$ 的类满足 $\operatorname{per}(\alpha)=\operatorname{ind}(\alpha)$。若猜想 2.3 成立，则 $\operatorname{per}(\alpha)=\operatorname{ind}(\alpha)$。

**证明状态：只引出处，原书不重证**


> 原文只给出条件与结论，并说条件 (2) 近似于 Saltman 的「无热点」（no hot spot）条件；完整证明指向 [20] 与 [15]，本章未展开。因此按 reference 记，不当作本章可复核的证明。


出处：ch6 §5.2 命题 5.2.6（证明从略）

## 易错点

- 把 Faddeev 指标与 $\operatorname{ind}(\alpha)$ 混为一谈：前者允许对 $\beta\in\operatorname{Br}(K)$ 取最小，可以远小于后者——双四元数例里 $\operatorname{ind}_{\mathbf{Q}}(A)=4$ 而每个 $\operatorname{ind}(A\otimes\mathbf{Q}_{\nu})=2$。
- 漏掉「$\alpha$ 分歧」：反向证明用它排除 Faddeev 指标 $1$；若 $\alpha$ 非分歧，则 $\alpha$ 落在 $\operatorname{Br}(\mathbf{Q})$ 的像里，Faddeev 指标直接是 $1$。
- 把命题 5.2.2 的稳定轨迹版本用在偶数次数上：只有 $[D\otimes\mathbf{Q}:\mathbf{Q}]$ 为奇数时，秩 $2$ 半稳定才自动几何稳定（秩与次数互素）；否则只能在半稳定轨迹里找点，条件更强。
- 局部模型的两个指数不能互换：$\tilde{x}=x/\sqrt{b}^{\,\varepsilon}$ 与 $\tilde{y}=y/\sqrt{b}$；$\varepsilon=0$ 给特征 $\{0,0,1,1\}$、$\varepsilon=1$ 给 $\{0,1,1,0\}$，虽都同构于 $\rho^{\oplus2}$，但写错就造不出 $\boldsymbol{\mu}_2$-等变结构。

## 相关卡

- [Faddeev 指标 4 的双四元数代数](../examples/bicyclic-algebra-faddeev-4.md)
- [扭曲层](../concepts/twisted-sheaf.md)
- [周期与指标](../concepts/period-and-index.md)
- [凝聚系](../concepts/coherent-system.md)

## 出处

- ch6 §5.2 定义 5.2.1–命题 5.2.6；中译 p.108（英文 PDF p.118），源码 `chapters/ch06.tex:426`
