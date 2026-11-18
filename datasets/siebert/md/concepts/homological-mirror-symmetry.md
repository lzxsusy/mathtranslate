# 同调镜像对称

> `siebert/concept/homological-mirror-symmetry` ｜ track F ｜ draft

**一句话**：D^bF(X)≃D^b(Y) 的 A∞ 等价：不止 Yukawa 耦合相等，而是整个导出范畴等价，故所有关联量自动匹配。

**自测**：同调镜像对称比数值镜像对称强在哪里？

## 定义

设 $(X,\omega)$ 紧 Calabi–Yau，$Y/S$ 是其镜像的极大退化族，$S=\Spec K$、$K=\Lambda_{nov,\CC}$。同调镜像对称断言存在典范的 A∞ 范畴等价\n$$\psi:D^b\mathcal F(X)=H^0(\mathrm{Tw}^\Pi\mathcal F(X))\xrightarrow{\sim}D^b(Y)$$\n（Conj 6.18），其中 $\mathrm{Tw}^\Pi$ 是分裂闭包（扭曲复形再加幂等元的像）。

记号：$\mathcal F(X)$ Fukaya 范畴；$\mathrm{Tw}^\Pi$ 分裂闭包；$D^b$ 有界导出范畴；$K=\Lambda_{nov,\CC}$ Novikov 域。

## 要点

- 比数值强：数值镜像只要求一个函数（Yukawa 耦合）相等；HMS 给的是范畴等价，由此所有 GW 不变量、高阶 A∞ 运算、开弦不变量都自动匹配。
- 历史：Kontsevich 1994 报告（p.9）；Givental 1996 证超曲面数值情形；Seidel 2003 证 $\PP^3$ 四次超曲面的 HMS；Sheridan 2011 证所有 CY 超曲面（p.9）。
- 为什么必须导出化 + 完备化：$\mathcal F(X)$ 只有 A∞ 结构、不是三角范畴；要 $\mathrm{Tw}$ 成三角 A∞ 范畴、取 $H^0$、再加幂等元像，才能与导出范畴比较。
- B 侧是 $D^b(Y)$ 而不是 $D^b(\mathcal O_X)$：$Y$ 定义在 Novikov 域上（极大退化族的基），不是原来的复流形；系数域必须是 Novikov 域，因为圆盘面积可任意小。
- Polishchuk 刚性（Thm 6.4）：对 $A_L=\oplus_{p,q}H^p(X,L^q)$，保内部次数、扩 $m_2$ 的非平凡极小 A∞ 结构在严格同构（$f_1=\id$）与缩放下唯一；故 HMS 的内容集中在 Hochschild 类 $[m_{d+2}]\in HH^{d+2}_{0,d}$（Cor 6.6）。

## 公式

$$\psi:D^b\mathcal F(X)=H^0(\mathrm{Tw}^\Pi\mathcal F(X))\xrightarrow{\sim}D^b(Y)$$
$$A_L=\bigoplus_{p,q\in\ZZ}H^p(X,L^q),\qquad \langle L\rangle\ \text{分裂生成}\ D^b(X)$$
$$\dim HH^{d+2}_{0,d}(A_L)\le1,\qquad [m_{d+2}-m'_{d+2}]=0\iff\text{严格 A∞ 同构}$$

## 定理与证明

### Conj 6.18：HMS 的精确陈述

$(X,\omega)$ 紧 Calabi–Yau，$Y/S$ 为镜像极大退化族，$K=\Lambda_{nov,\CC}$。则存在典范 A∞ 等价 $\psi:D^b\mathcal F(X)\xrightarrow{\sim}D^b(Y)$。

（none；来源：原书 p.100（Conj 6.18）、p.9）


缺口：对一般 CY 仍是猜想；已证情形：椭圆曲线（Polishchuk）、$\PP^3$ 四次超曲面（Seidel 2003）、所有 CY 超曲面（Sheridan 2011），见 p.9。

### Thm 6.4：Polishchuk 刚性

$X$ 射影、$\dim X=d\ge1$、$L$ 甚丰且 $H^q(X,L^{\otimes p})=0$（$q\ne0,d$）。则 $A_L$ 上保内部次数、扩既定 $m_2$ 的非平凡极小 A∞ 结构在严格 A∞ 同构（$f_1=\id$）与缩放下唯一；两结构间的严格同构在同伦意义下唯一。

（sketch；来源：原书 p.103–106（Thm 6.4、Prop 6.5、Cor 6.6））

1. 把两个 A∞ 结构逐阶比较：设到 $n-1$ 阶相同，则 $c=m_n-m'_n$ 是 Hochschild $n$-上闭链，且落在 $C^n_{0,n-2}$（6.50）。  
   为什么：A∞ 关系相减后只剩这些项，故差是一个上闭链。
2. Prop 6.5：$i<l(d+2)$ 时 $HH^i_{0,ld}(A)=0$，且 $\dim HH^{d+2}_{0,d}(A)\le1$；故 $l>1$ 的差自动可消去，只有 $n=d+2$ 可能留下非平凡类。  
   为什么：Hochschild 上同调的消失范围决定了哪些阶的差异能被吸收。
3. Cor 6.6：两结构严格同构 $\iff$ $[m_{d+2}-m'_{d+2}]=0\in HH^{d+2}_{0,d}(A)$；由 $\dim\le1$，非零类在缩放意义下唯一。  
   为什么：一维上同调群意味着只剩一个可调参数，对应『缩放』这一自由度。

缺口：Prop 6.5 的证明用 Polishchuk 的 bar 复形计算（Lemma 6.7 + 谱序列），讲义只给归纳思路。

## 易错点

- 讲义 (0.12) 把 HMS 写成 $D\,\mathrm{Fuk}(X)=D^b(\mathcal O_Y)$，这是幻灯片简写：严格版本要 $H^0(\mathrm{Tw}^\Pi\mathcal F(X))$、系数取 Novikov 域、右边是 $D^b(Y)$ 而非 $D^b(\mathcal O_Y)$。
- 漏掉幂等完备化 $\mathrm{Tw}^\Pi$ 会得到错误的等价：分裂闭包不是可选装饰，它让扭曲 Fukaya 范畴成为三角范畴。
- B 侧对象是 $Y$ 上凝聚层的复形，不是 $Y$ 的点；把 HMS 说成『点对应 Lagrange 子流形』只在 SYZ 图像下成立（p.9 只提 SYZ 纤维化，未展开）。
- 系数域必须含 Novikov 形式参数；直接取 $\CC$ 会让圆盘计数不收敛，等价也就不成立。
- HMS 是亏格零（开弦）的陈述；高亏格 GW/开弦理论讲义明确说还没有定义（p.95 脚注），不要把它推广到高亏格。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，概览 §1 计数镜像对称，p.9–9（原书 p.9）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 6 章 §1 概览，p.95–100（原书 p.95–100）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 6 章 §3 Polishchuk 的刚性定理，p.103–106（原书 p.103–106）

关联：`siebert/concept/fukaya-category`、`siebert/concept/mirror-symmetry`、`siebert/concept/calabi-yau-manifold`

来源说明：原书 p.9（Kontsevich 1994、Givental 1996、Seidel 2003、Sheridan 2011、SYZ）、p.95–106（Conj 6.18、Thm 6.1、Thm 6.4、Prop 6.5、Cor 6.6、Note 6.6）。nLab「mirror symmetry」（last revised 2024-04-01；homological+mirror+symmetry 重定向到该页）与「Fukaya category」（2026-01-17）核过陈述；Stacks Project 无对应章节。
