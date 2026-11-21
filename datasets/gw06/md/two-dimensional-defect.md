# 二维缺陷：抛物子群与离散参数

- **id**：`gw06/concept/two-dimensional-defect`
- **类型**：concept
- **位置**：§2.6
- **问题**：列维子群趋于整个 $G$ 时，面算符的连续参数 $\alpha,\eta$ 为什么变成离散的，二者在对偶下怎样互换？

> 面算符是二维缺陷；抛物子群刻画其连续参数，极大列维情形则退化为中心里的离散 $\alpha$ 与离散 $\eta$。

## 定义

面算符可看成支撑在曲面 $D$ 上的二维缺陷：四维规范场定义在 $M\backslash D$ 上，绕 $D$ 的单值性由 $\alpha$ 标记，$D$ 上的丛由特征类 $\xi$ 分类，路径积分还可按 $D$ 上的二维 $\theta$ 角 $\eta$ 加权。它的连续参数与 $G_\C$ 的抛物子群密切相关：取 $\mathbb L$-正则的 $\alpha$，由 $[\alpha,\psi]=i\lambda\psi$、$\lambda\ge0$ 张成的 $\mathfrak p$ 定义抛物子群 $\EUP$，$\lambda>0$ 部分给出幂幺根 $\EUN$；$\mathbb L=\TT$ 且 $\alpha$ 正则时得博雷尔子群。非极小的 $\mathbb L$ 可联系若干不等价的 $\EUP$。当 $\mathbb L=G$（$\alpha=0$）时，$\alpha$ 取值于中心 ${\mathcal Z}(G)$、$\eta$ 取值于 ${\rm Hom}(\pi_1(G),U(1))$，参数变成离散的。

**记号**：$\EUP$：抛物子群；$\EUB$：博雷尔子群；$\EUN$：$\EUP$ 的幂幺根；$\alpha$：正则元／单值性；${\mathcal Z}(G)$：群中心；$\xi\in H^2(D,\pi_1(G))$：$D$ 上丛的特征类；${\rm Hom}(\pi_1(G),U(1))$：离散 $\eta$ 的取值群。

## 关键点

- 抛物子群由 $[\alpha,\psi]=i\lambda\psi,\ \lambda\ge0$ 张成的 $\mathfrak p$ 定义（式 (2.56)）；把条件换成 $\lambda>0$ 得到 $\EUN$ 的李代数，$\EUN$ 称为 $\EUP$ 的幂幺根。
- $\mathbb L=\TT$、$\alpha=i\,{\rm diag}(y_1,y_2,y_3)$、$y_1>y_2>y_3$ 时得博雷尔子群（式 (2.57)），其幂幺根为式 (2.58) 的上三角幺幂矩阵。
- 非极小 $\mathbb L$ 可联系不等价的 $\EUP$：$\alpha=iy\,{\rm diag}(1,1,-2)$（式 (2.59)）在 $y>0$ 与 $y<0$ 时分别给式 (2.60) 与 (2.61)，幂幺根为 (2.62)、(2.63)。
- 极大列维 $\mathbb L=G$（$\alpha=0$）：$\alpha$ 取值于 ${\mathcal Z}(G)$，绕 $D$ 的单值性由它标记；$D$ 上 $G$-丛由 $\xi\in H^2(D,\pi_1(G))\cong\pi_1(G)$ 分类。
- 此时 $\eta$ 是取值于 ${\rm Hom}(\pi_1(G),U(1))$ 的离散 $\theta$ 角；对偶把 ${\mathcal Z}(G)$ 与 ${\rm Hom}(\pi_1(G),U(1))$ 互换，即式 (2.25) 的离散版本。
- $\alpha$ 的离散部分与 $\xi\in H^2(D,\pi_1(G))$ 不是同一数据：$\xi$ 标记 $G$-丛无法延拓过 $D$ 的拓扑障碍，$\alpha$ 标记绕 $D$ 的单值性。对偶把 ${\mathcal Z}(G)$ 与 ${\rm Hom}(\pi_1(G),U(1))$ 互换，故 $\alpha$ 的离散部分换到 $\eta$ 的离散部分。

## 公式

```latex
\left(\begin{matrix}*&*&*\\ 0&*&*\\ 0&0&*\end{matrix}\right)
```
```latex
\alpha=iy\left(\begin{matrix}1&0&0\\ 0&1&0\\ 0&0&-2\end{matrix}\right)
```
```latex
\left(\begin{matrix}* & * & 0 \\ * & * & 0\\ * & * & * \end{matrix}\right)
```

## 常见错误

- 把 $\alpha$ 与 $-\alpha$ 当成同一个抛物子群：$y>0$ 与 $y<0$ 给不共轭的 $\EUP$ 与 $\EUP^{\prime}$，只有列维部分相同。
- 在极大列维情形仍把 $\alpha$ 当李代数向量：它实际取值于有限群 ${\mathcal Z}(G)$，$\eta$ 取值于 ${\rm Hom}(\pi_1,U(1))$，两者都是离散的。
- 把 $\mathbb L=G$ 当作 $\alpha\to0$ 的平凡极限：此时单值性取在中心里，反映 $G$-丛一般无法延拓过 $D$，其障碍正是 $\xi$。

## 批注

### 易错预警：“在外尔变换下唯一”指共轭类

给定正则的 $(\TT,\alpha)$ 定出一个博雷尔子群；换一个正则 $\alpha^{\prime}$ 得到外尔共轭的 $B^{\prime}$。所以由 $(\TT,\alpha)$ 决定的不是单个子群而是共轭类；把它读成“同一个子群”会与“换 $\alpha$ 得 $B^{\prime}$”直接矛盾。

### 含糊点拨：$\lambda=0$ 与 $\lambda>0$ 的分工

式 (2.56) 中 $\lambda=0$ 的部分（与 $\alpha$ 交换的元素）张成 $\mathbb L$ 的李代数，$\lambda>0$ 的部分张成 $\mathfrak n$，故 $\EUP$ 是 $\mathbb L_\C$ 与 $\EUN$ 的半直积；$\mathbb L$ 只固定前者，正根的取向由 $\alpha$ 的符号决定。

### 背景直觉：离散 $\theta$ 角的对偶

原文说 ${\mathcal Z}(G)$ 与 ${\rm Hom}(\pi_1(G),U(1))$ 在对偶下互换。按字面用同一个 $G$ 会出问题：$G=SU(2)$ 时 ${\mathcal Z}(G)=\Z_2$，而 $\pi_1(G)=1$、${\rm Hom}(\pi_1(G),U(1))=1$，两者并不相等。正确的读法是右端的 $G$ 指对偶群 ${}^LG$：$\pi_1({}^LG)\cong{\mathcal Z}(G)$，故 ${\rm Hom}(\pi_1({}^LG),U(1))\cong{\mathcal Z}({}^LG)$，互换的其实是 ${\mathcal Z}(G)$ 与 ${\mathcal Z}({}^LG)$。$\alpha\in{\mathcal Z}(G)$ 标记绕 $D$ 的单值性；$\eta$ 是给拓扑类 $\xi\in\pi_1(G)$ 加权的离散 $\theta$ 角，$\xi$ 不能当成 $\alpha$ 的另一种写法。

## 出处

- S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric Langlands Program（arXiv:hep-th/0612073v2）中译校订本 §2.6；印刷页 [29, 30] / PDF 页 [30, 31]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s02b-duality.tex:1020-1131`
- 抛物子群、博雷尔子群与幂幺根（式 (2.57)–(2.63)），以及极大列维情形的离散 $\alpha,\eta$；印刷页 29–30，原文 PDF 第 30–31 页。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
