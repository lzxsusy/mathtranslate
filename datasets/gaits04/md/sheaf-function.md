# 层-函数对应（Grothendieck）

> `gaits04/concept/sheaf-function` · 轨 E 附录：层-函数对应 · 状态 reviewed · 核验 source-only

**问题：** 为什么张量积对应逐点乘积，而拉回/推前对应什么？

**一句话：** 定义在 $\mathbb{F}_q$ 上的叠 $\mathcal Y$，其导出范畴 $D^b(\mathcal Y)$ 的每个对象经「取纤维、算 Frobenius 迹的交替和」给出 $\mathcal Y$ 的 $\mathbb{F}_q$-点集上的函数；张量积对应逐点乘积。

**别名：** `sheaf-function correspondence`、`Grothendieck`、`Frobenius trace`

## 定义

回顾 Grothendieck 的层-函数对应的若干事实。首先，若 $\mathcal Y$ 是（任意基域上的）概形，可以定义范畴 $D^b(\mathcal Y)$，称为上同调可构造的 $\ell$-进层的导出范畴。若 $\phi:\mathcal Y_1\to\mathcal Y_2$ 是概形间的态射，则有拉回与直接像函子 $\phi^*:D^b(\mathcal Y_2)\to D^b(\mathcal Y_1)$，$\phi_!:D^b(\mathcal Y_1)\to D^b(\mathcal Y_2)$。若 $\mathcal F_1$ 与 $\mathcal F_2$ 是 $D^b(\mathcal Y)$ 的两个对象，可以定义它们的张量积 $\mathcal F_1\otimes\mathcal F_2\in D^b(\mathcal Y)$。现设 $\mathcal Y$ 定义在基域 $\mathbb{F}_q$ 上。记 $Y$ 为 $\mathcal Y$ 的 $\mathbb{F}_q$-值点集（它是有限集），$\operatorname{Funct}(Y)$ 为其上 $\overline{\mathbb Q}_\ell$-值函数构成的向量空间。$D^b(\mathcal Y)$ 的每个对象 $\mathcal F$ 都给出 $\operatorname{Funct}(Y)$ 中一个元素 $f$。首先，若 $\mathcal Y$ 是点概形 $\operatorname{Spec}(\mathbb{F}_q)$，则 $D^b(\operatorname{Spec}(\mathbb{F}_q))$ 的对象就是有限维 $\overline{\mathbb Q}_\ell$-向量空间构成的有复形，带 $\mathrm{Gal}(\overline{\mathbb F}_q/\mathbb F_q)$ 的作用。对应的函数（此时只是 $\overline{\mathbb Q}_\ell$ 的一个元素）是 $\mathrm{Gal}(\overline{\mathbb F}_q/\mathbb F_q)$ 中 Frobenius 元的迹的交替和。对一般的 $\mathcal Y$、$\mathcal F\in D^b(\mathcal Y)$ 与 $y\in Y$，$f$ 在 $y$ 处的值等于上述规则赋给 $\mathcal F_y$ 的数，其中 $\mathcal F_y\in D^b(\operatorname{Spec}(\mathbb{F}_q))$ 是 $\mathcal F$ 沿对应于 $y$ 的态射 $\operatorname{Spec}(\mathbb{F}_q)\to\mathcal Y$ 的拉回。对应的基本性质如下：张量积 $\mathcal F_1\otimes\mathcal F_2$ 对应 $f_1\cdot f_2$（逐点乘积）；对映射 $\phi:\mathcal Y_1\to\mathcal Y_2$，拉回 $\phi^*(\mathcal F)$ 对应 $\phi^*(f)$，推前同理（就证明而言，前两条性质由定义立得，第三条即 Grothendieck–Lefschetz 迹公式）。

**记号：** $D^b(\mathcal Y)$：可构造 $\ell$-进层的导出范畴；$Y$：$\mathbb{F}_q$-点集；$f$：$\mathcal F$ 对应的函数；$\mathcal F_y$：$y$ 处纤维。

## 要点

- 点概形上的对象是带 Galois 作用的复形，其函数是 Frobenius 迹的交替和 $\sum(-1)^i\mathrm{tr}(\mathrm{Fr}|H^i)$。
- 张量积 ↔ 逐点乘积是定义层面的；拉回 ↔ 拉回、推前 ↔ 推前（后者需迹公式）。
- 第三条性质（推前 ↔ 逐纤维求和）正是迹公式，也是 §2.5、§2.8 中 $!$-推前与积分对应的依据。

## 公式

$$
f(y)=\sum_i(-1)^i\,\mathrm{tr}\big(\mathrm{Fr}\mid H^i(\mathcal F_y)\big)
$$

$$
\mathcal F_1\otimes\mathcal F_2\ \mapsto\ f_1\cdot f_2
$$

## 易错点

- 把 $\phi_!$ 与 $\phi_*$ 混用：函数侧推前对应的是 $\phi_!$（紧支撑），用 $\phi_*$ 会多出边界项，迹公式不成立。

## 批注

**〔背景直觉〕第三条性质即迹公式**　它把「沿态射推前」与「逐纤维求和」等同起来。§2.5 中 $(h^{\rightarrow})_!$ 的求和、§2.8 中 $q_!$ 的积分都是它在函数侧的表现；到了层侧，同一件事由上同调直接像承担，而迹公式保证两边算出的函数一致。

## 相关

[[why-spherical]]、[[character-sheaf]]

## 来源

- D. Gaitsgory《几何朗兰兹的非正式导论》，Bernstein–Gelbart 编《朗兰兹纲领导论》第 12 章，Birkhäuser 2004，pp. 269–281，§4.1–4.2，原书 pp. 278–279（PDF pp. 280–281）
  - 锚点：`08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/源码/chapters/ch12_sec3.tex:75-98（§4.1–§4.2）`
