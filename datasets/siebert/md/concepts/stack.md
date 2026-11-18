# 叠

> `siebert/concept/stack` ｜ track B ｜ draft

**一句话**：群胚值的平展层：既记住对象也记住对象间的同构；模问题里同构类集合不可表，正是靠它救回来。

**自测**：为什么『同构类』的模函子不可表，换成叠之后就能谈模空间？

## 定义

概形范畴上的叠是一个纤维群胚 $p:F\to(\Sch/S)$，满足：(1) 对每个概形 $B$，$B\mapsto\Iso_{F(B)}(X|_B,X'|_B)$ 是平展拓扑的层（态射的下降）；(2) 对象满足平展下降：给定平展覆盖 $\{B_i\to B\}$、对象 $X_i\in F(B_i)$ 与余循环同构 $\varphi_{ij}$，存在 $X\in F(B)$ 连同同构 $X|_{B_i}\cong X_i$（Def 2.5）。等价地，$F$ 是群胚值的平展层。

记号：$F(B)$ 记 $B$ 上的对象群胚；$[X/G]$ 记商叠；$BG=[\mathrm{pt}/G]$；$\Iso_B(X,X')$ 记 $B$ 上从 $X$ 到 $X'$ 的同构函子。

## 要点

- 动机：$F_g$（曲线的同构类）不可表，因为存在非平凡但等平凡的族（例 2.3 用 $(C_0	imes\GG_m)/(\ZZ/a)$ 造）；把对象换成曲线族、态射换成族同构，得模群胚 $M_g$，它才是叠。
- 可表函子只是叠的特例：$\Hom_S(-,X)$ 是叠（例 2.16），且函子给出的群胚是叠 $\iff$ 该函子是平展层。
- 商叠 $[X/G]$：对象是 $G$ 主丛 $E/B$ 加 $G$ 等变映射 $E	o X$；当作用自由且商存在时 $[X/G]\cong X/G$（p.27）。
- 两条下降条件不能合并：态射的下降（$\Iso$ 是层）与对象的下降是独立的两条（Note 2.7）；$F_g$ 不是层，故不是叠。
- 纤维积只在 2-范畴意义下交换（Warning 2.1）：对象是三元组 $(x,y,\psi:f(x)	o h(y))$，这正是必须引入 2-态射的原因。

## 公式

$$\Iso_B(X,X'):(\Sch/S)^{op}\to\Set,\qquad B\mapsto\Iso_{F(B)}(X|_B,X'|_B)$$
$$\Hom_S(B,F)\simeq F(B)\qquad(\text{Yoneda})$$
$$\Hom_{F\times_HG}(b)=(x,y,\psi:f(x)\to h(y))$$

## 定理与证明

### Prop 2.3：商叠 $[X/G]$ 是叠

设 $G$ 是平坦、仿射、分离的 $S$-群概形，$G$ 作用在 $X$ 上，则 $[X/G]$ 是叠；且 $\Iso_B(f,f')\cong B\times_{X\times_SX}(G\times_SX)$。

（complete；来源：原书 p.33（Prop 2.3、2.46））

1. $[X/G](B)$ 的对象是 $G$ 主丛 $E	o B$ 连同等变映射 $f:E	o X$；同构是 $G$-等变主丛同构 $\varthetaarphi:E	o E'$ 使 $f'\circ\varphi=f$。  
   为什么：这是商叠的标准定义：把 $X$ 换成『$X$ 的 $G$-扭转』。
2. 给定 $f,f':E	o X$，同构 $f	o f'$ 的数据是 $g\in G$ 使 $f'=g\cdot f$（逐点看，$f'\circ\varphi=f$ 且 $\varphi$ 是主丛自同构）。  
   为什么：主丛自同构对应 $G$ 的『扭转』，故同构空间是 $G\times X$ 被 $X\times X$ 拉回。
3. $\Iso_B(f,f')\cong B\times_{X\times_SX}(G\times_SX)$ 是概形的纤维积，故是层；对象下降用主丛的平展下降逐项验证。  
   为什么：主丛在平展拓扑下可下降，等变映射也随之下降，两条条件都成立。

### Thm 2.2（Deligne–Mumford）：亏格 2 曲线族的 Iso 可表

对 $S$ 上亏格 2 的曲线族 $X,X'$，$\Iso_B(X,X')$ 被一个概形表示。

（sketch；来源：原书 p.31–32（Thm 2.2、Note 2.6））

1. 用相对典范丛 $\omega_{X/B}$ 作极化：亏格 2 时 $\omega^{\otimes3}$ 相对甚丰，故曲线的同构可由其在 $\PP^N$ 中的像决定。  
   为什么：亏格 $\ge2$ 的曲线没有自然的嵌入，必须借助典範丛的高次幂做成射影嵌入。
2. 把图像参数化：$X$ 与 $X'$ 在 $\PP^N$ 中的图像是相对 Hilbert 概形的点，同构对应图像相等的点。  
   为什么：相对 Hilbert 概形是概形，这就把 Iso 函子变成可表函子的子函子。

缺口：讲义只给证明思路，并指出 Note 2.6：Iso 有限、非分歧，但不必平坦。

## 易错点

- 叠取值在群胚而不是集合：$F(B)$ 里的对象有自同构，忘掉它们（取同构类）就退化成不可表的函子（$F_g$ 就是反例）。
- 『层』是平展拓扑的层，不是 Zariski 层；fppf/fpqc 下降也能用，但讲义固定平展拓扑，混用会让『对象下降』的形式不同。
- 纤维积是 2-纤维积，只 2-交换；写成严格交换会丢掉 $\psi:f(x)\to h(y)$ 这一项（Warning 2.1）。
- $F_g$ 不是叠（它不是层），$M_g$ 才是；两者差的就是自同构，不要把它们当成同一个东西的不同写法。
- 叠的『点』不是集合论的点：$\Spec k\to F$ 对应 $F(k)$ 中的对象，可能带非平凡自同构群。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 2 章 §1 模空间，p.24–26（原书 p.24–26）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 2 章 §2 叠，p.26–34（原书 p.26–34）

关联：`siebert/concept/deligne-mumford-stack`、`siebert/concept/virtual-fundamental-class`

来源说明：原书 p.24–34（Def 2.1、2.5，Prop 2.1/2.3，Warning 2.1，Note 2.7，例 2.3、2.16–2.17）。nLab「stack」（last revised 2025-11-04）与「algebraic stack」（2023-04-16）核过术语；Stacks Project Ch. 8「Stacks」(tag 0266)、Ch. 94「Algebraic Stacks」(tag 026K)、Ch. 95「Examples of Stacks」(tag 04SL) 已核对章节标题（未逐节比对内容）。
