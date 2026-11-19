# 命题 1.5：球向量是 Hecke 模，且不可约性保持

> `gaits04/concept/spherical-module` · 轨 A 阿代尔与球表示 · 状态 reviewed · 核验 source-only

**问题：** 为什么不可约表示的球向量子空间一定是不可约 Hecke 模？

**一句话：** 对 $G(K_x)$ 的表示 $\pi$，不动子空间 $\pi^{G(\mathcal O_x)}$ 自然是 Hecke 模；若 $\pi$ 不可约，则该模不可约或为 $0$。

**别名：** `Proposition 1.5`、`spherical vector`、`Hecke module`

## 定义

命题 1.5：设 $\pi$ 是 $G(K_x)$ 的表示，则 $G(\mathcal O_x)$-不动向量构成的子空间 $\pi^{G(\mathcal O_x)}$ 自然是 $\mathcal H(G(K_x),G(\mathcal O_x))$-模。此外，若 $\pi$ 不可约，则 $\pi^{G(\mathcal O_x)}$ 是不可约 $\mathcal H$-模，或为 $0$。

**记号：** $G=\mathrm{GL}_n$；$\pi^{G(\mathcal O_x)}$：不动向量子空间；$\mathcal H$：§1.4 的局部 Hecke 代数。

## 要点

- 作用定义为 $f\cdot v=\int_{G(K_x)}f(g)\,g(v)\,\mu(dg)$；$f$ 紧支撑，故积分是有限和。
- 证明的关键是平均化：任意 $v'\in\pi$ 可写成 $f'\cdot v$，而 $v'$ 若也不动，则 $f'$ 可对 $G(\mathcal O_x)$ 左侧平均成 $f$，使 $f'\cdot v=f\cdot v$。
- 「不可约或 $0$」不是平凡结论：它说明球向量子空间继承了不可约性，从而球表示与不可约 Hecke 模一一对应。

## 公式

$$
f\cdot v=\int_{G(K_x)}f(g)\cdot g(v)\,\mu(dg)
$$

## 定理与证明

**命题 1.5**　设 $\pi$ 是 $G(K_x)$ 的表示，则 $\pi^{G(\mathcal O_x)}$ 自然是 $\mathcal H(G(K_x),G(\mathcal O_x))$-模；若 $\pi$ 不可约，则该模不可约或为 $0$。

> 跳步说明：原书给出证明要点（平均化），未逐行展开紧支撑函数与积分的可交换性。

*出处：§1.5，原书 p.271*

## 易错点

- 以为 $\pi^{G(\mathcal O_x)}$ 自动非零：对球表示才非零；非球表示该空间为 $0$，命题的「或 $0$」正是为此。

## 批注

**〔背景直觉〕平均化在做什么**　对紧群 $G(\mathcal O_x)$ 积分是有限和（模掉开子群后有限），所以「平均化」是纯代数操作。它把任意紧支撑函数换成双不变函数而不改变它在不动向量上的作用——这就是为什么 Hecke 代数足以控制球向量。

## 相关

[[local-hecke]]、[[satake]]

## 来源

- D. Gaitsgory《几何朗兰兹的非正式导论》，Bernstein–Gelbart 编《朗兰兹纲领导论》第 12 章，Birkhäuser 2004，pp. 269–281，§1.5 命题，原书 pp. 270–271（PDF pp. 272–273）
  - 锚点：`08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/源码/chapters/ch12_sec1.tex:43-71（命题 1.5）`
