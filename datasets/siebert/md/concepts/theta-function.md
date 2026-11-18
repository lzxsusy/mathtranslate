# 广义 $\theta$ 函数

> `siebert/concept/theta-function` ｜ track E ｜ draft

**一句话**：对渐近方向为 $m$ 的折线求和所得的 $\mathcal X^\circ$ 上正则函数；其乘法给出内蕴镜像映射的环结构，并被用作重建族的齐次坐标。

**自测**：为什么以「折线求和」定义的 $\vartheta_m$ 值得叫 $\theta$ 函数，它与经典 $\theta$ 函数的对应点在哪里？

## 定义

设壁结构 $\mathscr S$ 在余维不超过二处相容，$m$ 为一个渐近整向量场。对一切渐近单项式为 $z^m$ 的折线 $\beta$ 求和，得到 $\vartheta_m=\sum_\beta b_\beta z^{m_\beta}\in\OO(\mathcal X^\circ)$（式 5.72–5.73）；该表达式与同一腔室内终点 $p$ 的选择无关。在 $\mathfrak u\subseteq\sigma$ 对应的环 $R_{\mathfrak u}=A[\Lambda_\sigma]$ 上，它就是这些折线末项之和。讲义称之为典范函数或广义 $\theta$ 函数。

记号：$A=\CC[t]/(t^{k+1})$；$m$ 渐近整向量场；$b_\beta\in A$；$m_\beta$ 折线末段的指数；$\vartheta_m\in\OO(\mathcal X^\circ)$；$N_{m_1,m_2,p}$ 为式 5.78 中的亏格零曲线计数。

## 要点

- 定义：$\vartheta_m$ 只依赖「渐近方向 $m$」这一个连续参数，其余全部由壁结构（即散射数据）决定。无壁时它退化为单项式 $z^m$（环面上的特征函数 $\chi^m$）；有壁时它是「被散射逐阶修改过的单项式」。
- 与经典 $\theta$ 的对应点：经典 $\theta$ 函数是对格点（或平移格点）求和、并对周期取商，得到的函数与代表元选取无关；这里「格点」换成折线、「周期/模参数」换成壁结构的数据，得到的 $\vartheta_m$ 同样与终点选取无关。这就是「广义」二字的含义。
- 归一化：$\vartheta_0=1$（零方向的折线只有平凡一条）；一般 $\vartheta_m$ 的最高项就是渐近单项式 $z^m$ 本身，其余项都带 $t$ 的正幂。
- 乘法即内蕴镜像映射的环：$\vartheta_{m_1}\vartheta_{m_2}=\sum_pN_{m_1,m_2,p}\vartheta_p$（式 5.78），其中 $N_{m_1,m_2,p}$ 计数与除子 $D$ 的接触阶为 $m_1,m_2,-p$ 的亏格零曲线。难点是证明这个乘法的结合律。
- 重建族：仿射情形 $\mathcal X=\Spec\bigl(\bigoplus_{m\in B(\ZZ)}A\vartheta_m\bigr)$（式 5.75）；一般情形 $\mathcal X=\Proj\bigl(\bigoplus_mA\vartheta_m\bigr)$（式 5.80）。$\vartheta_m$ 在 $\mathcal X$ 上扮演齐次坐标的角色。
- 为什么必须求和而不是只取一项：单条折线依赖路径，只有在相容壁结构下把所有折线加起来、并让穿壁的坐标变换相互抵消，才得到与路径无关的对象——这与 $\theta$ 函数「对全部格点求和才周期」是同一个机制。

## 公式

$$\vartheta_m=\sum_{\substack{\beta\ \text{的渐近单项式为}\ z^m\\ \text{终点为}\ p}}b_\beta z^{m_\beta}\in\OO(\mathcal X^\circ)$$
$$\vartheta_{m_1}\vartheta_{m_2}=\sum_pN_{m_1,m_2,p}\,\vartheta_p$$
$$\mathcal X=\Spec\Bigl(\bigoplus_{m\in B(\ZZ)}A\vartheta_m\Bigr),\qquad \mathcal X=\Proj\Bigl(\bigoplus_mA\vartheta_m\Bigr)$$

## 定理与证明

### 式 5.72–5.73：折线求和给出 $\mathcal X^\circ$ 上的正则函数

若 $\mathscr S$ 在余维不超过二处相容，则对每个渐近整向量场 $m$，折线求和定义的 $\vartheta_m$ 是 $\mathcal X^\circ$ 上的正则函数，且它在每个环 $R_{\mathfrak u}=A[\Lambda_\sigma]$ 中的表达式与腔室内终点的选择无关。

（sketch；来源：原书 p.92）

1. 在每个腔室 $\mathfrak u$ 上，折线求和给出 $R_{\mathfrak u}$ 的一个元素；模 $t^{k+1}$ 时只有有限条折线贡献，故和有意义。  
   为什么：有限性来自「穿 $r$ 面壁系数抬到 $t^{r}$」，只需 $r\le k$；每段的选择有限（$f_{\mathfrak p}$ 是有限和）。
