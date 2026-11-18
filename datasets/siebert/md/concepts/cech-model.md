# Čech 模型（$D^b(X)$ 的 dg 增强）

> `siebert/concept/cech-model` ｜ track F ｜ draft

**一句话**：用有限仿射覆盖的 Čech 上链搭出 $D^b(X)$ 的 dg 范畴：态射是 Čech 与内部 Hom 的双分次全复形，故取上同调后还要靠 HPL 补高阶运算。

**自测**：为什么 $D^b(X)$ 的 dg 模型要用 Čech 上链来写态射，而不能直接用整体截面 $\Hom(E^\bullet,F^\bullet)$？

## 定义

设 $X$ 光滑射影，$\mathscr U=\{U_i\}$ 为有限仿射覆盖。$D^b_{\mathrm{dg}}(X)$ 的对象是局部自由 $\OO_X$ 模的有界复形 $E^\bullet$；态射复形为 $\Hom^n(E^\bullet,F^\bullet)=\bigoplus_{p+q=n}\check C^p(\mathscr U,\mathcal Hom^q_{\OO_X}(E^\bullet,F^\bullet))$，其中 $\check C^p(\mathscr U,\mathcal G)=\bigoplus_{i_0<\cdots<i_p}\Gamma(U_{i_0}\cap\cdots\cap U_{i_p},\mathcal G)$；$m_1$ 由 Čech 微分与内部 Hom 微分相加给出，$m_2(g,f)=(-1)^{\deg f}g\circ f$。

记号：$\check C^p$ 记 Čech $p$ 上链；$\mathcal Hom^q(E^\bullet,F^\bullet)=\mathcal Hom(E^\bullet,F^\bullet[q])$（式 6.23）；$\mathscr U$ 固定后把所得 dg 范畴记作 $\mathcal A=(D^b_{\mathrm{dg}}(X),\mathscr U)$。

## 要点

- 为什么需要它：$D^b(X)$ 只有 Hom 群，要谈 $A_\infty$ 结构必须先把 Hom 提升为复形；有限仿射覆盖的 Čech 上链给出一个具体可算的 dg 模型。
- $X$ 光滑射影时每个凝聚层都有有限局部自由消解，故 $D^b(X)=D^b(\operatorname{Coh}X)=\operatorname{Perf}(X)$（6.19），可以取局部自由（完美）复形作对象。
- 它是严格的 dg 范畴（$m_k=0,k\ge3$）；所以 $H(\mathcal A)=D^b(X)$ 上的 $A_\infty$ 结构不是免费的，必须由同调扰动引理转移得到。
- $m_1$ 的两部分：Čech 微分与内部微分 $d_{\mathcal Hom}$；$m_2$ 的符号 $(-1)^{\deg f}$、$(-1)^{q'p}$ 来自把 $g\circ f$ 搬到「Čech 次数 + 内部次数」的双分次上。
- 不同覆盖给出不同的 dg 范畴，但彼此只差 $A_\infty$ 拟等价；所以「Čech 模型」是一个模型而非典范对象。

## 公式

$$\Hom^n_{D^b_{\mathrm{dg}}(X)}(E^\bullet,F^\bullet)=\bigoplus_{p+q=n}\check C^p\bigl(\mathscr U,\mathcal Hom^q_{\OO_X}(E^\bullet,F^\bullet)\bigr)\qquad(6.22)$$
$$\check C^p(\mathscr U,\mathcal G)=\bigoplus_{i_0<\cdots<i_p}\Gamma\bigl(U_{i_0}\cap\cdots\cap U_{i_p},\mathcal G\bigr)\qquad(6.24)$$
$$m_2(g,f)=(-1)^{\deg f}g\circ f,\qquad g\circ f=\bigl((-1)^{q'p}g_{n+q,i_0,\ldots,i_{p'}}\circ f_{n,i_{p'},\ldots,i_{p+p'}}\bigr)\big|_{U_{i_0}\cap\cdots\cap U_{i_{p+p'}}}\qquad(6.27\text{–}6.28)$$

## 定理与证明

### 事实：Čech 模型计算 $\RHom$

对 $E^\bullet,F^\bullet\in D^b_{\mathrm{dg}}(X)$，有 $H^n\bigl(\Hom^\bullet(E^\bullet,F^\bullet)\bigr)\cong\Hom_{D^b(X)}(E^\bullet,F^\bullet[n])$。

（sketch；来源：原书 p.100–101）

1. 对每一对 $p,q$，Čech 上链 $\check C^p(\mathscr U,\mathcal Hom^q(E^\bullet,F^\bullet))$ 计算层 $\mathcal Hom^q(E^\bullet,F^\bullet)$ 的超上同调。  
   为什么：$\mathscr U$ 有限且仿射，Čech 复形与导出函子计算的超上同调一致（Čech-to-derived 比较），这是 Čech 方法能替代内射消解的原因。
2. 把双复形总复形的微分拆成 Čech 微分与内部微分之和，写出与 $\Ext$ 谱序列对应的双复形。  
   为什么：6.22 的指标 $p+q=n$ 正是双复形的总次数，$m_1$ 的两项分别沿两个方向。
3. 谱序列收敛到 $H^n(\Hom_{D^b(X)}(E^\bullet,F^\bullet))$，再用局部自由性使内部方向退化。  
   为什么：$E^\bullet$ 局部自由时 $\mathcal Hom^q$ 就是普通 Hom 层，双复形的内部上同调集中在 $q$ 处，谱序列只剩一列，故总上同调就是 $\Ext^n$。

缺口：讲义直接使用 6.21–6.24，未证此比较；严格证明需要有限仿射覆盖的 Leray 性质与 Čech-to-derived 谱序列，本卡只给骨架。

## 易错点

- $\check C^p$ 里是整体截面 $\Gamma$，不是层本身；把 $\mathcal Hom$ 当系数层再取截面才是 6.24 的意思。
- 不要把它当成「Čech 复形」：每个 $n$ 次分量是 $\bigoplus_{p+q=n}$ 的双分次全复形，取上同调前还有内部 Hom 微分。
- 有限仿射覆盖的存在性用 $X$ 拟紧分离（射影当然满足）；无限覆盖会让 $\check C^p$ 变成无穷直和，紧性论证失效。
- $m_2$ 的 Koszul 符号漏掉后，Leibniz 法则与 6.28 的结合律都会坏，整个 dg 范畴不成立。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 6 章 §2.1 导出范畴的 Čech 模型，p.100–101（原书 p.100–101）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 6 章 §2.2 同调扰动引理，p.101–101（原书 p.101）

关联：`siebert/concept/dg-category`、`siebert/deriv/hpl-deformation`、`siebert/concept/homological-perturbation-lemma`、`siebert/correction/perfect-vs-compact`

来源说明：原书 p.100–101 §2.1（6.19–6.28）；p.101 §2.2 开头说明为何取上同调后要用 HPL。nLab「dg-category」（last revised 2024-05-14）核对 $\Hom^n$ 的定义；nLab「Čech cohomology」（2026-06-30）核对 Čech 上链与超上同调的比较；nLab「perfect complex」（2016-01-02）核对「光滑射影下 $\operatorname{Perf}=D^b$」。
