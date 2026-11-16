# 几何量子化总览：从相空间到量子希尔伯特空间

> `geoq/concept/overview-geometric-quantization` · 轨道 总览 · 状态 draft

> **先自测**：拿到一个辛流形，几何量子化要怎么一步步造出量子希尔伯特空间？每一步各自解决了什么、又留下了什么缺口？

## 一句话

第 5 章主线：辛几何搭相空间，半经典给出 (L,Ω)，海森堡群给出表示模型，再由预量子化、极化与半形式三步组装成几何量子化。

## 定义

几何量子化是把经典辛流形 $(M,\omega)$ 变成量子希尔伯特空间与算子代数的一套构造：先取预量子化线丛 $(\mathcal{L},\nabla)$，使曲率 $F_\nabla=-\frac{i}{\hbar}\omega$；再取极化 $P\subset T^\mathbb{C}M$，把注意力限制在「只依赖一半变量」的 $P$-极化截面上；最后张量半形式线丛 $\sqrt{K_M}$ 修正马斯洛夫相位。对 $P$-保持函数 $f$（即 $[V_f,P]\subset P$），量子化算子为 $Q(f)=i\hbar\nabla_{V_f}+f$。

**记号约定**：$P$ 是可积拉格朗日子丛；$\Gamma_P(\mathcal{L})$ 记 $P$-极化截面空间；$K_M=\Lambda^nT^{*(1,0)}M$ 是典范线丛；$\Omega$ 是拉格朗日子流形上的半密度；$\{f,g\}=\iota_{V_f}\iota_{V_g}\omega$ 是泊松括号。

## 要点

- 经典侧的数据是辛流形 $(M,\omega)$：它同时给出哈密顿向量场 $V_f$（由 $\iota_{V_f}\omega=df$）与泊松括号，使 $C^\infty(M)$ 成为李代数。
- 半经典侧把 WKB 解 $\psi=e^{iS/\hbar}a$ 几何化：相函数 $S$ 给出拉格朗日子流形 $L_{dS}$，振幅 $a$ 升级为 $L$ 上在 $V_{\mathcal{H}}$ 下不变的半密度 $\Omega$；能否整体定义相位，取决于玻尔–索末菲条件与马斯洛夫修正。
- 表示论侧把正则对易关系编码进海森堡群 $H_n$：薛定谔表示与 Segal–Bargmann 表示是它的不可约酉表示，斯通–冯·诺依曼定理保证本质唯一。
- 狄拉克原理 Q1–Q5 是量子化的目标清单；格罗嫩沃尔德–范霍夫定理证明它在四次多项式上已不可能全部满足，所以必须放宽某条（通常是 Q5）。
- 预量子化满足 Q1–Q4，但 $L^2(M,\mathcal{L})$ 太大、$Q(f)$ 始终一阶；极化砍掉一半变量，半形式再把 $n\hbar$ 修成 $(n+\frac12)\hbar$。
- 整性条件 $\frac{1}{2\pi\hbar}\int_\Sigma\omega\in\mathbb{Z}$ 决定预量子化线丛是否存在；它把「哪些辛流形可量子化」变成拓扑问题。
- 并非所有函数都能直接量子化：只有 $P$-保持函数保证把 $P$-极化截面送到 $P$-极化截面；其余函数要靠 BKS 核在极化之间搬移，书中只给思路。

## 关键公式

$$
$F_\nabla=-\frac{i}{\hbar}\omega$
$$

$$
$Q(f)=i\hbar\nabla_{V_f}+f$
$$

$$
$\frac{1}{2\pi\hbar}\int_\Sigma\omega\in\mathbb{Z}$
$$

$$
$\nabla_Xs=0,\qquad \forall X\in P$
$$

$$
$\mathcal{H}_P=\Gamma_P(\mathcal{L}\otimes\sqrt{K_M})$
$$

$$
$E_n=\hbar\omega\left(n+\frac12\right)$
$$