2. 两个相邻腔室的表达式通过壁穿越 $\Theta_{\mathfrak p}$ 相互转换：把折线在该壁上展开，正好是 $\Theta_{\mathfrak p}$ 的作用。  
   为什么：$\Theta_{\mathfrak p}$ 的定义（式 5.55）就是「穿壁时单项式如何展开」，故按 $\Theta_{\mathfrak p}$ 粘合两侧的求和逐项一致。
3. $\mathcal X^\circ$ 是这些 $\Spec R_{\mathfrak u}$ 沿壁穿越的余极限（式 5.68），故各腔室上的表达式粘成 $\OO(\mathcal X^\circ)$ 的一个整体截面。  
   为什么：余极限的万有性：只要相邻副本在重叠处一致，就存在唯一的整体截面；一致性正是第 2 步。

缺口：讲义只给定义与「与 $p$ 无关」的结论，粘合一致性（折线展开 = 壁穿越）没有逐项验证。

### 式 5.78：$\vartheta$ 的乘法是亏格零曲线计数

$\vartheta_{m_1}\vartheta_{m_2}=\sum_pN_{m_1,m_2,p}\vartheta_p$，其中 $N_{m_1,m_2,p}$ 计数与 $D$ 的接触阶为 $m_1,m_2,-p$ 的亏格零曲线；该乘法使 $\bigoplus_mA\vartheta_m$ 成为环。

（sketch；来源：原书 p.93）

1. 把乘积 $\vartheta_{m_1}\vartheta_{m_2}$ 按 $\vartheta$ 的基展开，系数由「两条折线合并成一条」的组合给出。  
   为什么：两条折线的乘积在 $\OO(\mathcal X^\circ)$ 里逐项相乘；展开后每项仍是一个 $\vartheta_p$，系数即是配对数目。
2. 配对数目等于与 $D$ 有指定接触阶的亏格零曲线数（对数 GW 不变量）。  
   为什么：这是内蕴镜像映射的核心定理：$\mathcal X^\circ$ 的乘法常数与 $(Y,D)$ 上的对数 GW 理论一致（p.93 §6 开头的说明）。
3. 结合律即 $(\vartheta_{m_1}\vartheta_{m_2})\vartheta_{m_3}=\vartheta_{m_1}(\vartheta_{m_2}\vartheta_{m_3})$，讲义明确指出这是困难之处。  
   为什么：结合律等价于曲线计数的三项关系（WDVV 型），需要几何证明而非形式展开。

缺口：讲义只陈述乘法规则并点明「困难之处在于证明结合律」，未给证明；$N_{m_1,m_2,p}$ 的完整定义（带负接触阶的对数 GW 不变量）在 p.93 §6 才出现。

## 易错点

- 别与经典 Jacobi $\theta$ 函数混同：nLab 的「theta function」条目讲的是椭圆函数的 $\theta$，与这里的 $\vartheta_m$ 名同实异，不可互引。
- $\vartheta_m$ 依赖渐近方向 $m$，不是 $B(\ZZ)$ 上的函数；不同的 $m$ 给出 $\OO(\mathcal X^\circ)$ 中不同的元素，把它们当成同一个「坐标」会算错乘法。
- $\vartheta_m\in\OO(\mathcal X^\circ)$，不是 $\OO(\mathcal X)$：要成为 $\mathcal X$ 的齐次坐标，必须先由定理 5.7 作部分完备化（取截断锥）。
- 「与 $p$ 无关」只在同一腔室内成立；跨腔室要同时用 $\Theta_{\mathfrak p}$ 换坐标，否则和会差一个自同构。
- 式 5.78 的 $N$ 是带接触阶条件的亏格零曲线计数（允许负接触阶），不是通常的 GW 不变量；漏掉接触阶条件会把它误当成一般的三点函数。
- 「广义 $\theta$ 函数」不是「theta 特征」的推广：这里的「广义」指把周期换成壁结构数据，与奇偶性/特征无关。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 5 章 §5.5 典范函数：式 5.72–5.73，p.92–92（原书 p.92）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 5 章 §5.6 定理 5.7 的证明：式 5.75，p.93–93（原书 p.93）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 5 章 §6 内蕴镜像映射：式 5.77–5.80，p.93–94（原书 p.93–94）

关联：`siebert/concept/broken-line`、`siebert/concept/wall-structure`、`siebert/deriv/scattering-consistency`、`siebert/concept/batyrev-mirror-construction`、`siebert/concept/homological-mirror-symmetry`、`siebert/concept/gromov-witten-invariant`

来源说明：原书 p.91–94：$\vartheta_m$ 的定义与良定性（p.92，式 5.72–5.73）、定理 5.7 中 $\mathcal X=\Spec(\bigoplus A\vartheta_m)$（p.93，式 5.75）、内蕴镜像映射的乘法与 $X=\Proj(\bigoplus A\vartheta_m)$（p.93–94，式 5.78–5.80，例 5.8 的 $\PP^2$ 情形）。外部核对：Gross–Siebert, The canonical wall structure and intrinsic mirror symmetry（arXiv:2105.02502）的 theta 函数构造；Gross–Siebert, From real affine geometry to complex geometry（arXiv:math/0703822）§3–§4。nLab「theta function」条目讲经典椭圆 $\theta$，与本章名同实异，未用作依据；nLab 无 Gross–Siebert theta function 条目（站内检索 0 结果）。
