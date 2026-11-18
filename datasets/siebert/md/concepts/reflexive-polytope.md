# 反身多胞体

> `siebert/concept/reflexive-polytope` ｜ track E ｜ draft

**一句话**：内部只有原点一个格点、每个侧面到原点整距离为 1 的格多胞体；极多胞体仍是格多胞体，对应 Fano 环面簇与 Calabi–Yau 超曲面族。

**自测**：为什么『内部只有原点、侧面到原点距离为 1』这两个条件，恰好等价于极多胞体仍是格多胞体？

## 定义

设 $P\subset M_{\RR}$ 是满维格多胞体，$0\in\Int(P)$。若 (i) $\Int(P)\cap M=\{0\}$；(ii) $P$ 的每个侧面到原点的整仿射距离都是 $1$，则称 $P$ 为反身多胞体（Def 5.1）。等价地：$P$ 与极多胞体 $P^\circ=\{n\in N_{\RR}:\langle n,m\rangle\ge-1\ \text{对一切}\ m\in P\}$ 都是格多胞体。此时 $P^\circ$ 的顶点正是 $P$ 各侧面的本原法向，故 $P^\circ$ 是顶点本原的格多胞体。反身多胞体与 Fano 环面簇 $X(\Sigma_P)$、Calabi–Yau 超曲面族 $Z(s)\subset X_\Sigma$ 一一对应（Prop 5.1、§1.5）。

记号：$M,N$ 互为对偶格；$P\subset M_{\RR}$ 与 $P^\circ\subset N_{\RR}$ 互为极多胞体；$\Sigma_P$ 为在 $P^\circ$ 的面上取锥得到的扇；$\Sigma$ 为 $\Sigma_P$ 的 MPCP 细分；$D_\rho$ 为环面不变除子。

## 要点

- 两种等价写法：本章用『$0$ 是唯一内部格点 + 每个侧面到原点整距离 $1$』；Batyrev 的原始论文常用『极多胞体 $P^\circ$ 也是格多胞体』。二者由极对偶的『顶点 $\leftrightarrow$ 侧面』对应等同。
- 『顶点本原』要加在对偶这一边：$P$ 的侧面法向（即 $P^\circ$ 的顶点）自动本原，这是『距离 $1$』的直接推论；$P$ 自己的顶点不必本原，别把条件加错边。
- 分类计数：二维恰有 16 个，三维 4319 个，四维 473800776 个（Ex 5.1–5.2 与 p.81）。二维的 16 个对应 16 个 Fano 环面曲面（含轨形），低维可手工分类，四维靠计算机。
- 与 Fano 环面簇的对应（Prop 5.1）：$X(\Sigma_P)$ 是 Fano 当且仅当 $P$ 反身，此时 $K_{X(\Sigma_P)}=-\sum_\rho D_\rho$ 是 Cartier 且 $-K$ 丰。
- 与 Calabi–Yau 超曲面的对应：$P$ 的每个格点 $m\in P\cap M$ 给一个单项式截面，$\Gamma(X,-K_X)=\operatorname{Map}(P\cap M,k)$；取一般截面即得 $K_{Z(s)}=0$ 的超曲面族（式 5.3、5.5）。
- 二维的 MPCP 细分唯一（Ex 5.3 的图 5.2），三维起不唯一（Note 5.1）：同一个反身多胞体可以给出多个互为 flop 的 crepant 消解，故镜像族只在双有理意义下确定。

## 公式

$$P^\circ=\{n\in N_{\RR}:\langle n,m\rangle\ge-1\ \ \forall m\in P\},\qquad \Int(P)\cap M=\{0\}$$
$$\operatorname{dist}(F,0)=1\ \ \text{对每个侧面}\ F,\qquad K_{X(\Sigma_P)}=-\sum_{\rho}D_\rho$$
$$16\ (d=2),\quad 4319\ (d=3),\quad 473800776\ (d=4);\qquad \Gamma(X,-K_X)=\operatorname{Map}(P\cap M,k)$$

## 定理与证明

### Prop 5.1：反身多胞体对应的环面簇恰是 Fano