## 定理与证明

### 三步流水线：预量子化 → 极化 → 半形式

设 $(M,\omega)$ 可量子化，$(\mathcal{L},\nabla)$ 是预量子化线丛，$P$ 是极化。则：(i) 预量子化算子 $Q(f)=i\hbar\nabla_{V_f}+f$ 在 $\Gamma(M,\mathcal{L})$ 上满足 Q1–Q4；(ii) 取 $P$-极化截面 $\Gamma_P(\mathcal{L})=\{s\mid\nabla_Xs=0,\ X\in P\}$ 可把自由度减半；(iii) 把系数张量到 $\sqrt{K_M}$ 上，可把谐振子谱从 $n\hbar$ 修正为 $(n+\frac12)\hbar$。

**完整证明**

1. 曲率条件 $F_\nabla=-\frac{i}{\hbar}\omega$ 使 $[Q(f),Q(g)]$ 中的曲率项恰好抵消泊松括号项，得到 $[Q(f),Q(g)]=i\hbar Q(\{f,g\})$（Q4）；$Q(1)=1$（Q2），自伴性由刘维尔定理给出（Q3）。
   - *为什么*：这一步只用到预量子化线丛，不需要极化；它已经给出一个「合法但不是最终」的量子化。
2. 对 $X\in P$ 要求 $\nabla_Xs=0$，把截面从依赖全部 $2n$ 个相空间变量缩减为只依赖 $n$ 个变量。对实极化 $P=\operatorname{Span}\{\partial/\partial p_i\}$，$P$-极化截面就是只依赖 $x$ 的函数。
   - *为什么*：这一步解决 Q5：$L^2(M,\mathcal{L})$ 太大，砍掉一半变量后才像波函数。
3. 在焦散处，相位的多值性由半密度平方根的 $\Theta^{1/4}$ 承担；把量子态改成 $\mathcal{L}\otimes\sqrt{K_M}$ 的 $P$-极化截面后，$S^2$ 或谐振子例子里 $Q(\mathcal{H})=\hbar z\partial_z$ 的谱从 $n\hbar$ 变为 $(n+\frac12)\hbar$。
   - *为什么*：这一步补上马斯洛夫修正；没有它，半经典与精确谱相差 $\frac12\hbar$。
4. 若 $f$ 是 $P$-保持的，即 $[V_f,P]\subset P$，则 $[\nabla_X,Q(f)]=i\hbar\nabla_{[X,V_f]}$ 仍落在 $P$ 中，故 $Q(f)$ 把 $P$-极化截面送到 $P$-极化截面。
   - *为什么*：这给出量子算子的定义域：先在一类「与极化相容」的函数上定义，其余函数需要额外的极化搬移机制。
5. 三步合起来给出 $\mathcal{H}_P=\Gamma_P(\mathcal{L}\otimes\sqrt{K_M})$ 与 $Q:C^\infty(M)_P\to\operatorname{End}(\mathcal{H}_P)$。
   - *为什么*：这就是几何量子化的输出数据；每一步的必要性都能由前面的反例说明。

来源：ch05b.tex:817-1470（原书 p.285–296）

### 格罗嫩沃尔德–范霍夫不可行定理

不存在 $\mathbb{R}$-线性映射 $Q:P^{\le4}\to L^2(\mathbb{R}^n)$ 上的自伴算子，使得 $Q(1)=1$、$Q(x^i)=\hat x^i$、$Q(p_i)=\hat p_i$，且 $[Q(f),Q(g)]=i\hbar Q(\{f,g\})$ 对所有 $f,g\in P^{\le4}$ 成立。

**完整证明**

1. 由 Q1、Q2 与 Q4 可推出：在次数 $\le3$ 的多项式上，$Q$ 与 Weyl 量子化 $\mathcal{W}_\hbar$ 至多相差一个常数；再用 $x^3=\frac13\{x^3,xp\}$、$x^2p=\frac16\{x^3,p^2\}$ 等恒等式把常数逼成零，故 $Q=\mathcal{W}_\hbar$ 于 $P^{\le3}$。
   - *为什么*：先把低次部分钉死，才能在四次项上制造矛盾；这一步是 Weyl 对应与泊松括号相容性的直接推论。
