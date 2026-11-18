# 镜像五次超曲面

> `siebert/concept/mirror-quintic` ｜ track A ｜ draft

**一句话**：把 Fermat 五次对 (Z/5)³ 取商再消解奇点，得 h^{1,1}=101、h^{2,1}=1 的流形；100 个例外除子来自 10 条曲线与 10 个点。

**自测**：为什么要先取 (Z/5)³ 商再吹起奇点，才能得到 h^{1,1}=101 的镜像？

## 定义

设 $X=\{x_0^5+\cdots+x_4^5=0\}\subset\PP^4$ 为 Fermat 五次。对角子群 $(\ZZ/5)^5\subset\PGL(5)$ 在 $X$ 上的作用是有效的 $(\ZZ/5)^4$；取 $G=(\ZZ/5)^3\subset(\ZZ/5)^4$，商 $\overline Y=X/G$ 是轨形（orbifold）。取射影消解 $Y\to\overline Y$（Prop 1.2），所得光滑三维流形 $Y$ 称为镜像五次超曲面，它满足 $h^{1,1}(Y)=101$、$h^{2,1}(Y)=1$（Prop 1.3）。

记号：$\zeta=e^{2\pi i/5}$；$\overline Y$ 记轨形商，$Y$ 记其光滑消解；$z=(5\psi)^{-5}$ 是族参数；$\beta_0,\beta_1,\alpha_1,\alpha_0$ 是 $H_3$ 的辛基。

## 要点

- 稳定子只有两种：$\{x_i=x_j=0\}$ 处稳定子为 $\ZZ/5$，得到五次曲线 $\widetilde C_{ij}$（共 $inom52=10$ 条，每条 $\cong\PP^1$）；$\{x_i=x_j=x_k=0\}$ 处稳定子为 $(\ZZ/5)^2$，得到点 $\widetilde P_{ijk}$（共 $inom53=10$ 个）。
- 局部模型：沿 $C_{ij}$ 奇点型为 $\CC^2/(\ZZ/5)$ 即 $A_4$ 曲面奇点 $uv=w^5$，其极小消解给出 4 个例外除子（一条链 $E_0,\ldots,E_3$）；在 $P_{ijk}$ 处给出 6 个。合计 $4\cdot10+6\cdot10=100$。
- 这 100 个例外除子与超平面类一起生成 $H^2(Y)$，故 $h^{1,1}(Y)=100+1=101$；同为镜像的 $h^{2,1}(Y)=1$（Prop 1.3，Roan 的直接计算与 Batyrev 的环面方法）。
- 单参数 Dwork 族：$f_\psi=\sum x_i^5-5\psi x_0x_1x_2x_3x_4$，$z=(5\psi)^{-5}$；$\psi\mapsto\zeta\psi$ 是自同构，故 $Y_\psi\cong Y_{\zeta\psi}$，族实际是商族。
- 三个特殊纤维：$z=0$ 五个坐标超平面之并（$\cup\,\PP^3_i$）；$\psi=1$（$z=5^{-5}$）处 125 个三维 $A_1$ 奇点落在同一 $(\ZZ/5)^3$ 轨道，故 $Y$ 上只剩一个 conifold；$\psi=0$（$z=\infty$）是 Fermat 点，多出 $\ZZ/5$ 对称，对应轨形点。

## 公式

$$\overline Y=X/(\ZZ/5)^3,\qquad 4\cdot10+6\cdot10=100,\qquad h^{1,1}(Y)=100+1=101$$
$$f_\psi=\sum_{i=0}^4x_i^5-5\psi\,x_0x_1x_2x_3x_4,\qquad z=(5\psi)^{-5}$$
$$uv=w^5\ \ (A_4)\ \rightsquigarrow\ 4\ \text{个例外除子};\qquad \CC^3/(\ZZ/5)^2\ \rightsquigarrow\ 6\ \text{个}$$

## 定理与证明

### Prop 1.2：射影消解的存在

轨形 $\overline Y=X/(\ZZ/5)^3$ 存在射影消解 $Y\to\overline Y$。

