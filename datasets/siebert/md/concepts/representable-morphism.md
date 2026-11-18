# 可表态射

> `siebert/concept/representable-morphism` ｜ track B ｜ draft

**一句话**：叠的态射 $f:\mathcal F\to\mathcal G$ 可表，指沿任意概形 $B\to\mathcal G$ 的纤维积仍是概形；于是概形态射的性质可沿 $f$ 搬到叠上。

**自测**：为什么「沿任意概形取纤维积仍是概形」这一条就能让光滑、固有这类概形性质对叠也有意义？

## 定义

设 $f:\mathcal F\to\mathcal G$ 是 $S$ 上两个叠（更一般地，纤维群胚）之间的态射。称 $f$ 可表，如果对任意概形 $B$ 与任意态射 $B\to\mathcal G$，纤维积 $B\times_{\mathcal G}\mathcal F$ 同构于某个概形 $E$ 的关联群胚 $\underline E$（讲义注明：更合适的做法是允许它只是代数空间）。等价的说法：每个从概形出发的态射 $B\to\mathcal G$ 都可表。对在基变换下稳定的概形态射性质 $P$（有限型、分离、平坦、仿射、固有等），称可表的 $f$ 具有性质 $P$，如果对每个 $B\to\mathcal G$，投影 $B\times_{\mathcal G}\mathcal F\to B$ 具有性质 $P$（定义 2.7、定义 2.8）。

记号：$B\times_{\mathcal G}\mathcal F$：2-纤维积（只在相差 2-态射的意义下交换）；$\Delta_{\mathcal F}:\mathcal F\to\mathcal F\times_S\mathcal F$：对角态射，它是 $\mathcal F\to S$ 沿自身的纤维积；$\operatorname{Iso}_B(X,Y)$：$B$ 上两点间同构的函子。

## 要点

