# Deligne–Mumford 叠

> `siebert/concept/deligne-mumford-stack` ｜ track B ｜ draft

**一句话**：对角可表、拟紧分离、带平展图册的代数叠；稳定曲线的模叠是典型例子，其自同构群有限。

**自测**：为什么稳定曲线的模空间必须是 DM 叠，而不能只是一个概形或 Artin 叠？

## 定义

代数叠 $F\to(\Sch/S)$ 称为 Deligne–Mumford 叠，若 (1) 对角 $\Delta_F:F\to F\times_SF$ 可表、拟紧、分离；(2) 存在平展满射 $U\to F$，$U$ 为概形（平展图册）（Def 2.9）。等价判别（Thm 2.6）：在 Noether 基上带有限型光滑图册的代数叠是 DM $\iff$ $\Delta_F$ 非分歧。

记号：$\Mbar_g$ 记亏格 $g$ 稳定曲线的模叠；$H_{g,n}$ 记稳定 $n$-典范曲线的 Hilbert 概形；$PGL(N+1)$ 作用在 $H_{g,n}$ 上；$\omega_{C/S}$ 相对对偶层。

## 要点

- 三个条件各司其职：对角可表让 $\Iso$ 有几何意义；拟紧防 $\Iso$ 失控；分离保证『一般点恒等 $\Rightarrow$ 恒等』。
- 平展图册 $\Rightarrow$ $\Delta$ 非分歧 $\Rightarrow$ 自同构离散；再加有限型 $\Rightarrow$ 自同构有限。只有光滑图册则是 Artin 叠（$BG$ 当 $G$ 正维数就是这样，其对角不非分歧）。
- 稳定曲线（Def 2.10）：固有平坦、几何纤维约化连通一维、奇点至多结点，且每个光滑有理分支正规化后至少 3 个特殊点；不许光滑亏格 0/1。
- 稳定性 $\iff$ 自同构有限（Note 2.9），这正是 DM 的实质：模叠的每个点都有有限自同构群，故可以用平展图册描述。
- $\Mbar_g\cong[H_{g,n}/PGL(N+1)]$（Thm 2.10）；Cor 2.11 给出有限型分离 DM，Thm 2.13 给出固有；边界是正规交叉除子、有 $\lfloor g/2\rfloor+1$ 个不可约分支（Thm 2.15）。

## 公式

$$\Mbar_g\cong[H_{g,n}/PGL(N+1)],\qquad N=(2n-1)(g-1)-1$$
$$P_{g,n}(t)=(2nt-1)(g-1)\qquad(\text{稳定曲线的 Hilbert 多项式})$$
$$\pi_*\bigl(\omega_{C/S}^{\otimes n}\bigr)\ \text{局部自由，秩}\ (2n-1)(g-1)$$

## 定理与证明

### Thm 2.6：DM 的判别

设 $F$ 是 Noether 概形 $S$ 上有限型的代数叠，带光滑图册。则 $F$ 是 DM 叠 $\iff$ $\Delta_F$ 非分歧。

（sketch；来源：原书 p.36（Thm 2.6））

1. 先证 $\Delta$ 可表 $\iff$ 每个从概形到 $F$ 的态射可表（Prop 2.4）；这给出对角可表这一条。  
   为什么：对角可表是 DM 定义的第一条，判别定理要把它与更易验证的条件挂钩。
2. 光滑图册 $U\to F$ 使 $U\times_FU\to U\times U$ 成为群胚，$\Delta$ 的非分歧性等价于这个群胚态射的非分歧性。  
   为什么：图册把叠的问题拉回到概形上的群胚，非分歧性是可逐点检验的。
3. 非分歧 $\Rightarrow$ 稳定子有限 $\Rightarrow$ 可换成平展图册（把 $U$ 换成稳定子作用的商/平展局部截面）。  
   为什么：这一步是 DM 叠『存在平展图册』的来源：光滑图册加非分歧对角可以精化成平展图册。

缺口：讲义给判别与证明思路，未写出第 3 步的平展化细节。

### Cor 2.11 + Thm 2.13：$\Mbar_g$ 是固有分离有限型 DM 叠

$\\Mbar_g$ 是有限型、分离的 DM 叠，且固有。

（sketch；来源：原书 p.39–41（Cor 2.11、Thm 2.13–2.15））

1. $\Mbar_g\cong[H_{g,n}/PGL(N+1)]$：稳定曲线的 $n$-典范嵌入使其成为 Hilbert 概形的点，$PGL$ 作用对应坐标变换（Thm 2.10）。  
   为什么：这一步把抽象模问题变成具体的商叠，从而可以谈有限型与分离性。
2. 对角非分歧来自稳定性 $\Rightarrow$ 自同构有限（Note 2.9）；配合有限型与 $PGL$ 的平坦性得 DM。  
   为什么：稳定曲线的自同构有限是『稳定性』定义的设计目的。
3. 固有性用赋值判别 + 稳定约化定理（Thm 2.14）：任意一族曲线的极限可经消解、基变换、正规化、收缩不稳定有理分支化为稳定曲线。  
   为什么：没有稳定约化，模空间的边界就补不全，$\Mbar_g$ 不会固有。

缺口：稳定约化定理（Thm 2.14）讲义只给陈述与证明梗概；固有性的赋值判别细节未展开。

## 易错点

- 平展图册不能换成光滑图册：光滑图册只给 Artin 叠，$BG_m$ 就是这样，它的对角不非分歧、自同构是一维的。
- DM 的自同构群是有限群，不是代数群；这是 $\Delta$ 非分歧的直接推论，不是额外假设出来的。
- $\Mbar_g$ 的点是稳定曲线的同构类；把『点』当成曲线本身会漏掉自同构与坐标变换，也就无法解释为什么它是叠而不是概形。
- 亏格 0/1 的光滑曲线被排除，是因为 $\Aut$ 无限（$\GG_m$ / 椭圆曲线的平移），不是因为它们不连通或不可约。
- 边界 $\partial\Delta$ 是正规交叉除子且有 $\lfloor g/2\rfloor+1$ 个不可约分支（Thm 2.15）；不要写成 $g-1$ 个。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 2 章 §2 叠，p.35–36（原书 p.35–36）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 2 章 §3 稳定曲线，p.36–41（原书 p.36–41）

关联：`siebert/concept/stack`、`siebert/concept/gromov-witten-invariant`、`siebert/concept/virtual-fundamental-class`

来源说明：原书 p.35–41（Def 2.9、Prop 2.4、Note 2.6、Thm 2.6、Cor 2.7、Def 2.10、Note 2.9、Thm 2.8、Thm 2.10、Cor 2.11、Thm 2.13–2.15）。nLab「Deligne-Mumford stack」（last revised 2023-04-16）与「moduli space of curves」（2026-03-02）核过术语；Stacks Project Ch. 94「Algebraic Stacks」(tag 026K)、Ch. 109「Moduli of Curves」(tag 0DMG)、Ch. 101「Morphisms of Algebraic Stacks」(tag 04XM) 已核对章节标题（026K 页内未命中『Deligne-Mumford』，故未声称某节即 DM 定义）。
