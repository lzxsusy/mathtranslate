# 障碍理论与余切复形

> `siebert/concept/obstruction-theory` ｜ track C ｜ draft

**一句话**：把形变与障碍线性化为两项局部自由复形到余切复形的态射；$h^0$ 同构、$h^{-1}$ 满射，虚拟维数就是这两项的秩差。

**自测**：障碍理论为什么必须用余切复形 $L^\bullet_{X/Y}$，而不能直接用相对微分模 $\Omega_{X/Y}$？

## 定义

先在局部理解：把 $U\subset M$ 嵌入光滑空间 $V$（相对某个基），得到理想层 $\mathcal I$；法锥 $C_{U/V}=\Spec_U\bigoplus_{m\ge0}\mathcal I^m/\mathcal I^{m+1}$ 落在 $N_{U/V}=\Spec_U\Sym^\bullet(\mathcal I/\mathcal I^2)$ 里，而 $T_V|_U$ 的加法作用保持 $C_{U/V}$ 不变。要把这个作用整体化，就取 $N_{U/V}\hookrightarrow E_1$ 与粘合数据 (3.70)，并要求 $T_V|_U\to E_0\oplus N_{U/V}\to E_1\to0$ 正合 (3.71)。用导出范畴的语言就是：$\tau_{\ge-1}L^\bullet_{X/Y}=[\mathcal I/\mathcal I^2\to\Omega_{Z/Y}|_X]$（式 (3.84)，两项在次数 $-1,0$），其对偶的线性纤维空间正是 $[T_{Z/Y}|_X\to N_{X/Z}]$。完美障碍理论（Def 3.5）指的是：两项局部自由凝聚层复形 $\mathcal F^\bullet=[\mathcal F^{-1}\to\mathcal F^0]$ 连同 $\DQCoh(\OO_X)$ 中的态射 $\phi^\bullet:\mathcal F^\bullet\to L^\bullet_{X/Y}$，使 $h^0(\phi^\bullet)$ 为同构、$h^{-1}(\phi^\bullet)$ 为满射。

记号：$L^\bullet_{X/Y}$ 余切复形；$\tau_{\ge-1}$ 截断（只留次数 $-1,0$）；$\DQCoh(\OO_X)$ 拟凝聚层导出范畴；$\mathcal F^\bullet$ 障碍理论复形；$F_i=L(\mathcal F^{-i})=\Spec_X\Sym^\bullet\mathcal F^{-i}$ 对应的线性纤维空间；$\mathrm{Ob}(h)\in\Ext^1(Lh^*L_{X/Y},\mathcal I)$ 提升障碍类。

## 要点

- 为什么不用 $\Omega_{X/Y}$：一般情况下 $f^*\Omega_Y\to\Omega_X$ 不是单射，$\Omega_{X/Y}$ 不再正确刻画形变；必须换成复形 $L^\bullet_{X/Y}$ 并把正合三角 (3.73) 接上去（原书 p.52–53）。
- 为什么只取截断：$L^\bullet_{X/Y}$ 一般有无穷多项，但障碍理论只用到 $h^{-1}$ 与 $h^0$；局部嵌入光滑的 $Z$ 给出两项模型 (3.84)，所以「两项局部自由」不是额外限制而是可计算性要求（原书 p.53）。
- 障碍类是 Ext 类而不是上同调类：对平方零扩张 $T\hookrightarrow\overline T$（$\mathcal I^2=0$）的提升问题，$\mathrm{Ob}(h)=[Lh^*L_{X/Y}\to L_{T/\overline T}\to\tau_{\ge-1}L_{T/\overline T}=\mathcal I[1]]\in\Ext^1(Lh^*L_{X/Y},\mathcal I)$（式 (3.99)），且 $\mathrm{Ob}(h)=0$ 当且仅当提升存在、提升构成 $\Ext^0$-挠子（事实 2，原书 p.55）。
- $h^0$ 同构与 $h^{-1}$ 满射各管一件事：$h^0$ 同构让一阶形变空间与 $F_0$ 对得上，$h^{-1}$ 满射让障碍空间被 $F_1$「盖住」；两条一起才能把 $L^\bullet$ 的两项上同调搬进有限秩（原书 p.54）。
- 两条并行路线：Artin 风格的障碍理论（讲义引 [ref21]）与余切复形/导出范畴路线（[ref3] 即 Behrend–Fantechi）。讲义选后者，因为它顺势给出内蕴法锥与虚拟基本类（原书 p.52）。
- 存在的意义是可算的维数：$\dim^{virt}=\rank F_0-\rank F_1+\dim Y$（式 (3.115)），即形变空间减障碍空间的秩差；模空间的实际维数不可控，秩差可控。

## 公式

