# 反身多胞体对

> `siebert/concept/reflexive-pair` ｜ track E ｜ draft

**一句话**：一对互为极对偶的格多胞体，两侧都把原点放在内部、侧面到原点整距离为 1；它们给出互为镜像的两个 Calabi–Yau 超曲面族。

**自测**：为什么『反身对』不是额外数据，而是任取一个反身多胞体就自动得到的东西？

## 定义

设 $\Xi\subset M_{\RR}$、$\Xi^\circ\subset N_{\RR}$ 是满维格多胞体，各自把 $0$ 含在内部，且满足极对偶关系 $\Xi^\circ=\{n\in N_{\RR}:\langle n,m\rangle\ge-1\ \text{对一切}\ m\in\Xi\}$。等价地：$\Xi$ 反身（Def 5.1）当且仅当 $\Xi$ 与 $\Xi^\circ$ 都是格多胞体。此时 $(\Xi^\circ)^\circ=\Xi$，称 $(\Xi,\Xi^\circ)$ 为反身多胞体对。它给出镜像的两个族：取各自的 MPCP 细分 $\Sigma$、$\check\Sigma$ 与一般截面 $s$、$\check s$，得 $Z(s)\subset X_\Sigma$ 与 $Z(\check s)\subset X_{\check\Sigma}$（式 5.5–5.6）。

记号：$M,N$ 为互为对偶的格；$\Xi\subset M_{\RR}$、$\Xi^\circ\subset N_{\RR}$；$\Sigma$、$\check\Sigma$ 为 MPCP 细分；$\check X=X(\Sigma_{\check\Xi})$；$\Lambda_\sigma$ 记整切格。

## 要点

- 对偶是 involution：$(\Xi^\circ)^\circ=\Xi$，所以『对』不是额外数据——任给一个反身多胞体就自动得到反身对。这正是镜像对称被称为『对偶』而非法则的原因。
- 计数（Ex 5.1–5.2 与 p.81）：二维恰有 16 个反身多胞体，三维 4319 个，四维 473800776 个。弦论『大量真空』的说法就来自这个计数。
- 反身性强制内部格点唯一：定义同时要求 $\Int(\Xi)\cap M=\{0\}$ 与 $\Int(\Xi^\circ)\cap N=\{0\}$，故例 5.1 的两个多胞体都只有一个内部格点。
- 反例（Counterexample 3）：$\operatorname{conv}\{(-1,-1),(-1,0),(1,0),(0,2)\}$ 不是反身——$0$ 在内部，但某个侧面到原点的整仿射距离不是 $1$（等价地 $\Xi^\circ$ 出现非整顶点）。
- 在镜像构造里反身对是『数据对』：一侧给 $\Sigma_\Xi$ 的 MPCP 细分与壁函数 $f_\rho$，另一侧给 $\check\Sigma$；多胞体图景下这个对偶就是离散 Legendre 变换 $(B,\mathscr P,\varphi)\leftrightarrow(\check B,\check{\mathscr P},\check\varphi)$（式 5.19）。
- Hodge 数互换是反身对的判据：$h^{1,1}(X)=h^{n-1,1}(\check X)$（Thm 5.3，光滑情形）；轨形情形换成 $h^{p,q}_{\mathrm{st}}$（Thm 5.4）。

## 公式

$$\Xi^\circ=\{n\in N_{\RR}:\langle n,m\rangle\ge-1\ \ \forall m\in\Xi\},\qquad (\Xi^\circ)^\circ=\Xi$$
$$\Int(\Xi)\cap M=\{0\},\qquad \Int(\Xi^\circ)\cap N=\{0\}$$
$$16\ (d=2),\qquad 4319\ (d=3),\qquad 473800776\ (d=4)$$

## 定理与证明

### 引理：Def 5.1 的等价刻画

$\Xi$ 满足 $\Int(\Xi)\cap M=\{0\}$ 且每个侧面到原点的整仿射距离为 $1$，当且仅当 $\Xi$ 与 $\Xi^\circ$ 都是格多胞体。

