# Weil–Deligne 群与 Frobenius 半单化

> `lbook04/concept/ch10-weil-deligne` · 轨 G GL_n 的 Langlands 纲领 · 状态 reviewed · 核验 source-only

**问题：** 为什么局部 $L$ 因子要用 $(\ker N)^{\rho(I)}$ 而不是惯性不变子空间 $V^I$？

**一句话：** 局部 Weil–Deligne 群 $W'_k=W_k\rtimes\mathbb{G}_a$ 的表示等价于 $(\rho,N)$，且 $\rho(w)N\rho(w)^{-1}=\|w\|N$；半单化后局部因子只看 $(\ker N)^{\rho(I)}$ 上的 $\det(1-t\rho(\Phi))$。

**别名：** `W'_k`、`Frobenius 半单化`、`局部 L 因子`、`(rho,N) 表示`

## 定义

局部 Langlands 猜想的 Galois 侧不是 $\mathcal{G}_k$ 而是 Weil–Deligne 群 $W'_k=W_k\rtimes\mathbb{G}_a$（Deligne）。$W'_k$ 的表示与「$(\rho,N)$：$\rho$ 是 $W_k$ 的表示，$N$ 幂幺，且 $\rho(w)N\rho(w)^{-1}=\|w\|N$」等价；不可约时 $N=0$，故 Frobenius 半单表示就是 $W_k$ 的半单表示。一般情形取唯一的幂幺 $u$ 使 $\rho u^{-v}$ 半单，半单化 $\rho'_{\mathrm{ss}}=(\rho u^{-v},N)$；局部因子定义为 $Z(t,V)=\det(1-t\rho(\Phi)|_{V_N^I})^{-1}$，其中 $V_N^I=(\ker N)^{\rho(I)}$，再令 $L(s,\rho')=Z(q^{-s},\rho')$。阿基米德域没有 $W'_k$（没有 $\mathbb{G}_a$ 部分），约定 $W'_k=W_k$；$W_{\mathbb{R}}$ 是 $\mathbb{C}^\times$ 与 $j\mathbb{C}^\times$ 的并，$jcj^{-1}=\bar c$、$j^2=-1$，它不是 $\mathbb{C}^\times\times\mathbb{Z}/2$ 的直积。

**记号：** $W_k$：Weil 群；$I$：惯性群；$\Phi$：几何 Frobenius；$\|\cdot\|$：$\|w\|=q^{-v(w)}$，$v$ 为赋值；$\rho,N$：$W'_k$ 表示的半单部分与幂幺部分；$u$：唯一的幂幺元素使 $\rho u^{-v}$ 半单；$Z(t,V)$：局部 zeta 函数。

## 要点

- 交叉项必须是 $x_1+\|w_1\|x_2$：若写成 $x_1+x_2$，结合律失效（§1 的译注专门验算过）。
- 半单化只改 $\rho$，不改 $N$；不可约表示自动 $N=0$，此时「Frobenius 半单」与「$\rho$ 半单」一致。
- 局部因子只取 $(\ker N)^{\rho(I)}$ 上 $\Phi$ 的作用；$N\ne0$ 时若误用 $V^I$ 会多出因子（Steinberg 例 $\omega\otimes\mathrm{Sp}(2)$）。
- 整体 $L(s,\rho)=\prod_vL(s,\rho_v)$、$\varepsilon(s,\rho)=\prod_v\varepsilon(s,\rho_v,\psi_v)$，三条良好性质与 Artin $L$ 函数一致。

## 公式

$$
(w_1,x_1)(w_2,x_2)=(w_1w_2,\;x_1+\|w_1\|x_2)
$$

$$
\rho(w)N\rho(w)^{-1}=\|w\|N
$$

$$
Z(t,V)=\det\bigl(1-t\rho(\Phi)\big|_{V_N^I}\bigr)^{-1},\qquad V_N^I=(\ker N)^{\rho(I)}
$$

$$
L(s,\rho')=Z(q^{-s},\rho')
$$

## 定理与证明

**局部因子的定义**　$L(s,\rho')=Z(q^{-s},\rho')$，$Z(t,V)=\det(1-t\rho(\Phi)|_{V_N^I})^{-1}$；$N=0$ 时 $\varepsilon$ 即 Artin–Weil 因子。

*出处：译文 §1*

## 易错点

- 把 $V_N^I$ 写成 $V^I$：$N\ne0$ 时 $(\ker N)^{\rho(I)}$ 严格小于 $V^{\rho(I)}$，局部因子会多算。
- 把 $W_{\mathbb{R}}$ 当成 $\mathbb{C}^\times\times\mathrm{Gal}(\mathbb{C}/\mathbb{R})$ 的直积：正合列 $1\to\mathbb{C}^\times\to W_{\mathbb{R}}\to\mathrm{Gal}\to1$ 不分裂，$j$ 的作用是共轭。

## 批注

**〔易错预警〕两个 $\Phi$**　本章的 $\Phi$ 是几何 Frobenius；第 11 章的 $\Phi(G)$ 是容许同态集。原书在 p. 254 专门提醒不要把两者混读，中译注也在第 11 章 §2 再次点明。

## 相关

[[ch10-local-langlands]]、[[ch10-global-function-field]]、[[ch9-functional-equation]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§1，原书 pp. 230–233（PDF pp. 233–236）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch10.tex:55-204`
