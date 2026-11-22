# L 函数与函数方程

> `lbook04/concept/ch3-modular-l` · 轨 M 模形式与自守表示 · 状态 reviewed · 核验 source-only

**问题：** 模形式的 L 函数为什么必然满足函数方程，Weil 逆定理又为什么能反过来刻画模形式？

**一句话：** 模形式 $f$ 的 L 级数由 Fourier 系数拼成；Hecke 特征形式给出 Euler 乘积，函数方程来自 $f$ 的模性，Rankin–Selberg 给出二阶 L。

**别名：** `模形式的 L 函数`、`函数方程`、`Rankin–Selberg`

## 定义

§4.3 定义 $L(f,s)=\sum a_n n^{-s}$ 与完备化 $\Lambda(f,s)$（(4.11)–(4.14)）。命题 4.4 证明 $\Lambda(f,s)$ 整延拓并满足函数方程 $\Lambda(f,s)=\varepsilon\Lambda(\overline f,k-s)$；推导只用 Mellin 变换 $\Lambda(f,s)=\int_0^{\infty}f(iy)y^{s-1}dy$ 与 $f$ 的模性，$y\mapsto1/y$ 把 $s$ 换成 $k-s$。§6.1 的 Weil 逆定理（定理 6.1）反向：若 $L(f,s)$ 及所有旁特征 twist 都满足函数方程，则 $f$ 是模形式。§6.2 的 Rankin–Selberg $L(f\times g,s)$（命题 6.2）给出二阶 L，$s=1$ 的极阶判别 $f=\overline g$，$s=k$ 的留数对应 Petersson 范数（注 6.5）。§6.3 用 theta 处理二次域（命题 6.6）：二次域的特征对应权 $1$ 全纯形式或权 $1/4$ 的 Maass 形式。

**记号：** $L(f,s)$：模形式 $f$ 的 L 级数；$\Lambda(f,s)=(2\pi)^{-s}\Gamma(s)L(f,s)$（或带 level 的完备化）；$\varepsilon$：根数；$L(f\times g,s)$：Rankin–Selberg L；$S_k(q,\chi)$：尖点形式空间。

## 要点

- 函数方程来自 Mellin 变换：$\int_0^{\infty}f(iy)y^{s-1}dy$ 的模性把 $y\mapsto1/y$ 变成 $s\mapsto k-s$。
- Euler 乘积只在 Hecke 特征形式上成立；一般模形式的 L 级数只是 Dirichlet 级数（但仍有函数方程）。
- Weil 逆定理说明「函数方程 + 所有 twist」足以刻画模性；这是「L 函数决定形式」的精确版本，也是模性提升的起点。

## 公式

$$
\Lambda(f,s)=\int_0^{\infty}f(iy)y^{s-1}\,dy=\varepsilon\,\Lambda(\overline f,k-s)
$$

$$
L(f\times g,s)=\sum_{n\ge1}\frac{a_nb_n}{n^{s}}\qquad(\text{Rankin--Selberg})
$$

$$
\Lambda(f\times g,s)\ \text{的 }s=1\text{ 极阶}=1\iff f=\overline g
$$

## 定理与证明

**定理 6.1（Weil 逆定理）**　设 $f$ 为 $\mathrm{H}$ 上的全纯函数，$L(f,s)=\sum a_n n^{-s}$。若对每个模 $q$ 的 Dirichlet 特征 $\chi$，twist $L(f\otimes\chi,s)$ 的完备化都满足函数方程（且 $f$ 满足适度的增长条件），则 $f$ 是 $\Gamma_0(q)$ 上的模形式。

1. 对每个 twist 的函数方程做 Mellin 反演，得到 $f$ 在 $\Gamma_0(q)$ 生成元下的变换公式。
1. 所有 twist 合起来给出足够的函数方程，使 $f$ 在 $\Gamma_0(q)$ 上自守。

> 跳步说明：书中只给定理陈述与思路，未展开「所有 twist」的充分性论证；Weil 原文用的是「函数方程 + 有界性」的版本。

*出处：ch03.tex:802-829（§6.1，定理 6.1）*

## 易错点

- 照抄 (4.13) 的 $L(f,s)$：左端应为 $\Lambda(f,s)$（完备化后的 L），否则函数方程两边次数不齐；中译注本已径改并出注。
- 把 Rankin–Selberg 的极点位置记错：注 6.5 说 $s=1$ 处极阶判别 $f=\overline g$，$s=k$ 处留数对应 Petersson 范数；书中原文把 $s=k$ 印成 $s=1$，注意区分。

## 批注

**〔易错预警〕(4.13) 的左端**　中译注本把原书 (4.13) 左端的 $L(f,s)$ 径改为 $\Lambda(f,s)$，因为右端是 $\varepsilon\Lambda(\overline f,k-s)$，两边必须是完备化 L 才能对齐；引用原书时需说明这一改动，否则会误以为函数方程对未完备化的 $L$ 成立。

**〔背景直觉〕逆定理的分量**　定理 6.1 要求对所有模 $q$ 的 Dirichlet 特征 twist 都满足函数方程，缺一不可；这正是 Weil 把「函数方程」变成「模性判据」的关键——单个函数方程不足以定 $f$，所有 twist 才够。

## 相关

[[ch3-hecke-operators]]、[[ch3-theta-modularity]]、[[ch3-eisenstein-cusp]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§4.3，原书 pp. 55–56（PDF pp. 62–63）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch03.tex:522-595`
- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§6.1，原书 pp. 63–65（PDF pp. 70–72）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch03.tex:769-829`