2. 对 $x^2p^2$ 写出两种括号表示：$x^2p^2=\frac19\{x^3,p^3\}=\frac13\{x^2p,xp^2\}$。由 Q4，$Q(x^2p^2)$ 必须同时等于 $\frac{1}{9i\hbar}[Q(x^3),Q(p^3)]$ 与 $\frac{1}{3i\hbar}[Q(x^2p),Q(xp^2)]$。
   - *为什么*：$x^2p^2$ 有两种不同的「泊松括号原像」，Q4 要求两条路径给同一个算子。
3. 用 $Q=\mathcal{W}_\hbar$ 计算：$[x^3,p^3]_*=9(i\hbar)x^2p^2+\frac32(i\hbar)^3$ 给出 $\mathcal{W}_\hbar(x^2p^2)-\frac16\hbar^2$；而 $[x^2p,xp^2]_*=3(i\hbar)x^2p^2-\frac12(i\hbar)^3$ 给出 $\mathcal{W}_\hbar(x^2p^2)+\frac16\hbar^2$。两者相差 $\frac13\hbar^2\ne0$。
   - *为什么*：Moyal 括号的 $\hbar^3$ 项在两条路径上符号相反，这是不可行性的定量来源。
4. 矛盾。因此满足全部 Q1–Q5 的量子化映射在 $P^{\le4}$ 上不存在。
   - *为什么*：结论不依赖具体流形，只依赖多项式代数与 Moyal 括号的结构。

来源：ch05b.tex:686-816（原书 p.281–284）

## 易错点

- 不要把预量子化当成几何量子化的全部：$L^2(M,\mathcal{L})$ 的截面同时依赖位置与动量，$Q(f)$ 对任意 $f$ 都只是一阶微分算子，得不到薛定谔算子。
- 极化不是唯一的：实极化给位置波函数，凯勒极化给全纯（Bargmann–Fock）波函数；不同极化的量子希尔伯特空间由 BKS 核联系，书中只说明思路、未展开构造。
- 半形式线丛 $\sqrt{K_M}$ 的存在性在一般辛流形上是额外的拓扑条件（需要 metaplectic 结构，$w_2(M)=0$）；书中默认它可以取到，遇到不可自旋的 $M$ 要单独检查。
- 马斯洛夫修正的因子是 $\frac14$：$\Theta^{1/4}$ 绕闭路改变 $e^{-i\pi m(\gamma)/2}$，不是 $\frac12$；漏掉或写成 $\frac12$ 会给出错误的半整数偏移。

## 相关卡

- [辛流形（symplectic manifold）](../concepts/symplectic-manifold.md)
- [WKB 半经典解与哈密顿–雅可比方程](../concepts/wkb-approximation.md)
- [海森堡群 $H_V$ 与中心扩张](../concepts/heisenberg-group.md)
- [狄拉克量子化原理 Q1–Q5](../concepts/dirac-quantization.md)
- [预量子化线丛](../concepts/prequantization.md)
- [极化：实极化与凯勒极化](../concepts/polarization.md)
- [量子希尔伯特空间与半形式修正](../concepts/quantum-hilbert-space.md)
- [量子算子与 P-保持条件](../concepts/quantum-operator.md)
- [凯勒极化、半形式与 $(n+\frac12)\hbar$ 谱](../examples/oscillator-half-form-spectrum.md)

## 出处

- §5.1–§5.2 相空间的辛几何与半经典量子化，p.250–271（PDF p.251–272），源码 `ch05a.tex:9-1221`
- §5.3–§5.4 海森堡群与几何量子化，p.272–296（PDF p.273–297），源码 `ch05b.tex:6-1470`