（sketch；来源：原书 p.81）

1. 设 $\Xi$ 的每个侧面 $F$ 都由 $\langle n_F,m\rangle=-1$ 切出，其中 $n_F\in N$ 本原；『整仿射距离 1』正是说支撑超平面可写成本原整线性泛函取值 $-1$。  
   为什么：整仿射距离是把超平面平移整数倍后过原点所需的最小整数，等价于存在本原整泛函取值为 $-1$。
2. 于是 $\Xi^\circ=\operatorname{conv}\{n_F\}$（$F$ 取遍侧面），顶点都是整点，故 $\Xi^\circ$ 是格多胞体；$\Xi$ 满维给出 $0\in\Int(\Xi^\circ)$。  
   为什么：极多胞体的顶点与原始多胞体的侧面一一对应，法向就是顶点。
3. 反向：若 $\Xi^\circ$ 是格多胞体，其每个顶点 $n\in N$ 给出 $\Xi$ 的一个面 $\langle n,m\rangle\ge-1$，即该侧面到原点距离为 $1$。  
   为什么：极对偶把『$\Xi^\circ$ 的顶点』与『$\Xi$ 的侧面』互换，顶点整性即距离整性。

缺口：讲义把等价性直接写进定义（『等价地，$\Xi$ 与 $\Xi^\circ$ 都是格多胞体』），未给证明；这里补出的三步仍是梗概，未验证对偶多胞体的满维性。

### Ex 5.1–5.2 与反身多胞体的分类计数

二维恰有 16 个反身多胞体，三维 4319 个，四维 473800776 个。

（none；来源：原书 p.81）


缺口：这是分类定理（Batyrev 之后由 Kreuzer–Skarke 完成的计算），讲义只引用结果；它数的是多胞体，不数镜像族。

## 易错点

- 反身对不是任意两个多胞体：$\Xi^\circ$ 必须由 $\langle n,m\rangle\ge-1$ 定义（极多胞体），且两侧都必须是格多胞体。
- 『两个多胞体都只有一个内部格点』是结论而不是定义；定义只要求 $\Int(\Xi)\cap M=\{0\}$，另一条由反身性推出。
- 反例里的四边形顶点都是整点、$0$ 也在内部，但某侧面距离 $\ne1$，于是 $\Xi^\circ$ 出现非整顶点，所以不反身。
- 别把反身对与『镜像族』混为一谈：多胞体对只是组合数据，镜像族还要选 MPCP 细分与截面 $s$。
- 四维的 473800776 只数多胞体，不数镜像族：每个多胞体还可能对应多个 MPCP 细分（Note 5.1）。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 5 章 §1.1 反身多胞体、例与计数，p.81–81（原书 p.81）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 5 章 §1.5–1.6 Batyrev 超曲面镜像与镜像定理，p.83–83（原书 p.83）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 5 章 §2.3 Mumford 退化的镜像对称（离散 Legendre 变换），p.85–85（原书 p.85）

关联：`siebert/concept/reflexive-polytope`、`siebert/concept/batyrev-mirror-construction`、`siebert/concept/crepant-resolution`、`siebert/concept/mirror-symmetry`、`siebert/deriv/mumford-degeneration`

来源说明：原书 p.81（Def 5.1、Ex 5.1–5.2、Counterexample 3、16/4319/473800776 的计数）、p.83（§1.5 式 5.5–5.6、Thm 5.3–5.4）、p.85（§2.3 式 5.19 离散 Legendre 变换）。外部核对：Batyrev 1994（arXiv:alg-geom/9310003）给出反身多胞体与镜像族的原始构造；Kreuzer–Skarke 的二维/三维/四维分类给出上述计数。nLab 无 reflexive polytope 条目（检索 0 结果），nLab『polytope』只讲一般多胞体，不能作为术语依据。