（sketch；来源：原书 p.16）

1. $\overline Y$ 只有商奇点，逐点做极小消解（$A_4$ 曲面奇点与三维 $(\ZZ/5)^2$ 商奇点）。  
   为什么：商奇点在局部是 $\CC^n/\ZZ/5$ 型，有已知的极小消解。
2. 把局部消解粘成整体并射影化，得到 $Y	o\overline Y$。  
   为什么：消解在轨形点上局部进行，粘合需要检查过渡函数的一致性与射影性。
3. 还需论证 $Y$ 上存在丰线丛：吹起后超平面类未必仍丰，须用相对丰的论证补上。  
   为什么：这正是讲义特别强调的『吹起后未必仍丰』的技术点；没有它就不能把 $Y$ 当作射影流形用。

缺口：讲义只给论证思路与结论，未写出 $Y$ 上丰线丛的显式构造。

### Prop 1.3：镜像的 Hodge 数

$h^{1,1}(Y)=101$、$h^{2,1}(Y)=1$。

（sketch；来源：原书 p.16）

1. 数例外除子：10 条 $C_{ij}$ 各贡献 4 个，10 个 $P_{ijk}$ 各贡献 6 个，共 100 个。  
   为什么：每个例外除子是 $Y	o\overline Y$ 的爆破中心上的 $\PP^1$-丛或 $\PP^2$-丛，其个数由奇点类型决定。
2. 证明这 100 个除子与超平面类张成 $H^2(Y)$（无关性 + 生成性）。  
   为什么：只数除子不给 $h^{1,1}$；必须先证明它们在 $H^2$ 中线性无关且生成整个 $H^2$。
3. $h^{2,1}(Y)=1$ 由消解后 $H^3$ 的维数（或 Batyrev 的环面公式）给出。  
   为什么：镜像的 $h^{2,1}$ 必须等于原五次超曲面的 $h^{1,1}=1$，这是镜像对称的预言，也是检验构造正确性的判据。

缺口：讲义列出 Roan 的直接计算与 Batyrev 的环面方法两条路线，均未展开细节。

## 易错点

- $(\ZZ/5)^3$ 商之后 $\overline Y$ 只是轨形：必须先消解奇点才有 $h^{1,1}=101$；直接在轨形上数 Hodge 数是错的。
- 100 个例外除子加上 1 个超平面类等于 101，但『100』本身不是 $h^{1,1}$：还要证明这些类线性无关且生成 $H^2$（Prop 1.3 的内容）。
- $\psi=1$ 处的 125 个三维 $A_1$ 奇点在同一个 $(\ZZ/5)^3$ 轨道里，故在 $Y$ 上只对应一个 conifold；不要数成 125 个奇点。
- $z$ 的指数是 $(5\psi)^{-5}$ 而不是 $(5\psi)^{-1}$；$z=0$ 对应 $\psi=\infty$（大复结构极限），$z=\infty$ 才是 Fermat 点。
- $G=(\ZZ/5)^3$ 而不是 $(\ZZ/5)^4$：$(\ZZ/5)^5$ 的对角子群在 $\PP^4$ 上作用平凡，故有效群是 $(\ZZ/5)^4$，镜像再取其中三维子群。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 1 章 §5 镜像五次超曲面，p.15–16（原书 p.15–16）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 1 章 §6 Yukawa 耦合，p.17–17（原书 p.17）

关联：`siebert/concept/quintic-threefold`、`siebert/concept/picard-fuchs-equation`、`siebert/concept/mirror-symmetry`

来源说明：原书 p.15–16（1.20–1.46、Note 1.1、Prop 1.2–1.3、Dwork 族与特殊纤维）、p.17（族与镜像陈述）。nLab 无 mirror quintic / quintic 条目（试 mirror+quintic、quintic+hypersurface 均 404）；nLab「mirror symmetry」（last revised 2024-04-01）与「Calabi-Yau variety」（2026-01-06）只有一般讨论。Stacks Project 无对应章节。
