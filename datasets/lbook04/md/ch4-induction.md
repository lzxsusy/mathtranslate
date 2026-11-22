# 分解与诱导

> `lbook04/concept/ch4-induction` · 轨 L L 函数 · 状态 reviewed · 核验 source-only

**问题：** Brauer 诱导定理为什么只能给亚纯延拓，而给不了解析延拓？

**一句话：** Artin L 对表示可加、对诱导有 (3.12)–(3.13) 的分解；Brauer 定理把任意特征写成单项特征整系数组合，从而把 $L(\chi,s)$ 化成 Hecke L 的乘积。

**别名：** `Brauer 诱导`、`Frobenius 互反律`、`Artin 表示`

## 定义

§3.4 列出初步性质：可加性 (3.12)、诱导 (3.13) $L(\operatorname{Ind}_H^G\psi,s)=L(\psi,s)$、膨胀 (3.14)；类域论情形 (3.15) 与 $\zeta_K(s)=\zeta_k(s)\prod_{\chi\ne1}L(\chi,s)^{\chi(1)}$ (3.16)。§4.4 的 Brauer 定理（定理 4.2，1947）说：有限群 $G$ 的每个特征都是单项特征 $\operatorname{Ind}_H^G\psi$（$\psi$ 一维）的整系数线性组合。于是 $\Lambda(\chi,s)=\prod_i\Lambda(\chi_i,s)^{n_i}$（(4.9)）。证明梗概（Brauer–Tate 1951）：幂零群全单项，再用 $A=\mathbb Z[\zeta]$ 与两条构造化到 $p$-初等子群。系数 $n_i$ 可为负，所以只得到亚纯延拓与函数方程；解析性（极点是否相消）正是 Artin 猜想。

**记号：** $\operatorname{Ind}_H^G$：诱导表示；$\psi$：$H$ 的一维特征；$n_i\in\mathbb Z$：Brauer 组合的整系数（可负）；$p$-初等子群：$p$-群与循环群的直积；$\Lambda(\chi,s)$：完备化 Artin L。

## 要点

- 诱导公式 (3.13) 是「L 函数按域塔分解」的表示论版本；膨胀 (3.14) 处理非 Galois/中间域。
- Brauer 定理给的是虚拟特征（整系数、可能为负）的组合，因此只能得到亚纯延拓与函数方程；要解析延拓需正系数分解（Artin 猜想）。
- 交换情形 (3.15)(3.16) 把 $\zeta_K/\zeta_k$ 写成 Dirichlet/Hecke L 的乘积，这是 Brauer 分解的最简单实例。

## 公式

$$
L(\operatorname{Ind}_H^G\psi,s)=L(\psi,s),\qquad \Lambda(\chi,s)=\prod_i\Lambda(\chi_i,s)^{n_i}
$$

$$
\zeta_K(s)=\zeta_k(s)\prod_{\chi\ne1}L(\chi,s)^{\chi(1)}
$$

$$
\sum_i n_i\operatorname{Ind}_{H_i}^G\psi_i=\chi\qquad(n_i\in\mathbb Z)
$$

## 易错点

- 把 Brauer 的整系数组合当成「正系数乘积」：$n_i$ 可以为负，故只能谈亚纯；极点/零点可能相消，解析性正是 Artin 猜想的内容。
- 把诱导与限制搞反：$\operatorname{Ind}_H^G$ 从 $H$ 的表示造 $G$ 的表示，$L$ 函数不变（(3.13)）；限制 $\operatorname{Res}$ 则把 $G$ 的表示拉回 $H$，$L$ 函数会分解。

## 批注

**〔易错预警〕诱导作用的方向**　(2.4) 的诱导空间是 $\{f:G\to W,\ f(hg)=\rho(h)f(g)\}$（左协变），而 (2.5) 的 $G$-作用是右平移 $f(g'g)$；两者方向相反但相容。notes 特别提醒不要把这两个作用混为同一个，否则 Frobenius 互反律 (2.7) 的配对会对错。

**〔背景直觉〕为什么 Brauer 够了**　单项表示是一维表示的诱导，其一维情形由 Hecke/类域论给出解析延拓；Brauer 定理保证任何特征都能由这些「已知块」拼出，代价是系数可能为负。这也解释了为什么 1947 年之后 Artin L 的亚纯延拓与函数方程立刻成为定理，而解析性至今未决。

## 相关

[[ch4-artin-definition]]、[[ch4-conductor-fe]]、[[ch1-cft-entry]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§3.4，原书 pp. 78–79（PDF pp. 84–85）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch04.tex:201-249`
- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§4.4，原书 pp. 81–83（PDF pp. 87–89）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch04.tex:311-353`