$$T_V|_U\longrightarrow E_0\oplus N_{U/V}\longrightarrow E_1\longrightarrow0$$
$$\cdots\longrightarrow Lf^*L_Y^\bullet\longrightarrow L_X^\bullet\longrightarrow L_{X/Y}^\bullet\longrightarrow Lf^*L_Y^\bullet[1]\longrightarrow\cdots$$
$$\tau_{\ge-1}L_{X/Y}^\bullet=\bigl[\mathcal I/\mathcal I^2\longrightarrow\Omega_{Z/Y}|_X\bigr]$$
$$\mathrm{Ob}(h)\in\Ext^1(Lh^*L_{X/Y}^\bullet,\mathcal I)$$
$$\dim^{virt}=\rank F_0-\rank F_1+\dim Y$$

## 定理与证明

### 事实 2：障碍类为零当且仅当提升存在

对平方零扩张 $T\hookrightarrow\overline T$ 与图式 (3.98)，$\mathrm{Ob}(h)=0$ 当且仅当提升 $\widetilde g$ 存在；此时提升在同构意义下构成 $\Ext^0(Lh^*L_{X/Y},\mathcal I)$-挠子。

（sketch；来源：原书 p.55（式 (3.98)(3.99)、事实 2））

1. 把提升问题写成本源图式 (3.98)：$T\to X$、$\overline T\to Y$ 给定，问虚线 $\widetilde g$ 是否存在。  
   为什么：障碍理论的名称就来自这类问题；没有它，「障碍」只是一堆线性代数。
2. 用 $L^\bullet$ 的函子性把两个映射拼成 $Lh^*L_{X/Y}\to L_{T/\overline T}\to\mathcal I[1]$，得到 $\Ext^1$ 类 $\mathrm{Ob}(h)$（式 (3.99)）。  
   为什么：平方零扩张的余切复形恰是 $\mathcal I[1]$，所以提升的「差」自然落在 $\Ext^1$。
3. 该类为零 ⟺ 两个映射可同伦地接上 ⟺ 提升存在；两个提升之差给出 $\Ext^0$ 的元素，于是提升集是 $\Ext^0$-挠子。  
   为什么：同伦类正是 $\Ext$ 群；这就是「存在性由 $\Ext^1$ 控制、唯一性由 $\Ext^0$ 控制」的标准机制。

缺口：讲义以「事实」的形式陈述（custom 块 fact:2），没有给出与导出范畴函子性的逐条对照；本卡按 $\Ext$ 的标准解释补足第 3 步。

### 余切复形的两项局部模型

若 $X\hookrightarrow Z$ 是相对 $Y$ 的闭嵌入、$Z/Y$ 光滑，$\mathcal I=\mathcal I_{X/Z}$，则 $\tau_{\ge-1}L^\bullet_{X/Y}=[\mathcal I/\mathcal I^2\to\Omega_{Z/Y}|_X]$（次数 $-1$ 与 $0$ 两项）；对偶地得到线性纤维空间 $[T_{Z/Y}|_X\to N_{X/Z}]$。

（none；来源：原书 p.53（式 (3.84)(3.85)））


缺口：讲义在 (3.72)–(3.74) 之后直接给出该局部模型（式 (3.84)）并说明它对偶后就是把 $C_{X/Z}\hookrightarrow N_{X/Z}$ 整体化所需的数据，未在此重证；完整证明属余切复形的一般理论（Stacks Chapter 92）。

## 易错点

- 别把 $L^\bullet_{X/Y}$ 当成 $\Omega_{X/Y}$ 的花哨写法：$\Omega$ 只在光滑态射时才有正确的形变意义，一般情形必须用复形。
- 截断不能省：完整的 $L^\bullet$ 有无穷多项，随手「取两项」通常得到错误的复形；式 (3.84) 的正确性依赖局部嵌入光滑的 $Z$。
- 两条条件方向不同：$h^0$ 要求同构（形变空间完全对上），$h^{-1}$ 只要求满射（障碍空间可以偏大）。若把 $h^{-1}$ 也要求成同构，就只剩 lci 情形。
- 障碍类住在 $\Ext^1$ 而不是某个 $H^1$：它依函数于 $\mathcal I$，换扩张就换类。
- 完美障碍理论不唯一：不同的 $\phi^\bullet$ 给出不同的 $C_{\phi^\bullet}$ 与不同的虚拟类，所以「虚拟类」总带着所选的 $\phi^\bullet$。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 3 章 §4 障碍理论与虚拟基本类，p.52–53（原书 p.52）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 3 章 §4 障碍理论与虚拟基本类，p.53–54（原书 p.53–54）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 3 章 §4 障碍理论与虚拟基本类，p.55–55（原书 p.55）

关联：`siebert/concept/intrinsic-normal-cone`、`siebert/concept/virtual-fundamental-class`、`siebert/deriv/behrend-fantechi`、`siebert/concept/gysin-map`

来源说明：原书 p.52–55 §4.1–4.3（基本思想、余切复形补充 (3.72)–(3.85)、Def 3.5、提升问题与事实 2）。nLab「cotangent complex」（last revised 2020-02-24：左导出函子、平方零扩张与切范畴）与「perfect obstruction theory」（2019-04-08：由 Behrend–Fantechi 引入）核过术语与条件；Stacks tag 08P5（Chapter 92 The Cotangent Complex）与 08G4（§21.47 Perfect complexes）核过「完美复形」一节的存在与定位（未逐条比对证明）。
