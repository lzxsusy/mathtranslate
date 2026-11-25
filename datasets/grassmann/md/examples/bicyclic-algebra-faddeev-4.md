# Faddeev 指标 4 的双四元数代数

> `grassmann/example/bicyclic-algebra-faddeev-4` · 轨道 6 · 曲线上层的算术 · 状态 draft

> **这张卡练什么**：一个在所有局部位上都指标 2 的代数，为什么会有 Faddeev 指标 4？失效的是 Hasse 原则还是模空间的正则性？

## 一句话

双四元数代数 (17,t)⊗(13,(t−1)(t−11)) 的 Faddeev 指标为 4，却在每个 Q_ν 上指标为 2；真正的障碍是 Q₁₇ 处没有正则扭曲层。

## 背景定义

**双四元数代数**指两个四元数代数的张量积 $(a,b)\otimes(c,d)$，它是 $\operatorname{Br}$ 中的 $2$-挠类。本例如下：取
$$A=(17,t)\otimes(13,(t-1)(t-11))\in\operatorname{Br}(\mathbf{Q}(t))[2],$$
它是 $\mathbf{Q}(t)$ 上分歧于 $D=\{0,\infty,1,11\}$ 的双四元数代数。$\operatorname{ind}_{\mathbf{Q}}(A)$ 指 Faddeev 指标 $\min_{\beta\in\operatorname{Br}(\mathbf{Q})}\operatorname{ind}(A+\beta_{\mathbf{Q}(t)})$；本例的结论是 $\operatorname{ind}_{\mathbf{Q}}(A)=4$，而对 $\mathbf{Q}$ 的**所有**位 $\nu$ 都有 $\operatorname{ind}(A\otimes\mathbf{Q}_{\nu}(t))=2$。

## 设定

取 $A=(17,t)\otimes(13,(t-1)(t-11))\in\operatorname{Br}(\mathbf{Q}(t))[2]$（Kunyavskii–Rowen–Tikhonov–Yanchevskii 2006 命题 4.3）。其分歧除子 $D\subset\mathbf{P}^{1}_{\mathbf{Z}}$ 非空且 snc，故可造 $\boldsymbol{\mu}_{2}$-gerbe $\mathscr{C}\to\mathscr{P}\to\mathbf{P}^{1}_{\mathbf{Q}}$，并考虑模叠 $M^{*}_{\mathscr{C}/\mathbf{Q}}(2,L)$（秩 $2$、行列式 $L$ 的稳定正则 $\mathscr{C}$-扭曲层）。位 $\nu=17$ 是关键位：$13$ 在 $\mathbf{Q}_{17}$ 中是平方（$8^{2}=64\equiv13\pmod{17}$，且 $13\equiv1\pmod 4$，Hensel 即得），故 $A_{17}=A\otimes\mathbf{Q}_{17}$ 退化为单个四元数代数 $(17,t)$。

## 计算

(1) **局部退化**：由 $13$ 在 $\mathbf{Q}_{17}$ 中为平方，$A_{17}=(17,t)\otimes(13,(t-1)(t-11))\cong(17,t)\otimes(1,\cdot)\cong(17,t)$；于是 $A_{17}$ 只分歧于 $t=0,\infty$。

(2) **两个特化**：$(17,1)$ 由 $y^{2}=1$ 分裂，故 $(17,1)=0\in\operatorname{Br}(\mathbf{Q}_{17})$；而 $11$ 在 $\mathbf{Q}_{17}$ 中不是平方（模 $17$ 的平方集为 $\{1,2,4,8,9,13,15,16\}$），故 $(17,11)\ne0$。任何与 $A_{17}$ Faddeev 等价的类都可写成 $\alpha'+(u,t)$（$\alpha'\in\operatorname{Br}(\mathbf{Z}_{17})$，$u\in\mathbf{Z}_{17}^{\times}$，见命题 C.1(1)）。它在 $t=1$ 处的特化为 $0+(u,1)=0$；在 $t=11$ 处的特化为 $(17,11)+(u,11)$，而 $u\in\mathbf{Z}_{17}^{\times}$ 使 $u$ 或 $17u$ 为平方但 $v(17u)=1$ 为奇数，故 $17u$ 必非平方，$(17u,11)$ 是 $\mathbf{Q}_{17}$ 上唯一的非平凡四元数代数。所以：**在 $1$ 与 $11$ 处的两个特化中恰有一个非平凡**。

(3) **正则性失效**：于是在 $t=11$ 上方，原始分歧截面之一落入 $A_{17}$ 非分歧的轨迹；该截面上方的叠点是 $\mathsf{B}\boldsymbol{\mu}_{2}\times\operatorname{Spec}\mathbf{Q}_{17}$，其上的 Brauer 类 $\gamma=(17,11)\ne0$。由引理 5.2.4，不存在秩 $2$ 正则 $\mathscr{G}$-扭曲层；由引理 5.2.3，$M^{*}_{\mathscr{C}/\mathbf{Q}}(2,L)^{ss}(\mathbf{Q}_{17})\ne\varnothing$ 也会给出 $M^{*}_{\mathscr{C}/\mathbf{Q}}(2,L)(\mathbf{Q}_{17})\ne\varnothing$。两者合起来：
$$\forall L: \ M^{*}_{\mathscr{C}/\mathbf{Q}}(2,L)(\mathbf{Q}_{17})=\varnothing .$$

