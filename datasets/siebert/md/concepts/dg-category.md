# 微分分次范畴（dg 范畴）

> `siebert/concept/dg-category` ｜ track F ｜ draft

**一句话**：把 Hom 集换成复形、复合换成满足分次 Leibniz 法则的映射；它是 $k>2$ 时 $m_k=0$ 的 $A_\infty$ 范畴，取上同调后高阶信息全丢。

**自测**：既然 dg 范畴取上同调后只剩三角范畴，为什么不能直接把 $H(\mathcal A)$ 当作 $D^b(X)$ 的模型？

## 定义

一个 dg 范畴 $\mathcal A$ 由对象集合、每对对象 $X_0,X_1$ 的 $\ZZ$ 分次 $K$ 向量空间 $\Hom(X_0,X_1)=\bigoplus_n\Hom^n(X_0,X_1)$、次数 $1$ 的微分 $m_1$（$m_1^2=0$）与次数 $0$ 的复合 $m_2$ 组成，且 $m_2$ 满足分次结合律与分次 Leibniz 法则 $m_1m_2=m_2(m_1\otimes\id+\id\otimes m_1)$。等价地，它就是 $k>2$ 时 $m_k=0$ 的 $A_\infty$ 范畴（原书 p.100）。

记号：$\Hom^n$ 记次数 $n$ 的态射，$[1]$ 记移位；$H(\mathcal A)$ 记同调范畴（对象不变、态射取 $H^*(\Hom_{\mathcal A})$）；$D^b_{\mathrm{dg}}(X)$ 记 $D^b(X)$ 的 Čech dg 模型。

## 要点

- 「dg = 高阶运算为零的 $A_\infty$」：$A_\infty$ 关系 (6.10) 在 $k=3$ 时化为 $m_2$ 的严格结合律，$k\ge4$ 时全为平凡恒等式；所以 dg 范畴是 $A_\infty$ 范畴的特例，反之不然。
- 同调范畴 $H(\mathcal A)$：对象不变，态射取 $H^*(\Hom_{\mathcal A})$，此时 $m_1=0$；$H(\mathcal A)$ 带平移 $[1]$ 与由映射锥给出的好三角，成为三角范畴，但三角公理不唯一、不函子化。
- 标准例子：$X$ 光滑射影时 $D^b_{\mathrm{dg}}(X)$ 的对象是局部自由层的有界复形，$\Hom^n=\bigoplus_{p+q=n}\check C^p(\mathscr U,\mathcal Hom^q(E^\bullet,F^\bullet))$，$m_1$ 为 Čech 微分加内部 Hom 微分，$m_2(g,f)=(-1)^{\deg f}g\circ f$。
- 拟等价：$F:\mathcal A\to\mathcal B$ 使 $H(F)$ 为等价即拟等价；$A_\infty$ 拟等价把它放宽成「$H$ 上同构加高阶修正」，同调扰动引理的结论正是 $H(\mathcal A)$ 与 $\mathcal A$ 拟等价。
- 取上同调会丢信息：$H(\mathcal A)$ 只记得 $m_2$ 的同调类，$m_3,m_4,\ldots$ 全部丢失；把它们搬回 $H(\mathcal A)$ 必须用同调扰动引理（§2.2），这就是本章 §2 的动机。

## 公式

$$\Hom^n_{D^b_{\mathrm{dg}}(X)}(E^\bullet,F^\bullet)=\bigoplus_{p+q=n}\check C^p\bigl(\mathscr U,\mathcal Hom^q_{\OO_X}(E^\bullet,F^\bullet)\bigr)$$
$$m_1^2=0,\qquad m_1m_2=m_2(m_1\otimes\id+\id\otimes m_1),\qquad m_2(m_2\otimes\id)=m_2(\id\otimes m_2)$$
$$\Hom_{\mathcal A}(X_0,X_1)=\bigoplus_{n\in\ZZ}\Hom^n(X_0,X_1),\qquad m_k=0\ (k\ge3)$$

## 定理与证明

### 命题：dg 范畴的同调范畴是三角范畴

若 $\mathcal A$ 是 dg 范畴，则 $H(\mathcal A)$ 带有平移 $[1]$ 与由映射锥给出的好三角，成为三角范畴。

（sketch；来源：原书 p.99–100）

1. 平移：$\Hom(X,Y)[1]^n=\Hom^{n+1}(X,Y)$，微分变号使 $m_1^2=0$ 仍成立。  
   为什么：移位后微分反号，这是 Koszul 符号约定的直接结果，也保证取上同调与平移可交换。
2. 对态射 $f:X\to Y$ 逐分量取映射锥 $\operatorname{Cone}(f)$，得序列 $X\to Y\to\operatorname{Cone}(f)\to X[1]$。  
   为什么：锥在复形层面有泛性质，取上同调后自动给出长正合列，这正是好三角的定义内容。
3. 验证 (TR1)–(TR4)；在 dg 情形用「好三角 = 可裂入三角」可避开八面体公理。  
   为什么：这是 Verdier 的定理；dg 范畴里可用链同伦显式构造，故不必走公理化的八面体证明。

缺口：讲义只把「取上同调得上同调范畴」当已知（p.99），未证三角公理；八面体公理在 dg 情形可用可裂三角回避，细节未写。

## 易错点

- $H(\mathcal A)$ 不是 dg 范畴：它上面 $m_1=0$，$m_2$ 只是同调层面的复合，高阶 $m_k$ 已经丢失。
- 「dg 范畴」与「复形范畴」不同：前者是 enriched 结构（Hom 是复形），后者是对象为复形、态射为链映射的普通范畴。
- $m_2$ 不是朴素复合：6.28 的 $(-1)^{q'p}$ 与 6.27 的 $(-1)^{\deg f}$ 是 Koszul 符号，漏掉后 Leibniz 法则与结合律都不成立。
- dg 增强不唯一：同一三角范畴可以有多个 dg 增强，只在拟等价意义下比较；Lunts–Orlov 的唯一性定理需要额外条件。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 6 章 §2.1 导出范畴的 Čech 模型，p.100–101（原书 p.100–101）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 6 章 §1.4 Fukaya 范畴，p.99–99（原书 p.99）

关联：`siebert/concept/enhanced-triangulated-category`、`siebert/concept/cech-model`、`siebert/concept/homological-perturbation-lemma`

来源说明：原书 p.100–101 §2.1（dg 范畴的定义与 Čech 模型）、p.98–99 §1.3（$A_\infty$ 关系作对照）。nLab「dg-category」（last revised 2024-05-14）核对定义与同调范畴的三角结构；nLab「enhanced triangulated category」（2026-01-27）核对 dg 增强与稳定 $\infty$-范畴的对应。Stacks 未用到。