完备环面簇 $X$ 是 Fano 簇，当且仅当 $X\simeq X(\Sigma_P)$，其中 $P$ 是反身多胞体。

（sketch；来源：原书 p.82）

1. 在仿射图 $U=\Spec k[\sigma^\vee\cap M]$ 上 $K_U=-\sum_iD_i$：全纯体积形式沿每个环面除子恰有一阶极点。  
   为什么：这给出典范除子的显式表示，是判据的出发点。
2. $K_U$ 是 Cartier，当且仅当存在 $m_\sigma\in M$ 使每条射线的本原生成元 $v_i$ 满足 $\langle m_\sigma,v_i\rangle=1$。  
   为什么：Cartier 即 $K_U=\operatorname{div}(\chi^{m_\sigma})$ 局部为主除子。
3. 把条件译成多胞体语言：$P=\operatorname{conv}\{m_\sigma\}$，而 $\langle m_\sigma,v_i\rangle=1$ 正是每个侧面到原点整距离为 $1$，故 $P$ 反身；反过来由 $-K$ 丰可验证 $P$ 满维且侧面距离为 $1$。  
   为什么：射线的本原生成元就是侧面的法向，『配对为 1』与『距离为 1』等价。

缺口：讲义把丰性的方向（$P$ 反身 $\Rightarrow$ $-K_X$ 丰）与 Gorenstein 性合在一起带过，只详细说明了 Cartier 那一步。

### Ex 5.1–5.2 与分类计数

反身多胞体在二维恰有 16 个，三维 4319 个，四维 473800776 个；例 5.1 的一对极多胞体都只有一个内部格点。

（none；来源：原书 p.81）


缺口：分类计数是 Kreuzer–Skarke 的计算结果（Batyrev 提出后完成），讲义只引用；例 5.1 的图形在讲义中以图片给出，卡中不复制。

## 易错点

- 『顶点本原』容易加错边：本原性属于 $P^\circ$ 的顶点（$P$ 的侧面法向），$P$ 自己的顶点不必本原。
- 反身性必须同时含『唯一内部格点』与『侧面距离 1』；只满足前者（例如任意大的格多边形）不是反身。
- $P^\circ$ 的顶点是 $P$ 的侧面法向，不是『把 $P$ 旋转再缩放』得到的点；例 5.2 的正方形是恰好可这样描述的特例。
- 四维的 473800776 数的是反身多胞体，不是镜像族；每个多胞体还可能对应多个 MPCP 细分（Note 5.1）。
- $d=1$ 时只有 $[-1,1]$：距离 $1$ 的条件强制两个端点为 $\pm1$，别的区间都不反身。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 5 章 §1.1 反身多胞体的定义、例与计数，p.81–81（原书 p.81）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 5 章 §1.2 Fano 环面簇（Prop 5.1 的证明），p.82–82（原书 p.82）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 5 章 §1.4–1.5 MPCP 细分与 Batyrev 超曲面镜像，p.83–83（原书 p.83）

关联：`siebert/concept/reflexive-pair`、`siebert/concept/batyrev-mirror-construction`、`siebert/concept/crepant-resolution`、`siebert/concept/toric-variety`、`siebert/deriv/polytope-to-fan`、`siebert/concept/mirror-symmetry`

来源说明：原书 p.81–84（本章范围内）：Def 5.1、Ex 5.1–5.2、Counterexample 3、16/4319/473800776 计数（p.81）、Def 5.2 与 Prop 5.1（p.82）、图 5.1 与图 5.2（p.82、p.84，二维反身多胞体及其唯一 MPCP 细分）、Def 5.3 与 Note 5.1（p.82–83）。外部核对：Batyrev, Dual polyhedra and mirror symmetry for Calabi–Yau hypersurfaces in toric varieties, JAG 3 (1994) 493–535（arXiv:alg-geom/9310003）给出反身多胞体的原始定义与极对偶刻画；Kreuzer–Skarke 的 473800776 计数。nLab 无 reflexive polytope / toric degeneration 条目（站内检索 0 结果），only『polytope』『toric variety』可作一般旁证。