- 可表性把叠的问题化归为概形的问题：一旦 $B\times_{\mathcal G}\mathcal F=\underline E$ 是概形，任何关于概形态射 $E\to B$ 的陈述（平坦、非分歧、有限、固有）都可以直接检验，再按「$B$ 任意」拼回叠的陈述。
- 它是逐概形的局部条件，所以可以只在一个覆盖上验证。讲义在命题 2.3 里正是这样算的：先在使 $G$ 主丛平凡的平展局部（等价于一个概形点）把 $\operatorname{Iso}_B(f,f')$ 写成 $B\times_{X\times_SX}(G\times_SX)$，再用下降拼回叠的层面。
- 商态射 $X\to[X/G]$ 可表：沿 $B\to[X/G]$（等价于给一个 $G$-主丛 $E\to B$ 与等变映射 $E\to X$）取纤维积，得到的正是 $E$ 本身（例 2.19）。这条与「$G$-主丛在平展局部平凡」配合，是商叠所有计算的入口。
- 万有曲线 $\mathcal C_g\to\mathcal M_g$ 可表：沿曲线族 $C/B$（即 $B\to\mathcal M_g$）取纤维积得到 $C$（例 2.20）。所以「万有曲线」不是额外的构造，就是「模叠的通用对象落在概形上」的表现。
- 对角可表与同构可表是同一件事：$\Delta_{\mathcal X}$ 可表 $\iff$ 每个 $B\to\mathcal X$ 可表，且此时 $\operatorname{Iso}_B(X,Y)$ 由 $B\times_{\mathcal X\times_S\mathcal X}\mathcal X$ 表示（命题 2.4、式 (2.52)）。DM 定义的第一条「$\Delta$ 可表、拟紧、分离」因此等价于「同构函子被概形表示」。
- 从 $\Delta$ 还能读出叠本身的性质：$\Delta$ 固有 $\iff$ 叠分离；$\Delta$ 非分歧 $\iff$ 稳定子离散（有限），这正是 Deligne–Mumford 叠相对 Artin 叠的差别。

## 公式

$$B\times_{\mathcal G}\mathcal F\ \cong\ \underline E\qquad(\text{对每个概形 }B\to\mathcal G\text{ 与某个概形 }E)$$
$$\operatorname{Iso}_B(X,Y)\ \cong\ B\times_{\mathcal X\times_S\mathcal X}\mathcal X$$
$$\operatorname{Iso}_B(f,f')\cong B\times_{X\times_SX}(G\times_SX)\qquad(\text{例 2.3 的商叠情形，式 (2.46)})$$

## 定理与证明

### 命题 2.4（对角可表 $\iff$ 逐概形可表）

设 $\mathcal X$ 是 $S$ 上的叠。对角态射 $\Delta_{\mathcal X}:\mathcal X\to\mathcal X\times_S\mathcal X$ 可表，当且仅当每个从概形出发的态射 $B\to\mathcal X$ 可表。此时对任意 $X,Y\in\operatorname{Obj}\mathcal X(B)$，$\operatorname{Iso}_B(X,Y)$ 由概形 $B\times_{\mathcal X\times_S\mathcal X}\mathcal X$ 表示。

（sketch；来源：原书 p.35 命题 2.4）

1. 设 $\Delta_{\mathcal X}$ 可表，$B\to\mathcal X$ 为概形点，$B'\to\mathcal X$ 另一个；则 $B'\times_{\mathcal X}B=(B'\times_SB)\times_{\mathcal X\times_S\mathcal X}\mathcal X$，右端是 $\Delta$ 沿概形态射 $B'\times_SB\to\mathcal X\times_S\mathcal X$ 的基变换，按可表性的定义是概形。  
   为什么：这是可表性定义的直接展开：纤维积沿概形作基变换后必须仍是概形。
2. 把 $B'$ 取成 $B$ 与自身，得到 $\operatorname{Iso}_B(X,Y)$ 的表示：$X,Y\in\mathcal X(B)$ 给出 $B\to\mathcal X\times_S\mathcal X$，于是 $\operatorname{Iso}_B(X,Y)\cong B\times_{\mathcal X\times_S\mathcal X}\mathcal X$。  
   为什么：「$B$ 上两点同构」的函子就是把 $B$ 沿 $\Delta$ 拉回，这是把对角可表翻译成同构可表的标准一步。
3. 反向：若每个 $B\to\mathcal X$ 可表，则对任意 $B\to\mathcal X\times_S\mathcal X$，把 $B$ 看作经第一个投影给出的 $\mathcal X$-点，可表性给出 $B\times_{\mathcal X\times_S\mathcal X}\mathcal X$ 是概形，故 $\Delta$ 可表。  
   为什么：反向只用到「可表性沿概形基变换封闭」，与正向是同一套形式推演。

缺口：讲义只写出「$\Delta$ 可表 $\Rightarrow$ 每个 $B\to\mathcal X$ 可表」这一方向（式 (2.50)–(2.51)）；反向与 $\operatorname{Iso}_B$ 的表示（式 (2.52)）只说「由概形表示」，没有逐点验证 2-纤维积的泛性质与 2-态射的相容性。

## 易错点

- 「$f$ 可表」是态射的性质，不是叠的性质：$\mathcal F,\mathcal G$ 一般都不是概形，也不需要是概形，可表性说的是「沿概形看 $f$ 局部是概形成分」。
- 严格说纤维积只在 2-范畴意义下交换（相差一个 2-态射，见讲义 Warning 2.1）：所以「$B\times_{\mathcal G}\mathcal F$ 是概形」应读作「同构于某个 $\underline E$」，不能要求图表严格交换。
- DM 定义里的三条（$\Delta$ 可表、拟紧、分离）是一条整体的要求：只验证「同构函数是层」不够，还要 $\Delta$ 的紧性、分离性与平展图册。
- 「可表」在本章既指可表函子（模函数被 $\operatorname{Hom}$ 表示）也指可表态射（纤维积是概形）。译稿的校订建议把后者统一改为「可表示态射」；本卡沿用本章译名「可表态射」，但引用时注意区分。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 2 章 §2 叠（可表态射），p.34–35（原书 p.34）

关联：`siebert/concept/etale-local`、`siebert/concept/deligne-mumford-stack`、`siebert/deriv/dm-stack-from-groupoid`

来源说明：原书 p.34–35 §2（定义 2.7、定义 2.8、例 2.19–2.21、命题 2.4、式 (2.46) 与 (2.50)–(2.52)）。术语与性质的定义按 nLab「representable morphism of stacks」（last revised 2012-11-07）与 Stacks Project tag 03HA（§67.3 Properties of representable morphisms）、tag 03YJ（§94.10 Properties of morphisms representable by algebraic spaces）核对。
