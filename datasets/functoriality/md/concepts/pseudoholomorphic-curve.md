# 伪全纯曲线

> `functoriality/concept/pseudoholomorphic-curve` ｜ track A ｜ draft

**一句话**：伪全纯曲线是从黎曼曲面到殆复流形的映射，满足微分与复结构相容的方程；辛几何里用条带与圆盘作边界条件，靠 Gromov 紧性提取计数不变量。

**自测**：为什么把全纯曲线推广为伪全纯曲线对辛几何是必要的一步，边界条件的加入又带来什么？

## 定义

设 $(M,J)$ 是殆复流形、$(\Sigma,j)$ 是黎曼曲面。映射 $u:\Sigma\to M$ 称伪全纯，若其微分与复结构相容：$du+J\circ du\circ j=0$，等价说法是 $\overline\partial_Ju=0$。辛 Floer 理论取 $\Sigma=\R\times[0,1]$（条带）或 $\Sigma=D^2$（圆盘），并要求 $u$ 把边界映到给定的拉格朗日子流形；此外要求 $u$ 的同伦类给定（从而能量可控）。

记号：条带坐标记 $(s,t)\in\R\times[0,1]$，方程写作 $\partial_su+J_t(u)\partial_tu=0$；圆盘/多边形用边界上的标记点与 Maslov 指标 $\ind$ 分层。

## 要点

- 目标只需是辛流形、$J$ 只需殆复，因此即使 $M$ 不是 Kähler 流形也能使用全纯技术——这是 Gromov 的关键洞见。
- 条带计数给出 Floer 微分 $d$，圆盘与多边形计数给出 Fukaya 范畴的高阶运算 $\mu_r$；两类曲线的区别只在定义域拓扑与标记点数。
- 相容性使能量等于辛面积：能量一致有界给出 Gromov 紧性，从而模空间有自然紧化，计数才有意义。
- 模空间的维数由 Maslov 指标决定（条带情形为 $\ind v-1$）；只数 0 维层即「刚性」曲线，这是所有不变量的来源。

## 公式

$$\overline\partial u\equiv du-J\circ du\circ j$$
$$\begin{gathered} \mathcal M(p_-,p_+;[v])\coloneqq\{u:\R\times[0,1]\to M\mid(*)\}/\R,\\ (*)\quad\coloneqq\quad u(s,0)\in L,\quad u(s,1)\in K,\quad\lim_{s\to\pm\infty}u(s,t)=p_{\mp},\\ \partial_su+J_t(u)\partial_tu=0,\quad[u]=[v], \end{gathered}$$

## 定理与证明

### Gromov 的全纯圆盘定理

对任意闭的嵌入拉格朗日子流形 L⊂C^n，存在非常值映射 u:D²→C^n，它把边界映到 L，并且关于圆盘与 C^n 上的标准复结构全纯。

（none；来源：原书 p.3 §1.1）


缺口：原文引 [Gro85] 的定理 0.4.A₂，未给证明；这是硬分析结果。

### 拉格朗日嵌入的拓扑障碍

若闭 n 维流形 L 满足 H¹(L;R)=0，则 L 不能拉格朗日嵌入到 C^n 中。

（sketch；来源：原书 p.3 §1.1）

1. 取 $\lambda\coloneqq\frac12\sum_{i=1}^n(x_i\,dy_i-y_i\,dx_i)$，它满足 $d\lambda=\omega_0$，是 $\omega_0$ 的原始形式。  
   为什么：有了原始形式才能对圆盘用 Stokes 定理，把边界积分与面积联系起来。
2. 对 Gromov 给出的全纯圆盘 $u$ 及其边界 $\gamma=u|_{S^1}$ 用 Stokes：$\int_{S^1}\gamma^*\lambda=\int_{D^2}u^*\omega_0>0$。  
   为什么：全纯性保证 $\int u^*\omega_0$ 是非负面积，非常值性使它严格为正。
3. 但 $H^1(L;\R)=0$ 且 $\omega|_L=0$ 使 $\lambda|_L$ 是正合 1-形式，故 $\int_{S^1}\gamma^*\lambda=0$，与步骤 2 矛盾。  
   为什么：$\gamma$ 的像落在 $L$ 中；闭形式在 $L$ 上正合，则它在闭链上的积分必为零。

缺口：原文把「非常值 ⇒ 面积严格为正」视为显然；这里补出全纯性给出非负、非常值给出正的论证。原文标题误写为嵌入 CP^n，译注说明障碍实际针对 C^n。

## 易错点

- 把伪全纯当成「$J$ 可积时的全纯函数」：$J$ 不可积时没有全纯函数概念，只有方程 $du+J\\circ du\\circ j=0$ 逐点成立。
- 忽略边界条件：辛几何中的曲线是带拉格朗日边界条件的条带/圆盘，闭曲线的 Gromov–Witten 理论不能直接搬过来。
- 忘记固定同伦类：不固定同伦类时模空间不连通、无法按能量分层，Maslov 指标维数公式也失去意义。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§1.1，p.2–3（原书 p.2–3 §1.1）

关联：`functoriality/concept/almost-complex-structure`、`functoriality/concept/floer-cohomology`、`functoriality/concept/lagrangian-submanifold`

来源说明：原书 p.3 §1.1（Gromov 全纯圆盘定理 thm:1.4、全纯性方程 eq:5、推论 thm:1.5）；条带方程取自 chapter2.tex 的 eq:12。