(4) **结论**：若 $\operatorname{ind}_{\mathbf{Q}}(A)=2$，命题 5.2.2 会给出某个 $L$ 使 $M^{*}_{\mathscr{C}/\mathbf{Q}}(2,L)^{ss}$ 有 $\mathbf{Q}$-有理点，从而在每个 $\mathbf{Q}_{\nu}$ 上都有局部点，与 (3) 矛盾。故 $\operatorname{ind}_{\mathbf{Q}}(A)>2$；而作者们已算出它是 $4$。这解释了「Hasse 原则失效」的措辞：真正失效的不是 Hasse 原则，而是「相伴的模问题在 $\mathbf{Q}_{17}$ 处有局部点」这一局部前提。

## 要点

- Faddeev 指标 $4$ 与局部指标 $2$ 不矛盾：局部指标只看 $A\otimes\mathbf{Q}_{\nu}(t)$ 本身，Faddeev 指标还允许平移 $\beta\in\operatorname{Br}(\mathbf{Q})$，而平移在 $\mathbf{Q}_{17}$ 处会改变特化的非平凡性。
- 关键计算只有两条：$13$ 在 $\mathbf{Q}_{17}$ 中是平方（故 $A_{17}=(17,t)$），$11$ 不是（故 $(17,11)\ne0$）。两条加起来给出「两个特化恰一非平凡」的精确陈述。
- 正则性是真正的条件：叠点处要求扭曲层是 $\rho^{\oplus m}$ 型的，秩 $2$ 只能是 $m=1$，于是 $\mu_{2}\times\mu_{2}$ 惯性的特征分解会把层劈成两个秩 $1$ 块（引理 5.2.4）——这不是可以绕过的技术假设，而是本章最重要的现象（批注 9、10）。
- 这个例子是命题 5.2.2 的反向见证：它说明「Faddeev 指标 $2$ $\Leftrightarrow$ 有有理点」并不是空洞的等价，而是可以真的用局部障碍否证的条件。

## 关键公式

$$
A=(17,t)\otimes(13,(t-1)(t-11))\in\operatorname{Br}(\mathbf{Q}(t))[2]
$$

$$
A_{17}=A\otimes\mathbf{Q}_{17}\cong(17,t),\qquad (17,1)=0,\qquad (17,11)\ne0
$$

$$
\forall L: \ M^{*}_{\mathscr{C}/\mathbf{Q}}(2,L)(\mathbf{Q}_{17})=\varnothing
$$

$$
\mathscr{I}(\mathscr{G})\cong\boldsymbol{\mu}_{2}\times\boldsymbol{\mu}_{2},\qquad F=F_{0}\oplus F_{1},\quad \operatorname{rk}F_{0}+\operatorname{rk}F_{1}=2
$$

## 相关定理

- **引理 5.2.4（$\mathsf{B}\boldsymbol{\mu}_{2}\times\operatorname{Spec}F$ 上没有秩 2 正则扭曲层）**：给定域 $F$ 与非平凡 Brauer 类 $\gamma\in\operatorname{Br}(F)[2]$，设 $\mathscr{G}\to\mathsf{B}\boldsymbol{\mu}_{2}\times\operatorname{Spec}F$ 是表示 $\gamma$ 在 $\operatorname{Br}(\mathsf{B}\boldsymbol{\mu}_{2}\times\operatorname{Spec}F)$ 中拉回的 $\boldsymbol{\mu}_{2}$-gerbe。则不存在秩为 $2$ 的正则 $\mathscr{G}$-扭曲层。
- **推论 5.2.5（模空间在 $\mathbf{Q}_{17}$ 处无点）**：对上述 $A$ 与所有可逆层 $L$，$M^{*}_{\mathscr{C}/\mathbf{Q}}(2,L)(\mathbf{Q}_{17})=\varnothing$。

## 易错点

- 把「Hasse 原则失效」照字面理解：作者们自己的措辞如此，但本章的结论是局部障碍——在 $\mathbf{Q}_{17}$ 处模空间没有点，所以 Hasse 原则根本没有被违反。
- 把 $(17,1)=0$ 记成 $\ne0$：$y^{2}=1$ 使 $(a,1)$ 分裂，这是判断两个特化「恰一非平凡」的关键一步；记反会得出完全相反的结论。
- 以为 $u$ 可以取成有奇赋值的元素：Faddeev 等价的平移只能来自 $u\in\mathbf{Z}_{17}^{\times}$（$\operatorname{Br}(\mathbf{Z}_{17})$ 的部分不分歧），否则 $v(17u)$ 的奇偶性会变，$(17u,11)$ 的平凡性判断就失效。
- 把秩 $2$ 的正则性与稳定性混为一谈：正则性是在叠点处的**局部**条件（$\rho^{\oplus m}$），稳定性是斜率条件；本例中秩 $2$ 层可能稳定，但它在叠点处一定不正则。

## 用到哪些概念

- [Faddeev 指标](../concepts/faddeev-index.md)
- [周期与指标](../concepts/period-and-index.md)
- [扭曲层](../concepts/twisted-sheaf.md)

## 相关卡

- [Faddeev 指标](../concepts/faddeev-index.md)
- [扭曲层](../concepts/twisted-sheaf.md)
- [周期与指标](../concepts/period-and-index.md)
- [凝聚系](../concepts/coherent-system.md)

## 出处

- ch6 §5.2 延伸的例子与引理 5.2.4–推论 5.2.5（引 [15] 命题 4.3）；中译 p.110（英文 PDF p.120），源码 `chapters/ch06.tex:463`
