# 强重数一定理

> `lbook04/concept/ch7-multiplicity-one` · 轨 M 模形式与自守表示 · 状态 reviewed · 核验 source-only

**问题：** 为什么几乎全部位的局部信息足以决定一个整体自守表示，而有限个位的信息却不够？

**一句话：** 若两个 $\operatorname{GL}(2)$ 自守表示在几乎全部位局部同构，则它们整体同构；Ramakrishnan 把它加强为例外位集密度小于 $1/8$ 即够。

**别名：** `strong multiplicity one`、`Miyake`、`Casselman`

## 定义

定理 2.6(iii)（Miyake、Casselman）：$\pi,\pi'$ 是 $\mathcal A_0(G)$ 的不可约成分，若存在有限位集 $S$ 使 $v\notin S$ 时 $\pi_v\cong\pi'_v$，则 $\pi\cong\pi'$。(iv)（Ramakrishnan）：把「有限个例外位」放宽为「例外位集密度 $<1/8$」，结论仍成立。证明用 $\operatorname{GL}(2)$ 的对称平方 $L$ 函数（Gelbart–Jacquet）与 Rankin–Selberg $L$ 函数：局部几乎处处相等的 $L$ 因子迫使整体 $L$ 函数相等，再由 $L$ 函数的唯一性得 $\pi\cong\pi'$。

**记号：** $\pi,\pi'$：自守表示；$S$：例外位集；$L(s,\pi\times\widetilde\pi')$；$\operatorname{Sym}^2L$；密度：Dirichlet 密度。

## 要点

- 经典来源：Miyake 1971（模形式的新旧形式理论）、Casselman 1973（局部理论）；Ramakrishnan 1994 给出 $1/8$ 的密度版本。
- 证明路线：$L(s,\pi\times\widetilde\pi')/L(s,\operatorname{Sym}^2\pi)$ 的极点位置读出 $\pi\cong\pi'$；局部几乎处处相等使这些 $L$ 函数相等。
- $1/8$ 的常数来自 Taylor 的密度估计（Invent. Math. 116 (1994) 645–649），不是最优。
- 对 $\operatorname{GL}(n)$ 的强重数一由 Jacquet–Shalika 证明；$\operatorname{SL}_n$（$n\ge3$）重数可 $>1$ 是另一回事。

## 公式

$$
\pi_v\cong\pi'_v\ \text{对几乎全部 }v\ \Longrightarrow\ \pi\cong\pi'
$$

$$
L(s,\pi\times\widetilde\pi')=\prod_v L(s,\pi_v\times\widetilde\pi'_v)
$$

## 易错点

- 强重数一 $\ne$ 重数一：前者说「局部决定整体」，后者说「$\mathcal A_0(\pi)$ 在 $\mathcal A_0(G)$ 中出现一次」；定理 2.6(ii) 与 (iii) 是两条不同的结论。
- $1/8$ 是充分条件、不是必要条件，也不是精确阈值；引用时不要把它当作最优常数。

## 批注

**〔背景直觉〕为什么 $L$ 函数能分辨**　两个表示若几乎处处局部同构，则它们的 Rankin–Selberg $L$ 函数有相同的 Euler 因子；$L$ 函数的极点与函数方程又编码了表示本身，故整体被迫相等。

**〔含糊点拨〕$1/8$ 的出处**　中译注 ch07.tex:423–427 指出 $1/8$ 来自 Ramakrishnan 附录的密度估计（Taylor 1994）；书中只给结论、不给证明。

## 相关

[[ch7-cuspidal-whittaker]]、[[ch7-restricted-tensor]]、[[ch7-automorphic-rep]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§2 定理 2.6，原书 pp. 142–143（PDF pp. 146–147）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch07.tex:409-429`
